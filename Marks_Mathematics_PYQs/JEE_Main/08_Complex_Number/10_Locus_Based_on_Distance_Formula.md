# JEE Main Mathematics - Complex Number

## Topic 10: Locus Based on Distance Formula

**Total Questions:** 8

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of values of $z \in \mathbb{C}$, satisfying the equations $|z-(4+8i)|=\sqrt{10}$ and $|z-(3+5i)|+|z-(5+11i)|=4\sqrt{5}$, is:

**Options:**

- **(A)** $0$
- **(B)** $2$
- **(C)** $1$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$**

**Detailed Solution:**

The first equation $|z-(4+8i)|=\sqrt{10}$ represents a circle with center $C(4, 8)$ and radius $r = \sqrt{10}$.

The second equation $|z-(3+5i)|+|z-(5+11i)|=4\sqrt{5}$ represents an ellipse with foci at $S_1(3, 5)$ and $S_2(5, 11)$, and length of the major axis $2a = 4\sqrt{5}$.

The distance between the foci is $2ae = \sqrt{(5-3)^2 + (11-5)^2} = \sqrt{4+36} = \sqrt{40} = 2\sqrt{10}$.

The center of the ellipse is the midpoint of the line segment joining the foci, which is $\left(\dfrac{3+5}{2}, \dfrac{5+11}{2}\right) = (4, 8)$. This is the same as the center of the circle.

The semi-major axis is $a = 2\sqrt{5}$, so $a^2 = 20$.

The semi-minor axis $b$ is given by $b^2 = a^2 - (ae)^2 = 20 - 10 = 10$, which gives $b = \sqrt{10}$.

Since the circle and the ellipse are concentric and the radius of the circle $r = \sqrt{10}$ is equal to the semi-minor axis $b$ of the ellipse, the circle is inscribed in the ellipse and touches it exactly at the two endpoints of the minor axis.

Therefore, there are exactly $2$ points of intersection, meaning there are $2$ values of $z$ satisfying both equations.

Answer: $2$

</details>

---

### Q2. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $z$ be a complex number such that $|z+2| = |z-2|$ and $\arg\left(\dfrac{z+3}{z-i}\right) = \dfrac{\pi}{4}$. Then $|z|^2$ is equal to:

**Options:**

- **(A)** $9$
- **(B)** $4$
- **(C)** $5$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $9$**

**Detailed Solution:**

Given $|z+2| = |z-2|$, the point $z$ lies on the perpendicular bisector of the line segment joining $(-2, 0)$ and $(2, 0)$. This means $z$ lies on the imaginary axis.

Let $z = iy$, where $y \in \mathbb{R}$.

We are given $\arg\left(\dfrac{z+3}{z-i}\right) = \dfrac{\pi}{4}$. Substituting $z = iy$, we get:

$\dfrac{iy+3}{iy-i} = \dfrac{3+iy}{i(y-1)} = \dfrac{-i(3+iy)}{y-1} = \dfrac{y - 3i}{y-1} = \dfrac{y}{y-1} - i\dfrac{3}{y-1}$

For a complex number $X + iY$ to have an argument of $\dfrac{\pi}{4}$, its real and imaginary parts must be equal and strictly positive. Therefore:

$\dfrac{y}{y-1} = \dfrac{-3}{y-1} > 0$

Since $y \neq 1$, equating the numerators gives $y = -3$.

Checking for positivity: $\dfrac{-3}{-3-1} = \dfrac{3}{4} > 0$, which is valid.

Thus, $z = -3i$.

The value of $|z|^2$ is $|-3i|^2 = 9$.

Answer: $9$

</details>

---

### Q3. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the circles $C_1 : |z| = r$ and $C_2 : |z - 3 - 4i| = 5$, $z \in \mathbb{C}$, be such that $C_2$ lies within $C_1$. If $z_1$ moves on $C_1$, $z_2$ moves on $C_2$ and $\min |z_1 - z_2| = 2$, then $\max |z_1 - z_2|$ is equal to:

**Options:**

- **(A)** $12$
- **(B)** $17$
- **(C)** $22$
- **(D)** $24$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $22$**

**Detailed Solution:**

The center of circle $C_1$ is $O_1(0,0)$ and its radius is $r_1 = r$.

The center of circle $C_2$ is $O_2(3,4)$ and its radius is $r_2 = 5$.

The distance between the centers of the two circles is $d = \sqrt{3^2 + 4^2} = 5$.

Since $C_2$ lies entirely within $C_1$, the minimum distance between a point on $C_1$ and a point on $C_2$ is given by $r_1 - (d + r_2)$.

We are given that $\min |z_1 - z_2| = 2$.

$r - (5 + 5) = 2 \Rightarrow r - 10 = 2 \Rightarrow r = 12$

The maximum distance between a point on $C_1$ and a point on $C_2$ is given by $r_1 + d + r_2$.

$\max |z_1 - z_2| = 12 + 5 + 5 = 22$

Answer: $22$

</details>

---

### Q4. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\{z \in \mathbb{C}:|z-2| \leqslant 4\}$ and $B=\{z \in \mathbb{C}:|z-2|+|z+2|=5\}$. Then the max $\left\{\left|z_{1}-z_{2}\right|: z_{1} \in \mathrm{~A}\right.$ and $\left.z_{2} \in \mathrm{~B}\right\}$ is :

**Options:**

- **(A)** $\frac{17}{2}$
- **(B)** 8
- **(C)** 9
- **(D)** $\frac{15}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{17}{2}$**

**Detailed Solution:**

$|z - 2| \leq 4 \Rightarrow (x - 2)^2 + y^2 \leq 16$
$|z - 2| + |z + 2| = 5 \Rightarrow \dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$
$\Rightarrow \dfrac{4x^2}{25} + \dfrac{4y^2}{9} = 1$
<img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/28S2_s_3_1.png">
Maximum value of $|z_1 - z_2| = 6 + \dfrac{5}{2} = \dfrac{17}{2}$

</details>

---

### Q5. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $z$ be a complex number such that $|z-6|=5$ and $|z+2-6 i|=5$. Then the value of $z^{3}+3 z^{2}-15 z+141$ is equal to

**Options:**

- **(A)** 50
- **(B)** 61
- **(C)** 37
- **(D)** 42

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 50**

**Detailed Solution:**

From $|z - 6| = 5$, point $z$ lies on circle centered at $(6, 0)$ with radius 5.
From $|z + 2 - 6i| = 5$, point lies on circle centered at $(-2, 6)$ with radius 5. 
 Let $z = x + iy$.
First condition gives: $x^2 + y^2 = 12x - 11$.
Second gives: $x^2 + y^2 = -4x + 12y - 15$. 
 Setting equal: $16x - 12y + 4 = 0$, so $x = \frac{3y - 1}{4}$.
Substituting into $(x-6)^2 + y^2 = 25$: $(3y - 25)^2 + 16y^2 = 400$, which simplifies to $25y^2 - 150y + 225 = 0$, giving $y = 3$ and $x = 2$. 
 Thus $z = 2 + 3i$, so $z^2 = -5 + 12i$ and $z^3 = -46 + 9i$. 
 $z^3 + 3z^2 - 15z + 141 = (-46 + 9i) + 3(-5 + 12i) - 15(2 + 3i) + 141 = 50$

</details>

---

### Q6. JEE Main 2025 (4 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $A=\{z \in C:|z-2-i|=3\}$, $B=\{z \in C: \operatorname{Re}(z-i z)=2\}$ and $S=A \cap B$. Then $\sum_{z \in S}|z|^2$ is equal to ________ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **22**

**Detailed Solution:**

Let $z=x+i y$
$\begin{aligned}
& A:|z-2-i|=3 \\
& |(x-2)+(y-1) i|=3 \\
& (x-2)^2+(y-1)^2=9 ....(1)\\
& B=\operatorname{Re}(z-i z)=2 \\
& \operatorname{Re}((x+y)+i(y-x))=2 \\
& x+y=2....(2)
\end{aligned} .$
On solving (1) and (2) we get
$\begin{aligned}
& x=\frac{3 \pm \sqrt{17}}{2}, y=\frac{1 \mp \sqrt{17}}{2} \\
& \sum_{z \in \mathrm{~s}}|z|^2=\frac{1}{4}[2 \times 26+2 \times 18] \\
& \Rightarrow \frac{88}{4}=22
\end{aligned}$

</details>

---

### Q7. JEE Main 2024 (27 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let the complex numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">α</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mover><mi mathvariant="normal">α</mi><mo>¯</mo></mover></mfrac></math> lie on the circles <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mi mathvariant="normal">z</mi><mo>-</mo><msub><mi mathvariant="normal">z</mi><mn>0</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mi mathvariant="normal">z</mi><mo>-</mo><msub><mi mathvariant="normal">z</mi><mn>0</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>16</mn></math> respectively, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">z</mi><mn>0</mn></msub><mo>=</mo><mn>1</mn><mo>+</mo><mi mathvariant="normal">i</mi></math>. Then, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>|</mo><mi mathvariant="normal">α</mi><msup><mo>|</mo><mn>2</mn></msup></math> is__________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **20**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mi mathvariant="normal">z</mi><mo>-</mo><msub><mi mathvariant="normal">z</mi><mn>0</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi mathvariant="normal">z</mi><mo>-</mo><msub><mi mathvariant="normal">z</mi><mn>0</mn></msub></mrow></mfenced><mfenced><mrow><menclose notation="top"><mi mathvariant="normal">z</mi></menclose><mo>-</mo><msub><menclose notation="top"><mi mathvariant="normal">z</mi></menclose><mn>0</mn></msub></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">z</mi><menclose notation="top"><mi mathvariant="normal">z</mi></menclose><mo>-</mo><msub><menclose notation="top"><mi mathvariant="normal">z</mi></menclose><mn>0</mn></msub><mi mathvariant="normal">z</mi><mo>-</mo><msub><mi mathvariant="normal">z</mi><mn>0</mn></msub><menclose notation="top"><mi mathvariant="normal">z</mi></menclose><mo>+</mo><msup><mfenced close="|" open="|"><msub><mi mathvariant="normal">z</mi><mn>0</mn></msub></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced close="|" open="|"><mi mathvariant="normal">z</mi></mfenced><mn>2</mn></msup><mo>-</mo><msub><menclose notation="top"><mi mathvariant="normal">z</mi></menclose><mn>0</mn></msub><mi mathvariant="normal">z</mi><mo>-</mo><msub><mi mathvariant="normal">z</mi><mn>0</mn></msub><menclose notation="top"><mi mathvariant="normal">z</mi></menclose><mo>=</mo><mn>2</mn><mo> </mo><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><msup><mfenced close="|" open="|"><msub><mi mathvariant="normal">z</mi><mn>0</mn></msub></mfenced><mn>2</mn></msup><mo>=</mo><mn>2</mn></mrow></mfenced></math></p><p>It is given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">α</mi></math> lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mi>z</mi><mo>-</mo><msub><mi>z</mi><mn>0</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced close="|" open="|"><mi mathvariant="normal">α</mi></mfenced><mn>2</mn></msup><mo>-</mo><mi mathvariant="normal">α</mi><msub><menclose notation="top"><mi mathvariant="normal">z</mi></menclose><mn>0</mn></msub><mo>-</mo><msub><mi mathvariant="normal">z</mi><mn>0</mn></msub><menclose notation="top"><mi mathvariant="normal">α</mi></menclose><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mi mathvariant="normal">α</mi></menclose><mo>·</mo><mi mathvariant="normal">α</mi><mo>=</mo><msup><mfenced close="|" open="|"><mi mathvariant="normal">α</mi></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><menclose notation="top"><mi mathvariant="normal">α</mi></menclose></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mi>z</mi><mo>-</mo><msub><mi>z</mi><mn>0</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mfrac><mn>1</mn><mover><mi mathvariant="normal">α</mi><mo>¯</mo></mover></mfrac><mo>-</mo><msub><mi mathvariant="normal">z</mi><mn>0</mn></msub></mrow></mfenced><mfenced><mrow><mfrac><mn>1</mn><mi mathvariant="normal">α</mi></mfrac><mo>-</mo><msub><mover><mi mathvariant="normal">z</mi><mo>¯</mo></mover><mn>0</mn></msub></mrow></mfenced><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mover><mi mathvariant="normal">α</mi><mo>¯</mo></mover><msub><mi mathvariant="normal">z</mi><mn>0</mn></msub></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">α</mi><msub><mover><mi mathvariant="normal">z</mi><mo>¯</mo></mover><mn>0</mn></msub></mrow></mfenced><mo>=</mo><mn>16</mn><mo>|</mo><mi mathvariant="normal">α</mi><msup><mo>|</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>1</mn><mo>-</mo><mover><mi mathvariant="normal">α</mi><mo>¯</mo></mover><msub><mi mathvariant="normal">z</mi><mn>0</mn></msub><mo>-</mo><mi mathvariant="normal">α</mi><msub><mover><mi mathvariant="normal">z</mi><mo>¯</mo></mover><mn>0</mn></msub><mo>+</mo><mo>|</mo><mi mathvariant="normal">α</mi><msup><mo>|</mo><mn>2</mn></msup><msup><mfenced close="|" open="|"><msub><mi mathvariant="normal">z</mi><mn>0</mn></msub></mfenced><mn>2</mn></msup><mo>=</mo><mn>16</mn><mo>|</mo><mi mathvariant="normal">α</mi><msup><mo>|</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>1</mn><mo>-</mo><mover><mi mathvariant="normal">α</mi><mo>¯</mo></mover><msub><mi mathvariant="normal">z</mi><mn>0</mn></msub><mo>-</mo><mi mathvariant="normal">α</mi><msub><mover><mi mathvariant="normal">z</mi><mo>¯</mo></mover><mn>0</mn></msub><mo>=</mo><mn>14</mn><mo>|</mo><mi mathvariant="normal">α</mi><msup><mo>|</mo><mn>2</mn></msup><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Using, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>5</mn><mo>|</mo><mi mathvariant="normal">α</mi><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>100</mn><mo>|</mo><mi mathvariant="normal">α</mi><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>20</mn></math></p>

</details>

---

### Q8. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>=</mo><mrow><mi mathvariant="normal">z</mi><mo>∈</mo><mi mathvariant="normal">C</mi><mo>:</mo><mo>|</mo><mi mathvariant="normal">z</mi><mo>-</mo><mi mathvariant="normal">i</mi><mo>|</mo><mo>=</mo><mo>|</mo><mi mathvariant="normal">z</mi><mo>+</mo><mi mathvariant="normal">i</mi><mo>|</mo><mo>=</mo><mo>|</mo><mi mathvariant="normal">z</mi><mo>-</mo><mn>1</mn><mo>|</mo></mrow></math>, then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mo>(</mo><mi mathvariant="normal">S</mi><mo>)</mo></math> is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi mathvariant="normal">z</mi><mo>-</mo><mi mathvariant="normal">i</mi><mo>|</mo><mo>=</mo><mo>|</mo><mi mathvariant="normal">z</mi><mo>+</mo><mi mathvariant="normal">i</mi><mo>|</mo><mo>=</mo><mo>|</mo><mi mathvariant="normal">z</mi><mo>-</mo><mn>1</mn><mo>|</mo></math></p><p>The given equation represents that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">z</mi></math> is a point such that it is equidistant from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo> </mo><mo>&amp;</mo><mo> </mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>We know that in a triangle only circumcentre is the point which is equidistant from the three vertices.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2b2ec73a-8e12-4c5b-9db0-3995a5c016d9.png" style="width: 323px; height: 194px;"/>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> is a triangle. Hence its circum-centre will be the only point whose distance from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>,</mo><mi mathvariant="normal">B</mi><mo>,</mo><mi mathvariant="normal">C</mi></math> will be same.
So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mo>(</mo><mi mathvariant="normal">S</mi><mo>)</mo><mo>=</mo><mn>1</mn></math></p>

</details>

---

