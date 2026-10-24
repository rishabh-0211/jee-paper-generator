# JEE Advanced Mathematics - Ellipse

## Topic 3: Tangent to ellipse

**Total Questions:** 7

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `numerical` | *Level:* `2`

<strong>Passage:</strong> Consider the ellipses given by $x^2 + 4y^2 = 1$ and $4x^2 + y^2 = 1$.

<strong>Question:</strong> Let $P$ be the point in the first quadrant where the given ellipses intersect. If $\theta$ is the acute angle between the tangents to the given ellipses at the point $P$, then the value of $4\tan\theta$ is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7.5**

**Detailed Solution:**

The given equations of the ellipses are $x^2 + 4y^2 = 1$ and $4x^2 + y^2 = 1$.

To find the point of intersection, we equate the two expressions:

$x^2 + 4y^2 = 4x^2 + y^2$

$3x^2 = 3y^2 \Rightarrow x = y$ (since $P$ lies in the first quadrant)

Substituting $x = y$ into the first ellipse equation:

$x^2 + 4x^2 = 1 \Rightarrow 5x^2 = 1 \Rightarrow x = \dfrac{1}{\sqrt{5}}$

Thus, the point of intersection is $P\left(\dfrac{1}{\sqrt{5}}, \dfrac{1}{\sqrt{5}}\right)$.

Differentiating $x^2 + 4y^2 = 1$ with respect to $x$ gives the slope of the tangent to the first ellipse:

$2x + 8y \dfrac{dy}{dx} = 0 \Rightarrow \dfrac{dy}{dx} = -\dfrac{x}{4y}$

At $P\left(\dfrac{1}{\sqrt{5}}, \dfrac{1}{\sqrt{5}}\right)$, the slope is $m_1 = -\dfrac{1}{4}$.

Differentiating $4x^2 + y^2 = 1$ with respect to $x$ gives the slope of the tangent to the second ellipse:

$8x + 2y \dfrac{dy}{dx} = 0 \Rightarrow \dfrac{dy}{dx} = -\dfrac{4x}{y}$

At $P\left(\dfrac{1}{\sqrt{5}}, \dfrac{1}{\sqrt{5}}\right)$, the slope is $m_2 = -4$.

The acute angle $\theta$ between the tangents is given by:

$\tan\theta = \left| \dfrac{m_1 - m_2}{1 + m_1 m_2} \right|$

$\tan\theta = \left| \dfrac{-\dfrac{1}{4} - (-4)}{1 + \left(-\dfrac{1}{4}\right)(-4)} \right| = \left| \dfrac{\dfrac{15}{4}}{2} \right| = \dfrac{15}{8}$

Therefore, the value of $4\tan\theta$ is:

$4\tan\theta = 4 \times \dfrac{15}{8} = \dfrac{15}{2} = 7.5$

Answer: $7.5$

</details>

---

### Q2. JEE Advanced 2024 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Consider the ellipse $\frac{x^2}{9}+\frac{y^2}{4}=1$. Let $S(p, q)$ be a point in the first quadrant such that $\frac{p^2}{9}+\frac{q^2}{4}>1$. Two tangents are drawn from $S$ to the ellipse, of which one meets the ellipse at one end point of the minor axis and the other meets the ellipse at a point $T$ in the fourth quadrant. Let $R$ be the vertex of the ellipse with positive $x$-coordinate and $O$ be the center of the ellipse. If the area of the triangle $\triangle O R T$ is $\frac{3}{2}$, then which of the following options is correct?

**Options:**

- **(A)** $q=2, p=3 \sqrt{3}$
- **(B)** $q=2, p=4 \sqrt{3}$
- **(C)** $q=1, p=5 \sqrt{3}$
- **(D)** $q=1, p=6 \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $q=2, p=3 \sqrt{3}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/oP0X7KDvFuLihZQG-kOpTM-UCss8zKkZuyPZ8LPOZSQ.original.fullsize.png">
$\operatorname{Ar}(\Delta \mathrm{ORT})=\frac{3}{2}$
$\left|\frac{1}{2} \times 3 \times 2 \sin \theta\right|=\frac{3}{2}$
$\sin \theta=\frac{1}{2} \Rightarrow \theta=\frac{11 \pi}{6}$ as point T is in third quadrant
$\mathrm{T}\left(\frac{3 \sqrt{3}}{2},-1\right)$
Tanget at $(0,2) \frac{x(0)}{9}+\frac{y(2)}{4}=1 \Rightarrow y=2...(1)$
Tangent at $\left(\frac{3 \sqrt{3}}{2},-1\right) \frac{x\left(\frac{3 \sqrt{3}}{2}\right)}{9}+\frac{y(-1)}{4}=1...(2)$
$\therefore$ By solving (1) & (2) $\Rightarrow \mathrm{p}=3 \sqrt{3}, \mathrm{q}=2$
$\Rightarrow$ Option (1) is Correct.

</details>

---

### Q3. JEE Advanced 2017 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Columns 1, 2 and 3 contain conics, equations of tangents to the conics and points of contact, respectively.<table border="1">	<tbody>		<tr>			<td>Column 1</td>			<td>Column 2</td>			<td>Column 3</td>		</tr>		<tr>			<td>(I) <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></math></td>			<td>(i) <math><mi>m</mi><mi>y</mi><mo>=</mo><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi><mo>+</mo><mi>a</mi></math></td>			<td>(P) <math><mfenced separators="|"><mrow><mfrac><mrow><mi>a</mi></mrow><mrow><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mi>a</mi></mrow><mrow><mi>m</mi></mrow></mfrac></mrow></mfenced></math></td>		</tr>		<tr>			<td>(II) <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></math></td>			<td>(ii) <math><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>+</mo><mi>a</mi><mi>&#160;</mi><msqrt><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt></math></td>			<td>(Q) <math><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><mi>m</mi><mi>a</mi></mrow><mrow><msqrt><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac><mo>,</mo><mfrac><mrow><mi>a</mi></mrow><mrow><msqrt><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac></mrow></mfenced></math></td>		</tr>		<tr>			<td>(III) <math><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn><mi>a</mi><mi>x</mi></math></td>			<td>(iii) <math><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>+</mo><mi>&#160;</mi><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></math></td>			<td>(R) <math><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>m</mi></mrow><mrow><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac></mrow></mfenced></math></td>		</tr>		<tr>			<td>(IV) <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></math></td>			<td>(iv) <math><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>+</mo><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt></math></td>			<td>(S) <math><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>m</mi></mrow><mrow><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac></mrow></mfenced></math></td>		</tr>	</tbody></table>The tangent to a suitable conic (Column 1) at <math><mfenced separators="|"><mrow><msqrt><mn>3</mn></msqrt><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> is found to be <math><msqrt><mn>3</mn></msqrt><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>4</mn></math> , then which of the following options is the only Correct combination?

**Options:**

- **(A)** (IV) (iii) (S)
- **(B)** (II) (iv) (R)
- **(C)** (IV) (iv) (S)
- **(D)** (II) (iii) (R)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) (II) (iv) (R)**

**Detailed Solution:**

<p><math><mi>P</mi><mfenced separators="|"><mrow><msqrt><mn>3</mn></msqrt><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>;</mo><mi>&#160;</mi></math> tangent <math><msqrt><mn>3</mn></msqrt><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><msqrt><mn>3</mn></msqrt></mfenced><mi>x</mi><mo>+</mo><mn>4</mn><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mi>y</mi><mo>=</mo><mn>4</mn></math>, comparing with (II)</p><p><math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>a</mi><mo>=</mo><mn>2</mn><mi>&#160;</mi></math></p><p><math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>+</mo><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt></math> is tangent for <math><mi>m</mi><mo>=</mo><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>  i.e. (ii)</p><p><math><mo>&#8756;</mo></math>    Point of contact for <math><mi>a</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#160;</mi><mi>m</mi><mo>=</mo><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math> is R</p>

</details>

---

### Q4. JEE Advanced 2017 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Columns 1, 2 and 3 contain conics, equations of tangents to the conics and points of contact, respectively.
 <table border="1">	<tbody>		<tr>			<td>Column 1</td>			<td>Column 2</td>			<td>Column 3</td>		</tr>		<tr>			<td>(I) <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></math></td>			<td>(i) <math><mi>m</mi><mi>y</mi><mo>=</mo><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi><mo>+</mo><mi>a</mi></math></td>			<td>(P) <math><mfenced separators="|"><mrow><mfrac><mrow><mi>a</mi></mrow><mrow><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mi>a</mi></mrow><mrow><mi>m</mi></mrow></mfrac></mrow></mfenced></math></td>		</tr>		<tr>			<td>(II) <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></math></td>			<td>(ii) <math><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>+</mo><mi>a</mi><mi>&#160;</mi><msqrt><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt></math></td>			<td>(Q) <math><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><mi>m</mi><mi>a</mi></mrow><mrow><msqrt><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac><mo>,</mo><mfrac><mrow><mi>a</mi></mrow><mrow><msqrt><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac></mrow></mfenced></math></td>		</tr>		<tr>			<td>(III) <math><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn><mi>a</mi><mi>x</mi></math></td>			<td>(iii) <math><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>+</mo><mi>&#160;</mi><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></math></td>			<td>(R) <math><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>m</mi></mrow><mrow><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac></mrow></mfenced></math></td>		</tr>		<tr>			<td>(IV) <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></math></td>			<td>(iv) <math><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>+</mo><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt></math></td>			<td>(S) <math><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>m</mi></mrow><mrow><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac></mrow></mfenced></math></td>		</tr>	</tbody></table>For <math><mi>a</mi><mo>=</mo><msqrt><mn>2</mn></msqrt></math> , if a tangent is drawn to a suitable conic (Column 1) at the point of contact <math><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math> , then which of the following options is the only Correct combination for obtaining its equation?

**Options:**

- **(A)** (II) (ii) (Q)
- **(B)** (III) (i) (P)
- **(C)** (I) (ii) (Q)
- **(D)** (I) (i) (P)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) (I) (ii) (Q)**

**Detailed Solution:**

<p>For <math><mi>a</mi><mo>=</mo><mi>&#160;</mi><msqrt><mn>2</mn></msqrt></math>  and point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>)</mo></math> only I of column-1 satisfies. Hence, equation of tangent is <math><mo>-</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>2</mn></math> or  <math><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>m</mi><mo>=</mo><mn>1</mn></math>  which matches with (ii) of column 2 and also with Q of column 3</p>

</details>

---

### Q5. JEE Advanced 2015 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> be two ellipse whose centers are at the origin. The major axes of <math><msub><mrow><mi>E</mi></mrow><mrow><mn>1</mn></mrow></msub><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><msub><mrow><mi>E</mi></mrow><mrow><mn>2</mn></mrow></msub></math> lie along the x - axis and the y - axis, respectively. Let S be the circle <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>2</mn><mo>.</mo></math> The straight line <math><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn></math> touches the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>,</mo><mo>&#160;</mo><msub><mi>E</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>,</mo><mo>&#160;</mo><mi>Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>,</mo></math> respectively. Suppose that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>=</mo><mi>P</mi><mi>R</mi><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac><mo>.</mo></math> If<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><msub><mi>e</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>e</mi><mn>2</mn></msub></math> are the eccentricities of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub><mo>,</mo></math>respectively, then the correct expression(s) is(are)

**Options:**

- **(A)** <math><msubsup><mrow><mi>e</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><mi> </mi><msubsup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mfrac><mrow><mn>43</mn></mrow><mrow><mn>40</mn></mrow></mfrac></math>
- **(B)** <math><msub><mrow><mi>e</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mi> </mi><mfrac><mrow><msqrt><mn>7</mn></msqrt></mrow><mrow><mn>2</mn><msqrt><mn>10</mn></msqrt></mrow></mfrac></math>
- **(C)** <math><mfenced close="|" open="|" separators="|"><mrow><msubsup><mrow><mi>e</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>-</mo><mi> </mi><msubsup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>
- **(D)** <math><msub><mrow><mi>e</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mi> </mi><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msub><mrow><mi>e</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mi> </mi><mfrac><mrow><msqrt><mn>7</mn></msqrt></mrow><mrow><mn>2</mn><msqrt><mn>10</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

Let Q be <math><mo>(</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>)</mo></math>
So equation tangent at Q will be
<math><mi>x</mi><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mi>y</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>
Comparing with <math><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn></math>
<math><mfenced separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced><mi>&#160;</mi><mo>&#8801;</mo><mo>(</mo><mn>1,2</mn><mo>)</mo></math>
So R and Q will be
<math><mfenced separators="|"><mrow><mn>1</mn><mi>&#160;</mi><mo>&#177;</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>3</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>&#177;</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>3</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mrow></mrow></mrow></mrow></mfenced></math>
<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>Q</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>&#160;</mi><mo>,</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mi>&#160;</mi><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>&#160;</mi><mo>,</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math>
Let Q lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mi>&#160;</mi></mrow><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mi>&#160;</mi><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math>
So tangent at P is
<math><mfrac><mrow><mn>5</mn><mi>x</mi></mrow><mrow><mn>3</mn><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mi>y</mi></mrow><mrow><mn>3</mn><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>1</mn></math>
Comparing with <math><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn></math>
<math><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>5</mn><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn><mi>&#160;</mi><mo>&#8658;</mo><msub><mrow><mi>e</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>5</mn></msqrt></mrow></mfrac></math>
And R lies on <math><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msubsup><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msubsup><mrow><mi>b</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac><mo>=</mo><mn>1</mn></math>
So tangent at <math><mfrac><mrow><mi>x</mi></mrow><mrow><msubsup><mrow><mn>3</mn><mi>a</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>8</mn><mi>y</mi></mrow><mrow><msubsup><mrow><mn>3</mn><mi>b</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac><mo>=</mo><mn>3</mn></math>
Comparing with <math><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn></math>
<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msubsup><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><msubsup><mrow><mi>b</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mn>8</mn><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><msub><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><msqrt><mfrac><mrow><mn>7</mn></mrow><mrow><mn>8</mn></mrow></mfrac></msqrt></math>
<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msubsup><mrow><mi>e</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mfrac><mrow><mn>43</mn></mrow><mrow><mn>40</mn></mrow></mfrac><mi>&#160;</mi><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><msub><mrow><mi>e</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><msqrt><mn>7</mn></msqrt></mrow><mrow><mn>2</mn><msqrt><mn>10</mn></msqrt></mrow></mfrac></math>

</details>

---

### Q6. JEE Advanced 2013 (Paper 1)

*Type:* `numerical` | *Level:* `3`

A vertical line passing through the point <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mtext>h</mtext> <mo>,</mo> <mtext>0</mtext> </mrow> </mfenced> </mrow> </math> intersects the ellipse <math> <mrow> <mfrac> <mrow> <msup> <mtext>x</mtext> <mn>2</mn> </msup> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mo>+</mo> <mfrac> <mrow> <msup> <mtext>y</mtext> <mn>2</mn> </msup> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> <mo>=</mo> <mn>1</mn> </mrow> </math> at the points <math> <mrow> <mtext>P</mtext> </mrow> </math> and <math> <mrow> <mtext>Q</mtext> </mrow> </math>. Let the tangents to the ellipse at <math> <mrow> <mtext>P</mtext> </mrow> </math> and <math> <mrow> <mtext>Q</mtext> </mrow> </math> meet at the point <math> <mrow> <mtext>R</mtext> </mrow> </math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#916;</mo><mo>(</mo><mi mathvariant="normal">h</mi><mo>)</mo><mo>=</mo></math> area of triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>PQR</mi><mo>,</mo><msub><mo>&#916;</mo><mn>1</mn></msub><mo>=</mo><munder><mi>max</mi><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8804;</mo><mi mathvariant="normal">h</mi><mo>&#8804;</mo><mn>1</mn></mrow></munder><mo>&#916;</mo><mfenced><mi mathvariant="normal">h</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><msub><mi mathvariant="normal">&#916;</mi><mn>2</mn></msub><mo>=</mo><munder><mi>min</mi><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8804;</mo><mi mathvariant="normal">h</mi><mo>&#8804;</mo><mn>1</mn></mrow></munder><mo>&#916;</mo><mo>(</mo><mi mathvariant="normal">h</mi><mo>)</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><msqrt><mn>5</mn></msqrt></mfrac><msub><mo>&#916;</mo><mn>1</mn></msub><mo>-</mo><mn>8</mn><msub><mo>&#916;</mo><mn>2</mn></msub><mo>=</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p>Point of intersection of tangents at P and Q is <math> <mrow> <mtext>R</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mtext>2 sec</mtext> <mi>θ</mi> <mo>,</mo> <mn>0</mn> </mrow> </mfenced> </mrow> </math>
Area of <math> <mrow> <mo>Δ</mo> <mtext>PQR</mtext> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>·</mo> <mn>2</mn> <msqrt> <mn>3</mn> </msqrt> <mo>sin</mo> <mi>θ</mi> <mo>·</mo> <mfenced close=")" open="(" separators=","> <mrow> <mtext>2 sec</mtext> <mi>θ</mi> <mo>-</mo> <mtext>2 cos </mtext> <mi>θ</mi> </mrow> </mfenced> </mrow> </math>
<math> <mrow> <mo>⇒</mo> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mo>Δ</mo> <mo>=</mo> <mn>2</mn> <msqrt> <mn>3</mn> </msqrt> <mo>·</mo> <mfrac> <mrow> <msup> <mtext>sin</mtext> <mn>3</mn> </msup> <mi>θ</mi> </mrow> <mrow> <mtext>cos </mtext> <mi>θ</mi> </mrow> </mfrac> </mrow> </math>; where <math> <mrow> <mtext>cos </mtext> <mi>θ</mi> <mo>∈</mo> <mfenced close="]" open="[" separators=","> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mtext>,</mtext> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/1df3a2e8-8393-419d-a335-f851dbae4e4a-82.PNG"/>
Now <math> <mrow> <mfrac> <mrow> <mtext>d</mtext> <mo>Δ</mo> </mrow> <mrow> <mtext>d</mtext> <mi>θ</mi> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>2</mn> <msqrt> <mn>3</mn> </msqrt> <mfenced close="|" open="|" separators=","> <mrow> <mtext>cos </mtext> <mi>θ</mi> <mo>·</mo> <msup> <mtext>3 sin</mtext> <mn>2</mn> </msup> <mi>θ</mi> <mtext>cos </mtext> <mi>θ</mi> <mo>-</mo> <msup> <mtext>sin</mtext> <mn>3</mn> </msup> <mi>θ</mi> <mfenced close=")" open="(" separators=","> <mrow> <mo>-</mo> <mtext>sin</mtext> <mi>θ</mi> </mrow> </mfenced> </mrow> </mfenced> </mrow> <mrow> <msup> <mtext>cos </mtext> <mn>2</mn> </msup> <mi>θ</mi> </mrow> </mfrac> <mo>></mo> <mn>0</mn> </mrow> </math>
As <math> <mrow> <mi>θ</mi> </mrow> </math> increases, <math> <mrow> <mo>Δ</mo> </mrow> </math> increases <math> <mrow> <mo>⇒</mo> </mrow> </math> when cos <math> <mrow> <mi>θ</mi> </mrow> </math> decreases, <math> <mrow> <mo>Δ</mo> </mrow> </math> increases
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mspace width="0.5em"></mspace><mspace width="0.5em"></mspace><msub><mo>Δ</mo><mtext>min</mtext></msub><mtext> occurs at cos</mtext><mi>θ</mi><mo>=</mo><mn>1</mn><mo>/</mo><mn>2</mn><mtext>,</mtext><mspace width="0.5em"></mspace><mtext>Therefore </mtext><msub><mo>Δ</mo><mn>2</mn></msub><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>·</mo><mfrac><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>1</mn><mo>/</mo><mn>4</mn></mrow></mfenced><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>·</mo><mfrac><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow><mn>8</mn></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mn>6</mn></mrow><mn>8</mn></mfrac></math>
<math> <mrow> <msub> <mo>Δ</mo> <mtext>max</mtext> </msub> <mtext> occurs at cos</mtext> <mi>θ</mi> <mo>=</mo> <mn>1</mn> <mo>/</mo> <mn>4</mn> <mtext>,</mtext> <mspace width="0.5em"></mspace> <mtext>Therefore </mtext> <mspace width="0.5em"></mspace> <msub> <mo>Δ</mo> <mn>1</mn> </msub> <mo>=</mo> <mn>2</mn> <msqrt> <mn>3</mn> </msqrt> <mo>·</mo> <mfrac> <mrow> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mo>-</mo> <mn>1</mn> <mo>/</mo> <mn>1</mn> <mn>6</mn> </mrow> </mfenced> </mrow> <mrow> <mn>3</mn> <mo>/</mo> <mn>2</mn> </mrow> </msup> </mrow> <mrow> <mn>1</mn> <mo>/</mo> <mn>4</mn> </mrow> </mfrac> <mo>=</mo> <mn>8</mn> <msqrt> <mn>3</mn> </msqrt> <mo>·</mo> <mfrac> <mrow> <mn>1</mn> <mn>5</mn> <mtext>.</mtext> <msqrt> <mn>1</mn> <mn>5</mn> </msqrt> </mrow> <mrow> <mtext>4.4.4</mtext> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>2</mn> <msqrt> <mn>3</mn> </msqrt> <mtext>.</mtext> <mn>1</mn> <mn>5</mn> <mtext>.</mtext> <msqrt> <mn>3</mn> </msqrt> <msqrt> <mn>5</mn> </msqrt> </mrow> <mrow> <mn>1</mn> <mn>6</mn> </mrow> </mfrac> </mrow> </math>
<math> <mrow> <mo>⇒</mo> <mspace width="0.5em"></mspace> <msub> <mo>Δ</mo> <mn>1</mn> </msub> <mo>=</mo> <mfrac> <mrow> <mn>4</mn> <mn>5</mn> </mrow> <mrow> <mn>8</mn> </mrow> </mfrac> <msqrt> <mn>5</mn> </msqrt> </mrow> </math>
Now <math> <mrow> <mfrac> <mrow> <mn>8</mn> </mrow> <mrow> <msqrt> <mn>5</mn> </msqrt> </mrow> </mfrac> <msub> <mo>Δ</mo> <mn>1</mn> </msub> <mo>-</mo> <mn>8</mn> <msub> <mo>Δ</mo> <mn>2</mn> </msub> <mo>=</mo> <mn>4</mn> <mn>5</mn> <mo>-</mo> <mn>3</mn> <mn>6</mn> <mo>=</mo> <mn>9</mn> </mrow> </math></p>

</details>

---

### Q7. JEE Advanced 2010 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
Tangents are drawn from the point $P(3,4)$ to the ellipse $\frac{x^2}{9}+\frac{y^2}{4}=1$ touching the ellipse at points $A$ and $B$.<strong>Question:</strong>
The coordinates of $A$ and $B$ are

**Options:**

- **(A)** $(3,0)$ and $(0,2)$
- **(B)** $\left(-\frac{8}{5}, \frac{2 \sqrt{161}}{15}\right)$ and $\left(-\frac{9}{5}, \frac{8}{5}\right)$
- **(C)** $\left(-\frac{8}{5}, \frac{2 \sqrt{161}}{15}\right)$ and $(0,2)$
- **(D)** $(3,0)$ and $\left(-\frac{9}{5}, \frac{8}{5}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(3,0)$ and $\left(-\frac{9}{5}, \frac{8}{5}\right)$**

**Detailed Solution:**

$$
\text { Figure is self explanatory }
$$

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/jDX6GkEhtNdY7zYO8pXOklILC_QwTFTGY_kNUs2S2r4.original.fullsize.png">

</details>

---

