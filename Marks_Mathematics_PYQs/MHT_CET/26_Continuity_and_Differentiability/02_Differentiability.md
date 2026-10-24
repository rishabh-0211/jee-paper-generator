# MHT CET Mathematics - Continuity and Differentiability

## Topic 2: Differentiability

**Total Questions:** 8

---

### Q1. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let K be the set of all real values of $x$, where the function $\mathrm{f}(x)=\sin |x|-|x|+2(x-\pi) \cos |x|$ is not differentiable. Then the set K is

**Options:**

- **(A)** $\{0\}$
- **(B)** an empty set
- **(C)** $\{\pi\}$
- **(D)** $\{0, \pi\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) an empty set**

**Detailed Solution:**

The given function is $f(x) = \sin |x| - |x| + 2(x-\pi) \cos |x|$.

Since $\cos |x| = \cos x$ for all $x \in \mathbb{R}$, we can rewrite the function as:
$f(x) = \sin |x| - |x| + 2(x-\pi) \cos x$

The function is composed of standard trigonometric and polynomial functions, which are differentiable everywhere except possibly at $x = 0$ due to the presence of $|x|$. We will check the differentiability of $f(x)$ at $x = 0$.

For $x > 0$, $|x| = x$, so:
$f(x) = \sin x - x + 2(x-\pi) \cos x$
Differentiating with respect to $x$:
$f'(x) = \cos x - 1 + 2 \cos x - 2(x-\pi) \sin x$
The right-hand derivative at $x = 0$ is:
$f'(0^+) = \cos(0) - 1 + 2 \cos(0) - 2(0-\pi) \sin(0) = 1 - 1 + 2(1) - 0 = 2$

For $x < 0$, $|x| = -x$, so:
$f(x) = \sin(-x) - (-x) + 2(x-\pi) \cos(-x) = -\sin x + x + 2(x-\pi) \cos x$
Differentiating with respect to $x$:
$f'(x) = -\cos x + 1 + 2 \cos x - 2(x-\pi) \sin x$
The left-hand derivative at $x = 0$ is:
$f'(0^-) = -\cos(0) + 1 + 2 \cos(0) - 2(0-\pi) \sin(0) = -1 + 1 + 2(1) - 0 = 2$

Since $f'(0^+) = f'(0^-) = 2$, the function $f(x)$ is differentiable at $x = 0$.

For all other real values of $x$, $f(x)$ is clearly differentiable as it is locally a combination of differentiable functions. 

Therefore, there is no real value of $x$ where $f(x)$ is not differentiable. The set K is an empty set.

Answer: an empty set

</details>

---

### Q2. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{S}=\left\{\mathrm{t} \in \mathrm{R} / \mathrm{f}(x)=|x-\pi|\left(\mathrm{e}^{|x|}-1\right) \sin |x|\right.$ is not differentiable at $\mathrm{t}\}$, then $\mathrm{S}$ is

**Options:**

- **(A)** $\phi$ (an empty set)
- **(B)** $\{0\}$
- **(C)** $\{\pi\}$
- **(D)** $\{0, \pi\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\phi$ (an empty set)**

**Detailed Solution:**

Differentiability at $x=\pi$ :
L.h.lim
$=\lim _{h \rightarrow 0} \frac{|\pi-h-\pi|\left(e^{|\pi-h|}-1\right) \sin |\pi-h|-0}{-h}=0$
R.h.lim
$=\lim _{h \rightarrow 0} \frac{|\pi+h-\pi|\left(e^{|\pi+h|}-1\right) \sin |\pi+h|-0}{h}=0$
Differentiability at $\boldsymbol{x}=\mathbf{0}$ :
L.h.lim $=\lim _{\mathrm{h} \rightarrow 0} \frac{|-\mathrm{h}-\pi|\left(\mathrm{e}^{|-\mathrm{h}|}-1\right) \sin |-\mathrm{h}|-0}{-\mathrm{h}}=0$
R.h.lim $=\lim _{h \rightarrow 0} \frac{|h-\pi|\left(e^{|h|}-1\right) \sin |h|-0}{h}=0$
The function $\mathrm{f}(x)$ is differentiable at $x=0, \pi$.
$\Rightarrow$ Set $\mathrm{S}$ is an empty set.

</details>

---

### Q3. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\mathrm{c}$ for the function $\mathrm{f}(x)=\log x$ on $[1, \mathrm{e}]$ if LMVT can be applied, is

**Options:**

- **(A)** $e-2$
- **(B)** $e+1$
- **(C)** $e-1$
- **(D)** e

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $e-1$**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{f}(x)=\log x \\
& \Rightarrow \mathrm{f}^{\prime}(x)=\frac{1}{x}
\end{aligned}$
By Lagrange's Mean value theorem,
$\begin{aligned}
& \mathrm{f}^{\prime}(\mathrm{c})=\frac{\mathrm{f}(\mathrm{e})-\mathrm{f}(1)}{\mathrm{e}-1} \\
& \Rightarrow \frac{1}{\mathrm{c}}=\frac{\log \mathrm{e}-\log 1}{\mathrm{e}-1} \\
& \Rightarrow \frac{1}{\mathrm{c}}=\frac{1}{\mathrm{e}-1} \\
& \Rightarrow \mathrm{c}=\mathrm{e}-1
\end{aligned}$

</details>

---

### Q4. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The function $f(x)=\frac{x+1}{9 x+x^{3}}$ is

**Options:**

- **(A)** discontinuous at exactly two points.
- **(B)** continuous for all real values of $x$.
- **(C)** discontinuous at exactly three points.
- **(D)** discontinuous at exactly one point.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) discontinuous at exactly one point.**

**Detailed Solution:**

(C)
$f(x)=\frac{x+1}{9 x+x^{3}}=\frac{x+1}{x\left(9+x^{2}\right)}$
The function is discontinuous at exactly one point i.e. $x=0$.

</details>

---

### Q5. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=|x|/x$ for x≠0 and 1 for X=0, then the function is

**Options:**

- **(A)** continuous but not differentiable at $x=0$
- **(B)** differentiable but not continuous at $x=0$
- **(C)** neither continuous nor differentiable at $x=0$
- **(D)** continuous and differentiable at $x=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) neither continuous nor differentiable at $x=0$**

**Detailed Solution:**

$f(x)=\left\{\begin{array}{cc}
1 & x>0 \\
-1 & x < 0 \\
1 & x=0
\end{array}\right.$
So function discontinuous and non differentiable

</details>

---

### Q6. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `2`

At the point $x=1$, the function $f(x)=\left\{\begin{array}{l}x^{3}-1,1 < x < \infty \\ x-1,-\infty < x \leq 1\end{array}\right.$ is

**Options:**

- **(A)** continuous and differentiable
- **(B)** continuous and not differentiable
- **(C)** discontinuous and differentiable
- **(D)** discontinuous and not differentiable

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) continuous and not differentiable**

**Detailed Solution:**

LHL $=\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1}(x-1)=0$
$$
\begin{aligned}
\mathrm{RHL} &=\lim _{x \rightarrow 1^{+}} f(x) \\
&=\lim _{x \rightarrow 1}\left(x^{3}-1\right)=0 \\
\text { Also, } \quad f(1) &=1-1=0
\end{aligned}
$$
$\therefore f$ is continuous at $x=1$ Now, $L f^{\prime}(1)=\lim _{h \rightarrow 0} \frac{f(1-h)-f(1)}{-h}$
$\begin{aligned} &=\lim _{h \rightarrow 0} \frac{(1-h)-1-0}{-h} \\ &=\lim _{h \rightarrow 0} \frac{-h}{-h}=1 \\ \text { and } R f^{\prime}(1) &=\lim _{h \rightarrow 0} \frac{f(1+h)-f(1)}{h} \end{aligned}$
$$
\begin{array}{l}
\quad=\lim _{h \rightarrow 0} \frac{(1+h)^{3}-1-0}{h} \\
=\lim _{h \rightarrow 0} \frac{1+h^{3}+3 h+3 h^{2}-1}{h} \\
=\lim _{h \rightarrow 0} h^{2}+3+3 h=3
\end{array}
$$
$\therefore f(x)$ is not differentiable at $x=1$

</details>

---

### Q7. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `2`

The set of points where the function $f(x)=|x-1| e^{x}$ is differentiable, is

**Options:**

- **(A)** $R$
- **(B)** $R-\{1\}$
- **(C)** $R-\{-1\}$
- **(D)** $R-\{0\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $R-\{1\}$**

**Detailed Solution:**

Since, $|x-1|$ is not differentiable at $x=1 .$ So, $f(x)=|x-1| e^{x}$ is not differentiable at $x=1$, Hence, the required set is $R-\{1\}$.

</details>

---

### Q8. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\sin ^{-1}\left(\frac{2 x}{1+x^{2}}\right)$, then $f(x)$ is
differentiable on

**Options:**

- **(A)** $[-1,1]$
- **(B)** $R-\{-1,1\}$
- **(C)** $R-(-1,1)$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $R-\{-1,1\}$**

**Detailed Solution:**

Given, $f(x)=\sin ^{-1}\left(\frac{2 x}{1+x^{2}}\right)$
On differentiating w.r.t. $x$, we get $\begin{aligned} f^{\prime}(x) &=\frac{1}{\sqrt{1-\left(\frac{2 x}{1+x^{2}}\right)^{2}} \times \frac{d}{d x}\left(\frac{2 x}{1+x^{2}}\right)} \\ &=\frac{1+x^{2}}{\sqrt{\left(1-x^{2}\right)^{2}}} \times \frac{2\left(1-x^{2}\right)}{\left(1+x^{2}\right)^{2}} \end{aligned}$
$=\frac{2}{1+x^{2}} \times \frac{1-x^{2}}{\left|1-x^{2}\right|}$
$=\left\{\begin{array}{l}\frac{2}{1+x^{2}}, \text { if }|x| < 1 \\ -\frac{2}{1+x^{2}}, \text { if }|x|>1\end{array}\right.$
$\therefore f^{\prime}(x)$ does not exist for $|x|=1, i e, x=\pm 1$
Hence, $f(x)$ is differentiable on $R-\{-1,1\}$.

</details>

---

