# JEE Main Mathematics - Quadratic Equation

## Topic 5: Location of Roots

**Total Questions:** 15

---

### Q1. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $e_1$ and $e_2$ be two distinct roots of the equation $x^2 - ax + 2 = 0$. Let the sets $\{a \in \mathbb{R} : e_1 \text{ and } e_2 \text{ are the eccentricities of hyperbolas}\} = (\alpha, \beta)$, and $\{a \in \mathbb{R} : e_1 \text{ and } e_2 \text{ are the eccentricities of an ellipse and a hyperbola, respectively}\} = (\gamma, \infty)$. Then $\alpha^2 + \beta^2 + \gamma^2$ is equal to:

**Options:**

- **(A)** $18$
- **(B)** $22$
- **(C)** $26$
- **(D)** $34$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $26$**

**Detailed Solution:**

The given quadratic equation is $x^2 - ax + 2 = 0$ with roots $e_1$ and $e_2$.

The sum of the roots is $e_1 + e_2 = a$ and the product is $e_1 e_2 = 2$.

For the roots to be real and distinct, the discriminant must be positive:

$\Delta = a^2 - 8 > 0 \Rightarrow a \in (-\infty, -2\sqrt{2}) \cup (2\sqrt{2}, \infty)$

Since $e_1$ and $e_2$ represent eccentricities, they must be positive. Given $e_1 e_2 = 2 > 0$, both roots have the same sign. For them to be positive, their sum must be positive, so $a > 0$. Thus, $a > 2\sqrt{2}$.

For $e_1$ and $e_2$ to be the eccentricities of hyperbolas, both must be strictly greater than $1$. This requires $1$ to lie outside the roots and the vertex of the parabola to be to the right of $1$:

$(e_1 - 1)(e_2 - 1) > 0 \Rightarrow e_1 e_2 - (e_1 + e_2) + 1 > 0$

$2 - a + 1 > 0 \Rightarrow a < 3$

Combining this with the discriminant condition, we get $a \in (2\sqrt{2}, 3)$.

Thus, $\alpha = 2\sqrt{2}$ and $\beta = 3$.

For $e_1$ and $e_2$ to be the eccentricities of an ellipse and a hyperbola, one root must be in $(0, 1)$ and the other in $(1, \infty)$. This requires $1$ to lie between the roots:

$(e_1 - 1)(e_2 - 1) < 0 \Rightarrow 2 - a + 1 < 0 \Rightarrow a > 3$

For $a > 3$, the roots are real, distinct, and positive. Thus, the set of such $a$ is $(3, \infty)$.

This gives $\gamma = 3$.

Finally, calculating the required sum:

$\alpha^2 + \beta^2 + \gamma^2 = (2\sqrt{2})^2 + 3^2 + 3^2 = 8 + 9 + 9 = 26$

Answer: $26$

</details>

---

### Q2. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the quadratic equation $(\lambda+2)x^2-3\lambda x+4\lambda=0$, $\lambda \neq -2$, has two positive roots, then the number of possible integral values of $\lambda$ is:

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $3$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$**

**Detailed Solution:**

For the quadratic equation $(\lambda+2)x^2-3\lambda x+4\lambda=0$ to have two positive roots, the following three conditions must be satisfied:

1. Discriminant $D \ge 0$
$(-3\lambda)^2 - 4(\lambda+2)(4\lambda) \ge 0$
$9\lambda^2 - 16\lambda^2 - 32\lambda \ge 0$
$-7\lambda^2 - 32\lambda \ge 0$
$7\lambda^2 + 32\lambda \le 0$
$\lambda(7\lambda + 32) \le 0$
$\lambda \in \left[-\dfrac{32}{7}, 0\right]$

2. Sum of roots $> 0$
$\alpha + \beta = \dfrac{3\lambda}{\lambda+2} > 0$
$\lambda \in (-\infty, -2) \cup (0, \infty)$

3. Product of roots $> 0$
$\alpha \beta = \dfrac{4\lambda}{\lambda+2} > 0$
$\lambda \in (-\infty, -2) \cup (0, \infty)$

Taking the intersection of all three conditions, we get:
$\lambda \in \left[-\dfrac{32}{7}, -2\right)$

Since $-\dfrac{32}{7} \approx -4.57$, the possible integral values of $\lambda$ in this interval are $-4$ and $-3$.

Thus, there are $2$ possible integral values of $\lambda$.

Answer: $2$

</details>

---

### Q3. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha$ and $\beta$ be the roots of the equation $x^{2}+2 a x+(3 a+10)=0$ such that $\alpha<1<\beta$. Then the set of all possible values of $a$ is :

**Options:**

- **(A)** $\left(-\infty, \frac{-11}{5}\right)$
- **(B)** $(-\infty,-2) \cup(5, \infty)$
- **(C)** $(-\infty,-3)$
- **(D)** $\left(-\infty, \frac{-11}{5}\right) \cup(5, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(-\infty, \frac{-11}{5}\right)$**

**Detailed Solution:**

Let $f(x) = x^2 + 2ax + (3a + 10)$. For $\alpha < 1 < \beta$, since the leading coefficient is positive, we need $f(1) < 0$.
$f(1) = 1 + 2a + 3a + 10 = 5a + 11 < 0$
$a < -\frac{11}{5}$
When $f(1) < 0$ with positive leading coefficient, the parabola is negative at $x = 1$, so 1 lies strictly between the two real roots. Discriminant is automatically positive.
$a \in \left(-\infty, -\frac{11}{5}\right)$.

</details>

---

### Q4. JEE Main 2024 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

The number of distinct real roots of the equation $|x+1||x+3|-4|x+2|+5=0$, is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

$|x+1||x+3|-4|x+2|+5=0$
case-1
$\begin{aligned}
& x \leq-3 \\
& (x+1)(x+3)+4(x+2)+5=0 \\
& x^2+4 x+3+4 x+8+5=0 \\
& x^2+8 x+16=0 \\
& (x+4)^2=0 \\
& x=-4
\end{aligned}$
case-2
$\begin{aligned}
& -3 \leq x \leq-2 \\
& -x^2-4 x-3+4 x+8+5=0 \\
& -x^2+10=0 \\
& x= \pm \sqrt{10}
\end{aligned}$
case-3
$\begin{aligned}
& -2 \leq x \leq-1 \\
& -x^2-4 x-3-4 x-8+5=0 \\
& -x^2-8 x-6=0 \\
& x^2+8 x+6=0 \\
& x=\frac{-8 \pm 2 \sqrt{10}}{2}=-4 \pm \sqrt{10}
\end{aligned}$
case-4
$\begin{aligned}
& x \geq-1 \\
& x^2+4 x+3-4 x-8+5=0 \\
& x^2=0 \\
& x=0
\end{aligned}$
No. of solution $=2$

</details>

---

### Q5. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The number of integral values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math>, for which one root of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mi>k</mi><mo>=</mo><mn>0</mn></math> lies in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> and its other root lies in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mi>k</mi><mo>=</mo><mn>0</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6ee01238-1f66-43ed-9b7a-c5f8b4ade02e-9896775.png" style="width: 350px; height: 129px;" /></p><p> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>&#62;</mo><mn>0</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#62;</mo><mn>0</mn><mo>&#8658;</mo><mn>2</mn><mo>-</mo><mn>8</mn><mo>+</mo><mi>k</mi><mo>&#62;</mo><mn>0</mn><mo>&#8658;</mo><mi>k</mi><mo>&#62;</mo><mn>6</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>&#60;</mo><mn>0</mn><mo>&#8658;</mo><mn>8</mn><mo>-</mo><mn>16</mn><mo>+</mo><mi>k</mi><mo>&#60;</mo><mn>0</mn><mo>&#8658;</mo><mi>k</mi><mo>&#60;</mo><mn>8</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>&#62;</mo><mn>0</mn><mo>&#8658;</mo><mn>18</mn><mo>-</mo><mn>24</mn><mo>+</mo><mi>k</mi><mo>&#62;</mo><mn>0</mn><mo>&#8658;</mo><mi>k</mi><mo>&#62;</mo><mn>6</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>3</mn><mo>)</mo></math></p><p>From equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>3</mn></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8712;</mo><mo>(</mo><mn>6</mn><mo>,</mo><mn>8</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Integral value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>7</mn></math></p><p>Therefore number of integral value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is one</p>

</details>

---

### Q6. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The set of all real values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> for which the quadratic equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>&#955;</mi><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math> always have exactly one root in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>)</mo></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8722;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>]</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>]</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>]</mo></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#8804;</mo><mn>0</mn><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math></p><p>But at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>1</mn></math>, both roots are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8800;</mo><mn>1</mn></math></p>

</details>

---

### Q7. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> be a quadratic polynomial such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>&#8211;</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>0</mn></math>. If one of the roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>, then its other root lies in

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8211;</mo><mn>3</mn><mo>,</mo><mo>&#8211;</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>**

**Detailed Solution:**

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></math> be a quadratic equation with roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>5</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mn>2</mn><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p> Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>9</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>a</mi><mrow><mo>-</mo><mn>5</mn></mrow></mfrac><mo>=</mo><mfrac><mi>b</mi><mn>13</mn></mfrac><mo>=</mo><mfrac><mi>c</mi><mn>6</mn></mfrac></math></p><p>Product of roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mfrac><mi>c</mi><mi>a</mi></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>6</mn><mn>5</mn></mfrac></math></p><p>We know <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p>

</details>

---

### Q8. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Consider the quadratic equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>c</mi><mo>-</mo><mn>5</mn></mrow></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>c</mi><mi>x</mi><mo>+</mo><mfenced separators="|"><mrow><mi>c</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>&#8800;</mo><mn>5</mn><mo>.</mo></math> Let <math><mi>S</mi></math> be the set of all integral values of <math><mi>c</mi></math> for which one root of the equation lies in the interval <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn></mrow></mfenced></math> and its other root lies in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn></mrow></mfenced><mo>.</mo></math> Then the number of elements in <math><mi>S</mi></math> is

**Options:**

- **(A)** <math><mn>11</mn></math>
- **(B)** <math><mn>12</mn></math>
- **(C)** <math><mn>18</mn></math>
- **(D)** <math><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>11</mn></math>**

**Detailed Solution:**

<p>Case <math><mo>-</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>-</mo><mn>5</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>&#62;</mo><mn>5</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Then, the graph of the quadratic is shown below</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/gscjfoyhgrrgbmxpfyaslgibjtijkccgnqjictepkbbhlrkqov.png" /></p><p>Hence, we have <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>-</mo><mn>4</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>&#62;</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>And <math><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mfenced separators="|"><mrow><mi>c</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mn>4</mn><mi>c</mi><mo>+</mo><mi>c</mi><mo>-</mo><mn>4</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>c</mi><mo>-</mo><mn>20</mn><mo>-</mo><mn>4</mn><mi>c</mi><mo>+</mo><mi>c</mi><mo>-</mo><mn>4</mn><mo>&#60;</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>&#60;</mo><mn>24</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>And <math><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mfenced separators="|"><mrow><mi>c</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mn>6</mn><mi>c</mi><mo>+</mo><mi>c</mi><mo>-</mo><mn>4</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mi>c</mi><mo>-</mo><mn>45</mn><mo>-</mo><mn>6</mn><mi>c</mi><mo>+</mo><mi>c</mi><mo>-</mo><mn>4</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>c</mi><mo>-</mo><mn>49</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>&#62;</mo><mfrac><mn>49</mn><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced></math></p><p>Hence, on taking the intersection of all the above inequalities, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mfrac><mn>49</mn><mn>4</mn></mfrac><mo>,</mo><mi>&#160;</mi><mn>24</mn></mrow></mfenced><mo>.</mo></math>

Case <math><mo>-</mo><mi>I</mi><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>-</mo><mn>5</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>&#60;</mo><mn>5</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>v</mi></mfenced></math></p><p>Then, the graph of the quadratic is shown below</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/pwjejsjfraighlufurgrcpuwbgfvjpoiqtnasdczbmartybolf.png" />

Hence, we have <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>&#60;</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>v</mi><mi>i</mi></mrow></mfenced></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>2</mn></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>&#62;</mo><mn>24</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>v</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>3</mn></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>&#60;</mo><mfrac><mn>49</mn><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>v</mi><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Hence, on taking the intersection of all the above inequalities, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>&#8712;</mo><mi>&#981;</mi></math></p><p>Hence, <math><mi>c</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>49</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>,</mo><mi>&#160;</mi><mn>24</mn></mrow></mfenced></math></p><p>Hence, the total number of element in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>.</mo></math></p>

</details>

---

### Q9. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If both the roots of the quadratic equation <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>m</mi><mi>x</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> are real and distinct and they lie in the interval <math><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>5</mn></mrow></mfenced><mo>,</mo></math> then <math><mi>m</mi></math> lies in the interval:

Note: In the actual JEE paper interval was <math><mfenced close="]" open="[" separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>5</mn></mrow></mfenced></math>

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mo>-</mo><mn>5</mn><mo>,</mo><mo>-</mo><mn>4</mn></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mi> </mi><mn>4</mn></mrow></mfenced></math>
- **(C)** <math><mo>(</mo><mn>5</mn><mo>,</mo><mi> </mi><mn>6</mn><mo>)</mo></math>
- **(D)** <math><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mi> </mi><mn>5</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mi> </mi><mn>5</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given roots of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>m</mi><mi>x</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> are distinct and lies in <math><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>5</mn></mrow></mfenced><mo>,</mo></math> Following conditions must be true

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>i</mi><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>&#62;</mo><mn>0</mn><mo>&#8658;</mo><msup><mi>m</mi><mn>2</mn></msup><mo>-</mo><mn>16</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>m</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi>m</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mo>-</mo><mi>&#8734;</mi><mo>,</mo><mi>&#160;</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>&#8746;</mo><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>i</mi><mi>i</mi><mo>)</mo></math> <math><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn><mo>&#8658;</mo><mi>m</mi><mo>&#60;</mo><mn>5</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>i</mi><mi>i</mi><mi>i</mi><mo>)</mo></math> <math><mi>f</mi><mfenced separators="|"><mrow><mn>5</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn><mo>&#8658;</mo><mi>m</mi><mo>&#60;</mo><mfrac><mrow><mn>29</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi>&#160;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>i</mi><mi>v</mi><mo>)</mo></math> <math><mn>1</mn><mo>&#60;</mo><mo>-</mo><mfrac><mrow><mi>b</mi></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac><mo>&#60;</mo><mn>5</mn><mo>&#8658;</mo><mn>2</mn><mo>&#60;</mo><mi>m</mi><mo>&#60;</mo><mn>10</mn></math>

Taking intersection of all conditions, we get <math><mi>m</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mi>&#160;</mi><mn>5</mn></mrow></mfenced></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a8075e17-6564-4f9a-b182-69e91ed46a96-image.png" style="width: 285px; height: 215px;" /></p>

</details>

---

### Q10. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `3`

The real number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> for which the equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>k</mi><mo>=</mo><mn>0</mn></math> has two distinct real roots in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>]</mo></math> belongs to

**Options:**

- **(A)** lies between <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>.
- **(B)** does not exist.
- **(C)** lies between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>.
- **(D)** lies between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) does not exist.**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></math>

As <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math>  for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is a strictly increasing function for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>.

Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> cannot have more than one root.</p>

</details>

---

### Q11. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `2`

Consider a quadratic equation $a x^2+b x+c=0$, where $2 a+3 b+6 c=0$ and let $g(x)=a \frac{x^3}{3}+b \frac{x^2}{2}+c x$.
Statement 1: The quadratic equation has at least one root in the interval $(0,1)$.
Statement 2: The Rolle's theorem is applicable to function $g(x)$ on the interval $[0,1]$.

**Options:**

- **(A)** Statement 1 is false, Statement 2 is true.
- **(B)** Statement 1 is true, Statement 2 is false.
- **(C)** Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation for Statement 1.
- **(D)** Statement 1 is true, Statement 2 is true, , Statement 2 is a correct explanation for Statement 1.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Statement 1 is true, Statement 2 is true, , Statement 2 is a correct explanation for Statement 1.**

**Detailed Solution:**

Let $g(x)=\frac{a x^3}{3}+b \cdot \frac{x^2}{2}+c x$
$$
\mathrm{g}^{\prime}(x)=a x^2+b x+c
$$
Given: $a x^2+b x+c=0$ and $2 a+3 b+6 c=0$
Statement-2:
(i) $g(0)=0$ and $g(1)$

$$
\begin{aligned}
& =\frac{a}{3}+\frac{b}{2}+c=\frac{2 a+3 b+6 c}{6} \\
& =\frac{0}{6}=0 \\
& \Rightarrow g(0)=g(1)
\end{aligned}
$$
(ii) $g$ is continuous on $[0,1]$ and differentiable on $(0,1)$
$\therefore$ By Rolle's theorem $\exists k \in(0,1)$ such that $g^{\prime}(k)=0$
This holds the statement 2. Also, from statement-2, we can say $a x^2+b x+c=0$ has at least one root in $(0,1)$.
Thus statement-1 and 2 both are true and statement-2 is a correct explanation for statement-1.

</details>

---

### Q12. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `3`

If the difference between the roots of the equation $x^2+a x+1=0$ is less than $\sqrt{5}$, then the set of possible values of $a$ is

**Options:**

- **(A)** $(-3,3)$
- **(B)** $(-3, \infty)$
- **(C)** $(3, \infty)$
- **(D)** $(-\infty,-3)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(-3,3)$**

**Detailed Solution:**

$x^2+a x+1=0$
$\alpha+\beta=-a \quad \alpha \beta=1$
$|\alpha-\beta|=\sqrt{(\alpha+\beta)^2-4 \alpha \beta}$
$|\alpha-\beta|=\sqrt{a^2-4}$
$\sqrt{a^2-4} < \sqrt{5}$
$a^2-4 < 5$
$a^2-9 < 0$
$a \in(-3,3)$.

</details>

---

### Q13. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `2`

All the values of $m$ for which both roots of the equations $x^2-2 m x+m^2-1=0$ are greater than $-2$ but less than 4 , lie in the interval

**Options:**

- **(A)** −2  < m < 0
- **(B)** m > 3
- **(C)** −1  < m < 3
- **(D)** 1  < m < 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) −1  < m < 3**

**Detailed Solution:**

Equation $x^2-2 m x+m^2-1=0$
$$
\begin{aligned}
& (x-m)^2-1=0 \\
& (x-m+1)(x-m-1)=0 \\
& x=m-1, m+1 \\
& -2 < m-1 \text { and } m+1 < 4
\end{aligned}
$$
$m>-1$ and $m < 3$
$-1 < m < 3$

</details>

---

### Q14. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

If both the roots of the quadratic equation $x^2-2 k x+k^2+k-5=0$ are less than 5 , then $\mathrm{k}$ lies in the interval

**Options:**

- **(A)** $(5,6]$
- **(B)** $(6, \infty)$
- **(C)** $(-\infty, 4)$
- **(D)** $[4,5]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(-\infty, 4)$**

**Detailed Solution:**

$$
\begin{aligned}
& \frac{-b}{2 a} < 5 \\
& f(5)>0 \\
& \Rightarrow k \in(-\infty, 4) .
\end{aligned}
$$

</details>

---

### Q15. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

If $2 a+3 b+6 c=0(a, b, c \in R)$ then the quadratic equation $a x^2+b x+c=0$ has

**Options:**

- **(A)** at least one root in [0, 1]
- **(B)** at least one root in [2, 3]
- **(C)** at least one root in [4, 5]
- **(D)** none of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) at least one root in [0, 1]**

**Detailed Solution:**

Let $f(x)=\frac{a x^3}{3}+\frac{b x^2}{2}+c x \Rightarrow f(0)=0$ and $f(1)=\frac{a}{3}+\frac{b}{2}+c=\frac{2 a+3 b+6 c}{6}=0$
Also $f(x)$ is continuous and differentiable in $[0,1]$ and $\left[0,1]\right.$. So by Rolle's theorem, $f^{\prime}(x)=0$. i.e. $a x^2+b x+c=0$ has at least one root in $[0,1]$

</details>

---

