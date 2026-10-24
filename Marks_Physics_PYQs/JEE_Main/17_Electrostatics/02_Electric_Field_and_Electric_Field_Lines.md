# JEE Main Physics - Electrostatics

## Topic 2: Electric Field and Electric Field Lines

**Total Questions:** 95

---

### Q1. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A thin half ring of radius $35$ cm is uniformly charged with a total charge of $Q$ coulomb. If the magnitude of the electric field at centre of the half ring is $100$ V/m, then the value of $Q$ is _______ nC. ($\epsilon_o = 8.85 \times 10^{-12}$ C$^2$/Nm$^2$ and $\pi = 3.14$)

**Options:**

- **(A)** $2.14$
- **(B)** $2.44$
- **(C)** $3.25$
- **(D)** $0.7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2.14$**

**Detailed Solution:**

The electric field at the center of a uniformly charged half ring is given by:

$E = \dfrac{2k\lambda}{R}$

where $\lambda = \dfrac{Q}{\pi R}$ is the linear charge density.

Substituting $\lambda$, we get:

$E = \dfrac{2kQ}{\pi R^2} = \dfrac{2Q}{4\pi\epsilon_0 \pi R^2} = \dfrac{Q}{2\pi^2\epsilon_0 R^2}$

Rearranging for $Q$:

$Q = 2\pi^2\epsilon_0 R^2 E$

Given values:
$E = 100$ V/m
$R = 35$ cm $= 0.35$ m
$\epsilon_0 = 8.85 \times 10^{-12}$ C$^2$/Nm$^2$
$\pi = 3.14$

Substituting the values:

$Q = 2 \times (3.14)^2 \times 8.85 \times 10^{-12} \times (0.35)^2 \times 100$

$Q = 2 \times 9.8596 \times 8.85 \times 10^{-12} \times 0.1225 \times 100$

$Q \approx 2137.8 \times 10^{-12}$ C

$Q \approx 2.14 \times 10^{-9}$ C $= 2.14$ nC

Answer: $2.14$

</details>

---

### Q2. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A particle of charge $q$ and mass $m$ is projected from origin with an initial velocity $\vec{v} = \left(\dfrac{v_0}{\sqrt{2}}\hat{x} + \dfrac{v_0}{\sqrt{2}}\hat{y}\right)$. There exists a uniform magnetic field $\vec{B} = B_0 \hat{z}$ and a space varying electric field $\vec{E} = E_0 e^{-\lambda x}\hat{x}$ within the region $0 \leq x \leq L$. After travelling a distance such that $x$-coordinate has changed from $x=0$ to $x=L$, the change in the kinetic energy is _______.

**Options:**

- **(A)** $\dfrac{qE_0}{\lambda}[1 - e^{-\lambda L}]$
- **(B)** $\left(\dfrac{v_0 q B_0}{2\lambda}\right)[2 - e^{-2\lambda L}]$
- **(C)** $\dfrac{qE_0}{\lambda}[1 + e^{-\lambda L}]$
- **(D)** $q\left(\dfrac{E_0 + v_0 B_0}{\lambda}\right)[1 - e^{-\lambda L/2}]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{qE_0}{\lambda}[1 - e^{-\lambda L}]$**

**Detailed Solution:**

According to the work-energy theorem, the change in kinetic energy of a particle is equal to the total work done by all the forces acting on it.

The forces acting on the particle are the electric force and the magnetic force. The magnetic force is given by $\vec{F}_B = q(\vec{v} \times \vec{B})$. Since the magnetic force is always perpendicular to the velocity vector of the particle, the work done by the magnetic field is zero.

The change in kinetic energy is equal to the work done by the electric field alone. The electric force is $\vec{F}_E = q\vec{E} = qE_0 e^{-\lambda x}\hat{x}$.

The work done by the electric field as the particle moves from $x = 0$ to $x = L$ is given by

$W_E = \int_{0}^{L} \vec{F}_E \cdot d\vec{r} = \int_{0}^{L} qE_0 e^{-\lambda x} dx$

Evaluating the integral, we get

$W_E = qE_0 \left[ \dfrac{e^{-\lambda x}}{-\lambda} \right]_{0}^{L}$

$W_E = -\dfrac{qE_0}{\lambda} (e^{-\lambda L} - e^{0})$

$W_E = \dfrac{qE_0}{\lambda} [1 - e^{-\lambda L}]$

Thus, the change in kinetic energy is $\dfrac{qE_0}{\lambda} [1 - e^{-\lambda L}]$.

Answer: $\dfrac{qE_0}{\lambda}[1 - e^{-\lambda L}]$

</details>

---

### Q3. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R

Assertion A: In electrostatics, a conductor does not store any net charge inside.

Reason R: Inside the capacitor (with no dielectric medium), the free charge carriers, if placed between the plates of capacitor, experience force and drift.

Choose the correct answer from the options given below

**Options:**

- **(A)** Both A and R are true and R is the correct explanation of A
- **(B)** Both A and R are true but R is NOT the correct explanation of A
- **(C)** A is true but R is false
- **(D)** A is false but R is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Both A and R are true but R is NOT the correct explanation of A**

**Detailed Solution:**

In electrostatics, the electric field inside a conductor is zero. According to Gauss's law, $\oint \vec{E} \cdot d\vec{s} = \dfrac{q_{in}}{\epsilon_0}$. Since $\vec{E} = 0$ everywhere inside the conductor, the net charge enclosed $q_{in}$ must be zero. Thus, a conductor does not store any net charge inside its bulk, and any excess charge resides only on its surface. Assertion A is true.

Inside a capacitor with no dielectric medium, a uniform electric field exists between the plates. If free charge carriers are placed in this region, they will experience an electrostatic force $\vec{F} = q\vec{E}$ and will drift towards the respective oppositely charged plates. Reason R is true.

Although both statements are factually correct, the behavior of charge carriers in the electric field of a capacitor does not explain why the net charge inside a conductor is zero in electrostatics. Therefore, both A and R are true but R is NOT the correct explanation of A.

Answer: Both A and R are true but R is NOT the correct explanation of A

</details>

---

### Q4. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two metal plates $(A, B)$ are kept horizontally with separation of $\left(\dfrac{12}{\pi}\right)$ cm, with plate A on the top. An atomizer jet sprays oil (density $1.5$ g/cm$^3$) droplets of radius $1$ mm horizontally. All oil droplets carry a charge $5$ nC. The potentials $V_A$ and $V_B$ are required on plates A and B respectively in order to ensure the droplets do not descend. The values of $V_A$ and $V_B$ are _______.
(Neglect the air resistance to the droplets and take $g = 10$ m/s$^2$)

**Options:**

- **(A)** $100 \, V$ and $580 \, V$
- **(B)** $580 \, V$ and $100 \, V$
- **(C)** $60 \, V$ and $400 \, V$
- **(D)** $0 \, V$ and $-200 \, V$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $100 \, V$ and $580 \, V$**

**Detailed Solution:**

For the oil droplets to not descend, the upward electric force must balance the downward gravitational force.

$qE = mg$

The mass of the oil droplet is given by:

$m = \dfrac{4}{3} \pi r^3 \rho$

Substituting the given values $r = 10^{-3}$ m and $\rho = 1500$ kg/m$^3$:

$m = \dfrac{4}{3} \pi (10^{-3})^3 \times 1500 = 2 \pi \times 10^{-6}$ kg

The electric field $E$ required is:

$E = \dfrac{mg}{q} = \dfrac{2 \pi \times 10^{-6} \times 10}{5 \times 10^{-9}} = 4000 \pi$ V/m

The potential difference $\Delta V$ between the plates is:

$\Delta V = E \times d = 4000 \pi \times \left(\dfrac{12}{\pi} \times 10^{-2}\right) = 480$ V

Since the charge on the droplet is positive, the electric field must be directed upwards to provide an upward force. Electric field lines point from higher potential to lower potential, so the bottom plate B must be at a higher potential than the top plate A.

$V_B - V_A = 480$ V

Checking the given options, $V_A = 100$ V and $V_B = 580$ V satisfies this condition.

Answer: $100 \, V$ and $580 \, V$

</details>

---

### Q5. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Identify the correct statements : 
 A. Electrostatic field lines form closed loops. 
 B. The electric field lines point radially outward when charge is greater than zero. 
 C. The Gauss - Law is valid only for inverse - square force. 
 D. The workdone in moving a charged particle in a static electric field around a closed path is zero. 
 E. The motion of a particle under Coulomb's force must take place in a plane. 
 Choose the correct answer from the options given below :

**Options:**

- **(A)** A, B, D, E Only
- **(B)** A, C, E Only
- **(C)** A, B, C, D Only
- **(D)** B, C, D, E Only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) B, C, D, E Only**

**Detailed Solution:**

Statement A: Electrostatic field lines originate from positive charges and terminate on negative charges. They do not form closed loops because the electrostatic field is conservative. Thus, A is incorrect.
Statement B: For a positive point charge ($q > 0$), the electric field lines are directed radially outwards. Thus, B is correct.
Statement C: Gauss's Law is a consequence of the inverse-square nature of Coulomb's law ($F \propto 1/r^2$). If the force law were different, Gauss's Law would not hold in its standard form. Thus, C is correct.
Statement D: The electrostatic field is conservative, meaning the work done in moving a charge along any closed path is zero ($\oint \vec{E} \cdot d\vec{l} = 0$). Thus, D is correct.
Statement E: Coulomb's force is a central force. The motion of a particle under a central force always takes place in a plane because the torque about the center is zero, keeping angular momentum constant in direction. Thus, E is correct.
Since B, C, D, and E are correct, the correct option is (4).

</details>

---

### Q6. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A simple pendulum has a bob with mass $m$ and charge $q$. The pendulum string has negligible mass. When a uniform and horizontal electric field $\vec{E}$ is applied, the tension in the string changes. The final tension in the string, when pendulum attains an equilibrium position is $\_\_\_\_$. (g: acceleration due to gravity)

**Options:**

- **(A)** $\sqrt{m^{2} g^{2}+q^{2} E^{2}}$
- **(B)** $m \mathrm{~g}+q E$
- **(C)** $m g-q E$
- **(D)** $\sqrt{m^{2} g^{2}-q^{2} E^{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{m^{2} g^{2}+q^{2} E^{2}}$**

**Detailed Solution:**

The charged bob experiences two forces at equilibrium:
Gravitational force: $F_g = mg$ (downward)
Electric force: $F_E = qE$ (horizontal, in direction of field)
These forces are perpendicular to each other. The string tension must balance their resultant.
At equilibrium, the string makes angle $\theta$ with vertical such that:
Vertical: $T\cos\theta = mg$
Horizontal: $T\sin\theta = qE$
The net force from gravity and electric field is $\sqrt{(mg)^2 + (qE)^2}$
Therefore, the tension in the string is: $T = \sqrt{m^2g^2 + q^2E^2}$

</details>

---

### Q7. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Six point charges are kept $60^{\circ}$ apart from each other on the circumference of a circle of radius $R$ as shown in figure. The net electric field at the center of the circle is $\_\_\_\_$. ($\epsilon_{0}$ is permittivity of free space)
<img style="width:200px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/22S1_q_39_1.png">

**Options:**

- **(A)** $\frac{Q}{4 \pi \in_{\mathrm{o}} R^{2}}(\sqrt{3} \hat{i}-\hat{j})$
- **(B)** $-\frac{5 Q}{8 \pi \epsilon_{\mathrm{o}} R^{2}}(\hat{i}+\sqrt{3} \hat{j})$
- **(C)** $-\left(\frac{5 Q}{8 \pi \epsilon_{\mathrm{o}} R^{2}}\right)(\hat{i}-3 \hat{j})$
- **(D)** $-\frac{\mathrm{Q}}{4 \pi \epsilon_{\mathrm{o}} R^{2}}(\sqrt{3} \hat{i}-\hat{j})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\frac{\mathrm{Q}}{4 \pi \epsilon_{\mathrm{o}} R^{2}}(\sqrt{3} \hat{i}-\hat{j})$**

**Detailed Solution:**

Six point charges equally spaced 60° apart on a circle of radius R, with alternating arrangement creating a dipole-like configuration.
Each charge creates an electric field at the center of magnitude $E_0 = \frac{Q}{4\pi\varepsilon_0R^2}$ pointing radially (outward for +Q, inward for -Q).
By vector addition of field contributions from all six charges with proper angle consideration:
The charges at specific positions create a net field with components that depend on their arrangement.
For the given symmetric configuration, the net electric field is: $\vec{E} = \frac{Q}{4\pi\varepsilon_0R^2}(\sqrt{3}\hat{i} - \hat{j})$
This corresponds to magnitude $2E_0$ at angle of $-30°$ from the positive x-axis.

</details>

---

### Q8. JEE Main 2025 (8 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

An electron is released from rest near an infinite non-conducting sheet of uniform charge density ' $-\sigma$ '. The rate of change of de-Broglie wave length associated with the electron varies inversely as $\mathrm{n}^{\text {th }}$ power of time. The numerical value of $n$ is ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

Let the momentum of $\mathrm{e}^{-}$at any time t is p and its de-broglie wavelength is $\lambda$.
Then, $\mathrm{p}=\frac{\mathrm{h}}{\lambda}$
$\begin{aligned}
& \frac{\mathrm{dp}}{\mathrm{dt}}=\frac{-\mathrm{h}}{\lambda^2} \frac{\mathrm{~d} \lambda}{\mathrm{dt}} \\
& \mathrm{ma}=\mathrm{F}=-\frac{\mathrm{h}}{\lambda} \frac{\mathrm{~d} \lambda}{\mathrm{dt}} \quad[\mathrm{~m}=\text { mass of } \mathrm{e}]
\end{aligned}$
Where, -ve sign represents decrease in $\lambda$ with time
$\mathrm{ma}=\frac{-\mathrm{h}}{(\mathrm{~h} / \mathrm{p})^2} \frac{\mathrm{~d} \lambda}{\mathrm{dt}}$
$\begin{aligned}
& \mathrm{a}=-\frac{\mathrm{p}^2}{\mathrm{mh}} \frac{\mathrm{~d} \lambda}{\mathrm{dt}} \\
& \mathrm{a}=-\frac{\mathrm{mv}^2}{\mathrm{~h}} \frac{\mathrm{~d} \lambda}{\mathrm{dt}} \\
& \frac{\mathrm{~d} \lambda}{\mathrm{dt}}=-\frac{\mathrm{ah}}{\mathrm{mv}^2}...(1)
\end{aligned}$
here, $\mathrm{a}=\frac{\mathrm{qE}}{\mathrm{m}}=\frac{\mathrm{e}}{\mathrm{m}} \frac{\sigma}{2 \varepsilon_0}$
$\mathrm{a}=\frac{\sigma \mathrm{e}}{2 \mathrm{~m} \varepsilon_0}$
and $\mathrm{v}=\mathrm{u}+\mathrm{at}$
$\mathrm{v}=\mathrm{at}$
Substituting values of a \& v in equation (1)
$\begin{aligned}
& \frac{\mathrm{d} \lambda}{\mathrm{dt}}=-\frac{2 \mathrm{~h} \varepsilon_0}{\sigma \mathrm{et}^2} \\
& \Rightarrow \frac{\mathrm{~d} \lambda}{\mathrm{dt}} \propto \frac{1}{\mathrm{t}^2} \\
& \Rightarrow \mathrm{n}=2
\end{aligned}$

</details>

---

### Q9. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Electric charge is transferred to an irregular metallic disk as shown in figure. If $\sigma_1, \sigma_2, \sigma_3$ and $\sigma_4$ are charge densities at given points then, choose the correct answer from the options given below:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/SUTgd9uFYrZn45gCVkOW56xbyi4qaZUhBRioGjQ_Ibs.original.fullsize.png"/>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/NkGNbtlJlTF4q2huDGpQger1hoOuk6h10jcEaQsHwXg.original.fullsize.png"/>

**Options:**

- **(A)** A, B and C Only
- **(B)** A and C Only
- **(C)** D and E Only
- **(D)** B and C Only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) A, B and C Only**

**Detailed Solution:**

$\begin{aligned} & \sigma \propto \frac{1}{\mathrm{ROC}} \\ & (\mathrm{ROC})_1 \lt (\mathrm{ROC})_3 \lt (\mathrm{ROC})_2=(\mathrm{ROC})_4 \\ & \sigma_1 \gt \sigma_3 \gt \sigma_2=\sigma_4\end{aligned}$

</details>

---

### Q10. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R).
Assertion (A) : The outer body of an air craft is made of metal which protects persons sitting inside from lightning-strikes.
Reason (R) : The electric field inside the cavity enclosed by a conductor is zero.
In the light of the above statements, chose the most appropriate answer from the options given below :

**Options:**

- **(A)** Both $(\mathrm{A})$ and $(\mathrm{R})$ are correct and $(\mathrm{R})$ is the correct explanation of $(\mathrm{A})$
- **(B)** $(\mathrm{A})$ is correct but $(\mathrm{R})$ is not correct
- **(C)** Both $(\mathrm{A})$ and $(\mathrm{R})$ are correct but $(\mathrm{R})$ is not correct explanation of (A)
- **(D)** (A) is not correct but $(\mathrm{R})$ is correct

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Both $(\mathrm{A})$ and $(\mathrm{R})$ are correct and $(\mathrm{R})$ is the correct explanation of $(\mathrm{A})$**

**Detailed Solution:**

Electric field of outside charge is zero inside conductor

</details>

---

### Q11. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two infinite identical charged sheets and a charged spherical body of charge density ' $\rho$ ' are arranged as shown in figure. Then the correct relation between the electrical fields at $\mathrm{A}, \mathrm{B}, \mathrm{C}$ and D points is :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/th3tMibD7SygKJEeyKd0o0zdVVqoi6_-MlaPcgYVE2I.original.fullsize.png"/>

**Options:**

- **(A)** $\overrightarrow{\mathrm{E}}_{\mathrm{A}}=\overrightarrow{\mathrm{E}}_{\mathrm{B}} ; \overrightarrow{\mathrm{E}}_{\mathrm{C}}=\overrightarrow{\mathrm{E}}_{\mathrm{D}}$
- **(B)** $\overrightarrow{\mathrm{E}}_{\mathrm{A}} \gt \overrightarrow{\mathrm{E}}_{\mathrm{B}} ; \overrightarrow{\mathrm{E}}_{\mathrm{C}}=\overrightarrow{\mathrm{E}}_{\mathrm{D}}$
- **(C)** $\overrightarrow{\mathrm{E}}_{\mathrm{C}} \neq \overrightarrow{\mathrm{E}}_{\mathrm{D}} ; \overrightarrow{\mathrm{E}}_{\mathrm{A}} \gt \overrightarrow{\mathrm{E}}_{\mathrm{B}}$
- **(D)** $\left|\overrightarrow{\mathrm{E}}_{\mathrm{A}}\right|=\left|\overrightarrow{\mathrm{E}}_{\mathrm{B}}\right| ; \overrightarrow{\mathrm{E}}_{\mathrm{C}} \gt \overrightarrow{\mathrm{E}}_{\mathrm{D}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\overrightarrow{\mathrm{E}}_{\mathrm{C}} \neq \overrightarrow{\mathrm{E}}_{\mathrm{D}} ; \overrightarrow{\mathrm{E}}_{\mathrm{A}} \gt \overrightarrow{\mathrm{E}}_{\mathrm{B}}$**

**Detailed Solution:**

Conceptual
$\begin{aligned}
& \mathrm{E}_{\mathrm{C}} \neq \mathrm{E}_{\mathrm{D}} \\
& \mathrm{E}_{\mathrm{A}} \gt \mathrm{E}_{\mathrm{B}}
\end{aligned}$

</details>

---

### Q12. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Consider two infinitely large plane parallel conducting plates as shown below. The plates are uniformly charged with a surface charge density $+\sigma$ and $-2 \sigma$. The force experienced by a point charge +q placed at the mid point between two plates will be :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/r4HXuiQoEYbEiIoXflUtL4nAelUcF41I1zkt5DRk9vg.original.fullsize.png"/>

**Options:**

- **(A)** $\frac{\sigma q}{4 \epsilon_0}$
- **(B)** $\frac{3 \sigma q}{2 \epsilon_0}$
- **(C)** $\frac{3 \sigma q}{4 \in_0}$
- **(D)** $\frac{\sigma q}{2 \epsilon_0}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3 \sigma q}{2 \epsilon_0}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Xe5lGE2sfm4KMRzOyWqRX82f_4YhryTlUICGkhlX8lE.original.fullsize.png"/>
Final charge distribution will be<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/uxNoLr1bjEgGA5MdAI_94fZsQ09EoJy7DbUw2i3R1M8.original.fullsize.png"/>
$\therefore \mathrm{F}_{\mathrm{net}}=\frac{3 \sigma}{2 \epsilon_0} \mathrm{q}$

</details>

---

### Q13. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A point charge +q is placed at the origin. A second point charge +9 q is placed at $(\mathrm{d}, 0,0)$ in Cartesian coordinate system. The point in between them where the electric field vanishes is :

**Options:**

- **(A)** $(4 \mathrm{~d} / 3,0,0)$
- **(B)** $(\mathrm{d} / 4,0,0)$
- **(C)** $(3 \mathrm{~d} / 4,0,0)$
- **(D)** $(\mathrm{d} / 3,0,0)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(\mathrm{d} / 4,0,0)$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EUmMu4RcgtNDEvOJCCTkUJrjF12MIvk59VVWSudZl2Y.original.fullsize.png"/>
Let $\mathrm{E}_{\mathrm{p}}=0$
$\begin{aligned}
& \therefore \frac{\mathrm{kq}}{\mathrm{x}^2}=\frac{\mathrm{k} 9 \mathrm{q}}{(\mathrm{~d}-\mathrm{x})^2} \\
& \Rightarrow \frac{\mathrm{~d}-\mathrm{x}}{\mathrm{x}}=3 \Rightarrow \mathrm{x}=\frac{\mathrm{d}}{4}
\end{aligned}$
$\therefore$ co-ordinate of P is $\left(\frac{\mathrm{d}}{4}, 0,0\right)$

</details>

---

### Q14. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A particle of mass ' $m$ ' and charge ' $q$ ' is fastened to one end ' $A$ ' of a massless string having equilibrium length $l$, whose other end is fixed at point ' $O$ '. The whole system is placed on a frictionless horizontal plane and is initially at rest. If uniform electric field is switched on along the direction as shown in figure, then the speed of the particle when it crosses the x -axis is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ZR8qEsrMUL9S07SehjtHYKmJYkz-Pg6VZZnqzETklkg.original.fullsize.png"/>

**Options:**

- **(A)** $\sqrt{\frac{\mathrm{qE} l}{2 \mathrm{~m}}}$
- **(B)** $\sqrt{\frac{\mathrm{qE} l}{\mathrm{~m}}}$
- **(C)** $\sqrt{\frac{\mathrm{qE} l}{4 \mathrm{~m}}}$
- **(D)** $\sqrt{\frac{2 q \mathrm{El}}{\mathrm{m}}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{\frac{\mathrm{qE} l}{\mathrm{~m}}}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/t7AFhNtyDqieioM_ENobZ1J-UI6MhzlcVOzrsxAQO-w.original.fullsize.png">




$\begin{aligned} & \mathrm{W}_{\mathrm{all}}=\Delta \mathrm{k} \\ & \mathrm{W}_{\mathrm{e}}=\mathrm{k}_{\mathrm{f}}-\mathrm{k}_{\mathrm{i}} \\ & \mathrm{qE} \frac{\ell}{2}=\frac{1}{2} \mathrm{mv}^2-0 \\ & \mathrm{v}=\sqrt{\frac{\mathrm{qE} \ell}{\mathrm{m}}}\end{aligned}$

</details>

---

### Q15. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An electron is made to enter symmetrically between two parallel and equally but oppositely charged metal plates, each of 10 cm length. The electron emerges out of the electric field region with a horizontal component of velocity $10^6 \mathrm{~m} / \mathrm{s}$. If the magnitude of the electric field between the plates is $9.1 \mathrm{~V} / \mathrm{cm}$, then the vertical component of velocity of electron is (mass of electron $=9.1 \times 10^{-31} \mathrm{~kg}$ and charge of electron $=1.6 \times 10^{-19} \mathrm{C}$ )

**Options:**

- **(A)** 0
- **(B)** $1 \times 10^6 \mathrm{~m} / \mathrm{s}$
- **(C)** $16 \times 10^6 \mathrm{~m} / \mathrm{s}$
- **(D)** $16 \times 10^4 \mathrm{~m} / \mathrm{s}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $16 \times 10^6 \mathrm{~m} / \mathrm{s}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ymJIzglRlGT1P1KG4Q71HNm2zxYmgZGc78UcDd1ZVBA.original.fullsize.png">



$\begin{aligned} & \Rightarrow \mathrm{t}=\frac{\ell}{\mathrm{V}_{\mathrm{x}}}=\frac{10 \times 10^{-2}}{10^6}=10^{-7} \\ & \Rightarrow \mathrm{~V}_{\mathrm{y}}=\mathrm{u}_{\mathrm{y}}+\mathrm{a}_{\mathrm{y}} \mathrm{t} \\ & \Rightarrow \mathrm{V}_{\mathrm{y}}=0+\frac{\mathrm{eE}}{\mathrm{m}} \times 10^{-7} \\ & \Rightarrow \mathrm{~V}_{\mathrm{y}}=\frac{1.6 \times 10^{-19}}{9.1 \times 10^{-31}} \times 9.1 \times 10^{-2} \times 10^{-7} \\ & \Rightarrow \mathrm{~V}_{\mathrm{y}}=16 \times 10^6\end{aligned}$

</details>

---

### Q16. JEE Main 2024 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

If the net electric field at point $\mathrm{P}$ along $\mathrm{Y}$ axis is zero, then the ratio of $\left|\frac{q_2}{q_3}\right|$ is $\frac{8}{5 \sqrt{x}}$, where $x=$ _____.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/TENXZqdWoZtzBsZzXo4X7z8-7UakOtjMlAyt617tVwQ.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/aLlQa_YLaVSo3Xz7UQdUsGIhidpMEPpGpv5LT2yOWas.original.fullsize.png">
$\begin{aligned} & \frac{\mathrm{Kq}_2}{20} \cos \beta=\frac{\mathrm{Kq}_3}{25} \cos \theta \\ & \frac{\mathrm{Kq}_2}{20} \frac{4}{\sqrt{20}}=\frac{\mathrm{Kq}_3}{25} \frac{4}{\sqrt{25}} \\ & \frac{\mathrm{q}_2}{\mathrm{q}_3}=\frac{20}{25} \sqrt{\frac{20}{25}}=\frac{8}{5 \sqrt{\mathrm{x}}} \\ & \Rightarrow \sqrt{\mathrm{x}}=\frac{8 \times 25 \sqrt{25}}{5 \times 20 \sqrt{20}} \\ & \mathrm{x}=5\end{aligned}$

</details>

---

### Q17. JEE Main 2024 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Three infinitely long charged thin sheets are placed as shown in figure. The magnitude of electric field at the point $P$ is $\frac{x \sigma}{\epsilon_o}$. The value of $x$ is _______ (all quantities are measured in SI units).
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Z47sHm9MBekJNh_U0cT9gbBvyiSmH-EoCdp_RPO4IuQ.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/-EWDPc2BJp_GXu3cIFKn0BDi0pkQun6XOhcR3wIjuqw.original.fullsize.png">
$\begin{aligned} \overrightarrow{\mathrm{E}}_{\mathrm{p}} & =\left(\frac{\sigma}{2 \varepsilon_0}+\frac{2 \sigma}{2 \varepsilon_0}+\frac{\sigma}{2 \varepsilon_0}\right)(-\hat{\mathrm{i}}) \\ & =-\frac{2 \sigma}{\varepsilon_0} \hat{\mathrm{i}}\end{aligned}$

</details>

---

### Q18. JEE Main 2024 (04 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

An infinite plane sheet of charge having uniform surface charge density $+\sigma_s \mathrm{C} / \mathrm{m}^2$ is placed on $x-y$ plane. Another infinitely long line charge having uniform linear charge density $+\lambda_e \mathrm{C} / \mathrm{m}$ is placed at $z=4 \mathrm{~m}$ plane and parallel to $y$-axis. If the magnitude values $\left|\sigma_{\mathrm{s}}\right|=2\left|\lambda_{\mathrm{e}}\right|$ then at point $(0,0,2)$, the ratio of magnitudes of electric field values due to sheet charge to that of line charge is $\pi \sqrt{n}: 1$. The value of $n$ is_______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3mmqnC3BUFI6_-UR7d3KSHmFH3qsNg8OiTadQ7S847k.original.fullsize.png">
$\begin{aligned} & \frac{\mathrm{E}_{\mathrm{S}}}{\mathrm{E}_{\ell}}=\frac{\sigma}{2 \epsilon_0} \times \frac{2 \pi \epsilon_0 \mathrm{r}}{\lambda} \\ & =\frac{\pi \times \sigma \mathrm{r}}{\lambda} \\ & =\frac{\pi \times 2 \lambda \times 2}{\lambda}=\frac{4 \pi}{1} \\ & \therefore \mathrm{n}=16\end{aligned}$

</details>

---

### Q19. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

An infinitely long positively charged straight thread has a linear charge density $\lambda \mathrm{Cm}^{-1}$. An electron revolves along a circular path having axis along the length of the wire. The graph that correctly represents the variation of the kinetic energy of electron as a function of radius of circular path from the wire is :

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9hE4FgtxJBT-PwhAsEMdPLNJD8Q0FTFVlHkWifXCKts.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0q8mevqjTkJlNzHN_8H1Fj2SRiJAxG2Oc0jg6RHQuuA.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/57jgWbXuEi4VZQmSpym1dzP840zTnYjth4WlspqJInk.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/BR6QEgN1adV8UGHk5Gz9fVIsWguMn31AMfZtwbLjFGU.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/57jgWbXuEi4VZQmSpym1dzP840zTnYjth4WlspqJInk.original.fullsize.png">**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/wczJbgWSqTYqVQpfX4c6gLi93uGcWR-uIYsuZ2qFgfE.original.fullsize.png">
Electric field $\mathrm{E}$ at a distance $\mathrm{r}$ due to infinite long wire is $E=\frac{2 k \lambda}{r}$
Force of electron $\Rightarrow F=e E$
$\begin{aligned}
& F=e\left(\frac{2 k \lambda}{r}\right) \\
& F=\frac{2 k \lambda e}{r}
\end{aligned}$
This force will provide required centripetal force
$\begin{aligned}
\mathrm{F} & =\frac{\mathrm{m}^2}{\mathrm{r}}=\frac{2 \mathrm{k} \lambda \mathrm{e}}{\mathrm{r}} \\
\mathrm{v} & =\sqrt{\frac{2 \mathrm{k} \lambda \mathrm{e}}{\mathrm{m}}} \\
\mathrm{KE} & =\frac{1}{2} \mathrm{mv}^2=\frac{1}{2} \mathrm{~m}\left(\frac{2 \mathrm{k} \lambda \mathrm{e}}{\mathrm{m}}\right) \\
& =\mathrm{k} \lambda \mathrm{e}
\end{aligned}$

</details>

---

### Q20. JEE Main 2024 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `3`

Suppose a uniformly charged wall provides a uniform electric field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>×</mo><msup><mn>10</mn><mn>4</mn></msup><mo> </mo><mi mathvariant="normal">N</mi><mo> </mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> normally. A charged particle of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo> </mo><mi mathvariant="normal">g</mi></math> being suspended through a silk thread of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo> </mo><mi>cm</mi></math> and remain stayed at a distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo> </mo><mi>cm</mi></math> from the wall. Then the charge on the particle will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mi mathvariant="normal">x</mi></msqrt></mfrac><mi>μ</mi><mi mathvariant="normal">C</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo></math> ________ [use <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>=</mo><mn>10</mn><mo> </mo><mi mathvariant="normal">m</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>]

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6d1fe597-09ec-49b4-804f-91d9d341ee8c.png" style="width: 200px; height: 228px;"/></p><p>As we can see from geometry, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>θ</mi><mo>=</mo><mfrac><mn>10</mn><mn>20</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>θ</mi><mo>=</mo><mn>30</mn><mo>°</mo></math></p><p>Vertical component of tension will balance the weight and the horizontal component will balance the electric force. Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>θ</mi><mo>=</mo><mfrac><mrow><mi>q</mi><mi>E</mi></mrow><mrow><mi>m</mi><mi>g</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mn>30</mn><mo>°</mo><mo>=</mo><mfrac><mrow><mi>q</mi><mo>×</mo><mn>2</mn><mo>×</mo><msup><mn>10</mn><mn>4</mn></msup></mrow><mrow><mn>2</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>×</mo><mn>10</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>=</mo><mi>q</mi><mo>×</mo><msup><mn>10</mn><mn>6</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>q</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mo> </mo><mi mathvariant="normal">C</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo> </mo><mi>μC</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math>.</p>

</details>

---

### Q21. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>q</mi></math> are separated by a distance ‘<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math>’ in air. At a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> from charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math>, the resultant electric field is zero. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>(</mo><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>)</mo></mrow><mi>r</mi></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>r</mi><mrow><mn>3</mn><mo>(</mo><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>)</mo></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>r</mi><mrow><mo>(</mo><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>)</mo></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>(</mo><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>r</mi><mrow><mo>(</mo><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>)</mo></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d4ff1517-ec91-46d2-af87-471bfb053b30.png" style="width: 300px; height: 67px;"/></p><p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><msub><mover><mi>E</mi><mo>→</mo></mover><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub></mfenced><mi>P</mi></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi><mo>×</mo><mn>3</mn><mi>q</mi></mrow><mstyle displaystyle="true"><msup><mfenced><mrow><mi>r</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mi>r</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>-</mo><mi>x</mi><mo>=</mo><msqrt><mn>3</mn></msqrt><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mfrac><mi>r</mi><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfrac></math></p>

</details>

---

### Q22. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A particle of charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>q</mi></math> and mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> moves in a circle of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> around an infinitely long line charge of linear density <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>λ</mi></math>. Then time period will be given as:
(Consider <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> as Coulomb's constant)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>T</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>4</mn><msup><mi>π</mi><mn>2</mn></msup><mo> </mo><mi>m</mi></mrow><mrow><mn>2</mn><mi>k</mi><mi>λ</mi><mi>q</mi></mrow></mfrac><msup><mi>r</mi><mn>3</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mn>2</mn><mi>π</mi><mi>r</mi><msqrt><mfrac><mi>m</mi><mrow><mn>2</mn><mi>k</mi><mi>λ</mi><mi>q</mi></mrow></mfrac></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>π</mi><mi>r</mi></mrow></mfrac><msqrt><mfrac><mi>m</mi><mrow><mn>2</mn><mi>k</mi><mi>λ</mi><mi>q</mi></mrow></mfrac></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>π</mi></mrow></mfrac><msqrt><mfrac><mrow><mn>2</mn><mi>k</mi><mi>λ</mi><mi>q</mi></mrow><mi>m</mi></mfrac></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mn>2</mn><mi>π</mi><mi>r</mi><msqrt><mfrac><mi>m</mi><mrow><mn>2</mn><mi>k</mi><mi>λ</mi><mi>q</mi></mrow></mfrac></msqrt></math>**

**Detailed Solution:**

<blockquote><p>Attractive electrostatic force due to line charge on the charged particle will provide the required centripetal force. Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mfenced><mfrac><mrow><mn>2</mn><mi>k</mi><mi>λ</mi></mrow><mi>r</mi></mfrac></mfenced><mo>=</mo><mi>m</mi><msup><mi>ω</mi><mn>2</mn></msup><mi>r</mi></math></p><p><sup><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>ω</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>2</mn><mi>k</mi><mi>λ</mi><mi>q</mi></mrow><mrow><mi>m</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac></math></sup></p><p><sup><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mi>T</mi></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>2</mn><mi>k</mi><mi>λ</mi><mi>q</mi></mrow><mrow><mi>m</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac></math></sup></p><p><sup><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>T</mi><mo>=</mo><mn>2</mn><mi>π</mi><mi>r</mi><msqrt><mfrac><mi>m</mi><mrow><mn>2</mn><mi>k</mi><mi>λ</mi><mi>q</mi></mrow></mfrac></msqrt></math></sup></p></blockquote>

</details>

---

### Q23. JEE Main 2024 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

An electron is moving under the influence of the electric field of a uniformly charged infinite plane sheet <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> having surface charge density <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>σ</mi></math>. The electron at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn></math> is at a distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo> </mo><mi mathvariant="normal">m</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> and has a speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo> </mo><mi mathvariant="normal">m</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>σ</mi></math>, if the electron strikes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>1</mn><mo> </mo><mi mathvariant="normal">s</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mfenced close="]" open="["><mfrac><mrow><mi>m</mi><msub><mi>ϵ</mi><mn>0</mn></msub></mrow><mi>e</mi></mfrac></mfenced><mo> </mo><mfrac><mi mathvariant="normal">C</mi><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></mfrac></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math> is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p>The value of the electric field due to the uniformly charged plane sheet is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mi>σ</mi><mrow><mn>2</mn><msub><mi>ε</mi><mn>0</mn></msub></mrow></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Thus, the force on the electron is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mi>F</mi></mtd><mtd><mo>=</mo></mtd><mtd><mo>-</mo><mi>e</mi><mi>E</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>-</mo><mfrac><mrow><mi>σ</mi><mi>e</mi></mrow><mrow><mn>2</mn><msub><mi>ε</mi><mn>0</mn></msub></mrow></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></mtd></mtr></mtable></math></p><p>So, the acceleration of the electron is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mi>σ</mi><mi>e</mi></mrow><mrow><mn>2</mn><msub><mi>ε</mi><mn>0</mn></msub><mo> </mo><mi>m</mi></mrow></mfrac></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mo>=</mo><mn>1</mn><mo> </mo><mi mathvariant="normal">m</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>1</mn><mo> </mo><mi mathvariant="normal">s</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo> </mo><mi mathvariant="normal">m</mi></math></p><p>Using the equation of motion, it can be written that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>=</mo><mn>1</mn><mo>×</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>×</mo><mfrac><mrow><mi>σ</mi><mi>e</mi></mrow><mrow><mn>2</mn><msub><mi>ε</mi><mn>0</mn></msub><mo> </mo><mi>m</mi></mrow></mfrac><mo>×</mo><mo>(</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mspace linebreak="newline"></mspace><mo>⇒</mo><mi>σ</mi><mo>=</mo><mn>8</mn><mfrac><mrow><msub><mi>ε</mi><mn>0</mn></msub><mo> </mo><mi>m</mi></mrow><mi>e</mi></mfrac><mo> </mo><mi mathvariant="normal">C</mi><mo> </mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mi>α</mi><mo>=</mo><mn>8</mn></math>.</p>

</details>

---

### Q24. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Given below are two statements : one is labelled as Assertion (A) and the other is labelled as Reason(R)
Assertion (A) : Work done by electric field on moving a positive charge on an equipotential surface is always zero.
Reason (R) : Electric lines of forces are always perpendicular to equipotential surfaces.
In the light of the above statements, choose the most appropriate answer from the options given below :

**Options:**

- **(A)** Both (A) and (R) are correct but (R) is not the correct explanation of (A)
- **(B)** (A) is correct but (R) is not correct
- **(C)** (A) is not correct but (R) is correct
- **(D)** Both (A) and (R) are correct and (R) is the correct explanation of (A)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Both (A) and (R) are correct and (R) is the correct explanation of (A)**

**Detailed Solution:**

<p>The equipotential surfaces are surfaces where the electric potential is the same at every point. In other words, there is no potential difference along an equipotential surface. Since work done <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>W</mi><mo>)</mo></math> is given by the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>W</mi><mo>=</mo><mi>q</mi><mo>∆</mo><mi>V</mi></math>, and there is no potential difference on an equipotential surface, the work done is always zero.</p><p>As there is no force along the surface of the equipotential surface, the electric field must be perpendicular to the surface.</p><p>Hence, while both statements are correct, the reason (R) is providing the correct explanation for why the work done on a positive charge on an equipotential surface is always zero.</p>

</details>

---

### Q25. JEE Main 2024 (27 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>A thin metallic wire having cross sectional area of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo> </mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math> is used to make a ring of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo> </mo><mi>cm</mi></math>. A positive charge of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>π</mi><mo> </mo><mi mathvariant="normal">C</mi></math> is uniformly distributed over the ring, while another positive charge of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo> </mo><mi>pC</mi></math> is kept at the centre of the ring. The tension in the ring is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_______</mi><mo> </mo><mi mathvariant="normal">N</mi></math>; provided that the ring does not get deformed (neglect the influence of gravity).</p><p>(Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><mi>π</mi><msub><mi>ϵ</mi><mn>0</mn></msub></mrow></mfrac><mo>=</mo><mn>9</mn><mo>×</mo><msup><mn>10</mn><mn>9</mn></msup></math> SI units)</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ac5fbda3-2d09-40cf-ba2a-fc68f379037b.png" style="width: 250px; height: 253px;"/></p><p>The linear charge density of the ring is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>=</mo><mfrac><mi>Q</mi><mrow><mn>2</mn><mi>π</mi><mi>R</mi></mrow></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>With reference to the above diagram, for the equilibrium condition of the ring, it can be written that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo> </mo><mi>T</mi><mi>s</mi><mi>i</mi><mi>n</mi><mfenced><mfrac><mrow><mi>d</mi><mi>θ</mi></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>π</mi><msub><mi>ε</mi><mn>0</mn></msub></mrow></mfrac><mfrac><msub><mi>q</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mfrac><mo>·</mo><mfenced close="]" open="["><mrow><mi>λ</mi><mfenced><mrow><mi>R</mi><mi>d</mi><mi>θ</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>T</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>π</mi><msub><mi>ε</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mrow><msub><mi>q</mi><mn>0</mn></msub><mi>Q</mi></mrow><mrow><mfenced><msup><mi>R</mi><mn>2</mn></msup></mfenced><mo>×</mo><mn>2</mn><mi>π</mi></mrow></mfrac></math> [As for very small angles <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mfenced><mfrac><mrow><mi>d</mi><mi>θ</mi></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>d</mi><mi>θ</mi></mrow><mn>2</mn></mfrac></math>]</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>9</mn><mo>×</mo><msup><mn>10</mn><mn>9</mn></msup></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>π</mi><mo>×</mo><mn>30</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>12</mn></mrow></msup></mrow></mfenced></mrow><mrow><mo>(</mo><mn>0</mn><mo>.</mo><mn>30</mn><msup><mo>)</mo><mn>2</mn></msup><mo>×</mo><mn>2</mn><mi>π</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>9</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>×</mo><mn>30</mn></mrow><mrow><mn>9</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>3</mn><mo> </mo><mi mathvariant="normal">N</mi></math></p>

</details>

---

### Q26. JEE Main 2023 (13 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>A thin infinite sheet charge and an infinite line charge of respective charge densities <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>&#963;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>&#955;</mi></math> are placed parallel at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> distance from each other. Points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> are at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mi>&#960;</mi></mfrac><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mi mathvariant="normal">&#960;</mi></mfrac><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> perpendicular distances from line charge towards sheet charge, respectively. <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>p</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>q</mi></msub></math> are the magnitudes of resultant electric field intensities at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>E</mi><mi>P</mi></msub><msub><mi>E</mi><mi>Q</mi></msub></mfrac><mo>=</mo><mfrac><mn>4</mn><mi>a</mi></mfrac></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>|</mo><mi>&#963;</mi><mo>|</mo><mo>=</mo><mo>|</mo><mi>&#955;</mi><mo>|</mo><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is _____.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<blockquote><p>Let&#39;s consider the following diagram:</p><p style="text-align: center;"><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6632b4b7-4467-431e-a8b2-6b27f168b004.png" style="width: 150px; height: 126px;" /></p><p>The formula to calculate the electric field due to an infinitely long charged sheet is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>s</mi></msub><mo>=</mo><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>The formula to calculate the electric field due to an infinitely long line charge is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>l</mi></msub><mo>=</mo><mfrac><mi>&#955;</mi><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>r</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Using equations (1) and (2), the electric field at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> can be calculated as follows:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>E</mi><mi>P</mi></msub></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="|" open="|"><mrow><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mrow><mn>2</mn><mi>&#955;</mi></mrow><mstyle displaystyle="true"><mfrac><mn>3</mn><mi>&#960;</mi></mfrac></mstyle></mfrac></mrow></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="|" open="|"><mrow><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>-</mo><mfrac><mi>&#955;</mi><mrow><mn>6</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac></mrow></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mi>&#963;</mi><mrow><mn>6</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></mtd></mtr></mtable></math></p><p>Similarly, the electric field at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>E</mi><mi>Q</mi></msub></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="|" open="|"><mrow><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mrow><mn>2</mn><mi>&#955;</mi></mrow><mstyle displaystyle="true"><mfrac><mn>4</mn><mi>&#960;</mi></mfrac></mstyle></mfrac></mrow></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="|" open="|"><mrow><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>-</mo><mfrac><mi>&#955;</mi><mrow><mn>8</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac></mrow></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mi>&#963;</mi><mrow><mn>4</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></mtd></mtr></mtable></math></p><p>Divide equation (3) by equation (4) to obtain the required ratio.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mfrac><msub><mi>E</mi><mi>P</mi></msub><msub><mi>E</mi><mi>Q</mi></msub></mfrac></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mstyle displaystyle="true"><mfrac><mi>&#963;</mi><mrow><mn>6</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mi>&#963;</mi><mrow><mn>4</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac></mstyle></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mn>4</mn><mn>6</mn></mfrac></mtd></mtr><mtr><mtd></mtd><mtd></mtd><mtd></mtd></mtr></mtable></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>6</mn></math>.</p></blockquote>

</details>

---

### Q27. JEE Main 2023 (10 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>An electron revolves around an infinite cylindrical wire having uniform linear charge density <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">C</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> in circular path under the influence of attractive electrostatic field as shown in the figure. The velocity of electron with which it is revolving is ______________ <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#215;</mo><msup><mn>10</mn><mn>6</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. Given mass of electron <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>31</mn></mrow></msup><mo>&#160;</mo><mi>kg</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3bfb655d-c817-49a5-b9ea-7b6426fe7028.png" style="width: 150px; height: 253px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<blockquote><p>The electric field is given by </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfenced><mfrac><mrow><mn>2</mn><mi>k</mi><mi>&#955;</mi></mrow><mi>r</mi></mfrac></mfenced></math></p><p>The required centripetal force is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mfenced><mfrac><mrow><mi>m</mi><msup><mi>v</mi><mn>2</mn></msup></mrow><mi>r</mi></mfrac></mfenced></math></p><p>The force due to the field is equal to the required centripetal force,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mfrac><mrow><mn>2</mn><mi>k</mi><mi>&#955;</mi></mrow><mi>r</mi></mfrac></mfenced><mi>e</mi><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mi>v</mi><mn>2</mn></msup></mrow><mi>r</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>v</mi><mo>=</mo><msqrt><mfrac><mrow><mn>2</mn><mi>k</mi><mi>&#955;</mi><mi>e</mi></mrow><mi>m</mi></mfrac></msqrt><mspace linebreak="newline"></mspace><mo>=</mo><msqrt><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup><mo>&#215;</mo><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>19</mn></mrow></msup></mrow><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>31</mn></mrow></msup></mrow></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mn>13</mn></msup></msqrt><mspace linebreak="newline"></mspace><mo>=</mo><mn>4</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mn>6</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mn>8</mn><mo>&#160;</mo><mo>&#215;</mo><mo>&#160;</mo><msup><mn>10</mn><mn>6</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p></blockquote>

</details>

---

### Q28. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Graphical variation of electric field due to a uniformly charged insulating solid sphere of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mo>,</mo><mo>&#160;</mo></math>with distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">r</mi></math> from the centre <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">O</mi></math> is represented by:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4467d891-8c42-4a4b-988a-94dcd3e77eaf.png" style="width: 200px; height: 191px;" /></p>

**Options:**

- **(A)** <p>Dig </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7aa4b8ce-b583-4dd8-9f7f-11d89ea01e69.png" style="width: 200px; height: 148px;" /></p>
- **(B)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/863d7968-bef1-4159-9395-c8edaf96af74.png" style="width: 200px; height: 147px;" /></p><p> </p>
- **(C)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1704a37e-5e6a-48a5-b9ac-166113d41067.png" style="width: 200px; height: 146px;" /></p><p> </p>
- **(D)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f6283172-645a-484d-8ecc-f42632aaf8b3.png" style="width: 200px; height: 153px;" /></p><p> </p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <p>Dig </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7aa4b8ce-b583-4dd8-9f7f-11d89ea01e69.png" style="width: 200px; height: 148px;" /></p>**

**Detailed Solution:**

<blockquote><p>The electric field inside a solid insulated sphere is given by </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mrow><mi>i</mi><mi>n</mi><mi>s</mi><mi>i</mi><mi>d</mi><mi>e</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>r</mi></mrow><mrow><mn>3</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>&#60;</mo><mi>R</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#961;</mi></math> is volume charge density.</p><p>Hence, the electric field varies linearly with the distance as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">E</mi><mi>inside</mi></msub><mo>&#8733;</mo><mo>&#160;</mo><msup><mi>r</mi><mn>1</mn></msup></math></p><p>Now, the electric field for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>&#62;</mo><mi>R</mi></math> is given by </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mrow><mi>o</mi><mi>u</mi><mi>t</mi><mi>s</mi><mi>i</mi><mi>d</mi><mi>e</mi></mrow></msub><mo>=</mo><mfrac><mi>Q</mi><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">E</mi><mi>outside</mi></msub><mo>&#8733;</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mfrac></math></p><p>Thus, the graph starts decreasing as a power law graph as shown in the figure for the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>&#62;</mo><mi>R</mi></math>.</p><p>Hence, this graph is the right option.</p></blockquote>

</details>

---

### Q29. JEE Main 2023 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>A cubical volume is bounded by the surfaces <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mi>a</mi></math>. The electric field in the region is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="italic">E</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><msub><mi>E</mi><mn>0</mn></msub><mi>x</mi><mover><mi mathvariant="italic">i</mi><mo mathvariant="italic">^</mo></mover></math>. Where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>0</mn></msub><mo>=</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mn>4</mn></msup><mo>&#160;</mo><msup><mi>NC</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>cm</mi></math>, the charge contained in the cubical volume is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8211;</mo><mn>14</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">C</mi></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> is ______.</p><p>(Take <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#1013;</mi><mn>0</mn></msub><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>12</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">N</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>)</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **288**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/250fe93b-ea5f-4a12-8efc-6d871966fb0f-9896827.png" style="width: 300px; height: 293px;" /></p><p>Given here, electric field, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>E</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mi>E</mi><mn>0</mn></msub><mi>x</mi><mover><mi mathvariant="italic">i</mi><mo mathvariant="italic">^</mo></mover></math></p><p>Here, the flux passes mainly through surface areas, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mi>E</mi><mi>F</mi><mi>G</mi><mi>H</mi></math>. As the surfaces <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AEFB</mi><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mi>CGHD</mi></math> are parallel to the electric field, so flux for these surfaces are zero. Again in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mi>F</mi><mi>G</mi><mi>H</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>0</mn></math>, thus, electric field is zero.</p><p>Hence, the flux only passes through the surface are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi></math>.</p><p>The net flux is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#981;</mi><mi>net</mi></msub><mo>=</mo><msub><mi>&#981;</mi><mi>ABCD</mi></msub><mo>=</mo><msub><mi>E</mi><mn>0</mn></msub><mi>a</mi><mo>&#183;</mo><msup><mi>a</mi><mn>2</mn></msup></math></p><p>Using Gauss&#39;s law, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>q</mi><mi>en</mi></msub><msub><mi>&#1013;</mi><mn>0</mn></msub></mfrac><mo>=</mo><msub><mi>E</mi><mn>0</mn></msub><msup><mi>a</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>q</mi><mi>en</mi></msub><mo>=</mo><msub><mi>E</mi><mn>0</mn></msub><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>a</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mn>4</mn></msup><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>12</mn></mrow></msup><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>288</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>14</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">C</mi></math></p><p>Hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mn>288</mn></math>.</p>

</details>

---

### Q30. JEE Main 2023 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

Two equal positive point charges are separated by a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi></math>. The distance of a point from the centre of the line joining two charges on the equatorial line (perpendicular bisector) at which force experienced by a test charge <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>0</mn></msub></math> becomes maximum is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><msqrt><mi>x</mi></msqrt></mfrac></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/95810be8-b04f-4cb9-b89c-4ddfe88ebbc2-9896737.png" style="width: 350px; height: 269px;" /></p><p>Let us assume at distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>, force is maximum.</p><p>Now, force at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub><mo>=</mo><mn>2</mn><mi>F</mi><mi>cos</mi><mi>&#952;</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mi>K</mi><mi>q</mi><msub><mi>q</mi><mn>0</mn></msub><mi>y</mi></mrow><msup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfenced><mstyle displaystyle="true"><mfrac bevelled="true"><mn>3</mn><mn>2</mn></mfrac></mstyle></msup></mfrac></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub></math> to be maximum, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><msub><mi>F</mi><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p>Or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mi>q</mi><msub><mi>q</mi><mn>0</mn></msub><mfrac><mrow><msup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfenced><mfrac bevelled="true"><mn>3</mn><mn>2</mn></mfrac></msup><mo>-</mo><mi>y</mi><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle><mo>&#215;</mo><mn>2</mn><mi>y</mi><msup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfenced><mfrac bevelled="true"><mn>1</mn><mn>2</mn></mfrac></msup></mrow><msup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfenced><mn>3</mn></msup></mfrac><mo>=</mo><mn>0</mn></math></p><p>Simplifying, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mi>a</mi><msqrt><mn>2</mn></msqrt></mfrac></math>.</p><p>Hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>.</p>

</details>

---

### Q31. JEE Main 2023 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Considering a group of positive charges, which of the following statements is correct?

**Options:**

- **(A)** Net potential of the system cannot be zero at a point but net electric field can be zero at that point
- **(B)** Net potential of the system at a point can be zero but net electric field can&#39;t be zero at that point
- **(C)** Both the net potential and the net field can be zero at a point
- **(D)** Both the net potential and the net electric field cannot be zero at a point

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Net potential of the system cannot be zero at a point but net electric field can be zero at that point**

**Detailed Solution:**

<p>As we know, net potential will be algebraic sum of potential due to each charge, so we can write <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub><mo>=</mo><mo>&#8721;</mo><mfenced><mfrac><mrow><mi>k</mi><msub><mi>Q</mi><mi>i</mi></msub></mrow><msub><mi>r</mi><mi>i</mi></msub></mfrac></mfenced></math>.</p><p>As given in the question, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>Q</mi><mi>i</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mi>i</mi></msub></math> are positive, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><msub><mi>V</mi><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub><mo>&#62;</mo><mn>0</mn></math></p><p>But electric field is a vector quantity, so it can be zero for a given arrangement of charges. For example, electric field at the centre of the two equal charges at certain distance will be zero as electric field due to both charges will be in opposite direction and hence will cancel each other.</p>

</details>

---

### Q32. JEE Main 2023 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>As shown in the figure, a point charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> is placed at the centre of conducting spherical shell of inner radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and outer radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>. The electric field due to charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> in three different regions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>,</mo><mo>&#160;</mo><mi>I</mi><mi>I</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>I</mi><mi>I</mi><mi>I</mi></math> is given by : <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>I</mi><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mi>r</mi><mo>&#160;</mo><mo>&#60;</mo><mo>&#160;</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>I</mi><mi>I</mi><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mi>a</mi><mo>&#160;</mo><mo>&#60;</mo><mo>&#160;</mo><mi>r</mi><mo>&#160;</mo><mo>&#60;</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>I</mi><mi>I</mi><mi>I</mi><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mi>r</mi><mo>&#160;</mo><mo>&#62;</mo><mo>&#160;</mo><mi>b</mi><mo>)</mo></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/66c2bd65-5b88-44e1-b4e7-cd5bb2d10b94-9895420.PNG" style="width: 250px; height: 216px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>I</mi></msub><mo>=</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>E</mi><mrow><mi>I</mi><mi>I</mi></mrow></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>E</mi><mrow><mi>I</mi><mi>I</mi><mi>I</mi></mrow></msub><mo>&#8800;</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>I</mi></msub><mo>&#8800;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>E</mi><mrow><mi>I</mi><mi>I</mi></mrow></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>E</mi><mrow><mi>I</mi><mi>I</mi><mi>I</mi></mrow></msub><mo>&#8800;</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>I</mi></msub><mo>&#8800;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>E</mi><mrow><mi>I</mi><mi>I</mi></mrow></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>E</mi><mrow><mi>I</mi><mi>I</mi><mi>I</mi></mrow></msub><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>I</mi></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>E</mi><mrow><mi>I</mi><mi>I</mi></mrow></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>E</mi><mrow><mi>I</mi><mi>I</mi><mi>I</mi></mrow></msub><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>I</mi></msub><mo>&#8800;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>E</mi><mrow><mi>I</mi><mi>I</mi></mrow></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>E</mi><mrow><mi>I</mi><mi>I</mi><mi>I</mi></mrow></msub><mo>&#8800;</mo><mn>0</mn></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/66c2bd65-5b88-44e1-b4e7-cd5bb2d10b94-9895420.PNG" style="width: 250px; height: 216px;" /></p><p>In region I, due to charge at centre, electric field will be present.</p><p>But in region II, electric field will be zero as electric field inside material of conductor is zero.</p><p>Again for outside region, net charges enclosed is not zero and therefore electric field will exist.</p>

</details>

---

### Q33. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A point charge of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mo>&#181;</mo><mi mathvariant="normal">C</mi></math> is placed at the origin. At what location on the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>-axis should a point charge of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>&#160;</mo><mo>&#181;</mo><mi mathvariant="normal">C</mi></math> be placed so that the net electric field is zero at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>cm</mi></math> on the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>-axis ?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi>cm</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi>cm</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>8</mn><mo>&#160;</mo><mi>cm</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>&#8211;</mo><mn>4</mn><mo>&#160;</mo><mi>cm</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi>cm</mi></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1ca50b91-8500-4d58-9b8f-0b4574c42e7d-874e8a3a-71d6-405c-8d39-79d277f30430-9894462.PNG" style="width: 300px; height: 139px;" /></p><p>Let the charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>&#160;</mo><mi>&#956;C</mi></math> be placed at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mn>0</mn></msub></math> from the origin as shown in the figure.</p><p>For the electric field at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> to be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>P</mi></msub><mo>=</mo><mn>0</mn><mspace linebreak="newline"/><mo>&#8658;</mo><mfrac><mrow><mi>k</mi><mo>&#215;</mo><mn>10</mn></mrow><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi><mo>&#215;</mo><mn>40</mn><mo>&#160;</mo></mrow><msup><mfenced><mrow><msub><mi>X</mi><mn>0</mn></msub><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>2</mn><mrow><msub><mi>X</mi><mn>0</mn></msub><mo>-</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>X</mi><mn>0</mn></msub><mo>-</mo><mn>2</mn><mo>=</mo><mn>4</mn></math></p><p>Therefore, the charge is located at <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mn>0</mn></msub><mo>=</mo><mn>4</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi>cm</mi></math></p>

</details>

---

### Q34. JEE Main 2023 (25 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>A uniform electric field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> is created between two parallel charged plates (as shown in figure). An electron enters the field symmetrically between the plates with a kinetic energy <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>eV</mi><mo>.</mo></math> The length of each plate is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>cm</mi></math>. The angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#952;</mi><mo>)</mo></math> of deviation of the path of electron as it comes out of the field is ______(in degree).</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b0a2f662-96ce-4fec-af47-df9ffda86136-9894312.PNG" style="width: 327px; height: 160px;" /></p><p> </p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **45**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/19d7b95b-6e55-4f63-a16c-f84194158a8a-9894312_1.PNG" style="width: 319px; height: 160px;" /></p><p>Given here, kinetic energy <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>e</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>m</mi><msubsup><mi>u</mi><mi>x</mi><mn>2</mn></msubsup><mo>&#8658;</mo><msub><mi>u</mi><mi>x</mi></msub><mo>=</mo><msqrt><mfrac><mi>e</mi><mi>m</mi></mfrac></msqrt></math></p><p>Acceleration of electron due to electric field is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mrow><mi>e</mi><mi>E</mi></mrow><mi>m</mi></mfrac></math>, where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math> is charge on electron.</p><p>Using equation of motion, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi><mo>=</mo><msub><mi>u</mi><mi>x</mi></msub><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>a</mi><mi>x</mi></msub><msup><mi>t</mi><mn>2</mn></msup></math>  along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> direction, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><msub><mi>u</mi><mi>x</mi></msub><mi>t</mi><mo>+</mo><mn>0</mn><mfenced><mrow><mo>&#8757;</mo><msub><mi>a</mi><mi>x</mi></msub><mo>=</mo><mn>0</mn></mrow></mfenced><mspace linebreak="newline"/><mo>&#8658;</mo><mn>10</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>=</mo><msub><mi>u</mi><mi>x</mi></msub><mi>t</mi><mspace linebreak="newline"/><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mfrac><msup><mn>10</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup><msub><mi>u</mi><mi>x</mi></msub></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Using equation of motion, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mi>y</mi></msub><mo>=</mo><msub><mi>u</mi><mi>y</mi></msub><mo>+</mo><msub><mi>a</mi><mi>y</mi></msub><mi>t</mi></math> along y direction, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mi>y</mi></msub><mo>=</mo><mn>0</mn><mo>+</mo><mfrac><mrow><mi>e</mi><mi>E</mi></mrow><mi>m</mi></mfrac><mi>t</mi><mo>=</mo><mfrac><mrow><mi>e</mi><mi>E</mi></mrow><mi>m</mi></mfrac><mi>t</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mi>y</mi></msub><mo>=</mo><mfrac><mrow><mi>e</mi><mi>E</mi></mrow><mi>m</mi></mfrac><mfenced><mfrac><msup><mn>10</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup><msub><mi>u</mi><mi>x</mi></msub></mfrac></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mfrac><msub><mi>v</mi><mi>y</mi></msub><msub><mi>v</mi><mi>x</mi></msub></mfrac><mo>=</mo><mfrac><mrow><mi>e</mi><mi>E</mi></mrow><mi>m</mi></mfrac><mfenced><mfrac><msup><mn>10</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup><msubsup><mi>u</mi><mi>x</mi><mn>2</mn></msubsup></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>e</mi><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mrow><mi>m</mi><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mi>e</mi><mi>m</mi></mfrac></mstyle></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p>The angle of deviation of the path of electron as it comes out of the field is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mn>45</mn><mo>&#176;</mo></math>.</p>

</details>

---

### Q35. JEE Main 2023 (24 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

A stream of a positively charged particles having <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="italic">q</mi><mi mathvariant="italic">m</mi></mfrac><mo>=</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mn>11</mn></msup><mo>&#160;</mo><mi mathvariant="normal">C</mi><mo>&#160;</mo><msup><mi>kg</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> and velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi mathvariant="normal">v</mi><mo>&#8594;</mo></mover><mn>0</mn></msub><mo>=</mo><mn>3</mn><mo>&#215;</mo><msup><mn>10</mn><mn>7</mn></msup><mo>&#160;</mo><mover><mi>i</mi><mo>^</mo></mover><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> is deflected by an electric field <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>8</mn><mover><mi>j</mi><mo mathvariant="italic">^</mo></mover><mo>&#160;</mo><mi>kV</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The electric field exists in a region of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>cm</mi></math> along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> direction. Due to the electric field, the deflection of the charge particles in the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> direction is _____  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mm</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/078253bf-0b23-417c-a34d-b5ba097a5d9b-9893917.PNG" style="width: 300px; height: 118px;" /></p><p>Acceleration of the particles due to electric field, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mi>F</mi><mi>m</mi></mfrac><mo>=</mo><mfrac><mrow><mi>q</mi><mi>E</mi></mrow><mi>m</mi></mfrac><mo>=</mo><mfenced><mrow><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mn>11</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>.</mo><mn>8</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mn>14</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p>Time to cross plates <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>d</mi><mi>v</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>10</mn></mrow><mrow><mn>3</mn><mo>&#215;</mo><msup><mn>10</mn><mn>7</mn></msup></mrow></mfrac></math></p><p>Now deflection,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>at</mi><mn>2</mn></msup><mspace linebreak="newline"/><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>3</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mn>14</mn></msup></mrow></mfenced><msup><mfenced><mfrac><mrow><mn>0</mn><mo>.</mo><mn>10</mn></mrow><mrow><mn>3</mn><mo>&#215;</mo><msup><mn>10</mn><mn>7</mn></msup></mrow></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>002</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>mm</mi></math></p>

</details>

---

### Q36. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>A spherically symmetric charge distribution is considered with charge density varying as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#961;</mi><mfenced><mi>r</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left" equalcolumns="true" equalrows="true"><mtr><mtd><msub><mi>&#961;</mi><mn>0</mn></msub><mfenced><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#8722;</mo><mfrac><mi>r</mi><mi>R</mi></mfrac></mrow></mfenced></mtd><mtd><mtext>&#160;for&#160;</mtext><mi>r</mi><mo>&#8804;</mo><mi>R</mi></mtd></mtr><mtr><mtd><mo>&#160;</mo><mi>Zero</mi></mtd><mtd><mo>&#160;</mo></mtd><mtd><mo>&#160;</mo></mtd><mtd><mi>for</mi><mo>&#160;</mo><mi>r</mi><mo>&#62;</mo><mi>R</mi></mtd></mtr></mtable></mfenced></math></p><p> </p><p>Where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mfenced><mrow><mi>r</mi><mo>&#60;</mo><mi>R</mi></mrow></mfenced></math> is the distance from the centre <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> (as shown in figure). The electric field at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> will be :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bc891dff-30ec-4b12-b920-07c5eeaa772d-image.png" style="width: 120px; height: 117px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>&#961;</mi><mn>0</mn></msub><mi>r</mi></mrow><mrow><mn>4</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mi>r</mi><mi>R</mi></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>&#961;</mi><mn>0</mn></msub><mi>r</mi></mrow><mrow><mn>3</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mi>r</mi><mi>R</mi></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>&#961;</mi><mn>0</mn></msub><mi>r</mi></mrow><mrow><mn>4</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>r</mi><mi>R</mi></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>&#961;</mi><mn>0</mn></msub><mi>r</mi></mrow><mrow><mn>5</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>r</mi><mi>R</mi></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>&#961;</mi><mn>0</mn></msub><mi>r</mi></mrow><mrow><mn>4</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>r</mi><mi>R</mi></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2da854da-3f86-449f-93c8-43d71f49f354-image.png" style="width: 130px; height: 129px;" /></p><p>According to Gauss&#39;s law, the electric flux through a closed surface area is equal to the charge inside the surface divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#949;</mi><mn>0</mn></msub></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8750;</mo><mover><mrow><mi>E</mi><mo>&#183;</mo></mrow><mo>&#8594;</mo></mover><mi mathvariant="normal">d</mi><mover><mi>s</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><msub><mi>Q</mi><mi>in</mi></msub><msub><mi>&#949;</mi><mn>0</mn></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>E</mi><mn>4</mn><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mi>r</mi></msubsup><msub><mi>&#961;</mi><mn>0</mn></msub><mfenced><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mi>r</mi><mi>R</mi></mfrac></mrow></mfenced><mn>4</mn><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup><mi mathvariant="normal">d</mi><mi>r</mi></mrow><msub><mi>&#949;</mi><mn>0</mn></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>E</mi><mn>4</mn><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msub><mi>&#961;</mi><mi>o</mi></msub><mn>4</mn><mi>&#960;</mi></mrow><msub><mi>&#949;</mi><mi>o</mi></msub></mfrac><mfenced><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><mfrac><msup><mi>r</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mfrac><msup><mi>r</mi><mn>4</mn></msup><mrow><mn>4</mn><mi>R</mi></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>E</mi><mo>=</mo><mfrac><mrow><msub><mi>&#961;</mi><mi>o</mi></msub><mi>r</mi></mrow><mrow><mn>4</mn><msub><mi>&#949;</mi><mi>o</mi></msub></mrow></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>r</mi><mi>R</mi></mfrac></mrow></mfenced></math></p></blockquote>

</details>

---

### Q37. JEE Main 2022 (28 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>A uniform electric field <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfenced><mfrac><mrow><mn>8</mn><mi>m</mi></mrow><mi>e</mi></mfrac></mfenced><mi mathvariant="normal">V</mi><mo> </mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> is created between two parallel plates of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo> </mo><mi mathvariant="normal">m</mi></math> as shown in figure, (where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo></math> mass of electron and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo></math> charge of electron). An electron enters the field symmetrically between the plates with a speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo> </mo><mi mathvariant="normal">m</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The angle of the deviation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>&theta;</mi></mfenced></math> of the path of the electron as it comes out of the field will be _____ .</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/842a1b33-c73e-45f6-bb43-e46c56c072fd-image.png" style="width: 250px; height: 123px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>4</mn></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>2</mn></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>3</mn></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>2</mn></mfenced></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e81a708d-37d6-42c5-9e9e-cf6249ce41c3-image.png" style="width: 350px; height: 145px;" /></p><p>Time taken by the electron to cross will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><msub><mi>v</mi><mi>x</mi></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>.</p><p>Acceleration of the electron along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> axis</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>g</mi></msub><mo>=</mo><mfrac><mi>F</mi><mi>m</mi></mfrac><mo>=</mo><mfrac><mrow><mi>E</mi><mi>e</mi></mrow><mi>m</mi></mfrac><mo>=</mo><mfrac><mrow><mn>8</mn><mi>m</mi></mrow><mi>e</mi></mfrac><mo>&#215;</mo><mfrac><mi>e</mi><mi>m</mi></mfrac><mo>=</mo><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mi>y</mi></msub></math> of the electron  when it has crossed the capacitor will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mi>y</mi></msub><mo>=</mo><msub><mi>a</mi><mi>y</mi></msub><mi>t</mi><mo>=</mo><mn>8</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mfrac><msub><mi>v</mi><mi>y</mi></msub><msub><mi>v</mi><mi>x</mi></msub></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>2</mn></mfrac><mo>=</mo><mn>2</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>2</mn></mfenced></math></p></blockquote>

</details>

---

### Q38. JEE Main 2022 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>A <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> long copper wire carries a current of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>. If the cross section of the wire is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>0</mn><msup><mrow><mo>&#160;</mo><mi>mm</mi></mrow><mn>2</mn></msup></math> and the resistivity of copper is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>7</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>. The force experienced by moving electron in the wire is _____<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>23</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi></math></p><p>(Charge of electron<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>19</mn></mrow></msup><mi mathvariant="normal">C</mi></math> )</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **136**

**Detailed Solution:**

<blockquote><p>Given here, length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>, current <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>, area <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> and resistivity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#961;</mi><mo>=</mo><mn>1</mn><mo>.</mo><mn>7</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>.</p><p>Resistance of wire is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>l</mi></mrow><mi>A</mi></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>.</mo><mn>7</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup><mo>&#215;</mo><mn>1</mn></mrow><mrow><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>5</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>.</mo><mn>7</mn></mrow><mn>2</mn></mfrac><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p></blockquote><blockquote><p>Now, electric field in the wire is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mi>&#961;</mi><mi>J</mi></math>, where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>J</mi><mo>=</mo><mfrac><mi>i</mi><mi>A</mi></mfrac></math> is current density.</p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mrow><mi>i</mi><mi>&#961;</mi></mrow><mi>A</mi></mfrac><mo>=</mo><mi>i</mi><mi>R</mi><mo>=</mo><mn>1</mn><mo>&#215;</mo><mfrac><mrow><mn>1</mn><mo>.</mo><mn>7</mn></mrow><mn>2</mn></mfrac><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Electric force in terms of electric field is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mi>q</mi><mi>E</mi></math></p><p>Therefore, force experienced by moving electron is  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>19</mn></mrow></msup><mo>&#215;</mo><mfrac><mrow><mn>1</mn><mo>.</mo><mn>7</mn></mrow><mn>2</mn></mfrac><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>.</mo><mn>36</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>21</mn></mrow></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>136</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>23</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi></math></p></blockquote>

</details>

---

### Q39. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A positive charge particle of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>&#160;</mo><mi>mg</mi></math> is thrown in opposite direction to a uniform electric field of strength <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mn>5</mn></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. If the charge on the particle is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>&#160;</mo><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> and the initial velocity is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, how much distance it will travel before coming to the rest momentarily

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>**

**Detailed Solution:**

<p>Force experienced by a particle with charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> in an electric field <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mi>q</mi><mi>E</mi></math>.</p><p>Now, the acceleration produced is given as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mi>F</mi><mi>m</mi></mfrac><mo>=</mo><mfrac><mrow><mi>q</mi><mi>E</mi></mrow><mi>m</mi></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>40</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mo>&#215;</mo><msup><mn>10</mn><mn>5</mn></msup></mrow><mrow><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mn>4</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>  (As the particle is projected against the electric field, hence it is decelerated)</p><p>Using, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>v</mi><mn>2</mn></msup><mo>=</mo><msup><mi>u</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>a</mi><mi>s</mi></math></p><p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>0</mn><mn>2</mn></msup><mo>=</mo><msup><mi>u</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>a</mi><mi>s</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi><mo>=</mo><mfrac><msup><mi>v</mi><mn>2</mn></msup><mrow><mn>2</mn><mi>a</mi></mrow></mfrac><mo>=</mo><mfrac><msup><mfenced><mn>200</mn></mfenced><mn>2</mn></msup><mrow><mn>2</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mn>4</mn></msup></mrow></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p>

</details>

---

### Q40. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Two point charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> of magnitude <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mn>8</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mi mathvariant="normal">C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>8</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mi mathvariant="normal">C</mi></math> respectively are placed at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> apart. The electric field at the middle point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> between the charges is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>.</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mn>4</mn></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The distance &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>&#39; between the point charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d3e44411-84eb-4461-ab3e-b30c0b06b303-image.png" style="width: 400px; height: 110px;" /></p><p>Direction of electric field at mid-point due to both charge will be in same direction, which is towards right.</p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> at mid-point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><msup><mfenced><mfrac><mi>d</mi><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><msup><mfenced><mfrac><mi>d</mi><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></mfrac></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mo>.</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mn>4</mn></msup><mo>=</mo><mn>2</mn><mo>&#215;</mo><mfenced close="]" open="["><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#215;</mo><mfrac><mfenced><mrow><mn>8</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup></mrow></mfenced><msup><mi>d</mi><mn>2</mn></msup></mfrac><mo>&#215;</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p>

</details>

---

### Q41. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>The three charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>q</mi><mn>2</mn></mfrac><mo>,</mo><mi>q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>q</mi><mn>2</mn></mfrac></math> are placed at the corners <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mi>D</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> of a square of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> as shown in figure. The magnitude of electric field <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>E</mi></mfenced></math> at the corner <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> of the square, is </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5ded6261-abb9-4c2e-bef2-043a34a5f104-D38.png" style="width: 150px; height: 152px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>q</mi><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>q</mi><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>q</mi><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>q</mi><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>q</mi><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6c80369c-addb-4703-9cb3-91b69723e7c9-image.png" style="width: 190px; height: 174px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>A</mi></msub><mo>=</mo><mfrac><mrow><mi>k</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>q</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mrow><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac></math>,  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>C</mi></msub><mo>=</mo><mfrac><mrow><mi>k</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>q</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mrow><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac></math>  and  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>D</mi></msub><mo>=</mo><mfrac><mrow><mi>k</mi><mfenced><mstyle displaystyle="true"><mi>q</mi></mstyle></mfenced></mrow><msup><mfenced><mrow><msqrt><mn>2</mn></msqrt><mi>a</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mrow><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>As we can see from diagram, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>C</mi></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>E</mi><mi>A</mi></msub></math> are perpendicular.</p><p>Therefore, net electric field will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mrow><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><msqrt><msup><mfenced><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mrow><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mrow><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mrow><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mrow><msqrt><mn>2</mn></msqrt><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mi>q</mi><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p>

</details>

---

### Q42. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p><strong>Statement-I : </strong>A point charge is brought in an electric field. The value of electric field at a point near to the charge may increase if the charge is positive.</p><p><strong>Statement-II :</strong> An electric dipole is placed in a uniform electric field. The net electric force on the dipole will not be zero.</p>

**Options:**

- **(A)** Both statement-I and statement-II are true.
- **(B)** Both statement-I and statement-II are false.
- **(C)** Statement-I is true but statement-II is false.
- **(D)** Statement-I is false but statement-II is true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Statement-I is true but statement-II is false.**

**Detailed Solution:**

<p>If a positive point charge is brought in an electric field. The value of electric field at a point near to the charge may increase or decreases. Hence, statement I is true.</p><p>An electric dipole experiences zero net force in a uniform electric field. Hence, statement II is false.</p>

</details>

---

### Q43. JEE Main 2022 (25 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>In the figure, a very large plane sheet of positive charge is shown. <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> are two points at distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>l</mi></math> from the charge distribution. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#963;</mi></math> is the surface charge density, then the magnitude of electric fields <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> respectively are </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d58dc51f-2638-4746-b21d-a8ee4186aa11-image.png" style="width: 230px; height: 160px;" /></p><p> </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>=</mo><mfrac><mi>&#963;</mi><msub><mi>&#949;</mi><mi>o</mi></msub></mfrac><mo>,</mo><msub><mi>E</mi><mn>2</mn></msub><mo>=</mo><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#949;</mi><mi>o</mi></msub></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#963;</mi></mrow><msub><mi>&#949;</mi><mi>o</mi></msub></mfrac><mo>,</mo><msub><mi>E</mi><mn>2</mn></msub><mo>=</mo><mfrac><mi>&#963;</mi><msub><mi>&#949;</mi><mi>o</mi></msub></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>=</mo><msub><mi>E</mi><mn>2</mn></msub><mo>=</mo><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#949;</mi><mi>o</mi></msub></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>=</mo><msub><mi>E</mi><mn>2</mn></msub><mo>=</mo><mfrac><mi>&#963;</mi><msub><mi>&#949;</mi><mi>o</mi></msub></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>=</mo><msub><mi>E</mi><mn>2</mn></msub><mo>=</mo><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#949;</mi><mi>o</mi></msub></mrow></mfrac></math>**

**Detailed Solution:**

<p>The electric field due to a large uniformly charged non-conducting sheet is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#949;</mi><mi>o</mi></msub></mrow></mfrac></math>. It is independent of the distance from the sheet. Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>=</mo><msub><mi>E</mi><mn>2</mn></msub><mo>=</mo><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#949;</mi><mi>o</mi></msub></mrow></mfrac></math></p>

</details>

---

### Q44. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A long cylindrical volume contains a uniformly distributed charge of density <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#961;</mi></math>. The radius of cylindrical volume is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>. A charge particle <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>q</mi></mfenced></math> revolves around the cylinder in a circular path. The kinetic energy of the particle is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#961;</mi><mi>q</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mrow><mn>4</mn><msub><mi>&#949;</mi><mi>o</mi></msub></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#961;</mi><mi>q</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><msub><mi>&#949;</mi><mi>o</mi></msub></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>q</mi><mi>&#961;</mi></mrow><mrow><mn>4</mn><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow><mrow><mi>q</mi><mi>&#961;</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#961;</mi><mi>q</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mrow><mn>4</mn><msub><mi>&#949;</mi><mi>o</mi></msub></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/94fd557d-f16a-49de-9513-569f2a896702-image.png" style="width: 210px; height: 180px;" /></p><p>Electric field due to a long cylinder is,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mi>&#955;</mi><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>r</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>A</mi></mrow><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>r</mi></mrow></mfrac></math></p><p>If a charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> is rotating in a circle of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>m</mi><msup><mi>v</mi><mn>2</mn></msup></mrow><mi>r</mi></mfrac><mo>=</mo><mi>q</mi><mi>E</mi></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>m</mi><msup><mi>v</mi><mn>2</mn></msup></mrow><mi>r</mi></mfrac><mo>=</mo><mi>q</mi><mfrac><mrow><mi>&#961;</mi><mi>A</mi></mrow><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>r</mi></mrow></mfrac><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>m</mi><msup><mi>v</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mi>q</mi><mi>&#961;</mi><mi>&#960;</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>q</mi><mi>&#961;</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mrow><mn>4</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac></math></p>

</details>

---

### Q45. JEE Main 2022 (24 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A vertical electric field of magnitude <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>5</mn></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> just prevents a water droplet of a mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">g</mi></math> from falling. The value of charge on the droplet will be : (Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>=</mo><mn>9</mn><mo>.</mo><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup><mi mathvariant="normal">C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>0</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup><mi mathvariant="normal">C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup><mi mathvariant="normal">C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup><mi mathvariant="normal">C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>0</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup><mi mathvariant="normal">C</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3201aeaf-2efa-4359-9909-37dee60888a0-image.png" style="width: 80px; height: 176px;" /></p><p>To balance gravitational force, electric force on the liquid drop should act in upward direction.</p><p>For translational equilibrium along vertical direction,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mi>E</mi><mo>=</mo><mi>m</mi><mi>g</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>q</mi><mo>=</mo><mfrac><mrow><mi>m</mi><mi>g</mi></mrow><mi>E</mi></mfrac><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#215;</mo><mn>9</mn><mo>.</mo><mn>8</mn></mrow><mrow><mn>4</mn><mo>.</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>5</mn></msup></mrow></mfrac><mo>=</mo><mn>2</mn><mo>.</mo><mn>0</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup><mi mathvariant="normal">C</mi></math></p>

</details>

---

### Q46. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Choose the incorrect statement:
(a) The electric lines of force entering into a Gaussian surface provide negative flux.
(b) A charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> is placed at the centre of a cube. The flux through all the faces will be the same.
(c) In a uniform electric field net flux through a closed Gaussian surface containing no net charge, is zero.
(d) When an electric field is parallel to a Gaussian surface, it provides a finite non-zero flux.</p><p>Choose the most appropriate answer from the options given below:</p>

**Options:**

- **(A)** (b) and (d) Only
- **(B)** (c) and (d) Only
- **(C)** (a) and (c) Only
- **(D)** (d) Only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) (d) Only**

**Detailed Solution:**

<p>We know that electric flux is a scalar quantity and this is the scalar product of the magnitude of electric field and surface area. </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8b19cb0e-4859-4977-a9d8-eaa0474c2dd1-image.png" style="width: 280px; height: 145px;" /></p><p>Recall, the formula given by Gauss theorem, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mover><mi>E</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>A</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>E</mi><mi>A</mi><mi>cos</mi><mi>&#952;</mi></math>, here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mn>90</mn><mo>&#176;</mo></math>, it means, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mn>0</mn></math>.</p>

</details>

---

### Q47. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two particles <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> having charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn><mo>&#160;</mo><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> respectively are held fixed with a separation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math> At what position a third charged particle should be placed so that it does not experience a net electric force ?
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/87d46ece-42b6-4410-9287-fad6b1c97525-c3f220ad-e8cc-4e73-a414-361bd39b736d-image.png" style="width: 300px; height: 77px;" />

**Options:**

- **(A)** At <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn><mo>&#160;</mo><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> on the right side
- **(B)** At <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> on the left side of system
- **(C)** At <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>25</mn><mo>&#160;</mo><mi>cm</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn><mo>&#160;</mo><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> between two charges
- **(D)** At midpoint between two charges

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) At <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn><mo>&#160;</mo><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> on the right side**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/52e5f78e-3d86-4232-9d07-60abe3ac31fa-image.png" style="width: 300px; height: 77px;" /></p><p>Charge should be placed near <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> distance
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cb33023c-f795-4e05-8821-345d9a6be8d2-image.png" style="width: 250px; height: 85px;" />
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>K</mi><mo>(</mo><mn>20</mn><mo>)</mo><mi>Q</mi></mrow><mrow><mo>(</mo><mn>5</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>K</mi><mo>(</mo><mn>5</mn><mo>)</mo><mi>Q</mi></mrow><msup><mi>X</mi><mn>2</mn></msup></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mo>(</mo><mn>5</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>25</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>10</mn><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>-</mo><mn>25</mn><mo>=</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q48. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Figure shows a rod <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math>, which is bent in a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn><mo>&#176;</mo></math> circular arc of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>. A charge<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>(</mo><mo>-</mo><mi>Q</mi><mo>)</mo></math> is uniformly distributed over rod <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AB</mi></math>. What is the electric filed <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>E</mi><mo>&#8594;</mo></mover></math> at the centre of curvature <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">O</mi></math> ?</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5ff2624b-2d48-46f6-b142-7c7f7918d8f1-image.png" style="width: 256px; height: 237px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mi>Q</mi></mrow><mrow><mn>8</mn><msup><mi>&#960;</mi><mn>2</mn></msup><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow></mfrac><mo>&#160;</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msqrt><mn>3</mn><mi>Q</mi></msqrt></mrow><mrow><mn>8</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow></mfrac><mo>&#160;</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>3</mn><msqrt><mn>3</mn></msqrt><mi>Q</mi></mrow><mrow><mn>8</mn><msup><mi>&#960;</mi><mn>2</mn></msup><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow></mfrac><mo>&#160;</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msqrt><mn>3</mn><mi>Q</mi></msqrt></mrow><mrow><mn>16</mn><msup><mi>&#960;</mi><mn>2</mn></msup><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow></mfrac><mo>&#160;</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mi>Q</mi></mrow><mrow><mn>8</mn><msup><mi>&#960;</mi><mn>2</mn></msup><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow></mfrac><mo>&#160;</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#948;</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">k</mi><mi>&#955;</mi></mrow><mi mathvariant="normal">R</mi></mfrac><mi>sin</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><mi>k</mi></mrow><mi>R</mi></mfrac><mfenced><mfrac><mi>Q</mi><mrow><mn>2</mn><mi>R</mi><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfrac></mfenced><mi>sin</mi><mn>60</mn><mo>&#176;</mo><mover><mi>i</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>3</mn><mi>k</mi><mi>Q</mi></mrow><mrow><mi>&#960;</mi><msup><mi>R</mi><mn>2</mn></msup></mrow></mfrac><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mover><mi>i</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn><mi>&#960;</mi></mrow></mfrac><mfrac><mi>kQ</mi><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup></mfrac><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></math></p>

</details>

---

### Q49. JEE Main 2021 (27 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A uniformly charged disc of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> having surface charge density <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#963;</mi></math> is placed in the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi></math> plane with its center at the origin. Find the electric field intensity along the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math>-axis at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi></math> from origin:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow><mi>&#963;</mi></mfrac><mfenced><mrow><mfrac><mn>1</mn><msup><mfenced><mrow><msup><mi>Z</mi><mn>2</mn></msup><mo>+</mo><msup><mi>R</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac><mo>+</mo><mi>Z</mi></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mi>Z</mi><msup><mfenced><mrow><msup><mi>Z</mi><mn>2</mn></msup><mo>+</mo><msup><mi>R</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>Z</mi><msup><mfenced><mrow><msup><mi>Z</mi><mn>2</mn></msup><mo>+</mo><msup><mi>R</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced><mrow><mfrac><mn>1</mn><mfenced><mrow><msup><mi>Z</mi><mn>2</mn></msup><mo>+</mo><msup><mi>R</mi><mn>2</mn></msup></mrow></mfenced></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>Z</mi><mn>2</mn></msup></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>Z</mi><msup><mfenced><mrow><msup><mi>Z</mi><mn>2</mn></msup><mo>+</mo><msup><mi>R</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b79c2dee-735c-42f3-95fa-b9a128040b74-asasaa.PNG" style="width: 200px; height: 151px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>R</mi></msubsup><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mi>&#963;</mi><mo>&#215;</mo><mn>2</mn><mi>&#960;</mi><mi>x</mi><mfenced><mrow><mi mathvariant="normal">d</mi><mi>x</mi></mrow></mfenced><mo>&#215;</mo><mi>x</mi></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>Z</mi><mn>2</mn></msup></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></msup></mfrac><mo>=</mo><mfrac><mi>&#963;</mi><mrow><mn>2</mn><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>Z</mi><msup><mfenced><mrow><msup><mi>Z</mi><mn>2</mn></msup><mo>+</mo><msup><mi>R</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac></mrow></mfenced></math></p>

</details>

---

### Q50. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>What will be the magnitude of the electric field at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> as shown in the figure? Each side of the figure is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> and perpendicular to the other?</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ad7f6d02-c6ce-4ab8-ad50-1d0446085c7f-image.png" style="width: 229px; height: 212px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mi>q</mi><msup><mi>l</mi><mn>2</mn></msup></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mi>q</mi><mfenced><mrow><mn>2</mn><msup><mi>l</mi><mn>2</mn></msup></mrow></mfenced></mfrac><mo>(</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>q</mi><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mo>(</mo><mn>2</mn><mi>l</mi><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mrow><mn>2</mn><mi>q</mi></mrow><mrow><mn>2</mn><msup><mi>l</mi><mn>2</mn></msup></mrow></mfrac><mo>(</mo><msqrt><mn>2</mn></msqrt><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mi>q</mi><mfenced><mrow><mn>2</mn><msup><mi>l</mi><mn>2</mn></msup></mrow></mfenced></mfrac><mo>(</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn><mo>)</mo></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><msup><mi>l</mi><mn>2</mn></msup></mfrac><mo>=</mo><msub><mi>E</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>3</mn></msub><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mrow><mo>(</mo><msqrt><mn>2</mn></msqrt><mi>&#8467;</mi><mi>l</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mrow><mn>2</mn><msup><mi>l</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><mi>k</mi><mi>q</mi></mrow><msup><mi>l</mi><mn>2</mn></msup></mfrac><mo>-</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mrow><mn>2</mn><msup><mi>l</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mrow><mn>2</mn><msup><mi>l</mi><mn>2</mn></msup></mrow></mfrac><mo>(</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn><mo>)</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7c87f7cf-e940-4e19-baea-3944ccc8649d-image.png" style="width: 231px; height: 218px;" /></p>

</details>

---

### Q51. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>A simple pendulum of mass &#39; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> &#39;, length &#39; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> &#39; and charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#39;</mo><mo>+</mo><msup><mi>q</mi><mo>&#39;</mo></msup></math> suspended in the electric field produced by two conducting parallel plates as shown. The value of deflection of pendulum in equilibrium position will be</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8aff2437-ae0f-4f7e-9dd2-af935aecdb6e-image.png" style="width: 325px; height: 247px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced open="[" close="]"><mrow><mfrac><mi mathvariant="normal">q</mi><mi>mg</mi></mfrac><mo>&#215;</mo><mfrac><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mfenced><mrow><msub><mrow><mo>&#160;</mo><mi mathvariant="normal">V</mi></mrow><mn>2</mn></msub><mo>-</mo><msub><mi mathvariant="normal">V</mi><mn>1</mn></msub></mrow></mfenced></mrow><mrow><mfenced><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub></mrow></mfenced><mo>(</mo><mi mathvariant="normal">d</mi><mo>-</mo><mi mathvariant="normal">t</mi><mo>)</mo></mrow></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced open="[" close="]"><mrow><mfrac><mi mathvariant="normal">q</mi><mi>mg</mi></mfrac><mo>&#215;</mo><mfrac><mrow><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><mfenced><mrow><msub><mrow><mo>&#160;</mo><mi mathvariant="normal">V</mi></mrow><mn>2</mn></msub><mo>-</mo><msub><mi mathvariant="normal">V</mi><mn>1</mn></msub></mrow></mfenced></mrow><mrow><mfenced><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub></mrow></mfenced><mo>(</mo><mi mathvariant="normal">d</mi><mo>-</mo><mi mathvariant="normal">t</mi><mo>)</mo></mrow></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced open="[" close="]"><mrow><mfrac><mi mathvariant="normal">q</mi><mi>mg</mi></mfrac><mo>&#215;</mo><mfrac><mrow><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><mfenced><mrow><msub><mrow><mo>&#160;</mo><mi mathvariant="normal">V</mi></mrow><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mrow></mfenced></mrow><mrow><mfenced><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub></mrow></mfenced><mo>(</mo><mi mathvariant="normal">d</mi><mo>-</mo><mi mathvariant="normal">t</mi><mo>)</mo></mrow></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced open="[" close="]"><mrow><mfrac><mi mathvariant="normal">q</mi><mi>mg</mi></mfrac><mo>&#215;</mo><mfrac><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mfenced><mrow><msub><mrow><mo>&#160;</mo><mi mathvariant="normal">V</mi></mrow><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mrow></mfenced></mrow><mrow><mfenced><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub></mrow></mfenced><mo>(</mo><mi mathvariant="normal">d</mi><mo>-</mo><mi mathvariant="normal">t</mi><mo>)</mo></mrow></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced open="[" close="]"><mrow><mfrac><mi mathvariant="normal">q</mi><mi>mg</mi></mfrac><mo>&#215;</mo><mfrac><mrow><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><mfenced><mrow><msub><mrow><mo>&#160;</mo><mi mathvariant="normal">V</mi></mrow><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mrow></mfenced></mrow><mrow><mfenced><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub></mrow></mfenced><mo>(</mo><mi mathvariant="normal">d</mi><mo>-</mo><mi mathvariant="normal">t</mi><mo>)</mo></mrow></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p><img height="258" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e03f3c08-908f-40d8-aaa2-89de6202a00b-image.png" width="317" /></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">E</mi></math> be electric field in air</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Tsin&theta;</mi><mo>=</mo><mi>qE</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Tcos&theta;</mi><mo>=</mo><mi>mg</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan&theta;</mi><mo>=</mo><mfrac><mi>qE</mi><mi>mg</mi></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a9acf2bf-4f63-4388-9f87-2b4ae6389bf5-image.png" style="width: 329px; height: 128px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Q</mi><mo>=</mo><mfenced close="]" open="["><mfrac><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub></mrow><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub></mrow></mfrac></mfenced><mfenced close="]" open="["><mrow><msub><mi mathvariant="normal">V</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">E</mi><mo>=</mo><mfrac><mi mathvariant="normal">Q</mi><mrow><mi mathvariant="normal">A</mi><msub><mi>Ïµ</mi><mi mathvariant="normal">o</mi></msub></mrow></mfrac><mo>=</mo><mfenced close="]" open="["><mfrac><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub></mrow><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub></mrow></mfrac></mfenced><mfrac><mfenced close="]" open="["><mrow><msub><mi mathvariant="normal">V</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mrow></mfenced><mrow><mi mathvariant="normal">A</mi><msub><mi>Ïµ</mi><mi mathvariant="normal">o</mi></msub></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><msub><mi>Ïµ</mi><mn>0</mn></msub><mo> </mo><mi mathvariant="normal">A</mi></mrow><mrow><mo> </mo><mi mathvariant="normal">d</mi><mo>-</mo><mi mathvariant="normal">t</mi></mrow></mfrac><mo>&rArr;</mo><mi mathvariant="normal">E</mi><mo>=</mo><mfrac><mrow><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><mfenced close="]" open="["><mrow><msub><mrow><mo> </mo><mi mathvariant="normal">V</mi></mrow><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mrow></mfenced></mrow><mrow><mfenced><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub></mrow></mfenced><mo>(</mo><mi mathvariant="normal">d</mi><mo>-</mo><mi mathvariant="normal">t</mi><mo>)</mo></mrow></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&theta;</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="["><mfrac><mrow><mi mathvariant="normal">q</mi><mo>&middot;</mo><mi mathvariant="normal">E</mi></mrow><mi>mg</mi></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&theta;</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="["><mrow><mfrac><mi mathvariant="normal">q</mi><mi>mg</mi></mfrac><mo>&times;</mo><mfrac><mrow><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><mfenced><mrow><msub><mrow><mo> </mo><mi mathvariant="normal">V</mi></mrow><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mrow></mfenced></mrow><mrow><mfenced><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub></mrow></mfenced><mo>(</mo><mi mathvariant="normal">d</mi><mo>-</mo><mi mathvariant="normal">t</mi><mo>)</mo></mrow></mfrac></mrow></mfenced></math></p>

</details>

---

### Q52. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Given below are two statements
Statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> : An electric dipole is placed at the centre of a hollow sphere. The flux of electric field through the sphere is zero, but the electric field is not zero anywhere in the sphere.</p><p>Statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> : If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is the radius of a solid metallic sphere and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> be the total charge on it. The electric field at any point on the spherical surface of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mfenced><mrow><mo>&#60;</mo><mi>R</mi></mrow></mfenced></math> is zero but the electric flux passing through this closed spherical surface of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> is not</p><p>In the light of the above statements, choose the correct answer from the options given below:</p>

**Options:**

- **(A)** Both Statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> and Statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> are true
- **(B)** Statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> is false but Statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> is true
- **(C)** Statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> is true but Statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> is false
- **(D)** Both Statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> and Statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> are false

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> is true but Statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> is false**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/af0add14-9c8c-4776-a470-6024e306b9b1-image.png" style="width: 232px; height: 134px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8750;</mo><mover><mi>E</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mi mathvariant="normal">d</mi><mover><mi>s</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><msub><mi>q</mi><mi>in</mi></msub><msub><mi>&#949;</mi><mn>0</mn></msub></mfrac><mo>=</mo><mn>0</mn><mo>=</mo><mi>&#981;</mi></math></p><p>Flux of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>E</mi><mo>&#8594;</mo></mover></math> through sphere is zero.</p><p>But <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8750;</mo><mover><mi>E</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mi mathvariant="normal">d</mi><mover><mi>s</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mfenced open="{" close="}"><mrow><mover><mi>E</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mi mathvariant="normal">d</mi><mover><mi>s</mi><mo>&#8594;</mo></mover><mo>&#8800;</mo><mn>0</mn></mrow></mfenced></math> for small section <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">d</mi><mi>s</mi></math> only</p><p>Statement-<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a9e9c72b-d608-45a5-9e21-ca9d83e6c5b5-65827e2f-2535-4c84-a2b8-f34181216f16-image.png" style="width: 300px; height: 227px;" /></p><p>As change encloses within gaussian surface is equal to zero.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mo>&#8750;</mo><mover><mi>E</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mi mathvariant="normal">d</mi><mover><mi>s</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q53. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Find the electric field at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> (as shown in figure) on the perpendicular bisector of a uniformly charged thin wire of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> carrying a charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>. The distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> from the centre of the rod is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mi>L</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d03d9e7e-e2a9-4d6e-8e32-5f4e1fe1c13e-image.png" style="width: 197px; height: 154px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>Q</mi><mrow><mn>3</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>L</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>Q</mi><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>L</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi>Q</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>L</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>Q</mi><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>L</mi><mn>2</mn></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>Q</mi><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>L</mi><mn>2</mn></msup></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mrow><mi>k</mi><mi>&#955;</mi></mrow><mi>a</mi></mfrac><mfenced><mrow><mi>sin</mi><msub><mi>&#952;</mi><mn>1</mn></msub><mo>+</mo><mi>sin</mi><msub><mi>&#952;</mi><mn>2</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>&#215;</mo><mfrac><mi>Q</mi><mi>L</mi></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi>L</mi></mrow><mn>2</mn></mfrac></mfenced></mfrac><mo>&#215;</mo><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mi>L</mi><mo>/</mo><mn>2</mn></mrow><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi>L</mi></mrow><mn>2</mn></mfrac></mfrac><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>2</mn><mi>Q</mi></mrow><mrow><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><msup><mi>L</mi><mn>2</mn></msup></mrow></mfrac><mo>&#215;</mo><mfenced><mrow><mn>2</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mi>Q</mi><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mo>&#160;</mo><msup><mi>L</mi><mn>2</mn></msup></mrow></mfrac></math></p>

</details>

---

### Q54. JEE Main 2021 (25 Feb Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>Two small spheres each of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>mg</mi></math> are suspended from a point by threads <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> long. They are equally charged and repel each other to a distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>. The charge on each of the sphere is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mn>21</mn></mfrac><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">C</mi><mo>.</mo></math> The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> will be ___.[Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>]</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **20**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/70663520-9ee3-4670-b438-615d61286aa9-image.png" style="width: 157px; height: 122px;" />.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mi>m</mi><mi>g</mi><mo>=</mo><mn>10</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mo>&#215;</mo><mn>10</mn><mo>=</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#215;</mo><msup><mi>q</mi><mn>2</mn></msup></mrow><mrow><mn>0</mn><mo>.</mo><mn>04</mn></mrow></mfrac><mo>=</mo><mi>F</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>1</mn></mrow><msqrt><mn>0</mn><mo>.</mo><mn>24</mn></msqrt></mfrac><mo>=</mo><mfrac><mi>F</mi><mrow><mi>m</mi><mi>g</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>10</mn></msqrt></mrow><mrow><mn>3</mn><msqrt><msqrt><mn>24</mn></msqrt></msqrt></mrow></mfrac><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>95</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup><mo>=</mo><mfrac><mi>a</mi><mn>21</mn></mfrac><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>20</mn></math></p>

</details>

---

### Q55. JEE Main 2021 (25 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

The peak electric field produced by the radiation coming from the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math> bulb at a distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>10</mn></mfrac><msqrt><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><mi>c</mi></mrow><mi>&#960;</mi></mfrac><mo>&#160;</mo></msqrt><mi mathvariant="normal">V</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The efficiency of the bulb is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>%</mo></math> and it is a point source. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is,

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>c</mi><mi>&#949;</mi><mmultiscripts><mi>E</mi><mn>0</mn><mn>2</mn><mprescripts/><mn>0</mn><none/></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mrow><mn>4</mn><mi>&#960;</mi><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup></mrow></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#215;</mo><mi>c</mi><mo>&#215;</mo><mfrac><mn>1</mn><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mi>c</mi><mn>2</mn></msup></mrow></mfrac><mo>&#215;</mo><msubsup><mi>E</mi><mn>0</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>0</mn></msub><mo>=</mo><mfrac><mn>2</mn><mn>10</mn></mfrac><mo>&#215;</mo><msqrt><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><mi>c</mi></mrow><mi>&#960;</mi></mfrac></msqrt><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q56. JEE Main 2021 (24 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>A cube of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> has point charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi mathvariant="normal">Q</mi></math> located at each of its vertices except at the origin where the charge is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi mathvariant="normal">Q</mi><mo>.</mo></math> The electric field at the centre of cube is:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3c631e3a-b7c2-479c-aadc-893be153d234-image.png" style="width: 270px; height: 225px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mi>Q</mi></mrow><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mfenced><mrow><mover><mi>x</mi><mo>^</mo></mover><mo>+</mo><mover><mi>y</mi><mo>^</mo></mover><mo>+</mo><mover><mi>z</mi><mo>^</mo></mover></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>Q</mi><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mfenced><mrow><mover><mi>x</mi><mo>^</mo></mover><mo>+</mo><mover><mi>y</mi><mo>^</mo></mover><mo>+</mo><mover><mi>z</mi><mo>^</mo></mover></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>2</mn><mi>Q</mi></mrow><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mfenced><mrow><mover><mi>x</mi><mo>^</mo></mover><mo>+</mo><mover><mi>y</mi><mo>^</mo></mover><mo>+</mo><mover><mi>z</mi><mo>^</mo></mover></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>Q</mi></mrow><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mfenced><mrow><mover><mi>x</mi><mo>^</mo></mover><mo>+</mo><mover><mi>y</mi><mo>^</mo></mover><mo>+</mo><mover><mi>z</mi><mo>^</mo></mover></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>2</mn><mi>Q</mi></mrow><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mfenced><mrow><mover><mi>x</mi><mo>^</mo></mover><mo>+</mo><mover><mi>y</mi><mo>^</mo></mover><mo>+</mo><mover><mi>z</mi><mo>^</mo></mover></mrow></mfenced></math>**

**Detailed Solution:**

<p>We can replace <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>Q</mi></math> charge at origin by <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>Q</mi><mo>.</mo></math></p><p>Now due to <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>Q</mi></math> charge at every corner of cube. Electric field at center of cube is zero so now net electric field at center is only due to <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi mathvariant="normal">Q</mi></math> charge at origin.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>E</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi><mover><mi>r</mi><mo>&#8594;</mo></mover></mrow><msup><mi>r</mi><mn>3</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mfenced><mrow><mo>-</mo><mn>2</mn><mi>Q</mi></mrow></mfenced><mfrac><mi>a</mi><mn>2</mn></mfrac><mfenced><mrow><mover><mi>x</mi><mo>^</mo></mover><mo>+</mo><mover><mi>y</mi><mo>^</mo></mover><mo>+</mo><mover><mi>z</mi><mo>^</mo></mover></mrow></mfenced></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mfenced><mrow><mfrac><mi>a</mi><mn>2</mn></mfrac><msqrt><mn>3</mn></msqrt></mrow></mfenced><mn>3</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>E</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mi>Q</mi><mfenced><mrow><mover><mi>x</mi><mo>^</mo></mover><mo>+</mo><mover><mi>y</mi><mo>^</mo></mover><mo>+</mo><mover><mi>z</mi><mo>^</mo></mover></mrow></mfenced></mrow><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mi>&#960;</mi><msup><mi>a</mi><mn>2</mn></msup><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac></math></p>

</details>

---

### Q57. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Charges <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">Q</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">Q</mi><mn>2</mn></msub></math> are at points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math> of a right-angled triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>A</mi><mi>B</mi></math>. The resultant electric field at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">O</mi></math> is perpendicular to the hypotenuse, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">Q</mi><mn>1</mn></msub><mo>/</mo><msub><mi mathvariant="normal">Q</mi><mn>2</mn></msub></math> is proportional to:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f1f935f9-27e7-406e-96c9-361f1967da4e-image.png" style="width: 241px; height: 200px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msubsup><mi>x</mi><mn>1</mn><mn>3</mn></msubsup><msubsup><mi>x</mi><mn>2</mn><mn>3</mn></msubsup></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>x</mi><mn>2</mn></msub><msub><mi>x</mi><mn>1</mn></msub></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>x</mi><mn>1</mn></msub><msub><mi>x</mi><mn>2</mn></msub></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>x</mi><mn>1</mn></msub><msub><mi>x</mi><mn>2</mn></msub></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8a7e5d25-777c-416d-a490-0cba5a7e44da-image.png" style="width: 258px; height: 230px;" /></p><p>  Using triangle properties</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mtext>&#952;</mtext><mo>=</mo><mfrac><msub><mi>x</mi><mn>1</mn></msub><msub><mi>x</mi><mn>2</mn></msub></mfrac><mspace linebreak="newline"></mspace><mi>tan</mi><mtext>&#952;</mtext><mo>=</mo><mfrac><msub><mi>E</mi><mn>2</mn></msub><msub><mi>E</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>K</mi><msub><mi>Q</mi><mn>2</mn></msub><mo>/</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup></mrow><mrow><mi>K</mi><msub><mi>Q</mi><mn>1</mn></msub><mo>/</mo><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup></mrow></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mfrac><msub><mi>x</mi><mn>1</mn></msub><msub><mi>x</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>K</mi><msub><mi>Q</mi><mn>2</mn></msub><mo>/</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup></mrow><mrow><mi>K</mi><msub><mi>Q</mi><mn>1</mn></msub><mo>/</mo><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup></mrow></mfrac></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>Q</mi><mn>1</mn></msub><msub><mi>Q</mi><mn>2</mn></msub></mfrac><mo>=</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>x</mi><mn>1</mn></msub><msub><mi>x</mi><mn>2</mn></msub></mfrac></math></p>

</details>

---

### Q58. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Two charged thin infinite plane sheets of uniform charge density <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#963;</mi><mo>+</mo></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#963;</mi><mo>-</mo></msub></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><msub><mi>&#963;</mi><mo>+</mo></msub></mfenced><mo>&#62;</mo><mfenced close="|" open="|"><msub><mi>&#963;</mi><mo>&#8722;</mo></msub></mfenced></math>, intersect at the right angle. Which of the following best represents the electric field lines for the system:

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1b1bd33b-1b0e-4a78-b3b5-c7746ace34ff-image.png" style="width: 180px; height: 165px;" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/32178670-a2d5-40dc-8d44-47d53803b737-image.png" style="width: 200px; height: 196px;" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5099706c-723d-46ec-8cad-46868c10a10e-image.png" style="width: 200px; height: 198px;" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/54b31ea3-44e2-4f2d-b50d-f98381602207-image.png" style="width: 200px; height: 196px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5099706c-723d-46ec-8cad-46868c10a10e-image.png" style="width: 200px; height: 198px;" />**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ef906631-a383-4d25-a04e-da9e7d859f39-image.png" style="width: 380px; height: 484px;" /></p><p>The electric field intensity due to each uniformly charged infinite plane is uniform. The electric field intensity at points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">B</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">D</mi></math>  as shown in figure. Hence, the electric lines of forces are as given in below figure.</p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5099706c-723d-46ec-8cad-46868c10a10e-image.png" style="width: 200px; height: 198px;" />

</details>

---

### Q59. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Consider a sphere of radius <math><mi>R</mi></math> which carries a uniform charge density <math><mi>&#961;</mi></math> . If a sphere of radius <math><mfrac><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math> is carved out of it, as shown, the ratio <math><mfrac><mrow><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><msub><mrow><mi>E</mi></mrow><mrow><mi>A</mi></mrow></msub></mrow><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mrow><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><msub><mrow><mi>E</mi></mrow><mrow><mi>B</mi></mrow></msub></mrow><mo>&#8594;</mo></mover></mrow></mfenced></mrow></mfrac></math> of magnitude of electric field <math><mover accent="true"><mrow><msub><mrow><mi>E</mi></mrow><mrow><mi>A</mi></mrow></msub></mrow><mo>&#8594;</mo></mover></math> and <math><mover accent="true"><mrow><msub><mrow><mi>E</mi></mrow><mrow><mi>B</mi></mrow></msub></mrow><mo>&#8594;</mo></mover></math> , respectively, at points <math><mi>A</mi></math> and <math><mi>B</mi></math> due to the remaining portion is:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1d906c2f-f6dd-46d1-bacc-ff9bafefef21-image.png" style="width: 200px; height: 223px;" />

**Options:**

- **(A)** <math><mfrac><mrow><mn>21</mn></mrow><mrow><mn>34</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>18</mn></mrow><mrow><mn>34</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>17</mn></mrow><mrow><mn>54</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>18</mn></mrow><mrow><mn>54</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>18</mn></mrow><mrow><mn>34</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>E</mi><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>r</mi></mrow><mrow><mn>3</mn><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
<math><msub><mrow><mi>E</mi></mrow><mrow><mi>A</mi></mrow></msub><mo>=</mo><mfrac><mrow><mo>-</mo><mi>&#961;</mi><mi>R</mi></mrow><mrow><mn>2</mn><mfenced separators="|"><mrow><mn>3</mn><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfenced></mrow></mfrac></math>
<math><mfenced close="|" open="|" separators="|"><mrow><msub><mrow><mi>E</mi></mrow><mrow><mi>A</mi></mrow></msub></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>R</mi></mrow><mrow><mn>6</mn><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
Electric filed at point <math><mi>B</mi><mo>=</mo><msub><mrow><mi>E</mi></mrow><mrow><mi>B</mi></mrow></msub><mo>=</mo><msub><mrow><mi>E</mi></mrow><mrow><mn>1</mn><mi>A</mi></mrow></msub><mo>+</mo><msub><mrow><mi>E</mi></mrow><mrow><mn>2</mn><mi>A</mi></mrow></msub></math>
<math><msub><mrow><mi>E</mi></mrow><mrow><mn>1</mn><mi>A</mi></mrow></msub><mo>=</mo></math> Electric Filed Due to solid sphere of radius R at point <math><mi>B</mi><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>R</mi></mrow><mrow><mn>3</mn><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
<math><msub><mrow><mi>E</mi></mrow><mrow><mn>2</mn><mi>A</mi></mrow></msub><mo>=</mo></math> Electric Filed Due to solid sphere of radius <math><mfrac><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math> (which having charge density <math><mo>&#8211;</mo><mi>&#961;</mi></math> ) at point B
<math><mo>=</mo><mo>-</mo><mfrac><mrow><mi>K</mi><msup><mrow><mi>Q</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mo>&#215;</mo><mn>4</mn></mrow><mrow><mn>9</mn><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><mi>&#961;</mi><mi>R</mi></mrow><mrow><mn>54</mn><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
<math><msub><mrow><mi>E</mi></mrow><mrow><mi>B</mi></mrow></msub><mo>=</mo><msub><mrow><mi>E</mi></mrow><mrow><mn>1</mn><mi>A</mi></mrow></msub><mo>+</mo><msub><mrow><mi>E</mi></mrow><mrow><mn>2</mn><mi>A</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>R</mi></mrow><mrow><mn>3</mn><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>&#961;</mi><mi>R</mi></mrow><mrow><mn>54</mn><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>17</mn><mi>&#961;</mi><mi>R</mi></mrow><mrow><mn>54</mn><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
<math><mfrac><mrow><mfenced close="|" open="|" separators="|"><mrow><msub><mrow><mi>E</mi></mrow><mrow><mi>A</mi></mrow></msub></mrow></mfenced></mrow><mrow><mfenced close="|" open="|" separators="|"><mrow><msub><mrow><mi>E</mi></mrow><mrow><mi>B</mi></mrow></msub></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>17</mn></mrow></mfrac><mi></mi></math>

</details>

---

### Q60. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Three charged particles <math><mtext>A</mtext><mo>, </mo><mtext></mtext><mtext>B</mtext></math> and <math><mtext>C</mtext></math> with charges <math><mo>-</mo><mn>4</mn><mi>q</mi><mo>,</mo><mi></mi><mn>2</mn><mi>q</mi></math> and <math><mo>-</mo><mn>2</mn><mi>q</mi></math> are present on the circumference of a circle of radius <math><mi>d</mi><mo>.</mo></math> The charged particles <math><mtext>A</mtext><mo>,</mo><mtext></mtext><mtext>C</mtext></math> and centre <math><mtext>O</mtext></math> of the circle formed an equilateral triangle as shown in the figure. The electric field at the point <math><mtext>O</mtext></math> is



<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/599323Q.PNG" style="width: 190px; height: 190px;" />

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi>q</mi></mrow><mrow><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>d</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt><mi>q</mi></mrow><mrow><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>d</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi>q</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>d</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mi>q</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>d</mi><mn>2</mn></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi>q</mi></mrow><mrow><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>d</mi><mn>2</mn></msup></mrow></mfrac></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d37215b6-bb7a-4d56-a4ab-a3d6fe6b4704.jpeg" />
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>4</mn><mi>k</mi><mi>q</mi></mrow><msup><mi>d</mi><mn>2</mn></msup></mfrac><mo>&#215;</mo><mn>2</mn><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>30</mn><mo>&#176;</mo><mo>=</mo><mfrac><mrow><mi>q</mi><msqrt><mn>3</mn></msqrt></mrow><mrow><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>d</mi><mn>2</mn></msup></mrow></mfrac></math>

</details>

---

### Q61. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A particle of mass <math><mi>m</mi></math> and charge <math><mi>q</mi></math> has an initial velocity <math><mover accent="true"><mrow><mi>v</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><msub><mrow><mi>v</mi></mrow><mrow><mn>0</mn></mrow></msub><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></math> . If an electric field <math><mover accent="true"><mrow><mi>E</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><msub><mrow><mi>E</mi></mrow><mrow><mn>0</mn></mrow></msub><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover></math> and magnetic field <math><mover accent="true"><mrow><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><msub><mrow><mi>B</mi></mrow><mrow><mn>0</mn></mrow></msub><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover></math> act on the particle, its speed will double after a time

**Options:**

- **(A)** <math><mfrac><mrow><mn>2</mn><mi>m</mi><msub><mrow><mi>v</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi>q</mi><msub><mrow><mi>E</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>3</mn><mi>m</mi><msub><mrow><mi>v</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi>q</mi><msub><mrow><mi>E</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><msqrt><mn>3</mn></msqrt><mtext>m</mtext><msub><mrow><mi>v</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msub><mrow><mtext>qE</mtext></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><msqrt><mn>2</mn></msqrt><mtext>m</mtext><msub><mrow><mi>v</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msub><mrow><mtext>qE</mtext></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><msqrt><mn>3</mn></msqrt><mtext>m</mtext><msub><mrow><mi>v</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msub><mrow><mtext>qE</mtext></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>**

**Detailed Solution:**

<p>Acceleration produced by electric field,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mrow><mi>q</mi><msub><mi>E</mi><mn>0</mn></msub></mrow><mi>m</mi></mfrac><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></math></p><p>After time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>, velocity of the particle,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mi>u</mi><mo>+</mo><mi>a</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>v</mi><mo>=</mo><msub><mi>v</mi><mn>0</mn></msub><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mfrac><mrow><mi>q</mi><msub><mi>E</mi><mn>0</mn></msub><mi>t</mi></mrow><mi>m</mi></mfrac></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><mi>u</mi><mo>=</mo><mi>v</mi><mo>=</mo><msub><mi>v</mi><mn>0</mn></msub><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>So, speed of the particle,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>v</mi></mfenced><mo>=</mo><msqrt><msubsup><mi>v</mi><mn>0</mn><mn>2</mn></msubsup><mo>+</mo><msup><mfenced><mfrac><mrow><mi>q</mi><msub><mi>E</mi><mn>0</mn></msub><mi>t</mi></mrow><mi>m</mi></mfrac></mfenced><mn>2</mn></msup></msqrt></math></p><p>Now, given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>v</mi></mfenced><mo>=</mo><mn>2</mn><msub><mi>v</mi><mn>0</mn></msub></math>after time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>, so
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>v</mi><mn>0</mn></msub><mo>=</mo><msqrt><msubsup><mi>v</mi><mn>0</mn><mn>2</mn></msubsup><mo>+</mo><msup><mfenced><mfrac><mrow><mi>q</mi><msub><mi>E</mi><mn>0</mn></msub><mi>t</mi></mrow><mi>m</mi></mfrac></mfenced><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>4</mn><msubsup><mi>v</mi><mn>0</mn><mn>2</mn></msubsup><mo>=</mo><msubsup><mi>v</mi><mn>0</mn><mn>2</mn></msubsup><mo>+</mo><msup><mfenced><mfrac><mrow><mi>q</mi><msub><mi>E</mi><mn>0</mn></msub><mi>t</mi></mrow><mi>m</mi></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>3</mn><msubsup><mi>v</mi><mn>0</mn><mn>2</mn></msubsup><mo>=</mo><msup><mfenced><mfrac><mrow><mi>q</mi><msub><mi>E</mi><mn>0</mn></msub><mi>t</mi></mrow><mi>m</mi></mfrac></mfenced><mn>2</mn></msup></math></p><p>So, time interval, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi>m</mi><msub><mi>v</mi><mn>0</mn></msub></mrow><mrow><mi>q</mi><msub><mi>E</mi><mn>0</mn></msub></mrow></mfrac></math></p><p>Here, we must note that no change in magnitude of velocity is caused by a perpendicular magnetic field. So, we are not taking effect of magnetic field while calculating change in speed.</p>

</details>

---

### Q62. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two infinite planes each with uniform surface charge density <math><mo>+</mo><mi>&#963;</mi></math> are kept in such a way that the angle between them is <math><msup><mrow><mn>30</mn></mrow><mrow><mi>o</mi></mrow></msup></math> . The electric field in the region shown between them is given by:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/599409.JPG" style="width: 280px; height: 92px;" />

**Options:**

- **(A)** <math><mfrac><mrow><mi>σ</mi></mrow><mrow><mn>2</mn><msub><mrow><mo>∈</mo></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mover accent="true"><mrow><mi>y</mi></mrow><mo>^</mo></mover><mo>-</mo><mfrac><mrow><mover accent="true"><mrow><mi>x</mi></mrow><mo>^</mo></mover></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
- **(B)** <math><mfrac><mrow><mi>σ</mi></mrow><mrow><msub><mrow><mo>∈</mo></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mover accent="true"><mrow><mi>y</mi></mrow><mo>^</mo></mover><mo>+</mo><mfrac><mrow><mover accent="true"><mrow><mi>x</mi></mrow><mo>^</mo></mover></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
- **(C)** <math><mfrac><mrow><mi>σ</mi></mrow><mrow><mn>2</mn><msub><mrow><mo>∈</mo></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mover accent="true"><mrow><mi>y</mi></mrow><mo>^</mo></mover><mo>+</mo><mfrac><mrow><mover accent="true"><mrow><mi>x</mi></mrow><mo>^</mo></mover></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
- **(D)** <math><mfrac><mrow><mi>σ</mi></mrow><mrow><mn>2</mn><msub><mrow><mo>∈</mo></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mover accent="true"><mrow><mi>y</mi></mrow><mo>^</mo></mover><mo>-</mo><mfrac><mrow><mover accent="true"><mrow><mi>x</mi></mrow><mo>^</mo></mover></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mi>σ</mi></mrow><mrow><mn>2</mn><msub><mrow><mo>∈</mo></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mover accent="true"><mrow><mi>y</mi></mrow><mo>^</mo></mover><mo>-</mo><mfrac><mrow><mover accent="true"><mrow><mi>x</mi></mrow><mo>^</mo></mover></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/35bbc9c8-4014-42ab-bc9c-097829b8f80f.png" />
<math><mover accent="true"><mrow><mi>E</mi></mrow><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mi>σ</mi></mrow><mrow><mn>2</mn><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><msup><mrow><mn>60</mn></mrow><mrow><mi mathvariant="normal">o</mi></mrow></msup></mrow></mrow><mfenced separators="|"><mrow><mo>-</mo><mover accent="true"><mrow><mi>x</mi></mrow><mn>^</mn></mover></mrow></mfenced><mo>+</mo><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>σ</mi></mrow><mrow><mn>2</mn><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>σ</mi></mrow><mrow><mn>2</mn><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><msup><mrow><mn>60</mn></mrow><mrow><mi mathvariant="normal">o</mi></mrow></msup></mrow></mrow></mrow></mfenced><mfenced separators="|"><mrow><mover accent="true"><mrow><mi>y</mi></mrow><mo>^</mo></mover></mrow></mfenced></math>
<math><mover accent="true"><mrow><mi>E</mi></mrow><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mi>σ</mi></mrow><mrow><mn>2</mn><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mover accent="true"><mrow><mi>y</mi></mrow><mo>^</mo></mover><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mover accent="true"><mrow><mi>x</mi></mrow><mn>^</mn></mover></mrow></mfenced></math>

</details>

---

### Q63. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A simple pendulum of length <math><mi mathvariant="normal">L</mi></math> is placed between the plates of a parallel plate capacitor having electric field <math><mi>&#160;</mi><mi mathvariant="normal">E</mi></math> , as shown in figure. Its bob has mass <math><mi mathvariant="normal">m</mi></math> and charge <math><mi>&#160;</mi><mi mathvariant="normal">q</mi></math> . The time period of the pendulum is given by:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9e802a89-29db-4258-aa54-0ca57db6e5c6-image.png" style="width: 300px; height: 285px;" />

**Options:**

- **(A)** <math><mn>2</mn><mi mathvariant="normal">π</mi><msqrt><mfrac><mrow><mi mathvariant="normal">L</mi></mrow><mrow><msqrt><msup><mrow><mi mathvariant="normal">g</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">q</mi><mi mathvariant="normal">E</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></msqrt></math>
- **(B)** <math><mn>2</mn><mi mathvariant="normal">π</mi><msqrt><mfrac><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">g</mi><mo>+</mo><mfrac><mrow><mi mathvariant="normal">q</mi><mi mathvariant="normal">E</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow></mfrac><mi mathvariant="normal"> </mi></mrow></mfenced></mrow></mfrac></msqrt></math>
- **(C)** <math><mn>2</mn><mi mathvariant="normal">π</mi><msqrt><mfrac><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">g</mi><mo>-</mo><mfrac><mrow><mi mathvariant="normal">q</mi><mi mathvariant="normal">E</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow></mfrac><mi mathvariant="normal"> </mi></mrow></mfenced></mrow></mfrac></msqrt></math>
- **(D)** <math><mn>2</mn><mi mathvariant="normal">π</mi><msqrt><mfrac><mrow><mi mathvariant="normal">L</mi></mrow><mrow><msqrt><msup><mrow><mi mathvariant="normal">g</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi mathvariant="normal">m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></msqrt></mrow></mfrac></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>2</mn><mi mathvariant="normal">π</mi><msqrt><mfrac><mrow><mi mathvariant="normal">L</mi></mrow><mrow><msqrt><msup><mrow><mi mathvariant="normal">g</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">q</mi><mi mathvariant="normal">E</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></msqrt></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5e0fb379-c363-43f5-b6cb-5a89eb6f3c3c-image.png" style="width: 200px; height: 268px;" />
Two forces will be acting on the mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math>, gravity force and force by the electric field.</p><p>Thus, the effective force <math><mo>=</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#160;</mi><msqrt><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">q</mi><mi mathvariant="normal">E</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">m</mi><mi mathvariant="normal">g</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math>
From force equation, <math><msub><mrow><mi mathvariant="normal">g</mi></mrow><mrow><mi mathvariant="normal">e</mi><mi mathvariant="normal">f</mi><mi mathvariant="normal">f</mi></mrow></msub><mo>=</mo><msqrt><msup><mrow><mi mathvariant="normal">g</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">q</mi><mi mathvariant="normal">E</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math>
Time period of the pendulum is <math><mfenced separators="|"><mrow><mi mathvariant="normal">T</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><msqrt><mfrac><mrow><mi mathvariant="normal">L</mi></mrow><mrow><msub><mrow><mi mathvariant="normal">g</mi></mrow><mrow><mi mathvariant="normal">e</mi><mi mathvariant="normal">f</mi><mi mathvariant="normal">f</mi></mrow></msub></mrow></mfrac></msqrt></math>
<math><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">&#160;</mi><msqrt><mfrac><mrow><mi mathvariant="normal">L</mi></mrow><mrow><msqrt><msup><mrow><mi mathvariant="normal">g</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">q</mi><mi mathvariant="normal">E</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></msqrt></math></p>

</details>

---

### Q64. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Four point charges <math><mo>-</mo><mi mathvariant="normal">q</mi><mo>,</mo><mi mathvariant="normal">&#160;</mi><mo>+</mo><mi mathvariant="normal">q</mi><mo>,</mo><mi mathvariant="normal">&#160;</mi><mo>+</mo><mi mathvariant="normal">q</mi></math> and <math><mo>-</mo><mi mathvariant="normal">q</mi></math> are placed on y-axis at <math><mi mathvariant="normal">y</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi mathvariant="normal">d</mi><mo>,</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">y</mi><mo>=</mo><mo>-</mo><mi mathvariant="normal">d</mi><mo>,</mo></math> and <math><mi mathvariant="normal">y</mi><mo>=</mo><mo>+</mo><mn>2</mn><mi mathvariant="normal">d</mi><mo>,</mo></math> respectively. The magnitude of the electric field <math><mi mathvariant="normal">E</mi></math> at a point on the x-axis at <math><mi mathvariant="normal">x</mi><mo>=</mo><mi mathvariant="normal">D</mi><mo>,</mo></math> with <math><mi mathvariant="normal">D</mi><mo>&#8811;</mo><mi mathvariant="normal">d</mi><mo>,</mo></math> will behave as:

**Options:**

- **(A)** <math><mi mathvariant="normal">E</mi><mo>∝</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfrac></math>
- **(B)** <math><mi mathvariant="normal">E</mi><mo>∝</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">D</mi></mrow></mfrac></math>
- **(C)** <math><mi mathvariant="normal">E</mi><mo>∝</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></math>
- **(D)** <math><mi mathvariant="normal">E</mi><mo>∝</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mi mathvariant="normal">E</mi><mo>∝</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfrac></math>**

**Detailed Solution:**

The electric field at <math><mi mathvariant="normal">P</mi></math> is superposition of the fields due to all four charges. The electric field due to the two <math><mo>+</mo><mi mathvariant="normal">q</mi></math> charges is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0f02fbe5-dd0c-40bb-89a9-e49c9fe96117-image9.png" />
<math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mo>+</mo><mi mathvariant="normal">q</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi mathvariant="normal">K</mi><mi mathvariant="normal">q</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><msub><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></mrow><mrow><mn>1</mn></mrow></msub><mo>&#215;</mo><mn>2</mn></math>
<math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mo>-</mo><mi mathvariant="normal">q</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi mathvariant="normal">K</mi><mi mathvariant="normal">q</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>4</mn><msup><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><msub><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></mrow><mrow><mn>2</mn></mrow></msub><mo>&#215;</mo><mn>2</mn></math>
The field due to <math><mo>+</mo><mi mathvariant="normal">q</mi></math> is towards right and the field due to <math><mo>-</mo><mi mathvariant="normal">q</mi></math> is towards left. Also <math><msub><mrow><mi mathvariant="normal">&#952;</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>&#8776;</mo><mn>0</mn></math> and <math><msub><mrow><mi mathvariant="normal">&#952;</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>&#8776;</mo><mn>0</mn></math> .
<math><mo>&#8756;</mo><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mi mathvariant="normal">n</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">t</mi></mrow></msub><mo>=</mo><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mo>+</mo><mi mathvariant="normal">q</mi></mrow></msub><mo>-</mo><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mo>-</mo><mi mathvariant="normal">q</mi></mrow></msub><mo>&#8776;</mo><mfrac><mrow><mi mathvariant="normal">K</mi><mi mathvariant="normal">q</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mi mathvariant="normal">K</mi><mi mathvariant="normal">q</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>4</mn><msup><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi mathvariant="normal">K</mi><mi mathvariant="normal">q</mi><mo>&#160;</mo><mn>3</mn><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup></mrow><mrow><mfenced separators="|"><mrow><msup><mi mathvariant="normal">D</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup></mrow></mfenced><mfenced separators="|"><mrow><msup><mi mathvariant="normal">D</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac><mo>&#8776;</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">K</mi><mi mathvariant="normal">q</mi><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup></mrow><msup><mi mathvariant="normal">D</mi><mn>4</mn></msup></mfrac></math>
<math><mi mathvariant="normal">E</mi><mo>&#8733;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfrac></math>

</details>

---

### Q65. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A positive point charge is released from rest at a distance <math><msub><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>0</mn></mrow></msub></math> from a positive line charge with uniform charge density. The speed <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">v</mi><mo>)</mo></math> of the point charge, as a function of instantaneous distance <math><mi mathvariant="normal">r</mi></math> from line charge, is proportional to
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/371a8355-0349-47ba-ae1f-9b99f2c4782b-image.png" style="width: 160px; height: 189px;" />

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">v</mi><mo>&#x221D;</mo><mfenced separators="|"><mfrac><mi mathvariant="normal">r</mi><msub><mi mathvariant="normal">r</mi><mn>0</mn></msub></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">v</mi><mo>&#8733;</mo><msqrt><mi>ln</mi><mo>&#8289;</mo><mfenced separators="|"><mfrac><mi mathvariant="normal">r</mi><msub><mi mathvariant="normal">r</mi><mn>0</mn></msub></mfrac></mfenced></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">v</mi><mo>&#x221D;</mo><mi>ln</mi><mo>&#x2061;</mo><mfenced separators="|"><mfrac><mi mathvariant="normal">r</mi><msub><mi mathvariant="normal">r</mi><mn>0</mn></msub></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">v</mi><mo>&#x221D;</mo><msup><mi mathvariant="normal">e</mi><mfrac bevelled="true"><mrow><mo>+</mo><mi mathvariant="normal">r</mi></mrow><msub><mi mathvariant="normal">r</mi><mn>0</mn></msub></mfrac></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">v</mi><mo>&#8733;</mo><msqrt><mi>ln</mi><mo>&#8289;</mo><mfenced separators="|"><mfrac><mi mathvariant="normal">r</mi><msub><mi mathvariant="normal">r</mi><mn>0</mn></msub></mfrac></mfenced></msqrt></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>mv</mi><mn>2</mn></msup><mo>=</mo><mi mathvariant="normal">q</mi><mo>&#8710;</mo><mi mathvariant="normal">V</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>mv</mi><mn>2</mn></msup><mo>=</mo><mi mathvariant="normal">q</mi><mo>&#215;</mo><mfrac><mi mathvariant="normal">&#955;</mi><mrow><mn>2</mn><msub><mi>&#960;&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced separators="|"><mrow><mi>ln</mi><mo>&#8289;</mo><mfenced separators="|"><mfrac><mi mathvariant="normal">r</mi><msub><mi mathvariant="normal">r</mi><mn>0</mn></msub></mfrac></mfenced></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">v</mi><mn>2</mn></msup><mo>=</mo><mfrac><mi>q&#955;</mi><msub><mi>m&#960;&#949;</mi><mn>0</mn></msub></mfrac><mfenced separators="|"><mrow><mi>ln</mi><mo>&#8289;</mo><mfenced separators="|"><mfrac><mi mathvariant="normal">r</mi><msub><mi mathvariant="normal">r</mi><mn>0</mn></msub></mfrac></mfenced></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">v</mi><mo>=</mo><msqrt><mfrac><mi>q&#955;</mi><msub><mi>m&#960;&#949;</mi><mn>0</mn></msub></mfrac><mfenced separators="|"><mrow><mi>ln</mi><mo>&#8289;</mo><mfenced separators="|"><mfrac><mi mathvariant="normal">r</mi><msub><mi mathvariant="normal">r</mi><mn>0</mn></msub></mfrac></mfenced></mrow></mfenced></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">v</mi><mo>&#8733;</mo><msqrt><mi>ln</mi><mo>&#8289;</mo><mfenced separators="|"><mfrac><mi mathvariant="normal">r</mi><msub><mi mathvariant="normal">r</mi><mn>0</mn></msub></mfrac></mfenced></msqrt></math></p><p> </p>

</details>

---

### Q66. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The bob of a simple pendulum has mass <math><mn>2</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">g</mi></math> and a charge of <math><mn>5.0</mn><mi>&#160;</mi><mi mathvariant="normal">&#956;</mi><mi mathvariant="normal">C</mi><mo>.</mo></math> It is at rest in a uniform horizontal electric field of intensity <math><mn>2000</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">V</mi><mo>/</mo><mi mathvariant="normal">m</mi></math> At equilibrium, the angle that the pendulum makes with the vertical is:
<math><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">k</mi><mi mathvariant="normal">e</mi><mo>&#8201;</mo><mi mathvariant="normal">g</mi><mo>=</mo><mn>10</mn><mi>&#160;</mi><mi mathvariant="normal">m</mi><mo>/</mo><msup><mrow><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math>

**Options:**

- **(A)** <math><mi> </mi><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>0.2</mn></mrow></mfenced></math>
- **(B)** <math><mi> </mi><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>2.0</mn></mrow></mfenced></math>
- **(C)** <math><mi> </mi><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>0.5</mn></mrow></mfenced></math>
- **(D)** <math><mi> </mi><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>5.0</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi> </mi><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>0.5</mn></mrow></mfenced></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/372b754a-7888-4928-ac9f-0c5b44e6939e-image.png" style="width: 280px; height: 211px;" />
<math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">Q</mi><mi mathvariant="normal">E</mi></mrow><mrow><mi mathvariant="normal">m</mi><mi mathvariant="normal">g</mi></mrow></mfrac></mrow></mrow><mo>=</mo><mfrac><mrow><mn>5</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>6</mn></mrow></msup><mo>&#215;</mo><mn>2000</mn></mrow><mrow><mn>2</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#215;</mo><mn>10</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><mo>&#8658;</mo><mi mathvariant="normal">&#952;</mi><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mn>0.5</mn></mrow></mfenced></mrow></mrow></math>

</details>

---

### Q67. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A parallel plate capacitor with plates of area <math><mn>1</mn><mi>&#160;</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></math> each, are at a separation of <math><mn>0.1</mn><mi>&#160;</mi><mi>m</mi><mo>.</mo></math> If the electric field between the plates is <math> <mrow> <mn>100</mn><mtext>&#8201;</mtext><mtext>&#8201;</mtext><mi>N</mi><mo>/</mo><mi>C</mi><mo>,</mo></mrow> </math> the magnitude of charge on each plate is: <math> <mrow> <mrow><mo>(</mo> <mrow> <mtext>Take</mtext><mtext>&#8201;</mtext><mtext>&#8201;</mtext><msub> <mo>&#8712;</mo> <mn>0</mn> </msub> <mo>=</mo><mn>8.85</mn><mo>&#215;</mo><msup> <mrow> <mn>10</mn></mrow> <mrow> <mo>&#8722;</mo><mn>12</mn></mrow> </msup> <mfrac> <mrow> <msup> <mi>C</mi> <mn>2</mn> </msup> </mrow> <mrow> <mi>N</mi><mtext>-</mtext><msup> <mi>m</mi> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> <mo>)</mo></mrow></mrow> </math>

**Options:**

- **(A)** <math><mn>8.85</mn><mo>x</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup><mi>C</mi></math>
- **(B)** <math><mn>6.85</mn><mo>x</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup><mi>C</mi></math>
- **(C)** <math><mn>9.85</mn><mo>x</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup><mi>C</mi></math>
- **(D)** <math><mn>7.85</mn><mo>x</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>8.85</mn><mo>x</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup><mi>C</mi></math>**

**Detailed Solution:**

<math><mi>E</mi><mo>=</mo><mfrac><mrow><mi>σ</mi></mrow><mrow><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>Q</mi></mrow><mrow><mi>A</mi><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mo>=</mo><mn>100</mn><mi> </mi><mrow><mrow><mi>V</mi></mrow><mo>/</mo><mrow><mi>m</mi></mrow></mrow></math>

<math><mi>Q</mi><mo>=</mo><mn>100</mn><mo>×</mo><mi>A</mi><mi> </mi><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub></math>

<math><mo>⇒</mo><mi>Q</mi><mo>=</mo><mn>100</mn><mo>×</mo><mn>1</mn><mo>×</mo><mn>8.85</mn><mo>×</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>12</mn></mrow></msup><mi>C</mi></math>

<math><mo>=</mo><mn>8.85</mn><mo>×</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup><mi>C</mi></math>

</details>

---

### Q68. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Two point charges <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>1</mn></msub><mfenced separators="|"><mrow><msqrt><mn>10</mn></msqrt><mi>&#160;</mi><mi>&#956;C</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>2</mn></msub><mfenced separators="|"><mrow><mo>-</mo><mn>25</mn><mi>&#160;</mi><mi>&#956;C</mi></mrow></mfenced></math> are placed on the <math><mi>x</mi></math> -axis at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mi>&#160;</mi><mi mathvariant="normal">m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn><mi>&#160;</mi><mi mathvariant="normal">m</mi></math> respectively. The electric field <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mtext>in</mtext><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">V</mi><mo>/</mo><mi mathvariant="normal">m</mi></mrow></mfenced></math> at a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>3</mn><mi>&#160;</mi><mi mathvariant="normal">m</mi></math> on <math><mi>y</mi></math>-axis is,

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mrow><mtext>Take</mtext><mo>&#160;</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub></mrow></mfrac><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mi>&#160;</mi><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mn>81</mn><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>81</mn><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>81</mn><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>81</mn><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mn>63</mn><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>27</mn><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>63</mn><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>27</mn><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>63</mn><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>27</mn><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup></math>**

**Detailed Solution:**

<blockquote><p>Electric field due to <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>10</mn></msqrt><mi>&#160;</mi><mi>&#956;C</mi></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/69ebea31-2c59-4a3d-9f72-d5aab22cc0f1-image.png" style="width: 320px; height: 239px;" />

<math><msub><mrow><mover accent="true"><mrow><mi>E</mi></mrow><mo>&#8594;</mo></mover></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mrow><mo>&#8712;</mo></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfrac><mrow><msqrt><mn>10</mn></msqrt><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>6</mn></mrow></msup></mrow><mrow><msubsup><mrow><mi>r</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></msubsup></mrow></mfrac><mi>&#160;</mi><msub><mrow><mover accent="true"><mrow><mi>r</mi></mrow><mo>&#8594;</mo></mover></mrow><mrow><mn>1</mn></mrow></msub></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub></mrow></mfrac><mfrac><mrow><msqrt><mn>10</mn></msqrt><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup></mrow><msup><mfenced separators="|"><msqrt><mn>10</mn></msqrt></mfenced><mn>3</mn></msup></mfrac><mfenced separators="|"><mrow><mo>-</mo><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced></math>

Similarly, electric field due to <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>25</mn><mi>&#160;</mi><mi>&#956;C</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover accent="true"><mi>E</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub></mrow></mfrac><mfrac><mrow><mn>25</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup></mrow><msup><mfenced separators="|"><mn>5</mn></mfenced><mn>3</mn></msup></mfrac><mfenced separators="|"><mrow><mn>4</mn><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced></math>

Net electric field, 
<math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi mathvariant="normal">E</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover></mrow><mn>10</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow><mn>10</mn></mfrac><mo>+</mo><mfrac><mn>4</mn><mn>5</mn></mfrac><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>7</mn><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover></mrow><mn>10</mn></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow><mn>10</mn></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mn>63</mn><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>27</mn><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup><mo>&#160;</mo><mfrac><mi mathvariant="normal">N</mi><mi mathvariant="normal">C</mi></mfrac></math></p></blockquote>

</details>

---

### Q69. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

For a uniformly charged ring of radius <math><mi>R</mi><mo>,</mo></math> the electric field on its axis has the largest magnitude at a distance <math><mi>h</mi></math> from its centre. Then value of <math><mi>h</mi></math> is:

**Options:**

- **(A)** <math><mfrac><mrow><mi>R</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>R</mi></mrow><mrow><msqrt><mn>5</mn></msqrt></mrow></mfrac></math>
- **(C)** <math><mi>R</mi><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math><mi>R</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mi>R</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/emuysnbttzbhzwdqwrybvgcovqwjdwbyeuuzobgvjcpuybamss.png" /> 

        Electric field at a distance  <math><mi>h</mi></math>  from centre on axis

         <math><mi>E</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi>π</mi><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfrac><mrow><mi>Q</mi><mi>h</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></mrow></mfrac></math> 

        To get maximum  <math><mi>E</mi><mo>,</mo><mtext> </mtext><mfrac><mrow><mi>d</mi><mi>E</mi></mrow><mrow><mi>d</mi><mi>h</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math> 

         <math><mn>0</mn><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi>π</mi><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfrac><mrow><mi>Q</mi><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup><mo>-</mo><mi>Q</mi><mi>h</mi><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup><mn>2</mn><mi>h</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></math> 

         <math><mo>⇒</mo><mi>h</mi><mo>=</mo><mo>±</mo><mfrac><mrow><mi>R</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>

</details>

---

### Q70. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `3`

[12]
A solid ball of radius $\mathrm{R}$ has a charge density $\rho$ given by $\rho=\rho_0\left(1-\frac{r}{R}\right)$ for $0 \leq r \leq R$. The electric field outside the ball is:

**Options:**

- **(A)** $\frac{\rho_0 R^3}{\varepsilon_0 r^2}$
- **(B)** $\frac{4 \rho_0 R^3}{3 \varepsilon_0 r^2}$
- **(C)** $\frac{3 \rho_0 R^3}{4 \varepsilon_0 r^2}$
- **(D)** $\frac{\rho_0 R^3}{12 \varepsilon_0 r^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\rho_0 R^3}{12 \varepsilon_0 r^2}$**

**Detailed Solution:**

Charge density, $\rho=\rho_0\left(1-\frac{r}{R}\right)$
$$
\begin{aligned}
&d q=\rho d v \\
&q_{\text {in }}=\int d q=\rho d v \\
&=\rho_0\left(1-\frac{r}{R}\right) 4 \pi r^2 d r \quad\left(\because d v=4 \pi \mathrm{r}^2 \mathrm{dr}\right) \\
&=4 \pi \rho_0 \int_0^R\left(1-\frac{r}{R}\right) r^2 d r \\
&=4 \pi \rho_0 \int_0^R r^2 d r-\frac{r^2}{R} d r \\
&=4 \pi \rho_0\left[\left[\frac{r^3}{3}\right]_0^R-\left[\frac{r^4}{4 R}\right]_0^R\right] \\
&=4 \pi \rho_0\left[\frac{R^3}{3}-\frac{R^4}{4 R}\right]
\end{aligned}
$$
$=4 \pi \rho_0\left[\frac{R^3}{3}-\frac{R^3}{4}\right]=4 \pi \rho_0\left[\frac{R^3}{12}\right]$
$q=\frac{\pi \rho_0 R^3}{3}$

$$
E .4 \pi r^2=\left(\frac{\pi \rho_0 R^3}{3 \epsilon_0}\right)
$$
$\therefore \quad$ Electric field outside the ball, $E=\frac{\rho_0 R^3}{12 \in_0 r^2}$

</details>

---

### Q71. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `3`

A body of mass $M$ and charge $q$ is connected to a spring of spring constant $k$. It is oscillating along $\mathrm{x}$-direction about its equilibrium position, taken to be at $x=0$, with an amplitude $A$. An electric field $E$ is applied along the $\mathrm{x}$-direction. Which of the following statements is correct?

**Options:**

- **(A)** The total energy of the system is
$$
\frac{1}{2} m \omega^2 A^2+\frac{1}{2} \frac{q^2 E^2}{k}
$$
- **(B)** The new equilibrium position is at a distance: $\frac{2 q E}{k}$ from $x=0$
- **(C)** The new equilibrium position is at a distance: $\frac{q E}{2 k}$ from $\mathrm{x}=0$
- **(D)** The total energy of the system is $\frac{1}{2} m \omega^2 A^2-\frac{1}{2} \frac{q^2 E^2}{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) The total energy of the system is
$$
\frac{1}{2} m \omega^2 A^2+\frac{1}{2} \frac{q^2 E^2}{k}
$$**

**Detailed Solution:**

Equilibrium position will shift to point where resultant force $=0$
$$
\mathrm{kx}_{\text {eq }}=\mathrm{qE} \Rightarrow \mathrm{x}_{\text {eq }}=\frac{\mathrm{qE}}{\mathrm{k}}
$$
Total energy $=\frac{1}{2} \mathrm{~m} \omega^2 \mathrm{~A}^2+\frac{1}{2} \mathrm{kx}_{\text {eq }}^2$
Total energy $=\frac{1}{2} m \omega^2 A^2+\frac{1}{2} \frac{q^2 E^2}{k}$

</details>

---

### Q72. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

A negative test charge is moving near a long straight wire carrying a current. The force acting on the test charge is parallel to the direction of the current. The motion of the charge is:

**Options:**

- **(A)** Away from the wire
- **(B)** Towards the wire
- **(C)** Parallel to the wire along the current
- **(D)** Parallel to the wire opposite to the current

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Towards the wire**

**Detailed Solution:**

<p>Force on a moving charge, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>F</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>q</mi><mfenced separators="|"><mrow><mover accent="true"><mi mathvariant="normal">v</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>B</mi><mo>&#8594;</mo></mover></mrow></mfenced></math>

Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>q</mi><mo>=</mo><mo>-</mo><mi>v</mi><mi>e</mi><mi>&#160;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover accent="true"><mi>F</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mi>q</mi><mfenced separators="|"><mrow><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>B</mi><mo>&#8594;</mo></mover></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mtext>motion&#160;of</mtext><mo>-</mo><mi mathvariant="normal">q</mi><mtext>&#160;is&#160;towards&#160;the&#160;wire.</mtext></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a8f94e4c-3cba-492f-8a8a-6d54c210333f-image.png" style="width: 141px; height: 160px;" /></p>

</details>

---

### Q73. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `3`

The region between two concentric spheres of radii &#39;a&#39; and &#39;b&#39;, respectively (see figure), has volume charge density <math><mi mathvariant="normal">&#961;</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mi mathvariant="normal">r</mi></mrow></mfrac></math> , where A is a constant and r is the distance from the centre. At the centre of the spheres is a point charge Q. The value of A such that the electric field in the region between the spheres will be constant, is:

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/135020_Diag.jpg" style="width: 200px; height: 193px;" />

**Options:**

- **(A)** <math><mfrac><mrow><mn>2</mn><mi mathvariant="normal">Q</mi></mrow><mrow><mi mathvariant="normal">π</mi><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi mathvariant="normal">b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>2</mn><mi mathvariant="normal">Q</mi></mrow><mrow><mi mathvariant="normal">π</mi><msup><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi mathvariant="normal">Q</mi></mrow><mrow><mn>2</mn><mi mathvariant="normal">π</mi><msup><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi mathvariant="normal">Q</mi></mrow><mrow><mn>2</mn><mi mathvariant="normal">π</mi><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mi mathvariant="normal">Q</mi></mrow><mrow><mn>2</mn><mi mathvariant="normal">π</mi><msup><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bikkkkggggggggg.JPG" style="width: 200px; height: 212px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mtext>E=E</mtext><mn>1</mn></msub><mo>+</mo><msub><mtext>E</mtext><mn>2</mn></msub></math></p><math><mi mathvariant="normal">&#8658;E</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">K</mi><mfenced close="]" open="[" separators="|"><mrow><mi mathvariant="normal">Q</mi><mo>+</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mi mathvariant="normal">r</mi></mrow></munderover><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi><mfrac><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></mfrac></mrow></mrow></mrow></mfenced></mrow><mrow><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

<math><mi mathvariant="normal">E</mi><mo>=</mo><mi mathvariant="normal">K</mi><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">Q</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mn>4</mn><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">A</mi><mfenced close="}" open="{" separators="|"><mrow><mfrac><mrow><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></mrow></mfenced></math>

<math><mfrac><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">E</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mfrac><mi>Q</mi><msup><mi>r</mi><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mrow><mn>8</mn><mi>&#960;</mi><mi>A</mi><msup><mi>a</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><msup><mi>r</mi><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mn>0</mn></math>

<math><mi mathvariant="normal">A</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">Q</mi></mrow><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi><msup><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

</details>

---

### Q74. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

A wire of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mn>20</mn><mi>&#160;</mi><mn>c</mn><mn>m</mn></math> is bent into a semi-circular arc and the two equal halves of the arc are uniformly charged with charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>Q</mi></math> as shown in the figure. The magnitude of the charge on each half is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mi>Q</mi></mfenced><mo>=</mo><msup><mn>10</mn><mn>3</mn></msup><msub><mi>&#949;</mi><mn>0</mn></msub></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#949;</mi><mn>0</mn></msub></math> is the permittivity of free the space. The net electric field at the centre <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> is

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b521b243-d9d9-44f2-a518-cbe0a25d5d6d-image.png" style="width: 350px; height: 141px;" />

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>25</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>50</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>25</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>50</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>25</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3bda223a-e611-4d14-906a-e95e77965795-image.png" style="width: 270px; height: 215px;" />

<math><mi>L</mi><mo>=</mo><mi>&#960;</mi><mi>R</mi></math>

<math> <mrow> <mo>&#8658;</mo><mi>R</mi><mo>=</mo><mfrac> <mi>L</mi> <mi>&#960;</mi> </mfrac> <mo>=</mo><mfrac> <mrow> <mn>20</mn></mrow> <mrow> <mn>100</mn><mi>&#960;</mi></mrow> </mfrac> <mtext>&#8201;</mtext><mtext>&#8201;</mtext><mtext>m</mtext><mo>=</mo><mfrac> <mn>1</mn> <mrow> <mn>5</mn><mi>&#960;</mi></mrow> </mfrac> <mo>&#160;</mo><mtext>&#8201;</mtext><mtext>m</mtext></mrow> </math>

<math><mo>&#8658;</mo></math> due to a charge arc, electric field at centre is given by

<math><mrow><mi>E</mi><mo>=</mo><mfrac> <mrow> <mn>2</mn><mi>K</mi><mi>&#955;</mi></mrow> <mi>R</mi> </mfrac> <mi>sin</mi><mfrac> <mi>&#952;</mi> <mn>2</mn> </mfrac> </mrow> </math>

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/06b1c364-efda-4e78-beea-ae1ba7c7531a-image.png" style="width: 140px; height: 207px;" />

<math><msub><mrow><mi>E</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><msub><mrow><mi>E</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mi>k</mi><mo>&#8907;</mo></mrow><mrow><mi>R</mi></mrow></mfrac><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mfrac><mrow><mn>90</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mo>{</mo><mo>&#8907;</mo><mo>=</mo><mfrac><mrow><mi>Q</mi></mrow><mrow><mi>&#960;</mi><mi>R</mi><mo>/</mo><mn>2</mn></mrow></mfrac><mo>}</mo></mrow></mrow></math>


undefined

Component along <math><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mi>&#160;</mi></math> gets cancelled and 

<math> <mrow> <msub> <mi>E</mi> <mrow> <mi>n</mi><mi>e</mi><mi>t</mi></mrow> </msub> <mo>=</mo><msqrt> <mn>2</mn> </msqrt> <msub> <mi>E</mi> <mn>1</mn> </msub> </mrow> </math>

<math> <mrow> <mo>=</mo><mfrac> <mrow> <mn>4</mn><mi>K</mi><mi>Q</mi></mrow> <mrow> <mi>&#960;</mi><msup> <mi>R</mi> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </math>

<math><mo>=</mo><mfrac><mrow><mn>4</mn><mo>&#215;</mo><mn>1</mn><mfenced separators="|"><mrow><msup><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></msup><msub><mrow><mi>&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfenced></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mrow><mi>&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>&#160;</mi><mi>&#960;</mi><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></msup><msub><mrow><mi>&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>4</mn><msup><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></msup><msub><mrow><mi>&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mrow><mn>10</mn></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>100</mn></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn><mi>&#960;</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>25</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover accent="true"><mi>E</mi><mo>&#8594;</mo></mover><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub><mo>=</mo><mn>25</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi mathvariant="normal">&#160;</mi><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover></math>

</details>

---

### Q75. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

<p>A thin disc of radius <math><mi>b</mi><mo>=</mo><mn>2</mn><mi>a</mi></math> has a concentric hole of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> in it (see figure). It carries uniform surface charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#963;</mi></math>  on it. If the electric field on its axis at a height <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>h</mtext><mfenced><mrow><mtext>h</mtext><mo>&#60;</mo><mo>&#60;</mo><mtext>a</mtext></mrow></mfenced></math> from its centre is given as <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>C</mtext><mtext>h</mtext></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/image24-293f48f3-e45c-4786-87cd-28362409a1c3.jpg" /></p>

**Options:**

- **(A)** <math><mfrac><mrow><mi>σ</mi></mrow><mrow><mn>4</mn><mi> </mi><mi>a</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>σ</mi></mrow><mrow><mi>a</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>σ</mi></mrow><mrow><mn>5</mn><mi>a</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>σ</mi></mrow><mrow><mn>2</mn><mi>a</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mi>σ</mi></mrow><mrow><mn>4</mn><mi> </mi><mi>a</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>**

**Detailed Solution:**

<math><mo>&#8757;</mo></math> At the axial point of a uniformly charged disc electric field is given by,

<math><mi>E</mi><mo>=</mo><mfrac><mrow><mi>&#963;</mi></mrow><mrow><mn>2</mn><msub><mrow><mi>&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>c</mi><mi>o</mi><mi>s</mi><mi>&#952;</mi></mrow></mfenced></math>

<img alt="" height="178" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/image25-118f4e4e-ad3f-43b1-84f3-8d236828c2cc.jpg" width="279" />

By superposition principle, when inner disc is removed , then, electric field due to remaining disc is,

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/image26-66eba4b6-ba0e-4225-bad4-71e3fc8f7cf1.jpg" />

<math><mi>E</mi><mo>=</mo><mfrac><mrow><mi>&#963;</mi></mrow><mrow><mn>2</mn><msub><mrow><mi>&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>c</mi><mi>o</mi><mi>s</mi><msub><mrow><mi>&#952;</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>c</mi><mi>o</mi><mi>s</mi><msub><mrow><mi>&#952;</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced></mrow></mfenced></math>

<math><mo>=</mo><mfrac><mrow><mi>&#963;</mi></mrow><mrow><mn>2</mn><msub><mrow><mi>&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mi>c</mi><mi>o</mi><mi>s</mi><msub><mrow><mi>&#952;</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><mi>c</mi><mi>o</mi><mi>s</mi><msub><mrow><mi>&#952;</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfenced></math>

<math><mo>=</mo><mfrac><mrow><mi>&#963;</mi></mrow><mrow><mn>2</mn><msub><mrow><mi>&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>h</mi></mrow><mrow><msqrt><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi></msqrt></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>h</mi></mrow><mrow><msqrt><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></mrow></mfenced></math>

<math><mo>=</mo><mfrac><mrow><mi>&#963;</mi></mrow><mrow><mn>2</mn><msub><mrow><mi>&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>h</mi></mrow><mrow><mi>a</mi><msqrt><mn>1</mn><mo>+</mo><mfrac><mrow><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></msqrt></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>h</mi></mrow><mrow><mi>b</mi><msqrt><mn>1</mn><mo>+</mo><mfrac><mrow><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mi>&#160;</mi></msqrt></mrow></mfrac></mrow></mfenced></math>

<math><mo>&#8757;</mo><mi>h</mi><mi>&#160;</mi><mo>&#8810;</mo><mi>a</mi></math> and b.

<math><mo>&#8756;</mo><mi>E</mi><mo>=</mo><mfrac><mrow><mi>&#963;</mi></mrow><mrow><mn>2</mn><msub><mrow><mi>&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>h</mi></mrow><mrow><mi>a</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>h</mi></mrow><mrow><mi>b</mi></mrow></mfrac></mrow></mfenced></math>

<math><mo>=</mo><mfrac><mrow><mi>&#963;</mi></mrow><mrow><mn>2</mn><msub><mrow><mi>&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>h</mi></mrow><mrow><mi>a</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>h</mi></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>&#963;</mi><mi>h</mi></mrow><mrow><mn>4</mn><msub><mrow><mi>&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>a</mi></mrow></mfrac></math>

<math><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mfrac><mrow><mi>&#963;</mi></mrow><mrow><mn>4</mn><msub><mrow><mi>a</mi><mi>&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>.

</details>

---

### Q76. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Shown in the figure are two point charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>Q</mi></math> inside the cavity of a spherical shell. The charges are kept near the surface of the cavity on opposite sides of the centre of the shell. If <math><msub><mrow><mi>&#963;</mi></mrow><mrow><mn>1</mn></mrow></msub></math> is the surface charge on the inner surface and <math><msub><mrow><mi>Q</mi></mrow><mrow><mn>1</mn></mrow></msub></math> net charge on it and <math><msub><mrow><mi>&#963;</mi></mrow><mrow><mn>2</mn></mrow></msub></math> the surface charge on the outer surface and <math><msub><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msub></math> net charge on it then:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f73bab95-b839-4fc1-958c-cfa20bde9726-image.png" style="width: 170px; height: 168px;" />

**Options:**

- **(A)** <math><msub><mrow><mi>σ</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><msub><mrow><mi>Q</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0</mn></math> , <math><msub><mrow><mi>σ</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><msub><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn></math>
- **(B)** <math><msub><mrow><mi>σ</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>≠</mo><mn>0</mn><mo>,</mo><mi> </mi><msub><mrow><mi>Q</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0</mn></math> ,    <math><msub><mrow><mi>σ</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≠</mo><mn>0</mn><mo>,</mo><mi> </mi><msub><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn></math>
- **(C)** <math><msub><mrow><mi>σ</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>≠</mo><mn>0</mn><mo>,</mo><msub><mrow><mi>Q</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>≠</mo><mn>0</mn></math> ,    <math><msub><mrow><mi>σ</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≠</mo><mn>0</mn><mo>,</mo><mi> </mi><msub><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≠</mo><mn>0</mn></math>
- **(D)** <math><msub><mrow><mi>σ</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>≠</mo><mn>0</mn><mo>,</mo><mi> </mi><msub><mrow><mi>Q</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0</mn></math> , <math><msub><mrow><mi>σ</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><msub><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msub><mrow><mi>σ</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>≠</mo><mn>0</mn><mo>,</mo><mi> </mi><msub><mrow><mi>Q</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0</mn></math> , <math><msub><mrow><mi>σ</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><msub><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

By the property of electrostatic shielding in the conductors <math><mi>E</mi><mo>=</mo><mn>0</mn></math> in the conductor. So, electric flux,<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn></math> through a dotted Gaussian surface as shown

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/94ec9d87-18ea-40a8-ab56-d1392740b3ac-image.png" style="width: 170px; height: 172px;" />

The net enclosed charge through the Gaussian surface<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn></math>,<math><mo>&#8658;</mo></math> The net charge <math><msub><mrow><mi>Q</mi></mrow><mrow><mn>1</mn></mrow></msub></math> on the inner surface<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn></math>, but the equal and opposite induced charge on the surface will be distributed non uniformly on the inner surface

So, <math><msub><mrow><mi>&#963;</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0</mn></math>

<math><mo>&#8757;</mo><msub><mrow><mi>Q</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0</mn></math> on the inner surface

So, net charge <math><msub><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn></math> on the outer surface as conductor is neutral but <math><mo>&#8757;</mo></math> outer surface is free from any electric field so no charge density exists on the outer surface. So, <math><msub><mrow><mi>&#963;</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn></math> .

</details>

---

### Q77. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `1`

A long cylindrical shell carries positive surface charge <math><mi>&#963;</mi></math> in the upper half and negative surface charge <math><mo>&#8211;</mo><mi>&#963;</mi></math> in the lower half. The electric field lines around the cylinder will look like figure given in:

(figures are schematic and not drawn to scale)

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8947391e-1bcc-4973-b000-39a1564e50cf-image.png" style="width: 268px; height: 164px;" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/73ce1e8a-5fd2-4e1a-8d53-4a34bc0c9318-image.png" style="width: 194px; height: 178px;" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3b70c375-32f5-48ec-a6ea-804d79d52d69-image.png" style="width: 189px; height: 192px;" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/52183c77-0adf-4c32-b59e-b766eb09970b-image.png" style="width: 285px; height: 174px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/73ce1e8a-5fd2-4e1a-8d53-4a34bc0c9318-image.png" style="width: 194px; height: 178px;" />**

**Detailed Solution:**

Using the properties of a dipole and laws of electric field line where two lines should not intersect, the graph would be, 

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c65ad572-73db-46ba-99bc-8a39a0869b8c-image.png" style="width: 236px; height: 215px;" />

</details>

---

### Q78. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `2`

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/P_37_Ans_correct_Dhiraj.jpg" style="width: 163px; height: 170px;" />

Two long currents carrying thin wires, both with current <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math>, are held by insulating threads of length L and are in equilibrium as shown in the figure, with threads making an angle &#39; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> &#39; with the vertical. If wires have a mass <math><mi mathvariant="normal">&#955;</mi></math> per unit length then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> is:
(<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>=</mo></math> gravitational acceleration)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mrow><mi mathvariant="normal">&#960;</mi><mi>&#955;</mi><mi>g</mi><mi>L</mi></mrow><msub><mi mathvariant="normal">&#956;</mi><mn>0</mn></msub></mfrac><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><msqrt><mfrac><mrow><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">&#955;</mi><mi>g</mi><mi>L</mi></mrow><mrow><msub><mi mathvariant="normal">&#956;</mi><mrow><mn>0</mn><mi mathvariant="normal">&#160;</mi></mrow></msub><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>&#952;</mi></mrow></mfrac></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><msqrt><mfrac><mrow><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">&#955;</mi><mi>g</mi><mi>L</mi></mrow><mrow><msub><mi mathvariant="normal">&#956;</mi><mn>0</mn></msub><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">&#952;</mi></mrow></mfrac></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mfrac><mrow><mi mathvariant="normal">&#960;</mi><mi>g</mi><mi>L</mi></mrow><msub><mi mathvariant="normal">&#956;</mi><mn>0</mn></msub></mfrac><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><msqrt><mfrac><mrow><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">&#955;</mi><mi>g</mi><mi>L</mi></mrow><mrow><msub><mi mathvariant="normal">&#956;</mi><mn>0</mn></msub><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">&#952;</mi></mrow></mfrac></msqrt></math>**

**Detailed Solution:**

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/P_37_Solu_Dia.jpg" style="width: 300px; height: 216px;" />

Two wires will repel each other due to magnetic force, then the magnetic force per unit length is, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mtext>d</mtext><mtext mathvariant="italic">f</mtext></mrow><mrow><mtext>d</mtext><mtext mathvariant="italic">l</mtext></mrow></mfrac><mo>=</mo><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mtext mathvariant="italic">I</mtext><mn>2</mn></msup></mrow><mrow><mn>2</mn><mi>&#960;</mi><mfenced><mrow><mn>2</mn><mtext mathvariant="italic">L</mtext><mtext>sin</mtext><mi>&#952;</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mtext mathvariant="italic">I</mtext><mn>2</mn></msup></mrow><mrow><mn>4</mn><mi>&#960;</mi><mtext mathvariant="italic">L</mtext><mtext>sin</mtext><mi>&#952;</mi></mrow></mfrac></math>. And mass per unit length of each wire<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mtext>d</mtext><mtext mathvariant="italic">m</mtext></mrow><mrow><mtext>d</mtext><mtext mathvariant="italic">l</mtext></mrow></mfrac><mo>=</mo><mi>&#955;</mi></math>. So, the magnetic force on the total length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> of the wire is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mtext mathvariant="italic">f</mtext><mtext>m</mtext></msub><mo>=</mo><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mtext mathvariant="italic">I</mtext><mn>2</mn></msup><mi>L</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><mtext mathvariant="italic">L</mtext><mtext>sin</mtext><mi>&#952;</mi></mrow></mfrac></math>, and weight <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#955;</mi><mi>L</mi><mtext>g</mtext></math>. By equilibrium of wire,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext mathvariant="italic">T</mtext><mtext>sin</mtext><mi>&#952;</mi><mo>=</mo><msub><mtext mathvariant="italic">f</mtext><mi>m</mi></msub><mtext>&#8201;&#160;&#38;&#160;&#160;</mtext><mtext mathvariant="italic">T</mtext><mtext>cos</mtext><mi>&#952;</mi><mtext>&#8201;</mtext><mtext>=</mtext><mtext>&#8201;</mtext><mtext>W&#8201;</mtext><mtext>=&#160;</mtext><mi>&#955;</mi><mi>l</mi><mo>'</mo><mi>g</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>&#8658;</mo><mfrac><mrow><mtext mathvariant="italic">T</mtext><mtext>sin</mtext><mi>&#952;</mi></mrow><mrow><mtext mathvariant="italic">T</mtext><mtext>cos</mtext><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mfrac><msub><mtext mathvariant="italic">f</mtext><mtext>m</mtext></msub><mtext mathvariant="italic">mg</mtext></mfrac><mo>&#8658;</mo><msub><mtext mathvariant="italic">f</mtext><mtext>m</mtext></msub><mo>=</mo><mi>&#955;</mi><mi>l</mi><mo>'</mo><mi>g</mi></mrow><mo>tan</mo><mi>&#952;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mtext>I</mtext><mn>2</mn></msup></mrow><mrow><mn>4</mn><mi>&#960;</mi><mtext>L</mtext><mo>sin</mo><mi>&#952;</mi></mrow></mfrac><mi>L</mi><mo>=</mo><mi>&#955;</mi><mi>L</mi><mtext>g</mtext><mfrac><mrow><mtext>sin</mtext><mi>&#952;</mi></mrow><mrow><mtext>cos</mtext><mi>&#952;</mi></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mtext mathvariant="italic">I</mtext><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mi>&#955;</mi><mtext>g</mtext><mi>&#960;</mi><mtext>L</mtext></mrow><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><mtext>cos</mtext><mi>&#952;</mi></mrow></mfrac><mn>4</mn><msup><mtext>sin</mtext><mn>2</mn></msup><mi>&#952;</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#8658;</mtext><mtext mathvariant="italic">I</mtext><mo>=</mo><mn>2</mn><mtext>sin</mtext><mi>&#952;</mi><msqrt><mfrac><mrow><mi>&#955;</mi><mi>&#960;</mi><mtext>gL</mtext></mrow><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><mtext>cos</mtext><mi>&#952;</mi></mrow></mfrac></msqrt></math>

</details>

---

### Q79. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A spherically symmetric charge distribution is characterised by a charge density having the following variations:
$\rho(r)=\rho_o\left(1-\frac{r}{R}\right)$ for $r < R$
$\rho(\mathrm{r})=0$ for $r \geq \mathrm{R}$
Where $r$ is the distance from the centre of the charge distribution $\rho_{\mathrm{o}}$ is a constant. The electric field at an internal point $(r < R)$ is:

**Options:**

- **(A)** $\frac{\rho_{\mathrm{o}}}{4 \varepsilon_{\mathrm{o}}}\left(\frac{\mathrm{r}}{3}-\frac{\mathrm{r}^2}{4 \mathrm{R}}\right)$
- **(B)** $\frac{\rho_0}{\varepsilon_0}\left(\frac{r}{3}-\frac{r^2}{4 R}\right)$
- **(C)** $\frac{\rho_{\mathrm{o}}}{3 \varepsilon_{\mathrm{o}}}\left(\frac{\mathrm{r}}{3}-\frac{\mathrm{r}^2}{4 \mathrm{R}}\right)$
- **(D)** $\frac{\rho_{\mathrm{o}}}{12 \varepsilon_{\mathrm{o}}}\left(\frac{\mathrm{r}}{3}-\frac{\mathrm{r}^2}{4 \mathrm{R}}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\rho_0}{\varepsilon_0}\left(\frac{r}{3}-\frac{r^2}{4 R}\right)$**

**Detailed Solution:**

Let us consider a spherical shell of radius $x$ and thickness $\mathrm{dx}$.


<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4WAtbLgIi4qs9ZchhCCvdzU6nNrqEIjdIUkTN0Pi6Fs.original.fullsize.png">



Charge on this shell
$$
d q=\rho .4 \pi x^2 d x=\rho_0\left(1-\frac{x}{R}\right) \cdot 4 \pi x^2 d x
$$
$\therefore$ Total charge in the spherical region from centre to $r(r < R)$ is
$$
\begin{aligned}
&q=\int d q=4 \pi \rho_0 \int_0^r\left(1-\frac{x}{R}\right) x^2 d x \\
&=4 \pi \rho_0\left[\frac{x^3}{3}-\frac{x^4}{4 R}\right]_0^r \\
&=4 \pi \rho_0\left[\frac{r^3}{3}-\frac{r^4}{4 R}\right] \\
&=4 \pi \rho_0 r^3\left[\frac{1}{3}-\frac{r}{4 R}\right]
\end{aligned}
$$
$\therefore$ Electric field at $\mathrm{r}, \mathrm{E}=\frac{1}{4 \pi \varepsilon_0} \cdot \frac{\mathrm{q}}{\mathrm{r}^2}$

$$
\begin{aligned}
&=\frac{1}{4 \pi \varepsilon_0} \cdot \frac{4 \pi \rho_0 r^3}{r^2}\left[\frac{1}{3}-\frac{r}{4 R}\right] \\
&=\frac{\rho_0}{\varepsilon_0}\left[\frac{r}{3}-\frac{r^2}{4 R}\right]
\end{aligned}
$$

</details>

---

### Q80. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The surface charge density of a thin charged disc of radius $\mathrm{R}$ is $\sigma$. The value of the electric field at the centre of the disc is $\frac{\sigma}{2 \in_0}$. With respect to the field at the centre, the electric field along the axis at a distance $\mathrm{R}$ from the centre of the disc:

**Options:**

- **(A)** reduces by $70.7 \%$
- **(B)** reduces by $29.3 \%$
- **(C)** reduces by $9.7 \%$
- **(D)** reduces by $14.6 \%$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) reduces by $70.7 \%$**

**Detailed Solution:**

Electric field intensity at the centre of the disc.
$$
\mathrm{E}=\frac{\sigma}{2 \epsilon_0} \quad \text { (given) }
$$
Electric field along the axis at any distance $x$ from the centre of the disc
$$
\mathrm{E}^{\prime}=\frac{\sigma}{2 \epsilon_0}\left(1-\frac{\mathrm{x}}{\sqrt{\mathrm{x}^2+\mathrm{R}^2}}\right)
$$
From question, $\mathrm{x}=\mathrm{R}$ (radius of disc)
$$
\begin{aligned}
\therefore \mathrm{E}^{\prime} &=\frac{\sigma}{2 \epsilon_0}\left(1-\frac{\mathrm{R}}{\sqrt{\mathrm{R}^2+\mathrm{R}^2}}\right) \\
&=\frac{\sigma}{2 \epsilon_0}\left(\frac{\sqrt{2} \mathrm{R}-\mathrm{R}}{\sqrt{2} \mathrm{R}}\right)
\end{aligned}
$$
$$
=\frac{4}{14} \mathrm{E}
$$
$\therefore \%$ reduction in the value of electric field
$$
=\frac{\left(E-\frac{4}{14} E\right) \times 100}{E}=\frac{1000}{14} \%=70.7 \%
$$

</details>

---

### Q81. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Two small equal point charges of magnitude $q$ are suspended from a common point on the ceiling by insulating mass less strings of equal lengths. They come to equilibrium with each string making angle $\theta$ from the vertical. If the mass of each charge is $m$, then the electrostatic potential at the centre of line joining them will be
$$
\left(\frac{1}{4 \pi \in_0}=k\right) \text {. }
$$

**Options:**

- **(A)** $2 \sqrt{k m g \tan \theta}$
- **(B)** $\sqrt{k m g \tan \theta}$
- **(C)** $4 \sqrt{k m g / \tan \theta}$
- **(D)** $4 \sqrt{k m g / \tan \theta}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4 \sqrt{k m g / \tan \theta}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cdW9q66Wx8BnBqRZdQFkcztpBNoeN-R5VXpQ6jCFJIQ.original.fullsize.png">

In equilibrium, $\mathrm{F}_{\mathrm{e}}=\mathrm{T} \sin \theta$
$$
\begin{aligned}
& m g=T \cos \theta \\
& \tan \theta=\frac{F_e}{m g}=\frac{q^2}{4 \pi \epsilon_0 x^2 \times m g} \\
& \therefore x=\sqrt{\frac{q^2}{4 \pi \epsilon_0 \tan \theta m g}}
\end{aligned}
$$
Electric potential at the centre of the line
$$
\mathrm{V}=\frac{\mathrm{kq}}{\mathrm{x} / 2}+\frac{\mathrm{kq}}{\mathrm{x} / 2}=4 \sqrt{\mathrm{kmg} / \tan \theta}
$$

</details>

---

### Q82. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Two balls of same mass and carrying equal charge are hung from a fixed support of length $l$. At electrostatic equilibrium, assuming that angles made by each thread is small, the separation, $x$ between the balls is proportional to :

**Options:**

- **(A)** $l$
- **(B)** $l^2$
- **(C)** $l^{2 / 3}$
- **(D)** $l^{1 / 3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $l^{1 / 3}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/i4R4cBuBTSb7CSxHGkkgUpIEASPZQiocxdcz2VbhZ2c.original.fullsize.png">

In equilibrium, $\mathrm{F}_{\mathrm{e}}=\mathrm{T} \sin \theta$
$m g=T \cos \theta$
$\tan \theta=\frac{F_e}{m g}=\frac{q^2}{4 \pi \epsilon_0 x^2 \times m g}$
also $\tan \theta \approx \sin =\frac{x / 2}{\ell}$
Hence, $\frac{x}{2 \ell}=\frac{q^2}{4 \pi \epsilon_0 x^2 \times m g}$
$\Rightarrow x^3=\frac{2 q^2 \ell}{4 \pi \epsilon_0 m g}$
$\therefore x=\left(\frac{q^2 \ell}{2 \pi \epsilon_0 m g}\right)^{1 / 3}$
Therefore $\mathrm{x} \propto \ell^{1 / 3}$

</details>

---

### Q83. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `2`

Three positive charges of equal value $q$ are placed at vertices of an equilateral triangle. The resulting lines of force should be sketched as in

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/TpNHHkmB_kPPoQ5eM0mTdY-1Di8kF7wf9WkHr-CSkJ4.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/wbynJnyNh3F0a0ULBi-iYRX0Ezq8-N0H-xdpSefpQ-w.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/k15aKv05RwSOPdecXAB3nVuQskjfNR5BYsDvCH2IXR8.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/xKNnWOKscLb8CWHa5om9g-7Z8nJO3BLSCovwRxxkpt0.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/k15aKv05RwSOPdecXAB3nVuQskjfNR5BYsDvCH2IXR8.original.fullsize.png">**

**Detailed Solution:**

Electric lines of force due to a positive charge is spherically symmetric.
All the charges are positive and equal in magnitude. So repulsion takes place. Due to which no lines of force are present inside the equilateral triangle and the resulting lines of force obtained as shown:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/QdTqNbAOfEPpyeR5XXgRCwwDdwGOaXjQqPoNUL66efs.original.fullsize.png">

</details>

---

### Q84. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `2`

In a uniformly charged sphere of total charge $Q$ and radius $R$, the electric field $E$ is plotted as a function of distance from the centre. The graph which would correspond to the above will be

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/NDBPO2u-hqEt3PL-s0fB8pNqrc-G7QyfAR0eJmBxl0k.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/994Tm_y8lZcqWY_noBDR7fsYATfgXFBT9YXlhp9QdA8.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/KK7qt2NQpdLHmNG2Acn1ds3ZAxiakdlwJGc03QXFkEA.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/UcUo1pacjvg7z9xfy_cbubnsyXEVnY1nMRtTeBmqeTA.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/KK7qt2NQpdLHmNG2Acn1ds3ZAxiakdlwJGc03QXFkEA.original.fullsize.png">**

**Detailed Solution:**

$\overrightarrow{\mathrm{E}}_{\text {inside }}=\left(\frac{1}{4 \pi \varepsilon_0} \frac{\mathrm{Q}}{\mathrm{R}^3}\right) \overrightarrow{\mathrm{r}}$
$\overrightarrow{\mathrm{E}}_{\text {outside }}\left(\frac{1}{4 \pi \varepsilon_0} \frac{\mathrm{Q}}{\mathrm{r}^3}\right) \overrightarrow{\mathrm{r}}$
$\therefore$ <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5RZS6VUwIIQ5juUK5ntJO6NSAIopRXsY3jQl-PQ2USA.original.fullsize.png">

</details>

---

### Q85. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `3`

Let there be a spherically symmetric charge distribution with charge density varying as $\rho(r)=\rho_0\left(\frac{5}{4}-\frac{r}{R}\right)$ upto $r=R$, and $\rho(r)=0$ for $r>R$, where $r$ is the distance from the origin. The electric field at a distance $r(r < R)$ from the origin is given by

**Options:**

- **(A)** $\frac{4 \pi \rho_0 r}{3 \varepsilon_0}\left(\frac{5}{3}-\frac{r}{R}\right)$
- **(B)** $\frac{\rho_0 r}{4 \varepsilon_0}\left(\frac{5}{3}-\frac{r}{R}\right)$
- **(C)** $\frac{4 \rho_0 r}{3 \varepsilon_0}\left(\frac{5}{4}-\frac{r}{R}\right)$
- **(D)** $\frac{\rho_0 r}{3 \varepsilon_0}\left(\frac{5}{4}-\frac{r}{R}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\rho_0 r}{4 \varepsilon_0}\left(\frac{5}{3}-\frac{r}{R}\right)$**

**Detailed Solution:**

Apply shell theorem the total charge upto distance $r$ can be calculated as followed $d q=4 \pi r^2 \cdot d r . \rho$
$$
\begin{aligned}
& =4 \pi r^2 \cdot d r \cdot \rho_0\left[\frac{5}{4}-\frac{r}{R}\right] \\
& =4 \pi \rho_0\left[\frac{5}{4} r^2 d r-\frac{r^3}{R} d r\right] \\
& \int d q=q=4 \pi \rho_0 \int_0^r\left(\frac{5}{4} r^2 d r-\frac{r^3}{R} d r\right) \\
& =4 \pi \rho_0\left[\frac{5}{4} \frac{r^3}{3}-\frac{1}{R} \frac{r^4}{4}\right] \\
& E=\frac{k q}{r^2} \\
& =\frac{1}{4 \pi \varepsilon_0} \frac{1}{r^2} \cdot 4 \pi \rho_0\left[\frac{5}{4}\left(\frac{r^3}{3}\right)-\frac{r^4}{4 R}\right] \\
& E=\frac{\rho_0 r}{4 \varepsilon_0}\left[\frac{5}{3}-\frac{r}{R}\right] \\
&
\end{aligned}
$$

</details>

---

### Q86. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `2`

A thin semi-circular ring of radius $r$ has a positive charge $q$ distributed uniformly over it. The net field $\vec{E}$ at the centre $O$ is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6veO4pRmU1iB6s2CMj7T3Ufs9Zx3Zpp5ws8jDDQXIXU.original.fullsize.png">

**Options:**

- **(A)** $\frac{q}{4 \pi^2 \varepsilon_0 r^2} \hat{j}$
- **(B)** $-\frac{q}{4 \pi^2 \varepsilon_0 r^2} \hat{j}$
- **(C)** $-\frac{q}{2 \pi^2 \varepsilon_0 r^2} \hat{j}$
- **(D)** $\frac{\mathrm{q}}{2 \pi^2 \varepsilon_0 \mathrm{r}^2} \hat{\mathrm{j}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\frac{q}{2 \pi^2 \varepsilon_0 r^2} \hat{j}$**

**Detailed Solution:**

Linear charge density $\lambda=\left(\frac{q}{\pi r}\right)$
$E=\int d E \sin \theta(-\hat{\mathrm{j}})=\int \frac{\mathrm{K} \cdot d q}{\mathrm{r}^2} \sin \theta(-\hat{\mathrm{j}})$
$\mathrm{E}=\frac{\mathrm{K}}{\mathrm{r}^2} \int \frac{\mathrm{qr}}{\pi r} \mathrm{~d} \theta \sin \theta(-\hat{\mathrm{j}})$
$=\frac{\mathrm{K}}{\mathrm{r}^2} \frac{\mathrm{q}}{\pi} \int_0^\pi \sin \theta(-\hat{\mathrm{j}})$
$=\frac{\mathrm{q}}{2 \pi^2 \varepsilon_0 \mathrm{r}^2}(-\hat{\mathrm{j}})$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/hVMGjVjZaHfEiDSqoB70ytJcuQ2SZ7rz0JvYo7K3Ehk.original.fullsize.png">

</details>

---

### Q87. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `3`

A charge $Q$ is placed at each of the opposite corners of a square. A charge $q$ is placed at each of the other two corners. If the net electrical force on $Q$ is zero, then the $Q / q$ equals

**Options:**

- **(A)** $-2 \sqrt{2}$
- **(B)** $-1$
- **(C)** 1
- **(D)** $-\frac{1}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-2 \sqrt{2}$**

**Detailed Solution:**

Three forces $F_{41}, F_{42}$ and $f_{43}$ acting on $Q$ are shown
Resultant of $F_{41}+F_{43}$
$$
\begin{aligned}
& =\sqrt{2} F_{\text {each }} \\
& =\sqrt{2} \frac{1}{4 \pi \varepsilon_0} \frac{Q q}{d^2}
\end{aligned}
$$
Resultant on $Q$ becomes zero only when ' $q$ ' charges are of negative nature.
$$
\begin{aligned}
& F_{4,2}=\frac{1}{4 \pi \varepsilon_0} \frac{Q \times Q}{(\sqrt{2} d)^2} \\
& \Rightarrow \sqrt{2} \frac{d Q}{d^2}=\frac{Q \times Q}{2 d^2} \\
& \Rightarrow \sqrt{2} \times q=\frac{Q \times Q}{2} \\
& \therefore q=-\frac{Q}{2 \sqrt{2}} \text { or } \frac{Q}{q}=-2 \sqrt{2}
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/xjQ8pK2jthsQMfE7Nm5fbek92vHsOw_qQl4LM-hndEY.original.fullsize.png">

</details>

---

### Q88. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `3`

Let $P(r)=\frac{Q}{\pi R^4} r$ be the charge density distribution for a solid sphere of radius $R$ and total charge $Q$. for a point ' $p$ ' inside the sphere at distance $r_1$ from the centre of the sphere, the magnitude of electric field is

**Options:**

- **(A)** 0
- **(B)** $\frac{Q}{4 \pi \varepsilon_0 r_1^2}$
- **(C)** $\frac{Q r_1^2}{4 \pi \varepsilon_0 R^4}$
- **(D)** $\frac{Q_1^2}{3 \pi \varepsilon_0 R^4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{Q r_1^2}{4 \pi \varepsilon_0 R^4}$**

**Detailed Solution:**

$$
E 4 \pi r_1^2=\frac{\int_0^{r_1} \frac{Q}{\pi R^4} r 4 \pi r^2 d r}{\varepsilon_0} \Rightarrow E=\frac{Q r_1^2}{4 \pi \varepsilon_0 R^4} .
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/VASiw03lshITscEsQoAy92_femN_Z--gdAGnGtvb6lo.original.fullsize.png">

</details>

---

### Q89. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `1`

A thin spherical shell of radius $R$ has charge $Q$ spread uniformly over its surface. Which of the following graphs most closely represents the electric field $E(r)$ produced by the shell in the range $0 \leq$ $r < \infty$, where $r$ is the distance from the centre of the shell?<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7QANz4ni6ZG6VcyzksfH6vhJOoJWld1lbkAXMN2x1Os.original.fullsize.png">

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cEvrUMZxHoJajage7slsM988Cl_lcgdIbdkhCsjnnp8.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/tRCpITDxeVihau1mb6RKt_1Om7Q5d6n0igfjwHZy05k.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Q5pNS7zdaNOBAV38JSrRgXIn3aXCaq1lsqleHnCfN7k.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/aJowl1ePmepPuhEDt9DdsY5OuQFTMbQm5NbMGTCseEE.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cEvrUMZxHoJajage7slsM988Cl_lcgdIbdkhCsjnnp8.original.fullsize.png">**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7QANz4ni6ZG6VcyzksfH6vhJOoJWld1lbkAXMN2x1Os.original.fullsize.png">

</details>

---

### Q90. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `2`

Two spherical conductors $A$ and $B$ of radii $1 \mathrm{~mm}$ and $2 \mathrm{~mm}$ are separated by a distance of $5 \mathrm{~cm}$ and are uniformly charged. If the spheres are connected by a conducting wire then in equilibrium condition, the ratio of the magnitude of the electric fields at the surface of spheres $A$ and $B$ is

**Options:**

- **(A)** $1: 4$
- **(B)** $4: 1$
- **(C)** $1: 2$
- **(D)** $2: 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2: 1$**

**Detailed Solution:**

$\frac{\mathrm{E}_{\mathrm{A}}}{\mathrm{E}_{\mathrm{B}}}=\frac{\mathrm{r}_{\mathrm{B}}}{\mathrm{r}_{\mathrm{A}}}=\frac{2}{1}$

</details>

---

### Q91. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `3`

A charged ball B hangs from a silk thread $S$ which makes an angle $\theta$ with a large charged conducting sheet $\mathrm{P}$, as show in the figure. The surface charge density $\sigma$ of the sheet is proportional to
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dHnSmwMLBG09rU28P7r_F3VnZ2HAxsV-R7FmMJ83ZN4.original.fullsize.png">

**Options:**

- **(A)** $\cos \theta$
- **(B)** $\cot \theta$
- **(C)** $\sin \theta$
- **(D)** $\tan \theta$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\tan \theta$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/RnRuKzA5ImXh3LpMnxlNL8s-v-zUX7SN5gPzIW8hL3g.original.fullsize.png">

$\tan \theta=\frac{q \sigma}{\left(2 \varepsilon_{\circ}\right) m g}$

</details>

---

### Q92. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

A charged oil drop is suspended in a uniform field of $3 \times 10^4 \mathrm{~V} / \mathrm{m}$ so that it neither falls nor rises. The charge on the drop will be (take the mass of the charge $=9.9 \times 10^{-15} \mathrm{~kg}$ and $\mathrm{g}=$ $10 \mathrm{~m} / \mathrm{s}^2$ )

**Options:**

- **(A)** $3.3 \times 10^{-18} \mathrm{C}$
- **(B)** $3.2 \times 10^{-18} \mathrm{C}$
- **(C)** $1.6 \times 10^{-18} \mathrm{C}$
- **(D)** $4.8 \times 10^{-18} \mathrm{C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3.3 \times 10^{-18} \mathrm{C}$**

**Detailed Solution:**

Since ball is hanging in equilibrium, force by gravity is balanced by electric force.
$$
\begin{aligned}
& \mathrm{qE}=\mathrm{mg} \\
& \Rightarrow \mathrm{q}=\frac{\mathrm{m} \times \mathrm{g}}{\mathrm{E}} \\
& \Rightarrow \frac{9.9 \times 10^{-15} \times 10}{3 \times 10^4} \\
& \therefore \mathrm{q}=3.3 \times 10^{-18} \mathrm{C}
\end{aligned}
$$

</details>

---

### Q93. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

Four charges equal to $-Q$ are placed at the four corners of a square and a charge $q$ is at its centre. If the system is in equilibrium the value of $q$ is

**Options:**

- **(A)** $-\frac{Q}{4}(1+2 \sqrt{2})$
- **(B)** $-\frac{Q}{2}(1+2 \sqrt{2})$
- **(C)** $-\frac{Q}{2}(1+2 \sqrt{2})$
- **(D)** $\frac{Q}{2}(1+2 \sqrt{2})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{Q}{2}(1+2 \sqrt{2})$**

**Detailed Solution:**

$q=+\frac{Q}{4}(1+2 \sqrt{2})$

</details>

---

### Q94. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `3`

Three charges $-q_1,+q_2$ and $-q_3$ are placed as shown in the figure. The $x$-component of the force on $-q_1$ is proportional to
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3PD4GSG2iGM4h9jlamuimPubBFv1SfxQFlwYEKHcKS0.original.fullsize.png">

**Options:**

- **(A)** $\frac{\mathrm{q}_2}{\mathrm{~b}^2}-\frac{\mathrm{q}_3}{\mathrm{a}^2} \cos \theta$
- **(B)** $\frac{\mathrm{q}_2}{\mathrm{~b}^2}+\frac{\mathrm{q}_3}{\mathrm{a}^2} \sin \theta$
- **(C)** $\frac{\mathrm{q}_2}{\mathrm{~b}^2}+\frac{\mathrm{q}_3}{\mathrm{a}^2} \cos \theta$
- **(D)** $\frac{\mathrm{q}_2}{\mathrm{~b}^2}-\frac{\mathrm{q}_3}{\mathrm{a}^2} \sin \theta$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\mathrm{q}_2}{\mathrm{~b}^2}+\frac{\mathrm{q}_3}{\mathrm{a}^2} \sin \theta$**

**Detailed Solution:**

The force body diagram
$F_1=\frac{1}{4 \pi \varepsilon_0} \cdot \frac{q_1 q_3}{a^2}$         $\mathrm{F}_2=\frac{1}{4 \pi \varepsilon_0} \cdot \frac{\mathrm{q}_1 \mathrm{q}_3}{\mathrm{~b}^2}$   <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/KbKrw2Or0F6AgX2g0bnbQ98qP8NPvJXhClzs9jkajrs.original.fullsize.png">

$\mathrm{F}_{\mathrm{X}}=\mathrm{F}_1 \sin \theta+\mathrm{F}_2=\frac{\mathrm{q}_1}{4 \pi \varepsilon_0}\left[\frac{\mathrm{q}_3}{\mathrm{a}^2} \sin \theta+\frac{\mathrm{q}_1}{\mathrm{~b}_2}\right] \Rightarrow \mathrm{F}_{\mathrm{X}} \propto\left(\frac{\mathrm{q}_3}{\mathrm{a}^2} \sin \theta+\frac{\mathrm{q}_2}{\mathrm{~b}^2}\right)$

</details>

---

### Q95. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

If a charge $q$ is placed at the centre of the line joining two equal charges $Q$ such that the system is in equilibrium then the value of $q$ is

**Options:**

- **(A)** $Q / 2$
- **(B)** $-Q / 2$
- **(C)** $\mathrm{Q} / 4$
- **(D)** $-Q / 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-Q / 4$**

**Detailed Solution:**

Apply the condition for equilibrium of each charge

</details>

---

