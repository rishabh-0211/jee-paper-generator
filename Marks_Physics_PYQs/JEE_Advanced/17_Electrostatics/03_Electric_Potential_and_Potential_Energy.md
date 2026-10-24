# JEE Advanced Physics - Electrostatics

## Topic 3: Electric Potential and Potential Energy

**Total Questions:** 12

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Two charges $Q_1 = q$ and $Q_2 = mq$ are placed at the points $P_1(a, b)$ and $P_2(ma, mb)$, respectively, in the $XY$ plane, where $a, b \neq 0$ and $m \neq 0, 1$. If $V_1$ is the potential at a point in the $XY$ plane due to charge $Q_1$ and $V_2$ is the potential at that point due to charge $Q_2$. Correct statement(s) for the points at which $|V_1| = |V_2|$ is/are:

**Options:**

- **(A)** For $m = -1$, locus of these points is $ax + by = 0$.
- **(B)** For $m = 2$, the locus of these points is a circle of radius $\dfrac{2}{3}\sqrt{a^2 + b^2}$ centered at $\left(\dfrac{2}{3}a, \dfrac{2}{3}b\right)$
- **(C)** For $m = -2$, the locus of these points is a circle of radius $2\sqrt{a^2 + b^2}$ centered at $(2a, 2b)$
- **(D)** For $m = -3$, locus of these points is $3bx + 3ay = 0$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) For $m = -2$, the locus of these points is a circle of radius $2\sqrt{a^2 + b^2}$ centered at $(2a, 2b)$**

**Detailed Solution:**

The potential at a point $(x, y)$ due to charge $Q_1$ is $V_1 = \dfrac{1}{4\pi\epsilon_0} \dfrac{q}{\sqrt{(x-a)^2 + (y-b)^2}}$.

The potential at $(x, y)$ due to charge $Q_2$ is $V_2 = \dfrac{1}{4\pi\epsilon_0} \dfrac{mq}{\sqrt{(x-ma)^2 + (y-mb)^2}}$.

Given $|V_1| = |V_2|$, we have:

$\dfrac{1}{(x-a)^2 + (y-b)^2} = \dfrac{m^2}{(x-ma)^2 + (y-mb)^2}$

Cross-multiplying and expanding both sides:

$(x-ma)^2 + (y-mb)^2 = m^2[(x-a)^2 + (y-b)^2]$

$x^2 + m^2a^2 - 2max + y^2 + m^2b^2 - 2mby = m^2(x^2 + a^2 - 2ax + y^2 + b^2 - 2by)$

$x^2 + y^2 - 2m(ax+by) + m^2(a^2+b^2) = m^2(x^2+y^2) - 2m^2(ax+by) + m^2(a^2+b^2)$

Canceling $m^2(a^2+b^2)$ from both sides and rearranging:

$(m^2-1)(x^2+y^2) - 2m(m-1)(ax+by) = 0$

Since $m \neq 1$, dividing by $m-1$ gives the general equation of the locus:

$(m+1)(x^2+y^2) - 2m(ax+by) = 0$

For $m = -1$:

$0 - 2(-1)(ax+by) = 0 \Rightarrow ax+by = 0$. This represents a straight line.

For $m = 2$:

$3(x^2+y^2) - 4(ax+by) = 0 \Rightarrow x^2+y^2 - \dfrac{4}{3}ax - \dfrac{4}{3}by = 0$.

This represents a circle with center $\left(\dfrac{2}{3}a, \dfrac{2}{3}b\right)$ and radius $\sqrt{\left(\dfrac{2}{3}a\right)^2 + \left(\dfrac{2}{3}b\right)^2} = \dfrac{2}{3}\sqrt{a^2+b^2}$.

For $m = -2$:

$(-1)(x^2+y^2) - 2(-2)(ax+by) = 0 \Rightarrow x^2+y^2 - 4ax - 4by = 0$.

This represents a circle with center $(2a, 2b)$ and radius $\sqrt{(2a)^2 + (2b)^2} = 2\sqrt{a^2+b^2}$.

For $m = -3$:

$(-2)(x^2+y^2) - 2(-3)(ax+by) = 0 \Rightarrow x^2+y^2 - 3ax - 3by = 0$.

This represents a circle, not a straight line.

Answer: For $m = -1$, locus of these points is $ax + by = 0$.; For $m = 2$, the locus of these points is a circle of radius $\dfrac{2}{3}\sqrt{a^2 + b^2}$ centered at $\left(\dfrac{2}{3}a, \dfrac{2}{3}b\right)$; For $m = -2$, the locus of these points is a circle of radius $2\sqrt{a^2 + b^2}$ centered at $(2a, 2b)$

</details>

---

### Q2. JEE Advanced 2025 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

A positive point charge of $10^{-8} \mathrm{C}$ is kept at a distance of 20 cm from the center of a neutral conducting sphere of radius 10 cm . The sphere is then grounded and the charge on the sphere is measured. The grounding is then removed and subsequently the point charge is moved by a distance of 10 cm further away from the center of the sphere along the radial direction. Taking $\frac{1}{4 \pi \epsilon_0}=9 \times 10^9 \mathrm{Nm}^2 / \mathrm{C}^2$ (where $\epsilon_0$ is the permittivity of free space), which of the following
statements is/are correct: :

**Options:**

- **(A)** Before the grounding, the electrostatic potential of the sphere is 450 V .
- **(B)** Charge flowing from the sphere to the ground because of grounding is $5 \times 10^{-9} \mathrm{C}$.
- **(C)** After the grounding is removed, the charge on the sphere is $-5 \times 10^{-9} \mathrm{C}$.
- **(D)** The final electrostatic potential of the sphere is 300 V .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) After the grounding is removed, the charge on the sphere is $-5 \times 10^{-9} \mathrm{C}$.**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/x0RO9YRVyHCm76_k4EH8ZJyG0R-ITGMwRh-LMRquBHc.original.fullsize.png">
Before grounding
$\begin{aligned} & \mathrm{V}_{\text {sphere }}=\left(\mathrm{V}_{\mathrm{C}}\right)_{\text {net }}=\left(\mathrm{V}_{\mathrm{C}}\right)_{\mathrm{q}}+\left(\mathrm{V}_{\mathrm{C}}\right)_{\text {ind }} \\ & \mathrm{V}_{\text {sphere }}=\frac{\mathrm{kq}}{\ell}+0=\frac{9 \times 10^9 \times 10^{-8}}{0.2}=\frac{90}{0.2}=\frac{900}{2}=450 \mathrm{volt}\end{aligned}$
After grounding<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/OowL2Vj5lPZCx01f5urK4GaFy3XZYnE09qpwQctVuyk.original.fullsize.png">
$\begin{aligned} & \frac{\mathrm{kQ}}{\ell}+\frac{\mathrm{kq}_{\mathrm{S}}}{\mathrm{R}}=\mathrm{V}_{\text {sphere }}^{\prime}=0 \\ & \mathrm{q}_{\mathrm{s}}=-\frac{\mathrm{R}}{\ell} \mathrm{q}=-\frac{1}{2} \times 10^{-8}=-5 \times 10^{-9} \\ & \mathrm{q}_{\mathrm{s}}=-5 \times 10^{-9} \text { Coulomb }\end{aligned}$
Charge flower from sphere to ground $=5 \times 10^{-9}$ Coulomb
After grounding is removed
$\begin{aligned} & \left(\mathrm{V}_{\text {sphere }}\right)_{\text {final }}=\frac{\mathrm{kq}}{\ell^{\prime}}+\frac{\mathrm{kq}_{\mathrm{s}}}{\mathrm{R}} \\ & =\frac{9 \times 10^9 \times 10^2 \times 10^{-8}}{30}-\frac{9 \times 10^9 \times 5 \times 10^{-9} \times 10^2}{10} \\ & =\frac{9 \times 1000}{30}-450=300 \mathrm{volt}-450 \mathrm{volt}=-150 \mathrm{volt}\end{aligned}$

</details>

---

### Q3. JEE Advanced 2024 (Paper 2)

*Type:* `numerical` | *Level:* `2`

An infinitely long thin wire, having a uniform charge density per unit length of $5 \mathrm{nC} / \mathrm{m}$, is passing through a spherical shell of radius $1 \mathrm{~m}$, as shown in the figure. A $10 \mathrm{nC}$ charge is distributed uniformly over the spherical shell. If the configuration of the charges remains static, the magnitude of the potential difference between points $\mathrm{P}$ and $\mathrm{R}$, in Volt, is _______ .
[Given: In SI units $\frac{1}{4 \pi \epsilon_0}=9 \times 10^9, \ln 2=0.7$. Ignore the area pierced by the wire.]
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/6PDjZmGanBIHngaoMG0q6Rf55My2K_H9Z8D9IDP9-NQ.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **171**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/W5Mg0ohUoASHAwaemv7UrZ2KlPbJrrz7_qXQ0epCF30.original.fullsize.png">
due to wire
$\begin{aligned} & \mathrm{dV}=-\overrightarrow{\mathrm{E}} \cdot \overrightarrow{\mathrm{dx}} \\ & \int_{\mathrm{v}_{\mathrm{P}}}^{\mathrm{v}_{\mathrm{R}}} \mathrm{dV}=-\int_{0.5}^2 \frac{2 \mathrm{k} \lambda}{\mathrm{x}} \mathrm{dx} \\ & \mathrm{v}_{\mathrm{R}}-\mathrm{v}_{\mathrm{P}}=-2 \mathrm{k} \lambda \ln \frac{2}{0.5} \\ & =-2 \times 9 \times 10^9 \times 3 \times 10^{-9} \times 2 \times 0.7=-126 \mathrm{~V}\end{aligned}$
due to sphere
$\begin{aligned} & \mathrm{v}_{\mathrm{R}}-\mathrm{v}_P=\frac{\mathrm{kQ}}{2}-\frac{\mathrm{kQ}}{1}=-\frac{\mathrm{kQ}}{2}=\frac{-9 \times 10^9 \times 10 \times 10^{-9}}{2} \\ &=-45 \mathrm{~V} \\ & \mathrm{v}_{\mathrm{R}}-\mathrm{v}_{\mathrm{P}}=-126-45=-171 \mathrm{~V} \\ & \mathrm{v}_{\mathrm{P}}-\mathrm{v}_{\mathrm{R}}=171 \mathrm{~V}\end{aligned}$

</details>

---

### Q4. JEE Advanced 2022 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

<p>A disk of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> with uniform positive charge density <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#963;</mi></math> is placed on the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi></math> plane with its center at the origin. The Coulomb potential along the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math>-axis is
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mfenced><mi>z</mi></mfenced><mo>=</mo><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#1013;</mi><mn>0</mn></msub></mrow></mfrac><mfenced><mrow><msqrt><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup></msqrt><mo>-</mo><mi>z</mi></mrow></mfenced></math></p><p>A particle of positive charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> is placed initially at rest at a point on the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math>-axis with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><msub><mi>z</mi><mn>0</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>0</mn></msub><mo>&#62;</mo><mn>0</mn></math>. In addition to the Coulomb force, the particle experiences a vertical force <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>F</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mi>c</mi><mover><mi>k</mi><mo>^</mo></mover></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>&#62;</mo><mn>0</mn></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>c</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow><mrow><mi>q</mi><mi>&#963;</mi></mrow></mfrac></math>. Which of the following statement(s) is(are) correct?</p>

**Options:**

- **(A)** For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>0</mn></msub><mo>=</mo><mfrac><mn>25</mn><mn>7</mn></mfrac><mi>R</mi></math>, the particle reaches the origin.
- **(B)** For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>0</mn></msub><mo>=</mo><mfrac><mn>3</mn><mn>7</mn></mfrac><mi>R</mi></math>, the particle reaches the origin.
- **(C)** For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>0</mn></msub><mo>=</mo><mfrac><mi>R</mi><msqrt><mn>3</mn></msqrt></mfrac></math>, the particle returns back to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><msub><mi>z</mi><mn>0</mn></msub></math>
- **(D)** For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>&#62;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>0</mn></msub><mo>&#62;</mo><mn>0</mn></math>, the particle always reaches the origin.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>&#62;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>0</mn></msub><mo>&#62;</mo><mn>0</mn></math>, the particle always reaches the origin.**

**Detailed Solution:**

<p>For the particle to reach at origin, work done by the force should be greater than the increase in the potential energy of the charged particle. Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mi>z</mi><mo>&#8805;</mo><mfrac><mrow><mi>&#963;</mi><mi>q</mi></mrow><mrow><mn>2</mn><msub><mi>&#1013;</mi><mn>0</mn></msub></mrow></mfrac><mfenced close="]" open="["><mrow><mi>R</mi><mo>-</mo><mfenced><mrow><msqrt><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup></msqrt><mo>-</mo><mi>z</mi></mrow></mfenced></mrow></mfenced><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mfrac><mrow><mi>c</mi><mn>2</mn><msub><mi>&#1013;</mi><mn>0</mn></msub></mrow><mrow><mi>&#963;</mi><mi>q</mi></mrow></mfrac><mo>&#8805;</mo><mfrac><mfenced close="]" open="["><mrow><mi>R</mi><mo>-</mo><mfenced><mrow><msqrt><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup></msqrt><mo>-</mo><mi>z</mi></mrow></mfenced></mrow></mfenced><mi>z</mi></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>&#946;</mi><mo>&#8805;</mo><mfrac><mfenced close="]" open="["><mrow><mi>R</mi><mo>-</mo><mfenced><mrow><msqrt><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup></msqrt><mo>-</mo><mi>z</mi></mrow></mfenced></mrow></mfenced><mi>z</mi></mfrac></math></p><p>For option A</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced close="]" open="["><mrow><mi>R</mi><mo>-</mo><mfenced><mrow><msqrt><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup></msqrt><mo>-</mo><mi>z</mi></mrow></mfenced></mrow></mfenced><mi>z</mi></mfrac><mo>=</mo><mfrac><mrow><mi>R</mi><mo>-</mo><mi>R</mi><mfenced><mrow><msqrt><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>625</mn><mn>49</mn></mfrac></mstyle></msqrt><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>25</mn><mn>7</mn></mfrac></mstyle></mrow></mfenced></mrow><mrow><mi>R</mi><mstyle displaystyle="true"><mfrac><mn>25</mn><mn>7</mn></mfrac></mstyle></mrow></mfrac><mo>&#8771;</mo><mn>0</mn><mo>.</mo><mn>242</mn></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>25</mn><mo>&#62;</mo><mn>0</mn><mo>.</mo><mn>242</mn></math></p><p>Option A is correct.</p><p>For option B</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced close="]" open="["><mrow><mi>R</mi><mo>-</mo><mfenced><mrow><msqrt><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup></msqrt><mo>-</mo><mi>z</mi></mrow></mfenced></mrow></mfenced><mi>z</mi></mfrac><mo>=</mo><mfrac><mrow><mi>R</mi><mo>-</mo><mi>R</mi><mfenced><mrow><msqrt><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>9</mn><mn>49</mn></mfrac></mstyle></msqrt><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>7</mn></mfrac></mstyle></mrow></mfenced></mrow><mrow><mi>R</mi><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>7</mn></mfrac></mstyle></mrow></mfrac><mo>&#8771;</mo><mn>0</mn><mo>.</mo><mn>79</mn></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>25</mn><mo>&#60;</mo><mn>0</mn><mo>.</mo><mn>79</mn></math></p><p>Option B is incorrect</p><p>For option C</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced close="]" open="["><mrow><mi>R</mi><mo>-</mo><mfenced><mrow><msqrt><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup></msqrt><mo>-</mo><mi>z</mi></mrow></mfenced></mrow></mfenced><mi>z</mi></mfrac><mo>=</mo><mfrac><mrow><mi>R</mi><mo>-</mo><mi>R</mi><mfenced><mrow><msqrt><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></msqrt><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mstyle></mrow></mfenced></mrow><mrow><mi>R</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mstyle></mrow></mfrac><mo>&#8771;</mo><mn>0</mn><mo>.</mo><mn>73</mn></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>25</mn><mo>&#60;</mo><mn>0</mn><mo>.</mo><mn>73</mn></math></p><p>Therefore, the particle returns to <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>0</mn></msub></math></p><p>Hence, option C is correct.</p><p>For option D,</p><p>For any value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced close="]" open="["><mrow><mi>R</mi><mo>-</mo><mfenced><mrow><msqrt><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup></msqrt><mo>-</mo><mi>z</mi></mrow></mfenced></mrow></mfenced><mi>z</mi></mfrac><mo>&#60;</mo><mn>1</mn></math></p><p>Hence, option D is correct.</p>

</details>

---

### Q5. JEE Advanced 2021 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Two point charges $-Q$ and $+Q / \sqrt{3}$ are placed in the $x y$-plane at the origin $(0,0)$ and a point $(2,0)$, respectively, as shown in the figure. This results in an equipotential circle of radius $R$ and potential $V=0$ in the $x y$-plane with its center at $(b, 0)$. All lengths are measured in meters.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/YK2c0hiklVd7NIyvRFvQnmglEF7ir3wGF8OnQ5lCpME.original.fullsize.png">
The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> is ________ meter.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>h</mi><mo>,</mo><mi>k</mi></mrow></mfenced></math> be be a general point with potential to be zero.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/003e4fae-d376-41f9-9225-5077f353de7c-9e36193f-e1d7-494f-bfd1-fd7bea650501-e10cfd36-e907-4f27-98ce-67ba07e57f86-image.png" style="width: 300px; height: 90px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>1</mn></msub><mo>+</mo><msub><mi>V</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn></math>   (as potential given <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>K</mi><mfenced><mrow><mo>&#8722;</mo><mi>Q</mi></mrow></mfenced></mrow><msqrt><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><mfrac><mrow><mi>K</mi><mfenced><mfrac><mi>Q</mi><msqrt><mn>3</mn></msqrt></mfrac></mfenced></mrow><msqrt><msup><mfenced><mrow><mi>h</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></msqrt></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msqrt><mn>3</mn></msqrt><msqrt><msup><mfenced><mrow><mi>h</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><msqrt><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mi>h</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><msup><mi>h</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>4</mn><mi>h</mi><mo>+</mo><mn>4</mn><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mi>k</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>12</mn><mi>h</mi><mo>+</mo><mn>12</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>6</mn><mi>h</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>h</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>6</mn><mi>h</mi><mo>+</mo><mn>6</mn></mrow></mfenced><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>h</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>6</mn><mi>h</mi><mo>+</mo><mn>9</mn></mrow></mfenced><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>h</mi><mo>&#8722;</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn></math></p><p>Standard equation of circle is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><msub><mi>x</mi><mn>1</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mo>&#8722;</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>R</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p><p>and value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> </p>

</details>

---

### Q6. JEE Advanced 2021 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Two point charges $-Q$ and $+Q / \sqrt{3}$ are placed in the $x y$-plane at the origin $(0,0)$ and a point $(2,0)$, respectively, as shown in the figure. This results in an equipotential circle of radius $R$ and potential $V=0$ in the $x y$-plane with its center at $(b, 0)$. All lengths are measured in meters.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/YK2c0hiklVd7NIyvRFvQnmglEF7ir3wGF8OnQ5lCpME.original.fullsize.png">
The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is ________ meter.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1.73**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>h</mi><mo>,</mo><mi>k</mi></mrow></mfenced></math> be be a general point with potential to be zero.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/003e4fae-d376-41f9-9225-5077f353de7c-9e36193f-e1d7-494f-bfd1-fd7bea650501-e10cfd36-e907-4f27-98ce-67ba07e57f86-image.png" style="width: 300px; height: 90px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>1</mn></msub><mo>+</mo><msub><mi>V</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn></math>   (as potential given <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>K</mi><mfenced><mrow><mo>&#8722;</mo><mi>Q</mi></mrow></mfenced></mrow><msqrt><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><mfrac><mrow><mi>K</mi><mfenced><mfrac><mi>Q</mi><msqrt><mn>3</mn></msqrt></mfrac></mfenced></mrow><msqrt><msup><mfenced><mrow><mi>h</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></msqrt></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msqrt><mn>3</mn></msqrt><msqrt><msup><mfenced><mrow><mi>h</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><msqrt><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mi>h</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><msup><mi>h</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>4</mn><mi>h</mi><mo>+</mo><mn>4</mn><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mi>k</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>12</mn><mi>h</mi><mo>+</mo><mn>12</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>6</mn><mi>h</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>h</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>6</mn><mi>h</mi><mo>+</mo><mn>6</mn></mrow></mfenced><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>h</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>6</mn><mi>h</mi><mo>+</mo><mn>9</mn></mrow></mfenced><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>h</mi><mo>&#8722;</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn></math></p><p>Standard equation of circle is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><msub><mi>x</mi><mn>1</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mo>&#8722;</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>R</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p><p>and value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> </p>

</details>

---

### Q7. JEE Advanced 2019 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

A thin spherical insulating shell of radius <math><mi mathvariant="normal">R</mi></math> carries a uniformly distributed charge such that the potential at its surface is <math><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>0</mn></mrow></msub></math> . A hole with a small area <math><mi mathvariant="normal">&#945;</mi><mn>4</mn><mi mathvariant="normal">&#960;</mi><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mi mathvariant="normal">&#945;</mi><mo>&#8810;</mo><mn>1</mn></mrow></mfenced></math> is made on the shell without affecting the rest of the shell. Which one of the following statements is correct?

**Options:**

- **(A)** The magnitude of electric field at the center of the shell is reduced by  <math><mfrac><mrow><mi mathvariant="normal">α</mi><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>2</mn><mi mathvariant="normal">R</mi></mrow></mfrac></math>
- **(B)** The potential at the center of the shell is reduced by  <math><mn>2</mn><mi mathvariant="normal">α</mi><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>0</mn></mrow></msub></math>
- **(C)** The ratio of the potential at the center of the shell to that of the point at  <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi mathvariant="normal">R</mi></math>  from center towards the hole will be  <math><mfrac><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">α</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi mathvariant="normal">α</mi></mrow></mfrac></math>
- **(D)** The magnitude of electric field at a point, located on a line passing through the hole and shell's center on a distance  <math><mn>2</mn><mi mathvariant="normal">R</mi></math>  from the center of the spherical shell will be reduced by  <math><mfrac><mrow><mi mathvariant="normal">α</mi><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>2</mn><mi mathvariant="normal">R</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) The ratio of the potential at the center of the shell to that of the point at  <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi mathvariant="normal">R</mi></math>  from center towards the hole will be  <math><mfrac><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">α</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi mathvariant="normal">α</mi></mrow></mfrac></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/uqsdysivylgxzsssaavufwpqwbfyvewbikzpfluvxrvwmfdgdo.png"/> 
Let  <math><mi>‘</mi><mi>A</mi><mi>’</mi></math>  be the point at a distance  <math><mn>2</mn><mi>R</mi></math>  from center and  <math><mi>‘</mi><mi>B</mi><mi>’</mi></math>  be the point at a distance of  <math><mfrac><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>  from center.
Now, let total charge on spherical shell distributed uniformly  <math><mo>=</mo><mi>Q</mi></math> 
 <math><mo>⇒</mo><mtext> </mtext><mi mathvariant="normal">C</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">g</mi><mi mathvariant="normal">e</mi><mtext> </mtext><mi mathvariant="normal">p</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">r</mi><mtext> </mtext><mi mathvariant="normal">u</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">t</mi><mtext> </mtext><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mo>=</mo><mfrac><mrow><mi>Q</mi></mrow><mrow><mn>4</mn><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math> 
Charge on elemental area  <math><mi>‘</mi><mi>d</mi><mi>A</mi><mi>’</mi></math> .
Given potential at surface  <math><msub><mrow><mo>=</mo><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub></math> 
 <math><mo>⇒</mo><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mfrac><mrow><mi>K</mi><mi>Q</mi></mrow><mrow><mi>R</mi></mrow></mfrac></math> 
Now, potential at center of the shell  <math><msub><mrow><mo>=</mo><mi>V</mi></mrow><mrow><mi>C</mi></mrow></msub></math> 
 <math><msub><mrow><mi>V</mi></mrow><mrow><mi>C</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>K</mi><mi>Q</mi></mrow><mrow><mi>R</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>K</mi><mo>(</mo><mi>d</mi><mi>Q</mi><mo>)</mo></mrow><mrow><mi>R</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>K</mi><mi>Q</mi></mrow><mrow><mi>R</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>K</mi><mo>(</mo><mi>α</mi><mi>Q</mi><mo>)</mo></mrow><mrow><mi>R</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>K</mi><mi>Q</mi></mrow><mrow><mi>R</mi></mrow></mfrac><mo>(</mo><mn>1</mn><mo>-</mo><mi>α</mi><mo>)</mo></math> 
 <math><mo>⇒</mo><msub><mrow><mi>V</mi></mrow><mrow><mi>C</mi></mrow></msub><mo>=</mo><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>α</mi></mrow></mfenced><mo>⇒</mo><mtext>Reduced </mtext><mi mathvariant="normal">b</mi><mi mathvariant="normal">y</mi><mtext> </mtext><mi>α</mi><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub></math> 
Now potential  <math><mo>=</mo><msub><mrow><mi>V</mi></mrow><mrow><mi>B</mi></mrow></msub></math> 
 <math><mo>⇒</mo><msub><mrow><mi>V</mi></mrow><mrow><mi>B</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>K</mi><mi>Q</mi></mrow><mrow><mi>R</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>K</mi><mfenced separators="|"><mrow><mi>a</mi><mi>Q</mi></mrow></mfenced></mrow><mrow><mrow><mrow><mi>R</mi></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></mfrac><mo>=</mo><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>a</mi></mrow></mfenced><mo>⇒</mo><mi mathvariant="normal">R</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">d</mi><mtext> </mtext><mi mathvariant="normal">b</mi><mi mathvariant="normal">y</mi><mtext> </mtext><mn>2</mn><mi>α</mi><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub></math> 
 <math><mo>∴</mo><mfrac><mrow><msub><mrow><mi>V</mi></mrow><mrow><mi>C</mi></mrow></msub></mrow><mrow><msub><mrow><mi>V</mi></mrow><mrow><mi>B</mi></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>a</mi></mrow></mfrac></math> 
Now, electric field at  <math><mi>A</mi><mo>=</mo><msub><mrow><mi>E</mi></mrow><mrow><mi>A</mi></mrow></msub></math> 
Then,  <math><msub><mrow><mi>E</mi></mrow><mrow><mi>A</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>K</mi><mi>Q</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><mi>R</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>K</mi><mi>a</mi><mi>Q</mi></mrow><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>K</mi><mi>Q</mi></mrow><mrow><mn>4</mn><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>a</mi><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi>R</mi></mrow></mfrac></math> 
So reduced by  <math><mfrac><mrow><mi>a</mi><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi>R</mi></mrow></mfrac></math> 
Electric field at center  <math><mi>‘</mi><mi>C</mi><mi>’</mi></math>  due to small change  <math><mi>‘</mi><mi>d</mi><mi>Q</mi><mi>’</mi></math> 
 <math><msub><mrow><mi>E</mi></mrow><mrow><mi>C</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>K</mi><mfenced separators="|"><mrow><mi>d</mi><mi>q</mi></mrow></mfenced></mrow><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>K</mi><mfenced separators="|"><mrow><mi>α</mi><mi>Q</mi></mrow></mfenced></mrow><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>α</mi><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi>R</mi></mrow></mfrac></math> 
So increased by  <math><mfrac><mrow><mi>a</mi><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi>R</mi></mrow></mfrac></math>

</details>

---

### Q8. JEE Advanced 2013 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

Two non-conducting spheres of radii <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> and carrying uniform volume charge densities <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>&#961;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>&#961;</mi></math>, respectively, are placed such that they partially overlap, as shown in the figure. At all points in the overlapping region,
<u><strong><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/EM0025819_Quest_1.jpg" style="width: 167px; height: 124px;" /></strong></u>

**Options:**

- **(A)** the electrostatic field is zero.
- **(B)** the electrostatic potential is constant.
- **(C)** the electrostatic field is constant in magnitude.
- **(D)** the electrostatic field has same direction.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) the electrostatic field has same direction.**

**Detailed Solution:**

<p>In triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><msub><mi>C</mi><mn>1</mn></msub><msub><mi>C</mi><mn>2</mn></msub></math>,
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>r</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>+</mo><msub><mover><mi>r</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></math></p><p>
<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/EM0025819_AnsEXp_1_.jpg" style="width: 164px; height: 135px;" /></p><p>The electrostatic field at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>E</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mrow><mi>K</mi><mfenced><mrow><mi>&#961;</mi><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msubsup><mi>R</mi><mn>1</mn><mn>3</mn></msubsup></mrow></mfenced><mfenced><msub><mover><mi>r</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mfenced></mrow><msubsup><mi>R</mi><mn>1</mn><mn>3</mn></msubsup></mfrac><mo>+</mo><mfrac><mrow><mi>K</mi><mfenced><mrow><mi>&#961;</mi><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msubsup><mi>R</mi><mn>2</mn><mn>3</mn></msubsup></mrow></mfenced><mfenced><mrow><mo>-</mo><msub><mover><mi>r</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mrow></mfenced></mrow><msubsup><mi>R</mi><mn>2</mn><mn>3</mn></msubsup></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>E</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>K</mi><mi>&#961;</mi><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><mfenced><mrow><msub><mover><mi>r</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>-</mo><msub><mover><mi>r</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>E</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mi>&#961;</mi><mrow><mn>3</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mover><mi>d</mi><mo>&#8594;</mo></mover></math></p>

</details>

---

### Q9. JEE Advanced 2012 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider a thin spherical shell of radius $R$ with centre at the origin, carrying uniform positive surface charge density. The variation of the magnitude of the electric field $|\vec{E}(r)|$ and the electric potential $V(r)$ with the distance $r$ from the centre, is best represented by which graph?

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/E3m10uZEbKDsryfNH6apC8lG9tonBECzbJDocju9JQk.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ZUWR2PHmFvOetGpbNJ5XeSiX4S1xKyQltlV82kwjSIw.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/etr6C3Rn7FUxZjqQnTXzGHWVwuP02jk7HEZLe3ddo1A.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ikjTnp-ZIgcQMIDCC4C-yNMcYCNlesQGvAePbfXQpaM.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ikjTnp-ZIgcQMIDCC4C-yNMcYCNlesQGvAePbfXQpaM.original.fullsize.png">**

**Detailed Solution:**

For a thin uniformly positive charged spherical shell

(i) Inside the shell at any point

$E=O$ and $V=\frac{1}{4 \pi \in_{0}} \quad \frac{q}{R}=$ constt.

where $q=$ charge on sphere

$R=$ Radius of sphere

(ii) Outside the shell at any point at any distance $r$ from

the centre $E \propto \frac{1}{r^{2}}$ and $V \propto \frac{1}{r}$

</details>

---

### Q10. JEE Advanced 2008 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

Statement 1 For practical purposes, the earth is used as a reference at zero potential in electrical circuits.
and Statement 2 The electrical potential of a sphere of radius $R$ with charge $Q$ uniformly distributed on the surface is given by $\frac{Q}{4 \pi \varepsilon_0 R}$.

**Options:**

- **(A)** Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation for Statement 1.
- **(B)** Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation for Statement 1.
- **(C)** Statement 1 is true, Statement 2 is false.
- **(D)** Statement 1 is false, Statement 2 is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation for Statement 1.**

**Detailed Solution:**

No solution is required.

</details>

---

### Q11. JEE Advanced 2008 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider a system of three charges $\frac{q}{3}, \frac{q}{3}$ and $-\frac{2 q}{3}$ placed at points $A, B$ and $C$, respectively, as shown in the figure. Take $O$ to be the centre of the circle of radius $R$ and angle $C A B=60^{\circ}$.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/h78g_hb3-iGHvg7H2ZK6jg55DjbqxES3XJLSjyLzlNQ.original.fullsize.png">

**Options:**

- **(A)** The electric field at point $O$ is $\frac{q}{8 \pi \varepsilon_0 R^2}$ directed along the negative $x$-axis
- **(B)** The potential energy of the system is zero
- **(C)** The magnitude of the force between the charges at $C$ and $B$ is $\frac{q^2}{54 \pi \varepsilon_0 R^2}$
- **(D)** The potential at point $O$ is $\frac{q}{12 \pi \varepsilon_0 R}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) The magnitude of the force between the charges at $C$ and $B$ is $\frac{q^2}{54 \pi \varepsilon_0 R^2}$**

**Detailed Solution:**

Distance $B C=A B \sin 60^{\circ}=(2 R) \frac{\sqrt{3}}{2}=\sqrt{3} R$
$\therefore \quad\left|F_{B C}\right|=\frac{1}{4 \pi \varepsilon_0} \frac{(q / 3)(2 q / 3)}{(\sqrt{3} R)^2}=\frac{q^2}{54 \pi \varepsilon_0 R^2}$
$\therefore$ correct option is (c).

</details>

---

### Q12. JEE Advanced 2006

*Type:* `multipleCorrect` | *Level:* `2`

For spherical symmetrical charge distribution, variation of electric potential with distance from centre is given in diagram. Given that:
$$
V=\frac{q}{4 \pi \varepsilon_0 R_0} \text { for } r \leq R_0
$$
and $V=\frac{q}{4 \pi \varepsilon_0 r}$ for $r \geq R_0$
Then which option(s) are correct
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/V-TQUHfwYXk9dF9HfnyFSvUsBlv8pTLPm32YbDf339w.original.fullsize.png">

**Options:**

- **(A)** Total charge within $2 R_0$ is $q$
- **(B)** Total electrostatic energy for $r \leq R_0$ is zero
- **(C)** At $r=R_0$ electric field is discontinuous
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) None of these**

**Detailed Solution:**

The given graph is of charged conducting sphere of radius $R_0$. The whole charge $q$ distributes on the surface of the sphere.

</details>

---

