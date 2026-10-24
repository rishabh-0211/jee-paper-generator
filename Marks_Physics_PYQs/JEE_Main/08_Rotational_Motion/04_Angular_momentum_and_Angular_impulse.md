# JEE Main Physics - Rotational Motion

## Topic 4: Angular momentum and Angular impulse

**Total Questions:** 52

---

### Q1. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

When the position vector $\vec{r}=x \hat{i}+y \hat{j}+z \hat{k}$ changes sign as $-\vec{r}$, which one of the following vector will not flip under sign change ?

**Options:**

- **(A)** Angular momentum
- **(B)** Velocity
- **(C)** Acceleration
- **(D)** Linear momentum

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Angular momentum**

**Detailed Solution:**

The transformation $\vec{r} \to -\vec{r}$ is known as a parity transformation (inversion through the origin).
Vectors that change sign under parity are called polar vectors, while those that do not change sign are called axial vectors (or pseudovectors).
Velocity is defined as $\vec{v} = \frac{d\vec{r}}{dt}$. Since $\vec{r} \to -\vec{r}$, we have $\vec{v} \to -\vec{v}$.
Acceleration is defined as $\vec{a} = \frac{d\vec{v}}{dt}$. Since $\vec{v} \to -\vec{v}$, we have $\vec{a} \to -\vec{a}$.
Linear momentum is defined as $\vec{p} = m\vec{v}$. Since $\vec{v} \to -\vec{v}$, we have $\vec{p} \to -\vec{p}$.
Angular momentum is defined as $\vec{L} = \vec{r} \times \vec{p}$.
Under the transformation $\vec{r} \to -\vec{r}$ and $\vec{p} \to -\vec{p}$, the cross product becomes:
$\vec{L}' = (-\vec{r}) \times (-\vec{p}) = \vec{r} \times \vec{p} = \vec{L}$.
Thus, angular momentum does not flip its sign under the transformation $\vec{r} \to -\vec{r}$.

</details>

---

### Q2. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A thin uniform rod $(X)$ of mass $M$ and length $L$ is pivoted at a height $\left(\frac{L}{3}\right)$ as shown in the figure. The rod is allowed to fall from a vertical position and lie horizontally on the table. The angular velocity of this rod when it hits the table top, is $\_\_\_\_$. ($\mathrm{g}=$ gravitational acceleration) 
 <img style="width:200px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/24S2_q_39_1.png">

**Options:**

- **(A)** $\frac{3}{\sqrt{2}} \sqrt{\frac{g}{L}}$
- **(B)** $\frac{1}{\sqrt{2}} \sqrt{\frac{g}{L}}$
- **(C)** $\sqrt{\frac{3}{2} \frac{g}{L}}$
- **(D)** $\sqrt{\frac{3 g}{L}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{\frac{3 g}{L}}$**

**Detailed Solution:**

The rod is pivoted at a distance $\frac{L}{3}$ from one end. The centre of mass is at a distance $\frac{L}{6}$ from the pivot.
Using energy conservation:
$mg\frac{\ell}{6} = \frac{1}{2}I\omega^2$
Moment of inertia about the pivot (using parallel axis theorem):
$I = \frac{m\ell^2}{12} + m\left(\frac{\ell}{6}\right)^2 = \frac{m\ell^2}{12} + \frac{m\ell^2}{36} = \frac{m\ell^2}{9}$
$mg\frac{\ell}{6} = \frac{1}{2} \cdot \frac{m\ell^2}{9} \cdot \omega^2$
$\omega^2 = \frac{9g}{6 \cdot \frac{\ell}{2}} = \frac{3g}{\ell}$
$\omega = \sqrt{\frac{3g}{\ell}}$

</details>

---

### Q3. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two small balls with masses $m$ and 2 m are attached to both ends of a rigid rod of length $d$ and negligible mass. If angular momentum of this system is $L$ about an axis ($A$) passing through its centre of mass and perpendicular to the rod then angular velocity of the system about $A$ is :

**Options:**

- **(A)** $\frac{2 L}{5 m d^{2}}$
- **(B)** $\frac{4}{3} \frac{L}{m d^{2}}$
- **(C)** $\frac{3}{2} \frac{L}{m d^{2}}$
- **(D)** $\frac{2 L}{m d^{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{2} \frac{L}{m d^{2}}$**

**Detailed Solution:**

CM from mass $m$: $x_{cm} = \frac{2md}{3m} = \frac{2d}{3}$.
Distances: $m$ is $2d/3$ from CM, $2m$ is $d/3$ from CM.
$I_{cm} = m(2d/3)^2 + 2m(d/3)^2 = \frac{4md^2}{9} + \frac{2md^2}{9} = \frac{2md^2}{3}$.
$L = I\omega \Rightarrow \omega = \frac{L}{I} = \frac{3L}{2md^2}$.

</details>

---

### Q4. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two cars $A$ and $B$ each of mass $10^{3} \mathrm{~kg}$ are moving on parallel tracks separated by a distance of 10 m, in same direction with speeds $72 \mathrm{~km} / \mathrm{h}$ and $36 \mathrm{~km} / \mathrm{h}$. The magnitude of angular momentum of $\operatorname{car} A$ with respect to $\operatorname{car} B$ is $\_\_\_\_$ J.s.

**Options:**

- **(A)** $2 \times 10^{5}$
- **(B)** $10^{5}$
- **(C)** $3.6 \times 10^{5}$
- **(D)** $3 \times 10^{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $10^{5}$**

**Detailed Solution:**

Mass of each car $m = 10^3$ kg.
Speed of car $A$, $v_A = 72$ km/h $= 72 \times \frac{5}{18} = 20$ m/s.
Speed of car $B$, $v_B = 36$ km/h $= 36 \times \frac{5}{18} = 10$ m/s.
Relative velocity of car $A$ with respect to car $B$ is $v_{AB} = v_A - v_B = 20 - 10 = 10$ m/s.
The cars are moving on parallel tracks separated by a perpendicular distance $d = 10$ m.
The magnitude of angular momentum of car $A$ with respect to car $B$ is given by $L = m \times v_{AB} \times d$.
Substituting the values: $L = 10^3 \times 10 \times 10 = 10^5$ J.s.
Thus, the correct option is (2).

</details>

---

### Q5. JEE Main 2025 (4 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

A solid sphere with uniform density and radius R is rotating initially with constant angular velocity $\left(\omega_1\right)$ about its diameter. After some time during the rotation its starts loosing mass at a uniform rate, with no change in its shape. The angular velocity of the sphere when its radius become $R / 2$ is $x \omega_1$. The value of $x$ is ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **32**

**Detailed Solution:**

When sphere is of radius $R$, its mass is $M$, when radius is reduced to $\frac{\mathrm{R}}{2}$, mass will reduced to $\frac{\mathrm{M}}{8}$ Now by conservation of angular momentum
$\begin{aligned}
& \left(\tau_{e x t}=0\right) \\
& L_1=L_2 \\
& I_1 \omega_1=I_2 \omega_2 \\
& \left(\frac{2}{5} M R^2\right) \omega_1=\left(\frac{2}{5}\left(\frac{\mathrm{M}}{8}\right)\left(\frac{\mathrm{R}}{2}\right)^2\right) \omega_2
\end{aligned}$
$\omega_2=32 \omega_1$ value of x is 32
Answer is 32

</details>

---

### Q6. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\overrightarrow{\mathrm{L}}$ and $\overrightarrow{\mathrm{P}}$ represent the angular momentum and linear momentum respectively of a particle of mass ' m ' having position vector $\overrightarrow{\mathrm{r}}=\mathrm{a}(\hat{\mathrm{i}} \cos \omega \mathrm{t}+\hat{\mathrm{j}} \sin \omega \mathrm{t})$. The direction of force is

**Options:**

- **(A)** Opposite to the direction of $\vec{r}$
- **(B)** Opposite to the direction of $\overrightarrow{\mathrm{L}}$
- **(C)** Opposite to the direction of $\vec{P}$
- **(D)** Opposite to the direction of $\overrightarrow{\mathrm{L}} \times \overrightarrow{\mathrm{P}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Opposite to the direction of $\vec{r}$**

**Detailed Solution:**

$\overrightarrow{\mathrm{a}}=-\omega^2 \overrightarrow{\mathrm{r}}$
$\therefore \overrightarrow{\mathrm{F}}$ opposite to $\overrightarrow{\mathrm{r}}-$

</details>

---

### Q7. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/jleg2iUvO_hwfoKICDw8lKIuI4YN3aQcis4J6iN1DFs.original.fullsize.png"/>

Three equal masses $m$ are kept at vertices (A, B, C) of an equilateral triangle of side a in free space. At $t=0$, they are given an initial velocity $\vec{V}_A=V_0 \overrightarrow{A C}, \vec{V}_B=V_0 \overrightarrow{B A}$ and $\vec{V}_C=V_0 \overrightarrow{C B}$. Here, $\overrightarrow{A C}, \overrightarrow{C B}$ and $\overrightarrow{B A}$ are unit vectors along the edges of the triangle. If the three masses interact gravitationally, then the magnitude of the net angular momentum of the system at the point of collision is :

**Options:**

- **(A)** $3 \mathrm{a} \mathrm{m} \mathrm{V}_0$
- **(B)** $\frac{3}{2}$ a $\mathrm{m} \mathrm{V}_0$
- **(C)** $\frac{\sqrt{3}}{2}$ a $\mathrm{m} \mathrm{V}_0$
- **(D)** $\frac{1}{2}$ a $\mathrm{mV}_0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\sqrt{3}}{2}$ a $\mathrm{m} \mathrm{V}_0$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/hdV4N75tdnwW__yunRZSjF6MYOM0mNPgQOk8yzpPW40.original.fullsize.png">

$d=\frac{a}{2 \sqrt{3}}$
Angular momentum of one mass about point $O$
$\begin{aligned}
L & =m v d \\
& =m v_0 \cdot \frac{a}{2 \sqrt{3}}
\end{aligned}$

Net angular momentum about point $O$
$\begin{aligned}
L_{\text {net }} & =32 \\
& =\frac{\sqrt{3} m v_0 a}{2}
\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

An object of mass ' m ' is projected from origin in a vertical $x y$ plane at an angle $45^{\circ}$ with the x axis with an initial velocity $\mathrm{v}_0$. The magnitude and direction of the angular momentum of the object with respect to origin, when it reaches at the maximum height, will be [ g is acceleration due to gravity]

**Options:**

- **(A)** $\frac{m v_o^3}{2 \sqrt{2} g}$ along negative $z$-axis
- **(B)** $\frac{m v_o^3}{4 \sqrt{2} g}$ along positive $z$-axis
- **(C)** $\frac{m v_o^3}{4 \sqrt{2} g}$ along negative $z$-axis
- **(D)** $\frac{m v_o^3}{2 \sqrt{2} g}$ along positive $z$-axis

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{m v_o^3}{4 \sqrt{2} g}$ along negative $z$-axis**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/iffaTEHUTnFGM_mNF9aLyYWmU-JddqJhEsdZzPm3aIs.original.fullsize.png">



$\begin{aligned}
& \mathrm{H}=\frac{\left(\frac{\mathrm{v}_0}{\sqrt{2}}\right)^2}{2 \mathrm{~g}}=\frac{\mathrm{v}_0^2}{4 \mathrm{~g}} \\
& \mathrm{~L}=\mathrm{mvh} \\
& \mathrm{~L}=\mathrm{m} \frac{\mathrm{v}_0}{\sqrt{2}} \frac{\mathrm{v}_0^2}{4 \mathrm{~g}}
\end{aligned}$

</details>

---

### Q9. JEE Main 2025 (22 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

The position vectors of two 1 kg particles, (A) and (B), are given by
$\overrightarrow{\mathrm{r}}_{\mathrm{A}}=\left(\alpha_1 \mathrm{t}^2 \hat{i}+\alpha_2 \mathrm{t} \hat{j}+\alpha_3 \mathrm{t} \hat{k}\right) \mathrm{m}$ and $\overrightarrow{\mathrm{r}}_{\mathrm{B}}=\left(\beta_1 \mathrm{t} \hat{i}+\beta_2 \mathrm{t}^2 \hat{j}+\beta_3 \mathrm{t} \hat{k}\right) \mathrm{m}$, respectively; $\left(\alpha_1=1 \mathrm{~m} / \mathrm{s}^2, \alpha_2=3 \mathrm{n} \mathrm{m} / \mathrm{s}, \alpha_3=2 \mathrm{~m} / \mathrm{s}, \beta_1=2 \mathrm{~m} / \mathrm{s}, \beta_2=-1 \mathrm{~m} / \mathrm{s}^2, \beta_3=4 \mathrm{pm} / \mathrm{s}\right)$, where t is time, n and p are constants. At $t=1 \mathrm{~s},\left|\overrightarrow{V_A}\right|=\left|\vec{V}_B\right|$ and velocities $\vec{V}_A$ and $\vec{V}_B$ of the particles are orthogonal to each other. At $t=1 \mathrm{~s}$, the magnitude of angular momentum of particle (A) with respect to the position of particle (B) is $\sqrt{\mathrm{L}} \mathrm{kgm}^2 \mathrm{~s}^{-1}$. The value of L is _______ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **90**

**Detailed Solution:**

At $t=1$
$r_{A B}=-1 \hat{i}+(3 n+1) \hat{j}+(2-4 p) \hat{k}$

At $t=1$
$\begin{aligned}
& v_A=2 \hat{i}+3 n \hat{j}+2 \hat{k} \\
& v_B=2 \hat{i}-2 \hat{j}+4 p \hat{k} \\
& \vec{v}_A-\vec{v}_B=0, \quad 4-6 n+8 p=0
\end{aligned}$
$\begin{gathered}\left|v_A\right|=\left|v_B\right| \quad(3 n)^2+4=4+16 p^2 \\ 3 n=-4 p \\ 4+16 p=0 \\ p=-\frac{1}{4}, n=\frac{1}{3} \\ r_{A B}=-\hat{i}+2 \hat{j}+3 \hat{k} \\ v_A=2 \hat{i}+\hat{j}+2 \hat{k} \\ \therefore L=m\left|\vec{r}_{A B} \times \vec{v}_A\right|=90\end{gathered}$

</details>

---

### Q10. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A thin circular disc of mass $M$ and radius $R$ is rotating in a horizontal plane about an axis passing through its centre and perpendicular to its plane with angular velocity $\omega$. If another disc of same dimensions but of mass $\mathrm{M} / 2$ is placed gently on the first disc co-axially, then the new angular velocity of the system is :

**Options:**

- **(A)** $\frac{3}{2} \omega$
- **(B)** $\frac{5}{4} \omega$
- **(C)** $\frac{2}{3} \omega$
- **(D)** $\frac{4}{5} \omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{3} \omega$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{I}_1 \omega=\mathrm{I}_2 \omega_2 \\ & \frac{\mathrm{MR}^2}{2} \omega=\frac{3}{2}\left(\frac{\mathrm{MR}^2}{2}\right) \omega_2 \\ & \omega_2=\frac{2}{3} \omega\end{aligned}$

</details>

---

### Q11. JEE Main 2024 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

If the radius of earth is reduced to three-fourth of its present value without change in its mass then value of duration of the day of earth will be ______ hours 30 minutes.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **13**

**Detailed Solution:**

By conservation of angular momentum
$\begin{aligned}
& \mathrm{I}_1 \omega_1=\mathrm{I}_2 \omega_2 \\
& \left(\frac{2}{5} \mathrm{MR}^2\right) \frac{2 \pi}{\mathrm{T}_1}=\frac{2}{5} \mathrm{M}\left(\frac{3}{4} \mathrm{R}\right)^2 \frac{2 \pi}{\mathrm{T}_2} \\
& \frac{1}{\mathrm{~T}_1}=\frac{9}{16 \mathrm{~T}_2} \\
& \frac{1}{\mathrm{~T}_2}=\frac{9}{16} \times \mathrm{T}_1=\frac{9}{16} \times 24 \mathrm{hr}=\frac{27}{2} \mathrm{hr}=13 \mathrm{hr} 30 \mathrm{mins} .
\end{aligned}$

</details>

---

### Q12. JEE Main 2024 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

A body of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is projected with a speed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi></math> making an angle of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>45</mn><mi mathvariant="normal">o</mi></msup></math> with the ground. The angular momentum of the body about the point of projection, at the highest point is expressed as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>2</mn></msqrt><mi>m</mi><msup><mi>u</mi><mn>3</mn></msup></mrow><mrow><mi>X</mi><mi>g</mi></mrow></mfrac></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> is_______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/92651a04-5986-48fd-be9f-65e25f032e75.png" style="width: 300px; height: 108px;"/></p><p>Consider projection as shown in above diagram.</p><p>At the topmost point, velocity of the body will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mi>cos</mi><mn>45</mn><mo>°</mo></math>.</p><p>Therefore, we can write the required angular momentum as </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mfenced><mrow><mi>m</mi><msub><mi>u</mi><mi>H</mi></msub></mrow></mfenced><mo>×</mo><mi>H</mi><mspace linebreak="newline"></mspace><mo>=</mo><mfenced><mrow><mi>m</mi><mi>u</mi><mi>cos</mi><mi>θ</mi></mrow></mfenced><mfenced><mfrac><mrow><msup><mi>u</mi><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mi>θ</mi></mrow><mrow><mn>2</mn><mi>g</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>m</mi><msup><mi>u</mi><mn>3</mn></msup><mo>×</mo><mfrac><mn>1</mn><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt><mi>g</mi></mrow></mfrac><mspace linebreak="newline"></mspace><mo>⇒</mo><mi>X</mi><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q13. JEE Main 2024 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Consider a disc of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo> </mo><mi>kg</mi></math>, radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo> </mo><mi mathvariant="normal">m</mi></math>, rotating with angular velocity of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo> </mo><mi>rad</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> about an axis perpendicular to the plane of rotation. An identical disc is kept gently over the rotating disc along the same axis. The energy dissipated so that both the discs continue to rotate together without slipping is _________<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">J</mi></math>.</p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fd27f85d-47bc-4367-b361-e7a4a9662e25.png" style="width: 300px; height: 210px;"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **250**

**Detailed Solution:**

<p>Initial angular momentum, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>i</mi></msub><mo>=</mo><mi>I</mi><msub><mi>ω</mi><mi>i</mi></msub><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>·</mo><mi>ω</mi><mo>=</mo><mn>100</mn><mo> </mo><mi>kg</mi><mo> </mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Initial kinetic energy, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>i</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>·</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>·</mo><msup><mi>ω</mi><mn>2</mn></msup><mo>=</mo><mn>500</mn><mo> </mo><mi mathvariant="normal">J</mi></math></p><p>From conservation of angular momentum, we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>L</mi><mo>→</mo></mover><mi>i</mi></msub><mo>=</mo><msub><mover><mi>L</mi><mo>→</mo></mover><mi>f</mi></msub><mspace linebreak="newline"></mspace><mo>⇒</mo><mn>100</mn><mo>=</mo><mn>2</mn><mi>I</mi><msub><mi>ω</mi><mi>f</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>ω</mi><mi>f</mi></msub><mo>=</mo><mn>5</mn><mo> </mo><mi>rad</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>f</mi></msub><mo>=</mo><mn>2</mn><mo>×</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>·</mo><mfrac><mrow><mn>5</mn><mo>(</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>·</mo><mo>(</mo><mn>5</mn><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mn>250</mn><mo> </mo><mi mathvariant="normal">J</mi></math></p><p>Therefore, required energy loss <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Δ</mi><mi>E</mi><mo>=</mo><mn>250</mn><mo> </mo><mi mathvariant="normal">J</mi></math></p>

</details>

---

### Q14. JEE Main 2024 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

A body of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo> </mo><mi>kg</mi></math> moving with a uniform speed <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>2</mn></msqrt><mo> </mo><mi mathvariant="normal">m</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>-</mo><mi>Y</mi></math> plane along the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>4</mn></math>. The angular momentum of the particle about the origin will be _______<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>kg</mi><mo> </mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **60**

**Detailed Solution:**

<p>Equation of line given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>.</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>1</mn></msub></math> be the perpendicular distance of given line from origin.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><msqrt><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt></mfrac></mfenced><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi mathvariant="italic">L</mi><mo mathvariant="italic">→</mo></mover><mo>|</mo><mo>=</mo><mi>m</mi><mi>v</mi><msub><mi>d</mi><mn>1</mn></msub><mo>=</mo><mn>5</mn><mo>×</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mo>×</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo> </mo><mi>kg</mi><mo> </mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>60</mn><mo> </mo><mi>kg</mi><mo> </mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p>

</details>

---

### Q15. JEE Main 2023 (13 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>A solid sphere is rolling on a horizontal plane without slipping. If the ratio of angular momentum about axis of rotation of the sphere to the total energy of moving sphere is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>:</mo><mn>22</mn></math> then, the value of its angular speed will be<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_________rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>.</mo></math></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<blockquote><p>The angular momentum is given by </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><msub><mi>I</mi><mrow><mi>C</mi><mi>M</mi></mrow></msub><mi>&#969;</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mi>&#969;</mi></mrow><mn>5</mn></mfrac></math></p><p>The total kinetic energy is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>(</mo><mi>M</mi><msup><mi>v</mi><mn>2</mn></msup><mo>+</mo><mfrac><mrow><mn>2</mn><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><msup><mi>&#969;</mi><mn>2</mn></msup></mrow><mn>5</mn></mfrac><mo>)</mo></math></p><p>The ratio of angular momentum and kinetic energy is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>L</mi><mi>E</mi></mfrac><mo>=</mo><mfrac><mrow><msub><mi>I</mi><mrow><mi>C</mi><mi>M</mi></mrow></msub><mi>&#969;</mi></mrow><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>M</mi><msup><mi>v</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><msup><mi>&#969;</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mi>&#969;</mi></mrow><mrow><mfrac><mn>7</mn><mn>10</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><msup><mi>&#969;</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>&#960;</mi><mn>22</mn></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>7</mn></mfrac><mo>&#183;</mo><mfrac><mn>1</mn><mi>&#969;</mi></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#969;</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p></blockquote>

</details>

---

### Q16. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>A spherical shell of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>kg</mi></math> mass and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is rolling with angular speed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi></math> on horizontal plane (as shown in figure). The magnitude of angular momentum of the shell about the origin <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mn>3</mn></mfrac><msup><mi>R</mi><mn>2</mn></msup><mi>&#969;</mi></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> will be</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0eac515c-ef27-40a6-9811-97f3b6cae570-image.png" style="width: 180px; height: 124px;" /> </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0eac515c-ef27-40a6-9811-97f3b6cae570-image.png" style="width: 180px; height: 124px;" /></p><p>Angular momentum of a rotating and translating body is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>O</mi></msub><mo>=</mo><mi>m</mi><mi>v</mi><mi>R</mi><mo>+</mo><mi>I</mi><mi>&#969;</mi><mo>=</mo><mi>m</mi><mi>v</mi><mi>R</mi><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mi>&#969;</mi></math></p><p>For rolling, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mi>&#969;</mi><mi>R</mi></math></p><p>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>L</mi><mi>O</mi></msub><mo>=</mo><mi>m</mi><mi>&#969;</mi><msup><mi>R</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mi>m</mi><mi>&#969;</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p>Therefore, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>5</mn></math>.</p>

</details>

---

### Q17. JEE Main 2022 (28 Jun Shift 1)

*Type:* `numerical` | *Level:* `1`

The position vector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>kg</mi></math> object is <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> and its velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The magnitude of its angular momentum is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>x</mi></msqrt><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **91**

**Detailed Solution:**

<p>Angular momentum of a particle is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>P</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mi>m</mi><mover><mi>v</mi><mo>&#8594;</mo></mover></math> also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi>kg</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>9</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><mi mathvariant="normal">s</mi></math></p><p>The magnitude of the angular momentum will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mover><mi>L</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><msup><mn>9</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>91</mn></msqrt><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><mi mathvariant="normal">s</mi></math></p><p>Therefore, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>91</mn></math>.</p>

</details>

---

### Q18. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A thin circular ring of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is rotating with a constant angular velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> in a horizontal plane about an axis vertical to its plane and passing through the center of the ring. If two objects each of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> be attached gently to the opposite ends of a diameter of ring, the ring will then rotate with an angular velocity (in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>).

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>M</mi><mfenced><mrow><mi>M</mi><mo>+</mo><mi>m</mi></mrow></mfenced></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced><mrow><mi>M</mi><mo>+</mo><mn>2</mn><mi>m</mi></mrow></mfenced><mrow><mn>2</mn><mi>M</mi></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>M</mi></mrow><mfenced><mrow><mi>M</mi><mo>+</mo><mn>2</mn><mi>m</mi></mrow></mfenced></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mfenced><mrow><mi>M</mi><mo>+</mo><mn>2</mn><mi>m</mi></mrow></mfenced></mrow><mi>M</mi></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>M</mi></mrow><mfenced><mrow><mi>M</mi><mo>+</mo><mn>2</mn><mi>m</mi></mrow></mfenced></mfrac></math>**

**Detailed Solution:**

<p>As the masses are gently placed we can apply conservation of angular momentum.</p><p>Initial moment of Inertia <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p>Final moment of inertia <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mn>2</mn><mi>m</mi></mrow></mfenced><msup><mi>R</mi><mn>2</mn></msup></math></p><p>By conservation of angular momentum</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><msub><mi>&#969;</mi><mn>1</mn></msub><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub><msub><mi>&#969;</mi><mn>2</mn></msub></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>&#215;</mo><mn>2</mn><mo>=</mo><mfenced><mrow><mi>M</mi><mo>+</mo><mn>2</mn><mi>m</mi></mrow></mfenced><msup><mi>R</mi><mn>2</mn></msup><mo>&#215;</mo><msub><mi>&#969;</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>&#969;</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mi>M</mi></mrow><mrow><mi>M</mi><mo>+</mo><mn>2</mn><mi>m</mi></mrow></mfrac><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p>

</details>

---

### Q19. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Angular momentum of a single particle moving with constant speed along circular path :

**Options:**

- **(A)** remains same in magnitude but changes in the direction
- **(B)** remains same in magnitude and direction
- **(C)** is zero
- **(D)** changes in magnitude but remains same in the direction

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) remains same in magnitude and direction**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/21aa058b-df68-46ba-94ed-4f0cccddb901-f6aa0c30-3119-4458-b817-758d96f3f930-image.png" style="width: 250px; height: 217px;" />
The angular momentum is defined as the vector product of linear momentum and perpendicular distance, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mi>m</mi><mover><mi>v</mi><mo>&#8594;</mo></mover></math>, And direction will be upward &amp; remain constant.

</details>

---

### Q20. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two discs have moments of intertia <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub></math> about their respective axes perpendicular to the plane and passing through the centre. They are rotating with angular speeds, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#969;</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#969;</mi><mn>2</mn></msub></math> respectively and are brought into contact face to face with their axes of rotation coaxial. The loss in kinetic energy of the system in the process is given by:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mrow><mfenced><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub></mrow></mfenced></mfrac><msup><mfenced><mrow><msub><mi>&#969;</mi><mn>1</mn></msub><mo>-</mo><msub><mi>&#969;</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mfenced><mrow><msub><mi>&#969;</mi><mn>1</mn></msub><mo>-</mo><msub><mi>&#969;</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><mrow><mn>2</mn><mfenced><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub></mrow></mfenced></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mrow><mrow><mn>2</mn><mfenced><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub></mrow></mfenced></mrow></mfrac><msup><mfenced><mrow><msub><mi>&#969;</mi><mn>1</mn></msub><mo>-</mo><msub><mi>&#969;</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mfenced><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>-</mo><msub><mi>I</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><msub><mi>&#969;</mi><mn>1</mn></msub><msub><mi>&#969;</mi><mn>2</mn></msub></mrow><mrow><mn>2</mn><mfenced><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub></mrow></mfenced></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mrow><mrow><mn>2</mn><mfenced><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub></mrow></mfenced></mrow></mfrac><msup><mfenced><mrow><msub><mi>&#969;</mi><mn>1</mn></msub><mo>-</mo><msub><mi>&#969;</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup></math>**

**Detailed Solution:**

<p>Angular momentum conservation</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><msub><mi>&#969;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub><msub><mi>&#969;</mi><mn>2</mn></msub><mo>=</mo><mfenced><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub></mrow></mfenced><mi>&#969;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mfrac><mrow><msub><mi>I</mi><mn>1</mn></msub><msub><mi>&#969;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub><msub><mi>&#969;</mi><mn>2</mn></msub></mrow><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub></mrow></mfrac></math></p><p>Loss <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>I</mi><mn>1</mn></msub><msubsup><mi>&#969;</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>I</mi><mn>2</mn></msub><msubsup><mi>&#969;</mi><mn>2</mn><mn>2</mn></msubsup><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub></mrow></mfenced><msup><mi>&#969;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>I</mi><mn>1</mn></msub><msubsup><mi>&#969;</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>I</mi><mn>2</mn></msub><msubsup><mi>&#969;</mi><mn>2</mn><mn>2</mn></msubsup><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub></mrow></mfenced><msup><mfenced><mfrac><mrow><msub><mi>I</mi><mn>1</mn></msub><msub><mi>&#969;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub><msub><mi>&#969;</mi><mn>2</mn></msub></mrow><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub></mrow></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfrac><mrow><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mrow><mfenced><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub></mrow></mfenced></mfrac><msup><mfenced><mrow><msub><mi>&#969;</mi><mn>1</mn></msub><mo>-</mo><msub><mi>&#969;</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">E</mi><mi mathvariant="normal">i</mi></msub><mo>-</mo><msub><mi mathvariant="normal">E</mi><mi mathvariant="normal">f</mi></msub><mo>=</mo><mfrac><mrow><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub><msup><mfenced><mrow><msub><mi>&#969;</mi><mn>1</mn></msub><mo>-</mo><msub><mi>&#969;</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mn>2</mn><mfenced><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub></mrow></mfenced></mrow></mfrac></math></p>

</details>

---

### Q21. JEE Main 2021 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>A particle of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is moving in time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> on a trajectory given by, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>10</mn><mi>&#945;</mi><msup><mi>t</mi><mn>2</mn></msup><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mi>&#946;</mi><mfenced><mrow><mi>t</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></math></p><p>where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are dimensional constants.</p><p>The angular momentum of the particle becomes the same as it was for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn></math> at time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo></math>_____ seconds.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>10</mn><mi>&#945;</mi><msup><mi>t</mi><mn>2</mn></msup><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mi>&#946;</mi><mfenced><mrow><mi>t</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>20</mn><mi>&#945;</mi><mo>+</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mi>&#946;</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>m</mi><mfenced><mrow><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>v</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>m</mi><mfenced close="]" open="["><mrow><mn>10</mn><mi>&#945;</mi><msup><mi>t</mi><mn>2</mn></msup><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mi>&#946;</mi><mfenced><mrow><mi>t</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><mfenced close="]" open="["><mrow><mn>20</mn><mi>&#945;</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mi>&#946;</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>m</mi><mfenced open="[" close="]"><mrow><mn>50</mn><mi>&#945;</mi><mi>&#946;</mi><msup><mi>t</mi><mn>2</mn></msup><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>-</mo><mn>100</mn><mi>&#945;</mi><mi>&#946;</mi><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>t</mi></mrow></mfenced><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mover><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mn>0</mn><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mi>&#945;</mi><mi>&#946;</mi><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>100</mn><mi>&#945;</mi><mi>&#946;</mi><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>t</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>-</mo><mn>2</mn><mfenced><mrow><mi>t</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi>sec</mi></math></p>

</details>

---

### Q22. JEE Main 2021 (17 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>A mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> hangs on a massless rod of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> which rotates at a constant angular frequency. The mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> moves with steady speed in a circular path of constant radius. Assume that the system is in steady circular motion with constant angular velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&omega;</mi><mo>.</mo></math> The angular momentum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> about point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>A</mi></msub></math> which lies in the positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> direction and the angular momentum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>B</mi></msub><mo>.</mo></math> The correct statement for this system is:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/44c0d896-bab0-400b-a2ce-1858f21200f0-image.png" style="width: 148px; height: 246px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>A</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>B</mi></msub></math> are both constant in magnitude and direction
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>B</mi></msub></math> is constant in direction with varying magnitude
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>B</mi></msub></math> is constant, both in magnitude and direction
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>A</mi></msub></math> is constant, both in magnitude and direction

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>A</mi></msub></math> is constant, both in magnitude and direction**

**Detailed Solution:**

<p>We know, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>m</mi><mo>(</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>)</mo></math></p><p>Now with respect to<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>A</mi><mo>,</mo></math> we always get direction
of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>L</mi><mo>&#8594;</mo></mover></math> along <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>v</mi><mi>e</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math>-axis and also constant magnitude as mvr. But with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>,</mo></math> we get constant magnitude but continuously changing direction.</p>

</details>

---

### Q23. JEE Main 2021 (16 Mar Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>A ball of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>kg</mi></math> moving with a velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><msqrt><mn>3</mn></msqrt><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>-axis, hits another ball of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi>kg</mi></math> which is at rest. After the collision, the first ball comes to rest and the second one disintegrates into two equal pieces. One of the pieces starts moving along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math>-axis at a speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The second piece starts moving at a speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> at an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> (degree) with respect to the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>-axis. The configuration of pieces after the collision is shown in the figure. The value of $\theta$ to the nearest integer is _________.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0a8aacf2-ca23-46e9-a541-464f20f935e1-image.png" style="width: 248px; height: 228px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **30**

**Detailed Solution:**

<p>Before Collision </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7b12a4e8-050b-4b7b-a04e-c111b1008627-image.png" style="width: 225px; height: 83px;" /></p><p>After Collision </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/90ff3124-edc4-4043-8c37-00cdf563f5a2-image.png" style="width: 269px; height: 163px;" /></p><p>From conservation of momentum along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> axis;</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>P</mi><mo>&#8594;</mo></mover><mi>i</mi></msub><mo>=</mo><msub><mover><mi>P</mi><mo>&#8594;</mo></mover><mi>f</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#215;</mo><mn>10</mn><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>200</mn><mi>cos</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mn>30</mn><mo>&#176;</mo></math></p>

</details>

---

### Q24. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The maximum and minimum distances of a comet from the Sun are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mn>12</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>.</mo><mn>0</mn><mo>&#215;</mo><msup><mn>10</mn><mn>10</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> respectively. If the speed of the comet at the nearest point is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mn>4</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, the speed at the farthest point is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>0</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>0</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<p>By angular momentum conservation :</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><msub><mi>v</mi><mn>1</mn></msub><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><mi>m</mi><msub><mi>v</mi><mn>2</mn></msub><msub><mi>r</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mn>48</mn><mo>&#215;</mo><msup><mn>10</mn><mn>14</mn></msup></mrow><mrow><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mn>12</mn></msup></mrow></mfrac><mo>=</mo><mn>3000</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>.</p>

</details>

---

### Q25. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>A sphere of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> rolls along a horizontal plane with constant speed <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mn>0</mn></msub></math>. It encounters an inclined plane at angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> and climbs upward. Assuming that it rolls without slipping, how far up the sphere will travel?</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/112eafc3-3a82-4385-8caf-1940fab39a76-image.png" style="width: 270px; height: 164px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>5</mn></mfrac><mfrac><msubsup><mi>v</mi><mn>0</mn><mn>2</mn></msubsup><mrow><mo>&#160;</mo><mi>g</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>7</mn><msubsup><mi>v</mi><mn>0</mn><mn>2</mn></msubsup></mrow><mrow><mn>10</mn><mo>&#160;</mo><mi>g</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msubsup><mi>v</mi><mn>0</mn><mn>2</mn></msubsup><mrow><mn>5</mn><mi>g</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msubsup><mi>v</mi><mn>0</mn><mn>2</mn></msubsup><mrow><mn>2</mn><mi>g</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>7</mn><msubsup><mi>v</mi><mn>0</mn><mn>2</mn></msubsup></mrow><mrow><mn>10</mn><mo>&#160;</mo><mi>g</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0a57a0b0-2a10-4f45-bd47-20d084ab1674-image.png" style="width: 300px; height: 179px;" /></p><p>From energy conservation
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mgh</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mi>mv</mi><mn>0</mn><mn>2</mn></msubsup><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>I&#969;</mi><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>mgh</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mi>mv</mi><mn>0</mn><mn>2</mn></msubsup><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><msup><mi>ma</mi><mn>2</mn></msup><mo>&#215;</mo><mfrac><msubsup><mi mathvariant="normal">v</mi><mn>0</mn><mn>2</mn></msubsup><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>gh</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mi mathvariant="normal">v</mi><mn>0</mn><mn>2</mn></msubsup><mo>+</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><msubsup><mi mathvariant="normal">v</mi><mn>0</mn><mn>2</mn></msubsup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>gh</mi><mo>=</mo><mfrac><mn>7</mn><mn>10</mn></mfrac><msubsup><mi mathvariant="normal">v</mi><mn>0</mn><mn>2</mn></msubsup></math></p><p>From triangle, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi mathvariant="normal">h</mi><mi>l</mi></mfrac></math>
Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">h</mi><mo>=</mo><mi>l</mi><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#952;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>l</mi><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#952;</mi><mo>=</mo><mfrac><mn>7</mn><mn>10</mn></mfrac><mfrac><msubsup><mi mathvariant="normal">v</mi><mn>0</mn><mn>2</mn></msubsup><mrow><mo>&#160;</mo><mi mathvariant="normal">g</mi></mrow></mfrac></math>
Thus, the sphere will travel distance, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mfrac><mn>7</mn><mn>10</mn></mfrac><mfrac><msup><msub><mi mathvariant="normal">v</mi><mn>0</mn></msub><mn>2</mn></msup><mrow><mo>&#160;</mo><mi mathvariant="normal">g</mi><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi></mrow></mfrac></math>.</p>

</details>

---

### Q26. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Four point masses, each of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi></math>, are fixed at the corners of a square of side I. The square is rotating with angular frequency <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>,</mo></math> about an axis passing through one of the corners of the square and parallel to tis diagonal, as shown in the figure. The angular momentum of the square about the axis is</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cd5726f9-83e6-4534-b914-9bc74c86b000-image.png" style="width: 239px; height: 230px;" />  </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi><msup><mi>&#8467;</mi><mn>2</mn></msup><mi>&#969;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi mathvariant="normal">m</mi><msup><mi>&#8467;</mi><mn>2</mn></msup><mi>&#969;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi mathvariant="normal">m</mi><msup><mi>&#8467;</mi><mn>2</mn></msup><mi>&#969;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">m</mi><msup><mi>&#8467;</mi><mn>2</mn></msup><mi>&#969;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi mathvariant="normal">m</mi><msup><mi>&#8467;</mi><mn>2</mn></msup><mi>&#969;</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/70b2feee-8382-48cf-9a3a-e3aa53694e74-image.png" style="width: 216px; height: 220px;" />  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>=</mo><mi>M</mi><msup><mfenced><mfrac><mi mathvariant="script">l</mi><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mi>m</mi><mo>(</mo><msqrt><mi mathvariant="script">l</mi></msqrt><mi>e</mi><msup><mo>)</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi mathvariant="normal">m</mi><msup><mi>&#8467;</mi><mn>2</mn></msup><mi>&#969;</mi></math></p><p> </p>

</details>

---

### Q27. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A wheel is rotating freely with an angular speed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi></math> on a shaft. The moment of inertia of the wheel is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> and the moment of inertia of the shaft is negligible. Another wheel of moment of inertia <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>I</mi></math> initially at rest is suddenly coupled to the same shaft. The resultant fractional loss in the kinetic energy of the system is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>From angular momentum conservation
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>&#969;</mi><mo>+</mo><mn>0</mn><mo>=</mo><mi>I</mi><msub><mi>&#969;</mi><mi mathvariant="normal">C</mi></msub><mo>+</mo><mn>3</mn><mi>I</mi><msub><mi>&#969;</mi><mi mathvariant="normal">C</mi></msub></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mi>c</mi><mo>=</mo><mfrac><mi>&#969;</mi><mn>4</mn></mfrac></math></p><p>Loss of kinetic energy <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>I</mi><msup><mi>&#969;</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>(</mo><mi>I</mi><mo>+</mo><mn>3</mn><mi>I</mi><mo>)</mo><msup><mfenced><mfrac><mi>&#969;</mi><mn>4</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>I</mi><msup><mi>&#969;</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>I</mi><mfrac><msup><mi>&#969;</mi><mn>2</mn></msup><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>8</mn></mfrac><mi>I</mi><msup><mi>&#969;</mi><mn>2</mn></msup></math></p><p>Fractional loss <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p>

</details>

---

### Q28. JEE Main 2020 (04 Sep Shift 1)

*Type:* `numerical` | *Level:* `3`

A circular disc of mass <math><mtext>M</mtext></math> and radius <math><mtext>R</mtext></math> is rotating about its axis with angular speed <math><mrow><msub><mi>&#969;</mi><mn>1</mn></msub></mrow></math>. If another stationary disc having radius <math><mrow><mfrac><mtext>R</mtext><mn>2</mn></mfrac></mrow></math> and same mass <math><mtext>M</mtext></math> is dropped co-axially on to the rotating disc. Gradually both discs attain constant angular speed <math><mrow><msub><mi>&#969;</mi><mn>2</mn></msub></mrow></math>. The energy lost in the process is <math><mrow><mtext>p%</mtext></mrow></math> of the initial energy. Value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">p</mi></math> is ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **20**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9dcc6c60-7ca4-4e1a-894f-c1416b348768-image.png" style="width: 351px; height: 128px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">I</mi><mn>1</mn></msub><msub><mi mathvariant="normal">&#969;</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub><msub><mi mathvariant="normal">&#969;</mi><mn>2</mn></msub><mo>=</mo><mfenced><mrow><msub><mi mathvariant="normal">I</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub></mrow></mfenced><mo>&#215;</mo><msub><mi mathvariant="normal">&#969;</mi><mi mathvariant="normal">f</mi></msub></math></p><p> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>MR</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>&#215;</mo><mi mathvariant="normal">&#969;</mi><mo>+</mo><mn>0</mn><mfenced><mrow><mfrac><msup><mi>MR</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>MR</mi><mn>2</mn></msup><mn>8</mn></mfrac></mrow></mfenced><mfrac><mn>16</mn><mn>25</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#969;</mi><mi mathvariant="normal">f</mi></msub><mo>=</mo><mfrac><mn>4</mn><mn>5</mn></mfrac><mi mathvariant="normal">&#969;</mi></math></p><p>Final <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">K</mi><mo>.</mo><mi mathvariant="normal">E</mi></math>., <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">f</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfrac><msup><mi>MR</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>MR</mi><mn>2</mn></msup><mn>8</mn></mfrac></mrow></mfenced><mfrac><mn>16</mn><mn>25</mn></mfrac><msup><mi mathvariant="normal">&#969;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">f</mi></msub><mo>=</mo><mfrac><mrow><msup><mi>MR</mi><mn>2</mn></msup><msup><mi mathvariant="normal">&#969;</mi><mn>2</mn></msup></mrow><mn>5</mn></mfrac></math> ; <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">i</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mfrac><msup><mi>MR</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><msup><mi mathvariant="normal">&#969;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msup><mi>MR</mi><mn>2</mn></msup><msup><mi mathvariant="normal">&#969;</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"></math>Percentage loss in kinetic energy <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>%</mo><mtext>&#8201;</mtext><mi>loss</mi><mo>=</mo><mfrac><mrow><mfrac><mrow><msup><mi>MR</mi><mn>2</mn></msup><msup><mi mathvariant="normal">&#969;</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>&#8722;</mo><mfrac><mrow><msup><mi>MR</mi><mn>2</mn></msup><msup><mi mathvariant="normal">&#969;</mi><mn>2</mn></msup></mrow><mn>5</mn></mfrac></mrow><mfrac><mrow><msup><mi>MR</mi><mn>2</mn></msup><msup><mi mathvariant="normal">&#969;</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></mfrac><mo>&#215;</mo><mn>100</mn><mo>=</mo><mn>20</mn><mo>%</mo></math></p>

</details>

---

### Q29. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>A block of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi>kg</mi></math> slides with velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">v</mi><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> on a frictionless horizontal surface and collides with a uniform vertical rod and sticks to it as shown. The rod is pivoted about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">O</mi></math> and swings as a result of the collision making angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> before momentarily coming to rest. if the rod has mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>kg</mi><mo>,</mo></math> and length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#8467;</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>,</mo></math> the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> is approximately<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open=""><mrow><mo>(</mo><mi>take</mi><mo>&#160;</mo><mi mathvariant="normal">g</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8a20654d-618e-4fbf-b5f5-8ed1da4b332b-image.png" style="width: 232px; height: 149px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>63</mn><mo>&#176;</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>55</mn><mo>&#176;</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>69</mn><mo>&#176;</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn><mo>&#176;</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>63</mn><mo>&#176;</mo></math>**

**Detailed Solution:**

<p>Angular momentum</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mv</mi><mi mathvariant="script">l</mi><mo>=</mo><mfenced><mrow><mi mathvariant="normal">m</mi><msup><mi mathvariant="script">l</mi><mn>2</mn></msup><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">m</mi><msup><mi mathvariant="script">l</mi><mn>2</mn></msup></mrow><mn>3</mn></mfrac></mrow></mfenced><mi mathvariant="normal">&#969;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mv</mi><mi mathvariant="script">l</mi><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mi mathvariant="normal">m</mi><msup><mi mathvariant="script">l</mi><mn>2</mn></msup><mi mathvariant="normal">&#969;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#969;</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">v</mi></mrow><mrow><mn>5</mn><mi mathvariant="script">l</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>I&#969;</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>mg</mi><mfrac><mi mathvariant="script">l</mi><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mo>&#160;</mo><mi mathvariant="normal">&#952;</mi></mrow></mfenced><mo>+</mo><mi>mg</mi><mi mathvariant="script">l</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mo>&#160;</mo><mi mathvariant="normal">&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfrac><mn>5</mn><mn>3</mn></mfrac><mi mathvariant="normal">m</mi><msup><mi mathvariant="script">l</mi><mn>2</mn></msup></mrow></mfenced><mfrac><mrow><mn>9</mn><msup><mi mathvariant="normal">v</mi><mn>2</mn></msup></mrow><mrow><mn>25</mn><msup><mi mathvariant="script">l</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>2</mn><mi>mg</mi><mi mathvariant="script">l</mi><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mo>&#160;</mo><mi mathvariant="normal">&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mrow><mn>5</mn><mo>&#215;</mo><mn>2</mn></mrow></mfrac><msup><mi>mv</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>mg</mi><mi mathvariant="script">l</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>cos&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>10</mn></mfrac><mo>&#215;</mo><mfrac><mn>36</mn><mrow><mn>2</mn><mo>&#215;</mo><mn>10</mn></mrow></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mi>cos</mi><mo>&#160;</mo><mi mathvariant="normal">&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfrac><mn>27</mn><mn>50</mn></mfrac><mo>=</mo><mi>cos</mi><mo>&#160;</mo><mi mathvariant="normal">&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mo>&#160;</mo><mi mathvariant="normal">&#952;</mi><mo>=</mo><mfrac><mn>23</mn><mn>50</mn></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>46</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#952;</mi><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>0</mn><mo>.</mo><mn>46</mn></mrow></mfenced><mo>=</mo><mn>63</mn><mo>&#176;</mo></math></p>

</details>

---

### Q30. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A person of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is sitting on a swing of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> and swinging with and an angular amplitude <math><msub><mrow><mi mathvariant="normal">&#952;</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>.</mo></math> If the person stands up when the swing passes through its lowest point, the work done by him, assuming that his centre of mass moves by a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mi>l</mi><mo>&#60;</mo><mo>&#60;</mo><mi>L</mi></mrow></mfenced><mo>,</mo></math> is close to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>g</mi><mi>l</mi><mi mathvariant="normal">&#160;</mi><mo>(</mo><mn>1</mn><mo>-</mo><msubsup><mi mathvariant="normal">&#952;</mi><mn>0</mn><mn>2</mn></msubsup><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>g</mi><mi>l</mi><mo>(</mo><mn>1</mn><mo>+</mo><mfrac><msubsup><mi mathvariant="normal">&#952;</mi><mn>0</mn><mn>2</mn></msubsup><mn>2</mn></mfrac><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>g</mi><mi>l</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>g</mi><mi>l</mi><mo>(</mo><mn>1</mn><mo>+</mo><msubsup><mi mathvariant="normal">&#952;</mi><mn>0</mn><mn>2</mn></msubsup><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>g</mi><mi>l</mi><mo>(</mo><mn>1</mn><mo>+</mo><msubsup><mi mathvariant="normal">&#952;</mi><mn>0</mn><mn>2</mn></msubsup><mo>)</mo></math>**

**Detailed Solution:**

From angular momentum conservation
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mi>M</mi><msub><mi>V</mi><mn>0</mn></msub><mi>L</mi><mo>=</mo><mi>M</mi><mi>V</mi><mo>(</mo><mi>L</mi><mo>-</mo><mi>l</mi><mo>)</mo></mtd></mtr><mtr><mtd><mi>V</mi><mo>=</mo><msub><mi>V</mi><mn>0</mn></msub><mfenced separators="|"><mfrac><mi>L</mi><mrow><mi>L</mi><mo>-</mo><mi>l</mi></mrow></mfrac></mfenced></mtd></mtr></mtable></math>
Now
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>W</mi><mo>=</mo><mi>M</mi><mi>g</mi><mi>l</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>M</mi><mfenced open="[" close="]" separators="|"><mrow><msup><msub><mi>V</mi><mn>0</mn></msub><mn>2</mn></msup><msup><mfenced separators="|"><mfrac><mi>L</mi><mrow><mi>L</mi><mo>-</mo><mi>l</mi></mrow></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><msup><msub><mi>V</mi><mn>0</mn></msub><mn>2</mn></msup></mrow></mfenced></math>
Since <math><mi>l</mi><mo>&#8810;</mo><mi>L</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mi>W</mi><mo>=</mo><mi>M</mi><mi>g</mi><mi>l</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>M</mi><mfenced open="[" close="]" separators="|"><mrow><msup><msub><mi>V</mi><mn>0</mn></msub><mn>2</mn></msup><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mi>l</mi><mi>L</mi></mfrac></mrow></mfenced><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><msup><msub><mi>V</mi><mn>0</mn></msub><mn>2</mn></msup></mrow></mfenced></mtd></mtr><mtr><mtd><mo mathvariant="italic">=</mo><mi>M</mi><mi>g</mi><mi>l</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>M</mi><mfenced open="[" close="]" separators="|"><mrow><msup><msub><mi>V</mi><mn>0</mn></msub><mn>2</mn></msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mfrac><mi>l</mi><mi>L</mi></mfrac></mrow></mfenced><mo>-</mo><msup><msub><mi mathvariant="normal">V</mi><mn>0</mn></msub><mn>2</mn></msup></mrow></mfenced></mtd></mtr><mtr><mtd><mo>=</mo><mi>M</mi><mi>g</mi><mi>l</mi><mo>+</mo><mi>M</mi><mfenced open="[" close="]" separators="|"><mrow><msup><msub><mi>V</mi><mn>0</mn></msub><mn>2</mn></msup><mfenced separators="|"><mfrac><mi>l</mi><mi>L</mi></mfrac></mfenced></mrow></mfenced></mtd></mtr></mtable></math>
From SHM
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>0</mn></msub><mo>=</mo><mi mathvariant="normal">&#969;</mi><mi mathvariant="normal">A</mi><mo>=</mo><msqrt><mfrac><mi mathvariant="italic">g</mi><mi mathvariant="italic">L</mi></mfrac></msqrt><mo>&#215;</mo><mi>L</mi><msub><mi mathvariant="normal">&#952;</mi><mn>0</mn></msub><mo>=</mo><msqrt><mi>g</mi><mi>L</mi></msqrt><msub><mi mathvariant="normal">&#952;</mi><mn>0</mn></msub></math>
Using this
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mi>W</mi><mo>=</mo><mi>M</mi><mi>g</mi><mi>l</mi><mo>+</mo><mi>M</mi><mfenced open="[" close="]" separators="|"><mrow><mi>g</mi><mi>L</mi><mo>&#215;</mo><msup><msub><mi mathvariant="normal">&#952;</mi><mn>0</mn></msub><mn>2</mn></msup><mo>&#215;</mo><mfenced separators="|"><mfrac><mi mathvariant="italic">l</mi><mi mathvariant="italic">L</mi></mfrac></mfenced></mrow></mfenced></mtd></mtr><mtr><mtd><mi>W</mi><mo>=</mo><mi>M</mi><mi>g</mi><mi>l</mi><mfenced open="[" close="]" separators="|"><mrow><mn>1</mn><mo>+</mo><msup><msub><mi mathvariant="normal">&#952;</mi><mn>0</mn></msub><mn>2</mn></msup></mrow></mfenced></mtd></mtr></mtable></math>

</details>

---

### Q31. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The time dependence of the position of a particle of mass <math><mi mathvariant="normal">m</mi><mo>=</mo><mn>2</mn></math> is given by <math><mi>&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">r</mi><mi mathvariant="normal">&#160;</mi></mrow><mo>&#8594;</mo></mover><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mi mathvariant="normal">t</mi><mi mathvariant="normal">&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>3</mn><msup><mrow><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn></mrow></msup><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover></math> . Its angular momentum, with respect to the origin, at time <math><mi mathvariant="normal">t</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#160;</mi></math> is:

**Options:**

- **(A)** <math><mn>36</mn><mi mathvariant="normal"> </mi><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></math>
- **(B)** <math><mn>48</mn><mi mathvariant="normal"> </mi><mfenced separators="|"><mrow><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover></mrow></mfenced></math>
- **(C)** <math><mo>-</mo><mn>48</mn><mi mathvariant="normal"> </mi><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></math>
- **(D)** <math><mo>-</mo><mn>34</mn><mi mathvariant="normal"> </mi><mfenced separators="|"><mrow><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mo>-</mo><mn>48</mn><mi mathvariant="normal"> </mi><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></math>**

**Detailed Solution:**

<math><mover accent="true"><mrow><mi mathvariant="normal">r</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mi mathvariant="normal">t</mi><mtext>&#8201;</mtext><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>3</mn><msup><mrow><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover></math>
<math><mover accent="true"><mrow><mi mathvariant="normal">v</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>6</mn><mi mathvariant="normal">t</mi><mi mathvariant="normal">&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover></math>
Momentum <math><mover accent="true"><mrow><mi mathvariant="normal">p</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi mathvariant="normal">m</mi><mover accent="true"><mrow><mi mathvariant="normal">v</mi></mrow><mo>&#8594;</mo></mover></math>
<math><mo>=</mo><mn>4</mn><mi mathvariant="normal">&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>12</mn><mi mathvariant="normal">t</mi><mi mathvariant="normal">&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover></math>
<math><mo>&#8756;</mo></math> angular momentum <math><mover accent="true"><mrow><mi mathvariant="normal">L</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mrow><mi mathvariant="normal">r</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi mathvariant="normal">p</mi></mrow><mo>&#8594;</mo></mover></math>
<math><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mi mathvariant="normal">t</mi><mi mathvariant="normal">&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>3</mn><msup><mrow><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><mfenced separators="|"><mrow><mn>4</mn><mi mathvariant="normal">&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>12</mn><mi mathvariant="normal">t</mi><mi mathvariant="normal">&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover></mrow></mfenced></math>
<math><mo>=</mo><mo>-</mo><mn>24</mn><msup><mrow><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>12</mn><msup><mrow><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></math>
<math><mo>=</mo><mo>-</mo><mn>12</mn><msup><mrow><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></math>
At time <math><mi mathvariant="normal">t</mi><mo>=</mo><mn>2</mn></math>
<math><mover accent="true"><mrow><mi mathvariant="normal">L</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>48</mn><mi mathvariant="normal">&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></math>

</details>

---

### Q32. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Two coaxial discs, having moments of inertia <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>1</mn></msub><mn>2</mn></mfrac></math> , are rotating with respective angular velocities <math><msub><mrow><mi mathvariant="normal">&#969;</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><mi>&#160;</mi><mfrac><mrow><msub><mrow><mi mathvariant="normal">&#969;</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><mn>2</mn></mrow></mfrac></math> , about their common axis. They are brought in contact with each other and thereafter they rotate with a common angular velocity. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>f</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>i</mi></msub></math> are the final and initial total energies, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msub><mi>E</mi><mi>f</mi></msub><mo>-</mo><msub><mi>E</mi><mi mathvariant="italic">i</mi></msub></mrow></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>I</mi><mn>1</mn></msub><msubsup><mi mathvariant="normal">&#969;</mi><mn>1</mn><mn>2</mn></msubsup></mrow><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>8</mn></mfrac><msub><mi>I</mi><mn>1</mn></msub><msubsup><mi mathvariant="normal">&#969;</mi><mn>1</mn><mn>2</mn></msubsup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mrow><msub><mi>I</mi><mn>1</mn></msub><msubsup><mi mathvariant="normal">&#969;</mi><mn>1</mn><mn>2</mn></msubsup></mrow><mn>12</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mrow><msub><mi>I</mi><mn>1</mn></msub><msubsup><mi mathvariant="normal">&#969;</mi><mn>1</mn><mn>2</mn></msubsup></mrow><mn>24</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mrow><msub><mi>I</mi><mn>1</mn></msub><msubsup><mi mathvariant="normal">&#969;</mi><mn>1</mn><mn>2</mn></msubsup></mrow><mn>24</mn></mfrac></math>**

**Detailed Solution:**

As external torque is zero, angular momentum remains conserved.
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><msub><mi mathvariant="normal">&#969;</mi><mn>1</mn></msub><mo>+</mo><mfrac><msub><mi>I</mi><mn>1</mn></msub><mn>2</mn></mfrac><mfrac><msub><mi mathvariant="normal">&#969;</mi><mn>1</mn></msub><mn>2</mn></mfrac><mo>=</mo><mfenced separators="|"><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><mfrac><msub><mi>I</mi><mn>1</mn></msub><mn>2</mn></mfrac></mrow></mfenced><mi mathvariant="normal">&#969;</mi></math>
<math><mo>&#8756;</mo></math> Common angular velocity <math><mi mathvariant="normal">&#969;</mi><mo>=</mo><mfrac><mrow><mn>5</mn><msub><mrow><mi mathvariant="normal">&#969;</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><mn>6</mn></mrow></mfrac></math>
<math><mo>&#8756;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>f</mi></msub><mo>-</mo><msub><mi>E</mi><mi>i</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfenced separators="|"><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><mfrac><msub><mi>I</mi><mn>1</mn></msub><mn>2</mn></mfrac></mrow></mfenced><msup><mi mathvariant="normal">&#969;</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><msub><mi>I</mi><mn>1</mn></msub><msub><mi mathvariant="normal">&#969;</mi><mn>1</mn></msub><msup><mi mathvariant="normal">&#160;</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><msub><mi>I</mi><mi mathvariant="normal">l</mi></msub><mn>2</mn></mfrac><msup><mfenced separators="|"><mfrac><msub><mi mathvariant="normal">&#969;</mi><mn>1</mn></msub><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mrow><mn>3</mn><msub><mi>I</mi><mn>1</mn></msub></mrow><mn>2</mn></mfrac><msup><mfenced separators="|"><mrow><mfrac><mn>5</mn><mn>6</mn></mfrac><msub><mi mathvariant="normal">&#969;</mi><mn>1</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mfrac><mn>9</mn><mn>16</mn></mfrac><msub><mi>I</mi><mn>1</mn></msub><msubsup><mi mathvariant="normal">&#969;</mi><mn>1</mn><mn>2</mn></msubsup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>75</mn><mtext mathvariant="italic">&#8201;</mtext><msub><mi>I</mi><mn>1</mn></msub><msubsup><mi mathvariant="normal">&#969;</mi><mn>1</mn><mn>2</mn></msubsup><mo>-</mo><mn>81</mn><mtext>&#8201;</mtext><msub><mi>I</mi><mn>1</mn></msub><msubsup><mi mathvariant="normal">&#969;</mi><mn>1</mn><mn>2</mn></msubsup></mrow><mn>144</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mrow><mn>6</mn><msub><mi>I</mi><mn>1</mn></msub><msubsup><mi mathvariant="normal">&#969;</mi><mn>1</mn><mn>2</mn></msubsup></mrow><mn>144</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mrow><msub><mi>I</mi><mn>1</mn></msub><msubsup><mi mathvariant="normal">&#969;</mi><mn>1</mn><mn>2</mn></msubsup></mrow><mn>24</mn></mfrac></math>

</details>

---

### Q33. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A thin smooth rod of length <math><mi mathvariant="normal">L</mi></math> and mass <math><mi mathvariant="normal">M</mi></math> is rotating freely with angular speed <math><msub><mrow><mi mathvariant="normal">&#969;</mi></mrow><mrow><mn>0</mn></mrow></msub></math> about an axis perpendicular to the rod and passing through center. Two beads of mass <math><mi mathvariant="normal">m</mi></math> and negligible size are at the center of the rod initially. The beads of mass <math><mi mathvariant="normal">m</mi></math> and negligible size are at the center of the rod initially. The beads are free to slide along the rod. The angular speed of the system, when the beads reach the opposite ends of the rod, will be:

**Options:**

- **(A)** <math><mfrac><mrow><mi mathvariant="normal">M</mi><mtext> </mtext><msub><mrow><mi mathvariant="normal">ω</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi mathvariant="normal">M</mi><mo>+</mo><mn>3</mn><mi mathvariant="normal">m</mi></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi mathvariant="normal">M</mi><mtext> </mtext><msub><mrow><mi mathvariant="normal">ω</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi mathvariant="normal">M</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">m</mi></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi mathvariant="normal">M</mi><mtext> </mtext><msub><mrow><mi mathvariant="normal">ω</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi mathvariant="normal">M</mi><mo>+</mo><mn>6</mn><mi mathvariant="normal">m</mi></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi mathvariant="normal">M</mi><mtext> </mtext><msub><mrow><mi mathvariant="normal">ω</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi mathvariant="normal">M</mi><mo>+</mo><mi mathvariant="normal">m</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mi mathvariant="normal">M</mi><mtext> </mtext><msub><mrow><mi mathvariant="normal">ω</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi mathvariant="normal">M</mi><mo>+</mo><mn>6</mn><mi mathvariant="normal">m</mi></mrow></mfrac></math>**

**Detailed Solution:**

From conservation of angular momentum. 
<math><mfrac><mrow><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac><msub><mrow><mi mathvariant="normal">ω</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mfenced open="[" close="]" separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac><mo>+</mo><mi mathvariant="normal">m</mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi mathvariant="normal">m</mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mi mathvariant="normal">ω</mi><mi mathvariant="normal">'</mi></math>  
<math><mfrac><mrow><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac><msub><mrow><mi mathvariant="normal">ω</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi mathvariant="normal">m</mi><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mi mathvariant="normal">ω</mi><mi mathvariant="normal">'</mi></math>  
<math><mi mathvariant="normal">ω</mi><mi mathvariant="normal">'</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">M</mi><msub><mrow><mi mathvariant="normal">ω</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi mathvariant="normal">M</mi><mo>+</mo><mn>6</mn><mi mathvariant="normal">m</mi></mrow></mfrac></math>

</details>

---

### Q34. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A rectangular solid box of length <math><mn>0.3</mn><mi>&#160;</mi><mi mathvariant="normal">m</mi></math> is held horizontally, with one of its sides on the edge of a platform of height <math><mn>5</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi></math> . When released, it slips off the table in a very short time <math><mi mathvariant="normal">&#964;</mi><mo>=</mo><mn>0.01</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">s</mi></math> , remaining essentially horizontal. The angle by which it would rotate when it hits the ground will be (in radians) close to:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c20799a3-c7e5-45e0-98d1-fb33bcf2a026-image5.png" />

**Options:**

- **(A)** <math><mn>0.5</mn></math>
- **(B)** <math><mn>0.3</mn></math>
- **(C)** <math><mn>0.02</mn></math>
- **(D)** <math><mn>0.28</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>0.5</mn></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a4671cad-65aa-488e-8dba-e8456ef5a835-image6.png"> 
Angular impulse = change in angular momentum 
<math><mi>τ</mi><mi>Δ</mi><mi>t</mi><mo>=</mo><mi>Δ</mi><mi>L</mi></math>  
<math><mi>m</mi><mi>g</mi><mfrac><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>×</mo><mn>0.01</mn><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac><mi>ω</mi></math>  
<math><mi>ω</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>g</mi><mo>×</mo><mn>0.01</mn></mrow><mrow><mn>2</mn><mi>l</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mo>×</mo><mn>10</mn><mo>×</mo><mn>0.01</mn></mrow><mrow><mn>2</mn><mo>×</mo><mn>0.3</mn></mrow></mfrac><mo>=</mo><mn>0.5</mn><mtext> </mtext><mrow><mrow><mi mathvariant="normal">r</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">d</mi></mrow><mo>/</mo><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow></mrow></math>  
Time taken by rod to hit the ground = <math><msqrt><mfrac><mrow><mn>2</mn><mi>h</mi></mrow><mrow><mi>g</mi></mrow></mfrac></msqrt><mo>=</mo><msqrt><mfrac><mrow><mn>2</mn><mo>×</mo><mn>5</mn></mrow><mrow><mn>10</mn></mrow></mfrac></msqrt><mo>=</mo><mn>1</mn><mi> </mi><mi mathvariant="normal">s</mi></math>  
Angle rotated by rod = <math><mi>ω</mi><mi>t</mi><mo>=</mo><mn>0.5</mn><mo>×</mo><mn>1</mn><mo>=</mo><mn>0.5</mn><mi> </mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">d</mi></math>

</details>

---

### Q35. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `3`

A thin uniform bar of length $\mathrm{L}$ and mass $8 \mathrm{~m}$ lies on a smooth horizontal table. Two point masses $\mathrm{m}$ and $2 \mathrm{~m}$ moving in the same horizontal plane from opposite sides of the bar with speeds $2 \mathrm{v}$ and $v$ respectively. The masses stick to the bar after collision at a distance $\frac{\mathrm{L}}{3}$ and $\frac{\mathrm{L}}{6}$ respectively from the centre of the bar. If the bar starts rotating about its center of mass as a result of collision, the angular speed of the bar will be:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3phYkTgNQb5pfpG-LcvzkVXJPFckecdRIHtFf1ILIjQ.original.fullsize.png">

**Options:**

- **(A)** $\frac{\mathrm{v}}{6 \mathrm{~L}}$
- **(B)** $\frac{6 \mathrm{v}}{5 \mathrm{~L}}$
- **(C)** $\frac{3 \mathrm{v}}{5 \mathrm{~L}}$
- **(D)** $\frac{\mathrm{v}}{5 \mathrm{~L}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\mathrm{v}}{6 \mathrm{~L}}$**

**Detailed Solution:**

No Solution Available

</details>

---

### Q36. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

<p>A cubical block of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>&#160;</mo><mi>cm</mi></math> is moving with velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> on a smooth horizontal surface. The surface has a bump at a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> as shown in the figure. The angular velocity (in rad/s) of the block immediately after it hits the bump, is :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1b86cc84-6848-4303-b54a-5dfb47fadd66-image.png" style="width: 270px; height: 121px;" /></p>

**Options:**

- **(A)** 13.3
- **(B)** 5.0
- **(C)** 9.4
- **(D)** 6.7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 5.0**

**Detailed Solution:**

Conservation of angular momentum about point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math>,
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>before</mi></msub><mo>=</mo><msub><mi>L</mi><mi>after</mi></msub></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mi>v</mi><mi>R</mi><mo>=</mo><mi>I</mi><mi>&#969;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#969;</mi><mo>=</mo><mfrac><mrow><mi>m</mi><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mfenced close="]" open="["><mfrac><mi>a</mi><mn>2</mn></mfrac></mfenced></mrow><mrow><mi>m</mi><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mfrac><msup><mi>a</mi><mn>2</mn></msup><mn>6</mn></mfrac><mo>+</mo><msup><mfenced separators="|"><mfrac><mi>a</mi><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#969;</mi><mo>=</mo><mfrac><mn>12</mn><mrow><mn>8</mn><mi>a</mi></mrow></mfrac><mo>=</mo><mfrac><mn>3</mn><mrow><mn>2</mn><mo>&#215;</mo><mn>0</mn><mo>.3</mo></mrow></mfrac><mo>=</mo><mfrac><mn>10</mn><mn>2</mn></mfrac><mo>=</mo><mn>5</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

</details>

---

### Q37. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `3`

A particle of mass m is moving along the side of a square of side &#39;a&#39;, with a uniform speed <math><mi mathvariant="normal">&#965;</mi></math> in the x-y plane as shown in the figure:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6c6b8a9d-a9ed-40c6-9b26-9ec9ef16e198-image.png" style="width: 180px; height: 156px;" />
Which of the following statements is false for the angular momentum <math><mover accent="true"><mrow><mi mathvariant="normal">L</mi></mrow><mo>&#8594;</mo></mover></math> about the origin?

**Options:**

- **(A)** <math><mover accent="true"><mrow><mi mathvariant="normal">L</mi></mrow><mo>→</mo></mover><mo>=</mo><mi mathvariant="normal">m</mi><mi mathvariant="normal">υ</mi><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">R</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>+</mo><mi mathvariant="normal">a</mi></mrow></mfenced><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></math> 

when the particle is moving from B to C.
- **(B)** <math><mover accent="true"><mrow><mi mathvariant="normal">L</mi></mrow><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mi mathvariant="normal">m</mi><mi mathvariant="normal">υ</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac><mi mathvariant="normal">R</mi><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></math> 

 when the particle is moving from D to A.
- **(C)** <math><mover accent="true"><mrow><mi mathvariant="normal">L</mi></mrow><mo>→</mo></mover><mo>=</mo><mo>-</mo><mfrac><mrow><mi mathvariant="normal">m</mi><mi mathvariant="normal">υ</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac><mi mathvariant="normal">R</mi><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></math> 

 when the particle is moving from A to B.
- **(D)** <math><mover accent="true"><mrow><mi mathvariant="normal">L</mi></mrow><mo>&rarr;</mo></mover><mo>=</mo><mi mathvariant="normal">m</mi><mi mathvariant="normal">&upsilon;</mi><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">R</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>+</mo><mi mathvariant="normal">a</mi></mrow></mfenced><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></math> 

 when the particle is moving from C to D.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mover accent="true"><mrow><mi mathvariant="normal">L</mi></mrow><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mi mathvariant="normal">m</mi><mi mathvariant="normal">υ</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac><mi mathvariant="normal">R</mi><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></math> 

 when the particle is moving from D to A.**

**Detailed Solution:**

<math><mover accent="true"><mrow><mi mathvariant="normal">L</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mrow><mi mathvariant="normal">r</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi mathvariant="normal">P</mi></mrow><mo>&#8594;</mo></mover></math> or <math><mover accent="true"><mrow><mi mathvariant="normal">L</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi mathvariant="normal">r</mi><mi mathvariant="normal">p</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow><mover accent="true"><mrow><mi mathvariant="normal">n</mi></mrow><mo>^</mo></mover></math>

For D to A, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi mathvariant="normal">L</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mi mathvariant="normal">R</mi><msqrt><mn>2</mn></msqrt></mfrac><mi>m</mi><mi>v</mi><mfenced separators="|"><mrow><mo>-</mo><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math>

For A to B, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi mathvariant="normal">L</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mi mathvariant="normal">R</mi><msqrt><mn>2</mn></msqrt></mfrac><mi>m</mi><mi>v</mi><mfenced separators="|"><mrow><mo>-</mo><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math>

For C to D, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi mathvariant="normal">L</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mfrac><mi mathvariant="normal">R</mi><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mi mathvariant="normal">a</mi></mrow></mfenced><mi>m</mi><mi>v</mi><mfenced separators="|"><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></mfenced></math>

For B to C, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi mathvariant="normal">L</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mfrac><mi mathvariant="normal">R</mi><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mi mathvariant="normal">a</mi></mrow></mfenced><mi>m</mi><mi>v</mi><mfenced separators="|"><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></mfenced></math>

</details>

---

### Q38. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

<p>A particle of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>kg</mi></math> is on a smooth horizontal table and moves in a circular path of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>. The height of the table from the ground is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>. If the angular speed of the particle is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi mathvariant="normal">&#160;</mi><mi>rad</mi><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> , the magnitude of its angular momentum about a point on the ground right under the center of the circle is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mo>.4</mo><mi mathvariant="normal">&#160;</mi><mi>kg</mi><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11.52</mn><mi mathvariant="normal">&#160;</mi><mi>kg</mi><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20.16</mn><mi mathvariant="normal">&#160;</mi><mi>kg</mi><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8.64</mn><mi mathvariant="normal">&#160;</mi><mi>kg</mi><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mo>.4</mo><mi mathvariant="normal">&#160;</mi><mi>kg</mi><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EM0102251.jpg" style="width: 172px; height: 143px;" />

<math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>p</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>m</mi><mi>v</mi><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>=</mo><mn>2</mn><mo>&#215;</mo><mi>v</mi><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>0</mn><mo>.6</mo><mo>&#215;</mo><mn>12</mn><mo>=</mo><mn>7</mn><mo>.2</mo><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>14</mn><mo>.4</mo><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>&#160;&#160;&#160;&#160;&#160;</mo><mfenced separators="|"><mrow><mi>v</mi><mo>=</mo><mi>r</mi><mi>&#969;</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>(</mo><mn>0</mn><mo>.8</mo><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mo>.6</mo><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>)</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover accent="true"><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>p</mi><mo>&#8594;</mo></mover></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mn>0</mn><mo>.6</mo><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mo>.8</mo><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><mn>14</mn><mo>.4</mo><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover><mi mathvariant="normal">&#160;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.6</mo><mo>&#215;</mo><mn>14</mn><mo>.4</mo><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>-</mo><mn>0</mn><mo>.8</mo><mo>&#215;</mo><mn>14</mn><mo>.4</mo><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover></math>

<math><mo>=</mo><mn>14.4</mn><mfenced separators="|"><mrow><mn>0.6</mn><mi>&#160;</mi><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>0.8</mn><mi>&#160;</mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover></mrow></mfenced></math>

<math><mo>&#8658;</mo><mo>|</mo><mover accent="true"><mrow><mi>L</mi></mrow><mo>&#8594;</mo></mover><mo>|</mo></math><math><mo>=</mo><mn>14.4</mn><mi>&#160;</mi><msqrt><msup><mrow><mfenced separators="|"><mrow><mn>0.6</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mn>0.8</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math>

<math><mo>=</mo><mn>14.4</mn><msqrt><mn>0.36</mn><mo>+</mo><mn>0.64</mn></msqrt></math>

<math><mo>=</mo><mn>14.4</mn><mo>&#215;</mo><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>14.4</mn><mi>&#160;</mi><mi>kg</mi><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

</details>

---

### Q39. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A ball of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>160</mn><mo>&#160;</mo><mi mathvariant="normal">g</mi></math> is thrown up at an angle of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>&#176;</mo></math> to the horizontal at a speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The angular momentum of the ball at the highest point of the trajectory with respect to the point from which the ball is thrown is nearly <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="normal">g</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>73</mn><mo>&#160;</mo><mi>kg</mi><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>46</mn><mo>&#160;</mo><mi>kg</mi><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi>kg</mi><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi>kg</mi><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi>kg</mi><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6bb0e2c2-08fb-4622-9406-776e1dca1cb5-image.png" style="width: 350px; height: 123px;" />

The angular momentum <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>p</mi><mo>&#8594;</mo></mover></math></p><p>At maximum height angular momentum about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mi>m</mi><mo>&#160;</mo><mi>v</mi><mi>cos&#952;</mi><mo>&#160;</mo><mi>H</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>m</mi><mi>v</mi><mi>cos&#952;</mi><mo>&#215;</mo><mfrac><mrow><msup><mi>u</mi><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mi mathvariant="normal">&#952;</mi></mrow><mrow><mn>2</mn><mi>g</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mi>f</mi><mi>o</mi><mi>r</mi><mo>&#160;</mo><mi>h</mi><mi>o</mi><mi>r</mi><mi>i</mi><mi>z</mi><mi>o</mi><mi>n</mi><mi>t</mi><mi>a</mi><mi>l</mi><mo>&#160;</mo><mi>v</mi><mo>=</mo><mi>u</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mi>u</mi><mn>3</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mrow><mn>60</mn><mo>&#176;</mo></mrow></mfenced><mi>cos</mi><mfenced><mrow><mn>60</mn><mo>&#176;</mo></mrow></mfenced></mrow><mrow><mn>2</mn><mi>g</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi>kg</mi><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p>

</details>

---

### Q40. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

A particle is moving in a circular path of radius a, with a constant velocity $\mathrm{v}$ as shown in the figure. The centre of circle is marked by ' $\mathrm{C}$ '. The angular momentum from the origin $\mathrm{O}$ can be written as:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/OLdOqi8h2rHvr6tQwLTOaTrBctb_USjc7mUistJF2yo.original.fullsize.png">

**Options:**

- **(A)** va $(1+\cos 2 \theta)$
- **(B)** va $(1+\cos \theta)$
- **(C)** va $\cos 2 \theta$
- **(D)** va

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) va $(1+\cos 2 \theta)$**

**Detailed Solution:**

No Solution Available

</details>

---

### Q41. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `1`

A bob of mass m attached to an inextensible string of length <math> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>l</mi><mo>&#8289;</mo> </mrow> </math> is suspended from a vertical support. The bob rotates in a horizontal circle with an angular speed <math> <mrow> <mi>&#969;</mi> </mrow> </math> rad/s about the vertical. About the point of suspension :

**Options:**

- **(A)** Angular momentum is conserved
- **(B)** Angular momentum changes in magnitude but not in direction
- **(C)** Angular momentum changes in direction but not in magnitude
- **(D)** Angular momentum changes both in direction and magnitude

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Angular momentum changes in direction but not in magnitude**

**Detailed Solution:**

<math><mrow><mi>&tau;</mi> <mo>=</mo> <mtext>mg</mtext> <mo>&times;</mo> <mi>l</mi> <mspace width="0.5em"></mspace> <mtext>sin</mtext> <mspace width="0.5em"></mspace> <mi>&theta;</mi> </mrow> </math>. (Direction parallel to plane of rotation of particle)

                          <strong><u><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EM0025726_Ans__xyz_ccc.jpg" style="width: 139px; height: 158px;" /></u></strong>

as <math><mrow><mi>&tau;</mi> </mrow> </math> is perpendicular to <math> <mrow> <mover accent="true"> <mtext>L</mtext> <mo>&rarr;</mo> </mover> </mrow> </math>, direction of L changes but magnitude remains same.

</details>

---

### Q42. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

A particle of mass $2 \mathrm{~kg}$ is moving such that at time $t$, its position, in meter, is given by $\vec{r}(t)=5 \hat{i}-2 t^2 \hat{j}$. The angular momentum of the particle at $t=2 s$ about the origin in $\mathrm{kg} \mathrm{m}^{-2} \mathrm{~s}^{-1}$ is :

**Options:**

- **(A)** $-80 \hat{k}$
- **(B)** $(10 \hat{i}-16 \hat{j})$
- **(C)** $-40 \hat{k}$
- **(D)** $40 \hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-80 \hat{k}$**

**Detailed Solution:**

Angular momentum $\mathrm{L}=\mathrm{m}(\mathrm{v} \times \mathrm{r})$
$$
\begin{aligned}
& =2 \mathrm{~kg}\left(\frac{\mathrm{dr}}{\mathrm{dt}} \times \mathrm{r}\right)=2 \mathrm{~kg}\left(4 \mathrm{t} \times \times 5 \mathrm{i}-2 \mathrm{t}^2 \hat{\mathrm{j}}\right) \\
& =2 \mathrm{~kg}(-20 \mathrm{t} \hat{\mathrm{k}})=2 \mathrm{~kg} \times-20 \times 2 \mathrm{~m}^{-2} \mathrm{~s}^{-1} \hat{\mathrm{k}} \\
& =-80 \hat{\mathrm{k}}
\end{aligned}
$$

</details>

---

### Q43. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `3`

A hoop of radius <math> <mrow> <mtext>r</mtext> </mrow> </math> and mass <math> <mrow> <mtext>m</mtext> </mrow> </math> rotating with an angular velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#969;</mi><mn>0</mn></msub></math> is placed on a rough horizontal surface. The initial velocity of the centre of the hoop is zero. What will be the velocity of the centre of the hoop when it ceases to slip?

**Options:**

- **(A)** <math> <mrow> <mfrac> <mrow> <mtext>r</mtext> <msub> <mi>ω</mi> <mn>0</mn> </msub> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
- **(B)** <math> <mrow> <mtext>r</mtext> <msub> <mi>&omega;</mi> <mn>0</mn> </msub> </mrow> </math>
- **(C)** <math> <mrow> <mfrac> <mrow> <mtext>r</mtext> <msub> <mi>&omega;</mi> <mn>0</mn> </msub> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mtext>r</mtext> <msub> <mi>&omega;</mi> <mn>0</mn> </msub> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mrow> <mfrac> <mrow> <mtext>r</mtext> <msub> <mi>ω</mi> <mn>0</mn> </msub> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<p>By conservation of angular momentum at the point of contact 
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a02a8fc2-9e95-4962-b5a3-dee0b5b49c3b-image.png" style="width: 370px; height: 117px;" /> 
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><msup><mi>r</mi><mn>2</mn></msup><msub><mi>&#969;</mi><mn>0</mn></msub><mo>=</mo><mi>m</mi><mi>v</mi><mi>r</mi><mo>+</mo><mi>m</mi><msup><mi>r</mi><mn>2</mn></msup><mi>&#969;</mi><mo>=</mo><mi>m</mi><mi>v</mi><mi>r</mi><mo>+</mo><mi>m</mi><msup><mi>r</mi><mn>2</mn></msup><mo>.</mo><mi>v</mi><mo>/</mo><mi>r</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msup><mi>r</mi><mn>2</mn></msup><msub><mi>&#969;</mi><mn>0</mn></msub><mo>=</mo><mn>2</mn><mi>v</mi><mi>r</mi><mo>&#8658;</mo><mi>v</mi><mo>=</mo><mi>r</mi><msub><mi>&#969;</mi><mn>0</mn></msub><mo>/</mo><mn>2</mn></math></p><p> </p>

</details>

---

### Q44. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `3`

A stone of mass $m$, tied to the end of a string, is whirled around in a circle on a horizontal frictionless table. The length of the string is reduced gradually keeping the angular momentum of the stone about the centre of the circle constant. Then, the tension in the string is given by $T=A r^n$, where $A$ is a constant, $r$ is the instantaneous radius of the circle. The value of $n$ is equal to

**Options:**

- **(A)** $-1$
- **(B)** $-2$
- **(C)** $-4$
- **(D)** $-3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-3$**

**Detailed Solution:**

No Solution Available

</details>

---

### Q45. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `1`

This question has Statement 1 and Statement 2. Of the four choices given after the Statements, choose the one that best describes the two Statements.
Statement 1: When moment of inertia $I$ of a body rotating about an axis with angular speed $\omega$ increases, its angular momentum $L$ is unchanged but the kinetic energy $K$ increases if there is no torque applied on it.
Statement 2: $L=I \omega$, kinetic energy of rotation $=\frac{1}{2} I \omega^2$

**Options:**

- **(A)** Statement 1 is true, Statement 2 is true, Statement 2 is not the correct explanation of Statement 1.
- **(B)** Statement 1 is false, Statement 2 is true.
- **(C)** Statement 1 is true, Statement 2 is true, Statement 2 is correct explanation of the Statement 1.
- **(D)** Statement 1 is true, Statement 2 is false.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement 1 is false, Statement 2 is true.**

**Detailed Solution:**

As $L=I \omega$ so $L$ increases with increase in $\omega$. Kinetic energy $_{\text {(rotational) }}$ depends on an angular velocity ' $\omega$ ' and moment of inertia of the body $I$.
i.e., $K \cdot E \cdot\left(\right.$ rotational $=\frac{1}{2} I \omega^2$

</details>

---

### Q46. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `1`

A thin horizontal circular disc is rotating about a vertical axis passing through its centre. An insect is at rest at a point near the rim of the disc. The insect now moves along a diameter of the disc to reach its other end. During the journey of the insect, the angular speed of the disc:

**Options:**

- **(A)** continuously decreases
- **(B)** continuously increases
- **(C)** first increases and then decreases
- **(D)** remains unchanged

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) first increases and then decreases**

**Detailed Solution:**

$$
\tau=0
$$
Angular momentum is conserve
$$
\mathrm{I}_1 \omega_1=\mathrm{I}_2 \omega_2 \Rightarrow \omega_2=\frac{\mathrm{I}_1 \omega_1}{\mathrm{I}_2}
$$
$\mathrm{I}_2$ first decreases and then increases
$\therefore \omega$ first increases and then decreases.

</details>

---

### Q47. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `1`

Angular momentum of the particle rotating with a central force is constant due to

**Options:**

- **(A)** Constant Force
- **(B)** Constant linear momentum.
- **(C)** Zero Torque
- **(D)** Constant Torque

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Zero Torque**

**Detailed Solution:**

No Solution Available

</details>

---

### Q48. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `2`

A thin circular ring of mass $\mathrm{m}$ and radius $\mathrm{R}$ is rotating about its axis with a constant angular velocity $\omega$. Two objects each of mass $M$ are attached gently to the opposite ends of a diameter of the ring. The ring now rotates with an angular velocity $\omega^{\prime}=$

**Options:**

- **(A)** $\frac{\omega \mathrm{m}}{(\mathrm{m}+2 \mathrm{M})}$
- **(B)** $\frac{\omega(\mathrm{m}+2 \mathrm{M})}{\mathrm{m}}$
- **(C)** $\frac{\omega(m-2 M)}{(m+2 M)}$
- **(D)** $\frac{\omega m}{(m+M)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\omega \mathrm{m}}{(\mathrm{m}+2 \mathrm{M})}$**

**Detailed Solution:**

$L_i=L_f$
$m R R^2 \omega=\left(m R^2+2 M R^2\right) \omega^{\prime}$
$\omega^{\prime}=\left(\frac{m \omega}{m+2 M}\right)$

</details>

---

### Q49. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

A solid sphere is rotating in free space. If the radius of the sphere is increased keeping mass same which one of the following will not be affected?

**Options:**

- **(A)** moment of inertia
- **(B)** angular momentum
- **(C)** angular velocity
- **(D)** rotational kinetic energy.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) angular momentum**

**Detailed Solution:**

Let it be assume that in "free space" not only the acceleration due to gravity it acting but al there are no external torque acting but also there are no external torque acting on the sphere. If due to internal changes in the system, the radius has increased, then the law of the conservation of angular momentum holds good.

</details>

---

### Q50. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

A particle performing uniform circular motion has angular frequency is doubled \& its kinetic energy halved, then the new angular momentum is

**Options:**

- **(A)** $\frac{\mathrm{L}}{4}$
- **(B)** $2 \mathrm{~L}$
- **(C)** $4 \mathrm{~L}$
- **(D)** $\frac{\mathrm{L}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\mathrm{L}}{4}$**

**Detailed Solution:**

Angular momentum $\propto \frac{1}{\text { Angular frequency }} \propto$ Kinetic energy $\Rightarrow \vec{L}=\frac{\mathrm{K} . \mathrm{E} .}{\mathrm{w}}$
$\frac{\mathrm{L}_1}{\mathrm{~L}_2}=\left(\frac{\mathrm{K} . \mathrm{E}_1}{\mathrm{w}_1}\right) \times \frac{\mathrm{w}_2}{\mathrm{KE}_2}=4 \Rightarrow \mathrm{L}_2=\frac{\mathrm{L}}{4}$

</details>

---

### Q51. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

A particle of mass $m$ moves along line $P C$ with velocity $v$ as shown. What is the angular momentum of the particle about $\mathrm{P} ?$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/_kcF-YWlaac6KAB10eRaguTUPipzymbH8XCk9urYRB4.original.fullsize.png">

**Options:**

- **(A)** mvL
- **(B)** mvl
- **(C)** mvr
- **(D)** zero

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) zero**

**Detailed Solution:**

Zero, line of motion through the point P.

</details>

---

### Q52. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `3`

Initial angular velocity of a circular disc of mass $M$ is $\omega_1$. Then two small spheres of mass $m$ are attached gently to diametrically opposite points on the edge of the disc. What is the final angular velocity of the disc?

**Options:**

- **(A)** $\left(\frac{M+m}{M}\right) \omega_1$
- **(B)** $\left(\frac{\mathrm{M}+\mathrm{m}}{\mathrm{m}}\right) \omega_1$
- **(C)** $\left(\frac{\mathrm{M}}{\mathrm{M}+4 \mathrm{~m}}\right) \omega_1$
- **(D)** $\left(\frac{M}{M+2 m}\right) \omega_1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(\frac{\mathrm{M}}{\mathrm{M}+4 \mathrm{~m}}\right) \omega_1$**

**Detailed Solution:**

Angular momentum = conserved
$\frac{1}{2} \mathrm{MR}^2 \omega_1=2 m R^2 \omega+\frac{1}{2} \mathrm{MR}^2 \omega \Rightarrow \omega=\frac{\mathrm{M} \omega_1}{\mathrm{M}+4 \mathrm{~m}}$

</details>

---

