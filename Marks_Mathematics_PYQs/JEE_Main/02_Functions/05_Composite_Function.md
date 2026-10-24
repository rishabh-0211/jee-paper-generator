# JEE Main Mathematics - Functions

## Topic 5: Composite Function

**Total Questions:** 26

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f:(1,\infty)\to\mathbb{R}$ be a function defined as $f(x) = \dfrac{x-1}{x+1}$. Let $f^{i+1}(x) = f(f^i(x))$, $i=1, 2, \ldots, 25$, where $f^1(x)=f(x)$. If $g(x) + f^{26}(x) = 0$, $x \in (1, \infty)$, then the area of the region bounded by the curves $y=g(x)$, $2y=2x-3$, $y=0$ and $x=4$ is:

**Options:**

- **(A)** $\dfrac{1}{8} + \log_e 2$
- **(B)** $\dfrac{1}{4} + \log_e 2$
- **(C)** $\dfrac{5}{6} + 3\log_e 2$
- **(D)** $\dfrac{5}{6} + \log_e 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{8} + \log_e 2$**

**Detailed Solution:**

Given $f(x) = \dfrac{x-1}{x+1}$. Let us find the first few compositions of $f(x)$:

$f^2(x) = f(f(x)) = \dfrac{\dfrac{x-1}{x+1}-1}{\dfrac{x-1}{x+1}+1} = \dfrac{x-1-x-1}{x-1+x+1} = \dfrac{-2}{2x} = -\dfrac{1}{x}$

$f^3(x) = f(f^2(x)) = f\left(-\dfrac{1}{x}\right) = \dfrac{-\dfrac{1}{x}-1}{-\dfrac{1}{x}+1} = \dfrac{-1-x}{-1+x} = \dfrac{x+1}{1-x}$

$f^4(x) = f(f^3(x)) = f\left(\dfrac{x+1}{1-x}\right) = \dfrac{\dfrac{x+1}{1-x}-1}{\dfrac{x+1}{1-x}+1} = \dfrac{x+1-1+x}{x+1+1-x} = \dfrac{2x}{2} = x$

Since $f^4(x) = x$, the sequence of functions is periodic with a period of $4$.

Therefore, $f^{26}(x) = f^{4 \times 6 + 2}(x) = f^2(x) = -\dfrac{1}{x}$.

We are given $g(x) + f^{26}(x) = 0$, which implies:
$g(x) - \dfrac{1}{x} = 0 \Rightarrow g(x) = \dfrac{1}{x}$

We need to find the area of the region bounded by the curves $y = \dfrac{1}{x}$, $y = x - \dfrac{3}{2}$ (from $2y = 2x - 3$), $y = 0$, and $x = 4$.

First, find the point of intersection of $y = \dfrac{1}{x}$ and $y = x - \dfrac{3}{2}$:
$\dfrac{1}{x} = x - \dfrac{3}{2} \Rightarrow 2x^2 - 3x - 2 = 0$
$(2x+1)(x-2) = 0$
Since $x \in (1, \infty)$, we get $x = 2$.

The line $y = x - \dfrac{3}{2}$ intersects the x-axis ($y = 0$) at $x = \dfrac{3}{2}$.

The required area $A$ is bounded by $y = x - \dfrac{3}{2}$ from $x = \dfrac{3}{2}$ to $x = 2$, and by $y = \dfrac{1}{x}$ from $x = 2$ to $x = 4$.

$A = \int_{3/2}^{2} \left(x - \dfrac{3}{2}\right) dx + \int_{2}^{4} \dfrac{1}{x} dx$

Evaluating the first integral:
$\int_{3/2}^{2} \left(x - \dfrac{3}{2}\right) dx = \left[ \dfrac{1}{2}\left(x - \dfrac{3}{2}\right)^2 \right]_{3/2}^{2} = \dfrac{1}{2} \left(2 - \dfrac{3}{2}\right)^2 - 0 = \dfrac{1}{2} \left(\dfrac{1}{2}\right)^2 = \dfrac{1}{8}$

Evaluating the second integral:
$\int_{2}^{4} \dfrac{1}{x} dx = [\log_e x]_{2}^{4} = \log_e 4 - \log_e 2 = \log_e 2$

Total Area = $\dfrac{1}{8} + \log_e 2$

</details>

---

### Q2. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $g(x)=3 x^{2}+2 x-3, f(0)=-3$ and $4 g(f(x))=3 x^{2}-32 x+72$, then $f(g(2))$ is equal to:

**Options:**

- **(A)** $-\frac{7}{2}$
- **(B)** $-\frac{25}{6}$
- **(C)** $\frac{7}{2}$
- **(D)** $\frac{25}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{7}{2}$**

**Detailed Solution:**

Let $f(x) = ax + b$. Then $4g(f(x)) = 12(ax+b)^2 + 8(ax+b) - 12$.
Comparing with $3x^2 - 32x + 72$:
$x^2$: $12a^2 = 3 \Rightarrow a = \pm\frac{1}{2}$
Constant: $12b^2 + 8b - 12 = 72 \Rightarrow 3b^2 + 2b - 21 = 0 \Rightarrow b = \frac{7}{3}$ or $b = -3$. Since $f(0) = -3$, $b = -3$.
$x$: $8a(3(-3)+1) = -32 \Rightarrow -8a = -4 \Rightarrow a = \frac{1}{2}$.
So $f(x) = \frac{x}{2} - 3$.
$g(2) = 3(4) + 4 - 3 = 13$.
$f(g(2)) = f(13) = \frac{13}{2} - 3 = \frac{7}{2}$.

</details>

---

### Q3. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=\log _{\mathrm{e}} x$ and $g(x)=\frac{x^4-2 x^3+3 x^2-2 x+2}{2 x^2-2 x+1}$. Then the domain of $f \circ g$ is

**Options:**

- **(A)** $[0, \infty)$
- **(B)** $[1, \infty)$
- **(C)** $(0, \infty)$
- **(D)** $\mathbb{R}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathbb{R}$**

**Detailed Solution:**

$f(g(x))=\ln \left(\frac{x^4-2 x^3+3 x^2-2 x+2}{2 x^2-2 x+1}\right)$

Since $2 x^2-2 x+1>0 \quad \forall x \in \mathbb{R} \because(-2)^2-4(2) < 0$
Consider
$\begin{aligned}
& x^4-2 x^3+3 x^2-2 x+2 \\
& =\left(x^4-2 x^3+x^2\right)+\left(x^2-2 x+1\right)+\left(1+x^2\right) \\
& =x^2(x-1)^2+(x-1)^2+\left(x^2+1\right)>0 \forall x \in \mathbb{R} \\
& \Rightarrow g(x)>0 \forall x \in \mathbb{R} \\
& \Rightarrow \ln f((x)), f(x)>0 \forall x \in \mathbb{R} \\
& \Rightarrow x \in \mathbb{R} \text { is domain }
\end{aligned}$

</details>

---

### Q4. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f, g: \mathbf{R} \rightarrow \mathbf{R}$ be defined as :
$f(x)=|x-1| \text { and } g(x)= \begin{cases}\mathrm{e}^x, \text { MARA } & x \geq 0 \\ x+1, & x \leq 0\end{cases}$
Then the function $f(g(x))$ is

**Options:**

- **(A)** neither one-one nor onto.
- **(B)** one-one but not onto.
- **(C)** onto but not one-one.
- **(D)** both one-one and onto.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) neither one-one nor onto.**

**Detailed Solution:**

$\begin{aligned} & f(g(x))=|g(x)-1| \\ & f o g\left[\begin{array}{cc}\left|e^x-1\right| & x \geq 0 \\ |x+1-1| & x \leq 0\end{array}\right. \\ & \text { fog }\left[\begin{array}{cc}e^x-1 & x \geq 0 \\ -x & x \leq 0\end{array}\right.\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/67p2RyqwuBcCWXIdB0onTLLxuNdUcOlhh0fAx3hYHzc.original.fullsize.png">

</details>

---

### Q5. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=x^5+2 x^3+3 x+1, x \in \mathbf{R}$, and $g(x)$ be a function such that $g(f(x))=x$ for all $x \in \mathbf{R}$. Then $\frac{g(7)}{g^{\prime}(7)}$ is equal to :

**Options:**

- **(A)** 14
- **(B)** 42
- **(C)** 7
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 14**

**Detailed Solution:**

$\begin{aligned} & f(x)=x^5+2 x^3+3 x+1 \\ & f^{\prime}(x)=5 x^4+6 x^2+3 \\ & f^{\prime}(1)=5+6+3=14 \\ & g(f(x))=x \\ & g^{\prime}(f(x)) f^{\prime}(x)=1 \\ & \text { for } f(x)=7 \\ & \Rightarrow x^5+2 x^3+3 x+1=7 \\ & \Rightarrow x=1 \\ & g^{\prime}(7) f^{\prime}(1)=1 \Rightarrow g^{\prime}(7)=\frac{1}{f^{\prime}(1)}=\frac{1}{14}\end{aligned}$
$\begin{aligned} & x=1, f(x)=7 \Rightarrow g(7)=1 \\ & \frac{g(7)}{g^{\prime}(7)}=\frac{1}{1 / 14}=14\end{aligned}$

</details>

---

### Q6. JEE Main 2024 (04 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Consider the function $f: \mathbb{R} \rightarrow \mathbb{R}$ defined by $f(x)=\frac{2 x}{\sqrt{1+9 x^2}}$. If the composition of $f, \underbrace{(f \circ f \circ f \circ \cdots \circ f)}_{10 \text { times }}(x)=\frac{2^{10} x}{\sqrt{1+9 \alpha x^2}}$, then the value of $\sqrt{3 \alpha+1}$ is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1024**

**Detailed Solution:**

$\begin{aligned}
& f(f(x))=\frac{2 f(x)}{\sqrt{1+9 f^2(x)}}=\frac{4 x}{\sqrt{1+9 x^2+9.2^2 x^2}} \\
& f(f(f(x)))=\frac{2^3 x / \sqrt{1+9 x^2}}{\sqrt{1+9\left(1+2^2\right) \frac{2^2 x^2}{1+9 x^2}}}=\frac{2^3 x}{\sqrt{1+9 x^2\left(1+2^2+2^4\right)}}
\end{aligned}$
$\therefore$ By observation
$\begin{aligned}
& \alpha=1+2^2+2^4+\ldots .+2^{18}=1\left(\frac{\left(2^2\right)^{10}-1}{2^2-1}\right)=\frac{2^{20}-1}{3} \\
& 3 \alpha+1=2^{20} \rightarrow \sqrt{3 \alpha+1}=2^{10}=1024
\end{aligned}$

</details>

---

### Q7. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>6</mn><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfrac><mo>,</mo><mo> </mo><mi>x</mi><mo>≠</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>f</mi><mi>o</mi><mi>f</mi><mo>)</mo><mo> </mo><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mo>→</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>g</mi><mi>o</mi><mi>g</mi><mi>o</mi><mi>g</mi><mo>)</mo><mo> </mo><mo>(</mo><mn>4</mn><mo>)</mo></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>19</mn><mn>20</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>20</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>6</mn><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mi>o</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn><mfenced><mfrac><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>6</mn><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfrac></mfenced><mo>+</mo><mn>3</mn></mrow><mrow><mn>6</mn><mfenced><mfrac><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>6</mn><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfrac></mfenced><mo>-</mo><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mi>o</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>16</mn><mi>x</mi><mo>+</mo><mn>12</mn><mo>+</mo><mn>18</mn><mi>x</mi><mo>-</mo><mn>12</mn></mrow><mrow><mn>24</mn><mi>x</mi><mo>+</mo><mn>18</mn><mo>-</mo><mn>24</mn><mi>x</mi><mo>+</mo><mn>16</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mi>o</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>34</mn><mi>x</mi></mrow><mn>34</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mi>o</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>g</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>g</mi><mi>o</mi><mi>g</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>g</mi><mi>o</mi><mi>g</mi><mi>o</mi><mi>g</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q8. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>→</mo><mi>R</mi></math> be a function defined <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></mrow></mfenced></mrow></mfenced></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><msubsup><mo>∫</mo><mn>0</mn><msqrt><mn>2</mn><msqrt><mn>5</mn></msqrt></msqrt></msubsup><msup><mi>x</mi><mn>2</mn></msup><mi>g</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>42</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>39</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>39</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfrac></math></p><p>Now, finding</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>f</mi><mn>4</mn></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfrac><mo>=</mo><mfrac><mfrac><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfrac><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><msup><mi>x</mi><mn>4</mn></msup><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfrac></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfrac><mo>=</mo><mfrac><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi>f</mi><mn>4</mn></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfrac><mo>=</mo><mfrac><mfrac><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfrac><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>4</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfrac></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfrac><mo>=</mo><mfrac><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfrac><mo>=</mo><mi>g</mi><mfenced><mi>x</mi></mfenced></math></p><p>Now finding,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><msubsup><mo>∫</mo><mn>0</mn><msqrt><mn>2</mn><msqrt><mn>5</mn></msqrt></msqrt></msubsup><msup><mi>x</mi><mn>2</mn></msup><mi>g</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>18</mn><msubsup><mo>∫</mo><mn>0</mn><msqrt><mn>2</mn><msqrt><mn>5</mn></msqrt></msqrt></msubsup><mfrac><msup><mi>x</mi><mn>3</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>x</mi><mn>4</mn></msup><mo>=</mo><msup><mi>t</mi><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>16</mn><msup><mi>x</mi><mn>3</mn></msup><mi>d</mi><mi>x</mi><mo>=</mo><mn>4</mn><msup><mi>t</mi><mn>3</mn></msup><mi>d</mi><mi>t</mi></math></p><p>So, the integral becomes</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>18</mn><mn>4</mn></mfrac><msubsup><mo>∫</mo><mn>1</mn><mn>3</mn></msubsup><mfrac><mrow><msup><mi>t</mi><mn>3</mn></msup><mi>dt</mi></mrow><mi mathvariant="normal">t</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><msubsup><mo>∫</mo><mn>1</mn><mn>3</mn></msubsup><msup><mi>t</mi><mn>2</mn></msup><mi>dt</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><msubsup><mfenced><mfrac><msup><mi>t</mi><mn>3</mn></msup><mn>3</mn></mfrac></mfenced><mn>1</mn><mn>3</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>·</mo><mn>26</mn><mo>=</mo><mn>39</mn></math></p></blockquote>

</details>

---

### Q9. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mrow><mtable columnalign="left"><mtr><mtd><mn>2</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>,</mo><mo> </mo><mo>-</mo><mn>1</mn><mo>≤</mo><mi>x</mi><mo>&lt;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>-</mo><mfrac><mi>x</mi><mn>3</mn></mfrac><mo>,</mo><mo> </mo><mn>0</mn><mo>≤</mo><mi>x</mi><mo>≤</mo><mn>3</mn></mtd></mtr></mtable><mo>;</mo><mo> </mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mo>-</mo><mi>x</mi><mo>,</mo><mo> </mo><mo>-</mo><mn>3</mn><mo>≤</mo><mi>x</mi><mo>≤</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>,</mo><mo> </mo><mn>0</mn><mo>&lt;</mo><mi>x</mi><mo>≤</mo><mn>1</mn></mtd></mtr></mtable></mfenced></mrow></mfenced></math>, then range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>f</mi><mo>∘</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>)</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>]</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mn>3</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>]</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>]</mo></math>**

**Detailed Solution:**

<p>Given: </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>2</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>,</mo><mo> </mo><mi>x</mi><mo>∈</mo><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo></mtd></mtr><mtr><mtd><mn>1</mn><mo>-</mo><mfrac><mi>x</mi><mn>3</mn></mfrac><mo>,</mo><mo> </mo><mi>x</mi><mo>∈</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mi>x</mi><mo>,</mo><mo> </mo><mi>x</mi><mo>∈</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>]</mo></mtd></mtr><mtr><mtd><mo>-</mo><mi>x</mi><mo>,</mo><mo> </mo><mi>x</mi><mo>∈</mo><mfenced close="]" open="["><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>0</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>2</mn><mo>+</mo><mn>2</mn><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>,</mo><mo> </mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>∈</mo><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo></mtd></mtr><mtr><mtd><mn>1</mn><mo>-</mo><mfrac><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow><mn>3</mn></mfrac><mo>,</mo><mo> </mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>∈</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>2</mn><mo>+</mo><mn>2</mn><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>,</mo><mo> </mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>∈</mo><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo><mo>⇒</mo><mi>x</mi><mo>∈</mo><mi>ϕ</mi></mtd></mtr><mtr><mtd><mn>1</mn><mo>-</mo><mfrac><mfenced close="|" open="|"><mi>x</mi></mfenced><mn>3</mn></mfrac><mo>,</mo><mo> </mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>∈</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><mi>x</mi><mo>∈</mo><mfenced close="]" open="["><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo> </mo><mtext>for </mtext><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>≤</mo><mn>3</mn><mo> </mo><mtext>but </mtext><mi>x</mi><mo>∈</mo><mfenced close="]" open="["><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo> </mo><mtext>in </mtext><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mfenced close="|" open="|"><mi>x</mi></mfenced><mn>3</mn></mfrac><mo>,</mo><mo> </mo><mi>x</mi><mo>∈</mo><mfenced close="]" open="["><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>Now, maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mfenced close="|" open="|"><mi>x</mi></mfenced><mn>3</mn></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>0</mn><mn>3</mn></mfrac><mo>=</mo><mn>1</mn></math> </p><p>And minimum value is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>3</mn><mn>3</mn></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Hence, the range of the function will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

### Q10. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi><mo>,</mo></math> two real valued functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> are such that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msqrt><mi>x</mi></msqrt><mo>+</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>-</mo><msqrt><mi>x</mi></msqrt><mo>.</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<blockquote><p>We have been given that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>-</mo><msqrt><mi>x</mi></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><msqrt><mi>x</mi></msqrt><mo>+</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>-</mo><msqrt><mi>x</mi></msqrt></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>x</mi></msqrt><mo>+</mo><mn>1</mn><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>x</mi></msqrt><mo>=</mo><mi>t</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>(</mo><mi>t</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mo>(</mo><mi>t</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>-</mo><mo>(</mo><mi>t</mi><mo>-</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>5</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q11. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mfenced><mrow><mi>tan</mi><msup><mn>1</mn><mo>&#176;</mo></msup></mrow></mfenced><mi>x</mi><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>123</mn></mfenced></mrow><mrow><mi>x</mi><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>1234</mn></mfenced><mo>-</mo><mfenced><mrow><mi>tan</mi><msup><mn>1</mn><mo>&#176;</mo></msup></mrow></mfenced></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>, then the least value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mfrac><mn>4</mn><mi>x</mi></mfrac></mfenced></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mfenced><mrow><mi>tan</mi><msup><mn>1</mn><mo>&#176;</mo></msup></mrow></mfenced><mi>x</mi><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>123</mn></mfenced></mrow><mrow><mi>x</mi><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>1234</mn></mfenced><mo>-</mo><mfenced><mrow><mi>tan</mi><msup><mn>1</mn><mo>&#176;</mo></msup></mrow></mfenced></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math></p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><msup><mn>1</mn><mo>&#176;</mo></msup><mo>=</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>123</mn></mfenced><mo>=</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>1234</mn></mfenced><mo>=</mo><mi>c</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></mrow><mrow><mi>c</mi><mi>x</mi><mo>-</mo><mi>a</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>a</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>b</mi></mrow><mrow><mi>c</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>a</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>a</mi><mfenced><mfrac><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></mrow><mrow><mi>c</mi><mi>x</mi><mo>-</mo><mi>a</mi></mrow></mfrac></mfenced><mo>+</mo><mi>b</mi></mrow><mrow><mi>c</mi><mfenced><mfrac><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></mrow><mrow><mi>c</mi><mi>x</mi><mo>-</mo><mi>a</mi></mrow></mfrac></mfenced><mo>-</mo><mi>a</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mfenced><mrow><mi>c</mi><mi>x</mi><mo>-</mo><mi>a</mi></mrow></mfenced></mrow><mrow><mi>a</mi><mi>c</mi><mi>x</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>-</mo><mi>a</mi><mfenced><mrow><mi>c</mi><mi>x</mi><mo>-</mo><mi>a</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>b</mi><mi>c</mi><mi>x</mi></mrow><mrow><mi>b</mi><mi>c</mi><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mfrac><mn>4</mn><mi>x</mi></mfrac></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><mn>4</mn><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>, then least value <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mi>x</mi><mo>&#183;</mo><mfrac><mn>4</mn><mi>x</mi></mfrac></msqrt><mo>=</mo><mn>2</mn></math></p></blockquote>

</details>

---

### Q12. JEE Main 2023 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mn>1</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced></math>. For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8805;</mo><mn>2</mn></math>, define <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mi>n</mi></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>f</mi><mn>1</mn></msup><mi>o</mi><msup><mi>f</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mn>5</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></mrow><mrow><mi>b</mi><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>gcd</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi></math> is equal to ________</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3125**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mn>1</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mn>2</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>f</mi><mn>1</mn></msup><mi>o</mi><msup><mi>f</mi><mn>1</mn></msup><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mn>2</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn><mfenced><mfrac><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn><mfenced><mfrac><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced><mo>+</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mn>2</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>9</mn><mi>x</mi><mo>+</mo><mn>6</mn><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow><mrow><mn>6</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>+</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>9</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mn>2</mn></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mn>13</mn><mi>x</mi><mo>+</mo><mn>12</mn></mrow><mrow><mn>12</mn><mi>x</mi><mo>+</mo><mn>13</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mn>3</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn><mfenced><mfrac><mrow><mn>13</mn><mi>x</mi><mo>+</mo><mn>12</mn></mrow><mrow><mn>12</mn><mi>x</mi><mo>+</mo><mn>13</mn></mrow></mfrac></mfenced><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn><mfenced><mfrac><mrow><mn>13</mn><mi>x</mi><mo>+</mo><mn>12</mn></mrow><mrow><mn>12</mn><mi>x</mi><mo>+</mo><mn>13</mn></mrow></mfrac></mfenced><mo>+</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mn>3</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>63</mn><mi>x</mi><mo>+</mo><mn>62</mn></mrow><mrow><mn>62</mn><mi>x</mi><mo>+</mo><mn>63</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mn>4</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn><mfenced><mfrac><mrow><mn>63</mn><mi>x</mi><mo>+</mo><mn>62</mn></mrow><mrow><mn>62</mn><mi>x</mi><mo>+</mo><mn>63</mn></mrow></mfrac></mfenced><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn><mfenced><mfrac><mrow><mn>63</mn><mi>x</mi><mo>+</mo><mn>62</mn></mrow><mrow><mn>62</mn><mi>x</mi><mo>+</mo><mn>63</mn></mrow></mfrac></mfenced><mo>+</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mn>4</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>313</mn><mi>x</mi><mo>+</mo><mn>312</mn></mrow><mrow><mn>312</mn><mi>x</mi><mo>+</mo><mn>313</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>f</mi><mn>5</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>1563</mn><mi>x</mi><mo>+</mo><mn>1562</mn></mrow><mrow><mn>1562</mn><mi>x</mi><mo>+</mo><mn>1563</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></mrow><mrow><mi>b</mi><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>1563</mn><mo>+</mo><mn>1562</mn><mo>=</mo><mn>3125</mn></math></p>

</details>

---

### Q13. JEE Main 2022 (28 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi></math> be three positive real numbers. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>&#945;</mi><msup><mi mathvariant="normal">x</mi><mn>5</mn></msup><mo>+</mo><mi>&#946;</mi><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mo>+</mo><mi>&#947;</mi><mi mathvariant="normal">x</mi><mo>,</mo><mi mathvariant="normal">x</mi><mo>&#8712;</mo><mi mathvariant="normal">R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>,</mo><msub><mi>a</mi><mi>n</mi></msub></math> be in arithmetic progression with mean zero, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mrow><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mi>f</mi><mfenced><msub><mi>a</mi><mi>i</mi></msub></mfenced></mrow></mfenced></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi></math> be three positive real numbers. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>&#945;</mi><msup><mi mathvariant="normal">x</mi><mn>5</mn></msup><mo>+</mo><mi>&#946;</mi><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mo>+</mo><mi>&#947;</mi><mi mathvariant="normal">x</mi><mo>,</mo><mi mathvariant="normal">x</mi><mo>&#8712;</mo><mi mathvariant="normal">R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>,</mo><msub><mi>a</mi><mi>n</mi></msub></math> be in arithmetic progression with mean zero, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mrow><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mi>f</mi><mfenced><msub><mi>a</mi><mi>i</mi></msub></mfenced></mrow></mfenced></mrow></mfenced></math> is equal to</p><p>Given,</p><p>Mean is zero, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow><mi>n</mi></mfrac><mo>=</mo><mn>0</mn></math></p><p>Now this means that first and last term, second and second last and so on are equal in magnitude but opposite in sign.</p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>&#945;</mi><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mi>&#946;</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>&#947;</mi><mi>x</mi></math></p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mi>f</mi><mfenced><msub><mi>a</mi><mi>i</mi></msub></mfenced><mo>=</mo><mi>&#945;</mi><mfenced><mrow><msubsup><mi>a</mi><mn>1</mn><mn>5</mn></msubsup><mo>+</mo><msubsup><mi>a</mi><mn>2</mn><mn>5</mn></msubsup><mo>+</mo><msubsup><mi>a</mi><mn>3</mn><mn>5</mn></msubsup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msubsup><mi>a</mi><mi>n</mi><mn>5</mn></msubsup></mrow></mfenced><mo>+</mo><mi>&#946;</mi><mfenced><mrow><msubsup><mi>a</mi><mn>1</mn><mn>3</mn></msubsup><mo>+</mo><msubsup><mi>a</mi><mn>2</mn><mn>3</mn></msubsup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msubsup><mi>a</mi><mi>n</mi><mn>3</mn></msubsup></mrow></mfenced><mo>+</mo><mi>&#947;</mi><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mi>&#945;</mi><mo>+</mo><mn>0</mn><mi>&#946;</mi><mo>+</mo><mn>0</mn><mi>&#947;</mi><mo>=</mo><mn>0</mn></math> ......equation<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>  {as first &amp; last, second and second last and so on are equal in magnitude and opposite in sign}</p><p>Now given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced close="]"><mrow><mi>g</mi><mfenced><mrow><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mi>f</mi><mfenced><msub><mi>a</mi><mi>i</mi></msub></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mi>f</mi><mfenced><msub><mi>a</mi><mi>i</mi></msub></mfenced><mo>=</mo><mn>0</mn></math> {from equation<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> }</p></blockquote>

</details>

---

### Q14. JEE Main 2022 (29 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> be two real polynomials of degree <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>1</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>g</mi><mfenced><mn>2</mn></mfenced></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced close=""><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced></math>and  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced close=""><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>c</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>d</mi><mi>x</mi><mo>+</mo><mi>e</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mi>c</mi><msup><mfenced><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mi>d</mi><mfenced><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mo>+</mo><mi>e</mi><mo>=</mo><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mi>a</mi><mfenced><mrow><mi>c</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>d</mi><mi>x</mi><mo>+</mo><mi>e</mi></mrow></mfenced><mo>+</mo><mi>b</mi><mo>=</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p>On comparing both side we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>e</mi><mo>=</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>&#8658;</mo><mi>g</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#38;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>8</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>15</mn></math>.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>g</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>18</mn></math></p>

</details>

---

### Q15. JEE Main 2022 (27 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>10</mn></mrow></mfenced></math>. Define <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>S</mi><mo>&#8594;</mo><mi>S</mi></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="center left"><mtr><mtd><mn>2</mn><mi>n</mi><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>n</mi><mo>-</mo><mn>11</mn></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>6</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>10</mn></mtd></mtr></mtable></mfenced></math>
Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>S</mi><mo>&#8805;</mo><mi>S</mi></math> be a function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>fog</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mi>n</mi><mo>+</mo><mn>1</mn></mtd><mtd><mo>,</mo><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>n</mi><mo>&#160;</mo><mi>is</mi><mo>&#160;</mo><mi>odd</mi><mo>&#160;</mo></mtd></mtr><mtr><mtd><mi>n</mi><mo>-</mo><mn>1</mn></mtd><mtd><mo>,</mo><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>n</mi><mo>&#160;</mo><mtext>is&#160;</mtext><mi>even</mi><mo>&#160;</mo></mtd></mtr></mtable></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>10</mn></mfenced><mfenced><mrow><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>g</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>g</mi><mfenced><mn>3</mn></mfenced><mo>+</mo><mi>g</mi><mfenced><mn>4</mn></mfenced><mo>+</mo><mi>g</mi><mfenced><mn>5</mn></mfenced></mrow></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **190**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="center left"><mtr><mtd><mn>2</mn><mi>n</mi><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>n</mi><mo>-</mo><mn>11</mn></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>6</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>10</mn></mtd></mtr></mtable></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>4</mn></math>, .....<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>=</mo><mn>10</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>6</mn></mfenced><mo>=</mo><mn>1</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>7</mn></mfenced><mo>=</mo><mn>3</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>8</mn></mfenced><mo>=</mo><mn>5</mn></math> ......<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>10</mn></mfenced><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>n</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mi>n</mi><mo>+</mo><mn>1</mn></mtd><mtd><mo>;</mo></mtd><mtd><mi>n</mi><mo>&#8712;</mo><mo>&#160;</mo><mi>odd</mi><mo>&#160;</mo></mtd></mtr><mtr><mtd><mi>n</mi><mo>-</mo><mn>1</mn></mtd><mtd><mo>;</mo></mtd><mtd><mi>n</mi><mo>&#8712;</mo><mo>&#160;</mo><mi>even</mi><mo>&#160;</mo></mtd></mtr></mtable></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mn>10</mn></mfenced></mrow></mfenced><mo>=</mo><mn>9</mn><mo>&#8658;</mo><mi>g</mi><mfenced><mn>10</mn></mfenced><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mn>1</mn></mfenced></mrow></mfenced><mo>=</mo><mn>2</mn><mo>&#8658;</mo><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mn>2</mn></mfenced></mrow></mfenced><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>g</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mn>3</mn></mfenced></mrow></mfenced><mo>=</mo><mn>4</mn><mo>&#8658;</mo><mi>g</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mn>4</mn></mfenced></mrow></mfenced><mo>=</mo><mn>3</mn><mo>&#8658;</mo><mi>g</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mn>5</mn></mfenced></mrow></mfenced><mo>=</mo><mn>6</mn><mo>&#8658;</mo><mi>g</mi><mfenced><mn>5</mn></mfenced><mo>=</mo><mn>3</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>10</mn></mfenced><mo>&#183;</mo><mfenced close="]" open="["><mrow><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>g</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>g</mi><mfenced><mn>3</mn></mfenced><mo>+</mo><mi>g</mi><mfenced><mn>4</mn></mfenced><mo>+</mo><mi>g</mi><mfenced><mn>5</mn></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><mo>&#183;</mo><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>190</mn></math></p>

</details>

---

### Q16. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mo>{</mo><mn>0</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo></math> . If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#160;&#160;</mo><mi>f</mi><mfenced><mrow><msup><mi>f</mi><mi>n</mi></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mn>6</mn></msup><mfenced><mn>6</mn></mfenced><mo>+</mo><msup><mi>f</mi><mn>7</mn></msup><mfenced><mn>7</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>12</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>11</mn><mn>12</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><msup><mi>f</mi><mn>1</mn></msup><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mn>2</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfrac><mrow><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mn>1</mn></mrow><mrow><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mn>3</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><msup><mi>f</mi><mn>2</mn></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mn>4</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>f</mi><mn>6</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>&#8658;</mo><msup><mi>f</mi><mn>6</mn></msup><mfenced><mn>6</mn></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mn>7</mn></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mn>7</mn></msup><mfenced><mn>7</mn></mfenced><mo>=</mo><mfrac><mn>8</mn><mrow><mo>-</mo><mn>6</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q17. JEE Main 2022 (25 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="bold-italic">R</mi><mo>&#8594;</mo><mi mathvariant="bold-italic">R</mi></math> be a function defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><msup><mi>x</mi><mn>25</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>+</mo><msup><mi>x</mi><mn>25</mn></msup></mrow></mfenced></mrow></mfenced><mfrac><mn>1</mn><mn>50</mn></mfrac></msup></math>. If the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math>, then the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>1</mn></mfenced></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced close="]" open="["><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><msup><mi>x</mi><mn>25</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>+</mo><msup><mi>x</mi><mn>25</mn></msup></mrow></mfenced></mrow></mfenced><mfrac><mn>1</mn><mn>50</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced close="]" open="["><mrow><mfenced><mrow><mn>2</mn><mo>-</mo><msup><mi>x</mi><mn>25</mn></msup></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>+</mo><msup><mi>x</mi><mn>25</mn></msup></mrow></mfenced></mrow></mfenced><mfrac><mn>1</mn><mn>50</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>4</mn><mo>-</mo><msup><mi>x</mi><mn>50</mn></msup></mrow></mfenced><mfrac><mn>1</mn><mn>50</mn></mfrac></msup></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><msup><mfenced><mrow><mn>4</mn><mo>-</mo><msup><mfenced><msup><mfenced><mrow><mn>4</mn><mo>-</mo><msup><mi>x</mi><mn>50</mn></msup></mrow></mfenced><mfrac><mn>1</mn><mn>50</mn></mfrac></msup></mfenced><mn>50</mn></msup></mrow></mfenced><mfrac><mn>1</mn><mn>50</mn></mfrac></msup><mo>=</mo><mi>x</mi></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>x</mi></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>1</mn><mo>=</mo><msup><mn>3</mn><mfrac><mn>1</mn><mn>50</mn></mfrac></msup><mo>+</mo><mn>1</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>g</mi><mfenced><mn>1</mn></mfenced></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msup><mn>3</mn><mfrac><mn>1</mn><mn>50</mn></mfrac></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q18. JEE Main 2021 (20 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mfrac><mi>&#945;</mi><mn>6</mn></mfrac></mfenced><mo>&#8594;</mo><mi>R</mi></math> be defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mfrac><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>6</mn><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow></mfrac></mfenced></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>f</mi><mi>o</mi><mi>f</mi></mrow></mfenced><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi></math>, for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mfrac><mi>&#945;</mi><mn>6</mn></mfrac></mfenced><mo>,</mo></math> is

**Options:**

- **(A)** No such <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> exists
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>y</mi><mo>=</mo><mfenced><mfrac><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>6</mn><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow></mfrac></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>6</mn><mi>x</mi><mi>y</mi><mo>-</mo><mi>&#945;</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>(</mo><mn>6</mn><mi>y</mi><mo>-</mo><mn>5</mn><mo>)</mo><mo>=</mo><mi>&#945;</mi><mi>y</mi><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mi>&#945;</mi><mi>y</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>6</mn><mi>y</mi><mo>-</mo><mn>5</mn></mrow></mfrac></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mfrac><mrow><mi>&#945;</mi><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>6</mn><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfrac></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>f</mi><mi>o</mi><mi>f</mi></mrow></mfenced><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>f</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mi>x</mi><mo>)</mo></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>6</mn><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow></mfrac></mfenced><mo>=</mo><mfenced><mfrac><mrow><mi>&#945;</mi><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>6</mn><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfrac></mfenced></math></p><p>Clearly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q19. JEE Main 2020 (06 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

For a suitably chosen real constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">a</mi></math>, let a function, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mi mathvariant="bold">R</mi><mo mathvariant="bold">-</mo><mfenced close="}" open="{"><mrow><mo mathvariant="bold">-</mo><mi mathvariant="bold">a</mi></mrow></mfenced><mo mathvariant="bold">&#8594;</mo><mi mathvariant="bold">R</mi></math> be defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mfrac><mrow><mi mathvariant="normal">a</mi><mo>-</mo><mi mathvariant="normal">x</mi></mrow><mrow><mi mathvariant="normal">a</mi><mo>+</mo><mi mathvariant="normal">x</mi></mrow></mfrac></math>. Further supposed that for any real number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>&#8800;</mo><mo>-</mo><mi mathvariant="normal">a</mi><mo>,</mo></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#8800;</mo><mo>-</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mfenced><mi>fof</mi></mfenced><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mi mathvariant="normal">x</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mi>a</mi><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>a</mi><mo>+</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mfrac><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>a</mi><mo>-</mo><mi>a</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>a</mi><mo>(</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>)</mo></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>a</mi><mo>-</mo><mi>x</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>x</mi></mrow></mfrac></math>        <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>&#8757;</mo><mi>a</mi><mo>=</mo><mn>1</mn><mo>)</mo></math></p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mn>3</mn></math></p><p> </p>

</details>

---

### Q20. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn></math> and <math><mfenced separators="|"><mrow><mi>g</mi><mi>o</mi><mi>f</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>,</mo><mi></mi></math> then <math><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>4</mn><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>10</mn><mo>.</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mn>5</mn><mo>=</mo><mo>-</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>  
<math><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>-</mo><mn>1</mn></math>  
<math><mo>-</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><msup><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>-</mo><mn>1</mn></math>  
<math><msup><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><mn>0</mn></math>  
<math><msup><mrow><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math>  
<math><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

</details>

---

### Q21. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For <math><mi>x</mi><mi>&#160;</mi><mi>&#1013;</mi><mi>&#160;</mi><mo>(</mo><mn>0</mn><mo>,</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>)</mo><mo>,</mo></math> let <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msqrt><mi>x</mi></msqrt><mo>,</mo><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></math> and <math><mi>h</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math> . If <math><mi mathvariant="normal">&#981;</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mo>(</mo><mi mathvariant="normal">h</mi><mi mathvariant="normal">o</mi><mi>f</mi><mo>)</mo><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mo>)</mo><mo>(</mo><mi>x</mi><mo>)</mo><mo>,</mo></math> then <math><mi mathvariant="normal">&#981;</mi><mi mathvariant="normal">&#160;</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>12</mn></mrow></mfrac></mrow></mrow></math>
- **(B)** <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>5</mn><mi>π</mi></mrow><mrow><mn>12</mn></mrow></mfrac></mrow></mrow></math>
- **(C)** <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>7</mn><mi>π</mi></mrow><mrow><mn>12</mn></mrow></mfrac></mrow></mrow></math>
- **(D)** <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>11</mn><mi>π</mi></mrow><mrow><mn>12</mn></mrow></mfrac></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>11</mn><mi>π</mi></mrow><mrow><mn>12</mn></mrow></mfrac></mrow></mrow></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msqrt><mi>x</mi></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>tan</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#8201;</mtext><mi>h</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math>
<math><mi>f</mi><mi>o</mi><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msqrt><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mi>o</mi><mi>f</mi><mi>o</mi><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>h</mi><mfenced separators="|"><msqrt><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></msqrt></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>tan</mi><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced></math>
<math><mi>&#981;</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>tan</mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></mrow></mfenced><mo>=</mo><mo>-</mo><mi>tan</mi><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math></p><p><math><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mi>&#960;</mi><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>12</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mn>11</mn><mi>&#960;</mi></mrow><mrow><mn>12</mn></mrow></mfrac></math></p>

</details>

---

### Q22. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></mfenced><mo>,</mo><mi mathvariant="normal">&#160;</mi><mfenced separators="|"><mrow><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mi>&#960;</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mrow><mo>(</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>)</mo></mrow><mo>,</mo><mi mathvariant="normal">&#160;</mi><mo>(</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn><mo>)</mo><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is a positive real number such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><msup><mfenced separators="|"><mrow><mi>f</mi><mi>o</mi><mi>g</mi></mrow></mfenced><mi mathvariant="normal">&#39;</mi></msup><mo>(</mo><mi>&#945;</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mfenced separators="|"><mrow><mi>f</mi><mi>o</mi><mi>g</mi></mrow></mfenced><mo>(</mo><mi>&#945;</mi><mo>)</mo><mo>,</mo></math> then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>&#945;</mi><mo>+</mo><mi>a</mi><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>&#945;</mi><mo>-</mo><mi>a</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>&#945;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mi>b</mi><mi>&#945;</mi><mo>-</mo><mi>a</mi><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mi>b</mi><mi>&#945;</mi><mo>-</mo><mi>a</mi><mo>=</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mi>b</mi><mi>&#945;</mi><mo>-</mo><mi>a</mi><mo>=</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></mfenced><mo>,</mo><mi mathvariant="normal">&#160;</mi><mfenced separators="|"><mrow><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mi>&#960;</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mrow><mo>(</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>)</mo></mrow><mo>,</mo><mi mathvariant="normal">&#160;</mi><mo>(</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn><mo>)</mo><mo>,</mo></math> then we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>f</mi><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>sin</mi><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mfenced></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mfenced><mo>=</mo><mo>-</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mi>o</mi><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced separators="|"><mi>&#945;</mi></mfenced></mrow></mfenced><mo>=</mo><mo>-</mo><mi>&#945;</mi></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow><mo>(</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mfenced><mo>)</mo></mrow><mo>'</mo></msup><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><msup><mfenced separators="|"><mrow><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced separators="|"><mi>&#945;</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>'</mo></msup><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>a</mi><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mi>b</mi><mi>&#945;</mi><mo>-</mo><mi>a</mi><mo>=</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mi>&#945;</mi><mo>-</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>1</mn><mo>.</mo></math></p>

</details>

---

### Q23. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> . For any <math><mi>A</mi><mo>&#8838;</mo><mi>R</mi><mo>,</mo></math> define <math><mi>g</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mo>{</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mi>&#160;</mi><mo>:</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#8712;</mo><mi>A</mi><mo>}</mo></math> . If <math><mi>S</mi><mo>=</mo><mo>[</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>4</mn><mo>]</mo></math> , then which one of the following statements is not true?

**Options:**

- **(A)** <math><mi>g</mi><mo>(</mo><mi>f</mi><mo>(</mo><mi>S</mi><mo>)</mo><mo>)</mo><mo>≠</mo><mi>S</mi></math>
- **(B)** <math><mi>f</mi><mo>(</mo><mi>g</mi><mo>(</mo><mi>S</mi><mo>)</mo><mo>)</mo><mo>≠</mo><mi>f</mi><mo>(</mo><mi>S</mi><mo>)</mo></math>
- **(C)** <math><mi>f</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>S</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>S</mi></math>
- **(D)** <math><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>S</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>g</mi><mfenced separators="|"><mrow><mi>S</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>S</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>g</mi><mfenced separators="|"><mrow><mi>S</mi></mrow></mfenced></math>**

**Detailed Solution:**

From the given information we can conclude 
<math><mi>g</mi><mfenced separators="|"><mrow><mi>S</mi></mrow></mfenced><mo>=</mo><mfenced open="[" close="]" separators="|"><mrow><mo>-</mo><mn>2,2</mn></mrow></mfenced></math> , So, <math><mi>f</mi><mo>(</mo><mi>g</mi><mo>(</mo><mi>S</mi><mo>)</mo><mo>)</mo><mo>=</mo><mfenced open="[" close="]" separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mn>4</mn></mrow></mfenced><mo>=</mo><mi>S</mi></math>  
And <math><mi>f</mi><mo>(</mo><mi>S</mi><mo>)</mo><mo>=</mo><mfenced open="[" close="]" separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mn>16</mn></mrow></mfenced><mo>⇒</mo><mi>f</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>S</mi></mrow></mfenced></mrow></mfenced><mo>≠</mo><mi>f</mi><mfenced separators="|"><mrow><mi>S</mi></mrow></mfenced></math>  
Also, <math><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>S</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced open="[" close="]" separators="|"><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mi> </mi><mn>4</mn></mrow></mfenced><mo>≠</mo><mi>g</mi><mfenced separators="|"><mrow><mi>S</mi></mrow></mfenced></math>  
So, <math><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>S</mi></mrow></mfenced></mrow></mfenced><mo>≠</mo><mi>S</mi></math>  
Hence, <math><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>S</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>g</mi><mfenced separators="|"><mrow><mi>S</mi></mrow></mfenced></math> is not true.

</details>

---

### Q24. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mo>,</mo><mi>&#160;</mi><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>&#60;</mo><mi>&#160;</mi><mn>1</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><msup><mfenced separators="|"><msup><mi>x</mi><mn>2</mn></msup></mfenced><mi>&#160;</mi></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8211;</mo><mn>2</mn><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>=</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><msup><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mn>2</mn></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mfenced close="|" open="|" separators="|"><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8201;</mo><mfenced><mrow><mo>&#8757;</mo><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>&#60;</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math></p>

</details>

---

### Q25. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mfenced open="{" close="}" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced><mo>,</mo></math> let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>1</mn></msub><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>,</mo><msub><mi>f</mi><mn>2</mn></msub><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>3</mn></msub><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></math> be three given functions. If a function, <math><mi>J</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msub><mi>f</mi><mn>2</mn></msub><mi>o</mi><mi>J</mi><mi>o</mi><msub><mi>f</mi><mn>1</mn></msub></mrow></mfenced><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msub><mi>f</mi><mn>3</mn></msub><mfenced separators="|"><mi>x</mi></mfenced></math> then <math><mi>J</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>3</mn></msub><mfenced separators="|"><mi>x</mi></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>x</mi></mfrac><msub><mi>f</mi><mn>3</mn></msub><mfenced separators="|"><mi>x</mi></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>1</mn></msub><mfenced separators="|"><mi>x</mi></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>2</mn></msub><mfenced separators="|"><mi>x</mi></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>3</mn></msub><mfenced separators="|"><mi>x</mi></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>2</mn></msub><mfenced separators="|"><mrow><mi>J</mi><mfenced separators="|"><mrow><msub><mi>f</mi><mn>1</mn></msub><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><msub><mi>f</mi><mn>3</mn></msub><mfenced separators="|"><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>f</mi><mn>2</mn></msub><mfenced separators="|"><mrow><mi>J</mi><mfenced separators="|"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mi>J</mi><mfenced separators="|"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>J</mi><mfenced separators="|"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mi>x</mi><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>J</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><mfrac><mn>1</mn><mi>x</mi></mfrac><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mi>J</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>f</mi><mn>3</mn></msub><mfenced><mi>x</mi></mfenced></math></p>

</details>

---

### Q26. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mn>2</mn><mn>10</mn></msup><mi>x</mi><mo>+</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mn>3</mn><mn>10</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn><mo>.</mo></math> If <math><mfenced separators="|"><mrow><mi>f</mi><mi>o</mi><mi>g</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>,</mo></math> then <math><mi>x</mi></math> is equal to:

**Options:**

- **(A)** <math><mfrac><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup><mo>-</mo><msup><mrow><mn>3</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></mrow><mrow><msup><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></msup><mo>-</mo><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><msup><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></msup><mo>-</mo><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mrow><mn>3</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup><mo>-</mo><msup><mrow><mn>3</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></mrow><mrow><msup><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></msup><mo>-</mo><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given <math><mi>f</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi></math></p><p>Where,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mn>2</mn><mn>10</mn></msup><mi>x</mi><mo>+</mo><mn>1</mn></math> ,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mn>3</mn><mn>10</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn><mo>.</mo></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><msup><mn>3</mn><mn>10</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mn>10</mn></msup><mfenced separators="|"><mrow><msup><mn>3</mn><mn>10</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+1</mo></math>

<math><mo>&#8658;</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup><mfenced separators="|"><mrow><msup><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></msup><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mo>=</mo><mi>x</mi></math>

<math><mo>&#8658;</mo><mi>x</mi><mfenced separators="|"><mrow><msup><mrow><mn>6</mn></mrow><mrow><mn>10</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup><mo>-</mo><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mn>6</mn><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow><msup><mn>2</mn><mn>10</mn></msup></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mrow><mo>(</mo><mn>2</mn><mo>&#215;</mo><mn>3</mn><msup><mo>)</mo><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow><msup><mn>2</mn><mn>10</mn></msup></mfrac></mstyle></mfrac></math>

<math><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></mrow><mrow><msup><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></msup><mo>-</mo><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></mrow></mfrac></math></p>

</details>

---

