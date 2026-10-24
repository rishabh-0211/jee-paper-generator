# JEE Main Mathematics - Limits

## Topic 3: Trigonometric and Inverse Trigonometric limits

**Total Questions:** 46

---

### Q1. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\lim\limits_{x \to 2} \dfrac{(\tan(x-2))(rx^2 + (p-2)x - 2p)}{(x-2)^2} = 5$ for some $r, p \in \mathbb{R}$. If the set of all possible values of $q$, such that the roots of the equation $rx^2 - px + q = 0$ lie in $(0, 2)$, be the interval $(\alpha, \beta]$, then $4(\alpha + \beta)$ equals :

**Options:**

- **(A)** $11$
- **(B)** $13$
- **(C)** $17$
- **(D)** $21$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $17$**

**Detailed Solution:**

Given limit is $\lim\limits_{x \to 2} \dfrac{\tan(x-2)}{x-2} \cdot \dfrac{rx^2 + (p-2)x - 2p}{x-2} = 5$

Since $\lim\limits_{x \to 2} \dfrac{\tan(x-2)}{x-2} = 1$, we have:

$\lim\limits_{x \to 2} \dfrac{rx^2 + (p-2)x - 2p}{x-2} = 5$

For the limit to exist, the numerator must be zero at $x = 2$:

$r(2)^2 + (p-2)(2) - 2p = 0$

$4r + 2p - 4 - 2p = 0 \Rightarrow 4r = 4 \Rightarrow r = 1$

Substituting $r = 1$ into the limit expression:

$\lim\limits_{x \to 2} \dfrac{x^2 + (p-2)x - 2p}{x-2} = 5$

$\lim\limits_{x \to 2} \dfrac{(x-2)(x+p)}{x-2} = 5$

$\lim\limits_{x \to 2} (x+p) = 5 \Rightarrow 2 + p = 5 \Rightarrow p = 3$

The quadratic equation is $rx^2 - px + q = 0$, which becomes $x^2 - 3x + q = 0$.

For both roots of $f(x) = x^2 - 3x + q = 0$ to lie in the interval $(0, 2)$, the following conditions must hold:

1) Discriminant $D \ge 0 \Rightarrow (-3)^2 - 4(1)(q) \ge 0 \Rightarrow 9 - 4q \ge 0 \Rightarrow q \le \dfrac{9}{4}$

2) $f(0) > 0 \Rightarrow q > 0$

3) $f(2) > 0 \Rightarrow 2^2 - 3(2) + q > 0 \Rightarrow q - 2 > 0 \Rightarrow q > 2$

4) The $x$-coordinate of the vertex must lie in $(0, 2) \Rightarrow 0 < \dfrac{-(-3)}{2(1)} < 2 \Rightarrow 0 < 1.5 < 2$, which is true.

Taking the intersection of all conditions, we get $q \in (2, \dfrac{9}{4}]$.

Comparing this with $(\alpha, \beta]$, we have $\alpha = 2$ and $\beta = \dfrac{9}{4}$.

Therefore, $4(\alpha + \beta) = 4(2 + \dfrac{9}{4}) = 8 + 9 = 17$.

Answer: $17$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\lim_{x \to 0}\left(\dfrac{x^2\sin^2 x}{x^2 - \sin^2 x}\right)$ is:

**Options:**

- **(A)** $2$
- **(B)** $3$
- **(C)** $4$
- **(D)** $6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3$**

**Detailed Solution:**

Let $L = \lim_{x \to 0} \dfrac{x^2\sin^2 x}{x^2 - \sin^2 x}$

Dividing the numerator and the denominator by $x^4$, we get:

$L = \lim_{x \to 0} \dfrac{\left(\dfrac{\sin x}{x}\right)^2}{\dfrac{x^2 - \sin^2 x}{x^4}}$

Factorizing the denominator:

$L = \lim_{x \to 0} \dfrac{\left(\dfrac{\sin x}{x}\right)^2}{\left(\dfrac{x - \sin x}{x^3}\right) \left(\dfrac{x + \sin x}{x}\right)}$

Using the standard limits:

$\lim_{x \to 0} \dfrac{\sin x}{x} = 1$

$\lim_{x \to 0} \dfrac{x - \sin x}{x^3} = \dfrac{1}{6}$ (using Taylor series expansion $\sin x = x - \dfrac{x^3}{3!} + \dots$)

$\lim_{x \to 0} \dfrac{x + \sin x}{x} = \lim_{x \to 0} \left(1 + \dfrac{\sin x}{x}\right) = 1 + 1 = 2$

Substituting these limits into the expression:

$L = \dfrac{1^2}{\left(\dfrac{1}{6}\right) \times 2} = \dfrac{1}{\dfrac{1}{3}} = 3$

Answer: $3$

</details>

---

### Q3. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x) = \lim_{y \to 0} \dfrac{(1 - \cos(xy)) \tan(xy)}{y^3}$. Then the number of solutions of the equation $f(x) = \sin x$, $x \in \mathbf{R}$ is :

**Options:**

- **(A)** $0$
- **(B)** $2$
- **(C)** $3$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3$**

**Detailed Solution:**

The given function is $f(x) = \lim_{y \to 0} \dfrac{(1 - \cos(xy)) \tan(xy)}{y^3}$.

Multiplying and dividing by $x^3$, we get:

$f(x) = \lim_{y \to 0} \dfrac{1 - \cos(xy)}{(xy)^2} \cdot \dfrac{\tan(xy)}{xy} \cdot x^3$

Using the standard limits $\lim_{t \to 0} \dfrac{1 - \cos t}{t^2} = \dfrac{1}{2}$ and $\lim_{t \to 0} \dfrac{\tan t}{t} = 1$, we obtain:

$f(x) = \dfrac{1}{2} \cdot 1 \cdot x^3 = \dfrac{x^3}{2}$

We need to find the number of solutions for the equation $f(x) = \sin x$, which is $\dfrac{x^3}{2} = \sin x$.

Let $g(x) = \dfrac{x^3}{2} - \sin x$.

Differentiating with respect to $x$:

$g'(x) = \dfrac{3x^2}{2} - \cos x$

$g''(x) = 3x + \sin x$

For $x > 0$, $g''(x) > 0$, which implies that $g'(x)$ is strictly increasing on $(0, \infty)$.

We have $g'(0) = -1 < 0$ and $g'(\pi/2) = \dfrac{3\pi^2}{8} > 0$. Thus, $g'(x) = 0$ has exactly one root in $(0, \infty)$, say at $x = x_0$.

This means $g(x)$ decreases on $(0, x_0)$ and increases on $(x_0, \infty)$.

Since $g(0) = 0$ and $g(x)$ initially decreases, $g(x_0) < 0$. As $x \to \infty$, $g(x) \to \infty$. Therefore, $g(x) = 0$ has exactly one positive root.

Since $g(x)$ is an odd function ($g(-x) = -g(x)$), it must also have exactly one negative root.

Including the trivial root $x = 0$, the equation $g(x) = 0$ has exactly $3$ solutions.

Answer: $3$

</details>

---

### Q4. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The product of all possible values of $\alpha$, for which $\displaystyle\lim_{x \to 0}\left(\dfrac{1 - \cos(\alpha x)\cos((\alpha+1)x)\cos((\alpha+2)x)}{\sin^2((\alpha+1)x)}\right) = 2$, is:

**Options:**

- **(A)** $-2$
- **(B)** $1$
- **(C)** $-1$
- **(D)** $\dfrac{5}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-1$**

**Detailed Solution:**

Using the standard expansions for small $x$, $\cos \theta \approx 1 - \dfrac{\theta^2}{2}$ and $\sin \theta \approx \theta$.

The given limit can be written as:

$\displaystyle\lim_{x \to 0} \dfrac{1 - \left(1 - \dfrac{\alpha^2 x^2}{2}\right)\left(1 - \dfrac{(\alpha+1)^2 x^2}{2}\right)\left(1 - \dfrac{(\alpha+2)^2 x^2}{2}\right)}{((\alpha+1)x)^2}$

Neglecting higher powers of $x$, the numerator simplifies to:

$1 - \left(1 - \dfrac{x^2}{2}\left(\alpha^2 + (\alpha+1)^2 + (\alpha+2)^2\right)\right) = \dfrac{x^2}{2}\left(\alpha^2 + (\alpha+1)^2 + (\alpha+2)^2\right)$

Substituting this back into the limit:

$\displaystyle\lim_{x \to 0} \dfrac{\dfrac{x^2}{2}\left(\alpha^2 + (\alpha+1)^2 + (\alpha+2)^2\right)}{(\alpha+1)^2 x^2} = \dfrac{\alpha^2 + (\alpha+1)^2 + (\alpha+2)^2}{2(\alpha+1)^2}$

We are given that this limit is equal to $2$. Therefore:

$\dfrac{\alpha^2 + (\alpha+1)^2 + (\alpha+2)^2}{2(\alpha+1)^2} = 2$

$\alpha^2 + (\alpha+1)^2 + (\alpha+2)^2 = 4(\alpha+1)^2$

Let $y = \alpha+1$. Then $\alpha = y-1$ and $\alpha+2 = y+1$. The equation becomes:

$(y-1)^2 + y^2 + (y+1)^2 = 4y^2$

$y^2 - 2y + 1 + y^2 + y^2 + 2y + 1 = 4y^2$

$3y^2 + 2 = 4y^2$

$y^2 = 2$

Substituting $y = \alpha+1$ back into the equation:

$(\alpha+1)^2 = 2$

$\alpha^2 + 2\alpha + 1 = 2$

$\alpha^2 + 2\alpha - 1 = 0$

The roots of this quadratic equation represent all possible values of $\alpha$. The product of the roots is given by $\dfrac{c}{a}$:

$\text{Product} = \dfrac{-1}{1} = -1$

Answer: $-1$

</details>

---

### Q5. JEE Main 2025 (7 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

If the function $f(x)=\frac{\tan (\tan x)-\sin (\sin x)}{\tan x-\sin x}$ is continuous at $\mathrm{x}=0$, then $f(0)$ is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

$\lim _{x \rightarrow 0} \frac{\frac{\tan (\tan x)-\tan x}{\tan ^3 x} \frac{\tan ^3 x}{x^3}+\frac{\tan x-\sin x}{x^3}+\frac{\sin x-\sin (\sin x)}{\sin ^3 x} \frac{\sin ^3 x}{x^3}}{\frac{\tan x-\sin x}{x^3}}$
$=\frac{\frac{1}{3}+\frac{1}{2}+\frac{1}{6}}{\frac{1}{2}}=2$

</details>

---

### Q6. JEE Main 2024 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

The value of $\lim _{x \rightarrow 0} 2\left(\frac{1-\cos x \sqrt{\cos 2 x} \sqrt[3]{\cos 3 x} \ldots \ldots \sqrt[10]{\cos 10 x}}{x^2}\right)$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **55**

**Detailed Solution:**

$\lim _{x \rightarrow 0} 2\left(\frac{1-\left(1-\frac{x^2}{2 !}\right)\left(1-\frac{4 x^2}{2 !}\right)\left(1-\frac{9 x^2}{2 !}\right) \ldots .\left(1-\frac{100 x^2}{2 !}\right)}{x^2}\right)$
By expansion
$\begin{gathered}
\left.\lim _{x \rightarrow 0} \frac{2\left(1-\left(1-\frac{x^2}{2}\right)\right)\left(1-\frac{1}{2} \cdot \frac{4 x^2}{2}\right)\left(1-\frac{1}{3} \cdot \frac{9 x^2}{2}\right) \ldots . .\left(1-\frac{1}{10} \cdot \frac{100 x^2}{2}\right)}{x^2}\right) \\
\lim _{x \rightarrow 0} 2\left(\frac{\left.1-\left(1-\frac{x^2}{2}\right)\left(1-\frac{2 x^2}{2}\right)\left(1-\frac{3 x^2}{2}\right) \ldots . .\left(1-\frac{10 x^2}{2}\right)\right)}{x^2}\right) \\
\lim _{x \rightarrow 0} \frac{2\left(1-1+x^2\left(\frac{1}{2}+\frac{2}{2}+\frac{3}{2}+\ldots .+\frac{10}{2}\right)\right)}{x^2} \\
2\left(\frac{1}{2}+\frac{2}{2}+\frac{3}{2}+\ldots .+\frac{10}{2}\right) \\
1+2+\ldots \ldots+10=\frac{10 \times 11}{2}=55
\end{gathered}$

</details>

---

### Q7. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#62;</mo><mi>&#946;</mi><mo>&#62;</mo><mn>0</mn></math> are the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>, and
<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mrow></munder><msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfenced></mrow><mrow><mn>2</mn><mo>(</mo><mn>1</mn><mo>-</mo><mi>&#945;</mi><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>=</mo><mfrac><mn>1</mn><mi>k</mi></mfrac><mfenced><mrow><mfrac><mn>1</mn><mi>&#946;</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#946;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#945;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#945;</mi></math>**

**Detailed Solution:**

<blockquote><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>, therefore <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>&#946;</mi></mfrac></math> would be the roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>a</mi><mo>=</mo><mn>0</mn></math>.</p><p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mrow></munder><msup><mfenced close="]" open="["><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfenced></mrow><mrow><mn>2</mn><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>&#945;</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>&#8594;</mo><mfrac><mn>0</mn><mn>0</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mrow></munder><msup><mfenced close="]" open="["><mfrac><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>a</mi></mrow><mn>2</mn></mfrac></mstyle></mfenced></mrow><mrow><mn>2</mn><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>&#945;</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mrow></munder><msup><mfenced close="]" open="["><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>&#946;</mi></mfrac></mrow></mfenced></mstyle></mfenced></mrow><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mstyle></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mrow></munder><msup><mfenced open="[" close="]"><mrow><mfrac><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>&#946;</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mrow><mn>4</mn><msup><mi>&#945;</mi><mn>2</mn></msup></mrow></mfrac><mo>&#215;</mo><mfrac><msup><mfenced open="{" close="}"><mrow><mi>sin</mi><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>&#946;</mi></mfrac></mrow></mfenced></mstyle></mfenced></mrow></mfenced><mn>2</mn></msup><mrow><msup><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></mfenced><mn>2</mn></msup><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mstyle></mrow></mfenced><mn>2</mn></msup><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>&#946;</mi></mfrac></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><mfrac><mfenced><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mstyle><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>&#946;</mi></mfrac></mstyle></mrow></mfenced><mrow><mn>2</mn><mi>&#945;</mi></mrow></mfrac></math></p><p>On comparing this value with the value given in the question we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>2</mn><mi>&#945;</mi></math>.</p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q8. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mrow><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mo>(</mo><mn>3</mn><mi>x</mi><mo>)</mo></mrow><mrow><msup><mi>cos</mi><mn>3</mn></msup><mo>(</mo><mn>4</mn><mi>x</mi><mo>)</mo></mrow></mfrac></mfenced><mfenced><mfrac><mrow><msup><mi>sin</mi><mn>3</mn></msup><mo>(</mo><mn>4</mn><mi>x</mi><mo>)</mo></mrow><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mn>5</mn></msup></mfrac></mfenced></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mrow><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mo>(</mo><mn>3</mn><mi>x</mi><mo>)</mo></mrow><mrow><msup><mi>cos</mi><mn>3</mn></msup><mo>(</mo><mn>4</mn><mi>x</mi><mo>)</mo></mrow></mfrac></mfenced><mfenced><mfrac><mrow><msup><mi>sin</mi><mn>3</mn></msup><mo>(</mo><mn>4</mn><mi>x</mi><mo>)</mo></mrow><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mn>5</mn></msup></mfrac></mfenced></mrow></mfenced></math></p><p>Now we now that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mi>x</mi></mfrac><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mstyle displaystyle="true"><mn>1</mn><mo>-</mo><mi>cos</mi><mi>x</mi></mstyle><mstyle displaystyle="true"><msup><mi>x</mi><mn>2</mn></msup></mstyle></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mstyle displaystyle="true"><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mstyle><mstyle displaystyle="true"><mi>x</mi></mstyle></mfrac><mo>=</mo><mn>1</mn></math></p><p>Now using the above formula we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mrow><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>3</mn><mi>x</mi></mrow><mrow><msup><mi>cos</mi><mn>3</mn></msup><mn>4</mn><mi>x</mi></mrow></mfrac></mfenced><mfenced><mfrac><mrow><msup><mi>sin</mi><mn>3</mn></msup><mn>4</mn><mi>x</mi></mrow><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mn>5</mn></msup></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></mfenced><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mfenced><mrow><msup><mi>cos</mi><mn>3</mn></msup><mn>4</mn><mi>x</mi></mrow></mfenced><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mfrac><mrow><msup><mfenced><mrow><mi>sin</mi><mn>4</mn><mi>x</mi></mrow></mfenced><mn>3</mn></msup><msup><mfenced><mrow><mn>64</mn><mi>x</mi></mrow></mfenced><mn>3</mn></msup><msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mn>5</mn></msup></mrow><mrow><mfenced><mrow><mn>64</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></mfenced><mn>5</mn></msup><msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mn>5</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mstyle displaystyle="true"><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>3</mn><mi>x</mi></mrow><mrow><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mstyle></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></mfenced></mrow><mfenced><mrow><msup><mi>cos</mi><mn>3</mn></msup><mn>4</mn><mi>x</mi></mrow></mfenced></mfrac><mfrac><msup><mfenced><mstyle displaystyle="true"><mfrac><mrow><mi>sin</mi><mn>4</mn><mi>x</mi></mrow><mrow><mn>4</mn><mi>x</mi></mrow></mfrac></mstyle></mfenced><mn>3</mn></msup><msup><mfenced><mstyle displaystyle="true"><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mstyle></mfenced><mn>5</mn></msup></mfrac><mo>&#215;</mo><mfrac><mrow><mn>9</mn><mo>&#215;</mo><mn>64</mn></mrow><mn>32</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></mfenced><mo>&#215;</mo><mfenced><mn>2</mn></mfenced></mrow><mfenced><mn>1</mn></mfenced></mfrac><mfrac><msup><mfenced><mstyle displaystyle="true"><mn>1</mn></mstyle></mfenced><mn>3</mn></msup><msup><mfenced><mstyle displaystyle="true"><mn>1</mn></mstyle></mfenced><mn>5</mn></msup></mfrac><mo>&#215;</mo><mfrac><mrow><mn>9</mn><mo>&#215;</mo><mn>64</mn></mrow><mn>32</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>9</mn><mo>&#215;</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mn>18</mn></math></p></blockquote>

</details>

---

### Q9. JEE Main 2023 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>,</mo><mi>g</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math> be the real valued functions defined on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8477;</mi></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mfrac><mi>x</mi><mfenced close="|" open="|"><mi>x</mi></mfenced></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8800;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mfrac><mrow><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8800;</mo><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> is the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>x</mi></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>1</mn></mrow></munder><mi>g</mi><mfenced><mrow><mi>h</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mfenced><mn>1</mn></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given,</p><p>Function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mfrac><mi>x</mi><mfenced close="|" open="|"><mi>x</mi></mfenced></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8800;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mfrac><mrow><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8800;</mo><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p>To find <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>1</mn></mrow></munder><mi>g</mi><mfenced><mrow><mi>h</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p>Taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">L</mi></math>, we take <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>-</mo><mi>h</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mi>g</mi><mo>(</mo><mi>h</mi><mo>(</mo><mn>1</mn><mo>-</mo><mi>h</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mi>g</mi><mfenced><mrow><mn>2</mn><mfenced close="]" open="["><mrow><mo>-</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mfrac><mrow><mo>-</mo><mi>h</mi></mrow><mfenced close="|" open="|"><mrow><mo>-</mo><mi>h</mi></mrow></mfenced></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mi>g</mi><mo>(</mo><mn>2</mn><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>+</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mi>g</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p>Now taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">L</mi></math>, we take <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>+</mo><mi>h</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mi>g</mi><mo>(</mo><mi>h</mi><mo>(</mo><mn>1</mn><mo>+</mo><mi>h</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mi>g</mi><mfenced><mrow><mn>2</mn><mfenced close="]" open="["><mi>h</mi></mfenced><mo>-</mo><mi>f</mi><mo>(</mo><mi>h</mi><mo>)</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mi>g</mi><mo>(</mo><mn>0</mn><mo>-</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mn>1</mn><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q10. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> be a root of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>p</mi><mi>x</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>p</mi><mi>x</mi><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>q</mi><mo>+</mo><mn>16</mn></mrow></mfenced></mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn><mi>p</mi></mrow></mfenced><mn>4</mn></msup></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8800;</mo><mn>2</mn><mi>p</mi></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>2</mn><mi>p</mi></mtd></mtr></mtable></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>2</mn><msup><mi>p</mi><mo>+</mo></msup></mrow></munder><mfenced close="]" open="["><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math>
where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mo>&#183;</mo></mfenced></math> denotes greatest integer function, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> be the root of the given equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>p</mi><mi>x</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>0</mn></math>,</p><p>Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> in given equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mo>+</mo><mn>2</mn><mi>p</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>q</mi><mo>+</mo><mn>4</mn><mo>=</mo><mo>-</mo><mn>2</mn><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>p</mi><mi>x</mi><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>q</mi><mo>+</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>p</mi><mi>x</mi><mo>+</mo><msup><mfenced><mrow><mi>q</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>p</mi><mi>x</mi><mo>+</mo><mn>4</mn><msup><mi>p</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>(</mo><mo>&#8757;</mo><mi>q</mi><mo>+</mo><mn>4</mn><mo>=</mo><mo>-</mo><mn>2</mn><mi>p</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mi>p</mi><msup><mo>)</mo><mn>2</mn></msup></math></p><p>Now, solving the limit <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>2</mn><msup><mi>p</mi><mo>+</mo></msup></mrow></munder><mfenced close="]" open="["><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>2</mn><msup><mi>p</mi><mo>+</mo></msup></mrow></munder><mfenced close="]" open="["><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mfenced><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn><mi>p</mi></mrow></mfenced><mn>2</mn></msup></mfenced></mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn><mi>p</mi></mrow></mfenced><mn>4</mn></msup></mfrac></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mi>p</mi><mo>=</mo><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfenced open="[" close="]"><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfenced open="[" close="]"><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mfenced><msup><mi>&#952;</mi><mn>2</mn></msup></mfenced></mrow><msup><mfenced><mi>&#952;</mi></mfenced><mn>4</mn></msup></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mfenced><msup><mi>&#952;</mi><mn>2</mn></msup></mfenced></mrow><msup><mfenced><mi>&#952;</mi></mfenced><mn>4</mn></msup></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>   (Using L&#39;Hospital&#39;s)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfenced close="]" open="["><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfenced close="]" open="["><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfenced close="]" open="["><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q11. JEE Main 2022 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><msup><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mn>7</mn></msup></mrow><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><msup><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mn>7</mn></msup></mrow><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mfrac><mn>0</mn><mn>0</mn></mfrac><mi>form</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mo>-</mo><mn>7</mn><msup><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mn>6</mn></msup><mfenced><mrow><mo>-</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfrac></math>  (using L&#39;Hospital Rule)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mn>56</mn><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mo>&#160;</mo><mfenced><mrow><mfrac><mn>0</mn><mn>0</mn></mfrac><mo>&#160;</mo><mi>form</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mo>-</mo><mn>56</mn><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfrac></math>  (using L&#39;Hospital Rule)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>56</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>=</mo><mn>14</mn></math></p></blockquote>

</details>

---

### Q12. JEE Main 2022 (28 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>1</mn></mrow></munder><mfenced><mfrac><mrow><mi>sin</mi><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>7</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></mrow></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>2</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **11**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>1</mn></mrow></munder><mfenced><mfrac><mrow><mi>sin</mi><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#8722;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>&#8722;</mo><mn>7</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></mrow></mfrac></mfenced><mo>=</mo><mo>&#8722;</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> in limit we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>1</mn></mrow></munder><mfenced><mfrac><mrow><mi>sin</mi><mn>0</mn><mo>-</mo><mn>1</mn><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><mo>-</mo><mn>7</mn><mo>+</mo><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>2</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>1</mn></mrow></munder><mfenced><mfrac><mn>0</mn><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>5</mn></mrow></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>For limit to exist <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>5</mn></math> should be zero</p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>5</mn><mo>=</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Now Using L-Hospital in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>1</mn></mrow></munder><mfrac><mrow><mi>cos</mi><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>6</mn><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mi>x</mi></mrow><mrow><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>14</mn><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>Again putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>1</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mi>cos</mi><mn>0</mn></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>6</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mn>2</mn></mrow><mrow><mn>6</mn><mo>-</mo><mn>14</mn><mo>+</mo><mi>a</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>1</mn></mrow></munder><mfrac><mn>0</mn><mrow><mi>a</mi><mo>-</mo><mn>8</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>Again for limit to exist <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>8</mn></math></p><p>So from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>+</mo><mi>b</mi><mo>=</mo><mn>5</mn><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mn>8</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>11</mn></math></p>

</details>

---

### Q13. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>cos</mi><mo>(</mo><mi>sin</mi><mi>x</mi><mo>)</mo><mo>-</mo><mi>cos</mi><mi>x</mi></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>12</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Consider <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>cos</mi><mo>(</mo><mi>sin</mi><mi>x</mi><mo>)</mo><mo>-</mo><mi>cos</mi><mi>x</mi></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mfrac><mn>0</mn><mn>0</mn></mfrac><mo>&#160;</mo><mtext>form</mtext></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>2</mn><mi>sin</mi><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mo>&#183;</mo><mi>sin</mi><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mn>2</mn><mfenced close="]" open="["><mfrac><mrow><mi>sin</mi><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mfrac></mfenced><mfenced close="]" open="["><mfrac><mrow><mi>sin</mi><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mfrac></mfenced><mo>&#215;</mo><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mo>&#215;</mo><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mo>&#215;</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>4</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mn>2</mn><mfenced close="]" open="["><mfrac><mrow><mi>sin</mi><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mfrac></mfenced><mfenced close="]" open="["><mfrac><mrow><mi>sin</mi><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mfrac></mfenced><mo>&#215;</mo><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>4</mn><msup><mi>x</mi><mn>4</mn></msup></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mn>2</mn><mo>&#215;</mo><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>4</mn><msup><mi>x</mi><mn>4</mn></msup></mrow></mfrac></mfenced><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mfrac><mn>0</mn><mn>0</mn></mfrac><mo>&#160;</mo><mtext>form</mtext></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mi>t</mi></mrow><mi>t</mi></mfrac><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p>Applying L&#39;Hospital&#39;s Rule,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mn>2</mn><mo>&#215;</mo><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><mn>4</mn><mo>&#183;</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mrow><mn>8</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mfrac><mn>0</mn><mn>0</mn></mfrac><mo>&#160;</mo><mtext>form</mtext></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mn>2</mn><mo>-</mo><mn>2</mn><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><mrow><mn>24</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mfrac><mn>0</mn><mn>0</mn></mfrac><mo>&#160;</mo><mtext>form</mtext></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mn>4</mn><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mrow><mn>48</mn><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><munder><mrow><mfrac><mn>1</mn><mn>6</mn></mfrac><mi>lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math></p></blockquote>

</details>

---

### Q14. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></munder><mfrac><mrow><mi>sin</mi><mfenced><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mfenced><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>=</mo><mi>t</mi></math>  i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>cos</mi><mi>t</mi></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mi>sin</mi><mi>t</mi><mo>&#8722;</mo><mi>cos</mi><mi>t</mi></mrow><mrow><mn>1</mn><mo>&#8722;</mo><mi>tan</mi><mi>t</mi></mrow></mfrac></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfenced><mrow><mo>&#8722;</mo><mi>cos</mi><mi>t</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mo>&#8722;</mo><mn>1</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac></math></p>

</details>

---

### Q15. JEE Main 2022 (25 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></munder><mfenced><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><msup><mfenced><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>6</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></mrow></mfenced></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>12</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>18</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>12</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>12</mn></mfrac></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></munder><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mfenced close="]" open="["><mrow><msqrt><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>4</mn></msqrt><mo>-</mo><msqrt><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>6</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></munder><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mfrac><mfenced close="]" open="["><mrow><msup><mfenced><msqrt><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>4</mn></msqrt></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><msqrt><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>6</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn></msqrt></mfenced><mn>2</mn></msup></mrow></mfenced><mrow><msqrt><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>4</mn></msqrt><mo>+</mo><msqrt><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>6</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></munder><mfrac><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mfenced close="]" open="["><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><msqrt><mn>9</mn></msqrt><mo>+</mo><msqrt><mn>9</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></munder><mfrac><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></munder><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></munder><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac></math></p>

</details>

---

### Q16. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mrow><mi>&#960;</mi><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>&#960;</mi><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#960;</mi><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>&#960;</mi><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#960;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>&#960;</mi><mn>2</mn></msup></math>**

**Detailed Solution:**

<p>Given that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mrow><mi>&#960;</mi><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mrow><mi>&#960;</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mi>&#960;</mi><mfenced><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mrow><mi>&#960;</mi><mfenced><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced><mfrac><mrow><mi>sin</mi><mfenced open="[" close="]"><mrow><mi>&#960;</mi><mfenced><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mi>&#960;</mi><mfenced><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac></mfenced><mn>2</mn></msup><mo>&#183;</mo><mfrac><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><msup><mfenced><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac></math>
When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mn>0</mn><mo>&#160;</mo></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>k</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced open="[" close="]"><mfrac><mrow><mi>sin</mi><mi>&#960;</mi><mi>k</mi><mo>&#160;</mo></mrow><mrow><mi>&#960;</mi><mi>k</mi></mrow></mfrac></mfenced><mn>2</mn></msup><mo>.</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>.</mo><mo>&#160;</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>&#160;</mo><msup><mfenced><mrow><mn>2</mn><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mi>k</mi><mi>x</mi></mrow><mi>x</mi></mfrac><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>k</mi><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><msup><mi>&#960;</mi><mn>2</mn></msup></mfrac><mo>.</mo><msup><mi>&#960;</mi><mn>2</mn></msup><mo>.</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced open="[" close="]"><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>&#160;</mo></mrow><mi>x</mi></mfrac></mfenced><mn>4</mn></msup><mo>.</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced><mrow><mn>2</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>&#960;</mi><mn>2</mn></msup><mo>&#160;</mo><mo>.</mo><mo>&#160;</mo><mn>1</mn><mo>&#160;</mo><mo>.</mo><mo>&#160;</mo><msup><mfenced><mn>2</mn></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><msup><mi>&#960;</mi><mn>2</mn></msup><mo>.</mo></math></p>

</details>

---

### Q17. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mi>x</mi><mrow><mroot><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>8</mn></mroot><mo>-</mo><mroot><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mn>8</mn></mroot></mrow></mfrac></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mi>x</mi><mrow><mroot><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>8</mn></mroot><mo>-</mo><mroot><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mn>8</mn></mroot></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mi>x</mi><mrow><mroot><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>8</mn></mroot><mo>-</mo><mroot><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mn>8</mn></mroot></mrow></mfrac></mfenced><mo>&#215;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mrow><mroot><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>8</mn></mroot><mo>+</mo><mroot><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mn>8</mn></mroot></mrow><mrow><mroot><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>8</mn></mroot><mo>+</mo><mroot><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mn>8</mn></mroot></mrow></mfrac></mfenced><mo>&#215;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mrow><mroot><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>4</mn></mroot><mo>+</mo><mroot><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mn>4</mn></mroot></mrow><mrow><mroot><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>4</mn></mroot><mo>+</mo><mroot><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mn>4</mn></mroot></mrow></mfrac></mfenced><mo>&#215;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mrow><msqrt><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></msqrt></mrow><mrow><msqrt><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></msqrt></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mi>x</mi><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mo>(</mo><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi><mo>)</mo></mrow></mfrac></mfenced><mo>&#215;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mroot><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>8</mn></mroot><mo>+</mo><mroot><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mn>8</mn></mroot></mrow></mfenced><mfenced><mrow><mroot><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>4</mn></mroot><mo>+</mo><mroot><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mn>4</mn></mroot></mrow></mfenced><mfenced><mrow><msqrt><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mi>x</mi><mrow><mo>(</mo><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>)</mo></mrow></mfrac><mfenced><mrow><mroot><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>8</mn></mroot><mo>+</mo><mroot><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mn>8</mn></mroot></mrow></mfenced><mo>&#215;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mroot><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>4</mn></mroot><mo>+</mo><mroot><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mn>4</mn></mroot></mrow></mfenced><mfenced><mrow><msqrt><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">=</mi><munder><mi>lim</mi><mrow><mi mathvariant="normal">x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mfenced><mn>2</mn></mfenced><mfenced><mn>2</mn></mfenced><mfenced><mn>2</mn></mfenced><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mo>&#8757;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mi>x</mi></mfrac><mo>=</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>4</mn></math></p>

</details>

---

### Q18. JEE Main 2021 (17 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of the limit <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>tan</mi><mfenced><mrow><mi>&#960;</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></mrow><mrow><mi>sin</mi><mfenced><mrow><mn>2</mn><mi>&#960;</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></mrow></mfrac></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>We have to find <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>tan</mi><mfenced><mrow><mi>&#960;</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></mrow><mrow><mi>sin</mi><mfenced><mrow><mn>2</mn><mi>&#960;</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></mrow></mfrac></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>1</mn><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>l</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>tan</mi><mfenced><mrow><mi>&#960;</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mi>sin</mi><mfenced><mrow><mn>2</mn><mi>&#960;</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>l</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>tan</mi><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mi>&#960;</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></mrow><mrow><mi>sin</mi><mfenced><mrow><mn>2</mn><mi>&#960;</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></mrow></mfrac></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>tan</mi><mi>&#952;</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>l</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mo>-</mo><mi>tan</mi><mfenced><mrow><mi>&#960;</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></mrow><mrow><mi>sin</mi><mfenced><mrow><mn>2</mn><mi>&#960;</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>l</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>-</mo><mfenced><mfrac><mrow><mi>tan</mi><mfenced><mrow><mi>&#960;</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></mrow><mrow><mi>&#960;</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac></mfenced><mfenced><mfrac><mrow><mn>2</mn><mi>&#960;</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mrow><mi>sin</mi><mfenced><mrow><mn>2</mn><mi>&#960;</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></mrow></mfrac></mfenced><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Using, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mi>x</mi></mfrac></mfenced><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mi>tan</mi><mi>x</mi></mrow><mi>x</mi></mfrac></mfenced><mo>=</mo><mn>1</mn><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q19. JEE Main 2021 (17 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mo>[</mo><mi>x</mi><msup><mo>]</mo><mn>2</mn></msup></mrow></mfenced><mo>&#183;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mo>[</mo><mi>x</mi><msup><mo>]</mo><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> denotes the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>x</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mo>[</mo><mi>x</mi><msup><mo>]</mo><mn>2</mn></msup></mrow></mfenced><mo>&#183;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mo>[</mo><mi>x</mi><msup><mo>]</mo><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>&#8658;</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p>Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mfrac><mo>&#215;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>&#215;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mtext>Apply&#160;L&#39;Hospital&#160;rule&#160;for&#160;</mtext><mfrac><mn>0</mn><mn>0</mn></mfrac><mtext>&#160;form</mtext></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math></p>

</details>

---

### Q20. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<div>The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="}" open="{"><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi>sin</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>+</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>cos</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>+</mo><mi>h</mi></mrow></mfenced></mrow><mrow><msqrt><mn>3</mn></msqrt><mi>h</mi><mfenced><mrow><msqrt><mn>3</mn></msqrt><mi>cos</mi><mi>h</mi><mo>-</mo><mi>sin</mi><mi>h</mi></mrow></mfenced></mrow></mfrac></mfenced></math> is :</div>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac></math>
- **(C)** <p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>cos</mi><mi>h</mi><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mi>sin</mi><mi>h</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mi>cos</mi><mi>h</mi><mo>-</mo><mfrac><mrow><mi>sin</mi><mi>h</mi></mrow><mn>2</mn></mfrac></mrow></mfenced></mrow><mrow><mfenced><mrow><msqrt><mn>3</mn></msqrt><mi>h</mi></mrow></mfenced><mfenced><msqrt><mn>3</mn></msqrt></mfenced></mrow></mfrac></mfenced></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>h</mi></mrow><mrow><mn>3</mn><mi>h</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q21. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is the positive root of the equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mi>x</mi><mo>&#8722;</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mi>&#945;</mi><mo>+</mo></msup></mrow></munder><mfrac><msqrt><mn>1</mn><mo>&#8722;</mo><mi>cos</mi><mi>p</mi><mfenced><mi>x</mi></mfenced></msqrt><mrow><mi>x</mi><mo>+</mo><mi>&#945;</mi><mo>&#8722;</mo><mn>4</mn></mrow></mfrac></math>is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><msqrt><mn>2</mn></msqrt></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><msqrt><mn>2</mn></msqrt></mfrac></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>&#160;&#160;</mo><mo>&#8756;</mo><mo>&#160;&#160;</mo><mi>&#945;</mi><mo>=</mo><mn>2</mn></math></p><p>Now,<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>2</mn><mo>+</mo></msup></mrow></munder><mfrac><msqrt><mn>1</mn><mo>&#8722;</mo><mi>cos</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mi>x</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced></msqrt><mrow><mi>x</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>2</mn><mo>+</mo></msup></mrow></munder><mfrac><msqrt><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mi>x</mi><mo>&#8722;</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mfenced></msqrt><mrow><mi>x</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>2</mn><mo>+</mo></msup></mrow></munder><msqrt><mn>2</mn></msqrt><mo>&#183;</mo><mfrac><mfenced open="|" close="|"><mrow><mi>sin</mi><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>2</mn><mo>+</mo></msup></mrow></munder><msqrt><mn>2</mn></msqrt><mo>&#183;</mo><mfrac><mrow><mi>sin</mi><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mfenced></mrow><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac></math> (because <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>2</mn></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>2</mn><mo>+</mo></msup></mrow></munder><mo>&#160;</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><mi>sin</mi><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mfenced></mrow><mrow><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mfenced><mo>&#183;</mo><mn>2</mn></mrow></mfrac><mo>&#183;</mo><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>2</mn><mo>+</mo></msup></mrow></munder><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>&#183;</mo><mfrac><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><msqrt><mn>2</mn></msqrt></mfrac></math>.</p>

</details>

---

### Q22. JEE Main 2020 (03 Sep Shift 1)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced open="{" close="}"><mrow><mfrac><mn>1</mn><msup><mi>x</mi><mn>8</mn></msup></mfrac><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>cos</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>&#8722;</mo><mi>cos</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mi>cos</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mi>cos</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mrow><mo>&#8722;</mo><mi>k</mi></mrow></msup></math> then the value of k is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="}" open="{"><mrow><mfrac><mn>1</mn><msup><mi>x</mi><mn>8</mn></msup></mfrac><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>cos</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>&#8722;</mo><mi>cos</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mi>cos</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mi>cos</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>cos</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>cos</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced></mrow><msup><mi>x</mi><mn>8</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>cos</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><msup><mi>x</mi><mn>4</mn></msup></mfrac><mo>&#215;</mo><mfrac><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>cos</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced><msup><mi>x</mi><mn>4</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>cos</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mrow><mn>4</mn><mo>&#215;</mo><mfenced><mstyle displaystyle="true"><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac></mstyle></mfenced></mrow></mfrac><mo>&#215;</mo><mfrac><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>cos</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced><mrow><mn>16</mn><mo>&#215;</mo><mfenced><mstyle displaystyle="true"><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>16</mn></mfrac></mstyle></mfenced></mrow></mfrac></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mi>x</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>256</mn></mfrac><mo>=</mo><msup><mn>2</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup><mo>=</mo><msup><mn>2</mn><mrow><mo>-</mo><mi>k</mi></mrow></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q23. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mi>&#160;</mi><mo>-</mo><mi>&#160;</mi><msqrt><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mn>2</mn></msup><mi>x</mi><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac></math> is

**Options:**

- **(A)** <math><mn>3</mn></math>
- **(B)** <math><mn>1</mn></math>
- **(C)** <math><mn>2</mn></math>
- **(D)** <math><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi></mrow><mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>&#8722;</mo><msqrt><mi>sin</mi><mi>x</mi><mo>&#8722;</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>0</mn><mn>0</mn></mfrac><mi>form</mi></mrow></mfenced></math></p><p>By using L&#39;Hospital Rule,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2</mn><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac><mo>&#8722;</mo><mfrac><mrow><mn>1</mn><mfenced><mrow><mi>sin</mi><mn>2</mn><mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn><msqrt><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>&#8722;</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfrac><mo>=</mo><mfrac><mn>3</mn><mfrac><mn>3</mn><mn>2</mn></mfrac></mfrac><mo>=</mo><mn>2</mn></math>.</p>

</details>

---

### Q24. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi mathvariant="normal">&#160;</mi><mfrac><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mn>2</mn></msup><mi>x</mi></mrow><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><msqrt><mn>1</mn><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></msqrt></mrow></mfrac></math> equals

**Options:**

- **(A)** <math><mn>4</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>4</mn><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p><math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi mathvariant="normal">&#160;</mi><mfrac><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi></mrow><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><msqrt><mn>1</mn><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></msqrt></mrow></mfrac></math></p><p>On Rationalisation, we get,</p><p>     <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi mathvariant="normal">&#160;</mi><mfrac><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mn>2</mn></msup><mi>x</mi></mrow><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><msqrt><mn>1</mn><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></msqrt></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi>sx</mi></msqrt></mrow><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi>sx</mi></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi mathvariant="normal">&#160;</mi><mfrac><msup><mfenced separators="|"><mrow><mn>2</mn><mi>sin</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mi>cos</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac><mo>&#215;</mo><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi mathvariant="normal">&#160;</mi><mfrac><mrow><mn>4</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mn>2</mn></msup><mfrac><mi>x</mi><mn>2</mn></mfrac><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mn>2</mn></msup><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow><mrow><mn>2</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mn>2</mn></msup><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfrac><mo>&#215;</mo><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>&#160;</mi><mn>2</mn><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mn>2</mn></msup><mfrac><mi>x</mi><mn>2</mn></mfrac><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></msqrt></mrow></mfenced><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p><p><math><mo>=</mo><mn>4</mn><msqrt><mn>2</mn></msqrt></math>.</p>

</details>

---

### Q25. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>1</mn><mo>-</mo></msup></mrow></munder><mfrac><mrow><msqrt><mi>&#960;</mi></msqrt><mo>-</mo><msqrt><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></msqrt></mrow><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>&#960;</mi></msqrt></math>
- **(B)** <math><msqrt><mfrac><mrow><mn>2</mn></mrow><mrow><mi>&#960;</mi></mrow></mfrac></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn><mi>&#960;</mi></msqrt></mfrac></math>
- **(D)** <math><msqrt><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msqrt><mfrac><mrow><mn>2</mn></mrow><mrow><mi>&#960;</mi></mrow></mfrac></msqrt></math>**

**Detailed Solution:**

<p>Given limit can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>1</mn><mo>-</mo></msup></mrow></munder><mfrac><mrow><msqrt><mi>&#960;</mi></msqrt><mo>-</mo><msqrt><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></msqrt></mrow><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt></mfrac><mo>&#215;</mo><mfrac><mrow><msqrt><mi>&#960;</mi></msqrt><mo>+</mo><msqrt><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></msqrt></mrow><mrow><msqrt><mi>&#960;</mi></msqrt><mo>+</mo><msqrt><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>1</mn><mo>-</mo></msup></mrow></munder><mfrac><mrow><mi>&#960;</mi><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mrow><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mi>&#160;</mi><mfenced separators="|"><mrow><msqrt><mi>&#960;</mi></msqrt><mo>+</mo><msqrt><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></msqrt></mrow></mfenced></mrow></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>1</mn><mo>-</mo></msup></mrow></munder><mfrac><mrow><mn>2</mn><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mrow><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mi>&#160;</mi><mfenced separators="|"><mrow><msqrt><mi>&#960;</mi></msqrt><mo>+</mo><msqrt><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></msqrt></mrow></mfenced></mrow></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>1</mn><mo>-</mo></msup></mrow></munder><mfrac><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt></mfrac></math> and put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>cos</mi><mi>&#952;</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfrac><mi>&#952;</mi><mn>2</mn></mfrac><mo>.</mo><mn>2</mn></mrow><mrow><msqrt><mn>2</mn></msqrt><mo>.</mo><mi>sin</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><msqrt><mn>2</mn></msqrt><mstyle displaystyle="true"><mfrac><mrow><mi>sin</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mfrac></mstyle></mfrac><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mi>x</mi></mfrac><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>L</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>2</mn><mi>&#160;</mi><msqrt><mi>&#960;</mi></msqrt></mrow></mfrac><mo>=</mo><msqrt><mfrac><mn>2</mn><mi>&#960;</mi></mfrac></msqrt></math>.</p>

</details>

---

### Q26. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><msup><mi mathvariant="normal">t</mi><mn>3</mn></msup><mi>x</mi><mo>-</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfrac></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">t</mi></mrow><mn>3</mn></msup><mi>x</mi><mo>-</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfrac></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mfenced separators="|"><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mrow><msup><mi>tan</mi><mn>3</mn></msup><mi>x</mi></mrow></mfrac></mstyle><mo>-</mo><mi>tan</mi><mi>x</mi></mrow></mfenced><mfenced separators="|"><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mi>cos</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mi>sin</mi><mi>x</mi></mrow></mfenced></mfrac><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><mo>&#160;</mo><mi>cot</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>tan</mi><mi>&#952;</mi></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">n</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">n</mi><mn>3</mn></msup><mi>x</mi><mo>.</mo><mfenced separators="|"><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mi>tan</mi><mn>3</mn></msup><mi>x</mi><mo>.</mo><mfenced separators="|"><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mi>cos</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><msqrt><mn>2</mn></msqrt><mfenced open="[" close="]"><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi></mrow></mfenced><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">n</mi><mn>3</mn></msup><mi>x</mi><mo>.</mo><mfenced separators="|"><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><mo>&#160;</mo><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><msqrt><mn>2</mn></msqrt><mfenced open="[" close="]"><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac></mstyle></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi></mrow></mfenced><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mi>tan</mi><mn>3</mn></msup><mi>x</mi><mo>.</mo><mfenced separators="|"><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><msqrt><mn>2</mn></msqrt><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>.</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi></mrow></mfenced><mo>.</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><msup><mi mathvariant="normal">c</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>.</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">n</mi><mn>3</mn></msup><mi>x</mi><mo>.</mo><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><msqrt><mn>2</mn></msqrt><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mi>cos</mi><mi>x</mi><mo>.</mo><mstyle displaystyle="true"><mfrac><mrow><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi></mrow><mrow><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi></mrow></mfrac></mstyle><mo>.</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><msqrt><mn>2</mn></msqrt><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle></mrow></mfenced></mrow><mrow><msup><mi>sin</mi><mn>3</mn></msup><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn></math>.</p>

</details>

---

### Q27. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0} \frac{x \cot (4 x)}{\sin ^{2} x \cot ^{2}(2 x)}$ is equal to:

**Options:**

- **(A)** 0
- **(B)** 2
- **(C)** 4
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

$\lim _{x \rightarrow 0} \frac{x \cot 4 x}{\sin ^{2} x \cdot \cot ^{2} 2 x}=\lim _{x \rightarrow 0} \frac{x \cdot \tan ^{2} 2 x}{\sin ^{2} x \cdot \tan 4 x}$

$=\lim _{x \rightarrow 0}\left(\frac{x}{\sin x}\right)^{2} \cdot\left(\frac{\tan 2 x}{2 x}\right)^{2} \cdot\left(\frac{4 x}{\tan 4 x}\right) \cdot \frac{4}{2^{2}}=1$

</details>

---

### Q28. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $[\mathrm{x}]$ denote the greatest integer less than or equal to $\mathrm{X}$. Then :

$\lim _{x \rightarrow 0} \frac{\tan \left(\pi \sin ^{2} x\right)+(|\mathrm{x}|-\sin (x[x]))^{2}}{x^{2}}$

**Options:**

- **(A)** does not exist
- **(B)** equals $\pi$
- **(C)** equals $\pi+1$
- **(D)** equals 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) does not exist**

**Detailed Solution:**

RHL is, $\lim _{x \rightarrow 0^{+}} \frac{\tan \left(\pi \sin ^{2} x\right)+(x-0)^{2}}{x^{2}}$

$=\lim _{x \rightarrow 0^{+}}\left(\frac{\tan \left(\pi \sin ^{2} x\right.}{x^{2}}+1\right)=1+\pi$

And LHL is, $\lim _{x \rightarrow 0^{-}} \frac{\tan \left(\pi \sin ^{2} x\right)+(-x+\sin x)^{2}}{x^{2}}$

$=\lim _{x \rightarrow 0^{-}} \frac{\tan \left(\pi \sin ^{2} x\right)+x^{2}+\sin ^{2} x-2 x \sin x}{x^{2}}$

$=\pi+1+1-2=\pi$

Since, LHL $\neq$ RHL Hence, limit does not exist.

</details>

---

### Q29. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For each <math><mi>t</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo></math> let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>t</mi></mfenced></math> be the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>1</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced open="|" close="|" separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mfenced open="[" close="]" separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></mrow><mrow><mfenced open="|" close="|" separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mfenced open="[" close="]" separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfrac></math>

**Options:**

- **(A)** equals  <math><mn>0</mn></math>
- **(B)** equals  <math><mo>-</mo><mn>1</mn></math>
- **(C)** does not exist
- **(D)** equal <math><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) equals  <math><mn>0</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>1</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mi>sin</mi><mfenced close="|" open="|"><mrow><mn>1</mn><mo>&#8722;</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>sin</mi><mfenced><mrow><mfenced close="]" open="["><mrow><mn>1</mn><mo>&#8722;</mo><mi>x</mi></mrow></mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></mrow><mrow><mfenced close="|" open="|"><mrow><mn>1</mn><mo>&#8722;</mo><mi>x</mi></mrow></mfenced><mfenced close="]" open="["><mrow><mn>1</mn><mo>&#8722;</mo><mi>x</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mfenced open="|" close="|"><mfenced><mrow><mn>1</mn><mo>+</mo><mi>h</mi></mrow></mfenced></mfenced><mo>+</mo><mi>sin</mi><mfenced open="|" close="|"><mrow><mn>1</mn><mo>&#8722;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>h</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mi>sin</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><mn>1</mn><mo>&#8722;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>h</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced></mrow><mrow><mfenced open="|" close="|"><mrow><mn>1</mn><mo>&#8722;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>h</mi></mrow></mfenced></mrow></mfenced><mfenced open="[" close="]"><mrow><mn>1</mn><mo>&#8722;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>h</mi></mrow></mfenced></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>h</mi><mo>&#8722;</mo><mn>1</mn><mo>+</mo><mi>sin</mi><mfenced close="|" open="|"><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>h</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></mfenced></mrow></mfenced><mi>sin</mi><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>1</mn><mo>&#8722;</mo><mn>1</mn><mo>&#8722;</mo><mi>h</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mfenced close="|" open="|"><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mn>1</mn><mo>&#8722;</mo><mi>h</mi></mrow></mfenced></mfenced><mfenced close="]" open="["><mrow><mn>1</mn><mo>&#8722;</mo><mn>1</mn><mo>&#8722;</mo><mi>h</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mo>&#8722;</mo><mi>h</mi><mo>+</mo><mi>sin</mi><mi>h</mi></mrow></mfenced><mi>sin</mi><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mo>&#8722;</mo><mi>h</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mfenced close="|" open="|"><mrow><mo>-</mo><mi>h</mi></mrow></mfenced><mfenced close="]" open="["><mrow><mo>&#8722;</mo><mi>h</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mo>&#8722;</mo><mi>h</mi><mo>+</mo><mi>sin</mi><mi>h</mi></mrow></mfenced><mi>sin</mi><mfenced><mrow><mo>&#8722;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></mrow><mrow><mi>h</mi><mfenced><mrow><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mo>&#8722;</mo><mi>h</mi><mo>+</mo><mi>sin</mi><mi>h</mi></mrow></mfenced><mfenced><mrow><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mo>&#8722;</mo><mi>h</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>&#8722;</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>.</p>

</details>

---

### Q30. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0} \frac{x \tan 2 x-2 x \tan x}{(1-\cos 2 x)^2}$ equals.

**Options:**

- **(A)** 1
- **(B)** $-\frac{1}{2}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{2}$**

**Detailed Solution:**

Let,
$$
\begin{aligned}
&L=\lim _{x \rightarrow 0} \frac{(x \tan 2 x-2 x \tan x)}{(1-\cos 2 x)^2}=\lim _{x \rightarrow 0} K \text { (say) } \\
&\Rightarrow K=\frac{x\left[\frac{2 \tan x}{1-(\tan x)^2}\right]-2 x \tan x}{\left(1-\left(1-2 \sin ^2 x\right)\right)^2} \\
&=\frac{2 x \tan x-\left[2 x \tan x-2 x \tan ^3 x\right]}{4 \sin ^4 x \times\left(1-\tan ^2 x\right)} \\
&=\frac{2 x \tan ^3 x}{4 \sin ^4 x \times\left(1-\tan ^2 x\right)} \\
&=\frac{2 x \tan ^3 x}{4 \sin ^4 x \times\left(\frac{\cos ^2 x-\sin ^2 x}{\cos ^2 x}\right)}
\end{aligned}
$$

$$
\begin{aligned}
&=\frac{2 x \frac{\sin ^3 x}{\cos ^3 x}}{4 \sin ^4 x \times\left(\frac{\cos ^2 x-\sin ^2 x}{\cos ^2 x}\right)} \\
& \Rightarrow K=\frac{x}{2 \sin x \times\left(\cos ^2 x-\sin ^2 x\right) \cos x} \\
\therefore L &=\lim _{x \rightarrow 0} \frac{x}{2 \sin x} \times \lim _{x \rightarrow 0} \frac{1}{\cos x\left(\cos ^2 x-\sin ^2 x\right)} \\
&=\lim _{x \rightarrow 0} \frac{x}{2 \sin x} \times \lim _{x \rightarrow 0} \frac{1}{\cos 0\left(\cos ^2 0-\sin ^2 0\right)} \\
&=\frac{1}{2}
\end{aligned}
$$

</details>

---

### Q31. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></munder><mfrac><mrow><mi>cot</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow><msup><mfenced separators="|"><mrow><mi>&#960;</mi><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>3</mn></msup></mfrac></math> equals

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>24</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Put, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>h</mi></math> in the given limit, we get

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mfrac><mrow><mi>cot</mi><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>cos</mi><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>h</mi></mrow></mfenced></mrow><msup><mfenced separators="|"><mrow><mi>&#960;</mi><mo>-</mo><mn>2</mn><mo>&#215;</mo><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>h</mi></mrow></mfenced></mrow></mfenced><mn>3</mn></msup></mfrac></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>tan</mi><mi>h</mi><mo>-</mo><mi>sin</mi><mi>h</mi></mrow><msup><mfenced separators="|"><mrow><mi>&#960;</mi><mo>-</mo><mn>2</mn><mo>&#215;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mi>h</mi></mrow></mfenced><mn>3</mn></msup></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced open="[" close="]"><mfrac><mrow><mi>tan</mi><mi>h</mi><mo>-</mo><mi>sin</mi><mi>h</mi></mrow><mrow><mn>8</mn><msup><mi>h</mi><mn>3</mn></msup></mrow></mfrac></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mi>&#160;</mi><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mi>h</mi></mrow><mi>h</mi></mfrac><mfenced open="[" close="]" separators="|"><mfrac><mrow><mi>sec</mi><mi>h</mi><mo>-</mo><mn>1</mn></mrow><msup><mi>h</mi><mn>2</mn></msup></mfrac></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mi>&#160;</mi><mfenced close="]" open="["><mrow><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mi>sin</mi><mi>h</mi></mrow><mi>h</mi></mfrac></mfenced></mrow></mfenced><mfenced close="]" open="["><mrow><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mi>h</mi></mrow><mrow><mfenced><mrow><mi>cos</mi><mi>h</mi></mrow></mfenced><mi>&#160;</mi><msup><mi>h</mi><mn>2</mn></msup></mrow></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mi>&#160;</mi><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mfenced close="]" open="["><mrow><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mi>h</mi></mrow><mrow><mfenced><mrow><mi>cos</mi><mi>h</mi></mrow></mfenced><mi>&#160;</mi><msup><mi>h</mi><mn>2</mn></msup></mrow></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mi>&#160;</mi><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="[" separators="|"><mfrac><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mi>h</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow><mrow><mfenced><mrow><mi>cos</mi><mi>h</mi></mrow></mfenced><mi>&#160;</mi><msup><mi>h</mi><mn>2</mn></msup></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mi>&#160;</mi><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced open="[" close="]"><mfrac><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mfenced separators="|"><mfrac><mi>h</mi><mn>2</mn></mfrac></mfenced></mrow><mrow><mfenced separators="|"><mfrac><msup><mi>h</mi><mn>2</mn></msup><mn>4</mn></mfrac></mfenced><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mi>cos</mi><mi>h</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>16</mn></mfrac></math>.</p>

</details>

---

### Q32. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

<math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder></mrow><mo>&#8289;</mo><mrow><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><mi>x</mi><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>-</mo><mi>x</mi><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></mrow><mi>&#160;</mi></math>is

**Options:**

- **(A)** <math><mn>2</mn></math>
- **(B)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mn>2</mn></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mo>-</mo><mn>2</mn></math>**

**Detailed Solution:**

<p><math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder></mrow><mo>&#8289;</mo><mrow><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><mi>x</mi><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>-</mo><mi>x</mi><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></mrow></math>

<math><mo>=</mo><mi>&#160;</mi><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder></mrow><mo>&#8289;</mo><mrow><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><mi>x</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow><mrow><mn>15</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>-</mo><mi>x</mi><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mfrac><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></msup><mi>&#160;</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mn>2</mn><mfrac><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></msup><mi>&#160;</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow><mrow><mn>15</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced></mrow></mfrac></mrow></mrow></math>

<math><mo>=</mo><mi>&#160;</mi><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder></mrow><mo>&#8289;</mo><mrow><mfrac><mrow><mn>4</mn><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow><mrow><mn>5</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mo>&#8230;</mo><mo>.</mo></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>6</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>15</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>64</mn></mrow><mrow><mn>15</mn></mrow></mfrac></mrow></mfenced></mrow></mfrac></mrow></mrow></math></p><p>(dividing numerator and denominator by <math><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup></math> )

<math><mo>=</mo><mi>&#160;</mi><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder></mrow><mo>&#8289;</mo><mrow><mfrac><mrow><mn>4</mn><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><mn>5</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mo>&#8230;</mo><mo>.</mo></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><mo>-</mo><mn>2</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>60</mn></mrow><mrow><mn>15</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mo>&#8230;</mo></mrow></mfrac></mrow></mrow></math>

<math><mo>=</mo><mi>&#160;</mi><mo>-</mo><mn>2</mn></math></p>

</details>

---

### Q33. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mfrac><mrow><msup><mi mathvariant="normal">e</mi><msup><mi>x</mi><mn>2</mn></msup></msup><mo>-</mo><mi>cos</mi><mo>&#8289;</mo><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#160;</mi><mi>x</mi></mrow></mfrac><mi>&#160;</mi></math>is equal to

**Options:**

- **(A)** <math><mn>2</mn></math>
- **(B)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi mathvariant="normal">e</mi><msup><mi>x</mi><mn>2</mn></msup></msup><mo>-</mo><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mspace linebreak="newline"></mspace><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mo>(</mo><msup><mi mathvariant="normal">e</mi><msup><mi>x</mi><mn>2</mn></msup></msup><mo>&#8722;</mo><mn>1</mn><mo>)</mo><mo>+</mo><mo>(</mo><mn>1</mn><mo>&#8722;</mo><mi>cos</mi><mi>x</mi><mo>)</mo></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#183;</mo><mfenced><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mrow><mfrac><mrow><msup><mi mathvariant="normal">e</mi><msup><mi>x</mi><mn>2</mn></msup></msup><mo>&#8722;</mo><mn>1</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>&#8722;</mo><mi>cos</mi><mi>x</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>

</details>

---

### Q34. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mo>cos</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>3</mn><mo>+</mo><mo>cos</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mi>x</mi><mo>tan</mo><mn>4</mn><mi>x</mi></mrow></mfrac><mo>=</mo></math>

**Options:**

- **(A)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mfrac><mrow><mo>(</mo><mn>1</mn><mo>-</mo><mi>cos</mi><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi><mo>)</mo><mi>&#160;</mi><mi>&#160;</mi><mo>(</mo><mn>3</mn><mo>+</mo><mi>cos</mi><mo>&#8289;</mo><mrow><mi>x</mi><mo>)</mo></mrow></mrow></mrow><mrow><mi>x</mi><mi>tan</mi><mo>&#8289;</mo><mn>4</mn><mi>x</mi></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#160;</mi><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mfrac><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mrow><mi>x</mi><mi>&#160;</mi><mo>&#8901;</mo><mo>(</mo><mn>3</mn><mo>+</mo><mi>cos</mi><mo>&#8289;</mo><mi>x</mi><mo>)</mo></mrow></mrow><mrow><mi>x</mi><mo>&#8901;</mo><mi>tan</mi><mo>&#8289;</mo><mn>4</mn><mi>x</mi></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#160;</mi><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mfrac><mrow><mn>2</mn><mo>&#8901;</mo><msup><mfenced separators="|"><mfrac><mrow><mi>sin</mi><mo>&#8289;</mo><mi>x</mi></mrow><mi>x</mi></mfrac></mfenced><mn>2</mn></msup><mo>&#8901;</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mfrac><mrow><mi>tan</mi><mo>&#8289;</mo><mn>4</mn><mi>x</mi></mrow><mrow><mn>4</mn><mi>x</mi></mrow></mfrac><mi>&#160;</mi><mo>&#8901;</mo><mn>4</mn></mrow></mfrac></math>

<math><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mn>2</mn><mo>&#8901;</mo><msup><mrow><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><mo>&#8901;</mo><mo>(</mo><mn>3</mn><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><mn>1</mn><mi>&#160;</mi><mo>&#8901;</mo><mn>4</mn></mrow></mfrac></math>

<math><mo>=</mo><mn>2</mn></math> .

</details>

---

### Q35. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If $\lim _{x \rightarrow 2} \frac{\tan \left(x-2\left\{x^2+k+2 x-2 k\right\}\right.}{x^2-4 x+4}=5$, then $\mathrm{k}$ is equal to:

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

$$
\begin{aligned}
\text { } & \lim _{x \rightarrow 2} \frac{\tan (x-2)\left\{x^2+(k-2) x-2 k\right\}}{x^2-4 x+4}=5 \\
\Rightarrow & \lim _{x \rightarrow 2} \frac{\tan (x-2)\left\{x^2+k x-2 x-2 k\right\}}{(x-2)^2}=5 \\
\Rightarrow & \lim _{x \rightarrow 2} \frac{\tan (x-2)\{x(x-2)+k(x-2)\}}{(x-2) \times(x-2)}=5 \\
\Rightarrow \lim _{x \rightarrow 2}\left(\frac{\tan (x-2)}{(x-2)}\right) \times \lim _{x \rightarrow 2}\left(\frac{(k+x)(x-2)}{(x-2)}\right)=5 \\
\Rightarrow & 1 \times \lim _{x \rightarrow 2}(k+x)=5 \\
&\left\{\because \lim _{h \rightarrow 0} \frac{\tan h}{h}=1\right\} \\
& \text { or } k+2=5 \\
\Rightarrow k=3
\end{aligned}
$$

</details>

---

### Q36. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>9</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>9</mn></mfrac><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>3</mn><mi>x</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced></math> equals to

**Options:**

- **(A)** <math> <mrow> <mfrac> <mrow> <mn>8</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> </mrow> </math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math> <mrow> <mfrac> <mrow> <mn>2</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>9</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math> <mrow> <mfrac> <mrow> <mn>2</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

Given:  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>9</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>9</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous.

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mo>cos</mo><mn>3</mn><mi>x</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>1</mn><mo>-</mo><mo>cos</mo><mn>3</mn><mi>x</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>f</mi><mfenced><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>2</mn><msup><mo>sin</mo><mn>2</mn></msup><mfenced><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>&#8757;</mo><mo>&#160;</mo><mn>1</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></math>


<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>f</mi><mfenced><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>2</mn><msup><mo>sin</mo><mn>2</mn></msup><mfenced><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow><mrow><mfrac><mn>4</mn><mn>9</mn></mfrac><msup><mfenced><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></mrow></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>f</mi><mfenced><mrow><mfrac><mn>9</mn><mn>2</mn></mfrac><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mo>sin</mo><mn>2</mn></msup><mfenced><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow><msup><mfenced><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>f</mi><mfenced><mrow><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>&#215;</mo><msup><mn>1</mn><mn>2</mn></msup></mrow></mfenced></math>     <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mi>x</mi></mfrac><mo>=</mo><mn>1</mn></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>f</mi><mfenced><mfrac><mn>9</mn><mn>2</mn></mfrac></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2</mn><mn>9</mn></mfrac></math>

</details>

---

### Q37. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mfenced><mrow><msup><mi>&#960;cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></math> is equal to

**Options:**

- **(A)** <math> <mrow> <mo>-</mo> <mi>&pi;</mi> </mrow> </math>
- **(B)** <math> <mrow> <mi>π</mi> </mrow> </math>
- **(C)** <math> <mrow> <mfrac> <mrow> <mi>&pi;</mi> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math> <mrow> <mi>π</mi> </mrow> </math>**

**Detailed Solution:**

We have  <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi mathvariant="normal">x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mfenced><mrow><msup><mi>&#960;cos</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow></mfenced></mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi mathvariant="normal">x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><msup><mi>&#960;cos</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow></mfenced></mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mfrac></math>                 <math> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <mo>&#8757;&#160;&#160;</mo> <mtext>sin</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mi>&#960;</mi> <mo>-</mo> <mi>&#952;</mi> </mrow> </mfenced> <mo>=</mo> <mtext>sin&#160;</mtext> <mi>&#952;</mi> </mrow> </mfenced> </mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>=</mtext><munder><mi>lim</mi><mrow><mi mathvariant="normal">x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>&#160;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow></mfenced></mrow><mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>&#160;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow></mfenced></mfrac><mo>&#215;</mo><mfrac><mrow><mi mathvariant="normal">&#960;</mi><mo>&#160;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>=</mtext><munder><mi>lim</mi><mrow><mi mathvariant="normal">x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi mathvariant="normal">&#960;</mi><mfenced open="[" close="]"><mfrac><mrow><mi>sin</mi><mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>&#160;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow></mfenced></mrow><mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>&#160;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow></mfenced></mfrac></mfenced></math>  <math> <mrow> <msup> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <mfrac> <mrow> <mtext>sin&#160;</mtext> <mtext>x</mtext> </mrow> <mrow> <mtext>x</mtext> </mrow> </mfrac> </mrow> </mfenced> </mrow> <mn>2</mn> </msup> </mrow> </math>     

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#960;</mi><mfenced><mn>1</mn></mfenced><mfenced><mn>1</mn></mfenced></math>     <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mi>As</mi><mo>,</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi mathvariant="normal">x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">t</mi></mrow><mi mathvariant="normal">t</mi></mfrac><mo>=</mo><mn>1</mn></mrow></mfenced></math>

<math> <mrow> <mo>=</mo> <mi>&#960;</mi> </mrow> </math>.

</details>

---

### Q38. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\lim _{x \rightarrow 0} \frac{1}{x}\left[\tan ^{-1}\left(\frac{x+1}{2 x+1}\right)-\frac{\pi}{4}\right]$ is :

**Options:**

- **(A)** 1
- **(B)** $-\frac{1}{2}$
- **(C)** 2
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{1}{2}$**

**Detailed Solution:**

$\lim _{x \rightarrow 0}\left(\frac{1}{x}\right)\left[\tan ^{-1}\left(\frac{x+1}{2 x+1}\right)-\frac{\pi}{4}\right]$
$=\lim _{x \rightarrow 0}\left(\frac{1}{x}\right)\left[\tan ^{-1}\left(\frac{x+1}{2 x+1}\right)-\tan ^{-1}(1)\right]$
$=\lim _{x \rightarrow 0}\left(\frac{1}{x}\right) \cdot \tan ^{-1}\left(\frac{\frac{x+1}{2 x+1}-1}{1+\frac{x+1}{2 x+1}}\right)$
$=\lim _{x \rightarrow 0} \frac{1}{x} \cdot \tan ^{-1}\left(\frac{-x}{3 x+2}\right)$
$=-\lim _{x \rightarrow 0}\left[\frac{\tan ^{-1}\left(\frac{x}{3 x+2}\right)}{\frac{x}{3 x+2}} \times \frac{1}{3 x+2}\right]=-\frac{1}{2}$

</details>

---

### Q39. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>3</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mi>x</mi><mi>tan</mi><mn>4</mn><mi>x</mi></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math><mrow>  <mn>1</mn></mrow></math>
- **(B)** <math> <mrow> <mn>2</mn> </mrow> </math>
- **(C)** <math> <mrow> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math> <mrow> <mn>2</mn> </mrow> </math>**

**Detailed Solution:**

Given <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>3</mn><mo>+</mo><mi>cos</mi><mo>&#160;</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mi>x</mi><mo>&#160;</mo><mi>tan</mi><mo>&#160;</mo><mn>4</mn><mi>x</mi></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><mn>3</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mi>x</mi><mo>&#160;</mo><mi>tan</mi><mo>&#160;</mo><mn>4</mn><mi>x</mi></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced><mfrac><mrow><mi>sin</mi><mo>&#160;</mo><mi>x</mi></mrow><mi>x</mi></mfrac></mfenced><mn>2</mn></msup><mfenced><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mrow><mi>tan</mi><mo>&#160;</mo><mn>4</mn><mi>x</mi></mrow></mfrac></mfenced><mfenced><mrow><mn>3</mn><mo>+</mo><mi>cos</mi><mo>&#160;</mo><mi>x</mi></mrow></mfenced><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn></math>

</details>

---

### Q40. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0} \frac{\sin \left(\pi \cos ^2 x\right)}{x^2}$ equals

**Options:**

- **(A)** $-\pi$
- **(B)** 1
- **(C)** $-1$
- **(D)** $\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\pi$**

**Detailed Solution:**

Consider
$$
\begin{aligned}
& \lim _{x \rightarrow 0} \frac{\sin \left(\pi \cos ^2 x\right)}{x^2} \\
& =\lim _{x \rightarrow 0} \frac{\sin \left(\pi-\pi \sin ^2 x\right)}{x^2} \\
& =\lim _{x \rightarrow 0} \frac{\sin \left(\pi \sin ^2 x\right)}{\pi \sin ^2 x} \times \frac{\left(\pi \sin ^2 x\right)}{x^2}=\pi
\end{aligned}
$$

</details>

---

### Q41. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `3`

$\lim _{x \rightarrow 0}\left(\frac{x-\sin x}{x}\right) \sin \left(\frac{1}{x}\right)$

**Options:**

- **(A)** equals 1
- **(B)** equals 0
- **(C)** does not exist
- **(D)** equals $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) equals 0**

**Detailed Solution:**

Consider $\lim _{x \rightarrow 0}\left(\frac{x-\sin x}{x}\right) \sin \left(\frac{1}{x}\right)$
$=\lim _{x \rightarrow 0}\left[\frac{x\left(1-\frac{\sin x}{x}\right)}{x}\right] \times \lim _{x \rightarrow 0} \sin \left(\frac{1}{x}\right)$
$=\lim _{x \rightarrow 0}\left[1-\frac{\sin x}{x}\right] \times \lim _{x \rightarrow 0} \sin \left(\frac{1}{x}\right)$
$=\left[1-\lim _{x \rightarrow 0} \frac{\sin x}{x}\right] \times \lim _{x \rightarrow 0} \sin \left(\frac{1}{x}\right)$
$=0 \times \lim _{x \rightarrow 0} \sin \left(\frac{1}{x}\right)=0$

</details>

---

### Q42. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `1`

$$
\lim _{x \rightarrow 2}\left(\frac{\sqrt{1-\cos \{2(x-2)\}}}{x-2}\right)

**Options:**

- **(A)** equals $\sqrt{2}$
- **(B)** equals $-\sqrt{2}$
- **(C)** equals $\frac{1}{\sqrt{2}}$
- **(D)** does not exist

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) does not exist**

**Detailed Solution:**

$$
\begin{aligned}
& \lim _{x \rightarrow 2} \frac{\sqrt{2 \sin ^2(x-2)}}{x-2} \\
& \lim _{x \rightarrow 2} \frac{\sqrt{2}|\sin (x-2)|}{x-2} \\
& \text { R.H.L. }=\sqrt{2}, \text { L.H.L. }=-\sqrt{2}
\end{aligned}
$$
Limit does not exist.

</details>

---

### Q43. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `3`

$\lim _{n \rightarrow \infty}\left[\frac{1}{n^2} \sec ^2 \frac{1}{n^2}+\frac{2}{n^2} \sec ^2 \frac{4}{n^2}+\ldots .+\frac{1}{n^2} \sec ^2 1\right]$ equals

**Options:**

- **(A)** $\frac{1}{2} \sec 1$
- **(B)** $\frac{1}{2} \operatorname{cosec} 1$
- **(C)** $\tan 1$
- **(D)** $\frac{1}{2} \tan 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{2} \tan 1$**

**Detailed Solution:**

$\lim _{n \rightarrow \infty}\left[\frac{1}{n^2} \sec ^2 \frac{1}{n^2}+\frac{2}{n^2} \sec ^2 \frac{4}{n^2}+\frac{3}{n^2} \sec ^2 \frac{9}{n^2}+\ldots .+\frac{1}{n} \sec ^2 1\right]$ is equal to $\lim _{n \rightarrow \infty} \frac{r}{n^2} \sec ^2 \frac{r^2}{n^2}=\lim _{n \rightarrow \infty} \frac{1}{n} \cdot \frac{r}{n} \sec ^2 \frac{r^2}{n^2}$
$\Rightarrow$ Given limit is equal to value of integral $\int_0^1 x \sec ^2 x^2 d x$
or $\frac{1}{2} \int_0^1 2 x \sec x^2 d x=\frac{1}{2} \int_0^1 \sec ^2 t d t$
[put $\left.x^2=t\right]$ $=\frac{1}{2}(\tan t)_0^1=\frac{1}{2} \tan 1$.

</details>

---

### Q44. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

Let $f(x)=\frac{1-\tan x}{4 x-\pi}, x \neq \frac{\pi}{4}, x \in\left[0, \frac{\pi}{2}\right]$. If $f(x)$ is continuous in $\left[0, \frac{\pi}{2}\right]$, then $f\left(\frac{\pi}{4}\right)$ is

**Options:**

- **(A)** 1
- **(B)** $\frac{1}{2}$
- **(C)** $-\frac{1}{2}$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\frac{1}{2}$**

**Detailed Solution:**

$f(x)=\frac{1-\tan x}{4 x-\pi} \Rightarrow \lim _{x \rightarrow \frac{\pi}{4}} \frac{1-\tan x}{4 x-\pi}=-\frac{1}{2}$

</details>

---

### Q45. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

$$
\lim _{x \rightarrow \frac{\pi}{2}} \frac{\left[1-\tan \left(\frac{x}{2}\right)\right][1-\sin x]}{\left[1+\tan \left(\frac{x}{2}\right)\right]\left[\pi-2 x^3\right]}
$$
is

**Options:**

- **(A)** $\infty$
- **(B)** $\frac{1}{8}$
- **(C)** 0
- **(D)** $\frac{1}{32}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{32}$**

**Detailed Solution:**

$\lim _{x \rightarrow \frac{\pi}{2}} \frac{\tan \left(\frac{\pi}{4}-\frac{x}{2}\right) \cdot(1-\sin x)}{(\pi-2 x)^3}$
Let $\mathrm{x}=\frac{\pi}{2}+\mathrm{y} ; \mathrm{y} \rightarrow 0$
$=\lim _{y \rightarrow 0} \frac{-\tan \left(-\frac{y}{2}\right) \cdot(1-\cos y)}{(-2 y)^3}=\lim _{y \rightarrow 0} \frac{-\tan \frac{y}{2} 2 \sin ^2 \frac{y}{2}}{(-8) \cdot \frac{y^3}{8} \cdot 8}$
$=\lim _{y \rightarrow 0} \frac{1}{32} \frac{\tan \frac{y}{2}}{\left(\frac{y}{2}\right)} \cdot\left[\frac{\sin y / 2}{y / 2}\right]^2=\frac{1}{32}$

</details>

---

### Q46. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `1`

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/UijjHtHxFoLykxDx1EjMtI16lxmtgmfHqcIFJcwuLfY.original.fullsize.png">

**Options:**

- **(A)** 1
- **(B)** -1
- **(C)** zero
- **(D)** does not exist

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

$$
\operatorname{Lim}_{x \rightarrow 0} \frac{\sqrt{1-\cos 2 x}}{\sqrt{2} x} \Rightarrow \operatorname{Lim}_{x \rightarrow 0} \frac{\sqrt{1-\left(1-2 \sin ^2 x\right)}}{\sqrt{2} x} ; \operatorname{Lim}_{x \rightarrow 0} \frac{\sqrt{2 \sin ^2 x}}{\sqrt{2} x} \Rightarrow \operatorname{Lim}_{x \rightarrow 0} \frac{|\sin x|}{x}
$$
the function does not exist or $\mathrm{LHS} \neq \mathrm{RHS}$

</details>

---

