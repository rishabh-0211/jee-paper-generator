# JEE Advanced Mathematics - Differential Equations

## Topic 4: Linear Differential Equation

**Total Questions:** 12

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Let $y = f(x)$ be the real valued function defined on the interval $(0, \infty)$, satisfying $y(1) = 0$ and the differential equation
$x\dfrac{dy}{dx} = y - x^3$.
Then which of the following statements is (are) TRUE ?

**Options:**

- **(A)** The function $f$ has a local minimum at $x = \dfrac{1}{\sqrt{3}}$
- **(B)** The function $f$ has a local maximum at $x = \dfrac{1}{\sqrt{3}}$
- **(C)** The function $f$ is increasing in the interval $(1, 2)$
- **(D)** If $g(x) = 4x^3 - 5x^2 + \dfrac{3}{2}x$ for $x > 0$, then the number of elements in the set $\{x \in (0, \infty) : f(x) = g(x)\}$ is $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) If $g(x) = 4x^3 - 5x^2 + \dfrac{3}{2}x$ for $x > 0$, then the number of elements in the set $\{x \in (0, \infty) : f(x) = g(x)\}$ is $2$**

**Detailed Solution:**

The given differential equation is $x\dfrac{dy}{dx} = y - x^3$.

Dividing by $x$, we get:
$\dfrac{dy}{dx} - \dfrac{1}{x}y = -x^2$

This is a linear differential equation of the form $\dfrac{dy}{dx} + P(x)y = Q(x)$, where $P(x) = -\dfrac{1}{x}$ and $Q(x) = -x^2$.

Integrating Factor (IF) = $e^{\int -\dfrac{1}{x} dx} = e^{-\ln x} = \dfrac{1}{x}$.

Multiplying the differential equation by the IF:
$\dfrac{d}{dx} \left( y \cdot \dfrac{1}{x} \right) = -x$

Integrating both sides with respect to $x$:
$\dfrac{y}{x} = -\dfrac{x^2}{2} + C$
$y = -\dfrac{x^3}{2} + Cx$

Given $y(1) = 0$:
$0 = -\dfrac{1}{2} + C \Rightarrow C = \dfrac{1}{2}$

Thus, $f(x) = \dfrac{x}{2} - \dfrac{x^3}{2}$.

To find local extrema, we find $f'(x)$:
$f'(x) = \dfrac{1}{2} - \dfrac{3x^2}{2}$

Setting $f'(x) = 0$ gives $3x^2 = 1 \Rightarrow x = \dfrac{1}{\sqrt{3}}$ (since $x > 0$).

Now, $f''(x) = -3x$. At $x = \dfrac{1}{\sqrt{3}}$, $f''\left(\dfrac{1}{\sqrt{3}}\right) = -\sqrt{3} < 0$.
So, $f(x)$ has a local maximum at $x = \dfrac{1}{\sqrt{3}}$.

For $x \in (1, 2)$, $x^2 > 1$, so $f'(x) = \dfrac{1 - 3x^2}{2} < 0$. Thus, $f(x)$ is decreasing in $(1, 2)$.

For the intersection of $f(x)$ and $g(x)$:
$\dfrac{x}{2} - \dfrac{x^3}{2} = 4x^3 - 5x^2 + \dfrac{3}{2}x$
$x - x^3 = 8x^3 - 10x^2 + 3x$
$9x^3 - 10x^2 + 2x = 0$
$x(9x^2 - 10x + 2) = 0$

Since $x \in (0, \infty)$, $x \neq 0$. We solve $9x^2 - 10x + 2 = 0$.
Discriminant $\Delta = (-10)^2 - 4(9)(2) = 100 - 72 = 28 > 0$.
Sum of roots $= \dfrac{10}{9} > 0$ and Product of roots $= \dfrac{2}{9} > 0$.
Both roots are real and positive. Therefore, there are exactly $2$ elements in the set.

Answer: The function $f$ has a local maximum at $x = \dfrac{1}{\sqrt{3}}$; If $g(x) = 4x^3 - 5x^2 + \dfrac{3}{2}x$ for $x > 0$, then the number of elements in the set $\{x \in (0, \infty) : f(x) = g(x)\}$ is $2$

</details>

---

### Q2. JEE Advanced 2023 (Paper 2)

*Type:* `numerical` | *Level:* `2`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be a solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>x</mi><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>7</mn></math>. Then the maximum value of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>x</mi><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mfrac><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn></mrow></mfrac></mfenced><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn></mrow></mfenced></math></p><p>Which is a linear differential equation,</p><p>So, integrating factor,<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#160;I.F.</mtext><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mfenced close="|" open="|" separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>5</mn></mrow></mfenced></mfrac></math></p><p>Now solution of differential equation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8901;</mo><mfrac><mn>1</mn><mfenced close="|" open="|" separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>5</mn></mrow></mfenced></mfrac><mo>=</mo><mo>&#8747;</mo><mo>&#8722;</mo><mn>2</mn><mi>x</mi><mo>&#8901;</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>5</mn></mrow><mfenced close="|" open="|" separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>5</mn></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mfrac><mi>y</mi><mfenced close="|" open="|" separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>5</mn></mrow></mfenced></mfrac><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>5</mn></mrow><mfenced close="|" open="|" separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>5</mn></mrow></mfenced></mfrac><mfenced separators="|"><mrow><mo>&#8722;</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>Now using the given value, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>7</mn><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is even function</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><msqrt><mn>5</mn></msqrt><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mo>-</mo><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>15</mn></math></p><p>For increasing function <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></math>
If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><msqrt><mn>5</mn></msqrt><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mo>-</mo><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>15</mn></math>
For increasing function <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>16</mn><mi>x</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>4</mn><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> but <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><msqrt><mn>5</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mi>&#981;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is increasing over <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></math></p><p>Now plotting the graph we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/9a840e0c-bf90-4bda-a907-fbfa95f33dd1.png" style="width: 400px; height: 231px;" /></p><p>Hence, maximum value of the function is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mi>f</mi><mo>(</mo><mi>x</mi><msub><mo>)</mo><mo>max</mo></msub><mo>=</mo><mn>16</mn></math></p></blockquote>

</details>

---

### Q3. JEE Advanced 2023 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mo>[</mo><mn>1</mn><mo>.</mo><mo>&#8734;</mo><mo>)</mo><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be a differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math> denote the base of the natural logarithm. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>e</mi></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>4</mn><mo>+</mo><mi>e</mi></mrow><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><msup><mi>e</mi><mn>2</mn></msup></mrow><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow><mn>3</mn></mfrac></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><msup><mi>e</mi><mn>2</mn></msup></mrow><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></math></p><p>Now differentiating both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mn>3</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>x</mi><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#8722;</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mi>x</mi><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#8722;</mo><mn>2</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#8722;</mo><mfrac><mn>2</mn><mi>x</mi></mfrac><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi></math></p><p>Which is a linear differential equation,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8722;</mo><mfrac><mn>2</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></math></p><p>Now solution is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mi>y</mi><mfenced separators="|"><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><mo>&#8747;</mo><mi>x</mi><mo>&#215;</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>ln</mi><mo>&#8289;</mo><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>(</mo><mi>ln</mi><mo>&#8289;</mo><mi>x</mi><mo>+</mo><mi>C</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>(</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>C</mi><mo>)</mo></math></p><p>Now using given value, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>+</mo><mi>C</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mi>ln</mi><mi>x</mi><mo>+</mo><mi>C</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>e</mi></mfenced><mo>=</mo><msup><mi>e</mi><mn>2</mn></msup><mfenced><mrow><mi>ln</mi><mi>e</mi><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>e</mi></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn><msup><mi>e</mi><mn>2</mn></msup></mrow><mn>3</mn></mfrac></math></p></blockquote>

</details>

---

### Q4. JEE Advanced 2022 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>, let the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>12</mn><mi>y</mi><mo>=</mo><mi>cos</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mi>x</mi></mrow></mfenced><mo>,</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>.</mo></math> Then, which of the following statements is/are TRUE?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is an increasing function
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is a decreasing function
- **(C)** There exists a real number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> such that the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>&#946;</mi></math> intersects the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> at infinitely many points
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is a periodic function

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) There exists a real number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> such that the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>&#946;</mi></math> intersects the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> at infinitely many points**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>12</mn><mi>y</mi><mo>=</mo><mi>cos</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>12</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mn>12</mn><mi>x</mi></mrow></msup></math></p><p>Now solution of the differential equation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mn>12</mn><mi>x</mi></mrow></msup><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mn>12</mn><mi>x</mi></mrow></msup><mo>&#183;</mo><mi>cos</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>12</mn></mfrac></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mn>12</mn><mi>x</mi></mrow></msup><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mn>12</mn><mi>x</mi></mrow></msup><mrow><msup><mn>12</mn><mn>2</mn></msup><mo>+</mo><msup><mfenced><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></mfenced><mn>2</mn></msup></mrow></mfrac><mfenced close="]" open="["><mrow><mn>12</mn><mi>cos</mi><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>12</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>12</mn></mfrac></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>Now given curve is passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mo>-</mo><mfrac><mn>12</mn><mrow><msup><mn>12</mn><mn>2</mn></msup><mo>+</mo><msup><mfenced><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mi>&#955;</mi></mfrac><mfenced close="]" open="["><mrow><munder><munder><mrow><mn>12</mn><mi>cos</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>12</mn></mfrac></mfenced><mo>+</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>12</mn></mfrac></mfenced></mrow><mo>&#9183;</mo></munder><mrow><msub><mi>f</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced></mrow></munder><mo>-</mo><mn>12</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>12</mn><mi>x</mi></mrow></msup></mrow></mfenced></math></p><p>{Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mfrac><mn>1</mn><mrow><msup><mn>12</mn><mn>2</mn></msup><mo>+</mo><msup><mfenced><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></mfenced><mn>2</mn></msup></mrow></mfrac></math> }</p><p>Now on differentiating we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><msup><mi>&#955;</mi><mo>&#39;</mo></msup></mfrac><mfenced close="]" open="["><mrow><munder><munder><mrow><mo>-</mo><mi>&#960;</mi><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>12</mn></mfrac></mfenced><mo>+</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><msup><mn>12</mn><mn>2</mn></msup></mfrac><mi>cos</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>12</mn></mfrac></mfenced></mrow><mo>&#9183;</mo></munder><mrow><msub><mi>f</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced></mrow></munder><mo>+</mo><mn>12</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>12</mn><mi>x</mi></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>where</mtext><mo>&#160;</mo><msup><mi>&#955;</mi><mo>&#39;</mo></msup><mo>=</mo><mfrac><mn>12</mn><mrow><msup><mn>12</mn><mn>2</mn></msup><mo>+</mo><msup><mfenced><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></mfenced><mn>2</mn></msup></mrow></mfrac></mrow></mfenced></math></p><p>Now when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is large then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>12</mn><mi>x</mi></mrow></msup></math> tends to zero.</p><p>But <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced></math> varies in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>-</mo><msqrt><msup><mi>&#960;</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></mfenced><mn>4</mn></msup></msqrt><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><msqrt><msup><mi>&#960;</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></mfenced><mn>4</mn></msup></msqrt></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>by&#160;using&#160;</mtext><mo>-</mo><msqrt><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></msqrt><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msqrt><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></msqrt></mrow></mfenced></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math> is changing its sign.</p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is non monotonic for all real number.
Also when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is very large then again <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>12</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>12</mn><mi>x</mi></mrow></msup></math> is almost zero but <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced></math> is periodic, so there exist some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>&#946;</mi></math> intersect <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> at infinitely many points.</p></blockquote>

</details>

---

### Q5. JEE Advanced 2021 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

<p>For any real numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></msub><mfenced><mi>x</mi></mfenced><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>, be the solution of the differential equation</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>&#945;</mi><mi>y</mi><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mi>&#946;</mi><mi>x</mi></mrow></msup><mo>,</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><msub><mi>y</mi><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></msub><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mo>:</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi>R</mi></mrow></mfenced></math>. Then which of the following functions belong(s) to the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>?</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mfenced><mrow><mi>e</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mfenced><mrow><mi>e</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>e</mi><mi>x</mi></msup><mn>2</mn></mfrac><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>e</mi><mo>-</mo><mfrac><msup><mi>e</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>e</mi><mi>x</mi></msup><mn>2</mn></mfrac><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>e</mi><mo>+</mo><mfrac><msup><mi>e</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>e</mi><mi>x</mi></msup><mn>2</mn></mfrac><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>e</mi><mo>-</mo><mfrac><msup><mi>e</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></math>**

**Detailed Solution:**

\(\frac{d y}{d x}+a y=x e^{\beta x}\)
Integrating factor (I.F.) \(=\mathrm{e}^{\mathrm{adx}}=\mathrm{e}^{\mathrm{ax}}\)
So, the solution is \(y \cdot e^{a x}=\int x e^{\beta x} \cdot e^{a x} d x\)
\(\Rightarrow y e^{a x}=\int x e^{(\alpha+\beta) x} d x\)
If \(\alpha+\beta \neq 0\)
\(\Rightarrow y e^{a x}=x \frac{e^{(\alpha+\beta) x}}{(\alpha+\beta)}-\frac{e^{(\alpha+\beta) x}}{(\alpha+\beta)^2}+C\)
\(\Rightarrow y=\frac{x e^{\beta x}}{(\alpha+\beta)}-\frac{e^{\beta x}}{(\alpha+\beta)^2}+C e^{-a x}\)
\(\Rightarrow y=\frac{e^{\beta x}}{(\alpha+\beta)}\left(x-\frac{1}{a+\beta}\right)+C e^{-\alpha x}\)
Put \(\alpha=\beta=1\) in (1)
\(y=\frac{e^x}{2}\left(x-\frac{1}{2}\right)+C e^{-x}\)
\(y(1)=1\)
\(1=\frac{e}{2} \times \frac{1}{2}+\frac{C}{e} \Rightarrow c=e-\frac{e^2}{4}\)
So, \(y=\frac{e^x}{2}\left(x-\frac{1}{2}\right)+\left(e-\frac{e^2}{4}\right) e^{-x}\)
If \(\alpha+\beta=0 \& \alpha=1\)
\(\begin{aligned}
&\frac{d y}{d x}+y=x e^{-x} \\
&\text { I.F. }=e^x
\end{aligned}\)
Solution is \(y e^x=\int x d x\)
\(\Rightarrow y e^x=\frac{x^2}{2}+C\)
\(y=\frac{x^2}{2} e^{-x}+C e^{-x}\)
\(y(1)=1\)
\(1=\frac{1}{2 e}+\frac{C}{e} \Rightarrow C=e-\frac{1}{2}\)
\(y=\frac{x^2}{2} e^{-x}+\left(e-\frac{1}{2}\right) e^{-x}\)

</details>

---

### Q6. JEE Advanced 2018 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be a continuous function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mi>t</mi></mrow></msup><mi>f</mi><mfenced separators="|"><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#8734;</mi></mrow></mfenced><mo>.</mo></math> Then, which of the following statement(s) is (are) TRUE?

**Options:**

- **(A)** The curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math> pass through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math>
- **(B)** The curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math> passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** The area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}" separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mfenced open="[" close="]" separators="|"><mn>0,1</mn></mfenced><mo>&#215;</mo><mi>R</mi><mo>:</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfenced><mi>&#160;</mi><mi>i</mi><mi>s</mi><mfrac><mrow><mi>&#960;</mi><mo>-</mo><mn>2</mn></mrow><mn>4</mn></mfrac></math>
- **(D)** The area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}" separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mfenced open="[" close="]" separators="|"><mn>0,1</mn></mfenced><mo>&#215;</mo><mi>R</mi><mo>:</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfenced><mi>&#160;</mi><mi>i</mi><mi>s</mi><mfrac><mrow><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) The area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}" separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mfenced open="[" close="]" separators="|"><mn>0,1</mn></mfenced><mo>&#215;</mo><mi>R</mi><mo>:</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfenced><mi>&#160;</mi><mi>i</mi><mi>s</mi><mfrac><mrow><mi>&#960;</mi><mo>-</mo><mn>2</mn></mrow><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/fdf1cbac-2b99-435e-9eab-2e27046b36bb-image.png"/>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><msubsup><mo>∫</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mi>t</mi></mrow></msup><mi>f</mi><mfenced separators="|"><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi> </mi><mi> </mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><msubsup><mo>∫</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mi>f</mi><mfenced separators="|"><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math>

Differentiate w.r.t. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><msup><mi>e</mi><mrow><mo>+</mo><mi>x</mi></mrow></msup><msup><mi>f</mi><mi>′</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mrow><mo>-</mo><mi>e</mi></mrow><mrow><mo>-</mo><mi>x</mi></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mfenced separators="|"><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi> </mi><mo>-</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><msup><mi>f</mi><mi>′</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mo>+</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi> </mi><mi> </mi><msup><mi>f</mi><mi>′</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>-</mo><mn>2</mn><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></math>

Integrating factor <math><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>.</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mo>=</mo><mo>∫</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>∫</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>-</mo><mo>∫</mo><mfenced separators="|"><mrow><mfenced separators="|"><mn>2</mn></mfenced><mo>∫</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi> </mi><mfrac><mrow><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>-</mo><mi> </mi><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mn>2</mn></mfrac><mo>+</mo><mi>c</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mi>c</mi><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mi>c</mi><mo>=</mo><mn>1</mn><mo>⇒</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mi> </mi><mi> </mi><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mi>x</mi></math>

Area <math><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>π</mi><mo>-</mo><mn>2</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

</details>

---

### Q7. JEE Advanced 2017 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

If <math><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> is a differentiable function such that <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mn>2</mn><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> for all <math><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> and <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math> then

**Options:**

- **(A)** <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&gt;</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></msup><mi> </mi><mi>i</mi><mi>n</mi><mi> </mi><mo>(</mo><mn>0</mn><mo>,</mo><mi>∞</mi><mo>)</mo></math>
- **(B)** <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi> </mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">g</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi> </mi><mo>(</mo><mn>0</mn><mo>,</mo><mi>∞</mi><mo>)</mo></math>
- **(C)** <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi> </mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">g</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi> </mi><mo>(</mo><mn>0</mn><mo>,</mo><mi>∞</mi><mo>)</mo></math>
- **(D)** <math> <mrow>  <mi>f</mi><mi>&#x0020;</mi><mo>&#x0027;</mo><mrow><mo>(</mo>   <mi>x</mi>  <mo>)</mo></mrow><mo>&#x003C;</mo><msup>   <mi>e</mi>   <mrow>    <mn>2</mn><mi>x</mi>   </mrow>  </msup>  <mi>&#x00A0;</mi><mtext>in</mtext><mi>&#x00A0;</mi><mo stretchy='false'>(</mo><mn>0</mn><mo>,</mo><mi>&#x221E;</mi><mo stretchy='false'>)</mo> </mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi> </mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">g</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi> </mi><mo>(</mo><mn>0</mn><mo>,</mo><mi>∞</mi><mo>)</mo></math>**

**Detailed Solution:**

<p>Given that,</p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mn>2</mn><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>&#160;</mi><mo>&#8704;</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p><math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mn>0</mn><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mo>&#8704;</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p><math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mi>&#160;</mi><mfenced separators="|"><mrow><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>&#62;</mo><mn>0</mn><mi>&#160;</mi><mo>&#8704;</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p><math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mfrac><mrow><mi>d</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced separators="|"><mrow><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>&#62;</mo><mn>0</mn><mi>&#160;</mi><mo>&#8704;</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p>Let  <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math></p><p>Now,  <math><msup><mrow><mi>g</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mn>0</mn><mi>&#160;</mi><mo>&#8704;</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p><math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is strictly increasing <math><mo>&#8704;</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p>Also  <math><mi>g</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mi>g</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mo>.</mo><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mn>1</mn><mi>&#160;</mi><mo>&#8704;</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></msup><mi>&#160;</mi><mo>&#8704;</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced></math></p><p>As,  <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mn>2</mn><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>&#62;</mo><mn>2</mn><mo>&#8704;</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced></math></p><p><math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  is strictly increasing on <math><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced></math></p>

</details>

---

### Q8. JEE Advanced 2016 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be a differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mo>-</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow><mi>x</mi></mfrac><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#8734;</mo><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>&#8800;</mo><mn>1</mn></math>. Then,

**Options:**

- **(A)** <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder></mrow><mo>&#8289;</mo><mrow><msup> <mi>f</mi> <mo>&#8242;</mo> </msup><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mn>1</mn></math>
- **(B)** <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder></mrow><mo>&#8289;</mo><mrow><mi>x</mi><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mn>2</mn></math>
- **(C)** <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder></mrow><mo>&#8289;</mo><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><msup> <mi>f</mi> <mo>&#8242;</mo> </msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math>
- **(D)** <math><mfenced close="|" open="|" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>&#8804;</mo><mn>2</mn></math> for all <math><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder></mrow><mo>&#8289;</mo><mrow><msup> <mi>f</mi> <mo>&#8242;</mo> </msup><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Let <math><mi>y</mi><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>
<math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn></math> (linear first order differential equation)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mi mathvariant="normal">&#8747;</mi><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mi>x</mi></mfenced></mrow></msup><mo>=</mo><mi>x</mi></math>, (I.F.=Integrating factor)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>y</mi><mo>&#183;</mo><mi>x</mi><mo>=</mo><mn>2</mn><mo>&#8747;</mo><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>y</mi><mi>x</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><mi>c</mi><mi>x</mi></mfrac><mo>;</mo></math>
As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>&#8800;</mo><mn>1</mn><mo>&#160;</mo><mo>&#8658;</mo><mi>c</mi><mo>&#8800;</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mi>c</mi><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>,</mo><mi>&#160;</mi><mi>c</mi><mi>&#160;</mi><mo>&#8800;</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mo>&#8289;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mo>&#8289;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>c</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mo>&#8289;</mo><mi>x</mi><mi>f</mi><mfenced separators="|"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mo>&#8289;</mo><mi>x</mi><mfenced separators="|"><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mi>c</mi><mi>x</mi></mrow></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mo>&#8289;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>c</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mo>&#8289;</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>f</mi><mo mathvariant="italic">'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mo>&#8289;</mo><msup><mi>x</mi><mn>2</mn></msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mi>c</mi><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mo>&#8289;</mo><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>c</mi><mo>&#8800;</mo><mn>0</mn></math> as <math><mi>c</mi><mo>&#8800;</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><mi>c</mi><mi>x</mi></mfrac><mo>,</mo><mi>&#160;</mi><mi>c</mi><mo>&#8800;</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mo>&#8289;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi mathvariant="normal">&#8734;</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>function is not bounded in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>.</p>

</details>

---

### Q9. JEE Advanced 2015 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><mi mathvariant="normal">y</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo></math> be a solution of the differential equation <math><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup></mrow></mfenced><mi mathvariant="normal">&#160;</mi><msup><mrow><mi mathvariant="normal">y</mi></mrow><mrow><mi mathvariant="normal">&#8242;</mi></mrow></msup><mo>+</mo><mi mathvariant="normal">y</mi><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup><mo>=</mo><mn>1</mn><mo>.</mo></math> If <math><mi mathvariant="normal">y</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>2</mn></math> , then which of the following statements is (are) true?

**Options:**

- **(A)** <math><mi mathvariant="normal">y</mi><mfenced separators="|"><mrow><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>
- **(B)** <math><mi mathvariant="normal">y</mi><mfenced separators="|"><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mi mathvariant="normal">y</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo></math>  has a critical point in the interval (-1, 0)
- **(D)** <math><mi mathvariant="normal">y</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo></math>  has no critical point in the interval (-1, 0)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi mathvariant="normal">y</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo></math>  has a critical point in the interval (-1, 0)**

**Detailed Solution:**

<math><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup></mrow></mfenced><mi mathvariant="normal">d</mi><mi mathvariant="normal">y</mi><mo>+</mo><mi mathvariant="normal">y</mi><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi><mo>=</mo><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></math> 
 <math><mi mathvariant="normal">d</mi><mi mathvariant="normal">y</mi><mo>+</mo><mi mathvariant="normal">d</mi><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup><mo>.</mo><mi mathvariant="normal">y</mi></mrow></mfenced><mo>=</mo><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></math> 
 <math><mi mathvariant="normal">y</mi><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup><mo>=</mo><mi mathvariant="normal">x</mi><mo>-</mo><mi mathvariant="normal">y</mi><mo>+</mo><mi mathvariant="normal">c</mi></math> 
Now,  <math><mi mathvariant="normal">x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi mathvariant="normal"> </mi><mi mathvariant="normal">y</mi><mo>=</mo><mn>2</mn></math> 
 <math><mn>2</mn><mo>.</mo><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mn>0</mn></mrow></msup><mo>=</mo><mn>0</mn><mo>-</mo><mn>2</mn><mo>+</mo><mi mathvariant="normal">c</mi></math> 
 <math><mo>⇒</mo><mi mathvariant="normal">c</mi><mo>=</mo><mn>4</mn></math> 
Now,  <math><mi mathvariant="normal">y</mi><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup><mo>=</mo><mi mathvariant="normal">x</mi><mo>-</mo><mi mathvariant="normal">y</mi><mo>+</mo><mn>4</mn></math> 
 <math><mi mathvariant="normal">y</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mn>4</mn></mrow><mrow><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math> 
Now,  <math><mfrac><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">y</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup></mrow><mrow><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math> 
 <math><mo>=</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup><mo>+</mo><mn>1</mn><mo>-</mo><mi mathvariant="normal">x</mi><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup><mo>-</mo><mn>4</mn><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup></mrow><mrow><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">x</mi><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup><mo>-</mo><mn>3</mn><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup></mrow><mrow><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math> 
 <math><msup><mrow><mi mathvariant="normal">f</mi></mrow><mrow><mi mathvariant="normal">&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mi mathvariant="normal">v</mi><mi mathvariant="normal">e</mi></math> 
 <math><msup><mrow><mi mathvariant="normal">f</mi></mrow><mrow><mi mathvariant="normal">&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">e</mi><mo>-</mo><mn>3</mn><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mrow><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mo>+</mo><mi mathvariant="normal">v</mi><mi mathvariant="normal">e</mi></math> 
Critical point in  <math><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mi mathvariant="normal"> </mi><mn>0</mn></mrow></mfenced></math>

</details>

---

### Q10. JEE Advanced 2014 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

The function <math><mi mathvariant="normal">y</mi><mo>=</mo><mi mathvariant="normal">f</mi><mfenced separators="|"><mrow><mi mathvariant="normal">x</mi></mrow></mfenced></math> is the solution of the differential equation <math><mfrac><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">y</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi mathvariant="normal">x</mi><mi mathvariant="normal">y</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><mn>2</mn><mi mathvariant="normal">x</mi></mrow><mrow><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></math> in (- 1 , 1) satisfying <math><mi mathvariant="normal">f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>.</mo></math> Then <math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mi mathvariant="normal">f</mi><mfenced separators="|"><mrow><mi mathvariant="normal">x</mi></mrow></mfenced><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow></mrow></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mi mathvariant="normal">π</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi mathvariant="normal">π</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>-</mo><mi mathvariant="normal"> </mi><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi mathvariant="normal">π</mi></mrow><mrow><mn>6</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi mathvariant="normal">π</mi></mrow><mrow><mn>6</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mi mathvariant="normal">π</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>-</mo><mi mathvariant="normal"> </mi><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>x</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mi>y</mi><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow><mrow><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></math>  
This is a linear differential equation
I.F.  <math><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mi> </mi><mi>d</mi><mi>x</mi></mrow></mrow></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi> </mi><mi>I</mi><mi>n</mi><mi> </mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi> </mi><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi>s</mi><mi>o</mi><mi>l</mi><mi>u</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi><mi> </mi><mi>i</mi><mi>s</mi></math>  
 <math><mi>y</mi><mi> </mi><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>=</mo><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mi>x</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></mrow></mrow><mi> </mi><mo>.</mo><mi> </mi><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mi> </mi><mi>d</mi><mi>x</mi></math>  
Or  <math><mi>y</mi><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>=</mo><mrow><mo stretchy="false">∫</mo><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi> </mi><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow><mrow><mn>5</mn></mrow></mfrac><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>c</mi></mrow></mrow></math> 
 <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mi> </mi><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi>c</mi><mo>=</mo><mn>0</mn></math>  
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi> </mi><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow><mrow><mn>5</mn></mrow></mfrac><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math>  
Now,  <math><mrow><munderover><mo stretchy="false">∫</mo><mrow><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo></mrow></mrow><mrow><munderover><mo stretchy="false">∫</mo><mrow><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac><mi> </mi><mi>d</mi><mi>x</mi></mrow></mrow></math>  (Using property)
 <math><mo>=</mo><mn>2</mn><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac><mi> </mi><mi>d</mi><mi>x</mi></mrow></mrow><mo>=</mo><mn>2</mn><mi> </mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow></mrow><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow></mrow></mfrac></mrow></mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi><mi>d</mi><mi>θ</mi></mrow></mrow><mi> </mi></math>  (Taking  <math><mi>x</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow></math> ) 
 <math><mo>=</mo><mn>2</mn><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></munderover><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>θ</mi><mi>d</mi><mi>θ</mi><mo>=</mo><mn>2</mn><msup><mrow><msub><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>θ</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mrow><mrow><mi mathvariant="italic">sin</mi><mn>2</mn></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></mrow></mrow></mrow></mrow><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced separators="|"><mrow><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>8</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>4</mn></mrow></mfrac></math>

</details>

---

### Q11. JEE Advanced 2011 (Paper 2)

*Type:* `numerical` | *Level:* `1`

Let $y^{\prime}(x)+y(x) g^{\prime}(x)=g(x) g^{\prime}(x) y(0)=0, x \in R$, where $f^{\prime}(x)$ denotes $\frac{d f(x)}{d x}$ and $g(x)$ is a given non-constant differentiable function on $R$ with $g(0)=g(2)=0$. Then, the value of $y$ (2) is...

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0**

**Detailed Solution:**

$\frac{d y}{d x}+y \cdot g^{\prime}(x)=g(x) g^{\prime}(x)$
$$
\mathrm{IF}=e^{\int g^{\prime}(x) d x}=e^{g(x)}
$$
$\therefore$ Solution is

$$
y\left(e^{g(x)}\right)=\int g(x) \cdot g^{\prime}(x) \cdot e^{g(x)} d x+C
$$
Put $g(x)=t, g^{\prime}(x) d x=d t$
$$
\begin{aligned}
& y\left(e^{g(x)}\right)=\int t \cdot e^t d t+C \\
= & t \cdot e^t-\int 1 \cdot e^t d t+C=t \cdot e^t-e^t+C \\
& y e^{g(x)}=(g(x)-1) e^{g(x)}+C \quad \ldots(\mathrm{i})
\end{aligned}
$$
Given, $y(0)=0, g(0)=g(2)=0$

$\therefore$ Eq. (i) becomes,
$$
\begin{aligned}
& \quad y(0) \cdot e^{g(0)}=(g(0)-1) \cdot e^{g(0)}+C \\
& \Rightarrow \quad 0=(-1) \cdot 1+C \Rightarrow C=1 \\
& \therefore \quad y(x) \cdot e^{g(x)}=(g(x)-1) e^{g(x)}+1 \\
& \Rightarrow \quad y(2) \cdot e^{g(2)}=(g(2)-1) e^{g(2)}+1 \\
& \text { where, } \quad g(2)=0 \\
& \Rightarrow \quad y(2) \cdot 1=(-1) \cdot 1+1 \Rightarrow y(2)=0
\end{aligned}
$$

</details>

---

### Q12. JEE Advanced 2010 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Let $f$ be a real-valued differentiable function on $R$ (the set of all real numbers) such that $f(1)=1$. If the $y$-intercept of the tangent at any point $P(x, y)$ on the curve $y=f(x)$ is equal to the cube of the abscissa of $P$, then the value of $f(-3)$ is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

The equation of the tangent at $(x, y)$ to the given curve $y=f(x)$ is
$$
\begin{gathered}
Y-y=\frac{d y}{d x}(X-x) \\
Y \text {-intercept }=y-x \frac{d y}{d x}
\end{gathered}
$$
According to the question
$$
x^3=y-x \frac{d y}{d x}
$$

$$
\Rightarrow \quad \frac{d y}{d x}-\frac{y}{x}=-x^2
$$
which is linear in $x$.
$$
\text { IF }=e^{\int \frac{-1}{x} d x}=\frac{1}{x}
$$
$\therefore$ Required solution is
$$
\begin{aligned}
& y \cdot \frac{1}{x}=\int-x^2 \cdot \frac{1}{x} d x \\
& \Rightarrow \quad \frac{y}{x}=\frac{-x^2}{2}+c \\
& \Rightarrow \quad y=\frac{-x^3}{2}+c x \\
& \text { At } x=1, y=1 \text {, } \\
& 1=\frac{-1}{2}+c \\
& \Rightarrow \quad c=\frac{3}{2} \\
&
\end{aligned}
$$
Now, $\begin{aligned} f(-3) & =\frac{27}{2}+\frac{3}{2}(-3) \\ & =\frac{27-9}{2}=9\end{aligned}$

</details>

---

