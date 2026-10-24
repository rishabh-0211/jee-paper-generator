# JEE Advanced Mathematics - Application of Derivatives

## Topic 1: Tangent Normal

**Total Questions:** 5

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $P$ be the point on the parabola $y = x^2$ such that the slope of the tangent to the parabola at the point $P$ is $4$. Let $Q$ be the point in the first quadrant lying on the circle $x^2 + y^2 = 2$ such that the slope of the tangent to the circle at the point $Q$ is $-1$. Let $R$ be the point in the first quadrant lying on the ellipse $x^2 + 4y^2 = 8$ such that the slope of the tangent to the ellipse at the point $R$ is $-\dfrac{1}{2}$.

Then the radius of the circle passing through the points $P, Q$ and $R$ is

**Options:**

- **(A)** $\sqrt{10}$
- **(B)** $\sqrt{5}$
- **(C)** $\sqrt{\dfrac{5}{2}}$
- **(D)** $2\sqrt{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{\dfrac{5}{2}}$**

**Detailed Solution:**

For the point $P$ on the parabola $y = x^2$, the slope of the tangent is $\dfrac{dy}{dx} = 2x$.
Given $2x = 4 \Rightarrow x = 2$.
Substituting $x = 2$ in $y = x^2$, we get $y = 4$.
Thus, the coordinates of $P$ are $(2, 4)$.

For the point $Q$ on the circle $x^2 + y^2 = 2$, differentiating with respect to $x$ gives $2x + 2y \dfrac{dy}{dx} = 0 \Rightarrow \dfrac{dy}{dx} = -\dfrac{x}{y}$.
Given $-\dfrac{x}{y} = -1 \Rightarrow x = y$.
Since $Q$ lies in the first quadrant, substituting $x = y$ in $x^2 + y^2 = 2$ gives $2x^2 = 2 \Rightarrow x = 1, y = 1$.
Thus, the coordinates of $Q$ are $(1, 1)$.

For the point $R$ on the ellipse $x^2 + 4y^2 = 8$, differentiating with respect to $x$ gives $2x + 8y \dfrac{dy}{dx} = 0 \Rightarrow \dfrac{dy}{dx} = -\dfrac{x}{4y}$.
Given $-\dfrac{x}{4y} = -\dfrac{1}{2} \Rightarrow x = 2y$.
Since $R$ lies in the first quadrant, substituting $x = 2y$ in $x^2 + 4y^2 = 8$ gives $4y^2 + 4y^2 = 8 \Rightarrow 8y^2 = 8 \Rightarrow y = 1, x = 2$.
Thus, the coordinates of $R$ are $(2, 1)$.

The points are $P(2, 4)$, $Q(1, 1)$, and $R(2, 1)$.
The line segment $PR$ lies on the vertical line $x = 2$, and the line segment $QR$ lies on the horizontal line $y = 1$.
Since $PR$ is perpendicular to $QR$, the angle $\angle PRQ = 90^{\circ}$.
Therefore, the triangle $PQR$ is a right-angled triangle with the hypotenuse $PQ$.
The circumcircle of $\triangle PQR$ has $PQ$ as its diameter.
The length of the diameter is $PQ = \sqrt{(2 - 1)^2 + (4 - 1)^2} = \sqrt{1^2 + 3^2} = \sqrt{10}$.
The radius of the circle is $\dfrac{PQ}{2} = \dfrac{\sqrt{10}}{2} = \sqrt{\dfrac{5}{2}}$.

Answer: $\sqrt{\dfrac{5}{2}}$

</details>

---

### Q2. JEE Advanced 2020 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></math> and <math> <mi>&#955;</mi> </math> be positive real numbers. Suppose <math> <mi>P</mi> </math> is an end point of the latus rectum of the parabola <math> <msup> <mi>y</mi> <mn>2</mn> </msup> <mo>=</mo><mn>4</mn><mi>&#955;</mi><mi>x</mi> </math>, and suppose the ellipse <math> <mrow> <mfrac> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> <mrow> <msup> <mi>a</mi> <mn>2</mn> </msup> </mrow> </mfrac> <mo>+</mo><mfrac> <mrow> <msup> <mi>y</mi> <mn>2</mn> </msup> </mrow> <mrow> <msup> <mi>b</mi> <mn>2</mn> </msup> </mrow> </mfrac> <mo>=</mo><mn>1</mn></mrow> </math> passes through the point <math> <mi>P</mi> </math>. If the tangents to the parabola and the ellipse at the point <math> <mi>P</mi> </math> are perpendicular to each other, then the eccentricity of the ellipse is

**Options:**

- **(A)** <math> <mrow> <mfrac> <mn>1</mn> <mrow> <msqrt> <mn>2</mn> </msqrt> </mrow> </mfrac> </mrow> </math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>5</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mrow> <mfrac> <mn>1</mn> <mrow> <msqrt> <mn>2</mn> </msqrt> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/88efa2a2-763a-4d21-a22e-d784b78cdc5f-image.png"/></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>λ</mi><mi>x</mi><mo>⇒</mo><msub><mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mi>P</mi></msub><mo>=</mo><mn>1</mn><mo>=</mo><msub><mi>m</mi><mn>1</mn></msub></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>⇒</mo><msub><mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mi>P</mi></msub><mo>=</mo><mfrac><mrow><mo>−</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><msub><mi>m</mi><mn>2</mn></msub></math></p><p>Given both tangents are perpendicular.</p><p><math> <mrow> <mo>⇒</mo><msub> <mi>m</mi> <mn>1</mn> </msub> <mo>⋅</mo><msub> <mi>m</mi> <mn>2</mn> </msub> <mo>=</mo><mo>−</mo><mn>1</mn><mo>⇒</mo><msup> <mi>b</mi> <mn>2</mn> </msup> <mo>=</mo><mn>2</mn><msup> <mi>a</mi> <mn>2</mn> </msup> </mrow> </math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><msup><mi>b</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mi>e</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math> <mrow> <mo>⇒</mo><mn>1</mn><mo>=</mo><mn>2</mn><mfenced> <mrow> <mn>1</mn><mo>−</mo><msup> <mi>e</mi> <mn>2</mn> </msup> </mrow> </mfenced></mrow> </math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>e</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p>

</details>

---

### Q3. JEE Advanced 2014 (Paper 1)

*Type:* `numerical` | *Level:* `2`

The slope of the tangent to the curve <math><msup><mrow><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mtext>x</mtext> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mo>+</mo> <msup> <mtext>x</mtext> <mn>2</mn> </msup> </mrow> </mfenced> </mrow> <mn>2</mn> </msup></math> at the point (1, 3) is ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<math><mn>2</mn><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfenced><mi> </mi><mfenced separators="|"><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>5</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfenced></math> 
 <math><mo>=</mo><mn>1</mn><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi> </mi><mfenced separators="|"><mrow><mn>2</mn><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mi> </mi><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mfenced></math> 
Now put  <math><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi> </mi><mi>y</mi><mo>=</mo><mn>3</mn></math>  and  <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>m</mi><mo>.</mo></math> 
 <math><mn>2</mn><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mi> </mi><mfenced separators="|"><mrow><mi>m</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mi> </mi><mfenced separators="|"><mrow><mn>4</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mi> </mi><mfenced separators="|"><mrow><mn>4</mn></mrow></mfenced><mi> </mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></math> 
 <math><mi>m</mi><mo>-</mo><mn>5</mn><mo>=</mo><mfrac><mrow><mn>12</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math> 
 <math><mi>m</mi><mo>=</mo><mn>5</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>8</mn></math> 
 <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>m</mi><mo>=</mo><mn>8</mn><mo>.</mo></math>

</details>

---

### Q4. JEE Advanced 2007 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

The tangent to the curve $y=e^x$ drawn at the point $\left(c, e^c\right)$ intersects the line joining the points $\left(c-1, e^{c-1}\right)$ and $\left(c+1, e^{c+1}\right)$

**Options:**

- **(A)** on the left of $x=c$
- **(B)** on the right of $x=c$
- **(C)** at no point
- **(D)** at all points

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) on the left of $x=c$**

**Detailed Solution:**

Slope of the line joining the points $\left(c-1, e^{c-1}\right)$ and $\left(c+1, e^{c+1}\right)$ is equal to $\frac{e^{c+1}-e^{c-1}}{2}>e^c$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/VGvkClDxV8F-gNTzbTW1cbZ_e9vEpZ4KBurvN0ItKJk.original.fullsize.png">

$$
\text { Tangent to the curve } y=e^x \text { will intersect the given line to the left of the line } x=c \text {. }
$$
ALITER
The equation of the tangent to the curve $y=e^x$ at $\left(c, e^c\right)$ is
$$
y-e^c=e^c(x-c)
$$
Equation of the line joining the given points is
$$
y-e^{c-1}=\frac{e^c\left(e-e^{-1}\right)}{2}[x-(c-1)]
$$
Eliminating $y$ from Eqs. (i) and (ii), we get
$$
\begin{aligned}
{[x-(c-1)]\left[2-\left(e-e^{-1}\right)\right] } & =2 e^{-1} \\
x-c & =\frac{e+e^{-1}-2}{2-\left(e-e^{-1}\right)} < 0 \Rightarrow x < c .
\end{aligned}
$$

</details>

---

### Q5. JEE Advanced 2006

*Type:* `multipleCorrect` | *Level:* `3`

Tangent is drawn at any point $P$ of a curve which passes through $(1,1)$ cutting $X$-axis and $Y$-axis at $A$ and $B$, respectively. If $A P: B P=3: 1$, then

**Options:**

- **(A)** differential equation of the curve is $3 x \frac{d y}{d x}+y=0$
- **(B)** differential equation of the curve is $3 x \frac{d y}{d x}-y=0$
- **(C)** curve is passing through $\left(\frac{1}{8}, 2\right)$
- **(D)** normal at $(1,1)$ is $x+3 y=4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) curve is passing through $\left(\frac{1}{8}, 2\right)$**

**Detailed Solution:**

Since, $\quad A P: B P=3: 1$
where, equation of tangent is $y-y_1=f^{\prime}(x)\left(x-x_1\right)$
$$
\begin{aligned}
\therefore & A\left(x_1-\frac{y_1}{f^{\prime}\left(x_1\right)}, 0\right) \text { and } B\left(0, y_1-x_1 f^{\prime}(x)\right) \\
& A P: B P=3: 1 \Rightarrow \frac{d y}{d x}=\frac{y}{-3 x} \\
\therefore \quad & 3 x \frac{d y}{d x}+y=0 \quad \text { or } \quad \frac{d y}{y}=-\frac{1}{3 x} d x,
\end{aligned}
$$
On integrating both sides, we get
$$
\begin{array}{lrlr}
\Rightarrow & x y^3 & =1 \\
& \therefore \text { At } & x & =\frac{1}{8} \quad \text { and } \quad y=2
\end{array}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/dhtulUI2EIb1uiFaZHVNmaiQS7PbvVRaxjWm9Q8Gdlo.original.fullsize.png">

</details>

---

