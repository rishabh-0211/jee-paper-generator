# JEE Advanced Mathematics - Three Dimensional Geometry

## Topic 3: Plane in Space

**Total Questions:** 18

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

Let $P$ be the plane such that it contains the straight line $\dfrac{x-1}{2} = \dfrac{y-3}{3} = \dfrac{z+2}{1}$ and is perpendicular to the plane $x + 2y + 3z = 4$. Let $P_1$ be the plane which passes through the point $(4, 2, 2)$ and is parallel to $P$.

Then which of the following statements is (are) TRUE?

**Options:**

- **(A)** The equation of the plane $P$ is $7x - 5y + z = -10$
- **(B)** The distance between the planes $P$ and $P_1$ is $30$
- **(C)** The distance of the plane $P$ from the origin is $2\sqrt{3}$
- **(D)** The acute angle between the plane $P$ and the plane $2x + 2y + z = 3$ is $\cos^{-1}\left(\dfrac{1}{3\sqrt{3}}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) The acute angle between the plane $P$ and the plane $2x + 2y + z = 3$ is $\cos^{-1}\left(\dfrac{1}{3\sqrt{3}}\right)$**

**Detailed Solution:**

Let the normal vector to the plane $P$ be $\vec{n}$.

Since the plane $P$ contains the line $\dfrac{x-1}{2} = \dfrac{y-3}{3} = \dfrac{z+2}{1}$, its normal vector $\vec{n}$ is perpendicular to the line's direction vector $\vec{b} = 2\hat{i} + 3\hat{j} + \hat{k}$.

Since $P$ is perpendicular to the plane $x + 2y + 3z = 4$, $\vec{n}$ is perpendicular to its normal vector $\vec{n}_1 = \hat{i} + 2\hat{j} + 3\hat{k}$.

$\vec{n} = (2\hat{i} + 3\hat{j} + \hat{k}) \times (\hat{i} + 2\hat{j} + 3\hat{k}) = \hat{i}(9-2) - \hat{j}(6-1) + \hat{k}(4-3) = 7\hat{i} - 5\hat{j} + \hat{k}$

Plane $P$ passes through the point $(1, 3, -2)$ which lies on the given line.

Equation of plane $P$ is $7(x-1) - 5(y-3) + 1(z+2) = 0 \Rightarrow 7x - 5y + z = -10$

Statement (1) is TRUE.

The plane $P_1$ is parallel to $P$ and passes through $(4, 2, 2)$.

Equation of plane $P_1$ is $7(x-4) - 5(y-2) + 1(z-2) = 0 \Rightarrow 7x - 5y + z = 20$

Distance between parallel planes $P$ and $P_1$ is $d = \dfrac{|20 - (-10)|}{\sqrt{7^2 + (-5)^2 + 1^2}} = \dfrac{30}{\sqrt{75}} = 2\sqrt{3}$. Statement (2) is FALSE.

Distance of plane $P$ from the origin is $d_0 = \dfrac{|-10|}{\sqrt{75}} = \dfrac{2}{\sqrt{3}}$. Statement (3) is FALSE.

Angle $\theta$ between the planes $7x - 5y + z + 10 = 0$ and $2x + 2y + z - 3 = 0$ is given by:

$\cos\theta = \dfrac{|7(2) + (-5)(2) + 1(1)|}{\sqrt{7^2+(-5)^2+1^2} \sqrt{2^2+2^2+1^2}} = \dfrac{5}{\sqrt{75} \sqrt{9}} = \dfrac{5}{15\sqrt{3}} = \dfrac{1}{3\sqrt{3}}$

$\theta = \cos^{-1}\left(\dfrac{1}{3\sqrt{3}}\right)$. Statement (4) is TRUE.

</details>

---

### Q2. JEE Advanced 2024 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let $\mathbb{R}^3$ denote the three-dimensional space. Take two points $P=(1,2,3)$ and $Q=(4,2,7)$. Let $\operatorname{dist}(X, Y)$ denote the distance between two points $X$ and $Y$ in $\mathbb{R}^3$. Let
$\begin{gathered}S=\left\{X \in \mathbb{R}^3:(\operatorname{dist}(X, P))^2-(\operatorname{dist}(X, Q))^2=50\right\} \text { and } \\T=\left\{Y \in \mathbb{R}^3:(\operatorname{dist}(Y, Q))^2-(\operatorname{dist}(Y, P))^2=50\right\} .\end{gathered}$
Then which of the following statements is (are) TRUE?

**Options:**

- **(A)** There is a triangle whose area is 1 and all of whose vertices are from $S$.
- **(B)** There are two distinct points $L$ and $M$ in $T$ such that each point on the line segment $L M$ is also in $T$.
- **(C)** There are infinitely many rectangles of perimeter 48 , two of whose vertices are from $S$ and the other two vertices are from $T$.
- **(D)** There is a square of perimeter 48 , two of whose vertices are from $S$ and the other two vertices are from $T$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) There is a square of perimeter 48 , two of whose vertices are from $S$ and the other two vertices are from $T$.**

**Detailed Solution:**

$\begin{aligned}& \mathrm{S}=\left\{\mathrm{X}:(\mathrm{XP})^2-(\mathrm{XQ})^2=50\right\} \\& \mathrm{T}=\left\{\mathrm{Y}:(\mathrm{YQ})^2-(\mathrm{YP})^2=50\right\}\end{aligned}$
for finding $S \equiv X(x, y, z)$ and for $T \equiv Y(x, y, z)$
$\begin{aligned}&\left((x-1)^2+(y-1)^2+(\mathrm{z}-1)^2\right)-\left((\mathrm{x}-4)^2+(\mathrm{y}-2)^2+(\mathrm{z}-7)^2\right)=50 \\& \Rightarrow \quad \mathrm{S}=\{(\mathrm{x}, \mathrm{y}, \mathrm{z}): 6 \mathrm{x}+8 \mathrm{z}=105\} \\& \mathrm{T}=\{(\mathrm{x}, \mathrm{y}, \mathrm{z}): 6 \mathrm{x}+8 \mathrm{z}=5\}\end{aligned}$
Since $\mathrm{S}$ and $\mathrm{T}$ both are plane ;
(1) There exist a triangle in plane $\mathrm{S}$ whose area $=1$ (always)
(2) $\mathrm{L} ~\&~ \mathrm{M}$ lies on plane $\mathrm{T}$, hence line segment joining $\mathrm{L} \& \mathrm{M}$ will lie on plane $\mathrm{T}$.
(3) Distance between $\mathrm{S} \& \mathrm{~T}$
$\mathrm{d}=\left|\frac{105-5}{10}\right|=10$
Hence for rectangle of perimeter 48 can exist.
(4) For Square
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/a9XIVkLb-k7s1awyKNeNOdYpCd5nYsKKTANatSFZxkY.original.fullsize.png">
There will be infinite such rectangle possible.
Hence Answers 1,2,3,4 are correct.

</details>

---

### Q3. JEE Advanced 2023 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#8467;</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#8467;</mi><mn>2</mn></msub></math> be the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>r</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mi>&#955;</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>r</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced><mrow><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>&#956;</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>, respectively, Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> be the set of all the planes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi></math> that contain the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#8467;</mi><mn>1</mn></msub></math>. For a plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mfenced><mi>H</mi></mfenced></math> denote the smallest possible distance between the points of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#8467;</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>H</mi><mn>0</mn></msub></math> be a plane in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mfenced><msub><mi>H</mi><mn>0</mn></msub></mfenced></math> is the maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mfenced><mi>H</mi></mfenced></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi></math> varies over all planes in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>.</p><p>Match each entry in List-I to the correct entries in List-II.</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td>List-I</td>			<td> </td>			<td>List-II</td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">P</mi></mfenced></math></td>			<td>The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mfenced><msub><mi>H</mi><mn>0</mn></msub></mfenced></math> is</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">Q</mi></mfenced></math></td>			<td>The distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>H</mi><mn>0</mn></msub></math> is</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">R</mi></mfenced></math></td>			<td>The distance of origin from <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>H</mi><mn>0</mn></msub></math> is</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">S</mi></mfenced></math></td>			<td>The distance of origin from the point of
			intersection of planes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>z</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>H</mi><mn>0</mn></msub></math> is</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt></math></td>		</tr>		<tr>			<td> </td>			<td> </td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>5</mn></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></td>		</tr>	</tbody></table><p>The correct option is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">P</mi></mfenced><mo>&#8594;</mo><mfenced><mn>2</mn></mfenced><mo>&#160;</mo><mfenced><mi mathvariant="normal">Q</mi></mfenced><mo>&#8594;</mo><mfenced><mn>4</mn></mfenced><mo>&#160;</mo><mfenced><mi mathvariant="normal">R</mi></mfenced><mo>&#8594;</mo><mfenced><mn>5</mn></mfenced><mo>&#160;</mo><mfenced><mi mathvariant="normal">S</mi></mfenced><mo>&#8594;</mo><mfenced><mn>1</mn></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">P</mi></mfenced><mo>&#8594;</mo><mfenced><mn>5</mn></mfenced><mo>&#160;</mo><mfenced><mi mathvariant="normal">Q</mi></mfenced><mo>&#8594;</mo><mfenced><mn>4</mn></mfenced><mo>&#160;</mo><mfenced><mi mathvariant="normal">R</mi></mfenced><mo>&#8594;</mo><mfenced><mn>3</mn></mfenced><mo>&#160;</mo><mfenced><mi mathvariant="normal">S</mi></mfenced><mo>&#8594;</mo><mfenced><mn>1</mn></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">P</mi></mfenced><mo>&#8594;</mo><mfenced><mn>2</mn></mfenced><mo>&#160;</mo><mfenced><mi mathvariant="normal">Q</mi></mfenced><mo>&#8594;</mo><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mfenced><mi mathvariant="normal">R</mi></mfenced><mo>&#8594;</mo><mfenced><mn>3</mn></mfenced><mo>&#160;</mo><mfenced><mi mathvariant="normal">S</mi></mfenced><mo>&#8594;</mo><mfenced><mn>2</mn></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">P</mi></mfenced><mo>&#8594;</mo><mfenced><mn>5</mn></mfenced><mo>&#160;</mo><mfenced><mi mathvariant="normal">Q</mi></mfenced><mo>&#8594;</mo><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mfenced><mi mathvariant="normal">R</mi></mfenced><mo>&#8594;</mo><mfenced><mn>4</mn></mfenced><mo>&#160;</mo><mfenced><mi mathvariant="normal">S</mi></mfenced><mo>&#8594;</mo><mfenced><mn>2</mn></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">P</mi></mfenced><mo>&#8594;</mo><mfenced><mn>5</mn></mfenced><mo>&#160;</mo><mfenced><mi mathvariant="normal">Q</mi></mfenced><mo>&#8594;</mo><mfenced><mn>4</mn></mfenced><mo>&#160;</mo><mfenced><mi mathvariant="normal">R</mi></mfenced><mo>&#8594;</mo><mfenced><mn>3</mn></mfenced><mo>&#160;</mo><mfenced><mi mathvariant="normal">S</mi></mfenced><mo>&#8594;</mo><mfenced><mn>1</mn></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>H</mi><mn>0</mn></msub></math> will be the plane containing the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#8467;</mi><mn>1</mn></msub></math> and parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#8467;</mi><mn>2</mn></msub></math>.</p><p>So, the normal vector of plane parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#8467;</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#8467;</mi><mn>2</mn></msub></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mover><mi>j</mi><mo>^</mo></mover><mfenced><mn>1</mn></mfenced><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mfenced><mrow><mn>1</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Hence, the equation of plane <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>H</mi><mrow><mn>0</mn><mo>&#160;</mo></mrow></msub></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>H</mi><mrow><mn>0</mn><mo>&#160;</mo></mrow></msub><mo>:</mo><mo>&#160;</mo><mi>x</mi><mo>-</mo><mi>z</mi><mo>=</mo><mi>C</mi></math> which passes through origin,</p><p>So,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msub><mi>H</mi><mn>0</mn></msub><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mi>x</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p>Now solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">P</mi></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mfenced><msub><mi>H</mi><mn>0</mn></msub></mfenced><mo>=</mo><mn>1</mn></math> distance of point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mn>0</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>&#160;</mo><mo>&#8756;</mo><mo>&#160;</mo><mi>P</mi><mo>&#8594;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">Q</mi></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mn>0</mn><mo>-</mo><mn>2</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>&#160;</mo><mo>&#8756;</mo><mo>&#160;</mo><mi>Q</mi><mo>&#8594;</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">R</mi></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mn>0</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#8756;</mo><mo>&#160;</mo><mi>R</mi><mo>&#8594;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">S</mi></mfenced></math> Point of intersection will be of given planes<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>z</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>x</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn></math>  will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo></math></p><p>Hence, distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><msqrt><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn></msqrt><mo>=</mo><msqrt><mn>3</mn></msqrt></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>S</mi><mo>&#8594;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Option (B) is correct.</p></blockquote>

</details>

---

### Q4. JEE Advanced 2022 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the reflection of a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> with respect to the plane given by
<math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mfenced><mrow><mi>t</mi><mo>+</mo><mi>p</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>t</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>p</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math>
where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>,</mo><mi>p</mi></math> are real parameters and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>i</mi><mo>^</mo></mover><mo>,</mo><mover><mi>j</mi><mo>^</mo></mover><mo>,</mo><mover><mi>k</mi><mo>^</mo></mover></math> are the unit vectors along the three positive coordinate axes. If the position vectors of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>15</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>20</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#947;</mi><mover><mi>k</mi><mo>^</mo></mover></math> respectively, then which of the following is/are TRUE?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>101</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>71</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mi>&#947;</mi><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>86</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>121</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mi>&#947;</mi><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>86</mn></math>**

**Detailed Solution:**

<p>Given,</p><p>Equation of plane is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mfenced><mrow><mi>t</mi><mo>+</mo><mi>p</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>t</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>p</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p>On rearranging we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>k</mi><mo>^</mo></mover><mo>+</mo><mi>t</mi><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>p</mi><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>So, equation of plane in standard form is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mtd><mtd><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>x</mi></mtd><mtd><mi>y</mi></mtd><mtd><mi>z</mi><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now given coordinate of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mfenced><mrow><mn>10</mn><mo>,</mo><mn>15</mn><mo>,</mo><mn>20</mn></mrow></mfenced></math></p><p>And coordinates of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></mrow></mfenced></math></p><p>Now using the image formula of point and plane we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#945;</mi><mo>-</mo><mn>10</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>&#946;</mi><mo>-</mo><mn>15</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>&#947;</mi><mo>-</mo><mn>20</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mfenced><mrow><mn>10</mn><mo>+</mo><mn>15</mn><mo>+</mo><mn>20</mn><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>-</mo><mn>10</mn><mo>=</mo><mi>&#946;</mi><mo>-</mo><mn>15</mn><mo>=</mo><mi>&#947;</mi><mo>-</mo><mn>20</mn><mo>=</mo><mo>-</mo><mfrac><mn>88</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mfrac><mn>58</mn><mn>3</mn></mfrac><mo>,</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mfrac><mn>43</mn><mn>3</mn></mfrac><mo>,</mo><mi>&#947;</mi><mo>=</mo><mo>-</mo><mfrac><mn>28</mn><mn>3</mn></mfrac></math></p><p>Now solving all options we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>101</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>71</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mi>&#947;</mi><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>86</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>129</mn></math></p>

</details>

---

### Q5. JEE Advanced 2022 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> be two planes given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><mo>:</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>15</mn><mi>y</mi><mo>+</mo><mn>12</mn><mi>z</mi><mo>-</mo><mn>60</mn><mo>=</mo><mn>0</mn><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub><mo>:</mo><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>-</mo><mn>20</mn><mo>=</mo><mn>0</mn></math>.</p><p>Which of the following straight lines can be an edge of some tetrahedron whose two faces lie on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math>?</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mn>5</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>6</mn></mrow><mrow><mo>-</mo><mn>5</mn></mrow></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> be two planes given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><mo>:</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>15</mn><mi>y</mi><mo>+</mo><mn>12</mn><mi>z</mi><mo>-</mo><mn>60</mn><mo>=</mo><mn>0</mn><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub><mo>:</mo><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>-</mo><mn>20</mn><mo>=</mo><mn>0</mn></math>.</p><p>Now finding line of intersection of both the planes,</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>&#955;</mi></math> then we have equations,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mi>x</mi><mo>+</mo><mn>15</mn><mi>y</mi><mo>=</mo><mn>60</mn><mo>-</mo><mn>12</mn><mi>&#955;</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>=</mo><mn>20</mn><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now on solving equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mrow><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>5</mn></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>Replacing&#160;</mtext><mi>&#955;</mi><mo>&#160;</mo><mtext>with&#160;</mtext><mi>z</mi></mrow></mfenced></math></p><p>Now any skew line with the line of intersection of given plane can be edge of tetrahedron,</p><p>Or any line which is intersecting  with the line of intersection passing through plane <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math> or  plane <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> can be edge of tetrahedron, </p><p>Now using above concept we will solve all options,</p><p>Now form option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> we have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mn>5</mn></mfrac></math>, any point lying on this line will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>5</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math> now satisfying this point in given planes we have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#215;</mo><mn>1</mn><mo>+</mo><mn>15</mn><mo>&#215;</mo><mn>1</mn><mo>+</mo><mn>12</mn><mo>&#215;</mo><mfenced><mrow><mn>5</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>60</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>60</mn><mi>&#955;</mi><mo>=</mo><mn>23</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mn>23</mn><mn>60</mn></mfrac></math> now we can see line is intersecting the plane at some point,</p><p>Now checking for plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> we have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn><mo>+</mo><mn>5</mn><mo>&#215;</mo><mn>1</mn><mo>+</mo><mn>4</mn><mo>&#215;</mo><mfenced><mrow><mn>5</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>20</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>20</mn><mi>&#955;</mi><mo>=</mo><mn>13</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mn>13</mn><mn>20</mn></mfrac></math></p><p>So, we can say line is also intersecting plane <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> for some value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math>, So this line can be edge of tetrahedron.</p><p>Now solving for option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced><mo>&#160;</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>6</mn></mrow><mrow><mo>-</mo><mn>5</mn></mrow></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>3</mn></mfrac></math> any point on the line will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>5</mn><mi>&#955;</mi><mo>+</mo><mn>6</mn><mo>,</mo><mn>2</mn><mi>&#955;</mi><mo>,</mo><mn>3</mn><mi>&#955;</mi></mrow></mfenced></math></p><p>Similarly putting in plane <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>P</mi><mn>2</mn></msub></math> we get value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><msub><mi>P</mi><mn>1</mn></msub></msub><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>&#955;</mi><msub><mi>P</mi><mn>2</mn></msub></msub><mo>=</mo><mn>1</mn><mo>&#160;</mo></math></p><p>So, it can be the edge of tetrahedron.</p><p>Now solving for option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>C</mi></mfenced><mo>&#160;</mo><mfrac><mi>x</mi><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>4</mn></mfrac></math> any point on this line will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>,</mo><mn>5</mn><mi>&#955;</mi><mo>+</mo><mn>4</mn><mo>,</mo><mn>4</mn><mi>&#955;</mi></mrow></mfenced></math></p><p>Similarly checking in plane we get,  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><msub><mi>P</mi><mn>1</mn></msub></msub><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>&#955;</mi><msub><mi>P</mi><mn>2</mn></msub></msub><mo>=</mo><mn>0</mn></math>, so it is passing through one point and not lying on plane </p><p>So, it cannot be the edge of tetrahedron.</p><p>Now checking for option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>D</mi></mfenced><mo>&#160;</mo><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>3</mn></mfrac></math> now any point on this line will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#955;</mi><mo>,</mo><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>4</mn><mo>,</mo><mn>3</mn><mi>&#955;</mi></mrow></mfenced></math> and for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>0</mn></math> point will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mn>4</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> which is lying on line of intersection and DR of plane <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> and DR of line is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>, </p><p>Now line is lying completely on plane <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn><mo>+</mo><mn>5</mn><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p>Hence, it can be the edge of tetrahedron.</p>

</details>

---

### Q6. JEE Advanced 2020 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mo>,</mo><mo>&#160;</mo><mi>&#948;</mi></math> be real numbers such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#947;</mi><mn>2</mn></msup><mo>&#8800;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>1</mn></math>. Suppose the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> is the mirror image of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> with respect to the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>x</mi><mo>+</mo><mi>&#946;</mi><mi>y</mi><mo>+</mo><mi>&#947;</mi><mi>z</mi><mo>=</mo><mi>&#948;</mi></math>. Then which of the following statements is/are TRUE?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#948;</mi><mo>-</mo><mi>&#947;</mi><mo>=</mo><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#948;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mi>&#948;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#948;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>4</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/2b50623e-3cc2-43af-9f27-013136e82c58-image.png"/></p><p>From the diagram,</p><p>Mid point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo> </mo><mo>&</mo><mo> </mo><mi>A</mi><mo>'</mo></math> lies on the plane, i.e.,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>α</mi><mo>+</mo><mi>β</mi><mo>-</mo><mi>γ</mi><mo>=</mo><mi>δ</mi><mo>…</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>+</mo><mi>γ</mi><mo>=</mo><mn>1</mn><mo>  </mo><mo>…</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Direction Ratio of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>AA</mi><mo>'</mo></msup><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> will be proportional to normal to the plane,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>α</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>β</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>γ</mi><mn>0</mn></mfrac><mo>=</mo><mi>λ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mn>2</mn><mi>λ</mi><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mn>2</mn><mi>λ</mi><mo>,</mo><mo> </mo><mi>γ</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mn>2</mn><mi>λ</mi><mo>+</mo><mn>0</mn><mo>=</mo><mn>1</mn><mo> </mo><mo>⇒</mo><mi>λ</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mi>α</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>γ</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><mi>δ</mi><mo>=</mo><mn>3</mn></math></p><p>Now,</p><p>(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>0</mn><mo>=</mo><mn>2</mn><mo>≠</mo><mi>δ</mi></math></p><p>(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>+</mo><mi>β</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>2</mn></math>
(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>δ</mi><mo>+</mo><mi>β</mi><mo>=</mo><mn>3</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>4</mn></math>
(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>δ</mi><mo>-</mo><mi>γ</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q7. JEE Advanced 2018 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be a point in the first octant, whose image <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> in the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn></math> (that is, the line segment <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> is perpendicular to the plane <math><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn></math> and the mid-point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> lies in the plane <math><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn></math>) lies on the z-axis. Let the distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> from the x-axis be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is the image of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> in the xy-plane, then the length of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>R</mi></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></mrow></mfenced></math>, <math><mi>Q</mi><mfenced separators="|"><mrow><mn>0,0</mn><mo>,</mo><mi>&#947;</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced separators="|"><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mo>-</mo><mi>&#947;</mi></mrow></mfenced></math>
Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>&#8741;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#160;</mo><mo>&#8658;</mo><mo>-</mo><mfenced><mrow><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#8741;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mi>&#946;</mi></math>
Also, mid point of PQ lies on the plane
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>&#945;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#946;</mi><mn>2</mn></mfrac><mo>=</mo><mn>3</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>6</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>3</mn></math>
Now, distance of point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> from x-axis is <math><msqrt><msup><mrow><mi>&#946;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>&#947;</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>=</mo><mn>5</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#947;</mi><mn>2</mn></msup><mo>=</mo><mn>25</mn><mo>&#8658;</mo><msup><mi>&#947;</mi><mn>2</mn></msup><mo>=</mo><mn>16</mn></math>
As <math><mi>&#946;</mi><mo>=</mo><mi>&#945;</mi><mo>=</mo><mn>3</mn></math>
As <math><mi>&#947;</mi><mo>=</mo><mn>4</mn></math>
Hence, <math><mi>P</mi><mi>R</mi><mo>=</mo><mn>2</mn><mi>&#947;</mi><mo>=</mo><mn>8</mn></math>

</details>

---

### Q8. JEE Advanced 2018 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><msub><mrow><mi>P</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>:</mo><mi>&#160;</mi><mn>2</mn><mi>x</mi><mi>&#160;</mi><mo>+</mo><mi>&#160;</mi><mi>y</mi><mi>&#160;</mi><mo>-</mo><mi>&#160;</mi><mi>z</mi><mi>&#160;</mi><mo>=</mo><mi>&#160;</mi><mn>3</mn><mi>&#160;</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi>&#160;</mi><msub><mrow><mi>P</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>:</mo><mi>&#160;</mi><mi>x</mi><mi>&#160;</mi><mo>+</mo><mi>&#160;</mi><mn>2</mn><mi>y</mi><mi>&#160;</mi><mo>+</mo><mi>&#160;</mi><mi>z</mi><mi>&#160;</mi><mo>=</mo><mi>&#160;</mi><mn>2</mn></math> be two planes. Then, which of the following statement(s) is (are) TRUE?

**Options:**

- **(A)** The line of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><mi>&#160;</mi><mo>,</mo><mi>&#160;</mi><msub><mi>P</mi><mn>2</mn></msub></math> has direction ratios <math><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn></math>
- **(B)** The line <math><mfrac><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>y</mi></mrow><mrow><mn>9</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math> is perpendicular to the line of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><mi>&#160;</mi><mo>,</mo><msub><mi>P</mi><mn>2</mn></msub></math>
- **(C)** The acute angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><mi>&#160;</mi><mo>,</mo><mi>&#160;</mi><msub><mi>P</mi><mn>2</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><msup><mn>60</mn><mi>o</mi></msup></math>
- **(D)** If <math><msub><mrow><mi>P</mi></mrow><mrow><mn>3</mn></mrow></msub></math> is the plane passing through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math> and perpendicular to the line of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><mi>&#160;</mi><mo>,</mo><mi>&#160;</mi><msub><mi>P</mi><mn>2</mn></msub></math> , then the distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2,1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> from the plane <math><msub><mrow><mi>P</mi></mrow><mrow><mn>3</mn></mrow></msub><mi>&#160;</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">s</mi><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) If <math><msub><mrow><mi>P</mi></mrow><mrow><mn>3</mn></mrow></msub></math> is the plane passing through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math> and perpendicular to the line of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><mi>&#160;</mi><mo>,</mo><mi>&#160;</mi><msub><mi>P</mi><mn>2</mn></msub></math> , then the distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2,1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> from the plane <math><msub><mrow><mi>P</mi></mrow><mrow><mn>3</mn></mrow></msub><mi>&#160;</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">s</mi><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

D.C of line intersection <math><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>b</mi><mo>,</mo><mi>&#160;</mi><mi>c</mi></mrow></mfenced></math>
<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>
<math><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>
<math><mfrac><mrow><mi>a</mi></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>b</mi></mrow><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>c</mi></mrow><mrow><mn>4</mn><mo>-</mo><mn>1</mn></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>D</mi><mo>.</mo><mi>C</mi><mi>&#160;</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math>
<math><mfenced separators="|"><mrow><mi>B</mi></mrow></mfenced></math> <math><mfrac><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>y</mi></mrow><mrow><mn>9</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math><mo>&#8658;</mo><mi>&#160;</mi><mfrac><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math><mo>&#8658;</mo><mi>&#160;</mi></math> lines are parallel
<math><mo>(</mo><mi>C</mi><mo>)</mo></math> Acute angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><mi>&#160;</mi><mo>,</mo><mi>&#160;</mi><msub><mi>P</mi><mn>2</mn></msub><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>&#215;</mo><mn>2</mn><mo>-</mo><mn>1</mn><mo>&#215;</mo><mn>1</mn></mrow><mrow><msqrt><mn>6</mn></msqrt><msqrt><mn>6</mn></msqrt></mrow></mfrac></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#160;</mi><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mn>3</mn><mn>6</mn></mfrac></mfenced><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>60</mn><mo>&#176;</mo></math>
<math><mfenced separators="|"><mrow><mi>D</mi></mrow></mfenced></math> Plane is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>z</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math>
Distance of<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> from plane <math><mo>=</mo><mfrac><mrow><mn>2</mn><mo>-</mo><mn>1</mn><mo>+</mo><mn>1</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>

</details>

---

### Q9. JEE Advanced 2017 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

The equation of the plane passing through the point <math><mo>(</mo><mn>1,1</mn><mo>,</mo><mn>1</mn><mo>)</mo></math> and perpendicular to the planes <math><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>5</mn></math> and <math><mn>3</mn><mi>x</mi><mo>-</mo><mn>6</mn><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>7</mn></math> is

**Options:**

- **(A)** <math><mn>14</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>15</mn><mi>z</mi><mo>=</mo><mn>31</mn></math>
- **(B)** <math><mn>14</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>15</mn><mi>z</mi><mo>=</mo><mn>1</mn></math>
- **(C)** <math><mo>-</mo><mn>14</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>15</mn><mi>z</mi><mo>=</mo><mn>3</mn></math>
- **(D)** <math><mn>14</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>15</mn><mi>z</mi><mo>=</mo><mn>27</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>14</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>15</mn><mi>z</mi><mo>=</mo><mn>31</mn></math>**

**Detailed Solution:**

<p>The normal vector of required plane is parallel to vector</p><p><math><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>6</mn></mtd><mtd><mn>-2</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mi> </mi><mo>-</mo><mn>14</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>15</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math></p><p><math><mo>∴</mo></math>    The equation of required plane passing through (1, 1, 1) will be  <math><mo>-</mo><mn>14</mn><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>15</mn><mfenced separators="|"><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mn>14</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>15</mn><mi>z</mi><mo>=</mo><mn>3</mn><mn>1</mn></math></p><p><math><mo>∴</mo></math>    option <math><mn>14</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>15</mn><mi>z</mi><mo>=</mo><mn>31</mn></math> is correct.</p>

</details>

---

### Q10. JEE Advanced 2016 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be the image of the point<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>(</mo><mn>3</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>7</mn><mo>)</mo></math> with respect to the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>3</mn><mo>.</mo></math> Then the equation of the plane passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and containing the straight line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>1</mn></mfrac></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/094fca22-e2aa-45cc-9f1a-984b998db4dc-image.png"/>    </p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math> be mid point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AP</mi></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/cd96a97b-2226-403a-9181-4f1ee2350602-image.png"/>
Line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AP</mi><mi> </mi><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>7</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mi>λ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>F</mi><mfenced separators="|"><mrow><mn>3</mn><mo>+</mo><mi>λ</mi><mo>,</mo><mi> </mi><mn>1</mn><mo>-</mo><mi>λ</mi><mo>,</mo><mi> </mi><mi>λ</mi><mo>+</mo><mn>7</mn></mrow></mfenced></math> lies in the plane</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mo> </mo><mn>3</mn><mo>+</mo><mi>λ</mi><mo>-</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>λ</mi></mrow></mfenced><mo>+</mo><mi>λ</mi><mo>+</mo><mn>7</mn><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>λ</mi><mo>=</mo><mi> </mi><mo>-</mo><mn>6</mn><mi> </mi><mo>⇒</mo><mi>λ</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>F</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>     (using mid point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math>)</p><p>So required plane (containing line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>1</mn></mfrac></math> & passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>) is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>x</mi><mo>-</mo><mn>0</mn></mtd><mtd><mi>y</mi><mo>-</mo><mn>0</mn></mtd><mtd><mi>z</mi><mo>-</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mtable><mtr></mtr><mtr></mtr><mtr></mtr></mtable><mo>∴</mo><mo> </mo><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q11. JEE Advanced 2016 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Consider a pyramid<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>P</mi><mi>Q</mi><mi>R</mi><mi>S</mi></math> located in the first octant <math><mfenced separators="|"><mrow><mi>x</mi><mi>&#160;</mi><mo>&#8805;</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>y</mi><mi>&#160;</mi><mo>&#8805;</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>z</mi><mi>&#160;</mi><mo>&#8805;</mo><mn>0</mn></mrow></mfenced></math> with<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math>, as origin, and<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>P</mi></math> and,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>R</mi></math> along the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8208;</mo><mi>a</mi><mi>x</mi><mi>i</mi><mi>s</mi></math> and the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8208;</mo><mi>a</mi><mi>x</mi><mi>i</mi><mi>s</mi></math>, respectively. The base<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>P</mi><mi>Q</mi><mi>R</mi></math> of the pyramid is a square with<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>P</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>3</mn></math>. The point S is directly above the mid-point T of diagonal, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>Q</mi></math>,  such that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mi>S</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>3</mn></math>. Then

**Options:**

- **(A)** The acute angle between OQ and OS is  <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** The equation of the plane containing the triangle OQS is <math><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>0</mn></math>
- **(C)** The length of the perpendicular from P to the plane containing the triangle OQS is <math><mfrac><mrow><mn>3</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(D)** The perpendicular distance from O to the straight line containing RS is <math><msqrt><mfrac><mrow><mn>15</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) The perpendicular distance from O to the straight line containing RS is <math><msqrt><mfrac><mrow><mn>15</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>**

**Detailed Solution:**

<math><mi mathvariant="normal">O </mi><mfenced separators="|"><mrow><mn>0,0</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>→</mo><mi mathvariant="normal">Origin</mi></math>
<math><mi mathvariant="normal">P </mi><mfenced separators="|"><mrow><mn>3,0</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>→</mo><mi mathvariant="normal">on x axis</mi></math>
<math><math><mi mathvariant="normal">R </mi><mfenced separators="|"><mrow><mn>0,3</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>→</mo><mi mathvariant="normal">on y axis</mi></math></math>
<math><mi mathvariant="normal">Q </mi><mfenced separators="|"><mrow><mn>3,3</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>
<math><mi mathvariant="italic">T </mi><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced><mi> </mi><mo>,</mo><mi> </mi><mn>5</mn><mi> </mi><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mn>3</mn></mrow></mfenced></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/math_43_solut_paper1.jpg"/>

Given OP = OR = 3 and OPQR is a square
<math><mo>⇒</mo></math> <math><mi>O</mi><mi>Q</mi><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi>O</mi><mi>T</mi><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math> and <math><mi>S</mi><mi>T</mi><mo>=</mo><mn>3</mn></math>
Let θ be a angle between OQ & OS
Using <math><mi mathvariant="normal">Δ</mi><mi>S</mi><mi>O</mi><mi>T</mi><mo>,</mo><mi> </mi><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow><mo>=</mo><mfrac><mrow><mi>S</mi><mi>T</mi></mrow><mrow><mi>O</mi><mi>T</mi></mrow></mfrac><mo>=</mo><mi> </mi><msqrt><mn>2</mn></msqrt><mi> </mi><mi> </mi><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi>θ</mi><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><msqrt><mn>2</mn></msqrt></mrow></mrow></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image_file_123.jpg"/>
Clearly, equation of plane containing triangle OQS is x - y = 0   as <math><mi mathvariant="normal"> O </mi><mfenced separators="|"><mrow><mn>0,0</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mi mathvariant="normal"> Q </mi><mfenced separators="|"><mrow><mn>3,3</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mi mathvariant="normal"> S </mi><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mn>, 3</mn></mrow></mfenced><mi mathvariant="normal">  lies on it</mi></math>
<math><mi mathvariant="normal">let ax</mi><mo>+</mo><mi mathvariant="normal">by</mi><mo>+</mo><mi mathvariant="normal">cz</mi><mo>=</mo><mi mathvariant="normal">d</mi></math>
<math><mfenced separators="|"><mrow><mn>0,0</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo> ⇒ </mo><mi>d</mi><mo>=</mo><mn>0</mn></math>
<math><mfenced separators="|"><mrow><mn>3,3</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo> ⇒ </mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>0</mn></math>
<math><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mn>3</mn></mrow></mfenced><mi> </mi><mo>⇒</mo><mfrac><mrow><mn>3</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mi>b</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mn>3</mn><mi>c</mi><mo>=</mo><mn>0</mn></math>
<math><mo>⇒</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>
<math><mo>⇒</mo><mi>b</mi><mo>=</mo><mo>-</mo><mi>a</mi></math>
<math><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>0</mn></math>
Also, length of perpendicular from P to the plane containing the triangle OQS is PT <math><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math> .
Also equation of RS is <math><mover accent="true"><mrow><mi>r</mi></mrow><mo>→</mo></mover><mo>=</mo><mn>3</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>t</mi><mi> </mi><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced></math>
<math><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn><mi>t</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi> </mi><mn>3</mn><mo>-</mo><mfrac><mrow><mn>3</mn><mi>t</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi> </mi><mn>3</mn><mi>t</mi></mrow></mfenced></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/maths_43_paper1_1.jpg"/>
Let M be foot of <math><mo>⊥</mo></math> from origin on line passing through R,S
Let co - ordinates of <math><mi>M</mi><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn><mi>t</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi> </mi><mn>3</mn><mo>-</mo><mfrac><mrow><mn>3</mn><mi>t</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi> </mi><mn>3</mn><mi>t</mi></mrow></mfenced></math>
<math><mo>∵</mo></math> <math><mover accent="true"><mrow><mi>O</mi><mi>M</mi></mrow><mo>→</mo></mover><mi> </mi><mo>.</mo><mi> </mi><mover accent="true"><mrow><mi>R</mi><mi>S</mi></mrow><mo>→</mo></mover><mo>=</mo><mn>0</mn></math>
<math><mo>⇒</mo></math> <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mi>t</mi><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><mfrac><mrow><mn>3</mn><mi>t</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mn>9</mn><mi>t</mi><mo>=</mo><mn>0</mn></math>
<math><mo>⇒</mo></math> <math><mfrac><mrow><mn>9</mn><mi>t</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mn>9</mn><mi>t</mi><mo>=</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><mo>⇒</mo></math> <math><mi>t</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math><mo>∴</mo></math> <math><mi>M</mi><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi> </mi><mn>1</mn></mrow></mfenced></math>
<math><mo>⇒</mo></math> <math><mi>O</mi><mi>M</mi><mo>=</mo><mi> </mi><msqrt><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>25</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mn>1</mn></msqrt><mo>=</mo><mi> </mi><msqrt><mfrac><mrow><mn>30</mn></mrow><mrow><mn>4</mn></mrow></mfrac></msqrt><mo>=</mo><mi> </mi><msqrt><mfrac><mrow><mn>15</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>

</details>

---

### Q12. JEE Advanced 2015 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

In <math><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>3</mn></mrow></msup></math> , let L be a straight line passing through the origin. Suppose that all the points on L are at a constant distance from the two planes <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub><mi mathvariant="normal">&#160;</mi><mo>:</mo><mi mathvariant="normal">x</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">y</mi><mo>-</mo><mi mathvariant="normal">z</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mi mathvariant="normal">&#160;</mi></math> and <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>2</mn></mrow></msub><mi mathvariant="normal">&#160;</mi><mo>:</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo>-</mo><mi mathvariant="normal">y</mi><mo>+</mo><mi mathvariant="normal">z</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>.</mo></math> Let M be the locus of the feet of the perpendiculars drawn from the points on L to the plane <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub></math> . Which of the following points lie (s) on M ?

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi mathvariant="normal"> </mi><mo>-</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>,</mo><mi mathvariant="normal"> </mi><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>,</mo><mi mathvariant="normal"> </mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>,</mo><mi mathvariant="normal"> </mi><mn>0</mn><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced><mi mathvariant="normal"> </mi></math>
- **(D)** <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mi mathvariant="normal"> </mi><mn>0</mn><mo>,</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>,</mo><mi mathvariant="normal"> </mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

Line L will lie on one of the angle bisector planes and will be parallel to line of intersection of the given planes. Also locus of foot of perpendicular of line L in plane <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub></math> will be line M, which will be parallel L.
Foot of perpendicular from (0, 0, 0) on plane <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub></math>  is  <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>,</mo><mi mathvariant="normal"> </mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced></math> 
Hence equation of line M
 <math><mfrac><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">y</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">z</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></mrow><mrow><mo>-</mo><mn>5</mn></mrow></mfrac></math> 
Where  <math><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></math>  is vector parallel to line of intersection of <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>2</mn></mrow></msub></math> .
On checking <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi mathvariant="normal"> </mi><mo>-</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>,</mo><mi mathvariant="normal"> </mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>,</mo><mi mathvariant="normal"> </mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced></math>  satisfy the above equation.

</details>

---

### Q13. JEE Advanced 2015 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `1`

In <math><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>3</mn></mrow></msup></math>, consider the planes <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub><mi mathvariant="normal">&#160;</mi><mo>:</mo><mi mathvariant="normal">y</mi><mo>=</mo><mn>0</mn></math> and <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>2</mn></mrow></msub><mi mathvariant="normal">&#160;</mi><mo>:</mo><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">z</mi><mo>=</mo><mn>1</mn><mo>.</mo></math> Let <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>3</mn></mrow></msub></math>, be a plane, different from <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>2</mn></mrow></msub></math>, which passes through the intersection of <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>2</mn></mrow></msub></math>. If the distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math>, from <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>3</mn></mrow></msub></math>, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>, and the distance of a point <math><mo>(</mo><mi mathvariant="normal">&#945;</mi><mo>,</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#946;</mi><mo>,</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#947;</mi><mo>)</mo></math>, from <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>3</mn></mrow></msub></math>, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>, then which of the following relations is (are) true ?

**Options:**

- **(A)** <math><mn>2</mn><mi mathvariant="normal">α</mi><mo>+</mo><mi mathvariant="normal">β</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">γ</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math><mn>2</mn><mi mathvariant="normal">α</mi><mo>-</mo><mi mathvariant="normal">β</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">γ</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mn>2</mn><mi mathvariant="normal">α</mi><mo>+</mo><mi mathvariant="normal">β</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">γ</mi><mo>-</mo><mn>10</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math><mn>2</mn><mi mathvariant="normal">α</mi><mo>-</mo><mi mathvariant="normal">β</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">γ</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>2</mn><mi mathvariant="normal">α</mi><mo>-</mo><mi mathvariant="normal">β</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">γ</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">P</mi><mn>1</mn></msub><mo>:</mo><mi mathvariant="normal">y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">P</mi><mn>2</mn></msub><mo>:</mo><mi mathvariant="normal">x</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">P</mi><mn>3</mn></msub><mo>:</mo><mi mathvariant="normal">y</mi><mo>+</mo><mi mathvariant="normal">λ</mi><mfenced separators="|"><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">z</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image65-359bcea6-7ecd-4a0f-bc6d-4999b997de48.png"/>
<math><mo>∴</mo><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">β</mi><mo>+</mo><mi mathvariant="normal">λ</mi><mfenced separators="|"><mrow><mi mathvariant="normal">α</mi><mo>+</mo><mi mathvariant="normal">γ</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><mn>2</mn><msup><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></mrow></mfenced><mo>=</mo><mo>±</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mi mathvariant="normal">β</mi><mo>+</mo><mi mathvariant="normal">λ</mi><mfenced separators="|"><mrow><mi mathvariant="normal">α</mi><mo>+</mo><mi mathvariant="normal">γ</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>±</mo><mn>2</mn><msqrt><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi>λ</mi><mn>2</mn></msup></msqrt></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image66-5ae4de7b-b22a-4750-9d45-455f35f5229a.png"/>
<math><mfrac><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">λ</mi></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><mn>2</mn><msup><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac><mo>=</mo><mo>±</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">λ</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo> </mo><mo> </mo><mo> </mo><mfenced><mrow><mi>λ</mi><mo>≠</mo><mn>0</mn></mrow></mfenced></math></p><p><math><mo>∴</mo><mi mathvariant="normal">β</mi><mo>-</mo><mn>2</mn><mfenced separators="|"><mrow><mi mathvariant="normal">α</mi><mo>+</mo><mi mathvariant="normal">γ</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>±</mo><mn>2</mn><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced></math></p><p><math><mn>2</mn><mi mathvariant="normal">α</mi><mo>-</mo><mi mathvariant="normal">β</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">γ</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> or <math><mn>2</mn><mi mathvariant="normal">α</mi><mo>-</mo><mi mathvariant="normal">β</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">γ</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn></math>.</p>

</details>

---

### Q14. JEE Advanced 2012 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

The equation of a plane passing through the line of intersection of the planes $x+2 y+3 z=2$ and $x-y+z=3$

and at a distance $\frac{2}{\sqrt{3}}$ from the point $(3,1,-1)$ is

**Options:**

- **(A)** $5 x-11 y+z=17$
- **(B)** $\sqrt{2} x+y=3 \sqrt{2}-1$
- **(C)** $x+y+z=\sqrt{3}$
- **(D)** $x-\sqrt{2} y=1-\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $5 x-11 y+z=17$**

**Detailed Solution:**

Equation of the plane passing through the intersection line of given planes is

$\begin{array}{ll} 

& (x+2 y+3 z-2)+\lambda(x-y+z-3)=0 \\

\text { or } & (1+\lambda) x+(2-\lambda) y+(3+\lambda) z+(-2-3 \lambda)=0

\end{array}$

$\because \quad$ Its distance from the point $(3,1,-1)$ is $\frac{2}{\sqrt{3}}$

$\begin{array}{l}

\therefore\left|\frac{3(1+\lambda)+1(2-\lambda)-1(3+\lambda)+(-2-3 \lambda)}{\sqrt{(1+\lambda)^{2}+(2-\lambda)^{2}+(3+\lambda)^{2}}}\right|=\frac{2}{\sqrt{3}} \\

\Rightarrow\left|\frac{-2 \lambda}{\sqrt{3 \lambda^{2}+4 \lambda+14}}\right|=\frac{2}{\sqrt{3}} \\

\Rightarrow 3 \lambda^{2}+4 \lambda+14=3 \lambda^{2} \Rightarrow \lambda=-\frac{7}{2}

\end{array}$

$\therefore$ Required equation of plane is

$(x+2 y+3 z-2)-\frac{7}{2}(x-y+z-3)=0$

or $5 x-11 y+z=17$

</details>

---

### Q15. JEE Advanced 2010 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

If the distance of the point $P(1,-2,1)$ from the plane $x+2 y-2 z=\alpha$, where $\alpha>0$, is 5 , then the foot of the perpendicular from $P$ to the plane is

**Options:**

- **(A)** $\left(\frac{8}{3}, \frac{4}{3},-\frac{7}{3}\right)$
- **(B)** $\left(\frac{4}{3},-\frac{4}{3}, \frac{1}{3}\right)$
- **(C)** $\left(\frac{1}{3}, \frac{2}{3}, \frac{10}{3}\right)$
- **(D)** $\left(\frac{2}{3},-\frac{1}{3}, \frac{5}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(\frac{8}{3}, \frac{4}{3},-\frac{7}{3}\right)$**

**Detailed Solution:**

$$
\text { Distance of point } P \text { from plane }=5
$$

$$
\begin{gathered}
\therefore=\left|\frac{1-4-2-\alpha}{3}\right| \\
\alpha=10
\end{gathered}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/MOxuxyIje_ig706wFu1-BnuXYO0fzZdi-AYRS4GoBC8.original.fullsize.png">


Foot of perpendicular
$$
\begin{aligned}
\quad \frac{x-1}{1} & =\frac{y+2}{2}=\frac{z-1}{-2}=\frac{5}{3} \\
\Rightarrow \quad \quad \quad x & =\frac{8}{3}, y=\frac{4}{3}, z=-\frac{7}{3}
\end{aligned}
$$
Thus, the foot of the perpendicular is
$$
A\left(\frac{8}{3}, \frac{4}{3},-\frac{7}{3}\right)
$$

</details>

---

### Q16. JEE Advanced 2010 (Paper 1)

*Type:* `numerical` | *Level:* `1`

If the distance between the plane $A x-2 y+z=d$ and the plane containing the lines $\frac{x-1}{2}=\frac{y-2}{3}=\frac{z-3}{4} \quad$ and $\frac{x-2}{3}=\frac{y-3}{4}=\frac{z-4}{5}$ is $\sqrt{6}$, then $|d|$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

Equation of plane containing the given lines is $\left|\begin{array}{ccc}x-1 & y-2 & z-3 \\ 2 & 3 & 4 \\ 3 & 4 & 5\end{array}\right|=0$
$$
\begin{array}{rr}
\Rightarrow & (x-1)(-1)-(y-2)(-2) \\
& +(z-3)(-1)=0 \\
\Rightarrow & -x+1+2 y-4-z+3=0 \\
\Rightarrow & -x+2 y-z=0 \quad \ldots(i)
\end{array}
$$
Given plane is
$$
x-2 y+z=d
$$

Eqs. (i) and (ii) are parallel.
Clearly, $\quad A=1$
Now, distance between plane
$$
\begin{aligned}
& =\left|\frac{d}{\sqrt{1+4+1}}\right|=\sqrt{6} \\
& \Rightarrow \quad|d|=6 \\
&
\end{aligned}
$$

</details>

---

### Q17. JEE Advanced 2010 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Equation of the plane containing the straight line $\frac{x}{2}=\frac{y}{3}=\frac{z}{4}$ and perpendicular to the plane containing the straight lines $\frac{x}{3}=\frac{y}{4}=\frac{z}{2}$ and $\frac{x}{4}=\frac{y}{2}=\frac{z}{3}$ is

**Options:**

- **(A)** $x+2 y-2 z=0$
- **(B)** $3 x+2 y-2 z=0$
- **(C)** $x-2 y+z=0$
- **(D)** $5 x+2 y-4 z=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x-2 y+z=0$**

**Detailed Solution:**

The DR's of normal to the plane containing $\frac{x}{3}=\frac{y}{4}=\frac{z}{2}$ and $\frac{x}{4}=\frac{y}{2}=\frac{z}{3}$. $\Rightarrow \quad \overrightarrow{\mathbf{n}}_1=\left|\begin{array}{ccc}\hat{\mathbf{i}} & \hat{\mathbf{j}} & \hat{\mathbf{k}} \\ 3 & 4 & 2 \\ 4 & 2 & 3\end{array}\right|=(8 \hat{\mathbf{i}}-\hat{\mathbf{j}}-10 \hat{\mathbf{k}})$
Also, equation of plane containing $\frac{x}{2}=\frac{y}{3}=\frac{z}{4}$ and DR's of normal to be $\overrightarrow{\mathbf{n}}_2=a \hat{\mathbf{i}}+b \hat{\mathbf{j}}+c \hat{\mathbf{k}}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ESo5D22LF0O07y3bQ2iMsKp6KgLfKJluZJ1-oU31OXI.original.fullsize.png">


$$
\begin{array}{ll}
\Rightarrow & a x+b y+c z=0 \\
\text { where, } \overrightarrow{\mathbf{n}}_1 \cdot \overrightarrow{\mathbf{n}}_2=0 \\
\Rightarrow & 8 a-b-10 c=0 \\
\text { and } & \overrightarrow{\mathbf{n}}_2 \perp(2 \hat{\mathbf{i}}+3 \hat{\mathbf{j}}+4 \hat{\mathbf{k}}) \\
\Rightarrow & 2 a+3 b+4 c=0
\end{array}
$$
From Eqs. (ii) and (iii), we get
$$
\begin{aligned}
& \frac{a}{-1 \quad-10}=\frac{b}{8}=\frac{c}{-1} \\
\Rightarrow \quad \frac{a}{-4+30} & =\frac{b}{-20-32}=\frac{c}{24+2} \\
\Rightarrow \quad \quad \quad \frac{a}{26} & =\frac{b}{-52}=\frac{c}{26} \\
\Rightarrow \quad \quad \quad \quad \frac{a}{1} & =\frac{b}{-2}=\frac{c}{1}
\end{aligned}
$$
From Eqs. (i) and (iv), required equation of plane, is $x-2 y+z=0$.

</details>

---

### Q18. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `2`

A plane passes through $(1,-2,1)$ and is perpendicular to two planes $2 x-2 y+z=0$ and $x-y+2 z=4$, then the distance of the plane from the point $(1,2,2)$ is

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** $\sqrt{2}$
- **(D)** $2 \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 \sqrt{2}$**

**Detailed Solution:**

Let the equation of plane be,
$$
a(x-1)+b(y+2)+c(z-1)=0
$$
which is perpendicular to $2 x-2 y+z=0$ and $x-y+2 z=4$
$$
\begin{array}{llrl}
\Rightarrow & 2 a-2 b+c & =0 \text { and } a-b+2 c=0 \\
\text { or } & \frac{a}{-2} 1 & =\frac{b}{2}=\frac{c}{-2} \\
\Rightarrow & -12 & 1 & -1 \\
\Rightarrow & \frac{a}{-3} & =\frac{b}{-3}=\frac{c}{0} \\
& \frac{a}{1}=\frac{b}{1}=\frac{c}{0}
\end{array}
$$
So, the equation of plane is,
$x-1+y+2=0$ or $x+y+1=0$, its distance from the point $(1,2,2)$ is $\frac{|1+2+1|}{\sqrt{2}}=2 \sqrt{2}$.

</details>

---

