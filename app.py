import os
import sys
import json
import random
import re
import io
import socket
import webbrowser
import threading
import time
import urllib.request
from datetime import datetime, date
from flask import Flask, render_template, request, jsonify, send_file
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVED_DIR = os.path.join(BASE_DIR, "saved_papers")
CATALOG_PATH = os.path.join(BASE_DIR, "catalog.json")
HISTORY_PATH = os.path.join(BASE_DIR, "question_history.json")

os.makedirs(SAVED_DIR, exist_ok=True)

def resolve_root_downloads():
    candidates = [
        os.path.abspath(os.path.join(BASE_DIR, "..")),
        BASE_DIR,
        os.path.join(os.path.expanduser("~"), "Downloads"),
        r"C:\Users\user\Downloads"
    ]
    for c in candidates:
        if os.path.exists(os.path.join(c, "Marks_Chemistry_PYQs")):
            return c
    return os.path.join(os.path.expanduser("~"), "Downloads")

ROOT_DOWNLOADS = resolve_root_downloads()

EXAMSIDE_CATALOG_PATH = os.path.join(BASE_DIR, "examside_catalog.json")

def resolve_examside_dir():
    candidates = [
        os.path.join(ROOT_DOWNLOADS, "examside pyq"),
        os.path.join(BASE_DIR, "examside pyq"),
        os.path.join(BASE_DIR, "..", "examside pyq"),
        r"C:\Users\91905\Downloads\examside pyq",
        os.path.join(os.path.expanduser("~"), "Downloads", "examside pyq")
    ]
    for c in candidates:
        if os.path.exists(c) and os.path.isdir(c):
            return os.path.abspath(c)
    return os.path.join(ROOT_DOWNLOADS, "examside pyq")

EXAMSIDE_DIR = resolve_examside_dir()
EXAMSIDE_CATALOG = None

def load_examside_catalog():
    global EXAMSIDE_CATALOG
    if EXAMSIDE_CATALOG:
        return EXAMSIDE_CATALOG
    if os.path.exists(EXAMSIDE_CATALOG_PATH):
        try:
            with open(EXAMSIDE_CATALOG_PATH, "r", encoding="utf-8") as f:
                EXAMSIDE_CATALOG = json.load(f)
                return EXAMSIDE_CATALOG
        except Exception as e:
            print(f"[ExamSIDE] Error loading catalog cache: {e}")
    return {"units": [], "total_questions": 0, "total_chapters": 0}

SUBJECT_DIRS = {
    "Chemistry": os.path.join(ROOT_DOWNLOADS, "Marks_Chemistry_PYQs"),
    "Physics": os.path.join(ROOT_DOWNLOADS, "Marks_Physics_PYQs"),
    "Mathematics": os.path.join(ROOT_DOWNLOADS, "Marks_Mathematics_PYQs")
}

CATALOG = None

def normalize_mathml(html_str):
    if not html_str or '<mfenced' not in html_str:
        return html_str

    # Process innermost <mfenced> tags iteratively to avoid nesting conflicts
    pattern = re.compile(r'<mfenced([^>]*)>((?:(?!<mfenced)[\s\S])*?)</mfenced>')

    iterations = 0
    while '<mfenced' in html_str and iterations < 15:
        iterations += 1
        prev_str = html_str
        
        def replacer(match):
            attrs = match.group(1)
            content = match.group(2)
            
            m_open = re.search(r'open=["\'](.*?)["\']', attrs)
            open_delim = m_open.group(1) if m_open else '('
            
            m_close = re.search(r'close=["\'](.*?)["\']', attrs)
            close_delim = m_close.group(1) if m_close else ')'
            
            res = ['<mrow>']
            if open_delim:
                res.append(f'<mo>{open_delim}</mo>')
            
            res.append(content)
            
            if close_delim:
                res.append(f'<mo>{close_delim}</mo>')
            res.append('</mrow>')
            return ''.join(res)
            
        html_str = pattern.sub(replacer, html_str)
        if html_str == prev_str:
            break
            
    return html_str

def sanitize_math_content(text):
    if not text:
        return ""
    # Normalize MathML mfenced into standard MathML Core
    text = normalize_mathml(text)
    # Fix raw < followed by letters in latex math delimiters $ ... $ or \( ... \)
    def fix_latex(m):
        delim_start, content, delim_end = m.group(1), m.group(2), m.group(3)
        fixed_content = re.sub(r'<([a-zA-Z])', r'&lt; \1', content)
        return f"{delim_start}{fixed_content}{delim_end}"
    text = re.sub(r'(\$|\\\()([^\$]+?)(\$|\\\))', fix_latex, text)
    # Remove empty tracking/placeholder tags
    text = re.sub(r'<gwmw[^>]*></gwmw>', '', text)
    return text

import html as py_html

def clean_html(text):
    if not text:
        return ""
    
    # 1. Normalize <mfenced> tags so brackets are preserved as explicit tokens
    text = normalize_mathml(text)
    
    # 2. Fractions: <mfrac>num den</mfrac> -> (num)/(den)
    frac_pat = re.compile(r'<mfrac[^>]*>((?:(?!<mfrac)[\s\S])*?)</mfrac>')
    for _ in range(8):
        if '<mfrac' not in text:
            break
        def frac_repl(m):
            inner = m.group(1)
            m_parts = re.findall(r'<([a-zA-Z0-9]+)[^>]*>([\s\S]*?)</\1>', inner)
            if len(m_parts) >= 2:
                num = clean_html(m_parts[0][1])
                den = clean_html(m_parts[1][1])
                return f"({num})/({den})"
            return inner
        text = frac_pat.sub(frac_repl, text)

    # 3. Square roots: <msqrt>...</msqrt> -> √( ... )
    sqrt_pat = re.compile(r'<msqrt[^>]*>([\s\S]*?)</msqrt>')
    text = sqrt_pat.sub(lambda m: f"√({clean_html(m.group(1))})", text)
    
    # 4. Roots: <mroot>(base)(index)</mroot> -> (index)√(base)
    mroot_pat = re.compile(r'<mroot[^>]*>([\s\S]*?)</mroot>')
    def mroot_repl(m):
        m_parts = re.findall(r'<([a-zA-Z0-9]+)[^>]*>([\s\S]*?)</\1>', m.group(1))
        if len(m_parts) >= 2:
            base = clean_html(m_parts[0][1])
            idx = clean_html(m_parts[1][1])
            return f"({idx})√({base})"
        return m.group(1)
    text = mroot_pat.sub(mroot_repl, text)

    # 5. Superscripts: <msup>(base)(exp)</msup> -> base^(exp)
    msup_pat = re.compile(r'<msup[^>]*>((?:(?!<msup)[\s\S])*?)</msup>')
    for _ in range(5):
        if '<msup' not in text:
            break
        def msup_repl(m):
            m_parts = re.findall(r'<([a-zA-Z0-9]+)[^>]*>([\s\S]*?)</\1>', m.group(1))
            if len(m_parts) >= 2:
                base = clean_html(m_parts[0][1])
                exp = clean_html(m_parts[1][1])
                return f"{base}^{exp}"
            return m.group(1)
        text = msup_pat.sub(msup_repl, text)

    # 6. Subscripts: <msub>(base)(sub)</msub> -> base_(sub)
    msub_pat = re.compile(r'<msub[^>]*>((?:(?!<msub)[\s\S])*?)</msub>')
    for _ in range(5):
        if '<msub' not in text:
            break
        def msub_repl(m):
            m_parts = re.findall(r'<([a-zA-Z0-9]+)[^>]*>([\s\S]*?)</\1>', m.group(1))
            if len(m_parts) >= 2:
                base = clean_html(m_parts[0][1])
                sub = clean_html(m_parts[1][1])
                return f"{base}_{sub}"
            return m.group(1)
        text = msub_pat.sub(msub_repl, text)

    # 7. Tables / Matrices: <mtable>
    text = re.sub(r'</mtr>', '\n', text)
    text = re.sub(r'</mtd>', '  ', text)

    # 8. Standard tags stripping & HTML entity unescaping
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = py_html.unescape(text)
    
    # Simplify (a)/(b) when a and b are single alphanumeric tokens
    text = re.sub(r'\(([a-zA-Z0-9]+)\)/\(([a-zA-Z0-9]+)\)', r'\1/\2', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def format_pyq_tag(tag, mode="full"):
    if not tag:
        return ""
    if mode == "full":
        return tag
    m_year = re.search(r'\b(19\d\d|20\d\d)\b', tag)
    if mode == "year_only":
        return m_year.group(1) if m_year else tag
    if mode == "exam_year":
        m_ey = re.match(r'^(.*?)\s*(\b(?:19|20)\d{2}\b)', tag)
        if m_ey:
            return f"{m_ey.group(1).strip()} {m_ey.group(2)}"
        return tag
    return tag

# ==================== QUESTION USAGE HISTORY ====================

def load_history():
    if os.path.exists(HISTORY_PATH):
        try:
            with open(HISTORY_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[History] Error reading history: {e}")
    return {"papers": [], "usage": {}}

def save_history(hist_data):
    try:
        with open(HISTORY_PATH, "w", encoding="utf-8") as f:
            json.dump(hist_data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[History] Error saving history: {e}")

def record_paper_usage(batch, test_date_str, paper_title, paper_id, question_ids):
    if not question_ids:
        return
    batch = (batch or "General Batch").strip()
    test_date_str = test_date_str or date.today().isoformat()
    
    hist = load_history()
    usage = hist.setdefault("usage", {})
    papers = hist.setdefault("papers", [])

    # Check if paper already recorded
    existing_paper = next((p for p in papers if p.get("paper_id") == paper_id), None)
    if existing_paper:
        existing_paper["batch"] = batch
        existing_paper["test_date"] = test_date_str
        existing_paper["paper_title"] = paper_title
        existing_paper["question_count"] = len(question_ids)
    else:
        papers.append({
            "paper_id": paper_id,
            "paper_title": paper_title,
            "batch": batch,
            "test_date": test_date_str,
            "question_count": len(question_ids),
            "recorded_at": datetime.now().isoformat()
        })

    for qid in question_ids:
        q_records = usage.setdefault(qid, [])
        # Avoid duplicate record for same paper_id
        if not any(r.get("paper_id") == paper_id for r in q_records):
            q_records.append({
                "paper_id": paper_id,
                "paper_title": paper_title,
                "batch": batch,
                "test_date": test_date_str
            })

    save_history(hist)

def check_question_usage(question_id, target_batch, target_date_str):
    hist = load_history()
    usage = hist.get("usage", {}).get(question_id, [])
    if not usage:
        return {"is_recent": False, "is_same_batch": False, "records": []}

    try:
        t_date = datetime.strptime(target_date_str, "%Y-%m-%d").date()
    except Exception:
        t_date = date.today()

    target_batch_norm = (target_batch or "").strip().lower()
    recent_records = []
    is_same_batch = False

    for rec in usage:
        r_date_str = rec.get("test_date")
        r_batch = rec.get("batch", "General Batch")
        try:
            r_date = datetime.strptime(r_date_str, "%Y-%m-%d").date()
            diff_days = (t_date - r_date).days
            # Within 7 days (1 week window)
            if 0 <= diff_days <= 7:
                same = (r_batch.strip().lower() == target_batch_norm) if target_batch_norm else True
                if same:
                    is_same_batch = True
                recent_records.append({
                    "batch": r_batch,
                    "test_date": r_date_str,
                    "paper_title": rec.get("paper_title", "Conducted Test"),
                    "days_ago": diff_days,
                    "is_same_batch": same
                })
        except Exception:
            pass

    return {
        "is_recent": len(recent_records) > 0,
        "is_same_batch": is_same_batch,
        "records": recent_records
    }

# ==================== CATALOG MANAGEMENT ====================

def build_or_load_catalog():
    global CATALOG
    if os.path.exists(CATALOG_PATH):
        try:
            with open(CATALOG_PATH, "r", encoding="utf-8") as f:
                CATALOG = json.load(f)
                print(f"[Catalog] Loaded {len(CATALOG['chapters'])} chapters from cache.")
                return CATALOG
        except Exception as e:
            print(f"[Catalog] Error loading cache: {e}, rebuilding...")

    print("[Catalog] Building fresh catalog index from 51,011 questions...")
    chapters_list = []
    hierarchy = {"Chemistry": {}, "Physics": {}, "Mathematics": {}}

    for sub_name, sdir in SUBJECT_DIRS.items():
        if not os.path.exists(sdir):
            continue
        exams = [d for d in os.listdir(sdir) if os.path.isdir(os.path.join(sdir, d)) and d != "assets"]
        for ex in sorted(exams):
            hierarchy[sub_name][ex] = []
            ed = os.path.join(sdir, ex)
            chs = [c for c in os.listdir(ed) if os.path.isdir(os.path.join(ed, c))]
            for c in sorted(chs):
                cd = os.path.join(ed, c)
                jf = os.path.join(cd, "chapter_raw_data.json")
                if not os.path.exists(jf):
                    continue
                try:
                    with open(jf, "r", encoding="utf-8") as f:
                        d = json.load(f)
                    ch_title = d.get("chapter", c)
                    topics = []
                    for t in d.get("topics", []):
                        topics.append({
                            "index": t.get("index", 0),
                            "topicId": t.get("topicId", ""),
                            "title": t.get("title", ""),
                            "totalQuestions": t.get("totalQuestions", len(t.get("questions", [])))
                        })
                    total_q = d.get("totalQuestions", sum(t["totalQuestions"] for t in topics))
                    item = {
                        "subject": sub_name,
                        "exam": ex,
                        "chapter": ch_title,
                        "folder": c,
                        "json_path": jf,
                        "totalQuestions": total_q,
                        "topics": topics
                    }
                    chapters_list.append(item)
                    hierarchy[sub_name][ex].append({
                        "chapter": ch_title,
                        "folder": c,
                        "totalQuestions": total_q,
                        "topics": topics
                    })
                except Exception as e:
                    pass

    CATALOG = {
        "chapters": chapters_list,
        "hierarchy": hierarchy
    }

    with open(CATALOG_PATH, "w", encoding="utf-8") as f:
        json.dump(CATALOG, f, ensure_ascii=False)
    print(f"[Catalog] Index built with {len(chapters_list)} chapters.")
    return CATALOG

build_or_load_catalog()

# ==================== FLASK ROUTES ====================

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/catalog")
def get_catalog():
    return jsonify(CATALOG)

@app.route("/api/mobile_info")
def get_mobile_info():
    url_file = os.path.join(BASE_DIR, "mobile_url.txt")
    cloud_url = None
    if os.path.exists(url_file):
        try:
            with open(url_file, "r", encoding="utf-8") as f:
                cloud_url = f.read().strip()
        except Exception:
            pass
    return jsonify({
        "cloud_url": cloud_url or "https://order-have-two-smell.trycloudflare.com",
        "local_wifi_url": "http://192.168.1.35:5000"
    })

@app.route("/api/examside/catalog")
def get_examside_catalog_route():
    return jsonify(load_examside_catalog())

@app.route("/api/examside/view/<unit>/<filename>")
def view_examside_pdf(unit, filename):
    fpath = os.path.join(EXAMSIDE_DIR, unit, filename)
    if not os.path.exists(fpath):
        return jsonify({"error": f"PDF file not found: {filename}"}), 404
    return send_file(
        fpath,
        mimetype="application/pdf",
        as_attachment=False,
        download_name=filename
    )

@app.route("/api/examside/download/<unit>/<filename>")
def download_examside_pdf(unit, filename):
    fpath = os.path.join(EXAMSIDE_DIR, unit, filename)
    if not os.path.exists(fpath):
        return jsonify({"error": f"PDF file not found: {filename}"}), 404
    return send_file(
        fpath,
        as_attachment=True,
        download_name=filename
    )

@app.route("/api/examside/answer_key/<unit>/<filename>")
def get_examside_answer_key(unit, filename):
    cat = load_examside_catalog()
    for u in cat.get("units", []):
        if u.get("unit_folder") == unit:
            for ch in u.get("chapters", []):
                if ch.get("filename") == filename:
                    return jsonify({
                        "chapter_name": ch.get("chapter_name"),
                        "unit_title": ch.get("unit_title"),
                        "questions_count": ch.get("questions_count"),
                        "total_keys": ch.get("answer_keys_count"),
                        "answer_keys": ch.get("answer_keys", [])
                    })
    return jsonify({"error": "Chapter not found in catalog"}), 404

def load_chapter_questions(ch_item_or_path):
    if isinstance(ch_item_or_path, str):
        path = ch_item_or_path
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                pass
    elif isinstance(ch_item_or_path, dict):
        sub = ch_item_or_path.get("subject")
        exam = ch_item_or_path.get("exam")
        folder = ch_item_or_path.get("folder")
        if sub in SUBJECT_DIRS:
            cand = os.path.join(SUBJECT_DIRS[sub], exam, folder, "chapter_raw_data.json")
            if os.path.exists(cand):
                try:
                    with open(cand, "r", encoding="utf-8") as f:
                        return json.load(f)
                except Exception as e:
                    pass
        p = ch_item_or_path.get("json_path", "")
        if p and os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
    return None

@app.route("/api/questions", methods=["POST"])
def query_questions():
    data = request.json or {}
    subject = data.get("subject")
    exam = data.get("exam")
    chapter_folder = data.get("chapter_folder")
    topic_ids = data.get("topic_ids", [])
    q_types = data.get("q_types", [])
    levels = [int(lvl) for lvl in data.get("levels", []) if str(lvl).isdigit()]
    limit = data.get("limit")
    randomize = data.get("randomize", False)
    search_query = data.get("search_query", "").strip().lower()
    target_batch = data.get("batch", "")
    target_date = data.get("test_date", date.today().isoformat())
    years = [str(y).strip() for y in data.get("years", []) if str(y).strip()]
    year_start = data.get("year_start")
    year_end = data.get("year_end")

    matched_chapters = []
    for ch in CATALOG["chapters"]:
        if subject and ch["subject"] != subject:
            continue
        if exam and exam != "all" and ch["exam"] != exam:
            continue
        if chapter_folder and ch["folder"] != chapter_folder:
            continue
        matched_chapters.append(ch)

    results = []
    for ch in matched_chapters:
        ch_data = load_chapter_questions(ch)
        if not ch_data:
            continue
        
        for topic in ch_data.get("topics", []):
            t_id = topic.get("topicId")
            if topic_ids and t_id not in topic_ids:
                continue
            
            for q in topic.get("questions", []):
                q_type = q.get("type", "singleCorrect")
                if q_types and q_type not in q_types:
                    continue
                
                lvl = q.get("level", 1)
                if levels and lvl not in levels:
                    continue

                q_text = q.get("question", {}).get("text", "")
                if search_query and search_query not in q_text.lower():
                    continue

                papers = [p.get("title", "") for p in q.get("previousYearPapers", []) if p.get("title")]
                paper_tag = ", ".join(papers) if papers else f"{ch['exam']}"
                
                year_match = re.search(r'\b(19\d\d|20\d\d)\b', paper_tag)
                pyq_year = year_match.group(1) if year_match else ""

                # Year range filter check
                if pyq_year and pyq_year.isdigit():
                    q_yr = int(pyq_year)
                    if year_start and str(year_start).isdigit() and q_yr < int(year_start):
                        continue
                    if year_end and str(year_end).isdigit() and q_yr > int(year_end):
                        continue
                elif year_start or year_end:
                    continue

                # Multiselect years list check
                if years:
                    matched_yr = False
                    for y in years:
                        if y == pyq_year or y in paper_tag:
                            matched_yr = True
                            break
                        if (y == "2015" or y == "older") and pyq_year and pyq_year.isdigit() and int(pyq_year) <= 2015:
                            matched_yr = True
                            break
                    if not matched_yr:
                        continue
                
                options = []
                for idx, opt in enumerate(q.get("options", [])):
                    if isinstance(opt, dict):
                        options.append({
                            "label": chr(65 + idx),
                            "text": sanitize_math_content(opt.get("text", "")),
                            "isCorrect": opt.get("isCorrect", False)
                        })
                    else:
                        options.append({
                            "label": chr(65 + idx),
                            "text": sanitize_math_content(str(opt)),
                            "isCorrect": False
                        })

                q_id = q.get("_id")
                usage_info = check_question_usage(q_id, target_batch, target_date)

                results.append({
                    "id": q_id,
                    "subject": ch["subject"],
                    "exam": ch["exam"],
                    "chapter": ch["chapter"],
                    "chapterFolder": ch["folder"],
                    "topicTitle": topic.get("title", ""),
                    "topicId": t_id,
                    "type": q_type,
                    "level": lvl,
                    "examTag": paper_tag,
                    "pyqYear": pyq_year,
                    "questionText": sanitize_math_content(q_text),
                    "options": options,
                    "correctValue": q.get("correctValue"),
                    "solutionText": sanitize_math_content(q.get("solution", {}).get("text", "")),
                    "recentUsage": usage_info
                })

    if randomize:
        random.shuffle(results)

    total_matched = len(results)
    if limit and isinstance(limit, int) and limit > 0:
        results = results[:limit]

    return jsonify({
        "total_matched": total_matched,
        "questions": results
    })

@app.route("/api/auto_pick", methods=["POST"])
def auto_pick():
    data = request.json or {}
    subject = data.get("subject")
    exam = data.get("exam", "all")
    chapter_folder = data.get("chapter_folder")
    topic_ids = data.get("topic_ids", [])
    mcq_count = int(data.get("mcq_count", 20))
    numerical_count = int(data.get("numerical_count", 5))
    levels = [int(lvl) for lvl in data.get("levels", []) if str(lvl).isdigit()]
    target_batch = data.get("batch", "")
    target_date = data.get("test_date", date.today().isoformat())
    exclude_recent = data.get("exclude_recent", True)
    pick_all = data.get("pick_all", False)
    years = [str(y).strip() for y in data.get("years", []) if str(y).strip()]
    year_start = data.get("year_start")
    year_end = data.get("year_end")

    mcq_pool = []
    num_pool = []
    excluded_recent_count = 0

    matched_chapters = []
    for ch in CATALOG["chapters"]:
        if subject and ch["subject"] != subject:
            continue
        if exam and exam != "all" and ch["exam"] != exam:
            continue
        if chapter_folder and ch["folder"] != chapter_folder:
            continue
        matched_chapters.append(ch)

    for ch in matched_chapters:
        ch_data = load_chapter_questions(ch)
        if not ch_data:
            continue
        
        for topic in ch_data.get("topics", []):
            t_id = topic.get("topicId")
            if topic_ids and t_id not in topic_ids:
                continue
            
            for q in topic.get("questions", []):
                q_type = q.get("type", "singleCorrect")
                lvl = q.get("level", 1)
                if levels and lvl not in levels:
                    continue

                q_id = q.get("_id")
                usage_info = check_question_usage(q_id, target_batch, target_date)

                # If exclude_recent is on, skip questions conducted in the same batch (or any batch if specified) within 7 days
                if exclude_recent and (usage_info["is_same_batch"] or usage_info["is_recent"]):
                    excluded_recent_count += 1
                    continue

                papers = [p.get("title", "") for p in q.get("previousYearPapers", []) if p.get("title")]
                paper_tag = ", ".join(papers) if papers else f"{ch['exam']}"
                
                year_match = re.search(r'\b(19\d\d|20\d\d)\b', paper_tag)
                pyq_year = year_match.group(1) if year_match else ""

                # Year range filter check
                if pyq_year and pyq_year.isdigit():
                    q_yr = int(pyq_year)
                    if year_start and str(year_start).isdigit() and q_yr < int(year_start):
                        continue
                    if year_end and str(year_end).isdigit() and q_yr > int(year_end):
                        continue
                elif year_start or year_end:
                    continue

                # Multiselect years list check
                if years:
                    matched_yr = False
                    for y in years:
                        if y == pyq_year or y in paper_tag:
                            matched_yr = True
                            break
                        if (y == "2015" or y == "older") and pyq_year and pyq_year.isdigit() and int(pyq_year) <= 2015:
                            matched_yr = True
                            break
                    if not matched_yr:
                        continue

                options = []
                for idx, opt in enumerate(q.get("options", [])):
                    if isinstance(opt, dict):
                        options.append({
                            "label": chr(65 + idx),
                            "text": sanitize_math_content(opt.get("text", "")),
                            "isCorrect": opt.get("isCorrect", False)
                        })
                    else:
                        options.append({
                            "label": chr(65 + idx),
                            "text": sanitize_math_content(str(opt)),
                            "isCorrect": False
                        })

                item = {
                    "id": q_id,
                    "subject": ch["subject"],
                    "exam": ch["exam"],
                    "chapter": ch["chapter"],
                    "chapterFolder": ch["folder"],
                    "topicTitle": topic.get("title", ""),
                    "topicId": t_id,
                    "type": q_type,
                    "level": lvl,
                    "examTag": paper_tag,
                    "pyqYear": pyq_year,
                    "questionText": sanitize_math_content(q.get("question", {}).get("text", "")),
                    "options": options,
                    "correctValue": q.get("correctValue"),
                    "solutionText": sanitize_math_content(q.get("solution", {}).get("text", "")),
                    "recentUsage": usage_info
                }

                if q_type == "numerical":
                    num_pool.append(item)
                else:
                    mcq_pool.append(item)

    if pick_all:
        picked_mcqs = mcq_pool
        picked_nums = num_pool
    else:
        random.shuffle(mcq_pool)
        random.shuffle(num_pool)
        picked_mcqs = mcq_pool[:mcq_count]
        picked_nums = num_pool[:numerical_count]

    return jsonify({
        "success": True,
        "requested_mcqs": mcq_count,
        "available_mcqs": len(mcq_pool),
        "picked_mcqs": len(picked_mcqs),
        "requested_nums": numerical_count,
        "available_nums": len(num_pool),
        "picked_nums": len(picked_nums),
        "excluded_recent_count": excluded_recent_count,
        "questions": picked_mcqs + picked_nums
    })

@app.route("/api/record_usage", methods=["POST"])
def record_usage():
    data = request.json or {}
    batch = data.get("batch", "General Batch")
    test_date = data.get("test_date", date.today().isoformat())
    paper_title = data.get("paper_title", "Untitled Test")
    paper_id = data.get("paper_id", f"test_{int(datetime.now().timestamp())}")
    question_ids = data.get("question_ids", [])
    record_paper_usage(batch, test_date, paper_title, paper_id, question_ids)
    return jsonify({"success": True, "message": f"Recorded usage of {len(question_ids)} questions for {batch} on {test_date}."})

@app.route("/api/history", methods=["GET"])
def get_history():
    hist = load_history()
    return jsonify(hist)

@app.route("/api/clear_history", methods=["POST"])
def clear_history():
    data = request.json or {}
    paper_id = data.get("paper_id")
    hist = load_history()
    if paper_id:
        hist["papers"] = [p for p in hist.get("papers", []) if p.get("paper_id") != paper_id]
        usage = hist.get("usage", {})
        for qid in list(usage.keys()):
            usage[qid] = [r for r in usage[qid] if r.get("paper_id") != paper_id]
            if not usage[qid]:
                del usage[qid]
        save_history(hist)
        return jsonify({"success": True, "message": "Paper usage record removed."})
    else:
        save_history({"papers": [], "usage": {}})
        return jsonify({"success": True, "message": "Entire question history reset."})

@app.route("/api/save_paper", methods=["POST"])
def save_paper():
    data = request.json or {}
    paper_id = data.get("id") or f"paper_{int(datetime.now().timestamp())}"
    data["id"] = paper_id
    batch = data.get("batch", "General Batch")
    test_date = data.get("test_date", date.today().isoformat())
    title = data.get("title", "Untitled Test")
    
    file_path = os.path.join(SAVED_DIR, f"{paper_id}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    # Automatically register questions in usage history for this batch & date
    q_ids = [q.get("id") for q in data.get("questions", []) if q.get("id")]
    record_paper_usage(batch, test_date, title, paper_id, q_ids)

    return jsonify({"success": True, "id": paper_id, "message": "Test paper saved and registered in batch history."})

@app.route("/api/list_papers")
def list_papers():
    papers = []
    if os.path.exists(SAVED_DIR):
        for fname in os.listdir(SAVED_DIR):
            if fname.endswith(".json"):
                fp = os.path.join(SAVED_DIR, fname)
                try:
                    with open(fp, "r", encoding="utf-8") as f:
                        d = json.load(f)
                    papers.append({
                        "id": d.get("id", fname[:-5]),
                        "title": d.get("title", "Untitled Test"),
                        "institute": d.get("institute", ""),
                        "batch": d.get("batch", ""),
                        "test_date": d.get("test_date", ""),
                        "subject": d.get("subject", ""),
                        "questionCount": len(d.get("questions", [])),
                        "savedAt": d.get("savedAt", "")
                    })
                except:
                    pass
    return jsonify(papers)

@app.route("/api/load_paper/<paper_id>")
def load_paper(paper_id):
    fp = os.path.join(SAVED_DIR, f"{paper_id}.json")
    if not os.path.exists(fp):
        return jsonify({"error": "Paper not found"}), 404
    with open(fp, "r", encoding="utf-8") as f:
        d = json.load(f)
    if "questions" in d and isinstance(d["questions"], list):
        for q in d["questions"]:
            if "questionText" in q:
                q["questionText"] = sanitize_math_content(q["questionText"])
            if "solutionText" in q:
                q["solutionText"] = sanitize_math_content(q["solutionText"])
            for opt in q.get("options", []):
                if isinstance(opt, dict) and "text" in opt:
                    opt["text"] = sanitize_math_content(opt["text"])
    return jsonify(d)

@app.route("/api/export_docx", methods=["POST"])
def export_docx():
    data = request.json or {}
    mode = data.get("mode", "paper") # 'paper' or 'solutions'
    title = data.get("title", "JEE Mock Test")
    institute = data.get("institute", "Narayana")
    batch = data.get("batch", "General Batch")
    test_date = data.get("test_date", date.today().isoformat())
    time_limit = data.get("time_limit", "60 Minutes")
    max_marks = data.get("max_marks", "100")
    instructions = data.get("instructions", "1. All questions are compulsory.\n2. For MCQs: +4 for correct, -1 for wrong.\n3. For Numerical: +4 for correct, 0 for wrong.")
    questions = data.get("questions", [])
    show_pyq_year = data.get("show_pyq_year", False)
    pyq_format = data.get("pyq_format", "full")
    show_date = data.get("show_date", False)
    show_time = data.get("show_time", False)
    show_batch = data.get("show_batch", False)
    show_marks = data.get("show_marks", False)
    show_instructions = data.get("show_instructions", False)
    include_answer_key = data.get("include_answer_key", False)

    # Auto-register question usage when exporting
    q_ids = [q.get("id") for q in questions if q.get("id")]
    record_paper_usage(batch, test_date, title, f"export_{int(datetime.now().timestamp())}", q_ids)

    doc = docx.Document()
    
    # Page Margins
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.6)
        section.left_margin = Inches(0.7)
        section.right_margin = Inches(0.7)

    # Institute Header
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_inst = p_inst.add_run(institute.upper())
    r_inst.bold = True
    r_inst.font.size = Pt(17)
    r_inst.font.color.rgb = RGBColor(14, 43, 92)

    # Title Header
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_title = f"{title} - SOLUTIONS & ANSWER KEY" if mode == 'solutions' else title
    r_title = p_title.add_run(sub_title)
    r_title.bold = True
    r_title.font.size = Pt(13)

    # Info Bar Table with Batch & Date
    table = doc.add_table(rows=2, cols=3)
    table.style = 'Table Grid'
    row0 = table.rows[0].cells
    if show_batch and batch:
        row0[0].paragraphs[0].add_run(f"Batch: {batch}").bold = True
    else:
        row0[0].paragraphs[0].add_run("")
    if show_date and test_date:
        row0[1].paragraphs[0].add_run(f"Date: {test_date}").bold = True
    else:
        row0[1].paragraphs[0].add_run("")
    if show_time and time_limit:
        row0[2].paragraphs[0].add_run(f"Time: {time_limit}").bold = True
    else:
        row0[2].paragraphs[0].add_run("")

    row1 = table.rows[1].cells
    if show_marks:
        row1[0].paragraphs[0].add_run(f"Max Marks: {max_marks}").bold = True
    else:
        row1[0].paragraphs[0].add_run("")
    row1[1].paragraphs[0].add_run(f"Total Questions: {len(questions)}").bold = True
    row1[2].paragraphs[0].add_run("Candidate Roll No: _________")

    doc.add_paragraph()

    # Instructions if question paper
    if mode == "paper" and show_instructions and instructions:
        p_ins = doc.add_paragraph()
        r_ins_title = p_ins.add_run("General Instructions:\n")
        r_ins_title.bold = True
        p_ins.add_run(instructions)
        doc.add_paragraph().paragraph_format.space_after = Pt(8)

    mcqs = [q for q in questions if q.get("type") != "numerical"]
    nums = [q for q in questions if q.get("type") == "numerical"]
    ordered_questions = mcqs + nums

    # In solutions mode, add Answer Key Summary Grid table at top
    if mode == "solutions" and ordered_questions:
        p_ans_head = doc.add_paragraph()
        r_ah = p_ans_head.add_run("ANSWER KEY SUMMARY")
        r_ah.bold = True
        r_ah.font.size = Pt(12)
        r_ah.font.color.rgb = RGBColor(14, 43, 92)
        p_ans_head.paragraph_format.space_before = Pt(4)
        p_ans_head.paragraph_format.space_after = Pt(4)

        chunk_size = 10
        for i in range(0, len(ordered_questions), chunk_size):
            chunk = ordered_questions[i:i + chunk_size]
            t_key = doc.add_table(rows=2, cols=len(chunk))
            t_key.style = 'Table Grid'
            hdr_cells = t_key.rows[0].cells
            ans_cells = t_key.rows[1].cells
            for col_idx, q_item in enumerate(chunk):
                q_num = i + col_idx + 1
                p_hdr = hdr_cells[col_idx].paragraphs[0]
                p_hdr.text = f"Q{q_num}"
                p_hdr.runs[0].bold = True
                p_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
                
                p_val = ans_cells[col_idx].paragraphs[0]
                if q_item.get("type") == "numerical":
                    val = q_item.get("correctValue")
                    ans_str = str(val) if (val is not None and str(val).strip() != "") else "-"
                else:
                    c_opts = [o.get("label") for o in q_item.get("options", []) if o.get("isCorrect")]
                    if c_opts:
                        ans_str = ",".join(c_opts)
                    elif q_item.get("correctValue") is not None and str(q_item.get("correctValue")).strip() != "":
                        ans_str = str(q_item.get("correctValue"))
                    else:
                        ans_str = "-"
                p_val.text = ans_str
                p_val.runs[0].bold = True
                p_val.alignment = WD_ALIGN_PARAGRAPH.CENTER
            doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # Render Section A: Multiple Choice
    if mcqs:
        p_sec = doc.add_paragraph()
        r_sec = p_sec.add_run(f"SECTION A: MULTIPLE CHOICE QUESTIONS ({len(mcqs)} Questions &bull; Single Correct)")
        r_sec.bold = True
        r_sec.font.size = Pt(11)
        r_sec.font.color.rgb = RGBColor(14, 43, 92)
        p_sec.paragraph_format.space_before = Pt(10)
        p_sec.paragraph_format.space_after = Pt(6)

        for idx, q in enumerate(mcqs, 1):
            p_q = doc.add_paragraph()
            p_q.paragraph_format.space_before = Pt(6)
            p_q.paragraph_format.space_after = Pt(3)
            r_num = p_q.add_run(f"Q{idx}. ")
            r_num.bold = True
            
            # In paper mode, show exam_tag only if show_pyq_year toggle is enabled
            if mode == "solutions" or show_pyq_year:
                raw_tag = q.get("examTag", "")
                exam_tag = format_pyq_tag(raw_tag, pyq_format) if (show_pyq_year and mode != "solutions") else raw_tag
                if exam_tag:
                    r_tag = p_q.add_run(f"[{exam_tag}] ")
                    r_tag.italic = True
                    r_tag.font.size = Pt(9)
                    r_tag.font.color.rgb = RGBColor(100, 100, 100)

            q_text = clean_html(q.get("questionText", ""))
            p_q.add_run(q_text)

            opts = q.get("options", [])
            for opt in opts:
                p_opt = doc.add_paragraph()
                p_opt.paragraph_format.left_indent = Inches(0.3)
                p_opt.paragraph_format.space_before = Pt(1)
                p_opt.paragraph_format.space_after = Pt(1)
                p_opt.add_run(f"({opt.get('label')}) ").bold = True
                p_opt.add_run(clean_html(opt.get("text", "")))

            if mode == "solutions":
                c_labels = [opt.get("label") for opt in opts if opt.get("isCorrect")]
                p_ans = doc.add_paragraph()
                p_ans.paragraph_format.left_indent = Inches(0.3)
                p_ans.paragraph_format.space_before = Pt(3)
                if len(c_labels) > 1:
                    r_ans = p_ans.add_run(f"Correct Answer: Options ({', '.join(c_labels)}) [Multiple Correct]")
                elif len(c_labels) == 1:
                    r_ans = p_ans.add_run(f"Correct Answer: Option ({c_labels[0]})")
                elif q.get("correctValue") is not None and str(q.get("correctValue")).strip() != "":
                    r_ans = p_ans.add_run(f"Correct Value: {q.get('correctValue')}")
                else:
                    r_ans = p_ans.add_run("Answer: Key Not Specified")
                r_ans.bold = True
                r_ans.font.color.rgb = RGBColor(0, 128, 0)

                sol_text = clean_html(q.get("solutionText", ""))
                if sol_text:
                    p_sol = doc.add_paragraph()
                    p_sol.paragraph_format.left_indent = Inches(0.3)
                    p_sol.add_run("Solution: ").bold = True
                    p_sol.add_run(sol_text)
                doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Render Section B: Numerical
    if nums:
        p_sec = doc.add_paragraph()
        r_sec = p_sec.add_run(f"SECTION B: NUMERICAL / INTEGER VALUE QUESTIONS ({len(nums)} Questions)")
        r_sec.bold = True
        r_sec.font.size = Pt(11)
        r_sec.font.color.rgb = RGBColor(14, 43, 92)
        p_sec.paragraph_format.space_before = Pt(14)
        p_sec.paragraph_format.space_after = Pt(6)

        start_num = len(mcqs) + 1
        for idx, q in enumerate(nums, start_num):
            p_q = doc.add_paragraph()
            p_q.paragraph_format.space_before = Pt(6)
            p_q.paragraph_format.space_after = Pt(3)
            r_num = p_q.add_run(f"Q{idx}. ")
            r_num.bold = True
            
            # In paper mode, show exam_tag only if show_pyq_year toggle is enabled
            if mode == "solutions" or show_pyq_year:
                raw_tag = q.get("examTag", "")
                exam_tag = format_pyq_tag(raw_tag, pyq_format) if (show_pyq_year and mode != "solutions") else raw_tag
                if exam_tag:
                    r_tag = p_q.add_run(f"[{exam_tag}] ")
                    r_tag.italic = True
                    r_tag.font.size = Pt(9)
                    r_tag.font.color.rgb = RGBColor(100, 100, 100)

            q_text = clean_html(q.get("questionText", ""))
            p_q.add_run(q_text)

            if mode == "paper":
                p_box = doc.add_paragraph()
                p_box.paragraph_format.left_indent = Inches(0.3)
                p_box.add_run("Answer: [                         ]")
            else:
                p_ans = doc.add_paragraph()
                p_ans.paragraph_format.left_indent = Inches(0.3)
                c_val = q.get('correctValue')
                val_str = str(c_val) if (c_val is not None and str(c_val).strip() != "") else "Not Specified"
                r_ans = p_ans.add_run(f"Correct Numerical Value: {val_str}")
                r_ans.bold = True
                r_ans.font.color.rgb = RGBColor(0, 128, 0)

                sol_text = clean_html(q.get("solutionText", ""))
                if sol_text:
                    p_sol = doc.add_paragraph()
                    p_sol.paragraph_format.left_indent = Inches(0.3)
                    p_sol.add_run("Solution: ").bold = True
                    p_sol.add_run(sol_text)
                doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # If question paper mode and include_answer_key is enabled, append Answer Key table at the end
    if mode == "paper" and include_answer_key and ordered_questions:
        doc.add_paragraph().paragraph_format.space_before = Pt(16)
        p_ans_head = doc.add_paragraph()
        r_ah = p_ans_head.add_run("OFFICIAL ANSWER KEY SUMMARY")
        r_ah.bold = True
        r_ah.font.size = Pt(12)
        r_ah.font.color.rgb = RGBColor(14, 43, 92)
        p_ans_head.paragraph_format.space_before = Pt(10)
        p_ans_head.paragraph_format.space_after = Pt(4)

        chunk_size = 10
        for i in range(0, len(ordered_questions), chunk_size):
            chunk = ordered_questions[i:i + chunk_size]
            t_key = doc.add_table(rows=2, cols=len(chunk))
            t_key.style = 'Table Grid'
            hdr_cells = t_key.rows[0].cells
            ans_cells = t_key.rows[1].cells
            for col_idx, q_item in enumerate(chunk):
                q_num = i + col_idx + 1
                p_hdr = hdr_cells[col_idx].paragraphs[0]
                p_hdr.text = f"Q{q_num}"
                p_hdr.runs[0].bold = True
                p_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
                
                p_val = ans_cells[col_idx].paragraphs[0]
                if q_item.get("type") == "numerical":
                    val = q_item.get("correctValue")
                    ans_str = str(val) if (val is not None and str(val).strip() != "") else "-"
                else:
                    c_opts = [o.get("label") for o in q_item.get("options", []) if o.get("isCorrect")]
                    if c_opts:
                        ans_str = ",".join(c_opts)
                    elif q_item.get("correctValue") is not None and str(q_item.get("correctValue")).strip() != "":
                        ans_str = str(q_item.get("correctValue"))
                    else:
                        ans_str = "-"
                p_val.text = ans_str
                p_val.runs[0].bold = True
                p_val.alignment = WD_ALIGN_PARAGRAPH.CENTER
            doc.add_paragraph().paragraph_format.space_after = Pt(4)

    f_stream = io.BytesIO()
    doc.save(f_stream)
    f_stream.seek(0)

    filename = f"{re.sub(r'[^a-zA-Z0-9_]', '_', title)}_{mode}.docx"
    return send_file(
        f_stream,
        as_attachment=True,
        download_name=filename,
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

def check_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(("0.0.0.0", port))
            return False
        except OSError:
            return True

def is_our_server_active(port=5000):
    try:
        req = urllib.request.Request(f"http://127.0.0.1:{port}/api/catalog", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=1.0) as resp:
            if resp.status == 200:
                return True
    except Exception:
        pass
    return False

def open_browser_delayed(url):
    time.sleep(1.2)
    try:
        webbrowser.open(url)
    except Exception:
        pass

if __name__ == "__main__":
    port_env = os.environ.get("PORT")
    is_cloud = bool(port_env or os.environ.get("SPACE_ID") or os.environ.get("RENDER"))
    target_port = int(port_env) if (port_env and port_env.isdigit()) else 5000

    if not is_cloud:
        # 1. If generator is already running on port 5000, open browser and do not crash
        if is_our_server_active(target_port):
            print("\n" + "="*60, flush=True)
            print(f"  [INFO] JEE Paper Generator is ALREADY RUNNING on http://localhost:{target_port}!", flush=True)
            print("  [INFO] Opening application in your default web browser...", flush=True)
            print("="*60 + "\n", flush=True)
            try:
                webbrowser.open(f"http://localhost:{target_port}")
            except Exception:
                pass
            print(f"Generator is active in your browser at http://localhost:{target_port}", flush=True)
            print("This launcher window will close in 3 seconds...", flush=True)
            time.sleep(3)
            sys.exit(0)

        # 2. If port 5000 is occupied by another app, dynamically find the next open port
        if check_port_in_use(target_port):
            for candidate_port in range(5001, 5050):
                if not check_port_in_use(candidate_port):
                    target_port = candidate_port
                    break

        target_url = f"http://localhost:{target_port}"
        print("\n" + "="*60)
        print("  JEE & Entrance Exam Paper Generator Starting...")
        print(f"  Local Address: {target_url}")
        print("  Opening browser automatically...")
        print("="*60 + "\n")
        threading.Thread(target=open_browser_delayed, args=(target_url,), daemon=True).start()
    else:
        print(f"Starting JEE Generator in Cloud Mode on port {target_port}...", flush=True)

    app.run(host="0.0.0.0", port=target_port, debug=False)
