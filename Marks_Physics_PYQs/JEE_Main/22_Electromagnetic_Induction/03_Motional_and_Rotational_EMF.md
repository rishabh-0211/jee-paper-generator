# JEE Main Physics - Electromagnetic Induction

## Topic 3: Motional and Rotational EMF

**Total Questions:** 34

---

### Q1. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A metal rod of length $L$ rotates about one end at origin with a uniform angular velocity $\omega$. The magnetic field radially falls off as $B(r) = B_0 e^{-\lambda r}$; $\lambda$ being a positive constant. The emf induced (neglecting the centripetal force on electrons in the rod) is :

**Options:**

- **(A)** $B_0 \omega \left[\dfrac{1}{\lambda^2} - e^{-\lambda L}\left(\dfrac{1}{\lambda^2} + \dfrac{L}{\lambda}\right)\right]$
- **(B)** $B_0 \omega \left[\dfrac{1}{\lambda^2} + e^{-\lambda L}\left(\dfrac{1}{\lambda^2} + \dfrac{L}{\lambda}\right)\right]$
- **(C)** $B_0 \omega \left[\dfrac{4}{\lambda^2} - e^{-2\lambda L}\left(\dfrac{1}{\lambda^2} + \dfrac{2L}{\lambda}\right)\right]$
- **(D)** $B_0 \omega \left[\dfrac{3}{\lambda^2} - e^{-3\lambda L}\left(\dfrac{3}{\lambda^2} + \dfrac{L}{\lambda}\right)\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $B_0 \omega \left[\dfrac{1}{\lambda^2} - e^{-\lambda L}\left(\dfrac{1}{\lambda^2} + \dfrac{L}{\lambda}\right)\right]$**

**Detailed Solution:**

The motional emf $dE$ induced in a small element of length $dr$ at a distance $r$ from the origin is given by:

$dE = B(r) v(r) dr$

Since the rod is rotating with angular velocity $\omega$, the velocity of the element is $v(r) = \omega r$.

$dE = B_0 e^{-\lambda r} (\omega r) dr$

The total emf induced $E$ is the integral of $dE$ from $r = 0$ to $r = L$:

$E = \int_0^L B_0 \omega r e^{-\lambda r} dr$

$E = B_0 \omega \int_0^L r e^{-\lambda r} dr$

Using integration by parts:

$\int r e^{-\lambda r} dr = r \left( \dfrac{e^{-\lambda r}}{-\lambda} \right) - \int 1 \cdot \left( \dfrac{e^{-\lambda r}}{-\lambda} \right) dr$

$= -\dfrac{r}{\lambda} e^{-\lambda r} - \dfrac{1}{\lambda^2} e^{-\lambda r}$

Evaluating the definite integral from $0$ to $L$:

$\int_0^L r e^{-\lambda r} dr = \left[ -\dfrac{L}{\lambda} e^{-\lambda L} - \dfrac{1}{\lambda^2} e^{-\lambda L} \right] - \left[ 0 - \dfrac{1}{\lambda^2} e^0 \right]$

$= \dfrac{1}{\lambda^2} - e^{-\lambda L} \left( \dfrac{1}{\lambda^2} + \dfrac{L}{\lambda} \right)$

Therefore, the total induced emf is:

$E = B_0 \omega \left[ \dfrac{1}{\lambda^2} - e^{-\lambda L} \left( \dfrac{1}{\lambda^2} + \dfrac{L}{\lambda} \right) \right]$

Answer: $B_0 \omega \left[\dfrac{1}{\lambda^2} - e^{-\lambda L}\left(\dfrac{1}{\lambda^2} + \dfrac{L}{\lambda}\right)\right]$

</details>

---

### Q2. JEE Main 2026 (23 January Shift 1)

*Type:* `numerical` | *Level:* `2`

A simple pendulum made of mass 10 g and a metallic wire of length 10 cm is suspended vertically in a uniform magnetic field of 2 T. The magnetic field direction is perpendicular to the plane of oscillations of the pendulum. If the pendulum is released from an angle of $60^{\circ}$ with vertical, then maximum induced EMF between the point of suspension and point of oscillation is $\_\_\_\_$ mV. (Take $\mathrm{g}=10 \mathrm{~m} / \mathrm{s}^{2}$)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **100**

**Detailed Solution:**

The maximum induced EMF for a rod of length $\ell$ rotating in a magnetic field $B$ is:
$\varepsilon_{max} = \frac{B \omega_{max} \ell^2}{2} \quad \cdots(1)$

Using energy conservation to find $\omega_{max}$:
$mg\ell(1 - \cos 60°) = \frac{1}{2}(m\ell^2)\omega_m^2$

$\omega_m = \sqrt{\frac{g}{\ell}} = \sqrt{\frac{10}{0.1}} = 10 \text{ rad/s}$

From equation (1):
$\varepsilon_{max} = \frac{2 \times 10 \times 0.01}{2} = 0.1 \text{ V} = 100 \text{ mV}$

</details>

---

### Q3. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A 20 m long uniform copper wire held horizontally is allowed to fall under the gravity ($g=10 \mathrm{~m} / \mathrm{s}^{2}$) through a uniform horizontal magnetic field of 0.5 Gauss perpendicular to the length of the wire. The induced EMF across the wire when it travells a vertical distance of 200 m is $\_\_\_\_$ mV.

**Options:**

- **(A)** $20 \sqrt{10}$
- **(B)** $0.2 \sqrt{10}$
- **(C)** $200 \sqrt{10}$
- **(D)** $2 \sqrt{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $20 \sqrt{10}$**

**Detailed Solution:**

For a conducting wire falling in a magnetic field, induced EMF is: $\mathcal{E} = BLv$
After falling through height $h = 200$ m, velocity: $v = \sqrt{2gh} = \sqrt{2 \times 10 \times 200} = \sqrt{4000} = 20\sqrt{10}$ m/s
Converting magnetic field: $B = 0.5$ Gauss $= 0.5 \times 10^{-4}$ T
Induced EMF: $\mathcal{E} = (0.5 \times 10^{-4}) \times 20 \times 20\sqrt{10} = 200 \times 10^{-4}\sqrt{10} = 0.02\sqrt{10}$ V $= 20\sqrt{10}$ mV

</details>

---

### Q4. JEE Main 2026 (22 January Shift 2)

*Type:* `numerical` | *Level:* `2`

A conducting circular loop is rotated about its diameter at a constant angular speed of $100 \mathrm{rad} / \mathrm{s}$ in a magnetic field of 0.5 T perpendicular to the axis of rotation. When the loop is rotated by $30^{\circ}$ from the horizontal position, the induced EMF is 15.4 mV. The radius of the loop is $\_\_\_\_$ mm. (Take $\pi=\frac{22}{7}$)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

$E = B\omega A \sin\omega t$
$15.4 \times 10^{-3} = \dfrac{1}{2} \times 100 \times \dfrac{22}{7} r^2 \times \dfrac{1}{2}$
$r = \sqrt{\dfrac{15.4 \times 28 \times 10^{-5}}{22}}$
$R = 14 \text{ mm}$

</details>

---

### Q5. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$X P Q Y$ is a vertical smooth long loop having a total resistance $R$ where $P X$ is parallel to $Q Y$ and separation between them is $l$. A constant magnetic field $B$ perpendicular to the plane of the loop exists in the entire space. A rod $C D$ of length $L(L>l)$ and mass $m$ is made to slide down from rest under the gravity as shown in figure. The terminal speed acquired by the rod is $\_\_\_\_$ $\mathrm{m} / \mathrm{s}.(\mathrm{g}=$ acceleration due to gravity) 
 <img style="width:200px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/22S1_q_36_1.png">

**Options:**

- **(A)** \(\frac{8 m g R}{B^2 l^2}\)
- **(B)** \(\frac{2 m g R}{B^2 L^2}\)
- **(C)** \(\frac{m \mathrm{~g} R}{B^2 l^2}\)
- **(D)** \(\frac{2 m g R}{B^2 l^2}\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) \(\frac{m \mathrm{~g} R}{B^2 l^2}\)**

**Detailed Solution:**

As rod CD slides down with velocity $v$, it cuts magnetic field lines.
Induced EMF: $\varepsilon = BLv$
Induced current in the circuit: $I = \frac{BLv}{R}$
Magnetic force on the rod (upward, by Lenz's law):
$F_{mag} = BIL = \frac{B^2L^2v}{R}$
At terminal velocity, acceleration is zero.
Applying Newton's second law:
$mg - F_{mag} = 0$
$mg = \frac{B^2L^2v_{terminal}}{R}$
$v_{terminal} = \frac{mgR}{B^2L^2}$

</details>

---

### Q6. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A 1 m long metal rod AB completes the circuit as shown in figure. The area of circuit is perpendicular to the magnetic field of 0.10 T. If the resistance of the total circuit is $2 \Omega$ then the force needed to move the rod towards right with constant speed (v) of $1.5 \mathrm{~m} / \mathrm{s}$ is $\_\_\_\_$ N. 
 <img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/21S1_q_42_1.png">

**Options:**

- **(A)** $5.7 \times 10^{-2}$
- **(B)** $7.5 \times 10^{-2}$
- **(C)** $7.5 \times 10^{-3}$
- **(D)** $5.7 \times 10^{-3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $7.5 \times 10^{-3}$**

**Detailed Solution:**

Given: $l = 1$ m, $B = 0.10$ T, $R = 2$ Ω, $v = 1.5$ m/s
Motional EMF: $\varepsilon = Blv = 0.10 \times 1 \times 1.5 = 0.15$ V
Current: $I = \frac{\varepsilon}{R} = \frac{0.15}{2} = 0.075$ A
Magnetic force on rod: $F = BIl = 0.10 \times 0.075 \times 1 = 7.5 \times 10^{-3}$ N
For constant velocity, applied force equals magnetic force.

</details>

---

### Q7. JEE Main 2025 (4 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Conductor wire ABCDE with each $\operatorname{arm} 10 \mathrm{~cm}$ in length is placed in magnetic field of $\frac{1}{\sqrt{2}}$ Tesla, perpendicular to its plane. When conductor is pulled towards right with constant velocity of $10 \mathrm{~cm} / \mathrm{s}$, induced emf between points A and E is _____ mV.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/FPVR5p89HZQbfccK6XuxSUaSRb1KGiFdcHIWE757RQo.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8biWp_JVSPTg-g3lgRlZJFlQSFjByYvEK4fFQOe4J5g.original.fullsize.png"/>
As field is uniform we can replace the bent wire with straight wire from $A$ to $B$.
So EMF :
$\varepsilon=\mathrm{Bv} \ell_{\mathrm{AB}}$
$\begin{aligned} & =\frac{1}{\sqrt{2}} \times \frac{10 \mathrm{~cm}}{5} \times 2\left(10 \sin 45^{\circ}\right) \mathrm{cm} \\ & \varepsilon=10 \mathrm{mV}\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A coil of area A and N turns is rotating with angular velocity \(\omega\) in a uniform magnetic field \(\vec{B}\) about an axis perpendicular to \(\vec{B}\). Magnetic flux \(\varphi\) and induced \(\operatorname{emf} \varepsilon\) across it, at an instant when \(\vec{B}\) is parallel to the plane of coil, are :

**Options:**

- **(A)** \(\varphi=\mathrm{AB}, \varepsilon=0\)
- **(B)** \(\varphi=0, \varepsilon=0\)
- **(C)** \(\varphi=0, \varepsilon=\mathrm{NAB} \omega\)
- **(D)** \(\varphi=\mathrm{AB}, \varepsilon=\mathrm{NAB} \omega\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) \(\varphi=0, \varepsilon=\mathrm{NAB} \omega\)**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/tRqC4OVurqIDgEyxkTpQjnBLQepjWGwUa6_bu56ua_M.original.fullsize.png">


$\begin{aligned}
\phi & =\mathrm{BAN} \cdot \cos (\omega \mathrm{t}) \\
\varepsilon & =\frac{-\mathrm{d} \phi}{\mathrm{dt}}=\mathrm{BA} \omega \mathrm{~N} \cdot \sin (\omega \mathrm{t})
\end{aligned}$

When $B$ is parallel to plane, $\underline{\underline{\omega t}}=\frac{\pi}{2}$
$\Rightarrow \phi=0, \varepsilon=\mathrm{BA} \omega \mathrm{~N}$

</details>

---

### Q9. JEE Main 2025 (28 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Fe-GcogvbelLVUxgZgoEYStw9hbvaAUAidXYQB2bMeM.original.fullsize.png"/>

A conducting bar moves on two conducting rails as shown in the figure. A constant magnetic field B exists into the page. The bar starts to move from the vertex at time $t=0$ with a constant velocity. If the induced EMF is $\mathrm{E} \propto \mathrm{t}^{\mathrm{n}}$, then value of n is _.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

As the bar moves without change in orientation, the length of bar will be proportional to its distance from the vertex.
i.e. $I=c(v t)$
$\begin{aligned}
& \text { induced emf } E=B / v \\
& =c B v^2 t
\end{aligned}$
$\Rightarrow n=1$

</details>

---

### Q10. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A uniform magnetic field of 0.4 T acts perpendicular to a circular copper disc 20 cm in radius. The disc is having a uniform angular velocity of $10 \pi \mathrm{rad} \mathrm{s}^{-1}$ about an axis through its centre and perpendicular to the disc. What is the potential difference developed between the axis of the disc and the rim ? $(\pi=3.14)$

**Options:**

- **(A)** $0.5024 \mathrm{~V}$
- **(B)** $\mathrm{~V}$
- **(C)** $0.2512 \mathrm{~V}$
- **(D)** $0.1256 \mathrm{~V}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.2512 \mathrm{~V}$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{B}=0.4 \mathrm{~T} \\ & \mathrm{r}=20 \mathrm{~cm} \\ & \omega=10 \pi \mathrm{rad} / \mathrm{s} \\ & \mathrm{E}=\frac{1}{2} \mathrm{~B} \omega \mathrm{R}^2 \\ & =0.2512 \mathrm{~V}\end{aligned}$

</details>

---

### Q11. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A square loop of side $15 \mathrm{~cm}$ being moved towards right at a constant speed of 2 $\mathrm{cm} / \mathrm{s}$ as shown in figure. The front edge enters the $50 \mathrm{~cm}$ wide magnetic field at $t=$ 0 . The value of induced emf in the loop at $t=10 \mathrm{~s}$ will be :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Xgs8Q8Qun4rlgV327RmadPvLXnHTCpiLCQjSDvyshEk.original.fullsize.png">

**Options:**

- **(A)** $0.3 \mathrm{mV}$
- **(B)** zero
- **(C)** $4.5 \mathrm{mV}$
- **(D)** $3 \mathrm{mV}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) zero**

**Detailed Solution:**

At $\mathrm{t}=10 \mathrm{sec}$ complete loop is in magnetic field therefore no change in flux
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/W7PT0et-nMmZr9R1x73xmW76aqhhIDZJP5LmJ1aZ43g.original.fullsize.png"/>
$\mathrm{e}=\frac{\mathrm{d} \phi}{\mathrm{dt}}=0$
$\mathrm{e}=0$ for complete loop

</details>

---

### Q12. JEE Main 2024 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

A square loop PQRS having 10 turns, area $3.6 \times 10^{-3} \mathrm{~m}^2$ and resistance $100 \Omega$ is slowly and uniformly being pulled out of a uniform magnetic field of magnitude $\mathrm{B}=0.5 \mathrm{~T}$ as shown. Work done in pulling the loop out of the field in $1.0 \mathrm{~s}$ is ______ $\times 10^{-6} \mathrm{~J}$.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Olesr8QJ7r6V-cRRq6q2NdQuCyMSkA5_ZoiB96ajLFE.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

$\begin{aligned} & \epsilon=N B \ell v \\ & i=\frac{\epsilon}{R}=\frac{N B \ell v}{R} \\ & F=N(i \ell B)=\frac{N^2 B^2 \ell^2 v}{R}\end{aligned}$
$\begin{aligned} & \mathrm{W}=\mathrm{F} \times \ell=\frac{\mathrm{N}^2 \mathrm{~B}^2 \ell^3}{\mathrm{R}}\left(\frac{\ell}{\mathrm{t}}\right) \\ & \mathrm{A}=\ell^2 \\ & \mathrm{~W}=\frac{(10 \times 10)(0.5)^2 \times\left(3.6 \times 10^{-3}\right)^2}{100 \times 1} \\ & \mathrm{~W}=3.24 \times 10^{-6} \mathrm{~J}\end{aligned}$

</details>

---

### Q13. JEE Main 2024 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

A coil of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn></math> turns and area <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>20</mn><mo> </mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math> is rotated at half a revolution per second and is placed in uniform magnetic field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>01</mn><mo> </mo><mi mathvariant="normal">T</mi></math> perpendicular to axis of rotation of the coil. The maximum voltage generated in the coil is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mi>β</mi></mfrac></math> volt. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>Time taken for one complete revolution = time period <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo> </mo><mi mathvariant="normal">s</mi></math>.</p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ω</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mi>T</mi></mfrac><mo>=</mo><mi>π</mi><mo> </mo><mi>rad</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Now flux, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ϕ</mi><mo>=</mo><mi>NABcos</mi><mo>(</mo><mi>ω</mi><mi mathvariant="normal">t</mi><mo>)</mo></math></p><p>Therefore, induced EMF <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ε</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mo>-</mo><mfrac><mrow><mi mathvariant="normal">d</mi><mi>ϕ</mi></mrow><mi>dt</mi></mfrac></mrow></mfenced><mo>=</mo><mi>NAB</mi><mi>ω</mi><mi>sin</mi><mo>(</mo><mi>ω</mi><mi mathvariant="normal">t</mi><mo>)</mo></math></p><p>The maximum voltage generated, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>ε</mi><mi>max</mi></msub><mo>=</mo><mi>NAB</mi><mi>ω</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>200</mn><mo>×</mo><mn>0</mn><mo>.</mo><mn>2</mn><mo>×</mo><mn>0</mn><mo>.</mo><mn>01</mn><mo>×</mo><mi>π</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mn>10</mn></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mn>5</mn></mfrac></math> volt</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>=</mo><mn>5</mn></math>.</p>

</details>

---

### Q14. JEE Main 2024 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `3`

A rectangular loop of sides <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo> </mo><mi>cm</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo> </mo><mi>cm</mi></math>, with its sides parallel to the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis respectively moves with a velocity of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo> </mo><mi>cm</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> in the positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> axis direction, in a space containing a variable magnetic field in the positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> direction. The field has a gradient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo> </mo><mi mathvariant="normal">T</mi><mo> </mo><msup><mi>cm</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> along the negative <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> direction and it is decreasing with time at the rate of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo> </mo><mi mathvariant="normal">T</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>.</mo></math> If the resistance of the loop is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo> </mo><mi mathvariant="normal">m</mi><mi>Ω</mi></math>, the power dissipated by the loop as heat is ______ <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup><mo> </mo><mi mathvariant="normal">W</mi><mo>.</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **216**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7a551720-d678-48ae-ad55-7daa54e734c5.png" style="width: 350px; height: 214px;"/></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mn>0</mn></msub></math> is the magnetic field at origin. Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>B</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msubsup><mo>∫</mo><msub><mi>B</mi><mn>0</mn></msub><mi>B</mi></msubsup><mi>d</mi><mi>B</mi><mo>=</mo><mo>-</mo><msubsup><mo>∫</mo><mn>0</mn><mi>x</mi></msubsup><msup><mn>10</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>B</mi><mo>-</mo><msub><mi>B</mi><mn>0</mn></msub><mo>=</mo><mo>-</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi mathvariant="normal">x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>B</mi><mo>=</mo><mfenced><mrow><msub><mi>B</mi><mn>0</mn></msub><mo>-</mo><mfrac><mi>x</mi><mn>10</mn></mfrac></mrow></mfenced></math></p><p>Motional emf in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mn>0</mn></math></p><p>Motional emf in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mi>D</mi><mo>=</mo><mn>0</mn></math></p><p>Motional emf in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>D</mi><mo>=</mo><msub><mi>ε</mi><mn>1</mn></msub><mo>=</mo><msub><mi>B</mi><mn>0</mn></msub><mi>ℓ</mi><mi>v</mi></math></p><p>Magnetic field on rod <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><msub><mi>B</mi><mn>0</mn></msub><mo>-</mo><mfrac><mfenced><mrow><mo>-</mo><mn>12</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mn>10</mn></mfrac></mrow></mfenced></math></p><p>Motional emf in  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mo>=</mo><msub><mi>ε</mi><mn>2</mn></msub><mo>=</mo><mfenced><mrow><msub><mi>B</mi><mn>0</mn></msub><mo>+</mo><mfrac><mrow><mn>12</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow><mn>10</mn></mfrac></mrow></mfenced><mi>ℓ</mi><mo>×</mo><mi>v</mi></math></p><p>Net equivalent emf <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">ε</mi><mi>eq</mi></msub><mo>=</mo><msub><mi mathvariant="normal">ε</mi><mn>2</mn></msub><mo>-</mo><msub><mi mathvariant="normal">ε</mi><mn>1</mn></msub><mo>=</mo><mn>300</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup><mo> </mo><mi mathvariant="normal">V</mi></math></p><p>For time variation</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><msub><mi>ε</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub></mfenced><mo>'</mo></msup><mo>=</mo><mi>A</mi><mfrac><mrow><mi>d</mi><mi>B</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>60</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup><mo> </mo><mi>V</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><msub><mi>ε</mi><mi>eq</mi></msub></mfenced><mtext>net </mtext></msub><mo>=</mo><msub><mi>ε</mi><mi>eq</mi></msub><mo>+</mo><msup><mfenced><msub><mi>ε</mi><mi>eq</mi></msub></mfenced><mo>'</mo></msup><mo>=</mo><mn>360</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup><mo> </mo><mi mathvariant="normal">V</mi></math></p><p>Power <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mfrac><msubsup><mfenced><msub><mi>ε</mi><mtext>eq </mtext></msub></mfenced><mtext>net </mtext><mn>2</mn></msubsup><mi>R</mi></mfrac><mo>=</mo><mn>216</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup><mo> </mo><mi mathvariant="normal">W</mi></math></p>

</details>

---

### Q15. JEE Main 2023 (15 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>A <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi>cm</mi></math> long metallic rod is rotated with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>210</mn><mo>&#160;</mo><mi>rpm</mi></math> about an axis normal to the rod passing through its one end. The other end of the rod is in contact with a circular metallic ring. A constant and uniform magnetic field <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></math> parallel to the axis exists everywhere. The emf developed between the centre and the ring is _________<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mV</mi></math>.</p><p>(Take <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>=</mo><mfrac><mn>22</mn><mn>7</mn></mfrac></math>)</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **88**

**Detailed Solution:**

<blockquote><p>The data given is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mn>210</mn><mo>&#215;</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>60</mn></mfrac><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mn>7</mn><mi>&#960;</mi><mo>&#160;</mo><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mspace linebreak="newline"></mspace><mi>l</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mspace linebreak="newline"></mspace><mi>B</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></math></p><p>The emf is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mfrac><mrow><mi>B</mi><mi>&#969;</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#215;</mo><mn>7</mn><mi>&#960;</mi><mo>&#215;</mo><mfrac><msup><mfenced><mrow><mn>0</mn><mo>.</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>88</mn><mo>&#160;</mo><mi>mV</mi></math></p></blockquote>

</details>

---

### Q16. JEE Main 2023 (12 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>A conducting circular loop is placed in a uniform magnetic field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></math> with its plane perpendicular to the field. Somehow, the radius of the loop starts expanding at a constant rate of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>mm</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The magnitude of induced emf in the loop at an instant when the radius of the loop is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>cm</mi></math> will be _______ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;V</mi></math>.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **50**

**Detailed Solution:**

<p>The data given is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi><mspace linebreak="newline"></mspace><mi>R</mi><mo>=</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p><p>It is given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>R</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Area of the loop is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mi>&#960;</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>A</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi>&#960;</mi><mi>R</mi><mfrac><mstyle displaystyle="true"><mi>d</mi><mi>R</mi></mstyle><mstyle displaystyle="true"><mi>d</mi><mi>t</mi></mstyle></mfrac></math></p><p>The flux is,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mn>2</mn><mi>&#960;</mi><mi>R</mi><mfrac><mrow><mi>d</mi><mi>R</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>&#215;</mo><mi>B</mi></math></p><p>So, the magnitude of emf is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mn>2</mn><mo>&#215;</mo><mfrac><mn>22</mn><mn>7</mn></mfrac><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>.</mo><mn>028</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>5</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>=</mo><mn>50</mn><mo>.</mo><mn>28</mn><mo>&#160;</mo><mi>&#956;V</mi><mo>&#8776;</mo><mn>50</mn><mo>&#160;</mo><mo>&#160;</mo><mi>&#956;V</mi></math></p>

</details>

---

### Q17. JEE Main 2023 (11 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

A metallic cube of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>&#160;</mo><mi>cm</mi></math> moving along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis at a uniform velocity of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. In a region of uniform magnetic field of magnitude <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></math> directed along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math>- axis. In equilibrium the potential difference between the faces of higher and lower potential developed because of the motion through the field will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mV</mi></math>.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c6bd4656-663d-4ee0-b29f-217ce50b89d9.png" style="width: 300px; height: 301px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **150**

**Detailed Solution:**

<p>Using the equation</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mi>E</mi><mo>=</mo><mi>q</mi><mi>v</mi><mi>B</mi><mo>&#160;</mo><mspace linebreak="newline"/><mo>&#8658;</mo><mi>E</mi><mo>=</mo><mi>v</mi><mi>B</mi></math></p><p>Using the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>V</mi><mo>=</mo><mi>E</mi><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8710;</mo><mi>V</mi><mo>=</mo><mi>v</mi><mi>B</mi><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>15</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>15</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>=</mo><mn>150</mn><mo>&#160;</mo><mi>mV</mi></math></p>

</details>

---

### Q18. JEE Main 2023 (10 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>A square loop of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi>cm</mi></math> is placed inside a long solenoid that has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> turns per centimetre and carries a sinusoidally varying current of amplitude <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> and angular frequency <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>700</mn><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The central axes of the loop and solenoid coincide. The amplitude of the emf induced in the loop is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is ___________</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo></math> Take, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open=""><mrow><mi>&#960;</mi><mo>=</mo><mfrac><mn>22</mn><mn>7</mn></mfrac></mrow></mfenced></math></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **44**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2def0a13-3d1b-440e-a579-ff591554c058.png" style="width: 300px; height: 174px;" /></p><p>It is given that the current is varying sinusoidally. The current can be written as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msub><mi>I</mi><mn>0</mn></msub><mi>sin</mi><mi>&#969;</mi><mi>t</mi></math>.</p><p>The magnetic field through the solenoid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><msub><mi>&#956;</mi><mn>0</mn></msub><mi>n</mi><mi>I</mi></math></p><p>The flux through the square is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><msub><mi>&#956;</mi><mn>0</mn></msub><mi>n</mi><mi>I</mi><mi>A</mi></math></p><p>The emf is</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><msub><mi>&#956;</mi><mn>0</mn></msub><mi>n</mi><mi>A</mi><mo>&#215;</mo><mfrac><mrow><mi>d</mi><mo>(</mo><msub><mi>I</mi><mn>0</mn></msub><mi>sin</mi><mi>&#969;</mi><mi>t</mi><mo>)</mo></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>&#949;</mi><mo>=</mo><msub><mi>&#956;</mi><mn>0</mn></msub><mi>n</mi><mi>A</mi><msub><mi>I</mi><mn>0</mn></msub><mi>&#969;</mi><mi>cos</mi><mi>&#969;</mi><mi>t</mi></math></p><p>The amplitude of the emf is,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><msub><mi>&#956;</mi><mn>0</mn></msub><mi>n</mi><mi>A</mi><msub><mi>I</mi><mn>0</mn></msub><mi>&#969;</mi><mo>=</mo><mn>4</mn><mi>&#960;</mi><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup><mo>&#215;</mo><mfrac><mn>50</mn><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfrac><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#215;</mo><mn>2</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><mn>700</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>&#949;</mi><mo>=</mo><mn>44</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p></blockquote>

</details>

---

### Q19. JEE Main 2023 (10 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>A <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> long metal rod <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mi>Y</mi></math> completes the circuit as shown in figure. The plane of the circuit is perpendicular to the magnetic field of flux density <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>15</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></math>. If the resistance of the circuit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mo>&#8486;</mo></math>, the force needed to move the rod in direction, as indicated, with a constant speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> will be _______<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow><mo>&#8211;</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d1f383d4-9dbb-40b0-b719-5a9d3262d9ac.png" style="width: 350px; height: 157px;" /></p><p> </p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

<blockquote><p>The force on the rod is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mi>i</mi><mi>l</mi><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>F</mi><mo>=</mo><mfrac><mrow><mi>B</mi><mi>v</mi><mi>l</mi></mrow><mi>R</mi></mfrac><mo>&#215;</mo><mi>l</mi><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>F</mi><mo>=</mo><mfrac><mrow><msup><mi>B</mi><mn>2</mn></msup><msup><mi>l</mi><mn>2</mn></msup><mi>v</mi></mrow><mi>R</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mo>)</mo></math></p><p>The data given is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mspace linebreak="newline"></mspace><mi>l</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mspace linebreak="newline"></mspace><mi>v</mi><mo>=</mo><mn>4</mn><mo mathvariant="italic">&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mspace linebreak="newline"></mspace><mi mathvariant="normal">B</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>15</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi><mspace linebreak="newline"></mspace></math></p><p>Substituting the values in equation (i)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mfrac><mrow><msup><mfenced><mrow><mn>0</mn><mo>.</mo><mn>15</mn></mrow></mfenced><mn>2</mn></msup><mo>&#215;</mo><msup><mfenced><mn>1</mn></mfenced><mn>2</mn></msup><mo>&#215;</mo><mn>4</mn></mrow><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>18</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi></math></p></blockquote>

</details>

---

### Q20. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

An emf of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>08</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> is induced in a metal rod of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>cm</mi></math> held normal to a uniform magnetic field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></math>, when move with a velocity of:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<blockquote><p>The formula to calculate the motional emf induced in a moving conductor in a magnetic field is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mi>B</mi><mi>l</mi><mi>v</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Substitute the values of the known parameters into equation (1) and solve to calculate the required velocity of the rod.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mn>0</mn><mo>.</mo><mn>08</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></mtd><mtd><mo>=</mo></mtd><mtd><mn>0</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi><mo>&#215;</mo><mfenced><mrow><mn>10</mn><mo>&#160;</mo><mi>cm</mi><mo>&#215;</mo><mfrac><mrow><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></mrow><mrow><mn>100</mn><mo>&#160;</mo><mi>cm</mi></mrow></mfrac></mrow></mfenced><mo>&#215;</mo><mi>v</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>&#8658;</mo></mtd><mtd><mi>v</mi><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>08</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></mrow><mrow><mn>0</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi><mo>&#215;</mo><mn>10</mn><mo>&#160;</mo><mi>cm</mi><mo>&#215;</mo><mfrac><mrow><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></mrow><mrow><mn>100</mn><mo>&#160;</mo><mi>cm</mi></mrow></mfrac></mrow></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mtd></mtr></mtable></math></p></blockquote>

</details>

---

### Q21. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A wire of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> moving with velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> at right angles to a magnetic field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></math>. The magnitude of induced emf, between the ends of wire will be ___________.

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5db4386a-b0a0-41b9-b795-d6a81ff39b1a-9894481.PNG" style="width: 250px; height: 238px;" /></p><p>The expression of motional emf is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><mi>B</mi><mi>L</mi><mi>v</mi><mi>sin</mi><mi>&#952;</mi></math>, where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> is angle between magnetic field and direction of motion.</p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mn>90</mn><mo>&#176;</mo></math>, </p><p>So, induced emf across the ends of wire is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><mo>&#160;</mo><mi>B</mi><mi>L</mi><mi>v</mi><mi>sin</mi><mn>90</mn><mo>&#176;</mo><mspace linebreak="newline"></mspace><mo>=</mo><mi>B</mi><mi>L</mi><mi>v</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mn>2</mn><mo>&#160;</mo><mo>&#215;</mo><mo>&#160;</mo><mn>1</mn><mo>&#160;</mo><mo>&#215;</mo><mo>&#160;</mo><mn>8</mn><mo>&#160;</mo><mspace linebreak="newline"></mspace><mo>=</mo><mo>&#160;</mo><mn>16</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p>

</details>

---

### Q22. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>A metallic rod of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> is rotated with an angular speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi></math> normal to a uniform magnetic field <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> about an axis passing through one end of rod as shown in figure. The induced emf will be :</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f95adc92-8a37-4e1a-949b-9f146a236eb1-9893978.PNG" style="width: 300px; height: 242px;" />.</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>B</mi><mn>2</mn></msup><msup><mi>L</mi><mn>2</mn></msup><mi>&#969;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>B</mi><msup><mi>L</mi><mn>2</mn></msup><mi>&#969;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>B</mi><msup><mi>L</mi><mn>2</mn></msup><mi>&#969;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><msup><mi>B</mi><mn>2</mn></msup><mi>L</mi><mi>&#969;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>B</mi><msup><mi>L</mi><mn>2</mn></msup><mi>&#969;</mi></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a0a133cd-b1e3-492f-b6ce-24ba9f603a69-9893978_1.PNG" style="width: 202px; height: 112px;" /></p><p>Linear velocity at the distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> from the centre can be written as, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mi>&#969;</mi><mi>x</mi></math>.</p><p>Therefore, induced EMF due to small element will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>&#949;</mi><mo>=</mo><mi>B</mi><mi>v</mi><mi mathvariant="normal">d</mi><mi>x</mi><mo>=</mo><mi>B</mi><mfenced><mrow><mi>&#969;</mi><mi>x</mi></mrow></mfenced><mi mathvariant="normal">d</mi><mi>x</mi></math></p><p>Integrating both sides, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mi>d</mi><mi>&#949;</mi><mo>=</mo><mo>&#8747;</mo><mi>B</mi><mfenced><mrow><mi>&#969;</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#949;</mi><mo>=</mo><mi>B</mi><mi>&#969;</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mi>L</mi></msubsup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>B</mi><mi>&#969;</mi><msup><mi>L</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math></p>

</details>

---

### Q23. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A metallic conductor of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> rotates in a vertical plane parallel to east-west direction about one of its end with angular velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. If the horizontal component of earth&#39;s magnetic field is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">T</mi></math>, then emf induced between the two ends of the conductor is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>&#956;</mi><mi>V</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mi>&#956;</mi><mi mathvariant="normal">V</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mi>V</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mi>V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mi>&#956;</mi><mi mathvariant="normal">V</mi></math>**

**Detailed Solution:**

<p>Given here,  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mi>H</mi></msub><mo>=</mo><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">T</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mo>&#160;</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>.</p><p>Emf induced in a rotating conducting rod is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>B</mi><mi>&#969;</mi><msup><mi>l</mi><mn>2</mn></msup></math></p><p>Substituting the given values, we obtain</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><msup><mfenced><mn>1</mn></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>=</mo><mn>50</mn><mo>&#160;</mo><mi>&#956;V</mi></math></p>

</details>

---

### Q24. JEE Main 2022 (24 Jun Shift 2)

*Type:* `numerical` | *Level:* `1`

A circular coil of 1000 turns each with area <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">m</mi></mrow><mn>2</mn></msup></math> is rotated about its vertical diameter at the rate of one revolution per second in a uniform horizontal magnetic field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>07</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></math>. The maximum voltage generation will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">V</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **440**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>=</mo><mn>1000</mn><mo>,</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>07</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></math></p><p>The maximum emf generated is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#949;</mi><mi>max</mi></msub><mo>=</mo><mi>N</mi><mi>B</mi><mi>A</mi><mi>&#969;</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>N</mi><mi>B</mi><mi>A</mi><mfenced><mrow><mn>2</mn><mi>&#960;</mi><mi>f</mi></mrow></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1000</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>07</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>2</mn><mi>&#960;</mi><mfenced><mn>1</mn></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>140</mn><mi>&#960;</mi></math></p><p>Thus, maximum emf is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>439</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>&#8776;</mo><mn>440</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>.</p>

</details>

---

### Q25. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>A constant magnetic field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi></math> is applied in the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>&#62;</mo><mn>0</mn></math> region. A metallic circular ring of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> is moving with a constant velocity of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> along the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis. At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>, the centre <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">O</mi></math> of the ring is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>. What will be the value of the induced emf in the ring at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">t</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> ? (Assume the velocity of the ring does not change.)</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/14cc627f-c15c-44c7-b792-d9ffdb452b8c-image.png" style="width: 233px; height: 162px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#960;</mi><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>**

**Detailed Solution:**

<p>Recall the formula of induced E.M.F. in terms of the length of the rod, and uniform magnetic field, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mi>B</mi><mi>v</mi><mi>l</mi></math>, here in the case of the ring, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>2</mn><mi>R</mi></math>,<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>E</mi><mo>=</mo><mi>B</mi><mi>v</mi><mn>2</mn><mi>R</mi></math>, when half ring enters, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mn>1</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>.</p>

</details>

---

### Q26. JEE Main 2021 (26 Aug Shift 2)

*Type:* `numerical` | *Level:* `1`

A circular coil of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi>cm</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> turns is rotated about its vertical diameter with an angular speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> in a uniform horizontal magnetic field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>0</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">T</mi></math>. The maximum emf induced in the coil will be _______<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></math> volt (rounded off to the nearest integer).

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **60**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Emf</mi><mo>=</mo><mi mathvariant="normal">B</mi><mi>&#969;</mi><mi>NAsin</mi><mi>&#969;</mi><mi mathvariant="normal">t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>Emf</mi><mi>max</mi></msub><mo>=</mo><mi>B&#969;NA</mi><mo>=</mo><mi>B&#969;N</mi><mfenced><msup><mi>&#960;R</mi><mn>2</mn></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>3</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mo>&#215;</mo><mfenced><mn>50</mn></mfenced><mo>&#215;</mo><mfenced><mn>20</mn></mfenced><mo>&#215;</mo><mfenced><mrow><mi>&#960;</mi><mo>&#215;</mo><mfrac><mn>64</mn><msup><mn>10</mn><mn>4</mn></msup></mfrac></mrow></mfenced><mo>&#8776;</mo><mn>60</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p>

</details>

---

### Q27. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The figure shows a square loop <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> of side <math><mn>5</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi></math> which is connected to a network of resistances. The whole setup is moving towards the right with a constant speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> . At some instant, a part of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> is in a uniform magnetic field of <math><mn>1</mn><mi mathvariant="normal">T</mi></math> perpendicular to the plane of the loop. If the resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> is <math><mn>1</mn><mo>.</mo><mn>7</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#937;</mi><mo>,</mo></math> the current in the loop at that instant will be close to:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2b456b23-cb2d-4c38-abba-9dfb52cac127-image.png" style="width: 419px; height: 175px;" />

**Options:**

- **(A)** <math><mn>115</mn><mi> </mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">A</mi></math>
- **(B)** <math><mn>60</mn><mi> </mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">A</mi></math>
- **(C)** <math><mn>150</mn><mi> </mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">A</mi></math>
- **(D)** <math><mn>170</mn><mi> </mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>170</mn><mi> </mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is magnetic field, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi></math> is velocity of rod and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> is the length of rod, then induced EMF in moving road is given by </p><p>    <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#949;</mi><mo>=</mo><mi>B</mi><mi>v</mi><mi>l</mi></math>     
    <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mi mathvariant="normal">T</mi></mrow></mfenced><mo>(</mo><mn>1</mn><mtext>&#8201;</mtext><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>)</mo><mo>(</mo><mn>5</mn><mtext>&#8201;</mtext><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi><mo>)</mo></math>
    <math><mo>=</mo><mn>1</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
    <math><mo>=</mo><mn>5</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>4</mn></mrow></msup><mtext>&#8201;&#8201;</mtext><mi mathvariant="normal">V</mi></math>
As given circuit forms balanced whetstone bridge, the current through <math><mn>3</mn><mtext>&#8201;</mtext><mi mathvariant="normal">&#937;</mi></math> is zero.
Equivalent resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi mathvariant="normal">e</mi><mi mathvariant="normal">q</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>4</mn><mo>&#215;</mo><mn>2</mn></mrow><mrow><mn>4</mn><mo>+</mo><mn>2</mn></mrow></mfrac><mo>+</mo><mn>1.7</mn><mo>=</mo><mn>3</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#937;</mi></math>
Current in the circuit <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#949;</mi><msub><mi>R</mi><mrow><mi mathvariant="normal">e</mi><mi mathvariant="normal">q</mi></mrow></msub></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup></mrow><mn>3</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>167</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#956;</mi><mi mathvariant="normal">A</mi><mo>&#8776;</mo><mn>170</mn><mo>&#160;</mo><mi>&#956;A</mi></math></p>

</details>

---

### Q28. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A thin strip <math><mn>10</mn><mi>&#160;</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi></math> long is on a <math><mi mathvariant="normal">U</mi></math> shaped wire of negligible resistance and it is connected to a spring of spring constant <math><mn>0.5</mn><mi>&#160;</mi><mi mathvariant="normal">N</mi><mi mathvariant="normal">&#160;</mi><msup><mrow><mi mathvariant="normal">m</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> (see figure). The assembly is kept in a uniform magnetic field of <math><mn>0.1</mn><mi>&#160;</mi><mi mathvariant="normal">T</mi><mo>.</mo></math> If the strip is pulled from its equilibrium position and released, the number of oscillations it performs before its amplitude decreases by a factor of <math><mi mathvariant="normal">e</mi></math> is <math><mi mathvariant="normal">N</mi></math> . If the mass of the strip is <math><mn>50</mn></math> grams, its resistance <math><mn>10</mn><mi mathvariant="normal">&#937;</mi></math> and air drag negligible, <math><mi mathvariant="normal">N</mi></math> will be close to:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d72e34f8-3dd4-4ae5-a09d-1dacd793ddec-image.png" style="width: 260px; height: 148px;" />

**Options:**

- **(A)** <math><mi> </mi><mn>1000</mn></math>
- **(B)** <math><mn>5000</mn></math>
- **(C)** <math><mn>10000</mn></math>
- **(D)** <math><mn>50000</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>5000</mn></math>**

**Detailed Solution:**

Equation of motion for slider: 
<math><mo>-</mo><mi mathvariant="normal">m</mi><mfrac><mrow><msup><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">x</mi></mrow><mrow><mi mathvariant="normal">d</mi><msup><mrow><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mi mathvariant="normal">k</mi><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">i</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">B</mi></math>  
<math><mi mathvariant="normal">m</mi><mfrac><mrow><msup><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">x</mi></mrow><mrow><mi mathvariant="normal">d</mi><msup><mrow><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mi mathvariant="normal">k</mi><mi mathvariant="normal">x</mi><mo>+</mo><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">B</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">v</mi></mrow><mrow><mi mathvariant="normal">R</mi></mrow></mfrac></mrow></mfenced><mi mathvariant="normal">l</mi><mi mathvariant="normal">B</mi><mo>=</mo><mn>0</mn><mi mathvariant="normal"> </mi><mo>⇒</mo><mi mathvariant="normal">m</mi><mfrac><mrow><msup><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">x</mi></mrow><mrow><mi mathvariant="normal">d</mi><msup><mrow><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">l</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">R</mi></mrow></mfrac><mo>.</mo><mfrac><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">t</mi></mrow></mfrac><mo>+</mo><mi mathvariant="normal">k</mi><mi mathvariant="normal">x</mi><mo>=</mo><mn>0</mn></math>  
Comparing with <math><mi mathvariant="normal">m</mi><mfrac><mrow><msup><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">x</mi></mrow><mrow><mi mathvariant="normal">d</mi><msup><mrow><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mi mathvariant="normal">b</mi><mo>.</mo><mfrac><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">t</mi></mrow></mfrac><mo>+</mo><mi mathvariant="normal">k</mi><mi mathvariant="normal">x</mi><mo>=</mo><mn>0</mn></math>  
<math><mi mathvariant="normal">m</mi><mo>=</mo><mi mathvariant="normal">m</mi><mi mathvariant="normal"> </mi><mo>;</mo><mi mathvariant="normal">b</mi><mo>=</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">l</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">R</mi></mrow></mfrac><mo>;</mo><mi mathvariant="normal">k</mi><mo>=</mo><mi mathvariant="normal">k</mi></math>  
We know: <math><mi mathvariant="normal">A</mi><mo>=</mo><msub><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mfrac><mrow><mo>-</mo><mi mathvariant="normal">b</mi></mrow><mrow><mn>2</mn><mi mathvariant="normal">m</mi></mrow></mfrac><mo>×</mo><mi mathvariant="normal">t</mi></mrow></msup><mo>=</mo><msub><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mo>-</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">l</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><mi mathvariant="normal">m</mi><mi mathvariant="normal">R</mi></mrow></mfrac><mo>×</mo><mi mathvariant="normal">t</mi></mrow></msup></math>  
For amplitude to be <math><msub><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>/</mo><mi mathvariant="normal">e</mi><mo>,</mo></math>  
<math><msub><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mo>-</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">l</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><mi mathvariant="normal">m</mi><mi mathvariant="normal">R</mi></mrow></mfrac><mo>×</mo><mi mathvariant="normal">t</mi></mrow></msup><mo>=</mo><mfrac><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mi mathvariant="normal">e</mi></mrow></mfrac><mo>⇒</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">l</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><mi mathvariant="normal">m</mi><mi mathvariant="normal">R</mi></mrow></mfrac><mo>×</mo><mi mathvariant="normal">t</mi><mo>=</mo><mn>1</mn></math>  
<math><mi mathvariant="normal">t</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">m</mi><mi mathvariant="normal">R</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">l</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>10,000</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></math>  
Time period = <math><mn>2</mn><mi mathvariant="normal">π</mi><msqrt><mfrac><mrow><mi mathvariant="normal">m</mi></mrow><mrow><mi mathvariant="normal">k</mi></mrow></mfrac></msqrt><mo>=</mo><mn>2</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">s</mi></math>  
Number of oscillations = <math><mfrac><mrow><mn>10,000</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mn>5,000</mn></math>

</details>

---

### Q29. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mi>&#160;</mi><mi mathvariant="normal">m</mi></math> long horizontal wire extends from North East to South West. It is falling with a speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5.0</mn><mi>&#160;</mi><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>,</mo></math> at right angles to the horizontal component of the earth&#39;s magnetic field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.3</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><mi>Wb</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>.</mo></math> The value of the induced emf in the wire is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.3</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1.1</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2.5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1.5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1.1</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7cb9c893-b011-4f1d-aaa9-2c69db647623-image.png" style="width: 250px; height: 130px;" /></p><p>The wire makes an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>&#176;</mo></math> with the magnetic field lines. Therefore, the induced emf will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mi>B</mi><mi>v</mi><mi>l</mi><mi>sin</mi><msup><mn>45</mn><mn>0</mn></msup></math></p><p><math><mo>=</mo><mn>0.3</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1.1</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p>

</details>

---

### Q30. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A solid metal cube of edge length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">&#160;</mi><mi>cm</mi></math> is moving in the positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi></math>-direction, at a constant speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. There is a uniform magnetic field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>0.1</mtext><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">T</mi></math> in the positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">z</mi></math>-direction. The potential difference between the two faces of the cube, perpendicular to the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi></math>-axis, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#xA0;</mo><mi>mV</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#xA0;</mo><mi>mV</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#xA0;</mo><mi>mV</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#xA0;</mo><mi>mV</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#xA0;</mo><mi>mV</mi></math>**

**Detailed Solution:**

<p>emf developed is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">e</mi><mo>=</mo><mi>Bvl</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi mathvariant="normal">e</mi><mo>=</mo><mtext>0.1</mtext><mfenced separators="|"><mrow><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mo>&#215;</mo><mn>6</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi mathvariant="normal">e</mi><mo>=</mo><mn>12</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>=</mo><mn>12</mn><mo>&#160;</mo><mi>mV</mi></math></p>

</details>

---

### Q31. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `2`

<p>A metallic rod of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> is tied to a string of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>l</mi></math> and made to rotate with angular speed <math> <mrow> <mi>&#969;</mi> </mrow> </math> on a horizontal table with one end of the string fixed. If there is a vertical magnetic field B in the region, the e.m.f. induced across the ends of the rod is:</p><p> <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0b3e1fe8-af80-4c27-956b-139150bf8366-image.png" style="width: 260px; height: 152px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mtext>B</mtext><mi>&#969;</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mtext>B</mtext><mi>&#969;</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mtext>B</mtext><mi>&#969;</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mtext>B</mtext><mi>&#969;</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mtext>B</mtext><mi>&#969;</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ace1a20a-4c2a-4c40-bb49-88c249a23a01-image.png" style="width: 260px; height: 90px;" />

<math><mi>e</mi><mo>=</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>2</mn><mi>l</mi></mrow><mrow><mn>3</mn><mi>l</mi></mrow></munderover><mrow><mi mathvariant="normal">B</mi><mi mathvariant="normal">V</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow></mrow></math>

<math> <mrow><mtext>e</mtext> <mo>=</mo> <munderover> <mo>&#8747;</mo> <mrow> <mn>2</mn> <mi>&#8467;</mi> </mrow> <mrow> <mn>3</mn> <mi>&#8467;</mi> </mrow></munderover></mrow></math>B(&omega;x)dx
<math><mi>e</mi><mo>=</mo><mi mathvariant="normal">&#969;</mi><mi mathvariant="normal">B</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>2</mn><mi>l</mi></mrow><mrow><mn>3</mn><mi>l</mi></mrow></munderover><mrow><mi mathvariant="normal">x</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow></mrow></math>

<math><mi>e</mi><mo>=</mo><mi mathvariant="normal">&#969;</mi><mi mathvariant="normal">B</mi><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn><mi>l</mi></mrow><mrow><mn>3</mn><mi>l</mi></mrow></msubsup></math>

<math><mi>e</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">&#969;</mi><mi mathvariant="normal">B</mi></mrow><mrow><mn>2</mn></mrow></mfrac><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mfenced separators="|"><mrow><mn>3</mn><mi>l</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><mi>l</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>2</mn><mi>l</mi></mrow><mrow><mn>3</mn><mi>l</mi></mrow></msubsup></math>

<math><mi>e</mi><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi mathvariant="normal">&#969;</mi><msup><mrow><mi mathvariant="normal">B</mi><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msup></math></p>

</details>

---

### Q32. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `3`

A rectangular loop has a sliding connector PQ of length $\ell$ and resistance $\mathrm{R} \Omega$ and it is moving with a speed $v$ as shown. The set-up is placed in a uniform magnetic field going into the plane of the paper. The three currents $I_1, I_2$ and $I$ are 
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bo-z63pX7OcPU9GNwHolUu62C_DPCEpRD3rYMWGQOqk.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{I}_1=-\mathrm{I}_2=\frac{\mathrm{B} \ell \mathrm{v}}{\mathrm{R}}, \mathrm{I}=\frac{2 \mathrm{~B} \ell \mathrm{v}}{\mathrm{R}}$
- **(B)** $\mathrm{I}_1=\mathrm{I}_2=\frac{\mathrm{B} \ell \mathrm{v}}{3 \mathrm{R}}, \mathrm{I}=\frac{2 \mathrm{~B} \ell \mathrm{v}}{3 \mathrm{R}}$
- **(C)** $l_1=I_2=I=\frac{B \ell v}{R}$
- **(D)** $I_1=I_2=\frac{B \ell v}{6 R}, I=\frac{B \ell v}{3 R}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{I}_1=\mathrm{I}_2=\frac{\mathrm{B} \ell \mathrm{v}}{3 \mathrm{R}}, \mathrm{I}=\frac{2 \mathrm{~B} \ell \mathrm{v}}{3 \mathrm{R}}$**

**Detailed Solution:**

A moving conductor is equivalent to a battery of emf $=\mathrm{v} \mathrm{B} \ell \quad$ (motion emf)
Equivalent circuit
$$
\mathrm{I}=\mathrm{l}_1+\mathrm{l}_2
$$
applying Kirchoff's law
$$
\begin{aligned}
& \mathrm{I}_1 R+I R-v B \ell=0 \\
& \mathrm{I}_2 R+I R-v B \ell=0
\end{aligned}
$$
adding (1) \& (2)
$$
\begin{aligned}
& 2 \mathrm{IR}+\mathrm{IR}=2 \mathrm{vB} \ell \\
& \mathrm{I}=\frac{2 \mathrm{vB} \ell}{3 \mathrm{R}} \\
& \mathrm{I}_1=\mathrm{I}_2=\frac{\mathrm{vB} \ell}{3 \mathrm{R}}
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/pUPjsjy75K1skV7dpyzQKQNVetAfCge7PX6GHTWQouE.original.fullsize.png">

</details>

---

### Q33. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

In an $\mathrm{AC}$ generator, a coil with $\mathrm{N}$ turns, all of the same area $\mathrm{A}$ and total resistance $\mathrm{R}$, rotates with frequency $\omega$ in a magnetic field $B$. The maximum value of emf generated in the coil is "

**Options:**

- **(A)** N.A.B. $\omega$
- **(B)** N.A.B.R. $\omega$
- **(C)** N.A.B
- **(D)** N.A.B.R

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) N.A.B. $\omega$**

**Detailed Solution:**

NBA $\omega$

</details>

---

### Q34. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

A metal conductor of length $1 \mathrm{~m}$ rotates vertically about one of its ends at angular velocity 5 radians per second. If the horizontal component of earth's magnetic field is $0.3 \times 10^{-4} \mathrm{~T}$, then the e.m.f. developed between the two ends of the conductor is

**Options:**

- **(A)** depends on the nature of the metal used
- **(B)** depends on the intensity of the radiation
- **(C)** depends both on the intensity of the radiation and the metal used
- **(D)** is the same for all metals and independent of the intensity of the radiation.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) depends on the intensity of the radiation**

**Detailed Solution:**

emf. developed is given by
$$
\varepsilon_{\text {ind }}=\frac{1}{2} \mathrm{~B} \omega \mathrm{R}^2=50 \mu \mathrm{V} \text {. }
$$

</details>

---

