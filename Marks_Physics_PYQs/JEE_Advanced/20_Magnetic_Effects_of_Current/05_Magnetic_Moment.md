# JEE Advanced Physics - Magnetic Effects of Current

## Topic 5: Magnetic Moment

**Total Questions:** 4

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `numerical` | *Level:* `3`

A hollow, right circular cone of base radius $R$ and height $h$, with its tip at the origin is rotating about the $Z$-axis with an angular velocity $\omega$, as shown in the figure. The cone carries a total charge $Q$ uniformly distributed on its curved surface. The magnitude of magnetic field at a point $(0, 0, z)$, where $z \gg R$ and $z \gg h$, is $\dfrac{n\mu_0}{4\pi}\dfrac{Q R^2 \omega}{z^3}$. The value of $n$ is:
<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/jee_adv/2026/watermarked_images/p1_english__q28_d1.png" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.5**

**Detailed Solution:**

For a point on the axis at a distance $z \gg R$ and $z \gg h$, the rotating cone can be considered as a magnetic dipole. The magnetic field on the axis of a dipole is given by:

$B = \dfrac{\mu_0}{4\pi} \dfrac{2M}{z^3}$

where $M$ is the magnetic dipole moment of the cone.

To find $M$, consider an elemental ring on the cone at a vertical distance $y$ from the origin, with vertical thickness $dy$. The radius of this ring is $r = \dfrac{R}{h}y$ and its slant length is $dl = \dfrac{\sqrt{R^2+h^2}}{h}dy$.

The surface charge density of the cone is $\sigma = \dfrac{Q}{\pi R \sqrt{R^2+h^2}}$.

The charge on the elemental ring is:

$dq = \sigma (2\pi r dl) = \dfrac{Q}{\pi R \sqrt{R^2+h^2}} \left(2\pi \dfrac{R}{h}y \dfrac{\sqrt{R^2+h^2}}{h}dy\right) = \dfrac{2Q}{h^2}y dy$

The current due to the rotation of this ring is:

$dI = \dfrac{dq}{T} = \dfrac{dq \omega}{2\pi} = \dfrac{Q\omega}{\pi h^2}y dy$

The magnetic moment of this elemental ring is:

$dM = dI (\pi r^2) = \left(\dfrac{Q\omega}{\pi h^2}y dy\right) \pi \left(\dfrac{R}{h}y\right)^2 = \dfrac{Q\omega R^2}{h^4}y^3 dy$

Integrating from $y = 0$ to $y = h$, the total magnetic moment is:

$M = \int_{0}^{h} \dfrac{Q\omega R^2}{h^4}y^3 dy = \dfrac{Q\omega R^2}{h^4} \left[\dfrac{y^4}{4}\right]_{0}^{h} = \dfrac{Q\omega R^2}{4}$

Alternatively, using the gyromagnetic ratio for a uniform charge distribution, $\dfrac{M}{L_{ang}} = \dfrac{Q}{2m}$. The moment of inertia of a hollow cone is $I = \dfrac{1}{2}mR^2$, so the angular momentum is $L_{ang} = \dfrac{1}{2}mR^2\omega$. Thus, $M = \dfrac{Q}{2m} \left(\dfrac{1}{2}mR^2\omega\right) = \dfrac{1}{4}QR^2\omega$.

Substituting $M$ into the magnetic field formula:

$B = \dfrac{\mu_0}{4\pi} \dfrac{2}{z^3} \left(\dfrac{1}{4}QR^2\omega\right) = \dfrac{\mu_0}{4\pi} \dfrac{QR^2\omega}{2z^3}$

Comparing this with the given expression $B = \dfrac{n\mu_0}{4\pi} \dfrac{QR^2\omega}{z^3}$, we get:

$n = \dfrac{1}{2} = 0.5$

Answer: $0.5$

</details>

---

### Q2. JEE Advanced 2025 (Paper 2)

*Type:* `numerical` | *Level:* `1`

A conducting solid sphere of radius $R$ and mass $M$ carries a charge $Q$. The sphere is rotating about an axis passing through its center with a uniform angular speed $\omega$. The ratio of the magnitudes of the magnetic dipole moment to the angular momentum about the same axis is given as $\alpha \frac{Q}{2 M}$. The value of $\alpha$ is _______ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1.66**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/8PV3uchCpyB4ABxur_-K1o17VanGEw9MdAB3vQ4AClI.original.fullsize.png">
$\begin{aligned} & d M=d I A \\ & A=\pi r^2=\pi(R \sin \theta)^2 \\ & d I=\frac{d a}{T}=\frac{\sigma(2 \pi r)(R d \theta) \omega}{2 \pi} \\ & d I=\frac{\sigma 2 \pi R^2 \omega \sin \theta d \theta}{2 \pi}\end{aligned}$
$\mathrm{dI}=\sigma \mathrm{R}^2 \omega \sin \theta \mathrm{~d} \theta$
Magnetic dipole moment :
$M=\int d M=\int_0^\pi \sigma R^2 \omega \pi R^2 \sin ^3 \theta d \theta$
$M=\sigma R^4 \omega \pi \int_0^\pi \sin ^3 \theta d \theta \quad\left(\because \int_0^\pi \sin ^3 \theta d \theta=\frac{4}{3}\right)$
$\mathrm{M}=\left(\frac{\mathrm{Q}}{4 \pi \mathrm{R}^2}\right) \mathrm{R}^4 \omega \pi\left(\frac{4}{3}\right)$
Magnetic dipole moment
$\mathrm{M}=\frac{\mathrm{QR}^2 \omega}{3}$
Angular momentum
$\mathrm{L}=\left(\frac{2}{5} \mathrm{MR}^2\right) \omega$
$\frac{\mathrm{M}}{\mathrm{~L}}=\frac{\mathrm{QR}^2 \omega}{3 \times \frac{2}{5} \mathrm{MR}^2 \omega}=\frac{\mathrm{Q}}{2 \mathrm{M}}\left(\frac{5}{3}\right)$
$\alpha=\frac{5}{3}=1.67$

</details>

---

### Q3. JEE Advanced 2012 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

A loop carrying current $I$ lies in the $x-y$ plane as shown in the figure. The unit vector $\hat{k}$ is coming out of the plane of the paper. The magnetic moment of the current loop is

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ZQI4dW5wmYwSBqFfVnVz4R2SgFtX3OlMJYgeeFwFsz8.original.fullsize.png">

**Options:**

- **(A)** $a^{2} I \hat{k}$
- **(B)** $\left(\frac{\pi}{2}+1\right) a^{2} I \hat{k}$
- **(C)** $-\left(\frac{\pi}{2}+1\right) a^{2} I \hat{k}$
- **(D)** $(2 \pi+1) a^{2} I \hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\frac{\pi}{2}+1\right) a^{2} I \hat{k}$**

**Detailed Solution:**

Magnetic moment of a current carrying loop $\vec{M}=N I \vec{A}$

Here $N=1, A=a^{2}+2 \pi\left(\frac{a}{2}\right)^{2}=a^{2}\left[1+\frac{\pi}{2}\right]$

From Screw law, direction of $m$ is outward or in +ve z-direction.

$\therefore \quad \vec{M}=I a^{2}\left[1+\frac{\pi}{2}\right] \hat{k}$

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/gqv5YWas2u0OrTX0h5hHA_A8CiX4RBcAhWprW1WAXoM.original.fullsize.png">

</details>

---

### Q4. JEE Advanced 2011 (Paper 1)

*Type:* `numerical` | *Level:* `3`

A long circular tube of length $10 \mathrm{~m}$ and radius $0.3 \mathrm{~m}$ carries a current I along its curved surface as shown. A wire loop of resistance $0.005 \Omega$ and of radius $0.1 \mathrm{~m}$ is placed inside the tube with its axis coinciding with the axis of the tube. The current varies as $I=I_0 \cos 300 t$, where $I_0$ is constant. If the magnetic moment of the loop is $N \mu_0 I_0 \sin 300 t$, then $N$ is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/CbAZwTPq4oMzOvE4BMMDId0ZYqPEcVqy6u9nDKdL4lA.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

Take the circular tube as a long solenoid. The wires are closely wound. Magnetic field inside the solenoid is
$$
B=\mu_0 n i
$$
Here, $n=$ number of turns per unit length
$\therefore n i=$ current per unit length
In the given problem,

$$
\begin{aligned}
& n i=\frac{I}{L} \\
\therefore \quad B & =\frac{\mu_0 I}{L}
\end{aligned}
$$
Flux passing through the circular coil is
$$
\phi=B S=\left(\frac{\mu_0 I}{L}\right)\left(\pi r^2\right)
$$
Induced emf, $e=-\frac{d \phi}{d t}=-\left(\frac{\mu_0 \pi r^2}{L R}\right) \cdot \frac{d I}{d t}$
Induced current,
$$
i=\frac{e}{R}=-\left(\frac{\mu_0 \pi r^2}{L R}\right) \frac{d I}{d t}
$$
Magnetic moment $i A=i \pi r^2$
or $\quad M=-\left(\frac{\mu_0 \pi^2 r^4}{L R}\right) \cdot \frac{d I}{d t}$
Given, $\quad I=I_0 \cos 300 t$
$$
\therefore \quad \frac{d I}{d t}=-300 I_0 \sin (300 t)
$$

Substituting in Eq. (i), we get
$$
\begin{aligned}
M & =\left(\frac{300 \pi^2 r^4}{L R}\right) \mu_0 I_0 \sin 300 t \\
\therefore \quad N & =\frac{300 \pi^2 r^4}{L R}
\end{aligned}
$$
Substituting the values, we get
$$
\begin{aligned}
N & =\frac{300(22 / 7)^2(0.1)^4}{(10)(0.005)} \\
& =5.926
\end{aligned}
$$
or $\quad N \simeq 6$
Analysis of Question
Question is difficult to understand inside the examination hall. But 5 to $10 \%$ question in IIT JEE are always difficult. Students should not panic. Because topper of IIT JEE scores approximately $80-90 \%$.

</details>

---

