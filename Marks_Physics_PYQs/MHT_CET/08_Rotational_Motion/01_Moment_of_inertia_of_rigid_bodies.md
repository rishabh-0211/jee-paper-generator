# MHT CET Physics - Rotational Motion

## Topic 1: Moment of inertia of rigid bodies

**Total Questions:** 140

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

At the corners of an equilateral triangle of side L, point masses, each of mass $2$ kg are placed. The moment of inertia of the system about an axis along any one side is (in kg$-$m$^2$)

**Options:**

- **(A)** $\dfrac{3L^2}{4}$
- **(B)** $\dfrac{L^2}{3}$
- **(C)** $\dfrac{3L^2}{2}$
- **(D)** $\dfrac{4L^2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{3L^2}{2}$**

**Detailed Solution:**

Let the three masses be placed at the vertices A, B, and C of the equilateral triangle. Let the axis of rotation be along the side AB.

The perpendicular distance of the masses at A and B from the axis of rotation is zero, so their contribution to the moment of inertia is zero.

The perpendicular distance of the mass at C from the side AB is the altitude of the equilateral triangle, given by $r = L \sin(60^{\circ}) = \dfrac{\sqrt{3}L}{2}$.

The moment of inertia of the system about the side AB is:

$I = m_A r_A^2 + m_B r_B^2 + m_C r_C^2$

Substituting the values $m_A = m_B = m_C = 2$ kg, $r_A = 0$, $r_B = 0$, and $r_C = \dfrac{\sqrt{3}L}{2}$:

$I = 2(0)^2 + 2(0)^2 + 2 \left( \dfrac{\sqrt{3}L}{2} \right)^2$

$I = 2 \left( \dfrac{3L^2}{4} \right) = \dfrac{3L^2}{2}$

Answer: $\dfrac{3L^2}{2}$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A ring of mass $M$ and radius $R$ is rotating with angular speed $\omega$ about a fixed vertical axis passing through its centre $O$ with two point masses each of mass $\dfrac{M}{8}$ at rest at $O$. These masses can move radially outwards along two mass-less rods fixed on the ring as shown in figure. At some instant the angular speed of the system is $\dfrac{8\omega}{9}$ and one of the masses is at a distance of $\dfrac{3}{5}R$ from point $O$. At this instant, the distance of the other mass from point $O$ is
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/19_may_shift_2__q38_d1.png" />

**Options:**

- **(A)** $\dfrac{2R}{3}$
- **(B)** $\dfrac{R}{3}$
- **(C)** $\dfrac{3R}{5}$
- **(D)** $\dfrac{4R}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{4R}{5}$**

**Detailed Solution:**

By the principle of conservation of angular momentum, since no external torque acts on the system about the axis of rotation, the initial angular momentum equals the final angular momentum:

$L_i = L_f$

$I_i \omega_i = I_f \omega_f$

Initially, the two point masses are at the centre $O$, so their distance from the axis of rotation is zero. The initial moment of inertia of the system is just that of the ring:

$I_i = MR^2$

Let the distance of the second mass from $O$ be $r_2$. The final moment of inertia of the system when one mass is at $r_1 = \dfrac{3}{5}R$ and the other is at $r_2$ is:

$I_f = MR^2 + \dfrac{M}{8}\left(\dfrac{3}{5}R\right)^2 + \dfrac{M}{8}r_2^2$

$I_f = MR^2 + \dfrac{9M}{200}R^2 + \dfrac{M}{8}r_2^2$

Substituting the values into the conservation of angular momentum equation:

$MR^2 \omega = \left( MR^2 + \dfrac{9M}{200}R^2 + \dfrac{M}{8}r_2^2 \right) \left( \dfrac{8\omega}{9} \right)$

Dividing both sides by $M\omega$:

$R^2 = \left( R^2 + \dfrac{9}{200}R^2 + \dfrac{r_2^2}{8} \right) \dfrac{8}{9}$

Multiplying by $\dfrac{9}{8}$:

$\dfrac{9}{8}R^2 = R^2 + \dfrac{9}{200}R^2 + \dfrac{r_2^2}{8}$

$\dfrac{9}{8}R^2 - R^2 = \dfrac{9}{200}R^2 + \dfrac{r_2^2}{8}$

$\dfrac{1}{8}R^2 = \dfrac{9}{200}R^2 + \dfrac{r_2^2}{8}$

Multiplying the entire equation by $200$ to clear the denominators:

$25R^2 = 9R^2 + 25r_2^2$

$16R^2 = 25r_2^2$

$r_2^2 = \dfrac{16}{25}R^2$

$r_2 = \dfrac{4}{5}R$

Answer: $\dfrac{4R}{5}$

</details>

---

### Q3. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A uniform rod of length $l$ is free to rotate in a vertical plane about a fixed horizontal axis through point B. The rod begins rotating from rest, from its unstable equilibrium position. The angular velocity $\omega$, when it has turned through an angle $\theta$, is
<img style="width: 150px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/19_may_shift_2__q37_d1_v2.png" />

**Options:**

- **(A)** $\sqrt{\dfrac{6g}{l}}\cos\dfrac{\theta}{2}$
- **(B)** $\sqrt{\dfrac{6g}{l}}\sin\theta$
- **(C)** $\sqrt{\dfrac{6g}{l}}\sin\dfrac{\theta}{2}$
- **(D)** $\sqrt{\dfrac{6g}{l}}\cos\theta$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{\dfrac{6g}{l}}\sin\dfrac{\theta}{2}$**

**Detailed Solution:**

Let the mass of the uniform rod be $m$.

The moment of inertia of the rod about the fixed horizontal axis passing through its end B is $I = \dfrac{ml^2}{3}$.

Let the horizontal plane passing through the pivot B be the reference level for potential energy.

In the initial unstable equilibrium position, the rod is vertically upright. The height of its center of mass from B is $h_i = \dfrac{l}{2}$.

When the rod has turned through an angle $\theta$, the height of its center of mass from B becomes $h_f = \dfrac{l}{2} \cos\theta$.

According to the principle of conservation of mechanical energy, the loss in gravitational potential energy is equal to the gain in rotational kinetic energy.

Loss in potential energy = $mg(h_i - h_f) = mg \left( \dfrac{l}{2} - \dfrac{l}{2} \cos\theta \right) = \dfrac{mgl}{2} (1 - \cos\theta)$

Gain in rotational kinetic energy = $\dfrac{1}{2} I \omega^2 = \dfrac{1}{2} \left( \dfrac{ml^2}{3} \right) \omega^2 = \dfrac{ml^2}{6} \omega^2$

Equating the energies:

$\dfrac{ml^2}{6} \omega^2 = \dfrac{mgl}{2} (1 - \cos\theta)$

$\omega^2 = \dfrac{3g}{l} (1 - \cos\theta)$

Using the trigonometric identity $1 - \cos\theta = 2 \sin^2\left(\dfrac{\theta}{2}\right)$:

$\omega^2 = \dfrac{3g}{l} \times 2 \sin^2\left(\dfrac{\theta}{2}\right)$

$\omega^2 = \dfrac{6g}{l} \sin^2\left(\dfrac{\theta}{2}\right)$

$\omega = \sqrt{\dfrac{6g}{l}} \sin\left(\dfrac{\theta}{2}\right)$

</details>

---

### Q4. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Three rings each of mass $M$ and radius $R$ are arranged as shown in the figure. The moment of inertia of a system about axis $YY'$ will be
<img style="width: 200px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/19_may_shift_2__q10_d1_v2.png" />

**Options:**

- **(A)** $\dfrac{3MR^2}{2}$
- **(B)** $3MR^2$
- **(C)** $\dfrac{7MR^2}{2}$
- **(D)** $5MR^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{7MR^2}{2}$**

**Detailed Solution:**

The system consists of three identical rings, each of mass $M$ and radius $R$, lying in the same plane. The axis $YY'$ is in the plane of the rings.

For ring A, the axis $YY'$ passes through its center and acts as a diameter. The moment of inertia of a ring about its diameter is:
$I_A = \dfrac{1}{2}MR^2$

For ring B, the axis $YY'$ is tangent to the ring. The distance from the center of ring B to the axis $YY'$ is $R$. Using the parallel axis theorem, the moment of inertia of ring B about the axis $YY'$ is the sum of its moment of inertia about a parallel diameter and the product of its mass and the square of the distance between the axes:
$I_B = I_{\text{diameter}} + MR^2$
$I_B = \dfrac{1}{2}MR^2 + MR^2 = \dfrac{3}{2}MR^2$

Similarly, for ring C, the axis $YY'$ is also a tangent, and its center is at a distance $R$ from the axis. Its moment of inertia about the axis $YY'$ is:
$I_C = \dfrac{1}{2}MR^2 + MR^2 = \dfrac{3}{2}MR^2$

The total moment of inertia of the system about the axis $YY'$ is the sum of the individual moments of inertia:
$I_{\text{total}} = I_A + I_B + I_C$
$I_{\text{total}} = \dfrac{1}{2}MR^2 + \dfrac{3}{2}MR^2 + \dfrac{3}{2}MR^2$
$I_{\text{total}} = \dfrac{7}{2}MR^2$

Answer: $\dfrac{7MR^2}{2}$

</details>

---

### Q5. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Moment of inertia of a disc of mass $m$ and radius $R$ about the centre of mass and perpendicular to plane is $I_1$ and moment of inertia of disc at a distance $\dfrac{2R}{3}$ from centre and perpendicular to plane is $I_2$ then $I_1/I_2$ is

**Options:**

- **(A)** $\dfrac{6}{17}$
- **(B)** $\dfrac{9}{17}$
- **(C)** $\dfrac{8}{9}$
- **(D)** $\dfrac{5}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{9}{17}$**

**Detailed Solution:**

Moment of inertia of the disc about its centre of mass and perpendicular to its plane is given by:

$I_1 = \dfrac{1}{2} m R^2$

Using the parallel axis theorem, the moment of inertia about an axis at a distance $d = \dfrac{2R}{3}$ from the centre and perpendicular to the plane is:

$I_2 = I_1 + m d^2$

$I_2 = \dfrac{1}{2} m R^2 + m \left(\dfrac{2R}{3}\right)^2$

$I_2 = \dfrac{1}{2} m R^2 + \dfrac{4}{9} m R^2$

$I_2 = \left(\dfrac{9 + 8}{18}\right) m R^2 = \dfrac{17}{18} m R^2$

The ratio of the moments of inertia is:

$\dfrac{I_1}{I_2} = \dfrac{\dfrac{1}{2} m R^2}{\dfrac{17}{18} m R^2} = \dfrac{9}{17}$

Answer: $\dfrac{9}{17}$

</details>

---

### Q6. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A square frame ABCD is formed by 4 identical rods each of mass $m$ and length $\ell$. This frame is in XY plane such that side AB coincides with x-axis and side AD along y-axis. The moment of inertia of the frame about x-axis is

**Options:**

- **(A)** $\dfrac{5m\ell^2}{3}$
- **(B)** $\dfrac{2m\ell^2}{3}$
- **(C)** $\dfrac{4m\ell^2}{3}$
- **(D)** $\dfrac{m\ell^2}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{5m\ell^2}{3}$**

**Detailed Solution:**

The square frame consists of four identical rods: AB, BC, CD, and DA, each of mass $m$ and length $\ell$.

The moment of inertia of the frame about the x-axis is the sum of the moments of inertia of each rod about the x-axis.

For rod AB, it lies on the x-axis, so its moment of inertia is $I_{AB} = 0$.

For rod BC, it is perpendicular to the x-axis with one end on the x-axis, so its moment of inertia is $I_{BC} = \dfrac{m\ell^2}{3}$.

For rod CD, it is parallel to the x-axis at a perpendicular distance $\ell$, so its moment of inertia is $I_{CD} = m\ell^2$.

For rod DA, it is perpendicular to the x-axis with one end on the x-axis, so its moment of inertia is $I_{DA} = \dfrac{m\ell^2}{3}$.

The total moment of inertia of the frame about the x-axis is:

$I = I_{AB} + I_{BC} + I_{CD} + I_{DA}$

$I = 0 + \dfrac{m\ell^2}{3} + m\ell^2 + \dfrac{m\ell^2}{3}$

$I = \dfrac{5m\ell^2}{3}$

Answer: $\dfrac{5m\ell^2}{3}$

</details>

---

### Q7. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A thin uniform rod of length $L$ and mass $m$ is swinging freely about a horizontal axis passing through its end. Its maximum angular speed is $\omega$. Its centre of mass rises to a maximum height of ($g$ = acceleration due to gravity)

**Options:**

- **(A)** $\dfrac{L^2\omega^2}{2g}$
- **(B)** $\dfrac{L\omega}{6g}$
- **(C)** $\dfrac{L\omega}{2g}$
- **(D)** $\dfrac{L^2\omega^2}{6g}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{L^2\omega^2}{6g}$**

**Detailed Solution:**

By the principle of conservation of mechanical energy, the maximum rotational kinetic energy of the rod is equal to the maximum potential energy gained by its centre of mass.

The maximum kinetic energy is given by

$K = \dfrac{1}{2} I \omega^2$

The moment of inertia of a uniform rod of mass $m$ and length $L$ about an axis passing through its end is

$I = \dfrac{mL^2}{3}$

Substituting $I$ into the kinetic energy expression, we get

$K = \dfrac{1}{2} \left( \dfrac{mL^2}{3} \right) \omega^2 = \dfrac{mL^2\omega^2}{6}$

Let $h$ be the maximum height to which the centre of mass rises. The maximum potential energy gained is

$U = mgh$

Equating the maximum kinetic energy and the maximum potential energy:

$mgh = \dfrac{mL^2\omega^2}{6}$

$h = \dfrac{L^2\omega^2}{6g}$

Answer: $\dfrac{L^2\omega^2}{6g}$

</details>

---

### Q8. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A solid sphere is rotating about a diameter at an angular velocity $\omega$. If it cools so that its radius reduces to $\left(\dfrac{1}{n}\right)^{\text{th}}$ of its original value, its angular velocity becomes

**Options:**

- **(A)** $\dfrac{\omega}{n}$
- **(B)** $\dfrac{\omega}{n^2}$
- **(C)** $n\omega$
- **(D)** $n^2 \omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $n^2 \omega$**

**Detailed Solution:**

By the principle of conservation of angular momentum, the angular momentum of the sphere remains constant since no external torque acts on it.

$I_1 \omega_1 = I_2 \omega_2$

The initial moment of inertia of the solid sphere is $I_1 = \dfrac{2}{5}MR^2$.

When the radius reduces to $\dfrac{1}{n}$ of its original value, the new radius is $R' = \dfrac{R}{n}$.

The new moment of inertia is $I_2 = \dfrac{2}{5}M\left(\dfrac{R}{n}\right)^2 = \dfrac{I_1}{n^2}$.

Substituting the values into the conservation of angular momentum equation:

$I_1 \omega = \left(\dfrac{I_1}{n^2}\right) \omega_2$

$\omega_2 = n^2 \omega$

Answer: $n^2 \omega$

</details>

---

### Q9. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The moment of inertia of a solid sphere about an axis passing through centre of gravity is $\dfrac{2MR^2}{5}$ where M is the mass and R is the radius. The radius of gyration about a parallel axis at a distance $2R$ from first axis is

**Options:**

- **(A)** $5R$
- **(B)** $\sqrt{\dfrac{22}{5}}\,R$
- **(C)** $\dfrac{5R}{2}$
- **(D)** $\sqrt{\dfrac{12}{5}}\,R$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{\dfrac{22}{5}}\,R$**

**Detailed Solution:**

Using the parallel axis theorem, the moment of inertia about the new axis is given by $I = I_{cm} + Md^2$.

Given $I_{cm} = \dfrac{2}{5}MR^2$ and $d = 2R$.

Substituting the values, we get $I = \dfrac{2}{5}MR^2 + M(2R)^2 = \dfrac{2}{5}MR^2 + 4MR^2 = \dfrac{22}{5}MR^2$.

The radius of gyration $K$ is given by $I = MK^2$.

Equating the two expressions for $I$, we get $MK^2 = \dfrac{22}{5}MR^2$.

Solving for $K$, we get $K = \sqrt{\dfrac{22}{5}}R$.

Answer: $\sqrt{\dfrac{22}{5}}\,R$

</details>

---

### Q10. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A thin wire of length $L$ and uniform linear mass density $\rho$ is bent into a circular loop with centre at '$O$' as shown in figure. The moment of inertia of the loop about the axis $XX'$ is
<img style="width: 250px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/13_may_shift_2__q13_d1_v2.png" />

**Options:**

- **(A)** $\dfrac{\rho L^3}{16\pi^2}$
- **(B)** $\dfrac{\rho L^3}{8\pi^2}$
- **(C)** $\dfrac{5}{16}\rho L^3 \pi$
- **(D)** $\dfrac{3\rho L^3}{8\pi^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{3\rho L^3}{8\pi^2}$**

**Detailed Solution:**

Let the mass of the circular loop be $M$ and its radius be $R$.

Given that the wire has length $L$ and linear mass density $ho$, the total mass of the loop is:
$M = ho L$

Since the wire is bent into a circular loop, its circumference is equal to $L$:
$2\pi R = L \Rightarrow R = \dfrac{L}{2\pi}$

The moment of inertia of a circular ring about its diameter is:
$I_d = \dfrac{1}{2}MR^2$

The axis $XX'$ is a tangent to the circular loop in its plane, which is parallel to the diameter at a distance $R$. Using the parallel axis theorem, the moment of inertia about the axis $XX'$ is:
$I_{XX'} = I_d + MR^2$
$I_{XX'} = \dfrac{1}{2}MR^2 + MR^2 = \dfrac{3}{2}MR^2$

Substituting the values of $M$ and $R$ into the equation:
$I_{XX'} = \dfrac{3}{2}(\rho L)\left(\dfrac{L}{2\pi}\right)^2$
$I_{XX'} = \dfrac{3}{2}(\rho L)\left(\dfrac{L^2}{4\pi^2}\right)$
$I_{XX'} = \dfrac{3\rho L^3}{8\pi^2}$

Answer: $\dfrac{3\rho L^3}{8\pi^2}$

</details>

---

### Q11. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The ratio of radius of gyration of circular disc about a tangential axis in its plane and of a circular ring of the same radius about a tangential axis in its plane is

**Options:**

- **(A)** $2 : 3$
- **(B)** $2 : 1$
- **(C)** $\sqrt{5} : \sqrt{6}$
- **(D)** $1 : \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{5} : \sqrt{6}$**

**Detailed Solution:**

Moment of inertia of a circular disc about a diametric axis is $I_{d} = \dfrac{1}{4}MR^2$.

Using the parallel axis theorem, the moment of inertia of the disc about a tangential axis in its plane is $I_{1} = I_{d} + MR^2 = \dfrac{1}{4}MR^2 + MR^2 = \dfrac{5}{4}MR^2$.

Radius of gyration of the disc is $K_{1} = \sqrt{\dfrac{I_{1}}{M}} = \sqrt{\dfrac{5}{4}}R = \dfrac{\sqrt{5}}{2}R$.

Moment of inertia of a circular ring about a diametric axis is $I_{r} = \dfrac{1}{2}MR^2$.

Using the parallel axis theorem, the moment of inertia of the ring about a tangential axis in its plane is $I_{2} = I_{r} + MR^2 = \dfrac{1}{2}MR^2 + MR^2 = \dfrac{3}{2}MR^2$.

Radius of gyration of the ring is $K_{2} = \sqrt{\dfrac{I_{2}}{M}} = \sqrt{\dfrac{3}{2}}R = \dfrac{\sqrt{3}}{\sqrt{2}}R$.

The required ratio is $\dfrac{K_{1}}{K_{2}} = \dfrac{\dfrac{\sqrt{5}}{2}R}{\dfrac{\sqrt{3}}{\sqrt{2}}R} = \dfrac{\sqrt{5}}{2} \times \dfrac{\sqrt{2}}{\sqrt{3}} = \dfrac{\sqrt{5}}{\sqrt{6}}$.

Answer: $\sqrt{5} : \sqrt{6}$

</details>

---

### Q12. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The moment of inertia of two equal masses each of mass m at separation L connected by a rod of mass M about an axis passing through centre and perpendicular to the length of rod is
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/13_may_shift_1__q49_d1.png" />

**Options:**

- **(A)** $\dfrac{(M+3m)L^2}{12}$
- **(B)** $\dfrac{(M+6m)L^2}{12}$
- **(C)** $\dfrac{ML^2}{4}$
- **(D)** $\dfrac{ML^2}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{(M+6m)L^2}{12}$**

**Detailed Solution:**

The total moment of inertia of the system about the axis $XX'$ is the sum of the moment of inertia of the rod and the moment of inertia of the two point masses.

Moment of inertia of the uniform rod of mass $M$ and length $L$ about an axis passing through its centre and perpendicular to its length is:
$I_{\text{rod}} = \dfrac{ML^2}{12}$

The two point masses, each of mass $m$, are located at the ends of the rod, which is at a distance of $L/2$ from the axis of rotation.
Moment of inertia of the two point masses is:
$I_{\text{masses}} = m\left(\dfrac{L}{2}\right)^2 + m\left(\dfrac{L}{2}\right)^2 = 2m\left(\dfrac{L^2}{4}\right) = \dfrac{mL^2}{2}$

Total moment of inertia $I$ is:
$I = I_{\text{rod}} + I_{\text{masses}}$

$I = \dfrac{ML^2}{12} + \dfrac{mL^2}{2}$

$I = \dfrac{ML^2 + 6mL^2}{12}$

$I = \dfrac{(M + 6m)L^2}{12}$

Answer: $\dfrac{(M+6m)L^2}{12}$

</details>

---

### Q13. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Moment of inertia of a thin uniform rod rotating about the perpendicular axis passing through its centre is I. If the same rod is bent in to a ring and its moment of inertia about its diameter is $I_1$, then the ratio $I / I_1$ is

**Options:**

- **(A)** $\dfrac{2\pi^2}{3}$
- **(B)** $\dfrac{3\pi^2}{2}$
- **(C)** $\dfrac{5\pi^2}{3}$
- **(D)** $\dfrac{8\pi^2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{2\pi^2}{3}$**

**Detailed Solution:**

Let the mass of the rod be $M$ and its length be $L$.

The moment of inertia of the rod about a perpendicular axis passing through its centre is:
$I = \dfrac{ML^2}{12}$

When the rod is bent into a ring, its length becomes the circumference of the ring. Let the radius of the ring be $R$.
$L = 2\pi R \Rightarrow R = \dfrac{L}{2\pi}$

The moment of inertia of the ring about its diameter is:
$I_1 = \dfrac{MR^2}{2}$

Substituting the value of $R$:
$I_1 = \dfrac{M}{2} \left( \dfrac{L}{2\pi} \right)^2 = \dfrac{ML^2}{8\pi^2}$

The ratio of the moments of inertia is:
$\dfrac{I}{I_1} = \dfrac{\dfrac{ML^2}{12}}{\dfrac{ML^2}{8\pi^2}} = \dfrac{8\pi^2}{12} = \dfrac{2\pi^2}{3}$

Answer: $\dfrac{2\pi^2}{3}$

</details>

---

### Q14. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A disc of mass $100$ kg and radius $1$m is rotating at $300$ r.p.m. The torque required to rotate the disc in opposite direction with same speed in time $50$ second is

**Options:**

- **(A)** $5\pi\,Nm$
- **(B)** $10\pi\,Nm$
- **(C)** $20\pi\,Nm$
- **(D)** $40\pi\,Nm$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $20\pi\,Nm$**

**Detailed Solution:**

Initial angular velocity $\omega_0 = \dfrac{300 \times 2\pi}{60} = 10\pi$ rad/s.

Final angular velocity $\omega = -10\pi$ rad/s.

Time $t = 50$ s.

Angular acceleration $\alpha = \dfrac{\omega - \omega_0}{t} = \dfrac{-10\pi - 10\pi}{50} = -0.4\pi$ rad/s$^2$.

Moment of inertia of the disc $I = \dfrac{1}{2}MR^2 = \dfrac{1}{2} \times 100 \times (1)^2 = 50$ kg m$^2$.

Magnitude of torque $\tau = |I\alpha| = 50 \times 0.4\pi = 20\pi$ Nm.

Answer: $20\pi\,Nm$

</details>

---

### Q15. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two loops $A$ and $B$ of radii $R_1$ and $R_2$ are made from uniform wire. If moment of inertia of loops $A$ and $B$ is $I_A$ and $I_B$ respectively then $\dfrac{R_1}{R_2}$ is (Given: $\dfrac{I_A}{I_B} = 27$)

**Options:**

- **(A)** $9:1$
- **(B)** $27:1$
- **(C)** $81:1$
- **(D)** $3:1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3:1$**

**Detailed Solution:**

Let the linear mass density of the uniform wire be \lambda.

The mass of loop A is M_A = \lambda (2\pi R_1) and the mass of loop B is M_B = \lambda (2\pi R_2).

The moment of inertia of a circular loop of mass M and radius R about its central axis is I = MR^2.

For loop A, I_A = M_A R_1^2 = \lambda (2\pi R_1) R_1^2 = 2\pi \lambda R_1^3.

For loop B, I_B = M_B R_2^2 = \lambda (2\pi R_2) R_2^2 = 2\pi \lambda R_2^3.

Taking the ratio of their moments of inertia:

\dfrac{I_A}{I_B} = \dfrac{2\pi \lambda R_1^3}{2\pi \lambda R_2^3} = \left(\dfrac{R_1}{R_2}\right)^3

Given that \dfrac{I_A}{I_B} = 27, we have:

\left(\dfrac{R_1}{R_2}\right)^3 = 27

\dfrac{R_1}{R_2} = 3

The ratio \dfrac{R_1}{R_2} is 3:1.

Answer: $3:1$

</details>

---

### Q16. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Four solid spheres, each of diameter $\sqrt{5}$ cm and mass $0.5$ kg are placed with their centres at the corners of a square of side $4$ cm. The M.I. of the system about the diagonal of the square is $N\times 10^{-4}$ kg-m$^2$, then $N$ is

**Options:**

- **(A)** $9$
- **(B)** $7$
- **(C)** $5$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $9$**

**Detailed Solution:**

Mass of each sphere, $M = 0.5$ kg

Radius of each sphere, $R = \dfrac{\sqrt{5}}{2}$ cm $= \dfrac{\sqrt{5}}{2} \times 10^{-2}$ m

Side of the square, $a = 4$ cm $= 4 \times 10^{-2}$ m

The diagonal of the square passes through the centres of two spheres. The perpendicular distance of the centres of the other two spheres from this diagonal is $r = \dfrac{a}{\sqrt{2}} = \dfrac{4}{\sqrt{2}} = 2\sqrt{2}$ cm $= 2\sqrt{2} \times 10^{-2}$ m.

The moment of inertia of the system about the diagonal is the sum of the moments of inertia of all four spheres. Using the parallel axis theorem for the two spheres not on the diagonal:

$I = 2 \times \left( \dfrac{2}{5} M R^2 \right) + 2 \times \left( \dfrac{2}{5} M R^2 + M r^2 \right)$

$I = \dfrac{8}{5} M R^2 + 2 M r^2$

Substituting the given values:

$I = \dfrac{8}{5} \times 0.5 \times \left( \dfrac{\sqrt{5}}{2} \times 10^{-2} \right)^2 + 2 \times 0.5 \times \left( 2\sqrt{2} \times 10^{-2} \right)^2$

$I = \dfrac{8}{5} \times \dfrac{1}{2} \times \dfrac{5}{4} \times 10^{-4} + 1 \times 8 \times 10^{-4}$

$I = 1 \times 10^{-4} + 8 \times 10^{-4}$

$I = 9 \times 10^{-4}$ kg-m$^2$

Comparing this with $N \times 10^{-4}$ kg-m$^2$, we get $N = 9$.

Answer: $9$

</details>

---

### Q17. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A solid sphere of mass 5 kg and a disc of mass 4 kg have the same radius. The ratio of moment of inertia of the sphere about its tangent to the moment of inertia of the disc about a tangent in its plane will be $x : y$. The value of $x$ and $y$ respectively is

**Options:**

- **(A)** $5, 8$
- **(B)** $6, 7$
- **(C)** $7, 5$
- **(D)** $4, 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $7, 5$**

**Detailed Solution:**

Mass of the solid sphere, $M_s = 5$ kg
Mass of the disc, $M_d = 4$ kg
Let the radius of both the sphere and the disc be $R$.

The moment of inertia of a solid sphere about its tangent is obtained using the parallel axis theorem:
$I_s = I_{cm} + M_s R^2 = \dfrac{2}{5} M_s R^2 + M_s R^2 = \dfrac{7}{5} M_s R^2$
Substituting $M_s = 5$ kg:
$I_s = \dfrac{7}{5} \times 5 \times R^2 = 7 R^2$

The moment of inertia of a disc about a tangent in its plane is also obtained using the parallel axis theorem (shifting from the diameter):
$I_d = I_{diameter} + M_d R^2 = \dfrac{1}{4} M_d R^2 + M_d R^2 = \dfrac{5}{4} M_d R^2$
Substituting $M_d = 4$ kg:
$I_d = \dfrac{5}{4} \times 4 \times R^2 = 5 R^2$

The ratio of their moments of inertia is:
$\dfrac{I_s}{I_d} = \dfrac{7 R^2}{5 R^2} = \dfrac{7}{5}$

Comparing this with $x : y$, we get $x = 7$ and $y = 5$.

Answer: $7, 5$

</details>

---

### Q18. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two identical rings A and B of same mass and radius are revolving, ring A arounds its own diameter and ring B about tangential axis in its own plane. Both the rings A and B have same rotational kinetic energy. The ratio of the angular velocity of ring B to that of ring A is

**Options:**

- **(A)** $1 : 3$
- **(B)** $1 : \sqrt{3}$
- **(C)** $3 : 2$
- **(D)** $\sqrt{3} : 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1 : \sqrt{3}$**

**Detailed Solution:**

Moment of inertia of ring A about its diameter is $I_A = \dfrac{1}{2}MR^2$.

Moment of inertia of ring B about a tangential axis in its own plane is obtained using the parallel axis theorem:
$I_B = I_A + MR^2 = \dfrac{1}{2}MR^2 + MR^2 = \dfrac{3}{2}MR^2$.

Rotational kinetic energy is given by $K = \dfrac{1}{2}I\omega^2$.

Given that both rings have the same rotational kinetic energy, $K_A = K_B$:
$\dfrac{1}{2}I_A\omega_A^2 = \dfrac{1}{2}I_B\omega_B^2$

$\dfrac{\omega_B^2}{\omega_A^2} = \dfrac{I_A}{I_B}$

$\dfrac{\omega_B}{\omega_A} = \sqrt{\dfrac{\dfrac{1}{2}MR^2}{\dfrac{3}{2}MR^2}} = \sqrt{\dfrac{1}{3}} = \dfrac{1}{\sqrt{3}}$

The ratio of the angular velocity of ring B to that of ring A is $1 : \sqrt{3}$.

Answer: $1 : \sqrt{3}$

</details>

---

### Q19. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A thin uniform rod AB of mass '$m$' and length '$l$' is hinged at one end A to the ground level. Initially the rod stands vertically and is allowed to fall freely to the ground in the vertical plane. The angular velocity of the rod when its B end strikes the ground is
($g$ = acceleration due to gravity)

**Options:**

- **(A)** $\sqrt{\dfrac{2g}{l}}$
- **(B)** $\sqrt{\dfrac{3g}{l}}$
- **(C)** $\sqrt{\dfrac{mg}{l}}$
- **(D)** $\sqrt{\dfrac{mg}{3l}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{\dfrac{3g}{l}}$**

**Detailed Solution:**

By the principle of conservation of mechanical energy, the loss in potential energy of the rod is equal to the gain in its rotational kinetic energy.

The initial height of the center of mass of the rod is $h_i = \dfrac{l}{2}$ and the final height is $h_f = 0$.

Loss in potential energy $= mg\left(\dfrac{l}{2}\right)$

Gain in rotational kinetic energy $= \dfrac{1}{2}I\omega^2$

The moment of inertia of the rod about the hinged end A is $I = \dfrac{ml^2}{3}$.

Equating the two energies:

$mg\left(\dfrac{l}{2}\right) = \dfrac{1}{2}\left(\dfrac{ml^2}{3}\right)\omega^2$

$mgl = \dfrac{ml^2}{3}\omega^2$

$\omega^2 = \dfrac{3g}{l}$

$\omega = \sqrt{\dfrac{3g}{l}}$

Answer: $\sqrt{\dfrac{3g}{l}}$

</details>

---

### Q20. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The radius of gyration of a solid sphere of radius 'R' and mass 'M' about its diameter is $K_d$ and that about a tangent of a solid sphere is $K_t$. The ratio of $K_d$ to $K_t$ is

**Options:**

- **(A)** $\left(\dfrac{7}{5}\right)^{1/2}$
- **(B)** $\left(\dfrac{7}{2}\right)^{1/2}$
- **(C)** $\left(\dfrac{2}{7}\right)^{1/2}$
- **(D)** $\left(\dfrac{2}{5}\right)^{1/2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(\dfrac{2}{7}\right)^{1/2}$**

**Detailed Solution:**

The moment of inertia of a solid sphere about its diameter is $I_d = \dfrac{2}{5}MR^2$.

The radius of gyration about the diameter is $K_d = \sqrt{\dfrac{2}{5}}R$.

Using the parallel axis theorem, the moment of inertia of the solid sphere about a tangent is $I_t = I_d + MR^2 = \dfrac{2}{5}MR^2 + MR^2 = \dfrac{7}{5}MR^2$.

The radius of gyration about the tangent is $K_t = \sqrt{\dfrac{7}{5}}R$.

The ratio of $K_d$ to $K_t$ is $\dfrac{K_d}{K_t} = \dfrac{\sqrt{\dfrac{2}{5}}R}{\sqrt{\dfrac{7}{5}}R} = \left(\dfrac{2}{7}\right)^{1/2}$.

Answer: $\left(\dfrac{2}{7}\right)^{1/2}$

</details>

---

### Q21. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given identical rings are arranged in a hexagonal plane pattern so as to touch each neighbouring ring as shown in figure. Each ring has mass M and radius R. The moment of inertia of the system of seven rings about an axis passing through the centre of central ring and normal to plane of all rings is
<img style="width: 180px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/17_april_shift_2__q13_d1.png" />

**Options:**

- **(A)** $31MR^2$
- **(B)** $19MR^2$
- **(C)** $11MR^2$
- **(D)** $7MR^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $31MR^2$**

**Detailed Solution:**

The moment of inertia of the central ring about the axis passing through its centre and perpendicular to its plane is:

$I_0 = MR^2$

For each of the six surrounding rings, the distance from its centre to the central axis is $d = 2R$.

Using the parallel axis theorem, the moment of inertia of one surrounding ring about the central axis is:

$I_1 = I_{cm} + Md^2$

$I_1 = MR^2 + M(2R)^2$

$I_1 = MR^2 + 4MR^2 = 5MR^2$

Since there are six identical surrounding rings, their total moment of inertia about the central axis is:

$I_{surrounding} = 6 \times I_1 = 6 \times 5MR^2 = 30MR^2$

The total moment of inertia of the system of seven rings is the sum of the moment of inertia of the central ring and the surrounding rings:

$I_{total} = I_0 + I_{surrounding}$

$I_{total} = MR^2 + 30MR^2 = 31MR^2$

Answer: $31MR^2$

</details>

---

### Q22. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The radius of gyration K of a hollow sphere of mass M and radius R about an axis XY is equal to R as shown in figure. The distance of that axis from the center of the sphere is h. The value of h is
<img style="width: 150px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/17_april_shift_1__q6_d1.png" />

**Options:**

- **(A)** $\dfrac{R}{\sqrt{3}}$
- **(B)** $\dfrac{R}{2}$
- **(C)** $\dfrac{R}{\sqrt{2}}$
- **(D)** $\dfrac{2R}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{R}{\sqrt{3}}$**

**Detailed Solution:**

The moment of inertia of a hollow sphere about an axis passing through its center is given by:

$I_{CM} = \dfrac{2}{3}MR^2$

Using the parallel axis theorem, the moment of inertia about the axis $XY$ at a distance $h$ from the center is:

$I_{XY} = I_{CM} + Mh^2$

$I_{XY} = \dfrac{2}{3}MR^2 + Mh^2$

The radius of gyration $K$ about the axis $XY$ is given as $R$. Therefore, the moment of inertia can also be written as:

$I_{XY} = MK^2 = MR^2$

Equating the two expressions for $I_{XY}$:

$MR^2 = \dfrac{2}{3}MR^2 + Mh^2$

$h^2 = R^2 - \dfrac{2}{3}R^2$

$h^2 = \dfrac{1}{3}R^2$

$h = \dfrac{R}{\sqrt{3}}$

Answer: $\dfrac{R}{\sqrt{3}}$

</details>

---

### Q23. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Radius of gyration of a thin uniform circular disc about the axis passing through its centre and perpendicular to its plane is $K_c$. Radius of gyration of the same disc about a diamter of the disc is $K_d$. the ratio $K_d : K_c$ is

**Options:**

- **(A)** $1 : 4$
- **(B)** $1 : \sqrt{2}$
- **(C)** $\sqrt{2} : 1$
- **(D)** $2 : 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1 : \sqrt{2}$**

**Detailed Solution:**

Moment of inertia of a uniform circular disc about an axis passing through its centre and perpendicular to its plane is $I_c = \dfrac{1}{2}MR^2$.

Radius of gyration $K_c = \sqrt{\dfrac{I_c}{M}} = \dfrac{R}{\sqrt{2}}$.

Moment of inertia of the disc about its diameter is $I_d = \dfrac{1}{4}MR^2$.

Radius of gyration $K_d = \sqrt{\dfrac{I_d}{M}} = \dfrac{R}{2}$.

Ratio $\dfrac{K_d}{K_c} = \dfrac{\dfrac{R}{2}}{\dfrac{R}{\sqrt{2}}} = \dfrac{1}{\sqrt{2}}$.

Thus, $K_d : K_c = 1 : \sqrt{2}$.

Answer: $1 : \sqrt{2}$

</details>

---

### Q24. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A solid sphere of radius R and mass M is rotating about its diameter. The moment of intertia of the solid sphere rotating about an axis at a distance $\dfrac{R}{3}$ from the centre and parallel to that diameter is

**Options:**

- **(A)** $\dfrac{11}{15}MR^2$
- **(B)** $\dfrac{13}{20}MR^2$
- **(C)** $\dfrac{23}{45}MR^2$
- **(D)** $\dfrac{47}{45}MR^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{23}{45}MR^2$**

**Detailed Solution:**

The moment of inertia of a solid sphere of mass $M$ and radius $R$ about its diameter (an axis passing through its centre) is given by:

$I_{cm} = \dfrac{2}{5}MR^2$

Using the parallel axis theorem, the moment of inertia $I$ about an axis parallel to the diameter and at a distance $d = \dfrac{R}{3}$ from the centre is:

$I = I_{cm} + Md^2$

Substituting the values:

$I = \dfrac{2}{5}MR^2 + M\left(\dfrac{R}{3}\right)^2$

$I = \dfrac{2}{5}MR^2 + \dfrac{1}{9}MR^2$

$I = \left(\dfrac{18 + 5}{45}\right)MR^2$

$I = \dfrac{23}{45}MR^2$

</details>

---

### Q25. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Four point masses m, 2m, 3m and 4m are kept at the corners A, B, C and D respectively of a square ABCD of side '$b$'. The moment of inertia of the system about an axis perpendicular to the plane of the square and passing through the point D is

**Options:**

- **(A)** $12\ mb^2$
- **(B)** $10\ mb^2$
- **(C)** $8\ mb^2$
- **(D)** $5\ mb^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $8\ mb^2$**

**Detailed Solution:**

The moment of inertia of a system of point masses is given by $I = \sum m_i r_i^2$, where $r_i$ is the perpendicular distance of the $i$-th mass from the axis of rotation.

The axis of rotation is perpendicular to the plane of the square and passes through point D. The distances of the masses from the axis are:

For mass at A ($m_A = m$): $r_A = b$

For mass at B ($m_B = 2m$): $r_B = b\sqrt{2}$ (diagonal of the square)

For mass at C ($m_C = 3m$): $r_C = b$

For mass at D ($m_D = 4m$): $r_D = 0$

Substituting these values into the formula:

$I = m(b)^2 + 2m(b\sqrt{2})^2 + 3m(b)^2 + 4m(0)^2$

$I = mb^2 + 2m(2b^2) + 3mb^2 + 0$

$I = mb^2 + 4mb^2 + 3mb^2 = 8mb^2$

Answer: $8\ mb^2$

</details>

---

### Q26. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A system of five solid spheres each of mass '$m$' and radius '$r$' are rotating about an axis AA' as shown in figure. Hence the moment of inertia of the system about the axis of rotation AA' is
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/16_april_shift_1__q12_d1.png" />

**Options:**

- **(A)** $6\ mr^2$
- **(B)** $5\ mr^2$
- **(C)** $4\ mr^2$
- **(D)** $3\ mr^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4\ mr^2$**

**Detailed Solution:**

The system consists of $5$ solid spheres, each of mass $m$ and radius $r$.

From the given figure, the axis of rotation AA' passes through the centers of $3$ spheres (one at the top and two at the bottom).

The moment of inertia of a solid sphere about an axis passing through its center is $I_{cm} = \dfrac{2}{5}mr^2$.

Total moment of inertia for these $3$ spheres is:

$I_1 = 3 \times \dfrac{2}{5}mr^2 = \dfrac{6}{5}mr^2$

The remaining $2$ spheres are placed such that they touch each other, and the axis AA' passes through their point of contact. Thus, the distance of their centers from the axis AA' is $r$.

Using the parallel axis theorem, the moment of inertia of one such sphere about the axis AA' is:

$I_{off} = I_{cm} + mr^2 = \dfrac{2}{5}mr^2 + mr^2 = \dfrac{7}{5}mr^2$

Total moment of inertia for these $2$ spheres is:

$I_2 = 2 \times \dfrac{7}{5}mr^2 = \dfrac{14}{5}mr^2$

The total moment of inertia of the system about the axis AA' is the sum of the moments of inertia of all $5$ spheres:

$I = I_1 + I_2 = \dfrac{6}{5}mr^2 + \dfrac{14}{5}mr^2 = \dfrac{20}{5}mr^2 = 4mr^2$

Answer: $4\ mr^2$

</details>

---

### Q27. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A solid sphere of mass M and a disc of mass $\dfrac{M}{2}$ have the same radius. The ratio of moment of inertia of the disc about a tangent in its plane to the moment of inertia of the sphere about its tangent will be

**Options:**

- **(A)** $15 : 8$
- **(B)** $25 : 56$
- **(C)** $12 : 7$
- **(D)** $16 : 9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $25 : 56$**

**Detailed Solution:**

Let the radius of the solid sphere and the disc be $R$.

Mass of the solid sphere, $m_{s} = M$

Mass of the disc, $m_{d} = \dfrac{M}{2}$

Moment of inertia of the disc about its diameter is $\dfrac{1}{4}m_{d}R^2$. Using the parallel axis theorem, the moment of inertia of the disc about a tangent in its plane is:

$I_{disc} = \dfrac{1}{4}m_{d}R^2 + m_{d}R^2 = \dfrac{5}{4}m_{d}R^2$

Substituting $m_{d} = \dfrac{M}{2}$:

$I_{disc} = \dfrac{5}{4}\left(\dfrac{M}{2}\right)R^2 = \dfrac{5}{8}MR^2$

Moment of inertia of the solid sphere about its diameter is $\dfrac{2}{5}m_{s}R^2$. Using the parallel axis theorem, the moment of inertia of the solid sphere about its tangent is:

$I_{sphere} = \dfrac{2}{5}m_{s}R^2 + m_{s}R^2 = \dfrac{7}{5}m_{s}R^2$

Substituting $m_{s} = M$:

$I_{sphere} = \dfrac{7}{5}MR^2$

The required ratio is:

$\dfrac{I_{disc}}{I_{sphere}} = \dfrac{\dfrac{5}{8}MR^2}{\dfrac{7}{5}MR^2} = \dfrac{5}{8} \times \dfrac{5}{7} = \dfrac{25}{56}$

Answer: $25 : 56$

</details>

---

### Q28. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A uniform solid cylinder with radius R and length L has moment of inertia $I_1$ about the axis of the cylinder. A concentric solid cylinder of radius $R/2$ and length $L/2$ is carved out of the original cylinder. If $I_2$ is the moment of inertia of the carved out portion of the cylinder then $I_1/I_2$ is (Both $I_1$ and $I_2$ are about the axis of the cylinder)

**Options:**

- **(A)** $4 : 1$
- **(B)** $8 : 1$
- **(C)** $16 : 1$
- **(D)** $32 : 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $32 : 1$**

**Detailed Solution:**

Let the density of the material of the cylinder be $\rho$.

The mass of the original solid cylinder is $M_1 = \rho \pi R^2 L$.
The moment of inertia of the original solid cylinder about its axis is:
$I_1 = \dfrac{1}{2} M_1 R^2 = \dfrac{1}{2} (\rho \pi R^2 L) R^2 = \dfrac{1}{2} \rho \pi R^4 L$

The carved out portion is a solid cylinder of radius $R/2$ and length $L/2$. Its mass is:
$M_2 = \rho \pi \left(\dfrac{R}{2}\right)^2 \left(\dfrac{L}{2}\right) = \dfrac{1}{8} \rho \pi R^2 L$

The moment of inertia of this carved out portion about the same axis is:
$I_2 = \dfrac{1}{2} M_2 \left(\dfrac{R}{2}\right)^2 = \dfrac{1}{2} \left(\dfrac{1}{8} \rho \pi R^2 L\right) \left(\dfrac{R^2}{4}\right) = \dfrac{1}{64} \rho \pi R^4 L$

Taking the ratio of $I_1$ to $I_2$:
$\dfrac{I_1}{I_2} = \dfrac{\dfrac{1}{2} \rho \pi R^4 L}{\dfrac{1}{64} \rho \pi R^4 L} = 32$

Thus, the ratio is $32 : 1$.

</details>

---

### Q29. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Solid sphere is rotating about an axis as shown in figure. If the radius of the sphere is 5 cm, then radius of gyration about that axis will be $\sqrt{x}$ cm. The value of x is
<img style="width: 150px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/15_april_shift_2__q3_d1.png" />

**Options:**

- **(A)** $100$
- **(B)** $110$
- **(C)** $120$
- **(D)** $140$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $110$**

**Detailed Solution:**

The moment of inertia of a solid sphere about an axis passing through its center of mass is given by $I_{cm} = \dfrac{2}{5}MR^2$.

Using the parallel axis theorem, the moment of inertia about the given axis of rotation is:

$I = I_{cm} + Md^2$

where $d$ is the distance from the axis of rotation to the center of mass of the sphere.

Given $R = 5$ cm and $d = 10$ cm, we have:

$I = \dfrac{2}{5}M(5)^2 + M(10)^2$

$I = 10M + 100M = 110M$

The radius of gyration $k$ is defined by $I = Mk^2$.

$Mk^2 = 110M$

$k^2 = 110$

$k = \sqrt{110}$ cm

Comparing this with $\sqrt{x}$ cm, we get $x = 110$.

</details>

---

### Q30. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A Solid sphere has mass M and radius R. Its moment of inertia about a parallel axis passing through a point at a distance R/3 from its centre is

**Options:**

- **(A)** $8\text{MR}^2/11$
- **(B)** $11\text{MR}^2/15$
- **(C)** $23\text{MR}^2/45$
- **(D)** $13\text{MR}^2/20$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $23\text{MR}^2/45$**

**Detailed Solution:**

The moment of inertia of a solid sphere about an axis passing through its centre is $I_{cm} = \dfrac{2}{5}MR^2$.

Using the parallel axis theorem, the moment of inertia about a parallel axis at a distance $d$ from the centre is given by $I = I_{cm} + Md^2$.

Given $d = \dfrac{R}{3}$, substituting the values:

$I = \dfrac{2}{5}MR^2 + M\left(\dfrac{R}{3}\right)^2$

$I = \dfrac{2}{5}MR^2 + \dfrac{1}{9}MR^2$

$I = \left(\dfrac{18 + 5}{45}\right)MR^2$

$I = \dfrac{23}{45}MR^2$

Answer: $23\text{MR}^2/45$

</details>

---

### Q31. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Moment of inertia of a disc of mass $M$ and radius 'R' about any of its diameter is $MR^2/4$. The moment of inertia of this disc about an axis normal to the disc and passing through a point on its edge will be, $(x/2) MR^2$. The value of $x$ is

**Options:**

- **(A)** $1$
- **(B)** $3$
- **(C)** $5$
- **(D)** $7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3$**

**Detailed Solution:**

Given the moment of inertia of the disc about its diameter is $I_{d} = \dfrac{MR^2}{4}$.

By the perpendicular axis theorem, the moment of inertia of the disc about an axis passing through its center and perpendicular to its plane is $I_{c} = I_{d} + I_{d} = \dfrac{MR^2}{4} + \dfrac{MR^2}{4} = \dfrac{MR^2}{2}$.

By the parallel axis theorem, the moment of inertia of the disc about an axis perpendicular to its plane and passing through a point on its edge is $I = I_{c} + MR^2$.

Substituting the value of $I_{c}$, we get $I = \dfrac{MR^2}{2} + MR^2 = \dfrac{3}{2}MR^2$.

Comparing this with the given expression $\dfrac{x}{2}MR^2$, we get $x = 3$.

Answer: $3$

</details>

---

### Q32. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A thin uniform rod of length $2$ m cross-sectional area 'A' and density 'd' is rotated about an axis passing through the centre and perpendicular to its length with angular velocity $\omega$. If the value of $\omega$ in terms of its rotational kinetic energy $E$ is $(\alpha E/Ad)^{1/2}$, then the value of $\alpha$ is

**Options:**

- **(A)** $2$
- **(B)** $3$
- **(C)** $4$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3$**

**Detailed Solution:**

Mass of the rod, $M = \text{Volume} \times \text{density} = A \times L \times d$

Given $L = 2$, $M = 2Ad$

Moment of inertia of the rod about an axis passing through its centre and perpendicular to its length is $I = \dfrac{ML^2}{12}$

Substituting the values of $M$ and $L$, we get $I = \dfrac{2Ad \times 2^2}{12} = \dfrac{2Ad}{3}$

Rotational kinetic energy is given by $E = \dfrac{1}{2}I\omega^2$

Substituting the value of $I$, $E = \dfrac{1}{2} \left( \dfrac{2Ad}{3} \right) \omega^2 = \dfrac{Ad}{3} \omega^2$

Rearranging for $\omega$, we get $\omega = \left( \dfrac{3E}{Ad} \right)^{1/2}$

Comparing this with the given expression $\omega = \left( \dfrac{\alpha E}{Ad} \right)^{1/2}$, we find $\alpha = 3$.

Answer: $3$

</details>

---

### Q33. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A disc of radius 0.4 m and mass 1 kg rotates about an axis passing through its centre and perpendicular to its plane. The angular acceleration is 10 rad/s$^2$. The tangential force applied to the rim of the disc is

**Options:**

- **(A)** $1$ N
- **(B)** $2$ N
- **(C)** $3$ N
- **(D)** $4$ N

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$ N**

**Detailed Solution:**

The moment of inertia of a disc about an axis passing through its centre and perpendicular to its plane is given by

$I = \dfrac{1}{2}MR^2$

The torque acting on the disc is related to the angular acceleration by

$\tau = I\alpha$

Since the torque is provided by a tangential force $F$ applied at the rim, we have

$\tau = F \times R$

Equating the two expressions for torque:

$F \times R = \dfrac{1}{2}MR^2\alpha$

$F = \dfrac{1}{2}MR\alpha$

Substituting the given values ($M = 1$ kg, $R = 0.4$ m, $\alpha = 10$ rad/s$^2$):

$F = \dfrac{1}{2} \times 1 \times 0.4 \times 10$

$F = 2$ N

Answer: $2$ N

</details>

---

### Q34. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The moment of inertia of a ring about an axis passing through its centre and perpendicular to its plane is I. It is rotating with angular velocity $\omega$. Another identical ring is gently placed on it so that their centres coincide. If both rings are rotating about the same axis then loss in kinetic energy is

**Options:**

- **(A)** $I\omega^2$
- **(B)** $\dfrac{I\omega^2}{2}$
- **(C)** $\dfrac{I\omega^2}{4}$
- **(D)** $\dfrac{I\omega^2}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{I\omega^2}{4}$**

**Detailed Solution:**

Initial angular momentum of the system is $L_i = I\omega$

Initial kinetic energy is $K_i = \dfrac{1}{2}I\omega^2$

When an identical ring is placed on it, the new moment of inertia becomes $I_f = I + I = 2I$

By conservation of angular momentum, $I_f\omega_f = I_i\omega_i$

$2I\omega_f = I\omega \Rightarrow \omega_f = \dfrac{\omega}{2}$

Final kinetic energy is $K_f = \dfrac{1}{2}(2I)\left(\dfrac{\omega}{2}\right)^2 = \dfrac{1}{4}I\omega^2$

Loss in kinetic energy is $\Delta K = K_i - K_f = \dfrac{1}{2}I\omega^2 - \dfrac{1}{4}I\omega^2 = \dfrac{I\omega^2}{4}$

Answer: $\dfrac{I\omega^2}{4}$

</details>

---

### Q35. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let M and L be the mass and length of thin uniform rod respectively. In first case, axis of rotation is passing through centre and perpendicular to length of rod. In second case axis of rotation is passing through one end and perpendicular to length of rod. The ratio of radius of gyration in first case to second case is

**Options:**

- **(A)** $\dfrac{1}{4}$
- **(B)** $\dfrac{1}{2}$
- **(C)** $\dfrac{1}{8}$
- **(D)** $\dfrac{1}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{2}$**

**Detailed Solution:**

Moment of inertia of a thin uniform rod about an axis passing through its centre and perpendicular to its length is $I_1 = \dfrac{ML^2}{12}$.

Radius of gyration in the first case is $K_1 = \sqrt{\dfrac{I_1}{M}} = \dfrac{L}{\sqrt{12}}$.

Moment of inertia of the rod about an axis passing through one end and perpendicular to its length is $I_2 = \dfrac{ML^2}{3}$.

Radius of gyration in the second case is $K_2 = \sqrt{\dfrac{I_2}{M}} = \dfrac{L}{\sqrt{3}}$.

The ratio of radius of gyration in the first case to the second case is $\dfrac{K_1}{K_2} = \dfrac{\dfrac{L}{\sqrt{12}}}{\dfrac{L}{\sqrt{3}}} = \sqrt{\dfrac{3}{12}} = \sqrt{\dfrac{1}{4}} = \dfrac{1}{2}$.

</details>

---

### Q36. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The moment of inertia of a thin uniform rod of mass ' $M$ ' and length ' $L$ ', about an axis perpendicular to length of the rod and at a distance ' $\mathrm{L} / 4$ ' from one end is

**Options:**

- **(A)** $\frac{\mathrm{ML}^2}{6}$
- **(B)** $\frac{\mathrm{ML}^2}{12}$
- **(C)** $\frac{7 \mathrm{ML}^2}{24}$
- **(D)** $\frac{7 \mathrm{ML}^2}{48}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{7 \mathrm{ML}^2}{48}$**

**Detailed Solution:**

The moment of inertia of a thin uniform rod about an axis passing through its centre of mass and perpendicular to its length is given by:

$I_{cm} = \dfrac{ML^2}{12}$

The centre of mass is at a distance of $\dfrac{L}{2}$ from either end. The given axis is at a distance of $\dfrac{L}{4}$ from one end. The perpendicular distance $h$ between the parallel axes is:

$h = \dfrac{L}{2} - \dfrac{L}{4} = \dfrac{L}{4}$

Using the theorem of parallel axes, the moment of inertia about the given axis is:

$I = I_{cm} + Mh^2$

$I = \dfrac{ML^2}{12} + M\left(\dfrac{L}{4}\right)^2$

$I = \dfrac{ML^2}{12} + \dfrac{ML^2}{16}$

$I = \dfrac{4ML^2 + 3ML^2}{48} = \dfrac{7ML^2}{48}$

Answer: $\frac{7 \mathrm{ML}^2}{48}$

</details>

---

### Q37. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A thin wire of length ' $L$ ' and uniform linear mass density ' $\lambda$ ' is bent into a circular ring. The moment of inertia of ring about a tangential axis in its plane is

**Options:**

- **(A)** $\frac{3 \lambda L^3}{8 \pi^2}$
- **(B)** $\frac{3 \lambda L^2}{8 \pi^2}$
- **(C)** $\frac{8 \pi^2}{3 \lambda L^3}$
- **(D)** $\frac{8 \pi^2}{3 \lambda L^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3 \lambda L^3}{8 \pi^2}$**

**Detailed Solution:**

Mass of the ring, $M = \lambda L$

Length of the wire is equal to the circumference of the ring, so $L = 2 \pi R \Rightarrow R = \dfrac{L}{2 \pi}$

Moment of inertia of the ring about its diametric axis is $I_d = \dfrac{1}{2} M R^2$

Using the theorem of parallel axes, the moment of inertia about a tangential axis in its plane is $I_t = I_d + M R^2 = \dfrac{1}{2} M R^2 + M R^2 = \dfrac{3}{2} M R^2$

Substituting the values of $M$ and $R$:

$I_t = \dfrac{3}{2} (\lambda L) \left( \dfrac{L}{2 \pi} \right)^2$

$I_t = \dfrac{3}{2} \lambda L \left( \dfrac{L^2}{4 \pi^2} \right) = \dfrac{3 \lambda L^3}{8 \pi^2}$

Answer: $\frac{3 \lambda L^3}{8 \pi^2}$

</details>

---

### Q38. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Four particles each of mass ' m ' are lying symmetrically on the rim of disc of mass ' $M$ ' and radius ' $R$ '. Moment of inertia of the system about an axis passing through one of the particle and perpendicular to plane of disc is

**Options:**

- **(A)** $(3 \mathrm{M}+16 \mathrm{~m}) \frac{\mathrm{R}^2}{2}$
- **(B)** $16 \mathrm{MR}^2$
- **(C)** $(3 M+12 m) \frac{R^2}{2}$
- **(D)** zero

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(3 \mathrm{M}+16 \mathrm{~m}) \frac{\mathrm{R}^2}{2}$**

**Detailed Solution:**

Moment of inertia of the disc about an axis passing through its centre and perpendicular to its plane is $I_{cm} = \dfrac{1}{2}MR^2$.

Using the parallel axis theorem, the moment of inertia of the disc about an axis passing through a point on its rim and perpendicular to its plane is:

$I_{disc} = I_{cm} + MR^2 = \dfrac{1}{2}MR^2 + MR^2 = \dfrac{3}{2}MR^2$

The four particles of mass $m$ are placed symmetrically on the rim. Let the axis pass through one of these particles. The distances of the four particles from this axis are $0$, $\sqrt{2}R$, $2R$, and $\sqrt{2}R$.

The moment of inertia of the four particles about this axis is:

$I_{particles} = m(0)^2 + m(\sqrt{2}R)^2 + m(2R)^2 + m(\sqrt{2}R)^2$

$I_{particles} = 0 + 2mR^2 + 4mR^2 + 2mR^2 = 8mR^2$

The total moment of inertia of the system is:

$I_{total} = I_{disc} + I_{particles} = \dfrac{3}{2}MR^2 + 8mR^2 = \dfrac{(3M + 16m)R^2}{2}$

Answer: $(3 \mathrm{M}+16 \mathrm{~m}) \frac{\mathrm{R}^2}{2}$

</details>

---

### Q39. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Moment of inertia of the rod about an axis passing through the centre and perpendicular to its length is ' $\mathrm{I}_1$ '. The same rod is bent into a ring and its moment of inertia about the diameter is ' $I_2$ '. Then $I_1 / I_2$ is

**Options:**

- **(A)** $\frac{3 \pi^2}{2}$
- **(B)** $\frac{2 \pi^2}{3}$
- **(C)** $\frac{\pi^2}{3}$
- **(D)** $\frac{\pi^2}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2 \pi^2}{3}$**

**Detailed Solution:**

Let $M$ be the mass and $L$ be the length of the rod.

The moment of inertia of the rod about an axis passing through its centre and perpendicular to its length is:

$I_1 = \dfrac{M L^2}{12}$

When the rod is bent into a ring, its circumference is equal to the length of the rod.

$2 \pi R = L \Rightarrow R = \dfrac{L}{2 \pi}$

The moment of inertia of the ring about its diameter is:

$I_2 = \dfrac{M R^2}{2}$

Substituting the value of $R$:

$I_2 = \dfrac{M}{2} \left( \dfrac{L}{2 \pi} \right)^2 = \dfrac{M L^2}{8 \pi^2}$

Taking the ratio of $I_1$ to $I_2$:

$\dfrac{I_1}{I_2} = \dfrac{\dfrac{M L^2}{12}}{\dfrac{M L^2}{8 \pi^2}} = \dfrac{8 \pi^2}{12} = \dfrac{2 \pi^2}{3}$

Answer: $\frac{2 \pi^2}{3}$

</details>

---

### Q40. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Moment of inertia of a solid sphere about its diameter is 'I'. It is then casted into 27 small spheres of same diameter. The moment of inertia of each small sphere about its diameter is

**Options:**

- **(A)** $\frac{\mathrm{I}}{44}$
- **(B)** $\frac{\mathrm{I}}{188}$
- **(C)** $\frac{\mathrm{I}}{204}$
- **(D)** $\frac{\mathrm{I}}{243}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\mathrm{I}}{243}$**

**Detailed Solution:**

Let the mass of the original solid sphere be $M$ and its radius be $R$.

The moment of inertia of the solid sphere about its diameter is $I = \dfrac{2}{5}MR^2$.

Let the mass of each small sphere be $m$ and its radius be $r$.

Since the original sphere is cast into $27$ small spheres, the total volume remains constant:

$\dfrac{4}{3}\pi R^3 = 27 \times \dfrac{4}{3}\pi r^3$

$R^3 = 27r^3 \Rightarrow r = \dfrac{R}{3}$

Also, the mass of each small sphere is $m = \dfrac{M}{27}$.

The moment of inertia of each small sphere about its diameter is:

$I' = \dfrac{2}{5}mr^2$

Substituting the values of $m$ and $r$:

$I' = \dfrac{2}{5} \left(\dfrac{M}{27}\right) \left(\dfrac{R}{3}\right)^2$

$I' = \dfrac{2}{5} \dfrac{M}{27} \dfrac{R^2}{9}$

$I' = \dfrac{1}{243} \left(\dfrac{2}{5}MR^2\right)$

$I' = \dfrac{I}{243}$

Answer: $\frac{\mathrm{I}}{243}$

</details>

---

### Q41. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The moment of inertia of a solid sphere of mass ' $m$ ' and radius ' $R$ ' about its diametric axis is 'I'. Its moment of inertia about a tangent in the plane is

**Options:**

- **(A)** $2.5 \mathrm{I}$
- **(B)** $3.0 \mathrm{I}$
- **(C)** $3.5 \mathrm{I}$
- **(D)** 4 I

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3.5 \mathrm{I}$**

**Detailed Solution:**

The moment of inertia of a solid sphere about its diametric axis is given by:

$I = \dfrac{2}{5}mR^2$

According to the theorem of parallel axes, the moment of inertia of the sphere about a tangent is:

$I_T = I_{cm} + mR^2$

$I_T = \dfrac{2}{5}mR^2 + mR^2 = \dfrac{7}{5}mR^2$

Expressing $I_T$ in terms of $I$:

$I_T = \dfrac{7}{2} \left(\dfrac{2}{5}mR^2\right) = 3.5 I$

Answer: $3.5 \mathrm{I}$

</details>

---

### Q42. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Four particles each of mass $M$ are placed at the corners of a square of side L. The radius of gyration of the system about an axis perpendicular to the square and passing through its centre is

**Options:**

- **(A)** $\frac{L}{2}$
- **(B)** $\frac{L}{\sqrt{2}}$
- **(C)** 2L
- **(D)** $\frac{L}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{L}{\sqrt{2}}$**

**Detailed Solution:**

The distance of each corner of the square from its centre is $r = \dfrac{L}{\sqrt{2}}$.

The moment of inertia of the system of four particles about an axis perpendicular to the square and passing through its centre is

$I = 4 \times M r^2 = 4M \left(\dfrac{L}{\sqrt{2}}\right)^2 = 2ML^2$

The total mass of the system is $M_{total} = 4M$.

The radius of gyration $K$ is given by $I = M_{total} K^2$.

$2ML^2 = 4M K^2$

$K^2 = \dfrac{L^2}{2}$

$K = \dfrac{L}{\sqrt{2}}$

Answer: $\frac{L}{\sqrt{2}}$

</details>

---

### Q43. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A thin metal wire of length ' $L$ ' and mass ' $M$ ' is bent to form semicircular ring as shown. The moment of inertia about $\mathrm{XX}^1$ is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/Go6r71WZpYnyEwotqDHl35aTm94bFPFjXUzakDz-BI8.original.fullsize.png">

**Options:**

- **(A)** $\frac{M L^2}{4 \pi^2}$
- **(B)** $\frac{2 \mathrm{ML}^2}{\pi^2}$
- **(C)** $\frac{M L^2}{2 \pi^2}$
- **(D)** $\frac{\mathrm{ML}^2}{\pi^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{M L^2}{2 \pi^2}$**

**Detailed Solution:**

Let $R$ be the radius of the semicircular ring.

The length of the wire is bent into a semicircle, so the arc length is equal to $L$.

$\pi R = L \Rightarrow R = \dfrac{L}{\pi}$

The axis $XX^1$ passes through the two ends of the semicircular wire, which corresponds to the diametric axis of the full circle.

The moment of inertia of a semicircular ring of mass $M$ and radius $R$ about its diametric base is the same as that of a full ring of the same mass and radius about its diameter.

$I = \dfrac{1}{2} M R^2$

Substituting the value of $R$ in the above equation, we get:

$I = \dfrac{1}{2} M \left( \dfrac{L}{\pi} \right)^2$

$I = \dfrac{M L^2}{2 \pi^2}$

Answer: $\frac{M L^2}{2 \pi^2}$

</details>

---

### Q44. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A solid sphere and thin walled hollow sphere have same mass and same material. Which of them have greater moment of inertia about their diameter?
[ $\mathrm{I}_{\mathrm{h}}=$ moment of inertia of hollow sphere about an axis coinciding with its diameter, $\mathrm{I}_{\mathrm{s}}=$ moment of inertia of solid sphere about an axis coinciding with its diameter]

**Options:**

- **(A)** $\mathrm{I}_{\mathrm{s}}>\mathrm{I}_{\mathrm{h}}$
- **(B)** $\mathrm{I}_{\mathrm{h}} \geqslant \mathrm{I}_{\mathrm{s}}$
- **(C)** $\mathrm{I}_{\mathrm{h}}>\mathrm{I}_{\mathrm{s}}$
- **(D)** $\mathrm{I}_{\mathrm{h}}=\mathrm{I}_{\mathrm{s}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{I}_{\mathrm{h}}>\mathrm{I}_{\mathrm{s}}$**

**Detailed Solution:**

Let $M$ be the mass and $\rho$ be the density of the material for both spheres.

The volume of the material for the solid sphere is $V_s = \dfrac{4}{3} \pi R_s^3$.

The volume of the material for the hollow sphere is $V_h = \dfrac{4}{3} \pi (R_{out}^3 - R_{in}^3)$.

Since they have the same mass and same material, their volumes of material must be equal, so $V_s = V_h$.

$\dfrac{4}{3} \pi R_s^3 = \dfrac{4}{3} \pi (R_{out}^3 - R_{in}^3) \Rightarrow R_s^3 = R_{out}^3 - R_{in}^3$

This implies $R_{out} > R_s$. For a thin-walled hollow sphere, its effective radius $R_h \approx R_{out}$, so $R_h > R_s$.

The moment of inertia of the solid sphere about its diameter is $I_s = \dfrac{2}{5} M R_s^2 = 0.4 M R_s^2$.

The moment of inertia of the thin-walled hollow sphere about its diameter is $I_h = \dfrac{2}{3} M R_h^2 \approx 0.67 M R_h^2$.

Since $R_h > R_s$ and $\dfrac{2}{3} > \dfrac{2}{5}$, it follows that $I_h > I_s$.

Answer: $\mathrm{I}_{\mathrm{h}}>\mathrm{I}_{\mathrm{s}}$

</details>

---

### Q45. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Moment of inertia of a thin uniform rod rotating about the perpendicular axis passing through its centre is 'I'. If the same rod is bent in the form of ring, its moment of inertia about the diameter is ' $\mathrm{I}_1{ }^{\prime}$. If $I_1=x I$, then the value of ' $x$ ' is

**Options:**

- **(A)** $\frac{2 \pi^2}{3}$
- **(B)** $\frac{3}{2 \pi^2}$
- **(C)** $\frac{3 \pi^2}{4}$
- **(D)** $\frac{4}{3 \pi^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3}{2 \pi^2}$**

**Detailed Solution:**

Let $M$ be the mass and $L$ be the length of the thin uniform rod.

Moment of inertia of the rod about a perpendicular axis passing through its centre is $I = \dfrac{M L^2}{12}$.

When the rod is bent into a ring of radius $R$, its length becomes the circumference of the ring.

$L = 2 \pi R \Rightarrow R = \dfrac{L}{2 \pi}$

Moment of inertia of the ring about its diameter is $I_1 = \dfrac{M R^2}{2}$.

Substituting the value of $R$, we get:

$I_1 = \dfrac{M}{2} \left( \dfrac{L}{2 \pi} \right)^2 = \dfrac{M L^2}{8 \pi^2}$

Given $I_1 = x I$, we have:

$x = \dfrac{I_1}{I} = \dfrac{\dfrac{M L^2}{8 \pi^2}}{\dfrac{M L^2}{12}} = \dfrac{12}{8 \pi^2} = \dfrac{3}{2 \pi^2}$

Answer: $\frac{3}{2 \pi^2}$

</details>

---

### Q46. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Three spheres, each of mass ' $m$ ' and radius ' $r$ ' are placed as shown in figure. Consider an axis $\mathrm{YY}^1$, which is touching two spheres and passing through the diameter of third sphere. The moment of inertia of the system consisting of these three spheres about $\mathrm{YY}^1$ axis is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/HHfZowIsORtbWKhCOgJbjow9W_gzHyZfB5-ZxkcsRQY.original.fullsize.png">

**Options:**

- **(A)** $\frac{7}{5} \mathrm{mr}^2$
- **(B)** $\frac{2}{5} \mathrm{mr}^2$
- **(C)** $\frac{16}{5} \mathrm{mr}^2$
- **(D)** $\frac{\mathrm{mr}^2}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{16}{5} \mathrm{mr}^2$**

**Detailed Solution:**

The moment of inertia of a solid sphere of mass $m$ and radius $r$ about its diameter is given by $I_{cm} = \dfrac{2}{5}mr^2$.

For sphere 1, the axis $\mathrm{YY}^1$ passes through its diameter. Therefore, its moment of inertia about the axis is:
$I_1 = \dfrac{2}{5}mr^2$

For spheres 2 and 3, the axis $\mathrm{YY}^1$ is tangent to their surfaces. The perpendicular distance from the center of each of these spheres to the axis $\mathrm{YY}^1$ is equal to their radius $r$.

Using the parallel axis theorem, the moment of inertia of sphere 2 about the axis $\mathrm{YY}^1$ is:
$I_2 = I_{cm} + mr^2 = \dfrac{2}{5}mr^2 + mr^2 = \dfrac{7}{5}mr^2$

Similarly, the moment of inertia of sphere 3 about the axis $\mathrm{YY}^1$ is:
$I_3 = I_{cm} + mr^2 = \dfrac{2}{5}mr^2 + mr^2 = \dfrac{7}{5}mr^2$

The total moment of inertia of the system about the axis $\mathrm{YY}^1$ is the sum of the moments of inertia of the three spheres:
$I_{total} = I_1 + I_2 + I_3$
$I_{total} = \dfrac{2}{5}mr^2 + \dfrac{7}{5}mr^2 + \dfrac{7}{5}mr^2$
$I_{total} = \dfrac{16}{5}mr^2$

Answer: $\frac{16}{5} \mathrm{mr}^2$

</details>

---

### Q47. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two circular loops P and Q of radii 'r' and 'nr' are made respectively from a uniform wire. Moment of inertia of loop Q about its axis is 4 times that of loop P about its axis. The value of n is

**Options:**

- **(A)** $(2)^{-2 / 3}$
- **(B)** $(2)^{2 / 3}$
- **(C)** $\sqrt{2}$
- **(D)** $2^{1 / 3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(2)^{2 / 3}$**

**Detailed Solution:**

Let $\lambda$ be the linear mass density of the uniform wire.

Mass of loop P, $M_P = \lambda (2\pi r)$

Mass of loop Q, $M_Q = \lambda (2\pi nr)$

Moment of inertia of a circular loop about its axis is given by $I = MR^2$.

Moment of inertia of loop P about its axis:
$I_P = M_P r^2 = \lambda (2\pi r) r^2 = 2\pi \lambda r^3$

Moment of inertia of loop Q about its axis:
$I_Q = M_Q (nr)^2 = \lambda (2\pi nr) (nr)^2 = 2\pi \lambda n^3 r^3$

Given that $I_Q = 4 I_P$:
$2\pi \lambda n^3 r^3 = 4 (2\pi \lambda r^3)$

$n^3 = 4$

$n = 4^{1/3} = (2^2)^{1/3} = 2^{2/3}$

Answer: $(2)^{2 / 3}$

</details>

---

### Q48. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two spheres each of mass M and radius R are connected with a massless rod of length 4 R . The moment of inertia of the system about an axis passing through the centre of one of the spheres and perpendicular to the rod will be
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/B5XC3IPdJF2DHoFONnHdBTzjDZNxVUvCPZ2NlaBiCdE.original.fullsize.png">

**Options:**

- **(A)** $\frac{21}{5} \mathrm{MR}^2$
- **(B)** $\frac{84}{5} \mathrm{MR}^2$
- **(C)** $\frac{42}{5} \mathrm{MR}^2$
- **(D)** $\frac{5}{21} \mathrm{MR}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{84}{5} \mathrm{MR}^2$**

**Detailed Solution:**

The system consists of two solid spheres, each of mass $M$ and radius $R$. The distance between their centers is given as $d = 4R$.

We need to find the moment of inertia of the system about an axis passing through the center of one of the spheres and perpendicular to the rod.

For the first sphere (where the axis passes through its center), the moment of inertia is:
$I_1 = \dfrac{2}{5}MR^2$

For the second sphere, the axis of rotation is at a distance $d = 4R$ from its center. Using the parallel axis theorem, its moment of inertia is:
$I_2 = I_{cm} + Md^2$
$I_2 = \dfrac{2}{5}MR^2 + M(4R)^2$
$I_2 = \dfrac{2}{5}MR^2 + 16MR^2 = \dfrac{82}{5}MR^2$

The total moment of inertia of the system is the sum of the moments of inertia of the two spheres:
$I = I_1 + I_2$
$I = \dfrac{2}{5}MR^2 + \dfrac{82}{5}MR^2$
$I = \dfrac{84}{5}MR^2$

Answer: $\frac{84}{5} \mathrm{MR}^2$

</details>

---

### Q49. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two discs $A$ and $B$ of same material and thickness have radii $R$ and $3 R$ respectively. Their moments of inertia about their axis will be in the ratio

**Options:**

- **(A)** $3: 1$
- **(B)** $1: 9$
- **(C)** 1:81
- **(D)** $1: 27$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1:81**

**Detailed Solution:**

Mass of a disc is given by $M = \text{volume} \times \text{density} = \pi R^2 t \rho$, where $t$ is the thickness and $\rho$ is the density.

Moment of inertia of a disc about its axis is $I = \dfrac{1}{2} M R^2$.

Substituting the expression for mass, we get $I = \dfrac{1}{2} (\pi R^2 t \rho) R^2 = \dfrac{1}{2} \pi t \rho R^4$.

Since both discs have the same material (same $\rho$) and same thickness (same $t$), $I \propto R^4$.

Therefore, the ratio of their moments of inertia is $\dfrac{I_A}{I_B} = \left(\dfrac{R_A}{R_B}\right)^4 = \left(\dfrac{R}{3R}\right)^4 = \dfrac{1}{81}$.

The ratio is $1:81$.

Answer: 1:81

</details>

---

### Q50. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Four particles each of mass M are placed at the corners of a square of side L . The radius of gyration of the system about an axis perpendicular to the square and passing through its centre is

**Options:**

- **(A)** L
- **(B)** $\frac{L}{2}$
- **(C)** $\frac{L}{4}$
- **(D)** $\frac{\mathrm{L}}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\mathrm{L}}{\sqrt{2}}$**

**Detailed Solution:**

The distance of each particle from the centre of the square is $r = \dfrac{L}{\sqrt{2}}$.

The moment of inertia of the system about an axis perpendicular to the square and passing through its centre is

$I = 4 \times M r^2 = 4 M \left(\dfrac{L}{\sqrt{2}}\right)^2 = 2 M L^2$

The total mass of the system is $M_{total} = 4M$.

The radius of gyration $K$ is given by $I = M_{total} K^2$.

$2 M L^2 = 4 M K^2$

$K^2 = \dfrac{L^2}{2}$

$K = \dfrac{L}{\sqrt{2}}$

Answer: $\frac{\mathrm{L}}{\sqrt{2}}$

</details>

---

### Q51. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Three point masses, each of mass ' $m$ ' are placed at the corners of an equilateral triangle of side ' $L$ '. The moment of inertia of the system about an axis passing through one of the vertices and parallel to the side joining other two vertices will be

**Options:**

- **(A)** $\frac{3 \mathrm{~mL}^2}{4}$
- **(B)** $\frac{\mathrm{mL}^2}{4}$
- **(C)** $\frac{3 \mathrm{~mL}^2}{2}$
- **(D)** $\frac{\mathrm{mL}^2}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3 \mathrm{~mL}^2}{2}$**

**Detailed Solution:**

Let the three masses be placed at the vertices A, B, and C of the equilateral triangle of side $L$.

The axis of rotation passes through vertex A and is parallel to the side BC.

The perpendicular distance of vertex A from the axis is zero.

The perpendicular distance of vertices B and C from the axis is equal to the altitude of the equilateral triangle.

Altitude of the equilateral triangle, $h = L \sin(60^{\circ}) = \dfrac{\sqrt{3}}{2} L$.

The moment of inertia of the system about the given axis is:

$I = I_A + I_B + I_C$

$I = m(0)^2 + m(h)^2 + m(h)^2$

$I = 2mh^2$

Substituting the value of $h$:

$I = 2m \left( \dfrac{\sqrt{3}}{2} L \right)^2$

$I = 2m \left( \dfrac{3}{4} L^2 \right)$

$I = \dfrac{3}{2} m L^2$

Answer: $\frac{3 \mathrm{~mL}^2}{2}$

</details>

---

### Q52. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two loops $P$ and $Q$ of radii $R_1$ and $R_2$ are made from uniform metal wire of same material. $\mathrm{I}_{\mathrm{P}}$ and $\mathrm{I}_{\mathrm{Q}}$ be the moment of inertia of loop P and Q respectively then ratio $R_1 / R_2$ is $\left(\right.$ Given $\left.I_P / I_Q=27\right)$

**Options:**

- **(A)** $4: 1$
- **(B)** $3: 1$
- **(C)** $9: 1$
- **(D)** $6: 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3: 1$**

**Detailed Solution:**

Let $\lambda$ be the linear mass density of the uniform metal wire.

The mass of a circular loop of radius $R$ is given by $M = 2\pi R \lambda$.

The moment of inertia of a circular loop about its central axis is $I = MR^2$.

Substituting the expression for mass, we get:

$I = (2\pi R \lambda) R^2 = 2\pi \lambda R^3$

This shows that the moment of inertia is directly proportional to the cube of the radius, $I \propto R^3$.

For loops P and Q, the ratio of their moments of inertia is:

$\dfrac{I_P}{I_Q} = \left(\dfrac{R_1}{R_2}\right)^3$

Given $\dfrac{I_P}{I_Q} = 27$, we have:

$\left(\dfrac{R_1}{R_2}\right)^3 = 27$

Taking the cube root on both sides:

$\dfrac{R_1}{R_2} = 3$

The ratio $R_1 : R_2$ is $3 : 1$.

Answer: $3: 1$

</details>

---

### Q53. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Two spheres of equal masses, one of which is a thin spherical shell and the other solid sphere, have the same moment of inertia about their respective diameters. The ratio of their radii is

**Options:**

- **(A)** $3: 5$
- **(B)** $\sqrt{3}: \sqrt{5}$
- **(C)** $\sqrt{3}: \sqrt{7}$
- **(D)** $5: 7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{3}: \sqrt{5}$**

**Detailed Solution:**

Let the mass of both spheres be $M$.

Let the radius of the thin spherical shell be $R_1$ and the radius of the solid sphere be $R_2$.

The moment of inertia of the thin spherical shell about its diameter is $I_1 = \dfrac{2}{3} M R_1^2$.

The moment of inertia of the solid sphere about its diameter is $I_2 = \dfrac{2}{5} M R_2^2$.

Given that $I_1 = I_2$, we have:

$\dfrac{2}{3} M R_1^2 = \dfrac{2}{5} M R_2^2$

$\dfrac{R_1^2}{R_2^2} = \dfrac{3}{5}$

$\dfrac{R_1}{R_2} = \dfrac{\sqrt{3}}{\sqrt{5}}$

The ratio of their radii is $\sqrt{3} : \sqrt{5}$.

Answer: $\sqrt{3}: \sqrt{5}$

</details>

---

### Q54. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The radius of gyration of a circular disc of radius R and mass m rotating about diameter as axis is

**Options:**

- **(A)** $\mathrm{R} \sqrt{2}$
- **(B)** $\mathrm{R} / \sqrt{2}$
- **(C)** $R / 2$
- **(D)** R

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $R / 2$**

**Detailed Solution:**

The moment of inertia of a circular disc of mass $m$ and radius $R$ about an axis passing through its centre and perpendicular to its plane is $I_{z} = \dfrac{1}{2}mR^{2}$.

By the theorem of perpendicular axes, the moment of inertia about its diameter is $I_{d} = \dfrac{I_{z}}{2} = \dfrac{1}{4}mR^{2}$.

The radius of gyration $k$ is given by $I_{d} = mk^{2}$.

Equating the two expressions for $I_{d}$:

$mk^{2} = \dfrac{1}{4}mR^{2}$

$k^{2} = \dfrac{R^{2}}{4}$

$k = \dfrac{R}{2}$

Answer: $R / 2$

</details>

---

### Q55. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Three thin rods, each of mass ' $M$ ' and length ' $L$ ' are placed along $X, Y$ and Z axes which are mutually perpendicular. One end of each rod is at origin. M. I. of the system about Z axis is

**Options:**

- **(A)** $\frac{3 \mathrm{ML}^2}{4}$
- **(B)** $\frac{2 \mathrm{ML}^2}{5}$
- **(C)** $\frac{2 \mathrm{ML}^2}{3}$
- **(D)** $\frac{3 \mathrm{ML}^2}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2 \mathrm{ML}^2}{3}$**

**Detailed Solution:**

The system consists of three rods placed along the X, Y, and Z axes, each with one end at the origin.

The moment of inertia of the rod along the X-axis about the Z-axis (which is perpendicular to the rod and passes through its end) is $I_1 = \dfrac{ML^2}{3}$.

The moment of inertia of the rod along the Y-axis about the Z-axis (which is also perpendicular to the rod and passes through its end) is $I_2 = \dfrac{ML^2}{3}$.

The moment of inertia of the rod along the Z-axis about the Z-axis is $I_3 = 0$, since the axis passes through the rod itself and its thickness is negligible.

The total moment of inertia of the system about the Z-axis is the sum of the individual moments of inertia:

$I = I_1 + I_2 + I_3$

$I = \dfrac{ML^2}{3} + \dfrac{ML^2}{3} + 0 = \dfrac{2ML^2}{3}$

Answer: $\frac{2 \mathrm{ML}^2}{3}$

</details>

---

### Q56. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Moment of inertia of a disc about an axis passing through its centre and perpendicular to its plane is 'I'. The ratio of moment of inertia about a parallel axis tangential to its rim to passing through a point midway between the centre and the rim is

**Options:**

- **(A)** 2: 1
- **(B)** 3:1
- **(C)** 4:1
- **(D)** 6: 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2: 1**

**Detailed Solution:**

Moment of inertia of a disc about an axis passing through its centre and perpendicular to its plane is $I_C = \dfrac{1}{2}MR^2$.

By the theorem of parallel axes, the moment of inertia about a parallel axis tangential to its rim is:
$I_1 = I_C + MR^2 = \dfrac{1}{2}MR^2 + MR^2 = \dfrac{3}{2}MR^2$

The moment of inertia about a parallel axis passing through a point midway between the centre and the rim (at a distance of $\dfrac{R}{2}$ from the centre) is:
$I_2 = I_C + M\left(\dfrac{R}{2}\right)^2 = \dfrac{1}{2}MR^2 + \dfrac{1}{4}MR^2 = \dfrac{3}{4}MR^2$

The required ratio is:
$\dfrac{I_1}{I_2} = \dfrac{\dfrac{3}{2}MR^2}{\dfrac{3}{4}MR^2} = \dfrac{3}{2} \times \dfrac{4}{3} = \dfrac{2}{1}$

Thus, the ratio is $2:1$.

Answer: 2: 1

</details>

---

### Q57. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Four thin metal rods each of mass ' $M$ ' and length ' $L$ ', are welded end to end to form a square. The moment of inertia of the system about an axis passing through the centre of the square and perpendicular to its plane is

**Options:**

- **(A)** $\frac{\mathrm{ML}^2}{3}$
- **(B)** $\frac{2 \mathrm{ML}^2}{3}$
- **(C)** $\frac{2 \mathrm{ML}^2}{9}$
- **(D)** $\frac{4 \mathrm{ML}^2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{4 \mathrm{ML}^2}{3}$**

**Detailed Solution:**

The moment of inertia of one rod about an axis passing through its centre and perpendicular to its length is $I_{CM} = \dfrac{ML^2}{12}$.

The distance of the centre of the square from the centre of each rod is $d = \dfrac{L}{2}$.

Using the parallel axis theorem, the moment of inertia of one rod about the axis passing through the centre of the square and perpendicular to its plane is:

$I_1 = I_{CM} + Md^2$

$I_1 = \dfrac{ML^2}{12} + M\left(\dfrac{L}{2}\right)^2$

$I_1 = \dfrac{ML^2}{12} + \dfrac{ML^2}{4} = \dfrac{ML^2}{3}$

Since the square is made of four identical rods, the total moment of inertia of the system is:

$I = 4 \times I_1 = 4 \times \dfrac{ML^2}{3} = \dfrac{4ML^2}{3}$

Answer: $\frac{4 \mathrm{ML}^2}{3}$

</details>

---

### Q58. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A solid metallic sphere of radius ' $R$ ' having moment of inertia ' I ' about diameter is melted and recast into a solid disc of radius ' $r$ ' of a uniform thickness. The moment of inertia of a disc about an axis passing through its edge and perpendicular to its plane is also equal to ' I '. The ratio $\dfrac{r}{R}$ is

**Options:**

- **(A)** $\dfrac{1}{\sqrt{2}}$
- **(B)** $\dfrac{2}{\sqrt{5}}$
- **(C)** $\dfrac{2}{\sqrt{10}}$
- **(D)** $\dfrac{2}{\sqrt{15}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{2}{\sqrt{15}}$**

**Detailed Solution:**

Moment of inertia of a solid sphere of mass $M$ and radius $R$ about its diameter is given by:

$I = \dfrac{2}{5}MR^2$

When the sphere is melted and recast into a disc, the mass $M$ remains constant.

Moment of inertia of a uniform solid disc of radius $r$ about an axis passing through its center and perpendicular to its plane is $\dfrac{1}{2}Mr^2$.

Using the parallel axis theorem, the moment of inertia of the disc about an axis passing through its edge and perpendicular to its plane is:

$I_{disc} = I_{cm} + Mr^2 = \dfrac{1}{2}Mr^2 + Mr^2 = \dfrac{3}{2}Mr^2$

It is given that the moment of inertia of the disc is equal to the moment of inertia of the sphere:

$\dfrac{3}{2}Mr^2 = \dfrac{2}{5}MR^2$

$\dfrac{r^2}{R^2} = \dfrac{4}{15}$

$\dfrac{r}{R} = \dfrac{2}{\sqrt{15}}$

Answer: $\dfrac{2}{\sqrt{15}}$

</details>

---

### Q59. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The moment of inertia of uniform circular disc is maximum about an axis perpendicular to the disc and passing through point
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/LwMLP4dfr2UKsPeVv1oeZk9e0yUvMaJDcQShgmit7ig.original.fullsize.png"/>

**Options:**

- **(A)** A
- **(B)** B
- **(C)** C
- **(D)** D

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) B**

**Detailed Solution:**

According to the parallel axis theorem, the moment of inertia of a body about any axis is given by:

$I = I_{cm} + Md^2$

where $I_{cm}$ is the moment of inertia about a parallel axis passing through the center of mass, $M$ is the mass of the body, and $d$ is the perpendicular distance between the two axes.

For the given uniform circular disc, the center of mass lies at point A. Thus, $I_{cm} = I_A$.

To maximize the moment of inertia $I$, the distance $d$ from the center of mass must be maximum.

From the given figure, the distances of the points from the center A are such that point B is on the circumference, while points C and D lie inside the disc. Therefore, the distance is maximum for point B ($d = R$).

Hence, the moment of inertia is maximum about an axis perpendicular to the disc and passing through point B.

Answer: B

</details>

---

### Q60. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Three thin rods, each mass ' 2 M ' and length ' $L$ ' are placed along $x, y$ and $z$ axis which are mutually perpendicular. One end of each rod is at origin. Moment of inertia of the system about x -axis is

**Options:**

- **(A)** $\dfrac{4 \mathrm{ML}^2}{3}$
- **(B)** $\dfrac{\mathrm{ML}^2}{12}$
- **(C)** $\dfrac{\mathrm{ML}^2}{6}$
- **(D)** $\dfrac{2 \mathrm{ML}^2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{4 \mathrm{ML}^2}{3}$**

**Detailed Solution:**

Mass of each rod $m = 2M$, length $= L$.

Moment of inertia of the system about the $x$-axis is the sum of the moments of inertia of the three rods about the $x$-axis.

$I_{x} = I_{1} + I_{2} + I_{3}$

For the rod along the $x$-axis, the distance of any mass element from the $x$-axis is zero.

$I_{1} = 0$

For the rod along the $y$-axis, the $x$-axis is perpendicular to it and passes through its end.

$I_{2} = \dfrac{m L^2}{3} = \dfrac{(2M) L^2}{3} = \dfrac{2ML^2}{3}$

For the rod along the $z$-axis, the $x$-axis is perpendicular to it and passes through its end.

$I_{3} = \dfrac{m L^2}{3} = \dfrac{(2M) L^2}{3} = \dfrac{2ML^2}{3}$

Total moment of inertia:

$I_{x} = 0 + \dfrac{2ML^2}{3} + \dfrac{2ML^2}{3} = \dfrac{4ML^2}{3}$

Answer: $\dfrac{4 \mathrm{ML}^2}{3}$

</details>

---

### Q61. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A circular disc of radius ' $R$ ' and thickness $\dfrac{R}{6}$ has moment of inertia 'I' about an axis passing through its centre and perpendicular to its plane. It is melted and recasted into a solid sphere then moment of inertia of sphere about an axis passing through diameter is

**Options:**

- **(A)** I
- **(B)** $\dfrac{2 \mathrm{I}}{3}$
- **(C)** $\dfrac{I}{5}$
- **(D)** $\dfrac{\mathrm{I}}{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{I}{5}$**

**Detailed Solution:**

Let the mass of the disc be $M$.

The moment of inertia of the disc about an axis passing through its centre and perpendicular to its plane is given by:
$I = \dfrac{1}{2} M R^2$

The volume of the disc is:
$V_{\text{disc}} = \pi R^2 t = \pi R^2 \left(\dfrac{R}{6}\right) = \dfrac{\pi R^3}{6}$

Let the radius of the solid sphere formed by melting the disc be $r$. The volume of the solid sphere is:
$V_{\text{sphere}} = \dfrac{4}{3} \pi r^3$

Since the volume remains constant during recasting:
$\dfrac{4}{3} \pi r^3 = \dfrac{\pi R^3}{6}$

$r^3 = \dfrac{R^3}{8} \Rightarrow r = \dfrac{R}{2}$

The moment of inertia of the solid sphere about its diameter is:
$I_{\text{sphere}} = \dfrac{2}{5} M r^2$

Substituting $r = \dfrac{R}{2}$:
$I_{\text{sphere}} = \dfrac{2}{5} M \left(\dfrac{R}{2}\right)^2 = \dfrac{2}{5} M \left(\dfrac{R^2}{4}\right) = \dfrac{M R^2}{10}$

Since $I = \dfrac{1}{2} M R^2$, we can write:
$I_{\text{sphere}} = \dfrac{1}{5} \left(\dfrac{1}{2} M R^2\right) = \dfrac{I}{5}$

Answer: $\dfrac{I}{5}$

</details>

---

### Q62. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The moment of inertia of thin square plate PQRS of uniform thickness, about an axis passing through centre ' O ' and perpendicular to the plane of the plate is $\left(\mathrm{I}_1, \mathrm{I}_2, \mathrm{I}_3, \mathrm{I}_4\right.$ are respectively the moments of inertia about axis $1,2,3,4$ which are in the plane of the plate as
shown in figure)
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/f7L6iHe9Wbxsrk4lmqkzok5dExpwzdQfjI59GZjEu7M.original.fullsize.png"/>

**Options:**

- **(A)** $\mathrm{I}_1+\mathrm{I}_2+\mathrm{I}_3$
- **(B)** $\mathrm{I}_1+\mathrm{I}_3+\mathrm{I}_4$
- **(C)** $\mathrm{I}_1+\mathrm{I}_2+\mathrm{I}_3+\mathrm{I}_4$
- **(D)** $\quad \mathrm{I}_1+\mathrm{I}_3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\quad \mathrm{I}_1+\mathrm{I}_3$**

**Detailed Solution:**

For a uniform square plate, the moment of inertia about any axis passing through its center and lying in its plane is the same due to symmetry.

Therefore, the moments of inertia about the given axes are equal:
$\mathrm{I}_1 = \mathrm{I}_2 = \mathrm{I}_3 = \mathrm{I}_4 = \mathrm{I}$

According to the perpendicular axis theorem, the moment of inertia about an axis passing through the center and perpendicular to the plane of the plate ($\mathrm{I}_z$) is equal to the sum of the moments of inertia about any two mutually perpendicular axes in the plane of the plate.

Taking axes 3 and 4 (which are mutually perpendicular):
$\mathrm{I}_z = \mathrm{I}_3 + \mathrm{I}_4 = \mathrm{I} + \mathrm{I} = 2\mathrm{I}$

Now, checking the given options, we look for a sum that equals $2\mathrm{I}$:
$\mathrm{I}_1 + \mathrm{I}_3 = \mathrm{I} + \mathrm{I} = 2\mathrm{I}$

Thus, the moment of inertia about the perpendicular axis is $\mathrm{I}_1 + \mathrm{I}_3$.

Answer: $\quad \mathrm{I}_1+\mathrm{I}_3$

</details>

---

### Q63. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Two solid spheres (A and B) are made of metals having densities $\rho_A$ and $\rho_B$ respectively. If there masses are equal then ratio of their moments of inertia $\left(\dfrac{I_B}{I_A}\right)$ about their respective diameter is

**Options:**

- **(A)** $\left(\dfrac{\rho_B}{\rho_A}\right)^{2 / 3}$
- **(B)** $\left(\dfrac{\rho_A}{\rho_B}\right)^{2 / 3}$.
- **(C)** $\dfrac{\rho_A}{\rho_B}$
- **(D)** $\dfrac{\rho_B}{\rho_A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\dfrac{\rho_A}{\rho_B}\right)^{2 / 3}$.**

**Detailed Solution:**

Moment of inertia of a solid sphere about its diameter is $I = \dfrac{2}{5}MR^2$.

Given that the masses of both spheres are equal, $M_A = M_B = M$.

Mass is related to density and radius by $M = \dfrac{4}{3}\pi R^3 \rho$.

Since $M$ is constant, $R^3 \propto \dfrac{1}{\rho} \Rightarrow R \propto \rho^{-1/3}$.

The moment of inertia $I \propto M R^2$. Since $M$ is constant, $I \propto R^2 \propto \rho^{-2/3}$.

Therefore, the ratio of their moments of inertia is $\dfrac{I_B}{I_A} = \left(\dfrac{\rho_A}{\rho_B}\right)^{2/3}$.

Answer: $\left(\dfrac{\rho_A}{\rho_B}\right)^{2 / 3}$.

</details>

---

### Q64. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A disc and a ring both have same mass and radius. The ratio of moment of inertia of the disc about its diameter to that of a ring about a tangent in its plane is

**Options:**

- **(A)** $1: 2$
- **(B)** $1: 4$
- **(C)** $1: 6$
- **(D)** $1: 8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1: 6$**

**Detailed Solution:**

Let the mass of the disc and the ring be $M$ and their radius be $R$.

The moment of inertia of a disc about its diameter is given by:
$I_{1} = \dfrac{1}{4}MR^2$

The moment of inertia of a ring about its diameter is:
$I_{diameter} = \dfrac{1}{2}MR^2$

Using the parallel axis theorem, the moment of inertia of the ring about a tangent in its plane is:
$I_{2} = I_{diameter} + MR^2 = \dfrac{1}{2}MR^2 + MR^2 = \dfrac{3}{2}MR^2$

The required ratio is:
$\dfrac{I_{1}}{I_{2}} = \dfrac{\dfrac{1}{4}MR^2}{\dfrac{3}{2}MR^2} = \dfrac{1}{4} \times \dfrac{2}{3} = \dfrac{1}{6}$

Answer: $1: 6$

</details>

---

### Q65. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two loops ' $A$ ' and ' $B$ ' of radii ' $R_1$ ' and ' $R_2$ ' are made from uniform wire. If moment of inertia of ' $A$ ' is ' $I_A$ ' and that ' $B$ ' is ' $\mathrm{B}_{\mathrm{B}}$ ', then $R_2 / R_1$ is $\left[\dfrac{I_A}{I_B}=27\right]$

**Options:**

- **(A)** $1: 6$
- **(B)** $1: 4$
- **(C)** $1: 3$
- **(D)** $1: 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1: 3$**

**Detailed Solution:**

Let the linear mass density of the uniform wire be \lambda.

The mass of loop $A$ is $M_A = \lambda (2\pi R_1)$ and the mass of loop $B$ is $M_B = \lambda (2\pi R_2)$.

The moment of inertia of a circular loop about its central axis is given by $I = MR^2$.

For loop $A$: $I_A = M_A R_1^2 = (2\pi \lambda R_1) R_1^2 = 2\pi \lambda R_1^3$

For loop $B$: $I_B = M_B R_2^2 = (2\pi \lambda R_2) R_2^2 = 2\pi \lambda R_2^3$

Taking the ratio of the moments of inertia:

$\dfrac{I_A}{I_B} = \left(\dfrac{R_1}{R_2}\right)^3$

Given that $\dfrac{I_A}{I_B} = 27$, we get:

$\left(\dfrac{R_1}{R_2}\right)^3 = 27$

$\dfrac{R_1}{R_2} = 3$

Therefore, $\dfrac{R_2}{R_1} = \dfrac{1}{3}$, which is $1:3$.

Answer: $1: 3$

</details>

---

### Q66. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two circular loops P and Q of radii ' r 'and ' nr ' are made respectively from a uniform wire. Moment of inertia of loop Q about its axis is four times that of loop P about its axis. The value of ' $n$ ' is

**Options:**

- **(A)** $(2)^{1 / 3}$
- **(B)** $(2)^{2 / 3}$
- **(C)** $\quad(2)^{3 / 4}$
- **(D)** $(2)^{1 / 4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(2)^{2 / 3}$**

**Detailed Solution:**

Let the linear mass density of the uniform wire be $\lambda$.

Mass of loop P, $M_P = \lambda (2\pi r)$

Moment of inertia of loop P about its axis, $I_P = M_P r^2 = \lambda (2\pi r) r^2 = 2\pi\lambda r^3$

Mass of loop Q, $M_Q = \lambda (2\pi nr)$

Moment of inertia of loop Q about its axis, $I_Q = M_Q (nr)^2 = \lambda (2\pi nr) (nr)^2 = 2\pi\lambda n^3 r^3$

Given that $I_Q = 4 I_P$

$2\pi\lambda n^3 r^3 = 4 (2\pi\lambda r^3)$

$n^3 = 4$

$n = 4^{1/3} = (2^2)^{1/3} = 2^{2/3}$

Answer: $(2)^{2 / 3}$

</details>

---

### Q67. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Ratio of radius of gyration of a circular dise to that of circular ring each of same mass and radius around their respective axes is

**Options:**

- **(A)** $\sqrt{2}: 1$
- **(B)** $\sqrt{2}: \sqrt{3}$
- **(C)** $\sqrt{3}: \sqrt{2}$
- **(D)** $1: \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1: \sqrt{2}$**

**Detailed Solution:**

Moment of inertia of a circular disc about its central axis is $I_{disc} = \dfrac{1}{2}MR^2$.

Radius of gyration of the disc is $K_{disc} = \sqrt{\dfrac{I_{disc}}{M}} = \dfrac{R}{\sqrt{2}}$.

Moment of inertia of a circular ring about its central axis is $I_{ring} = MR^2$.

Radius of gyration of the ring is $K_{ring} = \sqrt{\dfrac{I_{ring}}{M}} = R$.

Ratio of their radii of gyration is $\dfrac{K_{disc}}{K_{ring}} = \dfrac{\dfrac{R}{\sqrt{2}}}{R} = \dfrac{1}{\sqrt{2}}$.

The ratio is $1 : \sqrt{2}$.

Answer: $1: \sqrt{2}$

</details>

---

### Q68. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A solid sphere of mass ' $m$ ', radius ' $R$ ', having moment of inertia about an axis passing through center of mass as ' $I$ ' is recast into a disc of thickness ' $t$ ' whose moment of inertia about an axis passing through the rim (edge) \& perpendicular to plane remains ' $I$ '. Then the radius of disc is

**Options:**

- **(A)** $\dfrac{2 \mathrm{R}}{\sqrt{15}}$
- **(B)** $\left(\sqrt{\dfrac{2}{15}}\right) \mathrm{R}$
- **(C)** $\dfrac{4 \mathrm{R}}{\sqrt{15}}$
- **(D)** $\dfrac{\mathrm{R}}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{2 \mathrm{R}}{\sqrt{15}}$**

**Detailed Solution:**

The moment of inertia of a solid sphere of mass $m$ and radius $R$ about an axis passing through its center of mass is given by:

$I = \dfrac{2}{5} m R^2$

When the sphere is recast into a disc of radius $r$ and thickness $t$, its mass $m$ remains the same. The moment of inertia of the disc about an axis passing through its center and perpendicular to its plane is $\dfrac{1}{2} m r^2$.

Using the parallel axis theorem, the moment of inertia of the disc about an axis passing through its rim and perpendicular to its plane is:

$I_{\text{disc}} = I_{\text{cm}} + m r^2 = \dfrac{1}{2} m r^2 + m r^2 = \dfrac{3}{2} m r^2$

According to the given condition, the moment of inertia remains $I$. Therefore, we equate the two moments of inertia:

$\dfrac{3}{2} m r^2 = \dfrac{2}{5} m R^2$

$\Rightarrow r^2 = \dfrac{4}{15} R^2$

$\Rightarrow r = \dfrac{2R}{\sqrt{15}}$

Answer: $\dfrac{2 \mathrm{R}}{\sqrt{15}}$

</details>

---

### Q69. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

An annular disc has mass 10 kg and inner and outer radii are 5 m and 10 m respectively. Its moment of inertia about an axis passing through its centre and perpendicular to its plane is

**Options:**

- **(A)** $525 \text{ kg m}^2$
- **(B)** $625 \text{ kg m}^2$
- **(C)** $525 \text{ g cm}^2$
- **(D)** $625 \text{ g cm}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $625 \text{ kg m}^2$**

**Detailed Solution:**

The moment of inertia of an annular disc of mass $M$, inner radius $R_1$, and outer radius $R_2$ about an axis passing through its centre and perpendicular to its plane is given by:

$I = \dfrac{1}{2} M (R_1^2 + R_2^2)$

Given $M = 10 \text{ kg}$, $R_1 = 5 \text{ m}$, and $R_2 = 10 \text{ m}$.

Substituting the values:

$I = \dfrac{1}{2} \times 10 \times (5^2 + 10^2)$

$I = 5 \times (25 + 100)$

$I = 5 \times 125 = 625 \text{ kg m}^2$

Answer: $625 \text{ kg m}^2$

</details>

---

### Q70. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Four identical uniform solid spheres each of same mass ' $M$ ' and radius ' $R$ ' are placed touching each other as shown in figure, with centres $A, B, C, D . I_A, I_B, I_C$ and $I_D$ are the moment of inertia of these spheres respectively about an axis passing through centre and perpendicular to the plane. The difference in $\mathrm{I}_{\mathrm{A}}$, and $\mathrm{I}_{\mathrm{B}}$ is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/NwCEfR7s8wLChqj5uqj75gJjyiEBXsmrEmEl_1fg2fE.original.fullsize.png">

**Options:**

- **(A)** $24 \mathrm{MR}^2$
- **(B)** $32 \mathrm{MR}^2$
- **(C)** $56 \mathrm{MR}^2$
- **(D)** $80 \mathrm{MR}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $32 \mathrm{MR}^2$**

**Detailed Solution:**

Using the parallel axes theorem, the M.I. of the system about the axis passing through the centre of the sphere $\mathrm{A}$ is
$\begin{aligned}
\mathrm{I}_{\mathrm{A}}=\mathrm{I}_{\mathrm{A}}{ }^{\prime}+\mathrm{I}_{\mathrm{B}}{ }^{\prime}+\mathrm{I}_{\mathrm{C}^{\prime}}+\mathrm{I}_{\mathrm{D}}{ }^{\prime} & \\
\mathrm{I}_{\mathrm{A}}=\frac{2}{5} \mathrm{MR}^2+\left(\frac{2}{5} \mathrm{MR}^2+4 \mathrm{MR}^2\right) & +\left(\frac{2}{5} \mathrm{MR}^2+16 \mathrm{MR}^2\right) \\
& +\left(\frac{2}{5} \mathrm{MR}^2+36 \mathrm{MR}^2\right)
\end{aligned}$
$\therefore \quad \mathrm{I}_{\mathrm{A}}=57.6 \mathrm{MR}^2$
The M.I. about sphere B is,
$\begin{aligned}
\mathrm{I}_{\mathrm{B}}=\frac{2}{5} \mathrm{MR}^2+\left(\frac{2}{5} \mathrm{MR}^2+4 \mathrm{MR}^2\right) & +\left(\frac{2}{5} \mathrm{MR}^2+16 \mathrm{MR}^2\right) \\
& +\left(\frac{2}{5} \mathrm{MR}^2+4 \mathrm{MR}^2\right) \\
\therefore \quad \mathrm{I}_{\mathrm{B}}=25.6 \mathrm{MR}^2 & \mathrm{I}_{\mathrm{A}}-\mathrm{I}_{\mathrm{B}}=57.6 \mathrm{MR}^2-25.6 \mathrm{MR}^2=32 \mathrm{MR}^2
\end{aligned}$

</details>

---

### Q71. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Four identical uniform solid spheres each of same mass ' $M$ ' and radius ' $R$ ' are placed touching each other as shown in figure with centres A, B, C, D. $\mathrm{I}_{\mathrm{A}}, \mathrm{I}_{\mathrm{B}}, \mathrm{I}_{\mathrm{C}}, \mathrm{I}_{\mathrm{D}}$ are the moment of inertia of these spheres respectively about an axis passing through centre and perpendicular to the plane, then
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/w5dXWH5zLWYI1nfSfEOWR1lx9yqjL6o03Jicg5ZCKqY.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{I}_{\mathrm{A}}>\mathrm{I}_{\mathrm{B}}>\mathrm{I}_{\mathrm{C}}>\mathrm{I}_{\mathrm{D}}$
- **(B)** $\mathrm{I}_{\mathrm{D}}>\mathrm{I}_{\mathrm{C}}>\mathrm{I}_{\mathrm{B}}>\mathrm{I}_{\mathrm{A}}$
- **(C)** $\mathrm{I}_{\mathrm{A}}=\mathrm{I}_{\mathrm{D}}>\mathrm{I}_{\mathrm{B}}=\mathrm{I}_{\mathrm{C}}$
- **(D)** $\mathrm{I}_{\mathrm{A}}=\mathrm{I}_{\mathrm{D}} < \mathrm{I}_{\mathrm{B}}=\mathrm{I}_{\mathrm{C}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{I}_{\mathrm{A}}=\mathrm{I}_{\mathrm{D}}>\mathrm{I}_{\mathrm{B}}=\mathrm{I}_{\mathrm{C}}$**

**Detailed Solution:**

$\therefore \quad$ The moment of inertia of $\mathrm{A}$ and $\mathrm{D}$ will be equal as the mass, distance, and position are similar. Similarly, the moment of inertia of B and C are equal.
$\therefore \quad$ But the moment of inertia of A and D is greater than $\mathrm{B}$ and $\mathrm{C}$ as they are at the ends.

</details>

---

### Q72. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A thin wire of length ' $L$ ' and uniform linear mass density ' $\mathrm{m}$ ' is bent into a circular coil. The moment of inertia of this coil about tangential axis and in plane of the coil is

**Options:**

- **(A)** $\frac{3 \mathrm{~mL}^2}{5 \pi^2}$
- **(B)** $\frac{3 m L^3}{8 \pi^2}$
- **(C)** $\frac{3 \mathrm{~mL}^3}{4 \pi^2}$
- **(D)** $\frac{3 \mathrm{~mL}^2}{7 \pi^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3 m L^3}{8 \pi^2}$**

**Detailed Solution:**

$\therefore \quad$ Moment of inertia of thin wire:
$$
\begin{aligned}
\mathrm{I} & =\frac{\mathrm{MR}^2}{2} \\
\mathrm{M} & =\mathrm{V} \times \mathrm{m} \text { and } \mathrm{L}=2 \pi \mathrm{R} \\
\mathrm{R} & =\frac{\mathrm{L}}{2 \pi} \\
\therefore \quad \mathrm{I} & =\frac{\mathrm{Lm}}{2}\left(\frac{\mathrm{L}}{2 \pi}\right)^2 \\
\mathrm{I} & =\frac{\mathrm{mL}^3}{8 \pi^2}
\end{aligned}
$$
$\therefore \quad$ Using Parallel axis theorem:
$$
\begin{aligned}
& I^{\prime}=I+M R^2 \\
& I=\frac{m L^3}{8 \pi^2}+L m\left(\frac{L}{2 \pi}\right)^2 \\
& I=\frac{3 m L^3}{8 \pi^2}
\end{aligned}
$$

</details>

---

### Q73. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A thin uniform circular disc of mass ' $\mathrm{M}$ ' and radius ' $R$ ' is rotating with angular velocity ' $\omega$ ', in a horizontal plane about an axis passing through its centre and perpendicular to its plane. Another disc of same radius but of mass $\left(\frac{M}{2}\right)$ is placed gently on the first disc co-axially. The new angular velocity will be

**Options:**

- **(A)** $\frac{2}{3} \omega$
- **(B)** $\frac{4}{5} \omega$
- **(C)** $\frac{5}{4} \omega$
- **(D)** $\frac{3}{2} \omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2}{3} \omega$**

**Detailed Solution:**

Angular momentum $=\mathrm{I} \omega$ By conservation of angular momentum, $\mathrm{I}_1 \omega_1=\mathrm{I}_2 \omega_2$
Here, $I_1=\frac{M^2}{2}, I_2=\frac{(M+M / 2)}{2} R^2=\frac{3 M^2}{4}$
$$
\begin{aligned}
& \therefore \quad \frac{\mathrm{MR}^2}{2} \omega_1=\frac{3 \mathrm{MR}^2}{4} \omega_2 \\
& \therefore \quad \omega_2=\frac{2}{3} \omega_1
\end{aligned}
$$

</details>

---

### Q74. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\mathrm{I}_1$ is the moment of inertia of a circular disc about an axis passing through its centre and perpendicular to the plane of disc. $I_2$ is its moment of inertia about an axis AB perpendicular to plane and parallel to axis $\mathrm{CM}$ at a distance $\frac{2 R}{3}$ from centre. The ratio of $I_2$ and $I_1$ is $x= 9$. The value of ' $x$ ' is ( $\mathrm{R}=$ radius of the disc)
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/eR64Dx29ZWluNv6bI-GUqAC8JUW5zuGCKkr_AqOyjJk.original.fullsize.png">

**Options:**

- **(A)** 9
- **(B)** 12
- **(C)** 15
- **(D)** 17

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 17**

**Detailed Solution:**

Using Parallel axis theorem,
$$
\mathrm{I}_2=\mathrm{I}_1+\mathrm{Mh}^2
$$
For a disc, $\mathrm{I}_1=\frac{1}{2} \mathrm{MR}^2$ and given that, $\mathrm{h}=\frac{2 \mathrm{R}}{3}$
$$
\begin{aligned}
\therefore \quad I_2 & =I_1+M h^2 \\
I_2 & =\frac{1}{2} M R^2+M\left(\frac{2 R}{3}\right)^2 \\
I_2 & =\frac{17 M R^2}{18} \\
\therefore \quad I_2: I_1 & =\frac{17 M R^2}{18}: \frac{1}{2} M R^2 \\
I_2: I_1 & =17: 9
\end{aligned}
$$
On comparing
$$
x=17
$$

</details>

---

### Q75. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

From a disc of mass ' $M$ ' and radius ' $R$ ', a circular hole of diameter ' $R$ ' is cut whose rim passes through the centre. The moment of inertia of the remaining part of the disc about perpendicular axis passing through the centre is

**Options:**

- **(A)** $\frac{13 \mathrm{MR}^2}{32}$
- **(B)** $\frac{11 \mathrm{MR}^2}{32}$
- **(C)** $\frac{9 \mathrm{MR}^2}{32}$
- **(D)** $\frac{7 \mathrm{MR}^2}{32}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{13 \mathrm{MR}^2}{32}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/u8153xw42Tks5EVd2SkC9FcyB0jBRE1kj1oDqa2qHOc.original.fullsize.png">

Moment of inertia of disc is given by
$\mathrm{I}_{\text {disc }}=\mathrm{I}_{\mathrm{f}}+\mathrm{I}_{\text {hole }}$
.... $\left\{\mathrm{I}_{\mathrm{f}}=\right.$ M.I. of remaining part $\}$
$\begin{aligned}
& \therefore \quad \mathrm{I}_{\mathrm{r}}=\mathrm{I}_{\text {dise }}-\mathrm{I}_{\text {hole }} \\
& \mathrm{I}_{\text {disc }}=\frac{\mathrm{MR}^2}{2}
\end{aligned}$
By parallel axes theorem we get,
$\mathrm{I}_{\text {hole }}=\left[\frac{\frac{\mathrm{M}}{4}\left(\frac{\mathrm{R}}{2}\right)^2}{2}+\frac{\mathrm{M}}{4}\left(\frac{\mathrm{R}}{2}\right)^2\right]$
$\ldots\left\{\begin{array}{l}\because \mathrm{M}_{\text {bole }}=\frac{\mathrm{M}_{\text {dive }}}{4} \\ \because \text { the surface density is same }\end{array}\right\}$
$\therefore \quad \mathrm{I}_{\text {hole }}=\left[\frac{\mathrm{MR}^2}{32}+\frac{\mathrm{MR}^2}{16}\right]$
Substituting eq (iii) and eq (ii) in eq (i) we get,
$\begin{aligned}
\mathrm{I}_{\mathrm{r}} & =\frac{\mathrm{MR}^2}{2}-\frac{\mathrm{MR}^2}{32}-\frac{\mathrm{MR}^2}{16} \\
& =\mathrm{MR}^2\left[\frac{1}{2}-\frac{1}{32}-\frac{1}{16}\right] \\
& =\frac{13}{32} \mathrm{MR}^2
\end{aligned}$

</details>

---

### Q76. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Two bodies have their moments of inertia I and 2I respectively about their axis of rotation. If their kinetic energies of rotation are equal, their angular momenta will be in the ratio

**Options:**

- **(A)** $1: 2$
- **(B)** $\sqrt{2}: 1$
- **(C)** $2: 1$
- **(D)** $1: \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1: \sqrt{2}$**

**Detailed Solution:**

The equation for angular momentum is
$\mathrm{L}=\sqrt{2 \mathrm{~K}_{\mathrm{Rot}} \times \mathrm{I}}$
So, $\mathrm{L} \propto \sqrt{\mathrm{I}}$
$\therefore \quad$ The ratio of angular momentum of the two bodies is
$\frac{\mathrm{L}_1}{\mathrm{~L}_2}=\sqrt{\frac{\mathrm{I}_1}{\mathrm{I}_2}}$
$\frac{\mathrm{L}_1}{\mathrm{~L}_2}=\sqrt{\frac{\mathrm{I}}{2 \mathrm{I}}} \quad \ldots . .\left(\right.$ given $\left.\mathrm{I}_2=2 \mathrm{I}\right)$
$\therefore \quad \frac{\mathrm{L}_1}{\mathrm{~L}_2}=\frac{1}{\sqrt{2}}$

</details>

---

### Q77. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Radius of gyration of a thin uniform circular disc about the axis passing through its centre and perpendicular to its plane is $\mathrm{K}_{\mathrm{c}}$. Radius of gyration of the same disc about a diameter of the disc is $K_d$. The ratio $K_c: K_d$ is

**Options:**

- **(A)** $\sqrt{2}: 1$
- **(B)** $1: \sqrt{2}$
- **(C)** $2: 1$
- **(D)** $1: 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{2}: 1$**

**Detailed Solution:**

Let the radius of the disc be $\mathrm{R}$
$$
\begin{array}{ll}
\therefore & \mathrm{K}_{\mathrm{c}}=\frac{\mathrm{R}}{\sqrt{2}} \\
\therefore & \mathrm{K}_{\mathrm{d}}=\frac{\mathrm{R}}{2}
\end{array}
$$

Taking the ratio,
$$
\therefore \quad \frac{\mathrm{K}_{\mathrm{c}}}{\mathrm{K}_{\mathrm{d}}}=\frac{\frac{\mathrm{R}}{\sqrt{2}}}{\frac{\mathrm{R}}{2}}=\frac{\sqrt{2}}{1}
$$

</details>

---

### Q78. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The moment of inertia of a uniform square plate about an axis perpendicular to its plane and passing through the centre is $\frac{\mathrm{Ma}^2}{6}$, where ' $\mathrm{M}$ ' is the mass and ' $a$ ' is the side of square plate. Moment of inertia of this plate about an axis perpendicular to its plane and passing through one of its corners is

**Options:**

- **(A)** $\frac{\mathrm{Ma}^2}{6}$
- **(B)** $\frac{2 \mathrm{Ma}^2}{3}$
- **(C)** $\frac{\mathrm{Ma}^2}{3}$
- **(D)** $\frac{2 \mathrm{Ma}^2}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2 \mathrm{Ma}^2}{3}$**

**Detailed Solution:**

$\begin{aligned} \mathrm{I}_0 & =\frac{\mathrm{Ma}^2}{6} \\ \mathrm{AB} & =\sqrt{2 \mathrm{a}^2}=\sqrt{2} \mathrm{a} \\ \therefore \quad \mathrm{AO} & =\frac{\mathrm{a}}{\sqrt{2}}=\mathrm{h} \\ \therefore \quad \mathrm{I}_{\mathrm{A}} & =\mathrm{I}_0+\mathrm{Mh}^2 \\ & =\frac{\mathrm{Ma}^2}{6}+\frac{\mathrm{Ma}^2}{2} \\ & =\frac{8 \mathrm{Ma}^2}{12}=\frac{2}{3} \mathrm{Ma}^2\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/PNjG2xU0JAQ_j9D6_pErvLJOgCHB2rt_QZV1tM18Vgg.original.fullsize.png">

</details>

---

### Q79. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two spheres each of mass ' $M$ ' and radius $\frac{R}{2}$ are connected at the ends of massless rod of length ' $2 \mathrm{R}$ '. What will be the moment of inertia of the system about an axis passing through centre of one of the spheres and perpendicular to the rod?

**Options:**

- **(A)** $\frac{2}{3} \mathrm{MR}^2$
- **(B)** $\frac{5}{2} \mathrm{MR}^2$
- **(C)** $\frac{5}{21} \mathrm{MR}^2$
- **(D)** $\frac{21}{5} \mathrm{MR}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{21}{5} \mathrm{MR}^2$**

**Detailed Solution:**

From parallel axis theorem,
$\mathrm{I}_{\mathrm{o}}=\mathrm{I}_{\mathrm{c}}+\mathrm{Mh}^2$
Let the moment of inertia of sphere 1 be
$\mathrm{I}_1=\frac{2}{5} \mathrm{M}\left(\frac{\mathrm{R}}{2}\right)^2+\mathrm{M}(2 \mathrm{R})^2$
and,
Let the moment of inertia of sphere 2 be
$\mathrm{I}_2=\frac{2}{5} \mathrm{M}\left(\frac{\mathrm{R}}{2}\right)^2$
Moment of inertia of the rod $\mathrm{I}_3=0$
$\therefore \quad$ Moment of inertia of the system,
$\begin{aligned}
\mathrm{I} & =\mathrm{I}_1+\mathrm{I}_2+\mathrm{I}_3 \\
\mathrm{I} & =\frac{2}{5} \mathrm{M}\left(\frac{\mathrm{R}}{2}\right)^2+\mathrm{M}(2 \mathrm{R})^2+\frac{2}{5} \mathrm{M}\left(\frac{\mathrm{R}}{2}\right)^2 \\
& =\frac{4}{5} \mathrm{M}\left(\frac{\mathrm{R}}{2}\right)^2+4 \mathrm{MR}^2 \\
& =\frac{1}{5} \mathrm{MR}^2+4 \mathrm{MR}^2 \\
& =\frac{21}{5} \mathrm{MR}^2
\end{aligned}$

</details>

---

### Q80. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Seven identical discs each of mass $M$ and radius $\mathrm{R}$ are arranged in a hexagonal plane pattern so as to touch each neighbour disc as shown in the figure. The moment of inertia of the system of seven discs about an axis passing through the centre of central disc and normal to the plane of all discs is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/YG4sgyy0EN_ShgmcWJ2WayPsCBtrnuC6R9nWs2No99s.original.fullsize.png">

**Options:**

- **(A)** $\frac{7}{2} \mathrm{MR}^2$
- **(B)** $\frac{13}{2} \mathrm{MR}^2$
- **(C)** $\frac{29}{2} \mathrm{MR}^2$
- **(D)** $\frac{55}{2} \mathrm{MR}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{55}{2} \mathrm{MR}^2$**

**Detailed Solution:**

M.I of a circular disc $=\frac{\mathrm{MR}^2}{2}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/j8SFrB_x5IUP2rg9_abrdrE0lZF4wIFVQ9fUNGaCGOY.original.fullsize.png">

Using parallel axis theorem, M.I. about origin $\mathrm{I}=\mathrm{I}_{\mathrm{cm}}+6 \mathrm{I}$
where, $\mathrm{I}_{\mathrm{cm}}=\mathrm{M}$. I of the central disc $\mathrm{I}^{\prime}=\mathrm{M}$. I of the each disc about the given axis.
$\therefore \quad \mathrm{I}=\frac{\mathrm{MR}^2}{2}+6\left(\mathrm{I}_{\mathrm{cm}}+\mathrm{MD}^2\right)$
$=\frac{\mathrm{MR}^2}{2}+6\left(\frac{\mathrm{MR}^2}{2}+4 \mathrm{MR}^2\right) \quad \ldots(\because \mathrm{D}=2 \mathrm{R})$
$\begin{aligned}
& =\frac{\mathrm{MR}^2}{2}+6\left(\frac{\mathrm{MR}^2+8 \mathrm{MR}^2}{2}\right) \\
& =\frac{55 \mathrm{MR}^2}{2}
\end{aligned}$

</details>

---

### Q81. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two discs of same mass ąnd same thickness (t) are made from two different materials of densities ' $\mathrm{d}_1$ ' and ' $\mathrm{d}_2$ ' respectively. The ratio of the moment of inertia $\mathrm{I}_1$ to $\mathrm{I}_2$ of two discs about an axis passing through the centre and perpendicular to the plane of disc is

**Options:**

- **(A)** $\mathrm{d}_1: \mathrm{d}_2$
- **(B)** $\mathrm{d}_2: \mathrm{d}_1$
- **(C)** $1: \mathrm{d}_1 \mathrm{~d}_2$
- **(D)** $1: \mathrm{d}_1^2 \mathrm{~d}_2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{d}_2: \mathrm{d}_1$**

**Detailed Solution:**

The ratio of moments of inertia of two discs of the same mass and same thickness but of different densities is given by $\frac{\mathrm{I}_1}{\mathrm{I}_2}=\frac{\mathrm{R}_1^2}{\mathrm{R}_2^2}=\frac{\mathrm{d}_2}{\mathrm{~d}_1}$

</details>

---

### Q82. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A square lamina of side ' $b$ ' has same mass as a disc of radius ' $R$ ' the moment of inertia of the two objects about an axis perpendicular to the plane and passing through the centre is equal. The ratio $\frac{\mathrm{b}}{\mathrm{R}}$ is

**Options:**

- **(A)** $1:1$
- **(B)** $\sqrt{3}:1$
- **(C)** $\sqrt{6}:1$
- **(D)** $1:\sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{3}:1$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{I}_{\text {lamina }}=\frac{\mathrm{Mb}^2}{6} \\ & \mathrm{I}_{\text {disc }}=\frac{\mathrm{MR}^2}{2} \\ & \text { Given } \frac{\mathrm{Mb}^2}{6}=\frac{\mathrm{MR}^2}{2} \\ & \quad \frac{\mathrm{b}^2}{\mathrm{R}^2}=3 \\ & \therefore \quad \frac{\mathrm{b}}{\mathrm{R}}=\frac{\sqrt{3}}{1}\end{aligned}$

</details>

---

### Q83. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A ring, a solid sphere and a disc have same mass and radius. Which of them have the largest moment of inertia?

**Options:**

- **(A)** All have the same moment of inertia
- **(B)** Solid sphere only
- **(C)** Ring only
- **(D)** Disc only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Ring only**

**Detailed Solution:**

Formula for moment of inertia are listed below:
$I_{\text {Ring }}=M R^2$
$I_{\text {Sphere }}=\frac{2}{5} M R^2$
$I_{\text {Disc }}=\frac{1}{2} M R^2$
Ring has largest moment of inertia as the mass is distributed far away from the axis of rotation. Above formulas just confirm that.

</details>

---

### Q84. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A thin metal rod of mass $M$ and length $L$ is into four equal parts by cutting it perpendicular to the length. If moment of inertia of the rod about an axis passing through its centre and perpendicular to its axis it $I$, then moment of inertia of each part about the similar axis is

**Options:**

- **(A)** $\frac{I}{64}$
- **(B)** $\frac{I}{8}$
- **(C)** $\frac{I}{16}$
- **(D)** $\frac{I}{32}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{I}{64}$**

**Detailed Solution:**

We know, that moment of inertia has following functional dependence on mass and length of the rod:
$I \propto M L^2$
If thin rod is split into four equal parts.
$\begin{aligned} & M^{\prime}=\frac{M}{4} \\ & L^{\prime}=\frac{L}{4} \\ & \therefore I^{\prime} \propto \frac{M}{4}\left(\frac{L^2}{16}\right) \\ & \Rightarrow I^{\prime} \propto \frac{M L^2}{64} \\ & \Rightarrow I^{\prime}=\frac{I}{64}\end{aligned}$

</details>

---

### Q85. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A solid sphere has mass ' $M$ ' and radius ' $R$ '. Its moment of inertia about a parallel axis passing through a point at a distance $\frac{R}{2}$ from its centre is

**Options:**

- **(A)** $\frac{8 \mathrm{MR}^2}{11}$
- **(B)** $\frac{11 \mathrm{MR}^2}{18}$
- **(C)** $\frac{7 \mathrm{MR}^2}{10}$
- **(D)** $\frac{13 \mathrm{MR}^2}{20}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{13 \mathrm{MR}^2}{20}$**

**Detailed Solution:**

Concept: Parallel axis theorem application.
The moment of inertia for a sphere about the central rotation axis is:
$\mathrm{I}_{\text {sphere }}=\frac{2}{5} \mathrm{MR}^2$
See the diagram below,
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/UsD4n3TaDppw-kAz3y72m73aYJtRkUnf-iU06SPAFGI.original.fullsize.png">

To find the moment of inertia about the new rotation axis we use parallel axis theorem:<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/43EfPuSowv6LSaUTdI5Y2DXMhRsb73eCkCLdZgMnV9o.original.fullsize.png">

</details>

---

### Q86. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The ratio of radius of gyration of a ring to that of a disc (both circular) of same radius and mass, about a tangential axis perpendicular to the plane is

**Options:**

- **(A)** $\frac{2}{\sqrt{3}}$
- **(B)** $\frac{\sqrt{2}}{1}$
- **(C)** $\frac{\sqrt{3}}{2}$
- **(D)** $\frac{2}{\sqrt{5}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\sqrt{3}}{2}$**

**Detailed Solution:**

Radius of gyration is given by, $K=\sqrt{\frac{I}{m}}$
We know moment of inertia for the ring $I_{\text {disc }}=\frac{1}{2} m R^2$ and the disc $I_{\text {ring }}=m R^2$ about its central axis perpendicular to its plane.
Using parallel axis theorem, the moment of inertia about a tangential axis perpendicular to the plane can be easily obtained using,
$I^{\prime}=I+m R^2$
The radius of gyration is defined as:
$\begin{aligned}
& K=\sqrt{\frac{I}{m}} \\
& \therefore K_{\text {disc }}=\sqrt{\frac{\frac{1}{2} m R^2+m R^2}{m}}=\sqrt{\frac{3}{2}} R \\
& \therefore K_{\text {ring }}=\sqrt{\frac{m R^2+m R^2}{m}}=\sqrt{2} R
\end{aligned}$
Thus, the ratio of the radius of gyration of a ring to that of a disc of same radius and mass, about a tangential axis perpendicular to the plane is:
$\frac{K_{\text {disc }}}{K_{\text {ring }}}=\frac{\sqrt{3 / 2}}{\sqrt{2}}=\frac{\sqrt{3}}{2}$

</details>

---

### Q87. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two discs A and B each of radius $r$ and mass $m$ are attached as shown to form a system. The moment of inertia of this system about an axis perpendicular to the plane of the discs and passing through the center of disc $\mathrm{A}$ is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/aOyQXiudpU7wHSGA7-cYJi9V5hHjMugWouNYM6gLeQM.original.fullsize.png">

**Options:**

- **(A)** $\frac{9}{2} m r^2$
- **(B)** $m r^2$
- **(C)** $2 m r^2$
- **(D)** $5 m r^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5 m r^2$**

**Detailed Solution:**

The moment of inertia of the disc about the centroidal axis is $\frac{m r^2}{2}$
The moment of inertia of the disc at A about the axis passing through B is given using the parallel axis theorem as $\frac{m r^2}{2}+m(2 r)^2$
Thus, the total moment of inertia of the whole system is given as $\frac{m r^2}{2}+\frac{m r^2}{2}+m(2 r)^2=5 m r^2$

</details>

---

### Q88. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Match the following columns $(\mathrm{R}=$ radius, $\mathrm{k}=$ Radius of gyration $)$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/NN5I4KjI63yS6XAFTvns6AzVeViMyoeHc0buYjPMy5w.original.fullsize.png">

**Options:**

- **(A)** $(\mathrm{A})-(\mathrm{p}) ;(\mathrm{B})-(\mathrm{R}) ;(\mathrm{C})-(\mathrm{Q}) ;(\mathrm{D})-(\mathrm{s})$
- **(B)** $(\mathrm{A})-(\mathrm{p}) ;(\mathrm{B})-(\mathrm{Q}) ;(\mathrm{C})-(\mathrm{s}) ;(\mathrm{D})-(\mathrm{P})$
- **(C)** $(\mathrm{A})-(\mathrm{Q}) ;(\mathrm{B})-(\mathrm{R}) ;(\mathrm{C})-(\mathrm{p}) ;(\mathrm{D})-(\mathrm{S})$
- **(D)** $(\mathrm{A})-(\mathrm{R}) ;(\mathrm{B})-(\mathrm{P}) ;(\mathrm{C})-(\mathrm{S}) ;(\mathrm{D})-(\mathrm{Q})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\mathrm{A})-(\mathrm{R}) ;(\mathrm{B})-(\mathrm{P}) ;(\mathrm{C})-(\mathrm{S}) ;(\mathrm{D})-(\mathrm{Q})$**

**Detailed Solution:**

Relationship between radius of gyration and the moment of inertia about an axis is as follows:
$\mathrm{I}=\mathrm{mk}^2$
Summary for the different cases is listed below:
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/yJ4dinfmjcRtG0PMtGPPtjG9jUvobne04k5e927-xmM.original.fullsize.png">

</details>

---

### Q89. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A solid sphere of radius ' $R$ ' has mass ' $M$ ' the moment of inertia of a solid sphere about an axis at a distance $\left(\frac{\mathrm{R}}{2}\right)$ from the centre is

**Options:**

- **(A)** $\frac{9}{20} \mathrm{MR}^2$
- **(B)** $\frac{7}{5} \mathrm{MR}^2$
- **(C)** $\frac{9}{5} \mathrm{MR}^2$
- **(D)** $\frac{13}{20} \mathrm{MR}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{13}{20} \mathrm{MR}^2$**

**Detailed Solution:**

Using parallel axis theorem:
$I=\frac{2}{5} M R^2+M\left(\frac{R}{2}\right)^2=\frac{13}{20} M R^2$

</details>

---

### Q90. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Two circular loops $\mathrm{P}$ and $\mathrm{Q}$ of radii $r$ and $n r$ respectively are made from a uniform wire. Moment of inertia of $Q$ about its axis is four times that of $\mathrm{P}$ about its axis. The value of $n$ is

**Options:**

- **(A)** $(2)^{\frac{2}{3}}$
- **(B)** $(2)^{\frac{1}{3}}$
- **(C)** $2$
- **(D)** $\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(2)^{\frac{2}{3}}$**

**Detailed Solution:**

Given, $I_Q=4 I_P$.
Let $m$ be the mass per unit length of wire.
$\therefore m \times 2 \pi n r(n r)^2=4\left[(m 2 \pi r) r^2\right]$
Implies $n^3=4$
$\Rightarrow n=4^{1 / 3}$

</details>

---

### Q91. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Five solid spheres each of mass $m$ and radius $r$ are rotating about an axis $A$ as shown in figure. Hence the moment of inertia of the system about the axis of rotation A-A' as shown in figure. Hence the moment of inertia of the system about the axis of rotation A-A' is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/XGeXmfheSSHRr92frGMWiOtDw2oZaZsr_gmvnURZDbg.original.fullsize.png">

**Options:**

- **(A)** $6 m r^2$
- **(B)** $5 m r^2$
- **(C)** $3 m r^2$
- **(D)** $4 m r^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4 m r^2$**

**Detailed Solution:**

Moment of inertia of a sphere about diameter is $\frac{2}{5} m r^2$
Moment of inertia of a sphere about it tangent using parallel axis theorem
$\begin{aligned} & I=I_{\mathrm{am}}+m r^2=\frac{2}{5} m r^2+m r^2=\frac{7}{5} m r^2 \\ & I_{\text {total }}=3\left(\frac{2}{5} m r^2\right)+2\left(\frac{7}{5} m r^2\right)=\frac{20}{5} m r^2=4 m r^2\end{aligned}$

</details>

---

### Q92. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The moment of inertia of a ring about an axis perpendicular to its plane and passing through its center is $4 \mathrm{~kg} \mathrm{~m}^2$. Its moment of inertia about the tangent in the plane is

**Options:**

- **(A)** $6 \mathrm{~kg} \mathrm{~m}^2$
- **(B)** $8 \mathrm{~kg} \mathrm{~m}^2$
- **(C)** $4 \mathrm{~kg} \mathrm{~m}^2$
- **(D)** $2 \mathrm{~kg} \mathrm{~m}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $6 \mathrm{~kg} \mathrm{~m}^2$**

**Detailed Solution:**

Ring has moment of inertia $M R^2$ about the symmetric central axis. Using perpendicular axis theorem one can get moment of inertia about the planar diagonal as $\frac{M R^2}{2}$
Now, using to the parallel axis theorem, we shift by a distance R to be at the tangential position:
$I_t=\frac{1}{2} M R^2+M R^2=\frac{3}{2} M R^2$
Given $M R^2=4 \mathrm{kgm}^2$ :
$I_t=\frac{3}{2} \times 4 \mathrm{kgm}^2=6 \mathrm{kgm}^2$

</details>

---

### Q93. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A body is rotating about its own axis. Its rotational kinetic energy is ' $x$ ' and its angular momentum is ' $y$ '. Hence its moment of inertia about the axis is

**Options:**

- **(A)** $\frac{x^2}{2 y}$
- **(B)** $\frac{y}{2 x}$
- **(C)** $\frac{x}{2 y}$
- **(D)** $\frac{y^2}{2 x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{y^2}{2 x}$**

**Detailed Solution:**

The kinetic energy of a rotating body is given by $x=\frac{I \omega^2}{2}$ and the angular momentum is given by $\mathrm{y}=\mathrm{I} \omega$, where $\mathrm{I}$ is the moment of inertia, $\omega$ the angular velocity.
Therefore, we can write,
$\mathrm{y}^2=2 \mathrm{I}\left(\frac{\mathrm{I} \omega^2}{2}\right)=2 \mathrm{Ix}$
On re-writing,
$I=\frac{y^2}{2 x}$

</details>

---

### Q94. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The moment of inertia of a thin uniform rod of mass ' $M$ ' and length ' $L$ ' about an axis passing through a point at a distance $\frac{L}{4}$ from one of its ends and perpendicular to the length of the rod is

**Options:**

- **(A)** $\frac{\mathrm{ML}^2}{48}$
- **(B)** $\frac{7 \mathrm{ML}^2}{48}$
- **(C)** $\frac{5 \mathrm{ML}^2}{48}$
- **(D)** $\frac{9 \mathrm{ML}^2}{48}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{7 \mathrm{ML}^2}{48}$**

**Detailed Solution:**

The moment of inertia of the rod about an axis passing through the center and perpendicular to its length is given by
$\mathrm{I}_0=\frac{\mathrm{ML}^2}{12}$
Hence by parallel axis theorem,
$\mathrm{I}=\mathrm{I}_0+\mathrm{M}\left(\frac{\mathrm{L}}{4}\right)^2=\frac{\mathrm{ML}^2}{12}+\frac{\mathrm{ML}^2}{16}=\frac{7 \mathrm{ML}^2}{48}$

</details>

---

### Q95. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two circular loops $\mathrm{P}$ and $\mathrm{Q}$ are made from a uniform wire. The radii of $P$ and $Q$ are $R_1$ and $R_2$ respectively. The moments of inertia about their own axis are $\mathrm{I}_{\mathrm{P}}$ and $\mathrm{I}_{\mathrm{Q}}$ respectively. If $\frac{\mathrm{I}_{\mathrm{P}}}{\mathrm{I}_{\mathrm{Q}}}=\frac{1}{8}$ then $\frac{\mathrm{R}_2}{\mathrm{R}_1}$ is

**Options:**

- **(A)** 4
- **(B)** 3
- **(C)** 2
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

$$
\mathrm{I}_1=\mathrm{M}_1 \mathrm{R}_1^2, \mathrm{I}_2=\mathrm{M}_1 \mathrm{R}_2^2
$$
If $\mathrm{m}$ is mas per unit length then
$$
\begin{aligned}
& \mathrm{M}_1=2 \pi \mathrm{R}_1 \mathrm{~m} \text { and } \mathrm{M}_2=2 \pi \mathrm{R}_2 \mathrm{~m} \\
& \therefore \frac{\mathrm{M}_1}{\mathrm{M}_2}=\frac{\mathrm{R}_1}{\mathrm{R}_2} \\
& \frac{\mathrm{I}_1}{\mathrm{I}_2}=\frac{\mathrm{M}_1}{\mathrm{M}_2}\left(\frac{\mathrm{R}_1}{\mathrm{R}_2}\right)^2=\frac{\mathrm{R}_1}{\mathrm{R}_2}\left(\frac{\mathrm{R}_1}{\mathrm{R}_2}\right)^2=\left(\frac{\mathrm{R}_1}{\mathrm{R}_2}\right)^3=\frac{1}{8} \\
& \therefore \frac{\mathrm{R}_1}{\mathrm{R}_2}=\frac{1}{2} \text { or } \frac{\mathrm{R}_2}{\mathrm{R}_1}=2
\end{aligned}
$$

</details>

---

### Q96. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Three solid spheres each of mass ' $M$ ' and radius ' $R$ ' are arranged as shown in the figure. The moment of inertia of the system about YY' will be
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/7iM_N-tuJvb_Cca1_L8qsz5_LegFB7VlPIJJE8dJ3N4.original.fullsize.png">

**Options:**

- **(A)** $\frac{16}{5} \mathrm{MR}^2$
- **(B)** $\frac{21}{5} \mathrm{MR}^2$
- **(C)** $\frac{7}{5} \mathrm{MR}^2$
- **(D)** $\frac{11}{5} \mathrm{MR}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{16}{5} \mathrm{MR}^2$**

**Detailed Solution:**

Moment of inertia of the upper sphere $=\frac{2}{5} \mathrm{MR}^2$
For each lower sphere M.I. $=\frac{2}{5} \mathrm{MR}^2+\mathrm{MR}^2=\frac{7}{5} \mathrm{MR}^2$
$\therefore$ Total moment of inertia $\mathrm{I}=\frac{2}{5} \mathrm{MR}^2+2 \times \frac{7}{5} \mathrm{MR}^2=\frac{16}{5} \mathrm{MR}^2$

</details>

---

### Q97. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Figure shows triangular lamina which can rotate about different axes. Moment of inertia is maximum, about the axis
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/_vIIlO7AyaZ8ciXIWTt0hjbGjELmu2eom9ScBsOuxZ8.original.fullsize.png">

**Options:**

- **(A)** PR
- **(B)** QS
- **(C)** QR
- **(D)** PQ

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) QR**

**Detailed Solution:**

The moment of inertia is given by
$$
\mathrm{I}=\sum \mathrm{m}_{\mathrm{i}} \mathrm{r}_{\mathrm{i}}^2
$$
If the distance of particles from the axis of rotation is larger, then the moment of inertia will be larger. For axis $\mathrm{QR}$, the particles will be situated at greater distances and hence the moment of inertia will be greater.

</details>

---

### Q98. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A body of mass' $\mathrm{m}$ ' and radius of gyration ' $\mathrm{K}$ ' has an angular momentum ' $L$ '. Then its angular velocity is

**Options:**

- **(A)** $\frac{\mathrm{L}}{\mathrm{mK}^2}$
- **(B)** $\frac{\mathrm{mK}^2}{\mathrm{~L}}$
- **(C)** $\frac{\mathrm{K}^2}{\mathrm{~mL}}$
- **(D)** $\mathrm{mK}^2 \mathrm{~L}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\mathrm{L}}{\mathrm{mK}^2}$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{I}=\mathrm{mK}^2 \text { and } \mathrm{L}=\mathrm{I} \omega=\mathrm{mK}^2 \omega \\ & \therefore \omega=\frac{\mathrm{L}}{\mathrm{mK}^2}\end{aligned}$

</details>

---

### Q99. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Two rings of radius ' $R$ ' and ' $n R$ ' made of same material have the ratio of moment of inertia about an axis passing through its centre and perpendicular to the plane is $1: 8$. The value of ' $n$ ' is (mass per unit length $=\lambda$ )

**Options:**

- **(A)** 2
- **(B)** 4
- **(C)** 1
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

$\begin{aligned} & \mathrm{I}_1=\frac{1}{2} \mathrm{MR}^2 \\ & \mathrm{I}_2=\frac{1}{2}(\mathrm{nM})(\mathrm{nR})^2=\frac{1}{2} \mathrm{n}^3 \mathrm{MR}^2 \\ & \therefore \frac{\mathrm{I}_1}{\mathrm{I}_2}=\frac{1}{\mathrm{n}^3}=\frac{1}{8} \\ & \therefore \mathrm{n}^3=8 \text { or } \mathrm{n}=2\end{aligned}$

</details>

---

### Q100. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Three rings each of mass ' $M$ ' and radius ' $R$ ' are arranged as shown in the figure. The moment of inertia of system about axis YY' will be
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/7ZbD6eE4_eyoxeRYRKcJ5g0rOglhpE6x9iVEuX9IRnA.original.fullsize.png">

**Options:**

- **(A)** $5 \mathrm{MR}^2$
- **(B)** $\frac{7}{2} \mathrm{MR}^2$
- **(C)** $\frac{3}{2} \mathrm{MR}^2$
- **(D)** $3 \mathrm{MR}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{7}{2} \mathrm{MR}^2$**

**Detailed Solution:**

The moment of inertia of the upper ring about its diameter is given by
$$
\mathrm{I}_1=\frac{\mathrm{MR}^2}{2}
$$
The moment of inertia of the two lower rings about a tangent in their plane is given by
$$
\mathrm{I}_2=\mathrm{I}_3=\frac{3}{2} \mathrm{MR}^2
$$
Total moment of inertia $\mathrm{I}=\mathrm{I}_1+\mathrm{I}_2+\mathrm{I}_3$
$$
=\frac{\mathrm{MR}^2}{2}+\frac{3}{2} \mathrm{MR}^2+\frac{3}{2} \mathrm{MR}^2=\frac{7}{2} \mathrm{MR}^2
$$

</details>

---

### Q101. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The moment of inertia of a circular disc of radius $2 \mathrm{~m}$ and mass $1 \mathrm{~kg}$ about an axis $\mathrm{XY}$ passing through its center of mass and perpendicular to the plane of the disc is $2 \mathrm{~kg} \mathrm{~m}^2$. The moment of inertia about an axis parallel to the axis $\mathrm{XY}$ and passing through the edge of the disc is

**Options:**

- **(A)** $6 \mathrm{~kg} \mathrm{~m}^2$
- **(B)** $4 \mathrm{~kg} \mathrm{~m}^2$
- **(C)** $10 \mathrm{~kg} \mathrm{~m}^2$
- **(D)** $8 \mathrm{~kg} \mathrm{~m}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $6 \mathrm{~kg} \mathrm{~m}^2$**

**Detailed Solution:**

About XY axis, $\mathrm{I}=\frac{1}{2} \mathrm{MR}^2=\frac{1}{2} \times 1 \times(2)^2=2 \mathrm{~kg} \cdot \mathrm{m}^2$
Moment of inertia about an axis parallel to the axis XY and passing through the edge of the disc,
$$
\mathrm{I}^{\prime}=\frac{1}{2} \mathrm{MR}^2+\mathrm{MR}^2=\frac{3}{2} \mathrm{MR}^2=6 \mathrm{~kg} \cdot \mathrm{m}^2
$$

</details>

---

### Q102. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A solid sphere of mass $M$, radius $R$ has moment of inertia ' $I$ ' about its diameter. It is recast into a disc of thickness ' $t$ ' whose moment of inertia about an axis passing through its edge and perpendicular to its plane remains ' $I$ '. Radius of the disc will be

**Options:**

- **(A)** $\frac{4 \mathrm{R}}{\sqrt{11}}$
- **(B)** $\frac{3 R}{4}$
- **(C)** $\frac{2 \mathrm{R}}{\sqrt{15}}$
- **(D)** $\frac{2 R}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2 \mathrm{R}}{\sqrt{15}}$**

**Detailed Solution:**

For solid sphere, $\mathrm{I}=\frac{2}{5} \mathrm{MR}^2$
For disc, $\mathrm{I}^{\prime}=\frac{\mathrm{MR}^{\prime 2}}{2}+\mathrm{MR}^{\prime 2}=\frac{3}{2} \mathrm{MR}^{\prime 2}$
$$
\begin{aligned}
& \because I^{\prime}=I \\
& \therefore \frac{3}{2} M R^{\prime 2}=\frac{2}{5} M^2 \\
& R^{\prime}=\frac{2}{\sqrt{15}} R
\end{aligned}
$$

</details>

---

### Q103. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The ratio of radii of gyration of a circular ring and circular disc of the same mass and radius, about an axis passing through their centres and perpendicular to their planes is

**Options:**

- **(A)** $1: \sqrt{2}$
- **(B)** $2: 1$
- **(C)** $\sqrt{2}: 1$
- **(D)** $3: 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{2}: 1$**

**Detailed Solution:**

$\mathrm{I}=\mathrm{MK}^2$
For a ring, $\mathrm{MR}^2=\mathrm{MK}_{\mathrm{r}}{ }^2 \quad \therefore \mathrm{K}_{\mathrm{r}}=\mathrm{R}$
For a disc, $\frac{\mathrm{MR}^2}{2}=\mathrm{MK}_{\mathrm{d}}^2 \quad \therefore \mathrm{K}_{\mathrm{d}}=\frac{\mathrm{R}}{\sqrt{2}}$
$$
\frac{\mathrm{K}_{\mathrm{r}}}{\mathrm{K}_{\mathrm{d}}}=\sqrt{2}
$$

</details>

---

### Q104. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The moment of inertia of a uniform square plate about an axis perpendicular to its plane and passing through the centre is $\frac{\mathrm{Ma}^{2}}{6}$ where $\mathrm{M}$ is the mass and $\mathrm{a}^{\prime}$ ' is the side of square plate. Moment of inertia of this plate about an axis perpendicular to its plane and passing through one of its corner is

**Options:**

- **(A)** $\frac{\mathrm{Ma}^{2}}{3}$
- **(B)** $\frac{3}{\mathrm{Ma}^{2}}$
- **(C)** $\frac{3 \mathrm{Ma}^{2}}{2}$
- **(D)** $\frac{2 \mathrm{Ma}^{2}}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2 \mathrm{Ma}^{2}}{3}$**

**Detailed Solution:**

$I_{o}=\frac{M a^{2}}{6}$
$A B=\sqrt{2 a^{2}}=\sqrt{2} a \quad \quad A O=\frac{a}{\sqrt{2}}=h$
$\therefore I_{A}=I_{o}+M h^{2}$
$=\frac{\mathrm{Ma}^{2}}{6}+\frac{\mathrm{Ma}^{2}}{2}=\frac{\mathrm{Ma}^{2}+3 \mathrm{Ma}^{2}}{6}=\frac{4 \mathrm{Ma}^{2}}{6}=\frac{2 \mathrm{Ma}^{2}}{3}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/U2j4vq4bTwnah10o2xuSI99vYeT7gum-FpUWzNSojxU.original.fullsize.png">

</details>

---

### Q105. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the spherical planet of mass ' $\mathrm{M}^{\prime}$ and radius 'R' suddenly shrinks to half its size,  its mass reduces to half. The new moment of inertia of the planet about its diameter is

**Options:**

- **(A)** $\frac{\mathrm{MR}^{2}}{10}$
- **(B)** $\frac{\mathrm{MR}^{2}}{20}$
- **(C)** $\frac{2}{3} \mathrm{MR}^{2}$
- **(D)** $\frac{2}{5} \mathrm{MR}^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\mathrm{MR}^{2}}{20}$**

**Detailed Solution:**

$\mathrm{I}_{1}=\frac{2}{5} \mathrm{MR}^{2}$
$\mathrm{I}_{2}=\frac{2}{5} \frac{M}{2} \times\left(\frac{R}{2}\right)^{2}=\frac{2}{5} \times \frac{M}{2} \times \frac{R^{2}}{4}=\frac{M R^{2}}{20}$

</details>

---

### Q106. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two circular rings 'A' and 'B' of radii 'nR' and 'R' are made from the same wire. The
moment of inertia of 'A' about an axis passing through the centre and
perpendicular to the plane of 'A' is 64 times that of the ring 'B'. The value of ' $n$ ' is

**Options:**

- **(A)** 8
- **(B)** 3
- **(C)** 6
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

$\frac{\mathrm{I}_{\mathrm{A}}}{\mathrm{I}_{\mathrm{B}}}=\frac{64}{1}$
$64=\frac{m_{A} r_{A}^{2}}{m_{B} r_{B}^{2}}=\frac{2 \pi r_{A}}{2 \pi r_{B}} \frac{r_{A}^{2}}{r_{B}^{2}}=\frac{r_{A}^{3}}{r_{B}^{3}}=n^{3}$
$\therefore n=4$

</details>

---

### Q107. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Three point masses, each of mass 'm' are placed at the corners of an equilateral
triangle of side $' \ell^{\prime}$. The moment of inertia of the system about an axis along any
one side of the triangle is

**Options:**

- **(A)** $\frac{1}{3} \mathrm{~m} \ell^{2}$
- **(B)** $\frac{3}{2} \mathrm{~m} \ell^{2}$
- **(C)** $\frac{3}{4} \mathrm{~m} \ell^{2}$
- **(D)** $\mathrm{~m} \ell^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{4} \mathrm{~m} \ell^{2}$**

**Detailed Solution:**

$O P=\sqrt{\ell^{2}-\frac{\ell^{2}}{4}}=\frac{\sqrt{3}}{2} \ell$
$\therefore \mathrm{MOI}=\mathrm{m}\left(\frac{\sqrt{3} \ell}{2}\right)^{2}=\frac{3}{4} \mathrm{~m} \ell^{2}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/V1gI0oPubrsEOoqjfY0oEoPdjyIVfCuS4mnqNwixPQk.original.fullsize.png">

</details>

---

### Q108. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two discs having moment of inertia $\mathrm{l}_{1}$ and $\mathrm{I}_{2}$ are made from same material have
same mass. Their thickness and radii are $\mathrm{t}_{1}, \mathrm{t}_{2}$ and $\mathrm{R}_{1}, \mathrm{R}_{2}$ respectively. The relation
between moment of inertia of each disc about an axis passing through its centre
and perpendicular to its plane and its thickness is

**Options:**

- **(A)** $\mathrm{I}_{1} \mathrm{t}_{1}=\mathrm{I}_{2} \mathrm{t}_{2}$
- **(B)** $\mathrm{I}_{1} \mathrm{t}_{2}^{2}=\mathrm{I}_{2} \mathrm{t}_{1}^{2}$
- **(C)** $\mathrm{I}_{1} \mathrm{t}_{2}=\mathrm{I}_{2} \mathrm{t}_{1}$
- **(D)** $\mathrm{I}_{1} \mathrm{t}_{1}^{2}=\mathrm{I}_{2} \mathrm{t}_{2}^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{I}_{1} \mathrm{t}_{1}=\mathrm{I}_{2} \mathrm{t}_{2}$**

**Detailed Solution:**

$I_{1}=\frac{m R_{1}^{2}}{2}$
$I_{2}=\frac{m R_{2}^{2}}{2}$
$\frac{I_{1}}{I_{2}}=\frac{R_{1}^{2}}{R_{2}^{2}}=\frac{t_{2}}{t_{1}}$
$\therefore \mathrm{I}_{1} \mathrm{t}_{1}=\mathrm{I}_{2} \mathrm{t}_{2}$
$\mathrm{m}_{1}=\pi \mathrm{R}_{1}^{2} \mathrm{t}_{1}$
$\mathrm{~m}_{2}=\pi \mathrm{R}_{2}^{2} \mathrm{t}_{2}$\
$\mathrm{m}_{1}=\mathrm{m}_{2}$
$\therefore \mathrm{R}_{1}^{2} \mathrm{t}_{1}=\mathrm{R}_{2}^{2} \mathrm{t}_{2}$

</details>

---

### Q109. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Three points masses, each of mass 'm' are placed at the corners of an equilateral
triangle of side $\ell^{\prime}$. The moment of inertia of the system about an axis passing
through one of the vertices and parallel to the side joining other two vertices, will be

**Options:**

- **(A)** $\frac{3}{2} \mathrm{~m} \ell^{2}$
- **(B)** $\frac{3}{4} \mathrm{~m} \ell^{2}$
- **(C)** $\frac{1}{2} \mathrm{~m} \ell^{2}$
- **(D)** $\frac{1}{4} \mathrm{~m} \ell^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3}{2} \mathrm{~m} \ell^{2}$**

**Detailed Solution:**

(D)
$\begin{aligned} I &=2 \mathrm{mh}^{2} \\ & \mathrm{~h}=\ell \sin 60^{\circ}=\ell \times \frac{\sqrt{3}}{2} \\ I &=2 \mathrm{~m} \times \frac{3}{4} \cdot \ell^{2}=\frac{3}{2} \mathrm{~m} \ell^{2} \end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/uf6CzOiHW6RUC6URHbX0sI02H86xQpT_J1zEmlYW8IY.original.fullsize.png">

</details>

---

### Q110. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two circular loops $\mathrm{A}$ and $\mathrm{B}$ of radii ${ }^{\prime} \mathrm{R}^{\prime}$ and ' $\mathrm{NR}^{\prime}$ respectively are made from a
uniform wire. Moment of inertia of B about its axis is 3 times that of A about its
axis. The value of $\mathrm{N}$ is

**Options:**

- **(A)** $[5]^{\frac{1}{3}}$
- **(B)** $[3]^{\frac{1}{3}}$
- **(C)** $[4]^{\frac{1}{3}}$
- **(D)** $[2]^{\frac{1}{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $[3]^{\frac{1}{3}}$**

**Detailed Solution:**

(D)
If $m$ is the mass per unit length of the wire, then mass of loop $\mathrm{A} \quad=\mathrm{M}_{\mathrm{A}}=2 \pi \mathrm{Rm}$ mass of loop $\mathrm{B} \quad=\mathrm{M}_{\mathrm{B}}=2 \pi \mathrm{NRm}$ $\therefore \frac{\mathrm{M}_{\mathrm{B}}}{\mathrm{M}_{\mathrm{A}}}=\mathrm{N}$
$\mathrm{I}_{\mathrm{A}}=\mathrm{M}_{\mathrm{A}} \mathrm{R}^{2}, \mathrm{I}_{\mathrm{B}}=\mathrm{M}_{\mathrm{B}}(\mathrm{NR})^{2}=\mathrm{M}_{\mathrm{B}} \mathrm{N}^{2} \mathrm{R}^{2}$
$\therefore \frac{\mathrm{I}_{\mathrm{B}}}{\mathrm{I}_{\mathrm{A}}}=\frac{\mathrm{M}_{\mathrm{B}} \mathrm{N}^{2}}{\mathrm{M}_{\mathrm{A}}}=\mathrm{N}^{3}$
$\therefore \quad 3=\mathrm{N}^{3}$
$\therefore \quad \mathrm{N}=(3)^{\frac{1}{3}}$

</details>

---

### Q111. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A thin metal rod of mass 'M' and length 'L' is cut into 4 equal parts by cutting it
perpendicular to its length, If moment of inertia of the rod about an axis passing through its centre and perpendicular to its axis is 'I' then moment of inertia of each
part about the similar axis is

**Options:**

- **(A)** $\frac{\mathrm{I}}{16}$
- **(B)** $\frac{\mathrm{I}}{32}$
- **(C)** $\frac{\mathrm{I}}{128}$
- **(D)** $\frac{\mathrm{I}}{64}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\mathrm{I}}{64}$**

**Detailed Solution:**

(C)
$I=\frac{M L^{2}}{12}$
$\therefore \frac{I^{\prime}}{I}=\frac{\frac{M}{4} \cdot\left(\frac{L}{4}\right)^{2}}{M L^{2}}=\frac{1}{64}$

</details>

---

### Q112. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A thin uniform rod has mass 'M' and length 'L'. The moment of inertia about an axis perpendicular to it and passing through the point at a distance $\frac{\mathrm{L}}{3}$ from one of its ends, will be

**Options:**

- **(A)** $\frac{\mathrm{ML}^{2}}{12}$
- **(B)** $\frac{7}{8} \mathrm{ML}^{2}$
- **(C)** $\frac{\mathrm{ML}^{2}}{9}$
- **(D)** $\frac{\mathrm{ML}^{2}}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\mathrm{ML}^{2}}{9}$**

**Detailed Solution:**

(B)
$\begin{aligned} \mathrm{I} &=\mathrm{I}_{0}+\mathrm{Mh}^{2} \\ \mathrm{~h} &=\frac{\mathrm{L}}{2}-\frac{\mathrm{L}}{3}=\frac{\mathrm{L}}{6} \\ \mathrm{I} &=\frac{\mathrm{ML}^{2}}{12}+\mathrm{Mh}^{2} \\ &=\frac{\mathrm{ML}^{2}}{12}+\frac{\mathrm{ML}^{2}}{36} \\ &=\frac{4 \mathrm{ML}^{2}}{36}=\frac{\mathrm{ML}^{2}}{9} \end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/IDujifTsKx2zx4VGFbpfDJBVBzX4I93xHBJvgEghVwo.original.fullsize.png">

</details>

---

### Q113. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The ratio of radii of gyration of a ring to a disc (both circular) of same radii and mass, about a tangential axis perpendicular to the plane is

**Options:**

- **(A)** $\frac{2}{\sqrt{3}}$
- **(B)** $\frac{\sqrt{2}}{1}$
- **(C)** $\frac{\sqrt{3}}{\sqrt{2}}$
- **(D)** $\frac{2}{\sqrt{5}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2}{\sqrt{3}}$**

**Detailed Solution:**

(C)
$I_{\text {Ring }}=M R^{2}+M h^{2}=M R^{2}+M R^{2}=2 M R^{2}$
$I_{\text {Disc }}=\frac{1}{2} M R^{2}+M h^{2}=\frac{1}{2} M R^{2}+M R^{2}=\frac{3}{2} M R^{2}$
$\therefore k_{\text {ring }}=\sqrt{2} R$
$\quad k_{\text {disc }}=\sqrt{\frac{3}{2}} R$
$\therefore \frac{k_{\text {ring }}}{k_{\text {disc }}}=\frac{\sqrt{2} R}{\sqrt{3}}=\frac{2}{\sqrt{3}} R$

</details>

---

### Q114. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

From a disc of mass 'M' and radius 'R' a circular hole of diameter $\mathrm{R}$ is cut whose rim passes through the centre. The moment of inertia of the remaining part of the disc about perpendicular axis passing through the centre is

**Options:**

- **(A)** $\frac{11 \mathrm{MR}^{2}}{32}$
- **(B)** $\frac{7 \mathrm{MR}^{2}}{32}$
- **(C)** $\frac{9 \mathrm{MR}^{2}}{32}$
- **(D)** $\frac{13 \mathrm{MR}^{2}}{32}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{13 \mathrm{MR}^{2}}{32}$**

**Detailed Solution:**

\(\mathrm{I}_{\text {T otal disc }}=\frac{\mathrm{MR}^{2}}{2}\)
As mass is proportional to area, \(\mathrm{M}_{\text {Removed }}=\frac{\mathrm{M}}{4}\)
Now, about the same perpendicular axis:
\(I_{\text {Removed }}=\frac{M}{4} \frac{(R / 2)^{2}}{2}+\frac{M}{4}\left(\frac{R}{2}\right)^{2}=\frac{3 \mathrm{MR}^{2}}{32}\)
\(\Rightarrow \mathrm{I}_{\text {Remaining Disc }}=\mathrm{I}_{\text {Total }}-\mathrm{I}_{\text {Removed }}\)
\(=\frac{\mathrm{MR}^{2}}{2}-\frac{3 \mathrm{MR}^{2}}{32}\)
\(=\frac{13 \mathrm{MR}^{2}}{32}\)
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/562wtedgxb_cvfte7qi.png">

</details>

---

### Q115. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two rings of same mass 'M' and radius 'R' are so placed that their centre is
common and their planes are perpendicular to each other. The moment of inertia
of the system about an axis passing through the centre and perpendicular to any
one ring is

**Options:**

- **(A)** $\frac{3 \mathrm{MR}^{2}}{2}$
- **(B)** $\frac{\mathrm{MR}^{2}}{2}$
- **(C)** $\frac{2 \mathrm{MR}^{2}}{3}$
- **(D)** $\mathrm{MR}^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3 \mathrm{MR}^{2}}{2}$**

**Detailed Solution:**

$\mathrm{MR}^{2}+\frac{\mathrm{MR}^{2}}{2}=\frac{3 \mathrm{MR}^{2}}{2}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/BkS52k9lG880N9ueTe_pse5DvHXdc55Wn2-kjEueOhw.original.fullsize.png">
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/rx1OdHFkFlsXWQVEpfsapC9IgAx_jsrrtEbY59fGy60.original.fullsize.png">

</details>

---

### Q116. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A thin, uniform metal rod of mass 'M' and length 'L' is swinging about a horizontal
axis passing through its end. Its maximum angular velocity is ' $\omega^{\prime}$. Its centre of mass
rises to a maximum height of
$(\mathrm{g}=$ acceleration due to gravity)

**Options:**

- **(A)** $\frac{\mathrm{L}^{2} \omega^{2}}{6 \mathrm{~g}}$
- **(B)** $\frac{\mathrm{L}^{2} \omega^{2}}{\mathrm{~g}}$
- **(C)** $\frac{\mathrm{L}^{2} \omega^{2}}{2 \mathrm{~g}}$
- **(D)** $\frac{\mathrm{L}^{2} \omega^{2}}{3 \mathrm{~g}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\mathrm{L}^{2} \omega^{2}}{6 \mathrm{~g}}$**

**Detailed Solution:**

$$
\begin{array}{l}
\mathrm{mgh}=\frac{1}{2} \mathrm{I} \omega^{2} \\
\mathrm{I}=\frac{\mathrm{mL}^{2}}{3} \\
\therefore \quad \mathrm{mgh}=\frac{1}{2}\left(\frac{\mathrm{mL}^{2}}{3}\right) \omega^{2} \\
\quad \mathrm{~h}=\frac{1}{6 \mathrm{~g}} \mathrm{~L}^{2} \omega^{2}
\end{array}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/RbRUbWnVLg084cK0VOtMt9kRk6P2kRxze5FPR6pYceE.original.fullsize.png">

</details>

---

### Q117. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A solid sphere of mass 'M' and radius 'R' has moment of inertia 'l' about its diameter.
It is recast into a disc of thickness 't' whose moment of inertia about an axis passing
through its edge and perpendicular to its plane, remains 'I'. Radius of the disc will
be

**Options:**

- **(A)** $\mathrm{R}/\sqrt{19}$
- **(B)** $R / \sqrt{15}$
- **(C)** $2 \mathrm{R} / \sqrt{15}$
- **(D)** $2 R / \sqrt{19}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 \mathrm{R} / \sqrt{15}$**

**Detailed Solution:**

Moment of inertia of solid sphere is
$\mathrm{I}_{\mathrm{s}}=\frac{2}{5} \mathrm{MR}^{2}$
Moment of inertia of the disc is given by about the given axis is
$\begin{aligned}
\mathrm{I}_{d} &=\frac{3}{2} \mathrm{Mr}^{2} \\
\therefore \mathrm{r}^{2} &=\frac{4}{15} \mathrm{R}^{2} \quad \therefore \frac{3}{2} \mathrm{Mr}^{2}=\frac{2}{5} \mathrm{MR}^{2} \\
\therefore \mathrm{r} &=\frac{2 \mathrm{R}}{\sqrt{15}}
\end{aligned}$

</details>

---

### Q118. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A thin uniform rod of length 'L' and mass 'M' is bent at the middle point ' 0 ' at an angle
of $45^{\circ}$ as shown in the figure. The moment of inertia of the system about an axis
passing through '0' and perpendicular to the plane of the bent rod, is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/zdZCTeP-aP1b7c2T0OqYKbiQuo47yCt6yew5QlmtFuc.original.fullsize.png">

**Options:**

- **(A)** $\frac{\mathrm{ML}^{2}}{12}$
- **(B)** $\frac{M L^{2}}{24}$
- **(C)** $\frac{\mathrm{M} \mathrm{L}^{2}}{3}$
- **(D)** $\frac{\mathrm{M} L^{2}}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\mathrm{ML}^{2}}{12}$**

**Detailed Solution:**

Moment of inertia of each half of the rod about the mid point is given by
$I_{1}=\frac{\frac{M}{2}\left(\frac{L}{2}\right)^{2}}{3}=\frac{M L^{2}}{24}$
Total moment of inertia $=\mathrm{I}=2 \mathrm{I}_{1}=\frac{\mathrm{ML}^{2}}{12}$

</details>

---

### Q119. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{M}$ and $\mathrm{L}$ be the mass and length of thin uniform rod respectively. In $1^{\text {st }}$ case, axis of rotation is passing through centre and perpendicular to its length. In $2^{\text {nd }}$ case, axis of rotation is passing through one end and perpendicular to its length. The ratio of radius of gyration in first case to second case is

**Options:**

- **(A)** $3: 1$
- **(B)** $1: 2$
- **(C)** $2: 1$
- **(D)** $1: 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1: 2$**

**Detailed Solution:**

$\begin{array}{l}\mathrm{I}_{1}=\frac{\mathrm{ML}^{2}}{12}=\mathrm{MK}_{1}^{2} \\ \mathrm{I}_{2}=\frac{\mathrm{ML}^{2}}{3}=\mathrm{MK}_{2}^{2} \\ \mathrm{k}_{2}=\frac{\mathrm{L}}{\sqrt{3}} \\ \frac{\mathrm{k}_{1}}{\mathrm{k}_{2}}=\frac{1}{2}\end{array} \quad \therefore \mathrm{K}_{1}=\frac{\mathrm{L}}{\sqrt{12}}=\frac{\mathrm{L}}{2 \sqrt{3}}$

</details>

---

### Q120. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The moment of inertia of a thin uniform rod about a perpendicular axis passing through one of its ends is 'I'. Now, the rod is bent in a ring and its moment of inertia about diameter is ' $\mathrm{I}_{1}^{\prime}$. Then $\frac{\mathrm{I}}{\mathrm{I}_{1}}$ is

**Options:**

- **(A)** $\frac{8 \pi^{2}}{3}$
- **(B)** $\frac{11 \pi^{2}}{3}$
- **(C)** $\frac{4 \pi^{2}}{3}$
- **(D)** $\frac{\pi^{2}}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{8 \pi^{2}}{3}$**

**Detailed Solution:**

If $M$ is the mass of the rod and $L$ is its length, then $I=\frac{M L^{2}}{3}$ Radius of the circular ring is given by
$\begin{aligned}
2 \pi r=L &=\frac{L}{2 \pi} \\
\therefore I_{1} &=\frac{M r^{2}}{2}=\frac{M}{2} \cdot \frac{L^{2}}{4 \pi^{2}} \\
\therefore \frac{1}{I_{1}} &=\frac{8 \pi^{2}}{3}
\end{aligned}$

</details>

---

### Q121. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two rings of radius 'R' and 'nR' made of same material have the ratio of moment of inertia about an axis passing through its centre and perpendicular to the plane as $1: 8 .$ The value of 'n' is (mass per unit length is constant)

**Options:**

- **(A)** 1
- **(B)** 3
- **(C)** 4
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2**

**Detailed Solution:**

$\begin{array}{l}
I_{1}=M R^{2}, I_{2}=(n M)(n R)^{2}=n^{3} m R^{2} \\
\therefore \frac{I_{1}}{I_{2}}=\frac{1}{n^{3}}=\frac{1}{8} \\
\therefore n=2
\end{array}$

</details>

---

### Q122. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A ring and a disc have same mass and same radius. The ratio of moment of inertia
of a ring about a tangent in its plane to that of the disc about its diameter is

**Options:**

- **(A)** $6: 1$
- **(B)** $4: 1$
- **(C)** $2: 1$
- **(D)** $8: 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $6: 1$**

**Detailed Solution:**

Moment of inertia of a ring about a tangent in its plane is given by $I=\frac{3}{2} M R^{2}$
Moment of inertia of a disc about its diameter is given by $I^{\prime}=\frac{1}{4} M R^{2}$
$\therefore \frac{I}{I^{\prime}}=6$

</details>

---

### Q123. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

From a uniform circular thin disc of mass $9 \mathrm{M}$ and radius $\mathrm{R}$, a small disc of radius $\frac{\mathrm{R}}{3}$
is removed. The centre of the small disc is at a distance $\frac{2 \mathrm{R}}{3}$ from the centre of
original disc. The moment of inertia of the remaining disc about an axis
perpendicular to the plane of the disc and passing through the centre of the disc
of radius $\mathrm{R}$ is

**Options:**

- **(A)** $4 \mathrm{MR}^{2}$
- **(B)** $3 \mathrm{MR}^{2}$
- **(C)** $\frac{\mathrm{MR}^{2}}{2}$
- **(D)** $\mathrm{MR}^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $4 \mathrm{MR}^{2}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/l7Qj5gVei19cSY5_purWhTjxzE0joyjh4Ogq-nStVc8.original.fullsize.png">

The moment of inertia of the complete disc $\mathrm{I}_{1}=\frac{9 \mathrm{MR}^{2}}{2}$ The moment of inertia of the removed disc $=$
$$
\begin{aligned}
I^{\prime} &=\frac{M}{2}\left(\frac{R}{3}\right)^{2}+M\left(\frac{2 R}{3}\right)^{2}=\frac{M R^{2}}{18}+\frac{4 M R^{2}}{9} \\
&=\frac{M R^{2}}{2}
\end{aligned}
$$
[Since mass is proportional to area, it is proportional to square of the radius. Since the radius of the removed disc is $\frac{R}{3}$, its mass will be $M$ ]
$\therefore$ Moment of inertia of the remaining disc will be $I_{2}=I_{1}-I^{\prime}=\frac{9 m R^{2}}{2}-\frac{M R^{2}}{2}=4 M R^{2}$

</details>

---

### Q124. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Moment of inertia of a solid sphere about its diameter is 'I'. It is then casted into 27
small spheres of same diameter. The moment of inertia of each new sphere is

**Options:**

- **(A)** $\frac{\text { I }}{243}$
- **(B)** $\frac{\text { I }}{122}$
- **(C)** $\frac{\mathrm{I}}{31}$
- **(D)** $\frac{\mathrm{I}}{62}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\text { I }}{243}$**

**Detailed Solution:**

No Solution

</details>

---

### Q125. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A thin metal wire of length ‘ <math><mi>L</mi></math> ’ and uniform linear mass density ‘ <math><mi>Q</mi></math> ’ is bent into a circular coil with ‘ <math><mi>O</mi></math> ’ as centre. The moment of inertia of a coil about the axis <math><mi>X</mi><mi>X</mi><mi>'</mi></math> is

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/40c88ea7-367f-4e5f-bf1b-cd76cfd2fb72.png" style="height: 127px; width: 210px;" />

**Options:**

- **(A)** <math><mrow><mrow><mn>3</mn><mi>Q</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mo>/</mo><mrow><mn>8</mn><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></math>
- **(B)** <math><mrow><mrow><mi>Q</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mo>/</mo><mrow><mn>4</mn><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></math>
- **(C)** <math><mrow><mrow><mn>3</mn><mi>Q</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>/</mo><mrow><mn>4</mn><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></math>
- **(D)** <math><mrow><mrow><mi>Q</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mo>/</mo><mrow><mn>8</mn><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mrow><mrow><mn>3</mn><mi>Q</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mo>/</mo><mrow><mn>8</mn><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></math>**

**Detailed Solution:**

<math><msub><mrow><mi>I</mi></mrow><mrow><mi>x</mi><mi>x</mi><mi mathvariant="normal">'</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mi>m</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>  
<math><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>.</mo><mi>m</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>  
<math><mo>∴</mo><mn>2</mn><mi>π</mi><mi>R</mi><mo>=</mo><mi>L</mi><mi></mi><mo>∴</mo><mi>R</mi><mo>=</mo><mfrac><mrow><mi>L</mi></mrow><mrow><mn>2</mn><mi>π</mi></mrow></mfrac></math>  
So <math><mo> </mo><msub><mrow><mi>I</mi></mrow><mrow><mi>x</mi><mi>x</mi><mi>'</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mi>Q</mi></mrow></mfenced><mo>.</mo><mn>2</mn><mi>π</mi><mi>R</mi><mo>.</mo><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>  
<math><mo>=</mo><mn>3</mn><mi>Q</mi><mi>π</mi><mfenced separators="|"><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></math>  
<math><mo>=</mo><mfrac><mrow><mn>3</mn><mi>Q</mi><mi>π</mi><mo>.</mo><msup><mrow><mi>L</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>8</mn><msup><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></math>

</details>

---

### Q126. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If radius of the solid sphere is doubled by keeping its mass constant, the ratio of their moment of inertia about any of its diameter is

**Options:**

- **(A)** <math><mn>1</mn><mo>:</mo><mn>8</mn></math>
- **(B)** <math><mn>2</mn><mo>:</mo><mn>5</mn></math>
- **(C)** <math><mn>2</mn><mo>:</mo><mn>3</mn></math>
- **(D)** <math><mn>1</mn><mo>:</mo><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>1</mn><mo>:</mo><mn>4</mn></math>**

**Detailed Solution:**

<math><mfrac><mrow><msub><mrow><mi>I</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>I</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi>m</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi>m</mi><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><mi>R</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

</details>

---

### Q127. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

When a 12000 joule of work is done on a flywheel, its frequency of rotation increases from 10 Hz to 20 Hz. The moment of inertia of flywheel about its axis of rotation is <math><mfenced separators="|"><mrow><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>10</mn></mrow></mfenced></math>

**Options:**

- **(A)** <math><mn>1</mn><mi></mi><mi>k</mi><mi>g</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(B)** <math><mn>2</mn><mi></mi><mi>k</mi><mi>g</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(C)** <math><mn>1.688</mn><mi></mi><mi>k</mi><mi>g</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(D)** <math><mn>1.5</mn><mi></mi><mi>k</mi><mi>g</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>2</mn><mi></mi><mi>k</mi><mi>g</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

Given, work done, W = 12000 J, 
Initial frequency, <math><msub><mrow><mi>f</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>10</mn><mi>H</mi><mi>z</mi></math>  
Angular velocity for rotational motion is given by 
<math><mi>ω</mi><mo>=</mo><mn>2</mn><mi>π</mi><mi>f</mi></math>  
<math><mo>∴</mo><msub><mrow><mi>ω</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn><mi>π</mi><msub><mrow><mi>f</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn><mi>π</mi><mo>×</mo><mn>10</mn><mo>=</mo><mn>20</mn><mi>π</mi><mfrac><mrow><mi>r</mi><mi>a</mi><mi>d</mi></mrow><mrow><mi>s</mi></mrow></mfrac></math>  
<math><mi>a</mi><mi>n</mi><mi>d</mi><mi></mi><msub><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>2</mn><mi>π</mi><msub><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>2</mn><mi>π</mi><mo>×</mo><mn>20</mn><mo>=</mo><mfrac><mrow><mn>40</mn><mi>π</mi><mi>r</mi><mi>a</mi><mi>d</mi></mrow><mrow><mi>s</mi></mrow></mfrac></math>  
According to work-energy theorem, 
Work done in rotation = change in rotational kinetic energy 
<math><mo>⇒</mo><mi>W</mi><mo>=</mo><mfrac><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><msubsup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac><mo>-</mo><mfrac><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><msubsup><mrow><mi>ω</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mo>∵</mo><mfrac><mrow><mi>K</mi><msub><mrow><mi>E</mi></mrow><mrow><mi>r</mi><mi>o</mi><mi>t</mi><mi>a</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi><mi>a</mi><mi>l</mi></mrow></msub><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math>  
= <math><mi mathvariant="normal"></mi><mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mo>/</mo><mrow><mfenced separators="|"><mrow><msubsup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>-</mo><msubsup><mrow><mi>ω</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfenced></mrow></mrow></math> …(i) 
Where, l = moment of inertia of the flywheel. 
Substituting given values in Eq. (i), we get 
<math><mfrac><mrow><mn>12000</mn><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mn>1600</mn><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>400</mn><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>  
<math><mo>⇒</mo><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>1200</mn><mo>×</mo><mn>10</mn></mrow></mfenced><mfenced close="]" open="[" separators="|"><mrow><mo>∵</mo><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>10</mn></mrow></mfenced></math>  
<math><mo>⇒</mo><mi>l</mi><mo>=</mo><mfrac><mrow><mn>12000</mn><mo>×</mo><mn>2</mn></mrow><mrow><mn>12000</mn></mrow></mfrac><mo>=</mo><mn>2</mn><mi></mi><mi>k</mi><mi>g</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

</details>

---

### Q128. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Three identical rods each of mass ‘M’ and length ‘L’ are joined to form a symbol ‘H’. The moment of inertia of the system about one of the sides of ‘H’ is

**Options:**

- **(A)** <math><mfrac><mrow><mn>2</mn><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>4</mn><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>4</mn><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

The given situation can be shown as 
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/e1abd52f-375a-42ee-95b7-0316b012cf4b.png"> 
Let us take the moment of inertia of the system about rod <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mi></mi></math> then total moment of inertia is 
For rod <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi>l</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0</mn></math>  
For rod <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></math> , using perpendicular axis theorem, 
<math><msub><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac><mi></mi></math>  
For rod <math><msub><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msub></math> , using parallel axis theorem, 
<math><msub><mrow><mi>l</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><msub><mrow><mi>l</mi></mrow><mrow><mi>C</mi><mi>M</mi></mrow></msub><mo>+</mo><msub><mrow><mi>l</mi></mrow><mrow><mfenced separators="|"><mrow><mi>a</mi><mi>t</mi><mi>L</mi></mrow></mfenced></mrow></msub><mo>=</mo><mn>0</mn><mo>+</mo><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></math>  
Now, putting the values of <math><msub><mrow><mi>l</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msub></math> and <math><msub><mrow><mi>l</mi></mrow><mrow><mn>3</mn></mrow></msub></math> in Eq. (i), we get 
<math><msub><mrow><mi>l</mi></mrow><mrow><mi>τ</mi></mrow></msub><mo>=</mo><mn>0</mn><mo>+</mo><mfrac><mrow><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>⇒</mo><msub><mrow><mi>l</mi></mrow><mrow><mi>τ</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>4</mn><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac></math>

</details>

---

### Q129. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `2`

The moment of inertia of a ring about an axis passing through the centre and perpendicular to its plane is <math><mi>I</mi></math>. It is rotating with angular velocity <math><mi>ω.</mi></math> Another identical ring is gently placed on it so that their centres coincide. If both the rings are rotating about the same axis then loss in kinetic energy is

**Options:**

- **(A)** <math><mfrac><mrow><mi>I</mi><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>I</mi><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>I</mi><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>I</mi><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>8</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mi>I</mi><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

From conservation of angular momentum
<math> <mrow> <msub> <mi>I</mi> <mn>1</mn> </msub> <msub> <mi>&#969;</mi> <mn>1</mn> </msub> <mo>=</mo><msub> <mi>I</mi> <mn>2</mn> </msub> <msub> <mi>&#969;</mi> <mn>2</mn> </msub></mrow></math>
<math> <mrow> <mi>I</mi><mi>&#969;</mi><mo>=</mo><mn>2</mn><mi>I</mi><msub> <mi>&#969;</mi> <mn>2</mn> </msub></mrow></math>
<math> <mrow> <msub> <mi>&#969;</mi> <mn>2</mn> </msub> <mo>=</mo><mfrac> <mi>&#969;</mi> <mn>2</mn> </mfrac></mrow></math>
New <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>KE</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>.</mo><mrow><mo>(</mo><mn>2</mn><mi>I</mi><mo>)</mo></mrow><msup><mrow><mo>(</mo><mfrac><mi>&#969;</mi><mn>2</mn></mfrac><mo>)</mo></mrow><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mi>I</mi><msup><mi>&#969;</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math>
Loss in  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>KE</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>I</mi><msup><mi>&#969;</mi><mn>2</mn></msup><mo>&#8722;</mo><mfrac><mrow><mi>I</mi><msup><mi>&#969;</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>I</mi><msup><mi>&#969;</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math>

</details>

---

### Q130. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `2`

The moment of inertia of a thin uniform rod of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> and mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> about an axis passing through a point at a distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>L</mi><mn>3</mn></mfrac></math> from one of its ends and perpendicular to the rod is

**Options:**

- **(A)** <math><mfrac><mrow><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>7</mn><mi> </mi><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>48</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>48</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><msub><mrow><mi>I</mi></mrow><mrow><mi>C</mi><mi>M</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac></math> (about middle point)
<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/image2-a755ff19-0207-4f4b-8506-f522bdffe378.jpg" />
Using parallel axis theorem.
<math><mo>∴</mo></math> <math><mi>I</mi><mo>=</mo><msub><mrow><mi>I</mi></mrow><mrow><mi>C</mi><mi>M</mi></mrow></msub><mo>+</mo><mi>M</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
<math><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac><mo>+</mo><mi>M</mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>L</mi></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>
<math><mi>I</mi><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac></math>

</details>

---

### Q131. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

Let <math> <mi>M</mi> </math> be the mass and <math> <mi>L</mi> </math> be the length of a thin uniform rod. In first case, axis of rotation is passing through center and perpendicular to the length of the rod. In second case axis of rotation is passing through one end and perpendicular to the length of the rod. The ratio of radius of gyration in first case to second case is

**Options:**

- **(A)** <math><mn>1</mn></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

Moment of inertia of rod whose axis of rotation is passing through center and perpendicular to the plane of rod is
<math><mi>I</mi><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><mi>I</mi><mo>=</mo><mi>M</mi><msubsup><mrow><mi>K</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup></math> (where <math> <mrow> <msub> <mtext>K</mtext> <mn>1</mn> </msub> </mrow> </math> radius of gravitation)
<math><mo>⇒</mo><msub><mrow><mi>K</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mi>L</mi></mrow><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math> ..... (i)
When axis of rotation of rod is passing through one end of rod, then
<math><mi>I</mi><mo>=</mo><mi>M</mi><msubsup><mrow><mi>K</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac><mo>⇒</mo><msub><mrow><mi>K</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><mi>L</mi></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac></math> ..... (ii)
Taking ratios of (i) and (ii) we get
<math><mfrac><mrow><msub><mrow><mi>K</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>K</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>L</mi></mrow><mrow><mn>2</mn><msqrt><mn>3</mn><mi> </mi></msqrt></mrow></mfrac><mo>×</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mi>L</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mfrac><mrow><msub><mrow><mi>K</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>K</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

</details>

---

### Q132. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

A disc of radius <math><mi> R</mi></math> and thickness <math><mfrac><mrow><mi>R</mi></mrow><mrow><mn>6</mn></mrow></mfrac></math> has a moment of inertia <math><msup><mrow><mi>I</mi></mrow></msup></math> about an axis passing through its centre and perpendicular to its plane. The disc is melted and recast into a solid sphere. The moment of inertia of a sphere about its diameter is

**Options:**

- **(A)** <math><mfrac><mrow><mi>I</mi></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>I</mi></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>I</mi></mrow><mrow><mn>32</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>I</mi></mrow><mrow><mn>64</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mi>I</mi></mrow><mrow><mn>5</mn></mrow></mfrac></math>**

**Detailed Solution:**

Volume of disc is A.d <math><mo>=</mo><mi>π</mi><mo>.</mo><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>×</mo><mfrac><mrow><mi>R</mi></mrow><mrow><mn>6</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>×</mo><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac><mi> </mi></math>
Moment of inertia of disc is <math><mi>I</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
When the disk is remolded in solid sphere of volume V having radius r, then
<math><mfrac><mrow><mi>π</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>6</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>×</mo><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>⇒</mo><mfrac><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>6</mn></mrow></mfrac><mo>×</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><msup><mrow><mi>r</mi></mrow><mrow><mn>3</mn></mrow></msup></math>
<math><mo>∴</mo><msup><mrow><mi>r</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>=</mo><mfrac><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>8</mn></mrow></mfrac><mo>⇒</mo><mi>r</mi><mo>=</mo><mfrac><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
Moment of inertia of sphere is given by <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi> </mi><mi>M</mi><mo>.</mo><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>×</mo><mi>M</mi><mo>.</mo><mfrac><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>10</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>×</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>I</mi></mrow><mrow><mn>5</mn></mrow></mfrac></math>

</details>

---

### Q133. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

A circular disc is to be made by using iron and aluminium, so that it aquires momentum of inertia about its geometrical axis. It is possible with

**Options:**

- **(A)** iron and aluminium layers in alternate order
- **(B)** aluminium at interior and iron surrounding it
- **(C)** iron at interior and aluminium surrounding it
- **(D)** Either (a) or (c)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) aluminium at interior and iron surrounding it**

**Detailed Solution:**

By doing so the distribution of mass can be made away from the axis of rotation.

</details>

---

### Q134. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `2`

Moment of inertia of a disc about a diameter is $I .$ Find the moment of inertia of disc about an axis perpendicular to its plane and passing through its rim?

**Options:**

- **(A)** $6 I$
- **(B)** $4 I$
- **(C)** $2 I$
- **(D)** $8 I$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $6 I$**

**Detailed Solution:**

Moment of inertia of a disc about a diameter is
$$
\frac{1}{4} M R^{2}=I
$$
(given)
$$
\therefore \quad M R^{2}=4 I
$$
Now, required moment of inertia $=\frac{3}{2} M R^{2}$
$$
=\frac{3}{2}(4 I)=6 I
$$

</details>

---

### Q135. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

The moment of inertia of a thin uniform rod of length $L$ and mass $M$ about an axis passing through a point at a distance of $1 / 3$ from one of its ends and perpendicular to the rod is

**Options:**

- **(A)** $\frac{M L^{2}}{12}$
- **(B)** $\frac{M L^{2}}{9}$
- **(C)** $\frac{7 M L^{2}}{48}$
- **(D)** $\frac{M L^{2}}{48}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{M L^{2}}{9}$**

**Detailed Solution:**

$I_{\mathrm{CM}}=\frac{M L^{2}}{12}$
(about middle point)
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/N1OU6Sc4wEGT8Cxs9O8UfgJiS00ICCARYbRkOnO5BRQ.original.fullsize.png">

$\therefore$
$$
I=I_{\mathrm{CM}}+M x^{2}
$$
$$
\begin{array}{l}
=\frac{M L^{2}}{12}+M\left(\frac{L}{6}\right)^{2} \\
I=\frac{M L^{2}}{9}
\end{array}
$$

</details>

---

### Q136. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

From a disc of radius $R$, a concentric dircular portion of radius $r$ is cut out so as to leave an annular disc of mass $M$. The moment of inertia
of this annular disc about the axis perpendicular to its plane and passing through its centre of gravity is

**Options:**

- **(A)** $\frac{1}{2} M\left(R^{2}+r^{2}\right)$
- **(B)** $\frac{1}{2} M\left(R^{2}-r^{2}\right)$
- **(C)** $\frac{1}{2} M\left(R^{4}+r^{4}\right)$
- **(D)** $\frac{1}{2} M^{\prime}\left(R^{4}-r^{4}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2} M\left(R^{2}+r^{2}\right)$**

**Detailed Solution:**

The moment of inertia of this annular disc about the axis perpendicular to its plane will be $\frac{1}{2} M\left(R^{2}+r^{2}\right)$

</details>

---

### Q137. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `2`

Moment of inertia of a rod of mass $M$ and length $L$ about an axis passing through a point midway between centre and end is

**Options:**

- **(A)** $\frac{M L^{2}}{6}$
- **(B)** $\frac{M L^{2}}{12}$
- **(C)** $\frac{7 M L^{2}}{24}$
- **(D)** $\frac{7 M L^{2}}{48}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{7 M L^{2}}{48}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/dgrxFPFs40hzfd0CbmoqJbvsA2AGOSECZwubuozAQEU.original.fullsize.png">

$$
\begin{array}{l}
=\frac{M L^{2}}{12}+M\left[\frac{L}{4}\right]^{2} \\
=\frac{M L^{2}}{12}+\frac{M L^{2}}{16}=\frac{7 M L^{2}}{48}
\end{array}
$$

</details>

---

### Q138. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `3`

Moment of inertia of big drop is $I$. If 8 droplets are formed from big drop, then moment of inertia of small droplet is

**Options:**

- **(A)** $\frac{I}{32}$
- **(B)** $\frac{I}{16}$
- **(C)** $\frac{I}{8}$
- **(D)** $\frac{I}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{I}{32}$**

**Detailed Solution:**

Moment of inertia of big drop is $I=\frac{2}{5} M R^{2}$ When small droplets are formed from big drop volume of liquid remain same
$$
\begin{aligned}
n \frac{4}{3} \pi r^{3} &=\frac{4}{3} \pi R^{3} \\
n^{1 / 3} r &=R \text { as } n=8 \Rightarrow r=\frac{R}{2}
\end{aligned}
$$
Mass of each small droplet $=\frac{M}{8}$
$\therefore$ Moment of inertia of each small droplet
$$
\begin{array}{l}
=\frac{2}{5}\left[\frac{M}{8}\right]\left[\frac{R}{2}\right]^{2} \\
=\frac{1}{32}\left[\frac{2}{5} M R^{2}\right]=\frac{I}{32}
\end{array}
$$

</details>

---

### Q139. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

Two spheres of equal masses, one of which is a thin spherical shell and the other a solid, have the same moment of inertia about their respective diameters. The ratio of their radii will be

**Options:**

- **(A)** $5: 7$
- **(B)** $3: 5$
- **(C)** $\sqrt{3}: \sqrt{5}$
- **(D)** $\sqrt{3}: \sqrt{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{3}: \sqrt{5}$**

**Detailed Solution:**

Let the radii of the thin spherical shell and the solid sphere are $R_{1}$ and $R_{2}$ respectively. Then the moment of inertia of the spherical shell about their diameter
$I=\frac{2}{3} M R_{1}^{2}$ ...(i)
and the moment of inertia of the solid sphere is given by
$I=\frac{2}{5} M R_{2}^{2}$ ...(ii)
Given that the masses and moment of inertia for both the bodies are equal, then from Eqs. (i) and (ii)
$$
\begin{array}{r}
\frac{2}{3} M R_{1}^{2}=\frac{2}{5} M R_{2}^{2} \Rightarrow \frac{R_{1}^{2}}{R_{2}^{2}}=\frac{3}{5} \\
\Rightarrow \frac{R_{1}}{R_{2}}=\sqrt{\frac{3}{5}} \Rightarrow R_{1}: R_{2}=\sqrt{3}: \sqrt{5}
\end{array}
$$

</details>

---

### Q140. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

A rubber ball is dropped from a height of $5 \mathrm{~m}$ on a planet, where the acceleration due to gravity is not known. On bouncing it rises to $1.8 \mathrm{~m}$. The ball loses its velocity on bouncing by a factor of

**Options:**

- **(A)** $\frac{16}{25}$
- **(B)** $\frac{2}{5}$
- **(C)** $\frac{3}{5}$
- **(D)** $\frac{9}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{5}$**

**Detailed Solution:**

Key Idea According to conservation of energy, potential energy at height $h=$ kinetic energy at
ground. Potential energy = Kinetic energy
ie,
$$
m g h=\frac{1}{2} m v^{2}
$$
$$
\Rightarrow \quad v=\sqrt{2 g h}
$$
If $h_{1}$ and $h_{2}$ are initial and final heights, then
$$
v_{1}=\sqrt{2 g h_{1}}, \quad v_{2}=\sqrt{2 g h_{2}}
$$
Loss in velocity
$$
\Delta v=v_{1}-v_{2}=\sqrt{2 g h_{1}}-\sqrt{2 g h_{2}}
$$
$\therefore$ Fractional loss in velocity $=\frac{\Delta v}{v_{1}}$
$$
\begin{array}{l}
=\frac{\sqrt{2 g h_{1}}-\sqrt{2 g h_{2}}}{\sqrt{2 g h_{1}}} \\
=1-\sqrt{\frac{h_{2}}{h_{1}}}
\end{array}
$$
Substituting the values, we have
$\therefore$
$$
\frac{\Delta v}{v_{1}}=1-\sqrt{\frac{1.8}{5}}
$$
$$
\begin{array}{l}
=1-\sqrt{0.36}=1-0.6 \\
=0.4=\frac{2}{5}
\end{array}
$$

</details>

---

