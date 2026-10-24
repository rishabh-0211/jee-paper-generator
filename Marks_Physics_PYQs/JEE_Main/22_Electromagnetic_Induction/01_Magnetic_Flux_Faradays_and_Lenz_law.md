# JEE Main Physics - Electromagnetic Induction

## Topic 1: Magnetic Flux, Faraday's and Lenz law

**Total Questions:** 45

---

### Q1. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A square loop of side $2$ cm is placed in a time varying magnetic field with magnitude as $B = 0.4\sin(300t)$ Tesla. The normal to the plane of loop makes an angle of $60°$ with the field. The maximum induced emf produced in the loop is __________ mV.

**Options:**

- **(A)** $12$
- **(B)** $18$
- **(C)** $21$
- **(D)** $24$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $24$**

**Detailed Solution:**

Given:
Side of the square loop, $a = 2$ cm $= 2 \times 10^{-2}$ m
Area of the loop, $A = a^2 = 4 \times 10^{-4}$ m$^2$
Magnetic field, $B = 0.4 \sin(300t)$ T
Angle between the normal to the plane and the magnetic field, $\theta = 60^\circ$

The magnetic flux through the loop is given by:
$\Phi = \vec{B} \cdot \vec{A} = B A \cos\theta$
$\Phi = (0.4 \sin(300t))(4 \times 10^{-4}) \cos(60^\circ)$
$\Phi = 1.6 \times 10^{-4} \sin(300t) \times \dfrac{1}{2}$
$\Phi = 0.8 \times 10^{-4} \sin(300t)$ Wb

By Faraday's law of induction, the induced emf is:
$e = -\dfrac{d\Phi}{dt}$
$e = -\dfrac{d}{dt} (0.8 \times 10^{-4} \sin(300t))$
$e = -0.8 \times 10^{-4} \times 300 \cos(300t)$
$e = -240 \times 10^{-4} \cos(300t)$ V
$e = -24 \times 10^{-3} \cos(300t)$ V

The maximum induced emf is the amplitude of $e$:
$e_{\text{max}} = 24 \times 10^{-3}$ V $= 24$ mV

Answer: $24$

</details>

---

### Q2. JEE Main 2026 (05 April Shift 2)

*Type:* `numerical` | *Level:* `2`

A circular loop of radius $20\text{ cm}$ and resistance $2\ \Omega$ is placed in a time varying magnetic field $\vec{B} = (2t^2 + 2t + 3)\text{ T}$. At $t = 0$, for the plane of the loop being perpendicular to the magnetic field and, the induced current in the loop at $t = 3\text{ s}$ is $\dfrac{\alpha}{50}\text{ A}$. The value of $\alpha$ is _______.
(Take $\pi = 22/7$)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **44**

**Detailed Solution:**

The magnetic flux linked with the circular loop is given by $\Phi = BA \cos \theta$. Since the plane of the loop is perpendicular to the magnetic field, the angle between the area vector and the magnetic field is $\theta = 0^{\circ}$.

$\Phi = B \cdot \pi r^2$

Given $r = 20\text{ cm} = 0.2\text{ m}$, the area of the loop is:

$A = \pi (0.2)^2 = 0.04\pi\text{ m}^2$

The induced emf in the loop is given by Faraday's law of induction:

$|E| = \dfrac{d\Phi}{dt} = A \dfrac{dB}{dt}$

Given the magnetic field $B = 2t^2 + 2t + 3$, we differentiate it with respect to time $t$:

$\dfrac{dB}{dt} = \dfrac{d}{dt}(2t^2 + 2t + 3) = 4t + 2$

At $t = 3\text{ s}$, the rate of change of the magnetic field is:

$\dfrac{dB}{dt} = 4(3) + 2 = 14\text{ T/s}$

Now, substituting the values into the emf equation:

$|E| = 0.04\pi \times 14 = 0.56\pi\text{ V}$

The induced current $I$ in the loop is:

$I = \dfrac{|E|}{R} = \dfrac{0.56\pi}{2} = 0.28\pi\text{ A}$

Using $\pi = \dfrac{22}{7}$, we get:

$I = 0.28 \times \dfrac{22}{7} = 0.04 \times 22 = 0.88\text{ A}$

We are given that the induced current is $\dfrac{\alpha}{50}\text{ A}$. Equating the two values:

$\dfrac{\alpha}{50} = 0.88$

$\alpha = 0.88 \times 50 = 44$

Answer: $44$

</details>

---

### Q3. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

When a coil is placed in a time dependent magnetic field the power dissipated in it is $P$. The number of turns, area of the coil and radius of the coil wire are $N$, $A$ and $r$ respectively. For a second coils number of turns, area of the coil and radius of the coil wire are $2N$, $2A$ and $3r$ respectively. When the first coil is replaced with second coil the power dissipated in it is $\sqrt{2}\,\alpha P$. The value of $\alpha$ is _______.

**Options:**

- **(A)** $36$
- **(B)** $128\sqrt{2}$
- **(C)** $16$
- **(D)** $64$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $36$**

**Detailed Solution:**

The induced emf in the coil is given by Faraday's law:

$E = N A \dfrac{dB}{dt}$

The resistance of the coil is $R = \rho \dfrac{l}{a}$, where $l$ is the total length of the wire and $a$ is its cross-sectional area.

The length of the wire is $l = N (2\pi R_c)$, where $R_c$ is the radius of the coil. Since the area of the coil is $A = \pi R_c^2$, we have $R_c = \sqrt{\dfrac{A}{\pi}}$.

Thus, $l = 2N\sqrt{\pi A}$.

The cross-sectional area of the wire is $a = \pi r^2$.

Therefore, the resistance is:

$R = \rho \dfrac{2N\sqrt{\pi A}}{\pi r^2} \propto \dfrac{N\sqrt{A}}{r^2}$

The power dissipated in the coil is:

$P = \dfrac{E^2}{R} \propto \dfrac{(N A)^2}{\dfrac{N\sqrt{A}}{r^2}} = N A^{3/2} r^2$

For the second coil, the parameters are $N' = 2N$, $A' = 2A$, and $r' = 3r$. The new power dissipated is:

$P' = P \left(\dfrac{2N}{N}\right) \left(\dfrac{2A}{A}\right)^{3/2} \left(\dfrac{3r}{r}\right)^2$

$P' = P (2) (2\sqrt{2}) (9) = 36\sqrt{2} P$

Given that $P' = \sqrt{2}\alpha P$, we can compare the expressions to find:

$\sqrt{2}\alpha = 36\sqrt{2} \Rightarrow \alpha = 36$

Answer: $36$

</details>

---

### Q4. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A circular loop of radius 7 cm is placed in uniform magnetic field of 0.2 T directed perpendicular to plane of loop. The loop is converted into a square loop in 0.5 s. The EMF induced in the loop is $\_\_\_\_$ mV.

**Options:**

- **(A)** 13.2
- **(B)** 1.32
- **(C)** 8.25
- **(D)** 6.6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1.32**

**Detailed Solution:**

Circular loop with radius $r = 0.07$ m in magnetic field $B = 0.2$ T.
Initial flux through circular loop: $\Phi_1 = B \times \pi r^2 = 0.2 \times \pi(0.07)^2 = 0.000980\pi$ Wb
The loop is converted to a square maintaining the same perimeter: $C = 2\pi r = 0.14\pi$ m
Side of square: $a = \frac{0.14\pi}{4} = 0.035\pi$ m
Final flux through square loop: $\Phi_2 = B \times a^2 = 0.2 \times (0.035\pi)^2 = 0.2 \times 0.001225\pi^2$ Wb
Evaluating: $\Phi_1 = 0.2 \times 0.0154 = 0.00308$ Wb
$\Phi_2 = 0.2 \times 0.001225 \times 9.87 = 0.00242$ Wb
Change in flux: $\Delta\Phi = 0.00308 - 0.00242 = 0.00066$ Wb
Average EMF: $\varepsilon = \frac{\Delta\Phi}{\Delta t} = \frac{0.00066}{0.5} = 0.00132$ V $= 1.32$ mV

</details>

---

### Q5. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A conducting circular loop of area $1.0 \mathrm{~m}^{2}$ is placed perpendicular to a magnetic field which varies as $B=\sin (100 t)$ Tesla. If the resistance of the loop is $100 \Omega$, then the average thermal energy dissipated in the loop in one period is $\_\_\_\_$ J.

**Options:**

- **(A)** $\pi^{2}$
- **(B)** $\pi$
- **(C)** $\frac{\pi}{2}$
- **(D)** $2 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\pi$**

**Detailed Solution:**

Flux: $\phi = BA = \sin(100t)$ Wb
Induced EMF: $\varepsilon = -\frac{d\phi}{dt} = -100\cos(100t)$ V
Induced current: $I = \frac{\varepsilon}{R} = -\cos(100t)$ A
Power dissipated: $P = I^2R = 100\cos^2(100t)$ W
Average power: $P_{avg} = \frac{1}{2} \times 100 = 50$ W
Time period: $T = \frac{2\pi}{100}$ s
Energy in one period: $E = P_{avg} \times T = 50 \times \frac{2\pi}{100} = \pi$ J

</details>

---

### Q6. JEE Main 2024 (04 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

A rod of length $60 \mathrm{~cm}$ rotates with a uniform angular velocity $20 \mathrm{rad} \mathrm{s}^{-1}$ about its perpendicular bisector, in a uniform magnetic filed $0.5 T$. The direction of magnetic field is parallel to the axis of rotation. The potential difference between the two ends of the rod is _____V.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/pY5NTwDivYJtX6CHaY0E8FN4ZcowSiTO_6MYgFE6tPk.original.fullsize.png">
$\begin{aligned} & \because \mathrm{V}_0-\mathrm{V}_{\mathrm{A}}=\frac{\mathrm{B} \omega \ell^2}{2} \\ & \mathrm{~V}_0-\mathrm{V}_{\mathrm{B}}=\frac{\mathrm{B} \omega \ell^2}{2} \\ & \therefore \mathrm{V}_{\mathrm{A}}=\mathrm{V}_{\mathrm{B}} \therefore \mathrm{V}_{\mathrm{A}}-\mathrm{V}_{\mathrm{B}}=0\end{aligned}$

</details>

---

### Q7. JEE Main 2024 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

The magnetic flux <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ϕ</mi></math> (in weber) linked with a closed circuit of resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo> </mo><mi>Ω</mi></math> varies with time (in seconds) as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ϕ</mi><mo>=</mo><mn>5</mn><msup><mi>t</mi><mn>2</mn></msup><mo>−</mo><mn>36</mn><mi>t</mi><mo>+</mo><mn>1</mn></math>. The induced current in the circuit at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo> </mo><mo>=</mo><mn>2</mn><mo> </mo><mi mathvariant="normal">s</mi></math> is _______ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Induced EMF is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>ε</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mo>−</mo><mfenced><mfrac><mrow><mi>d</mi><mi>ϕ</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></mfenced></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>10</mn><mi>t</mi><mo>−</mo><mn>36</mn></mrow></mfenced></math></p><p>Now, it is given that at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>2</mn><mo> </mo><mi mathvariant="normal">s</mi><mo>,</mo><mo> </mo><mi>ε</mi><mo>=</mo><mn>16</mn><mo> </mo><mi mathvariant="normal">V</mi></math>.</p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mfenced close="|" open="|"><mi>ε</mi></mfenced><mi>R</mi></mfrac><mo>=</mo><mfrac><mn>16</mn><mn>8</mn></mfrac><mo>=</mo><mn>2</mn><mo> </mo><mi mathvariant="normal">A</mi></math></p>

</details>

---

### Q8. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A coil is placed perpendicular to a magnetic field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5000</mn><mo> </mo><mi mathvariant="normal">T</mi></math>. When the field is changed to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3000</mn><mo> </mo><mi mathvariant="normal">T</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo> </mo><mi mathvariant="normal">s</mi></math>, an induced emf of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn><mo> </mo><mi mathvariant="normal">V</mi></math> is produced in the coil. If the diameter of the coil is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>02</mn><mo> </mo><mi mathvariant="normal">m</mi></math>, then the number of turns in the coil is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>70</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>140</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>70</mn></math>**

**Detailed Solution:**

<p>Average induced EMF is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ε</mi><mo>=</mo><mi>N</mi><mfenced><mfrac><mrow><mo>∆</mo><mi>ϕ</mi></mrow><mi>t</mi></mfrac></mfenced></math></p><p>Also, change in flux <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∆</mo><mi>ϕ</mi><mo>=</mo><mo>(</mo><mo>∆</mo><mi>B</mi><mo>)</mo><mi>A</mi></math></p><p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mi>i</mi></msub><mo>=</mo><mn>5000</mn><mo> </mo><mi mathvariant="normal">T</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mi>f</mi></msub><mo>=</mo><mn>3000</mn><mo> </mo><mi mathvariant="normal">T</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>02</mn><mo> </mo><mi mathvariant="normal">m</mi><mo> </mo><mo>⇒</mo><mi>r</mi><mo>=</mo><mfrac><mi>d</mi><mn>2</mn></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>01</mn><mo> </mo><mi mathvariant="normal">m</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∆</mo><mi>ϕ</mi><mo>=</mo><mo>(</mo><mo>∆</mo><mi>B</mi><mo>)</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mn>2000</mn></mfenced><mi>π</mi><msup><mfenced><mrow><mn>0</mn><mo>.</mo><mn>01</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn><mo>.</mo><mn>2</mn><mi>π</mi></math></p><p>EMF, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ε</mi><mo>=</mo><mi>N</mi><mfenced><mfrac><mrow><mo>∆</mo><mi>ϕ</mi></mrow><mi>t</mi></mfrac></mfenced><mo>⇒</mo><mn>22</mn><mo>=</mo><mi>N</mi><mfenced><mfrac><mrow><mn>0</mn><mo>.</mo><mn>2</mn><mi>π</mi></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>N</mi><mo>=</mo><mn>70</mn></math></p>

</details>

---

### Q9. JEE Main 2024 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

A square loop of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo> </mo><mi>cm</mi></math> and resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>7</mn><mo> </mo><mi mathvariant="normal">Ω</mi></math> is placed vertically in the east-west plane. A uniform magnetic field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>20</mn><mo> </mo><mi mathvariant="normal">T</mi></math> is set up across the plane in the north-east direction. The magnetic field is decreased to zero in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo> </mo><mi mathvariant="normal">s</mi></math> at a steady rate. Then, the magnitude of induced emf is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>x</mi></msqrt><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo> </mo><mi mathvariant="normal">V</mi></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6cc14ab6-3a8c-44cb-84af-b3d461f7efac.png" style="width: 300px; height: 266px;"/></p><p>The area vector for the square loop is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">A</mi><mo>→</mo></mover><mo>=</mo><mo>(</mo><mn>0</mn><mo>.</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo> </mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo> </mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math></p><p>According to the above diagram, the magnetic field is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">B</mi><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>2</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>2</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></math></p><p>Hence, the magnitude of induced emf can be calculated as follows</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mi>e</mi></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mrow><mi>Δ</mi><mi>ϕ</mi></mrow><mrow><mi>Δ</mi><mi>t</mi></mrow></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mrow><mover><mi>B</mi><mo>→</mo></mover><mo>·</mo><mover><mi>A</mi><mo>→</mo></mover><mo>-</mo><mn>0</mn></mrow><mn>1</mn></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mrow><mfenced><mrow><mfrac><mrow><mn>0</mn><mo>.</mo><mn>2</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>2</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced><mo>·</mo><mfenced><mrow><mo>(</mo><mn>0</mn><mo>.</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo> </mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo> </mo></mrow></mfenced><mo>-</mo><mn>0</mn></mrow><mn>1</mn></mfrac><mo> </mo><mi mathvariant="normal">V</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><msqrt><mn>2</mn></msqrt><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo> </mo><mi mathvariant="normal">V</mi></mtd></mtr></mtable></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>.</p>

</details>

---

### Q10. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> battery connected to a coil of resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mo>&#8486;</mo></math> through a switch, drives a constant current in the circuit. The switch is opened in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>ms</mi></math>. The emf induced across the coil is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>. The inductance of the coil is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>mH</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi>mH</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>mH</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#160;</mo><mi>mH</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>mH</mi></math>**

**Detailed Solution:**

<blockquote><p>The current <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> through the circuit is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mi>i</mi></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mi>V</mi><mi>R</mi></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mfrac><mrow><mn>12</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></mrow><mrow><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></mrow></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></mtd></mtr></mtable></math></p><p>The formula to calculate the induced emf in the coil can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mi>L</mi><mfrac><mrow><mi>d</mi><mi>i</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Substitute the values of the known parameters into equation (1) and solve to calculate the inductance of the coil.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></mtd><mtd><mo>=</mo></mtd><mtd><mi>L</mi><mo>&#215;</mo><mfrac><mrow><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mrow><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>&#8658;</mo></mtd><mtd><mi>L</mi><mo>=</mo><mo>&#160;</mo><mfrac><mrow><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mn>10</mn><mo>&#160;</mo><mi>mH</mi></mtd></mtr></mtable></math></p></blockquote>

</details>

---

### Q11. JEE Main 2023 (13 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

An insulated copper wire of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math> turns is wrapped around a wooden cylindrical core of the cross-sectional area <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn><mo>&#160;</mo><msup><mi>cm</mi><mn>2</mn></msup></math>. The two ends of the wire are connected to a resistor. The total resistance in the circuit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>. If an externally applied uniform magnetic field in the core along its axis changes from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></math> in one direction to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></math> in the opposite direction, the charge flowing through a point in the circuit during the change of magnetic field will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mC</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **60**

**Detailed Solution:**

<blockquote><p>The induced emf <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>&#949;</mi></mfenced></math> in the turns of the coil can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mi>&#949;</mi></mtd><mtd><mo>=</mo></mtd><mtd><mo>-</mo><mfrac><mrow><mi>d</mi><mi>&#966;</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mi>i</mi><mi>R</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></mtd></mtr></mtable></math></p><p>Simplify equation (1) to obtain the required charge through a point in the circuit.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mo>-</mo><mfrac><mrow><mi>d</mi><mi>&#966;</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></mtd><mtd><mo>=</mo></mtd><mtd><mi>i</mi><mi>R</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>&#8658;</mo></mtd><mtd><mo>-</mo><mfrac><mn>1</mn><mi>R</mi></mfrac><msubsup><mo>&#8747;</mo><msub><mi>&#966;</mi><mn>1</mn></msub><msub><mi>&#966;</mi><mn>2</mn></msub></msubsup><mi>d</mi><mi>&#966;</mi><mo>=</mo><mo>&#8747;</mo><mi>i</mi><mi>d</mi><mi>t</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>&#8658;</mo></mtd><mtd><mi>q</mi><mo>=</mo><mfrac><mrow><msub><mi>&#966;</mi><mn>1</mn></msub><mo>-</mo><msub><mi>&#966;</mi><mn>2</mn></msub></mrow><mi>R</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></mtd></mtr></mtable></math></p><p>Where, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#966;</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>&#966;</mi><mn>2</mn></msub></math> are the magnetic flux associated with the coil from two ends.</p><p>As, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#966;</mi><mo>=</mo><mi>N</mi><mi>B</mi><mi>A</mi></math>, from equation (2), it can be written that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mfrac><mrow><mi>N</mi><mi>A</mi></mrow><mi>R</mi></mfrac><mfenced><mrow><msub><mi>B</mi><mn>1</mn></msub><mo>-</mo><msub><mi>B</mi><mn>2</mn></msub></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>,</mo><mo>&#160;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> are the number of turns and the cross-sectional area of the core respectively.</p><p>Substitute the values of the known parameters into equation (3) to calculate the required charge.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mi>q</mi></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mrow><mn>100</mn><mo>&#215;</mo><mn>24</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#215;</mo><mfenced><mrow><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi><mo>-</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>12</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></mrow></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mn>0</mn><mo>.</mo><mn>06</mn><mo>&#160;</mo><mi mathvariant="normal">C</mi><mo>&#215;</mo><mfrac><mrow><mn>1000</mn><mo>&#160;</mo><mi>mC</mi></mrow><mrow><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">C</mi></mrow></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mn>60</mn><mo>&#160;</mo><mi>mC</mi></mtd></mtr></mtable></math></p></blockquote>

</details>

---

### Q12. JEE Main 2023 (11 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>The magnetic field B crossing normally a square metallic plate of area <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math> is changing with time as shown in figure. The magnitude of induced emf in the plate during <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>, is _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mi>V</mi></math>.</p><p style="text-align: center;"><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5d6c8bc7-7667-4b17-8b7e-ef248b88dcf4-image.png" style="width: 300px; height: 193px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5d6c8bc7-7667-4b17-8b7e-ef248b88dcf4-image.png" style="width: 300px; height: 193px;" /></p><p>From the graph, it can be seen that the value of the magnetic field at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi>mT</mi></math>, whereas the magnetic field at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi>mT</mi></math>.</p><p>The formula to calculate the magnitude of the induced emf is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>&#949;</mi><mtext>ind&#160;</mtext></msub></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mrow><mi>d</mi><mi>&#981;</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mi>d</mi><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mfenced><mrow><mi>B</mi><mi>A</mi></mrow></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mi>A</mi><mfrac><mrow><mi>d</mi><mi>B</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>B</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></math> is the slope of the given graph.</p><p>Hence, the value of the induced emf can be calculated as follows:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnspacing="0px" columnalign="right center left"><mtr><mtd><msub><mi>&#949;</mi><mtext>ind&#160;</mtext></msub></mtd><mtd><mo>=</mo></mtd><mtd><mn>4</mn><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#215;</mo><mfenced><mfrac><mrow><mn>8</mn><mo>&#160;</mo><mi>mT</mi><mo>-</mo><mn>4</mn><mo>&#160;</mo><mi>mT</mi></mrow><mrow><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow></mfrac></mfenced></mtd></mtr><mtr><mtd/><mtd><mo>=</mo></mtd><mtd><mn>8</mn><mo>&#160;</mo><mi>mV</mi></mtd></mtr></mtable></math></p>

</details>

---

### Q13. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>The induced emf can be produced in a coil by</p><p>A. moving the coil with uniform speed inside uniform magnetic field</p><p>B. moving the coil with non uniform speed inside uniform magnetic field</p><p>C. rotating the coil inside the uniform magnetic field</p><p>D. changing the area of the coil inside the uniform magnetic field</p><p>Choose the correct answer from the options given below:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> only
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> only
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> only
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> only**

**Detailed Solution:**

<blockquote><p>Induced emf is given by Faraday&#39;s law</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>&#949;</mi></mfenced><mo>=</mo><mfrac><mrow><mi>d</mi><mi>&#981;</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></math></p><p>where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi></math> is the magnetic flux.</p><p>The rate of change of flux through a circuit is defined as emf. The formula for flux is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mover><mi>B</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>A</mi><mo>&#8594;</mo></mover></math>. In the statements <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#38;</mo><mi>B</mi></math> given in the question, the magnetic flux in the coil in uniform magnetic field does not change. So, no emf is induced.</p><p>But in statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math>, the angle between the area vector and the magnetic field continuously changes hence, an emf is generated. In statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math>, the area is changing in unit time so magnetic flux will change and an emf is generated.</p><p> </p></blockquote>

</details>

---

### Q14. JEE Main 2023 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

A certain elastic conducting material is stretched into a circular loop. It is placed with its plane perpendicular to a uniform magnetic field <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></math>. When released the radius of the loop starts shrinking at a constant rate of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>cm</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup></math>. The induced emf in the loop at an instant when the radius of the loop is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>cm</mi></math> will be ______ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mV</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<p>According to the Faraday&#39;s law of electromagnetic induction, the emf induced in a conducting loop is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mo>d</mo><mi>&#981;</mi></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac></math>, here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> is time and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mi>B</mi><mi>A</mi></math> is magnetic flux.</p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mo>d</mo><mi>&#981;</mi></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac></mfenced><mo>=</mo><mfrac><mrow><mo>d</mo><mfenced><mrow><mi>B</mi><mi>A</mi></mrow></mfenced></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac><mo>=</mo><mi>B</mi><mfrac><mrow><mo>d</mo><mfenced><mrow><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>B</mi><mi>&#960;</mi><mfenced><mrow><mn>2</mn><mi>r</mi><mfrac><mrow><mo>d</mo><mi>r</mi></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac></mrow></mfenced><mspace linebreak="newline"/><mo>=</mo><mn>2</mn><mo>&#215;</mo><mi>&#960;</mi><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>8</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8776;</mo><mn>10</mn><mo>&#160;</mo><mi>mV</mi></math> (rounded off)</p>

</details>

---

### Q15. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A conducting loop of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><msqrt><mi>&#960;</mi></msqrt></mfrac><mo>&#160;</mo><mi>cm</mi></math> is placed perpendicular to a uniform magnetic field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></math>. The magnetic field is decreased to zero in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> at a steady rate. The induced emf in the circular loop at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>25</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>emf</mtext><mo>=</mo><mn>1</mn><mi>mV</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>emf</mtext><mo>=</mo><mn>10</mn><mi>mV</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>emf</mtext><mo>=</mo><mn>100</mn><mi>mV</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>emf</mtext><mo>=</mo><mn>5</mn><mi>mV</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>emf</mtext><mo>=</mo><mn>10</mn><mi>mV</mi></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi><mo>&#160;</mo><mo>&#160;</mo><mtext>at</mtext><mo>&#160;</mo><mi>t</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mn>0</mn></math>, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>.</p><p>Magnetic field will decrease linearly as given below. We can say, value of magnetic field at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>25</mn><mo>&#160;</mo><mtext>will&#160;be</mtext><mo>&#160;</mo><mi>B</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>25</mn></math>.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/435e5f2f-d67d-4ffc-8792-8dbf3a9aea8d-9884753.png" style="width: 300px; height: 245px;" /></p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#949;</mi><mtext>ind&#160;</mtext></msub><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mi>&#916;</mi><mi>&#981;</mi></mrow><mrow><mi>&#916;</mi><mi>t</mi></mrow></mfrac></mfenced><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mi>&#916;</mi><mfenced><mrow><mi>B</mi><mi>A</mi></mrow></mfenced></mrow><mrow><mi>&#916;</mi><mi>t</mi></mrow></mfrac></mfenced><mo>=</mo><mi>A</mi><mfenced close="|" open="|"><mfrac><mrow><mi>&#916;</mi><mfenced><mi>B</mi></mfenced></mrow><mrow><mi>&#916;</mi><mi>t</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#960;</mi><mo>&#215;</mo><msup><mfenced><mfrac><mn>10</mn><msqrt><mi>&#960;</mi></msqrt></mfrac></mfenced><mn>2</mn></msup><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#215;</mo><mfenced><mfrac><mrow><mn>0</mn><mo>.</mo><mn>25</mn></mrow><mrow><mn>0</mn><mo>.</mo><mn>25</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#215;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>01</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi><mspace linebreak="newline"/><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi>mV</mi></math></p>

</details>

---

### Q16. JEE Main 2022 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `1`

A conducting circular loop is placed in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>-</mo><mi>Y</mi></math> plane in presence of magnetic field <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>B</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>3</mn><msup><mi>t</mi><mn>3</mn></msup><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math> in SI unit. If the radius of the loop is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>, the induced emf in the loop, at time, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>&#960;</mi><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<blockquote><p>By the faraday&#39;s law in electromagnetic induction</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#949;</mi><mrow><mi>i</mi><mi>n</mi><mi>d</mi></mrow></msub><mo>=</mo><mo>-</mo><mfrac><mrow><mo>d</mo><mi>&#981;</mi></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><mo>d</mo><mfenced><mrow><mover><mi>B</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>A</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac></math></p><p>Magnetic flux is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mover><mi mathvariant="normal">B</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi mathvariant="normal">A</mi><mo>&#8594;</mo></mover></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>3</mn><msup><mi>t</mi><mn>3</mn></msup><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mi>&#960;</mi><msup><mfenced><mn>1</mn></mfenced><mn>2</mn></msup><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mi>&#960;</mi></math></p><p>Now, induced emf is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#949;</mi><mrow><mi>i</mi><mi>n</mi><mi>d</mi></mrow></msub><mo>=</mo><mfenced open="|" close="|"><mfrac><mrow><mo>d</mo><mi>&#981;</mi></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac></mfenced><mo>=</mo><mn>6</mn><mi>t</mi><mi>&#960;</mi></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><msub><mi>&#949;</mi><mrow><mi>i</mi><mi>n</mi><mi>d</mi></mrow></msub><mo>=</mo><mn>6</mn><mfenced><mn>2</mn></mfenced><mi>&#960;</mi><mo>=</mo><mn>12</mn><mi>&#960;</mi><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>.</p><p>Thus, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>12</mn></math>.</p></blockquote>

</details>

---

### Q17. JEE Main 2022 (26 Jul Shift 2)

*Type:* `numerical` | *Level:* `1`

In a coil of resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>, the magnetic flux due to an external magnetic field varies with time as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mfenced><mrow><mn>9</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced></math>. The value of total heat produced in the coil, till the flux becomes zero, will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">J</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<blockquote><p>It is given that magnetic flux <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mfenced><mrow><mn>9</mn><mo>-</mo><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup></mrow></mfenced></math></p><p>For magnetic flux to be zero <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mfenced><mrow><mn>9</mn><mo>-</mo><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup></mrow></mfenced><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math></p><p>According to Faraday&#39;s law of electromagnetic induction,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mi mathvariant="normal">d</mi><mi>&#981;</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mfenced><mrow><mn>0</mn><mo>-</mo><mn>2</mn><mi>t</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn><mi>t</mi></mrow><mn>3</mn></mfrac></math></p><p>Heat produced from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mfrac><msup><mi>&#949;</mi><mn>2</mn></msup><mi>R</mi></mfrac><mi mathvariant="normal">d</mi><mi>t</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mfrac><mrow><mn>16</mn><msup><mi>t</mi><mn>2</mn></msup></mrow><mrow><mn>9</mn><mo>&#215;</mo><mn>8</mn></mrow></mfrac><mi mathvariant="normal">d</mi><mi>t</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi></math></p></blockquote>

</details>

---

### Q18. JEE Main 2022 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `1`

Magnetic flux (in weber) in a closed circuit of resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> varies with time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mfenced><mi>s</mi></mfenced></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mn>8</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mi>t</mi><mo>+</mo><mn>5</mn></math>. The magnitude of the induced current at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>25</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mA</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **250**

**Detailed Solution:**

<blockquote><p>Given that magnetic flux <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mn>8</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mi>t</mi><mo>+</mo><mn>5</mn></math></p><p>According to Faraday&#39;s law of electromagnetic induction</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>emf</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mi mathvariant="normal">d</mi><mi>&#981;</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfenced><mrow><mn>16</mn><mi>t</mi><mo>-</mo><mn>9</mn></mrow></mfenced></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>25</mn><mo>&#160;</mo><mi>s</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>emf</mi><mo>=</mo><mo>-</mo><mfenced close="]" open="["><mrow><mfenced><mrow><mn>16</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>25</mn></mrow></mfenced><mo>-</mo><mn>9</mn></mrow></mfenced><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>Current <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>emf</mi><mo>&#160;</mo></mrow><mrow><mo>&#160;</mo><mi>Resistance</mi><mo>&#160;</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></mrow><mrow><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>=</mo><mfrac><mn>1000</mn><mn>4</mn></mfrac><mo>&#160;</mo><mi>mA</mi><mo>=</mo><mn>250</mn><mo>&#160;</mo><mi>mA</mi></math></p></blockquote>

</details>

---

### Q19. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The magnetic flux through a coil perpendicular to its plane is varying according to the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mfenced><mrow><mn>5</mn><msup><mi mathvariant="normal">t</mi><mn>3</mn></msup><mo>+</mo><mn>4</mn><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi mathvariant="normal">t</mi><mo>-</mo><mn>5</mn></mrow></mfenced></math> Weber. If the resistance of the coil is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>ohm</mi></math>, then the induced current through the coil at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">t</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> will be,

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mn>5</mn><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>4</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>t</mi><mo>-</mo><mn>5</mn></math></p><p>Magnitude of induced emf <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mfenced open="|" close="|"><mfrac><mrow><mo>d</mo><mi>&#981;</mi></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac></mfenced><mo>=</mo><mn>15</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>t</mi><mo>+</mo><mn>2</mn></math></p><p>At, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mn>60</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>78</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>Current, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mi>&#949;</mi><mi>R</mi></mfrac><mo>=</mo><mfrac><mn>78</mn><mn>5</mn></mfrac><mo>=</mo><mn>15</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p>

</details>

---

### Q20. JEE Main 2021 (01 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>A square loop of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi>cm</mi></math> and resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> is moved towards right with a constant speed <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mn>0</mn></msub><mo>.</mo></math> The right arm of the loop is in a uniform magnetic field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi><mo>.</mo></math> The field is perpendicular to the plane of the loop and is going into it. The loop is connected to a network of resistors each of value <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi mathvariant="normal">&#937;</mi><mo>.</mo></math> What should be the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mn>0</mn></msub></math> so that a steady current of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>mA</mi></math> flows in the loop ?</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/03382d32-03b2-45b4-85d3-47af11af1134-image.png" style="width: 503px; height: 239px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi>cm</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>cm</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>2</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>cm</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<p>The EMF is induced in the coil when it is moving in a uniform magnetic field,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><mi>B</mi><mi>v</mi><mi>l</mi></math> and the current, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mi>e</mi><mi>R</mi></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>B</mi><mi>l</mi><mi>v</mi></mrow><mi>R</mi></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>002</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#8658;</mo><mi>v</mi><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>002</mn><mo>&#215;</mo><mi>R</mi></mrow><mrow><mi>B</mi><mi>l</mi></mrow></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>002</mn><mo>&#215;</mo><mfenced><mrow><mn>4</mn><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>5</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>01</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi>cm</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>.</p>

</details>

---

### Q21. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A coil is placed in a magnetic field <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>B</mi><mo>&#8594;</mo></mover></math> as shown below :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/70d5d857-d8e7-4199-b783-f39442e1730e-image.png" style="width: 348px; height: 160px;" />
A current is induced in the coil because <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>B</mi><mo>&#8594;</mo></mover></math> is :

**Options:**

- **(A)** parallel to the plane of coil and increasing with time
- **(B)** outward and increasing with time
- **(C)** outward and decreasing with time
- **(D)** parallel to the plane of coil and decreasing with time

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) outward and decreasing with time**

**Detailed Solution:**

<p>Lenz&#39;s law state that the direction of the induced current is such that it opposes its cause of generation, so, </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f06837a1-9753-4b36-b74c-b777081d41fc-image.png" style="width: 180px; height: 196px;" />
<math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>B</mi><mo>&#8594;</mo></mover></math>, must not be parallel to the plane of coil for non-zero flux and according to Lenz&#39;s law if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is outward it should be decreasing for anticlockwise induced current.</p>

</details>

---

### Q22. JEE Main 2021 (27 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>A bar magnet is passing through a conducting loop of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> with velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>.</mo></math> The radius of the bar magnet is such that it just passes through the loop. The induced e.m.f. in the loop can be represented by the approximate curve:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c88b273c-a99c-4166-b77e-5bfdacc51392-image.png" style="width: 102px; height: 161px;" /> <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6afea83f-af2a-4000-a59f-fd8f0e28909f-b2909a94-b955-4119-8168-9f16585efe92-image.png" style="width: 290px; height: 194px;" /></p>

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/89257063-8a5e-44b3-8107-9fef30547eb1-image.png" style="width: 337px; height: 225px;" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e5e21bb4-3fd8-4bf2-b8ef-f0e24a70f544-image.png" style="width: 341px; height: 227px;" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/16fe1ffe-6580-41b9-aca4-066f4345a16d-image.png" style="width: 341px; height: 229px;" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/27554301-3d14-4a27-b0bd-f70c0443adb9-image.png" style="width: 341px; height: 229px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/16fe1ffe-6580-41b9-aca4-066f4345a16d-image.png" style="width: 341px; height: 229px;" />**

**Detailed Solution:**

<p>As Magnet is approaching toward the loop magnetic flux increases and Rate of increment of flux also increases so emf increases with time</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2fc19aff-772e-4b46-9a09-d6f7284318cf-image.png" style="width: 175px; height: 195px;" /> at this moment emf is maximum and negative</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f4730ae7-2121-496a-a636-820ae0b1ae6c-image.png" style="width: 211px; height: 190px;" /> Magnet is in middle of coil, at this moment emf is equal to zero</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8cee5c32-e558-48e4-a7f2-7d3d4c0018cd-image.png" style="width: 208px; height: 196px;" /> Now again flux start changing however polarity of emf get reverse</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c5ae7610-8b4b-4c1b-a5bd-6bf0a8de319b-image.png" style="width: 185px; height: 219px;" /> At this moment emf is again maximum</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e4a1ff39-9ab8-4d5d-b298-a00292dcbc24-image.png" style="width: 229px; height: 188px;" /> emf again become zero</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/16fe1ffe-6580-41b9-aca4-066f4345a16d-image.png" style="width: 341px; height: 229px;" /></p>

</details>

---

### Q23. JEE Main 2021 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>In the given figure the magnetic flux through the loop increases according to the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#981;</mi><mi>B</mi></msub><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mn>10</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>20</mn><mi>t</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#981;</mi><mi>B</mi></msub></math> is in milliwebers and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> is in seconds. The magnitude of current through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resistor at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> is _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mA</mi><mo>.</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/249963bb-0e18-4476-bc96-6ef1ed150131-image.png" style="width: 287px; height: 193px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **60**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>&#1013;</mi><mo>|</mo><mo>=</mo><mfrac><mrow><mi mathvariant="normal">d</mi><mi>&#981;</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>20</mn><mi>t</mi><mo>+</mo><mn>20</mn><mo>&#160;</mo><mi>mV</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>i</mi><mo>|</mo><mo>=</mo><mfrac><mrow><mo>|</mo><mi>&#1013;</mi><mo>|</mo></mrow><mi>R</mi></mfrac><mo>=</mo><mn>10</mn><mi>t</mi><mo>+</mo><mn>10</mn><mo>&#160;</mo><mi>mA</mi></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>i</mi><mo>|</mo><mo>=</mo><mn>60</mn><mo>&#160;</mo><mi>mA</mi></math></p>

</details>

---

### Q24. JEE Main 2021 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>A circular conducting coil of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> is being heated by the change of magnetic field <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>B</mi><mo>&#8594;</mo></mover></math> passing perpendicular to the plane in which the coil is laid. The resistance of the coil is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>&#956;&#937;</mi></math>. The magnetic field is slowly switched off such that its magnitude changes in time as  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfrac><mn>4</mn><mi>&#960;</mi></mfrac><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi>T</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>t</mi><mn>100</mn></mfrac></mrow></mfenced></math></p><p>The energy dissipated by the coil before the magnetic field is switched off completely is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>mJ</mi></math>.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **80**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mover><mi>B</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>S</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mfrac><mn>4</mn><mi>&#960;</mi></mfrac><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi mathvariant="normal">t</mi><mn>100</mn></mfrac></mrow></mfenced><mo>&#183;</mo><mi>&#960;</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#215;</mo><msup><mfenced><mn>1</mn></mfenced><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>t</mi><mn>100</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mtext>d</mtext><mi>&#981;</mi></mrow><mrow><mtext>d</mtext><mi>t</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mtext>d</mtext></mrow><mrow><mtext>d</mtext><mi>t</mi></mrow></mfrac><mfenced><mrow><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>t</mi><mn>100</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>100</mn></mfrac></mfenced><mo>=</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>5</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfrac><mi>t</mi><mn>100</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>100</mn><mo>&#160;</mo><mi>sec</mi></math></p><p>Heat <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mi>&#949;</mi><mn>2</mn></msup><mi>R</mi></mfrac><mi>t</mi></math></p><p>Heat <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mfenced><mrow><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>5</mn></mrow></msup></mrow></mfenced><mn>2</mn></msup><mrow><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup></mrow></mfrac><mo>&#215;</mo><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi></math></p><p>Heat <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>16</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>10</mn></mrow></msup><mo>&#215;</mo><mn>100</mn></mrow><mrow><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup></mrow></mfrac><mo>&#160;</mo><mi mathvariant="normal">J</mi></math></p><p>Heat <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>08</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi></math></p><p>Heat <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>80</mn><mo>&#160;</mo><mi>mJ</mi></math></p>

</details>

---

### Q25. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>The arm <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> of a rectangular conductor is moving from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mi>b</mi></math> outwards and then inwards from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mi>b</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> as shown in the figure. A uniform magnetic field perpendicular to the plane is acting from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>b</mi><mo>.</mo></math> Identify the graph showing the variation of different quantities with distance:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4ceb9990-61fc-42f4-a738-22cab5e0de0f-image.png" style="width: 250px; height: 193px;" /></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8c159ec7-6b61-4436-aef4-f74c380ceed2-image.png" style="width: 262px; height: 213px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>&mdash;Flux, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>&mdash;Power dissipated, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math>&mdash;EMF
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>&mdash;Power dissipated, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>&mdash;Flux, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>&#8212;</mo><mi>E</mi><mi>M</mi><mi>F</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>&mdash;Flux, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8212;</mo><mi>E</mi><mi>M</mi><mi>F</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math>&mdash;Power dissipated
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8212;</mo><mi>E</mi><mi>M</mi><mi>F</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>&mdash;Power dissipated, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math>&mdash;Flux

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>&mdash;Flux, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8212;</mo><mi>E</mi><mi>M</mi><mi>F</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math>&mdash;Power dissipated**

**Detailed Solution:**

As rod moves in field area increases upto <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>b</mi></math>, then field is absent and again flux is generated on return journey from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>b</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>. Thus plot <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> for flux.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>e</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mi mathvariant="normal">d</mi><mi>&#981;</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi>t</mi></mrow></mfrac><mo>&#8658;</mo></math> curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>emf</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> Power dissipated <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>v</mi><mi>i</mi><mo>&#8658;</mo></math> curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> for power dissipated

</details>

---

### Q26. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The magnetic field in a region is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>B</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mi>B</mi><mn>0</mn></msub><mfenced><mfrac><mi>x</mi><mi>a</mi></mfrac></mfenced><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math>. A square loop of side d is placed with its edges along the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> axes. The loop is moved with a constant velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mi>v</mi><mn>0</mn></msub><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></math>. The emf induced in the loop is :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/06df4e17-d725-40fd-b508-779676e846fb-image.png" style="width: 209px; height: 190px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>B</mi><mn>0</mn></msub><msubsup><mi>v</mi><mn>0</mn><mn>2</mn></msubsup><mo>&#160;</mo><mi>d</mi></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>B</mi><mn>0</mn></msub><msub><mi>v</mi><mn>0</mn></msub><mi>d</mi></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>B</mi><mn>0</mn></msub><msub><mi>v</mi><mn>0</mn></msub><msup><mi>d</mi><mn>2</mn></msup></mrow><mi>a</mi></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>B</mi><mn>0</mn></msub><msub><mi>v</mi><mn>0</mn></msub><msup><mi>d</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>B</mi><mn>0</mn></msub><msub><mi>v</mi><mn>0</mn></msub><msup><mi>d</mi><mn>2</mn></msup></mrow><mi>a</mi></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><msub><mi>B</mi><mn>0</mn></msub><mfenced><mrow><mi>x</mi><mo>+</mo><mi>d</mi></mrow></mfenced></mrow><mi>a</mi></mfrac><msub><mi>v</mi><mn>0</mn></msub><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><msub><mi>B</mi><mn>0</mn></msub><mfenced><mi>x</mi></mfenced></mrow><mi>a</mi></mfrac><msub><mi>v</mi><mn>0</mn></msub><mo>&#160;</mo><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>net</mi></msub><mo>=</mo><msub><mi>E</mi><mn>1</mn></msub><mo>-</mo><msub><mi>E</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>net</mi></msub><mo>=</mo><mfrac><mrow><msub><mi>B</mi><mn>0</mn></msub><msub><mi>v</mi><mn>0</mn></msub><msup><mi>d</mi><mn>2</mn></msup></mrow><mi>a</mi></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/55f82c0f-1c3f-4ab9-b9b9-33c181686cb6-image.png" style="width: 236px; height: 186px;" /></p>

</details>

---

### Q27. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>A conducting bar of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> is free to slide on two parallel conducting rails as shown in the figure</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/20ac010b-512c-416e-84bd-0ce6eaf66c83-image.png" style="width: 355px; height: 153px;" /></p><p>Two resistors <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> are connected across the ends of the rails. There is a uniform magnetic field <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>B</mi><mo>&#8594;</mo></mover></math> pointing into the page. An external agent pulls the bar to the left at a constant speed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi></math>.</p><p>The correct statement about the directions of induced currents <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub></math> flowing through <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> respectively is :</p>

**Options:**

- **(A)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub></math> are in anticlockwise direction
- **(B)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub></math> are in clockwise direction
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> is in clockwise direction and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub></math> is in anticlockwise direction
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> is in anticlockwise direction and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub></math> is in clockwise direction

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> is in clockwise direction and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub></math> is in anticlockwise direction**

**Detailed Solution:**

<p>Given, the external agent pulls the bar towards left. According to Lenz&#39;s law and Fleming&#39;s right hand rule, there will be a motional EMF generated in the bar. The right-hand rule tells us that the magnetic force on positive charges will be in downward direction and the electric equivalent circuit can be drawn as shown below.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f1c23f93-641b-4239-98e0-baea7d055e9a-image.png" style="width: 251px; height: 136px;" /></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> is in the clockwise direction and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub></math> is in the anticlockwise direction.</p>

</details>

---

### Q28. JEE Main 2021 (25 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

A coil of inductance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">H</mi></math> having negligible resistance is connected to a source of supply whose voltage is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>3</mn><mi>t</mi></math> volt. (where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> is in second). If the voltage is applied when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn></math>, then the energy stored in the coil after <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">J</mi></math>,

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **144**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mfrac><mrow><mi>L</mi><mi>d</mi><mi>I</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>4</mn></msubsup><mi>t</mi><mi>d</mi><mi>t</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>d</mi><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>16</mn><mo>=</mo><mn>2</mn><mi mathvariant="normal">I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>L</mi><msup><mi>I</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>2</mn><msup><mfenced><mn>12</mn></mfenced><mn>2</mn></msup><mo>=</mo><mn>144</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9e9c7fdb-a169-41cf-a71e-74c40eb9c382-image.png" style="width: 173px; height: 174px;" /></p>

</details>

---

### Q29. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>An infinitely long straight wire carrying current I, one side opened rectangular loop and a conductor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> with a sliding connector are located in the same plane, as shown in the figure. The connector has length l. and resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>. It slides to the right with a velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi></math>. The resistance of the conductor and the self inductance of the loop are negligible. The induced current in the loop, as a function of separation r, between the connector and the straight wire is</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ef547f74-9ac7-49ca-a06a-c7ae769ff3f0-image.png" style="width: 299px; height: 202px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>&#956;</mi><mn>0</mn></msub><mrow><mn>4</mn><mi>&#960;</mi></mrow></mfrac><mfrac><mrow><mi>Iv</mi><mi>&#8467;</mi></mrow><mi>Rr</mi></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>&#956;</mi><mn>0</mn></msub><mi>&#960;</mi></mfrac><mfrac><mrow><mi>Iv</mi><mi>&#8467;</mi></mrow><mi>Rr</mi></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msub><mi>&#956;</mi><mn>0</mn></msub></mrow><mi>&#960;</mi></mfrac><mfrac><mrow><mi>Iv</mi><mi>&#8467;</mi></mrow><mi>Rr</mi></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>&#956;</mi><mn>0</mn></msub><mrow><mn>2</mn><mi>&#960;</mi></mrow></mfrac><mfrac><mrow><mi>Iv</mi><mi>&#8467;</mi></mrow><mi>Rr</mi></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>&#956;</mi><mn>0</mn></msub><mrow><mn>2</mn><mi>&#960;</mi></mrow></mfrac><mfrac><mrow><mi>Iv</mi><mi>&#8467;</mi></mrow><mi>Rr</mi></mfrac></math>**

**Detailed Solution:**

<p>The induced current in the wire  will be due to the motional EMF developed in the moving resistor  and that back emf developed  at that point will be  equal to  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mi>B</mi><mi>L</mi><mspace linebreak="newline"></mspace></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo></math>velocity of the conductor</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo></math>perpendicular magnetic field</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo></math>length of conductor</p><p>We know magnetic field due to a long wire is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><mi>i</mi></mrow><mrow><mn>2</mn><mi>&#960;</mi><mi>r</mi></mrow></mfrac></math></p><p>Hence the induced current across wire will be :</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mi>e</mi><mi>R</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><msub><mi>&#956;</mi><mn>0</mn></msub><mrow><mn>2</mn><mi>&#960;</mi></mrow></mfrac><mfrac><mrow><mi>Iv</mi><mi>&#8467;</mi></mrow><mi>Rr</mi></mfrac></math></p>

</details>

---

### Q30. JEE Main 2020 (05 Sep Shift 1)

*Type:* `numerical` | *Level:* `3`

Two concentric circular coils, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>2</mn></msub></math>, are placed in the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mi>Y</mi></math> plane. <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn></math>turns, and a radius of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>cm</mi></math>. <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>2</mn></msub></math> has 200 turns and radius of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi>cm</mi><mtext>.</mtext><mo>&#160;</mo><msub><mi>C</mi><mn>2</mn></msub></math> carries a time dependent current <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi mathvariant="italic">t</mi></mfenced><mo>=</mo><mfenced><mrow><mn>5</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>t</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mi mathvariant="normal">A</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> is in s. The emf induced in <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub><mfenced><mrow><mi>in</mi><mo>&#160;</mo><mi>mV</mi></mrow></mfenced></math> at the instant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>1</mn></math>s is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mi>x</mi></mfrac><mo>.</mo></math> The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is ..........

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfenced><mrow><mn>5</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>t</mi><mo>+</mo><mi>C</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>i</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mo>(</mo><mn>10</mn><mi>t</mi><mo>+</mo><mn>2</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#981;</mi><mtext>small&#160;</mtext></msub><mo>=</mo><mi>B</mi><mi>A</mi><mo>=</mo><mfenced><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><mi>I</mi><msub><mi>N</mi><mn>2</mn></msub></mrow><mrow><mn>2</mn><mi>R</mi></mrow></mfrac></mfenced><mfenced><mrow><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced></math></p><p>induced emf in small coil</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">e</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">d</mi><mi>&#981;</mi></mrow><mi>dt</mi></mfrac><mo>=</mo><mfenced><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><msub><mi mathvariant="normal">N</mi><mn>2</mn></msub></mrow><mrow><mn>2</mn><mi mathvariant="normal">r</mi></mrow></mfrac></mfenced><mi>&#960;</mi><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup><msub><mi mathvariant="normal">N</mi><mn>1</mn></msub><mfrac><mi>di</mi><mi>dt</mi></mfrac><mo>=</mo><mfenced><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><msub><mi mathvariant="normal">N</mi><mn>1</mn></msub><msub><mi mathvariant="normal">N</mi><mn>2</mn></msub><mi>&#960;</mi><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mi mathvariant="normal">R</mi></mrow></mfrac></mfenced><mo>(</mo><mn>10</mn><mi mathvariant="normal">t</mi><mo>-</mo><mn>2</mn><mo>)</mo></math></p><p>at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">e</mi><mo>=</mo><mfenced><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><msub><mi mathvariant="normal">N</mi><mn>1</mn></msub><msub><mi mathvariant="normal">N</mi><mn>2</mn></msub><mi>&#960;</mi><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mi mathvariant="normal">R</mi></mrow></mfrac></mfenced><mn>8</mn><mo>=</mo><mn>4</mn><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><msub><mi mathvariant="normal">N</mi><mn>1</mn></msub><msub><mi mathvariant="normal">N</mi><mn>2</mn></msub><mi>&#960;</mi><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mrow><mi mathvariant="normal">R</mi></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mo>(</mo><mn>4</mn><mi>&#960;</mi><mo>)</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup><mo>&#215;</mo><mn>200</mn></mrow><mn>20</mn></mfrac><mo>&#215;</mo><mn>500</mn><mo>&#215;</mo><mfrac><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfrac><mi>&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>80</mn><mo>&#215;</mo><msup><mi>&#960;</mi><mn>2</mn></msup><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>=</mo><mn>8</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><mi>volt</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>8</mn><mo>&#160;</mo><mi>mV</mi><mo>=</mo><mfrac><mn>4</mn><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q31. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A uniform magnetic field B exists in a direction perpendicular to the plane of a square loop made of a metal wire. The wire has a diameter of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi>mm</mi></math> and a total length of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>&#160;</mo><mi>cm</mi><mo>.</mo></math> The magnetic field changes with time at a steady rate <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>dB</mi><mo>/</mo><mi>dt</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>032</mn><msup><mi>Ts</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>.</mo></math> The induced current in the <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>loop</mo></math>is close to (Resistivity of the metal wire is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>23</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup><mo>&#160;</mo><mi>&#937;m</mi></math> )

**Options:**

- **(A)** 0.43 A
- **(B)** 0.61 A
- **(C)** 0.34 A
- **(D)** 0.53 A

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0.61 A**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2b901711-211b-41a1-9103-eb2b50139a14-image.png" style="width: 167px; height: 119px;" /></p><p>Radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi mathvariant="normal">d</mi><mo>/</mo><mn>2</mn><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>mm</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">R</mi><mi>wire</mi></msub><mo>=</mo><mfrac><mrow><mi mathvariant="normal">&#961;</mi><mi mathvariant="script">l</mi></mrow><mi mathvariant="normal">A</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#981;</mi><mo>=</mo><mi>BA</mi><mo>&#160;;&#160;</mo><mfenced close="|" open="|"><mi mathvariant="normal">e</mi></mfenced><mo>=</mo><mfrac><mi>d&#981;</mi><mi>dt</mi></mfrac><mo>=</mo><mfrac><mi>dB</mi><mi>dt</mi></mfrac><mfenced><mi mathvariant="normal">A</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">i</mi><mo>=</mo><mfrac><mi mathvariant="normal">e</mi><mi mathvariant="normal">R</mi></mfrac><mo>=</mo><mfenced close="|" open="|"><mfrac><mi>dB</mi><mi>dt</mi></mfrac></mfenced><mfrac><msup><mfenced><mi mathvariant="normal">A</mi></mfenced><mn>2</mn></msup><mrow><mi mathvariant="normal">&#961;</mi><mi mathvariant="script">l</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>032</mn><mo>&#215;</mo><msup><mfenced close="}" open="{"><mrow><mi mathvariant="normal">&#960;</mi><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>.</mo><mn>23</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>61</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p>

</details>

---

### Q32. JEE Main 2020 (02 Sep Shift 1)

*Type:* `numerical` | *Level:* `2`

A circular coil of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>cm</mi></math> is placed in a uniform magnetic field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>0</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>5</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">T</mi></math> with its plane perpendicular to the field initially. It is rotated at constant angular speed about an axis along the diameter of coil and perpendicular to magnetic field so that it undergoes half of rotation in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>. The maximum value of EMF induced (in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;V</mi></math>) in the coil will be close to the integer....

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **15**

**Detailed Solution:**

<p>Flux as a function of time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mover><mi mathvariant="normal">B</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi mathvariant="normal">A</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>A</mi><mi>B</mi><mi>cos</mi><mo>(</mo><mi>&#969;</mi><mi>t</mi><mo>)</mo></math></p><p>Emf induced,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">e</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi mathvariant="normal">d</mi><mi>&#981;</mi></mrow><mi>dt</mi></mfrac><mo>=</mo><mi>AB</mi><mi>&#969;</mi><mi>sin</mi><mo>(</mo><mi>&#969;</mi><mi mathvariant="normal">t</mi><mo>)</mo></math></p><p>Max. value of Emf <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mi>A</mi><mi>B</mi><mi>&#969;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#960;</mi><msup><mi>R</mi><mn>2</mn></msup><mi>B</mi><mi>&#969;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>.</mo><mn>14</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>5</mn></mrow></msup><mo>&#215;</mo><mfrac><mi>&#960;</mi><mrow><mn>0</mn><mo>.</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mn>15</mn></math></p>

</details>

---

### Q33. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

At time <math><mi>t</mi><mo>=</mo><mn>0</mn></math> magnetic field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn><mo>&#160;</mo><mi mathvariant="normal">G</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">s</mi></math> is passing perpendicularly through the area defined by the closed loop shown in the figure. If the magnetic field reduces linearly to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn><mo>&#160;</mo><mi mathvariant="normal">G</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">s</mi><mo>,</mo></math> in the next <math><mn>5</mn><mi></mi><mi mathvariant="normal">s</mi><mo>,</mo></math> then induced <math><mi mathvariant="normal">E</mi><mi mathvariant="normal">M</mi><mi mathvariant="normal">F</mi></math> in the loop is:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d24881a3-f5bc-432e-af67-811a6b4d3a0d-image.png" style="width: 400px; height: 175px;" />

**Options:**

- **(A)** <math><mn>56</mn><mi></mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">V</mi></math>
- **(B)** <math><mn>28</mn><mi></mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">V</mi></math>
- **(C)** <math><mn>48</mn><mi></mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">V</mi></math>
- **(D)** <math><mn>36</mn><mi></mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>56</mn><mi></mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">V</mi></math>**

**Detailed Solution:**

<math><mi>ε</mi><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>d</mi><mi>&#x03D5;</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>A</mi><mi>d</mi><mi>B</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></mrow></mfenced></math>
<math> <mrow> <mi>ε</mi><mo>=</mo><mfenced close="|" open="|"> <mrow> <mo>−</mo><mfrac> <mrow> <mi>Δ</mi><mi>ϕ</mi></mrow> <mrow> <mi>Δ</mi><mi>t</mi></mrow> </mfrac> </mrow> </mfenced><mo>=</mo><mfenced close="|" open="|"> <mrow> <mfrac> <mrow> <mi>A</mi><mi>Δ</mi><mi>B</mi></mrow> <mrow> <mi>Δ</mi><mi>t</mi></mrow> </mfrac> </mrow> </mfenced></mrow> </math>
<math><mo>=</mo><mfenced separators="|"><mrow><mn>16</mn><mo>×</mo><mn>4</mn><mo>-</mo><mn>4</mn><mo>×</mo><mn>2</mn></mrow></mfenced><mfrac><mrow><mfenced separators="|"><mrow><mn>1000</mn><mo>-</mo><mn>500</mn></mrow></mfenced></mrow><mrow><mn>5</mn></mrow></mfrac><mo>×</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>×</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>4</mn></mrow></msup></math>
<math><mo>=</mo><mn>56</mn><mo>×</mo><mfrac><mrow><mn>500</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>×</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>8</mn></mrow></msup><mo>=</mo><mn>56</mn><mo>×</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>6</mn></mrow></msup><mi>V</mi></math>

</details>

---

### Q34. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A planar loop of wire rotates in a uniform magnetic field. Initially, at <math><mi>t</mi><mo>=</mo><mn>0</mn></math> , the plane of the loop is perpendicular to the magnetic field. If it rotates with a period of <math><mn>10</mn><mi mathvariant="normal"></mi><mi mathvariant="normal">s</mi></math> about an axis in its plane then the magnitude of induced emf will be maximum and minimum, respectively at:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2.5</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7.5</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2.5</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5.0</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5.0</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7.5</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5.0</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2.5</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5.0</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#934;</mi><mo>=</mo><mover><mi>B</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mrow><mi>A</mi><mo>&#160;</mo></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>B</mi><mi>A</mi><mi>cos</mi><mi>&#952;</mi><mo>&#160;</mo><mo>=</mo><mi>B</mi><mi>A</mi><mi>cos</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><mfenced open="|" close="|"><mfrac><mrow><mi>d</mi><mi>&#981;</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></mfenced><mo>&#160;</mo><mo>=</mo><mi>B</mi><mi>A</mi><mi>&#969;</mi><mi>sin</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi></mrow></mfenced></math></p><p>
When <math><mi>&#969;</mi><mi>t</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><mo>&#8757;</mo><mi>&#981;</mi></math> will be minimum.
<math><mo>&#8756;</mo><mi mathvariant="normal">e</mi></math> will be maximum
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mfrac><mi>&#960;</mi><mn>5</mn></mfrac></mfrac><mo>=</mo><mn>2</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math></p><p>When <math><mi>&#969;</mi><mi mathvariant="normal">t</mi><mo>=</mo><mi>&#960;</mi></math>
<math><mo>&#8757;</mo><mi>&#981;</mi></math> will be maximum.
<math><mo>&#8756;</mo><mi mathvariant="normal">e</mi></math> will be minimum
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mi>&#960;</mi><mrow><mi>&#960;</mi><mo>/</mo><mn>5</mn></mrow></mfrac><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math></p>

</details>

---

### Q35. JEE Main 2020 (07 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

A loop <math><mi mathvariant="normal">A</mi><mi mathvariant="normal">B</mi><mi mathvariant="normal">C</mi><mi mathvariant="normal">D</mi><mi mathvariant="normal">E</mi><mi mathvariant="normal">F</mi><mi mathvariant="normal">A</mi></math> of straight edges has six corner points <math><mi>A</mi><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi></mi><mn>0</mn><mo>,</mo><mi></mi><mn>0</mn></mrow></mfenced><mo>,</mo><mi></mi><mi>B</mi><mfenced separators="|"><mrow><mn>5</mn><mo>,</mo><mi></mi><mn>0</mn><mo>,</mo><mi></mi><mn>0</mn></mrow></mfenced><mo>,</mo><mi></mi><mi>C</mi><mfenced separators="|"><mrow><mn>5</mn><mo>,</mo><mi></mi><mn>5</mn><mo>,</mo><mi></mi><mn>0</mn></mrow></mfenced><mo>,</mo><mi></mi><mi>D</mi><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi></mi><mn>5</mn><mo>,</mo><mi></mi><mn>0</mn></mrow></mfenced><mo>,</mo><mi></mi><mi>E</mi><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi></mi><mn>5</mn><mo>,</mo><mi></mi><mn>5</mn></mrow></mfenced></math> and <math><mi>F</mi><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi></mi><mn>0</mn><mo>,</mo><mi></mi><mn>5</mn></mrow></mfenced></math> . The magnetic field in this region is <math><mover accent="true"><mrow><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mi>T</mi></math> . The quantity of flux through the loop <math><mi mathvariant="normal">A</mi><mi mathvariant="normal">B</mi><mi mathvariant="normal">C</mi><mi mathvariant="normal">D</mi><mi mathvariant="normal">E</mi><mi mathvariant="normal">F</mi><mi mathvariant="normal">A</mi></math> (in <math><mi mathvariant="normal">W</mi><mi mathvariant="normal">b</mi></math> ) is _____________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **175**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mover accent="true"><mi>B</mi><mo>&#8594;</mo></mover><mo>.</mo><mover accent="true"><mi>A</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mn>3</mn><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>.</mo><mfenced separators="|"><mrow><mn>25</mn><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>25</mn><mover accent="true"><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/79097522-cd58-49ea-9a17-a831c4eaa16d.png" />
<math><mi>&#981;</mi><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mo>&#215;</mo><mn>25</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mn>4</mn><mo>&#215;</mo><mn>25</mn></mrow></mfenced><mo>=</mo><mn>175</mn><mi></mi><mi mathvariant="normal">w</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">b</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">r</mi></math>

</details>

---

### Q36. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Consider a circular coil of wire carrying constant current <math><mi mathvariant="normal">I</mi><mo>,</mo><mi mathvariant="normal"></mi></math> forming a magnetic dipole. The magnetic flux through an infinite plane that contains the circular coil and excluding the circular coil area is given by <math><msub><mrow><mi>&#981;</mi></mrow><mrow><mi>i</mi></mrow></msub></math> The magnetic flux through the area of the circular coil area is given by <math><msub><mrow><mi>&#981;</mi></mrow><mrow><mn>0</mn></mrow></msub></math> . Which of the following option is correct?

**Options:**

- **(A)** <math><msub><mrow><mi>ϕ</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>=</mo><msub><mrow><mi>ϕ</mi></mrow><mrow><mn>0</mn></mrow></msub></math>
- **(B)** <math><msub><mrow><mi>ϕ</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>&gt;</mo><msub><mrow><mi>ϕ</mi></mrow><mrow><mn>0</mn></mrow></msub></math>
- **(C)** <math><msub><mrow><mi>ϕ</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>&lt;</mo><msub><mrow><mi>ϕ</mi></mrow><mrow><mn>0</mn></mrow></msub></math>
- **(D)** <math><msub><mrow><mi>ϕ</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>=</mo><mo>-</mo><msub><mrow><mi>ϕ</mi></mrow><mrow><mn>0</mn></mrow></msub></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msub><mrow><mi>ϕ</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>=</mo><mo>-</mo><msub><mrow><mi>ϕ</mi></mrow><mrow><mn>0</mn></mrow></msub></math>**

**Detailed Solution:**

As magnetic field lines always form a closed loop, hence every magnetic field line creating magnetic flux in the inner region must be passing through the outer region. Since flux in two regions are in opposite direction.
<math><mo>&#8756;</mo><msub><mrow><mi>&#981;</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>=</mo><mo>-</mo><msub><mrow><mi>&#981;</mi></mrow><mrow><mn>0</mn></mrow></msub></math>

</details>

---

### Q37. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A conducting circular loop made of a thin wire has area <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3.5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mi>&#160;</mi><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math> and resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mi>&#160;</mi><mi mathvariant="normal">&#937;</mi></math> It is placed perpendicular to a time-dependent magnetic field <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced separators="|"><mi>t</mi></mfenced><mo>=</mo><mfenced separators="|"><mrow><mn>0.4</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow></mfenced><mi>sin</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mn>50</mn><mi>&#960;</mi><mi>t</mi></mrow></mfenced></math> The field is uniform in space. Then the net charge flowing through the loop during <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn><mi>&#160;</mi><mi mathvariant="normal">s</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>10</mn><mi>&#160;</mi><mi>ms</mi></math> is close to

**Options:**

- **(A)** <math><mn>1.4</mn><mi> </mi><mi>m</mi><mi>C</mi></math>
- **(B)** <math><mn>7</mn><mi> </mi><mi>m</mi><mi>C</mi></math>
- **(C)** <math><mn>21</mn><mi> </mi><mi>m</mi><mi>C</mi></math>
- **(D)** <math><mn>6</mn><mi> </mi><mi>m</mi><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>1.4</mn><mi> </mi><mi>m</mi><mi>C</mi></math>**

**Detailed Solution:**

<p>It is given that, the magnetic field,</p><p><math><mi>B</mi><mo>=</mo><mn>0.4</mn><mtext>&#8201;</mtext><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mn>50</mn><mi>&#960;</mi><mi>t</mi></mrow></mfenced></math></p><p>and the area of the given circular conducting loop,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>3.5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math></p><p>Magnetic flux,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mi>B</mi><mi>A</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>Then, induced emf,

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mi>d</mi><mi>&#981;</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p>When resistance in the circuit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>, the differential charge accumulated, based on current <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math>,

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>Q</mi><mo>=</mo><mi>i</mi><mi>d</mi><mi>t</mi><mo>=</mo><mfrac><mi>&#949;</mi><mi>R</mi></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mi>R</mi></mfrac><mi>d</mi><mi>&#981;</mi><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mo>&#8710;</mo><mi>Q</mi><mo>=</mo><mfrac><mn>1</mn><mi>R</mi></mfrac><mi>&#160;</mi><mo>&#8747;</mo><mi>d</mi><mi>&#966;</mi><mo>=</mo><mfrac><mn>1</mn><mi>R</mi></mfrac><mi>&#160;</mi><mo>&#8710;</mo><mi>&#981;</mi></math></p><p>Substituting given values and using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>)</mo></math>,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>Q</mi><mo>=</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mfenced close="]" open="["><mrow><mn>0.4</mn><mi>sin</mi><mfenced><mrow><mn>50</mn><mi>&#960;</mi><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced><mo>-</mo><mn>0</mn></mrow></mfenced><mo>&#215;</mo><mn>3</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mo>&#8710;</mo><mi>Q</mi><mo>=</mo><mfrac><mrow><mn>0.4</mn><mo>&#215;</mo><mn>3</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow><mn>10</mn></mfrac><mo>=</mo><mn>1</mn><mo>.</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8710;</mo><mi>Q</mi><mo>=</mo><mn>1</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi>mC</mi></math></p>

</details>

---

### Q38. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `2`

At the centre of a fixed large circular coil of radius $\mathrm{R}$, a much smaller circular coil of radius $r$ is placed. The two coils are concentric and are in the same plane. The larger coil carries a current I. The smaller coil is set to rotate with a constant angular velocity $\omega$ about an axis along their common diameter. Calculate the emf induced in the smaller coil after a time $t$ of its start of rotation.

**Options:**

- **(A)** $\frac{\mu_0 \mathrm{I}}{2 \mathrm{R}} \omega \mathrm{r}^2 \sin \omega \mathrm{t}$
- **(B)** $\frac{\mu_0 I}{4 R} \omega \pi r^2 \sin \omega t$
- **(C)** $\frac{\mu_0 I}{2 R} \omega \pi r^2 \sin \omega t$
- **(D)** $\frac{\mu_0 \mathrm{I}}{4 \mathrm{R}} \omega \mathrm{r}^2 \sin \omega \mathrm{t}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\mu_0 I}{2 R} \omega \pi r^2 \sin \omega t$**

**Detailed Solution:**

According to Faraday's law of electromagnetic induction,
$$
\begin{array}{r}
e=-\frac{d \phi}{d t} \text { and } \phi=B A \cos \omega t=B \pi r^2 \cos \omega t \\
\Rightarrow \quad e=-\frac{d}{d t}\left(\pi r^2 B \cos \omega t\right)=\pi r^2 B \sin \omega t(\omega) \\
\therefore e=\frac{\mu_0 I}{2 R} \pi \omega r^2 \sin \omega t\left(\because B=\frac{\mu_0 I}{2 R}\right)
\end{array}
$$

</details>

---

### Q39. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `3`

A copper rod of mass $\mathrm{m}$ slides under gravity on two smooth parallel rails, with separation $l$ and set at an angle of $\theta$ with the horizontal. At the bottom, rails are joined by a resistance R. There is a uniform magnetic field $\mathrm{B}$ normal to the plane of the rails, as shown in the figure. The terminal speed of the copper rod is:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/nPtk98OV8m_xU2gG5kncRd0J3LvljrdeUJRyRI0A220.original.fullsize.png">

**Options:**

- **(A)** $\frac{\mathrm{mgR} \cos \theta}{\mathrm{B}^2 l^2}$
- **(B)** $\frac{\mathrm{mgR} \sin \theta}{\mathrm{B}^2 l^2}$
- **(C)** $\frac{\mathrm{mgR} \tan \theta}{\mathrm{B}^2 l^2}$
- **(D)** $\frac{\mathrm{mgR} \cot \theta}{\mathrm{B}^2 l^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\mathrm{mgR} \sin \theta}{\mathrm{B}^2 l^2}$**

**Detailed Solution:**

From Faraday's law of electomagnetic induction,
$$
\begin{aligned}
e &=\frac{d \phi}{d t}=\frac{d(B A)}{l t}=\frac{d(B l l)}{d t} \\
&=\frac{B d l \times l}{d t}=B V l
\end{aligned}
$$
Also, $F=i l B=\left(\frac{B V}{R}\right)\left(l^2 B\right)=\frac{B^2 l^2 V}{R}$
At equilibrium
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/IThq93sgx3l5iFAgin_lVatWj22hs8CBE9bN-ro8ftM.original.fullsize.png">

$$
m g \sin \theta=\frac{B^2 l V}{R} \Rightarrow V=\frac{m g R \sin \theta}{B^2 l^2}
$$

</details>

---

### Q40. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `3`

A circular loop of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>3</mn><mo>&#160;</mo><mi>cm</mi></math> lies parallel to a much bigger circular loop of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi>cm</mi></math>. The centre of the small loop is on the axis of the bigger loop. The distance between their centres is<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cm</mi></math>. If a current of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> flows through the smaller loop, then the flux linked with a bigger loop is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.3</mo><mo>&#215;</mo><mn>1</mn><msup><mn>0</mn><mrow><mo>-</mo><mn>1</mn><mn>1</mn></mrow></msup><mi>weber</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>.6</mo><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup><mi>weber</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>.1</mo><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>11</mn></mrow></msup><mi>weber</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">6</mi><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>11</mn></mrow></msup><mi>weber</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>.1</mo><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>11</mn></mrow></msup><mi>weber</mi></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><msub><mi>&#981;</mi><mn>2</mn></msub><mo>=</mo><msub><mi>B</mi><mn>1</mn></msub><mo>&#215;</mo><msub><mi>A</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><mo>=</mo><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><mi>I</mi><msubsup><mi>R</mi><mn>1</mn><mn>2</mn></msubsup></mrow><mrow><mn>2</mn><msup><mrow><mo>(</mo><msubsup><mi>R</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>)</mo></mrow><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mrow></mfrac><mo>&#215;</mo><mi>&#960;</mi><msubsup><mi>R</mi><mn>2</mn><mn>2</mn></msubsup></mtd></mtr></mtable></math>

= <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><mrow><mo>(</mo><mn>2</mn><mo>)</mo></mrow><msup><mrow><mo>(</mo><mn>20</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8722;</mo><mn>2</mn></mrow></msup><mo>)</mo></mrow><mn>2</mn></msup></mrow><mrow><mn>2</mn><msup><mrow><mo>[</mo><msup><mrow><mo>(</mo><mn>0.2</mn><mo>)</mo></mrow><mn>2</mn></msup><mo>+</mo><msup><mrow><mo>(</mo><mn>0.15</mn><mo>)</mo></mrow><mn>2</mn></msup><mo>]</mo></mrow><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mrow></mfrac><mo>&#215;</mo><mi>&#960;</mi><mrow><mo>(</mo><mn>0.3</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8722;</mo><mn>2</mn></mrow></msup><mo>)</mo></mrow></math>

On solving

<math> <mrow> <mo>=</mo> <mtext>9.216</mtext> <mo>&#215;</mo> <mn>1</mn> <msup> <mn>0</mn> <mrow> <mo>-</mo> <mn>1</mn> <mn>1</mn> </mrow> </msup> </mrow> </math>

<math> <mrow> <mo>&#8776;</mo> <mtext>9.2</mtext> <mo>&#215;</mo> <mn>1</mn> <msup> <mn>0</mn> <mrow> <mo>-</mo> <mn>1</mn> <mn>1</mn> </mrow> </msup> <mtext>&#160;weber</mtext> </mrow> </math>

</details>

---

### Q41. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `3`

A coil of self inductance $L$ is connected at one end of two rails as shown in figure. A connector of length $l$, mass $m$ can slide freely over the two parallel rails. The entire set up is placed in a magnetic field of induction $B$ going into the page. At an instant $t=0$ an initial velocity $v_0$ is imparted to it and as a result of that it starts moving along $x$-axis. The displacement of the connector is represented by the figure.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/gT78fcZPPJaHs1iWBjjYlFhHtALAEOib9wiGdjz0uaQ.original.fullsize.png">

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/KJltPs9gN6K3jYlhzaaC4cM9xM0UIYF2VG0Akp-Ia1A.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/eelhiZD6J_B3XLGKWEgkgdCnEqkGUw-VPN34kpon0QQ.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/BBARl0UeNSk4Ld5O9OF6LqjsHw9aewCS0pz0rWZ-Agc.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/uFLWjrrRnuF7lfhp4sqmfBedSLYHCZE9oHP5_iF1Nis.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/uFLWjrrRnuF7lfhp4sqmfBedSLYHCZE9oHP5_iF1Nis.original.fullsize.png">**

**Detailed Solution:**

No Solution Available

</details>

---

### Q42. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `2`

Magnetic flux through a coil of resistance $10 \Omega$ is changed by $\Delta \phi$ in $0.1 \mathrm{~s}$. The resulting current in the coil varies with time as shown in the figure. Then $|\Delta \phi|$ is equal to (in weber)
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/IEwm4vf3MZmgAAq995SWfpIvp0Gd0U-i_hFf2VOVUaU.original.fullsize.png">

**Options:**

- **(A)** 6
- **(B)** 4
- **(C)** 2
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

$$
\text { As } \begin{aligned}
e=\frac{\Delta \phi}{\Delta t} & \text { or } R i=\frac{\Delta \phi}{\Delta t} \quad(\because e=R i) \\
\Rightarrow \quad \Delta \phi & =R(i . \Delta t) \\
& =R \times \text { area under } i-t \text { graph } \\
= & 10 \times \frac{1}{2} \times 4 \times 0.1=2 \text { weber }
\end{aligned}
$$

</details>

---

### Q43. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

The flux linked with a coil at any instant ' $t$ ' is given by
$\phi=10 t^2-50 t+250$
The induced emf at $t=3 \mathrm{~s}$ is

**Options:**

- **(A)** $190 \mathrm{~V}$
- **(B)** $-190 \mathrm{~V}$
- **(C)** $-10 \mathrm{~V}$
- **(D)** $10 \mathrm{~V}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-10 \mathrm{~V}$**

**Detailed Solution:**

$e=-\frac{d \phi}{d t}=-(20 t-50)=-10$ volt

</details>

---

### Q44. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `3`

In a uniform magnetic field of induction $B$ a wire in the form of semicircle of radius $r$ rotates about the diameter of the circle with angular frequency $\omega$. The axis of rotation is perpendicular to the field. If the total resistance of the circuit is $R$ the mean power generated per period of rotation is

**Options:**

- **(A)** $\frac{B \pi r^2 \omega}{2 R}$
- **(B)** $\frac{\left(B \pi r^2 \omega\right)^2}{2 R}$
- **(C)** $\frac{(\mathrm{B} \pi \mathrm{r} \omega)^2}{2 \mathrm{R}}$
- **(D)** $\frac{\left(B \pi r \omega^2\right)^2}{8 R}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\left(B \pi r^2 \omega\right)^2}{2 R}$**

**Detailed Solution:**

Magnetic flux $=B A \cos \theta=B \cdot \frac{\pi r^2}{2} \cos \omega t$
$$
\begin{aligned}
& \therefore \varepsilon_{\text {ind }}=-\frac{\mathrm{d} \phi}{\mathrm{dt}}=\frac{1}{2} \mathrm{~B} \pi \mathrm{r}^2 \omega \sin \omega \mathrm{t} \\
& \therefore \mathrm{P}=\frac{\varepsilon_{\text {ind }}^2}{\mathrm{R}}=\frac{\mathrm{B}^2 \pi^2 \mathrm{r}^4 \omega^2 \sin ^2 \omega \mathrm{t}}{4 \mathrm{R}}
\end{aligned}
$$
Now, $ < \sin ^2 \omega t>=1 / 2$ (mean value)
$$
\therefore\langle\mathrm{P}\rangle=\frac{\left(\mathrm{B} \pi \mathrm{r}^2 \omega\right)^2}{8 \mathrm{R}} \text {. }
$$

</details>

---

### Q45. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `1`

The mass of product liberated on anode in an electrochemical cell depends on
(where t is the time period, for which the current is passed)

**Options:**

- **(A)** $(\mathrm{It})^{1 / 2}$
- **(B)** IT
- **(C)** I/t
- **(D)** $\mathrm{I}^{2} \mathrm{t}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) IT**

**Detailed Solution:**

From Faradays law of electrolysis, $\mathrm{m} \propto$ it.

</details>

---

