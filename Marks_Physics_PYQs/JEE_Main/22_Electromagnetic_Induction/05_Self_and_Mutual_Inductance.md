# JEE Main Physics - Electromagnetic Induction

## Topic 5: Self and Mutual Inductance

**Total Questions:** 29

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A $30$ cm long solenoid has $10$ turns per cm and area of $5$ cm$^2$. The current through the solenoid coil varies from $2$ A to $4$ A in $3.14$ s. The e.m.f. induced in the coil is $\alpha\times 10^{-5}$ V. The value $\alpha$ is ________.

**Options:**

- **(A)** $60$
- **(B)** $12$
- **(C)** $120$
- **(D)** $34$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $12$**

**Detailed Solution:**

Given:
Length of the solenoid, $l = 30 \text{ cm} = 0.3 \text{ m}$
Number of turns per unit length, $n = 10 \text{ turns/cm} = 1000 \text{ turns/m}$
Area of cross-section, $A = 5 \text{ cm}^2 = 5 \times 10^{-4} \text{ m}^2$
Change in current, $\Delta I = 4 \text{ A} - 2 \text{ A} = 2 \text{ A}$
Time interval, $\Delta t = 3.14 \text{ s}$

The self-inductance of the solenoid is given by:
$L = \mu_0 n^2 A l$

Substituting the given values:
$L = 4\pi \times 10^{-7} \times (1000)^2 \times 5 \times 10^{-4} \times 0.3$
$L = 4\pi \times 10^{-7} \times 10^6 \times 1.5 \times 10^{-4}$
$L = 6\pi \times 10^{-5} \text{ H}$

The magnitude of the induced e.m.f. is:
$e = L \dfrac{\Delta I}{\Delta t}$

Substituting the values of $L$, $\Delta I$, and $\Delta t$:
$e = 6\pi \times 10^{-5} \times \dfrac{2}{3.14}$

Using $\pi \approx 3.14$:
$e = 6 \times 10^{-5} \times 2 = 12 \times 10^{-5} \text{ V}$

Comparing this with $e = \alpha \times 10^{-5} \text{ V}$, we get:
$\alpha = 12$

Answer: $12$

</details>

---

### Q2. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A circular current loop of radius $R$ is placed inside square loop of side length $L$ $(L >> R)$ such that they are co-planar and their centers coincide. The permeability of free space is $\mu_0$. The mutual inductance between circular loop and square loop is _______.

**Options:**

- **(A)** $2\sqrt{2} \, \dfrac{\mu_0 L^2}{R}$
- **(B)** $\sqrt{2} \, \dfrac{\mu_0 L^2}{R}$
- **(C)** $\sqrt{2} \, \dfrac{\mu_0 R^2}{L}$
- **(D)** $2\sqrt{2} \, \dfrac{\mu_0 R^2}{L}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2\sqrt{2} \, \dfrac{\mu_0 R^2}{L}$**

**Detailed Solution:**

Using the reciprocity theorem, assume a current $I$ flows through the larger square loop and compute the flux through the smaller circular loop. The mutual inductance is given by $M = \dfrac{\Phi}{I}$.

Magnetic field at the centre of the square loop:
For a square of side $L$, the perpendicular distance from the centre to any side is $d = \dfrac{L}{2}$, and each side subtends angles $\theta_1 = \theta_2 = 45^\circ$ at the centre.

The field due to one finite straight segment is:
$B_{\text{segment}} = \dfrac{\mu_0 I}{4\pi d}(\sin\theta_1 + \sin\theta_2)$

$B_{\text{segment}} = \dfrac{\mu_0 I}{4\pi \cdot \frac{L}{2}}\left(\dfrac{1}{\sqrt{2}} + \dfrac{1}{\sqrt{2}}\right) = \dfrac{\mu_0 I}{2\pi L} \cdot \sqrt{2} = \dfrac{\sqrt{2}\,\mu_0 I}{2\pi L}$

All four sides contribute equally in the same direction at the centre, so:
$B_{\text{total}} = 4 \cdot \dfrac{\sqrt{2}\,\mu_0 I}{2\pi L} = \dfrac{2\sqrt{2}\,\mu_0 I}{\pi L}$

Flux through the circular loop:
Since $L \gg R$, the field $B_{\text{total}}$ can be treated as uniform over the area $A = \pi R^2$ of the circular loop.

$\Phi = B_{\text{total}} \cdot A = \dfrac{2\sqrt{2}\,\mu_0 I}{\pi L} \cdot \pi R^2 = \dfrac{2\sqrt{2}\,\mu_0 R^2 I}{L}$

Mutual inductance:
$M = \dfrac{\Phi}{I} = \dfrac{2\sqrt{2}\,\mu_0 R^2}{L}$

Hence, the correct option is $(4)\ \dfrac{2\sqrt{2}\,\mu_0 R^2}{L}$.

</details>

---

### Q3. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Suppose a long solenoid of 100 cm length, radius 2 cm having 500 turns per unit length, carries a current $I=10 \sin (\omega \mathrm{t}) \mathrm{A}$, where $\omega=1000 \mathrm{rad}. / \mathrm{s}$. A circular conducting loop $(B)$ of radius 1 cm coaxially slided through the solenoid at a speed $v=1 \mathrm{~cm} / \mathrm{s}$. The r.m.s. current through the loop when the coil $B$ is inserted 10 cm inside the solenoid is $\alpha / \sqrt{2} \mu \mathrm{~A}$. The value of $\alpha$ is $\_\_\_\_$. 
 [Resistance of the loop $=10 \Omega$ ]

**Options:**

- **(A)** 197
- **(B)** 80
- **(C)** 100
- **(D)** 280

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 197**

**Detailed Solution:**

EMF induced $\varepsilon = A \dfrac{dB}{dt} = A\mu_0 n \dfrac{di}{dt}$
$\varepsilon = A\mu_0 n \, i_0 \omega \cos\omega t$
current induced $i = \dfrac{\varepsilon}{R} = \dfrac{\pi r^2 \mu_0 n i_0 \omega}{R} \cos\omega t$
So $i = \dfrac{\pi r^2 \mu_0 n i_0 \omega}{\sqrt{2} R}$
$= \dfrac{\pi \times 10^{-4} \times 4\pi \times 10^{-7} \times 500 \times 10 \times 10^3}{\sqrt{2} \times 10}$
$= \dfrac{20\pi^2}{\sqrt{2}} \times 10^{-6}$
$\simeq \dfrac{197}{\sqrt{2}} \, \mu A$

</details>

---

### Q4. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Three identical coils $C_{1}, C_{2}$ and $C_{3}$ are closely placed such that they share a common axis. $C_{2}$ is exactly midway. $C_{1}$ carries current $I$ in anti-clockwise direction while $C_{3}$ carries current $I$ in clockwise direction. An induced current flows through $C_{2}$ will be in clockwise direction when

**Options:**

- **(A)** $C_{1}$ moves away from $C_{2}$ and $C_{3}$ moves towards $C_{2}$
- **(B)** $C_{1}$ and $C_{3}$ move with equal speeds away from $C_{2}$
- **(C)** $C_{1}$ moves towards $C_{2}$ and $C_{3}$ moves away from $C_{2}$
- **(D)** $C_{1}$ and $C_{3}$ move with equal speeds towards $C_{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $C_{1}$ moves towards $C_{2}$ and $C_{3}$ moves away from $C_{2}$**

**Detailed Solution:**

Let the common axis be the z-axis.
$C_1$ is at $z = -d$, $C_2$ is at $z = 0$, and $C_3$ is at $z = +d$.
Current in $C_1$ is anti-clockwise (ACW), producing a magnetic field $B_1$ in the $+z$ direction at $C_2$.
Current in $C_3$ is clockwise (CW), producing a magnetic field $B_3$ in the $-z$ direction at $C_2$.
The net magnetic field at $C_2$ is $B_{net} = B_1 - B_3$. Since $C_1$ and $C_3$ are equidistant and carry equal current, initially $B_{net} = 0$.

To induce a clockwise current in $C_2$, Lenz's law states that the induced current must oppose the change in flux. A clockwise induced current produces a magnetic field in the $-z$ direction.
This happens if there is an increasing flux in the $+z$ direction or a decreasing flux in the $-z$ direction.

Case 1: $C_1$ moves towards $C_2$. The distance decreases, so $B_1$ (in $+z$ direction) increases. This causes an increasing flux in the $+z$ direction.

Case 2: $C_3$ moves away from $C_2$. The distance increases, so $B_3$ (in $-z$ direction) decreases. This causes a decreasing flux in the $-z$ direction.

Both actions (moving $C_1$ towards $C_2$ and moving $C_3$ away from $C_2$) result in a net change in flux that induces a clockwise current in $C_2$ to oppose the change.
Therefore, option (3) is correct.

</details>

---

### Q5. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider \(\mathrm{I}_1\) and \(\mathrm{I}_2\) are the currents flowing simultaneously in two nearby coils 1 & 2, respectively. If \(\mathrm{L}_1=\) self inductance of coil \(1, \mathrm{M}_{12}=\) mutual inductance of coil 1 with respect to coil 2, then the value of induced emf in coil 1 will be
Options

**Options:**

- **(A)** \(\varepsilon_1=-L_1 \frac{\mathrm{dI}_2}{d t}-\mathrm{M}_{12} \frac{\mathrm{dI}_1}{d t}\)
- **(B)** \(\varepsilon_1=-L_1 \frac{\mathrm{dI}_1}{d t}-\mathrm{M}_{12} \frac{\mathrm{dI}_2}{d t}\)
- **(C)** \(\varepsilon_1=-L_1 \frac{\mathrm{dI}_1}{d t}-\mathrm{M}_{12} \frac{\mathrm{dI}_1}{d t}\)
- **(D)** \(\varepsilon_1=-L_1 \frac{\mathrm{dI}_1}{d t}+\mathrm{M}_{12} \frac{\mathrm{dI}_2}{\mathrm{dt}}\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) \(\varepsilon_1=-L_1 \frac{\mathrm{dI}_1}{d t}-\mathrm{M}_{12} \frac{\mathrm{dI}_2}{d t}\)**

**Detailed Solution:**

$\begin{aligned} & \phi_1=\mathrm{L}_1 \mathrm{I}_1+\mathrm{M}_{12} \mathrm{I}_2 \\ & \varepsilon_1=-\frac{\mathrm{d} \phi_1}{\mathrm{dt}}=-\mathrm{L}_1 \frac{\mathrm{dI}}{1} \frac{\mathrm{I}_{12}}{\mathrm{dt}}-\mathrm{M}_{12} \frac{\mathrm{~d} I_2}{\mathrm{dt}}\end{aligned}$

</details>

---

### Q6. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Regarding self-inductance:
A. The self-inductance of the coil depends on its geometry.
B. Self-inductance does not depend on the permeability of the medium.
C. Self-induced e.m.f. opposes any change in the current in a circuit.
D. Self-inductance is electromagnetic analogue of mass in mechanics.
E. Work needs to be done against self-induced e.m.f. in establishing the current.

Choose the correct answer from the options given below:

**Options:**

- **(A)** $\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{E}$ only
- **(B)** B, C, D, E only
- **(C)** $\mathrm{A}, \mathrm{C}, \mathrm{D}, \mathrm{E}$ only
- **(D)** A, B, C, D only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{A}, \mathrm{C}, \mathrm{D}, \mathrm{E}$ only**

**Detailed Solution:**

A. The self-inductance of the coil depends on its geometry.
This is true because the self-inductance of a coil is given by formulas that include its geometrical parameters (number of turns, cross-sectional area, length, etc.). For example, for a solenoid,
\(L=\mu_0 \mu_r \frac{N^2 A}{l}\)
where \(N\) is the number of turns, \(A\) is the cross-sectional area, and \(l\) is the length.
B. Self-inductance does not depend on the permeability of the medium.
This is false. The permeability of the medium (represented by \(\mu=\mu_0 \mu_r\)) directly influences the inductance, as seen in the formula above. So, any change in the medium's permeability will affect the inductance.
C. Self-induced e.m.f. opposes any change in the current in a circuit.
This is true, and it is a direct consequence of Lenz's law. The induced electromotive force (e.m.f.) always acts in a direction such that it opposes the change in current that produced it.
D. Self-inductance is the electromagnetic analogue of mass in mechanics.
This is true. Just as mass resists changes in velocity (inertia), inductance resists changes in current, which is why it is often compared to the inertial mass in mechanical systems.
E. Work needs to be done against self-induced e.m.f. in establishing the current.
This is true because, when you try to change the current, you must do work to overcome the opposing self-induced e.m.f., storing energy in the magnetic field of the inductor. Based on the above reasoning, the true statements are \(\mathrm{A}, \mathrm{C}, \mathrm{D}\), and E.
Thus, the correct answer is:
Option C
A, C, D, E only

</details>

---

### Q7. JEE Main 2024 (09 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

When a coil is connected across a $20 \mathrm{~V}$ dc supply, it draws a current of $5 \mathrm{~A}$. When it is connected across $20 \mathrm{~V}, 50 \mathrm{~Hz}$ ac supply, it draws a current of $4 \mathrm{~A}$. The self inductance of the coil is ______ $\mathrm{mH}$. $($ Take $\pi=3$ )

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

Case-I:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/40ICr09IOfMfea6ofQ8WIVFtA51c8p0h2VXGoKZWvG8.original.fullsize.png">
$i=\frac{20}{R} \Rightarrow R=4 \Omega$
Case-II:<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/aYHJcavg8RiqhaKYu2Ea7SeQVrTZ5q8hqb7-fDs1Rac.original.fullsize.png">
$\begin{aligned} & \mathrm{i}=\frac{20}{\mathrm{Z}} \\ & 4=\frac{20}{\sqrt{\mathrm{R}^2+\mathrm{X}_{\mathrm{L}}^2}} \Rightarrow \sqrt{\mathrm{R}^2+\mathrm{X}_{\mathrm{L}}^2}=5 \\ & \mathrm{R}^2+\mathrm{X}_{\mathrm{L}}^2=25 \Rightarrow \mathrm{X}_{\mathrm{L}}=3 \Omega \\ & \mathrm{L}=\frac{3}{2 \pi \mathrm{f}}=\frac{1}{2 \times 50}=\frac{1000}{100} \mathrm{mH} \\ & \mathrm{L}=10 \mathrm{mH}\end{aligned}$

</details>

---

### Q8. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In a coil, the current changes from $-2 \mathrm{~A}$ to $+2 \mathrm{~A}$ in $0.2 \mathrm{~s}$ and induces an emf of $0.1 \mathrm{~V}$. The self inductance of the coil is :

**Options:**

- **(A)** $4 \mathrm{mH}$
- **(B)** $1 \mathrm{mH}$
- **(C)** $5 \mathrm{mH}$
- **(D)** $2.5 \mathrm{mH}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5 \mathrm{mH}$**

**Detailed Solution:**

$(E m f)_{\text {induced }}=-L \frac{d i}{d t}$
In magnitude form,
$\begin{aligned}
& \left|\operatorname{Emf}_{\text {ind }}\right|=\left|(-) L \frac{\mathrm{di}}{\mathrm{dt}}\right| \\
& \Rightarrow 0.1=\frac{(\mathrm{L})[+2-(-2)]}{0.2} \\
& \Rightarrow \mathrm{L}=\frac{0.1 \times 0.2}{4}=5 \mathrm{mH}
\end{aligned}$

</details>

---

### Q9. JEE Main 2024 (05 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

The current in an inductor is given by $\mathrm{I}=(3 \mathrm{t}+8)$ where $\mathrm{t}$ is in second. The magnitude of induced emf produced in the inductor is $12 \mathrm{mV}$. The self-inductance of the inductor _____ $\mathrm{mH}$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

$\begin{aligned} & \mathrm{I}=3 \mathrm{t}+8 \\ & \varepsilon=12 \mathrm{mV} \\ & |\varepsilon|=\mathrm{L}\left|\frac{\mathrm{dI}}{\mathrm{dt}}\right| \\ & 12=\mathrm{L} \times 3 \\ & \mathrm{~L}=4 \mathrm{mH}\end{aligned}$

</details>

---

### Q10. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two conducting circular loops A and B are placed in the same plane with their centers coinciding as shown in figure. The mutual inductance between them is :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/U36tbNPWw38Nzax4Rfn2XC_gLMAfxmx0q-nyFveJwNc.original.fullsize.png">

**Options:**

- **(A)** $\frac{\mu_0 \pi b^2}{2 a}$
- **(B)** $\frac{\mu_o}{2 \pi} \cdot \frac{b^2}{a}$
- **(C)** $\frac{\mu_0}{2 \pi} \cdot \frac{a^2}{b}$
- **(D)** $\frac{\mu_0 \pi a^2}{2 b}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\mu_0 \pi a^2}{2 b}$**

**Detailed Solution:**

$\begin{aligned} & \phi=\mathrm{Mi}=\mathrm{BA} \\ & \Rightarrow \mathrm{Mi}=\frac{\mu_0 \mathrm{i}}{2 \mathrm{~b}} \pi \mathrm{a}^2 \\ & \therefore \mathrm{M}=\frac{\mu_0 \pi \mathrm{a}^2}{2 \mathrm{~b}}\end{aligned}$

</details>

---

### Q11. JEE Main 2024 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

A small square loop of wire of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> is placed inside a large square loop of wire of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>L</mi><mo>=</mo><msup><mi>l</mi><mn>2</mn></msup></mrow></mfenced></math>. The loops are coplanar and their centers coincide. The value of the mutual inductance of the system is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>x</mi></msqrt><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup><mo> </mo><mi mathvariant="normal">H</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo></math>______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **128**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8c04d83b-14ba-451a-8567-e05d119ed428.png" style="width: 200px; height: 215px;"/></p><p>Flux linkage for inner loop</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ϕ</mi><mo>=</mo><msub><mi>B</mi><mi>center</mi></msub><mo>×</mo><msup><mi>l</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>×</mo><mfrac><mrow><msub><mi>μ</mi><mn>0</mn></msub><mi>i</mi></mrow><mrow><mn>4</mn><mi mathvariant="normal">π</mi><mstyle displaystyle="true"><mfrac><mi>L</mi><mn>2</mn></mfrac></mstyle></mrow></mfrac><mfenced><mrow><mi>sin</mi><mn>45</mn><mo>°</mo><mo>+</mo><mi>sin</mi><mn>45</mn><mo>°</mo></mrow></mfenced><msup><mi>l</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>ϕ</mi><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mfrac><mrow><msub><mi>μ</mi><mn>0</mn></msub><mi>i</mi></mrow><mrow><mi>π</mi><mi>L</mi></mrow></mfrac><msup><mi>l</mi><mn>2</mn></msup></math></p><p>Therefore, mutual inductance will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfrac><mi>ϕ</mi><mi>i</mi></mfrac><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>μ</mi><mn>0</mn></msub><msup><mi>l</mi><mn>2</mn></msup></mrow><mrow><mi>π</mi><mi>L</mi></mrow></mfrac><mspace linebreak="newline"></mspace><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mfrac><msub><mi>μ</mi><mn>0</mn></msub><mi mathvariant="normal">π</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mi mathvariant="normal">π</mi></mfrac><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><msqrt><mn>2</mn></msqrt><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>128</mn></msqrt><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup><mo> </mo><mi mathvariant="normal">H</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>128</mn></math>.</p>

</details>

---

### Q12. JEE Main 2024 (27 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Two coils have mutual inductance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>002</mn><mo> </mo><mi mathvariant="normal">H</mi></math>. The current changes in the first coil according to the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><msub><mi>i</mi><mn>0</mn></msub><mi>s</mi><mi>i</mi><mi>n</mi><mi>ω</mi><mi>t</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mn>0</mn></msub><mo>=</mo><mn>5</mn><mo> </mo><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ω</mi><mo>=</mo><mn>50</mn><mi>π</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>rad</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>emf</mi></math> in the second coil is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mi>α</mi></mfrac><mo> </mo><mi mathvariant="normal">V</mi></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>The amount of flux induced in the second coil due to the first one is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>ϕ</mi><mn>2</mn></msub></mtd><mtd><mo>=</mo></mtd><mtd><mi>M</mi><mi>i</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mi>M</mi><msub><mi>i</mi><mn>0</mn></msub><mi>s</mi><mi>i</mi><mi>n</mi><mi>ω</mi><mi>t</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></mtd></mtr></mtable></math></p><p>where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is the mutual inductance of the coils.</p><p>The formula to calculate the emf induced can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ε</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mi>d</mi><msub><mi>ϕ</mi><mn>2</mn></msub></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>From equation (2), it follows that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>ε</mi><mi>max</mi></msub></mtd><mtd><mo>=</mo></mtd><mtd><mi>M</mi><msub><mi>i</mi><mn>0</mn></msub><mi>ω</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mn>0</mn><mo>.</mo><mn>002</mn><mo>×</mo><mn>5</mn><mo>×</mo><mn>50</mn><mi>π</mi><mo> </mo><mi mathvariant="normal">V</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mi>π</mi><mn>2</mn></mfrac><mo> </mo><mi mathvariant="normal">V</mi></mtd></mtr></mtable></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mn>2</mn></math>.</p>

</details>

---

### Q13. JEE Main 2023 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>Two concentric circular coils with radii <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>cm</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn><mo>&#160;</mo><mi>cm</mi></math> and number of turns <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn></math> respectively are placed coaxially with centers coinciding. The mutual inductance of this arrangement will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8211;</mo><mn>8</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">H</mi></math>. (Take, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#960;</mi><mn>2</mn></msup><mo>=</mo><mn>10</mn></math>)</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<blockquote><p>Let the magnetic field of the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn></math> turns be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mn>1</mn></msub></math>. The formula of magnetic field is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><mi>i</mi></mrow><mrow><mn>2</mn><mi>r</mi></mrow></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>1000</mn><mo>&#160;</mo><mi>cm</mi></math>. Thus, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mi>n</mi><msub><mi>&#956;</mi><mn>0</mn></msub><mo>&#215;</mo><mi>I</mi></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>10</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>200</mn><msub><mi>&#956;</mi><mn>0</mn></msub><mi>I</mi></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>10</mn></mrow></mfrac></math></p><p>The flux through the coil of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi>cm</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mn>10</mn><mo>&#215;</mo><mfenced><mrow><mover><mi>B</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>A</mi><mo>&#8594;</mo></mover></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><mo>&#215;</mo><msub><mi>B</mi><mn>1</mn></msub><mi>&#960;</mi><msub><msup><mi>r</mi><mn>2</mn></msup><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#981;</mi><mo>=</mo><mn>10</mn><mo>&#215;</mo><mfrac><mrow><mn>200</mn><msub><mi>&#956;</mi><mn>0</mn></msub><mi>I</mi></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>10</mn></mrow></mfrac><mo>&#215;</mo><mi>&#960;</mi><msup><mfenced><mrow><mn>0</mn><mo>.</mo><mn>01</mn></mrow></mfenced><mn>2</mn></msup></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mn>10</mn><mo>&#215;</mo><mfrac><mrow><mn>200</mn><msub><mi>&#956;</mi><mn>0</mn></msub></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>10</mn></mrow></mfrac><mo>&#215;</mo><mi>&#960;</mi><msup><mfenced><mrow><mn>0</mn><mo>.</mo><mn>01</mn></mrow></mfenced><mn>2</mn></msup><mspace linebreak="newline"/><mo>=</mo><mn>10</mn><mo>&#215;</mo><mfrac><mrow><mn>200</mn><mfenced><mrow><mn>4</mn><mi>&#960;</mi><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>10</mn></mrow></mfrac><mo>&#215;</mo><mi>&#960;</mi><msup><mfenced><mrow><mn>0</mn><mo>.</mo><mn>01</mn></mrow></mfenced><mn>2</mn></msup><mspace linebreak="newline"/><mo>=</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">H</mi></math></p></blockquote>

</details>

---

### Q14. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Find the mutual inductance in the arrangement, when a small circular loop of wire of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is placed inside a large square loop of wire of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>(</mo><mi>L</mi><mo>&#8811;</mo><mi>R</mi><mo>)</mo></math>. The loops are coplanar and their centres coincide :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ac83f3be-97d0-4516-98b9-900c9c981097-9894865.png" style="width: 300px; height: 327px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow><mi>L</mi></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><mi>R</mi></mrow><msup><mi>L</mi><mn>2</mn></msup></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow><mi>L</mi></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><mi>R</mi></mrow><msup><mi>L</mi><mn>2</mn></msup></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow><mi>L</mi></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ac83f3be-97d0-4516-98b9-900c9c981097-9894865.png" style="width: 300px; height: 327px;" /></p><p>The magnetic field due to the rectangular loop at its centre is:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>4</mn><mo>&#215;</mo><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><mi>i</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>L</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow></mfrac><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><mi>i</mi></mrow><mrow><mi>&#960;</mi><mi>L</mi></mrow></mfrac></math></p><p>Therefore, the flux through the circular loop <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mi>&#960;</mi><msup><mi>R</mi><mn>2</mn></msup><mo>&#215;</mo><mi>B</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup><mi>i</mi></mrow><mi>L</mi></mfrac></math></p><p>If M is the mutual inductance, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mfrac><mrow><mo>d</mo><mi>i</mi></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>d</mo><mi>&#981;</mi></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow><mi>L</mi></mfrac><mfrac><mrow><mi mathvariant="normal">d</mi><mi>i</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi>t</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>M</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow><mi>L</mi></mfrac></math></p>

</details>

---

### Q15. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>A small square loop of wire of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> is placed inside a large square loop of wire <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mfenced><mrow><mi>L</mi><mo>&#8811;</mo><mi>l</mi></mrow></mfenced></math>. Both loops are coplanar and their centres coincide at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> as shown in figure. The mutual inductance of the system is</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bb2446ca-823a-4a72-bf46-3cc1db8f0449-image.png" style="width: 150px; height: 170px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mi>L</mi><mn>2</mn></msup></mrow><mrow><mi>&#960;</mi><mi>l</mi></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mi>l</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mi>&#960;</mi><mi>L</mi></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mi>L</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mi>&#960;</mi><mi>l</mi></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mi>l</mi><mn>2</mn></msup></mrow><mrow><mi>&#960;</mi><mi>L</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mi>l</mi><mn>2</mn></msup></mrow><mrow><mi>&#960;</mi><mi>L</mi></mrow></mfrac></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/db54367e-5890-4534-988f-c7bfec6a66dc-image.png" style="width: 382px; height: 200px;" /></p><p>Let a current, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> pass through the square loop of side, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math>. The magnetic field at the centre <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>4</mn><mo>&#215;</mo><mi>Magnetic</mi><mo>&#160;</mo><mi>field</mi><mo>&#160;</mo><mi>due</mi><mo>&#160;</mo><mi>to</mi><mo>&#160;</mo><mi>each</mi><mo>&#160;</mo><mo>side</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>B</mi><mo>=</mo><mn>4</mn><mo>&#215;</mo><mfrac><msub><mi>&#956;</mi><mn>0</mn></msub><mrow><mn>4</mn><mi>&#960;</mi></mrow></mfrac><mo>&#8901;</mo><mfrac><mi>I</mi><mrow><mi>L</mi><mo>/</mo><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mi>sin</mi><mo>&#160;</mo><msup><mn>45</mn><mo>&#8728;</mo></msup><mo>+</mo><mi>sin</mi><mo>&#160;</mo><msup><mn>45</mn><mo>&#8728;</mo></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>B</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msub><mi>&#956;</mi><mn>0</mn></msub><mi>I</mi></mrow><mrow><mi>&#960;</mi><mi>L</mi></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><mi>I</mi></mrow><mrow><mi>&#960;</mi><mi>L</mi></mrow></mfrac></math></p></blockquote><blockquote><p>Magnetic flux linked with the small square loop,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mi>B</mi><mi>A</mi><mo>=</mo><mi>B</mi><msup><mi>l</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><mi>I</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mrow><mi>&#960;</mi><mi>L</mi></mrow></mfrac></math></p><p>Mutual inductance of the coil, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfrac><mi>&#981;</mi><mi>I</mi></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mi>l</mi><mn>2</mn></msup></mrow><mrow><mi>&#960;</mi><mi>L</mi></mrow></mfrac></math>.</p></blockquote>

</details>

---

### Q16. JEE Main 2022 (25 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

The current in a coil of self inductance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mn>2</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">H</mi></math> is increasing according to the law <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mn>2</mn><mi>sin</mi><mfenced><msup><mi>t</mi><mn>2</mn></msup></mfenced></math>. Find the amount of energy spent (in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">J</mi></math>) during the period when the current changes from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>Let the current be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>A</mi></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mi>&#964;</mi></math>
Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>=</mo><mn>2</mn><mi>s</mi><mi>i</mi><mi>n</mi><msup><mi>&#964;</mi><mn>2</mn></msup><mo>&#8658;</mo><mi>&#964;</mi><mo>=</mo><msqrt><mi>&#960;</mi><mo>/</mo><mn>2</mn></msqrt></math>
when the instantaneous current is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math>, the
self-induced emf is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mfrac><mrow><mi>d</mi><mi>i</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>q</mi></math> amount of
charge is displaced in time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>t</mi></math>, then elementary work done
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mi>L</mi><mfrac><mrow><mi>d</mi><mi>i</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>q</mi><mo>=</mo><mi>L</mi><mfrac><mrow><mi>d</mi><mi>i</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mi>i</mi><mi>d</mi><mi>t</mi><mo>=</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>L</mi><mi>i</mi><mi>d</mi><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>W</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>t</mi></msubsup><mo>&#160;</mo><mi>L</mi><mi>i</mi><mi>d</mi><mi>i</mi></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>t</mi></msubsup><mi>L</mi><mn>2</mn><mi>s</mi><mi>i</mi><mi>n</mi><msup><mi>t</mi><mn>2</mn></msup><mi>d</mi><mfenced><mrow><mn>2</mn><mi>s</mi><mi>i</mi><mi>n</mi><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>W</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>t</mi></msubsup><mn>8</mn><mi>L</mi><mi>s</mi><mi>i</mi><mi>n</mi><msup><mi>t</mi><mn>2</mn></msup><mi>c</mi><mi>o</mi><mi>s</mi><msup><mi>t</mi><mn>2</mn></msup><mi>t</mi><mi>d</mi><mi>t</mi><mo>=</mo><mn>4</mn><mi>L</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mi>t</mi></msubsup><mi>s</mi><mi>i</mi><mi>n</mi><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup><mi>d</mi><mi>t</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup><mo>&#8658;</mo><mi>d</mi><mi>&#952;</mi><mo>=</mo><mn>4</mn><mi>t</mi><mi>d</mi><mi>t</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> the integral
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mi>L</mi><mo>&#8747;</mo><mi>s</mi><mi>i</mi><mi>n</mi><mi>&#952;</mi><mi>d</mi><mi>t</mi><mo>/</mo><mn>4</mn><mi>L</mi><mo>(</mo><mo>-</mo><mi>c</mi><mi>o</mi><mi>s</mi><mi>&#952;</mi><mo>)</mo><mo>=</mo><mo>-</mo><mi>L</mi><mi>c</mi><mi>o</mi><mi>s</mi><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><mi>W</mi><mo>=</mo><mo>-</mo><msubsup><mfenced open="[" close="]"><mrow><mi>c</mi><mi>o</mi><mi>s</mi><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mn>0</mn><msqrt><mi>&#960;</mi><mo>/</mo><mn>2</mn></msqrt></msubsup><mo>=</mo><mn>2</mn><mi>L</mi><mo>=</mo><mn>4</mn><mi>J</mi></math></p>

</details>

---

### Q17. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A small square loop of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and one turn is placed inside a larger square loop of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> and one turn <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>b</mi><mo>&#8811;</mo><mi>a</mi><mo>)</mo><mo>.</mo></math> The two loops are coplanar with their centres coinciding. If a current <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> is passed in the square loop of side  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>,</mo></math> then the coefficient of mutual inductance between the two loops is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>&#956;</mi><mn>0</mn></msub><mrow><mn>4</mn><mi>&#960;</mi></mrow></mfrac><mn>8</mn><msqrt><mn>2</mn></msqrt><mfrac><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mrow><mo>&#160;</mo><mi mathvariant="normal">b</mi></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>&#956;</mi><mn>0</mn></msub><mrow><mn>4</mn><mi>&#960;</mi></mrow></mfrac><mn>8</mn><msqrt><mn>2</mn></msqrt><mfrac><msup><mi mathvariant="normal">b</mi><mn>2</mn></msup><mi mathvariant="normal">a</mi></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>&#956;</mi><mn>0</mn></msub><mrow><mn>4</mn><mi>&#960;</mi></mrow></mfrac><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mo>&#160;</mo><mi mathvariant="normal">b</mi></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>&#956;</mi><mn>0</mn></msub><mrow><mn>4</mn><mi>&#960;</mi></mrow></mfrac><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt></mrow><mi>a</mi></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>&#956;</mi><mn>0</mn></msub><mrow><mn>4</mn><mi>&#960;</mi></mrow></mfrac><mn>8</mn><msqrt><mn>2</mn></msqrt><mfrac><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mrow><mo>&#160;</mo><mi mathvariant="normal">b</mi></mrow></mfrac></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/61eaa9c3-1955-47eb-b070-8bb0816d59e5-image.png" style="width: 300px; height: 152px;" />|
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>4</mn><mo>&#215;</mo><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><mi>i</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><mfenced><mfrac><mi>b</mi><mn>2</mn></mfrac></mfenced></mrow></mfrac><msqrt><mn>2</mn></msqrt></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>B</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><mi>i</mi></mrow><mrow><mi>&#960;</mi><mi>b</mi></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#981;</mi><mo>=</mo><mi>M</mi><mi>I</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>B</mi><mi>A</mi><mo>=</mo><mi>M</mi><mi>I</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><mi>i</mi></mrow><mrow><mi>&#960;</mi><mi>b</mi></mrow></mfrac><mo>&#183;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mi>M</mi><mi>i</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>M</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mi>a</mi><mn>2</mn></msup></mrow><mrow><mi>&#960;</mi><mi>b</mi></mrow></mfrac><mo>=</mo><mfrac><msub><mi>&#956;</mi><mn>0</mn></msub><mrow><mn>4</mn><mi>&#960;</mi></mrow></mfrac><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt><msup><mi>a</mi><mn>2</mn></msup></mrow><mi>b</mi></mfrac></math>

</details>

---

### Q18. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An inductance coil has a reactance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> . When an AC signal of frequency <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn><mo>&#160;</mo><mi>Hz</mi></math> is applied to the coil, the applied voltage leads the current by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>&#176;</mo></math>. The self-inductance of the coil is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">H</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">H</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>5</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">H</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>.</mo><mn>7</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">H</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">H</mi></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan&#952;</mi><mo>=</mo><mfrac><msub><mi mathvariant="normal">x</mi><mi mathvariant="normal">L</mi></msub><mi mathvariant="normal">R</mi></mfrac><mo>=</mo><mi>tan</mi><mn>45</mn><mo>&#176;</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">x</mi><mi mathvariant="normal">L</mi></msub><mo>=</mo><mi mathvariant="normal">R</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>100</mn><mo>=</mo><msqrt><msubsup><mi mathvariant="normal">x</mi><mi mathvariant="normal">L</mi><mn>2</mn></msubsup><mo>+</mo><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>=</mo><msqrt><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mi mathvariant="normal">R</mi><mo>=</mo><mn>100</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mo>=</mo><mn>50</mn><msqrt><mn>2</mn></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi mathvariant="normal">x</mi><mi mathvariant="normal">L</mi></msub><mo>=</mo><mn>50</mn><msqrt><mn>2</mn></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L&#969;</mi><mo>=</mo><mn>50</mn><msqrt><mn>2</mn></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi><mo>=</mo><mfrac><mrow><mn>50</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi><mo>&#215;</mo><mn>1000</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>25</mn><msqrt><mn>2</mn></msqrt></mrow><mi mathvariant="normal">&#960;</mi></mfrac><mi>mH</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>.</mo><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mi mathvariant="normal">H</mi></math>

</details>

---

### Q19. JEE Main 2020 (09 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

In a fluorescent lamp choke (a small transformer) <math><mn>100</mn><mi></mi><mi>V</mi></math> of reverse voltage is produced when the choke current changes uniformly from <math><mn>0.25</mn><mi></mi><mi>A</mi></math> to <math><mn>0</mn></math> in a duration of <math><mn>0.025</mn><mi></mi><mi>m</mi><mi>s</mi></math> . The self-inductance of the choke (in <math><mi>m</mi><mi>H</mi></math> ) is estimated to be ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<math><mn>100</mn><mo>=</mo><mfrac><mrow><mi>L</mi><mfenced separators="|"><mrow><mn>0.25</mn></mrow></mfenced></mrow><mrow><mn>0.025</mn></mrow></mfrac><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></msup></math>
<math><mo>&#8756;</mo><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>L</mi><mo>=</mo><mn>100</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>4</mn></mrow></msup><mi>H</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi>m</mi><mi>H</mi></math>

</details>

---

### Q20. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The total number of turns and cross-section area in a solenoid is fixed. However, its length <math><mi mathvariant="normal">L</mi></math> is varied by adjusting the separation between windings. The inductance of solenoid will be proportional to:

**Options:**

- **(A)** <math><mi mathvariant="normal">L</mi></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">L</mi></mrow></mfrac></math>
- **(D)** <math><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">L</mi></mrow></mfrac></math>**

**Detailed Solution:**

Self-Inductance <math><mo>=</mo><msub><mrow><mi mathvariant="normal">μ</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">π</mi><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">L</mi></math> (n = number of turns per unit length) 
<math><mo>=</mo><msub><mrow><mi mathvariant="normal">μ</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mi mathvariant="normal">L</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">π</mi><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">L</mi></math>  
<math><mo>=</mo><mfrac><mrow><msub><mrow><mi mathvariant="normal">μ</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">π</mi><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">L</mi></mrow></mfrac></math>  
Self-Inductance <math><mo>∝</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">L</mi></mrow></mfrac></math>

</details>

---

### Q21. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A copper wire is wound on a wooden frame, whose shape is that of an equilateral triangle. If the linear dimension of each side of the frame is increased by a factor of $3,$ keeping the number of turns of the coil per unit length of the frame the same, then the self inductance of the coil:

**Options:**

- **(A)** decreases by a factor of 9
- **(B)** increases by a factor of 27
- **(C)** increases by a factor of 3
- **(D)** decreases by a factor of $9 \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) increases by a factor of 3**

**Detailed Solution:**

As total length $L$ of the wire will remain constant

$$

\mathrm{L}=(3 \mathrm{a}) \mathrm{N} \quad(\mathrm{N}=\text { total turns })

$$

and length of winding $=(\mathrm{d}) \mathrm{N}$

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/AwhDsCHiFGmqnF3aQf06y5-65Q23Nslyy8btneTYKEo.original.fullsize.png">


(d = diameter of wire)

$$

\begin{array}{l}

\text { self inductance }=\mu_{0} \mathrm{n}^{2} \mathrm{~A} \ell \\

\quad=\mu_{0} \mathrm{n}^{2}\left(\frac{\sqrt{3} \mathrm{a}^{2}}{4}\right) \mathrm{d} \mathrm{N} \\

\quad \propto \mathrm{a}^{2} \mathrm{~N} \propto \mathrm{a}\left[\text { as } \mathrm{N}=\mathrm{L} / 3 \mathrm{a} \Rightarrow \mathrm{N} \propto \frac{1}{\mathrm{a}}\right]

\end{array}

$$

Now 'a' increased to ' $3 \mathrm{a}$ ' So self inductance will become 3 times

</details>

---

### Q22. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

There are two long co-axial solenoids of same length $l$. The inner and outer coils have radii $r_{1}$ and $r_{2}$ and number of turns per unit length $\mathrm{n}_{1}$ and $\mathrm{n}_{2}$, respectively. The ratio of mutual inductance to the self-inductance of the inner-coil is :

**Options:**

- **(A)** $\frac{n_{1}}{n_{2}}$
- **(B)** $\frac{n_{2}}{n_{1}} \cdot \frac{r_{1}}{r_{2}}$
- **(C)** $\frac{n_{2}}{n_{1}} \cdot \frac{r_{2}^{2}}{r_{1}^{2}}$
- **(D)** $\frac{n_{2}}{n_{1}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{n_{2}}{n_{1}}$**

**Detailed Solution:**

The rate of mutual inductance is given by

$$

\mathrm{M}=\mu_{0} \mathrm{n}, \mathrm{n}_{2} \pi \mathrm{r}_{1}^{2} \quad \ldots(\mathrm{i})

$$

The rate of self inductance is given by

$\mathrm{L}=\mu_{0} \mathrm{n}_{1}^{2} \pi \mathrm{r}_{1}^{2} \quad \ldots(\mathrm{ii})$

Dividing (i) by (ii) $\Rightarrow \frac{\mathrm{M}}{\mathrm{L}}=\frac{\mathrm{n}_{2}}{\mathrm{n}_{1}}$

</details>

---

### Q23. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

When the current in a coil changes from <math> <mrow> <mtext>5&#160;A</mtext></mrow> </math> to <math> <mrow> <mtext>2&#160;A</mtext></mrow> </math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>0</mtext><mtext>.1&#160;s</mtext></math>, an average voltage of <math> <mrow> <mtext>50</mtext><mtext>&#8201;</mtext><mtext>V</mtext></mrow> </math> is produced. The self-inductance of the coil is

**Options:**

- **(A)** <math> <mrow> <mtext>1</mtext><mtext>.67&#160;H</mtext></mrow> </math>
- **(B)** <math > <mrow>  <mtext>6&#x00A0;H</mtext></mrow></math>
- **(C)** <math > <mrow>  <mtext>3&#x00A0;H</mtext></mrow></math>
- **(D)** <math > <mrow>  <mtext>0</mtext><mtext>.67&#x00A0;H</mtext></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mrow> <mtext>1</mtext><mtext>.67&#160;H</mtext></mrow> </math>**

**Detailed Solution:**

Magnetic flux

<math><mi>ϕ</mi><mo>=</mo><mi>L</mi><mi>I</mi><mi> </mi><mo>⇒</mo><mi> </mi><mfrac><mrow><mo>∆</mo><mi>ϕ</mi></mrow><mrow><mo>∆</mo><mi>t</mi></mrow></mfrac><mo>=</mo><mi>L</mi><mi> </mi><mfrac><mrow><mo>∆</mo><mi>I</mi></mrow><mrow><mo>∆</mo><mi>t</mi></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mi> </mi><msub><mfenced separators="|"><msub><mi>ε</mi><mi>ind</mi></msub></mfenced><mi>average</mi></msub><mo>=</mo><mi> </mi><mfenced close="|" open="|" separators="|"><mfrac><mrow><mo>∆</mo><mi>ϕ</mi></mrow><mrow><mo>∆</mo><mi>t</mi></mrow></mfrac></mfenced><mo>=</mo><mi>L</mi><mi> </mi><mfenced close="|" open="|" separators="|"><mfrac><mrow><mo>∆</mo><mi>I</mi></mrow><mrow><mo>∆</mo><mi>t</mi></mrow></mfrac></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo> </mo><mn>50</mn><mo>=</mo><mi>L</mi><mi> </mi><mo>×</mo><mi> </mi><mfrac><mrow><mn>5</mn><mo>-</mo><mn>2</mn></mrow><mn>0.1</mn></mfrac></math>

<math><mo>⇒</mo><mi> </mi><mi> </mi><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mi>L</mi></math>

<math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi>L</mi><mo>=</mo><mn>1.67</mn><mi> </mi><mn>H</mn></math>

</details>

---

### Q24. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Two coils, $\mathrm{X}$ and $\mathrm{Y}$, are kept in close vicinity of each other. When a varying current, $I(t)$, flows through coil $\mathrm{X}$, the induced $\operatorname{emf}(V(t))$ in coil $\mathrm{Y}$, varies in the manner shown here. The variation of $I(t)$, with time, can then be represented by the graph labelled as graph :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/PcPu9mFaCqLNVvcG4G14fnist3GS8AGm-M4z-usRHQ8.original.fullsize.png">

(A)<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/wdMNqTr_ei7Bx9h1aeu_cth3DDTr41d8HcKciXD8dHw.original.fullsize.png">

(B)<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/NL1N44opfaOnf8RxLwz4xg1vVmDyVB7T4FxSe7P6wbA.original.fullsize.png">

(C)<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/m9toxfyfv0_tavqtrn8PdfTuuZBkmAssF-9kRbjm3Ds.original.fullsize.png">

(D)<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/o3g3w8a1yR14NlEuNjh_bBiDS6QOiDPVfv3nsBfh3IY.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{A}$
- **(B)** $\mathrm{C}$
- **(C)** $\mathrm{B}$
- **(D)** $\mathrm{D}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{A}$**

**Detailed Solution:**

Induced emf
$\varepsilon \propto \frac{-\mathrm{di}}{\mathrm{dt}}$

</details>

---

### Q25. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `2`

This question has Statement 1 and Statement 2. Of the four choices given after the Statements, choose the one that best describes the two Statements.
Statement 1: Self inductance of a long solenoid of length $L$, total number of turns $\mathrm{N}$ and radius $\mathrm{r}$ is less than $\frac{\pi \mu_0 N^2 r^2}{L}$.
Statement 2: The magnetic induction in the solenoid in Statement 1 carrying current $I$ is $\frac{\mu_0 N I}{L}$ in the middle of the solenoid but becomes less as we move towards its ends.

**Options:**

- **(A)** Statement 1 is true, Statement 2 is false.
- **(B)** Statement 1 is true, Statement 2 is true, Statement 2 is the correct explanation of Statement 1.
- **(C)** Statement 1 is false, Statement 2 is true.
- **(D)** Statement 1 is true, Statement 2 is true, Statement 2 is not the correct explanation of Statement 1.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement 1 is true, Statement 2 is true, Statement 2 is the correct explanation of Statement 1.**

**Detailed Solution:**

Self inductance of a long solenoid is given by
$$
L=\frac{\mu_0 N^2 A}{l}
$$
Magnetic field at the centre of solenoid
$$
B=\frac{\mu_0 N I}{l}
$$
So both the statements are correct and statement 2 is correct explanation of statement 1

</details>

---

### Q26. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `1`

Two coaxial solenoids are made by winding thin insulated wire over a pipe of cross sectional area $A=$ $10 \mathrm{~cm}^2$ and length $=20 \mathrm{~cm}$. If one of the solenoids has 300 turns and the other 400 turns, their mutual inductance is $\left(\mu_0=4 \pi \times 10^{-7} \mathrm{Tm} \mathrm{A}^{-1}\right)$

**Options:**

- **(A)** $2.4 \pi \times 10^{-5} \mathrm{H}$
- **(B)** $4.8 \pi \times 10^{-4} \mathrm{H}$
- **(C)** $4.8 \pi \times 10^{-5} \mathrm{H}$
- **(D)** $2.4 \pi \times 10^{-4} \mathrm{H}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2.4 \pi \times 10^{-4} \mathrm{H}$**

**Detailed Solution:**

$$
M=\frac{\mu_0 N_1 N_2 A}{\ell}=2.4 \pi \times 10^{-4} \mathrm{H}
$$

</details>

---

### Q27. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

The self inductance of the motor of an electric fan is $10 \mathrm{H}$. In order to impart maximum power at $50 \mathrm{~Hz}$, it should be connected to a capacitance of

**Options:**

- **(A)** $C=4 \mu F$
- **(B)** $C=8 \mu F$
- **(C)** $C=1 \mu F$
- **(D)** $C=2 \mu F$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $C=1 \mu F$**

**Detailed Solution:**

$f=\frac{1}{2 \pi \sqrt{L C}}$
$C=\frac{1}{4 \times \pi^2 f^2 \times 10}$
$C=1 \mu F$

</details>

---

### Q28. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

When the current changes from $+2 \mathrm{~A}$ to $-2 \mathrm{~A}$ in $0.05$ second, an e.m.f. of $8 \mathrm{~V}$ is induced in a coil. The coefficient of self-induction of the coil is

**Options:**

- **(A)** $0.2 \mathrm{H}$
- **(B)** $0.4 \mathrm{H}$
- **(C)** $0.8 \mathrm{H}$
- **(D)** $0.1 \mathrm{H}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.1 \mathrm{H}$**

**Detailed Solution:**

$e=-\mathrm{L} \frac{\mathrm{dl}}{\mathrm{dt}} \Rightarrow 8=(\mathrm{L}) \frac{2-(-2)}{0.05} \Rightarrow \mathrm{L}=0.1 \mathrm{H}$

</details>

---

### Q29. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

Two coils are placed close to each other. The mutual inductance of the pair of coils depends upon

**Options:**

- **(A)** the rates at which currents are changing in the two coils
- **(B)** relative position and orientation of the two coils
- **(C)** the materials of the wires of the coils.
- **(D)** the currents in the two coils

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) relative position and orientation of the two coils**

**Detailed Solution:**

No Solution Available

</details>

---

