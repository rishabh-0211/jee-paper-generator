# MHT CET Mathematics - Three Dimensional Geometry

## Topic 1: Basics of point in 3 dimension

**Total Questions:** 32

---

### Q1. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The Incenter of the triangle whose vertices are $A(0, 3, 0)$, $B(0, 0, 4)$, and $C(0, 3, 4)$ is;

**Options:**

- **(A)** $2\hat{i} + 3\hat{k}$
- **(B)** $2\hat{i} - 3\hat{k}$
- **(C)** $2\hat{j} - 3\hat{k}$
- **(D)** $2\hat{j} + 3\hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2\hat{j} + 3\hat{k}$**

**Detailed Solution:**

The vertices of the triangle are $A(0, 3, 0)$, $B(0, 0, 4)$, and $C(0, 3, 4)$.

The lengths of the sides of the triangle are:
$a = BC = \sqrt{(0-0)^2 + (3-0)^2 + (4-4)^2} = 3$
$b = AC = \sqrt{(0-0)^2 + (3-3)^2 + (4-0)^2} = 4$
$c = AB = \sqrt{(0-0)^2 + (0-3)^2 + (4-0)^2} = 5$

The coordinates of the incenter $I$ are given by the formula:
$I = \left( \dfrac{a x_1 + b x_2 + c x_3}{a + b + c}, \dfrac{a y_1 + b y_2 + c y_3}{a + b + c}, \dfrac{a z_1 + b z_2 + c z_3}{a + b + c} \right)$

Substituting the values:
$x = \dfrac{3(0) + 4(0) + 5(0)}{3 + 4 + 5} = 0$

$y = \dfrac{3(3) + 4(0) + 5(3)}{12} = \dfrac{9 + 0 + 15}{12} = 2$

$z = \dfrac{3(0) + 4(4) + 5(4)}{12} = \dfrac{0 + 16 + 20}{12} = 3$

The coordinates of the incenter are $(0, 2, 3)$.

In vector form, the position vector of the incenter is $2\hat{j} + 3\hat{k}$.

Answer: $2\hat{j} + 3\hat{k}$

</details>

---

### Q2. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In $\triangle ABC$, mid-points of the sides AB, BC and CA are respectively $(l, 0, 0), (0, m, 0)$ and $(0, 0, n)$. Then $\dfrac{(AB)^2 + (BC)^2 + (CA)^2}{l^2 + m^2 + n^2} = $

**Options:**

- **(A)** $2$
- **(B)** $16$
- **(C)** $1$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $8$**

**Detailed Solution:**

Let the midpoints of the sides $AB$, $BC$, and $CA$ be $D(l, 0, 0)$, $E(0, m, 0)$, and $F(0, 0, n)$ respectively.

By the midpoint theorem, the length of the line segment joining the midpoints of two sides of a triangle is half the length of the third side.

Therefore, $DE = \dfrac{1}{2} AC \Rightarrow AC^2 = 4 DE^2$

$EF = \dfrac{1}{2} AB \Rightarrow AB^2 = 4 EF^2$

$FD = \dfrac{1}{2} BC \Rightarrow BC^2 = 4 FD^2$

Using the distance formula, we calculate the squares of the distances between the midpoints:

$DE^2 = (l - 0)^2 + (0 - m)^2 + (0 - 0)^2 = l^2 + m^2$

$EF^2 = (0 - 0)^2 + (m - 0)^2 + (0 - n)^2 = m^2 + n^2$

$FD^2 = (0 - l)^2 + (0 - 0)^2 + (n - 0)^2 = n^2 + l^2$

Substituting these into the equations for the sides of the triangle:

$AC^2 = 4(l^2 + m^2)$

$AB^2 = 4(m^2 + n^2)$

$BC^2 = 4(n^2 + l^2)$

Adding the squares of the sides of the triangle:

$(AB)^2 + (BC)^2 + (CA)^2 = 4(m^2 + n^2) + 4(n^2 + l^2) + 4(l^2 + m^2)$

$(AB)^2 + (BC)^2 + (CA)^2 = 8(l^2 + m^2 + n^2)$

Thus, the required ratio is:

$\dfrac{(AB)^2 + (BC)^2 + (CA)^2}{l^2 + m^2 + n^2} = \dfrac{8(l^2 + m^2 + n^2)}{l^2 + m^2 + n^2} = 8$

Answer: $8$

</details>

---

### Q3. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $a$ and $b$ be the distances from the point $(2,3,4)$ to the XY plane and Y-Axis respectively. Then $a^2 + b^2 = $

**Options:**

- **(A)** $10$
- **(B)** $29$
- **(C)** $22$
- **(D)** $36$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $36$**

**Detailed Solution:**

The given point is $P(2, 3, 4)$.

The distance of a point $P(x, y, z)$ from the XY plane is given by $|z|$.

$a = |4| = 4$

The distance of a point $P(x, y, z)$ from the Y-axis is given by $\sqrt{x^2 + z^2}$.

$b = \sqrt{2^2 + 4^2} = \sqrt{4 + 16} = \sqrt{20}$

We need to find the value of $a^2 + b^2$.

$a^2 + b^2 = 4^2 + (\sqrt{20})^2 = 16 + 20 = 36$

Answer: $36$

</details>

---

### Q4. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The ratio and the coordinates of the point where the segment joining $(3, 5, 6)$ and $(4, 6, -3)$ is divided by the YZ-plane are respectively:

**Options:**

- **(A)** $4:3$ internally, $(0, 2, 33)$
- **(B)** $3:4$ internally, $(0, 2, 33)$
- **(C)** $3:4$ externally, $(0, 2, 33)$
- **(D)** $4:3$ externally, $(2, 0, 33)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3:4$ externally, $(0, 2, 33)$**

**Detailed Solution:**

Let the YZ-plane divide the line segment joining the points $(3, 5, 6)$ and $(4, 6, -3)$ in the ratio $k:1$.

The coordinates of the point of division are $\left(\dfrac{4k+3}{k+1}, \dfrac{6k+5}{k+1}, \dfrac{-3k+6}{k+1}\right)$.

Since the point lies on the YZ-plane, its x-coordinate is zero.

$\dfrac{4k+3}{k+1} = 0 \Rightarrow 4k + 3 = 0 \Rightarrow k = -\dfrac{3}{4}$

The negative sign indicates that the division is external. Thus, the ratio is $3:4$ externally.

Substituting $k = -\dfrac{3}{4}$ into the y and z coordinates:

$y = \dfrac{6\left(-\dfrac{3}{4}\right) + 5}{-\dfrac{3}{4} + 1} = \dfrac{-\dfrac{9}{2} + 5}{\dfrac{1}{4}} = \dfrac{\dfrac{1}{2}}{\dfrac{1}{4}} = 2$

$z = \dfrac{-3\left(-\dfrac{3}{4}\right) + 6}{-\dfrac{3}{4} + 1} = \dfrac{\dfrac{9}{4} + 6}{\dfrac{1}{4}} = \dfrac{\dfrac{33}{4}}{\dfrac{1}{4}} = 33$

The coordinates of the point are $(0, 2, 33)$.

Answer: $3:4$ externally, $(0, 2, 33)$

</details>

---

### Q5. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The ratio in which the point $\hat{i} + 2\hat{j} + 3\hat{k}$ divides the line segment joining $-2\hat{i} + 3\hat{j} + 5\hat{k}$ and $7\hat{i} - \hat{k}$ is....

**Options:**

- **(A)** $1:2$
- **(B)** $2:3$
- **(C)** $3:4$
- **(D)** $1:4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1:2$**

**Detailed Solution:**

Let the required ratio be $\lambda : 1$.

The position vector of the point dividing the line segment joining $\vec{a} = -2\hat{i} + 3\hat{j} + 5\hat{k}$ and $\vec{b} = 7\hat{i} - \hat{k}$ is given by:

$\vec{r} = \dfrac{\lambda \vec{b} + \vec{a}}{\lambda + 1}$

Given $\vec{r} = \hat{i} + 2\hat{j} + 3\hat{k}$, we have:

$\hat{i} + 2\hat{j} + 3\hat{k} = \dfrac{\lambda(7\hat{i} - \hat{k}) + (-2\hat{i} + 3\hat{j} + 5\hat{k})}{\lambda + 1}$

Equating the coefficients of $\hat{i}$ on both sides:

$1 = \dfrac{7\lambda - 2}{\lambda + 1}$

$\lambda + 1 = 7\lambda - 2$

$6\lambda = 3$

$\lambda = \dfrac{1}{2}$

The ratio is $1:2$.

Answer: $1:2$

</details>

---

### Q6. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If M denotes the midpoint of the line joining A$(4, 5, -10)$ and B$(-1, 2, 1)$, then the equation of the plane through M and perpendicular to AB is:

**Options:**

- **(A)** $\bar{r} \cdot \left(-5\hat{i} - 3\hat{j} + 11\hat{k}\right) + \dfrac{135}{2} = 0$
- **(B)** $\bar{r} \cdot \left(\dfrac{3}{2}\hat{i} + \dfrac{7}{2}\hat{j} - \dfrac{9}{2}\hat{k}\right) + \dfrac{135}{2} = 0$
- **(C)** $\bar{r} \cdot \left(4\hat{i} + 5\hat{j} - 10\hat{k}\right) + 4 = 0$
- **(D)** $\bar{r} \cdot \left(-\hat{i} + 2\hat{j} + \hat{k}\right) + 4 = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\bar{r} \cdot \left(-5\hat{i} - 3\hat{j} + 11\hat{k}\right) + \dfrac{135}{2} = 0$**

**Detailed Solution:**

The coordinates of the midpoint $M$ of the line segment joining $A(4, 5, -10)$ and $B(-1, 2, 1)$ are given by:

$M = \left(\dfrac{4 - 1}{2}, \dfrac{5 + 2}{2}, \dfrac{-10 + 1}{2}\right) = \left(\dfrac{3}{2}, \dfrac{7}{2}, -\dfrac{9}{2}\right)$

The normal vector $\vec{n}$ to the plane is parallel to the vector $\overrightarrow{AB}$ since the plane is perpendicular to $AB$.

$\vec{n} = \overrightarrow{AB} = (-1 - 4)\hat{i} + (2 - 5)\hat{j} + (1 - (-10))\hat{k} = -5\hat{i} - 3\hat{j} + 11\hat{k}$

The equation of the plane passing through $M$ with normal vector $\vec{n}$ is:

$(\bar{r} - \vec{m}) \cdot \vec{n} = 0$

$\bar{r} \cdot \vec{n} = \vec{m} \cdot \vec{n}$

Substituting the values of $\vec{m}$ and $\vec{n}$:

$\vec{m} \cdot \vec{n} = \left(\dfrac{3}{2}\hat{i} + \dfrac{7}{2}\hat{j} - \dfrac{9}{2}\hat{k}\right) \cdot (-5\hat{i} - 3\hat{j} + 11\hat{k})$

$\vec{m} \cdot \vec{n} = \dfrac{3}{2}(-5) + \dfrac{7}{2}(-3) + \left(-\dfrac{9}{2}\right)(11)$

$\vec{m} \cdot \vec{n} = -\dfrac{15}{2} - \dfrac{21}{2} - \dfrac{99}{2} = -\dfrac{135}{2}$

Thus, the equation of the plane is:

$\bar{r} \cdot (-5\hat{i} - 3\hat{j} + 11\hat{k}) = -\dfrac{135}{2}$

$\bar{r} \cdot (-5\hat{i} - 3\hat{j} + 11\hat{k}) + \dfrac{135}{2} = 0$

Answer: $\bar{r} \cdot \left(-5\hat{i} - 3\hat{j} + 11\hat{k}\right) + \dfrac{135}{2} = 0$

</details>

---

### Q7. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

From a point P $(a, b, c)$, perpendiculars PA and PB are drawn to XY plane and ZX plane respectively. If O is the origin, then the equation of plane OAB is

**Options:**

- **(A)** $\dfrac{x}{a} - \dfrac{y}{b} - \dfrac{z}{c} = 0$
- **(B)** $\dfrac{x}{a} - \dfrac{y}{b} + \dfrac{z}{c} = 0$
- **(C)** $\dfrac{x}{a} + \dfrac{y}{b} - \dfrac{z}{c} = 0$
- **(D)** $\dfrac{x}{a} + \dfrac{y}{b} + \dfrac{z}{c} = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{x}{a} - \dfrac{y}{b} - \dfrac{z}{c} = 0$**

**Detailed Solution:**

The coordinates of point P are $(a, b, c)$.

Since PA is perpendicular to the XY plane, the $z$-coordinate of A is $0$. Thus, the coordinates of A are $(a, b, 0)$.

Since PB is perpendicular to the ZX plane, the $y$-coordinate of B is $0$. Thus, the coordinates of B are $(a, 0, c)$.

The equation of the plane passing through the origin O $(0, 0, 0)$, A $(a, b, 0)$, and B $(a, 0, c)$ is given by:

$\begin{vmatrix} x & y & z \\ a & b & 0 \\ a & 0 & c \end{vmatrix} = 0$

Expanding the determinant along the first row, we get:

$x(bc - 0) - y(ac - 0) + z(0 - ab) = 0$

$bcx - acy - abz = 0$

Dividing the entire equation by $abc$, we get:

$\dfrac{x}{a} - \dfrac{y}{b} - \dfrac{z}{c} = 0$

Answer: $\dfrac{x}{a} - \dfrac{y}{b} - \dfrac{z}{c} = 0$

</details>

---

### Q8. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If A and B are the feet of the perpendiculars drawn from $(1, 2, 3)$ to planes $YZ$ and $ZX$, then the equation of the plane passing through the points A, B and the origin is

**Options:**

- **(A)** $6x + 3y + 2z = 0$
- **(B)** $6x - 3y - 2z = 0$
- **(C)** $6x + 3y - 2z = 0$
- **(D)** $3x + 6y + 2z = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $6x + 3y - 2z = 0$**

**Detailed Solution:**

Let the given point be $P(1, 2, 3)$.

The foot of the perpendicular from $P$ to the $YZ$-plane ($x = 0$) is $A(0, 2, 3)$.

The foot of the perpendicular from $P$ to the $ZX$-plane ($y = 0$) is $B(1, 0, 3)$.

The equation of the plane passing through the origin $(0, 0, 0)$ is $ax + by + cz = 0$.

Since the plane passes through $A(0, 2, 3)$ and $B(1, 0, 3)$, we have:

$2b + 3c = 0$

$a + 3c = 0$

Solving these equations, we get $a = -3c$ and $b = -\dfrac{3}{2}c$.

Substituting the values of $a$ and $b$ in the equation of the plane:

$-3cx - \dfrac{3}{2}cy + cz = 0$

Dividing by $-\dfrac{c}{2}$, we get the required equation of the plane:

$6x + 3y - 2z = 0$

Answer: $6x + 3y - 2z = 0$

</details>

---

### Q9. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the product of the distances of the point (1, 2, 3) from the origin and the plane $2x - 3y + z + k = 0$ is 7, then the value of k is

**Options:**

- **(A)** $8$
- **(B)** $10$
- **(C)** $7$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $8$**

**Detailed Solution:**

Distance of the point $(1, 2, 3)$ from the origin is $d_1 = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{14}$

Distance of the point $(1, 2, 3)$ from the plane $2x - 3y + z + k = 0$ is $d_2 = \dfrac{|2(1) - 3(2) + 1(3) + k|}{\sqrt{2^2 + (-3)^2 + 1^2}} = \dfrac{|k - 1|}{\sqrt{14}}$

Given that $d_1 \times d_2 = 7$

$\sqrt{14} \times \dfrac{|k - 1|}{\sqrt{14}} = 7$

$|k - 1| = 7$

$k - 1 = 7$ or $k - 1 = -7$

$k = 8$ or $k = -6$

From the given options, $k = 8$.

Answer: $8$

</details>

---

### Q10. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the centroid of a tetrahedron $OABC$ is $(1, 2, -1)$, where O is the origin, $A(a, 2, 3), B(1, b, 2), C(2, 1, c)$ are the other vertices, then the distance of the point $P(a, b, c)$ from the origin is...

**Options:**

- **(A)** $42$ units
- **(B)** $\sqrt{107}$ units
- **(C)** $25$ units
- **(D)** $15$ units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{107}$ units**

**Detailed Solution:**

The coordinates of the centroid of a tetrahedron with vertices $(x_1, y_1, z_1)$, $(x_2, y_2, z_2)$, $(x_3, y_3, z_3)$, and $(x_4, y_4, z_4)$ are given by $\left( \dfrac{x_1 + x_2 + x_3 + x_4}{4}, \dfrac{y_1 + y_2 + y_3 + y_4}{4}, \dfrac{z_1 + z_2 + z_3 + z_4}{4} \right)$.

Given the vertices $O(0, 0, 0)$, $A(a, 2, 3)$, $B(1, b, 2)$, and $C(2, 1, c)$, and the centroid $(1, 2, -1)$, equating the coordinates gives:

$\dfrac{0 + a + 1 + 2}{4} = 1 \Rightarrow a + 3 = 4 \Rightarrow a = 1$

$\dfrac{0 + 2 + b + 1}{4} = 2 \Rightarrow b + 3 = 8 \Rightarrow b = 5$

$\dfrac{0 + 3 + 2 + c}{4} = -1 \Rightarrow c + 5 = -4 \Rightarrow c = -9$

The point $P(a, b, c)$ is $(1, 5, -9)$.

The distance of $P$ from the origin is:

$OP = \sqrt{1^2 + 5^2 + (-9)^2} = \sqrt{1 + 25 + 81} = \sqrt{107}$ units.

Answer: $\sqrt{107}$ units

</details>

---

### Q11. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A plane meets the coordinate axes at points A, B and C, such that the centroid of a triangle ABC is $\left(2, -\dfrac{2}{3}, \dfrac{1}{2}\right)$. The perpendicular distance from the origin to this plane is...

**Options:**

- **(A)** $\dfrac{6}{\sqrt{26}}$
- **(B)** $\dfrac{5}{\sqrt{26}}$
- **(C)** $\dfrac{4}{\sqrt{26}}$
- **(D)** $\dfrac{3}{\sqrt{26}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{6}{\sqrt{26}}$**

**Detailed Solution:**

Let the coordinates of points A, B, and C on the coordinate axes be $(a, 0, 0)$, $(0, b, 0)$, and $(0, 0, c)$ respectively.

The equation of the plane passing through these points is $\dfrac{x}{a} + \dfrac{y}{b} + \dfrac{z}{c} = 1$.

The centroid of the triangle ABC is given by $\left(\dfrac{a}{3}, \dfrac{b}{3}, \dfrac{c}{3}\right)$.

Comparing this with the given centroid $\left(2, -\dfrac{2}{3}, \dfrac{1}{2}\right)$, we obtain:

$\dfrac{a}{3} = 2 \Rightarrow a = 6$

$\dfrac{b}{3} = -\dfrac{2}{3} \Rightarrow b = -2$

$\dfrac{c}{3} = \dfrac{1}{2} \Rightarrow c = \dfrac{3}{2}$

Substituting the values of $a$, $b$, and $c$ in the equation of the plane:

$\dfrac{x}{6} + \dfrac{y}{-2} + \dfrac{z}{\dfrac{3}{2}} = 1$

$\dfrac{x}{6} - \dfrac{y}{2} + \dfrac{2z}{3} = 1$

Multiplying the entire equation by 6:

$x - 3y + 4z = 6$

$x - 3y + 4z - 6 = 0$

The perpendicular distance $d$ from the origin $(0, 0, 0)$ to this plane is:

$d = \dfrac{|1(0) - 3(0) + 4(0) - 6|}{\sqrt{1^2 + (-3)^2 + 4^2}}$

$d = \dfrac{|-6|}{\sqrt{1 + 9 + 16}} = \dfrac{6}{\sqrt{26}}$

</details>

---

### Q12. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The centroid of tetrahedron with vertices $\mathrm{A}(3,-5, x), \mathrm{B}(5,4,2)$, $\mathrm{C}(7,-7, \mathrm{y}), \mathrm{D}(1,0, \mathrm{z})$ is $\mathrm{G}(4,-2,2)$, then $x+\mathrm{y}+\mathrm{z}=$

**Options:**

- **(A)** 6
- **(B)** 2
- **(C)** -6
- **(D)** -2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 6**

**Detailed Solution:**

The centroid of a tetrahedron with vertices $(x_1, y_1, z_1)$, $(x_2, y_2, z_2)$, $(x_3, y_3, z_3)$, and $(x_4, y_4, z_4)$ is given by $\left( \dfrac{x_1+x_2+x_3+x_4}{4}, \dfrac{y_1+y_2+y_3+y_4}{4}, \dfrac{z_1+z_2+z_3+z_4}{4} \right)$.

Given vertices are $A(3,-5, x)$, $B(5,4,2)$, $C(7,-7, y)$, $D(1,0, z)$ and centroid is $G(4,-2,2)$.

Equating the z-coordinates, we get:

$\dfrac{x + 2 + y + z}{4} = 2$

$x + y + z + 2 = 8$

$x + y + z = 6$

Answer: 6

</details>

---

### Q13. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the sum of the squares of the distances of a point $P(x, y, z)$ from the three co-ordinate axes is 324 , then the distance of point $P$ from the origin is ....

**Options:**

- **(A)** $18$
- **(B)** $162$
- **(C)** $9 \sqrt{2}$
- **(D)** $324$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $9 \sqrt{2}$**

**Detailed Solution:**

For a point $P(x, y, z)$, the distance from the x-axis is $\sqrt{y^2 + z^2}$.

The distance from the y-axis is $\sqrt{x^2 + z^2}$.

The distance from the z-axis is $\sqrt{x^2 + y^2}$.

The sum of the squares of the distances from the three coordinate axes is $324$.

$(y^2 + z^2) + (x^2 + z^2) + (x^2 + y^2) = 324$

$2(x^2 + y^2 + z^2) = 324$

$x^2 + y^2 + z^2 = 162$

The distance of point $P$ from the origin is $\sqrt{x^2 + y^2 + z^2}$.

$\sqrt{x^2 + y^2 + z^2} = \sqrt{162} = 9\sqrt{2}$

Answer: $9 \sqrt{2}$

</details>

---

### Q14. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the plane $\frac{x}{3}+\frac{y}{2}-\frac{z}{4}=1$ cuts the co-ordinate axes at points $\mathrm{A}, \mathrm{B}$ and C , then the area of the triangle $A B C$ is

**Options:**

- **(A)** $\frac{\sqrt{61}}{2}$ sq. units
- **(B)** $2 \sqrt{61}$ sq. units
- **(C)** $\sqrt{61}$ sq. units
- **(D)** $3 \sqrt{61}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{61}$ sq. units**

**Detailed Solution:**

The equation of the plane is $\dfrac{x}{3} + \dfrac{y}{2} - \dfrac{z}{4} = 1$.

The plane intersects the coordinate axes at $A(3, 0, 0)$, $B(0, 2, 0)$, and $C(0, 0, -4)$.

The position vectors of the points are $\vec{a} = 3\hat{i}$, $\vec{b} = 2\hat{j}$, and $\vec{c} = -4\hat{k}$.

The vectors representing the sides of the triangle are:

$\overrightarrow{AB} = \vec{b} - \vec{a} = -3\hat{i} + 2\hat{j}$

$\overrightarrow{AC} = \vec{c} - \vec{a} = -3\hat{i} - 4\hat{k}$

The cross product of these vectors is:

$\overrightarrow{AB} \times \overrightarrow{AC} = (-3\hat{i} + 2\hat{j}) \times (-3\hat{i} - 4\hat{k}) = -8\hat{i} - 12\hat{j} + 6\hat{k}$

The area of $\triangle ABC$ is given by $\dfrac{1}{2} |\overrightarrow{AB} \times \overrightarrow{AC}|$.

Area $= \dfrac{1}{2} \sqrt{(-8)^2 + (-12)^2 + 6^2}$

Area $= \dfrac{1}{2} \sqrt{64 + 144 + 36}$

Area $= \dfrac{1}{2} \sqrt{244}$

Area $= \dfrac{1}{2} \times 2\sqrt{61} = \sqrt{61}$ sq. units.

Answer: $\sqrt{61}$ sq. units

</details>

---

### Q15. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the sum of the squares of the distance of the point $\mathrm{P}(\mathrm{x}, \mathrm{y}, \mathrm{z})$ from the co-ordinate axes is 242 , then the distance of the point $P$ from the origin is _______ units.

**Options:**

- **(A)** $121$
- **(B)** $11$
- **(C)** $22$
- **(D)** $\frac{121}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $11$**

**Detailed Solution:**

The distance of the point $P(x, y, z)$ from the x-axis is $\sqrt{y^2 + z^2}$.

The distance of the point $P(x, y, z)$ from the y-axis is $\sqrt{x^2 + z^2}$.

The distance of the point $P(x, y, z)$ from the z-axis is $\sqrt{x^2 + y^2}$.

The sum of the squares of the distances from the coordinate axes is given by:

$(y^2 + z^2) + (x^2 + z^2) + (x^2 + y^2) = 242$

$2(x^2 + y^2 + z^2) = 242$

$x^2 + y^2 + z^2 = 121$

The distance of the point $P$ from the origin is $\sqrt{x^2 + y^2 + z^2}$.

$\sqrt{x^2 + y^2 + z^2} = \sqrt{121} = 11$ units.

Answer: $11$

</details>

---

### Q16. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\triangle \mathrm{ABC}$ is right angled at $\mathrm{A}$, where $\mathrm{A} \equiv(4,2, x), \mathrm{B} \equiv(3,1,8)$ and $\mathrm{C} \equiv(2,-1,2)$, then the value of $x$ is

**Options:**

- **(A)** $4$
- **(B)** $2$
- **(C)** $3$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3$**

**Detailed Solution:**

Since $\triangle \mathrm{ABC}$ is right angled at $\mathrm{A}$,
$$
\begin{aligned}
& \overline{\mathrm{AB}} \cdot \overline{\mathrm{AC}}=0 \\
& \Rightarrow[-\hat{\mathrm{i}}-\hat{\mathrm{j}}+(8-x) \hat{\mathrm{k}}] \cdot(-2 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}+(2-x) \hat{\mathrm{k}})=0 \\
& \Rightarrow 2+3+(8-x)(2-x)=0 \\
& \Rightarrow x^2-10 x+21=0 \\
& \Rightarrow(x-3)(x-7)=0 \\
& \Rightarrow x=3 \text { or } x=7
\end{aligned}
$$

</details>

---

### Q17. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A tetrahedron has vertices at $\mathrm{P}(2,1,3)$, $\mathrm{Q}(-1,1,2), \mathrm{R}(1,2,1)$ and $\mathrm{O}(0,0,0)$, then angle between the faces OPQ and PQR is

**Options:**

- **(A)** $\cos ^{-1}\left(\frac{5}{7 \sqrt{59}}\right)$
- **(B)** $\cos ^{-1}\left(\frac{\sqrt{25}}{\sqrt{59} \cdot \sqrt{35}}\right)$
- **(C)** $\cos ^{-1}\left(\frac{5}{413}\right)$
- **(D)** $\quad \cos ^{-1}\left(\frac{25}{\sqrt{59} \sqrt{35}}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\quad \cos ^{-1}\left(\frac{25}{\sqrt{59} \sqrt{35}}\right)$**

**Detailed Solution:**

$\begin{aligned} O P \times O Q & =\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 2 & 1 & 3 \\ -1 & 1 & 2\end{array}\right| \\ & =-\hat{\mathrm{i}}-7 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}\end{aligned}$
$\begin{aligned} P Q \times P R & =\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ -3 & 0 & -1 \\ -1 & 1 & -2\end{array}\right| \\ & =\hat{\mathrm{i}}-5 \hat{\mathrm{j}}-3 \hat{\mathrm{k}}\end{aligned}$
Angle between the faces OPQ and PQR is
$\cos \theta=\frac{(-\hat{\mathrm{i}}-7 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}) \cdot(\hat{\mathrm{i}}-5 \hat{\mathrm{j}}-3 \hat{\mathrm{k}})}{\sqrt{(-1)^2+(-7)^2+3^2} \sqrt{1^2+(-5)^2+(-3)^2}}$
$=\frac{-1+35-9}{\sqrt{59} \sqrt{35}}$
$\begin{aligned} & \Rightarrow \cos \theta=\frac{25}{\sqrt{59} \sqrt{35}} \\ & \Rightarrow \theta=\cos ^{-1}\left(\frac{25}{\sqrt{59} \sqrt{35}}\right)\end{aligned}$

</details>

---

### Q18. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The incentre of the triangle $\mathrm{ABC}$, whose vertices are $\mathrm{A}(0,2,1), \mathrm{B}(-2,0,0)$ and $\mathrm{C}(-2,0,2)$, is

**Options:**

- **(A)** $\left(-\frac{3}{2}, \frac{1}{2}, 1\right)$
- **(B)** $\left(\frac{3}{2}, \frac{1}{2}, 1\right)$
- **(C)** $\left(-\frac{3}{2},-\frac{1}{2},-1\right)$
- **(D)** $\left(\frac{3}{2},-\frac{1}{2},-1\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(-\frac{3}{2}, \frac{1}{2}, 1\right)$**

**Detailed Solution:**

Let $\bar{a}=2 \hat{j}+\hat{k}, \hat{b}=-2 \hat{i}, \hat{c}=-2 \hat{i}+2 \hat{k}$
$\therefore \quad \overline{\mathrm{AB}}=-2 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}-\hat{\mathrm{k}}$,
$\overline{\mathrm{BC}}=2 \hat{\mathrm{k}}$
$\begin{aligned} & \overline{\mathrm{AC}}=-2 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\hat{\mathrm{k}} \\ & \Rightarrow|\overline{\mathrm{AB}}|=3,|\overline{\mathrm{BC}}|=2,|\overline{\mathrm{AC}}|=3\end{aligned}$
Incentre of $\triangle \mathrm{ABC}$ is given by
$\frac{|\overline{\mathrm{AB}}| \overline{\mathrm{c}}+|\overline{\mathrm{BC}}| \overline{\mathrm{a}}+|\overline{\mathrm{AC}}| \overline{\mathrm{b}}}{|\overline{\mathrm{AB}}|+|\overline{\mathrm{BC}}|+|\overline{\mathrm{AC}}|}$
$\begin{aligned} & =\frac{3(-2 \hat{i}+2 \hat{k})+2(2 \hat{j}+\hat{k})+3(-2 \hat{i})}{3+2+3} \\ & =\frac{-12 \hat{i}+4 \hat{j}+8 \hat{k}}{8} \\ & =-\frac{3}{2} \hat{i}+\frac{1}{2} \hat{j}+\hat{k}\end{aligned}$

</details>

---

### Q19. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A(1,4,2)$ and $C(5,-7,1)$ are two vertices of triangle $\mathrm{ABC}$ and $\mathrm{G}\left(\frac{4}{3}, 0, \frac{-2}{3}\right)$ is centroid of the triangle $\mathrm{ABC}$, then the mid point of side $\mathrm{BC}$ is

**Options:**

- **(A)** $\left(-2,-2, \frac{3}{2}\right)$
- **(B)** $\left(2,2, \frac{3}{2}\right)$
- **(C)** $\left(\frac{3}{2}, 2,-2\right)$
- **(D)** $\left(\frac{3}{2},-2,-2\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(\frac{3}{2},-2,-2\right)$**

**Detailed Solution:**

Let $\mathrm{B} \equiv\left(x_1, y_1, \mathrm{z}_1\right)$
Co-ordinates of centroid
$$
\begin{gathered}
\equiv\left(\frac{1+x_1+5}{3}, \frac{4+y_1-7}{3}, \frac{2+\mathrm{z}_1+1}{3}\right) \\
\Rightarrow\left(\frac{4}{3}, 0, \frac{-2}{3}\right) \equiv\left(\frac{6+x_1}{3}, \frac{y_1-3}{3}, \frac{3+\mathrm{z}_1}{3}\right) \\
\Rightarrow x_1=-2, y_1=3, \mathrm{z}_1=-5 \\
\therefore \quad \mathrm{B} \equiv(-2,3,-5) \\
\text { Midpoint side } \mathrm{BC}=\left(\frac{-2+5}{2}, \frac{3-7}{2}, \frac{-5+1}{2}\right) \\
=\left(\frac{3}{2},-2,-2\right)
\end{gathered}
$$

</details>

---

### Q20. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The length (in units) of the projection of the line segment, joining the points $(5,-1,4)$ and $(4,-1,3)$, on the plane $x+y+z=7$ is

**Options:**

- **(A)** $\frac{2}{\sqrt{3}}$
- **(B)** $\frac{2}{3}$
- **(C)** $\frac{\sqrt{2}}{3}$
- **(D)** $\sqrt{\frac{2}{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{\frac{2}{3}}$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } A=(5,-1,4), B=(4,-1,3) \\ & \overline{\mathrm{AB}}=-\hat{\mathrm{i}}-\hat{\mathrm{k}} \Rightarrow|\overline{\mathrm{AB}}|=\sqrt{2}\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Jn8sIK4sAOXQoe2CpB5TGW7FISg5nt8BBd2W_rllO7Y.original.fullsize.png">

Projection of $\overline{\mathrm{AB}}$ in the plane $x+y+z=7$ is $|\overline{\mathrm{AB}}| \cos \theta=\left|\overline{\mathrm{A}^{\prime} \mathrm{B}^{\prime}}\right| \cos \theta$

Direction ratios of normal to the given plane is $1,1,1$.
$$
\begin{aligned}
& \cos \left(90^{\circ}-\theta\right)=\left|\frac{1(-1)+1(0)+1(-1)}{\sqrt{1^2+1^2+1^2} \sqrt{1^2+0^2+1^2}}\right| \\
& \begin{array}{r}
\sin \theta=\frac{2}{\sqrt{6}} \Rightarrow \cos \theta=\sqrt{1-\frac{4}{6}}=\sqrt{\frac{1}{3}} \\
\text { Required projection }=|\overline{\mathrm{AB}}| \cos \theta \\
=\sqrt{2} \times \frac{1}{\sqrt{3}}=\sqrt{\frac{2}{3}}
\end{array}
\end{aligned}
$$

</details>

---

### Q21. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the area of the triangle with vertices $(1,2,0)$, $(1,0,2)$ and $(0, x, 1)$ is $\sqrt{6}$ square units, then the value of $x$ is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \mathrm{A} \equiv(1,2,0), \mathrm{B} \equiv(1,0,2) \text { and } \mathrm{C} \equiv(0, x, 1) \\ & \therefore \quad \overline{\mathrm{AB}}=-2 \hat{\mathrm{j}}+2 \hat{\mathrm{k}} \text { and } \overline{\mathrm{AC}}=-\hat{\mathrm{i}}+(x-2) \hat{\mathrm{j}}+\hat{\mathrm{k}} \\ & \therefore \quad \text { Area of } \triangle \mathrm{ABC}=\frac{1}{2}|\overline{\mathrm{AB}} \times \overline{\mathrm{AC}}|=\sqrt{6} \\ & |\overline{\mathrm{AB}} \times \overline{\mathrm{AC}}|=\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 0 & -2 & 2 \\ -1 & x-2 & 1\end{array}\right| \\ & =\hat{\mathrm{i}}[-2-2(x-2)]-\hat{\mathrm{j}}(0+2)+\hat{\mathrm{k}}(0-2) \\ & =(2-2 x) \hat{\mathrm{i}}-2 \hat{\mathrm{j}}-2 \hat{\mathrm{k}} \\ & \therefore \quad \frac{1}{2}|\overline{\mathrm{AB}} \times \overline{\mathrm{AC}}|=\sqrt{6} \\ & \Rightarrow \frac{1}{2} \sqrt{(2-2 x)^2+4+4}=\sqrt[6]{6} \\ & \Rightarrow(2-2 x)^2=16 \\ & \Rightarrow 4-8 x+4 x^2=16 \\ & \Rightarrow x^2-2 x+3=0 \\ & \Rightarrow(x-3)(x+1)=0 \\ & \Rightarrow x=3 \text { or }-1 \\ & \end{aligned}$

</details>

---

### Q22. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The mirror image of the point $(1,2,3)$ in a plane is $\left(-\frac{7}{3},-\frac{4}{3},-\frac{1}{3}\right)$. Thus, the point lies on this plane.

**Options:**

- **(A)** $(1,-1,1)$
- **(B)** $(-1,-1,1)$
- **(C)** $(1,1,1)$
- **(D)** $(-1,-1,-1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(1,-1,1)$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/-pKToT0T9Awweeo0m_0ZY0eobfwfo-joW7mOG1HyPho.original.fullsize.png">

$\mathrm{M}$ is the midpoint.
$$
\therefore \quad \mathrm{M} \equiv\left(-\frac{2}{3}, \frac{1}{3}, \frac{4}{3}\right)
$$
D.r.s of $\mathrm{AB}$ are $\frac{-10}{3}, \frac{-10}{3}, \frac{-10}{3}$ i.e., $1,1,1$

Equation of plane is
$$
\begin{aligned}
& 1\left(x+\frac{2}{3}\right)+1\left(y-\frac{1}{3}\right)+1\left(z-\frac{4}{3}\right)=0 \\
& \Rightarrow x+y+z=1
\end{aligned}
$$

Option (A) satisfies this equation of the plane.

</details>

---

### Q23. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If two vertices of a triangle are $\mathrm{A}(3,1,4)$ and $\mathrm{B}(-4,5,-3)$ and the centroid of the triangle is $\mathrm{G}(-1,2,1)$, then the third vertex $\mathrm{C}$ of the triangle is

**Options:**

- **(A)** $(2,0,2)$
- **(B)** $(-2,0,2)$
- **(C)** $(0,-2,2)$
- **(D)** $(2,-2,0)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(-2,0,2)$**

**Detailed Solution:**

Let $\overline{\mathrm{a}}, \overline{\mathrm{b}}, \overline{\mathrm{c}}$ and $\overline{\mathrm{g}}$ be the position vectors of $\mathrm{A}$, $\mathrm{B}, \mathrm{C}$ and $\mathrm{G}$ respectively.
$\begin{aligned}
& \overline{\mathrm{a}}=3 \hat{\mathrm{i}}+1 \hat{\mathrm{j}}+4 \hat{\mathrm{k}}, \\
& \overline{\mathrm{b}}=-4 \hat{\mathrm{i}}+5 \hat{\mathrm{j}}-3 \hat{\mathrm{k}}, \\
& \overline{\mathrm{g}}=-\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}},
\end{aligned}$
$\mathrm{G}$ is centroid of $\triangle \mathrm{ABC}$.
$\begin{array}{rl}
\therefore \quad \bar{g} & =\frac{\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}}{3} \\
3 \bar{g} & =\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}} \\
3 & 3(-\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}})=3 \hat{\mathrm{i}}+\hat{\mathrm{j}}+4 \hat{\mathrm{k}}-4 \hat{\mathrm{i}}+5 \hat{\mathrm{j}}-3 \hat{\mathrm{k}}+\overline{\mathrm{c}} \\
\therefore \quad \overline{\mathrm{c}} & =-3 \hat{\mathrm{i}}+6 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}-3 \hat{\mathrm{i}}-\hat{\mathrm{j}}-4 \hat{\mathrm{k}}+4 \hat{\mathrm{i}}-5 \hat{\mathrm{j}}+3 \hat{\mathrm{k}} \\
& =-2 \hat{\mathrm{i}}+0 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}
\end{array}$
$\therefore \quad$ Third vertex $\mathrm{C} \equiv(-2,0,2)$

</details>

---

### Q24. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The position vector of a point that divides the line segment joining $\mathrm{P} \equiv(1,2,-1)$ and $\mathrm{Q} \equiv(-1,1,1)$ externally in the ratio $1: 2$, is

**Options:**

- **(A)** $3 \hat{i}-3 \hat{k}$
- **(B)** $3 \hat{i}+3 \hat{j}-3 \hat{k}$
- **(C)** $-3 \hat{i}+3 \hat{k}$
- **(D)** $3 \hat{i}+\hat{j}+3 \hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3 \hat{i}+3 \hat{j}-3 \hat{k}$**

**Detailed Solution:**

Using section formula for external division
$\begin{aligned} & \left(\frac{1 \times(-1)-2 \times 1}{1-2}, \frac{1 \times 1-2 \times 2}{1-2}, \frac{1 \times 1-2 \times(-1)}{1-2}\right) \equiv(3,3,-3) \\ & \equiv 3 \hat{i}+3 \hat{j}-3 \hat{k}\end{aligned}$

</details>

---

### Q25. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The vectors $\overrightarrow{\mathrm{AB}}=3 \hat{\mathrm{i}}+4 \hat{\mathrm{k}}$ and $\overrightarrow{\mathrm{AC}}=5 \hat{\mathrm{i}}-2 \hat{\mathrm{k}}+4 \hat{\mathrm{k}}$ are the sies of a triangle $\mathrm{ABC}$. The length of the median through $\mathrm{A}$ is

**Options:**

- **(A)** $\sqrt{33}$ unit
- **(B)** $\sqrt{288}$ unit
- **(C)** $\sqrt{18}$ unit
- **(D)** $\sqrt{72}$ unit

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{33}$ unit**

**Detailed Solution:**

Let $\mathrm{A}$ be the origin.
Then $\mathrm{B}=(3,0,4)$ and $\mathrm{C}=(5,-1,4)$
Mid point of $\mathrm{BC}=\left(\frac{3+5}{2}, \frac{0-2}{2}, \frac{4+4}{2}\right)$ i.e. $(4,-1,4)$
$\therefore$ Length of medium $=\sqrt{(4)^2+(-1)^2+(4)^2}=\sqrt{33}$

</details>

---

### Q26. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The Cartesian equation of the plane $\bar{r}=(\hat{i}-\hat{j})+\lambda(\hat{i}+\hat{j}+\hat{k})+\mu(\hat{i}-2 \hat{j}+3 \hat{k})$ is

**Options:**

- **(A)** $\mathrm{x}+\mathrm{y}+\mathrm{z}=0$
- **(B)** $5 \mathrm{x}+2 \mathrm{y}+3 \mathrm{z}=0$
- **(C)** $2 x+y+z=0$
- **(D)** $5 \mathrm{x}-2 \mathrm{y}-3 \mathrm{z}-7=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5 \mathrm{x}-2 \mathrm{y}-3 \mathrm{z}-7=0$**

**Detailed Solution:**

$$
\begin{aligned}
& \overline{\mathrm{r}}=(\hat{\mathrm{i}}-\hat{\mathrm{j}})+\lambda(\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}})+\mu(\hat{\mathrm{i}}-2 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}) \\
& \overline{\mathrm{a}}=\hat{\mathrm{i}}-\hat{\mathrm{j}}, \overline{\mathrm{A}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}}, \overline{\mathrm{B}}=\hat{\mathrm{i}}-2 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}
\end{aligned}
$$
$\overline{\mathrm{n}}$ is $\perp$ er $\overline{\mathrm{A}}$ and $\overline{\mathrm{B}}$
$$
\begin{aligned}
& \therefore \overline{\mathrm{n}}=\overline{\mathrm{A}} \times \overline{\mathrm{B}}=\left|\begin{array}{ccc}
\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\
1 & 1 & 1 \\
1 & -2 & 3
\end{array}\right| \\
& =\hat{\mathrm{i}}(3+2)-\hat{\mathrm{j}}(3-1)+\hat{\mathrm{k}}(-2-1)=5 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}-3 \hat{\mathrm{k}} \\
& \overline{\mathrm{a}} \cdot \overline{\mathrm{n}}=\mathrm{d}=(\hat{\mathrm{i}}-\hat{\mathrm{j}}) \cdot(5 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}-3 \hat{\mathrm{k}})=5+2=7 \\
& \therefore \overline{\mathrm{r}} \cdot(5 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}-3 \hat{\mathrm{k}})=7 \\
& \Rightarrow \text { Cartesian equation is } 5 \mathrm{x}-2 \mathrm{y}-3 \mathrm{z}-7=0
\end{aligned}
$$

</details>

---

### Q27. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The vector equation of the lien whose Cartesian equations are $y$ $=2$ and $4 x-3 z+5=0$ is

**Options:**

- **(A)** $\overline{\mathrm{r}}=(2 \hat{\mathrm{j}}+\hat{\mathrm{k}})+\lambda(3 \hat{\mathrm{i}}-4 \hat{\mathrm{k}})$
- **(B)** $\overline{\mathrm{r}}=\left(2 \hat{\mathrm{j}}+\frac{5}{3} \hat{\mathrm{k}}\right)+\lambda(3 \hat{\mathrm{i}}+4 \hat{\mathrm{k}})$
- **(C)** $\overline{\mathrm{r}}=(2 \hat{\mathrm{j}}+\hat{\mathrm{k}})+\lambda(3 \hat{\mathrm{i}}+4 \hat{\mathrm{k}})$
- **(D)** $\overline{\mathrm{r}}=\left(2 \hat{\mathrm{j}}+\frac{5}{3} \hat{\mathrm{k}}\right)+\lambda(3 \hat{\mathrm{i}}-4 \hat{\mathrm{k}})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\overline{\mathrm{r}}=\left(2 \hat{\mathrm{j}}+\frac{5}{3} \hat{\mathrm{k}}\right)+\lambda(3 \hat{\mathrm{i}}+4 \hat{\mathrm{k}})$**

**Detailed Solution:**

We have lines $y-2=0$ and $4 x-3 z+5=0$
$$
\begin{aligned}
& \therefore 4 x=3 z-5=3\left[z-\left(\frac{5}{3}\right)\right] \\
& \therefore \frac{4 x}{12}=\frac{3\left[z-\left(\frac{5}{3}\right)\right]}{12} \Rightarrow \frac{x}{3}=\frac{z-\left(\frac{5}{3}\right)}{4}, y=2
\end{aligned}
$$
Thus line passes through the point $\left(0,2, \frac{5}{3}\right)$ i.e. a point having position vector $2 \hat{\mathrm{j}}+\frac{5}{3} \hat{\mathrm{k}}$
Also direction ratios of a line are $3,0,4$ Hence required vector equation is
$$
\overline{\mathrm{r}}=\left(2 \hat{\mathrm{j}}+\frac{5}{3} \hat{\mathrm{k}}\right)+\lambda(3 \hat{\mathrm{i}}+4 \hat{\mathrm{k}})
$$

</details>

---

### Q28. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>G</mi><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mi></mi><mo>-</mo><mn>5</mn><mo>,</mo><mi></mi><mi></mi><mi>r</mi></mrow></mfenced></math> is centroid of triangle <math><mi>A</mi><mi>B</mi><mi>C</mi></math> where, <math><mi>A</mi><mfenced separators="|"><mrow><mn>7</mn><mo>,</mo><mi></mi><mo>-</mo><mn>8</mn><mo>,</mo><mi></mi><mn>1</mn></mrow></mfenced><mo>,</mo><mi></mi><mi></mi><mi>B</mi><mfenced separators="|"><mrow><mi>p</mi><mo>,</mo><mi></mi><mi>q</mi><mo>,</mo><mi></mi><mn>5</mn></mrow></mfenced></math> and <math><mi>C</mi><mfenced separators="|"><mrow><mi>q</mi><mo>+</mo><mn>1</mn><mo>,</mo><mi></mi><mn>5</mn><mi></mi><mi>p</mi><mo>,</mo><mi></mi><mn>0</mn></mrow></mfenced></math> are vertices of a triangle then values of <math><mi>p</mi><mo>,</mo><mi></mi><mi></mi><mi>q</mi><mo>,</mo><mi></mi><mi></mi><mi>r</mi></math> are respectively ________

**Options:**

- **(A)** <math><mn>6</mn><mo>,</mo><mi></mi><mn>5</mn><mo>,</mo><mi></mi><mn>4</mn></math>
- **(B)** <math><mo>-</mo><mn>4</mn><mo>,</mo><mi></mi><mn>5</mn><mo>,</mo><mi></mi><mn>4</mn></math>
- **(C)** <math><mo>-</mo><mn>3</mn><mo>,</mo><mi></mi><mn>4</mn><mo>,</mo><mi></mi><mn>3</mn></math>
- **(D)** <math><mo>-</mo><mn>2</mn><mo>,</mo><mi></mi><mn>3</mn><mo>,</mo><mi></mi><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mo>-</mo><mn>2</mn><mo>,</mo><mi></mi><mn>3</mn><mo>,</mo><mi></mi><mn>2</mn></math>**

**Detailed Solution:**

Given <math><mi>A</mi><mfenced separators="|"><mrow><mn>7</mn><mo>,</mo><mo>-</mo><mn>8,1</mn></mrow></mfenced><mo>,</mo><mi mathvariant="normal"></mi><mi>B</mi><mfenced separators="|"><mrow><mi>p</mi><mo>,</mo><mi>q</mi><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,C</mo><mfenced separators="|"><mrow><mi>q</mi><mo>+</mo><mn>1</mn><mo>,</mo><mi mathvariant="normal"></mi><mn>5</mn><mi>p</mi><mo>,</mo><mn>0</mn></mrow></mfenced></math>  
And centroid, of <math><mo>∆</mo><mi>A</mi><mi>B</mi><mi>C</mi></math>  is  <math><mi>G</mi><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mo>-</mo><mn>5</mn><mo>,</mo><mi>r</mi></mrow></mfenced></math>  
then, <math><mo> </mo><mi>p</mi><mo>+</mo><mi>q</mi><mo>+</mo><mn>8</mn><mo>=</mo><mn>9</mn><mo> </mo><mo>&#8658;</mo><mi>p</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>1</mn></math> … (1) 
and  <math><mn>5</mn><mi>p</mi><mo>+</mo><mi>q</mi><mo>-</mo><mn>8</mn><mo>=</mo><mo>-</mo><mn>15</mn><mo> </mo><mo>&#8658;</mo><mo> </mo><mn>5</mn><mi>p</mi><mo>+</mo><mi>q</mi><mo>=</mo><mo>-</mo><mn>7</mn></math> … (2) 
and <math><mn>1</mn><mo>+</mo><mn>5</mn><mo>=</mo><mn>3</mn><mi>r</mi><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>2</mn></math>  
Solving equation (1) and (2) we get <math><mi>p</mi><mo>=</mo><mo>–</mo><mn>2</mn></math> and <math><mi>q</mi><mo>=</mo><mn>3</mn></math>

</details>

---

### Q29. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `2`

<math><mo>∆</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> has vertices at <math><mi>A</mi><mo>≡</mo><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mi> </mi><mn>3</mn><mo>,</mo><mi> </mi><mn>5</mn></mrow></mfenced><mo>,</mo><mi> </mi><mi>B</mi><mo>≡</mo><mo>(</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi> </mi><mn>3</mn><mo>,</mo><mi> </mi><mn>2</mn><mo>)</mo></math> and <math><mi>C</mi><mo>≡</mo><mfenced separators="|"><mrow><mi>λ</mi><mo>,</mo><mi> </mi><mn>5</mn><mo>,</mo><mi> </mi><mi>μ</mi></mrow></mfenced><mo>.</mo></math> If the median through <math><mi>A</mi></math> is equally inclined to the axes, then the values of <math><mi>λ</mi></math> and <math><mi>μ</mi></math> respectively are

**Options:**

- **(A)** <math > <mrow>  <mn>10</mn><mo>,</mo><mn>7</mn> </mrow></math>
- **(B)** <math > <mrow>  <mn>9</mn><mo>,</mo><mn>10</mn> </mrow></math>
- **(C)** <math > <mrow>  <mn>7</mn><mo>,</mo><mn>9</mn> </mrow></math>
- **(D)** <math > <mrow>  <mn>7</mn><mo>,</mo><mn>10</mn> </mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math > <mrow>  <mn>7</mn><mo>,</mo><mn>10</mn> </mrow></math>**

**Detailed Solution:**

<math><mi>D</mi><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>λ</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mo>+</mo><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mi>μ</mi><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
<math><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>λ</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mn>4</mn><mo>,</mo><mfrac><mrow><mi>μ</mi><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
Direction ratios of AD are (<math><mfrac><mrow><mi>λ</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mi> </mi><mn>4</mn><mo>-</mo><mn>3</mn><mo>,</mo><mfrac><mrow><mi>μ</mi><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mn>5</mn></math>)
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/dmitzybrfmtliodsuibiowqzpgkerapeaufzfvduzvrqzicory.jpeg" />
<math><mi>i</mi><mo>.</mo><mi>e</mi><mo>.(</mo><mfrac><mrow><mi>λ</mi><mo>-</mo><mn>1</mn><mo>-</mo><mn>4</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mn>1</mn><mo>,</mo><mfrac><mrow><mi>μ</mi><mo>+</mo><mn>2</mn><mo>-</mo><mn>10</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>)
<math><mi>i</mi><mo>.</mo><mi>e</mi><mo>.(</mo><mfrac><mrow><mi>λ</mi><mo>-</mo><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mn>1</mn><mo>,</mo><mfrac><mrow><mi>μ</mi><mo>+</mo><mn>8</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>)
Now if we go by options (since the line AD is equally inclined to coordinate axes, its direction ratio are in ratio (<math><mo>±</mo><mi> </mi><mn>1</mn><mi> </mi><mo>:</mo><mo>±</mo><mi> </mi><mn>1</mn><mi> </mi><mo>:</mo><mi> </mi><mo>±</mo><mi> </mi><mn>1</mn></math> )
We get that for <math> <mrow> <mi>λ</mi><mo>=</mo><mn>7</mn><mo>,</mo><mi>μ</mi><mo>=</mo><mn>10</mn></mrow> </math> direction ratios of AD are <math > <mrow>  <mtext>1,1,1</mtext><mtext>.</mtext> </mrow></math>

</details>

---

### Q30. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

If <math><msub><mrow><mi>z</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi>z</mi></mrow><mrow><mn>2</mn></mrow></msub></math> are the <math> <mrow> <mi>z</mi><mo>−</mo></mrow></math>coordinates of the points of trisection of the line segment joining the points <math> <mrow> <mi>A</mi><mrow><mo>(</mo> <mrow> <mn>2</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>4</mn> </mrow> <mo>)</mo></mrow><mo> and </mo><mi>B</mi><mrow><mo>(</mo> <mrow> <mo>−</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>6</mn> </mrow> <mo>)</mo></mrow> </mrow> </math> then <math><msub><mrow><mi>z</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>z</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo></math>

**Options:**

- **(A)** <math > <mn>1</mn></math>
- **(B)** <math > <mn>4</mn></math>
- **(C)** <math > <mn>5</mn></math>
- **(D)** <math> <mn>10</mn> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math> <mn>10</mn> </math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/317525-1.PNG" style="width: 372px; height: 77px;" />
<math> <mrow> <mtable> <mtr> <mtd> <mrow> <mtext>For              </mtext><mi> </mi><msub> <mi>z</mi> <mn>1</mn> </msub> <mi> </mi><mi> </mi><mo>→</mo><mn>1</mn><mi> </mi><mo>:</mo><mn>2</mn> </mrow> </mtd> </mtr> <mtr> <mtd> <mrow> <mtext>For</mtext><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><msub> <mi>z</mi> <mn>2</mn> </msub> <mi> </mi><mo>→</mo><mn>2</mn><mi> </mi><mo>:</mo><mn>1</mn> </mrow> </mtd> </mtr> <mtr> <mtd> <mrow> <mtable> <mtr> <mtd> <mrow> <mo stretchy="false">(</mo><mtext>Internal division formula</mtext><mo stretchy="false">)</mo> </mrow> </mtd> </mtr> <mtr> <mtd> <mi> </mi> </mtd> </mtr> <mtr> <mtd> <mrow> <mtable> <mtr> <mtd> <mi> </mi> </mtd> </mtr> <mtr> <mtd> <mi> </mi> </mtd> </mtr> </mtable> </mrow> </mtd> </mtr> </mtable> </mrow> </mtd> </mtr> </mtable><mi> </mi><mrow><mo>|</mo><mrow> <mtable> <mtr> <mtd> <mrow> <mi>z</mi><mo>=</mo><msub> <mi>z</mi> <mn>1</mn> </msub> <mo>+</mo><msub> <mi>z</mi> <mn>2</mn> </msub> </mrow> </mtd> </mtr> <mtr> <mtd> <mrow> <mo>=</mo><mfrac> <mrow> <mrow><mo>(</mo> <mn>1</mn> <mo>)</mo></mrow><mrow><mo>(</mo> <mn>6</mn> <mo>)</mo></mrow><mo>+</mo><mn>2</mn><mo stretchy="false">(</mo><mn>4</mn><mo stretchy="false">)</mo> </mrow> <mrow> <mn>1</mn><mo>+</mo><mn>2</mn> </mrow> </mfrac> <mo>+</mo><mfrac> <mrow> <mn>2</mn><mrow><mo>(</mo> <mn>6</mn> <mo>)</mo></mrow><mo>+</mo><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo><mo stretchy="false">(</mo><mn>4</mn><mo stretchy="false">)</mo> </mrow> <mrow> <mn>2</mn><mo>+</mo><mn>1</mn> </mrow> </mfrac> </mrow> </mtd> </mtr> <mtr> <mtd> <mrow> <mtable> <mtr> <mtd> <mrow> <mo>=</mo><mfrac> <mrow> <mn>6</mn><mo>+</mo><mn>8</mn> </mrow> <mn>3</mn> </mfrac> <mo>+</mo><mfrac> <mrow> <mn>12</mn><mo>+</mo><mn>4</mn> </mrow> <mn>3</mn> </mfrac> </mrow> </mtd> </mtr> <mtr> <mtd> <mrow> <mo>=</mo><mfrac> <mrow> <mn>14</mn><mo>+</mo><mn>16</mn> </mrow> <mn>3</mn> </mfrac> </mrow> </mtd> </mtr> <mtr> <mtd> <mrow> <mtable> <mtr> <mtd> <mrow> <mo>=</mo><mfrac> <mrow> <mn>30</mn> </mrow> <mn>3</mn> </mfrac> </mrow> </mtd> </mtr> <mtr> <mtd> <mrow> <mo>=</mo><mn>10</mn> </mrow> </mtd> </mtr> </mtable> </mrow> </mtd> </mtr> </mtable> </mrow> </mtd> </mtr> </mtable> </mrow></mrow> </mrow> </math>

</details>

---

### Q31. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

A point on $X O Z$ -plane divides the join of $(5,-3,-2)$ and $(1,2,-2)$ at

**Options:**

- **(A)** $\left(\frac{13}{5}, 0,-2\right)$
- **(B)** $\left(\frac{13}{5}, 0,2\right)$
- **(C)** $(5,0,2)$
- **(D)** $(5,0,-2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(\frac{13}{5}, 0,-2\right)$**

**Detailed Solution:**

Let point $P(x, y, z)$ divides the line joining the points $A$ and $B$ in the ratio $m: 1$.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/NszdUdoLovA3rQaKMVGuu1DHMqhRaHTByM1eOOH7yqM.original.fullsize.png">

Since, point $P$ is on $X O Z$ -plane $\therefore y$ coordinate $=0$ $\Rightarrow \quad \frac{2 m-3}{m+1}=0$
$\Rightarrow \quad m=\frac{3}{2}$
Now, $x=\frac{3+2 \times 5}{3+2}=\frac{13}{5}$
and $z=\frac{3 \times(-2)+2 \times(-2)}{5}=-2$
$\therefore$ Required point is $\left(\frac{13}{5}, 0,-2\right)$.

</details>

---

### Q32. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `1`

The position vector of the points $A, B, C$ are $(2 \hat{\mathbf{i}}+\hat{\mathbf{j}}-\hat{\mathbf{k}}),(3 \mathbf{i}-2 \mathbf{j}+\hat{\mathbf{k}})$ and $(\hat{\mathbf{i}}+4 \hat{\mathbf{j}}-3 \hat{\mathbf{k}})$
respectively. These points

**Options:**

- **(A)** form an isosceles triangle
- **(B)** form a right angled triangle
- **(C)** are collinear
- **(D)** form a scalene triangle

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) are collinear**

**Detailed Solution:**

$\overrightarrow{\mathbf{A B}}=(3-2) \hat{\mathbf{i}}+(-2-1) \hat{\mathbf{j}}+(1+1) \hat{\mathbf{k}}$
$\begin{aligned} &=\hat{\mathbf{i}}-3 \hat{\mathbf{j}}+2 \hat{\mathbf{k}} \\ \Rightarrow|\overrightarrow{\mathbf{A B}}| &=\sqrt{1+9+4}=\sqrt{14} \\ \overrightarrow{\mathbf{B C}} &=(1-3) \hat{\mathbf{i}}+(4+2) \hat{\mathbf{j}}+(-3-1) \hat{\mathbf{k}} \\ &=-2 \hat{\mathbf{i}}+6 \mathbf{j}-4 \hat{\mathbf{k}} \end{aligned}$
$$
\begin{aligned}
\Rightarrow \quad|\overrightarrow{\mathbf{B C}}| &=\sqrt{4+36+16} \\
&=\sqrt{56}=2 \sqrt{14} \\
\overrightarrow{\mathbf{C A}} &=(2-1) \hat{\mathbf{i}}+(1-4) \hat{\mathbf{j}}+(-1+3) \hat{\mathbf{k}} \\
&=\hat{\mathbf{i}}-3 \hat{\mathbf{j}}+2 \hat{\mathbf{k}} \\
\Rightarrow \quad|\overrightarrow{\mathbf{C A}}| &=\sqrt{1+9+4}=\sqrt{14}
\end{aligned}
$$
So, $|\overrightarrow{\mathbf{A B}}|+|\overrightarrow{\mathbf{A C}}|=|\overrightarrow{\mathbf{B C}}|$ and angle between
$A B$ and $B C$ is $180^{\circ} .$
$\therefore$ Points $A, B, C$ cannot form an isosceles triangle. Hence, $A, B, C$ are collinear.

</details>

---

