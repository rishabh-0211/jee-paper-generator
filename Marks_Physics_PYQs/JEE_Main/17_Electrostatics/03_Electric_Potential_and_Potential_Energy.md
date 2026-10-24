# JEE Main Physics - Electrostatics

## Topic 3: Electric Potential and Potential Energy

**Total Questions:** 87

---

### Q1. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The electric potential as a function of $x, y$ is given by $V = 5(x^2 - y^2)$ V. The electric field at a point $(2, 3)$ m is __________ V/m.

**Options:**

- **(A)** $(-20\hat{i} + 30\hat{j})$
- **(B)** $(20\hat{i} - 30\hat{j})$
- **(C)** $(20\hat{i} + 45\hat{j})$
- **(D)** $(-4\hat{i} + 6\hat{j})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(-20\hat{i} + 30\hat{j})$**

**Detailed Solution:**

The electric field $\vec{E}$ is given by the negative gradient of the electric potential $V$:

$\vec{E} = -\left( \dfrac{\partial V}{\partial x} \hat{i} + \dfrac{\partial V}{\partial y} \hat{j} \right)$

Given $V = 5(x^2 - y^2)$, we find the partial derivatives:

$\dfrac{\partial V}{\partial x} = 10x$

$\dfrac{\partial V}{\partial y} = -10y$

Substituting these into the expression for $\vec{E}$:

$\vec{E} = -(10x \hat{i} - 10y \hat{j}) = -10x \hat{i} + 10y \hat{j}$

At the point $(2, 3)$, substitute $x = 2$ and $y = 3$:

$\vec{E} = -10(2) \hat{i} + 10(3) \hat{j} = -20\hat{i} + 30\hat{j}$ V/m

Answer: $(-20\hat{i} + 30\hat{j})$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 1)

*Type:* `numerical` | *Level:* `2`

A three coulomb charge moves from the point $(0, -2, -5)$ to the point $(5, 1, 2)$ in an electric field expressed as $\vec{E} = 2x\hat{i} + 3y^2\hat{j} + 4\hat{k}$ N/C. The work done in moving the charge is _______ J.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **186**

**Detailed Solution:**

The force experienced by the charge in the electric field is given by $\vec{F} = q\vec{E}$.

Given $q = 3$ C and $\vec{E} = 2x\hat{i} + 3y^2\hat{j} + 4\hat{k}$ N/C, the force is:
$\vec{F} = 3(2x\hat{i} + 3y^2\hat{j} + 4\hat{k}) = 6x\hat{i} + 9y^2\hat{j} + 12\hat{k}$ N

The work done by the electric field in moving the charge is:
$W = \int \vec{F} \cdot d\vec{r} = \int_{x_1}^{x_2} F_x dx + \int_{y_1}^{y_2} F_y dy + \int_{z_1}^{z_2} F_z dz$

Substituting the limits from the initial point $(0, -2, -5)$ to the final point $(5, 1, 2)$:
$W = \int_{0}^{5} 6x dx + \int_{-2}^{1} 9y^2 dy + \int_{-5}^{2} 12 dz$

Evaluating each integral separately:
$\int_{0}^{5} 6x dx = \left[ 3x^2 \right]_{0}^{5} = 3(5^2 - 0^2) = 75$ J

$\int_{-2}^{1} 9y^2 dy = \left[ 3y^3 \right]_{-2}^{1} = 3(1^3 - (-2)^3) = 3(1 - (-8)) = 3(9) = 27$ J

$\int_{-5}^{2} 12 dz = \left[ 12z \right]_{-5}^{2} = 12(2 - (-5)) = 12(7) = 84$ J

Total work done $W = 75 + 27 + 84 = 186$ J.

Answer: $186$

</details>

---

### Q3. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two charged conducting spheres $S_1$ and $S_2$ of radii $8$ cm and $18$ cm are connected to each other by a wire. After equilibrium is established, the ratio of electric fields on $S_1$ and $S_2$ spheres are $E_{S_1}$ and $E_{S_2}$ respectively. The value of $\dfrac{E_{S_1}}{E_{S_2}}$ is _______.

**Options:**

- **(A)** $\dfrac{3}{2}$
- **(B)** $\dfrac{2}{3}$
- **(C)** $\dfrac{4}{9}$
- **(D)** $\dfrac{9}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{9}{4}$**

**Detailed Solution:**

When two conducting spheres are connected by a wire, charge flows until their potentials become equal.

$V_1 = V_2$

$\dfrac{k Q_1}{R_1} = \dfrac{k Q_2}{R_2}$

The electric field on the surface of a conducting sphere is given by $E = \dfrac{k Q}{R^2}$, which can be written as $E = \dfrac{V}{R}$.

Since $V_1 = V_2$, we have:

$E_{S_1} R_1 = E_{S_2} R_2$

$\dfrac{E_{S_1}}{E_{S_2}} = \dfrac{R_2}{R_1}$

Given $R_1 = 8$ cm and $R_2 = 18$ cm:

$\dfrac{E_{S_1}}{E_{S_2}} = \dfrac{18}{8} = \dfrac{9}{4}$

Answer: $\dfrac{9}{4}$

</details>

---

### Q4. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two point charges of 1 nC and 2 nC are placed at the two corners of equilateral triangle of side 3 cm. The work done in bringing a charge of 3 nC from infinity to the third corner of the triangle is $\_\_\_\_$ $\mu \mathrm{J}$. 
 $\frac{1}{4 \pi \epsilon_{0}}=9 \times 10^{9} \mathrm{~N}. \mathrm{m}^{2} / \mathrm{C}^{2}$

**Options:**

- **(A)** 27
- **(B)** 5.4
- **(C)** 2.7
- **(D)** 3.3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2.7**

**Detailed Solution:**

Two point charges of 1 nC and 2 nC are placed at two corners of an equilateral triangle with side 3 cm. The work done in bringing a 3 nC charge from infinity to the third corner equals the charge times the potential at that point.
Both source charges are at distance 0.03 m from the third corner.
The potential due to the 1 nC charge is $V_1 = \frac{9 \times 10^9 \times 1 \times 10^{-9}}{0.03} = 300$ V
and due to the 2 nC charge is $V_2 = \frac{9 \times 10^9 \times 2 \times 10^{-9}}{0.03} = 600$ V.
Total potential: $V_{total} = 300 + 600 = 900$ V
Work done: $W = 3 \times 10^{-9} \times 900 = 2.7 \times 10^{-6}$ J = 2.7 μJ

</details>

---

### Q5. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The electrostatic potential in a charged spherical region of radius $r$ varies as $V=a r^{3}+b$, where $a$ and $b$ are constants. The total charge in the sphere of unit radius is $\alpha \times \pi a \in_{\mathrm{o}}$. The value of $\alpha$ is $\_\_\_\_$. 
 (permittivity of vacuum is $\epsilon_{0}$)

**Options:**

- **(A)** $-9$
- **(B)** -12
- **(C)** -8
- **(D)** -6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -12**

**Detailed Solution:**

From $V = ar^3 + b$, the electric field is $E = -dV/dr = -3ar^2$. 
By Gauss's law: 
$E(r) \cdot 4\pi r^2 = Q(r)/\epsilon_0$, so $-3ar^2 \times 4\pi r^2 = Q(r)/\epsilon_0$. 
This gives $Q(r) = -12\pi ar^4\epsilon_0$. 
At $r = 1$: $Q(1) = -12\pi a\epsilon_0$. 
Since $Q(1) = \alpha \times \pi a\epsilon_0$, we have $\alpha = -12$

</details>

---

### Q6. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

There are three co-centric conducting spherical shells $A, B$ and $C$ of radii $a, b$ and $c$ respectively $(c>b>a)$ and they are charged with charge $q_{1}, q_{2}$ and $q_{3}$ respectively. The potentials of the spheres $A, B$ and $C$ respectively, are :

**Options:**

- **(A)** $\frac{1}{4 \pi \epsilon_{\mathrm{o}}}\left(\frac{q_{1}+q_{2}+q_{3}}{a}\right), \frac{1}{4 \pi \epsilon_{\mathrm{o}}}\left(\frac{q_{1}+q_{2}+q_{3}}{b}\right), \frac{1}{4 \pi \epsilon_{\mathrm{o}}}\left(\frac{q_{1}+q_{2}+q_{3}}{c}\right)$
- **(B)** $\frac{1}{4 \pi \epsilon_{\mathrm{o}}}\left(\frac{q_{1}}{a}+\frac{q_{2}}{b}+\frac{q_{3}}{c}\right), \frac{1}{4 \pi \epsilon_{\mathrm{o}}}\left(\frac{q_{1}+q_{2}+q_{3}}{b}\right), \frac{1}{4 \pi \epsilon_{\mathrm{o}}}\left(\frac{q_{1}+q_{2}+q_{3}}{c}\right)$
- **(C)** $\frac{1}{4 \pi \epsilon_{\mathrm{o}}}\left(\frac{q_{1}}{a}+\frac{q_{2}}{b}+\frac{q_{3}}{c}\right), \frac{1}{4 \pi \epsilon_{\mathrm{o}}}\left(\frac{q_{1}+q_{2}}{b}+\frac{q_{3}}{c}\right), \frac{1}{4 \pi \epsilon_{\mathrm{o}}}\left(\frac{q_{1}+q_{2}+q_{3}}{c}\right)$
- **(D)** $\frac{1}{4 \pi \epsilon_{\mathrm{o}}}\left(\frac{q_{1}+q_{2}+q_{3}}{a}\right), \frac{1}{4 \pi \epsilon_{\mathrm{o}}}\left(\frac{q_{1}+q_{2}}{b}+\frac{q_{3}}{c}\right), \frac{1}{4 \pi \epsilon_{\mathrm{o}}}\left(\frac{q_{1}}{a}+\frac{q_{2}}{b}+\frac{q_{3}}{c}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{4 \pi \epsilon_{\mathrm{o}}}\left(\frac{q_{1}}{a}+\frac{q_{2}}{b}+\frac{q_{3}}{c}\right), \frac{1}{4 \pi \epsilon_{\mathrm{o}}}\left(\frac{q_{1}+q_{2}}{b}+\frac{q_{3}}{c}\right), \frac{1}{4 \pi \epsilon_{\mathrm{o}}}\left(\frac{q_{1}+q_{2}+q_{3}}{c}\right)$**

**Detailed Solution:**

The potential at any point due to a charged spherical shell of radius $R$ and charge $Q$ is $V = \frac{1}{4\pi\epsilon_o} \frac{Q}{R}$ for points inside or on the surface ($r \le R$), and $V = \frac{1}{4\pi\epsilon_o} \frac{Q}{r}$ for points outside ($r > R$).
Let $k = \frac{1}{4\pi\epsilon_o}$. The potentials of the three shells $A, B, C$ with radii $a < b < c$ and charges $q_1, q_2, q_3$ are calculated by superposition.
For shell $A$ ($r = a$):
Shell $A$ is on its own surface, while it is inside shells $B$ and $C$.
$V_A = k\frac{q_1}{a} + k\frac{q_2}{b} + k\frac{q_3}{c} = \frac{1}{4\pi\epsilon_o} \left( \frac{q_1}{a} + \frac{q_2}{b} + \frac{q_3}{c} \right)$
For shell $B$ ($r = b$):
Shell $B$ is outside shell $A$, on its own surface, and inside shell $C$.
$V_B = k\frac{q_1}{b} + k\frac{q_2}{b} + k\frac{q_3}{c} = \frac{1}{4\pi\epsilon_o} \left( \frac{q_1 + q_2}{b} + \frac{q_3}{c} \right)$
For shell $C$ ($r = c$):
Shell $C$ is outside shells $A$ and $B$, and on its own surface.
$V_C = k\frac{q_1}{c} + k\frac{q_2}{c} + k\frac{q_3}{c} = \frac{1}{4\pi\epsilon_o} \left( \frac{q_1 + q_2 + q_3}{c} \right)$
Comparing these expressions with the given options, option (3) matches correctly.

</details>

---

### Q7. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two charges $7 \mu \mathrm{C}$ and $-2 \mu \mathrm{C}$ are placed at $(-9,0,0) \mathrm{cm}$ and $(9,0,0) \mathrm{cm}$ respectively in an external field $E=\frac{\mathrm{A}}{r^{2}} \hat{r}$, where $A=9 \times 10^{5} \mathrm{~N} / \mathrm{C}. \mathrm{m}^{2}$. Considering the potential at infinity is 0, the electrostatic energy of the configuration is $\_\_\_\_$ J.

**Options:**

- **(A)** 49.3
- **(B)** -90.7
- **(C)** 24.3
- **(D)** 1.4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 49.3**

**Detailed Solution:**

The total electrostatic energy $U$ of a system of two charges $q_1$ and $q_2$ in an external field is given by $U = q_1 V(r_1) + q_2 V(r_2) + \frac{k q_1 q_2}{r_{12}}$.
Given external electric field $E = \frac{A}{r^2} \hat{r}$, the potential $V(r)$ is found by $V(r) = -\int_{\infty}^{r} E \cdot dr = -\int_{\infty}^{r} \frac{A}{r^2} dr = \frac{A}{r}$.
Parameters given:
$q_1 = 7 \mu C = 7 \times 10^{-6} C$ at $r_1 = 9 cm = 0.09 m$.
$q_2 = -2 \mu C = -2 \times 10^{-6} C$ at $r_2 = 9 cm = 0.09 m$.
Distance between charges $r_{12} = 9 - (-9) = 18 cm = 0.18 m$.
$A = 9 \times 10^5 N/C \cdot m^2$.
Calculating individual terms:
$q_1 V(r_1) = q_1 \frac{A}{r_1} = (7 \times 10^{-6}) \frac{9 \times 10^5}{0.09} = 7 \times 10^{-6} \times 10^7 = 70 J$.
$q_2 V(r_2) = q_2 \frac{A}{r_2} = (-2 \times 10^{-6}) \frac{9 \times 10^5}{0.09} = -2 \times 10^{-6} \times 10^7 = -20 J$.
Interaction energy $\frac{k q_1 q_2}{r_{12}} = \frac{9 \times 10^9 \times (7 \times 10^{-6}) \times (-2 \times 10^{-6})}{0.18} = \frac{-126 \times 10^{-3}}{0.18} = -0.7 J$.
Total energy $U = 70 - 20 - 0.7 = 49.3 J$.

</details>

---

### Q8. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Three small identical bubbles of water having same charge on each coalesce to form a bigger bubble. Then the ratio of the potentials on one initial bubble and that on the resultant bigger bubble is :

**Options:**

- **(A)** $3^{2 / 3}: 1$
- **(B)** $1: 2^{2 / 3}$
- **(C)** $1: 3^{2 / 3}$
- **(D)** $1: 3^{1 / 3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1: 3^{2 / 3}$**

**Detailed Solution:**

For three identical conducting bubbles with charge $q$ and radius $r$,
Initial potential on each: $V_i = \frac{kq}{r}$
When three bubbles coalesce,
Total charge $Q = 3q$ and new radius from volume: $\frac{4}{3}\pi R^3 = 3 \times \frac{4}{3}\pi r^3$
So $R = 3^{1/3}r$
Final potential: $V_f = \frac{k(3q)}{3^{1/3}r} = \frac{3kq}{3^{1/3}r} = V_i \cdot 3^{2/3}$
Ratio: $V_i : V_f = 1 : 3^{2/3}$

</details>

---

### Q9. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Five positive charges each having charge $q$ are placed at the vertices of a pentagon as shown in the figure. The electric potential $(V)$ and the electric field $(\vec{E})$ at the center $O$ of the pentagon due to these five positive charges are:
<img style="width:200px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/22S2_q_33_1.png">

**Options:**

- **(A)** $V=\frac{5 q}{4 \pi \varepsilon_{o} r} \text { and } \vec{E}=\frac{5 \sqrt{3} q}{8 \pi \varepsilon_{o} r^{2}} \hat{r}$
- **(B)** $V=\frac{5 q}{4 \pi \varepsilon_{o} r} \text { and } \vec{E}=0$
- **(C)** $V=0 \text { and } \vec{E}=0$
- **(D)** $V=\frac{5 q}{4 \pi \varepsilon_{o} r} \text { and } \vec{E}=\frac{5 q}{4 \pi \varepsilon_{\mathrm{o}} r^{2}} \hat{r}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $V=\frac{5 q}{4 \pi \varepsilon_{o} r} \text { and } \vec{E}=0$**

**Detailed Solution:**

The electric potential at center O is the scalar sum of contributions from all 5 charges.
Each charge is equidistant from center, so $V = 5 cdot \frac{kq}{r} = \frac{5q}{4\pi\epsilon_0 r}$.
The electric field is a vector sum of field vectors from all 5 charges.
Due to 5-fold rotational symmetry of a regular pentagon, the 5 field vectors point radially outward from center, equally spaced at 72° angles.
The vector sum of 5 equally spaced unit vectors is zero, so $\vec{E} = 0$.

</details>

---

### Q10. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Electric field in a region is given by $\vec{E}=A x \hat{i}+B y \hat{j}$, where $A=10 \mathrm{~V} / \mathrm{m}^{2}$ and $B=5 \mathrm{~V} / \mathrm{m}^{2}$. If the electric potential at a point $(10,20)$ is 500 V, then the electric potential at origin is $\_\_\_\_$ V.

**Options:**

- **(A)** 0
- **(B)** 2000
- **(C)** 500
- **(D)** 1000

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2000**

**Detailed Solution:**

The electric field is related to potential by $\vec{E} = -\nabla V$.
Given: $\vec{E} = Ax\hat{i} + By\hat{j}$ with $A = 10$ V/m² and $B = 5$ V/m²
This means:
$\frac{\partial V}{\partial x} = -Ax$ and $\frac{\partial V}{\partial y} = -By$
Integrating:
$V(x,y) = -\frac{Ax^2}{2} - \frac{By^2}{2} + C = -5x^2 - \frac{5y^2}{2} + C$
Using the boundary condition at $(10, 20)$ where $V = 500$ V:
$500 = -5(100) - \frac{5(400)}{2} + C$
$500 = -500 - 1000 + C$
$C = 2000$ V
At the origin $(0, 0)$:
$V(0,0) = -5(0) - \frac{5(0)}{2} + 2000 = 2000$ V

</details>

---

### Q11. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider two identical metallic spheres of radius $R$ each having charge $Q$ and mass $m$. Their centers have an initial separation of $4 R$. Both the spheres are given an initial speed of $u$ towards each other. The minimum value of $u$, so that they can just touch each other is : 
 (Take $k=\frac{1}{4 \pi \epsilon_{0}}$ and assume $k Q^{2}>G m^{2}$ where $G$ is the Gravitational constant)

**Options:**

- **(A)** $\sqrt{\frac{k Q^{2}}{2 m R}\left(1-\frac{G m^{2}}{k Q^{2}}\right)}$
- **(B)** $\sqrt{\frac{k Q^{2}}{4 m R}\left(1-\frac{G m^{2}}{k Q^{2}}\right)}$
- **(C)** $\sqrt{\frac{k Q^{2}}{2 m R}\left(1-\frac{G m^{2}}{2 k Q^{2}}\right)}$
- **(D)** $\sqrt{\frac{k Q^{2}}{4 m R}\left(1+\frac{G m^{2}}{k Q^{2}}\right)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{\frac{k Q^{2}}{4 m R}\left(1-\frac{G m^{2}}{k Q^{2}}\right)}$**

**Detailed Solution:**

Using energy conservation, the system's kinetic energy must overcome the increase in electrostatic potential energy as the spheres approach.
Initial state: separation 4R, speed u each.
Final state: touching (separation 2R), speed zero.
Change in potential energy: $\Delta U = k\frac{Q^2}{2R} - k\frac{Q^2}{4R} = k\frac{Q^2}{4R}$.
Initial kinetic energy: $KE_i = mu^2$.
Energy equation: $mu^2 = k\frac{Q^2}{4R}\left(1 - \frac{Gm^2}{kQ^2}\right)$.
Therefore, $u = \sqrt{\frac{kQ^2}{4mR}\left(1 - \frac{Gm^2}{kQ^2}\right)}$.

</details>

---

### Q12. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A point charge of $10^{-8} \mathrm{C}$ is placed at origin. The work done in moving a point charge $2 \mu \mathrm{C}$ from point $A(4,4,2) \mathrm{m}$ to $B(2,2,1) \mathrm{m}$ is $\_\_\_\_$ J. $\left(\frac{1}{4 \pi \epsilon_{o}}=9 \times 10^{9}\right.$ in SI units $)$

**Options:**

- **(A)** $45 \times 10^{-6}$
- **(B)** $15 \times 10^{-6}$
- **(C)** 0
- **(D)** $30 \times 10^{-6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $30 \times 10^{-6}$**

**Detailed Solution:**

Distance from origin to A: $r_A = \sqrt{4^2 + 4^2 + 2^2} = 6$ m
Distance from origin to B: $r_B = \sqrt{2^2 + 2^2 + 1^2} = 3$ m
Work done: $W = q_2(V_B - V_A) = q_2 \times \frac{q_1}{4\pi\varepsilon_0}\left(\frac{1}{r_B} - \frac{1}{r_A}\right)$
$= 2 \times 10^{-6} \times 9 \times 10^9 \times 10^{-8} \times \left(\frac{1}{3} - \frac{1}{6}\right)$
$= 18 \times 10^{-5} \times \frac{1}{6} = 30 \times 10^{-6}$ J

</details>

---

### Q13. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason $\mathrm{R}$ Assertion A : Work done in moving a test charge between two points inside a uniformly charged spherical shell is zero, no matter which path is chosen.
Reason $\mathrm{R}$ : Electrostatic potential inside a uniformly charged spherical shell is constant and is same as that on the surface of the shell. In the light of the above statements, choose the correct answer from the options given below

**Options:**

- **(A)** $\mathrm{A}$ is true but $\mathrm{R}$ is false
- **(B)** Both $\mathrm{A}$ and $\mathrm{R}$ are true and $\mathrm{R}$ is the correct explanation of $\mathrm{A}$
- **(C)** $\mathrm{A}$ is false but $\mathrm{R}$ is true
- **(D)** Both $\mathrm{A}$ and $\mathrm{R}$ are true but $\mathrm{R}$ is NOT the correct explanation of $\mathrm{A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Both $\mathrm{A}$ and $\mathrm{R}$ are true and $\mathrm{R}$ is the correct explanation of $\mathrm{A}$**

**Detailed Solution:**

For a uniformly charged spherical shell:
- The electric field inside the shell is zero everywhere (from Gauss's law)
* When the electric field is zero, no work is done in moving a charge
- Since work - force $\times$ displacement, and force - q̧E (where E - 0), work - 0
- The potential inside is constant and equal to the value at the surface
Assertion A is correct: Since the electric field is zero everywhere inside the shell, no work is done moving a charge between any two points, regardless of path.
Reason R is correct: The potential inside a uniformly charged spherical shell is indeed constant and equal to the value at the surface.
Does R explain $A$ ? Yes, because:
- Constant potential means zero electric field (since $\mathrm{E}=-\mathrm{FW}$)
- Zero electric field means no force on a test charge
- No force means no work done in moving the charge
Therefore, opxion (2) is correct: Both A and R are true and R is the correct explanation of A.

</details>

---

### Q14. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two charges $\mathrm{q}_1$ and $\mathrm{q}_2$ are separated by a distance of 30 cm. A third charge $q_3$ initially at ' C ' as shown in the figure, is moved along the circular path of radius 40 cm from C to D. If the difference in potential energy due to movement of $q_3$ from $C$ to $D$ is given by $\frac{\mathrm{q}_3 \mathrm{~K}}{4 \pi \epsilon_0}$, the value of K is :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/LrbTO9WzxnPZTVtmm9Hblrkh8kwL7NDDzg4jb1XHKxE.original.fullsize.png"/>

**Options:**

- **(A)** $8 \mathrm{q}_2$
- **(B)** $6 \mathrm{q}_2$
- **(C)** $8 q_1$
- **(D)** $6 \mathrm{q}_1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $8 \mathrm{q}_2$**

**Detailed Solution:**

Potential at C
$\mathrm{V}_{\mathrm{C}}=\frac{\mathrm{kq}_1}{0.4}+\frac{\mathrm{kq}_2}{0.5}$
Potential at D
$\mathrm{V}_{\mathrm{D}}=\frac{\mathrm{kq}_1}{0.4}+\frac{\mathrm{kq}_2}{0.1}$
$\Delta \mathrm{U}=\left(\mathrm{V}_{\mathrm{D}}-\mathrm{V}_{\mathrm{c}}\right)\left(\mathrm{q}_3\right)=\left(\frac{\mathrm{kq}_2}{0.1}-\frac{\mathrm{kq}_2}{0.5}\right)\left(\mathrm{q}_3\right)$
$\Delta \mathrm{U}=8 \mathrm{kq}_2 \mathrm{q}_3=\frac{8 \mathrm{q}_2 \mathrm{q}_3}{4 \pi \varepsilon_0}$

</details>

---

### Q15. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A metallic ring is uniformly charged as shown in figure. AC and BD are two mutually perpendicular diameters. Electric field due to $\operatorname{arc} \mathrm{AB}$ to ' O ' is ' E ' is magnitude. What would be the magnitude of electric field at ' O ' due to arc ABC ?
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/JNnY13ocXIf14XuxPFPx_pTcXxrNwiBW0QiI2RowQhc.original.fullsize.png"/>

**Options:**

- **(A)** 2 E
- **(B)** $\sqrt{2} \mathrm{E}$
- **(C)** $\mathrm{E} / 2$
- **(D)** Zero

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{2} \mathrm{E}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bOgV_ysFuaZml1i3pzWZisDzInYn4kplUHN_9oqIPEM.original.fullsize.png"/>

</details>

---

### Q16. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two small spherical balls of mass 10 g each with charges $-2 \mu \mathrm{C}$ and $2 \mu \mathrm{C}$, are attached to two ends of very light rigid rod of length 20 cm. The arrangement is now placed near an infinite nonconducting charge sheet with uniform charge density of $100 \mu \mathrm{C} / \mathrm{m}^2$ such that length of rod makes an angle of $30^{\circ}$ with electric field generated by charge sheet. Net torque acting on the rod is:
(Take $\varepsilon_0: 8.85 \times 10^{-12} \mathrm{C}^2 / \mathrm{Nm}^2$)

**Options:**

- **(A)** 112 Nm
- **(B)** 1.12 Nm
- **(C)** 2.24 Nm
- **(D)** 11.2 Nm

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1.12 Nm**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ag2WDdcT1Ga5RNkKc538jDdq7OrsfxQ8SrysJhBfmQs.original.fullsize.png"/>
$\begin{aligned} \mathrm{E} & =\frac{\sigma}{2 \varepsilon_0} \\ \tau & =\mathrm{PE} \sin \theta\end{aligned}$
$\begin{aligned} & =\left[\left(2 \times 10^{-6}\right)\left(\frac{2}{10}\right)\right]\left[\frac{100 \times 10^{-6}}{2 \times 8.85 \times 10^{-12}}\right]\left(\frac{1}{2}\right) \\ & =\frac{10}{8.85}=1.12 \mathrm{Nm}\end{aligned}$

</details>

---

### Q17. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The electrostatic potential on the surface of uniformly charged spherical shell of radius $\mathrm{R}=10 \mathrm{~cm}$ is 120 V. The potential at the centre of shell, at a distance $\mathrm{r}=5 \mathrm{~cm}$ from centre, and at a distance $\mathrm{r}=15 \mathrm{~cm}$ from the centre of the shell respectively, are :

**Options:**

- **(A)** $120 \mathrm{~V}, 120 \mathrm{~V}, 80 \mathrm{~V}$
- **(B)** $40 \mathrm{~V}, 40 \mathrm{~V}, 80 \mathrm{~V}$
- **(C)** $0 \mathrm{~V}, 0 \mathrm{~V}, 80 \mathrm{~V}$
- **(D)** $0 \mathrm{~V}, 120 \mathrm{~V}, 40 \mathrm{~V}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $120 \mathrm{~V}, 120 \mathrm{~V}, 80 \mathrm{~V}$**

**Detailed Solution:**

Potential inside shell is equal to potential on surface
$\mathrm{V}_{\mathrm{in}}=\mathrm{V}_{\text {surface }}=\frac{\mathrm{kQ}}{\mathrm{R}}=120 \mathrm{~V}$
at $\mathrm{r}=15 \mathrm{~cm}$
$\mathrm{V}=\frac{\mathrm{kQ}}{\mathrm{r}}=\frac{120 \times 10}{15}=80 \mathrm{~V}$

</details>

---

### Q18. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Consider a circular loop that is uniformly charged and has a radius $\mathrm{a} \sqrt{2}$. Find the position along the positive z -axis of the cartesian coordinate system where the electric field is maximum if the ring was assumed to be placed in xy-plane at the origin :

**Options:**

- **(A)** $\frac{a}{\sqrt{2}}$
- **(B)** $\frac{a}{2}$
- **(C)** a
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) a**

**Detailed Solution:**

$\begin{aligned} & \mathrm{E}=\frac{\mathrm{KQr}}{\left(\mathrm{x}^2+\mathrm{R}^2\right)^{3 / 2}} \\ & \frac{\mathrm{dE}}{\mathrm{dx}}=0 \\ & \therefore \mathrm{x}=\frac{\mathrm{R}}{\sqrt{2}}=\frac{\sqrt{2} \mathrm{a}}{\sqrt{2}}=\mathrm{a}\end{aligned}$

</details>

---

### Q19. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two large plane parallel conducting plates are kept 10 cm apart as shown in figure. The potential difference between them is $V$. The potential difference between the points A and B (shown in the figure) is :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Yy-KGTzPVqw_1y8atbiVCX300fB0JDfzKm5eZjSNPEI.original.fullsize.png"/>

**Options:**

- **(A)** $\frac{1}{4} \mathrm{~V}$
- **(B)** $\frac{2}{5} \mathrm{~V}$
- **(C)** $\frac{3}{4} \mathrm{~V}$
- **(D)** 1 V

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{5} \mathrm{~V}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/nxqOK_1IqcUUDYExPxsyF6lnsl2EEk-2FHNzYZJvKAo.original.fullsize.png"/>
$\begin{aligned} & \text { Using } \Delta V=E(\Delta d) \\ & V=E(10) \\ & V_{A B}=E \cdot 4=\frac{V}{10} \times 4=\frac{2 V}{5}\end{aligned}$

</details>

---

### Q20. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Match List - I with List - II.
\(\begin{array}{l|l}
\text { List - I } & \text { List - II } \\
\hline \text { (A) }\begin{array}{l}
\text { Electric field inside (distance } r&gt;0 \text { from center) } \\
\text { of a uniformly charged spherical shell with } \\
\text { surface charge density } \sigma \text {, and radius R. }
\end{array} & \text { (I) } \begin{array}{l}
\sigma / \epsilon_0
\end{array} \\
\text { (B) } \begin{array}{l}
\text { Electric field at distance r&gt;0 from a uniformly } \\
\text { charged infinite plane sheet with surface } \\
\text { charge density } \sigma .
\end{array} & \text { (II) } \sigma / 2 \epsilon_0 \\
\text { (C) } \begin{array}{l}
\text { Electric field outside (distance r&gt;0 from center) } \\
\text { of a uniformly charged spherical shell with } \\
\text { surface charge density } \sigma \text {, and radius R. }
\end{array} & \text { (III) } 0 \\
\text { (D) } \begin{array}{l}
\text { Electric field between } 2 \text { oppositely charged } \\
\text { infinite plane parallel sheets with uniform } \\
\text { surface charge density } \sigma .
\end{array} & \text { (IV) } \frac{\sigma R^2}{\epsilon_0 r^2}
\end{array}\)
Choose the correct answer from the options given below :

**Options:**

- **(A)** (A)-(III), (B)-(II), (C)-(IV), (D)-(I)
- **(B)** (A)-(IV), (B)-(II), (C)-(III), (D)-(I)
- **(C)** (A)-(II), (B)-(I), (C)-(IV), (D)-(III)
- **(D)** (A)-(IV), (B)-(I), (C)-(III), (D)-(II)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) (A)-(III), (B)-(II), (C)-(IV), (D)-(I)**

**Detailed Solution:**

Inside uniformly charged spherical shell, $E=0$
$\therefore \mathrm{A} \rightarrow \mathrm{III}$

For uniformly charged infinite plate
$E=\frac{\sigma}{2 \varepsilon_0}$
$\therefore \mathrm{B} \rightarrow \mathrm{II}$

Outside of spherical shell
$E=\frac{Q}{4 \pi \varepsilon_0 r_2}=\frac{\sigma R^2}{\varepsilon_0 r^2}$
$\therefore \mathrm{C} \rightarrow \mathrm{IV}$

Between two plates $E=\frac{\sigma}{\varepsilon_0}$
$\therefore \mathrm{D} \rightarrow \mathrm{I}$

</details>

---

### Q21. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Three infinitely long wires with linear charge density $\lambda$ are placed along the $x-a x i s, y$-axis and $z-$ axis respectively. Which of the following denotes an equipotential surface?

**Options:**

- **(A)** $x y z=$ constant
- **(B)** $x y+y z+z x=$ constant
- **(C)** $\left(x^2+y^2\right)\left(y^2+z^2\right)\left(z^2+x^2\right)=$ constant
- **(D)** $(x+y)(y+z)(z+x)=$ constant

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(x^2+y^2\right)\left(y^2+z^2\right)\left(z^2+x^2\right)=$ constant**

**Detailed Solution:**

Potential due to an infinite wire is $V=2 k \lambda \ln r$, where $r$ is the distance from the wire.

Taking the point in space $P(x, y, z)$
Distance from wire along $x$-axis is $r_x=\sqrt{y^2+z^2}$
Distance from wire along $y$-axis is $r_y=\sqrt{x^2+z^2}$
Distance from wire along $z$-axis is $r_z=\sqrt{x^2+y^2}$
$\Rightarrow$ Potential at $P$ due to wire along $x$-axis is
$V_x=2 k \lambda \ln r_x$

Potential at $P$ due to wire along $y$-axis is
$V_y=2 k \lambda \ln r_y$

Potential at $P$ due to wire along $z$-axis is
$V_z=2 k \lambda \ln r_z$
$\Rightarrow$ Not potential at $P=V=V_x+V_y+V_z$
or $\quad V=2 k \lambda \ln r_x+2 k \lambda \ln r_y+2 k \lambda \ln r_z$
i.e. $V=2 k \lambda \ln \left(r_x r_y r_z\right)$
or
$\begin{aligned}
& V=2 k \lambda \ln \left(\sqrt{y^2+z^2} \sqrt{z^2+x^2} \sqrt{x^2+y^2}\right) \\
& =k \lambda \ln \left(y^2+z^2\right)\left(z^2+x^2\right)\left(x^2+y^2\right)
\end{aligned}$
$\Rightarrow$ For equipotential surface
$\left(x^2+y^2\right)\left(y^2+z^2\right)\left(z^2+x^2\right)=\text { constant }$

</details>

---

### Q22. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<img src="https://cdn.quizrr.in/question-assets/jee_main_pyq/Ao5joBsvmCmQZX4Y4M62dbHDKgfFwj21dBe8nz7pVEE.original.fullsize_2.png"/>
In the first configuration (1) as shown in the figure, four identical charges \(\left(q_0\right)\) are kept at the corners \(A, B, C\) and \(D\) of square of side length 'a'. In the second configuration (2), the same charges are shifted to mid points \(\mathrm{G}, \mathrm{E}, \mathrm{H}\) and F, of the square, If \(\mathrm{K}=\frac{1}{4 \pi \varepsilon_0}\), the difference between the potential energies of configuration (2) and (1) is given by :

**Options:**

- **(A)** $\frac{K q_0^2}{\mathrm{a}}(4-2 \sqrt{2})$
- **(B)** $\frac{K q_0^2}{\mathrm{a}}(3-\sqrt{2})$
- **(C)** $\frac{\mathrm{Kq}_0^2}{\mathrm{a}}(4 \sqrt{2}-2)$
- **(D)** $\frac{\mathrm{Kq}_0^2}{\mathrm{a}}(3 \sqrt{2}-2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\mathrm{Kq}_0^2}{\mathrm{a}}(3 \sqrt{2}-2)$**

**Detailed Solution:**

$\begin{aligned}
& u_{\oplus}=\left(2 \frac{K q_0}{a}+\frac{K q_0}{\sqrt{2} a}\right) q_0 \times 2 \\
& u_0=\left(2 \frac{K q_0 \sqrt{2}}{a}+\frac{K q_0}{a}\right) q_0 \times 2
\end{aligned}$
$\begin{aligned}
& \text { So, } \quad \Delta u=u_2-u_1=2 q_0 \frac{k q_0}{a}\left[2 \sqrt{2}+1-2-\frac{1}{\sqrt{2}}\right] \\
& \Rightarrow \quad \Delta u=\frac{2 q_0^2}{4 \pi \varepsilon_0 a}\left[\frac{4-\sqrt{2}-1}{\sqrt{2}}\right]=\frac{2 q_0^2}{4 \pi \varepsilon_0 a} \frac{(3-\sqrt{2})}{\sqrt{2}} \\
& \Rightarrow \quad \Delta u=\frac{2 k q_0^2}{a}\left[\frac{3-\sqrt{2}}{\sqrt{2}}\right]=\frac{k q_0^2}{a}(3 \sqrt{2}-2)
\end{aligned}$

</details>

---

### Q23. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two charges $7 \mu \mathrm{c}$ and $-4 \mu \mathrm{c}$ are placed at $(-7 \mathrm{~cm}, 0,0)$ and $(7 \mathrm{~cm}, 0,0)$ respectively. Given, $\epsilon_0=8.85 \times 10^{-12} \mathrm{C}^2 \mathrm{~N}^{-1} \mathrm{~m}^{-2}$, the electrostatic potential energy of the charge configuration is :

**Options:**

- **(A)** -1.8 J
- **(B)** -2.0 J
- **(C)** -1.5 J
- **(D)** -1.2 J

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -1.8 J**

**Detailed Solution:**

P.E. of two charges
$\begin{aligned}
& \mathrm{u}=\frac{1}{4 \pi \varepsilon_0} \frac{\mathrm{q}_1 \mathrm{q}_2}{\mathrm{r}} \\
& \mathrm{r}=\sqrt{\left(\mathrm{x}_2-\mathrm{x}_1\right)^2+\left(\mathrm{y}_2-\mathrm{y}_1\right)^2+\left(\mathrm{z}_2-\mathrm{z}_1\right)^2} \\
& =14 \mathrm{~cm} \\
& \therefore \mathrm{u}=\frac{9 \times 10^9 \times 7 \times 10^{-6} \times(-4) \times 10^{-6}}{14 \times 10^{-2}} \\
& =-1.8 \mathrm{~J}
\end{aligned}$

</details>

---

### Q24. JEE Main 2024 (09 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

At the centre of a half ring of radius $\mathrm{R}=10 \mathrm{~cm}$ and linear charge density $4 \mathrm{n} \mathrm{C} \mathrm{m}^{-1}$, the potential is $x \pi \mathrm{V}$. The value of $x$ is _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **36**

**Detailed Solution:**

Potential at centre of half ring
$\begin{aligned} & V=\frac{K Q}{R} \\ & V=\frac{K \lambda \pi R}{R} \\ & V=K \lambda \pi \Rightarrow V=9 \times 10^9 \times 4 \times 10^{-9} \pi \\ & V=36 \pi\end{aligned}$

</details>

---

### Q25. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two charged conducting spheres of radii $a$ and $b$ are connected to each other by a conducting wire. The ratio of charges of the two spheres respectively is:

**Options:**

- **(A)** $\frac{a}{b}~v$
- **(B)** $\sqrt{a b}$
- **(C)** $\frac{b}{a}$
- **(D)** $a b$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{a}{b}~v$**

**Detailed Solution:**

Potential at surface will be same
$\begin{aligned} & \frac{\mathrm{Kq}_1}{\mathrm{a}}=\frac{\mathrm{Kq}_2}{\mathrm{~b}} \\ & \frac{\mathrm{q}_1}{\mathrm{q}_2}=\frac{\mathrm{a}}{\mathrm{b}}\end{aligned}$

</details>

---

### Q26. JEE Main 2024 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>The distance between charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>q</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>l</mi></math> and between <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mn>2</mn><mi>q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>q</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>l</mi></math>. The electrostatic potential at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> from centre <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>α</mi><mfenced close="]" open="["><mfrac><mrow><mi>q</mi><mi>l</mi></mrow><msup><mi>r</mi><mn>2</mn></msup></mfrac></mfenced><mo>×</mo><msup><mn>10</mn><mn>9</mn></msup><mo> </mo><mi mathvariant="normal">V</mi></math>, where the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math> is ______. (Use <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><mi>π</mi><msub><mi>ε</mi><mn>0</mn></msub></mrow></mfrac><mo>=</mo><mn>9</mn><mo>×</mo><msup><mn>10</mn><mn>9</mn></msup><mo> </mo><mi mathvariant="normal">N</mi><mo> </mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo> </mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>)</p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f7d1ac28-d957-44f9-bd2c-1b977c35d1f0.png" style="width: 350px; height: 186px;"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **27**

**Detailed Solution:**

<p>Considering two dipoles with charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>q</mi><mo> </mo><mo>&amp;</mo><mo> </mo><mi>q</mi></math>, we can write the equivalent setup as shown below:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c57f78f6-26e2-4447-b6ca-0fdb6d335b5c.png" style="width: 400px; height: 150px;"/></p><p>Therefore, net dipole moment is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub><mo>=</mo><mn>6</mn><mi>q</mi><mi>l</mi></math> in the leftward direction.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4f326f6c-3c5f-4122-9eaf-71c7707d2c9f.png" style="width: 250px; height: 199px;"/></p><p>Potential required, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mrow><mi>K</mi><mover><mi>p</mi><mo>→</mo></mover><mo>·</mo><mover><mi>r</mi><mo>→</mo></mover></mrow><msup><mi>r</mi><mn>3</mn></msup></mfrac><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mrow><mn>9</mn><mo>×</mo><msup><mn>10</mn><mn>9</mn></msup><mfenced><mrow><mn>6</mn><mi>q</mi><mi mathvariant="script">l</mi></mrow></mfenced></mrow><msup><mi>r</mi><mn>2</mn></msup></mfrac><mi>cos</mi><mfenced><msup><mn>120</mn><mi mathvariant="normal">o</mi></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>−</mo><mfenced><mn>27</mn></mfenced><mfenced><mfrac><mrow><mi>q</mi><mi mathvariant="script">l</mi></mrow><msup><mi>r</mi><mn>2</mn></msup></mfrac></mfenced><mo>×</mo><msup><mn>10</mn><mn>9</mn></msup></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mn>27</mn></math>.</p>

</details>

---

### Q27. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The electrostatic potential due to an electric dipole at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> varies as :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>r</mi><mn>2</mn></msup></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>r</mi><mn>3</mn></msup></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>r</mi></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>r</mi><mn>2</mn></msup></mfrac></math>**

**Detailed Solution:**

<p>The potential at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> due to a short dipole is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mrow><mi>d</mi><mi>i</mi><mi>p</mi></mrow></msub><mfenced><mi>r</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>π</mi><msub><mi>ε</mi><mo>∘</mo></msub></mrow></mfrac><mo> </mo><mfrac><mrow><mover><mi>p</mi><mo>→</mo></mover><mo>·</mo><mover><mi>r</mi><mo>^</mo></mover></mrow><msup><mi>r</mi><mn>2</mn></msup></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>→</mo></mover></math>=dipole moment.</p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mrow><mi>d</mi><mi>i</mi><mi>p</mi></mrow></msub><mo>(</mo><mi>r</mi><mo>)</mo></math> is proportional to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>r</mi><mn>2</mn></msup></mfrac></math>.</p>

</details>

---

### Q28. JEE Main 2024 (27 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>The electric potential at the surface of an atomic nucleus <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>Z</mi><mo>=</mo><mn>50</mn><mo>)</mo></math> of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>13</mn></mrow></msup><mo> </mo><mi>cm</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>×</mo><msup><mn>10</mn><mn>6</mn></msup><mo> </mo><mi mathvariant="normal">V</mi></math>. What is the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math>?</p><p>(Charge of proton <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>6</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>19</mn></mrow></msup><mo> </mo><mi mathvariant="normal">C</mi></math>)</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p>The electric potential at the surface of an atomic nucleus can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mrow><mi>k</mi><mi>Q</mi></mrow><mi>R</mi></mfrac><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mrow><mi>k</mi><mo>·</mo><mfenced><mrow><mi>Z</mi><mi>e</mi></mrow></mfenced></mrow><mi>R</mi></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>From equation (1), it follows that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mi>V</mi></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mrow><mn>9</mn><mo>×</mo><msup><mn>10</mn><mn>9</mn></msup><mo>×</mo><mn>50</mn><mo>×</mo><mn>1</mn><mo>.</mo><mn>6</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>19</mn></mrow></msup></mrow><mrow><mn>9</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>13</mn></mrow></msup><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfrac><mo> </mo><mi mathvariant="normal">V</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mn>8</mn><mo>×</mo><msup><mn>10</mn><mn>6</mn></msup><mo> </mo><mi mathvariant="normal">V</mi></mtd></mtr></mtable></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mn>8</mn></math>.</p>

</details>

---

### Q29. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

An electric charge <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mo> </mo><mi>μ</mi><mi mathvariant="normal">C</mi></math> is placed at origin <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo> </mo><mn>0</mn><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">X</mi><mo>-</mo><mi mathvariant="normal">Y</mi></math> co-ordinate system. Two points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> are situated at <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msqrt><mn>3</mn></msqrt><mo>,</mo><mo> </mo><msqrt><mn>3</mn></msqrt><mo>)</mo><mo> </mo><mi mathvariant="normal">m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msqrt><mn>6</mn></msqrt><mo>,</mo><mo> </mo><mn>0</mn><mo>)</mo><mo> </mo><mi mathvariant="normal">m</mi></math> respectively. The potential difference between the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> will be :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mo> </mo><mi mathvariant="normal">V</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>6</mn></msqrt><mo> </mo><mi mathvariant="normal">V</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo> </mo><mi mathvariant="normal">V</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo> </mo><mi mathvariant="normal">V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo> </mo><mi mathvariant="normal">V</mi></math>**

**Detailed Solution:**

<p>The formula to calculate the potential difference between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∆</mo><mi>V</mi><mo>=</mo><mi>k</mi><mi>q</mi><mfenced><mrow><mfrac><mn>1</mn><msub><mi>r</mi><mn>1</mn></msub></mfrac><mo>-</mo><mfrac><mn>1</mn><msub><mi>r</mi><mn>2</mn></msub></mfrac></mrow></mfenced><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>r</mi><mn>1</mn></msub></mtd><mtd><mo>=</mo></mtd><mtd><msqrt><mo>(</mo><msqrt><mn>3</mn></msqrt><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><msqrt><mn>3</mn></msqrt><msup><mo>)</mo><mn>2</mn></msup></msqrt><mo> </mo><mi mathvariant="normal">m</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><msqrt><mn>6</mn></msqrt><mo> </mo><mi mathvariant="normal">m</mi></mtd></mtr></mtable></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>r</mi><mn>2</mn></msub></mtd><mtd><mo>=</mo></mtd><mtd><msqrt><mo>(</mo><msqrt><mn>6</mn></msqrt><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>0</mn></msqrt><mo> </mo><mi mathvariant="normal">m</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><msqrt><mn>6</mn></msqrt><mo> </mo><mi mathvariant="normal">m</mi></mtd></mtr></mtable></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><msqrt><mn>6</mn></msqrt><mo> </mo><mi mathvariant="normal">m</mi></math> and the value of the charge remains constant, the potential difference between the points is zero.</p>

</details>

---

### Q30. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math> is the gravitational potential due to sphere of uniform density on its surface, then its value at the centre of sphere will be:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi>V</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>V</mi><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>V</mi></mrow><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>V</mi></mrow><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>The magnitude of gravitational potential of a solid sphere at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> from the centre is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi>G</mi><mi>M</mi></mrow><mrow><mn>2</mn><msup><mi>R</mi><mn>3</mn></msup></mrow></mfrac><mo>(</mo><mn>3</mn><msup><mi>R</mi><mn>2</mn></msup><mo>-</mo><msup><mi>r</mi><mn>2</mn></msup><mo>)</mo></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mi>R</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi>G</mi><mi>M</mi></mrow><mi>R</mi></mfrac></math>.</p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>&#39;</mo><mo>=</mo><mfrac><mrow><mo>-</mo><mi>G</mi><mi>M</mi></mrow><mrow><mn>2</mn><msup><mi>R</mi><mn>3</mn></msup></mrow></mfrac><mo>(</mo><mn>3</mn><msup><mi>R</mi><mn>2</mn></msup><mo>)</mo><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mi>G</mi><mi>M</mi></mrow><mrow><mn>2</mn><mi>R</mi></mrow></mfrac></math></p><p>Clearly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>&#39;</mo><mo>=</mo><mfrac><mrow><mn>3</mn><mi>V</mi></mrow><mn>2</mn></mfrac></math>.</p></blockquote>

</details>

---

### Q31. JEE Main 2023 (10 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Three concentric spherical metallic shells <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>,</mo><mo>&#160;</mo><mi>Y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi></math> of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> respectively <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>a</mi><mo>&#60;</mo><mi>b</mi><mo>&#60;</mo><mi>c</mi></mrow></mfenced></math> have surface charge densities <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#963;</mi><mo>,</mo><mo>&#160;</mo><mo>&#8211;</mo><mo>&#160;</mo><mi>&#963;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#963;</mi></math>, respectively. The shells <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi></math> are at same potential. If the radii of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>Y</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>cm</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi>cm</mi></math>, respectively. The radius of shell <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi></math> is _____<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cm</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a825d304-d6c3-4aa6-9113-e50076c9f846.png" style="width: 300px; height: 217px;" /></p><p>The charges on the spheres are</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mi>X</mi></msub><mo>=</mo><mi>&#963;</mi><mn>4</mn><mi>&#960;</mi><msup><mi>a</mi><mn>2</mn></msup><mspace linebreak="newline"></mspace><msub><mi>q</mi><mi>Y</mi></msub><mo>=</mo><mo>-</mo><mi>&#963;</mi><mn>4</mn><mi>&#960;</mi><msup><mi>b</mi><mn>2</mn></msup><mspace linebreak="newline"></mspace><msub><mi>q</mi><mi>Z</mi></msub><mo>=</mo><mi>&#963;</mi><mn>4</mn><mi>&#960;</mi><msup><mi>c</mi><mn>2</mn></msup><mo>&#160;</mo></math></p><p>It is given that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>X</mi></msub><mo>=</mo><msub><mi>V</mi><mi>Z</mi></msub></math></p><p>So, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>q</mi><mi>X</mi></msub><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>a</mi></mrow></mfrac><mo>+</mo><mfrac><msub><mi>q</mi><mi>Y</mi></msub><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>b</mi></mrow></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><msub><mi>q</mi><mi>Z</mi></msub></mstyle><mstyle displaystyle="true"><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>c</mi></mstyle></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><msub><mi>q</mi><mi>X</mi></msub></mstyle><mstyle displaystyle="true"><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>c</mi></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><msub><mi>q</mi><mi>Y</mi></msub></mstyle><mstyle displaystyle="true"><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>c</mi></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><msub><mi>q</mi><mi>Z</mi></msub></mstyle><mstyle displaystyle="true"><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>c</mi></mstyle></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mfrac><mrow><mi>&#963;</mi><mn>4</mn><mi>&#960;</mi><msup><mi>a</mi><mn>2</mn></msup></mrow><mi>a</mi></mfrac><mo>-</mo><mfrac><mstyle displaystyle="true"><mi>&#963;</mi><mn>4</mn><mi>&#960;</mi><msup><mi>b</mi><mn>2</mn></msup></mstyle><mstyle displaystyle="true"><mi>b</mi></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mi>&#963;</mi><mn>4</mn><mi>&#960;</mi><msup><mi>c</mi><mn>2</mn></msup></mstyle><mstyle displaystyle="true"><mi>c</mi></mstyle></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mi>&#963;</mi><mn>4</mn><mi>&#960;</mi><mo>(</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>)</mo></mstyle><mstyle displaystyle="true"><mi>c</mi></mstyle></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>c</mi><mo>(</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>)</mo><mo>=</mo><mo>(</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>)</mo><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>cm</mi><mo>+</mo><mn>3</mn><mo>&#160;</mo><mi>cm</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math></p></blockquote>

</details>

---

### Q32. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Electric potential at a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> due to a point charge of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>. The distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> from the point charge is:
(Assume, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>&#160;</mo><mi>cm</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi>cm</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>9</mn><mo>&#160;</mo><mi>cm</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mo>&#160;</mo><mi>cm</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mo>&#160;</mo><mi>cm</mi></math>**

**Detailed Solution:**

<blockquote><p>The electric potential for a point charge is given by </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mi>Q</mi><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>r</mi></mrow></mfrac></math></p><p>The data given is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>50</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi><mspace linebreak="newline"></mspace><mi mathvariant="normal">Q</mi><mo>=</mo><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">C</mi></math></p><p>So, the distance of the point is </p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mi>Q</mi><mi>V</mi></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#215;</mo><mfrac><mrow><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup></mrow><mn>50</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>9</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>=</mo><mn>90</mn><mo>&#160;</mo><mi>cm</mi></math></p></blockquote>

</details>

---

### Q33. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>For a uniformly charged thin spherical shell, the electric potential <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>V</mi></mfenced></math> radially away from the centre <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>O</mi></mfenced></math> of shell can be graphically represented as</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bbb24b56-cd7e-470b-b5be-66acbb58458a-image.png" style="width: 250px; height: 219px;" /></p>

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/80b01ebf-0a49-4cae-96fa-58ab289d1933.png" style="width: 250px; height: 169px;" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b28714ce-8b98-4533-8f25-96fb07f97c2a.png" style="width: 250px; height: 159px;" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4bd0e424-45d8-492a-bb34-866f8372d341.png" style="width: 250px; height: 167px;" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/81ec1174-a786-42b4-88ea-0a7e42414368.png" style="width: 250px; height: 167px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b28714ce-8b98-4533-8f25-96fb07f97c2a.png" style="width: 250px; height: 159px;" />**

**Detailed Solution:**

<blockquote><p>The potential is constant inside the sphere as the electric field is zero inside the sphere. So, the value is given by </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mi>Q</mi><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>R</mi></mrow></mfrac></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>&#60;</mo><mi>R</mi></math></p><p>The potential at the surface is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mi>Q</mi><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>R</mi></mrow></mfrac></math></p><p>The potential outside the sphere starts decreasing and is given by the formula </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mi>Q</mi><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>r</mi></mrow></mfrac></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>&#62;</mo><mi>R</mi></math></p></blockquote>

</details>

---

### Q34. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following correctly represents the variation of electric potential <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>V</mi><mo>)</mo></math> of a charged spherical conductor of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>R</mi><mo>)</mo></math> with radial distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>r</mi><mo>)</mo></math> from the centre?

**Options:**

- **(A)** <img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/aeebb1bf-c7d4-40c1-b362-5533a45615e7-9895803.PNG" style="width: 226px; height: 150px;" />
- **(B)** <img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4946f2c0-42b1-479c-bbd8-22338be47c08-9895803_1.PNG" style="width: 223px; height: 150px;" />
- **(C)** <img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/63647b99-2e2d-4909-8fe1-6b3f7787dd1a-9895803_2.PNG" style="width: 222px; height: 150px;" />
- **(D)** <img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/aa4e7fac-b97a-4bfc-a612-d9bf6ba4aabe-9895803_3.PNG" style="width: 225px; height: 180px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/63647b99-2e2d-4909-8fe1-6b3f7787dd1a-9895803_2.PNG" style="width: 222px; height: 150px;" />**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/63647b99-2e2d-4909-8fe1-6b3f7787dd1a-9895803_2.PNG" style="width: 222px; height: 150px;" /></p><p>As electric field inside the charged conducting sphere is zero, therefore potential will be constant for the inside part.</p><p>For outside part, electric potential decreases as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mi>r</mi></mfrac></math> and the conducting sphere behaves like a point charge concentrated at the centre. </p>

</details>

---

### Q35. JEE Main 2023 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two isolated metallic solid spheres of radii <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>R</mi></math> are charged such that both have same charge density <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#963;</mi></math> . The spheres are then connected by a thin conducting wire. If the new charge density of the bigger sphere is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mo>'</mo></msup></math>. The ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>&#963;</mi><mo>'</mo></msup><mi>&#963;</mi></mfrac></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>6</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>6</mn></mfrac></math>**

**Detailed Solution:**

<p>Charge and charge density on both isolated metallic solid spheres are show below.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6bed463d-e0f7-4746-99a9-d6323ab0a8bc-9895324.PNG" style="width: 360px; height: 190px;" /></p><p>Let the charges and the charge densities on both the spheres after connected by thin conducting wire be <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>Q</mi><mn>1</mn><mo>&#39;</mo></msubsup><mo>,</mo><mo>&#160;</mo><msubsup><mi>Q</mi><mn>2</mn><mo>&#39;</mo></msubsup><mo>,</mo><mo>&#160;</mo><mi>&#963;</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><msup><mi>&#963;</mi><mo>&#39;</mo></msup></math> as shown below.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0811017f-990a-4640-9fec-da174f927b0c-9895324-1.PNG" style="width: 329px; height: 160px;" /></p><p>Once connected, charge on both the spheres will redistribute such that potentials at the surface of both spheres is the same.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mrow><mi>k</mi><msubsup><mi>Q</mi><mn>1</mn><mo>&#39;</mo></msubsup></mrow><mi>R</mi></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi><msubsup><mi>Q</mi><mn>2</mn><mo>&#39;</mo></msubsup></mrow><mrow><mn>2</mn><mi>R</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msubsup><mi>Q</mi><mn>1</mn><mo>&#39;</mo></msubsup><mrow><mn>4</mn><msub><mi>&#960;&#949;</mi><mn>0</mn></msub><mi mathvariant="normal">R</mi></mrow></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><msubsup><mi>Q</mi><mn>2</mn><mo>&#39;</mo></msubsup></mstyle><mstyle displaystyle="true"><mn>4</mn><mi mathvariant="normal">&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mfenced><mrow><mn>2</mn><mi mathvariant="normal">R</mi></mrow></mfenced></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msubsup><mi>Q</mi><mn>2</mn><mo>&#39;</mo></msubsup><mo>=</mo><mn>2</mn><msubsup><mi>Q</mi><mn>1</mn><mo>&#39;</mo></msubsup></math></p><p>Using charge conservation, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>Q</mi><mn>1</mn><mo>&#39;</mo></msubsup><mo>+</mo><msubsup><mi>Q</mi><mn>2</mn><mo>&#39;</mo></msubsup><mo>=</mo><msub><mi>Q</mi><mn>1</mn></msub><mo>+</mo><msub><mi>Q</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><msubsup><mi>Q</mi><mn>2</mn><mo>&#39;</mo></msubsup><mn>2</mn></mfrac><mo>+</mo><msubsup><mi>Q</mi><mn>2</mn><mo>&#39;</mo></msubsup><mo>=</mo><mn>20</mn><msup><mi>&#960;R</mi><mn>2</mn></msup><mi mathvariant="normal">&#963;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac><msubsup><mi mathvariant="normal">Q</mi><mn>2</mn><mo>&#39;</mo></msubsup><mo>=</mo><mn>20</mn><msup><mi>&#960;R</mi><mn>2</mn></msup><mi mathvariant="normal">&#963;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><msubsup><mi mathvariant="normal">Q</mi><mn>2</mn><mo>&#39;</mo></msubsup><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi><msup><mfenced><mrow><mn>2</mn><mi mathvariant="normal">R</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mrow><mn>20</mn><msup><mi>&#960;R</mi><mn>2</mn></msup><mi mathvariant="normal">&#963;</mi></mrow><mrow><mn>16</mn><msup><mi>&#960;R</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mstyle displaystyle="true"><mi mathvariant="normal">&#963;</mi><mo>&#39;</mo></mstyle><mi mathvariant="normal">&#963;</mi></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></math></p>

</details>

---

### Q36. JEE Main 2023 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>For a charged spherical ball, electrostatic potential inside the ball varies with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>2</mn><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi></math>.</p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> are constant and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> is the distance from the center. The volume charge density inside the ball is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>&#955;</mi><mi>a</mi><mi>&#949;</mi></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is ______.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo></math> permittivity of medium.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<p>As we know, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mi>d</mi><mi>V</mi></mrow><mrow><mi>d</mi><mi>r</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>4</mn><mi>a</mi><mi>r</mi></math></p><p>Now, electric field inside the charged sphere is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>r</mi></mrow><mrow><mn>3</mn><mi>&#949;</mi></mrow></mfrac></math>. </p><p>Comparing both, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#961;</mi><mo>=</mo><mo>-</mo><mn>12</mn><mi>a</mi><mi>&#949;</mi></math>.</p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>12</mn></math>.</p>

</details>

---

### Q37. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A point charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8211;</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">C</mi></math> is moved from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> in a uniform electric field of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup></math> directed along positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis. If coordinates of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>)</mo><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>)</mo><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> respectively, the work done by electric field will be

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1200</mn><mo>&#160;</mo><mi>mJ</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>600</mn><mo>&#160;</mo><mi>mJ</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>600</mn><mo>&#160;</mo><mi>mJ</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1200</mn><mo>&#160;</mo><mi>mJ</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>600</mn><mo>&#160;</mo><mi>mJ</mi></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/76f815ff-80e4-43a0-bf80-c65cbfc02644-9895086.PNG" style="width: 350px; height: 130px;" /></p><p>As electric field is uniform, so force acting on the charged particle will be uniform.</p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>W</mi><mi>E</mi></msub><mo>=</mo><mover><mi>F</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>s</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>q</mi><mover><mi>E</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>s</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mfenced close="]" open="["><mrow><mn>30</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>&#183;</mo><mfenced close="]" open="["><mrow><mfenced><mrow><mn>0</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>-</mo><mfenced><mrow><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>60</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">J</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>600</mn><mo>&#160;</mo><mi>mJ</mi></math></p>

</details>

---

### Q38. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The electric potential at the centre of two concentric half rings of radii <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math>, having same linear charge density <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0aa952ba-0a7a-4ebb-a028-a7c3373b9784-9893914.PNG" style="width: 300px; height: 167px;" />.</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>&#955;</mi></mrow><msub><mo>&#8712;</mo><mn>0</mn></msub></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#955;</mi><mrow><mn>2</mn><msub><mo>&#8712;</mo><mn>0</mn></msub></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#955;</mi><mrow><mn>4</mn><msub><mo>&#8712;</mo><mn>0</mn></msub></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#955;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#955;</mi><mrow><mn>2</mn><msub><mo>&#8712;</mo><mn>0</mn></msub></mrow></mfrac></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0aa952ba-0a7a-4ebb-a028-a7c3373b9784-9893914.PNG" style="width: 300px; height: 167px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>O</mi></msub><mo>=</mo><msub><mi>V</mi><mn>1</mn></msub><mo>+</mo><msub><mi>V</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>V</mi><mi>O</mi></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><msub><mi>&#955;</mi><mn>1</mn></msub><mfenced><mrow><mi>&#960;</mi><msub><mi>R</mi><mn>1</mn></msub></mrow></mfenced></mrow><msub><mi>R</mi><mn>1</mn></msub></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><msub><mi>&#955;</mi><mn>1</mn></msub><mfenced><mrow><mi>&#960;</mi><msub><mi>R</mi><mn>2</mn></msub></mrow></mfenced></mrow><msub><mi>R</mi><mn>2</mn></msub></mfrac><mspace linebreak="newline"/><mo>=</mo><mfrac><mi>&#955;</mi><mrow><mn>2</mn><msub><mi>&#1013;</mi><mn>0</mn></msub></mrow></mfrac></math></p>

</details>

---

### Q39. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Given below are two statements.
<strong>Statement I :</strong> Electric potential is constant within and at the surface of each conductor.</p><p><strong>Statement II :</strong> Electric field just outside a charged conductor is perpendicular to the surface of the conductor at every point.</p><p>In the light of the above statements, choose the most appropriate answer from the options give below.</p>

**Options:**

- **(A)** Both statement I and statement II are correct
- **(B)** Both statement I and statement II are incorrect
- **(C)** Statement I is correct but statement II is incorrect
- **(D)** Statement I is incorrect but and statement II is correct

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Both statement I and statement II are correct**

**Detailed Solution:**

<blockquote><p><strong>Statement - I</strong>: True as body of conductor acts as equipotential surface.</p><p><strong>Statement II:</strong> True, as conductor is equipotential. Tangential component of electric field should be zero. Therefore, electric field should be perpendicular to surface.</p></blockquote>

</details>

---

### Q40. JEE Main 2022 (26 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two uniformly charged spherical conductors <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> of radii <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>mm</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>mm</mi></math> are separated by a distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>cm</mi></math>. If the spheres are connected by a conducting wire, then in equilibrium condition, the ratio of the magnitudes of the electric fields at the surface of the sphere <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> will be

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>1</mn></math>**

**Detailed Solution:**

<blockquote><p>When two conductors are connected by a conducting wire, their potentials become equal. Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>A</mi></msub><mo>=</mo><msub><mi>V</mi><mi>B</mi></msub></math></p><p>The potential of a spherical conductor is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mrow><mi>k</mi><mi>Q</mi></mrow><mi>R</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>k</mi><msub><mi>Q</mi><mi>A</mi></msub></mrow><msub><mi>R</mi><mi>A</mi></msub></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi><msub><mi>Q</mi><mi>B</mi></msub></mrow><msub><mi>R</mi><mi>B</mi></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Q</mi><mo>&#8733;</mo><mi>R</mi></math></p><p>Now the electric field near the surface of the conductor will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mrow><mi>k</mi><mi>Q</mi></mrow><msup><mi>R</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>E</mi><mi>A</mi></msub><msub><mi>E</mi><mi>B</mi></msub></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mrow><mi>k</mi><msub><mi>Q</mi><mi>A</mi></msub></mrow><msubsup><mi>R</mi><mi>A</mi><mn>2</mn></msubsup></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mrow><mi>k</mi><msub><mi>Q</mi><mi>B</mi></msub></mrow><msubsup><mi>R</mi><mi>B</mi><mn>2</mn></msubsup></mfrac></mstyle></mfrac><mo>=</mo><mfrac><msub><mi>R</mi><mi>B</mi></msub><msub><mi>R</mi><mi>A</mi></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>E</mi><mi>A</mi></msub><msub><mi>E</mi><mi>B</mi></msub></mfrac><mo>=</mo><mfrac><mn>10</mn><mn>5</mn></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>1</mn></mfrac></math></p></blockquote>

</details>

---

### Q41. JEE Main 2022 (29 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the electric potential at any point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> in space is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></math> volt. The electric field at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> will be :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><msup><mi>Vm</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, directed along positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis.
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><msup><mi>Vm</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, directed along negative <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis.
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><msup><mi>Vm</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, directed along negative <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis.
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><msup><mi>Vm</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, directed along positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><msup><mi>Vm</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, directed along negative <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis.**

**Detailed Solution:**

<p>Electric potential <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></math></p><p>Electric potential and electric field are related as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mo>d</mo><mi>V</mi></mrow><mrow><mo>d</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>6</mn><mi>x</mi></math>.</p><p>At the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>E</mi><mo>=</mo><mo>-</mo><mn>6</mn><mo>&#215;</mo><mn>1</mn><mo>=</mo><mo>-</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Thus, electric field is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> along negative <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8208;</mo></math> axis.</p>

</details>

---

### Q42. JEE Main 2022 (25 Jun Shift 2)

*Type:* `numerical` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math> identical drops are charged at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> each. They combine to form a bigger drop. The potential of the bigger drop will be _____  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">V</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **198**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9e5c9397-1c7c-4a9a-858b-152403dee417-e6eae665-9e1f-4be0-868c-2f49ad6d905c-5d4f6ccf-73e4-43b9-996d-09e857a8186f-image.png" style="width: 250px; height: 140px;" /></p><p>Total volume of the drop will remain unchanged,</p><p>So,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn><mo>&#215;</mo><mfenced><mrow><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msup><mi>r</mi><mn>3</mn></msup></mrow></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msup><mi>R</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>R</mi><mo>=</mo><mn>3</mn><mi>r</mi></math></p><p>Potential of the small drops, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mi>r</mi></mfrac></math></p><p>For bigger drop, potential will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mrow><mi>k</mi><mfenced><mrow><mn>27</mn><mi>q</mi></mrow></mfenced></mrow><mfenced><mrow><mn>3</mn><mi>r</mi></mrow></mfenced></mfrac><mo>=</mo><mn>9</mn><mfenced><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mi>r</mi></mfrac></mfenced><mo>=</mo><mn>9</mn><mo>&#215;</mo><mn>22</mn><mo>=</mo><mn>198</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p>

</details>

---

### Q43. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The two thin coaxial rings, each of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and having charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi mathvariant="normal">Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi mathvariant="normal">Q</mi></math> respectively are separated by a distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math>. The potential difference between the centres of the two rings is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>Q</mi><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><msqrt><msup><mi>s</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></msqrt></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>Q</mi><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><msqrt><msup><mi>s</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></msqrt></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>Q</mi><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><msqrt><msup><mi>s</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></msqrt></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>Q</mi><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><msqrt><msup><mi>s</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></msqrt></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>Q</mi><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><msqrt><msup><mi>s</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></msqrt></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mi>K</mi><mi>Q</mi></mrow><mi>a</mi></mfrac><mo>+</mo><mfrac><mrow><mo>-</mo><mi>K</mi><mi>Q</mi></mrow><msqrt><msup><mi>s</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mi>K</mi><mi>Q</mi></mrow><msqrt><msup><mi>s</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><mfrac><mrow><mo>-</mo><mi>K</mi><mi>Q</mi></mrow><mi>a</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>1</mn></msub><mo>-</mo><msub><mi>V</mi><mn>2</mn></msub><mo>=</mo><mfrac><mi>Q</mi><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><msqrt><msup><mi>s</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></msqrt></mfrac></mrow></mfenced></math></p>

</details>

---

### Q44. JEE Main 2021 (26 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math> similar drops of mercury are maintained at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> each. All these spherical drops combine into a single big drop. The potential energy of the bigger drop is ___________ times that of a smaller drop.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **243**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>27</mn></mfenced><mfenced><mrow><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msup><mi mathvariant="normal">r</mi><mn>3</mn></msup></mrow></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msup><mi mathvariant="normal">R</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>3</mn><mi>r</mi></math></p><p>Potential energy of smaller drop <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>U</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mfrac><mrow><mi>k</mi><msup><mi>q</mi><mn>2</mn></msup></mrow><mi>r</mi></mfrac></math></p><p>Potential energy of bigger drop : <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>U</mi><mo>=</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mfrac><mrow><mi>k</mi><msup><mi>Q</mi><mn>2</mn></msup></mrow><mi>R</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>U</mi><mo>=</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mfrac><mrow><mi>k</mi><msup><mfenced><mrow><mn>27</mn><mi>q</mi></mrow></mfenced><mn>2</mn></msup></mrow><mi>R</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>U</mi><mo>=</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mi>k</mi><mfrac><mrow><mfenced><mn>27</mn></mfenced><mfenced><mn>27</mn></mfenced><msup><mi>q</mi><mn>2</mn></msup></mrow><mrow><mn>3</mn><mi>r</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>U</mi><mo>=</mo><mfrac><mrow><mfenced><mn>27</mn></mfenced><mfenced><mn>27</mn></mfenced></mrow><mn>3</mn></mfrac><mfenced><mrow><mfrac><mn>3</mn><mn>5</mn></mfrac><mfrac><mrow><mi>k</mi><msup><mi>q</mi><mn>2</mn></msup></mrow><mi>r</mi></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>U</mi><mo>=</mo><mn>243</mn><msub><mi>U</mi><mn>1</mn></msub></math></p>

</details>

---

### Q45. JEE Main 2021 (26 Feb Shift 1)

*Type:* `numerical` | *Level:* `1`

In an electrical circuit, a battery is connected to pass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">C</mi></math> of charge through it in a certain given time. The potential difference between two plates of the battery is maintained at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>. The workdone by the battery is _______ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">J</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **300**

**Detailed Solution:**

<p>Work done by battery <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>Q</mi><mfenced><mrow><mi>&#916;</mi><mi>V</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>20</mn><mo>&#215;</mo><mn>15</mn><mo>=</mo><mn>300</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>300</mn></math></p>

</details>

---

### Q46. JEE Main 2021 (25 Feb Shift 1)

*Type:* `numerical` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>512</mn></math> identical drops of mercury are charged to a potential of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> each. The drops are joined to form a single drop. The potential of this drop is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math> in Volt.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **128**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mn>512</mn><mo>&#160;</mo><mi>q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>Volume</mi><msub><mo>&#160;</mo><mi>i</mi></msub><mo>=</mo><mo>&#160;</mo><mi>Volume</mi><msub><mo>&#160;</mo><mi>f</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>512</mn><mo>&#215;</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msup><mi>r</mi><mn>3</mn></msup><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msup><mi>R</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>9</mn></msup><msup><mi>r</mi><mn>3</mn></msup><mo>=</mo><msup><mi>R</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi></mrow><mi>r</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mrow><mi>k</mi><mi>Q</mi></mrow><mi>R</mi></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi><mn>512</mn><mi mathvariant="normal">q</mi></mrow><mrow><mn>8</mn><mi mathvariant="normal">r</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>128</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>.</p>

</details>

---

### Q47. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Ten charges are placed on the circumference of a circle of radius R with constant angular separation between successive charges. Alternate charges<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>9</mn></math> have charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>+</mo><mi>q</mi><mo>)</mo></math> each, while <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>10</mn></math> have charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>&#8211;</mo><mi>q</mi><mo>)</mo></math> each. The potential V and the electric field E at the centre of the circle are respectively : (Take<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>0</mn></math> at infinity)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mrow><mn>10</mn><mi>q</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><mi>R</mi></mrow></mfrac><mo>;</mo><mi>E</mi><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">V</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi mathvariant="normal">E</mi><mo>=</mo><mfrac><mrow><mn>10</mn><mi mathvariant="normal">q</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>V</mi><mo>=</mo><mn>0</mn><mo>;</mo><mo>&#160;</mo><mi>E</mi><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mrow><mn>10</mn><mi>q</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><mi>R</mi></mrow></mfrac><mo>;</mo><mi>E</mi><mo>=</mo><mfrac><mrow><mn>10</mn><mi>q</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>V</mi><mo>=</mo><mn>0</mn><mo>;</mo><mo>&#160;</mo><mi>E</mi><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0016be3b-1f6e-4f93-aacf-9ba5af99a3d9-image.png" style="width: 300px; height: 279px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">v</mi><mi>net</mi></msub><mo>=</mo><mn>5</mn><mfenced><mfrac><mi>kq</mi><mi mathvariant="normal">R</mi></mfrac></mfenced><mo>+</mo><mfenced><mfrac><mrow><mn>5</mn><mi mathvariant="normal">k</mi><mo>(</mo><mo>-</mo><mi mathvariant="normal">q</mi><mo>)</mo></mrow><mi mathvariant="normal">R</mi></mfrac></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">v</mi><mi>net</mi></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfenced close="]" open="["><mrow><msub><mi mathvariant="normal">Q</mi><mi>net</mi></msub><mo>=</mo><mn>0</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">E</mi><mi>net</mi></msub><mo>=</mo><mn>0</mn></math>, by symmetry</p></blockquote>

</details>

---

### Q48. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>A two point charges <math><mrow><mn>4</mn><mi>q</mi></mrow></math> and <math><mrow><mo>&#8211;</mo><mi>q</mi></mrow></math> are fixed on the <math><mi>x</mi></math> -axis at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mo>&#8722;</mo><mi>d</mi></mrow><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>d</mi><mn>2</mn></mfrac></math>, respectively. If the third point charge &lsquo;<math><mi>q</mi></math> &rsquo; is taken from the origin to <math><mrow><mi>x</mi><mo>=</mo><mi>d</mi></mrow></math> along the semicircle as shown in the figure, the energy of the charge will:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8eb1910b-51d4-4276-867b-bdbb013eed2c-image.png" style="width: 231px; height: 140px;" /> </p>

**Options:**

- **(A)** Increase by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msup><mi>q</mi><mn>2</mn></msup></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub><mi>d</mi></mrow></mfrac></math>
- **(B)** Increase by <math><mrow><mfrac><mrow><mn>2</mn><msup><mi>q</mi><mn>2</mn></msup></mrow><mrow><mn>3</mn><mi>&#960;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub><mi>d</mi></mrow></mfrac></mrow></math>
- **(C)** decrease by <math><mrow><mfrac><mrow><msup><mi>q</mi><mn>2</mn></msup></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub><mi>d</mi></mrow></mfrac></mrow></math>
- **(D)** decrease by <math><mrow><mfrac><mrow><mn>4</mn><msup><mi>q</mi><mn>2</mn></msup></mrow><mrow><mn>3</mn><mi>&#960;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub><mi>d</mi></mrow></mfrac></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) decrease by <math><mrow><mfrac><mrow><mn>4</mn><msup><mi>q</mi><mn>2</mn></msup></mrow><mrow><mn>3</mn><mi>&#960;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub><mi>d</mi></mrow></mfrac></mrow></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a776f1b2-a045-46cc-90f3-435930e73241-image.png" style="width: 219px; height: 128px;" /></p><p>Potential at origin <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math>, the potential due to two charges is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn mathvariant="italic">0</mn></msub><mo mathvariant="italic">=</mo><mfrac><mrow><mn mathvariant="italic">4</mn><mi>q</mi></mrow><mrow><mn mathvariant="italic">4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn mathvariant="italic">0</mn></msub><mfenced><mfrac><mi mathvariant="italic">d</mi><mn mathvariant="italic">2</mn></mfrac></mfenced></mrow></mfrac><mo mathvariant="italic">+</mo><mfrac><mfenced><mrow><mo mathvariant="italic">&#8722;</mo><mi>q</mi></mrow></mfenced><mrow><mn mathvariant="italic">4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn mathvariant="italic">0</mn></msub><mfenced><mfrac><mi mathvariant="italic">d</mi><mn mathvariant="italic">2</mn></mfrac></mfenced></mrow></mfrac><mo mathvariant="italic">=</mo><mfrac><mrow><mn mathvariant="italic">6</mn><mi>q</mi></mrow><mrow><mn mathvariant="italic">4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn mathvariant="italic">0</mn></msub><mi>d</mi></mrow></mfrac></math></p><p>Potential at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> at a distance, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>d</mi></math> is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>P</mi></msub><mo mathvariant="italic">=</mo><mfrac><mrow><mn mathvariant="italic">4</mn><mi>q</mi></mrow><mrow><mn mathvariant="italic">4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn mathvariant="italic">0</mn></msub><mfenced><mfrac><mrow><mn mathvariant="italic">3</mn><mi mathvariant="italic">d</mi></mrow><mn mathvariant="italic">2</mn></mfrac></mfenced></mrow></mfrac><mo mathvariant="italic">+</mo><mfrac><mfenced><mrow><mo mathvariant="italic">&#8722;</mo><mi>q</mi></mrow></mfenced><mrow><mn mathvariant="italic">4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn mathvariant="italic">0</mn></msub><mfenced><mfrac><mi mathvariant="italic">d</mi><mn mathvariant="italic">2</mn></mfrac></mfenced></mrow></mfrac><mo mathvariant="italic">=</mo><mfrac><mi>q</mi><mrow><mn mathvariant="italic">6</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn mathvariant="italic">0</mn></msub><mi>d</mi></mrow></mfrac></math></p><p>Change in potential energy due the charge motion of charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> is given by</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">&#8710;</mo><mi>U</mi><mo mathvariant="italic">=</mo><mi>q</mi><mi>&#916;</mi><mi>V</mi><mo mathvariant="italic">=</mo><mi>q</mi><mfenced><mrow><msub><mi>V</mi><mi>f</mi></msub><mo mathvariant="italic">&#8722;</mo><msub><mi>V</mi><mi>i</mi></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">&#8658;</mo><mo mathvariant="italic">&#8710;</mo><mi>U</mi><mo mathvariant="italic">=</mo><mi>q</mi><mfenced><mrow><msub><mi>V</mi><mi>P</mi></msub><mo mathvariant="italic">&#8722;</mo><msub><mi>V</mi><mi>O</mi></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>U</mi><mo>=</mo><mi>q</mi><mfenced><mrow><mfrac><mi>q</mi><mrow><mn>6</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn mathvariant="italic">0</mn></msub><mi>d</mi></mrow></mfrac><mo mathvariant="italic">&#8722;</mo><mfrac><mrow><mn>3</mn><mi>q</mi></mrow><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn mathvariant="italic">0</mn></msub><mi>d</mi></mrow></mfrac></mrow></mfenced><mo mathvariant="italic">=</mo><mo mathvariant="italic">&#8722;</mo><mfrac><mrow><mn>4</mn><msup><mi>q</mi><mn mathvariant="italic">2</mn></msup></mrow><mrow><mn>3</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn mathvariant="italic">0</mn></msub><mi>d</mi></mrow></mfrac></math></p>

</details>

---

### Q49. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Concentric metallic hollow spheres of radii R and 4R hold charges <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">Q</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">Q</mi><mn>2</mn></msub></math> respectively. Given that surface charge densities of the concentric spheres are equal, the potential difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">V</mi><mfenced><mi mathvariant="normal">R</mi></mfenced><mo>-</mo><mi mathvariant="normal">V</mi><mo>(</mo><mn>4</mn><mi mathvariant="normal">R</mi><mo>)</mo></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>Q</mi><mn>2</mn></msub><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>R</mi></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msub><mi mathvariant="normal">Q</mi><mn>2</mn></msub></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>R</mi></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msub><mi mathvariant="normal">Q</mi><mn>1</mn></msub></mrow><mrow><mn>16</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi mathvariant="normal">R</mi></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msub><mi>Q</mi><mn>1</mn></msub></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>R</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msub><mi mathvariant="normal">Q</mi><mn>1</mn></msub></mrow><mrow><mn>16</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi mathvariant="normal">R</mi></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ea6ea7f3-696c-473e-b693-bdc4eda8f804-D764.png" style="width: 180px; height: 214px;" /></p><p>As given the surface charge density for both the spheres is same, hence</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><msub><mi>&#963;</mi><mn>1</mn></msub><mo>=</mo><msub><mi>&#963;</mi><mn>2</mn></msub><mspace linebreak="newline"></mspace><mo>&#8756;</mo><mfrac><msub><mi>Q</mi><mn>1</mn></msub><msub><mi>A</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><msub><mi>Q</mi><mn>2</mn></msub><msub><mi>A</mi><mn>2</mn></msub></mfrac><mo>&#8658;</mo><mfrac><msub><mi>Q</mi><mn>1</mn></msub><mrow><mn>4</mn><mi>&#960;</mi><msup><mi>R</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><msub><mi>Q</mi><mn>2</mn></msub><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi><msup><mfenced><mrow><mn>4</mn><mi mathvariant="normal">R</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mspace linebreak="newline"></mspace><mo>&#8756;</mo><msub><mi mathvariant="normal">Q</mi><mn>2</mn></msub><mo>=</mo><mn>16</mn><msub><mi mathvariant="normal">Q</mi><mn>1</mn></msub></math></p><p>From above diagram, the electric potential for both the spheres is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mi>Inner</mi></msub><mo>=</mo><mfrac><msub><mi>KQ</mi><mn>1</mn></msub><mi mathvariant="normal">R</mi></mfrac><mo>+</mo><mfrac><msub><mi>KQ</mi><mn>2</mn></msub><mrow><mn>4</mn><mi mathvariant="normal">R</mi></mrow></mfrac><mo>=</mo><mfrac><mi mathvariant="normal">K</mi><mi mathvariant="normal">R</mi></mfrac><mfenced><mrow><msub><mi mathvariant="normal">Q</mi><mn>1</mn></msub><mo>+</mo><mfrac><mrow><mn>16</mn><msub><mi mathvariant="normal">Q</mi><mn>1</mn></msub></mrow><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>5</mn><msub><mi>KQ</mi><mn>1</mn></msub></mrow><mi mathvariant="normal">R</mi></mfrac><mo>.</mo><mspace linebreak="newline"></mspace></math></p><p>In the same way for outer sphere, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mi>Outer</mi></msub><mo>=</mo><mfrac><msub><mi>KQ</mi><mn>1</mn></msub><mrow><mn>4</mn><mi mathvariant="normal">R</mi></mrow></mfrac><mo>+</mo><mfrac><msub><mi>KQ</mi><mn>2</mn></msub><mrow><mn>4</mn><mi mathvariant="normal">R</mi></mrow></mfrac><mo>=</mo><mfrac><mi mathvariant="normal">K</mi><mrow><mn>4</mn><mi mathvariant="normal">R</mi></mrow></mfrac><mfenced><mrow><mn>16</mn><msub><mi mathvariant="normal">Q</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">Q</mi><mn>1</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>17</mn><msub><mi>KQ</mi><mn>1</mn></msub></mrow><mrow><mn>4</mn><mi mathvariant="normal">R</mi></mrow></mfrac></math>.</p><p>Now the potential difference is,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi mathvariant="normal">V</mi><mo>=</mo><msub><mi mathvariant="normal">V</mi><mi>inner</mi></msub><mo>-</mo><msub><mi mathvariant="normal">V</mi><mi>outer</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>5</mn><msub><mi>KQ</mi><mn>1</mn></msub></mrow><mi mathvariant="normal">R</mi></mfrac><mo>-</mo><mfrac><mrow><mn>17</mn><msub><mi>KQ</mi><mn>1</mn></msub></mrow><mrow><mn>4</mn><mi mathvariant="normal">R</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><msub><mi mathvariant="normal">Q</mi><mn>1</mn></msub></mrow><mrow><mn>16</mn><msub><mi>&#960;&#949;</mi><mn>0</mn></msub><mi mathvariant="normal">R</mi></mrow></mfrac></math>.</p>

</details>

---

### Q50. JEE Main 2020 (08 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Consider two charged metallic spheres <math><msub><mrow><mi>S</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi>S</mi></mrow><mrow><mn>2</mn></mrow></msub></math> of radii <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi></mi></math> respectively. The electric fields <math><msub><mrow><mi>E</mi></mrow><mrow><mn>1</mn></mrow></msub></math> (on <math><msub><mrow><mi>S</mi></mrow><mrow><mn>1</mn></mrow></msub></math> ) and <math><msub><mrow><mi>E</mi></mrow><mrow><mn>2</mn></mrow></msub></math> (on <math><msub><mrow><mi>S</mi></mrow><mrow><mn>2</mn></mrow></msub></math> ) on their surfaces are such that <math><mfrac><mrow><msub><mrow><mi>E</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>E</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>.</mo></math> Then the ratio <math><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub></math> (on <math><msub><mrow><mi>S</mi></mrow><mrow><mn>1</mn></mrow></msub></math> )<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>/</mo></math><math><msub><mrow><mi>V</mi></mrow><mrow><mn>2</mn></mrow></msub></math> (on <math><msub><mrow><mi>S</mi></mrow><mrow><mn>2</mn></mrow></msub></math> ) of the electrostatic potentials on each sphere is:

**Options:**

- **(A)** <math><mfrac><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></math>
- **(B)** <math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(C)** <math><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac></mrow></mfenced></math>
- **(D)** <math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>E</mi><mn>1</mn></msub><msub><mi>E</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub></mfrac></math>
Then ratio of potential would be,<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>V</mi><mn>1</mn></msub><msub><mi>V</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><msub><mi>E</mi><mn>1</mn></msub><msub><mi>R</mi><mn>1</mn></msub></mrow><mrow><msub><mi>E</mi><mn>2</mn></msub><msub><mi>R</mi><mn>2</mn></msub></mrow></mfrac><mo>=</mo><mfrac><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub></mfrac><mo>&#215;</mo><mfrac><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub></mfrac><mo>=</mo><msup><mfenced separators="|"><mfrac><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub></mfrac></mfenced><mn>2</mn></msup></math>

</details>

---

### Q51. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

In free space, a particle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> of charge <math><mn>1</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#956;</mi><mi mathvariant="normal">C</mi></math> is held fixed at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> . Another particle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> of the same charge and mass <math><mn>4</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#956;</mi><mi mathvariant="normal">g</mi></math> is kept at a distance of <math><mn>1</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">m</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is released, then its velocity at a distance of <math><mn>9</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">m</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is:
[Take <math><mi>&#160;</mi><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi><msub><mrow><mi mathvariant="normal">&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>9</mn></mrow></msup><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">N</mi><mi mathvariant="normal">&#160;</mi><msup><mrow><mi mathvariant="normal">m</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><msup><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math> ]

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1.0</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1.5</mn><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup><mi>&#160;</mi><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2.0</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3.0</mn><mo>&#215;</mo><msup><mn>10</mn><mn>4</mn></msup><mi>&#160;</mi><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2.0</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

From conservation in mechanical energy:
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi mathvariant="normal">&#916;</mi><mi>P</mi><mo mathvariant="italic">.</mo><mi>E</mi><mo>.</mo><mo>=</mo><mi mathvariant="normal">&#916;</mi><mi>K</mi><mo mathvariant="italic">.</mo><mi>E</mi><mo mathvariant="italic">.</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi><msub><mi mathvariant="normal">&#949;</mi><mn>0</mn></msub></mrow></mfrac><msup><mfenced separators="|"><mrow><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mn>6</mn></msup></mrow></mfenced><mn>2</mn></msup><mfenced close="]" open="[" separators="|"><mrow><mfrac><mn>1</mn><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mo>&#215;</mo><msup><mi>V</mi><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>12</mn></mrow></msup><mfenced close="]" open="[" separators="|"><mfrac><mn>8</mn><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfrac></mfenced><mo>=</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mo>&#215;</mo><msup><mi>V</mi><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>V</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mn>6</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

</details>

---

### Q52. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A uniformly charged ring of radius <math><mn>3</mn><mi>a</mi></math> and total charge <math><mi>q</mi></math> is placed in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8208;</mo><mi>y</mi></math> plane centred at origin. A point charge <math><mi>q</mi></math> is moving towards the ring along the <math><mi>z</mi><mo>-</mo></math> axis and has speed <math><mi>v</mi></math> at <math><mi>&#160;</mi><mi>z</mi><mo>=</mo><mn>4</mn><mi>a</mi></math> . The minimum value of <math><mi>v</mi></math> such that it crosses the origin is:

**Options:**

- **(A)** <math><msqrt><mfrac><mrow><mn>2</mn></mrow><mrow><mi>m</mi></mrow></mfrac></msqrt><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>15</mn></mrow></mfrac><mfrac><mrow><msup><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn><mi>π</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>a</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></math>
- **(B)** <math><msqrt><mfrac><mrow><mn>2</mn></mrow><mrow><mi>m</mi></mrow></mfrac></msqrt><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>15</mn></mrow></mfrac><mfrac><mrow><msup><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn><mi>π</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>a</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></math>
- **(C)** <math><msqrt><mfrac><mrow><mn>2</mn></mrow><mrow><mi>m</mi></mrow></mfrac></msqrt><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mfrac><mrow><msup><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn><mi>π</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>a</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></math>
- **(D)** <math><msqrt><mfrac><mrow><mn>2</mn></mrow><mrow><mi>m</mi></mrow></mfrac></msqrt><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>15</mn></mrow></mfrac><mfrac><mrow><msup><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn><mi>π</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>a</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msqrt><mfrac><mrow><mn>2</mn></mrow><mrow><mi>m</mi></mrow></mfrac></msqrt><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>15</mn></mrow></mfrac><mfrac><mrow><msup><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn><mi>π</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>a</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e5872bf9-6e96-4c5d-ae9e-6bc3386296ac-image11.png" />
From the conservation of energy,
<math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfrac><mrow><msup><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msqrt><msup><mrow><mfenced separators="|"><mrow><mn>3</mn><mi>a</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mn>4</mn><mi>a</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>m</mi><msup><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfrac><mrow><msup><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mfenced separators="|"><mrow><mn>3</mn><mi>a</mi></mrow></mfenced></mrow></mfrac></math>
<math><mi>v</mi><mo>=</mo><msqrt><mfrac><mrow><msup><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>a</mi></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>15</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>m</mi></mrow></mfrac></msqrt></math>
<math><mo>=</mo><msqrt><mfrac><mrow><mn>2</mn></mrow><mrow><mi>m</mi></mrow></mfrac></msqrt><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>15</mn></mrow></mfrac><mfrac><mrow><msup><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>a</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></math>

</details>

---

### Q53. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A system of three charges are placed as shown in the figure:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5f6e26f6-4757-4e4d-ab08-145cb986046c-image5.png" />
If <math><mi mathvariant="normal">D</mi><mi mathvariant="normal">&#160;</mi><mo>&#62;</mo><mo>&#62;</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">d</mi><mo>,</mo></math> the potential energy of the system is best given by:

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi mathvariant="normal">π</mi><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced open="[" close="]" separators="|"><mrow><mo>-</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi mathvariant="normal">q</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">Q</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">d</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi mathvariant="normal">π</mi><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced open="[" close="]" separators="|"><mrow><mo>+</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi mathvariant="normal">q</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">Q</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">d</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi mathvariant="normal">π</mi><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced open="[" close="]" separators="|"><mrow><mo>-</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi mathvariant="normal">q</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">Q</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi mathvariant="normal">π</mi><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced open="[" close="]" separators="|"><mrow><mo>-</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">q</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">Q</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">d</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi mathvariant="normal">π</mi><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced open="[" close="]" separators="|"><mrow><mo>-</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi mathvariant="normal">q</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">Q</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">d</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<math><mi mathvariant="normal">U</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">k</mi><mfenced separators="|"><mrow><mo>-</mo><mi mathvariant="normal">q</mi></mrow></mfenced><mfenced separators="|"><mrow><mi mathvariant="normal">q</mi></mrow></mfenced></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi mathvariant="normal">k</mi><mfenced separators="|"><mrow><mo>-</mo><mi mathvariant="normal">q</mi></mrow></mfenced><mfenced separators="|"><mrow><mi mathvariant="normal">Q</mi></mrow></mfenced></mrow><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mi mathvariant="normal">D</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mrow><mi mathvariant="normal">k</mi><mfenced separators="|"><mrow><mi mathvariant="normal">q</mi></mrow></mfenced><mfenced separators="|"><mrow><mi mathvariant="normal">Q</mi></mrow></mfenced></mrow><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">D</mi><mo>+</mo><mfrac><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mfrac></math>  
<math><mo>=</mo><mfrac><mrow><mo>-</mo><mi mathvariant="normal">k</mi><msup><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi mathvariant="normal">k</mi><mi mathvariant="normal">Q</mi><mi mathvariant="normal">q</mi></mrow><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">D</mi><mo>-</mo><mfrac><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mrow><mi mathvariant="normal">K</mi><mi mathvariant="normal">Q</mi><mi mathvariant="normal">q</mi></mrow><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">D</mi><mo>+</mo><mfrac><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mfrac></math>  
<math><mo>=</mo><mfrac><mrow><mo>-</mo><mi mathvariant="normal">k</mi><msup><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac><mo>+</mo><mi mathvariant="normal">k</mi><mi mathvariant="normal">Q</mi><mi mathvariant="normal">q</mi><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><mi mathvariant="normal">D</mi><mo>-</mo><mfrac><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mi mathvariant="normal"> </mi><mi mathvariant="normal">D</mi><mo>-</mo><mfrac><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfrac></mrow></mfenced></math>  
<math><mo>=</mo><mfrac><mrow><mo>-</mo><mi mathvariant="normal">k</mi><msup><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi mathvariant="normal">k</mi><mi mathvariant="normal">Q</mi><mi mathvariant="normal">q</mi><mi mathvariant="normal">d</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfrac></math>  
Since, D&gt;&gt;d 
<math><mi mathvariant="normal">U</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi mathvariant="normal">k</mi><msup><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi mathvariant="normal">k</mi><mi mathvariant="normal">Q</mi><mi mathvariant="normal">q</mi><mi mathvariant="normal">d</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi mathvariant="normal">π</mi><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced open="[" close="]" separators="|"><mrow><mo>-</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi mathvariant="normal">q</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">Q</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">d</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">D</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math>

</details>

---

### Q54. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The electric field in a region is given by <math><mover accent="true"><mrow><mi mathvariant="normal">E</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mi mathvariant="normal">A</mi><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">B</mi></mrow></mfenced><mi mathvariant="normal">&#160;</mi><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mi>&#160;</mi><mo>,</mo></math> where <math><mi mathvariant="normal">E</mi></math> is in <math><mi mathvariant="normal">N</mi><msup><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> and <math><mi>x</mi></math> is in metres. The values of constants are <math><mi mathvariant="normal">A</mi><mo>=</mo><mn>20</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">S</mi><mi mathvariant="normal">I</mi></math> unit and <math><mi mathvariant="normal">B</mi><mo>=</mo><mn>10</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">S</mi><mi mathvariant="normal">I</mi></math> unit. If the potential at <math><mi>x</mi><mo>=</mo><mn>1</mn></math> is <math><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and that at <math><mi>x</mi><mo>=</mo><mo>-</mo><mn>5</mn></math> is <math><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo></math> then <math><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>2</mn></mrow></msub></math> is

**Options:**

- **(A)** <math><mn>320</mn><mi> </mi><mi mathvariant="normal">V</mi></math>
- **(B)** <math><mo>-</mo><mn>520</mn><mi> </mi><mi mathvariant="normal">V</mi></math>
- **(C)** <math><mn>180</mn><mi> </mi><mi mathvariant="normal">V</mi></math>
- **(D)** <math><mo>-</mo><mn>48</mn><mi> </mi><mi mathvariant="normal">V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>180</mn><mi> </mi><mi mathvariant="normal">V</mi></math>**

**Detailed Solution:**

<math><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mo>-</mo><mrow><mo stretchy="false">&#8747;</mo><mrow><mi mathvariant="normal">E</mi><mo>.</mo><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow></mrow></math>
<math><mo>=</mo><mo>-</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mo>-</mo><mn>5</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">a</mi><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">b</mi></mrow></mfenced><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow></mrow></math>
<math><mo>=</mo><msubsup><mrow><mo>-</mo><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">a</mi><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mi mathvariant="normal">b</mi><mi mathvariant="normal">x</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mn>5</mn></mrow><mrow><mn>1</mn></mrow></msubsup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi mathvariant="normal">&#160;</mi><mo>-</mo><mfenced open="[" close="]" separators="|"><mrow><mfenced separators="|"><mrow><mfrac><mi mathvariant="normal">a</mi><mn>2</mn></mfrac><mo>+</mo><mi mathvariant="normal">b</mi></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mfrac><mrow><mtext>a</mtext><mo>&#215;</mo><mn>25</mn></mrow><mn>2</mn></mfrac><mo>-</mo><mn>5</mn><mi mathvariant="normal">b</mi></mrow></mfenced></mrow></mfenced></math>
<math><mo>=</mo><mi mathvariant="normal">&#160;</mi><mo>-</mo><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>20</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mn>10</mn><mo>-</mo><mn>250</mn><mo>+</mo><mn>50</mn></mrow></mfenced></math>
<math><mo>=</mo><mn>180</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">V</mi></math>

</details>

---

### Q55. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A solid conducting sphere, having a charge <math><mi mathvariant="normal">Q</mi><mo>,</mo></math> is surrounded by an uncharged conducting hollow spherical shell. Let the potential difference between the surface of the solid sphere and that of the outer surface of the hollow shell be <math><mi mathvariant="normal">V</mi><mo>.</mo></math> If the shell is now given a charge of <math><mo>&#8211;</mo><mn>4</mn><mi mathvariant="normal">Q</mi><mo>,</mo></math> the new potential difference between the same two surfaces is:

**Options:**

- **(A)** <math><mi> </mi><mo>–</mo><mn>2</mn><mi mathvariant="normal">V</mi></math>
- **(B)** <math><mn>2</mn><mi> </mi><mi mathvariant="normal">V</mi></math>
- **(C)** <math><mi mathvariant="normal">V</mi></math>
- **(D)** <math><mn>4</mn><mi> </mi><mi mathvariant="normal">V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi mathvariant="normal">V</mi></math>**

**Detailed Solution:**

First condition:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9939f9df-53d2-4d26-a785-f74a52929f59-image18.png" />
Both conducting spheres are shown.
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mrow><mi>i</mi><mi>n</mi></mrow></msub><mo>-</mo><msub><mi>V</mi><mrow><mi>o</mi><mi>u</mi><mi>t</mi></mrow></msub><mo>=</mo><mfenced separators="|"><mfrac><mrow><mi>K</mi><mi>Q</mi></mrow><msub><mi>r</mi><mn>1</mn></msub></mfrac></mfenced><mo>-</mo><mfenced separators="|"><mfrac><mrow><mi>K</mi><mi>Q</mi></mrow><msub><mi>r</mi><mn>2</mn></msub></mfrac></mfenced></math>
<math><mo>&#8658;</mo><mi>V</mi><mo>=</mo><mi>K</mi><mi>Q</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msub><mrow><mi>r</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msub><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></mrow></mfenced></math>
Second condition:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dd82afb0-7689-4c99-9c57-20706987164c-image19.png" />
Shell is now given charge <math><mo>-</mo><mn>4</mn><mi>Q</mi></math> .
<math><msub><mrow><mi>V</mi></mrow><mrow><mi>i</mi><mi>n</mi></mrow></msub><mo>-</mo><msub><mrow><mi>V</mi></mrow><mrow><mi>o</mi><mi>u</mi><mi>t</mi></mrow></msub><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>K</mi><mi>Q</mi></mrow><mrow><msub><mrow><mi>r</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>4</mn><mi>K</mi><mi>Q</mi></mrow><mrow><msub><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>K</mi><mi>Q</mi></mrow><mrow><msub><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>4</mn><mi>K</mi><mi>Q</mi></mrow><mrow><msub><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></mrow></mfenced></math>
<math><mo>=</mo><mfrac><mrow><mi>K</mi><mi>Q</mi></mrow><mrow><msub><mrow><mi>r</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>K</mi><mi>Q</mi></mrow><mrow><msub><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></math>
<math><mo>=</mo><mi>K</mi><mi>Q</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msub><mrow><mi>r</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msub><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>V</mi></math>

</details>

---

### Q56. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

There is a uniform spherically symmetric surface charge density at a distance <math><msub><mrow><mi>R</mi></mrow><mrow><mn>0</mn></mrow></msub></math> from the origin. The charge distribution is initially at rest and starts expanding because of mutual repulsion. The figure that represents best the speed <math><mi>V</mi><mfenced separators="|"><mrow><mi>R</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced></mrow></mfenced></math> of the distribution as a function of its instantaneous radius <math><mi>R</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced></math> is:

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/wcrohqgbpbcvumtjiqimeyqnfbjvifdinnthcaqnixsbmghwtj.png" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/wnhjzcvnisfffuaqadjamiipbkrkshoajkhcpxymhnxhgmiqnf.png" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/qhxkuldaifvocoairrvvnzytasvozrconkosdohpyngqoasxki.png" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/xxippitwtlshozqsbusamujgboxvechrosrohxvzwtqhjdwrgs.png" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/wcrohqgbpbcvumtjiqimeyqnfbjvifdinnthcaqnixsbmghwtj.png" />**

**Detailed Solution:**

<math><msub><mrow><mi>U</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>+</mo><msub><mrow><mi>K</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>=</mo><msub><mrow><mi>U</mi></mrow><mrow><mi>f</mi></mrow></msub><mo>+</mo><msub><mrow><mi>K</mi></mrow><mrow><mi>f</mi></mrow></msub></math> 

 <math><mfrac><mrow><mi>K</mi><msup><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><msub><mrow><mi>r</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mo>+</mo><mn>0</mn><mo>=</mo><mfrac><mrow><mi>K</mi><msup><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><mi>r</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>m</mi><msup><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msup></math> 

 <math><msup><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mi>K</mi><msup><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>m</mi></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msub><mrow><mi>r</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>r</mi></mrow></mfrac></mrow></mfenced></math> 

 <math><mi>v</mi><mo>=</mo><msqrt><mfrac><mrow><mi>K</mi><msup><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>m</mi></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msub><mrow><mi>r</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>r</mi></mrow></mfrac></mrow></mfenced></msqrt></math>

</details>

---

### Q57. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Three charges $Q,+y$ and $+q$ are placed at the vertices of a right-angle isosceles triangle as shown below. The net electrostatic energy of the configuration is zero, if the value of $\mathrm{Q}$ is

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ACMkbyx-gJKYcY_ZkGmz2yf3DeBJaTAYM4bYcnXGj14.original.fullsize.png">

**Options:**

- **(A)** $+q$
- **(B)** $\frac{-\sqrt{2} q}{\sqrt{2}+1}$
- **(C)** $\frac{-q}{1+\sqrt{2}}$
- **(D)** $-2 q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-\sqrt{2} q}{\sqrt{2}+1}$**

**Detailed Solution:**

Net electrostatic energy for the system

$\mathrm{U}=\mathrm{K}\left[\frac{\mathrm{q}^{2}}{\mathrm{a}}+\frac{\mathrm{Qq}}{\mathrm{a}}+\frac{\mathrm{Qq}}{\mathrm{a} \sqrt{2}}\right]=0$

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Ta7PcdFDTix28uAoxUaawKRwl8re3wKyVF-k34afOU8.original.fullsize.png">


$\begin{aligned} \Rightarrow q &=-Q\left[1+\frac{1}{\sqrt{2}}\right] \\ & \Rightarrow Q=\frac{-q \sqrt{2}}{\sqrt{2}+1} \end{aligned}$

</details>

---

### Q58. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The given graph shows variation (with distancer from centre) of:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Wq9uSUVm3YpgTAIYt4Uc5AWUUMwP6PG7GxluZxfXbsc.original.fullsize.png">

**Options:**

- **(A)** Electric field of a uniformly charged sphere
- **(B)** Potential of a uniformly charged spherical shell
- **(C)** Potential of a uniformly charged sphere
- **(D)** Electric field of a uniformly charged spherical shell

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Potential of a uniformly charged spherical shell**

**Detailed Solution:**

Electric potential is constant inside a charged spherical shell.

</details>

---

### Q59. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Four equal point charges <math><mi>Q</mi></math> each are placed in the <math><mi>x</mi><mi>y</mi></math> plane at <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mtext>&#8201;</mtext><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mtext>&#8201;</mtext><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mtext>&#8201;</mtext><mo>-</mo><mn>2</mn></mrow></mfenced></math> and <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mtext>&#8201;</mtext><mo>-</mo><mn>2</mn></mrow></mfenced></math> . The work required to put a fifth charge <math><mi>Q</mi></math> at the origin of the coordinate system will be:

**Options:**

- **(A)** <math><mfrac><mrow><msup><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn><mi>π</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><msup><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mi>π</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><msup><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn><mi>π</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>5</mn></msqrt></mrow></mfrac></mrow></mfenced></math>
- **(D)** <math><mfrac><mrow><msup><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn><mi>π</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><msup><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn><mi>π</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>5</mn></msqrt></mrow></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Work done in bringing the fifth charge at origin is equal to change in the potential energy of the system of charges.</p><p><math><msub><mrow><mi>W</mi></mrow><mrow><mi>e</mi><mi>x</mi><mi>t</mi></mrow></msub><mo>=</mo><mi>&#916;</mi><mi>U</mi></math><math><mo>=</mo><msub><mrow><mi>U</mi></mrow><mrow><mi>f</mi></mrow></msub><mo>-</mo><msub><mrow><mi>U</mi></mrow><mrow><mi>i</mi></mrow></msub></math> if  <math><msub><mrow><mi>U</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>=</mo><mn>0</mn></math> (assumed)

<math><msub><mrow><mi>W</mi></mrow><mrow><mi>e</mi><mi>x</mi><mi>t</mi></mrow></msub><mo>=</mo><msub><mrow><mi>U</mi></mrow><mrow><mi>f</mi></mrow></msub><mo>-</mo><mn>0</mn></math><math><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>K</mi><msup><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>K</mi><msup><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>K</mi><msup><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><msqrt><mn>5</mn></msqrt></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>K</mi><msup><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><msqrt><mn>5</mn></msqrt></mrow></mfrac></mrow></mfenced></math></p><p>Hence, the work done in bringing the fifth charge at the origin is 
<math><msub><mrow><mi>W</mi></mrow><mrow><mi>e</mi><mi>x</mi><mi>t</mi></mrow></msub><mo>=</mo><mfrac><mrow><msup><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>5</mn></msqrt></mrow></mfrac></mrow></mfenced></math>.</p></blockquote>

</details>

---

### Q60. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Charges <math><mo>-</mo><mi>q</mi></math> and <math><mo>+</mo><mi>q</mi></math>, located at <math><mi>A</mi></math> and <math><mi>B</mi></math>, respectively, constitute an electric dipole. Distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mn>2</mn><mi>a</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> is the mid point of the dipole and <math><mi>O</mi><mi>P</mi></math> is perpendicular to <math><mi>A</mi><mi>B</mi></math>. A charge <math><mi>Q</mi></math> is placed at <math><mi>P</mi></math> where <math><mi>O</mi><mi>P</mi><mo>=</mo><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8811;</mo><mn>2</mn><mi>a</mi></math>. The charge <math><mi>Q</mi></math> experiences an electrostatic force <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math>. If <math><mi>Q</mi></math> is now moved along the equatorial line to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>'</mo></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>P</mi><mo>'</mo><mo>=</mo><mfenced separators="|"><mfrac><mi>y</mi><mn>3</mn></mfrac></mfenced></math> the force on <math><mi>Q</mi></math> will be close to<math><mfenced separators="|"><mrow><mfrac><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>&#8810;</mo><mn>2</mn><mi>a</mi></mrow></mfenced></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/22694bf5-4440-4673-870e-bed5e58cbc9d-image.png" style="width: 300px; height: 263px;" />

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn><mi>F</mi></math>.
- **(B)** <math><mfrac><mrow><mi>F</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>.
- **(C)** <math><mn>3</mn><mi>F</mi></math>.
- **(D)** <math><mn>9</mn><mi>F</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn><mi>F</mi></math>.**

**Detailed Solution:**

<p>Electric field intensity at the distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> along the perpendicular bisector is

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>=</mo><mfrac><mrow><mi>K</mi><mi>P</mi></mrow><msup><mi>y</mi><mn>3</mn></msup></mfrac></math>

So, force at distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>,

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mi>Q</mi><mo>(</mo><msub><mi>E</mi><mn>1</mn></msub><mo>)</mo><mo>=</mo><mi>Q</mi><mfenced><mfrac><mrow><mi>K</mi><mi>P</mi></mrow><msup><mi>y</mi><mn>3</mn></msup></mfrac></mfenced></math> ...<math><mo>(</mo><mn>1</mn><mo>)</mo></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>'</mo><mo>=</mo><mi>Q</mi><mfrac><mrow><mi>K</mi><mi>P</mi></mrow><msup><mfenced><mstyle displaystyle="true"><mfrac><mi>y</mi><mn>3</mn></mfrac></mstyle></mfenced><mn>3</mn></msup></mfrac></math> ...<math><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p>Dividing <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>F</mi><mo>&#39;</mo></mrow><mi>F</mi></mfrac><mo>=</mo><msup><mfenced separators="|"><mn>3</mn></mfenced><mn>3</mn></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>F</mi><mo>&#39;</mo><mo>=</mo><mn>27</mn><mi>F</mi></math></p>

</details>

---

### Q61. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A charge <math><mi>Q</mi></math> is distributed over three concentric spherical shells of radii <math><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>b</mi><mo>,</mo><mi>&#160;</mi><mi>c</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mi>a</mi><mo>&#60;</mo><mi>b</mi><mo>&#60;</mo><mi>c</mi></mrow></mfenced></math> such that their surface charge densities are equal to one another.

The total potential at a point at distance <math><mi>r</mi></math> from their common centre, where <math><mi>r</mi><mo>&#60;</mo><mi>a</mi><mo>,</mo></math> would be:

**Options:**

- **(A)** <math><mfrac><mrow><mi>Q</mi></mrow><mrow><mn>4</mn><mi>π</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>Q</mi><mi> </mi><mfenced separators="|"><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>4</mn><mi>π</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>Q</mi></mrow><mrow><mn>12</mn><mi>π</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfrac><mrow><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>c</mi><mi>a</mi></mrow><mrow><mi>a</mi><mi>b</mi><mi>c</mi></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>Q</mi><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced></mrow><mrow><mn>4</mn><mi>π</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mi>Q</mi><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced></mrow><mrow><mn>4</mn><mi>π</mi><msub><mrow><mi>ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Surface charge densities of all sphere is given as <math><mfrac><mrow><msub><mrow><mi>q</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><msub><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><msub><mrow><mi>q</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow><mrow><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">t</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>1</mn></msub></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>3</mn></msub></math> is charge on sphere of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> respectively.

<math><msub><mrow><mi>q</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><msub><mrow><mi>q</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mi>Q</mi></math>

<math><msub><mrow><mi>q</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>(</mo><mi>Q</mi><mo>)</mo></mrow><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

<math><msub><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>(</mo><mi>Q</mi><mo>)</mo></mrow><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

<math><msub><mrow><mi>q</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mfrac><mrow><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mi>Q</mi></mrow></mfenced></mrow><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math></p></blockquote><blockquote><p>Potential at a point where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>&#60;</mo><mi>a</mi></math> is given as <math><mi>V</mi><mo>=</mo><mfrac><mrow><mi>K</mi><msub><mrow><mi>q</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><mi>a</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>K</mi><msub><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><mi>b</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>K</mi><msub><mrow><mi>q</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow><mrow><mi>c</mi></mrow></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> is a constant.

<math><mi>V</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mi>Q</mi></mrow></mfenced><mfenced separators="|"><mrow><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math></p></blockquote>

</details>

---

### Q62. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `2`

Three concentric metal shells <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> of respective radii <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>&#160;</mo><mo>(</mo><mi>a</mi><mo>&#160;</mo><mo>&#60;</mo><mo>&#160;</mo><mi>b</mi><mo>&#160;</mo><mo>&#60;</mo><mo>&#160;</mo><mi>c</mi><mo>)</mo></math> have surface charge densities <c) charge="" densities="" have="" math="" surface=""><span style="display: none;"> </span><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>&#963;</mi><mo>,</mo><mo>&#160;</mo><mo>-</mo><mi>&#963;</mi></math><span style="display: none;"> </span> and <math><mo>+</mo><mi>&#963;</mi></math> respectively. The potential of shell <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math><span style="display: none;"> </span> is:</c)>

**Options:**

- **(A)** <math><mfrac><mrow><mi>σ</mi></mrow><mrow><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>c</mi></mrow></mfrac><mo>+</mo><mi>a</mi></mrow></mfenced></math>
- **(B)** <math><mfrac><mrow><mi>σ</mi></mrow><mrow><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>a</mi></mrow></mfrac><mo>+</mo><mi>c</mi></mrow></mfenced></math>
- **(C)** <math><mfrac><mrow><mi>σ</mi></mrow><mrow><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>b</mi></mrow></mfrac><mo>+</mo><mi>c</mi></mrow></mfenced></math>
- **(D)** <math><mfrac><mrow><mi>σ</mi></mrow><mrow><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>b</mi></mrow></mfrac><mo>+</mo><mi>a</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mi>σ</mi></mrow><mrow><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>b</mi></mrow></mfrac><mo>+</mo><mi>c</mi></mrow></mfenced></math>**

**Detailed Solution:**

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/hjhhjhhjhjhhj.JPG" style="width: 250px; height: 250px;" />

Net potential at B is due to the superposition of potential due to all shells, 

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8744;</mo><mi>B</mi></msub><mo>=</mo><msub><mo>&#8744;</mo><mrow><mi>B</mi><mfenced separators="|"><mi>I</mi></mfenced></mrow></msub><mo>+</mo><msub><mo>&#8744;</mo><mrow><mi>B</mi><mfenced separators="|"><mrow><mi>I</mi><mi>I</mi></mrow></mfenced></mrow></msub><mo>+</mo><msub><mo>&#8744;</mo><mrow><mi>B</mi><mfenced separators="|"><mrow><mi>I</mi><mi>I</mi><mi>I</mi></mrow></mfenced></mrow></msub></math>

<math><mo>=</mo><mfrac><mrow><mi>K</mi><mn>4</mn><mi>&#960;</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#963;</mi></mrow><mrow><mi>b</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>K</mi><mn>4</mn><mi>&#960;</mi><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mo>-</mo><mi>&#963;</mi></mrow></mfenced></mrow><mrow><mi>b</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>K</mi><mn>4</mn><mi>&#960;</mi><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mi>&#963;</mi></mrow></mfenced></mrow><mrow><mi>c</mi></mrow></mfrac></math>

Required potential of b

<math><mo>=</mo><mfrac><mrow><mi>&#963;</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>b</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>&#963;</mi><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>b</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>&#963;</mi><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>c</mi></mrow></mfrac></math>

<math><mo>=</mo><mfrac><mrow><mi>&#963;</mi></mrow><mrow><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>b</mi></mrow></mfrac><mo>+</mo><mi>c</mi></mrow></mfenced></math>

</details>

---

### Q63. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The energy stored in the electric field produced by a metal sphere is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi></math>. If the sphere contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi>&#956;C</mi></math> charge, its radius will be: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">T</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">k</mi><mi mathvariant="normal">e</mi><mo>:</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub></mrow></mfrac><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn><mo>&#160;</mo><mi>mm</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>&#160;</mo><mi>mm</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn><mo>&#160;</mo><mi>mm</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi>mm</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>&#160;</mo><mi>mm</mi></math>**

**Detailed Solution:**

Energy of sphere <math><mo>=</mo><mfrac><mrow><msup><mrow><mi>Q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><mi>C</mi></mrow></mfrac></math>

<math><mn>4.5</mn><mo>=</mo><mfrac><mrow><mn>16</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>12</mn></mrow></msup></mrow><mrow><mn>2</mn><mi>C</mi></mrow></mfrac></math>

<math><mi>C</mi><mo>=</mo><mfrac><mrow><mn>16</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>12</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac><mo>=</mo><mn>4</mn><mi>&#960;</mi><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>R</mi></math>

<math><mi>R</mi><mo>=</mo><mfrac><mrow><mn>16</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>12</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>

<math><mi>R</mi><mo>=</mo><mfrac><mrow><mn>16</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>12</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mrow><mi>&#949;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>

<math><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>9</mn></mrow></msup><mo>&#215;</mo><mfrac><mrow><mn>16</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>12</mn></mrow></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>16</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>=</mo><mn>16</mn><mi>&#160;</mi><mi>mm</mi></math>

</details>

---

### Q64. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

There is a uniform electrostatic field in a region. The potential at various points on a small sphere centred at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>, in the region, is found to vary between the limits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>589</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mn>589</mn><mo>.</mo><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>. What is the potential at a point on the sphere whose radius vector makes an angle of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>&#176;</mo></math> with the direction of the field?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>589</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>589</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>589</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>589</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>589</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/076ce32f-6717-45fc-a385-67ebb63feae4-image.png" style="width: 200px; height: 116px;" />

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#916;</mi><mi>V</mi><mo>=</mo><mi>E</mi><mi>d</mi></math>

<math><mi mathvariant="normal">Along diameter </mi><mi mathvariant="normal">&#160;</mi><mo>&#8710;</mo><mi mathvariant="normal">V</mi><mo>=</mo><mn>589.8</mn><mo>-</mo><mn>589.0</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">V</mi></math>
                              <math><mo>=</mo><mn>0.8</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">V</mi></math>

<math><mn>0.8</mn><mo>=</mo><mi>E</mi><mi>d</mi></math>

Now
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/697fbac2-f3ba-49b1-ae01-5681a1a91d50-image.png" style="width: 200px; height: 141px;" />
<math> <mi>&#916;</mi><mi>V</mi><mo>=</mo><mi>E</mi><mfrac> <mi>d</mi> <mn>2</mn> </mfrac> <mi>cos</mi><mi>&#952;</mi><mo>=</mo><mn>0.4</mn><mo>&#215;</mo><mi>cos</mi><msup> <mn>60</mn> <mi>o</mi> </msup> </math>

<math> <mo>=</mo><mn>0.2</mn> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mn>589.8</mn><mo>&#8722;</mo><mi>V</mi><mo>=</mo><mn>0.2</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>589.6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>

</details>

---

### Q65. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Within a spherical charge distribution of charge density <math><mi>&#961;</mi><mfenced separators="|"><mrow><mi>r</mi></mrow></mfenced><mo>,</mo><mi>&#160;</mi></math> N equipotential surfaces of potential <math><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>+</mo><mo>&#8710;</mo><mi>V</mi><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>+</mo><mn>2</mn><mo>&#8710;</mo><mi>V</mi><mo>,</mo><mo>&#8230;</mo><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>+</mo><mi>N</mi><mo>&#8710;</mo><mi>V</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mo>&#8710;</mo><mi>V</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced><mo>,</mo></math> are drawn and have increasing radii <math><msub><mrow><mi>r</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>r</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mo>&#8230;</mo><msub><mrow><mi>r</mi></mrow><mrow><mi>N</mi></mrow></msub><mo>,</mo></math> respectively. If the difference in the radii of the surfaces is constant for all values of <math><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>&#160;</mi><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><mo>&#8710;</mo><mi>V</mi></math> then :

**Options:**

- **(A)** <math><mi>ρ</mi><mfenced separators="|"><mrow><mi>r</mi></mrow></mfenced><mo> =</mo></math> constant
- **(B)** <math> <mrow>  <mi>&#x03C1;</mi><mrow><mo>(</mo>   <mi>r</mi>  <mo>)</mo></mrow><mo>&#x00A0;</mo><mo>&#x221D;</mo><mfrac>   <mn>1</mn>   <mrow>    <msup>     <mi>r</mi>     <mn>2</mn>    </msup>    </mrow>  </mfrac>  </mrow></math>
- **(C)** <math> <mrow> <mi>ρ</mi><mrow><mo>(</mo> <mi>r</mi> <mo>)</mo></mrow><mo> </mo><mo>∝</mo><mo> </mo><mfrac> <mn>1</mn> <mi>r</mi> </mfrac> </mrow> </math>
- **(D)** <math> <mrow>  <mi>&#x03C1;</mi><mrow><mo>(</mo>   <mi>r</mi>  <mo>)</mo></mrow><mo>&#x00A0;</mo><mo>&#x221D;</mo><mo>&#x00A0;</mo><mi>r</mi></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math> <mrow> <mi>ρ</mi><mrow><mo>(</mo> <mi>r</mi> <mo>)</mo></mrow><mo> </mo><mo>∝</mo><mo> </mo><mfrac> <mn>1</mn> <mi>r</mi> </mfrac> </mrow> </math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/59f27039-8404-4695-819b-d3b312ba4298-image.png" style="width: 302px; height: 150px;" /></p><p><math> <mrow> <mi>E</mi><mo>=</mo><mo>&#8722;</mo><mfrac> <mrow> <mi>&#916;</mi><mi>V</mi></mrow> <mrow> <mi>&#916;</mi><mi>r</mi></mrow> </mfrac> </mrow> </math>

<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi></math> <mo>△<mo>v and <mo>△<mo>r are constant

E = constant

<math><mi>E</mi><mo>=</mo><mfrac><mrow><mi>K</mi><mi>q</mi></mrow><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mi>c</mi></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>q</mi><mi>&#160;</mi><mo>&#8733;</mo><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>q</mi><mo>=</mo><mrow><msubsup><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi>r</mi></mrow></msubsup><mrow><mi>&#961;</mi><mn>4</mn><mi>&#960;</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>d</mi><mi>r</mi></mrow></mrow><mi>&#160;</mi></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#961;</mi><mo>&#8733;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>r</mi></mrow></mfrac></math></mo></mo></mo></mo></p>

</details>

---

### Q66. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The potential (in volts) of a charge distribution is given by

<math><mi mathvariant="normal">V</mi><mfenced separators="|"><mrow><mi mathvariant="normal">z</mi></mrow></mfenced><mo>=</mo><mn>30</mn><mo>-</mo><mn>5</mn><msup><mrow><mi mathvariant="normal">z</mi></mrow><mrow><mn>2</mn></mrow></msup></math> for <math><mfenced close="|" open="|" separators="|"><mrow><mi mathvariant="normal">z</mi></mrow></mfenced><mo>&#8804;</mo><mn>1</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi></math>

<math><mi mathvariant="normal">V</mi><mfenced separators="|"><mrow><mi mathvariant="normal">z</mi></mrow></mfenced><mo>=</mo><mn>35</mn><mo>-</mo><mn>10</mn><mi mathvariant="normal">&#160;</mi><mfenced close="|" open="|" separators="|"><mrow><mi mathvariant="normal">z</mi></mrow></mfenced></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mi mathvariant="normal">z</mi></mfenced><mo>&#8805;</mo><mn>1</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi></math> .

<math><mi mathvariant="normal">V</mi><mfenced separators="|"><mrow><mi mathvariant="normal">z</mi></mrow></mfenced></math> does not depend on x and y. If this potential is generated by a constant charge per unit volume <math><msub><mrow><mi mathvariant="normal">&#961;</mi></mrow><mrow><mn>0</mn></mrow></msub></math> (in units of <math><msub><mrow><mi mathvariant="normal">&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub></math> ) which is spread over a certain region, then choose the correct statement.

**Options:**

- **(A)** <math><msub><mrow><mi mathvariant="normal">ρ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>20</mn><mi mathvariant="normal"> </mi><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></math>  in the entire region
- **(B)** <math><msub><mrow><mi mathvariant="normal">ρ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>10</mn><mi mathvariant="normal"> </mi><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></math> for <math><mfenced close="|" open="|" separators="|"><mrow><mi mathvariant="normal">z</mi></mrow></mfenced><mo>≤</mo><mn>1</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi></math> and <math><msub><mrow><mi mathvariant="normal">ρ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>0</mn></math> else where
- **(C)** <math><msub><mrow><mi mathvariant="normal">ρ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>20</mn><mi mathvariant="normal"> </mi><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></math>  for  <math><mfenced close="|" open="|" separators="|"><mrow><mi mathvariant="normal">z</mi></mrow></mfenced><mo>≤</mo><mn>1</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi></math>  and  <math><msub><mrow><mi mathvariant="normal">ρ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>0</mn></math>  else where
- **(D)** <math><msub><mrow><mi mathvariant="normal">ρ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>40</mn><mi mathvariant="normal"> </mi><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></math>  in the entire region

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msub><mrow><mi mathvariant="normal">ρ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>10</mn><mi mathvariant="normal"> </mi><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></math> for <math><mfenced close="|" open="|" separators="|"><mrow><mi mathvariant="normal">z</mi></mrow></mfenced><mo>≤</mo><mn>1</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi></math> and <math><msub><mrow><mi mathvariant="normal">ρ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>0</mn></math> else where**

**Detailed Solution:**

<p>Electric field due to given potentials is </p><p><math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mo>-</mo><mi mathvariant="normal">d</mi><mi mathvariant="normal">V</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">z</mi></mrow></mfrac><mo>=</mo><mn>10</mn><mi mathvariant="normal">&#160;</mi><mfenced close="|" open="|" separators="|"><mrow><mi mathvariant="normal">z</mi></mrow></mfenced></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8739;</mo><mi mathvariant="normal">z</mi><mo>&#8739;</mo><mo>&#8804;</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>. Here  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub></math> is proportional to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math>, so charge distribution is continuous for <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi mathvariant="normal">z</mi></mfenced><mo>&#8804;</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>

<math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mo>-</mo><mfrac><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">V</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">z</mi></mrow></mfrac><mo>=</mo><mn>10</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mi mathvariant="normal">z</mi></mfenced><mo>&#8805;</mo><mn>1</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi></math>. Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> is constant. </p><p>So, using the Poisson&rsquo;s equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>&#8711;</mo><mn>2</mn></msup><mi>V</mi><mo>=</mo><mo>-</mo><mfrac><mi>&#961;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mfrac></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#961;</mi><mo>=</mo><mn>0</mn></math>.

<math><mo>&#8756;</mo></math> The source is an infinity large non-conducting thick plate.  </p><p>Hence, consider a cylindrical Gaussian surface:</p><p>Applying Gauss&#39;s law for <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8739;</mo><mi mathvariant="normal">z</mi><mo>&#8739;</mo><mo>&#8804;</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">E</mi><mo>&#215;</mo><mn>2</mn><mi mathvariant="normal">A</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">&#961;</mi><mo>&#215;</mo><mn>2</mn><mi mathvariant="normal">z</mi><mo>&#215;</mo><mi mathvariant="normal">A</mi></mrow><msub><mi mathvariant="normal">&#949;</mi><mn>0</mn></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mn>10</mn><mi mathvariant="normal">z</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mi mathvariant="normal">A</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi mathvariant="normal">&#961;</mi><mo>(</mo><mn>2</mn><mi>Az</mi><mo>)</mo></mrow><msub><mi mathvariant="normal">&#949;</mi><mn>0</mn></msub></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi mathvariant="normal">&#961;</mi><mn>0</mn></msub><mo>=</mo><mn>10</mn><msub><mi mathvariant="normal">&#949;</mi><mn>0</mn></msub></math> for <math><mfenced close="|" open="|" separators="|"><mrow><mi mathvariant="normal">z</mi></mrow></mfenced><mo>&#8804;</mo><mn>1</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi></math>.</p>

</details>

---

### Q67. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

An electric field <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>E</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mn>25</mn><mi>&#160;</mi><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>30</mn><mi>&#160;</mi><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> exists in a region of space. If the potential at the origin is taken to be zero then the potential at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>110</mn><mi>&#160;</mi><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>140</mn><mi>&#160;</mi><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>130</mn><mi>&#160;</mi><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>120</mn><mi>&#160;</mi><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>110</mn><mi>&#160;</mi><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<math><mo>&#8757;</mo><mo>&#8710;</mo><mi>V</mi><mo>=</mo><mo>-</mo><mover accent="true"><mrow><mi>E</mi></mrow><mo>&#8594;</mo></mover><mo>.</mo><mo>&#8710;</mo><mover accent="true"><mrow><mi>r</mi></mrow><mo>&#8594;</mo></mover></math>

<math><mi>V</mi><mo>-</mo><mn>0</mn><mo>=</mo><mo>-</mo><mfenced separators="|"><mrow><mn>25</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>30</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>.</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mrow></mfenced></math>

<math><mo>=</mo><mo>-</mo><mfenced separators="|"><mrow><mn>50</mn><mo>+</mo><mn>60</mn></mrow></mfenced></math>

<math><mi>V</mi><mo>=</mo><mo>-</mo><mn>110</mn><mi>&#160;</mi><mi>v</mi><mi>o</mi><mi>l</mi><mi>t</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>110</mn><mi>&#160;</mi><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

</details>

---

### Q68. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `2`

<p>A uniformly charged solid sphere of radius R has potential <math><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub></math> (measured with respect to <math><mi>&#8734;</mi></math> ) on its surface. For this sphere the equipotential surfaces with potential <math><mfrac><mrow><mn>3</mn><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>4</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>4</mn></mrow></mfrac></math> and <math><mfrac><mrow><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>4</mn></mrow></mfrac></math> have radius <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></math> , <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msub></math> and <math><msub><mrow><mi>R</mi></mrow><mrow><mn>4</mn></mrow></msub></math> respectively. Then</p><p>Note : This question had two option correct at the time of examination. Proper corrections are made in the question to avoid it.</p>

**Options:**

- **(A)** <math><mn>2</mn><mi>R</mi><mo>&gt;</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>4</mn></mrow></msub></math>
- **(B)** <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0</mn></math>  and  <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>&gt;</mo><mfenced separators="|"><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>-</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow></mfenced></math>
- **(C)** <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>≠</mo><mn>0</mn></math> and <math><mfenced separators="|"><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced><mo>&gt;</mo><mi> </mi><mo>(</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>-</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>)</mo><mi> </mi></math>
- **(D)** <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0</mn></math> and <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>&lt;</mo><mfenced separators="|"><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>-</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0</mn></math> and <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>&lt;</mo><mfenced separators="|"><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>-</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow></mfenced></math>**

**Detailed Solution:**

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/P_53_Ans.jpg" style="width: 120px; height: 120px;" />
Potential for uniformly charged solid sphere

<math> <mrow> <mtext>v</mtext> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mtext>r</mtext> </mrow> </mfrac> </mrow> </math>      outside i.e r &gt; R

<math> <mrow> <mtext>v</mtext> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mtext>R</mtext> </mrow> </mfrac> </mrow> </math>  on the surface

<math> <mrow> <mtext>v</mtext> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mtext>R</mtext> </mrow> </mfrac> <mfenced close="]" open="[" separators=","> <mrow> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mfrac> <mrow> <msup> <mtext>r</mtext> <mn>2</mn> </msup> </mrow> <mrow> <msup> <mtext>R</mtext> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>  inside i.e. r &lt; R

Clearly

<math><mrow><mo>&#160;&#160;</mo> <mfrac> <mrow> <mn>3</mn> <msub> <mtext>v</mtext> <mn>0</mn> </msub> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mtext>,</mtext> <mfrac> <mrow> <mn>5</mn> <msub> <mtext>v</mtext> <mn>0</mn> </msub> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math> are inside potentials <math> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <mo>&#8757;</mo> <mo>&#62;</mo> <msub> <mtext>v</mtext> <mn>0</mn> </msub> </mrow> </mfenced> </mrow> </math>

<math> <mrow> <mfrac> <mrow> <mn>3</mn> <msub> <mtext>v</mtext> <mn>0</mn> </msub> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mtext>,</mtext> <mfrac> <mrow> <msub> <mtext>v</mtext> <mn>0</mn> </msub> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math> are outside potentials <math> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <mo>&#8757;</mo> <mo>&#60;</mo> <msub> <mtext>v</mtext> <mn>0</mn> </msub> </mrow> </mfenced> </mrow> </math>

To get <math> <mrow> <msub> <mtext>R</mtext> <mn>1</mn> </msub> </mrow> </math>: <math> <mrow> <mfrac> <mrow> <mn>3</mn> <msub> <mtext>v</mtext> <mn>0</mn> </msub> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mtext>R</mtext> </mrow> </mfrac> <mfenced close="]" open="[" separators=","> <mrow> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mfrac> <mrow> <msubsup> <mtext>R</mtext> <mn>1</mn> <mn>2</mn> </msubsup> </mrow> <mrow> <msup> <mtext>R</mtext> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>

<math><mrow><msub><mtext>where, v</mtext> <mn>0</mn> </msub> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mtext>R</mtext> </mrow> </mfrac> </mrow> </math>

<math> <mrow> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>2</mn> <mo>&#215;</mo> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mtext>R</mtext> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mtext>R</mtext> </mrow> </mfrac> <mfenced close="]" open="[" separators=","> <mrow> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mfrac> <mrow> <msubsup> <mtext>R</mtext> <mn>1</mn> <mn>2</mn> </msubsup> </mrow> <mrow> <msup> <mtext>R</mtext> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>

<math> <mrow> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mfrac> <mrow> <msubsup> <mtext>R</mtext> <mn>1</mn> <mn>2</mn> </msubsup> </mrow> <mrow> <msup> <mtext>R</mtext> <mn>2</mn> </msup> </mrow> </mfrac> <mo>&#8658;</mo> <msub> <mtext>R</mtext> <mn>1</mn> </msub> <mo>=</mo> <mn>0</mn> </mrow> </math>

To get <math> <mrow> <msub> <mtext>R</mtext> <mn>2</mn> </msub> </mrow> </math>: <math> <mrow> <mfrac> <mrow> <mn>5</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <msub> <mtext>v</mtext> <mn>0</mn> </msub> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mtext>R</mtext> </mrow> </mfrac> <mfenced close="]" open="[" separators=","> <mrow> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mfrac> <mrow> <msubsup> <mtext>R</mtext> <mn>2</mn> <mn>2</mn> </msubsup> </mrow> <mrow> <msup> <mtext>R</mtext> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>

<math> <mrow> <mfrac> <mrow> <mn>5</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mtext>R</mtext> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mtext>R</mtext> </mrow> </mfrac> <mfenced close="]" open="[" separators=","> <mrow> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mfrac> <mrow> <msubsup> <mtext>R</mtext> <mn>2</mn> <mn>2</mn> </msubsup> </mrow> <mrow> <msup> <mtext>R</mtext> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>

<math> <mrow> <mfrac> <mrow> <mn>5</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mfrac> <mrow> <msubsup> <mtext>R</mtext> <mn>2</mn> <mn>2</mn> </msubsup> </mrow> <mrow> <msup> <mtext>R</mtext> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </math>

<math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mfrac> <mrow> <msubsup> <mtext>R</mtext> <mn>2</mn> <mn>2</mn> </msubsup> </mrow> <mrow> <msup> <mtext>R</mtext> <mn>2</mn> </msup> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn>&#160; </mrow></mfrac></mrow></math><math> <mo>&#8658;</mo> </math> <math><mrow><msub><mtext>R</mtext> <mn>2</mn> </msub> <mo>=</mo> <mfrac> <mrow> <mtext>R</mtext> </mrow> <mrow> <msqrt> <mn>2</mn> </msqrt> </mrow> </mfrac> </mrow> </math>

To get <math> <mrow> <msub> <mtext>R</mtext> <mn>3</mn> </msub> </mrow> </math> : <math> <mrow> <mfrac> <mrow> <mn>3</mn> <msub> <mtext>v</mtext> <mn>0</mn> </msub> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <msub> <mtext>R</mtext> <mn>3</mn> </msub> </mrow> </mfrac> </mrow> </math>

<math> <mrow> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mtext>R</mtext> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <msub> <mtext>R</mtext> <mn>3</mn> </msub> </mrow> </mfrac> </mrow> </math>

<math> <mrow> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>4</mn> <mtext>R</mtext> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <msub> <mtext>R</mtext> <mn>3</mn> </msub> </mrow> </mfrac> </mrow> </math>

<math> <mrow> <msub> <mtext>R</mtext> <mn>3</mn> </msub> <mo>=</mo> <mfrac> <mrow> <mn>4</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> <mtext>R</mtext> </mrow> </math>

To get <math> <mrow> <msub> <mtext>R</mtext> <mn>4</mn> </msub> </mrow> </math>: <math> <mrow> <mfrac> <mrow> <msub> <mtext>v</mtext> <mn>0</mn> </msub> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <msub> <mtext>R</mtext> <mn>4</mn> </msub> </mrow> </mfrac> </mrow> </math>

<math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mo>&#215;</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mtext>R</mtext> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <msub> <mtext>R</mtext> <mn>4</mn> </msub> </mrow> </mfrac> </mrow> </math>

<math> <mrow> <msub> <mtext>R</mtext> <mn>4</mn> </msub> <mo>=</mo> <mn>4</mn> <mtext>R</mtext> </mrow> </math>

<math> <mrow> <msub> <mtext>R</mtext> <mn>4</mn> </msub> <mo>-</mo> <msub> <mtext>R</mtext> <mn>3</mn> </msub> <mo>=</mo> <mn>4</mn> <mtext>R</mtext> <mo>-</mo> <mfrac> <mrow> <mn>4</mn> <mtext>R</mtext> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>8</mn> <mtext>R</mtext> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> <mo>&#62;</mo> <msub> <mtext>R</mtext> <mn>2</mn> </msub> </mrow> </math>

<math> <mrow> <msub> <mtext>R</mtext> <mn>1</mn> </msub> <mo>=</mo> <mn>0</mn> </mrow> </math> and <math> <mrow> <msub> <mtext>R</mtext> <mn>2</mn> </msub> <mo>&#60;</mo> <mfenced close=")" open="(" separators=","> <mrow> <msub> <mtext>R</mtext> <mn>4</mn> </msub> <mo>-</mo> <msub> <mtext>R</mtext> <mn>3</mn> </msub> </mrow> </mfenced> </mrow> </math>

</details>

---

### Q69. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `1`

Assume that an electric field <math> <mrow> <mover accent="true"> <mtext>E</mtext> <mo>&#8594;</mo> </mover> <mo>=</mo> <mn>3</mn> <mn>0</mn> <msup> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>x</mi><mo>&#8289;</mo> </mrow> <mn>2</mn> </msup> <mover accent="true"> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>i</mi><mo>&#8289;</mo> </mrow> <mo>^</mo> </mover> </mrow> </math>  exists in space. Then the potential difference <math> <mrow> <msub> <mtext>V</mtext> <mtext>A</mtext> </msub> <mo>-</mo> <msub> <mtext>V</mtext> <mtext>O</mtext> </msub> </mrow> </math>  ,  where V<sub>O</sub> is the potential at the origin and V<sub>A</sub> the potential at x = 2 m is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>120</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>80</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>80</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<math><mo>&#8756;</mo><mi>d</mi><mi>V</mi><mo>=</mo><mo>-</mo><mover accent="true"><mrow><mi>E</mi></mrow><mo>&#8594;</mo></mover><mo>.</mo><mover accent="true"><mrow><mi>d</mi><mi>x</mi></mrow><mo>&#8594;</mo></mover></math>

Integrating both sides, 

<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><msub><mi>V</mi><mi>O</mi></msub><msub><mi>V</mi><mi>A</mi></msub></msubsup><mi>d</mi><mi>V</mi><mo>=</mo><mo>&#8722;</mo><mn>30</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>A</mi></msub><mo>&#8722;</mo><msub><mi>V</mi><mi>O</mi></msub><mo>=</mo><mo>&#8722;</mo><mn>30</mn><msubsup><mfenced open="[" close="]"><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mfenced><mn>0</mn><mn>2</mn></msubsup><mo>=</mo><mo>&#8722;</mo><mn>80</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

</details>

---

### Q70. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The gravitational field in a region is given by: $\vec{E}=(5 N / k g) \hat{i}+(12 N / k g) \hat{j}$
If the potential at the origin is taken to be zero, then the ratio of the potential at the points $(12 \mathrm{~m}, 0)$ and $(0,5 \mathrm{~m})$ is :

**Options:**

- **(A)** Zero
- **(B)** 1
- **(C)** $\frac{144}{25}$
- **(D)** $\frac{25}{144}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

From question, $\mathrm{E}_{\mathrm{x}}=5 \mathrm{~N} / \mathrm{kg}$ and $\mathrm{E}_{\mathrm{y}}=12 \mathrm{~N} / \mathrm{kg}$
Gravitational potential
$=$ Gravitational field $\times$ distance
$\therefore \mathrm{V}_{(12 \mathrm{~m}, 0)}=\mathrm{E}_{\mathrm{x}} \times 12 \mathrm{~J} / \mathrm{kg}$
and $\mathrm{V}_{(0,5 \mathrm{~m})}=\mathrm{E}_{\mathrm{y}} \times 5 \mathrm{~J} / \mathrm{kg}$
(Given : potential at the origin is zero)
$$
\therefore \frac{V_{(12 \mathrm{~m}, 0)}}{\mathrm{V}_{(0,5 \mathrm{~m})}}=\frac{\mathrm{E}_{\mathrm{x}} \times 12}{\mathrm{E}_{\mathrm{y}} \times 5}=\frac{5 \times 12}{12 \times 5}=1
$$

</details>

---

### Q71. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

This question has Statement-1 and Statement-2. Of the four choices given after the Statements, choose the one that best describes the two Statements.

Statement 1: No work is required to be done to move a test charge between any two points on an equipotential surface.
Statement 2 : Electric lines of force at the equipotential surfaces are mutually perpendicular to each other.

**Options:**

- **(A)** Statement 1 is true, Statement 2 is true, Statement 2 is the correct explanation of Statement 1.
- **(B)** Statement 1 is true, Statement 2 is true, Statement 2 is not the correct explanation of Statement 1.
- **(C)** Statement 1 is true, Statement 2 is false.
- **(D)** Statement 1 is false, Statement 2 is true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Statement 1 is true, Statement 2 is false.**

**Detailed Solution:**

The work done is moving a charge along an equipotential surface is always zero.
The direction of electric field is perpendicular to the equipotential surface or lines.

</details>

---

### Q72. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A point charge of magnitude $+1 \mu \mathrm{C}$ is fixed at $(0$, $0,0)$. An isolated uncharged spherical conductor, is fixed with its center at $(4,0,0)$. The potential and the induced electric field at the centre of the sphere is :

**Options:**

- **(A)** $1.8 \times 10^5 \mathrm{~V}$ and $-5.625 \times 10^6 \mathrm{~V} / \mathrm{m}$
- **(B)** $0 \mathrm{~V}$ and $0 \mathrm{~V} / \mathrm{m}$
- **(C)** $2.25 \times 10^5 \mathrm{~V}$ and $-5.625 \times 10^6 \mathrm{~V} / \mathrm{m}$
- **(D)** $2.25 \times 10^5 \mathrm{~V}$ and $0 \mathrm{~V} / \mathrm{m}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2.25 \times 10^5 \mathrm{~V}$ and $-5.625 \times 10^6 \mathrm{~V} / \mathrm{m}$**

**Detailed Solution:**

$\mathrm{q}=1 \mu \mathrm{C}=1 \times 10^{-6} \mathrm{C}$
$$
\mathrm{r}=4 \mathrm{~cm}=4 \times 10^{-2} \mathrm{~m}
$$
Potential $\mathrm{V}=\frac{\mathrm{kq}}{\mathrm{r}}$
$$
\begin{aligned}
& =\frac{9 \times 10^9 \times 10^{-6}}{4 \times 10^{-2}} \\
& =2.25 \times 10^5 \mathrm{~V} .
\end{aligned}
$$
Induced electric field $\mathrm{E}=-\frac{\mathrm{kq}}{\mathrm{r}^2}$
$$
=\frac{9 \times 10^9 \times 1 \times 10^{-6}}{16 \times 10^{-4}}=-5.625 \times 10^6 \mathrm{~V} / \mathrm{m}
$$

</details>

---

### Q73. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `3`

<p>A charge Q is uniformly distributed over a long rod AB of length L as shown in the figure. The electric potential at the point O lying at a distance L from the end A is :</p><p>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f6be4e73-2d8d-4671-b001-2c75bf140727-image.png" style="width: 340px; height: 46px;" /></p>

**Options:**

- **(A)** <math> <mrow> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mn>4</mn> <mi>&pi;</mi> <msub> <mo>&isin;</mo> <mn>0</mn> </msub> <mtext>L</mtext> <mtext mathvariant="italic"> ln </mtext> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
- **(B)** <math> <mrow> <mfrac> <mrow> <mtext>Q</mtext> <mtext mathvariant="italic"> ln </mtext> <mn>2</mn> </mrow> <mrow> <mn>4</mn> <mi>π</mi> <msub> <mo>∈</mo> <mn>0</mn> </msub> <mtext>L</mtext> </mrow> </mfrac> </mrow> </math>
- **(C)** <math> <mrow> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mn>8</mn> <mi>&pi;</mi> <msub> <mo>&isin;</mo> <mn>0</mn> </msub> <mtext>L</mtext> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>3</mn> <mtext>Q</mtext> </mrow> <mrow> <mn>4</mn> <mi>&pi;</mi> <msub> <mo>&isin;</mo> <mn>0</mn> </msub> <mtext>L</mtext> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math> <mrow> <mfrac> <mrow> <mtext>Q</mtext> <mtext mathvariant="italic"> ln </mtext> <mn>2</mn> </mrow> <mrow> <mn>4</mn> <mi>π</mi> <msub> <mo>∈</mo> <mn>0</mn> </msub> <mtext>L</mtext> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2e9f7e99-29e4-4d96-956b-3a68957b8764-image.png" style="width: 260px; height: 90px;" />

<math> <mrow> <mtext>V</mtext> <mo>=</mo> <munderover> <mo>&#8747;</mo> <mtext>L</mtext> <mrow> <mn>2</mn> <mtext>L</mtext> </mrow> </munderover> <mfrac> <mrow> <mtext>kdq</mtext> </mrow> <mrow> <mtext>x</mtext> </mrow> </mfrac> </mrow> </math>

<math> <mrow> <mo>=</mo> <munderover> <mo>&#8747;</mo> <mtext>L</mtext> <mrow> <mn>2</mn> <mtext>L</mtext> </mrow> </munderover> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mtext>L</mtext> </mrow> </mfrac> </mrow> </mfenced> <mtext>dx</mtext> </mrow> <mrow> <mtext>x</mtext> </mrow> </mfrac> </mrow> </math>

<math> <mrow> <mo>=</mo> <mfrac> <mrow> <mtext>Q</mtext> </mrow> <mrow> <mn>4</mn> <mi>&#960;</mi> <msub> <mi>&#949;</mi> <mn>0</mn> </msub> <mtext>L</mtext> </mrow> </mfrac> <mi>&#8467;</mi> <mtext>n</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mn>2</mn> </mrow> </mfenced> </mrow> </math>

</details>

---

### Q74. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `3`

A charge of total amount $Q$ is distributed over two concentric hollow spheres of radii $r$ and $R(R$ $>r$ ) such that the surface charge densities on the two spheres are equal. The electric potential at the common centre is

**Options:**

- **(A)** $\frac{1}{4 \pi \varepsilon_0} \frac{(R-r) Q}{\left(R^2+r^2\right)}$
- **(B)** $\frac{1}{4 \pi \varepsilon_0} \frac{(R+r) Q}{2\left(R^2+r^2\right)}$
- **(C)** $\left.\frac{1}{4 \pi \varepsilon_0} \frac{(R+r) Q}{\left(R^2+r^2\right.}\right)$
- **(D)** $\frac{1}{4 \pi \varepsilon_0} \frac{(R-r) Q}{2\left(R^2+r^2\right)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left.\frac{1}{4 \pi \varepsilon_0} \frac{(R+r) Q}{\left(R^2+r^2\right.}\right)$**

**Detailed Solution:**

Let $q_1$ and $q_2$ be charge on two spheres of radius ' $r$ ' and ' $R$ ' respectively As, $q_1+q_2=\mathrm{Q}$ and $\sigma_1=\sigma_2 \quad$ [Surface charge density are equal]
$$
\therefore \frac{q_1}{r \pi r^2}=\frac{q_2}{4 \pi R^2}
$$
So, $q_1=\frac{Q r^2}{R^2+r^2}$ and $q_2=\frac{Q R^2}{R^2+r^2}$
Now, potential, $V=\frac{1}{4 \pi \varepsilon_0}\left[\frac{q_1}{r}+\frac{q_2}{R}\right]$
$$
\begin{aligned}
& =\frac{1}{4 \pi \varepsilon_0}\left[\frac{Q r}{R^2+r^2}+\frac{Q R}{R^2+r^2}\right] \\
& =\frac{Q(R+r)}{R^2+r^2} \frac{1}{4 \pi \varepsilon_0}
\end{aligned}
$$

</details>

---

### Q75. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `2`

The electric potential $V(x)$ in a region around the origin is given by $V(x)=4 x^2$ volts. The electric charge enclosed in a cube of $1 \mathrm{~m}$ side with its centre at the origin is (in coulomb)

**Options:**

- **(A)** $8 \varepsilon_0$
- **(B)** $-4 \varepsilon_0$
- **(C)** 0
- **(D)** $-8 \varepsilon_0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

Charges reside only on the outer surface of a conductor with cavity.

</details>

---

### Q76. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `3`

This question has statement $1$ and statement $2$ . Of the four choices given after the statements, choose the one that best describes the two statements.
An insulating solid sphere of radius $\mathrm{R}$ has a uniformly positive charge density $\rho$. As a result of this uniform charge distribution there is a finite value of electric potential at the centre of the sphere, at the surface of the sphere and also at a point out side the sphere. The electric potential at infinity is zero.
Statement $1$: When a charge $q$ is taken from the centre to the surface of the sphere, its potential energy changes by $\frac{\mathrm{qp}}{3 \varepsilon_0}$
Statement $2$: The electric field at a distance $r(r < R)$ from the centre of the sphere is $\frac{\rho r}{3 \varepsilon_0}$

**Options:**

- **(A)** Statement $1$ is true, Statement $2$ is true, Statement $2$ is not the correct explanation for statement $1$.
- **(B)** Statement $1$ is true, Statement $2$ is false
- **(C)** Statement $1$ is false, Statement $2$ is true
- **(D)** Statement $1$ is true, Statement $2$ is the correct explanation for statement $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Statement $1$ is false, Statement $2$ is true**

**Detailed Solution:**

$\oint \overrightarrow{\mathrm{E}} \cdot \overrightarrow{\mathrm{d}} \mathrm{A}=\frac{1}{\varepsilon_0}\left(\rho \times \frac{4}{3} \pi \mathrm{r}^3\right)$
$\mathrm{E}=\frac{\rho \mathrm{r}}{3 \varepsilon_0}$
Statement $2$ is correct
$\Delta \mathrm{PE}=\left(\mathrm{V}_{\text {sur }}-\mathrm{V}_{\text {cent }}\right) \mathrm{q}=-\frac{\mathrm{q}}{6 \varepsilon_0} \rho \mathrm{R}^2$
Statement $1$ is incorrect

</details>

---

### Q77. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `3`

The electrostatic potential inside a charged spherical ball is given by $\phi=\alpha \rho^2+b$ where $r$ is the distance from the centre; $a, b$ are constants. Then the charge density inside ball is

**Options:**

- **(A)** $-6 a \varepsilon_0 r$
- **(B)** $-24 \pi a \varepsilon_0 r$
- **(C)** $-6 a \varepsilon_0$
- **(D)** $-24 \pi a \varepsilon_0 r$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-6 a \varepsilon_0$**

**Detailed Solution:**

Potential inside $(\phi)=a r^2+b$
$$
\therefore \mathrm{E}_{\mathrm{r}}=-\frac{\delta \mathrm{v}}{\delta \mathrm{r}}=-2 \mathrm{ar}
$$
Electric field inside uniformly charged solid volume varies with ' $r$ '. So charge density is constant
$$
\begin{aligned}
& \phi_{\text {net }}=(-2 \mathrm{ar}) 4 \pi \mathrm{r}^2=-8 \pi a r^3 \\
& -8 \pi \mathrm{ar}^3=\frac{\sigma \times \frac{4}{3} \pi \mathrm{r}^3}{\varepsilon_0} \\
& \therefore \sigma=-6 \mathrm{a} \varepsilon_0
\end{aligned}
$$

</details>

---

### Q78. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `2`

Two points $P$ and $Q$ are maintained at the potentials of $10 \mathrm{~V}$ and $-4 \mathrm{~V}$ respectively. The work done in moving 100 electrons from $P$ to $Q$ is

**Options:**

- **(A)** $-19 \times 10^{-17} \mathrm{~J}$
- **(B)** $9.60 \times 10^{-17} \mathrm{~J}$
- **(C)** $-2.24 \times 10^{-16} \mathrm{~J}$
- **(D)** $2.24 \times 10^{-16} \mathrm{~J}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2.24 \times 10^{-16} \mathrm{~J}$**

**Detailed Solution:**

$$
\begin{aligned}
& W=Q d V=Q\left(V_q-V_P\right)=-100 \times\left(1.6 \times 10^{-19}\right) \times(-4-10) \\
& =+100 \times 1.6 \times 10^{-19} \times 14=+2.2410^{-16} \mathrm{~J}
\end{aligned}
$$

</details>

---

### Q79. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `1`

This question contains Statement-1 and Statement-2. Of the four choices given after the statements, choose the one that best describes the two statements.
Statement - 1: For a charged particle moving from point $P$ to point $Q$, the net work done by an electrostatic field on the particle is independent of the path connecting point $P$ to point $Q$.
Statement-2: The net work done by a conservative force on an object moving along a closed loop is zero

**Options:**

- **(A)** Statement-1 is true, Statement-2 is false
- **(B)** Statement-1 is true, Statement-2 is true; Statement-2 is the correct explanation of Statement-1.
- **(C)** Statement-1 is true, Statement-2 is true; Statement-2 is not the correct explanation of Statement-1.
- **(D)** Statement-1 is false, Statement-2 is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement-1 is true, Statement-2 is true; Statement-2 is the correct explanation of Statement-1.**

**Detailed Solution:**

Work done by conservative force does not depend on the path. Electrostatic force is a conservative force.

</details>

---

### Q80. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `2`

The potential at a point $x$ (measured in $\mu \mathrm{m}$ ) due to some charges situated on the $\mathrm{x}$-axis is given by $\mathrm{V(x)=20 /\left(x^2-4\right)} \mathrm{~Volts}$. The electric field $\mathrm{E}$ at $\mathrm{x=4 ~\mu m}$ is given by

**Options:**

- **(A)** $5 / 3 \mathrm{~Volt}/$ $\mu \mathrm{m}$ and in the $-ve$ $x$ direction
- **(B)** $5 / 3 \mathrm{~Volt}/$ $\mu \mathrm{m}$ and in the $+ve$ $x$ direction.
- **(C)** $10 / 9 \mathrm{~Volt} / \mu \mathrm{m}$ and in the $-ve$ $x$ direction
- **(D)** $10 / 9 \mathrm{~Volt} / \mu \mathrm{m}$ and in the $+ve$ $x$ direction.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $10 / 9 \mathrm{~Volt} / \mu \mathrm{m}$ and in the $+ve$ $x$ direction.**

**Detailed Solution:**

$\mathrm{V_x=\frac{20}{x^2-4}}$
$\mathrm{E=-\frac{d V}{d x}=\frac{20}{\left(x^2-4\right)^2}(2 x-0)=\frac{160}{144}=\frac{10}{9}}$

</details>

---

### Q81. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `1`

An electric charge $10^{-3} \mu \mathrm{C}$ is placed at the origin $(0,0)$ of $X-Y$ co-ordinate system. Two points $A$ and $\mathrm{B}$ are situated at $(\sqrt{2}, \sqrt{2})$ and $(2,0)$ respectively. The potential difference between the points $A$ and $B$ will be

**Options:**

- **(A)** $9 \mathrm{~volt}$
- **(B)** zero
- **(C)** $2 \mathrm{~volt}$
- **(D)** $4.5 \mathrm{~volt}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) zero**

**Detailed Solution:**

Both points are at same distance from the charge.

</details>

---

### Q82. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `2`

Two insulating plates are both uniformly charged in such a way that the potential difference between them is $V_2-V_1=20 \mathrm{~V}$. (i.e. plate 2 is at a higher potential). The plates are separated by $d=0.1 \mathrm{~m}$ and can be treated as infinitely large. An electron is released from rest on the inner surface of plate 1 . What is its speed when it hits plate $2 ?$
$\left(\mathrm{e}=1.6 \times 10^{-19} \mathrm{C}, \mathrm{m}_{\mathrm{e}}=9.11 \times 10^{-31} \mathrm{~kg}\right)$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7RgZydYdIgxs3GSXGB7peZbJrJKolT9aih-buvofSvc.original.fullsize.png">

**Options:**

- **(A)** $32 \times 10^{-19} \mathrm{~m} / \mathrm{s}$
- **(B)** $2.65 \times 10^6 \mathrm{~m} / \mathrm{s}$
- **(C)** $7.02 \times 10^{12} \mathrm{~m} / \mathrm{s}$
- **(D)** $1.87 \times 10^6 \mathrm{~m} / \mathrm{s}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2.65 \times 10^6 \mathrm{~m} / \mathrm{s}$**

**Detailed Solution:**

$\frac{1}{2} \mathrm{mv}^2=\mathrm{eV}$
$\mathrm{v}=\sqrt{\frac{2 \mathrm{eV}}{\mathrm{m}}}=2.65 \times 10^6 \mathrm{~m} / \mathrm{s}$

</details>

---

### Q83. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `3`

Two thin wires rings each having a radius $R$ are placed at a distance $d$ apart with their axes coinciding. The charges on the two rings are $+q$ and $-q$. The potential difference between the centres of the two rings is

**Options:**

- **(A)** $\mathrm{QR} / 4 \pi \varepsilon_0 \mathrm{~d}^2$
- **(B)** $\frac{Q}{2 \pi \varepsilon_0}\left[\frac{1}{R}-\frac{1}{\sqrt{R^2+d^2}}\right]$
- **(C)** zero
- **(D)** $\frac{Q}{4 \pi \varepsilon_0}\left[\frac{1}{R}-\frac{1}{\sqrt{R^2+d^2}}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{Q}{2 \pi \varepsilon_0}\left[\frac{1}{R}-\frac{1}{\sqrt{R^2+d^2}}\right]$**

**Detailed Solution:**

$v_1=\frac{k q}{R}-\frac{k q}{\sqrt{R^2+d^2}}$
$v_2=\frac{-k q}{R}+\frac{k q}{\sqrt{R^2+d^2}}$

</details>

---

### Q84. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `3`

An $\alpha$-particle of energy $5 \mathrm{MeV}$ is scattered through $180^{\circ}$ by a fixed uranium nucleus. The distance of the closest approach is of the order of

**Options:**

- **(A)** $1 Å$
- **(B)** $10^{-10} \mathrm{~cm}$
- **(C)** $10^{-12} \mathrm{~cm}$
- **(D)** $10^{-15} \mathrm{~cm}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $10^{-12} \mathrm{~cm}$**

**Detailed Solution:**

At closest approach, all the kinetic energy of the $\alpha$-particle will converted into the potential energy of the system, K.E. = P.E.
$$
\begin{aligned}
& 5 \mathrm{MeV}=\frac{1}{4 \pi \varepsilon_0} \frac{\mathrm{q}_1 \mathrm{q}_2}{\mathrm{r}} \\
& 5 \times 10^6 \times \mathrm{e}=9 \times 10^9 \frac{\mathrm{Z}_1 \times \mathrm{Z}_2 \mathrm{e}^2}{\mathrm{r}} \\
& \mathrm{r}=\frac{9 \times 10^9 \times 92 \times 2 \times 1.6 \times 10^{-19}}{5 \times 10^6} \\
& \therefore \mathrm{r}=5.3 \times 10^{-14} \mathrm{~m}=5.3 \times 10^{-12} \mathrm{~cm}
\end{aligned}
$$

</details>

---

### Q85. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `3`

A charged particle $q$ is shot towards another charged particle $Q$ which is fixed, with a speed $v$ it approaches $Q$ upto a closest distance $r$ and then returns. If $q$ were given a speed $2 v$, the closest distances of approach would be

**Options:**

- **(A)** $\mathrm{r}$
- **(B)** $2 r$
- **(C)** $\mathrm{r} / 2$
- **(D)** $\mathrm{r} / 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{r} / 4$**

**Detailed Solution:**

By principle of conservation of energy
Finally, $\frac{1}{2} m(2 v)^2=\frac{K q Q}{r^2}$
Equation (i) $\div$ (ii),
$$
\begin{aligned}
& \frac{1}{4}=\frac{r^{\prime}}{r} \\
& \Rightarrow r^{\prime}=\frac{r}{4} .
\end{aligned}
$$

</details>

---

### Q86. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `3`

A thin spherical conducting shell of radius $\mathrm{R}$ has a charge $\mathrm{q}$. Another charge $\mathrm{Q}$ is placed at the centre of the shell. The electrostatic potential at a point $\mathrm{P}$ a distance $\frac{\mathrm{R}}{2}$ from the centre of the shell is

**Options:**

- **(A)** $\frac{2 Q}{4 \pi \varepsilon_0 R}$
- **(B)** $\frac{2 \mathrm{Q}}{4 \pi \varepsilon_0 \mathrm{R}}-\frac{2 \mathrm{q}}{4 \pi \varepsilon_0 \mathrm{R}}$
- **(C)** $\frac{2 Q}{4 \pi \varepsilon_0 R}+\frac{q}{4 \pi \varepsilon_0 R}$
- **(D)** $\frac{(\mathrm{q}+\mathrm{Q}) 2}{4 \pi \varepsilon_0 \mathrm{R}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2 Q}{4 \pi \varepsilon_0 R}+\frac{q}{4 \pi \varepsilon_0 R}$**

**Detailed Solution:**

Potential due to spherical shell, $\mathrm{v}_1=\frac{\mathrm{q}}{4 \pi \varepsilon_0 \mathrm{R}}$. Potential difference due to charge at the centre
$\mathrm{V}_2=\frac{2 \mathrm{Q}}{4 \pi \varepsilon_0 r} ; \mathrm{V}=\mathrm{V}_1+\mathrm{V}_2=\frac{2 \mathrm{Q}}{4 \pi \varepsilon_0 \mathrm{R}}+\frac{\mathrm{q}}{4 \pi \varepsilon_0 \mathrm{R}}$

</details>

---

### Q87. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `1`

On moving a charge of 20 coulombs by $2 \mathrm{~cm}, 2 \mathrm{~J}$ of work is done, then the potential difference between the points is

**Options:**

- **(A)** 0.1 V
- **(B)** 8 V
- **(C)** 2 V
- **(D)** 0.5 V

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0.1 V**

**Detailed Solution:**

$$
\mathrm{W}=\mathrm{qV} \Rightarrow \mathrm{V}_{\mathrm{A}}-\mathrm{V}_{\mathrm{B}}=2 / 20=0.1 \mathrm{~V}
$$
Here $W$ is the work done in moving charge $q$ from point $A$ to $B$

</details>

---

