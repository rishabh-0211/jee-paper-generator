# JEE Advanced Physics - Wave Optics

## Topic 5: Diffraction of Light

**Total Questions:** 2

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `numerical` | *Level:* `3`

In a single slit diffraction experiment, a slit of width $(0.016 \pm 0.002)$ mm is used to measure the wavelength of a monochromatic light source. In the diffraction pattern, the angular distance between the central maximum and first minimum is measured to be $(2^\circ \pm 40')$. The value of the fractional error in the measurement of wavelength is:
[Given: $\sin(2^\circ) = 0.035$]

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.46**

**Detailed Solution:**

For a single slit diffraction, the condition for the first minimum is given by:

$a \sin \theta = \lambda$

Taking the natural logarithm on both sides, we get:

$\ln \lambda = \ln a + \ln(\sin \theta)$

Differentiating to find the maximum fractional error:

$\dfrac{\Delta \lambda}{\lambda} = \dfrac{\Delta a}{a} + \cot \theta \Delta \theta$

Since $\theta = 2^\circ$ is very small, $\cos \theta \approx 1$, which gives $\cot \theta \approx \dfrac{1}{\sin \theta}$.

Given $\sin(2^\circ) = 0.035$, we can approximate the angle in radians as $\theta \approx \sin \theta = 0.035$ rad.

The error in the angle is $\Delta \theta = 40' = \left(\dfrac{40}{60}\right)^\circ = \left(\dfrac{2}{3}\right)^\circ$.

Converting $\Delta \theta$ into radians:

$\Delta \theta = \dfrac{2}{3} \times \left(\dfrac{0.035}{2}\right) = \dfrac{0.035}{3}$ rad

The fractional error in the angular term is:

$\cot \theta \Delta \theta \approx \dfrac{\Delta \theta}{\sin \theta} = \dfrac{\dfrac{0.035}{3}}{0.035} = \dfrac{1}{3}$

The fractional error in the slit width is:

$\dfrac{\Delta a}{a} = \dfrac{0.002}{0.016} = \dfrac{1}{8}$

Substituting these values into the error equation:

$\dfrac{\Delta \lambda}{\lambda} = \dfrac{1}{8} + \dfrac{1}{3} = \dfrac{3 + 8}{24} = \dfrac{11}{24}$

Answer: $0.46$

</details>

---

### Q2. JEE Advanced 2025 (Paper 1)

*Type:* `numerical` | *Level:* `2`

A single slit diffraction experiment is performed to determine the slit width using the equation, $\frac{b d}{D}=m \lambda$, where $b$ is the slit width, $D$ the shortest distance between the slit and the screen, $d$ the distance between the $m^{\text {th }}$ diffraction maximum and the central maximum, and $\lambda$ is the wavelength. $D$ and $d$ are measured with scales of least count of 1 cm and 1 mm, respectively. The values of $\lambda$ and $m$ are known precisely to be 600 nm and 3, respectively. The maximum absolute error (in $\mu \mathrm{m}$) in the value of $b$ estimated using the diffraction maximum that occurs for $m=3$ with $d=5 \mathrm{~mm}$ and $D=1 \mathrm{~m}$ is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **94.5**

**Detailed Solution:**

Original question asked about absolute error which can be both minimum or maximum, we added word maximum to make it clear for students
$\begin{aligned} & \mathrm{b}=\frac{\mathrm{m} \lambda \mathrm{D}}{\mathrm{d}}=360 \mu \mathrm{~m} \\ & \mathrm{~b}_{\max }=\frac{3 \times 600 \times 10^{-3} \times 1.01}{4 \times 10^{-3}} \mu \mathrm{~m}=454.5 \mu \mathrm{~m} \\ & \mathrm{~b}_{\min }=\frac{3 \times 600 \times 10^{-3} \times 0.99}{6 \times 10^{-3}} \mu \mathrm{~m}=297 \mu \mathrm{~m}\end{aligned}$
Maximum value of b gives error, $\Delta \mathrm{b}_1=94.5 \mu \mathrm{~m}$
Minimum value of $b$ gives error, $\Delta b_2=63 \mu \mathrm{~m}$
$\therefore$ We always report the largest error, hence correct answer should be $94.5 \mu \mathrm{~m}$

</details>

---

