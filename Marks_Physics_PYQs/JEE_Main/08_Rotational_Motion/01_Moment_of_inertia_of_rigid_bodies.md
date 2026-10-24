# JEE Main Physics - Rotational Motion

## Topic 1: Moment of inertia of rigid bodies

**Total Questions:** 95

---

### Q1. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A solid sphere ($A$) of mass $5m$ and a spherical shell ($B$) of mass $m$, both having same radius, are placed on a rough surface. When a force of same magnitude is applied tangentially at the highest points of $A$ and $B$, they start rolling without slipping with an acceleration of $a_A$ and $a_B$, respectively. The ratio of $a_A$ and $a_B$ is __________.

**Options:**

- **(A)** $5 : 21$
- **(B)** $6 : 10$
- **(C)** $21 : 25$
- **(D)** $1 : 5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $5 : 21$**

**Detailed Solution:**

For a body of mass $M$ and radius $R$ rolling without slipping under a force $F$ applied tangentially at the highest point, the torque about the point of contact with the ground is $\tau = F(2R)$.

The moment of inertia about the point of contact is $I = I_{cm} + MR^2$.

Using $\tau = I\alpha$ and the rolling without slipping condition $a = \alpha R$, we get:

$F(2R) = (I_{cm} + MR^2) \dfrac{a}{R} \Rightarrow a = \dfrac{2FR^2}{I_{cm} + MR^2}$

For the solid sphere $A$ of mass $5m$:

$I_{cm,A} = \dfrac{2}{5}(5m)R^2 = 2mR^2$

$a_A = \dfrac{2FR^2}{2mR^2 + 5mR^2} = \dfrac{2F}{7m}$

For the spherical shell $B$ of mass $m$:

$I_{cm,B} = \dfrac{2}{3}mR^2$

$a_B = \dfrac{2FR^2}{\dfrac{2}{3}mR^2 + mR^2} = \dfrac{2F}{\dfrac{5}{3}m} = \dfrac{6F}{5m}$

The ratio of their accelerations is:

$\dfrac{a_A}{a_B} = \dfrac{\dfrac{2F}{7m}}{\dfrac{6F}{5m}} = \dfrac{2}{7} \times \dfrac{5}{6} = \dfrac{5}{21}$

Answer: $5 : 21$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A solid sphere of radius $4$ cm and mass $5$ kg is rotating (rotation axis is passing through the centre of the sphere) with an angular velocity of $1200$ rpm. It is brought to rest in $10$ s by applying a constant torque. The torque applied and the number of rotations it made before it comes to rest are _______ and _______ respectively.

**Options:**

- **(A)** $0.128\pi$ Nm, $100$
- **(B)** $0.0128\pi$ Nm, $50$
- **(C)** $0.128\pi$ Nm, $50$
- **(D)** $0.0128\pi$ Nm, $100$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.0128\pi$ Nm, $100$**

**Detailed Solution:**

Initial angular velocity $\omega_0 = 1200 \text{ rpm} = \dfrac{1200 \times 2\pi}{60} = 40\pi \text{ rad/s}$

Final angular velocity $\omega = 0$

Time $t = 10 \text{ s}$

Angular acceleration $\alpha = \dfrac{\omega - \omega_0}{t} = \dfrac{0 - 40\pi}{10} = -4\pi \text{ rad/s}^2$

Moment of inertia of the solid sphere $I = \dfrac{2}{5}MR^2 = \dfrac{2}{5} \times 5 \times (0.04)^2 = 0.0032 \text{ kg m}^2$

Torque $\tau = I|\alpha| = 0.0032 \times 4\pi = 0.0128\pi \text{ Nm}$

Angle rotated $\theta = \dfrac{\omega_0 + \omega}{2}t = \dfrac{40\pi + 0}{2} \times 10 = 200\pi \text{ rad}$

Number of rotations $N = \dfrac{\theta}{2\pi} = \dfrac{200\pi}{2\pi} = 100$

Answer: $0.0128\pi$ Nm, $100$

</details>

---

### Q3. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An object of uniform density rolls up the curved path with the initial velocity $v_0$ as shown in the figure. If the maximum height attained by an object is $\dfrac{7v_0^2}{10g}$ ($g$ = acceleration due to gravity), the object is a _______.
<img style="width: 200px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/05APRS2__q31_d1.jpg" />

**Options:**

- **(A)** solid cylinder
- **(B)** ring
- **(C)** disc
- **(D)** solid sphere

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) solid sphere**

**Detailed Solution:**

By the law of conservation of mechanical energy, the total initial kinetic energy of the rolling object is converted into potential energy at the maximum height.

Total initial kinetic energy for an object rolling without slipping is given by:
$K = K_{\text{translational}} + K_{\text{rotational}}$
$K = \dfrac{1}{2}mv_0^2 + \dfrac{1}{2}I\omega^2$

Substituting $\omega = \dfrac{v_0}{R}$ and $I = mk^2$ (where $k$ is the radius of gyration):
$K = \dfrac{1}{2}mv_0^2 + \dfrac{1}{2}(mk^2)\left(\dfrac{v_0}{R}\right)^2 = \dfrac{1}{2}mv_0^2\left(1 + \dfrac{k^2}{R^2}\right)$

The potential energy at the maximum height $h$ is:
$U = mgh$

Given $h = \dfrac{7v_0^2}{10g}$, we have:
$U = mg\left(\dfrac{7v_0^2}{10g}\right) = \dfrac{7}{10}mv_0^2$

Equating kinetic and potential energy ($K = U$):
$\dfrac{1}{2}mv_0^2\left(1 + \dfrac{k^2}{R^2}\right) = \dfrac{7}{10}mv_0^2$

$1 + \dfrac{k^2}{R^2} = \dfrac{14}{10} = \dfrac{7}{5}$

$\dfrac{k^2}{R^2} = \dfrac{7}{5} - 1 = \dfrac{2}{5}$

The moment of inertia is $I = \dfrac{2}{5}mR^2$, which corresponds to a solid sphere.

Answer: solid sphere

</details>

---

### Q4. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A solid sphere of mass $M$ and radius $R$ is divided into two unequal parts. The smaller part having mass $M/8$ is converted into a sphere of radius $r$ and the larger part is converted into a circular disc of thickness $t$ and radius $2R$. If $I_1$ is moment of inertia of a sphere having radius $r$ about an axis through its centre and $I_2$ is the moment of inertia of a disc about its diameter, the ratio of their moment of inertia $I_2/I_1 = $ _____.

**Options:**

- **(A)** $35$
- **(B)** $70$
- **(C)** $140$
- **(D)** $210$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $70$**

**Detailed Solution:**

Let the mass of the original solid sphere be $M$ and its radius be $R$.

Mass of the smaller sphere, $m_1 = \dfrac{M}{8}$.
Since the material remains the same, the density is constant. The volume is directly proportional to the mass.
$\dfrac{4}{3}\pi r^3 = \dfrac{1}{8} \left(\dfrac{4}{3}\pi R^3\right) \Rightarrow r^3 = \dfrac{R^3}{8} \Rightarrow r = \dfrac{R}{2}$

Moment of inertia of the smaller sphere about an axis through its centre is:
$I_1 = \dfrac{2}{5} m_1 r^2 = \dfrac{2}{5} \left(\dfrac{M}{8}\right) \left(\dfrac{R}{2}\right)^2 = \dfrac{2}{5} \times \dfrac{M}{8} \times \dfrac{R^2}{4} = \dfrac{M R^2}{80}$

Mass of the larger part (which is converted into a disc) is:
$m_2 = M - \dfrac{M}{8} = \dfrac{7M}{8}$

The radius of the disc is given as $2R$. The moment of inertia of a disc about its diameter is:
$I_2 = \dfrac{1}{4} m_2 (\text{radius})^2 = \dfrac{1}{4} \left(\dfrac{7M}{8}\right) (2R)^2 = \dfrac{1}{4} \times \dfrac{7M}{8} \times 4R^2 = \dfrac{7M R^2}{8}$

The ratio of their moments of inertia is:
$\dfrac{I_2}{I_1} = \dfrac{\dfrac{7M R^2}{8}}{\dfrac{M R^2}{80}} = \dfrac{7}{8} \times 80 = 70$

Answer: $70$

</details>

---

### Q5. JEE Main 2026 (02 April Shift 2)

*Type:* `numerical` | *Level:* `2`

Moment of inertia about an axis $AB$ for a rod of mass $40$ kg and length $3$ m is same as that of a solid sphere of mass of $10$ kg and radius $R$ about an axis parallel to $AB$ axis with separation of $3$ m as shown in figure below. The value of $R$ is given as $\sqrt{\dfrac{\alpha}{2}}$. The value of $\alpha$ is _______.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/02APRS2__q50_d1.png" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **15**

**Detailed Solution:**

Moment of inertia of the rod about axis $AB$ passing through one of its ends:
$I_{\text{rod}} = \dfrac{ML^2}{3} = \dfrac{40 \times (3)^2}{3} = \dfrac{40 \times 9}{3} = 120\text{ kg}\cdot\text{m}^2$

Moment of inertia of the solid sphere about the same axis $AB$, using the parallel axis theorem $I = I_{\text{cm}} + md^2$:
Mass $m = 10\text{ kg}$, radius $R$, distance from the centre of the sphere to axis $AB$ is $d = 3\text{ m}$.

$I_{\text{sphere}} = \dfrac{2}{5}mR^2 + md^2 = \dfrac{2}{5}(10)R^2 + 10(3)^2 = 4R^2 + 90$

Equating the two moments of inertia:
$120 = 4R^2 + 90$
$4R^2 = 30$
$R^2 = \dfrac{15}{2}$
$R = \sqrt{\dfrac{15}{2}}$

Comparing with $R = \sqrt{\dfrac{\alpha}{2}}$:
$\alpha = 15$

Hence, $\alpha = 15$.

</details>

---

### Q6. JEE Main 2026 (28 January Shift 1)

*Type:* `numerical` | *Level:* `2`

A solid sphere of radius 10 cm is rotating about an axis which is at a distance 15 cm from its centre. The radius of gyration about this axis is $\sqrt{n} \mathrm{~cm}$. The value of $n$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **265**

**Detailed Solution:**

Using the parallel axis theorem for radius of gyration:
$k^2 = k_{cm}^2 + d^2$ where $k_{cm}$ is the radius of gyration about the center of mass and $d$ is the distance from the center.
For a solid sphere:
$I_{center} = \frac{2}{5}MR^2$, so $k_{cm}^2 = \frac{2}{5}R^2$
With $R = 10$ cm and $d = 15$ cm:
$k^2 = \frac{2}{5}(10)^2 + (15)^2 = 40 + 225 = 265$
Since $k = \sqrt{n}$, we have $n = 265$.

</details>

---

### Q7. JEE Main 2026 (24 January Shift 2)

*Type:* `numerical` | *Level:* `2`

A uniform solid cylinder of length $L$ and radius $R$ has moment of inertia about its axis equal to $I_{1}$. A small co-centric cylinder of length $L / 2$ and radius $R / 3$ carved from this cylinder has moment of inertia about its axis equals to $I_{2}$. The ratio $I_{1} / I_{2}$ is $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **162**

**Detailed Solution:**

For solid cylinder: $I = \frac{1}{2}mR^2$
Large cylinder: mass $m_1 = \rho \pi R^2 L$, so $I_1 = \frac{1}{2}\rho \pi R^2 L \times R^2 = \frac{\rho \pi R^4 L}{2}$
Small cylinder (carved out): length L/2, radius R/3, mass $m_2 = \rho \pi(R/3)^2(L/2) = \frac{\rho \pi R^2 L}{18}$
$I_2 = \frac{1}{2} \times \frac{\rho \pi R^2 L}{18} \times (R/3)^2 = \frac{1}{2} \times \frac{\rho \pi R^2 L}{18} \times \frac{R^2}{9} = \frac{\rho \pi R^4 L}{324}$
$\frac{I_1}{I_2} = \frac{\rho \pi R^4 L/2}{\rho \pi R^4 L/324} = \frac{324}{2} = 162$

</details>

---

### Q8. JEE Main 2026 (23 January Shift 2)

*Type:* `numerical` | *Level:* `3`

Suppose there is a uniform circular disc of mass $M \mathrm{~kg}$ and radius $r \mathrm{~m}$ shown in figure. The shaded regions are cut out from the disc. The moment of inertia of the remainder about the axis $A$ of the disc is given by $\frac{x}{256} M r^{2}$. The value of $x$ is $\_\_\_\_$. 
 <img style="width:250px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/23S2_q_48_1.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **109**

**Detailed Solution:**

The moment of inertia of the complete disc about axis A is
$I_{disc} = \frac{1}{2}Mr^2 = \frac{128Mr^2}{256}$.
Each removed circular region has radius $r/4$ and mass $m_i = M/(r^2/16r^2) = M/16$. 
For each removed disc at distance $3r/4$ from axis A, using the parallel axis theorem:
$I_{removed} = \frac{1}{2}m_i(r/4)^2 + m_i(3r/4)^2 = \frac{Mr^2}{512} + \frac{9Mr^2}{256} = \frac{19Mr^2}{512}$. 
For two removed discs:
$I_{2removed} = \frac{38Mr^2}{512} = \frac{19Mr^2}{256}$. 
Therefore:
$I_{remainder} = \frac{128Mr^2}{256} - \frac{19Mr^2}{256} = \frac{109Mr^2}{256}$, so $x = 109$.

</details>

---

### Q9. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The moment of inertia of a square loop made of four uniform solid cylinders, each having radius $R$ and length $L(\mathrm{R}<\mathrm{L})$ about an axis passing through the mid points of opposite sides, is (Take the mass of the entire loop as $M$) :

**Options:**

- **(A)** $\frac{3}{4} M R^{2}+\frac{7}{12} M L^{2}$
- **(B)** $\frac{3}{8} M R^{2}+\frac{1}{6} M L^{2}$
- **(C)** $\frac{3}{4} M R^{2}+\frac{1}{6} M L^{2}$
- **(D)** $\frac{3}{8} M R^{2}+\frac{7}{12} M L^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3}{8} M R^{2}+\frac{1}{6} M L^{2}$**

**Detailed Solution:**

Each cylinder has mass $M/4$, radius $R$, length $L$.
Axis through midpoints of top and bottom sides (along y-direction).
Top/bottom cylinders (perpendicular to axis, axis through midpoint):
$I = \frac{M_c R^2}{4} + \frac{M_c L^2}{12}$ each.
Left/right cylinders (parallel to axis, distance $L/2$ from it):
$I = \frac{M_c R^2}{2} + M_c(L/2)^2$ each.
Total $= 2\left(\frac{M_c R^2}{4}+\frac{M_c L^2}{12}\right) + 2\left(\frac{M_c R^2}{2}+\frac{M_c L^2}{4}\right)$ 
$= \frac{M}{2}\left(\frac{3R^2}{4}+\frac{L^2}{3}\right) = \frac{3MR^2}{8}+\frac{ML^2}{6}$.

</details>

---

### Q10. JEE Main 2026 (22 January Shift 2)

*Type:* `numerical` | *Level:* `2`

Two masses $m$ and 2 m are connected by a light string going over a pulley (disc) of mass 30 m with radius $r=0.1 \mathrm{~m}$. The pulley is mounted in a vertical plane and it is free to rotate about its axis. The 2 m mass is released from rest and its speed when it has descended through a height of 3.6 m is $\_\_\_\_$ $\mathrm{m} / \mathrm{s}$. (Assume string does not slip and $\mathrm{g}=10 \mathrm{~m} / \mathrm{s}^{2}$)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

Let the speed of the masses be $v$ and the angular velocity of the pulley be $\omega = v/r$ since the string does not slip.
The pulley is a disc of mass $M = 30m$ and radius $r$. Its moment of inertia is $I = \frac{1}{2}Mr^2 = \frac{1}{2}(30m)r^2 = 15mr^2$.
Using the principle of conservation of mechanical energy, the loss in potential energy of the system equals the gain in kinetic energy.
When the mass $2m$ descends by $h = 3.6$ m, the mass $m$ ascends by $h = 3.6$ m.
Loss in potential energy $\Delta U = (2m)gh - (m)gh = mgh$.
Gain in kinetic energy $\Delta K = \frac{1}{2}(2m)v^2 + \frac{1}{2}(m)v^2 + \frac{1}{2}I\omega^2$.
Substituting $I$ and $\omega$: $\Delta K = \frac{3}{2}mv^2 + \frac{1}{2}(15mr^2)(\frac{v}{r})^2 = \frac{3}{2}mv^2 + \frac{15}{2}mv^2 = 9mv^2$.
Equating $\Delta U = \Delta K$: $mgh = 9mv^2$.
$v^2 = \frac{gh}{9}$.
Given $g = 10$ m/s$^2$ and $h = 3.6$ m:
$v^2 = \frac{10 \times 3.6}{9} = \frac{36}{9} = 4$.
$v = \sqrt{4} = 2$ m/s.

</details>

---

### Q11. JEE Main 2026 (22 January Shift 1)

*Type:* `numerical` | *Level:* `1`

A circular disc has radius $R_{1}$ and thickness $T_{1}$. Another circular disc made of the same material has radius $R_{2}$ and thickness $T_{2}$. If the moment of inertia of both discs are same and $\frac{R_{1}}{R_{2}}=2$ then $\frac{T_{1}}{T_{2}}=\frac{1}{\alpha}$. The value of $\alpha$ is $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

For a circular disc made of material with density $\rho$, moment of inertia is $I = \frac{1}{2}MR^2 = \frac{1}{2}\rho \pi R^2 T \cdot R^2 = \frac{1}{2}\rho \pi R^4 T$.
For disc 1: $I_1 = \frac{1}{2}\rho \pi R_1^4 T_1$
For disc 2: $I_2 = \frac{1}{2}\rho \pi R_2^4 T_2$
Given $I_1 = I_2$:
$R_1^4 T_1 = R_2^4 T_2$
With $\frac{R_1}{R_2} = 2$:
$(2R_2)^4 T_1 = R_2^4 T_2$
$16 R_2^4 T_1 = R_2^4 T_2$
$\frac{T_1}{T_2} = \frac{1}{16}$
Therefore $\alpha = 16$.

</details>

---

### Q12. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A solid sphere of mass 5 kg and radius 10 cm is kept in contact with another solid sphere of mass 10 kg and radius 20 cm. The moment of inertia of this pair of spheres about the tangent passing through the point of contact is $\_\_\_\_$ $\mathrm{kg}. \mathrm{m}^{2}$.

**Options:**

- **(A)** 0.72
- **(B)** 0.36
- **(C)** 0.18
- **(D)** 0.63

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0.63**

**Detailed Solution:**

For two solid spheres in contact with the tangent line at the contact point.
Sphere 1: $m_1 = 5$ kg, $r_1 = 0.1$ m
Sphere 2: $m_2 = 10$ kg, $r_2 = 0.2$ m
For a solid sphere, $I_{cm} = \frac{2}{5}mr^2$
The tangent at contact is perpendicular to the line joining centers. The perpendicular distance from each sphere's center to this tangent line equals its radius.
Using parallel axis theorem: $I_{total} = I_{cm} + md^2$
For sphere 1: $I_1 = \frac{2}{5}(5)(0.1)^2 + 5(0.1)^2 = 0.02 + 0.05 = 0.07$ kg·m²
For sphere 2: $I_2 = \frac{2}{5}(10)(0.2)^2 + 10(0.2)^2 = 0.16 + 0.4 = 0.56$ kg·m²
Total: $I = 0.07 + 0.56 = 0.63$ kg·m²

</details>

---

### Q13. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The pulley shown in figure is made using a thin rim and two rods of length equal to diameter of the rim. The rim and each rod have a mass of $M$. Two blocks of mass of $M$ and $m$ are attached to two ends of a light string passing over the pulley, which is hinged to rotate freely in vertical plane about its center. The magnitudes of the acceleration experienced by the blocks is $\_\_\_\_$ (assume no slipping of string on pulley).
<img style="width:200px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/21S2_q_33_1.png">

**Options:**

- **(A)** $\frac{(M-m) g}{\left[\left(\frac{13}{6}\right) M+m\right]}$
- **(B)** $\frac{(M-m) g}{\left[\left(\frac{8}{3}\right) M+m\right]}$
- **(C)** $\frac{(M-m) g}{2 M+m}$
- **(D)** $\frac{(M-m) g}{M+m}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{(M-m) g}{\left[\left(\frac{8}{3}\right) M+m\right]}$**

**Detailed Solution:**

The pulley consists of a rim (mass $M$) and two rods (each mass $M$) forming a diameter structure.
The moment of inertia is: $I = I_{rim} + I_{rods} = MR^2 + 2 \times \frac{MR^2}{3} = \frac{5MR^2}{3}$.
For the Atwood pulley system, applying Newton's second law:
Mass $m$ (upward): $T_1 = m(g-a)$
Mass $M$ (downward): $T_2 = M(g+a)$
Pulley rotation: $T_2 R - T_1 R = I\alpha = \frac{5MR^2}{3} \cdot \frac{a}{R}$
Thus: $T_2 - T_1 = \frac{5Ma}{3}$
Substituting: $M(g+a) - m(g-a) = \frac{5Ma}{3}$
$(M-m)g + (M+m)a = \frac{5Ma}{3}$
$(M-m)g = a\left(\frac{5M}{3} - M - m\right) = a\left(\frac{2M}{3} - m\right)$
$a = \frac{(M-m)g}{\frac{2M-3m}{3}} = \frac{3(M-m)g}{2M+3m}$, which is option (2).

</details>

---

### Q14. JEE Main 2026 (21 January Shift 1)

*Type:* `numerical` | *Level:* `2`

Two identical thin rods of mass $M \mathrm{~kg}$ and length $L \mathrm{~m}$ are connected as shown in figure. Moment of inertia of the combined rod system about an axis passing through point $P$ and perpendicular to the plane of the rods is $\frac{x}{12} \mathrm{ML}^{2} \mathrm{~kg} \mathrm{~m}^{2}$. The value of $x$ is $\_\_\_\_$. 
 <img style="width:150px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/21S1_q_50_1.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **17**

**Detailed Solution:**

For vertical rod with axis at end P: $I_1 = \frac{ML^2}{3}$
For horizontal rod centered at distance L from P:
$I_2 = \int_{-L/2}^{L/2} \frac{M}{L}(x^2 + L^2)dx = \frac{M}{L}\left[\frac{x^3}{3} + L^2x\right]_{-L/2}^{L/2}$
$= \frac{M}{L}\left[\frac{L^3}{12} + L^3\right] = \frac{13ML^2}{12}$
Total: $I = \frac{ML^2}{3} + \frac{13ML^2}{12} = \frac{4ML^2 + 13ML^2}{12} = \frac{17ML^2}{12}$
$x = 17$

</details>

---

### Q15. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A rod of linear mass density ' $\lambda$ ' and length ' $L$ ' is bent to form a ring of radius 'R'. Moment of inertia of ring about any of its diameter is :

**Options:**

- **(A)** $\frac{\lambda \mathrm{L}^3}{16 \pi^2}$
- **(B)** $\frac{\lambda \mathrm{L}^3}{12}$
- **(C)** $\frac{\lambda \mathrm{L}^3}{4 \pi^2}$
- **(D)** $\frac{\lambda L^3}{8 \pi^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\lambda L^3}{8 \pi^2}$**

**Detailed Solution:**

$L=2 \pi R$
$\mathrm{I}=\frac{\mathrm{MR}^2}{2}=\frac{\lambda \times \mathrm{L}}{2} \times\left(\frac{\mathrm{L}}{2 \pi}\right)^2=\frac{\lambda \mathrm{L}^3}{8 \pi^2}$

</details>

---

### Q16. JEE Main 2025 (7 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

M and R be the mass and radius of a disc. A small disc of radius $R / 3$ is removed from the bigger disc as shown in figure. The moment of inertia of remaining part of bigger disc about an axis AB passing through the centre O and perpendicular to the plane of disc is $\frac{4}{x} M R^2$. The value of $x$ is ________.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/KcliJzNaFMnfovgRyc1zuvcly7Fy1k4s-viBpp50uCw.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

Without cavity $\mathrm{I}_1=\frac{\mathrm{MR}^2}{2}$
$\begin{aligned}
\text { Mass of removed disc }= & \frac{\mathrm{M}}{\pi \mathrm{R}^2} \times\left(\frac{\mathrm{R}}{3}\right)^2 \pi \\
& =\left(\frac{\mathrm{M}}{9}\right)
\end{aligned}$
M.I. of removed disc $I_2=\frac{\frac{M}{9}\left(\frac{R}{3}\right)^2}{2}+\frac{M}{9} \times\left(\frac{2 R}{3}\right)^2$
$\begin{aligned}
& =\frac{\mathrm{MR}^2}{18} \\
& \mathrm{I}=\mathrm{I}_1-\mathrm{I}_2=\frac{\mathrm{MR}^2}{2}-\frac{\mathrm{MR}^2}{18}=\frac{4 \mathrm{MR}^2}{9} \\
& (\mathrm{n}=9)
\end{aligned}$

</details>

---

### Q17. JEE Main 2025 (7 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

$\mathrm{A}, \mathrm{B}$ and C are disc, solid sphere and spherical shell respectively with same radii and masses. These masses are placed as shown in figure.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/hW8JwDZfpG4HMKGE0e9Y-LkEwpHLenRt8K6TasGbcys.original.fullsize.png"/>
The moment of inertia of the given system about $P Q$ is $\frac{X}{15} I$, where $I$ is the moment of inertia of the disc about its diameter. The value of x is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **199**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7g8XYv2AjecR4OWB7_hQwtaEA2AjKk2zhK6pYdu0chE.original.fullsize.png"/>
All bodies have same mass and same radius.
$\mathrm{A} \rightarrow$ Disc
$\mathrm{B} \rightarrow$ Solid sphere
$\mathrm{C} \rightarrow$ Spherical shell
and, $\mathrm{I}=\frac{\mathrm{MR}^2}{4}$
$\mathrm{I}_{\mathrm{PQ}}=\frac{\mathrm{MR}^2}{4}+\left(\frac{2}{5} \mathrm{MR}^2+\mathrm{MR}^2\right)+\left(\frac{2}{3} \mathrm{MR}^2+\mathrm{MR}^2\right)$
$\mathrm{I}_{\mathrm{PQ}}=\frac{15 \mathrm{MR}^2+24 \mathrm{MR}^2+60 \mathrm{MR}^2+40 \mathrm{MR}^2+60 \mathrm{MR}^2}{60}$
$\mathrm{I}_{\mathrm{PQ}}=\frac{199}{60} \mathrm{MR}^2=\frac{199}{15}\left(\frac{\mathrm{MR}^2}{4}\right)$
$=\frac{199}{15} \mathrm{I}$

</details>

---

### Q18. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The moment of inertia of a circular ring of mass $M$ and diameter r about a tangential axis lying in the plane of the ring is :

**Options:**

- **(A)** $\frac{1}{2} \mathrm{Mr}^2$
- **(B)** $\frac{3}{8} \mathrm{Mr}^2$
- **(C)** $\frac{3}{2} \mathrm{Mr}^2$
- **(D)** $2 \mathrm{Mr}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3}{8} \mathrm{Mr}^2$**

**Detailed Solution:**

Diameter is given as R.
$\begin{aligned}
& \therefore \text { Radius }=\mathrm{R} / 2 \\
& \mathrm{I}_{\text {tan gent }}=\frac{3}{2} \mathrm{~m}\left(\frac{\mathrm{R}}{2}\right)^2=\frac{3}{8} \mathrm{mR}^2
\end{aligned}$

</details>

---

### Q19. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Moment of inertia of a rod of mass ' M ' and length 'L' about an axis passing through its center and normal to its length is ' $\alpha$ '. Now the rod is cut into two equal parts and these parts are joined symmetrically to form a cross shape. Moment of inertia of cross about an axis passing through its center and normal to plane containing cross is :

**Options:**

- **(A)** $\alpha$
- **(B)** $\alpha / 4$
- **(C)** $\alpha / 8$
- **(D)** $\alpha / 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\alpha / 4$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/mVsxC_8RydLIrdnKP5T0lz20itJ0pD2GK3y_aO6z1IE.original.fullsize.png"/>
$\alpha=\frac{\mathrm{M} \ell^2}{12}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ZLig7_We2VTKkJqbt1HKJHVgYbw3HAIqDj3rG7eXMsE.original.fullsize.png"/>
$\begin{aligned} & \alpha^{\prime}=2\left[\frac{\frac{\mathrm{M}}{2}\left(\frac{\ell}{2}\right)^2}{12}\right] \\ & \alpha^{\prime}=\frac{\mathrm{M} \ell^2}{48}=\frac{\alpha}{4}\end{aligned}$
Correct option is (2)

</details>

---

### Q20. JEE Main 2025 (28 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

The moment of inertia of a solid disc rotating along its diameter is 2.5 times higher than the moment of inertia of a ring rotating in similar way. The moment of inertia of a solid sphere which has same radius as the disc and rotating in similar way, is $n$ times higher than the moment of inertia of the given ring. Here, $\mathrm{n}=$_________
Consider all the bodies have equal masses.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/yqX2MrunpEtoRnhF-GwWAK658o7p9Ik23_lAeJYZABI.original.fullsize.png">


$\mathrm{I}_1=\frac{\mathrm{MR}_1^2}{4}, \mathrm{I}_2=\frac{\mathrm{MR}_2^2}{2}, \mathrm{I}_3=\frac{2 \mathrm{MR}_1^2}{5}$

According to problem

$\frac{\mathrm{I}_1}{\mathrm{I}_2}=2.5 \Rightarrow \frac{\frac{\mathrm{MR}_1^2}{4}}{\frac{\mathrm{MR}_2^2}{2}}=\frac{5}{2} \Rightarrow \frac{\mathrm{R}_1^2}{\mathrm{R}_2^2}=5 \ldots$

Now we are provided with information that
$\begin{aligned}
& \frac{\mathrm{I}_3}{\mathrm{I}_2}=\mathrm{n} \\
& \Rightarrow \frac{\frac{2 \mathrm{MR}_1^2}{5}}{\frac{\mathrm{MR}_2^2}{2}}=\mathrm{n} \Rightarrow \frac{4 \mathrm{R}_1^2}{5 \mathrm{R}_2^2}=\mathrm{n}
\end{aligned}$

From Eq', (1) and (2)
$\Rightarrow n=4$

</details>

---

### Q21. JEE Main 2025 (28 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

Two iron solid discs of negligible thickness have radii $R_1$ and $R_2$ and moment of intertia $I_1$ and $I_2$, respectively. For $R_2=2 R_1$, the ratio of $I_1$ and $I_2$ would be $1 / x$, where $\mathrm{x}=$ ________ -

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/LCWd07a_Ujs8S8XbMrPQB-ZSMFPXmLzDyKzoBa3c_qI.original.fullsize.png">


Given $R_2=2 R_1$
$\begin{aligned}
& M_1=\sigma \times \pi R_1^2=M_o \\
& M_2=\sigma \times \pi R_2^2=M_o \\
& M_2=\sigma \times \pi R_2^2=\sigma \times \pi\left[2 R_1\right]^2=\sigma \times 4 \pi R_1^2=4 M_o
\end{aligned}$
$\frac{I_1}{I_2}=\frac{\frac{M_1 R_1^2}{2}}{\frac{M_2 R_2^2}{2}}=\frac{M_1 R_1^2}{M_2 R_2^2}=\frac{1}{4} \times \frac{1}{4}=\frac{1}{16}$

</details>

---

### Q22. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A solid sphere and a hollow sphere of the same mass and of same radius are rolled on an inclined plane. Let the time taken to reach the bottom by the solid sphere and the hollow sphere be $t_1$ and $t_2$, respectively, then

**Options:**

- **(A)** $t_1\gt t_2$
- **(B)** $t_1=t_2$
- **(C)** $t_1 \lt t_2$
- **(D)** $t_1=2 t_2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $t_1 \lt t_2$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/G5rnumTQkuWquyp3XVaWY-KiXhQI2Ti62i_56KmUXhY.original.fullsize.png">




$\begin{aligned} & \mathrm{t}=\sqrt{\frac{2 \ell}{\mathrm{a}_{\mathrm{cm}}}} \\ & \mathrm{a}_{\mathrm{cm}}=\frac{\mathrm{g} \sin \theta}{1+\frac{\mathrm{I}_{\mathrm{cm}}}{\mathrm{MR}^2}} \\ & \mathrm{a}_1=\mathrm{a}_{\mathrm{cm}_1}=\frac{5 \mathrm{~g} \sin \theta}{7} \ldots . . \text { Solid } \\ & \mathrm{a}_2=\mathrm{a}_{\mathrm{cm}_2}=\frac{3 \mathrm{~g} \sin \theta}{5} \ldots . . \text { Hollow } \\ & \mathrm{a}_1>\mathrm{a}_2 \\ & \mathrm{t}_1 < \mathrm{t}_2\end{aligned}$

</details>

---

### Q23. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A uniform circular disc of radius ' R ' and mass ' M ' is rotating about an axis perpendicular to its plane and passing through its centre. A small circular part of radius $\mathrm{R} / 2$ is removed from the original disc as shown in the figure. Find the moment of inertia of the remaining part of the original disc about the axis as given above.

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/XH-mqgZIJ4pMQOp1OP8gFQPAjGY1zV6gk8jFyMgDynI.original.fullsize.png"/>

**Options:**

- **(A)** $\frac{7}{32} \mathrm{MR}^2$
- **(B)** $\frac{9}{32} \mathrm{MR}^2$
- **(C)** $\frac{17}{32} \mathrm{MR}^2$
- **(D)** $\frac{13}{32} \mathrm{MR}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{13}{32} \mathrm{MR}^2$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/M01VSsfAguNI4rXoEPwBjy_ShsUfVP5k2MO4laHx5ck.original.fullsize.png">

$\begin{aligned} & I_{\text {complete }}=\frac{M R^2}{2} \\ & \begin{aligned} I_{\text {removed }} & =\left(\frac{M}{4}\right)\left(\frac{R}{2}\right)^2 \frac{1}{2}+\left(\frac{M}{4}\right)\left(\frac{R}{2}\right)^2 \\ & =\frac{3 M R^2}{32} \\ I=\frac{M R^2}{2} & -\frac{3 M R^2}{32}=\frac{13}{32} M R^2\end{aligned}\end{aligned}$

</details>

---

### Q24. JEE Main 2024 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Three balls of masses $2 \mathrm{~kg}, 4 \mathrm{~kg}$ and $6 \mathrm{~kg}$ respectively are arranged at centre of the edges of an equilateral triangle of side $2 \mathrm{~m}$. The moment of intertia of the system about an axis through the centroid and perpendicular to the plane of triangle, will be _______ $\mathrm{kg} \mathrm{m}^2$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Y9HoriFGYNLWkpL6wZWw1CIGBPr66In48QGPDPzd9Kk.original.fullsize.png">
Moment of inertia about $\mathrm{C}$ and perpendicular to the plane is :
$\begin{aligned}
\mathrm{I} & =\mathrm{r}^2[2+4+6] \\
& =\frac{1}{3} \times 12 \\
\mathrm{I} & =4 \mathrm{~kg}-\mathrm{m}^2
\end{aligned}$

</details>

---

### Q25. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Ratio of radius of gyration of a hollow sphere to that of a solid cylinder of equal mass, for moment of Inertia about their diameter axis $\mathrm{AB}$ as shown in figure is $\sqrt{8 / x}$. The value of $x$ is :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/X2HVRwgsocDf1AWw9so1jfU3kfMh8eClEXm_MUQPg40.original.fullsize.png">

**Options:**

- **(A)** $51$
- **(B)** $34$
- **(C)** $17$
- **(D)** $67$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $67$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{I}_{\text {sphere }}=\frac{2}{3} \mathrm{MR}^2=\mathrm{Mk}_1^2 \\ & \mathrm{I}_{\text {cylinder }}=\frac{1}{12} \mathrm{M}\left(4 \mathrm{R}^2\right)+\frac{1}{4} \mathrm{MR}^2+\mathrm{M}(2 \mathrm{R})^2 \\ & =\frac{67}{12} \mathrm{MR}^2=\mathrm{Mk}_2^2 \\ & \frac{\mathrm{k}_1}{\mathrm{k}_2}=\sqrt{\frac{2}{3} \cdot \frac{12}{67}}=\sqrt{\frac{8}{67}}\end{aligned}$

</details>

---

### Q26. JEE Main 2024 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Two identical spheres each of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo> </mo><mi>kg</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo> </mo><mi>cm</mi></math> are fixed at the ends of a light rod so that the separation between the centers is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>150</mn><mo> </mo><mi>cm</mi></math>. Then, moment of inertia of the system about an axis perpendicular to the rod and passing through its middle point is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>20</mn></mfrac><mo> </mo><mi>kg</mi><mo> </mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math>, where the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **53**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2532099a-6b7c-4fd9-9106-6af3319ce692.png" style="width: 350px; height: 163px;"/></p><p>Using parallel axis theorem, we can write total moment of inertia as, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfenced><mrow><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>m</mi><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><mi>m</mi><msup><mi>d</mi><mn>2</mn></msup></mrow></mfenced><mo>×</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mn>2</mn><mfenced><mrow><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>×</mo><mn>2</mn><mo>×</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>×</mo><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>2</mn></msup></mrow></mfenced><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mn>53</mn><mn>20</mn></mfrac><mo> </mo><mi>kg</mi><mo> </mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>53</mn></math>.</p>

</details>

---

### Q27. JEE Main 2024 (27 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>Four particles, each of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo> </mo><mi>kg</mi></math> are placed at four corners of a square of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo> </mo><mi mathvariant="normal">m</mi></math>. The moment of inertia of the system about an axis perpendicular to its plane and passing through one of its vertex is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mo> </mo><mi>kg</mi><mo> </mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math>.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9b147497-491a-4e6a-8ef1-b90d1ee75f60.png" style="width: 220px; height: 196px;"/></p><p>The formula to calculate the moment of inertia of a system of particles about a point can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msub><mi>m</mi><mi>i</mi></msub><msubsup><mi>r</mi><mi>i</mi><mn>2</mn></msubsup><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>where, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mi>i</mi></msub></math> is the mass of the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>i</mi><mi>th</mi></msup></math> particle situated at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mi>i</mi></msub></math> from the point.</p><p>With reference to the above diagram, it can be written that the net moment of inertia of the system of particles is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mi>I</mi></mtd><mtd><mo>=</mo></mtd><mtd><mi>m</mi><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mi>m</mi><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mi>m</mi><mo>(</mo><msqrt><mn>2</mn></msqrt><mi>a</mi><msup><mo>)</mo><mn>2</mn></msup></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mn>4</mn><mi>m</mi><msup><mi>a</mi><mn>2</mn></msup></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mn>4</mn><mo>×</mo><mn>1</mn><mo> </mo><mi>kg</mi><mo>×</mo><msup><mfenced><mrow><mn>2</mn><mo> </mo><mi mathvariant="normal">m</mi></mrow></mfenced><mn>2</mn></msup></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mn>16</mn><mo> </mo><mi>kg</mi><mo> </mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></mtd></mtr></mtable></math></p>

</details>

---

### Q28. JEE Main 2023 (15 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

A solid sphere and a solid cylinder of same mass and radius are rolling on a horizontal surface without slipping. The ratio of their radius of gyrations respectively <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>k</mi><mrow><mi>s</mi><mi>p</mi><mi>h</mi></mrow></msub><mo>:</mo><msub><mi>k</mi><mrow><mi>c</mi><mi>y</mi><mi>l</mi></mrow></msub></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><msqrt><mi>x</mi></msqrt></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<blockquote><p>Considering rotational axis as the diametrical axis for sphere and axis of cylinder. Then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>K</mi><mn>1</mn><mn>2</mn></msubsup><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><msup><mi>R</mi><mn>2</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>K</mi><mn>2</mn><mn>2</mn></msubsup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>R</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfrac><msub><mi>K</mi><mn>1</mn></msub><msub><mi>K</mi><mn>2</mn></msub></mfrac><mo>=</mo><msqrt><mfrac><mrow><mn>2</mn><mo>/</mo><mn>5</mn></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></mfrac></msqrt><mo>=</mo><msqrt><mfrac><mn>4</mn><mn>5</mn></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>K</mi><mn>1</mn></msub><msub><mi>K</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mn>2</mn><msqrt><mn>5</mn></msqrt></mfrac></math></p><p>Comparing it with the given value in the question,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><msqrt><mn>5</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>2</mn><msqrt><mi>x</mi></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q29. JEE Main 2023 (11 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

A solid sphere of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn><mo>&#160;</mo><mi mathvariant="normal">g</mi></math> radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math> is rotated about one of its diameter with angular speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. If the moment of inertia of the sphere about its tangent is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></math> times its angular momentum about the diameter. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> will be

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **35**

**Detailed Solution:**

<p>The angular momentum about the diameter is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mtext>diameter&#160;</mtext></msub><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mi>&#969;</mi><mo>;</mo><mspace width="1em"></mspace></math></p><p>The moment of inertia of a sphere is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mrow><mi>C</mi><mi>M</mi></mrow></msub><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math>. The moment of inertia about the tangent is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mtext>tangent&#160;</mtext></msub><mo>=</mo><msub><mi>I</mi><mrow><mi>C</mi><mi>M</mi></mrow></msub><mo>+</mo><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>7</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math>.</p><p>It is given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Using the given relation between the moment of inertia and the angular momentum,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>=</mo><mi>x</mi><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#215;</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mi>&#969;</mi><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>3</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup></mstyle><mi>&#969;</mi></mfrac><mo>=</mo><mn>3</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><mn>10</mn><mo>=</mo><mn>35</mn></math></p>

</details>

---

### Q30. JEE Main 2023 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

The moment of inertia of a semicircular ring about an axis, passing through the center and perpendicular to the plane of ring, is<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac><mo>&#160;</mo><msup><mi>MR</mi><mn>2</mn></msup></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi></math> is the radius and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math> is the mass of the semicircular ring. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<blockquote><p>The moment of inertia of a semicircular ring about a line perpendicular to the plane of the ring and passing through its centre is given as<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;I</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>R</mi></math> are the mass and radius of the ring. Comparing the given value</p><p>.<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><mo>&#160;</mo><msup><mi>MR</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">x</mi><mo>=</mo><mn>1</mn></math></p></blockquote>

</details>

---

### Q31. JEE Main 2023 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>A ring and a solid sphere rotating about an axis passing through their centres have same radii of gyration. The axis of rotation is perpendicular to plane of ring. The ratio of radius of ring to that of sphere is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>2</mn><mi>x</mi></mfrac></msqrt></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is _____.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<blockquote><p>The moment of inertia of the ring about an axis perpendicular to the plane of ring is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>r</mi></msub><mo>=</mo><mi>m</mi><msup><mi>k</mi><mn>2</mn></msup></math>.</p><p>The moment of inertia of the sphere is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>s</mi></msub><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>m</mi><msub><msup><mi>R</mi><mn>2</mn></msup><mi>s</mi></msub></math></p><p>It is given that </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mi>m</mi><msub><msup><mi>R</mi><mn>2</mn></msup><mi>r</mi></msub><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>m</mi><msup><msub><mi>R</mi><mi>s</mi></msub><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mo>)</mo></math></p><p>From equation (i)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>r</mi></msub><mo>=</mo><msqrt><mfrac><mn>2</mn><mn>5</mn></mfrac></msqrt><msub><mi>R</mi><mi>s</mi></msub></math></p><p>From the question, it can be written that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>R</mi><mi>r</mi></msub><msub><mi>R</mi><mi>s</mi></msub></mfrac><mo>=</mo><msqrt><mfrac><mn>2</mn><mi>x</mi></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>R</mi><mi>r</mi></msub><msub><mi>R</mi><mi>s</mi></msub></mfrac><mo>=</mo><msqrt><mfrac><mn>2</mn><mn>5</mn></mfrac></msqrt><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q32. JEE Main 2023 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Two identical solid spheres each of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>kg</mi></math> and radii <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>cm</mi><mo>&#160;</mo></math>are fixed at the ends of a light rod. The separation between the centres of the spheres is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>&#160;</mo><mi>cm</mi><mo>.</mo></math> The moment of inertia of the system about an axis perpendicular to the rod passing through its middle point is<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>______</mi><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8211;</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>.</mo></math></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **176**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/672d0e8a-d42e-4391-8c5a-8c6f67617b65.png" style="width: 300px; height: 195px;" /></p><p>The moment of inertia of a sphere is given by the formula <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math>.</p><p>Since there are two masses, the total moment of inertia about the axis perpendicular to the rod passing through the centre is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>2</mn><mo>&#215;</mo><mfenced close="]" open="["><mrow><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><mi>M</mi><msup><mfenced><mrow><mfrac><mi>l</mi><mn>2</mn></mfrac><mo>+</mo><mi>r</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mo>)</mo></math></p><p>The given data is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>kg</mi><mspace linebreak="newline"></mspace><mi>l</mi><mo>=</mo><mfenced><mrow><mn>0</mn><mo>.</mo><mn>4</mn><mo>-</mo><mn>0</mn><mo>.</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mspace linebreak="newline"></mspace><mi mathvariant="normal">R</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p><p>Substituting the values in equation (i)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfenced><mrow><mfrac><mn>4</mn><mn>5</mn></mfrac><mo>(</mo><mn>2</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><msup><mn>1</mn><mn>2</mn></msup><mo>)</mo><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>(</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>+</mo><mn>0</mn><mo>.</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfenced><mrow><mfenced><mrow><mfrac><mn>4</mn><mn>5</mn></mfrac><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>02</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>4</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>04</mn></mrow></mfenced></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfenced><mrow><mn>0</mn><mo>.</mo><mn>016</mn><mo>+</mo><mn>0</mn><mo>.</mo><mn>16</mn></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn><mo>.</mo><mn>176</mn><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math></p></blockquote>

</details>

---

### Q33. JEE Main 2023 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `1`

Moment of inertia of a disc of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and radius &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>&#39; about any of its diameter is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math>. The moment of inertia of this disc about an axis normal to the disc and passing through a point on its edge will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>2</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ccf6bf2e-3e06-4b7e-9ef2-6a43f12e3956-9896810.PNG" style="width: 180px; height: 140px;" /></p><p>Given here, </p><p>Moment of inertia of a disc of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and radius &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>&#39; about any of its diameter is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math>. </p><p>Moment of inertia of disc about centre is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mrow><mi>c</mi><mi>m</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>+</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math></p><p>Using parallel axis theorem, we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msub><mi>I</mi><mrow><mi>c</mi><mi>m</mi></mrow></msub><mo>+</mo><mi>M</mi><msup><mi>d</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p>Hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math>.</p>

</details>

---

### Q34. JEE Main 2023 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

Two discs of same mass and different radii are made of different materials such that their thicknesses are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>cm</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math> respectively. The densities of materials are in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>:</mo><mn>5</mn></math>. The moment of inertia of these discs respectively about their diameters will be in the ratio of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>6</mn></mfrac></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>Mass of the disc in terms of density can be written as, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mi>&#961;</mi><mfenced><mrow><mi>&#960;</mi><msup><mi>R</mi><mn>2</mn></msup><mi>t</mi></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>R</mi><mn>2</mn></msup><mo>=</mo><mfrac><mi>m</mi><mrow><mi>&#961;</mi><mi>&#960;</mi><mi>t</mi></mrow></mfrac></math></p><p>Now moment of inertia of the disc about the diameter is, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>m</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math>.</p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><msup><mi>m</mi><mn>2</mn></msup><mrow><mn>4</mn><mi>&#961;</mi><mi>&#960;</mi><mi>t</mi></mrow></mfrac><mspace linebreak="newline"/><mo>&#8658;</mo><mi>I</mi><mo>&#8733;</mo><mfrac><mn>1</mn><mrow><mi>&#961;</mi><mi>t</mi></mrow></mfrac></math></p><p>Required ratio, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><msub><mi>&#961;</mi><mn>2</mn></msub><msub><mi>t</mi><mn>2</mn></msub></mrow><mrow><msub><mi>&#961;</mi><mn>1</mn></msub><msub><mi>t</mi><mn>1</mn></msub></mrow></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>5</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>5</mn></math>.</p>

</details>

---

### Q35. JEE Main 2023 (25 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

If a solid sphere of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>kg</mi></math> and a disc of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi>kg</mi></math> have the same radius, then the ratio of moment of inertia of the disc about a tangent in its plane to the moment of inertia of the sphere about its tangent will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>7</mn></mfrac></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ae8e1578-662d-40d1-90bb-4888a1842cf9-9894815.png" style="width: 200px; height: 223px;" /></p><p>Moment of inertia of the solid sphere about any diameter is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msub><mi>m</mi><mn>1</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>5</mn></mfrac></math>.</p><p>Using parallel axis theorem, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mtext>solid&#160;sphere&#160;</mtext></msub><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><msub><mi>m</mi><mn>1</mn></msub><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msub><mi>m</mi><mn>1</mn></msub><msup><mi>R</mi><mn>2</mn></msup><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mn>7</mn><mn>5</mn></mfrac><msub><mi>m</mi><mn>1</mn></msub><msup><mi>R</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>7</mn><mn>5</mn></mfrac><mo>&#215;</mo><mn>5</mn><msup><mi>R</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><msup><mi>R</mi><mn>2</mn></msup></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/066a4cbf-4a68-4fae-8b65-29ec041839f8-a6c48194-a27a-4a4a-8ab0-47fbfce7fd8f-9894815_2.png" style="width: 200px; height: 211px;" /></p><p>Moment of inertia of the disc about the diameter is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>m</mi><mn>2</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math>.</p><p>Now using parallel axis theorem, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mtext>disc&#160;</mtext></msub><mo>=</mo><mfrac><mrow><msub><mi>m</mi><mn>2</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>+</mo><msub><mi>m</mi><mn>2</mn></msub><msup><mi>R</mi><mn>2</mn></msup><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mn>5</mn><mn>4</mn></mfrac><msub><mi>m</mi><mn>2</mn></msub><msup><mi>R</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>5</mn><mn>4</mn></mfrac><mo>&#215;</mo><mn>4</mn><msup><mi>R</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><msup><mi>R</mi><mn>2</mn></msup></math></p><p>Therefore,<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mtext>disc&#160;</mtext></msub><msub><mi>I</mi><mtext>soild sphere&#160;</mtext></msub></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>7</mn></mfrac></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>5</mn></math>.</p>

</details>

---

### Q36. JEE Main 2023 (25 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">I</mi><mi>CM</mi></msub></math> is moment of inertia of a circular disc about an axis (CM) passing through its center and perpendicular to the plane of disc. <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">I</mi><mi>AB</mi></msub></math> is its moment of inertia about an axis AB perpendicular to plane and parallel to axis CM at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><mi mathvariant="normal">R</mi></math> from center, where R is the radius of the disc. The ratio of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">I</mi><mi>AB</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">I</mi><mi>CM</mi></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>:</mo><mn>9</mn></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is ______.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f7735e0a-6334-4508-a46e-b593bb9c1ec9-9894275.png" style="width: 150px; height: 289px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **17**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f7735e0a-6334-4508-a46e-b593bb9c1ec9-9894275.png" style="width: 150px; height: 289px;" /></p><p>We have,  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>CM</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>&#160;</mo></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> is parallel to diameter and at a distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>R</mi></math> from it, using parallel axis theorem,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>AB</mi></msub><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mi>m</mi><msup><mfenced><mfrac><mrow><mn>2</mn><mi>R</mi></mrow><mn>3</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>17</mn><mn>18</mn></mfrac><mi>m</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p>Thus, the ratio is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><msub><mi>I</mi><mi>AB</mi></msub><msub><mi>I</mi><mi>CM</mi></msub></mfrac><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>17</mn><mn>18</mn></mfrac></mstyle><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>17</mn><mn>9</mn></mfrac></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mn>17</mn></math></p>

</details>

---

### Q37. JEE Main 2023 (24 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>A uniform solid cylinder with radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> and length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> has moment of inertia <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math>, about the axis of cylinder. A concentric solid cylinder of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>R</mi><mo>&#39;</mo></msup><mo>=</mo><mfrac><mi>R</mi><mn>2</mn></mfrac></math>  and length <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>L</mi><mo>&#39;</mo></msup><mo>=</mo><mfrac><mi>L</mi><mn>2</mn></mfrac></math> is carved out of the original cylinder. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub></math> is the moment of inertia of the carved out portion of the cylinder then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mfrac><mo>=</mo></math>  __________.</p><p>(Both <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub></math> are about the axis of the cylinder)   </p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **32**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/367d683c-3449-49a2-b366-a45c91a771a3-9894278.PNG" style="width: 400px; height: 159px;" /></p><p>Moment of inertia of solid cylinder of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> and length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> about the axis is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><msub><mi>M</mi><mn>1</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math>.</p><p>Moment of inertia of carved out portion of the cylinder of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>R</mi><mn>2</mn></mfrac></math> and length <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>L</mi><mn>2</mn></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><msub><mi>M</mi><mn>2</mn></msub><msup><mfenced><mstyle displaystyle="true"><mfrac><mi>R</mi><mn>2</mn></mfrac></mstyle></mfenced><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><msub><mi>M</mi><mn>2</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>8</mn></mfrac></math></p><p>Now, the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><msub><mi>M</mi><mn>1</mn></msub></mrow><msub><mi>M</mi><mn>2</mn></msub></mfrac></math></p><p>As, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mass</mi><mo>=</mo><mi>density</mi><mo>&#215;</mo><mi>volume</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mo>&#215;</mo><mi>&#961;</mi><mi>&#960;</mi><msup><mi>R</mi><mn>2</mn></msup><mi>L</mi></mrow><mstyle displaystyle="true"><mfrac><mrow><mi>&#961;</mi><mi>&#960;</mi><msup><mi>R</mi><mn>2</mn></msup><mi>L</mi></mrow><mrow><mn>4</mn><mo>&#215;</mo><mn>2</mn></mrow></mfrac></mstyle></mfrac><mo>=</mo><mn>32</mn></math></p>

</details>

---

### Q38. JEE Main 2023 (24 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Solid sphere <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is rotating about an axis <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math>. If the radius of the sphere is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math>, then its radius of gyration about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>x</mi></msqrt><mo>&#160;</mo><mi>cm</mi></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is _____.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d9f8350c-05eb-4236-831b-9000e0873bcc-9893891.PNG" style="width: 283px; height: 260px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **110**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d9f8350c-05eb-4236-831b-9000e0873bcc-9893891.PNG" style="width: 283px; height: 260px;" /></p><p> </p><p>Using parallel axis theorem,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mrow><mi>P</mi><mi>Q</mi></mrow></msub><mo>=</mo><msub><mi>I</mi><mtext>COM&#160;</mtext></msub><mo>+</mo><mi>M</mi><msup><mi>d</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><mi>M</mi><msup><mi>d</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>M</mi><mfenced close="]" open="["><mrow><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>&#215;</mo><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><msup><mn>10</mn><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>M</mi><mo>[</mo><mn>110</mn><mo>]</mo><mo>=</mo><mi>M</mi><msup><mi>k</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><msqrt><mn>110</mn></msqrt><mo>&#160;</mo><mi>cm</mi></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>110</mn></math>.</p>

</details>

---

### Q39. JEE Main 2022 (28 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>Four identical discs each of mass &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math>&#39; and diameter &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>&#39; are arranged in a small plane as shown in figure. If the moment of inertia of the system about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><msup><mi>O</mi><mo>&#39;</mo></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>4</mn></mfrac><mi>M</mi><msup><mi>a</mi><mn>2</mn></msup></math>. Then, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> will be _____ .</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e0a5b2da-c579-4149-aac0-7d0525226316-image.png" style="width: 120px; height: 196px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<blockquote><p>Considering four identical discs as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5131e197-a522-4de2-8437-0c0848b698a8-image.png" style="width: 150px; height: 191px;" /></p><p>Moment of inertia of disc about diagonal is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msub><mi>I</mi><mn>3</mn></msub><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math></p><p>Now using parallel axis theorem, </p><p>Moment of inertia of disc <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msub><mi>I</mi><mn>4</mn></msub><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>+</mo><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>5</mn><mn>4</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p>So, net moment of inertia about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><msup><mi>O</mi><mo>&#39;</mo></msup></math> is </p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub><mo>+</mo><msub><mi>I</mi><mn>3</mn></msub><mo>+</mo><msub><mi>I</mi><mn>4</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mfrac><mn>5</mn><mn>4</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p>Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mi>a</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>M</mi><msup><mi>a</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math>, so,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math></p></blockquote>

</details>

---

### Q40. JEE Main 2022 (26 Jul Shift 2)

*Type:* `numerical` | *Level:* `1`

The radius of gyration of a cylindrical rod about an axis of rotation perpendicular to its length and passing through the center will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi><mo>.</mo></math> Given, the length of the rod is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/995a3f27-f4b1-4cf7-a779-418f12374229-image.png" style="width: 120px; height: 101px;" /></p><p>Moment of inertia of the rod about an axis perpendicular to its length and passing through the centre is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mn>12</mn></mfrac></math>.</p><p>Using the relation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mi>m</mi><msup><mi>k</mi><mn>2</mn></msup></math>, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mfrac><msup><mi>l</mi><mn>2</mn></msup><mn>12</mn></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mi>l</mi><msqrt><mn>12</mn></msqrt></mfrac><mo>=</mo><mfrac><mi>l</mi><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>10</mn><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p></blockquote>

</details>

---

### Q41. JEE Main 2022 (29 Jun Shift 2)

*Type:* `numerical` | *Level:* `1`

The moment of inertia of a uniform thin rod about a perpendicular axis passing through one end is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math>. The same rod is bent into a ring and its moment of inertia about a diameter is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><msup><mi>&#960;</mi><mn>2</mn></msup></mrow><mn>3</mn></mfrac></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> will be ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/02bb39c6-b080-47f6-9237-8a4237b14e03-image.png" style="width: 150px; height: 172px;" /></p><p>Moment of inertia of rod rotating about an axis passing through one end is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mn>3</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math> </p><p>Moment of inertia of ring rotating about one of its diameters is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math>.</p><p>Since the rod is bent into a ring, the circumference of the ring and the length of the rod are equal, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>2</mn><mi>&#960;</mi><mi>R</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/322b3509-32b7-46b3-8e3c-fa1057ddab24-image.png" style="width: 150px; height: 133px;" /></p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mrow><mn>8</mn><msup><mi>&#960;</mi><mn>2</mn></msup></mrow></mfrac></math> </p><p>Thus, the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mn>8</mn><msup><mi>&#960;</mi><mn>2</mn></msup></mrow><mn>3</mn></mfrac></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>8</mn></math>.</p>

</details>

---

### Q42. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Match List-I with List-II</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td style="text-align: center;"><strong>List-I</strong></td>			<td style="text-align: center;"> </td>			<td style="text-align: center;"><strong>List-II</strong></td>		</tr>		<tr>			<td>(A)</td>			<td>Moment of inertia of solid sphere
			of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> about any tangent.</td>			<td>(I)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>3</mn></mfrac><msup><mi>MR</mi><mn>2</mn></msup></math></td>		</tr>		<tr>			<td>(B)</td>			<td>Moment of inertia of hollow sphere of radius
			<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>R</mi></mfenced></math> about any tangent.</td>			<td>(II)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>5</mn></mfrac><msup><mi>MR</mi><mn>2</mn></msup></math></td>		</tr>		<tr>			<td>(C)</td>			<td>Moment of inertia of circular ring of radius
			<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>R</mi></mfenced></math> about its diameter.</td>			<td>(III)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><msup><mi>MR</mi><mn>2</mn></msup></math></td>		</tr>		<tr>			<td>(D)</td>			<td>Moment of inertia of circular disc of radius
			<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>R</mi></mfenced></math> about any diameter.</td>			<td>(IV)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>MR</mi><mn>2</mn></msup></math></td>		</tr>	</tbody></table>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>-</mo><mi>II</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">B</mi><mo>-</mo><mi mathvariant="normal">I</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">C</mi><mo>-</mo><mi>IV</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">D</mi><mo>-</mo><mi>III</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>-</mo><mi mathvariant="normal">I</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">B</mi><mo>-</mo><mi>II</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">C</mi><mo>-</mo><mi>IV</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">D</mi><mo>-</mo><mi>III</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>-</mo><mi>II</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">B</mi><mo>-</mo><mi mathvariant="normal">I</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">C</mi><mo>-</mo><mi>III</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">D</mi><mo>-</mo><mi>IV</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>-</mo><mi mathvariant="normal">I</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">B</mi><mo>-</mo><mi>II</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">C</mi><mo>-</mo><mi>III</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">D</mi><mo>-</mo><mi>IV</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>-</mo><mi>II</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">B</mi><mo>-</mo><mi mathvariant="normal">I</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">C</mi><mo>-</mo><mi>IV</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">D</mi><mo>-</mo><mi>III</mi></math>**

**Detailed Solution:**

<p>For solid sphere</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9b482886-249b-42d9-ae6e-2018a8de370c-image.png" style="width: 120px; height: 186px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub><mo>=</mo><msub><mi>I</mi><mrow><mi>com</mi><mo>&#160;</mo></mrow></msub><mo>+</mo><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math>  (Using parallel axis theorem)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub><mo>=</mo><mfrac><mn>7</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>&#8594;</mo><mi>I</mi><mi>I</mi></math></p><p>For hollow sphere</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9b482886-249b-42d9-ae6e-2018a8de370c-image.png" style="width: 120px; height: 186px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msub><mi>I</mi><mi>com</mi></msub><mo>+</mo><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>&#8658;</mo><mi>B</mi><mo>&#8594;</mo><mi>I</mi></math></p><p>For Circular ring</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5efac0a7-111e-4477-bce2-9be673721334-image.png" style="width: 170px; height: 191px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msub><mi>I</mi><mn>3</mn></msub></math> ( Using perpendicular axis theorem)</p><p>By symmetry MOI</p><p>About <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> Axis are same i.e.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>2</mn><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msub><mi>I</mi><mn>3</mn></msub><mo>=</mo><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><msub><mi>I</mi><mrow><mi>c</mi><mi>o</mi><mi>m</mi></mrow></msub><mo>=</mo><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>&#8658;</mo><mo>&#160;</mo><mi>C</mi><mo>&#8594;</mo><mi>I</mi><mi>V</mi></math></p><p>Similarly in disc</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mfenced close="}" open="{"><mrow><mo>&#8757;</mo><msub><mi>I</mi><mi>com</mi></msub><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>&#8658;</mo><mi>D</mi><mo>&#8594;</mo><mi>I</mi><mi>I</mi><mi>I</mi></math></p>

</details>

---

### Q43. JEE Main 2022 (25 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Moment of Inertia (M.I.) of four bodies having same mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>R</mi></math> are as follows
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo></math> M.I. of solid sphere about its diameter
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo></math> M.I. of solid cylinder about its axis
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>3</mn></msub><mo>=</mo></math> M.I. of solid circular disc about its diameter
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>4</mn></msub><mo>=</mo></math> M.I. of thin circular ring about its diameter
If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><msub><mi>I</mi><mn>2</mn></msub><mo>+</mo><msub><mi>I</mi><mn>3</mn></msub></mrow></mfenced><mo>+</mo><msub><mi>I</mi><mn>4</mn></msub><mo>=</mo><mi>x</mi><msub><mi>I</mi><mn>1</mn></msub></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> will be _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mn>2</mn><mfenced><mrow><msub><mi>I</mi><mn>2</mn></msub><mo>+</mo><msub><mi>I</mi><mn>3</mn></msub></mrow></mfenced><mo>+</mo><msub><mi>I</mi><mn>4</mn></msub><mo>=</mo><mi>x</mi><msub><mi>I</mi><mn>1</mn></msub></math></p><p>Now</p><p>For solid sphere about its diameter <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math>,</p><p>For solid cylinder about its axis <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math>,</p><p>For circular disc about its diameter <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>3</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p>And for circular ring about its diameter <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>4</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></mrow></mfenced><mo>+</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>=</mo><mi>x</mi><mo>&#215;</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mi>x</mi><mo>&#215;</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>=</mo><mi>x</mi><mo>&#215;</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q44. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A system consists of two identical spheres each of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>kg</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>&#160;</mo><mi>cm</mi></math> at the ends of a light rod. The distance between the centres of the two spheres is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>.</mo></math> What will be the moment of inertia of the system about an axis perpendicular to the rod passing through its midpoint?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>905</mn><mo>&#215;</mo><msup><mn>10</mn><mn>5</mn></msup><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mo>.</mo><mn>75</mn><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn><mo>.</mo><mn>05</mn><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>875</mn><mo>&#215;</mo><msup><mn>10</mn><mn>5</mn></msup><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn><mo>.</mo><mn>05</mn><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/65215889-72dd-4818-a00d-b4b17d6b1e18-image.png" style="width: 445px; height: 224px;" />
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open=""><mrow><mi>I</mi><mo>=</mo><mfenced><mrow><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><mi>M</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>&#215;</mo><mn>2</mn><mo>=</mo><mfenced open="["><mrow><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>&#215;</mo><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><msup><mfenced><mrow><mn>0</mn><mo>.</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><msup><mfenced><mrow><mn>2</mn><mo>.</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></mrow></mfenced><mo>&#215;</mo><mn>2</mn><mo>=</mo><mo>[</mo><mn>0</mn><mo>.</mo><mn>15</mn><mo>+</mo><mn>9</mn><mo>.</mo><mn>375</mn><mo>]</mo><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>19</mn><mo>.</mo><mn>05</mn><msup><mi>kgm</mi><mn>2</mn></msup></math>

</details>

---

### Q45. JEE Main 2021 (27 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Moment of inertia of a square plate of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> about the axis passing through one of the corner and perpendicular to the plane of square plate is given by:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>M</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>M</mi><msup><mi>l</mi><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><msup><mi>l</mi><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>M</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mn mathvariant="bold">12</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>M</mi><msup><mi>l</mi><mn>2</mn></msup></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2ad3a86e-499a-4ba9-9031-2da1644ce354-image.png" style="width: 274px; height: 285px;" /></p><p>Use parallel axis theorem to get the magnitude of the moment of inertia of a square plate of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> about the axis passing through one of the corners and perpendicular to the plane of a square plate, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>z</mi></msub><mo>=</mo><msub><mi>I</mi><mi>cm</mi></msub><mo>+</mo><mi>M</mi><msup><mfenced><mfrac><mi>l</mi><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mi>z</mi></msub><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mn>6</mn></mfrac><mo>+</mo><mfrac><mrow><mi>M</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mi>M</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mn>6</mn></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>M</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mn>3</mn></mfrac></math>.</p>

</details>

---

### Q46. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The solid cylinder of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn><mo>&#160;</mo><mi>cm</mi></math> and mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> has a radius of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi>cm</mi><mo>.</mo></math> Calculate the density of the material used if the moment of inertia of the cylinder about an axis <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mi>D</mi></math> parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> as shown in figure is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>7</mn><mo>&#160;</mo><mi>kg</mi><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">m</mi></mrow><mn>2</mn></msup></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/13a668ec-f60a-4549-b8f1-66da20be28b9-image.png" style="width: 292px; height: 265px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>49</mn><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mn>1</mn></msup><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mo>.</mo><mn>9</mn><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>49</mn><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>r</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mfenced><mrow><mi>&#961;</mi><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup><mi>L</mi></mrow></mfenced><msup><mi>r</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mfenced><mrow><mi>&#961;</mi><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup><mi>L</mi></mrow></mfenced><mfrac><msup><mi>L</mi><mn>2</mn></msup><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#961;</mi><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup><mi>L</mi><mfenced><mrow><mfrac><msup><mi>r</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>L</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#961;</mi><mo>=</mo><mfrac><mi>I</mi><mrow><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup><mi>L</mi><mfenced><mrow><mfrac><msup><mi>r</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>L</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p>On putting the values, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#961;</mi><mo>=</mo><mn>1</mn><mo>.</mo><mn>49</mn><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>.</p>

</details>

---

### Q47. JEE Main 2021 (26 Aug Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Consider a badminton racket with length scales as shown in the figure.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b61ab3d4-c125-4d30-9ee0-74102bcbce5a-image.png" style="width: 387px; height: 247px;" /></p><p>If the mass of the linear and circular portions of the badminton racket are same (<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math>) and the mass of the threads are negligible, the moment of inertia of the racket about an axis perpendicular to the handle and in the plane of the ring at, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>r</mi><mn>2</mn></mfrac></math> distance from the end <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> of the handle will be ______<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><msup><mi>r</mi><mn>2</mn></msup></math>.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **52**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>A</mi></msub><mo>=</mo><mfenced open="[" close="]" separators="|"><mrow><mfrac><mrow><mi>M</mi><msup><mi>r</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mi>M</mi><msup><mfenced separators="|"><mrow><mn>7</mn><mi>r</mi><mo>&#8722;</mo><mfrac><mi>r</mi><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mfenced open="[" close="]" separators="|"><mrow><mfrac><mrow><mi>M</mi><mo>(</mo><mn>6</mn><mi>r</mi><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>12</mn></mfrac><mo>+</mo><mfenced separators="|"><mrow><mi>M</mi><msup><mfenced separators="|"><mrow><mn>3</mn><mi>r</mi><mo>&#8722;</mo><mfrac><mi>r</mi><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mfrac><mrow><mi>M</mi><msup><mi>r</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mi>M</mi><mfrac><mrow><mo>(</mo><mn>169</mn><mo>)</mo><msup><mi>r</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced open="{" close="}" separators="|"><mrow><mn>3</mn><mi>M</mi><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mfrac><mrow><mn>25</mn><mi>M</mi><msup><mi>r</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></mrow></mfenced><mspace linebreak="newline"/><mo>=</mo><mfrac><mrow><mn>171</mn><mi>M</mi><msup><mi>r</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>+</mo><mfrac><mrow><mn>37</mn><mi>M</mi><msup><mi>r</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mspace linebreak="newline"/><mo>=</mo><mfrac><mn>208</mn><mn>4</mn></mfrac><mi>M</mi><msup><mi>r</mi><mn>2</mn></msup><mspace linebreak="newline"/><mo>=</mo><mn>52</mn><mi>M</mi><msup><mi>r</mi><mn>2</mn></msup></math></p>

</details>

---

### Q48. JEE Main 2021 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>In the given figure, two wheels <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> are connected by a belt <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>. The radius of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is three times that of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>. In the case of the same rotational kinetic energy, the ratio of rotational inertias <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mfrac></mfenced></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>:</mo><mo>&#160;</mo><mn>1</mn><mo>&#160;</mo><mo>.</mo></math> The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> will be ______.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/da73d93b-d7f3-4c43-825f-2bd297ac2f20-image.png" style="width: 348px; height: 155px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/421d0ba7-edb0-49fe-b736-8421ccdbe88b-image.png" style="width: 358px; height: 159px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>I</mi><mn>1</mn></msub><msup><mfenced><msub><mi>&#969;</mi><mn>1</mn></msub></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>I</mi><mn>2</mn></msub><msup><mfenced><msub><mi>&#969;</mi><mn>2</mn></msub></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><msup><mfenced><mfrac><mi>v</mi><mrow><mn>3</mn><mi>R</mi></mrow></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub><msup><mfenced><mfrac><mi mathvariant="italic">v</mi><mi mathvariant="italic">R</mi></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>1</mn></mfrac></math></p>

</details>

---

### Q49. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>The figure shows two solid discs with radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> respectively. If mass per unit area is the same for both, what is the ratio of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>I</mi></math> of bigger disc around axis <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> (Which is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8869;</mo></math> to the plane of the disc and passing through its centre) of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>I</mi></math> of smaller disc around one of its diameters lying on its plane? Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is the mass of the larger disc.</p><p>(<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>I</mi></math> stands for a moment of inertia)</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/abcc741d-63a6-4ca9-bfa9-496b647386c5-image.png" style="width: 224px; height: 212px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>R</mi><mn>2</mn></msup><mo>:</mo><mo>&#160;</mo><msup><mi>r</mi><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>r</mi><mn>4</mn></msup><mo>:</mo><mo>&#160;</mo><msup><mi>R</mi><mn>4</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>R</mi><mn>2</mn></msup><mo>:</mo><mo>&#160;</mo><msup><mi>r</mi><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>R</mi><mn>4</mn></msup><mo>:</mo><mo>&#160;</mo><msup><mi>r</mi><mn>4</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>R</mi><mn>4</mn></msup><mo>:</mo><mo>&#160;</mo><msup><mi>r</mi><mn>4</mn></msup></math>**

**Detailed Solution:**

<p>Ratio of the moment of inertia <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>m</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#963;&#960;</mi><msup><mi>R</mi><mn>2</mn></msup><msup><mi>R</mi><mn>2</mn></msup></mrow><mrow><mi>&#963;</mi><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>R</mi><mn>4</mn></msup></mrow><msup><mi>r</mi><mn>4</mn></msup></mfrac></math></p>

</details>

---

### Q50. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td>List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math></td>			<td>List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">a</mi><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>I</mi></math> of the rod (length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>,</mo></math> Mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>,</mo></math> about an axis <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8869;</mo></math> to the rod passing through the midpoint)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>8</mn><mi>M</mi><msup><mi>L</mi><mn mathvariant="italic">2</mn></msup></mrow><mn>3</mn></mfrac></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">b</mi><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>I</mi></math> of the rod (length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>,</mo></math> Mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">M</mi><mo>,</mo></math> about an axis <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8869;</mo></math> to the rod passing through one of its end)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>ii</mi><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>M</mi><msup><mi>L</mi><mn mathvariant="italic">2</mn></msup></mrow><mn>3</mn></mfrac></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">c</mi><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>I</mi></math> of the rod (length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">L</mi><mo>,</mo></math> Mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo mathvariant="italic">,</mo></math> about an axis <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8869;</mo></math> to the rod passing through its midpoint)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>iii</mi><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup></mrow><mn>12</mn></mfrac></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">d</mi><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>I</mi></math> of the rod (Length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>L</mi><mo>,</mo></math> Mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">M</mi><mo>,</mo></math> about an axis <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8869;</mo></math> to the rod passing through one of its end)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>iv</mi><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup></mrow><mn>3</mn></mfrac></math></td>		</tr>	</tbody></table><p>Choose the correct answer from the options given below:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">a</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>ii</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">b</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iii</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">c</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">d</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iv</mi><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">a</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>ii</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">b</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">c</mi><mo>)</mo><mo>-</mo><mo>&#160;</mo><mo>(</mo><mi>iii</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">d</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iv</mi><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">a</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iii</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">b</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iv</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">c</mi><mo>)</mo><mo>-</mo><mo>&#160;</mo><mo>(</mo><mi>ii</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">d</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">a</mi><mo>)</mo><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mo>(</mo><mi>iii</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">b</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iv</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">c</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">d</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>ii</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">a</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iii</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">b</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iv</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">c</mi><mo>)</mo><mo>-</mo><mo>&#160;</mo><mo>(</mo><mi>ii</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">d</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5555b6be-b9ac-4add-8f63-56a32a6ec2d3-image.png" style="width: 300px; height: 278px;" />

</details>

---

### Q51. JEE Main 2021 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

A solid disc of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi>cm</mi></math> and mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>kg</mi></math> is rotating with an angular velocity of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>600</mn><mo>&#160;</mo><mi>rpm</mi></math>, about an axis normal to its circular plane and passing through its centre of mass. The retarding torque required to bring the disc at rest in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> is _________<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#964;</mi><mo>=</mo><mfrac><mrow><mi>&#916;</mi><mi>L</mi></mrow><mrow><mi>&#916;</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>I</mi><mfenced><mrow><msub><mi>&#969;</mi><mi>f</mi></msub><mo>-</mo><msub><mi>&#969;</mi><mi>i</mi></msub></mrow></mfenced></mrow><mrow><mi>&#916;</mi><mi>t</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#964;</mi><mo>=</mo><mfrac><mrow><mfrac><mrow><mi>m</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>&#215;</mo><mo>[</mo><mn>0</mn><mo>-</mo><mi>&#969;</mi><mo>]</mo></mrow><mrow><mi>&#916;</mi><mi>t</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>10</mn><mo>&#215;</mo><msup><mfenced><mrow><mn>20</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mrow><mn>600</mn><mo>&#215;</mo><mi>&#960;</mi></mrow><mrow><mn>30</mn><mo>&#215;</mo><mn>10</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>4</mn><mi>&#960;</mi><mo>=</mo><mn>4</mn><mi>&#960;</mi><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p>

</details>

---

### Q52. JEE Main 2021 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R.</p><p>Assertion A: Moment of inertia of a circular disc of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>,</mo><mi>Y</mi></math> axes (passing through its plane) and Z-axis which is perpendicular to its plane were found to be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi mathvariant="normal">x</mi></msub><mo>,</mo><msub><mi>I</mi><mi mathvariant="normal">y</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi mathvariant="normal">z</mi></msub></math>, respectively. The respective radii of gyration about all the three axes will be the same.</p><p>Reason R: A rigid body making rotational motion has fixed mass and shape. In the light of the above statements, choose the most appropriate answer from the options given below:</p>

**Options:**

- **(A)** Both A and R are correct but R is not the correct explanation of A.
- **(B)** A is not correct but R is correct.
- **(C)** A is correct but R is not correct.
- **(D)** Both A and R are correct and R is the correct
explanation of A.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) A is not correct but R is correct.**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>z</mi></msub><mo>=</mo><msub><mi>I</mi><mi>x</mi></msub><mo>+</mo><msub><mi>I</mi><mi>y</mi></msub></math> (using perpendicular axis theorem)</p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mi>m</mi><msup><mi>k</mi><mn>2</mn></msup><mo>(</mo><mi>K</mi><mo>:</mo></math> radius of gyration) </p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><msubsup><mi>K</mi><mi mathvariant="normal">z</mi><mn>2</mn></msubsup><mo>=</mo><mi>m</mi><msubsup><mi>K</mi><mi mathvariant="normal">x</mi><mn>2</mn></msubsup><mo>+</mo><mi>m</mi><msubsup><mi>K</mi><mi mathvariant="normal">y</mi><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>K</mi><mi mathvariant="normal">z</mi><mn>2</mn></msubsup><mo>=</mo><msubsup><mi>K</mi><mi mathvariant="normal">x</mi><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>K</mi><mi mathvariant="normal">y</mi><mn>2</mn></msubsup></math></p><p>So radius of gyration about axes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> will not be same, hence assertion A is not correct reason R is correct statement (property of a rigid body).</p>

</details>

---

### Q53. JEE Main 2021 (18 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider a uniform wire of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math>. It is bent into a semicircle. Its moment of inertia about a line perpendicular to the plane of the wire passing through the centre is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><mfrac><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup></mrow><msup><mi>&#960;</mi><mn>2</mn></msup></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>5</mn></mfrac><mfrac><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup></mrow><msup><mi>&#960;</mi><mn>2</mn></msup></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup></mrow><msup><mi>&#960;</mi><mn>2</mn></msup></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfrac><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup></mrow><msup><mi>&#960;</mi><mn>2</mn></msup></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup></mrow><msup><mi>&#960;</mi><mn>2</mn></msup></mfrac></math>**

**Detailed Solution:**

<div><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mi>r</mi><mo>=</mo><mi>L</mi><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mfrac><mi>L</mi><mi>&#960;</mi></mfrac></math></div><div><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mi>M</mi><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup></mrow><msup><mi>&#960;</mi><mn>2</mn></msup></mfrac></math></div>

</details>

---

### Q54. JEE Main 2021 (18 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A thin circular ring of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> is rotating about its axis with an angular speed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>.</mo></math> Two particles having mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> each are now attached at diametrically opposite points. The angular speed of the ring will become:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mfrac><mi>M</mi><mrow><mi>M</mi><mo>+</mo><mi>m</mi></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mfrac><mrow><mi>M</mi><mo>+</mo><mn>2</mn><mo>&#160;</mo><mi>m</mi></mrow><mi>M</mi></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mfrac><mi>M</mi><mrow><mi>M</mi><mo>+</mo><mn>2</mn><mo>&#160;</mo><mi>m</mi></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mfrac><mrow><mi>M</mi><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>m</mi></mrow><mrow><mi>M</mi><mo>+</mo><mn>2</mn><mo>&#160;</mo><mi>m</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mfrac><mi>M</mi><mrow><mi>M</mi><mo>+</mo><mn>2</mn><mo>&#160;</mo><mi>m</mi></mrow></mfrac></math>**

**Detailed Solution:**

<p>Using conservation of angular momentum
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>M</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced><mi>&#969;</mi><mo>=</mo><mfenced><mrow><mi>M</mi><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>m</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced><msup><mi>&#969;</mi><mo>'</mo></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#969;</mi><mo>'</mo></msup><mo>=</mo><mfrac><mrow><mi>M</mi><mi>&#969;</mi></mrow><mrow><mi>M</mi><mo>+</mo><mn>2</mn><mo>&#160;</mo><mi>m</mi></mrow></mfrac></math>.</p>

</details>

---

### Q55. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Four equal masses, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> each are placed at the corners of a square of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>l</mi></mfenced></math> as shown in the figure. The moment of inertia of the system about an axis passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mi>B</mi></math> would be :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cdbbb4b4-04b5-4004-9195-da9732cf82be-image.png" style="width: 224px; height: 233px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><msup><mi>l</mi><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>m</mi><msup><mi>l</mi><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi>m</mi><msup><mi>l</mi><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi>m</mi><msup><mi>l</mi><mn>2</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi>m</mi><msup><mi>l</mi><mn>2</mn></msup></math>**

**Detailed Solution:**

<p>Moment of inertia of point mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#215;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>Perpendicular</mi><mo>&#160;</mo><mi>distance</mi><mo>&#160;</mo><mi>from</mi><mo>&#160;</mo><mi>axis</mi></mrow></mfenced><mn>2</mn></msup></math></p><p style="margin:0cm 0cm 8pt"><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/73e0535d-bd94-41a1-ad80-de736993e02e-image.png" style="width: 241px; height: 245px;" /></p><p style="margin:0cm 0cm 8pt">Moment of Inertia </p><p style="margin:0cm 0cm 8pt"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>m</mi><msup><mfenced><mn>0</mn></mfenced><mn>2</mn></msup><mo>+</mo><mi>m</mi><msup><mfenced><mrow><mi>l</mi><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mi>m</mi><msup><mfenced><mfrac><mi>l</mi><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mi>m</mi><msup><mfenced><mfrac><mi>l</mi><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mn>2</mn></msup></math></p><p style="margin:0cm 0cm 8pt"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi>m</mi><msup><mi>l</mi><mn>2</mn></msup></math></p>

</details>

---

### Q56. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A cord is wound round the circumference of wheel of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mi></mi></math>, The axis of the wheel is horizontal and the moment of inertia about it is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math>. A weight <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mi>g</mi></math> is attached to the cord at the end. The weight falls from rest. After falling through a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">h</mi><mo>,</mo></math> the square of angular velocity of wheel will be

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>m</mi><mi>g</mi><mi>h</mi></mrow><mrow><mi>I</mi><mo>+</mo><mi>m</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>m</mi><mi>g</mi><mi>h</mi></mrow><mrow><mi>I</mi><mo>+</mo><mn>2</mn><mi>m</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>g</mi><mi>h</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>g</mi><mi>h</mi></mrow><mrow><mi>I</mi><mo>+</mo><mi>m</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>m</mi><mi>g</mi><mi>h</mi></mrow><mrow><mi>I</mi><mo>+</mo><mi>m</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6b9ebf58-fa51-4c9e-9075-eecd7507b685-image.png" style="width: 103px; height: 188px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mi>g</mi><mi>h</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>I</mi><msup><mi>&#969;</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>m</mi><msup><mi>v</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mi>&#969;</mi><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mi>g</mi><mi>h</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>I</mi><msup><mi>&#969;</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;</mo><mi>m</mi><msup><mi>&#969;</mi><mn>2</mn></msup><msup><mi>r</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>m</mi><mi>g</mi><mi>h</mi></mrow><mfenced><mrow><mi>I</mi><mo>+</mo><mi>m</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced></mfrac><mo>=</mo><msup><mi>&#969;</mi><mn>2</mn></msup></math></p>

</details>

---

### Q57. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Four identical solid spheres each of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> are placed with their centres on the four corners of a square of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>. The moment of inertia of the system about one side of square where the axis of rotation is parallel to the plane of the square is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>5</mn></mfrac><mi>m</mi><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mi>m</mi><msup><mi>b</mi><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>5</mn></mfrac><mi>m</mi><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>m</mi><msup><mi>b</mi><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>5</mn></mfrac><mi>m</mi><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>m</mi><msup><mi>b</mi><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>5</mn></mfrac><mi>m</mi><msup><mi>a</mi><mn>2</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>5</mn></mfrac><mi>m</mi><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>m</mi><msup><mi>b</mi><mn>2</mn></msup></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/03e59b7d-0060-477f-a1c1-019cf4fc276d-image.png" style="width: 177px; height: 140px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>2</mn><mo>&#215;</mo><mfenced><mrow><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>m</mi><msup><mi>a</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mn>2</mn><mo>&#215;</mo><mfenced><mrow><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>m</mi><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mi>m</mi><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><mi>m</mi><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>m</mi><msup><mi>b</mi><mn>2</mn></msup></math></p>

</details>

---

### Q58. JEE Main 2021 (24 Feb Shift 2)

*Type:* `numerical` | *Level:* `3`

A uniform thin bar of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi>kg</mi></math> and length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>4</mn></math> meter is bent to make an equilateral hexagon. The moment of inertia about an axis passing through the centre of mass and perpendicular to the plane of hexagon is ___________ <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>.</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d7d8da66-a7ef-4ae6-a092-47cc20108b17-image.png" style="width: 370px; height: 206px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>61</mn><mo>=</mo><mn>2</mn><mo>.</mo><mn>4</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="box"><mi>&#8467;</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></menclose></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mo>&#160;</mo><mn>60</mn><mo>&#176;</mo><mo>=</mo><mfrac><mi>r</mi><mi>&#8467;</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mn>60</mn><mo>&#176;</mo><mo>=</mo><mfrac><mrow><mi>&#8467;</mi><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p>MOI, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfenced close="]" open="["><mrow><mfrac><mrow><mi>m</mi><msup><mi>&#8467;</mi><mn>2</mn></msup></mrow><mn>12</mn></mfrac><mo>+</mo><mi>m</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><mfrac><mrow><mi>m</mi><msup><mi>&#8467;</mi><mn>2</mn></msup></mrow><mn>12</mn></mfrac><mo>+</mo><mi>m</mi><msup><mfenced><mfrac><mrow><mi>&#8467;</mi><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></mrow></mfenced><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi>m</mi><msup><mi>l</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>8</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math></p></blockquote>

</details>

---

### Q59. JEE Main 2021 (24 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Moment of inertia <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="normal">M</mi><mo>.</mo><mi mathvariant="normal">I</mi><mo>.</mo></mrow></mfenced></math> of four bodies, having same mass and radius, are reported as;</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mi mathvariant="normal">M</mi><mo>.</mo><mi mathvariant="normal">I</mi><mo>.</mo></math> of thin circular ring about its diameter,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mi mathvariant="normal">M</mi><mo>.</mo><mi mathvariant="normal">I</mi><mo>.</mo></math> of circular disc about an axis perpendicular to disc and going through the centre,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>3</mn></msub><mo>=</mo><mi mathvariant="normal">M</mi><mo>.</mo><mi mathvariant="normal">I</mi><mo>.</mo></math> of solid cylinder about its axis and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>4</mn></msub><mo>=</mo><mi mathvariant="normal">M</mi><mo>.</mo><mi mathvariant="normal">I</mi><mo>.</mo></math> of solid sphere about its diameter.</p><p>Then:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msub><mi>I</mi><mn>3</mn></msub><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><msub><mi>I</mi><mn>4</mn></msub></math>.
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>3</mn></msub><mo>&#60;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>+</mo><msub><mi>I</mi><mn>4</mn></msub></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msub><mi>I</mi><mn>3</mn></msub><mo>&#62;</mo><msub><mi>I</mi><mn>4</mn></msub></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msub><mi>I</mi><mn>3</mn></msub><mo>&#60;</mo><msub><mi>I</mi><mn>4</mn></msub></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msub><mi>I</mi><mn>3</mn></msub><mo>&#62;</mo><msub><mi>I</mi><mn>4</mn></msub></math>**

**Detailed Solution:**

<p>Ring <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math> about diameter</p><p>Disc <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math></p><p>Solid cylinder <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>3</mn></msub><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math></p><p>Solid sphere <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>4</mn></msub><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msub><mi>I</mi><mn>3</mn></msub><mo>&#62;</mo><msub><mi>I</mi><mn>4</mn></msub></math></p>

</details>

---

### Q60. JEE Main 2020 (06 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The linear mass density of a thin rod <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AB</mi></math> of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi></math> varies from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#955;</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><msub><mi mathvariant="normal">&#955;</mi><mn>0</mn></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mi mathvariant="normal">x</mi><mi mathvariant="normal">L</mi></mfrac></mrow></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi></math> is the distance from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math> is the mass of the rod then its moment of inertia about an axis passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> and perpendicular to the rod :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>12</mn></mfrac><msup><mi>ML</mi><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>18</mn></mfrac><msup><mi>ML</mi><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>5</mn></mfrac><msup><mi>ML</mi><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>7</mn></mfrac><msup><mi>ML</mi><mn>2</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>18</mn></mfrac><msup><mi>ML</mi><mn>2</mn></msup></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5e2fa8da-fdb5-4aec-a0a6-4c8fd31cddce-image.png" style="width: 317px; height: 81px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>dm</mi><mo>=</mo><mi mathvariant="normal">&#955;</mi><mo>.</mo><mi>dv</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>dI</mi><mo>=</mo><mi>dm</mi><mo>.</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi mathvariant="normal">&#955;</mi><mn>0</mn></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mi mathvariant="normal">x</mi><mi mathvariant="normal">L</mi></mfrac></mrow></mfenced><mo>.</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><msub><mi mathvariant="normal">&#955;</mi><mn>0</mn></msub><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>+</mo><mfrac><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mi mathvariant="normal">L</mi></mfrac></mrow></mfenced><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi mathvariant="normal">&#955;</mi><mn>0</mn></msub><msubsup><mfenced close="|" open="|"><mrow><mfrac><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mfrac><msub><mi mathvariant="normal">x</mi><mn>4</mn></msub><mrow><mn>4</mn><mi mathvariant="normal">L</mi></mrow></mfrac></mrow></mfenced><mn>0</mn><mi mathvariant="normal">L</mi></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi mathvariant="normal">&#955;</mi><mn>0</mn></msub><mfenced close="]" open="["><mrow><mfrac><msup><mi mathvariant="normal">L</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mfrac><msub><mi mathvariant="normal">L</mi><mn>3</mn></msub><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mrow><mn>7</mn><msub><mi mathvariant="normal">&#955;</mi><mn>0</mn></msub><msup><mi mathvariant="normal">L</mi><mn>3</mn></msup></mrow><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mi mathvariant="normal">L</mi></munderover><mi>&#955;dx</mi><mo>=</mo><mfrac><mrow><mn>3</mn><msub><mi mathvariant="normal">&#955;</mi><mn>0</mn></msub><mi mathvariant="normal">L</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">I</mi><mi mathvariant="normal">m</mi></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup></mrow><mrow><mn>12</mn><mo>&#215;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup></mrow><mn>18</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mn>7</mn><mn>18</mn></mfrac><msup><mi>mL</mi><mn>2</mn></msup></math></p><p> </p>

</details>

---

### Q61. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Shown in the figure is a hollow ice-cream cone (it is open at top). If its mass is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math>, radius of its top is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi></math> and height, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">H</mi></math>, then its moment of inertia about its axis is</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/eb02c1ca-ac0e-48eb-9505-899ed438a4f7-image.png" style="width: 152px; height: 260px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>MR</mi><mn>2</mn></msup><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">M</mi><mfenced><mrow><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">H</mi><mn>2</mn></msup></mrow></mfenced></mrow><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>MH</mi><mn>2</mn></msup><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>MR</mi><mn>2</mn></msup><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>MR</mi><mn>2</mn></msup><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>It can be assumed as several parts of discs having different radius, so</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/393649f4-7d5d-4b12-9c2c-d0545a5208b5-image.png" style="width: 155px; height: 183px;" />  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><mo>&#8747;</mo><mi>dl</mi><mo>=</mo><mo>&#8747;</mo><mi>dm</mi><mfenced><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mfenced></math></p><p>From diagram</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>r</mi><mi>y</mi></mfrac><mo>=</mo><mi>tan</mi><mtext>&#952;</mtext><mo>=</mo><mfrac><mi>R</mi><mi>H</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mfrac><mi>R</mi><mi>H</mi></mfrac><mo>&#183;</mo><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>dm</mi><mo>=</mo><mtext>&#961;</mtext><mfenced><mrow><mtext>&#960;</mtext><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mrow></mfenced><mi>dy</mi></math></p><p>From equation (i), (ii) and (iii)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math></p>

</details>

---

### Q62. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p><img height="137" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/68982c09-79a7-4762-994c-a72716815c0f-image.png" width="144" /> </p><p>For a uniform rectangular sheet shown in the figure, the ratio of moments of inertia about the axes perpendicular to the sheet and passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">O</mi></math> (the centre of mass) and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">O</mi></math>&#39; (corner point) is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>/</mo><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>/</mo><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>/</mo><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>/</mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>/</mo><mn>4</mn></math>**

**Detailed Solution:**

<p>We will use Parallel Axes Theorem here,</p><p>Distance between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><msup><mi>O</mi><mo>'</mo></msup></math> is,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><msup><mi>O</mi><mo>'</mo></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msqrt><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mfrac><msup><mi>a</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><mn>4</mn></mfrac></msqrt></math></p><p>So, according to parallel axis theorem we have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi mathvariant="normal">I</mi><mi mathvariant="normal">O</mi></msub><msub><mi mathvariant="normal">I</mi><msup><mi mathvariant="normal">O</mi><mo>&#39;</mo></msup></msub></mfrac><mo>=</mo><mfrac><mrow><mfrac><mi mathvariant="normal">M</mi><mn>12</mn></mfrac><mfenced><mrow><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">b</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mfrac><mi mathvariant="normal">M</mi><mn>12</mn></mfrac><mfenced><mrow><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">b</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mi mathvariant="normal">M</mi><mfenced><mrow><mfrac><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><msup><mi mathvariant="normal">b</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mfrac><mi mathvariant="normal">M</mi><mn>12</mn></mfrac><mfenced><mrow><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">b</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mfrac><mi mathvariant="normal">M</mi><mn>3</mn></mfrac><mfenced><mrow><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">b</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math> </p>

</details>

---

### Q63. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Consider two uniform discs of the same thickness and different radii  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mi>&#945;</mi><mi>R</mi></math> made of the same material. If the ratio of their moments of inertia <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub></math>, respectively, about their axes is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>:</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>:</mo><mn>16</mn></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Moment of inertia of disc is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><msup><mi>MR</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mfenced open="[" close="]"><mrow><mi mathvariant="normal">&#961;</mi><mfenced><msup><mi>&#960;R</mi><mn>2</mn></msup></mfenced><mi mathvariant="normal">t</mi></mrow></mfenced><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>&#160;</mo><msup><mi mathvariant="normal">R</mi><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub><msub><mi mathvariant="normal">I</mi><mn>1</mn></msub></mfrac><mo>=</mo><msup><mfenced><mfrac><msub><mi mathvariant="normal">R</mi><mn>2</mn></msub><msub><mi mathvariant="normal">R</mi><mn>1</mn></msub></mfrac></mfenced><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>16</mn><mn>1</mn></mfrac><mo>=</mo><msup><mi mathvariant="normal">&#945;</mi><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#945;</mi><mo>=</mo><mn>2</mn></math> </p>

</details>

---

### Q64. JEE Main 2020 (04 Sep Shift 1)

*Type:* `numerical` | *Level:* `2`

<p><math><mrow><mi>A</mi><mi>B</mi><mi>C</mi></mrow></math> is a plane lamina of the shape of an equilateral triangle. <math><mrow><mi>D</mi><mo>,</mo><mo>&#160;</mo><mi>E</mi></mrow></math> are mid-points of <math><mrow><mi>A</mi><mi>B</mi><mo>,</mo><mo>&#160;</mo><mi>A</mi><mi>C</mi></mrow></math> and <math><mi>G</mi></math> is the centroid of the lamina. Moment of inertia of the lamina about an axis passing through <math><mi>G</mi></math> and perpendicular to the plane <math><mrow><mi>A</mi><mi>B</mi><mi>C</mi></mrow></math> is <math><mrow><msub><mi>I</mi><mn>0</mn></msub></mrow></math>. If part <math><mrow><mi>A</mi><mi>D</mi><mi>E</mi></mrow></math> is removed, the moment of inertia of the remaining part about the same axis is <math><mrow><mfrac><mrow><mi>N</mi><msub><mi>I</mi><mn>0</mn></msub></mrow><mrow><mn>16</mn></mrow></mfrac></mrow></math> where <math><mi>N</mi></math> is an integer. Value of <math><mi>N</mi></math> is:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bf713175-08d5-4dc1-8547-7dd0460fb38d-image.png" style="width: 109px; height: 110px;" /> </p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **11**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/89390183-377b-4af5-bb55-d81d6b0af44f-image.png" style="width: 136px; height: 141px;" /></p><p>Let mass of lamina <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>m</mi></math>, and length of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi mathvariant="script">l</mi></math>, then moment of inertila of lamina about an axis passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi></math> and perpendicular to the plane.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub><mo>&#8733;</mo><mi>m</mi><msup><mi mathvariant="script">l</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub><mo>=</mo><mi>k</mi><mi>m</mi><msup><mi mathvariant="script">l</mi><mn>2</mn></msup></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/964d9380-5543-436b-9237-b4e7cb1a2500-image.png" style="width: 156px; height: 161px;" /></p><p>Let moment of inertila of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mi>E</mi><mi>F</mi><mo>=</mo><msub><mi>I</mi><mn>1</mn></msub></math> about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi></math></p><p>then, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>16</mn></mfrac></math></p><p>then,<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mrow><mi>A</mi><mi>D</mi><mi>E</mi></mrow></msub><mo>=</mo><msub><mi>I</mi><mrow><mi>B</mi><mi>D</mi><mi>F</mi></mrow></msub><mo>=</mo><msub><mi>I</mi><mrow><mi>E</mi><mi>F</mi><mi>C</mi></mrow></msub><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msub><mi>I</mi><mn>2</mn></msub><mo>+</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msub><mi>I</mi><mn>0</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msub><mi>I</mi><mn>2</mn></msub><mo>+</mo><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>16</mn></mfrac><mo>=</mo><msub><mi>I</mi><mn>0</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mn>5</mn><msub><mi>I</mi><mn>0</mn></msub></mrow><mn>16</mn></mfrac></math></p><p>So, Moment of inertila of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mi>E</mi><mi>C</mi><mi>B</mi><mo mathvariant="italic">=</mo><mn mathvariant="italic">2</mn><msub><mi>I</mi><mn mathvariant="italic">2</mn></msub><mo mathvariant="italic">+</mo><msub><mi>I</mi><mn mathvariant="italic">1</mn></msub><mn mathvariant="italic">2</mn><mfenced><mfrac><mrow><mn mathvariant="italic">5</mn><msub><mi mathvariant="italic">I</mi><mn mathvariant="italic">0</mn></msub></mrow><mn mathvariant="italic">16</mn></mfrac></mfenced><mo mathvariant="italic">+</mo><mfenced><mfrac><msub><mi mathvariant="italic">I</mi><mn mathvariant="italic">0</mn></msub><mn mathvariant="italic">16</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">=</mo><mfrac><mrow><mn mathvariant="italic">11</mn><msub><mi>I</mi><mn mathvariant="italic">0</mn></msub></mrow><mn mathvariant="italic">16</mn></mfrac></math></p>

</details>

---

### Q65. JEE Main 2020 (03 Sep Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>An massless equilateral triangle EFG of side &#39;a&#39; (As shown in figure) has three particles of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi></math> situated at its vertices. The moment of inertia of the system about the line EX perpendicular to EG in the plane of EFG is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">N</mi><mn>20</mn></mfrac><msup><mi>ma</mi><mn>2</mn></msup></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math> is an integer. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math> is ___________ .</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/73ba7dbe-ddce-4767-9ea1-9b2a1b2db46d-image.png" style="width: 91px; height: 104px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><mi mathvariant="normal">m</mi><mo>&#215;</mo><msup><mi mathvariant="normal">O</mi><mn>2</mn></msup><mo>+</mo><msup><mi>ma</mi><mn>2</mn></msup><mo>+</mo><mi mathvariant="normal">m</mi><msup><mfenced><mfrac><mi mathvariant="normal">a</mi><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>5</mn><mn>4</mn></mfrac><msup><mi>ma</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>25</mn><mn>20</mn></mfrac><msup><mi>ma</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi><mo>=</mo><mn>25</mn></math></p>

</details>

---

### Q66. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Moment of inertia of a cylinder of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi><mo>,</mo></math> length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi></math> about an axis passing through its centre and perpendicular to the axis of the cylinder is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mi>M</mi><mfenced><mrow><mfrac><msup><mi>R</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><msup><mi>L</mi><mn>2</mn></msup><mn>12</mn></mfrac></mrow></mfenced><mo>.</mo></math> If such a cylinder is to be made for a given mass of a material, the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>L</mi><mi>R</mi></mfrac></math> for it to have minimum possible <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>3</mn><mn>2</mn></mfrac></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>2</mn><mn>3</mn></mfrac></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>3</mn><mn>2</mn></mfrac></msqrt></math>**

**Detailed Solution:**

<p>Let a cylinder of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">m</mi><mn>1</mn></msub></math>, length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi></math> then take elementary disc of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi></math> and trickiness <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>dx</mi></math> at distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi></math> from axis <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>O</mi><mo>&#39;</mo></math> then moment of inertia about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>O</mi><mo>&#39;</mo></math> as this element</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/de968068-2d76-4a86-9ca1-fb93342a9e87-image.png" style="width: 350px; height: 165px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>dl</mi><mo>=</mo><mfrac><msup><mi>dmR</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><msup><mi>dmx</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><mo>&#8747;</mo><mi>dl</mi><mo>=</mo><mo>&#8747;</mo><mfrac><msup><mi>dmR</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mi mathvariant="normal">n</mi><mo>=</mo><mi mathvariant="normal">L</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi mathvariant="normal">n</mi><mo>=</mo><mo>-</mo><mi mathvariant="normal">L</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfrac><mi mathvariant="normal">M</mi><mi mathvariant="normal">L</mi></mfrac><mi>dx</mi><mo>&#215;</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><msup><mi>MR</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><msup><mi>ML</mi><mn>2</mn></msup><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mi mathvariant="normal">M</mi><mn>4</mn></mfrac><mo>&#215;</mo><mfrac><mi mathvariant="normal">V</mi><mi>&#960;L</mi></mfrac><mo>+</mo><mfrac><msup><mi>ML</mi><mn>2</mn></msup><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>dI</mi><mi>dL</mi></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><mi>m</mi><mi>V</mi></mrow><mrow><mn>4</mn><msup><mi>&#960;L</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mi mathvariant="normal">M</mi><mo>&#215;</mo><mn>2</mn><mi mathvariant="normal">L</mi></mrow><mn>12</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>&#960;L</mi><mn>3</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>&#960;R</mi><mn>2</mn></msup><mi mathvariant="normal">L</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>&#960;L</mi><mn>3</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mi mathvariant="normal">L</mi><mi mathvariant="normal">R</mi></mfrac><mo>=</mo><msqrt><mfrac><mn>3</mn><mn>2</mn></mfrac></msqrt></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mi>MV</mi><mrow><mn>4</mn><mi>&#960;L</mi></mrow></mfrac><mo>+</mo><mfrac><msup><mi>ML</mi><mn>2</mn></msup><mn>12</mn></mfrac></mrow></mfenced></math></p>

</details>

---

### Q67. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1479427_1697291_ans_7df680f30ec7439a9c4fb9778f2a9aa5.png" />

Three solid spheres each of mass <math><mi>m</mi></math> and diameter <math><mi>d</mi></math> are stuck together such that the lines connecting the centres form an equilateral triangle of side of length <math><mi>d</mi></math> . The ratio <math><mfrac><mrow><msub><mrow><mi>I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msub><mrow><mi>I</mi></mrow><mrow><mi>A</mi></mrow></msub></mrow></mfrac></math> of moment of inertia <math><msub><mrow><mi>I</mi></mrow><mrow><mn>0</mn></mrow></msub></math> of the system about an axis passing the centroid and about center of any of the spheres <math><msub><mrow><mi>I</mi></mrow><mrow><mi>A</mi></mrow></msub></math> and perpendicular to the plane of the triangle is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>23</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>15</mn></mrow><mrow><mn>13</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>23</mn></mrow><mrow><mn>13</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>23</mn></mrow></mfrac></math>**

**Detailed Solution:**

M.I about O <math><mo>=</mo><mn>3</mn><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi>M</mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>M</mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>d</mi></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>13</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
M.I about A <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced open="[" close="]" separators="|"><mrow><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mfenced separators="|"><mfrac><mi>d</mi><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mi>M</mi><msup><mfenced separators="|"><mi>d</mi></mfenced><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mfenced separators="|"><mfrac><mi>d</mi><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>23</mn><mn>10</mn></mfrac><mi>M</mi><msup><mi>d</mi><mn>2</mn></msup></math>
Now ratio <math><mo>=</mo><mfrac><mrow><mn>13</mn></mrow><mrow><mn>23</mn></mrow></mfrac></math>

</details>

---

### Q68. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Mass per unit area of a circular disc of radius a depends on the distance <math><mi>r</mi></math> from its centre as <math><mi>&#963;</mi><mfenced separators="|"><mrow><mi>r</mi></mrow></mfenced><mo>=</mo><mi>A</mi><mo>+</mo><mi>B</mi><mi>r</mi></math> . The moment of inertia of the disc about the axis, perpendicular to the plane and passing through its centre is:

**Options:**

- **(A)** <math><mn>2</mn><mi>π</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>4</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mi>A</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>a</mi><mi>B</mi></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></math>
- **(B)** <math><mn>2</mn><mi>π</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>4</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mi>a</mi><mi>A</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>B</mi></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></math>
- **(C)** <math><mi>π</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>4</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mi>A</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>a</mi><mi>B</mi></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></math>
- **(D)** <math><mn>2</mn><mi>π</mi><msup><mrow><mtext>a</mtext></mrow><mrow><mn>4</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mtext>A</mtext></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mtext>B</mtext></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>2</mn><mi>π</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>4</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mi>A</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>a</mi><mi>B</mi></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/03c9f12d-aace-4b1e-853d-f4cb35001b01-image.png" style="width: 173px; height: 169px;" />
<math><mi mathvariant="normal">&#963;</mi><mo>=</mo><mi mathvariant="normal">A</mi><mo>+</mo><mi mathvariant="normal">B</mi><mi mathvariant="normal">r</mi></math>
<math><mrow><mo stretchy="false">&#8747;</mo><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">m</mi><mo>=</mo><mrow><mo stretchy="false">&#8747;</mo><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">A</mi><mo>+</mo><mi mathvariant="normal">B</mi><mi mathvariant="normal">r</mi></mrow></mfenced><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi></mrow></mrow><mi mathvariant="normal"></mi></mrow></mrow><mi mathvariant="normal"></mi></math>
<math><mi mathvariant="normal">I</mi><mo>=</mo><mrow><mo stretchy="false">&#8747;</mo><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal"></mi><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></math>
<math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi>a</mi></mrow></munderover><mrow><mfenced separators="|"><mrow><mi>A</mi><mo>+</mo><mi>B</mi><mi>r</mi></mrow></mfenced><mn>2</mn><mi>&#960;</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi></math>
<math><mo>=</mo><mn>2</mn><mi>&#960;</mi><mfenced separators="|"><mrow><mi mathvariant="normal">A</mi><mfrac><mrow><msup><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mi mathvariant="normal">B</mi><mfrac><mrow><msup><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></math>
<math><mo>=</mo><mn>2</mn><mi>&#960;</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>4</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mi>A</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>a</mi><mi>B</mi></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></math>

</details>

---

### Q69. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The radius of gyration of a uniform rod of length <math><mi>l</mi><mo>,</mo><mi></mi></math> about an axis passing through a point <math><mfrac><mrow><mi>l</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math> away from the centre of the rod, and perpendicular to it, is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mi>l</mi></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac><mi>l</mi></math>
- **(C)** <math><msqrt><mfrac><mrow><mn>7</mn></mrow><mrow><mn>48</mn></mrow></mfrac></msqrt><mi>l</mi></math>
- **(D)** <math><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac></msqrt><mi>l</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msqrt><mfrac><mrow><mn>7</mn></mrow><mrow><mn>48</mn></mrow></mfrac></msqrt><mi>l</mi></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/599411A.JPG" style="height: 150px; width: 167px;" />
<math><mfrac><mrow><mi>M</mi><msup><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac><mo>+</mo><mi>M</mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>l</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>M</mi><msup><mrow><mi>K</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
<math><mfrac><mrow><msup><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msup><mi></mi></mrow><mrow><mn>12</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>16</mn></mrow></mfrac><mo>=</mo><msup><mrow><mi>K</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
<math><mi>K</mi><mo>=</mo><msqrt><mfrac><mrow><mn>7</mn></mrow><mrow><mn>48</mn></mrow></mfrac></msqrt><mi>l</mi></math>

</details>

---

### Q70. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A circular disc of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> has a hole of radius <math><mi mathvariant="normal">a</mi></math> at its centre(see figure). If the mass per unit area of the disc varies as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mfrac><msub><mi>&#963;</mi><mn>0</mn></msub><mi>r</mi></mfrac></mfenced></math> then, the radius of gyration of the disc about its axis passing through the center is 
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2e84498d-4cca-42cb-8041-c0c72a8d0ace-image.png" style="width: 300px; height: 312px;" />

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>b</mi></mrow><mn>3</mn></mfrac></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>b</mi></mrow><mn>2</mn></mfrac></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>b</mi></mrow><mn>3</mn></mfrac></msqrt></math>**

**Detailed Solution:**

Solution: (B)
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>m</mi><mo>=</mo><mi>&#963;</mi><mtext>&#8201;&#8201;&#8201;</mtext><mn>2</mn><mi>&#960;</mi><mi>r</mi><mi>d</mi><mi>r</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msub><mi>&#963;</mi><mn>0</mn></msub><mi>r</mi></mfrac><mn>2</mn><mtext>&#8201;</mtext><mi>&#960;</mi><mi>r</mi><mi>d</mi><mi>r</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=2</mo><mi>&#960;</mi><msub><mi>&#963;</mi><mn>0</mn></msub><msubsup><mo stretchy="true">&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>d</mi><mi>r</mi><mo>=</mo><mn>2</mn><mi>&#960;</mi><mi>&#8201;</mi><msub><mi>&#963;</mi><mn>0</mn></msub><mo>(</mo><mi>b</mi><mo>-</mo><mi>a</mi><mo>)</mo></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5fe0c097-b629-4531-b1b8-3a5f39fd8ca3-image.png" style="width: 300px; height: 319px;" />
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>2</mn><mi>&#960;</mi><mtext>&#8201;</mtext><msub><mi>&#963;</mi><mn>0</mn></msub><msubsup><mo stretchy="true">&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><msup><mi>r</mi><mn>2</mn></msup><mi>d</mi><mi>r</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>&#960;</mi><msub><mi>&#963;</mi><mn>0</mn></msub><mfenced separators="|"><mrow><msup><mi>b</mi><mn>3</mn></msup><mo>-</mo><msup><mi>a</mi><mn>3</mn></msup></mrow></mfenced></math>
Radius of gyration <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mfrac><mi>I</mi><mi>m</mi></mfrac><mi>&#160;</mi></msqrt><mo>=</mo><msqrt><mfrac><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>&#960;</mi><mtext>&#8201;</mtext><msub><mi>&#963;</mi><mn>0</mn></msub><mfenced separators="|"><mrow><msup><mi>b</mi><mn>3</mn></msup><mo>-</mo><msup><mi>a</mi><mn>3</mn></msup></mrow></mfenced></mrow><mrow><mn>2</mn><mi>&#960;</mi><mtext>&#8201;</mtext><msub><mi>&#963;</mi><mn>0</mn></msub><mfenced separators="|"><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mfenced></mrow></mfrac></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mfrac><mrow><msup><mi>b</mi><mn>3</mn></msup><mo>-</mo><msup><mi>a</mi><mn>3</mn></msup></mrow><mrow><mn>3</mn><mo>(</mo><mi>b</mi><mo>-</mo><mi>a</mi><mo>)</mo></mrow></mfrac></msqrt><mo>=</mo><msqrt><mfrac><mrow><mo>(</mo><mi>b</mi><mo>-</mo><mi>a</mi><mo>)</mo><mo>(</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>b</mi><mo>)</mo></mrow><mrow><mn>3</mn><mtext>&#8201;&#8201;</mtext><mo>(</mo><mi>b</mi><mo>-</mo><mi>a</mi><mo>)</mo></mrow></mfrac></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mfrac><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>b</mi></mrow><mn>3</mn></mfrac></msqrt></math>.

</details>

---

### Q71. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A solid sphere of mass <math><mi mathvariant="normal">M</mi></math> and radius <math><mi mathvariant="normal">R</mi></math> is divided into two unequal parts. The first part has a mass of <math><mfrac><mrow><mn>7</mn><mi mathvariant="normal">M</mi></mrow><mrow><mn>8</mn></mrow></mfrac></math> and is converted into uniform disc of radius <math><mi>&#160;</mi><mn>2</mn><mi mathvariant="normal">R</mi></math> . The second part is converted into a uniform solid sphere. Let <math><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>1</mn></mrow></msub></math> be the moment of inertia of the disc about its axis and <math><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>2</mn></mrow></msub></math> be the moment of inertia of the new sphere about its axis. The ratio <math><mi>&#160;</mi><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>/</mo><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>2</mn></mrow></msub></math> is given by:

**Options:**

- **(A)** <math><mn>140</mn></math>
- **(B)** <math><mn>185</mn></math>
- **(C)** <math><mn>65</mn></math>
- **(D)** <math><mn>285</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>140</mn></math>**

**Detailed Solution:**

Moment of inertia of disc about the axis passing its centre and perpendicular to its surface, <math><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>7</mn><mi mathvariant="normal">M</mi></mrow><mrow><mn>8</mn></mrow></mfrac></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><mi mathvariant="normal">R</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac></math>.
Radius of small sphere <math><mi mathvariant="normal">r</mi></math> is related as
<math><mfrac><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi mathvariant="normal">&#960;</mi><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mfrac><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mn>8</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi mathvariant="normal">&#960;</mi><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></math>
<math><mi mathvariant="normal">r</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
Moment of inertia of sphere about its axis passing through its centre<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mfenced separators="|"><mfrac><mi mathvariant="normal">M</mi><mn>8</mn></mfrac></mfenced><msup><mfenced separators="|"><mfrac><mi mathvariant="normal">R</mi><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mi mathvariant="normal">M</mi><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup></mrow><mn>80</mn></mfrac></math>
<math><mfrac><mrow><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>80</mn></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mn>140</mn></math>

</details>

---

### Q72. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A thin disc of mass <math><mi mathvariant="normal">M</mi></math> and radius <math><mi mathvariant="normal">R</mi></math> has mass per unit area <math><mi mathvariant="normal">&#963;</mi><mfenced separators="|"><mrow><mi mathvariant="normal">r</mi></mrow></mfenced><mo>=</mo><mi mathvariant="normal">k</mi><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup></math> where <math><mi mathvariant="normal">r</mi></math> is the distance from its centre. Its moment inertia about an axis going through its centre of mass and perpendicular to its plane is:

**Options:**

- **(A)** <math><mfrac><mrow><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>2</mn><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>2</mn><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/12653ae2-88a1-46d5-9472-5189e262b554-image.png" style="width: 318px; height: 313px;" />
<math><mi mathvariant="normal">d</mi><mi mathvariant="normal">m</mi><mo>=</mo><mi mathvariant="normal">&#963;</mi><mo>&#8901;</mo><mi mathvariant="normal">d</mi><mi mathvariant="normal">A</mi><mo>=</mo><mi mathvariant="normal">&#963;</mi><mtext>&#8201;</mtext><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">r</mi><mtext>&#8201;</mtext><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi></math>
<math><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">k</mi><mtext>&#8201;</mtext><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>3</mn></mrow></msup><mtext>&#8201;</mtext><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi></math>
<math><mi mathvariant="normal">M</mi><mo>=</mo><mo>&#8747;</mo><mi mathvariant="normal">d</mi><mi mathvariant="normal">m</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">k</mi><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi mathvariant="normal">R</mi></mrow></munderover><mrow><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>3</mn></mrow></msup><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi></mrow></mrow></math>
<math><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">k</mi><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">k</mi><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><mi mathvariant="normal">d</mi><mi mathvariant="normal">I</mi><mo>=</mo><mi mathvariant="normal">d</mi><mi mathvariant="normal">m</mi><mtext>&#8201;</mtext><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">k</mi><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>5</mn></mrow></msup><mtext>&#8201;</mtext><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">k</mi><munderover><mo stretchy="true">&#8747;</mo><mn>0</mn><mi mathvariant="normal">R</mi></munderover><msup><mi mathvariant="normal">r</mi><mn>5</mn></msup><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">k</mi><mfrac><msup><mi mathvariant="normal">R</mi><mn>6</mn></msup><mn>6</mn></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">k</mi><msup><mi mathvariant="normal">R</mi><mn>6</mn></msup></mrow><mrow><mn>3</mn><mo>&#215;</mo><mn>2</mn></mrow></mfrac></math></p><p>since,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>M</mtext><mo>=</mo><mfrac><msup><mi>&#960;kR</mi><mn>4</mn></msup><mn>2</mn></mfrac></math></p><p>so,
<math><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac></math></p>

</details>

---

### Q73. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A thin circular plate of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> has its density varying as <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext mathvariant="italic">ρ</mtext><mrow><mo>(</mo><mi>r</mi><mo>)</mo></mrow><msub><mtext>=ρ</mtext><mtext>0</mtext></msub><mtext mathvariant="italic">r</mtext></math> with <math><msub><mrow><mi>ρ</mi></mrow><mrow><mn>0</mn></mrow></msub></math> as constant and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> is the distance from its centre. The moment of Inertia of the circular plate about an axis perpendicular to the plate and passing through its edge is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mi>a</mi><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math>. The value of the coefficient <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is:

**Options:**

- **(A)** <math><mi> </mi><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(B)** <math><mi> </mi><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mi> </mi><mfrac><mrow><mn>8</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(D)** <math><mi> </mi><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi> </mi><mfrac><mrow><mn>8</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi mathvariant="normal">d</mi><mi mathvariant="normal">m</mi><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi></mrow></mfenced><mo>&#215;</mo><mi mathvariant="normal">&#961;</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><msub><mrow><mi mathvariant="normal">&#961;</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi></math>
<math><mi mathvariant="normal">M</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><msub><mrow><mi mathvariant="normal">&#961;</mi></mrow><mrow><mn>0</mn></mrow></msub><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi mathvariant="normal">R</mi></mrow></munderover><mrow><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi></mrow></mrow><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi mathvariant="normal">&#960;</mi><msub><mrow><mi mathvariant="normal">&#961;</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>3</mn></mrow></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">I</mi><mi>CM</mi></msub><mo>=</mo><mi mathvariant="normal">&#961;</mi><mfenced separators="|"><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">m</mi></mrow></mfenced><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><msub><mi mathvariant="normal">&#961;</mi><mn>0</mn></msub><mo>&#8747;</mo><msup><mi mathvariant="normal">r</mi><mn>4</mn></msup><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi mathvariant="normal">&#960;</mi><msub><mi mathvariant="normal">&#961;</mi><mn>0</mn></msub><msup><mi mathvariant="normal">R</mi><mn>5</mn></msup></math>
<math><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
<math><mi mathvariant="normal">I</mi><mo>=</mo><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi></mrow></msub><mo>+</mo><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

</details>

---

### Q74. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The moment of inertial of a solid sphere, about an axis parallel to its diameter and at a distance of <math><mi>x</mi></math> from it, is <math><mi>&#8242;</mi><mi>I</mi><msup><mrow><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mi>&#8242;</mi></mrow></msup><mo>.</mo></math> Which one of the graphs represents the variation of <math><mi>I</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> with <math><mi>x</mi></math> correctly?

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c9ba4b3f-5973-46f4-9094-d0348d621151-image.png" style="width: 140px; height: 148px;" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0e8d82a0-187c-4fa6-9983-c078ccccf899-image.png" style="width: 180px; height: 137px;" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4c1991b1-33a3-495f-8d2a-95e02baa34ca-image.png" style="width: 160px; height: 162px;" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/452e94d4-197e-42a4-861e-b6290032ee87-image.png" style="width: 190px; height: 147px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c9ba4b3f-5973-46f4-9094-d0348d621151-image.png" style="width: 140px; height: 148px;" />**

**Detailed Solution:**

<p>we know that by se the parallel axis theorem :-</p><p>Moment of inertia about a point which is parallel of the axis  and at a distance of  X given as </p><p><math><msub><mrow><mi>I</mi></mrow><mrow><mi>x</mi></mrow></msub><mo>=</mo><msub><mrow><mi>I</mi></mrow><mrow><mi>c</mi><mi>m</mi></mrow></msub><mo>+</mo><mi>m</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><msub><mrow><mi>I</mi></mrow><mrow><mi>x</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi>m</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>m</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi></math> Parabola opening upward</p>

</details>

---

### Q75. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the moment of inertia of a hollow cylinder of length <math><mn>30</mn><mi>&#160;</mi><mi>c</mi><mi>m</mi></math> (inner radius <math><mn>10</mn><mi>&#160;</mi><mi>c</mi><mi>m</mi></math> and outer radius <math><mn>20</mn><mi>&#160;</mi><mi>c</mi><mi>m</mi></math> ), about its axis be <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>I</mtext></math> . The radius of a thin cylinder of the same mass such that its moment of inertia about its axis is also <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>I</mtext><mo>,</mo></math> is:

**Options:**

- **(A)** <math><mn>16</mn><mi> </mi><mi>c</mi><mi>m</mi></math>
- **(B)** <math><mn>14</mn><mi> </mi><mi>c</mi><mi>m</mi></math>
- **(C)** <math><mn>12</mn><mi> </mi><mi>c</mi><mi>m</mi></math>
- **(D)** <math><mn>18</mn><mi> </mi><mi>c</mi><mi>m</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>16</mn><mi> </mi><mi>c</mi><mi>m</mi></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/kuzlmisjpcrhbfbaoofnrpuunrrjnxgvjikndneazfcfkpbfat.png" /></p><p>Moment of inertia of a hollow cylinder whose inner radius id r and outer radius is R is given as </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mrow><mi>m</mi><mo>(</mo><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msup><mi>r</mi><mn>2</mn></msup><mo>)</mo></mrow><mn>2</mn></mfrac></math></p><p><math><mfrac><mrow><mi>m</mi><mfenced separators="|"><mrow><msup><mrow><mn>20</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mi>m</mi><msup><mrow><mi>k</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mi>K</mi><mo>=</mo><msqrt><mfrac><mrow><mn>400</mn><mo>+</mo><mn>100</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt><mi>; K</mi><mo>=</mo><msqrt><mn>250</mn></msqrt></math>

<math><mi>K</mi><mo>=</mo><mn>5</mn><msqrt><mn>10</mn></msqrt><mtext>&#8201;</mtext><mi>c</mi><mi>m</mi></math></p></blockquote>

</details>

---

### Q76. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A circular disc $D_{1}$ of mass $M$ and radius $R$ has two identical $\operatorname{discs} D_{2}$ and $D_{3}$ of the same mass $M$ and radius R attached rigidly at its opposite ends (see figure). The moment of inertia of the system about the axis OO', passing through the centre of $D_{1}$, as shown in the figure, will be

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/lHZn1xr5ajTxeMwsl8rb5W4hAB43u72PdeucHOqytz8.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{MR}^{2}$
- **(B)** $3 \mathrm{MR}^{2}$
- **(C)** $\frac{4}{5} \mathrm{MR}^{2}$
- **(D)** $\frac{2}{3} \mathrm{MR}^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3 \mathrm{MR}^{2}$**

**Detailed Solution:**

Moment of inertia of disc $D_{1}$ about $O O^{\prime}=I_{1}=\frac{M R^{2}}{2}$

M.O.I of $\mathrm{D}_{2}$ about $\mathrm{OO}^{\prime}$ $=I_{2}=\frac{1}{2}\left(\frac{M R^{2}}{2}\right)+M R^{2}=\frac{M R^{2}}{4}+M R^{2}$

M.O.I of $\mathrm{D}_{3}$ about $\mathrm{OO}^{\prime}$ $=I_{3}=\frac{1}{2}\left(\frac{M R^{2}}{2}\right)+M R^{2}=\frac{M R^{2}}{4}+M R^{2}$

so, resultant M.O.I about $\mathrm{OO}^{\prime}$ is $\mathrm{I}=\mathrm{I}_{1}+\mathrm{I}_{2}+\mathrm{I}_{3}$

$$

\begin{aligned}

\Rightarrow & I=\frac{M R^{2}}{2}+2\left(\frac{M R^{2}}{4}+M R^{2}\right) \\

&=\frac{M R^{2}}{2}+\frac{M R^{2}}{2}+2 M R^{2}=3 M R^{2}

\end{aligned}

$$

</details>

---

### Q77. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An equilateral triangle $\mathrm{ABC}$ is cut from a thin solid sheet of wood. (See figure) $\mathrm{D}, \mathrm{E}$ and $\mathrm{F}$ are the mid-points of its sides as shown and $\mathrm{G}$ is the centre of the triangle. The moment of inertia of the triangle about an axis passing through $\mathrm{G}$ and perpendicular to the plane of the triangle is $\mathrm{I}_{0}$. If the smaller triangle $\mathrm{DEF}$ is removed from $\mathrm{ABC}$, the moment of inertia of the remaining figure about the same axis is $I$. Then

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/taQVmicDXbKfmmPAv4m_FYEGBG2TYSw56_9Z-NOmYjk.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{I}=\frac{15}{16} \mathrm{I}_{0}$
- **(B)** $\mathrm{I}=\frac{3}{4} \mathrm{I}_{0}$
- **(C)** $\mathrm{I}=\frac{9}{16} \mathrm{I}_{0}$
- **(D)** $\mathrm{I}=\frac{\mathrm{I}_{0}}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{I}=\frac{15}{16} \mathrm{I}_{0}$**

**Detailed Solution:**

Let mass of the larger triangle $=\mathrm{M}$ Side of larger triangle $=\ell$ Moment of inertia of larger triangle $=\mathrm{ma}^{2}$

Mass of smaller triangle $=\frac{\mathrm{M}}{4}$

Length of smaller triangle $=\frac{\ell}{2}$

Moment of inertia of removed triangle $=\frac{\mathrm{M}}{4}\left(\frac{\mathrm{a}}{2}\right)^{2}$

$\therefore \frac{\mathrm{I}_{\text {removed }}}{\mathrm{I}_{\text {original }}}=\frac{\frac{\mathrm{M}}{4}}{\mathrm{M}} \cdot \frac{\left(\frac{\mathrm{a}}{2}\right)^{2}}{(\mathrm{a})^{2}}$

$I_{\text {removed }}=\frac{I_{0}}{16}$

$\mathrm{So}, \mathrm{I}=\mathrm{I}_{0}-\frac{\mathrm{I}_{0}}{16}=\frac{15 \mathrm{I}_{0}}{16}$

</details>

---

### Q78. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Two identical spherical balls of mass <math><mi>M</mi></math> and radius <math><mi>R</mi></math> each are stuck on two ends of a rod of length <math><mn>2</mn><mi>R</mi></math> and mass <math><mi>M</mi></math>(see figure). The moment of inertia of the system about the axis passing perpendicularly through the centre of the rod is</p><p>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/411f611a-a60d-4c7d-b64c-8930670382de-image.png" style="width: 300px; height: 154px;" /></p>

**Options:**

- **(A)** <math><mfrac><mrow><mn>209</mn></mrow><mrow><mn>15</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>.
- **(B)** <math><mfrac><mrow><mn>152</mn></mrow><mrow><mn>15</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>.
- **(C)** <math><mfrac><mrow><mn>137</mn></mrow><mrow><mn>15</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>.
- **(D)** <math><mfrac><mrow><mn>17</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>137</mn></mrow><mrow><mn>15</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>.**

**Detailed Solution:**

<p>Applying parallel axis theorem for the balls,
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi mathvariant="normal">b</mi></msub><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><mi>M</mi><msup><mfenced separators="|"><mrow><mn>2</mn><mi>R</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></math></p><p>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>total</mi></msub><mo>=</mo><mn>2</mn><msub><mi>I</mi><mi mathvariant="normal">b</mi></msub><mo>+</mo><msub><mi>I</mi><mi mathvariant="normal">R</mi></msub></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>total</mi></msub><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><mi>M</mi><msup><mfenced separators="|"><mrow><mn>2</mn><mi>R</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mo>&#215;</mo><mn>2</mn><mo>+</mo><mfrac><mi>M</mi><mn>12</mn></mfrac><msup><mfenced separators="|"><mrow><mn>2</mn><mi>R</mi></mrow></mfenced><mn>2</mn></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>total</mi></msub><mo>=</mo><mfrac><mn>137</mn><mn>15</mn></mfrac><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></math></p>

</details>

---

### Q79. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

A thin circular disk is in the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi></math> plane as shown in the figure. The ratio of its moment of inertia about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>&#39;</mo></math> axes will be:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5b586212-ba6e-4596-9b65-dfe4f2f06fe9-image.png" style="width: 200px; height: 184px;" />

**Options:**

- **(A)** <math><mn>1</mn><mi> </mi><mo>:</mo><mn>4</mn></math>
- **(B)** <math><mn>1</mn><mo>:</mo><mn>5</mn></math>
- **(C)** <math><mn>1</mn><mo>:</mo><mn>3</mn></math>
- **(D)** <math><mn>1</mn><mo>:</mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>1</mn><mo>:</mo><mn>3</mn></math>**

**Detailed Solution:**

<math><msub><mrow><mi>I</mi></mrow><mrow><mi>Z</mi></mrow></msub><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mi>m</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac></math>

(by parallel axis theorem)

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><msub><mi>I</mi><mi>z</mi></msub><mi>&#8242;</mi></msup><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mi>m</mi><msup><mi>R</mi><mn>2</mn></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mi>Z</mi></msub><mrow><msub><mi>I</mi><mi>z</mi></msub><mi>&#8242;</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>

</details>

---

### Q80. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `3`

From a uniform circular disc of radius R and mass 9 M, a small disc of radius <math><mfrac><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math> is removed as shown in the figure. The moment of inertia of the remaining disc about an axis perpendicular to the plane of the disc and passing through centre of disc is:

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/26643_chem.jpg" style="width: 155px; height: 157px;" />

**Options:**

- **(A)** <math><mfrac><mrow><mn>37</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(B)** <math><mn>4</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(C)** <math><mfrac><mrow><mn>40</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(D)** <math><mn>10</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>4</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

By parallel axis theorem,

Mass of smaller disc <math> <mrow> <mo>=</mo><mfrac> <mi>9M</mi> <mrow> <mi>π</mi><msup> <mi>R</mi> <mn>2</mn> </msup> </mrow> </mfrac> <mi>π</mi><msup> <mrow> <mrow><mo>(</mo> <mrow> <mfrac> <mi>R</mi> <mn>3</mn> </mfrac> </mrow> <mo>)</mo></mrow></mrow> <mn>2</mn> </msup> <mo>=</mo><mi>M</mi></mrow> </math>

MI of smaller disc <math><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mi>M</mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn><mi>R</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mi>M</mi><mi>I</mi><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>18</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac></math>

<math><mi>M</mi><mi>I</mi><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><mi>M</mi><mi>I</mi><mo>=</mo><mi>M</mi><mi>I</mi><mfenced separators="|"><mrow><mi>B</mi><mi>i</mi><mi>g</mi><mi>g</mi><mi>e</mi><mi>r</mi></mrow></mfenced><mo>-</mo><mi>M</mi><mi>I</mi><mfenced separators="|"><mrow><mi>S</mi><mi>m</mi><mi>a</mi><mi>l</mi><mi>l</mi><mi>e</mi><mi>r</mi></mrow></mfenced></math>

<math><mo>=</mo><mfrac><mrow><mn>9</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><mo>=</mo><mn>4</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

</details>

---

### Q81. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `2`

<p>Seven identical circular planar disks, each of mass M and radius R are welded symmetrically as shown. The moment of inertia of the arrangement about the axis normal to the plane and passing through the point P is:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/342daea2-3c3e-4e75-9595-9c02e7e18bc4-image.png" style="width: 251px; height: 250px;" /></p>

**Options:**

- **(A)** <math><mfrac><mrow><mn>181</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(B)** <math><mfrac><mrow><mn>19</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi> </mi><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(C)** <math><mfrac><mrow><mn>55</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(D)** <math><mfrac><mrow><mn>73</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>181</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

The motion of inertia of the system about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math>,

<math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>6</mn><mo>&#215;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>6</mn><mo>&#215;</mo><mi>M</mi><mo>&#215;</mo><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><mi>R</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msub><mrow><mi>I</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>24</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

The motion of inertia of the system about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>, 

<math><msub><mrow><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>I</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>7</mn><mi>M</mi><msup><mrow><mi>D</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mfrac><mrow><mn>7</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>24</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>7</mn><mi>M</mi><mo>&#215;</mo><msup><mrow><mfenced separators="|"><mrow><mn>3</mn><mi>R</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mfrac><mrow><mn>181</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

</details>

---

### Q82. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

A circular hole of radius <math><mfrac><mrow><mi>R</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math> is made in a thin uniform disc having mass and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>, as shown in figure. The moment of inertia of the remaining portion of the disc about an axis passing through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> and perpendicular to the plane of the disc is-
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e582585b-b834-446d-b941-d91d8ced306c-image.png" style="width: 200px; height: 212px;" />

**Options:**

- **(A)** <math><mfrac><mrow><mn>219</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>256</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>237</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>512</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>197</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>256</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>19</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>512</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>237</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>512</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><msub><mrow><mi>I</mi></mrow><mrow><mi>D</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac></math>

Moment of inertia of removed portion about the axis.

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mrow><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">v</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">d</mi></mrow></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>&#160;</mi><mi>&#160;</mi><mfenced><mfrac><mi>m</mi><mn>16</mn></mfrac></mfenced><mi>&#160;</mi><mfenced><mrow><mi>&#160;</mi><mfrac><msup><mi>r</mi><mn>2</mn></msup><mn>16</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mfrac><mi>m</mi><mn>16</mn></mfrac></mfenced><mi>&#160;</mi><mi>&#160;</mi><mfenced><mrow><mfrac><mrow><mn>9</mn><msup><mi>r</mi><mn>2</mn></msup></mrow><mn>16</mn></mfrac><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi></mrow></mfenced></math>(by parallel axis theorem)

<math><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>18</mn><mi>m</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>512</mn></mrow></mfrac></math>

<math><mo>=</mo><mfrac><mrow><mn>19</mn><mi>m</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>512</mn></mrow></mfrac></math>

<math><msub><mrow><mi>I</mi></mrow><mrow><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">g</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>19</mn></mrow><mrow><mn>512</mn></mrow></mfrac><mi>&#160;</mi><mi>m</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mo>=</mo><mfrac><mrow><mn>237</mn></mrow><mrow><mn>512</mn></mrow></mfrac><mi>&#160;</mi><mi>m</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

</details>

---

### Q83. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Moment of inertia of an equilateral triangular lamina <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math>, about the axis passing through its centre <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> and perpendicular to its plane is <math><msub><mrow><mi>I</mi></mrow><mrow><mn>0</mn></mrow></msub></math> as shown in the figure. A cavity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mi>E</mi><mi>F</mi></math> is cut out from the lamina, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>,</mo><mo>&#160;</mo><mi>E</mi><mo>,</mo><mo>&#160;</mo><mi>F</mi></math> are the mid points of the sides. Moment of inertia of the remaining part of lamina about the same axis is:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ea7cec15-5066-4905-aba8-42e087619541-image.png" style="width: 200px; height: 204px;" />

**Options:**

- **(A)** <math> <mrow> <mfrac> <mn>7</mn> <mn>8</mn> </mfrac> <msub> <mi>I</mi> <mn>0</mn> </msub> </mrow> </math>
- **(B)** <math> <mrow> <mfrac> <mrow> <mn>15</mn> </mrow> <mrow> <mn>16</mn> </mrow> </mfrac> <msub> <mi>I</mi> <mn>0</mn> </msub> </mrow> </math>
- **(C)** <math> <mrow> <mfrac> <mn>3</mn> <mn>4</mn> </mfrac> <msub> <mi>I</mi> <mn>0</mn> </msub> </mrow> </math>
- **(D)** <math><mfrac><mrow><mn>31</mn><msub><mrow><mi>I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>32</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math> <mrow> <mfrac> <mrow> <mn>15</mn> </mrow> <mrow> <mn>16</mn> </mrow> </mfrac> <msub> <mi>I</mi> <mn>0</mn> </msub> </mrow> </math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mi>B</mi><mi>C</mi><mo>=</mo><mi>A</mi><mi>C</mi><mo>=</mo><mi>l</mi></math>

Moment of inertia of a triangular lamina <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub><mo>=</mo><mi>k</mi><mi>m</mi><msup><mi>l</mi><mn>2</mn></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mi>E</mi><mo>=</mo><mi>E</mi><mi>F</mi><mo>=</mo><mi>D</mi><mi>F</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mfrac><mi>l</mi><mn>2</mn></mfrac></math>

<math><mo>&#8756;</mo></math> Moment of inertia of <math><mo>&#8710;</mo><mi>D</mi><mi>E</mi><mi>F</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mrow><mi>D</mi><mi>E</mi><mi>F</mi></mrow></msub><mo>=</mo><mi>k</mi><mfrac><mi>m</mi><mn>4</mn></mfrac><msup><mfenced separators="|"><mfrac><mi>l</mi><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mrow><mi>D</mi><mi>E</mi><mi>F</mi></mrow></msub><mo>=</mo><mfrac><mi>k</mi><mn>16</mn></mfrac><mi>&#160;</mi><mi>m</mi><msup><mi>l</mi><mn>2</mn></msup></math>.

<math><msub><mrow><mi>I</mi></mrow><mrow><mi>D</mi><mi>E</mi><mi>F</mi></mrow></msub><mo>=</mo><mfrac><mrow><msub><mrow><mi>I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>16</mn></mrow></mfrac></math>

Moment of inertia of the remaining part

<math><msub><mrow><mi>I</mi></mrow><mrow><mi>r</mi><mi>e</mi><mi>m</mi><mi>a</mi><mi>i</mi><mi>n</mi></mrow></msub><mo>=</mo><msub><mrow><mi>I</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>-</mo><mfrac><mrow><msub><mrow><mi>I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>16</mn></mrow></mfrac></math>

<math><mo>=</mo><mfrac><mrow><mn>15</mn><msub><mrow><mi>I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>16</mn></mrow></mfrac></math></p>

</details>

---

### Q84. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `3`

The moment of inertia of a uniform cylinder of length <math><mi>l</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> about its perpendicular bisector is <math><mi>I</mi><mo>.</mo></math> What is the ratio <math><mrow><mrow><mi>l</mi></mrow><mo>/</mo><mrow><mi>R</mi></mrow></mrow></math> such that the moment of inertia is minimum?

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(B)** <math><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>
- **(C)** <math><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mi>&#961;</mi><mfenced separators="|"><mrow><mi>&#960;</mi><msup><mi>R</mi><mn>2</mn></msup><mi>l</mi></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math>

<math><mi>d</mi><mi>m</mi><mo>=</mo><mi>&#961;</mi><mi>&#960;</mi><mfenced separators="|"><mrow><mn>2</mn><mi>R</mi><mo>.</mo><mi>d</mi><mi>R</mi><mi>l</mi><mo>+</mo><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>d</mi><mi>l</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>=</mo><mi>&#961;</mi><mi>&#960;</mi><mfenced separators="|"><mrow><mn>2</mn><mi>R</mi><mi>l</mi><mi>d</mi><mi>R</mi><mo>+</mo><msup><mi>R</mi><mn>2</mn></msup><mi>d</mi><mi>l</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>R</mi><mi>l</mi><mi>&#160;</mi><mi>d</mi><mi>R</mi><mo>=</mo><mo>-</mo><msup><mi>R</mi><mn>2</mn></msup><mi>d</mi><mi>l</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math>

<math><mi>I</mi><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>M</mi><msup><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac></math>

<math><mi>I</mi><mo>=</mo><mfrac><mrow><mi>M</mi></mrow><mrow><mn>12</mn></mrow></mfrac><mi>&#160;</mi><mfenced separators="|"><mrow><mn>3</mn><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>I</mi><mo>=</mo><mfrac><mi>M</mi><mn>12</mn></mfrac><mfenced separators="|"><mrow><mn>6</mn><mi>R</mi><mfenced separators="|"><mrow><mi>d</mi><mi>R</mi></mrow></mfenced><mo>+</mo><mn>2</mn><mi>l</mi><mi>&#160;</mi><mi>d</mi><mi>l</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mo>(</mo><mn>3</mn><mo>)</mo></math>

Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mn>2</mn><mo>)</mo></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mo>)</mo></math>

<math><mn>6</mn><mi>R</mi><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>d</mi><mi>l</mi></mrow><mrow><mn>2</mn><mi>R</mi><mi>l</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mn>2</mn><mi>l</mi><mi>&#160;</mi><mi>d</mi><mi>l</mi><mo>=</mo><mn>0</mn></math>

<math><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><mn>3</mn><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>l</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>l</mi></mrow></mfenced><mi>d</mi><mi>l</mi><mo>=</mo><mn>0</mn></math>

<math><mo>-</mo><mn>3</mn><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><msup><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math>

<math><mn>2</mn><msup><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>3</mn><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mfrac><mrow><mi>l</mi></mrow><mrow><mi>R</mi></mrow></mfrac><mo>=</mo><mi>&#160;</mi><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>

</details>

---

### Q85. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Consider a thin uniform square sheet made of a rigid material. If its side is <math> <mi>a</mi> </math>, mass m and moment of inertia <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> about one of its diagonals, then:

**Options:**

- **(A)** <math><mi>I</mi><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>24</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>m</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>24</mn></mrow></mfrac><mo>&lt;</mo><mi>I</mi><mo>&lt;</mo><mfrac><mrow><mi>m</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac></math>
- **(C)** <math><mi>I</mi><mo>&gt;</mo><mfrac><mrow><mi>m</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac></math>
- **(D)** <math><mi>I</mi><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi>I</mi><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac></math>**

**Detailed Solution:**

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/image18-fba4245f-1915-4ea8-bccc-567854e43f14.jpg" />

In a uniform square plate due to symmetry moment of Inertia about all the axis passing through centre and lying in the plane of the plate is same.

<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msub><mrow><mi>I</mi></mrow><mrow><mi>d</mi><mi>i</mi><mi>a</mi><mi>g</mi><mi>o</mi><mi>n</mi><mi>a</mi><mi>l</mi></mrow></msub></math><math><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac></math>

</details>

---

### Q86. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `2`

From a solid sphere of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>, a cube of the maximum possible volume is cut. Moment of inertia of cube about an axis passing through its centre and perpendicular to one of its faces is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>4</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mi>π</mi></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>32</mn><msqrt><mn>2</mn></msqrt><mi>π</mi></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>16</mn><msqrt><mn>2</mn></msqrt><mi>π</mi></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>4</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>9</mn><msqrt><mn>3</mn></msqrt><mi>π</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>4</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>9</mn><msqrt><mn>3</mn></msqrt><mi>π</mi></mrow></mfrac></math>**

**Detailed Solution:**

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> be the length of edge for the cube, with maximum possible volume diagonal length <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>R</mi></math><math><mo>&#8658;</mo><msqrt><mn>3</mn></msqrt><mi>a</mi><mo>=</mo><mn>2</mn><mi>R</mi><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>R</mi></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>. As densities of sphere and cube are equal. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>'</mo></math> be mass of the cube, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mtext mathvariant="italic">M</mtext><mrow><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msup><mtext mathvariant="italic">R</mtext><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mfrac><msup><mtext mathvariant="italic">M</mtext><mo mathvariant="italic">'</mo></msup><msup><mtext mathvariant="italic">a</mtext><mn>3</mn></msup></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>M</mi><mi>&#8242;</mi></msup><mo>=</mo><mfrac><mrow><mn>3</mn><mi>M</mi><msup><mi>a</mi><mn>3</mn></msup></mrow><mrow><mn>4</mn><mi>&#960;</mi><msup><mi>R</mi><mn>3</mn></msup></mrow></mfrac></math>. Moment of inertia of cube about an axis passing through its center is,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mrow><msup><mi>M</mi><mi>&#8242;</mi></msup><mfenced separators="|"><mrow><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfenced></mrow><mn>12&#160;</mn></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>3</mn><mi>M</mi><msup><mi>a</mi><mn>3</mn></msup></mrow><mrow><mn>4</mn><mi>&#960;</mi><msup><mi>R</mi><mn>3</mn></msup></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup></mrow><mn>12&#160;</mn></mfrac></math><math><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow><mrow><mn>8</mn><mi>&#960;</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></math>.

also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">a</mo><mo>=</mo><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac><mi>R</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>&#160;=</mo><mfrac><mrow><mi>M</mi><mo>&#215;</mo><mn>32</mn><mi>&#160;</mi><msup><mi>R</mi><mn>5</mn></msup></mrow><mrow><mn>8</mn><mi>&#960;</mi><mo>&#215;</mo><mn>9</mn><msqrt><mn>3</mn></msqrt><msup><mi>R</mi><mn>3&#160;</mn></msup></mrow></mfrac></math><math><mo>=</mo><mfrac><mrow><mn>4</mn><mi>M</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>9</mn><msqrt><mn>3</mn></msqrt><mi>&#960;</mi></mrow></mfrac></math>.

</details>

---

### Q87. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

A thin bar of length $\mathrm{L}$ has a mass per unit length $\lambda$, that increases linearly with distance from one end. If its total mass is $M$ and its mass per unit length at the lighter end is $\lambda_{\mathrm{O}}$, then the distance of the centre of mass from the lighter end is:

**Options:**

- **(A)** $\frac{\mathrm{L}}{2}-\frac{\lambda_0 \mathrm{~L}^2}{4 \mathrm{M}}$
- **(B)** $\frac{\mathrm{L}}{3}+\frac{\lambda_0 \mathrm{~L}^2}{8 \mathrm{M}}$
- **(C)** $\frac{\mathrm{L}}{3}+\frac{\lambda_0 \mathrm{~L}^2}{4 \mathrm{M}}$
- **(D)** $\frac{2 \mathrm{~L}}{3}-\frac{\lambda_0 \mathrm{~L}^2}{6 \mathrm{M}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\mathrm{L}}{3}+\frac{\lambda_0 \mathrm{~L}^2}{4 \mathrm{M}}$**

**Detailed Solution:**

No Solution Available

</details>

---

### Q88. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `3`

A circular hole of diameter $\mathrm{R}$ is cut from a disc of mass $M$ and radius $R$; the circumference of the cut passes through the centre of the disc. The moment of inertia of the remaining portion of the disc about an axis perpendicular to the disc and passing through its centre is

**Options:**

- **(A)** $\left(\frac{15}{32}\right) M R^2$
- **(B)** $\left(\frac{1}{8}\right) M R^2$
- **(C)** $\left(\frac{3}{8}\right) M R^2$
- **(D)** $\left(\frac{13}{32}\right) M R^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(\frac{13}{32}\right) M R^2$**

**Detailed Solution:**

M.I. of complete disc about its centre $O$.
$$
I_{\mathrm{Total}}=\frac{1}{2} M R^2
$$

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3DvF_kFHcZnIFTPaB15444tnrg0YV_2EnKCns1TIOaM.original.fullsize.png">



Mass of circular hole (removed)
$$
=\frac{M}{4} \quad\left(\text { As } M=\pi R^2 t \therefore M \propto R^2\right)
$$
M.I. of removed hole about its own axis
$$
=\frac{1}{2}\left(\frac{M}{4}\right)\left(\frac{R}{2}\right)^2=\frac{1}{32} M R^2
$$
M.I. of removed hole about $O^{\prime}$
$$
\begin{aligned}
I_{\text {removed hole }} & =I_{\mathrm{cm}}+m x^2 \\
& =\frac{M R^2}{32}+\frac{M}{4}\left(\frac{R}{2}\right)^2 \\
& =\frac{M R^2}{32}+\frac{M R^2}{16}=\frac{3 M R^2}{32}
\end{aligned}
$$
M.I. of complete disc can also be written as
$I_{\text {Total }}=I_{\text {removed hole }}+I_{\text {remaining disc }}$
$I_{\text {Total }}=\frac{3 M R^2}{32}+I_{\text {remaining disc }}$
From eq. (i) and (ii),
$$
\begin{aligned}
& \frac{1}{2} M R^2=\frac{3 M R^2}{32}+I_{\text {remaining disc }} \\
& \Rightarrow I_{\text {remaining disc }} \\
& \quad=\frac{M R^2}{2}-\frac{3 M R^2}{32}=\left(\frac{13}{32}\right) M R^2
\end{aligned}
$$

</details>

---

### Q89. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `2`

Consider a uniform square plate of side ' $a$ ' and mass ' $m$ '. The moment of inertia of this plate about an axis perpendicular to its plane and passing through one of its corners is

**Options:**

- **(A)** $\frac{5}{6} m a^2$
- **(B)** $\frac{1}{12} m a^2$
- **(C)** $\frac{7}{12} m a^2$
- **(D)** $\frac{2}{3} m a^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2}{3} m a^2$**

**Detailed Solution:**

$$
I=I_{c m}+m\left(\frac{a \sqrt{2}}{2}\right)^2=\frac{m a^2}{6}+\frac{m a^2}{2}=\frac{2}{3} m a^2
$$

</details>

---

### Q90. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `1`

For the given uniform square lamina $\mathrm{A B C D}$, whose centre is $\mathrm{O}$,
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/n7T5UMoT6AqWvHA_O5xdF8C8MfbgxFbda1HrAz6F5l0.original.fullsize.png">

**Options:**

- **(A)** $\sqrt{2 \mathrm{I}}_{\mathrm{AC}}=\mathrm{I}_{\mathrm{EF}}$
- **(B)** $\mathrm{I}_{\mathrm{AD}}=3\mathrm{I}_{\mathrm{EF}}$
- **(C)** $\mathrm{I}_{\mathrm{AC}}=\mathrm{I}_{\mathrm{EF}}$
- **(D)** $\mathrm{I_{A C}}=\sqrt{2} \mathrm{I_{E F}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{I}_{\mathrm{AC}}=\mathrm{I}_{\mathrm{EF}}$**

**Detailed Solution:**

$\mathrm{I}_{\mathrm{AC}}=\mathrm{I}_{\mathrm{EF}}$ (from $\perp^{\text {rd }}$ axis theorem)

</details>

---

### Q91. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `3`

Four point masses, each of value $\mathrm{m}$, are placed at the corners of a square $A B C D$ of side $\ell$. The moment of inertia through $A$ and parallel to $B D$ is

**Options:**

- **(A)** $\mathrm{m} \ell^2$
- **(B)** $2 \mathrm{~m} \ell^2$
- **(C)** $3 m \ell^2$
- **(D)** $3 \mathrm{~m} \ell^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3 \mathrm{~m} \ell^2$**

**Detailed Solution:**

$\mathrm{I}=2 \mathrm{~m}(\ell / \sqrt{2})^2=3 \mathrm{~m} \ell^2$

</details>

---

### Q92. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

The moment of inertia of a uniform semicircular disc of mass $M$ and radius $r$ about a line perpendicular to the plane of the disc through the centre is

**Options:**

- **(A)** $\frac{1}{4} \mathrm{Mr}^2$
- **(B)** $\frac{2}{5} \mathrm{Mr}^2$
- **(C)** $\mathrm{Mr}^2$
- **(D)** $\frac{1}{2} \mathrm{Mr}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{2} \mathrm{Mr}^2$**

**Detailed Solution:**

$2 \mathrm{I}=2 \mathrm{M} \frac{\mathrm{R}^2}{2}$
$\therefore \mathrm{I}=\frac{\mathrm{MR}^2}{2}$

</details>

---

### Q93. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

One solid sphere A and another hollow sphere B are of same mass and same outer radii. Their moment of inertia about their diameters are respectively $\mathrm{I}_{\mathrm{A}}$ and $\mathrm{I}_{\mathrm{B}}$ such that

**Options:**

- **(A)** $I_A=I_B$
- **(B)** $I_A>I_B$
- **(C)** $I_A < I_B$
- **(D)** yes, $45^{\circ}$
$I_A / I_B=d_A / d_B$
Where $d_A$ and $d_B$ are their densities.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $I_A < I_B$**

**Detailed Solution:**

Moment of inertia of a uniform density solid sphere, $A=\frac{2}{5} M R^2$
Since $M$ and $R$ are same, $I_A < I_B$.

</details>

---

### Q94. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `3`

A circular disc $X$ of radius $R$ is made from an iron plate of thickness $t$, and another disc $Y$ of radius $4 \mathrm{R}$ is made from an iron plate of thickness $\frac{\mathrm{t}}{4}$. Then the relation between the moment of inertia $\mathrm{I}_{\mathrm{X}}$ and $\mathrm{I}_{\mathrm{Y}}$ is

**Options:**

- **(A)** $\mathrm{I}_{\mathrm{Y}}=32 \mathrm{I}_{\mathrm{x}}$
- **(B)** $\mathrm{I}_{\mathrm{Y}}=16 \mathrm{I}_{\mathrm{x}}$
- **(C)** $\mathrm{I}_{\mathrm{Y}}=\mathrm{I}_{\mathrm{X}}$
- **(D)** $\mathrm{I}_{\mathrm{Y}}=64 \mathrm{I}_{\mathrm{X}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{I}_{\mathrm{Y}}=64 \mathrm{I}_{\mathrm{X}}$**

**Detailed Solution:**

$$
\mathrm{I}=\frac{1}{2} \mathrm{mR} \quad \text { or } \quad \mathrm{M} \propto \mathrm{t} \propto \mathrm{R}^2
$$
For $\operatorname{disc} X, I_x=\frac{1}{2}(m)(R)^2=\frac{1}{2}\left(\pi r^2 t\right) .(R)^2$
For disc $Y, I_y=\frac{1}{2}\left[\pi(4 R)^2 \cdot t / 4\right][4 R]^2$
$$
\Rightarrow \frac{I_x}{I_y}=\frac{1}{(4)^3} \Rightarrow I_y=64 I_x
$$

</details>

---

### Q95. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

Moment of inertia of a circular wire of mass M and radius R about its diameter is

**Options:**

- **(A)** $\mathrm{MR}^2 / 2$
- **(B)** $\mathrm{MR}^2$
- **(C)** $2 \mathrm{MR}^2$
- **(D)** $\mathrm{MR}^2 / 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{MR}^2$**

**Detailed Solution:**

No Solution Available

</details>

---

