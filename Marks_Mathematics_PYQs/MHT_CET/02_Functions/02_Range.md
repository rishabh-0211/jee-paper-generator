# MHT CET Mathematics - Functions

## Topic 2: Range

**Total Questions:** 12

---

### Q1. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x) = \{x\}$ represents the fractional part function, then for any $x \notin \mathbb{Z}$, the expression $f(x) + f(-x)$ is equal to...

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $2\{x\}$
- **(D)** $x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1$**

**Detailed Solution:**

The fractional part function is defined as $\{x\} = x - [x]$, where $[x]$ is the greatest integer function.

Substituting this into the given expression:

$f(x) + f(-x) = \{x\} + \{-x\}$

$f(x) + f(-x) = (x - [x]) + (-x - [-x])$

$f(x) + f(-x) = -([x] + [-x])$

For any non-integer $x \notin \mathbb{Z}$, the sum of the greatest integer functions of $x$ and $-x$ is a standard property:

$[x] + [-x] = -1$

Substituting this value back into the expression:

$f(x) + f(-x) = -(-1) = 1$

Answer: $1$

</details>

---

### Q2. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f: R \to R$ be defined by $f(x) = \dfrac{x^2 + 2x + 3}{x^2 + x + 1}$. If the range of $f(x)$ is $[a, b]$, then $a + b = \ldots$

**Options:**

- **(A)** $2$
- **(B)** $4$
- **(C)** $\dfrac{4}{\sqrt{3}}$
- **(D)** $2\sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4$**

**Detailed Solution:**

Let $y = \dfrac{x^2 + 2x + 3}{x^2 + x + 1}$

Cross-multiplying, we get:

$y(x^2 + x + 1) = x^2 + 2x + 3$

$(y - 1)x^2 + (y - 2)x + (y - 3) = 0$

Since $x \in R$, the discriminant of this quadratic equation must be greater than or equal to zero ($D \ge 0$):

$(y - 2)^2 - 4(y - 1)(y - 3) \ge 0$

$y^2 - 4y + 4 - 4(y^2 - 4y + 3) \ge 0$

$y^2 - 4y + 4 - 4y^2 + 16y - 12 \ge 0$

$-3y^2 + 12y - 8 \ge 0$

$3y^2 - 12y + 8 \le 0$

The roots of the equation $3y^2 - 12y + 8 = 0$ give the minimum and maximum values of $y$, which are $a$ and $b$ respectively. Thus, the range of $f(x)$ is $[a, b]$.

The sum of the roots of the quadratic equation $3y^2 - 12y + 8 = 0$ is given by:

$a + b = -\dfrac{-12}{3} = 4$

Answer: $4$

</details>

---

### Q3. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The Range of the function $y=\log(\sin x)$, defined for all $x$ such that $\sin x>0$ is ...

**Options:**

- **(A)** $(-\infty, 0]$
- **(B)** $(-\infty, 0)$
- **(C)** $R$
- **(D)** $(0, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(-\infty, 0]$**

**Detailed Solution:**

Given the function $y = \log(\sin x)$.

For the function to be defined, we must have $\sin x > 0$.

We know that the maximum value of $\sin x$ is $1$. Therefore, the possible values for $\sin x$ lie in the interval $(0, 1]$.

Let $t = \sin x$, which gives $t \in (0, 1]$.

The function becomes $y = \log(t)$.

As $t$ approaches $0$ from the positive side, $\log(t)$ approaches $-\infty$.

When $t = 1$, $\log(1) = 0$.

Since the logarithmic function is strictly increasing, the values of $y$ will lie in the interval $(-\infty, 0]$.

Thus, the range of the function is $(-\infty, 0]$.

Answer: $(-\infty, 0]$

</details>

---

### Q4. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Range of the function $\mathrm{f}(x)=\frac{x^2+x+2}{x^2+x+1}, x \in \mathbb{R}$ is

**Options:**

- **(A)** $\left(1, \frac{7}{3}\right)$
- **(B)** $\left[1, \frac{7}{3}\right)$
- **(C)** $\left[1, \frac{7}{3}\right]$
- **(D)** $\left(1, \frac{7}{3}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(1, \frac{7}{3}\right]$**

**Detailed Solution:**

Given function is $f(x) = \dfrac{x^2+x+2}{x^2+x+1}$

We can rewrite $f(x)$ as:

$f(x) = \dfrac{x^2+x+1+1}{x^2+x+1} = 1 + \dfrac{1}{x^2+x+1}$

Let $g(x) = x^2+x+1$. Completing the square, we get:

$g(x) = \left(x+\dfrac{1}{2}\right)^2 + \dfrac{3}{4}$

Since $\left(x+\dfrac{1}{2}\right)^2 \ge 0$ for all $x \in \mathbb{R}$, the minimum value of $g(x)$ is $\dfrac{3}{4}$.

As $x \to \pm\infty$, $g(x) \to \infty$.

Thus, the range of $g(x)$ is $\left[\dfrac{3}{4}, \infty\right)$.

Taking the reciprocal, we get:

$0 < \dfrac{1}{g(x)} \le \dfrac{4}{3}$

Adding $1$ to all parts of the inequality:

$1 < 1 + \dfrac{1}{g(x)} \le 1 + \dfrac{4}{3}$

$1 < f(x) \le \dfrac{7}{3}$

Therefore, the range of the function is $\left(1, \dfrac{7}{3}\right]$.

Answer: $\left(1, \frac{7}{3}\right]$

</details>

---

### Q5. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The range of the function $\mathrm{f}(x)=\frac{x^2}{x^2+1}$ is

**Options:**

- **(A)** $(0,1)$
- **(B)** $[0,1)$
- **(C)** $(0,1]$
- **(D)** $[0,1]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $[0,1)$**

**Detailed Solution:**

$$
\begin{aligned}
& \text { Let } y=\frac{x^2}{x^2+1} \\
& \Rightarrow y x^2+y=x^2 \\
& \Rightarrow x^2(y-1)+y=0 \\
& \Rightarrow x^2=\frac{y}{1-y}
\end{aligned}
$$

For $x$ to be real,
$$
\begin{aligned}
& y(1-y) \geq 0 \text { and } 1-y \neq 0 \\
& \Rightarrow y(y-1) \leq 0 \text { and } y \neq 1 \\
& \Rightarrow 0 \leq y < 1
\end{aligned}
$$

</details>

---

### Q6. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For all real $x$, the minimum value of $\frac{1-x+x^2}{1+x+x^2}$ is

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $\frac{1}{3}$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{3}$**

**Detailed Solution:**

$\begin{aligned} & f(x)=\frac{1-x+x^2}{1+x+x^2} \\ \therefore \quad & f^{\prime}(x)=\frac{\left(1+x+x^2\right)(-1+2 x)-\left(1-x+x^2\right)(1+2 x)}{\left(1+x+x^2\right)^2} \\ = & \frac{\left(-1+2 x-x+2 x^2-x^2+2 x^3\right)}{\left(1+x+x^2\right)^2} \\ = & \frac{-2+2 x^2}{\left(1+x+x^2\right)^2}\end{aligned}$
If $\mathrm{f}^{\prime}(x)=0$, then $\frac{-2+2 x^2}{\left(1+x+x^2\right)^2}=0 \Rightarrow x^2=1$
$\Rightarrow x= \pm 1$
$\therefore \quad \mathrm{f}(x)$ at $x=1$ is $\frac{1}{3}$ and $\mathrm{f}(x)$ at $x=-1$ is 1 ,
$\therefore \quad$ Minimum value of $\mathrm{f}(x)$ is $\frac{1}{3}$.

</details>

---

### Q7. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Range of the function $\mathrm{f}(\mathrm{x})=3+2^{\mathrm{x}}+4^{\mathrm{x}}$ is

**Options:**

- **(A)** $(3, \infty)$
- **(B)** $(-\infty, \infty)$
- **(C)** $(3, \infty)$
- **(D)** $(-\infty, 3)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(3, \infty)$**

**Detailed Solution:**

$$
f(x)=3+2^x+4^x=y
$$
Let $2^{\mathrm{x}}=\mathrm{a} \Rightarrow 4^{\mathrm{x}}=\mathrm{a}^2$
$$
\therefore \mathrm{a}^2+\mathrm{a}+(3-\mathrm{y})=0
$$
As $\mathrm{a} \in \mathrm{R}$, we write
$$
\begin{aligned}
& (1)^2-4(1)(3-\mathrm{y}) \geq 0 \\
& \therefore 1-12+4 \mathrm{y} \geq 0 \quad \Rightarrow 4 \mathrm{y} \geq 11 \quad \Rightarrow \mathrm{y} \geq \frac{11}{4}
\end{aligned}
$$
Also $2^x+4^x>0 \Rightarrow y \neq 3$
$\therefore$ Range from given option is $(3, \infty)$

</details>

---

### Q8. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{A}=\{10,11,12,14,26\}$ and let $\mathrm{f}: \mathrm{A} \rightarrow \mathrm{N}$ be such that $\mathrm{f}(\mathrm{a})=$ highest prime factor of $a$, where $a \in A$, then range of $f=$

**Options:**

- **(A)** $\{5,7,13\}$
- **(B)** $\{5,7,11,13\}$
- **(C)** $\{3,5,7,11,13\}$
- **(D)** $\{3,7,11,13\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\{3,5,7,11,13\}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/6xa7dqcignQ0qA0mb0PI-UwKkrgLXSnizA64XkDjWZI.original.fullsize.png">

</details>

---

### Q9. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The range of the function $f(x)=\frac{x-3}{5-x}, x \neq 5$ is

**Options:**

- **(A)** $\mathrm{R}-\{1\}$
- **(B)** $\mathrm{R}-\{-5\}$
- **(C)** $\mathrm{R}-\{5\}$
- **(D)** $\mathrm{R}-\{-1\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{R}-\{-1\}$**

**Detailed Solution:**

(A)
We have $y=\frac{x-3}{5-x}$ $\therefore 5 y-x y=x-3 \Rightarrow x+x y=5 y+3$ $\therefore x=\frac{5 y+3}{1+y}$ Hence Range $=R-\{-1\}$

</details>

---

### Q10. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{R}=\{(a, \mathrm{~b}) / \mathrm{b}=a-1, a \in \mathrm{Z}, 5 < a < 9\}$, then the range of $\mathrm{R}$ is

**Options:**

- **(A)** $\{7,8,9\}$
- **(B)** $\{5,6,7\}$
- **(C)** $\{6,7,8\}$
- **(D)** $\{5,6,7,8,9\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\{5,6,7\}$**

**Detailed Solution:**

(A)
Given $\mathbf{R}=\{(\mathbf{a}, \mathbf{b}), \mathbf{b}=\mathbf{a}-1, \mathbf{a} \in \mathbf{z}, 5 < \mathbf{a} < 9\}$
$\therefore \quad a=6,7,8$
$a=6, b=6-1=5$
$a=7, b=7-1=6$
$a=8, b=8-1=7$
$R=\{(6,5),(7,6),(8,7)\}$
Range of $R=\{5,6,7\}$

</details>

---

### Q11. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=\frac{2 x+3}{3 x-2}, x \neq \frac{2}{3}$, then the function fof is

**Options:**

- **(A)** an even function
- **(B)** an identity function
- **(C)** a constant function
- **(D)** an exponential function

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) an identity function**

**Detailed Solution:**

(B)
$f \circ f=f(f(x))$
$\begin{aligned}
=& \frac{2 \cdot\left(\frac{2 x+3}{3 x-2}\right)+3}{3 \cdot\left(\frac{2 x+3}{3 x-2}\right)-2}=\frac{\frac{4 x+6}{3 x-2}+3}{\frac{6 x+9}{3 x-2}-2} \\
=& \frac{4 x+6+9 x-6}{6 x+9-6 x+4}=\frac{13 x}{13}=x
\end{aligned}$
Therefore, we can say that the composite function for for given function is an identity function.

</details>

---

### Q12. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>f</mi><mo>:</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{" separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>→</mo><mi>R</mi></math> is a function defined by <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac><mo>,</mo></math> then range is

**Options:**

- **(A)** <math><mi>R</mi></math>
- **(B)** <math><mi>R</mi><mo>-</mo><mfenced close="}" open="{" separators="|"><mrow><mn>2</mn></mrow></mfenced></math>
- **(C)** <math><mi>R</mi><mo>-</mo><mfenced close="}" open="{" separators="|"><mrow><mn>4</mn></mrow></mfenced></math>
- **(D)** <math><mi>R</mi><mo>-</mo><mfenced close="}" open="{" separators="|"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mi> </mi><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>R</mi><mo>-</mo><mfenced close="}" open="{" separators="|"><mrow><mn>4</mn></mrow></mfenced></math>**

**Detailed Solution:**

Given <math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mfrac> <mrow> <mrow><mo>(</mo> <mrow> <mi>x</mi><mo>−</mo><mn>2</mn></mrow> <mo>)</mo></mrow><mrow><mo>(</mo> <mrow> <mi>x</mi><mo>+</mo><mn>2</mn></mrow> <mo>)</mo></mrow></mrow> <mrow> <mrow><mo>(</mo> <mrow> <mi>x</mi><mo>−</mo><mn>2</mn></mrow> <mo>)</mo></mrow></mrow> </mfrac> <mo>;</mo><mtext> </mtext><mo>&rArr;</mo><msub> <mi>D</mi> <mi>f</mi> </msub> <mo>:</mo><mi>R</mi><mo>−</mo><mrow><mo>{</mo> <mn>2</mn> <mo>}</mo></mrow></mrow> </math>
<math> <mo>&rArr;</mo><mrow> <msub> <mi>R</mi> <mi>f</mi> </msub> <mo>:</mo><mi>R</mi><mo>−</mo><mrow><mo>{</mo> <mn>4</mn> <mo>}</mo></mrow></mrow> </math>

</details>

---

