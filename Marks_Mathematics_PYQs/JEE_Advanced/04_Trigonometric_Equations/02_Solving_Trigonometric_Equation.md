# JEE Advanced Mathematics - Trigonometric Equations

## Topic 2: Solving Trigonometric Equation

**Total Questions:** 17

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `numerical` | *Level:* `2`

<strong>Passage:</strong> Consider the curve $C_1$ given by $y = e^{-x}$ for $x \in [0, 10\pi]$, and the curve $C_2$ given by $y = e^{-x}(\sin x + \cos x)$ for $x \in [0, 10\pi]$. Let $n$ be the total number of points of intersection of the curves $C_1$ and $C_2$. Suppose that $\alpha_1, \alpha_2, \ldots, \alpha_n \in [0, 10\pi]$ are the $x$-coordinates of the points of intersection of the curves $C_1$ and $C_2$ such that $\alpha_1 < \alpha_2 < \cdots < \alpha_n$.

<strong>Question:</strong> The value of $n$ is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **11**

**Detailed Solution:**

Equating the equations of the curves $C_1$ and $C_2$:

$e^{-x} = e^{-x}(\sin x + \cos x)$

Since $e^{-x} \neq 0$ for all real $x$, dividing both sides by $e^{-x}$ gives:

$\sin x + \cos x = 1$

Multiplying both sides by $\dfrac{1}{\sqrt{2}}$:

$\dfrac{1}{\sqrt{2}}\sin x + \dfrac{1}{\sqrt{2}}\cos x = \dfrac{1}{\sqrt{2}}$

$\sin\left(x + \dfrac{\pi}{4}\right) = \dfrac{1}{\sqrt{2}}$

The general solution is given by:

$x + \dfrac{\pi}{4} = 2m\pi + \dfrac{\pi}{4}$ or $x + \dfrac{\pi}{4} = 2m\pi + \dfrac{3\pi}{4}$ for integer $m$

This simplifies to:

$x = 2m\pi$ or $x = 2m\pi + \dfrac{\pi}{2}$

Given the interval $x \in [0, 10\pi]$, the valid values for $x$ are:

For $x = 2m\pi$: $x = 0, 2\pi, 4\pi, 6\pi, 8\pi, 10\pi$ (6 solutions)

For $x = 2m\pi + \dfrac{\pi}{2}$: $x = \dfrac{\pi}{2}, \dfrac{5\pi}{2}, \dfrac{9\pi}{2}, \dfrac{13\pi}{2}, \dfrac{17\pi}{2}$ (5 solutions)

The total number of points of intersection is $n = 6 + 5 = 11$.

Answer: $11$

</details>

---

### Q2. JEE Advanced 2026 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Match each entry in List-I to the correct entry in List-II and choose the correct option.
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><th style="border: 1px solid black; padding: 10px;">List-I</th><th style="border: 1px solid black; padding: 10px;">List-II</th></tr><tr><td style="border: 1px solid black; padding: 10px;">(P) The number of elements in the set $\{x \in [-\pi, \pi] : \sin^6 x + \cos^4 x = 1\}$</td><td style="border: 1px solid black; padding: 10px;">(1) is $1$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">(Q) The number of elements in the set $\left\{x \in \left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right] : \sin^2 x + \cos^6 x = 1\right\}$</td><td style="border: 1px solid black; padding: 10px;">(2) is $2$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">(R) The number of elements in the set $\left\{x \in [-\pi, \pi] : \cos^2\left(\dfrac{x}{2}\right) - \sin^2 x = \dfrac{1}{2}\right\}$</td><td style="border: 1px solid black; padding: 10px;">(3) is $3$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">(S) The number of elements in the set $\left\{x \in [-2\pi, 2\pi] : 6\sin^2\left(\dfrac{x}{2}\right) - \cos 3x = 3\right\}$</td><td style="border: 1px solid black; padding: 10px;">(4) is $4$</td></tr><tr><td style="border: 1px solid black; padding: 10px;"></td><td style="border: 1px solid black; padding: 10px;">(5) is $5$</td></tr></table>

**Options:**

- **(A)** (P) $\rightarrow$ (2), (Q) $\rightarrow$ (5), (R) $\rightarrow$ (3), (S) $\rightarrow$ (4)
- **(B)** (P) $\rightarrow$ (5), (Q) $\rightarrow$ (3), (R) $\rightarrow$ (2), (S) $\rightarrow$ (4)
- **(C)** (P) $\rightarrow$ (5), (Q) $\rightarrow$ (4), (R) $\rightarrow$ (1), (S) $\rightarrow$ (3)
- **(D)** (P) $\rightarrow$ (4), (Q) $\rightarrow$ (3), (R) $\rightarrow$ (2), (S) $\rightarrow$ (5)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) (P) $\rightarrow$ (5), (Q) $\rightarrow$ (3), (R) $\rightarrow$ (2), (S) $\rightarrow$ (4)**

**Detailed Solution:**

For (P):
$\sin^6 x + \cos^4 x = 1$
$\sin^6 x + (1 - \sin^2 x)^2 = 1$
$\sin^6 x + 1 - 2\sin^2 x + \sin^4 x = 1$
$\sin^2 x (\sin^4 x + \sin^2 x - 2) = 0$
$\sin^2 x (\sin^2 x - 1)(\sin^2 x + 2) = 0$
This gives $\sin^2 x = 0$ or $\sin^2 x = 1$.
In the interval $[-\pi, \pi]$, the solutions are $x \in \{-\pi, -\dfrac{\pi}{2}, 0, \dfrac{\pi}{2}, \pi\}$.
Number of solutions = $5$.

For (Q):
$\sin^2 x + \cos^6 x = 1$
$1 - \cos^2 x + \cos^6 x = 1$
$\cos^2 x (\cos^4 x - 1) = 0$
This gives $\cos^2 x = 0$ or $\cos^2 x = 1$.
In the interval $\left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]$, the solutions are $x \in \left\{-\dfrac{\pi}{2}, 0, \dfrac{\pi}{2}\right\}$.
Number of solutions = $3$.

For (R):
$\cos^2\left(\dfrac{x}{2}\right) - \sin^2 x = \dfrac{1}{2}$
$\dfrac{1 + \cos x}{2} - (1 - \cos^2 x) = \dfrac{1}{2}$
$1 + \cos x - 2 + 2\cos^2 x = 1$
$2\cos^2 x + \cos x - 2 = 0$
Solving the quadratic equation for $\cos x$, we get:
$\cos x = \dfrac{-1 \pm \sqrt{17}}{4}$
Since $\cos x \in [-1, 1]$, we reject the negative root. Thus, $\cos x = \dfrac{\sqrt{17} - 1}{4}$.
Since $0 < \dfrac{\sqrt{17} - 1}{4} < 1$, there are exactly $2$ solutions in $[-\pi, \pi]$.
Number of solutions = $2$.

For (S):
$6\sin^2\left(\dfrac{x}{2}\right) - \cos 3x = 3$
$3(1 - \cos x) - (4\cos^3 x - 3\cos x) = 3$
$3 - 3\cos x - 4\cos^3 x + 3\cos x = 3$
$-4\cos^3 x = 0 \Rightarrow \cos x = 0$
In the interval $[-2\pi, 2\pi]$, the solutions are $x \in \left\{-\dfrac{3\pi}{2}, -\dfrac{\pi}{2}, \dfrac{\pi}{2}, \dfrac{3\pi}{2}\right\}$.
Number of solutions = $4$.

Therefore, the correct matching is (P) $\rightarrow$ (5), (Q) $\rightarrow$ (3), (R) $\rightarrow$ (2), (S) $\rightarrow$ (4).

Answer: (P) $\rightarrow$ (5), (Q) $\rightarrow$ (3), (R) $\rightarrow$ (2), (S) $\rightarrow$ (4)

</details>

---

### Q3. JEE Advanced 2024 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\frac{\pi}{2} < x < \pi$ be such that $\cot x=\frac{-5}{\sqrt{11}}$. Then $\left(\sin \frac{11 x}{2}\right)(\sin 6 x-\cos 6 x)+\left(\cos \frac{11 x}{2}\right)(\sin 6 x+\cos 6 x)$ is equal to

**Options:**

- **(A)** $\frac{\sqrt{11}-1}{2 \sqrt{3}}$
- **(B)** $\frac{\sqrt{11}+1}{2 \sqrt{3}}$
- **(C)** $\frac{\sqrt{11}+1}{3 \sqrt{2}}$
- **(D)** $\frac{\sqrt{11}-1}{3 \sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\sqrt{11}+1}{2 \sqrt{3}}$**

**Detailed Solution:**

Given,
$\begin{aligned} & \cot x=-\frac{5}{\sqrt{11}} \\
& \frac{1-\tan ^2 \frac{x}{2}}{2 \tan \frac{x}{2}}=-\frac{5}{\sqrt{11}} \\
& \tan \frac{x}{2}=\sqrt{11},-\frac{1}{\sqrt{11}} \\
& \text{So, } \tan \frac{x}{2}=\sqrt{11}, \text { As } \frac{\pi}{4} < \frac{x}{2} < \frac{\pi}{2}\end{aligned}$
$\begin{aligned} & \text{As, } x \in\left(\frac{\pi}{2}, \pi\right) \\
& \text{Now, } \left(\sin \frac{11 x}{2}\right)(\sin 6 x-\cos 6 x)+\left(\cos \frac{11 x}{2}\right)(\sin 6 x+\cos 6 x) \\
& =\left\{\sin 6 x \sin \frac{11 x}{2}+\cos \frac{11 x}{2} \cos 6 x \right\} \\
& =\cos \left(6 x-\frac{11 x}{2}\right)+\sin \left(6 x-\frac{11 x}{2}\right) \\
& =\cos \frac{x}{2}+\sin \frac{x}{2} \\
& =\frac{1}{2 \sqrt{3}}+\frac{\sqrt{11}}{2 \sqrt{3}} \\
& =\frac{\sqrt{11}+1}{2 \sqrt{3}} \Rightarrow \text { Option (2) is correct. }\end{aligned}$

</details>

---

### Q4. JEE Advanced 2023 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

For any <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>y</mi></mfenced><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>y</mi></mfenced><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>. Then the sum of all the solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>6</mn><mi>y</mi></mrow><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>+</mo><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mrow><mn>6</mn><mi>y</mi></mrow></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mo>|</mo><mi>y</mi><mo>|</mo><mo>&#60;</mo><mn>3</mn></math>, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>-</mo><mn>4</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>6</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>6</mn><mi>y</mi></mrow><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>+</mo><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mrow><mn>6</mn><mi>y</mi></mrow></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mo>|</mo><mi>y</mi><mo>|</mo><mo>&#60;</mo><mn>3</mn><mo>&#8658;</mo><mi>y</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mfenced close="}" open="{"><mn>0</mn></mfenced></math></p><p>Now taking, <strong>Case-l:</strong></p><p>When <strong><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>6</mn><mi>y</mi></mrow><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac><mo>&#62;</mo><mn>0</mn><mo>&#8658;</mo><mi>y</mi><mo>&#62;</mo><mn>0</mn></math></strong></p><p><strong><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced separators="|"><mfrac><mrow><mn>6</mn><mi>y</mi></mrow><mrow><mn>9</mn><mo>&#8722;</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced separators="|"><mfrac><mrow><mn>6</mn><mi>y</mi></mrow><mrow><mn>9</mn><mo>&#8722;</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math></strong></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>6</mn><mi>y</mi></mrow><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>6</mn><mi>y</mi></mrow><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>6</mn><mi>y</mi></mrow><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi>y</mi><mo>=</mo><mn>9</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>3</mn></msqrt><msup><mi>y</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>3</mn></msqrt><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>y</mi><mo>-</mo><mn>9</mn><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>3</mn></msqrt><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn><mi>y</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>9</mn><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>y</mi><mo>+</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced><mfenced><mrow><msqrt><mn>3</mn></msqrt><mi>y</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8800;</mo><mo>-</mo><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>&#160;&#160;</mo><mo>&#8756;</mo><menclose notation="box"><mi>y</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></menclose></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8712;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>3</mn><mo>)</mo></math></p><p>Now taking, <strong>Case-II: </strong></p><p>When<strong> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>6</mn><mi>y</mi></mrow><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac><mo>&#60;</mo><mn>0</mn><mo>&#8658;</mo><mi>y</mi><mo>&#60;</mo><mn>0</mn></math></strong></p><p><strong><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>6</mn><mi>y</mi></mrow><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>+</mo><mi>&#960;</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>6</mn><mi>y</mi></mrow><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math></strong></p><p><strong><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>6</mn><mi>y</mi></mrow><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>=</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math></strong></p><p><strong><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>6</mn><mi>y</mi></mrow><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>=</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math></strong></p><p><strong><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>6</mn><mi>y</mi></mrow><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></strong></p><p><strong><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><msqrt><mn>3</mn></msqrt><mi>y</mi><mo>=</mo><mo>-</mo><mn>9</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></math></strong></p><p><strong><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><msqrt><mn>3</mn></msqrt><mi>y</mi><mo>-</mo><mn>9</mn><mo>=</mo><mn>0</mn></math></strong></p><p><strong><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>6</mn><msqrt><mn>3</mn></msqrt><mo>&#177;</mo><msqrt><mn>108</mn><mo>+</mo><mn>36</mn></msqrt></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>6</mn><msqrt><mn>3</mn></msqrt><mo>&#177;</mo><mn>12</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>&#177;</mo><mn>6</mn></math></strong></p><p><strong><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#160;As&#160;</mtext><mi>y</mi><mo>&#8712;</mo><mo>(</mo><mo>&#8722;</mo><mn>3</mn><mo>.0</mo><mo>)</mo><mo>,</mo><mo>&#160;</mo><mtext>so</mtext><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>&#8722;</mo><mn>6</mn></math></strong></p><p><strong><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mtext>&#160;Sum of solutions&#160;</mtext><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><mo>(</mo><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>&#8722;</mo><mn>6</mn><mo>)</mo><mo>=</mo><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>&#8722;</mo><mn>6</mn></math></strong></p></blockquote>

</details>

---

### Q5. JEE Advanced 2023 (Paper 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>. Then the number of real solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>+</mo><mi>cos</mi><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced></msqrt><mo>=</mo><msqrt><mn>2</mn></msqrt><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>tan</mi><mi>x</mi></mrow></mfenced></math> in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></mrow></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></msqrt><mo>=</mo><msqrt><mn>2</mn></msqrt><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>tan</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></msqrt><mo>=</mo><msqrt><mn>2</mn></msqrt><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>tan</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>tan</mi><mi>x</mi></mrow></mfenced></math></p><p>Now plotting the diagram of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>tan</mi><mi>x</mi></mrow></mfenced></math> we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/e8bc4c98-2dc0-4411-b78b-02a23399895f.png" style="width: 300px; height: 205px;" /></p><p>Now from above diagram we can say that,</p><p>Number of solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> Number of intersection points <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn></math></p></blockquote>

</details>

---

### Q6. JEE Advanced 2022 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Consider the following lists:</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td>List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math></td>			<td> </td>			<td>List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>:</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">P</mi></mfenced></math></td>			<td>has two elements</td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>II</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></mrow></mfenced><mo>:</mo><msqrt><mn>3</mn></msqrt><mi>tan</mi><mn>3</mn><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">Q</mi></mfenced></math></td>			<td>has three elements</td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>III</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mfrac><mrow><mn>6</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mn>6</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac></mrow></mfenced><mo>:</mo><mn>2</mn><mi>cos</mi><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">R</mi></mfenced></math></td>			<td>has four elements</td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>IV</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced><mo>:</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">S</mi></mfenced></math></td>			<td>has five elements</td>		</tr>		<tr>			<td> </td>			<td> </td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">T</mi></mfenced></math></td>			<td>has six elements</td>		</tr>	</tbody></table><p>The correct option is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">P</mi></mfenced><mo>;</mo><mfenced><mi>II</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">S</mi></mfenced><mo>;</mo><mfenced><mi>III</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">P</mi></mfenced><mo>;</mo><mfenced><mi>IV</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">S</mi></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">P</mi></mfenced><mo>;</mo><mfenced><mi>II</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">P</mi></mfenced><mo>;</mo><mfenced><mi>III</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">T</mi></mfenced><mo>;</mo><mfenced><mi>IV</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">R</mi></mfenced><mi></mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">Q</mi></mfenced><mo>;</mo><mfenced><mi>II</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">P</mi></mfenced><mo>;</mo><mfenced><mi>III</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">T</mi></mfenced><mo>;</mo><mfenced><mi>IV</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">S</mi></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">Q</mi></mfenced><mo>;</mo><mfenced><mi>II</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">S</mi></mfenced><mo>;</mo><mfenced><mi>III</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">P</mi></mfenced><mo>;</mo><mfenced><mi>IV</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">R</mi></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">P</mi></mfenced><mo>;</mo><mfenced><mi>II</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">P</mi></mfenced><mo>;</mo><mfenced><mi>III</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">T</mi></mfenced><mo>;</mo><mfenced><mi>IV</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">R</mi></mfenced><mi></mi></math>**

**Detailed Solution:**

<blockquote><p>Solving all questions one by one we get,</p><p>(i) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mrow><mo>-</mo><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>,</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mi>x</mi><mo>=</mo><mi>n</mi><mi>&#960;</mi><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mi>n</mi><mi>&#960;</mi><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> elements.<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mi>P</mi></math></p><p>(ii)  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mrow><mo>-</mo><mn>5</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></mrow></mfenced><mo>:</mo><msqrt><mn>3</mn></msqrt><mi>tan</mi><mn>3</mn><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mi>tan</mi><mn>3</mn><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mn>3</mn><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>x</mi><mo>=</mo><mi>n</mi><mi>&#960;</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mi>n</mi><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>18</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>18</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>5</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>18</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> elements.    <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mi>P</mi></math></p><p>(iii) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mrow><mo>-</mo><mn>6</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mn>6</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac></mrow></mfenced><mo>:</mo><mn>2</mn><mi>cos</mi><mn>2</mn><mi>x</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>cos</mi><mn>2</mn><mi>x</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mn>2</mn><mi>x</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mo>=</mo><mn>2</mn><mi>n</mi><mi>&#960;</mi><mo>&#177;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mi>n</mi><mi>&#960;</mi><mo>&#177;</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mo>&#177;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>12</mn></mfrac><mo>,</mo><mi mathvariant="normal">&#960;</mi><mo>&#177;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>12</mn></mfrac><mo>,</mo><mo>-</mo><mi mathvariant="normal">&#960;</mi><mo>&#177;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>12</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> elements.<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mi>T</mi></math></p><p>(iv) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mrow><mo>-</mo><mn>7</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced><mo>:</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>=</mo><mi>n</mi><mi>&#960;</mi><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mi>n</mi><mi>&#960;</mi><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mi mathvariant="normal">&#960;</mi><mo>,</mo><mo>-</mo><mi mathvariant="normal">&#960;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> elements.     <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> option <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is correct.</p></blockquote>

</details>

---

### Q7. JEE Advanced 2017 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><mi>&#945;</mi></math> and <math><mi>&#946;</mi></math> be non zero real numbers such that <math><mn>2</mn><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#946;</mi></mrow></mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#945;</mi></mrow></mrow></mrow></mfenced><mo>+</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#945;</mi></mrow></mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#946;</mi></mrow></mrow><mo>=</mo><mn>1</mn></math>. Then which of the following is/are true?

**Options:**

- **(A)** <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>&alpha;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>-</mo><msqrt><mn>3</mn></msqrt><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>&beta;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math>
- **(B)** <math><msqrt><mn>3</mn></msqrt><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>β</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>&alpha;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><msqrt><mn>3</mn></msqrt><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>&beta;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math>
- **(D)** <math><msqrt><mn>3</mn></msqrt><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>β</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>&alpha;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><msqrt><mn>3</mn></msqrt><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>&beta;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p><math><mn>2</mn><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>&beta;</mi></mrow></mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>&alpha;</mi></mrow></mrow></mrow></mfenced><mo>+</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>&alpha;</mi></mrow></mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>&beta;</mi></mrow></mrow><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>        .....(i)</p><p>Use   <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>&beta;</mi></mrow></mrow><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>&beta;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow></mrow><mrow><mn>1</mn><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>&beta;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow></mrow></mfrac><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mrow><mrow><mi mathvariant="normal"> cos</mi></mrow><mo>⁡</mo><mrow><mi>&alpha;</mi></mrow></mrow><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>&alpha;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow></mrow><mrow><mn>1</mn><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>&alpha;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow></mrow></mfrac></math> in (i)</p><p>We get <math><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>&alpha;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mn>3</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>&beta;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mi> </mi><mo>&rArr;</mo><mi> </mi><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>&alpha;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><msqrt><mn>3</mn></msqrt><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>&beta;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow><mo>=</mo><mn>0</mn><mi> </mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi><mrow><mrow><mi mathvariant="normal"> tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>&alpha;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>-</mo><mi> </mi><msqrt><mn>3</mn></msqrt><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>&beta;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q8. JEE Advanced 2016 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>S</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mo>-</mo><mi>&#960;</mi><mo>,</mo><mi>&#160;</mi><mi>&#960;</mi></mrow></mfenced><mo>:</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mo>&#177;</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> . The sum of all distinct solution of the equation <math><msqrt><mn>3</mn></msqrt><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mi>c</mi><mi>o</mi><mi>s</mi><mi>e</mi><mi>c</mi><mi>&#160;</mi><mi>x</mi><mo>+</mo><mn>2</mn><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced><mo>=</mo><mn>0</mn></math>, in the set S is equal to

**Options:**

- **(A)** <math><mo>-</mo><mfrac><mrow><mn>7</mn><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac></math>
- **(B)** <math><mo>-</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac></math>
- **(C)** <math><mn>0</mn></math>
- **(D)** <math><mfrac><mrow><mn>5</mn><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>0</mn></math>**

**Detailed Solution:**

<math><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mi mathvariant="normal">Cosx</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">Sinx</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi mathvariant="normal"> </mi><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">Sinx</mi></mrow><mrow><mi mathvariant="normal">cosx</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi mathvariant="normal">Cosx</mi></mrow><mrow><mi mathvariant="normal">sinx</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn><mi mathvariant="normal"> </mi></math>
<math><msqrt><mn>3</mn></msqrt><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>=</mo><mn>2</mn><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow></math>
<math><mo>&#8658;</mo></math> <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow><mo>=</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mo>=</mo><mn>2</mn><mi>n</mi><mi>&#960;</mi><mo>&#177;</mo><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></math>,<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>2</mn><mi>x</mi><mo>=</mo><mn>2</mn><mi>n</mi><mi>&#960;</mi><mo>+</mo><mi>x</mi><mo>&#8722;</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>=</mo><mn>2</mn><mi>n</mi><mi>&#960;</mi><mo>&#8722;</mo><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mtd></mtr></mtable></mfenced></math>
<math><mi>&#8658;&#160;x</mi><mo>=</mo><mfenced separators="|"><mrow><mn>6</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math> or <math><mfenced separators="|"><mrow><mn>6</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>9</mn></mrow></mfrac></math>
<math><mo>&#8658;</mo></math> <math><mi>x</mi><mo>=</mo><mi>&#160;</mi><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>9</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mrow><mn>9</mn></mrow></mfrac></math> and <math><mo>-</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mrow><mn>9</mn></mrow></mfrac></math> in <math><mfenced separators="|"><mrow><mo>-</mo><mi>&#960;</mi><mo>,</mo><mi>&#160;</mi><mi>&#960;</mi></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#8658;</mo><mi>s</mi><mi>u</mi><mi>m</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn></math>

</details>

---

### Q9. JEE Advanced 2015 (Paper 1)

*Type:* `numerical` | *Level:* `2`

The number of distinct solutions of the equation <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#160;</mi><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>6</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>6</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">x</mi><mo>=</mo><mn>2</mn></mrow></mrow></mrow></mrow></mrow></mrow></mrow></mrow></mrow></mrow></math> in the interval <math><mo>[</mo><mn>0</mn><mo>,</mo><mi mathvariant="normal">&#160;</mi><mn>2</mn><mi mathvariant="normal">&#960;</mi><mo>]</mo></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo></mrow></mrow><msup><mrow><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">x</mi></mrow></mrow><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">x</mi></mrow></mrow></mrow></mrow></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>5</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">x</mi></mrow></mrow><mo>.</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">x</mi></mrow></mrow><mo>=</mo><mn>2</mn></math>
<math><mo>&#8658;</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi mathvariant="normal">x</mi></mrow></mrow></mrow></mfenced><mo>-</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>2</mn></mrow></mrow></math>
<math><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mn>2</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi mathvariant="normal">x</mi></mrow></mrow><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi mathvariant="normal">x</mi><mo>=</mo></mrow></mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi mathvariant="normal">&#160;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo>=</mo><mi>n</mi><mi mathvariant="normal">&#960;</mi><mo>&#177;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math>
<math><mo>&#8658;</mo><mi mathvariant="normal">x</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">n</mi><mi mathvariant="normal">&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#177;</mo><mfrac><mrow><mi mathvariant="normal">&#960;</mi></mrow><mrow><mn>8</mn></mrow></mfrac></math>
Number of solution = 8

</details>

---

### Q10. JEE Advanced 2014 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

For <math><mi mathvariant="normal">x</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#1013;</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#160;</mi><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#960;</mi></mrow></mfenced><mo>,</mo></math> the equation <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mn>2</mn><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi mathvariant="normal">x</mi><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>3</mn><mi mathvariant="normal">x</mi><mo>=</mo><mn>3</mn></mrow></mrow></mrow></mrow></mrow></mrow></math> has

**Options:**

- **(A)** Infinitely solution
- **(B)** Three solutions
- **(C)** One solution
- **(D)** No solution

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) No solution**

**Detailed Solution:**

<math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mn>3</mn><mi>x</mi><mo>=</mo><mn>3</mn></mrow></mrow></mrow></mrow></mrow></mrow></math>  
 <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mn>4</mn><mi> </mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>-</mo><mn>3</mn><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mn>4</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>=</mo><mn>3</mn></mrow></mrow><mi> </mi></mrow></mrow></mrow></mrow></mrow></mrow></mrow></mrow><mi> </mi></math>  
 <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mi> </mi><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mn>2</mn><mo>+</mo><mn>4</mn><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mn>4</mn><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow></mrow></mfenced><mo>=</mo><mn>3</mn></mrow></mrow></math>  
 <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mi> </mi><mfenced close="]" open="[" separators="|"><mrow><mn>2</mn><mo>-</mo><mfenced separators="|"><mrow><mn>4</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>-</mo><mn>4</mn><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mrow></mrow></mrow></mrow></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>3</mn></mrow></mrow></math>  
 <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mi> </mi><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mn>3</mn><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mrow></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi> </mi></mrow></msup><mo>=</mo><mn>3</mn></mrow></mrow></math>  
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn><mi> </mi><mi>a</mi><mi>n</mi><mi>d</mi><mi> </mi><mn>2</mn><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></mrow></mrow></mrow></mrow></math>  
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mi> </mi><mi> </mi><mi>a</mi><mi>n</mi><mi>d</mi><mi> </mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>  
Which is not possible at same time
Hence, no solution

</details>

---

### Q11. JEE Advanced 2011 (Paper 1)

*Type:* `numerical` | *Level:* `3`

The positive integer value of $n>3$ satisfying the equation
$$
\frac{1}{\sin \left(\frac{\pi}{n}\right)}=\frac{1}{\sin \left(\frac{2 \pi}{n}\right)}+\frac{1}{\sin \left(\frac{3 \pi}{n}\right)} \text { is }
$$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

Given, $n>3 \in$ Integer
$$
\begin{aligned}
& \text { and } \frac{1}{\sin \left(\frac{\pi}{n}\right)}=\frac{1}{\sin \left(\frac{2 \pi}{n}\right)}+\frac{1}{\sin \left(\frac{3 \pi}{n}\right)} \\
& \Rightarrow \frac{1}{\sin \frac{\pi}{n}}-\frac{1}{\sin \frac{3 \pi}{n}}=\frac{1}{\sin \frac{2 \pi}{n}} \\
& \Rightarrow \quad \frac{\sin \frac{3 \pi}{n}-\sin \frac{\pi}{n}}{\sin \frac{\pi}{n} \cdot \sin \frac{3 \pi}{n}}=\frac{1}{\sin \frac{2 \pi}{n}}
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow \quad 2 \cos \left(\frac{2 \pi}{n}\right) \cdot \sin \frac{\pi}{n}=\frac{\sin \frac{\pi}{n} \cdot \sin \frac{3 \pi}{n}}{\sin \frac{2 \pi}{n}} \\
& \Rightarrow \quad 2 \sin \frac{2 \pi}{n} \cdot \cos \frac{2 \pi}{n}=\sin \frac{3 \pi}{n} \\
& \Rightarrow \quad \quad \sin \frac{4 \pi}{n}=\sin \frac{3 \pi}{n} \\
& \Rightarrow \frac{4 \pi}{n}=\pi-\frac{3 \pi}{n} \Rightarrow \frac{7 \pi}{n}=\pi \Rightarrow n=7
\end{aligned}
$$

</details>

---

### Q12. JEE Advanced 2011 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $P=\{\theta: \sin \theta-\cos \theta=\sqrt{2} \cos \theta\}$ and $Q=\{\theta: \sin \theta+\cos \theta=\sqrt{2} \sin \theta\}$ be two sets. Then,

**Options:**

- **(A)** $P \subset Q$ and $Q-P \neq \Phi$
- **(B)** $Q \not \subset P$
- **(C)** $P \not \subset Q$
- **(D)** $P=Q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $P=Q$**

**Detailed Solution:**

$$
\begin{aligned}
& P=\{\theta: \sin \theta-\cos \theta=\sqrt{2} \cos \theta\} \\
& \Rightarrow \quad \cos \theta(\sqrt{2}+1)=\sin \theta \\
& \Rightarrow \quad \tan \theta=\sqrt{2}+1 \\
& Q=\{\theta: \sin \theta+\cos \theta=\sqrt{2} \sin \theta\} \\
& \Rightarrow \quad \sin \theta(\sqrt{2}-1)=\cos \theta \\
& \Rightarrow \quad \tan \theta=\frac{1}{\sqrt{2}-1} \times \frac{\sqrt{2}+1}{\sqrt{2}+1} \\
& =(\sqrt{2}+1) \\
& \therefore \quad P=Q \\
&
\end{aligned}
$$

</details>

---

### Q13. JEE Advanced 2010 (Paper 1)

*Type:* `numerical` | *Level:* `1`

The number of values of $\theta$ in the interval $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ such that $\theta \neq \frac{n \pi}{5}$ for $n=0, \pm 1, \pm 2$ and $\tan \theta=\cot 5 \theta$ as well as $\sin 2 \theta=\cos 4 \theta$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

Given, $\tan \theta=\cot 5 \theta$
$$
\begin{aligned}
& \Rightarrow \quad \tan \theta=\tan \left(\frac{\pi}{2}-5 \theta\right) \\
& \Rightarrow \quad \frac{\pi}{2}-5 \theta=n \pi+\theta \\
& \Rightarrow \quad 6 \theta=\frac{\pi}{2}-n \pi \\
& \Rightarrow \quad \theta=\frac{\pi}{12}-\frac{n \pi}{6} \\
& \text { Also, } \cos 4 \theta=\sin 2 \theta=\cos \left(\frac{\pi}{2}-2 \theta\right) \\
& \Rightarrow \quad 4 \theta=2 n \pi \pm\left(\frac{\pi}{2}-2 \theta\right)
\end{aligned}
$$
Taking positive
$$
6 \theta=2 n \pi+\frac{\pi}{2} \Rightarrow \theta=\frac{n \pi}{3}+\frac{\pi}{12}
$$
Taking negative
$$
2 \theta=2 n \pi-\frac{\pi}{2} \Rightarrow \theta=n \pi-\frac{\pi}{4}
$$
Above values of $\theta$ suggests that there are only 3 common solutions.

</details>

---

### Q14. JEE Advanced 2010 (Paper 1)

*Type:* `numerical` | *Level:* `2`

The number of all possible values of $\theta$, where $0 < \theta < \pi$, for which the system of equations
$$
\begin{array}{r}
(y+z) \cos 3 \theta=(x y z) \sin 3 \theta \\
x \sin 3 \theta=\frac{2 \cos 3 \theta}{y}+\frac{2 \sin 3 \theta}{z}
\end{array}
$$
and $(x y z) \sin 3 \theta=(y+2 z) \cos 3 \theta$
$+y \sin 3 \theta$
have a solution $\left(x_0, y_0, z_0\right)$
with $\quad y_0 z_0 \neq 0$, is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

Given equations can be written as
$$
\begin{gathered}
x \sin 3 \theta-\frac{\cos 3 \theta}{y}-\frac{\cos 3 \theta}{z}=0 \\
x \sin 3 \theta-\frac{2 \cos 3 \theta}{y}-\frac{2 \sin 3 \theta}{z}=0 \\
\text { and } x \sin 3 \theta-\frac{2}{y} \cos 3 \theta \\
-\frac{1}{z}(\cos 3 \theta+\sin 3 \theta)=0
\end{gathered}
$$
Eqs. (ii) and (iii), implies
$$
\begin{aligned}
& 2 \sin 3 \theta=\cos 3 \theta+\sin 3 \theta \\
\Rightarrow & \sin 3 \theta=\cos 3 \theta \\
\therefore & \tan 3 \theta=1 \\
\Rightarrow & 3 \theta=\frac{\pi}{4}, \frac{5 \pi}{4}, \frac{9 \pi}{4} \text { or } \theta=\frac{\pi}{12}, \frac{5 \pi}{12}, \frac{9 \pi}{12} .
\end{aligned}
$$

</details>

---

### Q15. JEE Advanced 2009 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

For $0 < \theta < \frac{\pi}{2}$, the solution(s) of $\sum_{m=1}^6 \operatorname{cosec}\left[\theta+\frac{(m-1) \pi}{4}\right]$ $\operatorname{cosec}\left(\theta+\frac{m \pi}{4}\right)=4 \sqrt{2}$ is/are

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{6}$
- **(C)** $\frac{\pi}{12}$
- **(D)** $\frac{5 \pi}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{5 \pi}{12}$**

**Detailed Solution:**

For $0 < \theta < \frac{\pi}{2}$,
$$
\begin{array}{r}
\sum_{m=1}^6 \operatorname{cosec}\left[\theta+\frac{(m-1) \pi}{4}\right] \operatorname{cosec}\left(\theta+\frac{m \pi}{4}\right) \\
=4 \sqrt{2} \\
\Rightarrow \sum_{m=1}^6 \frac{\sin \left[\theta+\frac{m \pi}{4}-\left(\theta+\frac{(m-1) \pi}{4}\right)\right]}{\sin \frac{\pi}{4}\left\{\sin \left(\theta+\frac{(m-1) \pi}{4}\right) \sin \left(\theta+\frac{m \pi}{4}\right)\right\}} \\
=4 \sqrt{2}
\end{array}
$$

$$
\begin{array}{r}
\Rightarrow \sum_{m=1}^6 \frac{\cot \left(\theta+\frac{(m-1) \pi}{4}\right)-\cot \left(\theta+\frac{m \pi}{4}\right)}{1 / 2} \\
=4 \sqrt{2}
\end{array}
$$

$$
\begin{aligned}
& \Rightarrow \quad \sum_{m=1}^6\left[\cot \left(\theta+\frac{(m-1) \pi}{4}\right)\right. \\
& \left.-\cot \left(\theta+\frac{m \pi}{4}\right)\right]=4 \\
& \Rightarrow \cot (\theta)-\cot \left(\theta+\frac{\pi}{4}\right)+\cot \left(\theta+\frac{\pi}{4}\right) \\
& -\cot \left(\theta+\frac{2 \pi}{4}\right)+\ldots+\cot \left(\theta+\frac{5 \pi}{4}\right) \\
& -\cot \left(\theta+\frac{6 \pi}{4}\right)=4 \\
& \Rightarrow \quad \cot \theta-\cot \left(\frac{3 \pi}{2}+\theta\right)=4 \\
& \Rightarrow \quad \cot \theta+\tan \theta=4 \\
& \Rightarrow \quad \tan ^2 \theta-4 \tan \theta+1=0 \\
& \Rightarrow \quad(\tan \theta-2)^2-3=0 \\
& \Rightarrow(\tan \theta-2+\sqrt{3})(\tan \theta-2-\sqrt{3})=0 \\
& \Rightarrow \quad \tan \theta=2-\sqrt{3} \text { or } \\
& \tan \theta=2+\sqrt{3} \\
& \Rightarrow \theta=\frac{\pi}{12} ; \theta=\frac{5 \pi}{12} \Rightarrow \theta \in\left(0, \frac{\pi}{2}\right) \\
&
\end{aligned}
$$

</details>

---

### Q16. JEE Advanced 2009 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `1`

If $\frac{\sin ^4 x}{2}+\frac{\cos ^4 x}{3}=\frac{1}{5}$, then

**Options:**

- **(A)** $\tan ^2 x=\frac{2}{3}$
- **(B)** $\frac{\sin ^8 x}{8}+\frac{\cos ^8 x}{27}=\frac{1}{125}$
- **(C)** $\tan ^2 x=\frac{1}{3}$
- **(D)** $\frac{\sin ^8 x}{8}+\frac{\cos ^8 x}{27}=\frac{2}{125}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\sin ^8 x}{8}+\frac{\cos ^8 x}{27}=\frac{1}{125}$**

**Detailed Solution:**

$$
\begin{aligned}
& \frac{\sin ^4 x}{2}+\frac{\cos ^4 x}{3}=\frac{1}{5} \\
& \Rightarrow \quad \frac{\sin ^4 x}{2}+\frac{\left(1-\sin ^2 x\right)^2}{3}=\frac{1}{5} \\
& \Rightarrow \frac{\sin ^4 x}{2}+\frac{1+\sin ^4 x-2 \sin ^2 x}{3}=\frac{1}{5} \\
& \Rightarrow \quad 5 \sin ^4 x-4 \sin ^2 x+2=\frac{6}{5} \\
& \Rightarrow \quad 25 \sin ^4 x-20 \sin ^2 x+4=0 \\
& \Rightarrow \quad\left(5 \sin ^2 x-2\right)^2=0 \\
& \Rightarrow \sin ^2 x=\frac{2}{5}, \cos ^2 x=\frac{3}{5}, \tan ^2 x=\frac{2}{3} \\
& \therefore \quad \frac{\sin ^8 x}{8}+\frac{\cos ^8 x}{27}=\frac{1}{125} \\
&
\end{aligned}
$$

</details>

---

### Q17. JEE Advanced 2007 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

The number of solutions of the pair of equations $2 \sin ^2 \theta-\cos 2 \theta=0$ and $2 \cos ^2 \theta-3 \sin \theta=0$ in the interval $[0,2 \pi]$ is

**Options:**

- **(A)** zero
- **(B)** one
- **(C)** two
- **(D)** four

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) two**

**Detailed Solution:**

$2 \sin ^2 \theta-\cos 2 \theta=0 \Rightarrow \sin ^2 \theta=\frac{1}{4}$
Also, $2 \cos ^2 \theta=3 \sin \theta \Rightarrow \sin \theta=\frac{1}{2}$
$\Rightarrow$ Two solutions in $[0,2 \pi]$.

</details>

---

