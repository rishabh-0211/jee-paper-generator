# JEE Main Mathematics - Parabola

## Topic 3: Chord of parabola

**Total Questions:** 19

---

### Q1. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let chord PQ of length $3\sqrt{13}$ of the parabola $y^2 = 12x$ be such that the ordinates of points $P$ and $Q$ are in the ratio $1:2$. If the chord PQ subtends an angle $\alpha$ at the focus of the parabola, then $\sin\alpha$ is equal to:

**Options:**

- **(A)** $\dfrac{3}{5}$
- **(B)** $\dfrac{4}{5}$
- **(C)** $\dfrac{5}{13}$
- **(D)** $\dfrac{12}{13}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{3}{5}$**

**Detailed Solution:**

Let the coordinates of points $P$ and $Q$ on the parabola $y^2 = 12x$ be $(x_1, y_1)$ and $(x_2, y_2)$.

Given that the ordinates are in the ratio $1:2$, we have $y_2 = 2y_1$.

Since $P$ and $Q$ lie on the parabola, their abscissae are $x_1 = \dfrac{y_1^2}{12}$ and $x_2 = \dfrac{y_2^2}{12} = \dfrac{4y_1^2}{12} = \dfrac{y_1^2}{3}$.

The length of the chord $PQ$ is $3\sqrt{13}$, so $PQ^2 = 117$.

Using the distance formula:

$(x_2 - x_1)^2 + (y_2 - y_1)^2 = 117$

$\left(\dfrac{y_1^2}{3} - \dfrac{y_1^2}{12}\right)^2 + (2y_1 - y_1)^2 = 117$

$\left(\dfrac{y_1^2}{4}\right)^2 + y_1^2 = 117$

$\dfrac{y_1^4}{16} + y_1^2 - 117 = 0$

$y_1^4 + 16y_1^2 - 1872 = 0$

$(y_1^2 + 52)(y_1^2 - 36) = 0$

Since $y_1^2 > 0$, we get $y_1^2 = 36$, which gives $y_1 = 6$ (taking the positive root by symmetry).

Substituting $y_1 = 6$, we get $x_1 = \dfrac{36}{12} = 3$. Thus, $P$ is $(3, 6)$.

For $Q$, $y_2 = 12$ and $x_2 = \dfrac{144}{12} = 12$. Thus, $Q$ is $(12, 12)$.

The focus of the parabola $y^2 = 12x$ is $S(3, 0)$.

The vectors from the focus $S$ to points $P$ and $Q$ are:

$\overrightarrow{SP} = (3 - 3)\hat{i} + (6 - 0)\hat{j} = 6\hat{j}$

$\overrightarrow{SQ} = (12 - 3)\hat{i} + (12 - 0)\hat{j} = 9\hat{i} + 12\hat{j}$

The angle $\alpha$ subtended by $PQ$ at the focus is the angle between $\overrightarrow{SP}$ and $\overrightarrow{SQ}$.

$\cos\alpha = \dfrac{\overrightarrow{SP} \cdot \overrightarrow{SQ}}{|\overrightarrow{SP}| |\overrightarrow{SQ}|}$

$\cos\alpha = \dfrac{0(9) + 6(12)}{6 \times \sqrt{9^2 + 12^2}} = \dfrac{72}{6 \times 15} = \dfrac{72}{90} = \dfrac{4}{5}$

Therefore, $\sin\alpha = \sqrt{1 - \cos^2\alpha} = \sqrt{1 - \left(\dfrac{4}{5}\right)^2} = \dfrac{3}{5}$

Answer: $\dfrac{3}{5}$

</details>

---

### Q2. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let A be the focus of the parabola $y^{2}=8 x$. Let the line $y=\mathrm{m} x+\mathrm{c}$ intersect the parabola at two distinct points $B$ and $C$. If the centroid of the triangle $A B C$ is $\left(\frac{7}{3}, \frac{4}{3}\right)$, then $(B C)^{2}$ is equal to :

**Options:**

- **(A)** 80
- **(B)** 41
- **(C)** 89
- **(D)** 32

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 80**

**Detailed Solution:**

<img style="width:150px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/28S2_s_19_1.png">
Coordinates of centroid of triangle ABC are
$\dfrac{2}{3}(t_1^2 + t_2^2 + 1) = \dfrac{7}{3} \Rightarrow t_1^2 + t_2^2 = \dfrac{5}{2}$
$\dfrac{4}{3}(t_1 + t_2) = \dfrac{4}{3} \Rightarrow t_1 + t_2 = 1$
$(t_1 + t_2)^2 = t_1^2 + t_2^2 + 2t_1 t_2 \Rightarrow t_1 t_2 = \dfrac{-3}{4}$
$(t_1 - t_2)^2 = (t_1 + t_2)^2 - 4t_1 t_2 = 4$
$(BC)^2 = 4(t_1^2 - t_2^2)^2 + 16(t_1 - t_2)^2$
$\Rightarrow (BC)^2 = 80$

</details>

---

### Q3. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the chord joining the points $\mathrm{P}_{1}\left(x_{1}, y_{1}\right)$ and $\mathrm{P}_{2}\left(x_{2}, y_{2}\right)$ on the parabola $y^{2}=12 x$ subtends a right angle at the vertex of the parabola, then $x_{1} x_{2}-y_{1} y_{2}$ is equal to

**Options:**

- **(A)** 284
- **(B)** 280
- **(C)** 288
- **(D)** 292

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 288**

**Detailed Solution:**

Parabola $y^2 = 12x$ has $4a = 12$, so $a = 3$.
Parametric points: $P_1 = (3t_1^2, 6t_1)$, $P_2 = (3t_2^2, 6t_2)$.
Chord subtends right angle at vertex $O(0,0)$: $\vec{OP_1} \cdot \vec{OP_2} = 0$.
$9t_1^2 t_2^2 + 36t_1 t_2 = 0$
$\Rightarrow t_1 t_2(t_1 t_2 + 4) = 0$
$\Rightarrow t_1 t_2 = -4$.
$x_1 x_2 - y_1 y_2 = 9(t_1 t_2)^2 - 36(t_1 t_2)$ 
$= 9(16) - 36(-4) = 144 + 144 = 288$.

</details>

---

### Q4. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let one end of a focal chord of the parabola $y^{2}=16 x$ be $(16,16)$. If $\mathrm{P}(\alpha, \beta)$ divides this focal chord internally in the ratio $5: 2$, then the minimum value of $\alpha+\beta$ is equal to :

**Options:**

- **(A)** $16$
- **(B)** $5$
- **(C)** $7$
- **(D)** $22$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $7$**

**Detailed Solution:**

Parabola $y^2 = 16x$, $a = 4$, focus at $(4, 0)$. Point $(16, 16)$ has parameter $t_1 = 2$.
Other end of focal chord: $t_2 = -1/t_1 = -1/2$, giving $(4 \cdot 1/4, 8 \cdot (-1/2)) = (1, -4)$.
P divides the chord in ratio 5:2 internally (two cases):
From $(16,16)$ to $(1,-4)$: $P = \left(\frac{37}{7}, \frac{12}{7}\right)$, $\alpha + \beta = 7$.
From $(1,-4)$ to $(16,16)$: $P = \left(\frac{82}{7}, \frac{72}{7}\right)$, $\alpha + \beta = 22$.
Minimum value of $\alpha + \beta = 7$.

</details>

---

### Q5. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the point $P$ of the focal chord $P Q$ of the parabola $y^2=16 x$ be $(1,-4)$. If the focus of the parabola divides the chord PQ in the ratio $\mathrm{m}: \mathrm{n}$, $\operatorname{gcd}(m, n)=1$, then $m^2+n^2$ is equal to :

**Options:**

- **(A)** $17$
- **(B)** $10$
- **(C)** $37$
- **(D)** $26$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $17$**

**Detailed Solution:**

$y^2=16 x ; a=4 \quad$ focus $S \equiv(4,0)$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Z36FNxKiDIX337k0mKii2aIOOLDBEUB05LWYj157Zzw.original.fullsize.png"/>
$\begin{aligned} & 2 \mathrm{at}_1=-4 \\ & \Rightarrow 2(4) \mathrm{t}_1=-4 \\ & \Rightarrow \mathrm{t}_1=-\frac{1}{2} \\ & \because \mathrm{t}_1 \mathrm{t}_2=-1\end{aligned}$
$\begin{aligned}
& \Rightarrow \mathrm{t}_2=2 \\
& \therefore \mathrm{Q}\left(\mathrm{at}_2^2, 2 \mathrm{at}_2\right)=(16,16)
\end{aligned}$
Let, S divides PQ internally in $\lambda: 1$ ratio
$\begin{aligned}
& \therefore \frac{16 \lambda-4}{\lambda+1}=0 \\
& \lambda=\frac{1}{4}=\frac{\mathrm{m}}{\mathrm{n}} \\
& \therefore \mathrm{~m}^2+\mathrm{n}^2=1+16=17
\end{aligned}$

</details>

---

### Q6. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let the focal chord $P Q$ of the parabola $y^2=4 x$ make an angle of $60^{\circ}$ with the positive $x$-axis, where P lies in the first quadrant. If the circle, whose one diameter is PS, S being the focus of the parabola, touches the $y$-axis at the point $(0, \alpha)$, then $5 \alpha^2$ is equal to :

**Options:**

- **(A)** 15
- **(B)** 25
- **(C)** 30
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 15**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/IjTwyqnHbVkOCBXtO1yuOjO-qDCMCQJq6X1EofoXZs4.original.fullsize.png"/>
$\tan 60^{\circ}=\frac{2 \mathrm{t}-0}{\mathrm{t}^2-1}=\sqrt{3} \Rightarrow \mathrm{t}=\sqrt{3}$
$\therefore \mathrm{P}(3,2 \sqrt{3})$
Circle :
$(x-1)(x-3)+(y-0)(y-2 \sqrt{3})=0$
at $x=0$
$\Rightarrow 3+y^2-2 \sqrt{3} y=0$
$\Rightarrow \mathrm{y}=\sqrt{3}=\alpha$
$5 \alpha^2=15$

</details>

---

### Q7. JEE Main 2025 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $y^2=12 x$ be the parabola and $S$ be its focus. Let PQ be a focal chord of the parabola such that $(\mathrm{SP})(\mathrm{SQ})=\frac{147}{4}$. Let C be the circle described taking PQ as a diameter. If the equation of a circle $C$ is $64 x^2+64 y^2-\alpha x-64 \sqrt{3} y=\beta$, then $\beta-\alpha$ is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1328**

**Detailed Solution:**

$\mathrm{y}^2=12 \mathrm{x} \quad \mathrm{a}=3 \quad \mathrm{SP} \times \mathrm{SQ}=\frac{147}{4}$

Let $\mathrm{P}\left(3 \mathrm{t}^2, 6 \mathrm{t}\right)$ and $\mathrm{t}_1 \mathrm{t}_2=-1$
(ends of focal chord)
So, $Q\left(\frac{3}{t^2}, \frac{-6}{t}\right)$
$\begin{aligned}
& \mathrm{S}(3,0) \\
& \mathrm{SP} \times \mathrm{SQ}=\mathrm{PM}_1 \times \mathrm{QM}_2
\end{aligned}$
(dist. from directrix)
$\begin{aligned}
& =\left(3+3 \mathrm{t}^2\right)\left(3+\frac{3}{\mathrm{t}^2}\right)=\frac{147}{4} \\
& \Rightarrow \frac{\left(1+\mathrm{t}^2\right)^2}{\mathrm{t}^2}=\frac{49}{12} \\
& \mathrm{t}^2=\frac{3}{4}, \frac{4}{3} \\
& \mathrm{t}= \pm \frac{\sqrt{3}}{2}, \pm \frac{2}{\sqrt{3}}
\end{aligned}$
considering $\mathrm{t}=\frac{-\sqrt{3}}{2}$
$\mathrm{P}\left(\frac{9}{4},-3 \sqrt{3}\right) \text { and } \mathrm{Q}(4,4 \sqrt{3})$

Hence, diametric circle:
$\begin{aligned}
& (x-4)\left(x-\frac{9}{4}\right)+(y+3 \sqrt{3})(y-4 \sqrt{3})=0 \\
& \Rightarrow x^2+y^2-\frac{25}{4} x-\sqrt{3} y-27=0 \\
& \Rightarrow \alpha=400, \beta=1728 \\
& \beta-\alpha=1328
\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A B C D$ be a trapezium whose vertices lie on the parabola $y^2=4 x$. Let the sides $A D$ and $B C$ of the trapezium be parallel to y -axis. If the diagonal AC is of length $\frac{25}{4}$ and it passes through the point $(1,0)$, then the area of $A B C D$ is

**Options:**

- **(A)** $\frac{75}{4}$
- **(B)** $\frac{25}{2}$
- **(C)** $\frac{125}{8}$
- **(D)** $\frac{75}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{75}{4}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/RtE3cdTR4nN8ytMvAsisJbjNTGJ45PcE9G1pIcAKLmc.original.fullsize.png">


$\begin{aligned}
& \mathrm{A}\left(\mathrm{at}_1^2, 2 \mathrm{at}\right) \& \mathrm{C}\left(\frac{\mathrm{a}}{\mathrm{t}_1^2},-\frac{2 \mathrm{a}}{\mathrm{t}_1}\right) \\
& \text { Length } \mathrm{AC}=\mathrm{a}\left(\mathrm{t}_1+\frac{1}{\mathrm{t}_1}\right)^2=\frac{25}{4}, \mathrm{t}_1+\frac{1}{\mathrm{t}_1}= \pm \frac{5}{2} \\
& \Rightarrow \mathrm{t}_1=2 \text { or } \frac{1}{2}, \mathrm{~A}\left(\frac{1}{2}, 1\right), \mathrm{D}\left(\frac{1}{4},-1\right), \mathrm{B}(4,4), \mathrm{C}(4,-4)
\end{aligned}$

So, area of trapezium $=\frac{1}{2}(8+2)\left(4-\frac{1}{4}\right)=\frac{75}{4}$

</details>

---

### Q9. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the line $3 x-2 y+12=0$ intersects the parabola $4 y=3 x^2$ at the points $A$ and $B$, then at the vertex of the parabola, the line segment $A B$ subtends an angle equal to

**Options:**

- **(A)** $\tan ^{-1}\left(\frac{4}{5}\right)$
- **(B)** $\tan ^{-1}\left(\frac{9}{7}\right)$
- **(C)** $\tan ^{-1}\left(\frac{11}{9}\right)$
- **(D)** $\frac{\pi}{2}-\tan ^{-1}\left(\frac{3}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\tan ^{-1}\left(\frac{9}{7}\right)$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/rPQU_5KkhTKucCcb-Uxpt4_QWullcQgoXsh4hpdnCS8.original.fullsize.png">




$\begin{aligned} & 3 x-2 y+12=0 \\ & 4 y=3 x^2 \\ & \therefore 2(3 x+12)=3 x^2 \\ & \Rightarrow x^2-2 x-8=0 \\ & \Rightarrow x=-2,4 \\ & \mathrm{~m}_{\mathrm{OA}}=-3 / 2, \mathrm{~m}_{\mathrm{OB}}=3 \\ & \tan \theta=\left(\frac{\frac{-3}{2}-3}{1-\frac{9}{2}}\right)=\frac{9}{7} \\ & \theta=\tan ^{-1}\left(\frac{9}{7}\right) \text { (angle will be acute) }\end{aligned}$

</details>

---

### Q10. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{P}(4,4 \sqrt{3})$ be a point on the parabola $y^2=4 \mathrm{a} x$ and PQ be a focal chord of the parabola. If M and $N$ are the foot of perpendiculars drawn from $P$ and $Q$ respectively on the directrix of the parabola, then the area of the quadrilateral PQMN is equal to :

**Options:**

- **(A)** $17 \sqrt{3}$
- **(B)** $\frac{263 \sqrt{3}}{8}$
- **(C)** $\frac{34 \sqrt{3}}{3}$
- **(D)** $\frac{343 \sqrt{3}}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{343 \sqrt{3}}{8}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/edKlL4lWS-LQAQVAn9phCsBnVT8hSZBivjity4F1Jc0.original.fullsize.png">


$\begin{aligned}
& (4,4 \sqrt{3}) \text { lies on } y^2=4 \mathrm{ax} \\
& \Rightarrow 48=4 \mathrm{a} \cdot 4 \\
& \quad 4 \mathrm{a}=12
\end{aligned}$
$\Rightarrow y^2=12 x$ is equation of parabola
Now, parameter of $P$ is $t_1=\frac{2}{\sqrt{3}} \Rightarrow$ Parameters of $Q$ is $\mathrm{t}_2=-\frac{\sqrt{3}}{2} \Rightarrow \mathrm{Q}\left(\frac{9}{4},-3 \sqrt{3}\right)$
Area of trapezium PQNM
$\begin{aligned}
& =\frac{1}{2} \mathrm{MN} \cdot(\mathrm{PM}+\mathrm{QN}) \\
& =\frac{1}{2} \mathrm{MN} \cdot(\mathrm{PS}+\mathrm{QS}) \\
& =\frac{1}{2} \mathrm{MN} \cdot \mathrm{PQ} \\
& =\frac{1}{2} 7 \sqrt{3} \cdot \frac{49}{4}=(343) \frac{\sqrt{3}}{8}
\end{aligned}$

</details>

---

### Q11. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> be a focal chord of the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>36</mn><mi>x</mi></math> of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>,</mo></math> making an acute angle with the positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis. Let the ordinate of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be positive and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> be the point on the line segment <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>M</mi><mo>:</mo><mi>M</mi><mi>Q</mi><mo>=</mo><mn>3</mn><mo>:</mo><mn>1</mn><mo>.</mo></math> Then which of the following points does <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NOT</mi></math> lie on the line passing through M and perpendicular to the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math>?</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>6</mn><mo>,</mo><mn>45</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>6</mn><mo>,</mo><mn>29</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>33</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>43</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>43</mn></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>We have been given the length of focal chord <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>=</mo><mn>100</mn></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4108cf90-11c4-4fed-a4e0-1f68b319ba34.png" style="width: 250px; height: 243px;" /> </p><p>Length of focal chord at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>t</mi></mfenced><mo>=</mo><mi>a</mi><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>100</mn></math></p><p>Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>=</mo><mo>&#177;</mo><mfrac><mn>10</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>t</mi><mo>=</mo><mn>3</mn><mo>,</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mo>-</mo><mn>3</mn><mo>,</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac></math></p><p>Since ordinate of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>ve</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6b7112c9-9d8d-4249-9633-c7bfa13c062e.png" style="width: 250px; height: 80px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>t</mi><mo>=</mo><mn>3</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>(<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>3</mn></math> as slope of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> is positive)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>M</mi><mo>(</mo><mn>21</mn><mo>,</mo><mn>9</mn><mo>)</mo></math></p><p>Required line<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>:</mo><mi>y</mi><mo>-</mo><mn>9</mn><mo>=</mo><mfrac><mrow><mo>-</mo><mn>80</mn></mrow><mn>60</mn></mfrac><mo>(</mo><mi>x</mi><mo>-</mo><mn>21</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>111</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>43</mn></mrow></mfenced></math> does not lie on line.</p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q12. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be the focus of the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>20</mn><mi>x</mi></math> and the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>+</mo><mi>c</mi></math> intersect the parabola at two points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>. Let the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mfenced><mrow><mn>10</mn><mo>,</mo><mo>&#160;</mo><mn>10</mn></mrow></mfenced></math> be the centroid of the triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mi>R</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>-</mo><mi>m</mi><mo>=</mo><mn>6</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><msup><mi>Q</mi><mn>2</mn></msup></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>296</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>325</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>317</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>346</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>325</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be the focus of the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>20</mn><mi>x</mi></math> and the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>+</mo><mi>c</mi></math> intersect the parabola at two points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>,</p><p>And the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mfenced><mrow><mn>10</mn><mo>,</mo><mo>&#160;</mo><mn>10</mn></mrow></mfenced></math> be the centroid of the triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mi>R</mi></math>,</p><p>Now focus of the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>20</mn><mi>x</mi></math> will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mrow><mn>5</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>And parametric points of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mn>10</mn><mi>t</mi></mrow></mfenced></math>,</p><p>Now plotting the diagram we get, </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0358a636-438d-41df-a831-f30690931ea9.png" style="width: 250px; height: 226px;" /></p><p>Now finding the centroid of the triangle we get,</p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math> coordinate we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>5</mn><msup><msub><mi>t</mi><mn>1</mn></msub><mn>2</mn></msup><mo>+</mo><mn>5</mn><msup><msub><mi>t</mi><mn>2</mn></msub><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><msub><mi>t</mi><mn>1</mn></msub><mn>2</mn></msup><mo>+</mo><msup><msub><mi>t</mi><mn>2</mn></msub><mn>2</mn></msup><mo>=</mo><mn>5</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mo>)</mo></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo></math>coordinate we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>10</mn><mfenced><mrow><msub><mi>t</mi><mn>1</mn></msub><mo>+</mo><msub><mi>t</mi><mn>2</mn></msub></mrow></mfenced></mrow><mn>3</mn></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>t</mi><mn>1</mn></msub><mo>+</mo><msub><mi>t</mi><mn>2</mn></msub><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>)</mo></math></p><p>Now solving both equations we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>t</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>t</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn></math></p><p>So, points will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8801;</mo><mo>(</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>10</mn><mo>)</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>Q</mi><mo>&#8801;</mo><mfenced><mrow><mn>20</mn><mo>,</mo><mn>20</mn></mrow></mfenced></math></p><p>Hence, equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>=</mo><mi>y</mi><mo>-</mo><mn>10</mn><mo>=</mo><mfrac><mn>10</mn><mn>15</mn></mfrac><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>30</mn><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>x</mi><mo>+</mo><mfrac><mn>20</mn><mn>3</mn></mfrac></math>, so on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>+</mo><mi>c</mi></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>-</mo><mi>m</mi><mo>=</mo><mn>6</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><msup><mi>Q</mi><mn>2</mn></msup><mo>=</mo><mn>225</mn><mo>+</mo><mn>100</mn><mo>=</mo><mn>325</mn></math></p></blockquote>

</details>

---

### Q13. JEE Main 2023 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

If the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-intercept of a focal chord of the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>4</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>, then the length of this chord is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<p>Given,</p><p>The <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-intercept of a focal chord of the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>4</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>,</p><p>Now simplifying equation of the given parabola we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>8</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>Now on comparing with standard parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>a</mi><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>X</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>Y</mi><mo>=</mo><mi>y</mi><mo>-</mo><mn>2</mn></math></p><p>Hence, the vertex is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> and focus is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>So, equation of line passing through focus is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>2</mn><mo>=</mo><mi>m</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Now, putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> {as given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>intercept of focal chord is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>} in the above line we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> </p><p>So, equation of chord will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>3</mn><mo>-</mo><mi>x</mi></math>,</p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>3</mn><mo>-</mo><mi>x</mi></math> in parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>8</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>8</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><msqrt><msup><mn>10</mn><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>&#215;</mo><mn>7</mn></msqrt><mo>=</mo><msqrt><mn>128</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>3</mn><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mfenced><mrow><mn>3</mn><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow></mfenced><mo>=</mo><msqrt><mn>128</mn></msqrt></math></p><p>Length of focal chord <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><msup><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mrow><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>256</mn></msqrt><mo>=</mo><mn>16</mn></math>.</p>

</details>

---

### Q14. JEE Main 2022 (29 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>:</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>a</mi><mi mathvariant="normal">x</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>&#62;</mo><mn>0</mn></math> be a parabola with focus <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>.Let the tangents to the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> make an angle of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math> with the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>5</mn></math> touch the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> are collinear is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> only
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> only
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>only
- **(D)** any <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#62;</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) any <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#62;</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>Lines making angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>5</mn></math> </p><p>So using formula <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#945;</mi><mo>=</mo><mfrac><mrow><msub><mi>m</mi><mn>2</mn></msub><mo>-</mo><msub><mi>m</mi><mn>1</mn></msub></mrow><mrow><mn>1</mn><mo>+</mo><msub><mi>m</mi><mn>1</mn></msub><msub><mi>m</mi><mn>2</mn></msub></mrow></mfrac></math>, we have slope <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>.</p><p>Which are perpendicular to each-other so, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>S</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi></math>are collinear for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#62;</mo><mn>0</mn></math>. (by property that perpendicular tangents will lie on directrix and chord of contact will pass through focus, so the points are collinear )</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4efce012-094d-4c09-8138-8b74049cbaf8-image.png" style="width: 198px; height: 150px;" />   </p>

</details>

---

### Q15. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let the latus rectum of the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>x</mi></math> be the common chord to the circles <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>2</mn></msub></math> each of them having radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>5</mn></msqrt></math>. Then, the distance between the centres of the circles <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>2</mn></msub></math> is :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msqrt><mn>5</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>5</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ef92c4e9-2e74-46e3-96f8-4a72b5c250ee-image.png" style="width: 346px; height: 240px;" /></p><p>Co-ordinates of focus of parabola will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math>.</p><p>Now, length of latus-rectum <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math>.</p><p>So, length of semi latus-rectum <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn></math>.</p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8736;</mo><mi>L</mi><mi>S</mi><msub><mi>C</mi><mn>1</mn></msub><mo>=</mo><mn>90</mn><mo>&#176;</mo></math></p><p>Now, radius of circle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><msub><mi>C</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><msqrt><mn>5</mn></msqrt></math></p><p>Now, applying pythagoras theorem in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#9651;</mo><mi>L</mi><mi>S</mi><msub><mi>C</mi><mn>1</mn></msub></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>L</mi><msub><mi>C</mi><mn>1</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><msub><mi>C</mi><mn>1</mn></msub><mi>S</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>L</mi><mi>S</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msub><mi>C</mi><mn>1</mn></msub><mi>S</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>L</mi><msub><mi>C</mi><mn>1</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mrow><mi>L</mi><mi>S</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>2</mn><msqrt><mn>5</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mn>2</mn></mfenced><mn>2</mn></msup><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>C</mi><mn>1</mn></msub><mi>S</mi><mo>=</mo><msqrt><mn>16</mn></msqrt><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi>C</mi><mn>1</mn></msub><msub><mi>C</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><msub><mi>C</mi><mn>1</mn></msub><mi>S</mi><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>8</mn></math>.</p>

</details>

---

### Q16. JEE Main 2020 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If one end of a focal chord <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> of the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi></math> is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo>,</mo></math> then the equation of the tangent to it at <math><mi>B</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>24</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mn>24</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

Let <math><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mn>4</mn><mi>t</mi></mrow></mfenced><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math><p>Parameter of other end of focal chord is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>2</mn></math></p><p><math><mo>&#8658;</mo></math> Point is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>8</mn><mo>,</mo><mn>8</mn></mrow></mfenced></math></p><p><math><mo>&#8658;</mo></math> Equation of tangent is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>y</mi><mo>-</mo><mn>4</mn><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>8</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><mi></mi><mi></mi><mn>2</mn><mi>y</mi><mo>-</mo><mi>x</mi><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q17. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If one end of a focal chord of the parabola, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>16</mn><mi>x</mi></math> is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>, then the length of this focal chord is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>**

**Detailed Solution:**

<p>The given parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>16</mn><mi>x</mi></math> is of the form <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>a</mi><mi>x</mi><mo>,</mo></math> hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>4</mn></math> and the focus of the parabola is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>.</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d5e599c5-56fa-4ef0-87d3-0f068a9d80e5-1.png" style="width: 250px; height: 180px;" /></p><p>The equation of a line joining the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub><mo>=</mo><mfenced><mfrac><mrow><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow></mfrac></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow></mfenced><mo>.</mo></math></p><p>Therefore, equation of chord joining <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced></math> to focus <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>0</mn><mo>=</mo><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>y</mi><mo>=</mo><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>x</mi><mi>&#160;</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>16</mn><mo>=</mo><mn>0</mn></math></p><p>To find the points where this line will cut the parabola put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>16</mn></mfrac></math> from the parabola into the line, to get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mfenced><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>16</mn></mfrac></mfenced><mo>+</mo><mi>&#160;</mi><mn>3</mn><mi>y</mi><mo>-</mo><mn>16</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>&#160;</mi><mn>12</mn><mi>y</mi><mo>-</mo><mn>64</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>16</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>16</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>4</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>16</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>16</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p>Thus, the points are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>16</mn><mo>,</mo><mo>-</mo><mn>16</mn></mrow></mfenced><mo>,</mo></math> but <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced></math> is the given point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Q</mi><mo>=</mo><mfenced separators="|"><mrow><mn>16</mn><mo>,</mo><mo>-</mo><mn>16</mn></mrow></mfenced></math></p><p>The distance between the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><msup><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup></msqrt></math></p><p>So, the length of focal chord <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>=</mo><msqrt><msup><mfenced separators="|"><mrow><mn>16</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mo>-</mo><mn>16</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>225</mn><mo>+</mo><mn>400</mn></msqrt><mo>=</mo><msqrt><mn>625</mn></msqrt><mo>=</mo><mn>25</mn></math> units.</p>

</details>

---

### Q18. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The length of the chord of the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>y</mi></math> having equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><msqrt><mn>2</mn></msqrt><mi>y</mi><mo>+</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>=</mo><mn>0</mn></math> is

**Options:**

- **(A)** <math><mn>6</mn><msqrt><mn>3</mn></msqrt></math> units
- **(B)** <math><mn>8</mn><msqrt><mn>2</mn></msqrt></math> units
- **(C)** <math><mn>2</mn><msqrt><mn>11</mn></msqrt></math> units
- **(D)** <math><mn>3</mn><msqrt><mn>2</mn></msqrt></math> units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>6</mn><msqrt><mn>3</mn></msqrt></math> units**

**Detailed Solution:**

<p>Solving the equations of the given parabola and the line, we get,

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mi>y</mi><mo>-</mo><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>y</mi><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>y</mi><mo>+</mo><mn>16</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><msqrt><msup><mfenced separators="|"><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><msub><mi>y</mi><mn>1</mn></msub><msub><mi>y</mi><mn>2</mn></msub></msqrt><mo>=</mo><msqrt><mn>100</mn><mo>-</mo><mn>64</mn></msqrt><mo>=</mo><mn>6</mn></math>

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4081d255-cdf0-4457-ae2d-46c33f897460-image.png" style="width: 341px; height: 292px;" />

<math><mo>&#8658;</mo></math> Length of the chord <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>A</mi><mi>B</mi><mo>=</mo><msqrt><msup><mfenced separators="|"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>2</mn><msup><mfenced separators="|"><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>3</mn></msqrt><mfenced close="|" open="|" separators="|"><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced></math>

<math><mo>=</mo><mn>6</mn><msqrt><mn>3</mn></msqrt></math> units</p>

</details>

---

### Q19. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `2`

The chord $P Q$ of the parabola $y^2=x$, where one end $P$ of the chord is at point $(4,-2)$, is perpendicular to the axis of the parabola. Then the slope of the normal at $Q$ is

**Options:**

- **(A)** $-4$
- **(B)** $-\frac{1}{4}$
- **(C)** 4
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-4$**

**Detailed Solution:**

Point $P$ is $(4,-2)$ and $P Q \perp x$-axis So, $Q=(4,2)$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/uIx6mmuTF_FGALU_1iwHjbKu8dhu8y8PzUFSjJuNmZQ.original.fullsize.png">

Equation of tangent at $(4,2)$ is
$$
\begin{aligned}
& y y_1=\frac{1}{2}\left(x+x_1\right) \\
& \Rightarrow 2 y=\frac{1}{2}(x+2) \Rightarrow 4 y=x+2 \\
& \Rightarrow y=\frac{x}{4}+\frac{1}{2}
\end{aligned}
$$
So, slope of tangent $=\frac{1}{4}$
$\therefore$ Slope of normal $=-4$

</details>

---

