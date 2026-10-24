# JEE Main Mathematics - Functions

## Topic 10: Number of Solutions

**Total Questions:** 11

---

### Q1. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of distinct real solutions of the equation $x|x+4|+3|x+2|+10=0$ is

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** 3
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

Equation: $x|x+4| + 3|x+2| + 10 = 0$.
Critical points: $x = -4, -2$.
Case 1:
 $x \ge -2$: $x(x+4) + 3(x+2) + 10 = 0$
$\Rightarrow x^2+7x+16=0$.
Discriminant $= 49-64 = -15 < 0$. No real roots.

Case 2:
 $-4 \le x < -2$: $x(x+4) - 3(x+2) + 10 = 0$
$\Rightarrow x^2+x+4=0$.
Discriminant $= 1-16 = -15 < 0$. No real roots.

Case 3:
 $x < -4$: $-x(x+4) - 3(x+2) + 10 = 0$
$\Rightarrow x^2+7x-4=0$.
$x = \frac{-7 \pm \sqrt{65}}{2}$.
$x = \frac{-7+\sqrt{65}}{2} \approx 0.53$ (rejected, not in $x<-4$). $x = \frac{-7-\sqrt{65}}{2} \approx -7.53$ (valid).

Number of distinct real solutions $= 1$.

</details>

---

### Q2. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\text { The number of real solution(s) of the equation } x^2+3 x+2=\min \{|x-3|,|x+2|\} \text { is : }$

**Options:**

- **(A)** 1
- **(B)** 0
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

$x^2+3 x+2=\min \{|x-3|,|x+2|\}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4NjyNczt6hiZcFfSaMKKfslWVTOk3-7bH87VHxFl65o.original.fullsize.png">

$\begin{aligned}
& y=x^2+3 x+2 \\
& y=x^2+2\left(\frac{3}{2}\right) x+\frac{9}{4}-\frac{9}{4}+2 \\
& y=\left(x+\frac{3}{2}\right)^2-\frac{1}{4} \\
& y+\frac{1}{4}=\left(x+\frac{3}{2}\right)^2 \\
& \Rightarrow \text { Parabola vertex }\left(\frac{-3}{2}, \frac{-1}{4}\right)
\end{aligned}$
$\Rightarrow$ By graph 2 solution possible

</details>

---

### Q3. JEE Main 2024 (05 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

If $S=\{a \in \mathbf{R}:|2 a-1|=3[a]+2\{a\}\}$, where $[t]$ denotes the greatest integer less than or equal to $t$ and $\{t\}$ represents the fractional part of $t$, then $72 \sum_{a \in S} a$ is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

$\begin{aligned} & |2 \mathrm{a}-1|=3[\mathrm{a}]+2\{\mathrm{a}\} \\ & |2 \mathrm{a}-1|=[\mathrm{a}]+2 \mathrm{a}\end{aligned}$
$\begin{aligned} & \text { Case-1 }: \mathrm{a}>\frac{1}{2} \\ & 2 a-1=[a]+2 a \\ & {[a]=-1 \quad \therefore a \in[-1,0) \text { Reject }} \\ & \text { Case-2 }: \mathrm{a} < \frac{1}{2} \\ & -2 \mathrm{a}+1=[\mathrm{a}]+2 \mathrm{a} \\ & \mathrm{a}=\mathrm{I}+\mathrm{f} \\ & -2(\mathrm{I}+\mathrm{f})+1=\mathrm{I}+2 \mathrm{I}+2 \mathrm{f} \\ & \mathrm{I}=0, \mathrm{f}=\frac{1}{4} \quad \therefore \mathrm{a}=\frac{1}{4} \\ & \text { Hence } \mathrm{a}=\frac{1}{4} \\ & 72 \sum_{\mathrm{a} \in \mathrm{S}} \mathrm{a}=72 \times \frac{1}{4}=18\end{aligned}$

</details>

---

### Q4. JEE Main 2024 (05 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

The number of distinct real roots of the equation $|x||x+2|-5|x+1|-1=0$ is_______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4BnEG-f6yNCWkUSNtlLrEP5BfQgCfIAIUucOefrUTAA.original.fullsize.png">
Case-1
$\begin{aligned}
& x \geq 0 \\
& x^2+2 x-5 x-5-1=0 \\
& x^2-3 x-6=0 \\
& x=\frac{3 \pm \sqrt{9+24}}{2}=\frac{3 \pm \sqrt{33}}{2}
\end{aligned}$
One positive root
Case-2
$\begin{aligned}
& -1 \leq x < 0 \\
& -x^2-2 x-5 x-5-1=0 \\
& x^2+7 x+6=0 \\
& (x+6)(x+1)=0 \\
& x=-1
\end{aligned}$
one root in range
Case-3
$\begin{aligned}
& -2 \leq x < -1 \\
& x^2-2 x+5 x+5-1=0 \\
& x^2-3 x-4=0 \\
& (x-4)(x+1)=0
\end{aligned}$
No root in range
Case-4
$\begin{aligned}
& x < -2 \\
& x^2+7 x+4=0 \\
& x=\frac{-7 \pm \sqrt{49-16}}{2}=\frac{7 \pm \sqrt{33}}{2}
\end{aligned}$
one root in range
Total number of distinct roots are 3

</details>

---

### Q5. JEE Main 2024 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><msup><mn>2</mn><mi mathvariant="normal">x</mi></msup><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>,</mo><mo> </mo><mi mathvariant="normal">x</mi><mo>∈</mo><mi mathvariant="normal">R</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi></math> are respectively the number of points at which the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mfenced><mi mathvariant="normal">x</mi></mfenced></math> intersects the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>-</mo></math>axis, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi><mo>+</mo><mi mathvariant="normal">n</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>Given,</p><p>Function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><msup><mn>2</mn><mi mathvariant="normal">x</mi></msup><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>,</mo><mo> </mo><mi mathvariant="normal">x</mi><mo>∈</mo><mi mathvariant="normal">R</mi></math></p><p>Now, plotting the diagram of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mn>2</mn><mi mathvariant="normal">x</mi></msup><mo> </mo><mo>&amp;</mo><mo> </mo><mi>y</mi><mo>=</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></math> we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0bad6943-3d04-4c76-8a0a-5276e795aae9.png" style="width: 400px; height: 219px;"/></p><p>Now, from above diagram total point of intersection are three</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mi mathvariant="normal">m</mi><mo>=</mo><mn>3</mn></math></p><p>Now, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>=</mo><msup><mn>2</mn><mi mathvariant="normal">x</mi></msup><mi>ln</mi><mn>2</mn><mo>-</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi mathvariant="normal">x</mi></msup><mi>ln</mi><mn>2</mn><mo>=</mo><mn>2</mn><mi mathvariant="normal">x</mi></math></p><p>Now, again plotting the diagram of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><msup><mn>2</mn><mi mathvariant="normal">x</mi></msup><mi>ln</mi><mn>2</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mi mathvariant="normal">y</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">x</mi></math> we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bdb1a19e-f6c8-4cd4-8905-90d0cd998595.png" style="width: 400px; height: 278px;"/></p><p>So, from above diagram total point of intersection is two</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mi mathvariant="normal">n</mi><mo>=</mo><mn>2</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi><mo>+</mo><mi mathvariant="normal">n</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q6. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Consider the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced><mo>→</mo><mi mathvariant="normal">R</mi></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>-</mo><mn>1</mn></math>. Consider the statements
(I) The curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> intersects the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis exactly at one point
(II) The curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> intersects the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>cos</mi><mfrac><mi>π</mi><mn>12</mn></mfrac></math></p><p>Then</p>

**Options:**

- **(A)** Only (II) is correct
- **(B)** Both (I) and (II) are incorrect
- **(C)** Only (I) is correct
- **(D)** Both (I) and (II) are correct

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Both (I) and (II) are correct**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>12</mn><msqrt><mn>2</mn></msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mfenced><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1d48a3cc-c26f-4c15-a390-e438a42d5b68.png" style="width: 250px; height: 95px;"/></p><p>So, the function is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math>.</p><p>Thus, the function will intersect the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis only at one point.</p><p>Hence, statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> is correct.</p><p>Now, putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>π</mi><mn>12</mn></mfrac></math>in the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>3</mn><mi>x</mi><mo>=</mo><mn>4</mn><msup><mi>cos</mi><mn>3</mn></msup><mfrac><mi>π</mi><mn>12</mn></mfrac><mo>-</mo><mn>3</mn><mi>cos</mi><mfrac><mi>π</mi><mn>12</mn></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mfrac><mi>π</mi><mn>4</mn></mfrac><mo>=</mo><mn>4</mn><msup><mi>cos</mi><mn>3</mn></msup><mfrac><mi>π</mi><mn>12</mn></mfrac><mo>-</mo><mn>3</mn><mi>cos</mi><mfrac><mi>π</mi><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><msup><mi>cos</mi><mn>3</mn></msup><mfrac><mi>π</mi><mn>12</mn></mfrac><mo>-</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mi>cos</mi><mfrac><mi>π</mi><mn>12</mn></mfrac><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Now, comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>-</mo><mn>1</mn></math> we get.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfrac><mi>π</mi><mn>12</mn></mfrac></math> is a solution of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math>.</p><p>So, statement-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> is also correct.</p><p>Hence, both the statements are correct.</p>

</details>

---

### Q7. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mi>x</mi><mo>&#8712;</mo><mi>&#8477;</mi><mo>:</mo><mfenced open="[" close="]"><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mfenced open="[" close="]"><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>&#8804;</mo><mn>3</mn><mo>}</mo><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>x</mi><mo>&#8712;</mo><mi>&#8477;</mi><mo>:</mo><msup><mn>3</mn><mi>x</mi></msup><msup><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>3</mn><msup><mn>10</mn><mi>r</mi></msup></mfrac></mrow></mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></msup><mo>&#60;</mo><msup><mn>3</mn><mrow><mo>-</mo><mn>3</mn><mi>x</mi></mrow></msup></mrow></mfenced><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>t</mi><mo>]</mo></math> denotes greatest integer function. Then,

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8834;</mo><mi>C</mi><mo>,</mo><mo>&#160;</mo><mi>A</mi><mo>&#8800;</mo><mi>B</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8745;</mo><mi>B</mi><mo>=</mo><mi>&#981;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8834;</mo><mi>B</mi><mo>,</mo><mi>A</mi><mo>&#8800;</mo><mi>B</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mi>B</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mi>B</mi></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mi>x</mi><mo>&#8712;</mo><mi>&#8477;</mi><mo>:</mo><mfenced close="]" open="["><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>&#8804;</mo><mn>3</mn><mo>}</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>x</mi><mo>&#8712;</mo><mi>&#8477;</mi><mo>:</mo><msup><mn>3</mn><mi>x</mi></msup><msup><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>3</mn><msup><mn>10</mn><mi>r</mi></msup></mfrac></mrow></mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></msup><mo>&#60;</mo><msup><mn>3</mn><mrow><mo>-</mo><mn>3</mn><mi>x</mi></mrow></msup></mrow></mfenced><mo>,</mo></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>&#8804;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>+</mo><mn>3</mn><mo>+</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>+</mo><mn>4</mn><mo>&#8804;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced close="]" open="["><mi>x</mi></mfenced><mo>&#8804;</mo><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>&#8804;</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>1</mn><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mi>x</mi></msup><msup><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>3</mn><msup><mn>10</mn><mi>r</mi></msup></mfrac></mrow></mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></msup><mo>&#60;</mo><msup><mn>3</mn><mrow><mo>-</mo><mn>3</mn><mi>x</mi></mrow></msup></math></p><p>Now using infinite <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">G</mi><mo>.</mo><mi mathvariant="normal">P</mi></math> formula <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mo>&#8734;</mo></msub><mo>=</mo><mfrac><mi>a</mi><mrow><mn>1</mn><mo>-</mo><mi>r</mi></mrow></mfrac></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mi>x</mi></msup><msup><mfenced><mfrac><mrow><mn>3</mn><mo>&#183;</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></mrow></mfrac></mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></msup><mo>&#60;</mo><msup><mn>3</mn><mrow><mo>-</mo><mn>3</mn><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mi>x</mi></msup><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></msup><mo>&#60;</mo><msup><mn>3</mn><mrow><mo>-</mo><mn>3</mn><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mrow><mi>x</mi><mo>-</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>+</mo><mn>3</mn><mi>x</mi></mrow></msup><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mrow><mn>3</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></msup><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>1</mn><mo>&#8658;</mo><mi>B</mi><mo>=</mo><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mi>B</mi></math></p></blockquote>

</details>

---

### Q8. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>&#8211;</mo><mn>4</mn><mi>x</mi><mo>+</mo><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>3</mn><mo>=</mo><mi>x</mi><mo>[</mo><mi>x</mi><mo>]</mo></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo></math> denotes the greatest integer function, has:

**Options:**

- **(A)** exactly two solutions in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>&#160;</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(B)** no solution
- **(C)** a unique solution in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>)</mo></math>
- **(D)** a unique solution in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>&#160;</mo><mo>&#8734;</mo><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) a unique solution in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>&#160;</mo><mo>&#8734;</mo><mo>)</mo></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>+</mo><mn>3</mn><mo>=</mo><mi>x</mi><mfenced open="[" close="]"><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>=</mo><mi>x</mi><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>-</mo><mfenced open="[" close="]"><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mfenced open="[" close="]"><mi>x</mi></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>3</mn><mo>=</mo><mfenced open="[" close="]"><mi>x</mi></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>3</mn><mo>=</mo><mfenced open="[" close="]"><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8211;</mo><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="{" close="}"><mi>x</mi></mfenced><mo>=</mo><mn>3</mn></math></p><p>which is not Possible, since <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mi>x</mi></mfenced><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></math>.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> is the only one solution in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>.</p>

</details>

---

### Q9. JEE Main 2021 (22 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> denote the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>.</mo></math> Then, the values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> satisfying the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="]" open="["><msup><mi>e</mi><mi>x</mi></msup></mfenced><mn>2</mn></msup><mo>+</mo><mfenced close="]" open="["><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math> lie in the interval:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mi>e</mi></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn><mo>,</mo><mo>&#160;</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>3</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>e</mi></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="]" open="["><msup><mi>e</mi><mi>x</mi></msup></mfenced><mn>2</mn></msup><mo>+</mo><mfenced close="]" open="["><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>x</mi><mo>+</mo><mi>I</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>+</mo><mi>I</mi><mo>,</mo><mo>&#160;</mo><mi>I</mi><mo>&#8712;</mo><mi>Z</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mo>&#183;</mo></mfenced><mo>,</mo></math> represents the greatest integer function.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="]" open="["><msup><mi>e</mi><mi>x</mi></msup></mfenced><mn>2</mn></msup><mo>+</mo><mfenced close="]" open="["><msup><mi>e</mi><mi>x</mi></msup></mfenced><mo>+</mo><mn>1</mn><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><msup><mi>e</mi><mi>x</mi></msup></mfenced><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mi>t</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></math></p><p>But <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><msup><mi>e</mi><mi>x</mi></msup></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo></math>Not possible because we know that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>&#62;</mo><mn>0</mn><mo>)</mo></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><msup><mi>e</mi><mi>x</mi></msup></mfenced><mo>=</mo><mn>1</mn></math> and also, we know that if <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#8658;</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mn>1</mn><mo>&#8804;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>&#60;</mo><mn>2</mn></math></p><p>And, now by using the definition of logarithm, we have, if <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>a</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mi>a</mi><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></mrow></mfenced><mo>.</mo></math></p>

</details>

---

### Q10. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>:</mo><mfenced><mrow><mo>|</mo><mi>x</mi><mo>|</mo><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>6</mn></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mfenced open="|" close="|"><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mfenced><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mfrac><mn>6</mn><mfenced><mfenced open="|" close="|"><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mfenced></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d136a3b9-71d3-4cb8-89c6-edb553319895-image.png" style="width: 413px; height: 261px;" /></p><p>No. of solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q11. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

The graph of the function $y=f(x)$ is symmetrical about the line $x=2$, then

**Options:**

- **(A)** $f(x+2)=f(x-2)$
- **(B)** $f(2+x)=f(2-x)$
- **(C)** $f(x)=f(-x)$
- **(D)** $f(x)=-f(-x)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $f(2+x)=f(2-x)$**

**Detailed Solution:**

If $y=f(x)$ is symmetric about the line $x=2$ then $f(2+x)=f(2-x)$

</details>

---

