# JEE Main Physics - Oscillations

## Topic 1: Simple Harmonic Motion

**Total Questions:** 68

---

### Q1. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A particle is executing simple harmonic motion. Its amplitude is $A$ and time period is $5$ sec. The time required by it to move from $x = A$ to $x = \dfrac{A}{\sqrt{2}}$ is _______ sec.

**Options:**

- **(A)** $1/4$
- **(B)** $5/4$
- **(C)** $5/8$
- **(D)** $3/8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5/8$**

**Detailed Solution:**

The equation of simple harmonic motion for a particle starting from the extreme position $x = A$ is given by:

$x = A \cos(\omega t)$

We need to find the time $t$ when the particle reaches $x = \dfrac{A}{\sqrt{2}}$. Substituting this value into the equation:

$\dfrac{A}{\sqrt{2}} = A \cos(\omega t)$

$\cos(\omega t) = \dfrac{1}{\sqrt{2}}$

$\omega t = \dfrac{\pi}{4}$

Since the angular frequency $\omega = \dfrac{2\pi}{T}$, we have:

$\dfrac{2\pi}{T} t = \dfrac{\pi}{4}$

$t = \dfrac{T}{8}$

Given the time period $T = 5$ sec, the required time is:

$t = \dfrac{5}{8}$ sec

Answer: $5/8$

</details>

---

### Q2. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Match List-I with List-II.
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><th style="border: 1px solid black; padding: 5px;">List-I</th><th style="border: 1px solid black; padding: 5px;">List-II</th></tr><tr><td style="border: 1px solid black; padding: 5px;">A. $\sin^2 \omega t$</td><td style="border: 1px solid black; padding: 5px;">I. Periodic with time period $T = \dfrac{\pi}{\omega}$ but not simple harmonic motion (SHM)</td></tr><tr><td style="border: 1px solid black; padding: 5px;">B. $\sin^3(2\omega t)$</td><td style="border: 1px solid black; padding: 5px;">II. Periodic with time period $T = \dfrac{2\pi}{\omega}$ but Not SHM</td></tr><tr><td style="border: 1px solid black; padding: 5px;">C. $\sin(\omega t) + \cos(\pi \omega t)$</td><td style="border: 1px solid black; padding: 5px;">III. Periodic with time period $T = \dfrac{\pi}{\omega}$ and SHM</td></tr><tr><td style="border: 1px solid black; padding: 5px;">D. $\cos\omega t + \cos 2\omega t$</td><td style="border: 1px solid black; padding: 5px;">IV. Non-periodic</td></tr></table>
Choose the correct answer from the options given below :

**Options:**

- **(A)** A-III, B-I, C-IV, D-II
- **(B)** A-II, B-I, C-III, D-IV
- **(C)** A-III, B-II, C-IV, D-I
- **(D)** A-II, B-I, C-IV, D-III

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) A-III, B-I, C-IV, D-II**

**Detailed Solution:**

For A: $y = \sin^2 \omega t = \dfrac{1 - \cos 2\omega t}{2} = \dfrac{1}{2} - \dfrac{1}{2} \cos 2\omega t$

This represents simple harmonic motion (SHM) about the mean position $y = \dfrac{1}{2}$ with an angular frequency of $2\omega$. The time period is $T = \dfrac{2\pi}{2\omega} = \dfrac{\pi}{\omega}$. Thus, A matches III.

For B: $y = \sin^3(2\omega t) = \dfrac{3\sin 2\omega t - \sin 6\omega t}{4}$

This is a superposition of two SHMs with angular frequencies $2\omega$ and $6\omega$. It is periodic but not SHM. The time period is the LCM of $T_1 = \dfrac{2\pi}{2\omega} = \dfrac{\pi}{\omega}$ and $T_2 = \dfrac{2\pi}{6\omega} = \dfrac{\pi}{3\omega}$, which is $T = \dfrac{\pi}{\omega}$. Thus, B matches I.

For C: $y = \sin(\omega t) + \cos(\pi \omega t)$

The angular frequencies are $\omega_1 = \omega$ and $\omega_2 = \pi \omega$. The ratio $\dfrac{\omega_1}{\omega_2} = \dfrac{1}{\pi}$ is an irrational number. Therefore, the function is non-periodic. Thus, C matches IV.

For D: $y = \cos \omega t + \cos 2\omega t$

This is a superposition of two SHMs with angular frequencies $\omega$ and $2\omega$. It is periodic but not SHM. The time period is the LCM of $T_1 = \dfrac{2\pi}{\omega}$ and $T_2 = \dfrac{2\pi}{2\omega} = \dfrac{\pi}{\omega}$, which is $T = \dfrac{2\pi}{\omega}$. Thus, D matches II.

The correct matching is A-III, B-I, C-IV, D-II.

Answer: A-III, B-I, C-IV, D-II

</details>

---

### Q3. JEE Main 2026 (04 April Shift 1)

*Type:* `numerical` | *Level:* `2`

The velocity of a particle executing simple harmonic motion along $x$-axis is described as $v^2 = 50 - x^2$, where $x$ represents displacement. If the time period of motion is $\dfrac{x}{7}$ s, the value of $x$ is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **44**

**Detailed Solution:**

The given equation is $v^2 = 50 - x^2$

Differentiating with respect to $x$:

$2v \dfrac{dv}{dx} = -2x$

$v \dfrac{dv}{dx} = -x$

Since acceleration $a = v \dfrac{dv}{dx}$, we get:

$a = -x$

Comparing this with the standard equation of SHM $a = -\omega^2 x$, we get:

$\omega^2 = 1 \Rightarrow \omega = 1$ rad/s

The time period of the motion is given by:

$T = \dfrac{2\pi}{\omega} = 2\pi$

Taking $\pi = \dfrac{22}{7}$, we get:

$T = 2 \times \dfrac{22}{7} = \dfrac{44}{7}$ s

Given that the time period is $\dfrac{x}{7}$ s, comparing the two gives:

$x = 44$

Answer: $44$

</details>

---

### Q4. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The equation of motion of a particle is given by $x = a \sin\left(50t + \dfrac{\pi}{3}\right)$ cm. The particle will come to rest at time $t_1$ and it will have zero acceleration at time $t_2$. The $t_1$ and $t_2$ respectively are _______.

**Options:**

- **(A)** $\dfrac{\pi}{300} \, s, \dfrac{\pi}{75} \, s$
- **(B)** $\dfrac{\pi}{75} \, s, \dfrac{\pi}{300} \, s$
- **(C)** $\dfrac{\pi}{300} \, s, \dfrac{\pi}{25} \, s$
- **(D)** $\dfrac{\pi}{50} \, s, \dfrac{\pi}{100} \, s$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\pi}{300} \, s, \dfrac{\pi}{75} \, s$**

**Detailed Solution:**

The equation of motion is given by $x = a \sin\left(50t + \dfrac{\pi}{3}\right)$.

Velocity is the rate of change of displacement:
$v = \dfrac{dx}{dt} = 50a \cos\left(50t + \dfrac{\pi}{3}\right)$

The particle comes to rest when $v = 0$. For the first time it comes to rest:
$\cos\left(50t_1 + \dfrac{\pi}{3}\right) = 0$

$50t_1 + \dfrac{\pi}{3} = \dfrac{\pi}{2}$

$50t_1 = \dfrac{\pi}{2} - \dfrac{\pi}{3} = \dfrac{\pi}{6}$

$t_1 = \dfrac{\pi}{300} \text{ s}$

Acceleration is the rate of change of velocity:
$A = \dfrac{dv}{dt} = -2500a \sin\left(50t + \dfrac{\pi}{3}\right)$

The particle has zero acceleration when $A = 0$. For the first time it has zero acceleration:
$\sin\left(50t_2 + \dfrac{\pi}{3}\right) = 0$

$50t_2 + \dfrac{\pi}{3} = \pi$

$50t_2 = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$

$t_2 = \dfrac{2\pi}{150} = \dfrac{\pi}{75} \text{ s}$

Answer: $\dfrac{\pi}{300} \, s, \dfrac{\pi}{75} \, s$

</details>

---

### Q5. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

As shown in the figure, a spring is kept in a stretched position with some extension by holding the masses 1 kg and 0.2 kg with a separation more than spring natural length and are released. Assuming the horizontal surface to be frictionless, the angular frequency (in SI unit) of the system is : $k=150 \mathrm{~N} / \mathrm{m}$ 
 <img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/28S2_q_39_1.png">

**Options:**

- **(A)** 5
- **(B)** 27
- **(C)** 20
- **(D)** 30

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 30**

**Detailed Solution:**

Two masses (1 kg and 0.2 kg) connected by a spring (k = 150 N/m) on a frictionless surface undergo oscillation about their center of mass.
This two-body problem reduces to SHM with reduced mass $\mu = \frac{m_1 m_2}{m_1 + m_2} = \frac{1 \times 0.2}{1.2} = \frac{1}{6}$ kg.
The angular frequency is $\omega = \sqrt{\frac{k}{\mu}} = \sqrt{\frac{150}{1/6}} = \sqrt{900} = 30$ rad/s.

</details>

---

### Q6. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A cylindrical block of mass $M$ and area of cross section $A$ is floating in a liquid of density $\rho$ and with its axis vertical. When depressed a little and released the block starts oscillating. The period of oscillation is $\_\_\_\_$.

**Options:**

- **(A)** $\pi \sqrt{\frac{2 M}{\rho A g}}$
- **(B)** $\pi \sqrt{\frac{\rho A}{M g}}$
- **(C)** $2 \pi \sqrt{\frac{\rho A}{M g}}$
- **(D)** $2 \pi \sqrt{\frac{M}{\rho A g}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 \pi \sqrt{\frac{M}{\rho A g}}$**

**Detailed Solution:**

When the block is depressed by distance $x$, the additional buoyant force is $F = \rho Agx$ acting upward as restoring force. 
Equation of motion: $M\frac{d^2x}{dt^2} = -\rho Agx$. 
This gives $\omega^2 = \frac{\rho Ag}{M}$. 
Period of oscillation: $T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{M}{\rho Ag}}$

</details>

---

### Q7. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A particle is subjected two simple harmonic motions as :
$\mathrm{x}_1=\sqrt{7} \sin 5 \mathrm{tcm}$ 
and $x_2=2 \sqrt{7} \sin \left(5 t+\frac{\pi}{3}\right) \mathrm{cm}$
where x is displacement and $t$ is time in seconds. The maximum acceleration of the particle is $\mathrm{x} \times 10^{-2} \mathrm{~ms}^{-2}$. The value of x is :

**Options:**

- **(A)** $175$
- **(B)** $25 \sqrt{7}$
- **(C)** $5 \sqrt{7}$
- **(D)** $125$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $175$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{x}_1=\sqrt{7} \sin 5 \mathrm{t} \\ & \mathrm{x}_2=2 \sqrt{7} \sin \left(5 \mathrm{t}+\frac{\pi}{3}\right)\end{aligned}$
From phasor,
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4Kx0fElAHpb5zMDZEyiepYxWbjy8P19Z9AcOkPSLzj8.original.fullsize.png"/>
$\therefore$ Amplitude of resultant $\mathrm{SHM}=7$
$\begin{aligned} & \phi=\tan ^{-1} \frac{2 \sqrt{7} \times \sqrt{3} / 2}{\sqrt{7}+2 \sqrt{7} \times \frac{1}{2}}=\tan ^{-1} \frac{\sqrt{21}}{2 \sqrt{7}}=\tan ^{-1} \frac{\sqrt{3}}{2} \\ & \therefore \quad \mathrm{X}_{\mathrm{R}}=7 \sin (5 \mathrm{t}+\phi) \\ & \quad \mathrm{a}_{\mathrm{R}}=-7 \times 25 \sin (5 \mathrm{t}+\phi) \\ & \therefore \mathrm{a}_{\max }=175 \mathrm{~cm} / \mathrm{sec}=175 \times 10^{-2} \mathrm{~m} / \mathrm{sec}\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Two bodies A and B of equal mass are suspended from two massless springs of spring constant $k_1$ and $k_2$, respectively. If the bodies oscillate vertically such that their amplitudes are equal, the ratio of the maximum velocity of $A$ to the maximum velocity of $B$ is

**Options:**

- **(A)** $\frac{\mathrm{k}_1}{\mathrm{k}_2}$
- **(B)** $\sqrt{\frac{\mathrm{k}_1}{\mathrm{k}_2}}$
- **(C)** $\sqrt{\frac{\mathrm{k}_2}{\mathrm{k}_1}}$
- **(D)** $\frac{\mathrm{k}_2}{\mathrm{k}_1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{\frac{\mathrm{k}_1}{\mathrm{k}_2}}$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{V}_1=\mathrm{A}_1 \omega_1 \\ & \mathrm{~V}_2=\mathrm{A}_2 \omega_2 \\ & \mathrm{~A}_1=\mathrm{A}_2 \\ & \frac{\mathrm{~V}_1}{\mathrm{~V}_2}=\frac{\omega_1}{\omega_2}=\frac{\sqrt{\frac{\mathrm{K}_1}{\mathrm{~m}}}}{\sqrt{\frac{\mathrm{~K}_2}{\mathrm{~m}}}} \\ & \frac{\mathrm{~V}_1}{\mathrm{~V}_2}=\sqrt{\frac{\mathrm{K}_1}{\mathrm{~K}_2}}\end{aligned}$

</details>

---

### Q9. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A particle is executing simple harmonic motion with time period 2 s and amplitude 1 cm . If D and d are the total distance and displacement covered by the particle in 12.5 s , then $\frac{\mathrm{D}}{\mathrm{d}}$ is

**Options:**

- **(A)** $\frac{16}{5}$
- **(B)** $10$
- **(C)** $\frac{15}{4}$
- **(D)** $25$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $25$**

**Detailed Solution:**

A = 1 cm
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/uf2aSRAqlvDN2cj22DMM0nwdFMx9_7V_ItqgVYGCJIg.original.fullsize.png">


$\begin{aligned} & \mathrm{n}=\frac{12.5}{2}=6.25 \text { cycles } \\ & \therefore \mathrm{D}=4 \times 6+1=25 \\ & \mathrm{~d}=1 \\ & \frac{D}{d}=25\end{aligned}$

</details>

---

### Q10. JEE Main 2024 (09 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

The position, velocity and acceleration of a particle executing simple harmonic motion are found to have magnitudes of $4 \mathrm{~m}, 2 \mathrm{~ms}^{-1}$ and $16 \mathrm{~ms}^{-2}$ at a certain instant. The amplitude of the motion is $\sqrt{x}, \mathrm{~m}$ where $x$ is ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **17**

**Detailed Solution:**

$\begin{aligned} & x=4 \mathrm{~m}, V=2 \mathrm{~m} / \mathrm{s}, \mathrm{a}=16 \mathrm{~m} / \mathrm{s}^2 \\ & |\mathrm{a}|=\omega^2 \mathrm{x} \\ & \Rightarrow 16=\omega^2(4) \\ & \omega=2 \mathrm{rad} / \mathrm{s} \\ & \mathrm{v}=\omega \sqrt{\mathrm{A}^2-\mathrm{x}^2} \\ & A=\sqrt{\frac{\mathrm{v}^2}{\omega^2}+\mathrm{x}^2} \Rightarrow \mathrm{A}=\sqrt{\frac{4}{4}+16} \\ & A=\sqrt{17} \mathrm{~m}\end{aligned}$

</details>

---

### Q11. JEE Main 2024 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

An object of mass $0.2 \mathrm{~kg}$ executes simple harmonic motion along $\mathrm{x}$ axis with frequency of $\left(\frac{25}{\pi}\right) \mathrm{Hz}$. At the position $x=0.04 \mathrm{~m}$ the object has kinetic energy $0.5 \mathrm{~J}$ and potential energy $0.4 \mathrm{~J}$. The amplitude of oscillation is _____$\mathrm{cm}$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

$\begin{aligned} & \text { Total energy }=\text { K.E. }+ \text { P.E. } \\ & \text { at } x=0.04 \mathrm{~m}, \text { T.E. }=0.5+0.4=0.9 \mathrm{~J} \\ & \begin{aligned} \text { T.E } & =1 \mathrm{~m} \omega^2 \mathrm{~A}^2=0.9 \\ & =\frac{1}{2} \times 0.2\left(2 \pi \times \frac{25}{\pi}\right)^2 \times \mathrm{A}^2=0.9 \\ \Rightarrow \mathrm{A} & =0.06 \mathrm{~m} \\ \mathrm{~A} & =6 \mathrm{~cm}\end{aligned}\end{aligned}$

</details>

---

### Q12. JEE Main 2024 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

A particle is doing simple harmonic motion of amplitude $0.06 \mathrm{~m}$ and time period $3.14 \mathrm{~s}$. The maximum velocity of the particle is _______ $\mathrm{cm} / \mathrm{s}$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

We know
$\begin{aligned}
\mathrm{V}_{\max } & =\omega \mathrm{A} \quad \text { at mean position } \\
& =\frac{2 \pi}{\mathrm{T}} \mathrm{A}=\frac{2 \pi}{\pi} \times 0.06=0.12 \mathrm{~m} / \mathrm{sec} \\
\mathrm{V}_{\max } & =12 \mathrm{~cm} / \mathrm{sec}
\end{aligned}$

</details>

---

### Q13. JEE Main 2024 (04 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

The displacement of a particle executing SHM is given by $x=10 \sin \left(w t+\frac{\pi}{3}\right) m$. The time period of motion is $3.14 \mathrm{~s}$. The velocity of the particle at $t=0$ is ______$\mathrm{m} / \mathrm{s}$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

Given,
$\begin{aligned}
& \mathrm{T}=3.14=\frac{2 \pi}{\omega} \\
& \omega=2 \mathrm{rad} / \mathrm{s} \\
& \mathrm{x}=10 \sin \left(\omega \mathrm{t}+\frac{\pi}{3}\right) \\
& \mathrm{v}=\frac{\mathrm{dx}}{\mathrm{dt}}=10 \omega \cos \left(\omega \mathrm{t}+\frac{\pi}{3}\right) \\
& \text { at } \mathrm{t}=0 \\
& \mathrm{v}=10 \omega \cos \left(\frac{\pi}{3}\right)=10 \times 2 \times \frac{1}{2}[\mathrm{using} \omega=2 \mathrm{rad} / \mathrm{s}] \\
& \mathrm{v}=10 \mathrm{~m} / \mathrm{s}
\end{aligned}$

</details>

---

### Q14. JEE Main 2024 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

A particle performs simple harmonic motion with amplitude <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. Its speed is increased to three times at an instant when its displacement is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>A</mi></mrow><mn>3</mn></mfrac></math>. The new amplitude of motion is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><mi>A</mi></mrow><mn>3</mn></mfrac></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

<p>Speed in SHM in terms of displacement is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mi>ω</mi><msqrt><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></math>.</p><p>at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>A</mi></mrow><mn>3</mn></mfrac></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mi>ω</mi><msqrt><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><msup><mfenced><mfrac><mrow><mn>2</mn><mi>A</mi></mrow><mn>3</mn></mfrac></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><mfrac><mrow><msqrt><mn>5</mn></msqrt><mi>A</mi><mi>ω</mi></mrow><mn>3</mn></mfrac></math></p><p>Let the new amplitude be<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>A</mi><mo>'</mo></math></p><p>Then, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>'</mo><mo>=</mo><mn>3</mn><mi>v</mi><mspace linebreak="newline"></mspace><mo>⇒</mo><mi>ω</mi><msqrt><msup><mfenced><mrow><mi>A</mi><mo>'</mo></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mfrac><mrow><mn>2</mn><mi>A</mi></mrow><mn>3</mn></mfrac></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>5</mn></msqrt><mi>A</mi><mi>ω</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>'</mo><mo>=</mo><mfrac><mn>7</mn><mn>3</mn></mfrac><mi>A</mi></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>7</mn></math>. </p>

</details>

---

### Q15. JEE Main 2024 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

A simple harmonic oscillator has an amplitude <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and time period <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>π</mi></math> second. Assuming the oscillation starts from its mean position, the time required by it to travel from<math xmlns="http://www.w3.org/1998/Math/MathML"><mo> </mo><mi>x</mi><mo>=</mo><mi>A</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mi>A</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mi>x</mi></mfrac><mo> </mo><mi mathvariant="normal">s</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mo>.</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5e1960e6-8be0-43d2-ac3c-33e02f70c0fe.png" style="width: 350px; height: 233px;"/></p><p>From phasor diagram particle has to move from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> in a circle of radius equal to amplitude of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>SHM</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>ϕ</mi><mo>=</mo><mfrac><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo> </mo><mi mathvariant="normal">A</mi></mrow><mn>2</mn></mfrac><mrow><mo> </mo><mi mathvariant="normal">A</mi></mrow></mfrac><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>ϕ</mi><mo>=</mo><mfrac><mi>π</mi><mn>6</mn></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mn>6</mn></mfrac><mo>=</mo><mi>ω</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>π</mi><mn>6</mn></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mi>T</mi></mfrac><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>π</mi><mn>6</mn></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>6</mn><mi>π</mi></mrow></mfrac><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>t</mi><mo>=</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q16. JEE Main 2024 (27 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

A particle executes simple harmonic motion with an amplitude of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo> </mo><mi>cm</mi></math>. At the mean position, velocity of the particle is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo> </mo><mi>cm</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The distance of the particle from the mean position when its speed becomes <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo> </mo><mi>cm</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>α</mi></msqrt><mo> </mo><mi>cm</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo></math>______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<p>The formula to calculate the velocity of the particle at the mean position is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mi>A</mi><mi>ω</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>From equation (1), it follows that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>=</mo><mn>4</mn><mo>×</mo><mi>ω</mi><mspace linebreak="newline"></mspace><mo>⇒</mo><mi>ω</mi><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo> </mo><mi>rad</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>The formula to calculate the velocity of the particle at any instantaneous position <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> can be expressed as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mi>ω</mi><msqrt><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>From equation (2), it follows that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><msqrt><msup><mn>4</mn><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mspace linebreak="newline"></mspace><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>16</mn><mo>-</mo><mn>4</mn><mspace linebreak="newline"></mspace><mo>=</mo><mn>12</mn><mspace linebreak="newline"></mspace><mo>⇒</mo><mi>x</mi><mo>=</mo><msqrt><mn>12</mn></msqrt><mo> </mo><mi>cm</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mn>12</mn></math>.</p>

</details>

---

### Q17. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>In a linear Simple Harmonic Motion (SHM)</p><p>(A) Restoring force is directly proportional to the displacement.</p><p>(B) The acceleration and displacement are opposite in direction.</p><p>(C) The velocity is maximum at mean position.</p><p>(D) The acceleration is minimum at extreme points.</p><p>Choose the correct answer from the options given below:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">C</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">D</mi></mfenced></math> only
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">A</mi></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mi mathvariant="normal">C</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">D</mi></mfenced></math> only
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">A</mi></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mi mathvariant="normal">B</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">C</mi></mfenced></math> only
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">A</mi></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mi mathvariant="normal">B</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">D</mi></mfenced></math> only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">A</mi></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mi mathvariant="normal">B</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">C</mi></mfenced></math> only**

**Detailed Solution:**

<blockquote><p>The equations of SHM is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mo>&#8211;</mo><mi>k</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>&#8211;</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mi>x</mi></math></p><p>Velocity is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mi>&#969;</mi><msqrt><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></math>.</p><p>Clearly, velocity is maximum at mean position and acceleration is maximum at extreme positions.</p><p>Hence, this is the correct option.</p></blockquote>

</details>

---

### Q18. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For a periodic motion represented by the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>sin&#969;</mi><mi>t</mi><mo>+</mo><mi>cos&#969;</mi><mi>t</mi></math> the amplitude of the motion is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<blockquote><p>Given the equation of motion is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>sin&#969;</mi><mi>t</mi><mo>+</mo><mi>cos&#969;</mi><mi>t</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Simplify equation (1) to obtain the standard form:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mi>y</mi></mtd><mtd><mo>=</mo></mtd><mtd><msqrt><mn>2</mn></msqrt><mfenced><mrow><mi>sin</mi><mi>&#969;</mi><mi>t</mi><mi>cos</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mi>cos</mi><mi>&#969;</mi><mi>t</mi><mi>sin</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><msqrt><mn>2</mn></msqrt><mi>sin</mi><mfenced separators="|"><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mfrac><mstyle displaystyle="true"><mi>&#960;</mi></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></mtd></mtr></mtable></math></p><p>Comparing equation (2) with standard equation of SHM <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>A</mi><mi>sin</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi></mrow></mfenced></math>, we get amplitude of the given oscillation as <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt></math>.</p></blockquote>

</details>

---

### Q19. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>For particle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> revolving round the centre <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> with radius of circular path <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> and regular velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi></math>, as shown in below figure, the projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>P</mi></math> on the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis at time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> is</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/40424b7c-3f2d-42c6-80d3-c2a6dadfa149.png" style="width: 300px; height: 201px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mi>r</mi><mo>&#160;</mo><mi>cos</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mi>r</mi><mo>&#160;</mo><mi>cos</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mi>r</mi><mo>&#160;</mo><mi>sin</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mi>r</mi><mo>&#160;</mo><mi>cos</mi><mo>(</mo><mi>&#969;</mi><mi>t</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mi>r</mi><mo>&#160;</mo><mi>cos</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>As can be seen from the diagram, the initial phase of the particle is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mi>&#966;</mi></mtd><mtd><mo>=</mo></mtd><mtd><mn>30</mn><mo>&#176;</mo></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mtd></mtr></mtable></math></p><p>The equation of motion of the particle at its initial position at time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn></math> can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mi>r</mi><mi>cos</mi><mi>&#952;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> is the angular displacement of the particle at time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mi>t</mi></math>.</p><p>Since, the position of the particle at a later instant of time always lags behind its initial position at time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn></math>, the equation of motion of the particle at any instant of time is given by</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mi>r</mi><mi>cos</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mi>&#966;</mi></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Substitute the values of the known parameters into equation (2) to obtain the required expression</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mi>r</mi><mo>&#160;</mo><mi>cos</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></math></p></blockquote>

</details>

---

### Q20. JEE Main 2023 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

A particle of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>250</mn><mo>&#160;</mo><mi mathvariant="normal">g</mi></math> executes a simple harmonic motion under a periodic force <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mo>(</mo><mo>&#8211;</mo><mn>25</mn><mi>x</mi><mo>)</mo><mo>&#160;</mo><mi mathvariant="normal">N</mi></math>. The particle attains a maximum speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> during its oscillation. The amplitude of the motion is ______<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cm</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **40**

**Detailed Solution:**

<p>Given, force <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mo>(</mo><mo>&#8211;</mo><mn>25</mn><mi>x</mi><mo>)</mo><mo>&#160;</mo><mi mathvariant="normal">N</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>.</mo><mn>25</mn><mi>a</mi><mo>=</mo><mo>-</mo><mn>25</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mn>100</mn><mi>x</mi></math></p><p>Now comparing it with standard equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mi>x</mi></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mn>10</mn></math>.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow></msub><mo>=</mo><mi>&#969;</mi><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#969;</mi><mi>A</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><mn>4</mn><mn>10</mn></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mn>40</mn><mo>&#160;</mo><mi>cm</mi></math>.</p>

</details>

---

### Q21. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A particle executes simple harmonic motion between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>&#8211;</mo><mi>A</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>x</mi><mo>=</mo><mo>+</mo><mi>A</mi></math>. If time taken by particle to go from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>A</mi><mn>2</mn></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>; then time taken by particle in going from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>A</mi><mn>2</mn></mfrac></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/54edda86-c83e-4104-ab1e-37ff19be5f64-f40d1b4d-f99e-4b0b-9697-66502a077b73-9894470.PNG" style="width: 300px; height: 195px;" /></p><p>The position of a particle performing an SHM is given by:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>A</mi><mo>&#160;</mo><mi>sin</mi><mo>(</mo><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi><mo>)</mo></math></p><p>Since at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>, the particle is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, therefore the initial phase <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mn>0</mn></math>.</p><p>At time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>, the particle is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>A</mi><mn>2</mn></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfrac><mi>A</mi><mn>2</mn></mfrac><mo>=</mo><mi>A</mi><mo>&#160;</mo><mi>sin</mi><mfenced><mrow><mn>2</mn><mi>&#969;</mi></mrow></mfenced><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>&#969;</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>12</mn></mfrac><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Therefore, time period</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow><mi>&#969;</mi></mfrac><mo>=</mo><mn>24</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math></p><p>The total time taken from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>A</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>T</mi><mn>4</mn></mfrac><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>.</p><p>Since the time taken from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>A</mi><mn>2</mn></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>, therefore the time taken from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>A</mi><mn>2</mn></mfrac></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>A</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>.</p>

</details>

---

### Q22. JEE Main 2022 (28 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

The potential energy of a particle of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi>kg</mi></math> in motion along the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">U</mi><mo>=</mo><mn>4</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>4</mn><mi mathvariant="normal">x</mi></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">J</mi></math>. The time period of the particle for small oscillation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>sin</mi><mi>&#952;</mi><mo>&#8771;</mo><mi>&#952;</mi></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mi>&#960;</mi><mi mathvariant="normal">K</mi></mfrac></mfenced><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<blockquote><p>Given here, potential energy, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>U</mi><mo>=</mo><mn>4</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>4</mn><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">J</mi></math></p><p>Using the relation between conservative force and potential energy, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mo>d</mo><mi>U</mi></mrow><mrow><mo>d</mo><mi>x</mi></mrow></mfrac></math>.</p><p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mo>-</mo><mn>4</mn><mfenced><mrow><mo>+</mo><mi>sin</mi><mn>4</mn><mi>x</mi></mrow></mfenced><mn>4</mn><mo>=</mo><mo>-</mo><mn>16</mn><mi>sin</mi><mfenced><mrow><mn>4</mn><mi>x</mi></mrow></mfenced></math></p><p>For small <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>&#952;</mi><mo>&#8776;</mo><mi>&#952;</mi></math>.</p><p>Acceleration of particle is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>64</mn><mi>x</mi></mrow><mi>m</mi></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>64</mn><mi>x</mi></mrow><mn>4</mn></mfrac><mo>=</mo><mo>-</mo><mn>16</mn><mi>x</mi></math></p><p>As the oscillations are simple harmonic in nature, so  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mi>x</mi><mo>&#8658;</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mo>=</mo><mn>16</mn><mo>&#8658;</mo><mi>&#969;</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Now, time period of oscillation is<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mi>&#969;</mi></mfrac><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>.</p><p>Thus, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>=</mo><mn>2</mn></math>.</p></blockquote>

</details>

---

### Q23. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

When a particle executes simple Harmonic motion, the nature of graph of velocity as function of displacement will be

**Options:**

- **(A)** Circular
- **(B)** Ellipitical
- **(C)** Sinusoidal
- **(D)** Straight line

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Ellipitical**

**Detailed Solution:**

<blockquote><p>The displacement equation of a particle is given by </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>A</mi><mi>sin</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi></mrow></mfenced><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>sin</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi></mrow></mfenced><mo>=</mo><mfrac><mi>x</mi><mi>A</mi></mfrac></math></p><p>The velocity equation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mi>&#969;</mi><mi>A</mi><mi>cos</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi></mrow></mfenced><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>cos</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi></mrow></mfenced><mo>=</mo><mfrac><mi>v</mi><mrow><mi>&#969;</mi><mi>A</mi></mrow></mfrac></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>A</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>v</mi><mn>2</mn></msup><mrow><msup><mi>&#969;</mi><mn>2</mn></msup><msup><mi>A</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p>The above equation represents an ellipse.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8030a3c7-898f-46d8-b4bf-97f1ca5755c3-image.png" style="width: 242px; height: 170px;" /></p></blockquote>

</details>

---

### Q24. JEE Main 2022 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `1`

Two waves executing simple harmonic motion travelling in the same direction with same amplitude and frequency are superimposed. The resultant amplitude is equal to the <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt></math> times of amplitude of individual motions. The phase difference between the two motions is _____ (degree)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **60**

**Detailed Solution:**

<blockquote><p>When two waves of the same frequency superimpose, the resultant amplitude is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mrow><mi>resultant</mi><mo>&#160;</mo></mrow></msub><mo>=</mo><msqrt><msubsup><mi>A</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>A</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><mn>2</mn><msub><mi>A</mi><mn>1</mn></msub><msub><mi>A</mi><mn>2</mn></msub><mi>cos</mi><mi>&#981;</mi></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi>A</mi><mo>=</mo><msqrt><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mi>A</mi><mn>2</mn></msup><mi>cos</mi><mi>&#981;</mi></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mi>A</mi><mn>2</mn></msup><mi>cos</mi><mi>&#981;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>&#981;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#981;</mi><mo>=</mo><mn>60</mn><mo>&#176;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>Phase difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>60</mn></math> degree</p></blockquote>

</details>

---

### Q25. JEE Main 2022 (29 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The motion of a simple pendulum executing S.H.M. is represented by the following equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>A</mi><mi>sin</mi><mfenced><mrow><mi>&#960;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi></mrow></mfenced></math>, where time is measured in second. The length of pendulum is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>97</mn><mo>.</mo><mn>23</mn><mo>&#160;</mo><mi>cm</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mo>.</mo><mn>3</mn><mo>&#160;</mo><mi>cm</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>99</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi>cm</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>406</mn><mo>.</mo><mn>1</mn><mo>&#160;</mo><mi>cm</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>99</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi>cm</mi></math>**

**Detailed Solution:**

<p>Comparing the given equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>A</mi><mi>sin</mi><mfenced><mrow><mi>&#960;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi></mrow></mfenced></math> with a standard equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>A</mi><mi>sin</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi></mrow></mfenced></math>. We have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mi>&#960;</mi><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Since time period is  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mi>&#969;</mi></mfrac><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>, it is a second&#39;s pendulum.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mn>2</mn><mi>&#960;</mi><msqrt><mfrac><mi>L</mi><mi>g</mi></mfrac></msqrt><mo>&#8658;</mo><mi>L</mi><mo>=</mo><mfrac><mi>g</mi><msup><mi>&#960;</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>99</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi>cm</mi></math></p>

</details>

---

### Q26. JEE Main 2022 (29 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

A body is performing simple harmonic with an amplitude of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>cm</mi></math>. The velocity of the body was tripled by air Jet when it is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math> from its mean position. The new amplitude of vibration is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>x</mi></msqrt><mo>&#160;</mo><mi>cm</mi></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **700**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/872a3447-aafc-452a-bfa7-06f16ee24315-image.png" style="width: 240px; height: 75px;" /></p><p>In SHM, velocity of the particle at any displacement, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><msqrt><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></math>.</p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>v</mi><mrow><mn>3</mn><mi>v</mi></mrow></mfrac><mo>=</mo><mfrac><mfenced><msqrt><msubsup><mi>A</mi><mn>1</mn><mn>2</mn></msubsup><mo>-</mo><mn>25</mn></msqrt></mfenced><msqrt><msubsup><mi>A</mi><mn>2</mn><mn>2</mn></msubsup><mo>-</mo><mn>25</mn></msqrt></mfrac></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><msubsup><mi>A</mi><mn>2</mn><mn>2</mn></msubsup><mo>-</mo><mn>25</mn></msqrt><mo>=</mo><mn>3</mn><mo>&#215;</mo><msqrt><mn>75</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mi>A</mi><mn>2</mn><mn>2</mn></msubsup><mo>=</mo><mn>700</mn></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><msqrt><mn>700</mn></msqrt><mo>&#160;</mo><mi>cm</mi></math></p>

</details>

---

### Q27. JEE Main 2022 (27 Jun Shift 2)

*Type:* `numerical` | *Level:* `1`

A particle executes simple harmonic motion. Its amplitude is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi>cm</mi></math> and time period is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>. The time it will take to travel from its position of maximum displacement to the point corresponding to half of its amplitude, is _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">s</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>Given here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>8</mn><mo>&#160;</mo><mi>cm</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math></p><p>The displacement equation in SHM, when amplitude is halved is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>cos</mi><mfenced><mfrac><mrow><mn>2</mn><mi>&#960;</mi><mi>t</mi></mrow><mi>T</mi></mfrac></mfenced><mo>=</mo><mfrac><mi>A</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi><mi>t</mi></mrow><mi>T</mi></mfrac><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math></p><p>Time taken by the particle is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>T</mi><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>6</mn><mn>6</mn></mfrac><mo>=</mo><mn>1</mn><mi>sec</mi></math>.</p>

</details>

---

### Q28. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The equation of a particle executing simple harmonic motion is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>sin</mi><mi>&#960;</mi><mfenced><mrow><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>. At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>, the speed of particle will be (Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>=</mo><mn>3</mn><mo>.</mo><mn>14</mn></math>)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>157</mn><mo>&#160;</mo><mi>cm</mi><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#160;</mo><mi>cm</mi><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>272</mn><mo>&#160;</mo><mi>cm</mi><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>314</mn><mo>&#160;</mo><mi>cm</mi><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>157</mn><mo>&#160;</mo><mi>cm</mi><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>sin</mi><mfenced><mrow><mi>&#960;</mi><mi>t</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></math></p><p>Velocity  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mfrac><mrow><mo>d</mo><mi>x</mi></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac><mo>=</mo><mi>&#960;</mi><mi>cos</mi><mfenced><mrow><mi>&#960;</mi><mi>t</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></math></p><p>Now, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mi>&#960;</mi><mi>cos</mi><mfenced><mrow><mi>&#960;</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mo>.</mo><mn>14</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mo>-</mo><mn>1</mn><mo>.</mo><mn>57</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8658;</mo><mfenced open="|" close="|"><mi mathvariant="normal">v</mi></mfenced><mo>=</mo><mn>157</mn><mo>&#160;</mo><mi>cm</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p>

</details>

---

### Q29. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Two massless springs with spring constants <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">k</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi mathvariant="normal">k</mi></math>, carry <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>&#160;</mo><mi mathvariant="normal">g</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">g</mi></math> masses at their free ends. These two masses oscillate vertically such that their maximum velocities are equal. Then, the ratio of their respective amplitudes will be :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>:</mo><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>:</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>:</mo><mn>2</mn></math>**

**Detailed Solution:**

<p>Maximum velocity is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mi>max</mi></msub><mo>=</mo><mi>&#969;</mi><mi>A</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mfrac><mi>k</mi><mi>m</mi></mfrac></msqrt><mi>A</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/410f6e8b-ab56-475f-bdcf-0e037fc21bb4-image.png" style="width: 200px; height: 179px;" /></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><msub><mi>k</mi><mn>1</mn></msub><msub><mi>m</mi><mn>1</mn></msub></mfrac></msqrt><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><msqrt><mfrac><msub><mi>k</mi><mn>2</mn></msub><msub><mi>m</mi><mn>2</mn></msub></mfrac></msqrt><msub><mi>A</mi><mn>2</mn></msub></math></p><p>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mfrac><mrow><mn>2</mn><mi>k</mi></mrow><mrow><mn>50</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfrac></msqrt><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><msqrt><mfrac><mrow><mn>9</mn><mi>k</mi></mrow><mrow><mn>100</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfrac></msqrt><msub><mi>A</mi><mn>2</mn></msub></math></p><p>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><msub><mi>A</mi><mn>2</mn></msub></math></p><p>Thus, ratio of amplitude is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>A</mi><mn>1</mn></msub><msub><mi>A</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>=</mo><mn>3</mn><mo>:</mo><mn>2</mn></math>.</p>

</details>

---

### Q30. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A bob of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> suspended by a thread of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#8467;</mi></math> undergoes simple harmonic oscillations with time period <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>.</mo></math> If the bob is immersed in a liquid that has density <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math> times that of the bob and the length of the thread is increased by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mrow><mi>r</mi><mi>d</mi></mrow></msup></math> of the original length, then the time period of the simple harmonic oscillations will be:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac><mi>T</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>T</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac><mi>T</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>T</mi></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mn>2</mn><mi>&#960;</mi><msqrt><mfrac><mi>&#8467;</mi><mi>g</mi></mfrac></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>g</mi><mrow><mi>e</mi><mi>f</mi><mi>f</mi></mrow></msub><mo>=</mo><mi>g</mi><mo>-</mo><mfrac><mi>g</mi><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mi>g</mi></mrow><mn>4</mn></mfrac><mo>&#160;&#160;</mo><mspace linebreak="newline"/><mo>&#8756;</mo><mo>&#160;</mo><mi>T</mi><mo>'</mo><mo>=</mo><mn>2</mn><mi>&#960;</mi><msqrt><mfrac><mrow><mn>4</mn><mi>&#8467;</mi><mo>/</mo><mn>3</mn></mrow><mrow><mn>3</mn><mi>g</mi><mo>/</mo><mn>4</mn></mrow></mfrac></msqrt><mo>=</mo><mn>2</mn><mi>&#960;</mi><msqrt><mfrac><mrow><mn>16</mn><mi>&#8467;</mi></mrow><mrow><mn>9</mn><mi>g</mi></mrow></mfrac></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>&#39;</mo><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi>T</mi></math>

</details>

---

### Q31. JEE Main 2021 (31 Aug Shift 1)

*Type:* `numerical` | *Level:* `2`

A particle of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>kg</mi></math> is hanging from a spring of force constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>.</mo></math> The mass is pulled slightly downward and released so that it executes free simple harmonic motion with time period <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>.</mo></math> The time when the kinetic energy and potential energy of the system will become equal, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>T</mi><mi>n</mi></mfrac><mo>.</mo></math> The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mi>E</mi><mo>=</mo><mi>P</mi><mi>E</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>k</mi><mfenced><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>k</mi><msup><mi>x</mi><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mfrac><msup><mi>A</mi><mn>2</mn></msup><mn>2</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>&#177;</mo><mfrac><mi>A</mi><msqrt><mn>2</mn></msqrt></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>A</mi><mi>sin</mi><mi>&#969;</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>A</mi><msqrt><mn>2</mn></msqrt></mfrac><mo>=</mo><mi>A</mi><mi>sin</mi><mi>&#969;</mi><mi>t</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>=</mo><mi>sin</mi><mi>&#969;</mi><mi>t</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mi>t</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>;</mo><mi>t</mi><mo>=</mo><mfrac><mi>T</mi><mn>8</mn></mfrac><mo>.</mo></math> Thus <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q32. JEE Main 2021 (27 Aug Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>Two simple harmonic motion, are represented by the equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>1</mn></msub><mo>=</mo><mn>10</mn><mi>sin</mi><mfenced><mrow><mn>3</mn><mi>&#960;</mi><mi>t</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced><mo>;</mo><mo>&#160;&#160;</mo><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn><mo>(</mo><mi>sin</mi><mn>3</mn><mi>&#960;</mi><mi>t</mi><mo>+</mo><msqrt><mn>3</mn></msqrt><mi>cos</mi><mn>3</mn><mi>&#960;</mi><mi>t</mi><mo>)</mo></math></p><p>Ratio of amplitude of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>1</mn></msub></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><mi>x</mi><mo>:</mo><mn>1</mn></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>1</mn></msub><mo>=</mo><mn>10</mn><mi>sin</mi><mfenced><mrow><mn>3</mn><mi>&#960;</mi><mi>t</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn><mo>[</mo><mi>sin</mi><mn>3</mn><mi>&#960;</mi><mi>t</mi><mo>+</mo><msqrt><mn>3</mn></msqrt><mi>cos</mi><mi>&#960;</mi><mi>t</mi><mo>]</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">y</mi><mn>2</mn></msub><mo>=</mo><mn>10</mn><mi>sin</mi><mfenced><mrow><mn>3</mn><mi>&#960;</mi><mi mathvariant="normal">t</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced><mspace linebreak="newline"/><mo>&#8658;</mo><mfrac><msub><mi mathvariant="normal">A</mi><mn>2</mn></msub><msub><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mn>10</mn><mn>10</mn></mfrac><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q33. JEE Main 2021 (26 Aug Shift 2)

*Type:* `numerical` | *Level:* `1`

Two simple harmonic motions are represented by the equations <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mn>5</mn><mi>sin</mi><mfenced><mrow><mn>2</mn><mi>&#960;</mi><mi>t</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn><msqrt><mn>2</mn></msqrt><mo>(</mo><mi>sin</mi><mn>2</mn><mi>&#960;</mi><mi>t</mi><mo>+</mo><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>t</mi><mo>)</mo><mo>.</mo></math> The amplitude of the second motion is _____ times the amplitude in the first motion.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">A</mi><mn>1</mn></msub><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn><msqrt><mn>2</mn></msqrt><mo>[</mo><mi>sin</mi><mn>2</mn><mi>&#960;</mi><mi>t</mi><mo>+</mo><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>t</mi><mo>]</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">x</mi><mn>2</mn></msub><mo>=</mo><mn>10</mn><mfenced close="]" open="["><mrow><mi>sin</mi><mfenced><mrow><mn>2</mn><mi>&#960;</mi><mi mathvariant="normal">T</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">A</mi><mn>2</mn></msub><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">A</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><msub><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mn>1</mn></msub></math></p>

</details>

---

### Q34. JEE Main 2021 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

A particle executes simple harmonic motion represented by displacement function as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mi>A</mi><mi>sin</mi><mo>(</mo><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi><mo>)</mo></math>. If the position and velocity of the particle at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>cm</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#969;</mi><mo>&#160;</mo><mi>cm</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> respectively, then its amplitude is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><msqrt><mn>2</mn></msqrt><mo>&#160;</mo><mi>cm</mi></math> where the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mi>A</mi><mi>sin</mi><mo>(</mo><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mi>A</mi><mi>&#969;</mi><mi>cos</mi><mo>(</mo><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>=</mo><mi>Asin</mi><mi>&#981;</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#969;</mi><mo>=</mo><mi mathvariant="normal">A</mi><mi>&#969;</mi><mi>cos</mi><mi>&#981;</mi></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#981;</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mn>45</mn><mo>&#176;</mo></math></p><p>Putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi></math> in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>=</mo><mi>A</mi><mfenced open="{" close="}"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q35. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An object of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>kg</mi></math> is executing simple harmonic motion. It amplitude is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math> and time period (T) is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>. What will be the potential energy of the object at an instant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">t</mi><mo>=</mo><mfrac><mi mathvariant="normal">T</mi><mn>4</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> starting from mean position. Assume that the initial phase of the oscillation is zero.

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>62</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>.</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">J</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mo>&#160;</mo><mi mathvariant="normal">J</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>.</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mo>&#160;</mo><mi mathvariant="normal">J</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>62</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">T</mi><mo>=</mo><mn>2</mn><mi>&#960;</mi><msqrt><mfrac><mi mathvariant="normal">m</mi><mi mathvariant="normal">k</mi></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>2</mn><mo>=</mo><mn>2</mn><mi>&#960;</mi><msqrt><mfrac><mrow><mn>0</mn><mo>.</mo><mn>5</mn></mrow><mi mathvariant="normal">k</mi></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">k</mi><mo>=</mo><mn>50</mn><msup><mi>&#960;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8776;</mo><mn>500</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>A</mi><mi>sin</mi><mo>(</mo><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi>cmsin</mi><mfenced><mrow><mfrac><mrow><mi>&#969;</mi><mi mathvariant="normal">T</mi></mrow><mn>4</mn></mfrac><mo>+</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi>cmsin</mi><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>PE</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>kx</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>(</mo><mn>500</mn><mo>)</mo><msup><mfenced><mfrac><mn>5</mn><mn>100</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>6255</mn></math></p>

</details>

---

### Q36. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A particle starts executing simple harmonic motion <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>SHM</mi><mo>)</mo></math> of amplitude <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and total energy <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>.</mo></math> At any instant, its kinetic energy is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>E</mi></mrow><mn>4</mn></mfrac></math>, then its displacement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> is given by:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>a</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mi>a</mi><msqrt><mn>2</mn></msqrt></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mrow><mi>a</mi><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mi>a</mi><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mi>a</mi><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>K</mi><msup><mi>a</mi><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>E</mi></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;</mo><mi>K</mi><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>v</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>K</mi><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;</mo><mi>K</mi><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mfrac><mrow><mn>3</mn><msup><mi>a</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mi>a</mi><mn>2</mn></mfrac></math>

</details>

---

### Q37. JEE Main 2021 (18 Mar Shift 1)

*Type:* `numerical` | *Level:* `1`

A particle performs simple harmonic motion with a period of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> second. The time taken by the particle to cover a displacement equal to half of its amplitude from the mean position is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>&#160;</mo><mi mathvariant="normal">s</mi><mo>.</mo></math> The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> to the nearest integer is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bd7112a6-300d-4f49-b624-06544c4ffb75-image.png" style="width: 337px; height: 112px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mn>2</mn><mn>12</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Correct answer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>.</mo><mn>00</mn></math></p>

</details>

---

### Q38. JEE Main 2021 (17 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A block of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>kg</mi></math> attached to a spring is made to oscillate with an initial amplitude of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#160;</mo><mi>cm</mi></math>. After <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> minutes the amplitude decreases to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi>cm</mi></math>. Determine the value of the damping constant for this motion. (take <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mn>2</mn><mo>=</mo><mn>0</mn><mo>.</mo><mn>693</mn></math> )

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>16</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi>kg</mi><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>3</mn><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup><mo>&#160;</mo><mi>kg</mi><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>16</mn><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup><mo>&#160;</mo><mi>kg</mi><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>.</mo><mn>7</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi>kg</mi><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>16</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi>kg</mi><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<p>The amplitude of damped oscillation with time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> and damping constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msub><mi>A</mi><mn>0</mn></msub><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>b</mi><mi>t</mi><mo>/</mo><mn>2</mn><mi>m</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced><mfrac><msub><mi>A</mi><mn>0</mn></msub><mi>A</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>b</mi><mi>t</mi></mrow><mrow><mn>2</mn><mi>m</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mn>2</mn><mo>=</mo><mfrac><mi>b</mi><mrow><mn>2</mn><mi>m</mi></mrow></mfrac><mo>&#215;</mo><mn>120</mn></math>; here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>min</mi><mo>=</mo><mn>120</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>693</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow><mn>120</mn></mfrac><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mn>1</mn><mo>.</mo><mn>16</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>.</p>

</details>

---

### Q39. JEE Main 2021 (26 Feb Shift 2)

*Type:* `numerical` | *Level:* `1`

A particle executes S.H.M. with amplitude <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and time period <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math>. The displacement of the particle when its speed is half of maximum speed is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mi>x</mi></msqrt><mi>A</mi></mrow><mn>2</mn></mfrac><mo>.</mo></math> The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mi>&#969;</mi><msqrt><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>&#160;&#160;</mo><mo>&#160;</mo><msub><mi>V</mi><mi>max</mi></msub><mo>=</mo><mi>A</mi><mi>&#969;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>A</mi><mi>&#969;</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mi>&#969;</mi><msqrt><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>A</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>3</mn><mo>&#160;</mo><msup><mi>A</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>&#160;</mo><mi>A</mi></math></p>

</details>

---

### Q40. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A particle executes S.H.M., the graph of velocity as a function of displacement is :

**Options:**

- **(A)** a circle
- **(B)** a helix
- **(C)** a parabola
- **(D)** an ellipse

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) an ellipse**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>v</mi><mn>2</mn></msup><mo>=</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mfenced><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>v</mi><mn>2</mn></msup><msup><mi>&#969;</mi><mn>2</mn></msup></mfrac><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>v</mi><mn>2</mn></msup><msup><mfenced><mrow><mi>&#969;</mi><mi>A</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>A</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math></p><p>This is an equation of an ellipse.</p>

</details>

---

### Q41. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mi>A</mi><mi>sin</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><msub><mi>&#981;</mi><mn>0</mn></msub></mrow></mfenced></math> is the time-displacement equation of a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mi>H</mi><mi>M</mi><mo>.</mo></math> At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn></math> the displacement of the particle is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mfrac><mi>A</mi><mn>2</mn></mfrac></math> and it is moving along negative <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-direction. Then the initial phase angle <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#981;</mi><mn>0</mn></msub></math> will be:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/617c9322-761f-4c34-9bfc-220c9f24b9be-image.png" style="width: 179px; height: 177px;" /></p><p>Initial phase <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math>.</p><p>Also it can be seen as below </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1925df26-91e7-45c0-8910-76112f98167d-image.png" style="width: 550px; height: 182px;" /></p><p>The initial phase angle <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#981;</mi><mn>0</mn></msub><mo>=</mo><mi>&#960;</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math></p>

</details>

---

### Q42. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> moves with a uniform speed along the circumference of a circle of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>36</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> and covers <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>&#176;</mo></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>. The perpendicular projection <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> on the diameter <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>N</mi></math> represents the simple harmonic motion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>. The restoration force per unit mass when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> touches <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> will be :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/afb054e4-9d68-429e-96e6-bd5245736318-image.png" style="width: 200px; height: 148px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>49</mn><mo>&#160;</mo><mi mathvariant="normal">N</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>.</mo><mn>87</mn><mo>&#160;</mo><mi mathvariant="normal">N</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>&#160;</mo><mi mathvariant="normal">N</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">N</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>.</mo><mn>87</mn><mo>&#160;</mo><mi mathvariant="normal">N</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/afb054e4-9d68-429e-96e6-bd5245736318-image.png" style="width: 200px; height: 148px;" /></p><p>The point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> covers <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>&#176;</mo></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>.
Then, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>&#160;</mo><mi>rad</mi><mo>&#10230;</mo><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>.
Or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>rad</mi><mo>&#10230;</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>1</mn></mrow><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mstyle></mfrac><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>
Or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">&#960;</mi><mo>&#160;</mo><mi>in</mi><mo>&#8594;</mo><mo>&#160;</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#215;</mo><mn>6</mn></mrow><mi mathvariant="normal">&#960;</mi></mfrac><mo>&#215;</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi></math>
Thus, time taken is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">T</mi><mo>=</mo><mn>1</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi>sec</mi><mo>.</mo></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mi>T</mi></mfrac></math>
Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mrow><mn>1</mn><mo>.</mo><mn>2</mn></mrow></mfrac></math>
Restoration force <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">F</mi><mo>)</mo><mo>=</mo><msup><mi>m&#969;</mi><mn>2</mn></msup><mi mathvariant="normal">A</mi><mo>.</mo></math></p><p>Then Restoration force per unit mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mi mathvariant="normal">F</mi><mi mathvariant="normal">m</mi></mfrac></mfenced><mo>=</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mi mathvariant="normal">F</mi><mi mathvariant="normal">m</mi></mfrac></mfenced><mo>=</mo><msup><mfenced><mfrac><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow><mrow><mn>1</mn><mo>.</mo><mn>2</mn></mrow></mfrac></mfenced><mn>2</mn></msup><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8773;</mo><mn>9</mn><mo>.</mo><mn>87</mn><mo>&#160;</mo><mi mathvariant="normal">N</mi></math></p>

</details>

---

### Q43. JEE Main 2021 (24 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

When a particle executes SHM, the nature of graphical representation of velocity as a function of displacement is:

**Options:**

- **(A)** straight line
- **(B)** elliptical
- **(C)** circular
- **(D)** parabolic

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) elliptical**

**Detailed Solution:**

<p>For a particle executing SHM,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>A</mi><mi>sin</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mi>&#969;</mi><mi>A</mi><mi>cos</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mi>v</mi><mn>2</mn></msup><mrow><msup><mi>&#969;</mi><mn>2</mn></msup><msup><mi>A</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mo>&#160;</mo><msup><mi>A</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>1</mn><mo>&#8658;</mo></math> equation of ellipse between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></p>

</details>

---

### Q44. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A damped harmonic oscillator has a frequency of <math><mn>5</mn></math> oscillations per second. The amplitude drops to half its value for every 10 oscillations. The time it will take to drop to <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1000</mn></mrow></mfrac></math> of the original amplitude is close to:

**Options:**

- **(A)** <math><mn>50</mn><mi> </mi><mi mathvariant="normal">s</mi></math>
- **(B)** <math><mn>100</mn><mi> </mi><mi mathvariant="normal">s</mi></math>
- **(C)** <math><mn>20</mn><mi> </mi><mi mathvariant="normal">s</mi></math>
- **(D)** <math><mn>10</mn><mi> </mi><mi mathvariant="normal">s</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>20</mn><mi> </mi><mi mathvariant="normal">s</mi></math>**

**Detailed Solution:**

<math><mi>f</mi><mo>=</mo><mn>5</mn></math>  
So, <math><mi>T</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>  
Time taken for amplitude to drop to half: <math><mn>10</mn><mi>T</mi><mo>=</mo><mfrac><mrow><mn>10</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>=</mo><mn>2</mn></math> s 
Now, 
<math><mfrac><mrow><msub><mrow><mi>A</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>1000</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><msub><mrow><mi>A</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msup><mrow><mo>(</mo><mn>2</mn><mo>)</mo></mrow><mrow><mfrac><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></mrow></mfrac></math>  
<math><msup><mrow><mo>(</mo><mn>2</mn><mo>)</mo></mrow><mrow><mfrac><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup><mo>=</mo><mn>1000</mn></math>  
<math><mfenced separators="|"><mrow><mfrac><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mn>2</mn><mo>=</mo><mn>3</mn></math>  
<math><mi>t</mi><mo>=</mo><mfrac><mrow><mn>6</mn></mrow><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mn>2</mn></mrow></mfrac><mo>≈</mo><mn>20</mn><mtext> </mtext><mi mathvariant="normal">s</mi></math>

</details>

---

### Q45. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

An oscillator of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is at rest in its equilibrium position in a potential, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>k</mi><msup><mfenced separators="|"><mrow><mi>x</mi><mi>&#160;</mi><mo>&#8211;</mo><mi>X</mi></mrow></mfenced><mn>2</mn></msup></math> . A particle of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> comes from the right with speed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi></math> and collides completely inelastic with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and sticks to it. This process repeats every time the oscillator crosses its equilibrium position. The amplitude of oscillations after <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math> collisions is: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>M</mi><mo>=</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi>u</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>k</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math>

**Options:**

- **(A)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>3</mn><mi> </mi></msqrt></mrow></mfrac></math>
- **(C)** <math><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></msqrt></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>3</mn><mi> </mi></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p>In the first collision <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext mathvariant="italic">mu</mtext></math> momentum will be imparted to the system. In the second collision when the momentum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>M</mi><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi>m</mi><mo>)</mo></math> is in the opposite direction mu momentum of the particle will make its momentum zero. On <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>13</mn><mi>th</mi></msup></math> collision, 

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4cc99717-6608-41a7-84c2-471712b4182d-image.png" style="width: 229px; height: 117px;" />
Applying momentum conservation
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mi>u</mi><mo>=</mo><mo>(</mo><mi>M</mi><mo>+</mo><mn>13</mn><mi>m</mi><mo>)</mo><mi>v</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>v</mi><mo>=</mo><mfrac><mrow><mi>m</mi><mi>u</mi></mrow><mrow><mi>M</mi><mo>+</mo><mn>13</mn><mi>m</mi></mrow></mfrac><mo>=</mo><mfrac><mi>u</mi><mn>15</mn></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>M</mi><mo>=</mo><mn>2</mn><mi>m</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>v</mi><mo>=</mo><mi>&#160;</mi><mi>&#969;</mi><mi>A</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>u</mi><mn>15</mn></mfrac><mo>=</mo><mi mathvariant="normal">&#160;</mi><msqrt><mfrac><mi>K</mi><mrow><mi>M</mi><mo>+</mo><mn>13</mn><mi>m</mi></mrow></mfrac></msqrt><mo>&#215;</mo><mi>A</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><mn>15</mn></mfrac><msqrt><mfrac><mn>75</mn><mn>1</mn></mfrac></msqrt><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p>

</details>

---

### Q46. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `3`

Two simple harmonic motions, as shown, are at right angles. They are combined to form Lissajous figures.
$x(t)=A \sin (a t+\delta)$
$y(t)=B \sin (b t)$
Identify the correct match below

**Options:**

- **(A)** Parameters: $\mathrm{A}=\mathrm{B}, \mathrm{a}=2 \mathrm{~b} ; \delta=\frac{\pi}{2}$; Curve: Circle
- **(B)** Parameters: $\mathrm{A}=\mathrm{B}, \mathrm{a}=\mathrm{b} ; \delta=\frac{\pi}{2} ;$ Curve: Line
- **(C)** Parameters: $\mathrm{A} \neq \mathrm{B}, \mathrm{a}=\mathrm{b} ; \delta=\frac{\pi}{2} ;$ Curve: Ellipse
- **(D)** Parameters: $\mathrm{A} \neq \mathrm{B}, \mathrm{a}=\mathrm{b} ; \delta=0$; Curve: Parabola

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Parameters: $\mathrm{A} \neq \mathrm{B}, \mathrm{a}=\mathrm{b} ; \delta=\frac{\pi}{2} ;$ Curve: Ellipse**

**Detailed Solution:**

From the two mutually perpendicular S.H.M.'s, the general equation of Lissajous figure,
$$
\frac{x^2}{A^2}+\frac{y^2}{B^2}-\frac{2 x y}{A B} \cos \delta=\sin ^2 \delta
$$

$$
\begin{aligned}
&x=A \sin (a t+\delta) \\
&y=B \sin (b t+r)
\end{aligned}
$$
Clearly $A \neq B$ hence ellipse.

</details>

---

### Q47. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The ratio of maximum acceleration to maximum velocity in a simple harmonic motion is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mi>&#160;</mi><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>.</mo></math> At, <math><mi>t</mi><mo>=</mo><mn>0</mn></math> the displacement is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>.</mo></math> What is the maximum acceleration? The initial phase is <math><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math> .

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>750</mn><msqrt><mn>2</mn></msqrt><mi>&#160;</mi><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>750</mn><mi>&#160;</mi><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn><msqrt><mn>2</mn></msqrt><mi>&#160;</mi><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn><msqrt><mn>2</mn></msqrt><mi>&#160;</mi><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

<p>In a simple harmonic motion,</p><p>Maximum acceleration, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow></msub><mo>=</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mi>A</mi></math>

Maximum velocity, <math><msub><mrow><mi>v</mi></mrow><mrow><mi>max</mi></mrow></msub><mo>=</mo><mi>A</mi><mi>&#969;</mi></math>. 

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>f</mi><mi>max</mi></msub><msub><mi>v</mi><mi>max</mi></msub></mfrac><mo>=</mo><mfrac><mrow><msup><mi>&#969;</mi><mn>2</mn></msup><mi>A</mi></mrow><mrow><mi>A</mi><mi>&#969;</mi></mrow></mfrac><mo>=</mo><mi>&#969;</mi></math>

<math><mi>&#969;</mi><mo>=</mo><mn>10</mn></math>

Displacement in SHM is <math><mi>x</mi><mo>=</mo><mi>A</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mi>&#969;t</mi><mo>+</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>

At <math><mi>t</mi><mo>=</mo><mn>0</mn></math>

<math><mn>5</mn><mo>=</mo><mi>A</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>

<math><mi>A</mi><mo>=</mo><mn>5</mn><msqrt><mn>2</mn></msqrt></math>. 

Max acceleration = <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#969;</mi><mn>2</mn></msup><mi>A</mi></math>

<math><mo>=</mo><mn>100</mn><mo>&#215;</mo><mn>5</mn><msqrt><mn>2</mn></msqrt></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>500</mn><msqrt><mn>2&#160;</mn></msqrt><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math> </p>

</details>

---

### Q48. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Two particles are performing simple harmonic motion in a straight line about the same equilibrium point. The amplitude and time period for both particles are same and equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math>, respectively. At time <math><mi mathvariant="normal">t</mi><mo>=</mo><mn>0</mn></math> one particle has displacement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> while the other one has displacement <math><mo>-</mo><mfrac><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math> and they are moving towards each other. If they cross each other at time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>5</mn><mi mathvariant="normal">T</mi></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>6</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>6</mn></mrow></mfrac></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/633e0c9b-94ac-48f9-8260-4500bfb8ee85-image.png" style="width: 188px; height: 181px;" />

Angle covered to meet <math><mo>=</mo><msup><mrow><mn>60</mn></mrow><mrow><mi mathvariant="normal">o</mi></mrow></msup><mo>=</mo><mfrac><mrow><mi mathvariant="normal">&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mi mathvariant="normal">r</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">d</mi></math>

Therefore, <math> <mrow> <mi>t</mi><mo>=</mo><mfrac> <mi>&#952;</mi> <mi>&#969;</mi> </mfrac> <mo>=</mo><mfrac> <mi>&#960;</mi> <mn>3</mn> </mfrac> <mo>&#215;</mo><mfrac> <mi>T</mi> <mrow> <mn>2</mn><mi>&#960;</mi></mrow> </mfrac> <mo>=</mo><mfrac> <mi>T</mi> <mn>6</mn> </mfrac> </mrow> </math>

</details>

---

### Q49. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `2`

A particle performs simple harmonic motion with amplitude A. Its speed is tripled at the instant that it is at a distance <math><mfrac><mrow><mn>2</mn><mi mathvariant="normal">A</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math> from equilibrium position. The new amplitude of the motion is:

**Options:**

- **(A)** <math><mi mathvariant="normal">A</mi><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math><mfrac><mrow><mn>7</mn><mi mathvariant="normal">A</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>3</mn></mrow></mfrac><msqrt><mn>41</mn></msqrt></math>
- **(D)** <math><mn>3</mn><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>7</mn><mi mathvariant="normal">A</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

For Original SHM,

using        <math><mi mathvariant="normal">v</mi><mo>=</mo><mi mathvariant="normal">&#969;</mi><msqrt><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mi mathvariant="normal">&#160;</mi></math> 

                <math><mi mathvariant="normal">v</mi><mo>=</mo><mi mathvariant="normal">&#969;</mi><msqrt><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>4</mn><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac></msqrt></math>

                <math><mo>=</mo><mfrac><mrow><mi mathvariant="normal">&#969;</mi><msqrt><mn>5</mn></msqrt><mi mathvariant="normal">A</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>

New SHM will be,

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>v =&#160;</mi><mi mathvariant="normal">&#969;</mi><msqrt><msubsup><mi mathvariant="normal">A</mi><mi mathvariant="normal">N</mi><mn>2</mn></msubsup><mo>-</mo><msubsup><mi mathvariant="normal">X</mi><mi>N</mi><mn>2</mn></msubsup></msqrt></math> 

<math><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#969;</mi><msqrt><mn>5</mn></msqrt><mi mathvariant="normal">A</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mi mathvariant="normal">&#969;</mi><msqrt><msubsup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mn>2</mn></mrow></msubsup><mo>-</mo><mfrac><mrow><mn>4</mn><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac></msqrt></math>

<math><mn>5</mn><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msubsup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mn>2</mn></mrow></msubsup><mo>-</mo><mfrac><mrow><mn>4</mn><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac></math>

<math><msubsup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mfrac><mrow><mn>49</mn><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac></math>

<math><msub><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mi mathvariant="normal">N</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>7</mn><mi mathvariant="normal">A</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>

</details>

---

### Q50. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

A simple harmonic oscillator of angular frequency <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> is acted upon by an external force <math><mi>F</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi><mi>&#160;</mi><mi>N</mi><mo>.&#160;</mo></mrow></mrow></math>If the oscillator is at rest in its equilibrium position at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> its position at later times is proportional to:

**Options:**

- **(A)** <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>t</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>t</mi></mrow></mrow></mrow></mrow></math>
- **(B)** <math><mi>c</mi><mi>o</mi><mi>s</mi><mi>t</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>t</mi></mrow></mrow></math>
- **(C)** <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>t</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>t</mi></mrow></mrow></mrow></mrow></math>
- **(D)** <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>t</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>t</mi></mrow></mrow></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>t</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>t</mi></mrow></mrow></mrow></mrow></math>**

**Detailed Solution:**

It is given that oscillator at rest at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn></math> i.e. at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mn>0</mn></math>. So, in option, we can check by putting <math><mi>v</mi><mo>=</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math>.

(1) <math><mi>I</mi><mi>f</mi><mi>&#160;</mi><mi>x</mi><mo>&#8733;</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>t</mi></mrow></mrow></mrow></mrow></math>

<math><mo>&#10233;</mo><mi>v</mi><mo>&#8733;</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#215;</mo><mn>2</mn><mi>&#160;</mi><mo>(</mo><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>t</mi></mrow></mrow><mo>)</mo></mrow></mrow></math>

<math><mo>&#10233;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>a</mi><mi>t</mi><mi>&#160;</mi><mi>t</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>v</mi><mo>&#8733;</mo><mn>1</mn><mo>-</mo><mn>0</mn><mo>&#8800;</mo><mn>0</mn></math>

(2) <math><mi>I</mi><mi>f</mi><mi>&#160;</mi><mi>x</mi><mi>&#160;</mi><mo>&#8733;</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi></mrow></mrow></mrow></mrow></math>

<math><mo>&#10233;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>v</mi><mo>&#8733;</mo><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi></mrow></mrow></mrow></mrow></math>

<math><mo>&#10233;</mo><mi>a</mi><mi>t</mi><mi>&#160;</mi><mi>t</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>v</mi><mo>&#8733;</mo><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#8800;</mo><mn>0</mn></math>

(3) <math><mi>I</mi><mi>f</mi><mi>&#160;</mi><mi>x</mi><mo>&#8733;</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>&#160;</mi><mi>s</mi><mi>i</mi><mi>n</mi><mi>&#160;</mi><mn>2</mn><mi>t</mi></mrow></mrow></math>

<math><mi>t</mi><mi>h</mi><mi>e</mi><mi>n</mi><mi>&#160;</mi><mi>&#965;</mi><mo>&#8733;</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#215;</mo><mn>2</mn><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>t</mi></mrow></mrow></mrow></mrow></math>

<math><mo>&#10233;</mo><mi>a</mi><mi>t</mi><mi>&#160;</mi><mi>t</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>v</mi><mo>&#8733;</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>

(4) <math><mi>I</mi><mi>f</mi><mi>&#160;</mi><mi>x</mi><mo>&#8733;</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>t</mi></mrow></mrow></mrow></mrow></math>

<math><mo>&#10233;</mo><mi>v</mi><mo>&#8733;</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#215;</mo><mn>2</mn><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>t</mi></mrow></mrow></mrow></mrow></math>

<math><mo>&#10233;</mo><mi>a</mi><mi>t</mi><mi>&#160;</mi><mi>t</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>v</mi><mo>&#8733;</mo><mn>1</mn><mo>+</mo><mn>1</mn></math>

<math><mo>&#10233;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>v</mi><mo>&#8733;</mo><mn>2</mn><mo>&#8800;</mo><mn>0</mn></math>

<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>i</mi><mi>n</mi><mi>&#160;</mi><mi>o</mi><mi>p</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced><mi>&#160;</mi><mi>&#160;</mi><mi>v</mi><mo>=</mo><mn>0</mn><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>a</mi><mi>t</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>t</mi><mo>=</mo><mn>0</mn></math>

</details>

---

### Q51. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

<math><mi>x</mi><mi>&#160;</mi><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><mi>y</mi></math> displacements of a particle are given as <math><mi>x</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced><mo>=</mo><mi>a</mi><mrow><mrow><mi mathvariant="normal">&#160;sin&#160;</mi></mrow><mo>&#8289;</mo><mrow><mi>&#969;</mi><mi>t</mi><mi>&#160;</mi><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><mi>y</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced><mo>=</mo><mi>a</mi><mrow><mrow><mi mathvariant="normal">&#160;sin&#160;</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>&#969;</mi><mi>t</mi><mo>.</mo></mrow></mrow></mrow></mrow></math> Its trajectory will look like:

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/21b66e55-5186-417b-9613-518d5b4b7d97-image.png" style="width: 180px; height: 181px;" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/15da6808-9b0d-4c2c-9f91-98dc8a77ff25-image.png" style="width: 180px; height: 176px;" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/15acf882-f871-4cd9-94a0-215083bb3567-image.png" style="width: 180px; height: 188px;" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ba085bc6-1f8a-47b2-829e-efb56998db87-image.png" style="width: 180px; height: 180px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/15acf882-f871-4cd9-94a0-215083bb3567-image.png" style="width: 180px; height: 188px;" />**

**Detailed Solution:**

<math><mo>&#8757;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>=</mo><mi>A</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#969;</mi><mi>t</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>s</mi><mi>i</mi><mi>n</mi><mi>&#160;</mi><mi>&#969;</mi><mi>t</mi><mo>=</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mi>A</mi></mrow></mfrac></mrow></mrow></math>

Also, <math><mi>c</mi><mi>o</mi><mi>s</mi><mi>&#160;</mi><mi>&#969;</mi><mi>t</mi><mo>=</mo><mi>&#160;</mi><msqrt><mn>1</mn><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>&#969;</mi><mi>t</mi></mrow></mrow></msqrt><mo>=</mo><mi>&#160;</mi><msqrt><mn>1</mn><mo>-</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></msqrt><mi>&#160;</mi></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#160;</mi></mrow></mrow><mi>&#969;</mi><mi>t</mi><mo>=</mo><mi>&#160;</mi><mfrac><mrow><msqrt><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow><mrow><mi>A</mi></mrow></mfrac></math>

As, <math><mi>y</mi><mo>=</mo><mn>2</mn><mi>A</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#969;</mi><mi>t</mi><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#969;</mi><mi>t</mi></mrow></mrow></mrow></mrow></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>y</mi><mo>=</mo><mn>2</mn><mi>&#160;</mi><mi>A</mi><mfrac><mrow><mi>x</mi></mrow><mrow><mi>A</mi></mrow></mfrac><mi>&#160;</mi><mfrac><mrow><msqrt><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow><mrow><mi>A</mi></mrow></mfrac></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>y</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>A</mi></mrow></mfrac><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mi>&#160;</mi><msqrt><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mi>&#160;</mi></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>y</mi><mo>=</mo><mn>0</mn><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>a</mi><mi>t</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>=</mo><mn>0</mn><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>=</mo><mi>&#160;</mi><mo>&#177;</mo><mi>&#160;</mi><mi>A</mi></math>

Which is possible only in option (C)

</details>

---

### Q52. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A body is in simple harmonic motion with time period  <math> <mrow> <mi>T</mi><mo>=</mo><mn>0.5</mn><mtext>&#8201;</mtext><mtext>s</mtext></mrow> </math> and amplitude <math> <mrow> <mi>A</mi><mo>=</mo><mn>1</mn><mtext>&#8201;</mtext><mtext>cm</mtext></mrow> </math>. Find the average velocity in the interval in which it moves from equilibrium position to half of its amplitude.

**Options:**

- **(A)** <math> <mrow> <mn>16</mn><mtext> </mtext><mtext>cm/s</mtext></mrow> </math>
- **(B)** <math> <mrow>  <mn>6</mn><mtext>&#x2009;</mtext><mtext>cm/s</mtext></mrow></math>
- **(C)** <math> <mrow>  <mn>4</mn><mtext>&#x2009;</mtext><mtext>cm/s</mtext></mrow></math>
- **(D)** <math> <mrow> <mn>12</mn><mtext> </mtext><mtext>cm/s</mtext></mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math> <mrow> <mn>12</mn><mtext> </mtext><mtext>cm/s</mtext></mrow> </math>**

**Detailed Solution:**

<math><mo>&#8756;</mo><mi>x</mi><mo>=</mo><mi>A</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#969;</mi><mi>t</mi></mrow></mrow></math>

<math><mfrac><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mi>A</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#969;</mi><mi>t</mi></mrow></mrow></math>

<math><mi>&#969;</mi><mi>t</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>6</mn></mrow></mfrac></math>

<math><mi>t</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>6</mn><mi>&#969;</mi></mrow></mfrac></math>

<math><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>6</mn><mo>&#215;</mo><mn>2&#960;</mn></mrow></mfrac></math>

<math><mi>t</mi><mo>=</mo><mfrac><mrow><mi>T</mi></mrow><mrow><mn>12</mn></mrow></mfrac></math>

<math><mo>&#8756;</mo><mi>T</mi><mi>i</mi><mi>m</mi><mi>e</mi><mi>&#160;</mi><mi>t</mi><mi>a</mi><mi>k</mi><mi>e</mi><mi>n</mi><mi>&#160;</mi><mi>t</mi><mi>o</mi><mi>&#160;</mi><mi>r</mi><mi>e</mi><mi>a</mi><mi>c</mi><mi>h</mi><mi>&#160;</mi><mi>f</mi><mi>r</mi><mi>o</mi><mi>m</mi><mi>&#160;</mi><mi>x</mi><mo>=</mo><mn>0</mn><mi>&#160;</mi><mi>t</mi><mi>o</mi><mi>&#160;</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mi>&#160;</mi><mi>i</mi><mi>s</mi><mfrac><mrow><mi>T</mi></mrow><mrow><mn>12</mn></mrow></mfrac></math>

<math><mo>&#8756;</mo><mi>A</mi><mi>v</mi><mi>e</mi><mi>r</mi><mi>a</mi><mi>g</mi><mi>e</mi><mi>&#160;</mi><mi>v</mi><mi>e</mi><mi>l</mi><mi>o</mi><mi>c</mi><mi>i</mi><mi>t</mi><mi>y</mi><mo>=</mo><mfrac><mrow><mi>D</mi><mi>i</mi><mi>s</mi><mi>p</mi><mi>l</mi><mi>a</mi><mi>c</mi><mi>e</mi><mi>m</mi><mi>e</mi><mi>n</mi><mi>t</mi></mrow><mrow><mi>T</mi><mi>i</mi><mi>m</mi><mi>e</mi></mrow></mfrac></math>

<math><mo>=</mo><mfrac><mrow><mi>A</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi>T</mi><mo>/</mo><mn>12</mn></mrow></mfrac></math>

<math><mo>=</mo><mfrac><mrow><mi>A</mi></mrow><mrow><mi>T</mi></mrow></mfrac><mo>&#215;</mo><mn>6</mn></math>

<math><mo>=</mo><mfrac><mrow><mn>6</mn><mo>&#215;</mo><mn>1</mn></mrow><mrow><mn>0.5</mn><mi>&#160;</mi></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>12</mn><mo>&#160;</mo><mi>c</mi><mi>m</mi><mo>/</mo><mi>s</mi></math>

</details>

---

### Q53. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following expressions corresponds to simple harmonic motion along a straight line, where $\mathrm{x}$ is the displacement and $\mathrm{a}, \mathrm{b}, \mathrm{c}$ are positive constants?

**Options:**

- **(A)** $a+b x-c x^2$
- **(B)** $\mathrm{bx}^2$
- **(C)** $a-b x+c x^2$
- **(D)** $-b x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-b x$**

**Detailed Solution:**

In linear S.H.M., the restoring force acting on particle should always be proportional to the displacement of the particle and directed towards the equilibrium position. i.e., $\mathrm{F} \propto \mathrm{x}$
or $\mathrm{F}=-\mathrm{bx}$ where $\mathrm{b}$ is a positive constant.

</details>

---

### Q54. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A particle which is simultaneously subjected to two perpendicular simple harmonic motions represented by;  <math><mi>x</mi><mo>=</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#969;</mi><mi>t</mi></mrow></mrow></math>   and <math><mi>y</mi><mo>=</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msub><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>&#969;</mi><mi>t</mi></mrow></mrow></math> traces a curve given by :

**Options:**

- **(A)** <u><strong><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EM0025939.jpg" style="width: 200px; height: 168px;" /></strong></u>
- **(B)** <img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/223_form_1396898648078_14_e_10605_02.jpg" style="width: 200px; height: 172px;" />
- **(C)** <img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/223_form_1396898648078_14_e_10605_04.jpg" style="width: 200px; height: 175px;" />
- **(D)** <img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EM0025939_.jpg" style="width: 200px; height: 176px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EM0025939_.jpg" style="width: 200px; height: 176px;" />**

**Detailed Solution:**

<math><mi>x</mi><mo>=</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>ω</mi><mi>t</mi></mrow></mrow></math></br></br><math><mi>y</mi><mo>=</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msub><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mn>2</mn><mi>ω</mi><mi>t</mi></mrow></mfenced></mrow></mrow></math></br></br><math><mo>=</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced open="{" close="}" separators="|"><mrow><mn>2</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>ω</mi><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mrow></mrow></mfenced></math></br></br><math><mo>=</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced open="{" close="}" separators="|"><mrow><mn>2</mn><mi> </mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></br></br><math><mo>∴</mo><mfrac><mrow><mi>y</mi></mrow><mrow><msub><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msubsup><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac><mo>-</mo><mn>1</mn></math></br></br><math><mo>∴</mo><msubsup><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mi>y</mi><mo>=</mo><mn>2</mn><msub><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msub><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msubsup><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><msub><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msub></math></br></br>which is a parabola symmetrical about y-axis opening in upward direction

</details>

---

### Q55. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `3`

A particle moves with simple harmonic motion in a straight line. In first <math> <mrow> <mi>&#964;</mi> <mo>s</mo> </mrow> </math>, after starting from rest it travels a distance a, and in next <math> <mrow> <mi>&#964;</mi> <mo>s</mo> </mrow> </math> it travels 2a, in same direction, then :

**Options:**

- **(A)** Amplitude of motion is 3a
- **(B)** Time period of oscillations is <math> <mrow> <mn>8</mn> <mi>&tau;</mi> </mrow> </math>
- **(C)** Amplitude of motion is 4a
- **(D)** Time period of oscillations is <math> <mrow> <mn>6</mn> <mi>&tau;</mi> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Time period of oscillations is <math> <mrow> <mn>6</mn> <mi>&tau;</mi> </mrow> </math>**

**Detailed Solution:**

<math> <mrow> <mtext>x</mtext> <mo>=</mo> <mo>-</mo> <mo>A cos</mo> <mi>&#969;</mi> <mtext>t</mtext> </mrow> </math>

<math> <mrow> <mo>-</mo> <mtext>A</mtext> <mo>+</mo> <mtext>a</mtext> <mo>=</mo> <mo>-</mo> <mtext>A cos</mtext> <mi>&#969;</mi> <mi>&#964;</mi> </mrow> </math>               ...(i)

<math> <mrow> <mo>-</mo> <mtext>A</mtext> <mo>+</mo> <mn>3</mn> <mtext>a</mtext> <mo>=</mo> <mo>-</mo> <mtext>A cos</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mi>&#969;</mi> <mn>2</mn> <mi>&#964;</mi> </mrow> </mfenced> </mrow> </math>         ...(ii)

<math> <mrow> <mo>&#8756;&#160;&#160;&#160;</mo> <mo>-</mo> <mn>1</mn> <mo>+</mo> <mfrac> <mrow> <mtext>a</mtext> </mrow> <mrow> <mtext>A</mtext> </mrow> </mfrac> <mo>=</mo> <mo>-</mo> <mtext>cos</mtext> <mi>&#969;</mi> <mi>&#964;</mi> </mrow> </math>             ...(iii)

and <math> <mrow> <mo>-</mo> <mn>1</mn> <mo>+</mo> <mfrac> <mrow> <mn>3</mn> <mtext>a</mtext> </mrow> <mrow> <mtext>A</mtext> </mrow> </mfrac> <mo>=</mo> <mo>-</mo> <mtext>cos</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mn>2</mn> <mi>&#969;</mi> <mi>&#964;</mi> </mrow> </mfenced> </mrow> </math>          ...(iv)

Adding (iii) and (iv)

<math> <mrow> <mn>2</mn> <mo>=</mo> <mn>3</mn> <mo>&#160;cos</mo> <mfenced close=")" open="(" separators=","> <mrow> <mi>&#969;</mi> <mi>&#964;</mi> </mrow> </mfenced> <mo>-</mo> <mn>2</mn> <msup> <mtext>&#160;cos</mtext> <mn>2</mn> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mi>&#969;</mi> <mi>&#964;</mi> </mrow> </mfenced> <mo>+</mo> <mn>1</mn> </mrow> </math>

<math> <mrow> <mo>&#8756;&#160;&#160;&#160;</mo> <mn>2</mn> <msup> <mtext>&#160;cos</mtext> <mn>2</mn> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mi>&#969;</mi> <mi>&#964;</mi> </mrow> </mfenced> <mo>-</mo> <mn>3</mn> <mtext>&#160;cos</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mi>&#969;</mi> <mi>&#964;</mi> </mrow> </mfenced> <mo>+</mo> <mn>1</mn> <mo>=</mo> <mn>0</mn> </mrow> </math>

<math> <mrow> <mo>&#8756;&#160;&#160;&#160;</mo> <mtext>cos</mtext> <mi>&#969;</mi> <mi>&#964;</mi> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>

<math> <mrow> <mo>&#8756;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</mo> <mi>&#969;</mi> <mi>&#964;</mi> <mo>=</mo> <mfrac> <mrow> <mi>&#960;</mi> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </math>

<math> <mrow> <mo>&#8756;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</mo> <mtext>T</mtext> <mo>=</mo> <mn>6</mn> <mi>&#964;</mi> </mrow> </math>

</details>

---

### Q56. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A mass $m=1.0 \mathrm{~kg}$ is put on a flat pan attached to a vertical spring fixed on the ground. The mass of the spring and the pan is negligible. When pressed slightly and released, the mass executes simple harmonic motion. The spring constant is $500 \mathrm{~N} / \mathrm{m}$. What is the amplitude A of the motion, so that the mass $m$ tends to get detached from the pan ? (Take $g=10 \mathrm{~m} / \mathrm{s}^2$ ).
The spring is stiff enough so that it does not get distorted during the motion.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bj9m0IT5obyULwuC3ADS56QnN5XNoZmDV6rCT8IYxrs.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{A}>2.0 \mathrm{~cm}$
- **(B)** $\mathrm{A}=2.0 \mathrm{~cm}$
- **(C)** $\mathrm{A} < 2.0 \mathrm{~cm}$
- **(D)** $\mathrm{A}=1.5 \mathrm{~cm}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{A} < 2.0 \mathrm{~cm}$**

**Detailed Solution:**

As $\mathrm{F}=-\mathrm{kx}$

</details>

---

### Q57. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Two simple pendulums of length $1 \mathrm{~m}$ and $4 \mathrm{~m}$ respectively are both given small displacement in the same direction at the same instant. They will be again in phase after the shorter pendulum has completed number of oscillations equal to:

**Options:**

- **(A)** 2
- **(B)** 7
- **(C)** 5
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

Let $T_1$ and $T_2$ be the time period of the two pendulums $\mathrm{T}_1=2 \pi \sqrt{\frac{1}{\mathrm{~g}}}$ and $\mathrm{T}_2=2 \pi \sqrt{\frac{4}{\mathrm{~g}}}$ As $\ell_1 < \ell_2$ therefore $\mathrm{T}_1 < \mathrm{T}_2$ Let at $\mathrm{t}=0$ they start swinging together. Since their time periods are different, the swinging will not be in unison always. Only when number of completed oscillations
differ by an integer, the two pendulums will again begin to swing together Let longer length pendulum complete $\mathrm{n}$ oscillation and shorter length pendulum complete $(n+1)$ oscillation. For unison swinging
$$
\begin{aligned}
& (n+1) T_1=n_2 \\
& (n+1) \times 2 \pi \sqrt{\frac{1}{g}}=(n) \times 2 \pi \sqrt{\frac{4}{g}} \\
& \Rightarrow n=1 \\
& \therefore n+1=1+1=2
\end{aligned}
$$

</details>

---

### Q58. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `2`

The displacement $y(t)=A \sin (\omega t+\phi)$ of a pendulum for $\phi=\frac{2 \pi}{3}$ is correctly represented by

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cNCG8QEtftl450puhVNEe-8KOR8wNc0Gtvt50hQ7XCI.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ymZ24fJjM3-djnjRFGnxljXA0dAO4BAddDrSwC8AuEk.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/31Y86z8yvD9mKsbgSFvjo9EnGxQRjve9fvgQy2wNJqc.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/QFHwrQ1KK-fM7FoOXwzsz9ldbfiUe03DnLChTg4Ojh8.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cNCG8QEtftl450puhVNEe-8KOR8wNc0Gtvt50hQ7XCI.original.fullsize.png">**

**Detailed Solution:**

Displacement $y(t)=A \sin (\mathrm{w} t+\phi)$ [Given]
For $\phi=\frac{2 \pi}{3}$
at $t=0 ; y=A \sin \phi=A \sin \frac{2 \pi}{3}$
$$
=A \sin 120^{\circ}=0.87 \mathrm{~A}\left[\because \sin 120^{\circ} \simeq 0.866\right]
$$
Graph (a) depicts $y=0.87 A$ at $t=0$

</details>

---

### Q59. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `2`

A mass $M$, attached to a horizontal spring, executes S.H.M. with amplitude $A_1$. When the mass $M$ passes through its mean position then a smaller mass $\mathrm{m}$ is placed over it and both of them move together with amplitude $A_2$. The ratio of $\left(\frac{A_1}{A_2}\right)$ is :

**Options:**

- **(A)** $\frac{M+m}{M}$
- **(B)** $\left(\frac{M}{M+m}\right)^{1 / 2}$
- **(C)** $\left(\frac{\mathrm{M}+\mathrm{m}}{\mathrm{M}}\right)^{1 / 2}$
- **(D)** $\frac{M}{M+m}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(\frac{\mathrm{M}+\mathrm{m}}{\mathrm{M}}\right)^{1 / 2}$**

**Detailed Solution:**

Energy of simple harmonic oscillator is constant.
$$
\begin{aligned}
& \Rightarrow \frac{1}{2} M \omega^2 A_1^2=\frac{1}{2}(m+M) \omega^2 A_2^2 \\
& \frac{A_1^2}{A_2^2}=\frac{M+m}{M} \\
& \therefore \frac{A_1}{A_2}=\sqrt{\frac{M+m}{M}}
\end{aligned}
$$

</details>

---

### Q60. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `2`

Two particles are executing simple harmonic motion of the same amplitude $\mathrm{A}$ and frequency $\omega$ along the $x$-axis. Their mean position is separated by distance $X_0\left(X_0>A\right)$. If the maximum separation between them is $\left(X_0+A\right)$, the phase difference between their motion is :

**Options:**

- **(A)** $\frac{\pi}{3}$
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{6}$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{2}$**

**Detailed Solution:**

$\phi_1=0$
$\phi_2=\frac{\pi}{2}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/PzldBGdqHewVP25tXgzdEF4qL4lhjY-uz7LZtuIZlXY.original.fullsize.png">

</details>

---

### Q61. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `2`

If $x, v$ and a denote the displacement, the velocity and the acceleration of a particle executing simple harmonic motion of time period $\mathrm{T}$, then, which of the following does not change with time?

**Options:**

- **(A)** $a^2 T^2+4 \pi^2 v^2$
- **(B)** $\frac{a T}{x}$
- **(C)** $a T+2 \pi v$
- **(D)** $\frac{a T}{v}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{a T}{x}$**

**Detailed Solution:**

$$
\frac{\text { aT }}{\mathrm{X}}=\frac{\omega^2 \mathrm{XT}}{\mathrm{X}}=\frac{4 \pi^2}{\mathrm{~T}^2} \times \mathrm{T}=\frac{4 \pi^2}{\mathrm{~T}}=\text { constant. }
$$

</details>

---

### Q62. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `2`

A point mass oscillates along the $x$-axis according to the law $\mathrm{x=x_0 \cos (\omega t-\pi / 4)}$. If the acceleration of the particle is written as
$\mathrm{a=A \cos (\omega t+\delta)}$

**Options:**

- **(A)** $\mathrm{A}=\mathrm{x}_0, \delta=-\pi / 4$
- **(B)** $\mathrm{A}=\mathrm{x}_0 \omega^2, \delta=-\pi / 4$
- **(C)** $\mathrm{A}=\mathrm{x}_0 \omega^2, \delta=-\pi / 4$
- **(D)** $\mathrm{A=x_0 \omega^2, \delta=3 \pi / 4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{A=x_0 \omega^2, \delta=3 \pi / 4}$**

**Detailed Solution:**

$\mathrm{v=-x_0 \omega \sin (\omega t-\pi / 4)}$
$\mathrm{a=-x_0 \omega^2 \cos \left(\omega t+\pi-\frac{\pi}{4}\right)}$
$\mathrm{a=A \cos (\omega t+\delta)}$
$\mathrm{A=x_0 \omega^2 ; \quad \delta=\frac{3 \pi}{4}}$

</details>

---

### Q63. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `1`

The displacement of an object attached to a spring and executing simple harmonic motion is given by $x=2 \times 10^{-2} \cos \pi t$ metres. The time at which the maximum speed first occurs is

**Options:**

- **(A)** $0.5 \mathrm{~s}$
- **(B)** $0.75 \mathrm{~s}$
- **(C)** $0.125 \mathrm{~s}$
- **(D)** $0.25 \mathrm{~s}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.5 \mathrm{~s}$**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{x}=2 \times 10^{-2} \cos \pi t \\
& \mathrm{v}=-0.02 \pi \sin \pi t
\end{aligned}$
$\mathrm{v}$ is maximum at $\mathrm{t}=\frac{1}{2}=0.5 \mathrm{~sec}$

</details>

---

### Q64. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `3`

A coin is placed on a horizontal platform which undergoes vertical simple harmonic motion of angular frequency $\omega$. The amplitude of oscillation is gradually increased. The coin will leave contact with the platform for the first time

**Options:**

- **(A)** at the highest position of the platform
- **(B)** at the mean position of the platform
- **(C)** for an amplitude of $\frac{\mathrm{g}}{\omega^2}$
- **(D)** for an amplitude of $\frac{\mathrm{g}^2}{\omega^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) for an amplitude of $\frac{\mathrm{g}}{\omega^2}$**

**Detailed Solution:**

$A \omega^2=g$
$\Rightarrow A=g / \omega^2$

</details>

---

### Q65. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

Two simple harmonic motions are represented by the equation $\mathrm{y}_1=0.1$ $\sin \left(100 \pi t+\frac{\pi}{3}\right)$ and $y_2=0.1 \cos \pi t$. The phase difference of the velocity of particle 1 w.r.t. the velocity of the particle 2 is

**Options:**

- **(A)** $-\pi / 6$
- **(B)** $\pi / 3$
- **(C)** $-\pi / 3$
- **(D)** $\pi / 6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\pi / 6$**

**Detailed Solution:**

Phase difference $(\phi)=99 \pi \mathrm{t}+\pi / 3-\pi / 2$ at $t=0, \phi=-\pi / 6$.

</details>

---

### Q66. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

The function $\sin ^2(\omega t)$ represents

**Options:**

- **(A)** a periodic, but not simple harmonic motion with a period $2 \pi / \omega$
- **(B)** a periodic, but not simple harmonic motion with a period $\pi / \omega$
- **(C)** a simple harmonic motion with a period $2 \pi / \omega$
- **(D)** a simple harmonic motion with a period $\pi / \omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) a simple harmonic motion with a period $\pi / \omega$**

**Detailed Solution:**

$y=\frac{(1-\cos 2 \omega t)}{2}$

</details>

---

### Q67. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `3`

The displacement of a particle varies according to the relation $x=4(\cos \pi t+\sin \pi t)$. The amplitude of the particle is

**Options:**

- **(A)** $-4$
- **(B)** $4$
- **(C)** $4 \sqrt{2}$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4 \sqrt{2}$**

**Detailed Solution:**

$\left.x=4(\cos \pi t+\sin \pi t)=4\left[\sin \left(\frac{\pi}{2}-\pi t\right)\right]+\sin \pi t\right]=4\left[2 \times \sin \left(\frac{\pi t-\frac{\pi}{2}-\pi t}{2}\right) \cos \left(\frac{\pi \mathrm{t}-\frac{\pi}{2}+\pi \mathrm{t}}{2}\right)\right]$
$=8\left[\sin \frac{\pi}{4} \cdot \cos \left(-\frac{\pi}{4}+\pi t\right)\right]$
$=\frac{8}{\sqrt{2}} \cdot \cos \left[\pi t-\frac{\pi}{4}\right]=4 \sqrt{2} \cos \left[\pi t-\frac{\pi}{4}\right]$
Comparing it with standard equation
$X=A \cos (w t-K x) \quad \Rightarrow A=4 \sqrt{2}$

</details>

---

### Q68. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

Two particles $\mathrm{A}$ and $\mathrm{B}$ of equal masses are suspended from two massless springs of spring constant $\mathrm{k}_1$ and $\mathrm{k}_2$, respectively. If the maximum velocities, during oscillation, are equal, the ratio of amplitude of $A$ and $B$ is

**Options:**

- **(A)** $\sqrt{\frac{\mathrm{k}_1}{\mathrm{k}_2}}$
- **(B)** $\frac{\mathrm{k}_2}{\mathrm{k}_1}$
- **(C)** $\sqrt{\frac{\mathrm{k}_2}{\mathrm{k}_1}}$
- **(D)** $\frac{\mathrm{k}_1}{\mathrm{k}_2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{\frac{\mathrm{k}_2}{\mathrm{k}_1}}$**

**Detailed Solution:**

$\mathrm{V}_{\max }=\omega \mathrm{A}=\mathrm{m} \omega^2 \mathrm{I}=\mathrm{k}$
$\Rightarrow \omega^2=\frac{\mathrm{k}}{\mathrm{m}} \Rightarrow \omega=\sqrt{\frac{\mathrm{k}}{\mathrm{m}}} \quad \Rightarrow \omega \propto \sqrt{\mathrm{K}} \quad$ or $\quad \frac{\omega_1}{\omega_2}=\sqrt{\frac{\mathrm{k}_1}{\mathrm{k}_2}}$
$\mathrm{V}_{\mathrm{A}} \max =\mathrm{V}_{\mathrm{B}} \max \quad \Rightarrow\left(\sqrt{\frac{\mathrm{k}_1}{\mathrm{~m}}}\right)\left(\mathrm{A}_1\right)=\left(\sqrt{\frac{\mathrm{k}_2}{\mathrm{~m}}}\right)\left(\mathrm{A}_2\right) \Rightarrow \frac{\mathrm{A}_1}{\mathrm{~A}_2}=\sqrt{\frac{\mathrm{k}_2}{\mathrm{k}_1}}$

</details>

---

