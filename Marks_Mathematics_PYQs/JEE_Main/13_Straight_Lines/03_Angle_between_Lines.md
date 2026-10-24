# JEE Main Mathematics - Straight Lines

## Topic 3: Angle between Lines

**Total Questions:** 20

---

### Q1. JEE Main 2026 (05 April Shift 2)

*Type:* `numerical` | *Level:* `2`

From the point $(-1, -1)$, two rays are sent making angles of $45°$ with the line $x + y = 0$. These rays get reflected from the mirror $x + 2y = 1$. If the equations of the reflected rays are $ax + by = 9$ and $cx + dy = 7$, $a, b, c, d \in \mathbf{Z}$, then the value of $ad + bc$ is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

The given line is $x + y = 0$, which has a slope of $m_1 = -1$.

Let the slope of an incident ray be $m$. Since it makes an angle of $45^{\circ}$ with the line $x + y = 0$, we have:
$\left| \dfrac{m - (-1)}{1 + m(-1)} \right| = \tan 45^{\circ} = 1$
$\Rightarrow \dfrac{m + 1}{1 - m} = \pm 1$

Taking $+1$: $m + 1 = 1 - m \Rightarrow 2m = 0 \Rightarrow m = 0$
Taking $-1$: $m + 1 = -1 + m \Rightarrow 1 = -1$ (which is not possible, implying $m \to \infty$).

The incident rays pass through $P(-1, -1)$. Thus, their equations are:
Ray 1: $y = -1$
Ray 2: $x = -1$

Next, we find the points of intersection of these incident rays with the mirror $x + 2y = 1$.
For Ray 1 ($y = -1$): $x + 2(-1) = 1 \Rightarrow x = 3$. The point of incidence is $A(3, -1)$.
For Ray 2 ($x = -1$): $-1 + 2y = 1 \Rightarrow 2y = 2 \Rightarrow y = 1$. The point of incidence is $B(-1, 1)$.

The reflected rays will appear to originate from the image of $P(-1, -1)$ in the mirror $x + 2y - 1 = 0$. Let the image be $P'(x', y')$.
$\dfrac{x' - (-1)}{1} = \dfrac{y' - (-1)}{2} = -2 \dfrac{1(-1) + 2(-1) - 1}{1^2 + 2^2}$
$\dfrac{x' + 1}{1} = \dfrac{y' + 1}{2} = -2 \left(\dfrac{-4}{5}\right) = \dfrac{8}{5}$
$\Rightarrow x' = \dfrac{8}{5} - 1 = \dfrac{3}{5}$ and $y' = \dfrac{16}{5} - 1 = \dfrac{11}{5}$
So, $P' = \left(\dfrac{3}{5}, \dfrac{11}{5}\right)$.

The reflected rays pass through $P'$ and their respective points of incidence.

Equation of Reflected Ray 1 (passing through $A$ and $P'$):
Slope $m_1' = \dfrac{\dfrac{11}{5} - (-1)}{\dfrac{3}{5} - 3} = \dfrac{\dfrac{16}{5}}{-\dfrac{12}{5}} = -\dfrac{4}{3}$
$y - (-1) = -\dfrac{4}{3}(x - 3) \Rightarrow 3y + 3 = -4x + 12 \Rightarrow 4x + 3y = 9$
Comparing with $ax + by = 9$, we get $a = 4, b = 3$.

Equation of Reflected Ray 2 (passing through $B$ and $P'$):
Slope $m_2' = \dfrac{\dfrac{11}{5} - 1}{\dfrac{3}{5} - (-1)} = \dfrac{\dfrac{6}{5}}{\dfrac{8}{5}} = \dfrac{3}{4}$
$y - 1 = \dfrac{3}{4}(x - (-1)) \Rightarrow 4y - 4 = 3x + 3 \Rightarrow 3x - 4y = -7 \Rightarrow -3x + 4y = 7$
Comparing with $cx + dy = 7$, we get $c = -3, d = 4$.

Finally, we calculate $ad + bc$:
$ad + bc = (4)(4) + (3)(-3) = 16 - 9 = 7$

Answer: $7$

</details>

---

### Q2. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let a be the length of a side of a square OABC with $O$ being the origin. Its side OA makes an acute angle $\alpha$ with the positive $x$-axis and the equations of its diagonals are $(\sqrt{3}+1) x+(\sqrt{3}-1) y=0$ and $(\sqrt{3}-1) x-(\sqrt{3}+1) y+8 \sqrt{3}=0$. Then $\mathrm{a}^2$ is equal to

**Options:**

- **(A)** 48
- **(B)** 32
- **(C)** 16
- **(D)** 24

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 48**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7E1TbmK8_LhKLhbKOOd7S-ofSVNRGWgp_3b78T4QZnk.original.fullsize.png"/>
$\begin{aligned} & \text { Slope of diagonal OB }=\frac{\sqrt{3}+1}{1-\sqrt{3}} \\ & \therefore=\tan 105^{\circ} \\ & \therefore \alpha=60^{\circ} \\ & \therefore \mathrm{A}\left(\operatorname{acos} 60^{\circ}, \operatorname{asin} 60^{\circ}\right) \\ & \therefore \mathrm{A}\left(\frac{\mathrm{a}}{2}, \frac{\sqrt{3} \mathrm{a}}{2}\right)\end{aligned}$
A Lies on other diagonal
$\begin{aligned}
& \therefore\left(\frac{\sqrt{3}-1}{2}\right) a-\left(\frac{\sqrt{3}+1}{2}\right) \cdot \sqrt{3} a+8 \sqrt{3}=0 \\
& a\left[\frac{\sqrt{3}-1-3-\sqrt{3}}{2}\right]=-8 \sqrt{3} \\
& a=4 \sqrt{3} \\
& \therefore a^2=48
\end{aligned}$

</details>

---

### Q3. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A line passes through the origin and makes equal angles with the positive coordinate axes. It intersects the lines
$\mathrm{L}_1: 2 \mathrm{x}+\mathrm{y}+6=0$ and $\mathrm{L}_2: 4 \mathrm{x}+2 \mathrm{y}-\mathrm{p}=0, \mathrm{p} \gt 0$, at the points $A$ and $B$, respectively. If $A B=\frac{9}{\sqrt{2}}$ and the foot of the perpendicular from the point A on the line $L_2$ is $M$, then $\frac{A M}{B M}$ is equal to

**Options:**

- **(A)** $5$
- **(B)** $4$
- **(C)** $2$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/tQm72uYnii4rEoQdjqNq3g9or46Gw94S8uf3IYIjI4g.original.fullsize.png"/>
$\begin{aligned} & \text { Line is } \mathrm{y}=\mathrm{x} \\ & \mathrm{m}_1=1, \mathrm{~m}_2=-2 \\ & \text { so } \tan \theta=\left|\frac{1+2}{1-2}\right| \\ & \tan \theta=\frac{\mathrm{AM}}{\mathrm{BM}}=3\end{aligned}$

</details>

---

### Q4. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two equal sides of an isosceles triangle are along $-x+2 y=4$ and $x+y=4$. If m is the slope of its third side, then the sum, of all possible distinct values of $m$, is :

**Options:**

- **(A)** $-2 \sqrt{10}$
- **(B)** $12$
- **(C)** $6$
- **(D)** $-6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $6$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/SeNBcP9VVg8-b1sjEOAun5T89VdePL9GJbkE4LUiK8U.original.fullsize.png">

Slope of the third side = slope of the perpendicular bisector of given lines
$h: \frac{-x+2 y-4}{\sqrt{5}}= \pm \frac{x+y-4}{\sqrt{2}}$
$\begin{aligned} & h_1: \sqrt{2}(-x+2 y-4)=\sqrt{5}(x+y-4) \\ & h_2: \sqrt{2}(-x+2 y-4)=-\sqrt{5}(x+y-4) \\ & M_{L_1}:-\left[\frac{\sqrt{5}+\sqrt{2}}{\sqrt{5}-2 \sqrt{2}}\right] \\ & M_{L_2}:-\left[\frac{\sqrt{5}-\sqrt{2}}{\sqrt{5}+2 \sqrt{2}}\right] \\ & M_{L_1}+M_{L_2}=-\left[\frac{\sqrt{5}+\sqrt{2}}{\sqrt{5}-2 \sqrt{2}}+\frac{\sqrt{5}-\sqrt{2}}{\sqrt{5}+2 \sqrt{2}}\right]\end{aligned}$
$\begin{aligned} & =-\left[\frac{(\sqrt{5}+\sqrt{2})(\sqrt{5}+2 \sqrt{2})+(\sqrt{5}-\sqrt{2})(\sqrt{5}-2 \sqrt{2})}{-3}\right] \\ & =6\end{aligned}$

</details>

---

### Q5. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the line segment joining the points $(5,2)$ and $(2, a)$ subtends an angle $\frac{\pi}{4}$ at the origin, then the absolute value of the product of all possible values of $a$ is :

**Options:**

- **(A)** 6
- **(B)** 8
- **(C)** 2
- **(D)** -4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -4**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/pdu-fa3VOgXUrrjd7ZfSpaQCvVpjlhvARSjQKktnsY4.original.fullsize.png">
$\begin{aligned} & \mathrm{m}_{\mathrm{OA}}=\frac{2}{5} \\ & \mathrm{~m}_{\mathrm{OB}}=\frac{\mathrm{a}}{2}\end{aligned}$
$\begin{aligned} & \tan \frac{\pi}{4}=\left|\frac{2}{5}-\frac{a}{2}\right| \\ & 1=\left|\frac{4-5 a}{10+2 a}\right|\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/riLOymPOPjtFt3IJAPCRQvcJUXq7Lz8ssUtHSIiecA0.original.fullsize.png">

</details>

---

### Q6. JEE Main 2024 (04 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Consider a triangle $\mathrm{ABC}$ having the vertices $\mathrm{A}(1,2), \mathrm{B}(\alpha, \beta)$ and $\mathrm{C}(\gamma, \delta)$ and angles $\angle A B C=\frac{\pi}{6}$ and $\angle B A C=\frac{2 \pi}{3}$. If the points $\mathrm{B}$ and $\mathrm{C}$ lie on the line $y=x+4$, then $\alpha^2+\gamma^2$ is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/PjPkanOvgGZUmzBxHRPy8yyTLPKenw9MFPUr0MgkF-s.original.fullsize.png">
Equation of line passes through point $\mathrm{A}(1,2)$ which makes angle $\frac{\pi}{6}$ from $y=x+4$ is
$\begin{aligned}
& y-2=\frac{1 \pm \tan \frac{\pi}{6}}{1 \mp \tan \frac{\pi}{6}}(x-1) \\
& y-2=\frac{\sqrt{3} \pm 1}{\sqrt{3} \mp 1}(x-1) \\
& \begin{array}{c|c}
\oplus & \oplus \\
\mathrm{y}-2=(2+\sqrt{3})(\mathrm{x}-1) & \mathrm{y}-2=(2-\sqrt{3})(\mathrm{x}-1)
\end{array} \\
& \text { solve with } \mathrm{y}=\mathrm{x}+4 \quad \text { solve with } \mathrm{y}=\mathrm{x}+4 \\
& x+2=(2+\sqrt{3}) x-2-\sqrt{3} \quad x+2=(2-\sqrt{3}) x-2+\sqrt{3} \\
& x=\frac{4+\sqrt{3}}{1+\sqrt{3}} \quad x=\frac{4-\sqrt{3}}{1-\sqrt{3}} \\
&
\end{aligned}$
$\begin{aligned} & \alpha^2+\gamma^2=\left(\frac{4+\sqrt{3}}{1+\sqrt{3}}\right)^2+\left(\frac{4-\sqrt{3}}{1-\sqrt{3}}\right)^2 \\ & \alpha^2+\gamma^2=14\end{aligned}$

</details>

---

### Q7. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The portion of the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>=</mo><mn>20</mn></math> in the first quadrant is trisected by the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">L</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">L</mi><mn>2</mn></msub></math> passing through the origin. The tangent of an angle between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">L</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">L</mi><mn>2</mn></msub></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>5</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>41</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>5</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>30</mn><mn>41</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>30</mn><mn>41</mn></mfrac></math>**

**Detailed Solution:**

<p>Using section formula</p><p>Co-ordinates of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mfenced><mrow><mfrac><mrow><mn>1</mn><mo>×</mo><mn>5</mn><mo>+</mo><mn>2</mn><mo>×</mo><mn>0</mn></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn><mo>×</mo><mn>0</mn><mo>+</mo><mn>2</mn><mo>×</mo><mn>4</mn></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfenced><mrow><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>,</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></mrow></mfenced></math>
Co-ordinates of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi><mo>=</mo><mfenced><mrow><mfrac><mrow><mn>2</mn><mo>×</mo><mn>5</mn><mo>+</mo><mn>1</mn><mo>×</mo><mn>0</mn></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mo>×</mo><mn>0</mn><mo>+</mo><mn>1</mn><mo>×</mo><mn>4</mn></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfenced><mrow><mfrac><mn>10</mn><mn>3</mn></mfrac><mo>,</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></mrow></mfenced></math>
Slope of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>OA</mi><mo>=</mo><msub><mi mathvariant="normal">m</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>8</mn><mn>3</mn></mfrac></mstyle><mo>-</mo><mn>0</mn></mrow><mrow><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>3</mn></mfrac></mstyle><mo>-</mo><mn>0</mn></mrow></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac></math>
Slope of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>OB</mi><mo>=</mo><msub><mi mathvariant="normal">m</mi><mn>2</mn></msub><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>-</mo><mn>0</mn></mstyle><mstyle displaystyle="true"><mfrac><mn>10</mn><mn>3</mn></mfrac><mo>-</mo><mn>0</mn></mstyle></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/897d19ee-dce5-4b88-ab9d-d32cc077a7ba.png" style="width: 200px; height: 196px;"/></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>θ</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><msub><mi>m</mi><mn>1</mn></msub><mo>-</mo><msub><mi>m</mi><mn>2</mn></msub></mrow><mrow><mn>1</mn><mo>+</mo><msub><mi>m</mi><mn>1</mn></msub><msub><mi>m</mi><mn>2</mn></msub></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mi>θ</mi><mo>=</mo><mfrac><mfrac><mn>6</mn><mn>5</mn></mfrac><mrow><mn>1</mn><mo>+</mo><mfrac><mn>16</mn><mn>25</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mi>θ</mi><mo>=</mo><mfrac><mn>30</mn><mn>41</mn></mfrac></math></p>

</details>

---

### Q8. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The distance between the two points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mo>'</mo></msup></math> which lie on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn></math> such that both the line segments <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mo>'</mo></msup><mi>B</mi></math> (where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>) subtend angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math> at the origin, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>48</mn><mn>5</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>52</mn><mn>5</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>52</mn><mn>5</mn></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9269de49-75a6-44ff-9ac2-7c24421cd26c-image.png" style="width: 280px; height: 200px;" /></p><p>Let the slope of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>B</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p>and the slope of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>A</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>2</mn><mi>x</mi></mfrac></math></p><p>Now angle between two lines, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>2</mn><mi>x</mi></mfrac></mstyle></mrow><mrow><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>6</mn><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mstyle></mrow></mfrac></mfenced></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mfrac><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>2</mn><mi>x</mi></mfrac></mstyle><mrow><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>6</mn><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mstyle></mrow></mfrac></mfenced><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mfenced close="|" open="|"><mfrac><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>4</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfrac></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mo>&#177;</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><msup><mi>A</mi><mo>&#39;</mo></msup><mo>=</mo><mn>10</mn><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>=</mo><mfrac><mn>52</mn><mn>5</mn></mfrac></math></p>

</details>

---

### Q9. JEE Main 2021 (18 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The equation of one of the straight lines which passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>)</mo></math> and makes an angles <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><msqrt><mn>2</mn></msqrt><mo>)</mo></math> with the straight line, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mi>x</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>-</mo><mo>(</mo><mn>15</mn><mo>+</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>)</mo><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>-</mo><mo>(</mo><mn>15</mn><mo>+</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>)</mo><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>-</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>-</mo><mn>5</mn><mi>y</mi><mo>-</mo><mo>(</mo><mn>5</mn><mo>+</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>)</mo><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>-</mo><mo>(</mo><mn>15</mn><mo>+</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>)</mo><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>=</mo><mi>m</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mi>m</mi><mo>-</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>1</mn><mo>+</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mi>m</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi>m</mi><mo>+</mo><msqrt><mn>2</mn></msqrt><mo>=</mo><mo>&#177;</mo><mfenced><mrow><mi>m</mi><mo>-</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math></p><p>from Positive sign</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>m</mi><mo>=</mo><mo>-</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>&#160;</mo><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow><mn>5</mn></mfrac></math></p><p>from negative sign</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi>m</mi><mo>+</mo><msqrt><mn>2</mn></msqrt><mo>=</mo><mo>-</mo><mi>m</mi><mo>+</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>&#8658;</mo><mi mathvariant="normal">m</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow><mn>7</mn></mfrac></math></p><p>According to options take <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow><mn>5</mn></mfrac></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mi>x</mi></mrow><mn>5</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mo>+</mo><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>-</mo><mo>(</mo><mn>15</mn><mo>+</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>)</mo><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q10. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the two lines <math><mi>x</mi><mo>+</mo><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>y</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mi>y</mi><mo>=</mo><mn>1</mn><mo>,</mo><mfenced separators="|"><mrow><mi>a</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mfenced open="{" close="}" separators="|"><mn>0,1</mn></mfenced></mrow></mfenced></math> are perpendicular, then the distance of their point of intersection from the origin is

**Options:**

- **(A)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><mn>5</mn></msqrt></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(D)** <math><msqrt><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msqrt><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></msqrt></math>**

**Detailed Solution:**

<p>If two lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><mi>y</mi><mo>=</mo><msub><mi>c</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mi>y</mi><mo>=</mo><msub><mi>c</mi><mn>2</mn></msub></math> are perpendicular, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><msub><mi>b</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn><mo>.</mo></math></p><p>Since, given lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>y</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mi>y</mi><mo>=</mo><mn>1</mn></math> are perpendicular, hence, we get</p><p><math><mn>1</mn><mo>&#8901;</mo><mn>2</mn><mo>+</mo><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8901;</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#8901;</mo><mfenced separators="|"><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p>But, the discriminant of the quadratic equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>4</mn><mo>-</mo><mn>8</mn><mo>=</mo><mo>-</mo><mn>4</mn><mo>,</mo></math> hence, no real roots exist.</p><p>Thus, the only possible value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>.</mo></math></p><p>And, hence the lines are <math><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>1</mn></math> and <math><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn><mo>.</mo></math></p><p>Point of intersection of these two lines is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mfrac><mn>3</mn><mn>5</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>-</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></mrow></mfenced></math></p><p>We know that, the distance of a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced></math> from origin is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt></math>
Hence, distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>3</mn><mn>5</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>-</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></mrow></mfenced></math> from origin <math><mo>=</mo><msqrt><mfrac><mrow><mn>9</mn></mrow><mrow><mn>25</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>25</mn></mrow></mfrac></msqrt></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mfrac><mn>2</mn><mn>5</mn></mfrac></msqrt><mo>.</mo></math></p>

</details>

---

### Q11. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `2`

The foot of the perpendicular drawn from the origin, on the line, $3 x+y=\lambda(\lambda \neq 0)$ is $P$. If the line meets $x$-axis at $A$ and $y$-axis at $B$, then the ratio $B P$ $: P A$ is

**Options:**

- **(A)** $9: 1$
- **(B)** $1: 3$
- **(C)** $1: 9$
- **(D)** $3: 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3: 1$**

**Detailed Solution:**

Equation of the line, which is perpendicular to the line, $3 x+y=\lambda(\lambda \neq 0)$ and passing through origin, is given by
$$
\frac{x-0}{3}=\frac{y-0}{1}=r
$$
For foot of perpendicular
$$
r=\frac{-((3 \times 0)+(1 \times 0)-\lambda)}{3^2+1^2}=\frac{\lambda}{10}
$$
So, foot of perpendicular $P=\left(\frac{3 \lambda}{10}, \frac{\lambda}{10}\right)$
Given the line meets $\mathrm{X}$-axis at $A=\left(\frac{\lambda}{3}, 0\right)$ and meets $Y$-axis at $B=(0, \lambda)$
So,
$$
\begin{aligned}
&B P=\sqrt{\left(\frac{3 \lambda}{10}\right)^2+\left(\frac{\lambda}{10}-\lambda\right)^2} \Rightarrow B P=\sqrt{\frac{9 \lambda^2}{100}+\frac{81 \lambda^2}{100}} \\
&\Rightarrow B P=\sqrt{\frac{90 \lambda^2}{100}} \\
&\text { Now, } P A=\sqrt{\left(\frac{\lambda}{3}-\frac{3 \lambda}{10}\right)^2+\left(0-\frac{\lambda}{10}\right)^2} \\
&\Rightarrow P A \sqrt{\frac{\lambda^2}{900}+\frac{\lambda^2}{100}} \Rightarrow P A=\sqrt{\frac{10 \lambda^2}{900}}
\end{aligned}
$$
Therefore $B P: P A=3: 1$

</details>

---

### Q12. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A straight line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> through the point <math><mo>(</mo><mn>3</mn><mo>,</mo><mi>&#160;</mi><mo>-</mo><mn>2</mn><mo>)</mo></math> is inclined at an angle of <math><mn>60</mn><mo>&#176;</mo></math> to the line <math><msqrt><mn>3</mn></msqrt><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> also intersects the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>-axis, then the equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> is:

**Options:**

- **(A)** <math><mi>y</mi><mo>+</mo><msqrt><mn>3</mn></msqrt><mi> </mi><mi>x</mi><mo>+</mo><mn>2</mn><mo>-</mo><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>0</mn></math>
- **(B)** <math><msqrt><mn>3</mn></msqrt><mi> </mi><mi>y</mi><mo>-</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>0</mn></math>
- **(C)** <math><msqrt><mn>3</mn></msqrt><mi> </mi><mi>y</mi><mo>+</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>0</mn></math>
- **(D)** <math><mi>y</mi><mo>-</mo><msqrt><mn>3</mn></msqrt><mi>x</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi>y</mi><mo>-</mo><msqrt><mn>3</mn></msqrt><mi>x</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> be the slope of the line,</p><p>then <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><msup><mrow><mn>60</mn></mrow><mrow><mi>o</mi></mrow></msup></mrow></mrow><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mi>m</mi><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>1</mn><mo>-</mo><mi>m</mi><msqrt><mn>3</mn></msqrt></mrow></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>3</mn></msqrt><mo>=</mo><mfenced close="|" open="|" separators="|"><mfrac><mrow><mi>m</mi><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>1</mn><mo>-</mo><msqrt><mn>3</mn></msqrt><mi>&#160;</mi><mi>m</mi></mrow></mfrac></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#177;</mo><msqrt><mn>3</mn></msqrt><mo>=</mo><mfrac><mrow><mi>m</mi><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>1</mn><mo>-</mo><msqrt><mn>3</mn></msqrt><mi>&#160;</mi><mi>m</mi></mrow></mfrac></math></p><p><math><mo>&#8756;</mo><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>3</mn><mi>m</mi><mo>=</mo><mi>m</mi><mo>+</mo><msqrt><mn>3</mn></msqrt></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>3</mn><mi>m</mi><mo>=</mo><mi>m</mi><mo>+</mo><msqrt><mn>3</mn></msqrt></math>

<math><mn>4</mn><mi>m</mi><mo>=</mo><mn>0</mn></math> or <math><mn>2</mn><mi>m</mi><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math>

<math><mi>m</mi><mo>=</mo><mn>0</mn></math> or <math><mi>m</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></math>

Since L intersects <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>-axis we take <math><mi>m</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></math>

and get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msqrt><mn>3</mn></msqrt><mi>x</mi><mo>+</mo><mi>c</mi></math>

Since it passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math>, therefore line will become <math><mi>&#160;</mi><mi>y</mi><mo>-</mo><msqrt><mn>3</mn></msqrt><mi>x</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q13. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></mrow></mfenced><mo>,</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>82</mn><mo>,</mo><mn>30</mn></mrow></mfenced></math>

**Options:**

- **(A)** form an obtuse angled triangle
- **(B)** form an acute angled triangle
- **(C)** lie on a straight line
- **(D)** form a right angled triangle

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) lie on a straight line**

**Detailed Solution:**

<p>The points, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></mrow></mfenced><mo>,</mo><mi>B</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mi>C</mi><mfenced><mrow><mn>82</mn><mo>,</mo><mn>30</mn></mrow></mfenced></math> are collinear, as slope of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo></math>slope of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mo>,</mo></math> i.e.,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mo>-</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mn>0</mn></mrow></mfrac><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mn>30</mn><mo>-</mo><mn>3</mn></mrow><mrow><mn>82</mn><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>Hence, option (Lie on a straight line) is correct.</p>

</details>

---

### Q14. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let $\theta_1$ be the angle between two lines $2 x+3 y+$ $c_1=0$ and $-x+5 y+c_2=0$ and $\theta_2$ be the angle between two lines $2 x+3 y+c_1=0$ and $-x+5 y+$ $c_3=0$, where $c_1, c_2, c_3$ are any real numbers :
Statement-1: If $c_2$ and $c_3$ are proportional, then $\theta_1=\theta_2$.
Statement-2: $\theta_1=\theta_2$ for all $c_2$ and $c_3$.

**Options:**

- **(A)** Statement-1 is true, Statement-2 is true; Statement-2 is a correct explanation of Statement-1.
- **(B)** Statement-1 is true, Statement-2 is true; Statement-2 is not a correct explanation of Statement-1.
- **(C)** Statement-1 is false; Statement- 2 is true.
- **(D)** Statement-1 is true; Statement- 2 is false.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Statement-1 is true, Statement-2 is true; Statement-2 is a correct explanation of Statement-1.**

**Detailed Solution:**

Two lines $-x+5 y+c_2=0$ and $-x+5 y+c_3$ $=0$ are parallel to each other. Hence statement-1 is true, statement-2 is true and statement-2 is the correct explanation of statement-1.

</details>

---

### Q15. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The acute angle between two lines such that the direction cosines $l, m, n$, of each of them satisfy the equations $l+m+n=0$ and $l^2+m^2-n^2=0$ is :

**Options:**

- **(A)** $15^{\circ}$
- **(B)** $30^{\circ}$
- **(C)** $60^{\circ}$
- **(D)** $45^{\circ}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $60^{\circ}$**

**Detailed Solution:**

Let $l_1, m_1, n_1$ and $l_2, m_2, n_2$ be the d.c of line 1 and 2 respectively, then as given $l_1+m_1+n_1=0$
and $l_2+m_2+n_2=0$
and $l_1{ }^2+m_1{ }^2-n_1^2=0$ and $l_2^2+m_2^2-n_2^2=0$
$\left(\because l+m+n=0\right.$ and $\left.l^2+m^2-n^2=0\right)$
Angle between lines, $\theta$ is
$$
\cos \theta=l_1 l_2+m_1 m_2+n_1 n_2
$$
As given $l^2+m^2=n^2$ and $l+m=-n$ $\Rightarrow(-n)^2-2 l m=n^2 \Rightarrow 2 l m=0$ or $l m=0$
So $l_1 m_1=0, l_2 m_2=0$
If $l_1=0, m_1 \neq 0$ then $l_1 m_2=0$
If $m_1=0, l_1 \neq 0$ then $l_2 m_1=0$
If $l_2=0, m_2 \neq 0$ then $l_2 m_1=0$
If $m_2=0, l_2 \neq 0$ then $l_1 m_2=0$
Also $l_1 l_2=0$ and $m_1 m_2=0$
$$
\begin{aligned}
& l^2+m^2-n^2=l^2+m^2+n^2-2 n^2=0 \\
& \Rightarrow 1-2 n^2=0 \Rightarrow n=\pm \frac{1}{\sqrt{2}} \\
& \therefore n_1=\pm \frac{1}{\sqrt{2}}, n_2=\pm \frac{1}{\sqrt{2}} \\
& \therefore \cos \theta=\frac{1}{2} \theta=60^{\circ} \text { (acute angle) }
\end{aligned}
$$

</details>

---

### Q16. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If the three lines $x-3 y=p, a x+2 y=q$ and $a x+y=r$ form a right-angled triangle then :

**Options:**

- **(A)** $a^2-9 a+18=0$
- **(B)** $a^2-6 a-12=0$
- **(C)** $a^2-6 a-18=0$
- **(D)** $a^2-9 a+12=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $a^2-9 a+18=0$**

**Detailed Solution:**

Since three lines $x-3 y=p$, $a x+2 y=q$ and $a x+y=r$ form a right angled triangle $\therefore$ product of slopes of any two lines $=-1$ Suppose $a x+2 y=q$ and $x-3 y=p$ are $\perp$ to each other.
$$
\therefore \frac{-a}{2} \times \frac{1}{3}=-1 \Rightarrow a=6
$$
Now, consider option one by one $a=6$ satisfies only option (a)
$\therefore$ Required answer is $a^2-9 a+18=0$

</details>

---

### Q17. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `1`

If the straight lines $x+3 y=4,3 x+y=4$ and $x+y$ $=0$ form a triangle, then the triangle is

**Options:**

- **(A)** scalene
- **(B)** equilateral triangle
- **(C)** isosceles
- **(D)** right angled isosceles

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) isosceles**

**Detailed Solution:**

Let equation of $A B: x+3 y=4$
Let equation of $B C: 3 x+y=4$
Let equation of $C A: x+y=0$
Now, By solving these equations we get $A=(-2,2), B=(1,1)$ and $C=(2,-2)$
Now, $A B=\sqrt{9+1}=\sqrt{10}$,
$$
B C=\sqrt{1+9}=\sqrt{10}
$$
and $C A=\sqrt{16+16}=\sqrt{32}$
Since, length of $A B$ and $B C$ are same
therefore triangle is isosceles.

</details>

---

### Q18. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `1`

The line $L$ given by $\frac{x}{5}+\frac{y}{b}=1$ passes through the point $(13,32)$. The line $K$ is parallel to $L$ and has the equation $\frac{x}{c}+\frac{y}{3}=1$. Then the distance between $L$ and $K$ is

**Options:**

- **(A)** $\sqrt{17}$
- **(B)** $\frac{17}{\sqrt{15}}$
- **(C)** $\frac{23}{\sqrt{17}}$
- **(D)** $\frac{23}{\sqrt{15}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{23}{\sqrt{17}}$**

**Detailed Solution:**

Slope of line $L=-\frac{b}{5}$
Slope of line $\mathrm{K}=-\frac{3}{\mathrm{c}}$
Line $L$ is parallel to line $k$.
$$
\Rightarrow \frac{\mathrm{b}}{5}=\frac{3}{\mathrm{c}} \quad \Rightarrow \mathrm{bc}=15
$$
$(13,32)$ is a point on $\mathrm{L}$.
$$
\begin{aligned}
& \Rightarrow \frac{13}{5}+\frac{32}{b}=1 \quad \Rightarrow \frac{32}{b}=-\frac{8}{5} \\
& \Rightarrow \mathrm{b}=-20 \quad \Rightarrow \mathrm{c}=-\frac{3}{4} \\
&
\end{aligned}
$$
Equation of $K: y-4 x=3$
Distance between $\mathrm{L}$ and $\mathrm{K}=\frac{|52-32+3|}{\sqrt{17}}=\frac{23}{\sqrt{17}}$

</details>

---

### Q19. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

The two lines $x=a y+b, z=c y+d ;$ and $x=a^{\prime} y+b^{\prime}, z=c^{\prime} y+d^{\prime}$ are perpendicular to each other if

**Options:**

- **(A)** $\mathrm{aa}^{\prime}+\mathrm{cc}^{\prime}=-1$
- **(B)** $\mathrm{aa}^{\prime}+\mathrm{cc}^{\prime}=1$
- **(C)** $\frac{a}{a^{\prime}}+\frac{c}{c^{\prime}}=-1$
- **(D)** $\frac{a}{a^{\prime}}+\frac{c}{c^{\prime}}=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{aa}^{\prime}+\mathrm{cc}^{\prime}=-1$**

**Detailed Solution:**

Equation of lines $\frac{x-b}{a}=y=\frac{z-d}{c}$
$\frac{x-b^{\prime}}{a^{\prime}}=y=\frac{z-d^{\prime}}{c^{\prime}}$
Lines are perpendicular $\Rightarrow a a^{\prime}+1+c c^{\prime}=0$

</details>

---

### Q20. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

A line makes the same angle $\theta$, with each of the $x$ and $z$ axis. If the angle $\beta$, which it makes with $y$-axis, is such that $\sin ^2 \beta=3 \sin ^2 \theta$, then $\cos ^2 \theta$ equals

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{1}{5}$
- **(C)** $\frac{3}{5}$
- **(D)** $\frac{2}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{5}$**

**Detailed Solution:**

$I=\cos \theta, m=\cos \theta, n=\cos \beta$
$\cos ^2 \theta+\cos ^2 \theta+\cos ^2 \beta=1 \Rightarrow 2 \cos ^2 \theta=\sin ^2 \beta=3 \sin ^2 \theta \quad$ (given)
$\cos ^2 \theta=3 / 5$

</details>

---

