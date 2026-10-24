# JEE Main Mathematics - Basic of Mathematics

## Topic 1: Logarithm

**Total Questions:** 9

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `numerical` | *Level:* `2`

The sum of squares of all the real solutions of the equation $\log_{(x+1)}(2x^2+5x+3) = 4 - \log_{(2x+3)}(x^2+2x+1)$ is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

For the logarithms to be defined, we must satisfy the following conditions:
1. Base of the first logarithm: $x+1 > 0 \Rightarrow x > -1$ and $x+1 \neq 1 \Rightarrow x \neq 0$.
2. Base of the second logarithm: $2x+3 > 0 \Rightarrow x > -\dfrac{3}{2}$ and $2x+3 \neq 1 \Rightarrow x \neq -1$.
3. Arguments must be positive: $2x^2+5x+3 > 0$ and $x^2+2x+1 > 0$.
Taking the intersection of all these conditions, the domain of the equation is $x \in (-1, 0) \cup (0, \infty)$.

Now, factorizing the arguments of the logarithms:
$2x^2+5x+3 = (2x+3)(x+1)$
$x^2+2x+1 = (x+1)^2$

Substitute these into the given equation:
$\log_{(x+1)}((2x+3)(x+1)) = 4 - \log_{(2x+3)}((x+1)^2)$

Using the properties of logarithms:
$\log_{(x+1)}(2x+3) + \log_{(x+1)}(x+1) = 4 - 2\log_{(2x+3)}(x+1)$
$\log_{(x+1)}(2x+3) + 1 = 4 - \dfrac{2}{\log_{(x+1)}(2x+3)}$

Let $t = \log_{(x+1)}(2x+3)$. The equation becomes:
$t + 1 = 4 - \dfrac{2}{t}$
$t - 3 + \dfrac{2}{t} = 0$
$t^2 - 3t + 2 = 0$
$(t-1)(t-2) = 0$
$\Rightarrow t = 1$ or $t = 2$

Case 1: $t = 1$
$\log_{(x+1)}(2x+3) = 1$
$2x+3 = x+1$
$x = -2$
This value is rejected because $x = -2$ does not fall in the domain $x > -1$.

Case 2: $t = 2$
$\log_{(x+1)}(2x+3) = 2$
$2x+3 = (x+1)^2$
$2x+3 = x^2+2x+1$
$x^2 = 2$
$x = \pm\sqrt{2}$

Since $x > -1$, $x = -\sqrt{2}$ is rejected. The only valid solution is $x = \sqrt{2}$.

The sum of squares of all the real solutions is $(\sqrt{2})^2 = 2$.

Answer: $2$

</details>

---

### Q2. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The product of all solutions of the equation $\mathrm{e}^{5\left(\log _{\mathrm{e}} x\right)^2+3}=x^8, x\gt0$, is :

**Options:**

- **(A)** $e^{8 / 5}$
- **(B)** $e^{6 / 5}$
- **(C)** $\mathrm{e}^2$
- **(D)** e

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $e^{8 / 5}$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{e}^{5(\ln x)^2+3}=\mathrm{x}^8 \\ & \Rightarrow \ell \mathrm{ne}^{5(\ln x)^2+3}=\ell \mathrm{nn}^8 \\ & \Rightarrow 5(\ln \mathrm{x})^2+3=8 \ell \mathrm{nx} \\ & (\ell \mathrm{nx}=\mathrm{t}) \\ & \Rightarrow 5 \mathrm{t}^2-8 \mathrm{t}+3=0 \\ & \quad \mathrm{t}_1+\mathrm{t}_2=\frac{8}{5} \\ & \quad \ln \mathrm{x}_1 \mathrm{x}_2=\frac{8}{5} \\ & \mathrm{x}_1 \mathrm{X}_2=\mathrm{e}^{8 / 5}\end{aligned}$

</details>

---

### Q3. JEE Main 2023 (10 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></math> be the three distinct positive real numbers such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><mi>a</mi></mrow></mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>a</mi></mrow></msup><mo>=</mo><msup><mfenced><mrow><mi>b</mi><mi>c</mi></mrow></mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></msup><mo>=</mo><msup><mi>a</mi><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>c</mi></mrow></msup></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>a</mi><mo>+</mo><mn>5</mn><mi>b</mi><mi>c</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<blockquote><p>Given equation: <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><mi>a</mi></mrow></mfenced><mrow><mi>ln</mi><mfenced><mi>a</mi></mfenced></mrow></msup><mo>=</mo><msup><mfenced><mrow><mi>b</mi><mi>c</mi></mrow></mfenced><mrow><mi>ln</mi><mfenced><mi>b</mi></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced><mi>a</mi></mfenced><mo>&#183;</mo><mfenced><mrow><mi>ln</mi><mfenced><mrow><mn>2</mn><mi>a</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>ln</mi><mfenced><mi>b</mi></mfenced><mo>&#183;</mo><mi>ln</mi><mfenced><mrow><mi>b</mi><mi>c</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced><mi>a</mi></mfenced><mo>&#183;</mo><mfenced><mrow><mi>ln</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>ln</mi><mfenced><mi>a</mi></mfenced></mrow></mfenced><mo>=</mo><mi>ln</mi><mfenced><mi>b</mi></mfenced><mo>&#183;</mo><mfenced><mrow><mi>ln</mi><mfenced><mi>b</mi></mfenced><mo>+</mo><mi>ln</mi><mfenced><mi>c</mi></mfenced></mrow></mfenced></math></p><p>let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced><mi>a</mi></mfenced><mo>=</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>ln</mi><mfenced><mi>b</mi></mfenced><mo>=</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>ln</mi><mfenced><mi>c</mi></mfenced><mo>=</mo><mi>z</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mi>y</mi><mo>&#8800;</mo><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfenced><mrow><mi>ln</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>y</mi><mfenced><mrow><mi>y</mi><mo>+</mo><mi>z</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>ln</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>y</mi><mi>z</mi></math> ........(i)</p><p>Similarly, from second equation</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced><mn>2</mn></mfenced><mo>&#183;</mo><mi>ln</mi><mfenced><mi>b</mi></mfenced><mo>=</mo><mi>ln</mi><mfenced><mi>c</mi></mfenced><mo>&#183;</mo><mi>ln</mi><mfenced><mi>a</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mi>z</mi></mrow><mi>y</mi></mfrac></math> ......(ii)</p><p>Substitute <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mi>q</mi><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>&#160;</mo><mtext>in</mtext><mo>&#160;</mo><mi>e</mi><mi>q</mi><mfenced><mi>i</mi></mfenced></math>,</p><p>We get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>3</mn></msup><mo>-</mo><mi>y</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mi>z</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mfenced><mrow><mi>y</mi><mo>+</mo><mi>z</mi></mrow></mfenced><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mi>y</mi><mo>+</mo><mi>z</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mi>y</mi><mo>+</mo><mi>z</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mfenced><mrow><mi>y</mi><mo>+</mo><mi>z</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mi>y</mi><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mfenced><mrow><mi>y</mi><mo>+</mo><mi>z</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mi>z</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>x</mi><mo>=</mo><mi>z</mi></math></p><p>But <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mi>z</mi></mrow><mi>y</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mo>-</mo><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mo>-</mo><mi>ln</mi><mfenced><mi>a</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mi>ln</mi><mo>&#160;</mo><mn>2</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced><mi>b</mi></mfenced><mo>=</mo><mo>-</mo><mi>ln</mi><mfenced><mi>c</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>a</mi><mo>+</mo><mn>5</mn><mi>b</mi><mi>c</mi><mo>=</mo><mn>6</mn><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>+</mo><mn>5</mn><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>8</mn></math></p><p>Hence this is the required answer.</p></blockquote>

</details>

---

### Q4. JEE Main 2023 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the solution of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mrow><mi>cos</mi><mi>x</mi></mrow></msub><mfenced><mrow><mi>cot</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mn>4</mn><msub><mi>log</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msub><mfenced><mrow><mi>tan</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>&#945;</mi><mo>+</mo><msqrt><mi>&#946;</mi></msqrt></mrow><mn>2</mn></mfrac></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math> are integers, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mrow><mi>cos</mi><mi>x</mi></mrow></msub><mfenced><mrow><mi>cot</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mn>4</mn><msub><mi>log</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msub><mfenced><mrow><mi>tan</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>lncos</mi><mi>x</mi><mo>-</mo><mi>lnsin</mi><mi>x</mi></mrow><mrow><mi>lncos</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>4</mn><mfenced><mfrac><mrow><mi>lnsin</mi><mi>x</mi><mo>-</mo><mi>lncos</mi><mi>x</mi></mrow><mrow><mi>lnsin</mi><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mfenced><mfrac><mrow><mi>lnsin</mi><mi>x</mi></mrow><mrow><mi>lncos</mi><mi>x</mi></mrow></mfrac></mfenced><mo>+</mo><mn>4</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mi>lncos</mi><mi>x</mi></mrow><mrow><mi>lnsin</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mfrac><mrow><mi>lnsin</mi><mi>x</mi></mrow><mrow><mi>lncos</mi><mi>x</mi></mrow></mfrac></mfenced><mo>+</mo><mn>4</mn><mfenced><mfrac><mrow><mi>lncos</mi><mi>x</mi></mrow><mrow><mi>lnsin</mi><mi>x</mi></mrow></mfrac></mfenced><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>lnsin</mi><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>(</mo><mi>lnsin</mi><mi>x</mi><mo>)</mo><mo>(</mo><mi>lncos</mi><mi>x</mi><mo>)</mo><mo>+</mo><mn>4</mn><mo>(</mo><mi>lncos</mi><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>lnsin</mi><mi>x</mi><mo>-</mo><mn>2</mn><mi>lncos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>lnsin</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>lncos</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>lnsin</mi><mi>x</mi><mo>=</mo><msup><mi>lncos</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mi>sin</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mi>sin</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q5. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The sum of the roots of the equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfenced><mo>+</mo><mn>2</mn><msub><mi>log</mi><mn>4</mn></msub><mfenced><mrow><mn>10</mn><mo>-</mo><msup><mn>2</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> is :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>2</mn></msub><mn>14</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>2</mn></msub><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>2</mn></msub><mn>13</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>2</mn></msub><mn>11</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>2</mn></msub><mn>11</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfenced><mo>+</mo><mn>2</mn><msub><mi>log</mi><mn>4</mn></msub><mfenced><mrow><mn>10</mn><mo>-</mo><msup><mn>2</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfenced><mo>+</mo><mn>2</mn><msub><mi>log</mi><msup><mn>2</mn><mn>2</mn></msup></msub><mfenced><mfrac><mrow><mn>10</mn><mo>.</mo><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow><msup><mn>2</mn><mi>x</mi></msup></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfenced><mo>+</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mfrac><mrow><mn>10</mn><mo>.</mo><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow><msup><mn>2</mn><mi>x</mi></msup></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfenced><mo>+</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mn>10</mn><mo>.</mo><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><msub><mi>log</mi><mn>2</mn></msub><msup><mn>2</mn><mi>x</mi></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>-</mo><msub><mi>log</mi><mn>2</mn></msub><msup><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mn>10</mn><mo>.</mo><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>x</mi><msub><mi>log</mi><mn>2</mn></msub><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>-</mo><msub><mi>log</mi><mn>2</mn></msub><msup><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mn>10</mn><mo>.</mo><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>+</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced close="]" open="["><mfrac><mrow><mn>10</mn><mo>.</mo><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow><msup><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfenced><mn>2</mn></msup></mfrac></mfenced><mo>-</mo><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>+</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced close="]" open="["><mfrac><mrow><mn>10</mn><mo>.</mo><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow><msup><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfenced><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced close="]" open="["><mfrac><mrow><mn>10</mn><mo>.</mo><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow><msup><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfenced><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced close="]" open="["><mfrac><mrow><mn>10</mn><mo>.</mo><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow><mrow><mn>9</mn><mo>+</mo><msup><mfenced><msup><mn>2</mn><mi>x</mi></msup></mfenced><mn>2</mn></msup><mo>+</mo><mn>6</mn><mo>.</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfrac></mfenced><mo>=</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>10</mn><mo>.</mo><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow><mrow><mn>9</mn><mo>+</mo><msup><mfenced><msup><mn>2</mn><mi>x</mi></msup></mfenced><mn>2</mn></msup><mo>+</mo><mn>6</mn><mo>.</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><mn>10</mn><mo>.</mo><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>9</mn><mo>+</mo><msup><mfenced><msup><mn>2</mn><mi>x</mi></msup></mfenced><mn>2</mn></msup><mo>+</mo><mn>6</mn><mo>.</mo><msup><mn>2</mn><mi>x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><msup><mn>2</mn><mi>x</mi></msup></mfenced><mn>2</mn></msup><mo>-</mo><mn>14</mn><mo>.</mo><msup><mn>2</mn><mi>x</mi></msup><mo>+</mo><mn>11</mn><mo>=</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>x</mi></msup><mo>=</mo><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>14</mn><mi>y</mi><mo>+</mo><mn>11</mn><mo>=</mo><mn>0</mn></math></p><p>Let roots are <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>1</mn></msub><mo>=</mo><msup><mn>2</mn><msub><mi>x</mi><mn>1</mn></msub></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><msup><mn>2</mn><msub><mi>x</mi><mn>2</mn></msub></msup></math></p><p>Product of roots, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>1</mn></msub><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><msup><mn>2</mn><msub><mi>x</mi><mn>1</mn></msub></msup><mo>&#215;</mo><msup><mn>2</mn><msub><mi>x</mi><mn>2</mn></msub></msup><mo>=</mo><msup><mn>2</mn><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></msup><mo>=</mo><mn>11</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>log</mi><msup><mn>2</mn><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></msup><mo>=</mo><mi>log</mi><mn>11</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mi>log</mi><mn>2</mn><mo>=</mo><mi>log</mi><mn>11</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mi>log</mi><mn>11</mn></mrow><mrow><mi>log</mi><mn>2</mn></mrow></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><msub><mi>log</mi><mn>2</mn></msub><mn>11</mn></math></p>

</details>

---

### Q6. JEE Main 2021 (20 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

The number of solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></msub><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>+</mo><msub><mi>log</mi><mrow><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>)</mo></mrow></msub><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></msub><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>+</mo><msub><mi>log</mi><mrow><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>)</mo></mrow></msub><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msub><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><msub><mi>log</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msub><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msub><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>+</mo><msub><mi>log</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msub><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><msub><mi>log</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msub><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msub><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><msub><mi>log</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msub><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msub><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mn>2</mn><msub><mi>log</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msub><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msub><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mfrac><mn>2</mn><mrow><msub><mi>log</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msub><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mn>3</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></msub><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>)</mo><mo>=</mo><mi>t</mi></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>+</mo><mfrac><mn>2</mn><mi>t</mi></mfrac><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>t</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></math></p><p>Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></msub><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>)</mo><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></msub><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>)</mo><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>4</mn></math> (rejected) as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>2</mn></math> (rejected)</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p>Number of solution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>.</p>

</details>

---

### Q7. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>If for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo><msub><mi>log</mi><mn>10</mn></msub><mi>sin</mi><mi>x</mi><mo>+</mo><msub><mi>log</mi><mn>10</mn></msub><mi>cos</mi><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>10</mn></msub><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msub><mi>log</mi><mn>10</mn></msub><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mi>n</mi><mo>&#62;</mo><mn>0</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to : </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>10</mn></msub><mi>sin</mi><mi>x</mi><mo>+</mo><msub><mi>log</mi><mn>10</mn></msub><mi>cos</mi><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mn>10</mn></msub><mi>sin</mi><mi>x</mi><mo>.</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>x</mi><mo>.</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>10</mn></msub><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msub><mi>log</mi><mn>10</mn></msub><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>=</mo><msup><mn>10</mn><mfenced><mrow><msub><mi>log</mi><mn>10</mn></msub><msqrt><mi>n</mi></msqrt><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></msup><mo>=</mo><msup><mn>10</mn><mfenced><mrow><msub><mi>log</mi><mn>10</mn></msub><msqrt><mi>n</mi></msqrt><mo>-</mo><msub><mi>log</mi><mn>10</mn></msub><msqrt><mn>10</mn></msqrt></mrow></mfenced></msup><mo>=</mo><msqrt><mfrac><mi>n</mi><mn>10</mn></mfrac></msqrt></math></p><p>By squaring we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi><mo>=</mo><mfrac><mi>n</mi><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>.</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mfrac><mi>n</mi><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>=</mo><mfrac><mi>n</mi><mn>10</mn></mfrac><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>12</mn></math></p>

</details>

---

### Q8. JEE Main 2021 (26 Feb Shift 1)

*Type:* `numerical` | *Level:* `1`

The number of solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>4</mn></msub><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>4</mn></msub><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mn>2</mn></msub><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><mi>x</mi><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn><mo>-</mo><mn>6</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>10</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mn>5</mn></math></p><p>But <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mn>2</mn></math> because it is not satisfying the domain of given equation i.e <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#8594;</mo></math> its domain <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>3</mn></math> finally <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> No. of solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn></math>.</p>

</details>

---

### Q9. JEE Main 2020 (09 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of distinct solutions of the equation, <math><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msub></mrow><mo>&#8289;</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced><mo>=</mo></mrow></mrow><mn>2</mn><mo>-</mo><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msub></mrow><mo>&#8289;</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow></math> in the interval <math><mfenced close="]" open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi></mi><mn>2</mn><mi>&#960;</mi></mrow></mfenced><mo>,</mo></math> is ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<math><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msub></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced><mo>=</mo><mn>2</mn><mo>-</mo><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msub></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow></mrow></mrow></math>  
<math><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msub><mi></mi><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mi></mi></mrow></mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced><mo>=</mo><mn>2</mn></math>  
<math><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>  
<math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>x</mi><mo>=</mo><mo>±</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow></math>  
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/85fe5890-aa81-489d-be54-d09a1fae8d11.jpeg"> 
Number of solution <math><mo>=</mo><mn>8</mn></math> .

</details>

---

