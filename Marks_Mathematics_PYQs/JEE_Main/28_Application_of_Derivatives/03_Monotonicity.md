# JEE Main Mathematics - Application of Derivatives

## Topic 3: Monotonicity

**Total Questions:** 59

---

### Q1. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The number of critical points of the function $f(x) = \begin{cases} \left|\dfrac{\sin x}{x}\right|, & x \neq 0 \\ 1, & x = 0 \end{cases}$ in the interval $(-2\pi, 2\pi)$ is equal to :

**Options:**

- **(A)** $1$
- **(B)** $3$
- **(C)** $5$
- **(D)** $7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5$**

**Detailed Solution:**

The critical points of a function are the points in its domain where the derivative is zero or does not exist.

First, consider $x = 0$. The function is continuous at $x = 0$ since $\lim_{x \to 0} \left|\dfrac{\sin x}{x}\right| = 1 = f(0)$.

For $x \in (-\pi, \pi)$, $\dfrac{\sin x}{x} > 0$, so $f(x) = \dfrac{\sin x}{x}$.

The derivative at $x = 0$ is given by $f'(0) = \lim_{x \to 0} \dfrac{\dfrac{\sin x}{x} - 1}{x} = \lim_{x \to 0} \dfrac{\sin x - x}{x^2} = 0$.

Since $f'(0) = 0$, $x = 0$ is a critical point.

Next, consider the points where $f(x) = 0$, which occurs at $x = \pi$ and $x = -\pi$ in the interval $(-2\pi, 2\pi)$.

At $x = \pi$, the inner function $g(x) = \dfrac{\sin x}{x}$ has $g(\pi) = 0$ and $g'(\pi) = -\dfrac{1}{\pi} \neq 0$. Since the derivative of the inner function is non-zero, the absolute value function $f(x) = |g(x)|$ is not differentiable at $x = \pi$. By symmetry, $f(x)$ is also not differentiable at $x = -\pi$.

Thus, $x = \pi$ and $x = -\pi$ are critical points.

For $x \neq 0, \pi, -\pi$, the function is differentiable and $f'(x) = \pm \dfrac{x \cos x - \sin x}{x^2}$.

Setting $f'(x) = 0$ gives $x \cos x - \sin x = 0 \Rightarrow \tan x = x$.

We analyze the roots of $\tan x = x$ in $(-2\pi, 2\pi)$:

In $(0, \pi)$, $\tan x > x$ for $x \in (0, \pi/2)$ and $\tan x < 0 < x$ for $x \in (\pi/2, \pi)$. There are no roots in this interval.

In $(\pi, 2\pi)$, $\tan x$ increases from $0$ to $\infty$ on $(\pi, 3\pi/2)$. Since $\tan \pi = 0 < \pi$ and $\tan x \to \infty$ as $x \to 3\pi/2^{-}$, there is exactly one root in $(\pi, 3\pi/2)$. In $(3\pi/2, 2\pi)$, $\tan x < 0 < x$, yielding no roots.

Since $\tan x = x$ is an odd equation, there is exactly one symmetric root in $(-2\pi, -\pi)$.

This gives $2$ additional critical points where $f'(x) = 0$.

The total number of critical points in $(-2\pi, 2\pi)$ is $1$ (at $x=0$) $+ 2$ (at $x=\pm \pi$) $+ 2$ (roots of $\tan x = x$) $= 5$.

Answer: $5$

</details>

---

### Q2. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Consider the following three statements for the function $f:(0, \infty) \rightarrow \mathbb{R}$ defined by $f(x)=\left|\log _{\mathrm{e}} x\right|-|x-1|$ : 
 (I) $f$ is differentiable at all $x>0$. 
 (II) $f$ is increasing in $(0,1)$. 
 (III) $f$ is decreasing in $(1, \infty)$. 
 Then.

**Options:**

- **(A)** All (I), (II) and (III) are TRUE.
- **(B)** Only (II) and (III) are TRUE.
- **(C)** Only (I) is TRUE.
- **(D)** Only (I) and (III) are TRUE.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Only (I) and (III) are TRUE.**

**Detailed Solution:**

For $0 < x < 1$: $f(x) = -\ln x + x - 1$, $f'(x) = -\frac{1}{x} + 1 = \frac{x-1}{x} < 0$ (decreasing).
For $x > 1$: $f(x) = \ln x - x + 1$, $f'(x) = \frac{1}{x} - 1 = \frac{1-x}{x} < 0$ (decreasing).
At $x = 1$: LHD $= \frac{1-1}{1} = 0$, RHD $= \frac{1-1}{1} = 0$. So $f$ is differentiable at $x = 1$.
(I) TRUE: $f$ is differentiable for all $x > 0$.
(II) FALSE: $f$ is decreasing in $(0, 1)$.
(III) TRUE: $f$ is decreasing in $(1, \infty)$.
Only (I) and (III) are TRUE.

</details>

---

### Q3. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f: \mathbb{R} \to \mathbb{R}$ be a twice differentiable function such that $f''(x) > 0$ for all $x \in \mathbb{R}$ and $f'(a-1) = 0$, where $a$ is a real number. Let $g(x) = f\left( \tan^{2}x - 2\tan x + a \right), \; 0 < x < \frac{\pi}{2}$.
 
 Consider the following two statements: 
 (I) $g$ is increasing in $\left(0, \frac{\pi}{4}\right)$ 
 (II) $g$ is decreasing in $\left(\frac{\pi}{4}, \frac{\pi}{2}\right)$. Then,

**Options:**

- **(A)** Neither (I) nor (II) is True
- **(B)** Only (I) is True
- **(C)** Both (I) and (II) are True
- **(D)** Only (II) is True

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Neither (I) nor (II) is True**

**Detailed Solution:**

Given $f''(x) > 0$ for all $x \in \mathbb{R}$, which means $f'(x)$ is a strictly increasing function.
We are given $f'(a-1) = 0$. Since $f'(x)$ is strictly increasing, $f'(x) < 0$ for $x < a-1$ and $f'(x) > 0$ for $x > a-1$.
The function $g(x)$ is defined as $g(x) = f(\tan^2 x - 2\tan x + a)$ for $x \in (0, \pi/2)$.
Let $u(x) = \tan^2 x - 2\tan x + a = (\tan x - 1)^2 + a - 1$.
Differentiating $g(x)$ with respect to $x$:
$g'(x) = f'(u(x)) \cdot u'(x) = f'((\tan x - 1)^2 + a - 1) \cdot (2\tan x \sec^2 x - 2\sec^2 x)$
$g'(x) = f'((\tan x - 1)^2 + a - 1) \cdot 2\sec^2 x (\tan x - 1)$.

Case 1: $x \in (0, \pi/4)$.
In this interval, $0 < \tan x < 1$, so $(\tan x - 1) < 0$.
Also, $(\tan x - 1)^2 > 0$, so $u(x) = (\tan x - 1)^2 + a - 1 > a - 1$.
Since $f'(x)$ is increasing and $f'(a-1) = 0$, for $u(x) > a - 1$, we have $f'(u(x)) > 0$.
Thus, $g'(x) = (+)(+)(-) < 0$. So $g(x)$ is decreasing in $(0, \pi/4)$.
Statement (I) is False.

Case 2: $x \in (\pi/4, \pi/2)$.
In this interval, $\tan x > 1$, so $(\tan x - 1) > 0$.
Also, $(\tan x - 1)^2 > 0$, so $u(x) = (\tan x - 1)^2 + a - 1 > a - 1$.
Thus, $f'(u(x)) > 0$.
Then $g'(x) = (+)(+)(+) > 0$. So $g(x)$ is increasing in $(\pi/4, \pi/2)$.
 Statement (II) is False.

Therefore, neither (I) nor (II) is true.

</details>

---

### Q4. JEE Main 2026 (21 January Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $f: \mathbf{R} \rightarrow \mathbf{R}$ be a twice differentiable function such that the quadratic equation $f(x) \mathrm{m}^{2}-2 f^{\prime}(x) \mathrm{m}+f^{\prime \prime}(x)=0$ in m, has two equal roots for every $x \in \mathbf{R}$. If $f(0)=1, f^{\prime}(0)=2$, and $(\alpha, \beta)$ is the largest interval in which the function $f\left(\log _{\mathrm{e}} x-x\right)$ is increasing, then $\alpha+\beta$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

For equal roots in $f(x)m^2 - 2f'(x)m + f''(x) = 0$, discriminant = 0:
$[f'(x)]^2 = f(x)f''(x)$
This gives $\frac{f''(x)}{f'(x)} = \frac{f'(x)}{f(x)}$
Integrating: $f'(x) = kf(x)$, so $f(x) = Ae^{kx}$
Using $f(0) = 1$ and $f'(0) = 2$: $A = 1$, $k = 2$
$f(x) = e^{2x}$
For $g(x) = f(\ln x - x)$:
$g'(x) = 2e^{2(\ln x - x)} \cdot \left(\frac{1}{x} - 1\right)$
$g'(x) > 0$ when $\frac{1-x}{x} > 0$, i.e., $0 < x < 1$
$(\alpha, \beta) = (0, 1)$
$\alpha + \beta = 1$

</details>

---

### Q5. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let the function $f(x)=\frac{x}{3}+\frac{3}{x}+3, x \neq 0$ be strictly increasing in $\left(-\infty, \alpha_1\right) \mathrm{U}\left(\alpha_2, \infty\right)$ and strictly decreasing in $\left(\alpha_3, \alpha_4\right) \mathrm{U}\left(\alpha_4, \alpha_5\right)$. Then $\sum_{\mathrm{i}=1}^5 \alpha_{\mathrm{i}}^2$ is equal to :-

**Options:**

- **(A)** 48
- **(B)** 28
- **(C)** 40
- **(D)** 36

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 36**

**Detailed Solution:**

$\begin{aligned} & f(x)=\frac{x}{3}+\frac{3}{x}+3, x \neq 0 \\ & f^{\prime}(x)=\frac{1}{3}-\frac{3}{x^2}=0 \quad \Rightarrow x= \pm 3 \\ & f^{\prime}(x)=\frac{x^2-3}{3 x^2}\end{aligned}$
$\begin{aligned} & \mathrm{f}^{\prime}(\mathrm{x}) \gt 0 \forall(-\infty,-3) \cup(3, \infty) \rightarrow \text { increasing } \\ & \mathrm{f}^{\prime}(\mathrm{x}) \lt 0 \forall(-3,0) \cup(0,3) \rightarrow \text { decreasing }\end{aligned}$
$\sum_{i=1}^5 \alpha_i^2=(-3)^2+(3)^2+(-3)^2+(0)^2+(3)^2$
$=36$

</details>

---

### Q6. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{f}: \mathrm{R} \rightarrow \mathrm{R}$ be a function defined by $f(x)=\|x+2|-2| x\|$. If $m$ is the number of points of local minima and $n$ is the number of points of local maxima of $f$, then $m+n$ is

**Options:**

- **(A)** $5$
- **(B)** $3$
- **(C)** $2$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3$**

**Detailed Solution:**

$f(x)=\|x+2|-2| x\|$
Critical points, $0,-2,2,-\frac{2}{3}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/lUQwrsE8_MD9LMFoj2FFH_rP016pWcDUSH6D6T2Do_g.original.fullsize.png"/>
No. of maxima $=1$
No. of minima $=2$
option (2)

</details>

---

### Q7. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $(2,3)$ be the largest open interval in which the function $f(x)=2 \log _{\mathrm{e}}(x-2)-x^2+a x+1$ is strictly increasing and (b, c) be the largest open interval, in which the function $\mathrm{g}(x)=(x-1)^3(x+2-\mathrm{a})^2$ is strictly decreasing. Then $100(a+b-c)$ is equal to :

**Options:**

- **(A)** 420
- **(B)** 360
- **(C)** 160
- **(D)** 280

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 360**

**Detailed Solution:**

$\begin{aligned} & \mathrm{f}^{\prime}(\mathrm{x})=\frac{2}{\mathrm{x}-2}-2 \mathrm{x}+\mathrm{a} \geq 0 \\ & \mathrm{f}^{\prime \prime}(\mathrm{x})=\frac{-2}{(\mathrm{x}-2)^2}-2 < 0 \\ & \mathrm{f}^{\prime}(\mathrm{x}) \downarrow \\ & \mathrm{f}^{\prime}(3) \geq 0 \\ & 2-6+\mathrm{a} \geq 0 \\ & \mathrm{a} \geq 4 \\ & \mathrm{a}_{\min }=4 \\ & \mathrm{~g}(\mathrm{x})=(\mathrm{x}-1)^3(\mathrm{x}+2-\mathrm{a})^2 \\ & \mathrm{~g}(\mathrm{x})=(\mathrm{x}-1)^3(\mathrm{x}-2)^2 \\ & \mathrm{~g}{ }^{\prime}(\mathrm{x})=(\mathrm{x}-1)^3 2(\mathrm{x}-2)+(\mathrm{x}-2)^2 3(\mathrm{x}-1)^2 \\ & =(\mathrm{x}-1)^2(\mathrm{x}-2)(2 \mathrm{x}-2+3 \mathrm{x}-6) \\ & =(\mathrm{x}-1)^2(\mathrm{x}-2)(5 \mathrm{x}-8) < 0 \\ & \mathrm{x} \in\left(\frac{8}{5}, 2\right) \\ & 100(\mathrm{a}+\mathrm{b}-\mathrm{c})=100\left(4+\frac{8}{5}-2\right)=360\end{aligned}$

</details>

---

### Q8. JEE Main 2024 (09 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the set of all values of $p$, for which $f(x)=\left(p^2-6 p+8\right)\left(\sin ^2 2 x-\cos ^2 2 x\right)+2(2-p) x+7$ does not have any critical point, be the interval $(a, b)$. Then $16 a b$ is equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **252**

**Detailed Solution:**

$\begin{aligned} & f(x)=-\left(p^2-6 p+8\right) \cos 4 n+2(2-p) n+7 \\ & f^1(x)=+4\left(p^2-6 p+8\right) \sin 4 x+(4-2 p) \neq 0 \\ & \sin 4 x \neq \frac{2 p-4}{4(p-4)(p-2)}\end{aligned}$
$\begin{aligned}
& \sin 4 x \neq \frac{2(p-2)}{4(p-4)(p-2)} \\
& p \neq 2 \\
& \quad \sin 4 x \neq \frac{1}{2(p-4)} \\
& \Rightarrow\left|\frac{1}{2(p-4)}\right|>1
\end{aligned}$
on solving we get
$\therefore \mathrm{p} \in\left(\frac{7}{2}, \frac{9}{2}\right)$
Hence $\mathrm{a}=\frac{7}{2}, \mathrm{~b}=\frac{9}{2}$
$\therefore 16 \mathrm{ab}=252$

</details>

---

### Q9. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of critical points of the function $f(x)=(x-2)^{2 / 3}(2 x+1)$ is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 0
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2**

**Detailed Solution:**

$\begin{aligned} & \mathrm{f}(\mathrm{x})=(\mathrm{x}-2)^{2 / 3}(2 \mathrm{x}+1) \\ & \mathrm{f}^{\prime}(\mathrm{x})=\frac{2}{3}(\mathrm{x}-2)^{-1 / 3}(2 \mathrm{x}+1)+(\mathrm{x}-2)^{2 / 3} \\ & \mathrm{f}^{\prime}(\mathrm{x})=2 \times \frac{(2 \mathrm{x}+1)+(\mathrm{x}-2)}{3(\mathrm{x}-2)^{1 / 3}} \\ & \frac{3 \mathrm{x}-1}{(\mathrm{x}-2)^{1 / 3}}=0\end{aligned}$
Critical points $\mathrm{x}=\frac{1}{3}$ and $\mathrm{x}=2$

</details>

---

### Q10. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For the function $f(x)=(\cos x)-x+1, x \in \mathbb{R}$, between the following two statements
(S1) $f(x)=0$ for only one value of $x$ in $[0, \pi]$.
(S2) $f(x)$ is decreasing in $\left[0, \frac{\pi}{2}\right]$ and increasing in $\left[\frac{\pi}{2}, \pi\right]$.

**Options:**

- **(A)** Both (S1) and (S2) are correct.
- **(B)** Both (S1) and (S2) are incorrect.
- **(C)** Only (S2) is correct.
- **(D)** Only (S1) is correct.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Only (S1) is correct.**

**Detailed Solution:**

$\begin{aligned} & f^{\prime}(x)=\cos x-x+1 \\ & f^{\prime}(x)=-\sin x-1\end{aligned}$
$\mathrm{f}$ is decreasing $\forall \mathrm{x} \in \mathrm{R}$
$\begin{aligned} & \mathrm{f}(\mathrm{x})=0 \\ & \mathrm{f}(0)=2, \mathrm{f}(\pi)=-\pi\end{aligned}$
$\mathrm{f}$ is strictly decreasing in $[0, \pi]$ and $\mathrm{f}(0) . \mathrm{f}(\pi) < 0$
$\Rightarrow$ only one solution of $\mathrm{f}(\mathrm{x})=0$
$\mathrm{S} 1$ is correct and $\mathrm{S} 2$ is incorrect.

</details>

---

### Q11. JEE Main 2024 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>4</mn><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn><mo>,</mo><mo>∀</mo><mi>x</mi><mo>≠</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> is strictly increasing in:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac></mrow></mfenced><mo>∪</mo><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac><mo>,</mo><mi>∞</mi></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>−</mo><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced><mo>∪</mo><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac><mo>,</mo><mi>∞</mi></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>−</mo><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced><mo>∪</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>−</mo><mi>∞</mi><mo>,</mo><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac></mrow></mfenced><mo>∪</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>−</mo><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced><mo>∪</mo><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac><mo>,</mo><mi>∞</mi></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>4</mn><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Replacing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>x</mi></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>5</mn><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>+</mo><mn>4</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Using, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>×</mo><mn>5</mn><mo>-</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>×</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>25</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>20</mn><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>-</mo><mn>16</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>20</mn><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mo>-</mo><mfrac><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>9</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>-</mo><mn>2</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>9</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>×</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfenced><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>-</mo><mfrac><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mo>×</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mn>5</mn><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>y</mi><mo>'</mo></msup><mo>=</mo><mn>20</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>y</mi><mo>'</mo></msup><mo>=</mo><mn>4</mn><mi>x</mi><mfenced><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>For function to be increasing <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>'</mo></msup><mo>&gt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>∈</mo><mfenced><mrow><mo>-</mo><msqrt><mfrac><mn>1</mn><mn>5</mn></mfrac></msqrt><mo>,</mo><mn>0</mn></mrow></mfenced><mo>∪</mo><mfenced><mrow><msqrt><mfrac><mn>1</mn><mn>5</mn></mfrac></msqrt><mo>,</mo><mo>∞</mo></mrow></mfenced></math></p>

</details>

---

### Q12. JEE Main 2024 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>16</mn></mrow></mfrac><mo>,</mo><mi>x</mi><mo>∈</mo><mi mathvariant="normal">ℝ</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>8</mn></mrow></mfenced></math>

**Options:**

- **(A)** decreases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>8</mn><mo>)</mo></math> and increases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>∞</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>∪</mo><mo>(</mo><mn>8</mn><mo>,</mo><mo>∞</mo><mo>)</mo></math>
- **(B)** decreases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>∞</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>∪</mo><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>8</mn><mo>)</mo><mo>∪</mo><mo>(</mo><mn>8</mn><mo>,</mo><mo>∞</mo><mo>)</mo></math>
- **(C)** decreases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>∞</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo></math> and increases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>8</mn><mo>,</mo><mo>∞</mo><mo>)</mo></math>
- **(D)** increases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>∞</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>∪</mo><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>8</mn><mo>)</mo><mo>∪</mo><mo>(</mo><mn>8</mn><mo>,</mo><mo>∞</mo><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) decreases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>∞</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>∪</mo><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>8</mn><mo>)</mo><mo>∪</mo><mo>(</mo><mn>8</mn><mo>,</mo><mo>∞</mo><mo>)</mo></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>16</mn></mrow></mfrac></math></p><p>Now differentiating the above function we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>16</mn></mrow></mfenced><mo>·</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>·</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>6</mn></mrow></mfenced></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>16</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>16</mn></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>16</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>&lt;</mo><mn>0</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>16</mn><mo>≠</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>16</mn><mo>≠</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>8</mn></mrow></mfenced><mo>≠</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>≠</mo><mn>8</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>,</p><p>So, the function is always decreasing in<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mo>(</mo><mo>-</mo><mo>∞</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>∪</mo><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>8</mn><mo>)</mo><mo>∪</mo><mo>(</mo><mn>8</mn><mo>,</mo><mo>∞</mo><mo>)</mo></math>.</p>

</details>

---

### Q13. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>=</mo><mn>3</mn><mi mathvariant="normal">f</mi><mfenced><mfrac><mi mathvariant="normal">x</mi><mn>3</mn></mfrac></mfenced><mo>+</mo><mi mathvariant="normal">f</mi><mo>(</mo><mn>3</mn><mo>-</mo><mi mathvariant="normal">x</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">f</mi><mo>"</mo></msup><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>&gt;</mo><mn>0</mn></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>∈</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>3</mn><mo>)</mo></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi></math> is decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mi mathvariant="normal">α</mi><mo>)</mo></math> and increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">α</mi><mo>,</mo><mn>3</mn><mo>)</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi mathvariant="normal">α</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>=</mo><mn>3</mn><mi mathvariant="normal">f</mi><mfenced><mfrac><mi mathvariant="normal">x</mi><mn>3</mn></mfrac></mfenced><mo>+</mo><mi mathvariant="normal">f</mi><mo>(</mo><mn>3</mn><mo>-</mo><mi mathvariant="normal">x</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">f</mi><mo>"</mo></msup><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>&gt;</mo><mn>0</mn><mo>∀</mo><mi mathvariant="normal">x</mi><mo>∈</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>3</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo></math> is increasing function</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">g</mi><mo>'</mo></msup><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>=</mo><mn>3</mn><mo>×</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>·</mo><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mfenced><mfrac><mi mathvariant="normal">x</mi><mn>3</mn></mfrac></mfenced><mo>-</mo><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mo>(</mo><mn>3</mn><mo>-</mo><mi mathvariant="normal">x</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">g</mi><mo>'</mo></msup><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>=</mo><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mfenced><mfrac><mi mathvariant="normal">x</mi><mn>3</mn></mfrac></mfenced><mo>-</mo><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mo>(</mo><mn>3</mn><mo>-</mo><mi mathvariant="normal">x</mi><mo>)</mo></math></p><p>It is given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi></math> is decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo> </mo><mi mathvariant="normal">α</mi></mrow></mfenced></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">g</mi><mo>'</mo></msup><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>&lt;</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mfenced><mfrac><mi mathvariant="normal">x</mi><mn>3</mn></mfrac></mfenced><mo>-</mo><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mo>(</mo><mn>3</mn><mo>-</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>&lt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mfenced><mfrac><mi mathvariant="normal">x</mi><mn>3</mn></mfrac></mfenced><mo>&lt;</mo><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mo>(</mo><mn>3</mn><mo>-</mo><mi mathvariant="normal">x</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi mathvariant="normal">x</mi><mn>3</mn></mfrac><mo>&lt;</mo><mn>3</mn><mo>-</mo><mi mathvariant="normal">x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">x</mi><mo>&lt;</mo><mn>9</mn><mo>-</mo><mn>3</mn><mi mathvariant="normal">x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">x</mi><mo>&lt;</mo><mfrac><mn>9</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">α</mi><mo>=</mo><mfrac><mn>9</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>8</mn><mi mathvariant="normal">α</mi><mo>=</mo><mn>8</mn><mo>×</mo><mfrac><mn>9</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>8</mn><mi mathvariant="normal">α</mi><mo>=</mo><mn>18</mn></math></p>

</details>

---

### Q14. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>The set of all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math> for which the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>|</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>|</mo><mo>+</mo><mo>|</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>|</mo><mo>+</mo><mi>a</mi><mo>=</mo><mn>0</mn></math> has exactly one real root, is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>7</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>6</mn><mo>,</mo><mo>-</mo><mn>3</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>3</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>|</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>|</mo><mo>+</mo><mo>|</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>|</mo><mo>+</mo><mi>a</mi><mo>=</mo><mn>0</mn></math></p><p>Now taking, Case I: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>2</mn></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>+</mo><mi>a</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></math> is decreasing <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo></math></p><p>Now taking Case II: <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>+</mo><mi>a</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn></math> </p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo>)</mo></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> is decreasing <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo>)</mo></math></p><p>Now taking Case III: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>+</mo><mi>a</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced></math> is decreasing <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math></p><p>Hence, from all the cases we can say that nature of function is continuously decreasing so, it will cut <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis only one time,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Exactly one real root <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8704;</mo><mo>&#160;</mo><mi>a</mi><mo>&#8712;</mo><mi>R</mi></math></p></blockquote>

</details>

---

### Q15. JEE Main 2023 (11 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be a differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>1</mn><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>.
Consider the following two statements:</p><p>(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mtext>for&#160;all</mtext><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>1</mn><mo>/</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mtext>for&#160;all</mtext><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>Then,</p>

**Options:**

- **(A)** Neither statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>A</mi><mo>)</mo></math> nor statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>B</mi><mo>)</mo></math> is true
- **(B)** Only statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>B</mi><mo>)</mo></math> is true
- **(C)** Both the statements <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>A</mi><mo>)</mo></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>B</mi><mo>)</mo><mo>&#160;</mo></math>are true
- **(D)** Only statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>A</mi><mo>)</mo></math> is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Both the statements <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>A</mi><mo>)</mo></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>B</mi><mo>)</mo><mo>&#160;</mo></math>are true**

**Detailed Solution:**

<p>Given,</p><p>Domain and range of function,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced><mi>f</mi><mfenced><mi>x</mi></mfenced><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced><mo>&#8805;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced close="]" open="["><mrow><mi>x</mi><mi>ln</mi><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>&#8805;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced close="]" open="["><mrow><mi>x</mi><mi>ln</mi><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>&#8805;</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced close="]" open="["><mrow><mi>x</mi><mi>ln</mi><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>x</mi></mrow></mfenced><mo>&#8805;</mo><mn>0</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>x</mi><mfenced><mrow><mi>ln</mi><mi>x</mi></mrow></mfenced><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>x</mi></math> is a increasing function,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>h</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#8805;</mo><mi>h</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>2</mn><mo>,</mo><mn>4</mn><mo>]</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>ln</mi><mi>x</mi><mo>&#215;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>x</mi><mo>&#8805;</mo><mn>2</mn><mi>ln</mi><mn>2</mn><mo>&#215;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>ln</mi><mi>x</mi><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><mi>x</mi><mo>&#8805;</mo><mi>ln</mi><mn>2</mn><mo>-</mo><mn>2</mn></math></p><p>Similarly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mi>h</mi><mfenced><mn>4</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>ln</mi><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>x</mi><mo>&#8804;</mo><mi>ln</mi><mn>4</mn><mo>-</mo><mn>4</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>ln</mi><mn>2</mn><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mi>ln</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>ln</mi><mi>x</mi></mrow></mfrac><mo>&#8804;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#8804;</mo><mfrac><mrow><mi>ln</mi><mn>4</mn><mo>-</mo><mn>4</mn></mrow><mrow><mi>x</mi><mi>ln</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>ln</mi><mi>x</mi></mrow></mfrac></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>ln</mi><mn>4</mn><mo>-</mo><mn>4</mn></mrow><mrow><mi>x</mi><mi>ln</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>ln</mi><mi>x</mi></mrow></mfrac><mo>&#8804;</mo><mfrac><mrow><mi>ln</mi><mn>4</mn><mo>-</mo><mn>4</mn></mrow><mrow><mn>2</mn><mi>ln</mi><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>ln</mi><mn>2</mn></mrow></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mrow><mi>ln</mi><mn>2</mn></mrow></mfrac><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mn>1</mn><mo>&#160;</mo><mtext>for</mtext><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>ln</mi><mn>2</mn><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mi>ln</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>ln</mi><mi>x</mi></mrow></mfrac><mo>&#8805;</mo><mfrac><mrow><mi>ln</mi><mn>2</mn><mo>-</mo><mn>2</mn></mrow><mrow><mn>4</mn><mi>ln</mi><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>ln</mi><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>ln</mi><mn>2</mn><mo>-</mo><mn>2</mn></mrow><mrow><mn>4</mn><mi>ln</mi><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>ln</mi><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>ln</mi><mn>2</mn></mrow></mfrac><mo>&#62;</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#8805;</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math></p><p>Hence both <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are correct.
Note this question was bonus in Jee Main 2023 April session, as LMVT on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#183;</mo><mi>x</mi><mi>ln</mi><mi>x</mi></math> can&#39;t be satisfied.</p><p>Hence, no such <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> exist.</p>

</details>

---

### Q16. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is decreasing in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mi>&#945;</mi></mrow></mfenced></math> and increasing in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mn>1</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mi>&#945;</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow><mi>&#945;</mi></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#960;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#960;</mi></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is decreasing in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mi>&#945;</mi></mrow></mfenced></math> and increasing in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mn>1</mn></mrow></mfenced></math>,</p><p>Now solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math></p><p>Now differentiating both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>-</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math></p><p>Differentiating again we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math> is increasing as given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mn>0</mn></mfenced><mo>&#60;</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>0</mn></mfenced><mo>-</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>&#60;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>-</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>0</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>0</mn></mfenced><mo>&#60;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced></math></p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>-</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math> is positive for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math> is negative for  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>So, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mi>&#945;</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow><mi>&#945;</mi></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mo>+</mo><mn>3</mn></mrow><mrow><mn>1</mn><mo>-</mo><mn>6</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac><mo>=</mo><mi mathvariant="normal">&#960;</mi></math></p></blockquote>

</details>

---

### Q17. JEE Main 2023 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>The number of points, where the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>5</mn></msup><mo>-</mo><mn>20</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>50</mn><mi>x</mi><mo>+</mo><mn>2</mn></math> crosses the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis, is _____.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<blockquote><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>x</mi><mn>5</mn></msup><mo>-</mo><mn>20</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>50</mn><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p>Now differentiating the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> we get,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>5</mn><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>60</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>50</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>5</mn><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>10</mn></mrow></mfenced></math></p><p>Now equating <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>10</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>12</mn><mo>&#177;</mo><msqrt><mn>144</mn><mo>-</mo><mn>40</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>6</mn><mo>&#177;</mo><msqrt><mn>26</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8776;</mo><mn>11</mn><mo>.</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>.</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8776;</mo><mo>&#177;</mo><mn>3</mn><mo>.</mo><mn>31</mn><mo>,</mo><mo>&#160;</mo><mo>&#177;</mo><mn>0</mn><mo>.</mo><mn>95</mn></math></p><p>Now finding the nature of function at integer value near by above value we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>&#62;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>&#60;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#60;</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p>Now plotting the graph by observing above values, we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4bbf06d4-950b-4ae8-99cf-74634038d164.png" style="width: 299px; height: 146px;" /></p><p>Hence, it will cross <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> times.</p></blockquote>

</details>

---

### Q18. JEE Main 2023 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mi>x</mi><mo>+</mo><msup><mi>g</mi><mo>&#34;</mo></msup><mfenced><mn>2</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>-</mo><mi>g</mi><mfenced><mn>4</mn></mfenced></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mi>x</mi><mo>+</mo><msup><mi>g</mi><mo>&#34;</mo></msup><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mfenced open="[" close="]"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced></mrow></mfenced><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="[" close="]"><mrow><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>2</mn></mrow></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>f</mi><mfenced><mn>1</mn></mfenced><mi>x</mi><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>g</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, then we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>g</mi><mo>&#34;</mo></msup><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>2</mn><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mi>x</mi><mo>+</mo><msup><mi>g</mi><mo>&#34;</mo></msup><mfenced><mn>2</mn></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>, then we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>+</mo><msup><mi>g</mi><mo>&#34;</mo></msup><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi></math></p><p>And, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>-</mo><mi>g</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>4</mn><mo>+</mo><mn>10</mn><mo>=</mo><mn>14</mn></math></p>

</details>

---

### Q19. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mi>x</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>. Then

**Options:**

- **(A)** There exists <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>max</mi><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mi>max</mi><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced></math>
- **(C)** There exist <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>&#60;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#60;</mo><mn>3</mn></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>min</mi><mo>&#160;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><mi>max</mi><mo>&#160;</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>max</mi><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mi>max</mi><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>ln</mi><mfenced><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>&#8804;</mo><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>10</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>&#8804;</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>&#8804;</mo><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>&#8804;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>&#8804;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>21</mn><mn>10</mn></mfrac><mo>&#8804;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mn>3</mn></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>10</mn></msqrt></mfrac><mo>&#8804;</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>min</mi><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>21</mn><mn>10</mn></mfrac><mo>&#8800;</mo><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mi>max</mi><mo>&#160;</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced></math></p><p>Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math> is incorrect</p><p>From above,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p>Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> is incorrect.</p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math> are both positive so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> both are increasing</p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>max</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>max</mi><mfenced><mrow><mi>g</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></mrow></mfenced></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced><mrow><mn>3</mn><mo>+</mo><msqrt><mn>10</mn></msqrt></mrow></mfenced></math> </p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>3</mn><mo>&#62;</mo><mi>ln</mi><mfenced><mrow><mn>3</mn><mo>+</mo><msqrt><mn>10</mn></msqrt></mrow></mfenced></math> </p><p>Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> is correct</p>

</details>

---

### Q20. JEE Main 2023 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mn>2</mn><mi>b</mi><mi>x</mi><mo>+</mo><mfrac><mrow><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo><mi>a</mi><mo>&#8800;</mo><mn>2</mn><mi>b</mi></math> have a common extreme point, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mo>+</mo><mn>7</mn></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mn>2</mn><mi>b</mi><mi>x</mi><mo>+</mo><mfrac><mrow><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></math></p><p>Now differentiating the above function we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>a</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mi>x</mi></math></p><p>Now given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn><mo>&#160;</mo><mi>a</mi><mi>n</mi><mi>d</mi><mo>&#160;</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math> have a common extreme point,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>a</mi><mi>x</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mo>-</mo><mi>x</mi><mfenced><mrow><mn>2</mn><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>1</mn></math> is the common extreme point</p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>a</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mo>+</mo><mn>7</mn><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q21. JEE Main 2022 (28 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></msup><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>, is

**Options:**

- **(A)** increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(D)** decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></msup></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is:</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></msup></math></p><p>Differentiating both side w.r.t <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mi>e</mi><mrow><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msup><mi>e</mi><mrow><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msup><mi>e</mi><mrow><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Now finding critical point by equating <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p><p>And increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math></p></blockquote>

</details>

---

### Q22. JEE Main 2022 (26 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>, for which the function <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>a</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>a</mi><mi>x</mi><mo>+</mo><mn>7</mn></math> is non-decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></math>, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#175;</mo></mover></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mover><mi>a</mi><mo>&#175;</mo></mover></msub><mfenced><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>-</mo><mfrac><mrow><mn>9</mn><mi>&#960;</mi></mrow><mrow><mn>4</mn><mfenced><mrow><mn>9</mn><mo>+</mo><msup><mi>&#960;</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>-</mo><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mrow><mn>9</mn><mfenced><mrow><mn>4</mn><mo>+</mo><msup><mi>&#960;</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>&#960;</mi><mn>2</mn></msup></mrow><mrow><mn>9</mn><mo>+</mo><msup><mi>&#960;</mi><mn>2</mn></msup></mrow></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>-</mo><mfrac><mrow><mn>9</mn><mi>&#960;</mi></mrow><mrow><mn>4</mn><mfenced><mrow><mn>9</mn><mo>+</mo><msup><mi>&#960;</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>a</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>a</mi><mi>x</mi><mo>+</mo><mn>7</mn></math> is non-decreasing function in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></math>, so </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><msub><mi>f</mi><mi>a</mi></msub><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>-</mo><mn>3</mn><mi>a</mi><mo>&#8805;</mo><mn>0</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8804;</mo><msub><mfenced><mfrac><mn>2</mn><mrow><mn>3</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></mfenced><mi>min</mi></msub></math> </p><p>Now, maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>max</mi></msub><mo>=</mo><mover><mi>a</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mn>6</mn><mrow><mn>9</mn><mo>+</mo><msup><mi>&#960;</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mover><mi>a</mi><mo>&#175;</mo></mover></msub><mfenced><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mn>3</mn><mfenced><mfrac><mn>6</mn><mrow><mn>9</mn><mo>+</mo><msup><mi>&#960;</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mfenced><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mfenced><mo>+</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mrow><mn>9</mn><mi>&#960;</mi></mrow><mrow><mn>4</mn><mfenced><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn></mrow></mfenced></mrow></mfrac><mo>+</mo><mn>7</mn><mo>=</mo><mn>8</mn><mo>-</mo><mfrac><mrow><mn>9</mn><mi>&#960;</mi></mrow><mrow><mn>4</mn><mfenced><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn></mrow></mfenced></mrow></mfrac></math></p></blockquote>

</details>

---

### Q23. JEE Main 2022 (26 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

Let the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>,</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>, be decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mi>a</mi></mrow></mfenced></math> and increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mn>4</mn></mrow></mfenced></math>. A tangent to the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>a</mi><mi>x</mi></math> at a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> on it passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>8</mn><mi>a</mi><mo>,</mo><mo>&#160;</mo><mn>8</mn><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math> but does not pass through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced></math>. If the equation of the normal at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mi>&#945;</mi></mfrac><mo>+</mo><mfrac><mi>y</mi><mi>&#946;</mi></mfrac><mo>=</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **45**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>&#177;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>But given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mtext>so</mtext><mo>&#160;</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>So function is decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math> and increasing in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Now equation of parabola will be <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>x</mi></math></p><p>Now tangent to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>x</mi></math> will be given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>m</mi></mrow></mfrac></math>, given this tangent passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>8</mn><mi>a</mi><mo>,</mo><mn>8</mn><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8801;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>,</p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>=</mo><mn>4</mn><mi>m</mi><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>m</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;</mo><mtext>or&#160;</mtext><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p>So equation of tangent are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mn>1</mn><mo>&#160;</mo><mtext>or&#160;</mtext><mi>y</mi><mo>=</mo><mfrac><mi>x</mi><mn>4</mn></mfrac><mo>+</mo><mn>2</mn></math></p><p>But <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></math> passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> so rejected as given in the question.</p><p>Now equation of normal at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>2</mn><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mfenced><mrow><mo>-</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mfenced><mrow><mo>-</mo><mn>4</mn></mrow></mfenced><mn>3</mn></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as&#160;slope&#160;of&#160;normal&#160;=</mtext><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>4</mn></mfrac></mstyle></mfrac><mtext>=-4</mtext></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>+</mo><mn>32</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>+</mo><mn>4</mn><mi>x</mi><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>x</mi><mn>9</mn></mfrac><mo>+</mo><mfrac><mi>y</mi><mn>36</mn></mfrac><mo>=</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>9</mn><mo>,</mo><mi>&#946;</mi><mo>=</mo><mn>36</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>45</mn></math></p></blockquote>

</details>

---

### Q24. JEE Main 2022 (26 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of distinct real roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>5</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>x</mi><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>5</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>x</mi><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Now on rearranging we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>8</mn></msup><mo>-</mo><msup><mi>x</mi><mn>7</mn></msup><mo>-</mo><msup><mi>x</mi><mn>6</mn></msup><mo>+</mo><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>7</mn></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><msup><mi>x</mi><mn>5</mn></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mi>x</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>7</mn></msup><mo>-</mo><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>5</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>From above equation it is clearly visible that the root are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn></math> and for <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>5</mn><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>, hence it is monotonic in nature so it will have only one root other than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn></math>.</p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> real distinct roots.</p></blockquote>

</details>

---

### Q25. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The number of real solutions of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup><mo>+</mo><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> is equal to _____.

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>7</mn></msup><mo>+</mo><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p>For number of real solutions, we need to find the number of times the curve cuts <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis.</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>7</mn><msup><mi>x</mi><mn>6</mn></msup><mo>+</mo><mn>15</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is strictly increasing function</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bd513ca9-fee3-4c44-ae27-2ff211ea575e-image.png" style="width: 100px; height: 95px;" /></p><p>i.e. when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mi>y</mi><mo>&#8594;</mo><mo>-</mo><mo>&#8734;</mo></math> and when  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo><mo>,</mo><mi>y</mi><mo>&#8594;</mo><mo>&#8734;</mo></math></p><p>So, the curve will cut <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis only once.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> number of real solution will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></p>

</details>

---

### Q26. JEE Main 2022 (27 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

If the sum of all the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>11</mn><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>45</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mfrac><mn>81</mn><mn>2</mn></mfrac><mo>=</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mi>P</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **45**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>11</mn><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mfrac><mn>45</mn><msup><mi>e</mi><mi>x</mi></msup></mfrac><mo>+</mo><mfrac><mn>81</mn><mn>2</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>11</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mfrac><mn>81</mn><mn>2</mn></mfrac><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>45</mn><mo>=</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>t</mi></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>3</mn></msup><mo>-</mo><mn>11</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>81</mn><mn>2</mn></mfrac><mi>t</mi><mo>-</mo><mn>45</mn><mo>=</mo><mn>0</mn></math></p><p>Product of roots <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>t</mi><mn>1</mn></msub><msub><mi>t</mi><mn>2</mn></msub><msub><mi>t</mi><mn>3</mn></msub><mo>=</mo><mn>45</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><msub><mi>x</mi><mn>1</mn></msub></msup><mo>&#215;</mo><msup><mi>e</mi><msub><mi>x</mi><mn>2</mn></msub></msup><mo>&#215;</mo><msup><mi>e</mi><msub><mi>x</mi><mn>3</mn></msub></msup><mo>=</mo><mn>45</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub></mrow></msup><mo>=</mo><mn>45</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><msub><mi>log</mi><mn>2</mn></msub><mn>45</mn></math>  </p><p>Given sum of root <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>ln</mi><mfenced close="|" open="|"><mi>P</mi></mfenced></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mn>45</mn></math></p>

</details>

---

### Q27. JEE Main 2022 (27 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of distinct real roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p>So the extrema of the function is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p>Plotting the graph we get </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5737abf4-b453-48bf-9c52-7d113db354b0-image.png" style="width: 239px; height: 170px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup><mo>&#160;&#160;</mo><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>&#62;</mo><mn>0</mn></math> </p><p>And at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mo>&#60;</mo><mn>0</mn></math></p><p>So, graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> will cut x-axis at two points,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Number of real roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></p>

</details>

---

### Q28. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><mn>4</mn><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>10</mn><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math> is the range of the function, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>a</mi><mo>-</mo><mi>b</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>-</mo><mi>&#960;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>+</mo><mi>&#960;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>-</mo><mi>&#960;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>-</mo><mi>&#960;</mi></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><mn>4</mn><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac><mo>-</mo><mfrac><mn>4</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>2</mn><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is a decreasing function</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>&#960;</mi><mo>+</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>5</mn><mi>&#960;</mi><mo>+</mo><mn>5</mn></math></p><p>So, range: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8801;</mo><mfenced close="]" open="["><mrow><mi>&#960;</mi><mo>+</mo><mn>5</mn><mo>,</mo><mn>5</mn><mi>&#960;</mi><mo>+</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>&#960;</mi><mo>+</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>5</mn><mi>&#960;</mi><mo>+</mo><mn>5</mn><mo>&#8658;</mo><mn>4</mn><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mn>11</mn><mo>-</mo><mi>&#960;</mi></math></p>

</details>

---

### Q29. JEE Main 2022 (25 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="bold-italic">R</mi><mo>&#8594;</mo><mi mathvariant="bold-italic">R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi mathvariant="bold-italic">R</mi><mo>&#8594;</mo><mi mathvariant="bold-italic">R</mi></math> be two functions defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi mathvariant="normal">e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow><msup><mi mathvariant="normal">e</mi><mi>x</mi></msup></mfrac><mo>&#183;</mo></math> Then, for which of the following range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math>, the inequality <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mfrac><msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mn>3</mn></mfrac></mfenced></mrow></mfenced><mo>&#62;</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></mrow></mfenced></mrow></mfenced></math> holds?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>&#62;</mo><mn>0</mn><mo>,</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> increasing</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>-</mo><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mo>&#60;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> decreasing</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> is decreasing</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mfrac><mrow><mo>(</mo><mi>&#945;</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>3</mn></mfrac></mfenced></mrow></mfenced><mo>&#62;</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mn>3</mn></mfrac><mo>&#60;</mo><mi>&#945;</mi><mo>-</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#60;</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mi>&#945;</mi><mo>&#8712;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p>

</details>

---

### Q30. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#955;</mi><mo>*</mo></msup></math> be the largest value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> for which the function <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>&#955;</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><mi>&#955;</mi><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>36</mn><mi>&#955;</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>36</mn><mi>x</mi><mo>+</mo><mn>48</mn></math> is increasing for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><msup><mi>&#955;</mi><mo>*</mo></msup></msub><mfenced><mn>1</mn></mfenced><mo>+</mo><msub><mi>f</mi><mrow><mi>&#955;</mi><mo>,</mo><mo>*</mo></mrow></msub><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>&#955;</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><mi>&#955;</mi><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>36</mn><mi>&#955;</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>36</mn><mi>x</mi><mo>+</mo><mn>48</mn></math></p><p>Differentiating w.r.t <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>f</mi><mi>&#955;</mi><mo>&#39;</mo></msubsup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>12</mn><mi>&#955;</mi><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>72</mn><mi>&#955;</mi><mi>x</mi><mo>+</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>&#955;</mi></msub><mmultiscripts><mfenced><mi>x</mi></mfenced><mprescripts></mprescripts><none></none><mo>&#39;</mo></mmultiscripts><mo>=</mo><mn>12</mn><mfenced><mrow><mi>&#955;</mi><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>&#955;</mi><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#955;</mi><mo>&#62;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>&#215;</mo><mi>&#955;</mi><mo>&#215;</mo><mn>3</mn><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>&#955;</mi><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>&#955;</mi><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><msub><mi>&#955;</mi><mrow><mi>largest</mi><mo>&#160;</mo></mrow></msub><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>36</mn><mi>x</mi><mo>+</mo><mn>48</mn></math></p><p>So,<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>72</mn></math></p>

</details>

---

### Q31. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The number of distinct real roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup><mo>-</mo><mn>7</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup><mo>-</mo><mn>7</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup><mo>-</mo><mn>7</mn><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p>Now taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>7</mn></msup><mo>-</mo><mn>7</mn><mi>x</mi></math> (odd) &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn></math></p><p>Now differentiating <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> w.r.t <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>7</mn><mfenced><mrow><msup><mi>x</mi><mn>6</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>7</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn></math></p><p>So points of extrema are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#8201;</mo><mn>1</mn><mo>&#160;</mo></math>, Now plotting the graph to check number of solution we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e7b14698-bfab-4203-9c80-0186178ab58f-image.png" style="width: 230px; height: 142px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> real distinct solution.</p>

</details>

---

### Q32. JEE Main 2022 (24 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>,</mo><mi>x</mi><mo>&#62;</mo><mn>1</mn></math>, which one of the following is NOT correct?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math>  and decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math> has exactly two solutions
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi mathvariant="normal">e</mi></mfenced><mo>-</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mn>2</mn></mfenced><mo>&#60;</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> has a root in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>e</mi><mo>,</mo><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi mathvariant="normal">e</mi></mfenced><mo>-</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mn>2</mn></mfenced><mo>&#60;</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>,</mo><mi>x</mi><mo>&#62;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>4</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mn>4</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>2</mn><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>0</mn></math>  </p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> has a maxima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math> has two solution as the curve of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> will cut it at exactly two points.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>e</mi></mfenced><mo>&#62;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>e</mi></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math>  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>e</mi></mfenced><mo>-</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mn>4</mn><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mn>4</mn><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>8</mn><mo>&#62;</mo><mn>0</mn></math></p>

</details>

---

### Q33. JEE Main 2021 (01 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>The function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></math> is such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>0</mn></math>. </p><p>Consider two statements:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>S</mi><mn>1</mn></msub></mfenced></math> there exists <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#8712;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>&#60;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><msub><mi>x</mi><mn>1</mn></msub></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><msub><mi>x</mi><mn>2</mn></msub></mfenced><mo>=</mo><mn>0</mn><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>S</mi><mn>2</mn></msub></mfenced></math> there exists <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>3</mn></msub><mo>,</mo><msub><mi>x</mi><mn>4</mn></msub><mo>&#8712;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>3</mn></msub><mo>&#60;</mo><msub><mi>x</mi><mn>4</mn></msub></math>, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><msub><mi>x</mi><mn>4</mn></msub></mrow></mfenced></math>, increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>4</mn></msub><mo>,</mo><mn>4</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>f</mi><mo>'</mo></msup><mfenced><msub><mi>x</mi><mn>3</mn></msub></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt><mi>f</mi><mfenced><msub><mi>x</mi><mn>4</mn></msub></mfenced></math> then</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>S</mi><mn>1</mn></msub></mfenced></math> is true and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>S</mi><mn>2</mn></msub></mfenced></math> is false
- **(B)** both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>S</mi><mn>1</mn></msub></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>S</mi><mn>2</mn></msub></mfenced></math> are false
- **(C)** both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>S</mi><mn>1</mn></msub></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>S</mi><mn>2</mn></msub></mfenced></math> are true
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>S</mi><mn>1</mn></msub></mfenced></math> is false and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>S</mi><mn>2</mn></msub></mfenced></math> is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>S</mi><mn>1</mn></msub></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>S</mi><mn>2</mn></msub></mfenced></math> are true**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></math></p><p>Given that:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>16</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>4</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>32</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Solving both equations, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>8</mn></math></p><p>Now,</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>8</mn><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>9</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>&#8712;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>, therefore <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn></math>.</p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mn>12</mn><mo>&#177;</mo><msqrt><mn>144</mn><mo>-</mo><mn>96</mn></msqrt></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mn>12</mn><mo>&#177;</mo><msqrt><mn>48</mn></msqrt></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mn>12</mn><mo>&#177;</mo><mn>4</mn><msqrt><mn>3</mn></msqrt></mrow><mn>6</mn></mfrac><mo>=</mo><mfrac><mrow><mn>6</mn><mo>&#177;</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>2</mn><mo>+</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>-</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac></math></p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>&#8712;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mo>+</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math> is true.</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p>Sign scheme for <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced></math> is as follows:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/80b7c906-dd03-4684-b675-ae46c997f652-image.png" style="width: 330px; height: 91px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>2</mn><mo>-</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>, hence it is increasing.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac><mo>,</mo><mn>2</mn><mo>+</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac></mrow></mfenced></math>, hence it is decreasing.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>4</mn></msub><mo>=</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac></mrow></mfenced></math>.</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>f</mi><mo>'</mo></msup><mfenced><msub><mi>x</mi><mn>3</mn></msub></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt><mi>f</mi><mfenced><msub><mi>x</mi><mn>4</mn></msub></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced open="[" close="]"><mrow><mn>3</mn><msubsup><mi>x</mi><mn>3</mn><mn>2</mn></msubsup><mo>-</mo><mn>12</mn><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><mn>8</mn></mrow></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced open="[" close="]"><mrow><mn>3</mn><msubsup><mi>x</mi><mn>3</mn><mn>2</mn></msubsup><mo>-</mo><mn>12</mn><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><mn>8</mn></mrow></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt><mfenced><mrow><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac></mfenced><mfenced><mrow><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced close="]" open="["><mrow><mn>3</mn><msubsup><mi>x</mi><mn>3</mn><mn>2</mn></msubsup><mo>-</mo><mn>12</mn><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><mn>8</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mfrac><mn>12</mn><mn>9</mn></mfrac><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mrow><mn>3</mn><msubsup><mi>x</mi><mn>3</mn><mn>2</mn></msubsup><mo>-</mo><mn>12</mn><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><mn>8</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><msubsup><mi>x</mi><mn>3</mn><mn>2</mn></msubsup><mo>-</mo><mn>36</mn><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><mn>32</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><mfrac><mrow><mn>36</mn><mo>&#177;</mo><msqrt><mn>1296</mn><mo>-</mo><mn>1152</mn></msqrt></mrow><mn>18</mn></mfrac><mo>=</mo><mfrac><mrow><mn>36</mn><mo>&#177;</mo><mn>12</mn></mrow><mn>18</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> is true.</p>

</details>

---

### Q34. JEE Main 2021 (31 Aug Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is the least value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> such that the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi mathvariant="normal">a</mi><mi>x</mi><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mn>1</mn></math> is increasing on <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>]</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is the greatest value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> such that the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi>a</mi><mi>x</mi><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mn>1</mn></math> is decreasing on <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>]</mo></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>R</mi><mo>-</mo><mi>S</mi><mo>|</mo></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>a</mi><mo>&#8805;</mo><mn>0</mn><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>]</mo><mo>&#160;&#160;</mo><mo>&#8658;</mo><mi>a</mi><mo>&#8805;</mo><mo>-</mo><mn>2</mn><mi>x</mi><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>]</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>min</mi></msub><mo>=</mo><mi>R</mi><mo>=</mo><mo>-</mo><mn>2</mn></math> If</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow></msub><mo>=</mo><mi>S</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>R</mi><mo>-</mo><mi>S</mi><mo>|</mo><mo>=</mo><mn>2</mn></math></p><p>Alternate :</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is increasing for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>]</mo></math> then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>a</mi><mn>2</mn></mfrac><mo>&#8804;</mo><mn>1</mn><mo>&#8658;</mo><mi>a</mi><mo>&#8805;</mo><mo>-</mo><mn>2</mn><mo>&#8658;</mo><mi>R</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is decreasing for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>]</mo><mo>,</mo></math> then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>a</mi><mn>2</mn></mfrac><mo>&#8805;</mo><mn>2</mn><mo>&#8658;</mo><mi>a</mi><mo>&#8804;</mo><mo>-</mo><mn>4</mn><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0e282258-d950-4c75-958d-7629eeae1114-image.png" style="width: 249px; height: 182px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>R</mi><mo>-</mo><mi>S</mi><mo>|</mo><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q35. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of real roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;&#160;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>t</mi></math>,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><msup><mi>t</mi><mn>4</mn></msup><mo>+</mo><mn>2</mn><msup><mi>t</mi><mn>3</mn></msup><mo>-</mo><mi>t</mi><mo>-</mo><mn>6</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mn>4</mn><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>6</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mn>12</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>12</mn><mi>t</mi><mo>&#62;</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>t</mi><mo>&#62;</mo><mn>0</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mo>(</mo><mi>t</mi><mo>)</mo></math> is increasing function</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>9</mn></math></p><p>By using Intermediate value theorem there exists a root for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn><mo>&#160;</mo></math>if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><mi>f</mi><mfenced><mi>&#946;</mi></mfenced><mo>&#60;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>&#947;</mi></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mo>&#8712;</mo><mo>&#160;</mo><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></mrow></mfenced></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>&#946;</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4a7c405e-2cb3-4de0-8299-bf8a15814ebb-image.png" style="width: 319px; height: 269px;" /></p><p>Hence, only one real root.</p>

</details>

---

### Q36. JEE Main 2021 (27 Aug Shift 1)

*Type:* `numerical` | *Level:* `3`

The number of distinct real roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> is _________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p>So, </p><p>let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>12</mn><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>12</mn><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/666a8fd3-40fe-4a99-8fb4-bcf98ca8bdf2-10.JPG" style="width: 250px; height: 68px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/085c3688-d84d-4afe-a181-b6b52a23b017-11.JPG" style="width: 250px; height: 249px;" /></p><p>Ans. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></p>

</details>

---

### Q37. JEE Main 2021 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of real roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>6</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>2</mn><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>12</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>6</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>2</mn><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>12</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mn>12</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>12</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mo>=</mo><mn>12</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mfenced><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mfrac><mo>=</mo><mfrac><mn>12</mn><mfenced><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mo>=</mo><mfrac><mn>12</mn><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p>Assume, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>12</mn><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></math></p><p>Clearly, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>&#62;</mo><mn>0</mn><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></mrow></mfenced></math></p><p>So, here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is increasing and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math>and clearly <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is decreasing function because it is reciprocal function.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f5ab4ba4-3785-4dca-a82f-ef437ef94471-image.png" style="width: 247px; height: 240px;" /></p><p>From the graph, we can say that number of real roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q38. JEE Main 2021 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><mn>10</mn><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mn>6</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>3</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is :

**Options:**

- **(A)** increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>
- **(B)** decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>
- **(C)** increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced></math>
- **(D)** decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><mn>10</mn><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mn>6</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>12</mn><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mn>30</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mn>12</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi><mfenced><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>5</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi><mo>(</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0ae292b8-5c6d-4ab7-983a-c6390c112307-image.png" style="width: 283px; height: 98px;" /></p><p>From wavy curve, we can say <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#60;</mo><mn>0</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>So, the function is Decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced></math></p>

</details>

---

### Q39. JEE Main 2021 (22 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mrow><mtable><mtr><mtd><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>3</mn><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>,</mo></mtd><mtd><mo>&#160;&#160;</mo><mi>x</mi><mo>&#8804;</mo><mn>0</mn></mtd></mtr></mtable><mo>.</mo></mrow></mfenced></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is increasing function in the interval</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><msup><mi>x</mi><mi>n</mi></msup></mfenced><mo>=</mo><mi>n</mi><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><msup><mi>e</mi><mi>x</mi></msup></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mrow><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#215;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>=</mo><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></math></p><p>And, using product rule, we get<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mrow><mn>3</mn><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mo>=</mo><mn>3</mn><mi>x</mi><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><msup><mi>e</mi><mi>x</mi></msup></mfenced><mo>+</mo><mn>3</mn><msup><mi>e</mi><mi>x</mi></msup><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>3</mn><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mn>3</mn><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="right left"><mtr><mtd><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn><msup><mi>e</mi><mi>x</mi></msup><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8804;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>=</mo><mo>-</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p>The sign scheme of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math> is</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8fd6e4d4-1a95-441d-b595-ee07edd8cb03-WhatsAppImage2021-12-10at2.16.02PM.jpeg" style="width: 300px; height: 133px;" /></p><p>We know that, if <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math> then for those value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is increasing.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced><mo>.</mo></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8804;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>3</mn><msup><mi>e</mi><mi>x</mi></msup><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>&#62;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>)</mo><mo>.</mo></math></p><p>So, in complete domain, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced><mo>.</mo></math></p></blockquote>

</details>

---

### Q40. JEE Main 2021 (17 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mrow><mtable columnalign="left left"><mtr><mtd><mfenced><mrow><mn>2</mn><mo>-</mo><mi>sin</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></mrow></mfenced><mo>|</mo><mi>x</mi><mo>|</mo><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8800;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable><mo>.</mo></mrow></mfenced></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is:

**Options:**

- **(A)** monotonic on <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>0</mn><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(B)** not monotonic on <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>0</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(C)** monotonic on <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math> only
- **(D)** monotonic on <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>0</mn><mo>)</mo></math> only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) not monotonic on <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>0</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left left"><mtr><mtd><mfenced><mrow><mn>2</mn><mo>-</mo><mi>sin</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></mrow></mfenced><mo>|</mo><mi>x</mi><mo>|</mo><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8800;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> and we know that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left" columnspacing="1.4ex"><mtr><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left left"><mtr><mtd><mo>-</mo><mi>x</mi><mfenced><mrow><mn>2</mn><mo>-</mo><mi>sin</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></mrow></mfenced><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>x</mi><mfenced><mrow><mn>2</mn><mo>-</mo><mi>sin</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></mrow></mfenced><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>Now, differentiating using product rule,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left" columnspacing="1.4ex"><mtr><mtd><mo>-</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mi>sin</mi><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac></mrow></mfenced><mo>-</mo><mi mathvariant="normal">x</mi><mfenced><mrow><mo>-</mo><mi>cos</mi><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac><mo>&#183;</mo><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mfrac></mrow></mfenced></mrow></mfenced><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mi>sin</mi><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac></mrow></mfenced><mo>+</mo><mi mathvariant="normal">x</mi><mfenced><mrow><mo>-</mo><mi>cos</mi><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mfrac></mrow></mfenced></mrow></mfenced><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left" columnspacing="1.4ex"><mtr><mtd><mo>-</mo><mn>2</mn><mo>+</mo><mi>sin</mi><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>cos</mi><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>2</mn><mo>-</mo><mi>sin</mi><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>cos</mi><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo></math> is an oscillating function and hence it is non-monotonic in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>0</mn><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo><mo>.</mo></math></p>

</details>

---

### Q41. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> be a real valued function, defined on<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> and given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced close="|" open="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>-</mo><mfrac><mn>2</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math>. Then in which of the following intervals, function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is increasing?</p>

**Options:**

- **(A)** <p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfenced open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mn>1</mn></mfenced></mrow></mfenced></math></p>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfenced open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mn>1</mn></mfenced></mrow></mfenced></math></p>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>3</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfrac><mn>2</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>3</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mn>3</mn><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfenced open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mn>1</mn></mfenced></mrow></mfenced></math></p>

</details>

---

### Q42. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi>R</mi></math> for which the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mn>4</mn><mi>a</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>5</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mi>cot</mi><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mo>,</mo><mi>x</mi><mo>&#8800;</mo><mn>2</mn><mi>n</mi><mi>&#960;</mi><mo>,</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math>, has critical points, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>,</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>1</mn><mo>]</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>,</mo><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mn>4</mn><mi>a</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>5</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mi>cot</mi><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mo>,</mo><mi>x</mi><mo>&#8800;</mo><mn>2</mn><mi>n</mi><mi>&#960;</mi><mo>,</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mn>4</mn><mi>a</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>5</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mi>sin</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mn>4</mn><mi>a</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mn>1</mn></mfenced><mo>+</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mi>cos</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mn>4</mn><mi>a</mi></mrow><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mn>4</mn><mi>a</mi></mrow><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mo>-</mo><mn>4</mn><mi>a</mi></mrow><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfrac><mo>+</mo><mn>1</mn><mo>&#8805;</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mn>4</mn><mi>a</mi></mrow><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mo>-</mo><mn>4</mn><mi>a</mi><mo>+</mo><mi>a</mi><mo>-</mo><mn>7</mn></mrow><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfrac><mo>&#8805;</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mn>4</mn><mi>a</mi></mrow><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfrac><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>3</mn><mi>a</mi><mo>-</mo><mn>4</mn></mrow><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfrac><mo>&#8805;</mo><mn>0</mn><mo>&#160;&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mn>4</mn><mi>a</mi><mo>-</mo><mi>a</mi><mo>+</mo><mn>7</mn></mrow><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfrac><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>a</mi><mo>+</mo><mn>4</mn></mrow><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfrac><mo>&#8804;</mo><mn>0</mn><mo>&#160;&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mn>5</mn><mi>a</mi><mo>+</mo><mn>10</mn></mrow><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfrac><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>a</mi><mo>+</mo><mn>4</mn></mrow><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfrac><mo>&#8804;</mo><mn>0</mn><mo>&#160;&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mrow><mn>5</mn><mi>a</mi><mo>-</mo><mn>10</mn></mrow><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfrac><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>a</mi><mo>+</mo><mn>4</mn></mrow><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfrac><mo>&#8804;</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mrow><mn>5</mn><mfenced><mrow><mi>a</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfrac><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mfenced open="["><mrow><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>,</mo><mn>7</mn></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>2</mn><mo>]</mo><mo>&#8746;</mo><mo>(</mo><mn>7</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>,</mo><mn>2</mn></mrow></mfenced></math></p>

</details>

---

### Q43. JEE Main 2021 (26 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> be an integer such that all the real roots of the polynomial <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>5</mn><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>10</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>10</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>10</mn></math> lie in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>a</mi><mo>|</mo></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>5</mn><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>10</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>10</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>10</mn><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>34</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>3</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> has a root in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Further <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>10</mn><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>20</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>30</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>20</mn><mi>x</mi><mo>+</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>+</mo><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><msup><mi>x</mi><mn>2</mn></msup><mfenced close="]" open="["><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><msup><mi>x</mi><mn>2</mn></msup><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>+</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><msup><mi>x</mi><mn>2</mn></msup><mfenced close="]" open="["><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfenced><mo>&#62;</mo><mn>0</mn></math>  for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> belongs to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is strictly increasing function. Since it is an odd degree polynomial it will have exactly one real root.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> has only one real root, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>a</mi></mfenced><mo>=</mo><mn>2</mn></math>.</p>

</details>

---

### Q44. JEE Main 2021 (24 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be defined as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mo>-</mo><mn>55</mn><mi>x</mi><mo>,</mo></mtd><mtd><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>120</mn><mi>x</mi><mo>,</mo></mtd><mtd><mi>if</mi><mo>-</mo><mn>5</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>36</mn><mi>x</mi><mo>-</mo><mn>336</mn><mo>,</mo></mtd><mtd><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>:</mo><mi>f</mi></math> is increasing}. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is equal to:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>5</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>4</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>5</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>5</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>4</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mo>&#8734;</mo></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mo>-</mo><mn>55</mn><mi>x</mi><mo>,</mo></mtd><mtd><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>120</mn><mi>x</mi><mo>,</mo></mtd><mtd><mi>if</mi><mo>-</mo><mn>5</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>36</mn><mi>x</mi><mo>-</mo><mn>336</mn><mo>,</mo></mtd><mtd><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mo>-</mo><mn>55</mn><mo>,</mo></mtd><mtd><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>120</mn><mo>,</mo></mtd><mtd><mi>if</mi><mo>-</mo><mn>5</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>36</mn><mo>,</mo></mtd><mtd><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mo>-</mo><mn>55</mn><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>6</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>;</mo></mtd><mtd><mo>-</mo><mn>5</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>6</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is increasing</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>5</mn><mo>,</mo><mo>-</mo><mn>4</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p>

</details>

---

### Q45. JEE Main 2021 (24 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

The minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> for which the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>&#945;</mi></math> has at least one solution in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math> is______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>4</mn><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>4</mn><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><mi>cosec</mi><mi>x</mi><mo>+</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>tan</mi><mi>x</mi><mi>sec</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mrow><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mrow><mo>'</mo><mo>'</mo></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>4</mn><mfenced open="[" close="]"><mfrac><mrow><mo>-</mo><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac></mfenced><mo>+</mo><mfrac><mrow><mn>2</mn><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><mn>3</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mi>sin</mi><mi>x</mi><msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow><mrow><msup><mi>cos</mi><mn>6</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mrow><mo>'</mo><mo>'</mo></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>4</mn><mfenced open="[" close="]"><mfrac><mrow><mo>-</mo><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac></mfenced><mo>+</mo><mfrac><mrow><mn>2</mn><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mi>sin</mi><mi>x</mi><msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mn>3</mn></msup></mfrac></math></p><p>For critical points,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mrow><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>x</mi><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mn>2</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>3</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Now, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mrow><mo>'</mo><mo>'</mo></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>4</mn><mfenced open="[" close="]"><mfrac><mrow><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>8</mn><mn>27</mn></mfrac></mstyle><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>3</mn></mfrac></mstyle><mfenced><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>9</mn></mfrac></mstyle></mrow></mfenced></mrow><mstyle displaystyle="true"><mfrac><mn>16</mn><mn>81</mn></mfrac></mstyle></mfrac></mfenced><mo>+</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>3</mn></mfrac></mstyle><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>9</mn></mfrac></mstyle></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>9</mn></mfrac></mstyle></mrow></mfenced><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mn>2</mn><mn>3</mn></mfrac></mstyle><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mn>25</mn><mn>9</mn></mfrac></mstyle></mrow><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>9</mn></mfrac></mstyle></mrow></mfenced><mn>3</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mrow><mo>'</mo><mo>'</mo></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="[" close="]"><mrow><mn>4</mn><mfenced open="[" close="]"><mrow><mfrac><mn>28</mn><mn>27</mn></mfrac><mo>&#215;</mo><mfrac><mn>81</mn><mn>16</mn></mfrac></mrow></mfenced><mo>+</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>3</mn></mfrac></mstyle><msup><mfenced><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>9</mn></mfrac></mstyle></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mfenced><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>9</mn></mfrac></mstyle></mfenced><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mn>2</mn><mn>3</mn></mfrac></mstyle><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mn>25</mn><mn>9</mn></mfrac></mstyle></mrow><msup><mfenced><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>9</mn></mfrac></mstyle></mfenced><mn>3</mn></msup></mfrac></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p>Hence, it is the point of minima.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>f</mi><msub><mfenced><mi>x</mi></mfenced><mi>min</mi></msub><mo>=</mo><mfrac><mn>4</mn><mstyle displaystyle="true"><mfrac><mn>2</mn><mn>3</mn></mfrac></mstyle></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>2</mn><mn>3</mn></mfrac></mstyle></mrow></mfrac><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><msub><mfenced><mi>x</mi></mfenced><mi>max</mi></msub><mo>&#8594;</mo><mo>&#8734;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous function</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msub><mi>&#945;</mi><mi>min</mi></msub><mo>=</mo><mn>9</mn></math></p>

</details>

---

### Q46. JEE Main 2021 (24 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>6</mn></mfrac><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>cos</mi><mi>x</mi></math>:

**Options:**

- **(A)** increases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(B)** decreases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(C)** decreases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(D)** increases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) increases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>6</mn></mfrac><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>cos</mi><mi>x</mi></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mi>cos</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></math></p><p>for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#60;</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi><mo>&#60;</mo><mn>0</mn></math></p><p>for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>,</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>0</mn></math></p><p>for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> increases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p>

</details>

---

### Q47. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> is a critical point of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>x</mi><mo>-</mo><mn>2</mn><mo>-</mo><mi>a</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup><mo>,</mo></math> then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math> are local minima of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> and<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math> is a local maxima of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> is a local maxima and<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>2</mn></mfrac></math> is a local minima of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> is a local minima and<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math> are local maxima of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> is a local minima and<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math> are local maxima of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>x</mi><mo>-</mo><mn>2</mn><mo>-</mo><mi>a</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>x</mi><mo>-</mo><mn>2</mn><mo>-</mo><mi>a</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup><mo>(</mo><mn>6</mn><mi>x</mi><mo>+</mo><mi>a</mi><mo>)</mo><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>(</mo><mi>a</mi><mo>+</mo><mn>6</mn><mo>)</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>=</mo><mn>1</mn></math> is a critical point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;&#160;</mo><mo>&#8756;</mo><mo>&#160;&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mn>3</mn><mo>+</mo><mi>a</mi><mo>+</mo><mn>6</mn><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>(</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> maxima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>&#160;</mo></mrow><mn>3</mn></mfrac><mo>&#8756;</mo></math> minima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q48. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Suppose <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is a polynomial of degree four having critical points at <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>&#160;</mo><mo>|</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></mrow></mfenced></math>, then the sum of squares of all the elements of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>k</mi><mo>.</mo><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>k</mi><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced></math></p><p>Integrating both sides with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>k</mi><mo>&#160;</mo><mfenced><mrow><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mfrac><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>4</mn></mfrac><mo>+</mo><mi>c</mi><mo>=</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mo>&#160;</mo><mo>-</mo><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>T</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mo>&#160;</mo><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced></math></p><p>Thus, sum of squares of all the elements of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>0</mn></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn></math>.</p>

</details>

---

### Q49. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The function, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced><msup><mi>x</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">R</mi></math>, is increasing for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> lying in

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfrac><mn>14</mn><mn>15</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfrac><mn>3</mn><mn>7</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>14</mn><mn>15</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mn>14</mn><mn>15</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfrac><mn>14</mn><mn>15</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced><msup><mi>x</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is increasing <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math>.</p><p>Differentiate <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>x</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup><mo>+</mo><mfenced><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mfrac><mn>2</mn><mrow><mn>3</mn><msup><mi>x</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>9</mn><mi>x</mi><mo>+</mo><mn>2</mn><mfenced><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced></mrow><mrow><mn>3</mn><msup><mi>x</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>15</mn><mi>x</mi><mo>-</mo><mn>14</mn></mrow><mrow><mn>3</mn><msup><mi>x</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></msup></mrow></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mfrac><mrow><mn>15</mn><mi>x</mi><mo>-</mo><mn>14</mn></mrow><mrow><mn>3</mn><msup><mi>x</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></msup></mrow></mfrac><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfrac><mn>14</mn><mn>15</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>&#8734;</mo></mrow></mfenced></math></p>

</details>

---

### Q50. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn></math>. Then the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math>

**Options:**

- **(A)** Decreases in<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> and increases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(B)** Increases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(C)** Increases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> and decreases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(D)** Decreases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Decreases in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mfrac><mi>x</mi><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>-</mo><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>-</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mo>&#62;</mo><mn>0</mn></mtd><mtd><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mo>&#60;</mo><mn>0</mn></mtd><mtd><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>g</mi><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow></msub></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>g</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math> is the maximum value</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>0</mn><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>&#160;&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>0</mn><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is decreasing <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p>

</details>

---

### Q51. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow></mrow></mfenced><mo>,</mo><mi></mi><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>,</mo></mrow></mrow></math> then which of the following is true?

**Options:**

- **(A)** <math><mi>f</mi><mi>'</mi></math> is increasing in <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi></mi><mn>0</mn></mrow></mfenced></math> and decreasing in <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
- **(B)** <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mi>f</mi></math> is not differentiable at <math><mi>x</mi><mo>=</mo><mn>0</mn></math>
- **(D)** <math><mi>f</mi><mi>'</mi></math> is decreasing in <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi></mi><mn>0</mn></mrow></mfenced></math> and increasing in <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi>f</mi><mi>'</mi></math> is decreasing in <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi></mi><mn>0</mn></mrow></mfenced></math> and increasing in <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mfenced separators="|"><mrow><mi>&#960;</mi><mo>-</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi><mo>(</mo><mi>&#960;</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></math>
<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mi>x</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>x</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>
<math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mn>2</mn><mi>x</mi></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mn>2</mn><mi>x</mi></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>
<math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is increasing in <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mo>&#8201;</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> and decreasing in <math><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mo>&#8201;</mo><mn>0</mn></mrow></mfenced></math>.

</details>

---

### Q52. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the function <math><mi>f</mi></math> given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mn>2</mn></mrow></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>a</mi><mi>x</mi><mo>+</mo><mn>7</mn></math>, for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi>R</mi></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math> and decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>5</mn></mrow></mfenced></math>, then a root of the equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>14</mn></mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mfenced><mrow><mi>x</mi><mo>&#8800;</mo><mn>1</mn></mrow></mfenced></math> is :

**Options:**

- **(A)** <math><mn>7</mn></math>
- **(B)** <math><mo>-</mo><mn>7</mn></math>
- **(C)** <math><mn>6</mn></math>
- **(D)** <math><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>7</mn></math>**

**Detailed Solution:**

At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><msup><mi>f</mi><mi>&#8242;</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>f</mi><mi>&#8242;</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mn>3</mn><mi>a</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>-</mo><mn>6</mn><mi>&#160;</mi><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mi>a</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>-</mo><mn>14</mn></mrow><msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>15</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow><msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>7</mn></math></p>

</details>

---

### Q53. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)=\frac{x}{\sqrt{a^{2}+x^{2}}}-\frac{d-x}{\sqrt{b^{2}+(d-x)^{2}}}, x \in \mathbb{R}$ wherea, b

and d are non-zero real constants. Then :

**Options:**

- **(A)** $f$ is an increasing function of $x$
- **(B)** $f$ is a decreasing function of $x$
- **(C)** $f^{\prime}$ is not a continuous function of $x$
- **(D)** $f$ is neither increasing nor decreasing function of $x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $f$ is an increasing function of $x$**

**Detailed Solution:**

$f(x)=\frac{x}{\sqrt{a^{2}+x^{2}}}-\frac{(d-x)}{\sqrt{b^{2}+(d-x)^{2}}}$

$=\frac{x}{\sqrt{a^{2}+x^{2}}}+\frac{(x-d)}{\sqrt{b^{2}+(x-d)^{2}}}$

$\begin{array}{l}

f^{\prime}(x)=\frac{\sqrt{a^{2}+x^{2}}-\frac{x(2 x)}{2 \sqrt{a^{2}+x^{2}}}}{\left(a^{2}+x^{2}\right)} \\

=\frac{a^{2}+x^{2}-x^{2}}{\left(a^{2}+x^{2}\right)^{3 / 2}}+\frac{b^{2}+(x-d)^{2}-(x-d)^{2}}{\left(b^{2}+(x-d)^{2}\right)^{3 / 2}} \\

+\frac{\sqrt{b^{2}+(x-d)^{2}}-\frac{(x-d) 2(x-d)}{2 \sqrt{b^{2}+(x-d)^{2}}}}{\left(a^{2}+(x-d)^{2}\right)} \\

\Rightarrow f^{\prime}(x)>0, \square x \in R

\end{array}$

$\Rightarrow f(x)$ is increasing function.

Hence, $f(x)$ is increasing function

</details>

---

### Q54. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The function <math><mi>f</mi></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>7</mn></math><msup><mrow><mi></mi></mrow><mrow><mn></mn></mrow></msup><mo></mo><mn></mn><msup><mrow><mi></mi></mrow><mrow><mn></mn></mrow></msup><mo></mo><mn></mn><mi></mi><mo></mo><mn></mn> is:

**Options:**

- **(A)** Decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>
- **(B)** Increasing in <b><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></b>
- **(C)** Increasing in  <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mi>∞</mi></mrow></mfenced></math>  and decreasing in  <math><mfenced separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mi> </mi><mn>0</mn></mrow></mfenced></math>
- **(D)** Decreasing in  <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mi>∞</mi></mrow></mfenced></math>  and increasing in  <math><mfenced separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mi> </mi><mn>0</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Increasing in <b><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></b>**

**Detailed Solution:**

<p>We have <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>7</mn></math>

<math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>&#62;</mo><mn>0&#160; &#160; &#160;&#160;</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>a</mi><mi>c</mi><mo>=</mo><mn>36</mn><mo>-</mo><mn>4</mn><mo>&#183;</mo><mn>3</mn><mo>&#183;</mo><mn>5</mn><mo>=</mo><mo>-</mo><mn>14</mn><mo>&#160;</mo><mfenced><mrow><mo>-</mo><mi>ve</mi></mrow></mfenced></math></p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn><mo>.</mo><mo>&#160;</mo></math>

Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>.</mo><mo>&#160;</mo></math></p>

</details>

---

### Q55. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Statement-1: The function $x^2\left(e^x+e^{-x}\right)$ is increasing for all $x>0$.
Statement-2: The functions $x^2 e^x$ and $x^2 e^{-x}$ are increasing for all $x>0$ and the sum of two increasing functions in any interval $(a, b)$ is an increasing function in $(a, b)$.

**Options:**

- **(A)** Statement-1 is false; Statement-2 is true.
- **(B)** Statement-1 is true; Statement-2 is true; Statement-2 is not a correct explanation for Statement-1.
- **(C)** Statement-1 is true; Statement-2 is false.
- **(D)** Statement-1is true; Statement-2 is true; Statement-2 is a correct explanation for statement-1.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Statement-1 is true; Statement-2 is false.**

**Detailed Solution:**

Let $y=x^2 \cdot e^{-x}$
For increasing function,
$$
\begin{aligned}
& \frac{d y}{d x}>0 \Rightarrow x\left[(2-x) e^{-x}\right]>0 \\
& \because x>0, \therefore(2-x) e^{-x}>0 \\
& \Rightarrow(2-x) \frac{1}{e^x}>0 \\
& \text { For } 0 < x < 2,(2-x) < 0 \\
& \therefore \frac{1}{e^x} < 0, \text { but it is not possible }
\end{aligned}
$$
Hence the statement- 2 is false.

</details>

---

### Q56. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Statement-1: The equation $x \log x=2-x$ is satisfied by at least one value of $x$ lying between 1 and 2.

Statement-2: The function $f(x)=x \log x$ is an increasing function in $[1,2]$ and $g(x)=2-x$ is a decreasing function in $[1,2]$ and the graphs represented by these functions intersect at a point in $[1,2]$

**Options:**

- **(A)** Statement-1 is true; Statement-2 is true; Statement-2 is a correct explanation for Statement-1.
- **(B)** Statement-1 is true; Statement-2 is true; Statement-2 is not correct explanation for Statement-1.
- **(C)** Statement-1 1 is false, Statement- 2 is true.
- **(D)** Statement-1 1 is true, Statement- 2 is false.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Statement-1 is true; Statement-2 is true; Statement-2 is a correct explanation for Statement-1.**

**Detailed Solution:**

$f(x)=x \log x, f(1)=0, f(2)=4$
$g(x)=2-x, g(1)=1, g(2)=0$
$\log 10>\log 4 \Rightarrow 1>\log 4$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/mbDRu3guMspmm-flZpFGmcp67jiB4pVdk8Rtg5tujiI.original.fullsize.png">

Thus statement $-1$ and 2 both are true and statement-2 is a correct explanation of statement 1 .

</details>

---

### Q57. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=x e^{x(1-x)}, x \in R$, then $f(x)$ is

**Options:**

- **(A)** decreasing on $[-1 / 2,1]$
- **(B)** decreasing on $R$
- **(C)** increasing on $[-1 / 2,1]$
- **(D)** increasing on $R$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) increasing on $[-1 / 2,1]$**

**Detailed Solution:**

$$
\begin{aligned}
& f(x)=x e^{x(1-x)}, x \in R \\
& f^{\prime}(x)=e^{x(1-x)} \cdot\left[1+x-2 x^2\right]
\end{aligned}
$$

$$
\begin{aligned}
& =-e^{x(1-x} \cdot\left[2 x^2-x-1\right] \\
& =-2 e^{x(1-x} \cdot\left[\left(x+\frac{1}{2}\right)(x-1]\right) \\
& f^{\prime}(x)=-2 e^{x(1-x)} A \\
& \text { where } A=\left(x+\frac{1}{2}\right)(x-1)
\end{aligned}
$$
Now, exponential function is always $+$ ve and $f^{\prime}(x)$ will be opposite to the sign of $A$
which is -ve in $\left[-\frac{1}{2}, 1\right]$
Hence, $f^{\prime}(x)$ is $+$ ve in $\left[-\frac{1}{2}, 1\right]$
$\therefore f(x)$ is increasing on $\left[-\frac{1}{2}, 1\right]$

</details>

---

### Q58. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `1`

The function $f(x)=\tan ^{-1}(\sin x+\cos x)$ is an increasing function in

**Options:**

- **(A)** $\left(\frac{\pi}{4}, \frac{\pi}{2}\right)$
- **(B)** $\left(-\frac{\pi}{2}, \frac{\pi}{4}\right)$
- **(C)** $\left(0, \frac{\pi}{2}\right)$
- **(D)** $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(-\frac{\pi}{2}, \frac{\pi}{4}\right)$**

**Detailed Solution:**

$f^{\prime}(x)=\frac{1}{1+(\sin x+\cos x)^2}(\cos x-\sin x)$
$=\frac{\sqrt{2} \cos \left(x+\frac{\pi}{4}\right)}{1+(\sin x+\cos x)^2}$
$f(x)$ is increasing if $-\frac{\pi}{2} < x+\frac{\pi}{4} < \frac{\pi}{2}$
$-\frac{3 \pi}{4} < x < \frac{\pi}{4}$
hence $f(x)$ is increasing when $x \in\left(-\frac{\pi}{2}, \frac{\pi}{4}\right)$.

</details>

---

### Q59. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

A function is matched below against an interval where it is supposed to be increasing. Which of the following pairs is incorrectly matched?
$Interval \rightarrow Function$

**Options:**

- **(A)** $(-\infty, \infty) \rightarrow x^3-3 x^2+3 x+3$
- **(B)** $[2, \infty) \rightarrow 2x^3-3 x^2-12 x+6$
- **(C)** $\left(-\infty, \frac{1}{3}\right] \rightarrow \quad 3 x^2-2 x+1$
- **(D)** $(-\infty, -4] \rightarrow x^3+6 x^2+6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(-\infty, \frac{1}{3}\right] \rightarrow \quad 3 x^2-2 x+1$**

**Detailed Solution:**

Clearly function $f(x)=3 x^2-2 x+1$ is increasing when $f^{\prime}(x)=6 x-2 \geq 0 \Rightarrow x \in[1 / 3, \infty)$
Hence $(C)$ is incorrect.

</details>

---

