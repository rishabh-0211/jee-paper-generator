# JEE Advanced Mathematics - Differential Equations

## Topic 2: Variable Separable Form

**Total Questions:** 10

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $y : (-\infty, \infty) \rightarrow (0, \infty)$ be the solution of the differential equation
$\dfrac{dy}{dx} = \dfrac{e^{5x} y^3 + y^3}{e^x + e^x y^4}$,
satisfying $y(0) = \dfrac{1}{\sqrt{2}}$. Then the value of $y(\log_e 2)$ is

**Options:**

- **(A)** $\sqrt{\dfrac{5 + \sqrt{35}}{2}}$
- **(B)** $\sqrt{\dfrac{7 + \sqrt{53}}{2}}$
- **(C)** $\dfrac{7 + \sqrt{53}}{2}$
- **(D)** $\dfrac{5 + \sqrt{35}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{\dfrac{7 + \sqrt{53}}{2}}$**

**Detailed Solution:**

The given differential equation is

$\dfrac{dy}{dx} = \dfrac{e^{5x} y^3 + y^3}{e^x + e^x y^4}$

Factoring the numerator and denominator, we get

$\dfrac{dy}{dx} = \dfrac{y^3 (e^{5x} + 1)}{e^x (1 + y^4)}$

Separating the variables $x$ and $y$, we obtain

$\dfrac{1 + y^4}{y^3} dy = \dfrac{e^{5x} + 1}{e^x} dx$

$\left( \dfrac{1}{y^3} + y \right) dy = (e^{4x} + e^{-x}) dx$

Integrating both sides yields

$\int \left( y^{-3} + y \right) dy = \int (e^{4x} + e^{-x}) dx$

$-\dfrac{1}{2y^2} + \dfrac{y^2}{2} = \dfrac{e^{4x}}{4} - e^{-x} + C$

Multiplying by $2$, we get

$y^2 - \dfrac{1}{y^2} = \dfrac{e^{4x}}{2} - 2e^{-x} + 2C$

Using the initial condition $y(0) = \dfrac{1}{\sqrt{2}}$, we substitute $x = 0$ and $y = \dfrac{1}{\sqrt{2}}$:

$\left(\dfrac{1}{\sqrt{2}}\right)^2 - \dfrac{1}{\left(\dfrac{1}{\sqrt{2}}\right)^2} = \dfrac{e^0}{2} - 2e^0 + 2C$

$\dfrac{1}{2} - 2 = \dfrac{1}{2} - 2 + 2C$

This gives $2C = 0$, so $C = 0$. The equation becomes

$y^2 - \dfrac{1}{y^2} = \dfrac{e^{4x}}{2} - 2e^{-x}$

To find $y(\log_e 2)$, we substitute $x = \log_e 2$ into the equation. We have $e^{4x} = e^{4 \log_e 2} = 16$ and $e^{-x} = e^{-\log_e 2} = \dfrac{1}{2}$.

$y^2 - \dfrac{1}{y^2} = \dfrac{16}{2} - 2\left(\dfrac{1}{2}\right)$

$y^2 - \dfrac{1}{y^2} = 8 - 1 = 7$

Let $y^2 = t$. Since $y \in (0, \infty)$, $t > 0$.

$t - \dfrac{1}{t} = 7$

$t^2 - 7t - 1 = 0$

Solving for $t$ using the quadratic formula gives

$t = \dfrac{7 \pm \sqrt{49 - 4(1)(-1)}}{2} = \dfrac{7 \pm \sqrt{53}}{2}$

Since $t = y^2 > 0$, we must choose the positive root:

$y^2 = \dfrac{7 + \sqrt{53}}{2}$

Taking the positive square root since $y > 0$, we get

$y = \sqrt{\dfrac{7 + \sqrt{53}}{2}}$

</details>

---

### Q2. JEE Advanced 2025 (Paper 1)

*Type:* `numerical` | *Level:* `3`

For all $x>0$, let $y_1(x), y_2(x)$, and $y_3(x)$ be the functions satisfying
$\begin{aligned} & \frac{d y_1}{d x}-(\sin x)^2 y_1=0, y_1(1)=5 \\ & \frac{d y_2}{d x}-(\cos x)^2 y_2=0, y_2(1)=\frac{1}{3} \\ & \frac{d y_3}{d x}-\left(\frac{2-x^3}{x^3}\right) y_3=0, y_3(1)=\frac{3}{5 e}\end{aligned}$
respectively. Then $\lim _{x \rightarrow 0^{+}} \frac{y_1(x) y_2(x) y_3(x)+2 x}{e^{3 x} \sin x}$ is equal to _____

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

$\begin{aligned} & \frac{d y_1}{y_1}+\frac{d y_2}{y_2}+\frac{d y_3}{y_3}=\left(\sin ^2 x+\cos ^2 x+\frac{2-x^3}{x^3}\right) d x \\ & \ln \left(y_1 y_2 y_3\right)=\frac{-1}{x^2}+C \\ & \ln \left(y_1(x) y_2(x) y_3(x)\right)=\frac{-1}{x^2}+C \\ & \ln \left(5 \cdot \frac{1}{3} \cdot \frac{3}{5 e}\right)=\frac{-1}{x^2}+C \\ & \therefore C=0\end{aligned}$
$\begin{aligned} & y_1(x) y_2(x) y_3(x)=e^{\frac{-1}{x^2}} \\ & \lim _{x \rightarrow 0} \frac{e^{\frac{-1}{x^2}}+2 x}{e^{3 x} \sin x} \\ & \lim _{x \rightarrow 0} \frac{1}{e^{3 x+\frac{1}{x^2}} \sin x}+\lim _{x \rightarrow 0} \frac{2 x}{e^{3 x} \sin x}\end{aligned}$
$\lim _{x \rightarrow 0} \frac{1}{e^{3 x} \cdot \frac{\sin x}{x} \cdot \frac{e^{\frac{1}{x^2}}}{\frac{1}{x}}}+2$
$=0+2 \quad\left\{\lim _{\mathrm{y} \rightarrow \infty} \frac{\mathrm{e}^{\mathrm{y}^2}}{\mathrm{y}}=\frac{\mathrm{e}^{\mathrm{y}^2} \cdot 2 \mathrm{y}}{1}=\infty\right\}$
$=2$

</details>

---

### Q3. JEE Advanced 2022 (Paper 2)

*Type:* `numerical` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>d</mi><mi>y</mi><mo>-</mo><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>y</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn></math>, and the slope of the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is never zero, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mi>y</mi><mfenced><msqrt><mn>2</mn></msqrt></mfenced></math> is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<blockquote><p>Given differential equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><mfrac><mn>1</mn><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>y</mi></mfrac></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p>Integrating both sides, we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>ln</mi><mfenced close="|" open="|"><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mi>y</mi></mfrac></mfenced><mo>=</mo><mi>ln</mi><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mi>y</mi></mfrac><mo>=</mo><mo>&#177;</mo><msup><mi>x</mi><mn>4</mn></msup></math> or, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>4</mn><mrow><mn>1</mn><mo>&#177;</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfrac></math></p><p>Considering <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>4</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mi>y</mi><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mo>=</mo><mn>10</mn><mfenced><mfrac><mn>4</mn><mrow><mn>1</mn><mo>+</mo><mn>4</mn></mrow></mfrac></mfenced><mo>=</mo><mn>8</mn></math></p></blockquote>

</details>

---

### Q4. JEE Advanced 2020 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> be a nonzero real number. Suppose <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="normal">&#8477;</mi><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> is a differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math>. If the derivative <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> satisfies the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi><mo>,</mo></math> then which of the following statements is/are TRUE?

**Options:**

- **(A)** If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is an increasing function
- **(B)** If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>&#60;</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is a decreasing function
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>&#8658;</mo><mfrac><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>l</mi><mi>n</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>x</mi><mi>b</mi></mfrac><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8756;</mo><mn>0</mn><mo>=</mo><mn>0</mn><mo>+</mo><mi>C</mi><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>l</mi><mi>n</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>x</mi><mi>b</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mfrac><mn>1</mn><mi>b</mi></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>x</mi><mi>b</mi></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mfrac><mn>1</mn><mi>b</mi></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>x</mi><mi>b</mi></mfrac></mrow></msup><mo>.</mo><mfrac><mn>1</mn><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>&#62;</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is increasing for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>.</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mfrac><mn>1</mn><mi>b</mi></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>x</mi><mi>b</mi></mfrac></mrow></msup><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>x</mi><mi>b</mi></mfrac></mrow></msup><mo>=</mo><msup><mi>e</mi><mn>0</mn></msup><mo>=</mo><mn>1</mn></math>.</p>

</details>

---

### Q5. JEE Advanced 2019 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

Let <math><mi mathvariant="normal">T</mi></math> denote a curve <math><mi mathvariant="normal">y</mi><mo>=</mo><mi mathvariant="normal">y</mi><mfenced separators="|"><mrow><mi mathvariant="normal">x</mi></mrow></mfenced></math> which is in the first quadrant and let the point <math><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi mathvariant="normal">&#160;</mi><mn>0</mn></mrow></mfenced></math> lie on it. Let the tangent to <math><mi mathvariant="normal">T</mi></math> at a point <math><mi mathvariant="normal">P</mi></math> intersect the y-axis at <math><msub><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub><mo>.</mo></math> If <math><mi mathvariant="normal">P</mi><msub><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub></math> has length <math><mn>1</mn></math> for each point <math><mi mathvariant="normal">P</mi></math> on <math><mi mathvariant="normal">T</mi><mo>,</mo></math> then which of the following is options is/are correct?

**Options:**

- **(A)** <math><mi mathvariant="normal">y</mi><mo>=</mo><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi mathvariant="normal">e</mi></mrow></msub><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow><mrow><mi mathvariant="normal">x</mi></mrow></mfrac></mrow></mfenced><mo>-</mo><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math>
- **(B)** <math><mi mathvariant="normal">x</mi><msup><mrow><mi mathvariant="normal">y</mi></mrow><mrow><mi mathvariant="normal">&prime;</mi></mrow></msup><mo>-</mo><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mi mathvariant="normal">y</mi><mo>=</mo><mo>-</mo><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi mathvariant="normal">e</mi></mrow></msub><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow><mrow><mi mathvariant="normal">x</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math>
- **(D)** <math><mi mathvariant="normal">x</mi><msup><mrow><mi mathvariant="normal">y</mi></mrow><mrow><mi mathvariant="normal">&prime;</mi></mrow></msup><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi mathvariant="normal">x</mi><msup><mrow><mi mathvariant="normal">y</mi></mrow><mrow><mi mathvariant="normal">&prime;</mi></mrow></msup><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/twlqmgfamhgrhtmxmvrheldzhoslkcoixnvdhxguujkkbruowq.png"/>
Let point <math><mi mathvariant="normal">P</mi></math> is <math><mo>(</mo><mi mathvariant="normal">h</mi><mo>,</mo><mi mathvariant="normal"> </mi><mi mathvariant="normal">k</mi><mo>)</mo></math>
Now, equation of tangent at <math><mi mathvariant="normal">P</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>y</mi><mo>-</mo><mi>k</mi><mo>)</mo><mo>=</mo><msub><mi>m</mi><mi>T</mi></msub><mi> </mi><mo>(</mo><mi>x</mi><mo>-</mo><mi> </mi><mi>h</mi><mo>)</mo></math> ...(i) ( <math><msub><mrow><mi>m</mi></mrow><mrow><mi>T</mi></mrow></msub><mo>=</mo></math> slope of tangent at <math><mi mathvariant="normal">P</mi></math> )
For <math><msub><mrow><mi>Y</mi></mrow><mrow><mi>P</mi></mrow></msub></math> , put <math><mi>x</mi><mo>=</mo><mn>0</mn></math> in.....(i)
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>Y</mi><mi>P</mi></msub><mi> </mi><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mi>k</mi><mo>-</mo><mi> </mi><mi>h</mi><msub><mi>m</mi><mi>T</mi></msub></mrow></mfenced></math>
Now, as given <math><mi>P</mi><msub><mrow><mi>Y</mi></mrow><mrow><mi>P</mi></mrow></msub><mo>=</mo><mn>1</mn></math>
<math><msqrt><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup><msubsup><mrow><mi>m</mi></mrow><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msubsup></msqrt><mo>=</mo><mn>1</mn></math>
<math><msqrt><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msubsup><mrow><mi>m</mi></mrow><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfenced></msqrt><mo>=</mo><mn>1</mn></math>
<math><mn>1</mn><mo>+</mo><msubsup><mrow><mi>m</mi></mrow><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
<math><msubsup><mrow><mi>m</mi></mrow><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mn>1</mn></math>
<math><msubsup><mrow><mi>m</mi></mrow><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
<math><msub><mrow><mi>m</mi></mrow><mrow><mi>T</mi></mrow></msub><mo>=</mo><mo>±</mo><mfrac><mrow><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow><mrow><mi>h</mi></mrow></mfrac></math>
Put <math><msub><mrow><mi>m</mi></mrow><mrow><mi>T</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mtext> </mtext><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mtext> </mtext><mi>h</mi><mo>=</mo><mi>x</mi></math>
<math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>±</mo><mfrac><mrow><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow><mrow><mi>x</mi></mrow></mfrac><mtext> </mtext></math> ...(i)
<math><mi>y</mi><mo>=</mo><mo>±</mo><mfenced separators="|"><mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfenced></math>
As the curve lies in <math><msup><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">t</mi></mrow></msup></math> quadrant y must be positive. Hence,
<math><mi>y</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>-</mo><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math>
Also from equation (i) only negative sign will give the correct equation of centre.
Hence,
<math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow><mrow><mi>x</mi></mrow></mfrac></math>
<math><mi>x</mi><msup><mrow><mi>y</mi></mrow><mrow><mi>′</mi></mrow></msup><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>=</mo><mn>0</mn></math>

</details>

---

### Q6. JEE Advanced 2018 (Paper 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="normal">&#8477;</mi><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be a differentiable function with <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>. If <math><mi>y</mi><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> satisfies the differential equation <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mn>5</mn><mi>y</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>5</mn><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math>, then the value of  <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>-</mo><mi>&#8734;</mi></mrow></munder><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.4**

**Detailed Solution:**

<math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>25</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn></math>
So  <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mn>25</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mi>d</mi><mi>x</mi></math>
Integrating  <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>25</mn></mrow></mfrac><mo>×</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><mo>×</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfrac><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mi>y</mi><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow><mrow><mi>y</mi><mo>+</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mi>x</mi><mo>+</mo><mi>c</mi></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mn>5</mn><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mrow><mn>5</mn><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mn>20</mn><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mfenced></math>
Now,  <math><mi>c</mi><mo>=</mo><mn>0</mn></math> as <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>
Hence, <math><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mn>5</mn><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mrow><mn>5</mn><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mfenced separators="|"><mrow><mn>20</mn><mi>x</mi></mrow></mfenced></mrow></msup></math>
<math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mo>-</mo><mi>∞</mi></mrow></munder></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mn>5</mn><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mi> </mi></mrow><mrow><mn>5</mn><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mi> </mi><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mo>-</mo><mi>∞</mi></mrow></munder></mrow><mo>⁡</mo><mrow><msup><mrow><mi>e</mi></mrow><mrow><mfenced separators="|"><mrow><mn>20</mn><mi>x</mi></mrow></mfenced></mrow></msup></mrow></mrow></math>
Now,  
<math > <mrow>  <mi>R</mi><mi>H</mi><mi>S</mi><mo>=</mo><mn>0</mn><mo>&#x21D2;</mo><munder>   <mrow>    <mi>lim</mi></mrow>   <mrow>    <mi>x</mi><mo>&#x2192;</mo><mo>&#x2212;</mo><mi>&#x221E;</mi></mrow>  </munder>  <mrow><mo>(</mo>   <mrow>    <mn>5</mn><mi>f</mi><mrow><mo>(</mo>     <mi>x</mi>    <mo>)</mo></mrow><mo>&#x2212;</mo><mn>2</mn></mrow>  <mo>)</mo></mrow><mo>=</mo><mn>0</mn></mrow></math>
<math><mo>⇒</mo><math> <mrow>  <munder>   <mrow>    <mi>lim</mi></mrow>   <mrow>    <mi>x</mi><mo>&#x2192;</mo><mo>&#x2212;</mo><mi>&#x221E;</mi></mrow>  </munder>  <mi>f</mi><mrow><mo>(</mo>   <mi>x</mi>  <mo>)</mo></mrow><mo>=</mo><mfrac>   <mn>2</mn>   <mn>5</mn>  </mfrac>  </mrow></math>

</details>

---

### Q7. JEE Advanced 2017 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced separators="|"><mi>x</mi></mfenced></math> satisfies the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msqrt><mi>x</mi></msqrt><mfenced separators="|"><msqrt><mn>9</mn><mo>+</mo><msqrt><mi>x</mi></msqrt></msqrt></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><msup><mfenced separators="|"><msqrt><mn>4</mn><mo>+</mo><msqrt><mn>9</mn><mo>+</mo><msqrt><mi>x</mi></msqrt></msqrt></msqrt></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>d</mi><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>y</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><msqrt><mn>7</mn></msqrt><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mn>256</mn></mfenced><mo>=</mo></math>

**Options:**

- **(A)** <math><mn>80</mn></math>
- **(B)** <math><mn>3</mn></math>
- **(C)** <math><mn>16</mn></math>
- **(D)** <math><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>3</mn></math>**

**Detailed Solution:**

<p><math><mi>y</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac><mi>&#160;</mi><mrow><mo stretchy="false">&#8747;</mo><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msqrt><mn>4</mn><mo>+</mo><msqrt><mn>9</mn><mo>+</mo><msqrt><mi>x</mi></msqrt></msqrt><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><msqrt><mi>x</mi></msqrt><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><msqrt><mn>9</mn><mo>+</mo><msqrt><mi>x</mi></msqrt></msqrt></msqrt></mrow></mfrac></mrow></mrow></math></p><p>Put  <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>9</mn><mo>+</mo><msqrt><mi>x</mi></msqrt></msqrt><mo>=</mo><mi>t</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msqrt><mi>x</mi></msqrt><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><msqrt><mn>9</mn><mo>+</mo><msqrt><mi>x</mi></msqrt></msqrt></mrow></mfrac><mo>=</mo><mn>4</mn><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mi>y</mi><mo>=</mo><mfrac><mn>4</mn><mn>8</mn></mfrac><mi>&#160;</mi><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msqrt><mn>4</mn><mo>+</mo><mi>t</mi></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>&#160;</mi><msqrt><mn>4</mn><mo>+</mo><mi>t</mi></msqrt><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>&#160;</mi><msqrt><mn>4</mn><mo>+</mo><msqrt><mn>9</mn><mo>+</mo><msqrt><mi>x</mi></msqrt></msqrt></msqrt><mo>+</mo><mi>C</mi></math></p><p>At   <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>:</mo><mi>y</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mi>&#160;</mi><msqrt><mn>7</mn></msqrt><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mi>y</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>&#160;</mi><msqrt><mn>4</mn><mo>+</mo><msqrt><mn>9</mn><mo>+</mo><mi>&#160;</mi><msqrt><mi>x</mi></msqrt></msqrt></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced separators="|"><mn>256</mn></mfenced><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q8. JEE Advanced 2014 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced open="[" close="]" separators="|"><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be a function which is continuous on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> and is differentiable on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><msup><mi>x</mi><mn>2</mn></msup></munderover><mi>f</mi><mi mathvariant="normal">&#160;</mi><mfenced separators="|"><msqrt><mi>t</mi></msqrt></mfenced><mi>d</mi><mi>t</mi></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]" separators="|"><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>F</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced separators="|"><mn>2</mn></mfenced></math> equals

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math>
- **(B)** <math><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">e</mi><mo>-</mo><mn>1</mn></math>
- **(D)** <math><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mn>4</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>F</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>c</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup><mi>&#160;</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mo>&#8757;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><msup><mi>x</mi><mn>2</mn></msup></munderover><msup><mi>e</mi><mi>x</mi></msup><mi>&#160;</mi><mi>d</mi><mi>x</mi><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup><mo>-</mo><mn>1</mn><mi>&#160;</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mo>&#8757;</mo><mi>&#160;</mi><mi>F</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mi>F</mi><mfenced separators="|"><mn>2</mn></mfenced><mo>=</mo><msup><mi>e</mi><mn>4</mn></msup><mo>-</mo><mn>1</mn></math></p>

</details>

---

### Q9. JEE Advanced 2008 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Let a solution $y=y(x)$ of the differential equation $x \sqrt{x^2-1} d y-y \sqrt{y^2-1} d x=0$ satisfy $y(2)=\frac{2}{\sqrt{3}}$
Statement $1 y(x)=\sec \left(\sec ^{-1} x-\frac{\pi}{6}\right)$
Statement $2 y(x)$ is given by $\frac{1}{y}=\frac{2 \sqrt{3}}{x}-\sqrt{1-\frac{1}{x^2}}$

**Options:**

- **(A)** Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation for Statement 1.
- **(B)** Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation for Statement 1.
- **(C)** Statement 1 is true, Statement 2 is false.
- **(D)** Statement 1 is false, Statement 2 is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Statement 1 is true, Statement 2 is false.**

**Detailed Solution:**

$\because \frac{d y}{d x}=\frac{y \sqrt{y^2-1}}{x \sqrt{x^2-1}} \Rightarrow \int \frac{d y}{y \sqrt{y^2-1}}=\int \frac{d x}{x \sqrt{x^2-1}}$ $\Rightarrow \quad \sec ^{-1} y=\sec ^{-1} x+C$ At $\quad x=2, y=\frac{2}{\sqrt{3}}$ $$ \frac{\pi}{6}=\frac{\pi}{3}+C \Rightarrow C=-\frac{\pi}{6} $$
Now, $y=\sec \left(\sec ^{-1} x-\frac{\pi}{6}\right)$

$$
\begin{aligned}
& =\cos \left[\cos ^{-1} \frac{1}{x}-\cos ^{-1} \frac{\sqrt{3}}{2}\right] \\
& =\cos \left[\cos ^{-1}\left(\frac{\sqrt{3}}{2 x}+\sqrt{1-\frac{1}{x^2}} \sqrt{1-\frac{3}{4}}\right)\right] \\
\Rightarrow \quad \frac{1}{y} & =\frac{\sqrt{3}}{2 x}+\frac{1}{2} \sqrt{1-\frac{1}{x^2}} \\

</details>

---

### Q10. JEE Advanced 2007 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation $\frac{d y}{d x}=\frac{\sqrt{1-y^2}}{y}$ determines a family of circles with

**Options:**

- **(A)** variable radii and a fixed centre at $(0,1)$
- **(B)** variable radii and a fixed centre at $(0,-1)$
- **(C)** fixed radius 1 and variable centres along the $\mathrm{X}$-axis
- **(D)** fixed radius 1 and variable centres along the $\mathrm{Y}$-axis

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) fixed radius 1 and variable centres along the $\mathrm{X}$-axis**

**Detailed Solution:**

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{\sqrt{1-y^2}}{y} \\
& \Rightarrow \quad \int \frac{y}{\sqrt{1-y^2}} d y=\int d x \\
& \Rightarrow \quad-\sqrt{1-y^2}=x+C \\
& \Rightarrow \quad(x+c)^2+y^2=1 \\
&
\end{aligned}
$$
Centre $(-C, 0)$ and radius $=1$.

</details>

---

