# JEE Main Mathematics - Straight Lines

## Topic 1: Coordinate System

**Total Questions:** 71

---

### Q1. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In an equilateral triangle $PQR$, let the vertex $P$ be at $(3, 5)$ and the side $QR$ be along the line $x + y = 4$. If the orthocentre of the triangle $PQR$ is $(\alpha, \beta)$, then $9(\alpha + \beta)$ is equal to:

**Options:**

- **(A)** $16$
- **(B)** $27$
- **(C)** $36$
- **(D)** $48$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $48$**

**Detailed Solution:**

In an equilateral triangle, the orthocentre coincides with the centroid.

The centroid divides the altitude from the vertex to the opposite side in the ratio $2:1$.

Let $M$ be the foot of the perpendicular from $P(3, 5)$ to the line $QR$ given by $x + y - 4 = 0$. The coordinates of $M$ can be found using the formula:

$\dfrac{x - 3}{1} = \dfrac{y - 5}{1} = -\dfrac{3 + 5 - 4}{1^2 + 1^2}$

$\dfrac{x - 3}{1} = \dfrac{y - 5}{1} = -2$

This gives $x = 1$ and $y = 3$. Thus, $M$ is $(1, 3)$.

The orthocentre $H(\alpha, \beta)$ divides the segment $PM$ internally in the ratio $2:1$. Using the section formula:

$\alpha = \dfrac{2(1) + 1(3)}{2 + 1} = \dfrac{5}{3}$

$\beta = \dfrac{2(3) + 1(5)}{2 + 1} = \dfrac{11}{3}$

Adding $\alpha$ and $\beta$:

$\alpha + \beta = \dfrac{5}{3} + \dfrac{11}{3} = \dfrac{16}{3}$

Therefore, $9(\alpha + \beta) = 9 \left( \dfrac{16}{3} \right) = 48$

Answer: $48$

</details>

---

### Q2. JEE Main 2026 (04 April Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $A,B$ be points on the two half-lines $x-\sqrt{3}|y|=\alpha$, $\alpha>0$ at a distance of $\alpha$ from their point of intersection $P$. The line segment $AB$ meets the angle bisector of the given half-lines at the point $Q$. If $PQ=\dfrac{9}{2}$ and $R$ is the radius of the circumcircle of $\triangle PAB$, then $\dfrac{\alpha^2}{R}$ is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

The given equations of the half-lines are $x - \sqrt{3}y = \alpha$ for $y \ge 0$ and $x + \sqrt{3}y = \alpha$ for $y \le 0$.

The point of intersection $P$ is obtained by setting $y = 0$, which gives $x = \alpha$. Thus, $P \equiv (\alpha, 0)$.

The angle bisector of these half-lines is the x-axis ($y = 0$).

The slope of the first half-line is $\dfrac{1}{\sqrt{3}}$, so it makes an angle of $30^\circ$ with the positive x-axis. The second half-line has a slope of $-\dfrac{1}{\sqrt{3}}$, making an angle of $-30^\circ$ with the positive x-axis.

Since $A$ and $B$ are at a distance $\alpha$ from $P$, their coordinates can be written using the parametric form of a straight line:
$A \equiv (\alpha + \alpha \cos 30^\circ, 0 + \alpha \sin 30^\circ) \equiv \left(\alpha + \dfrac{\alpha\sqrt{3}}{2}, \dfrac{\alpha}{2}\right)$
$B \equiv (\alpha + \alpha \cos(-30^\circ), 0 + \alpha \sin(-30^\circ)) \equiv \left(\alpha + \dfrac{\alpha\sqrt{3}}{2}, -\dfrac{\alpha}{2}\right)$

The line segment $AB$ is vertical and intersects the angle bisector (x-axis) at $Q$. Thus, the coordinates of $Q$ are $\left(\alpha + \dfrac{\alpha\sqrt{3}}{2}, 0\right)$.

The distance $PQ$ is the difference in their x-coordinates:
$PQ = \left(\alpha + \dfrac{\alpha\sqrt{3}}{2}\right) - \alpha = \dfrac{\alpha\sqrt{3}}{2}$

Given $PQ = \dfrac{9}{2}$, we have:
$\dfrac{\alpha\sqrt{3}}{2} = \dfrac{9}{2} \Rightarrow \alpha\sqrt{3} = 9 \Rightarrow \alpha = 3\sqrt{3}$

In $\triangle PAB$, $PA = PB = \alpha$ and $\angle APB = 30^\circ - (-30^\circ) = 60^\circ$. Therefore, $\triangle PAB$ is an equilateral triangle with side length $\alpha$.

The circumradius $R$ of an equilateral triangle of side $\alpha$ is given by $R = \dfrac{\alpha}{\sqrt{3}}$.

We need to find the value of $\dfrac{\alpha^2}{R}$:
$\dfrac{\alpha^2}{R} = \dfrac{\alpha^2}{\dfrac{\alpha}{\sqrt{3}}} = \alpha\sqrt{3}$

Since we already found $\alpha\sqrt{3} = 9$, we get:
$\dfrac{\alpha^2}{R} = 9$

Answer: $9$

</details>

---

### Q3. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $P(3\cos\alpha, 2\sin\alpha)$, $\alpha \neq 0$, be a point on the ellipse $\dfrac{x^2}{9}+\dfrac{y^2}{4}=1$, $Q$ be a point on the circle $x^2+y^2-14x-14y+82=0$ and $R$ be a point on the line $x+y=5$ such that the centroid of the triangle $PQR$ is $\left(2+\cos\alpha, 3+\dfrac{2}{3}\sin\alpha\right)$. Then the sum of the ordinates of all possible points $R$ is:

**Options:**

- **(A)** $6$
- **(B)** $2$
- **(C)** $4$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $8$**

**Detailed Solution:**

Let the coordinates of the points be $P(3\cos\alpha, 2\sin\alpha)$, $Q(x_Q, y_Q)$, and $R(x_R, y_R)$.

The centroid of $\triangle PQR$ is given by:
$\left( \dfrac{3\cos\alpha + x_Q + x_R}{3}, \dfrac{2\sin\alpha + y_Q + y_R}{3} \right)$

We are given that the centroid is $\left(2+\cos\alpha, 3+\dfrac{2}{3}\sin\alpha\right)$. Equating the coordinates, we get:
$\dfrac{3\cos\alpha + x_Q + x_R}{3} = 2 + \cos\alpha \implies x_Q + x_R = 6$
$\dfrac{2\sin\alpha + y_Q + y_R}{3} = 3 + \dfrac{2}{3}\sin\alpha \implies y_Q + y_R = 9$

Since the point $R$ lies on the line $x+y=5$, we have $x_R = 5 - y_R$.

Substituting $x_R$ into the equation for $x_Q$:
$x_Q = 6 - x_R = 6 - (5 - y_R) = y_R + 1$
And we already have $y_Q = 9 - y_R$.

The point $Q(x_Q, y_Q)$ lies on the circle $x^2+y^2-14x-14y+82=0$. Rewriting the circle's equation in standard form:
$(x-7)^2 + (y-7)^2 = 16$

Substitute $x_Q$ and $y_Q$ into the circle's equation:
$(y_R + 1 - 7)^2 + (9 - y_R - 7)^2 = 16$
$(y_R - 6)^2 + (2 - y_R)^2 = 16$

Expanding the terms:
y_R^2 - 12y_R + 36 + y_R^2 - 4y_R + 4 = 16
2y_R^2 - 16y_R + 40 = 16
2y_R^2 - 16y_R + 24 = 0
y_R^2 - 8y_R + 12 = 0

Factoring the quadratic equation:
$(y_R - 2)(y_R - 6) = 0$

Thus, the possible ordinates for point $R$ are $y_R = 2$ and $y_R = 6$.

The sum of the ordinates of all possible points $R$ is $2 + 6 = 8$.

Answer: $8$

</details>

---

### Q4. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the vertex $A$ of a triangle $ABC$ be $(1, 2)$, and the mid-point of the side $AB$ be $(5, -1)$. If the centroid of this triangle is $(3, 4)$ and its circumcenter is $(\alpha, \beta)$, then $21(\alpha + \beta)$ is equal to:

**Options:**

- **(A)** $309$
- **(B)** $403$
- **(C)** $497$
- **(D)** $524$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $497$**

**Detailed Solution:**

Let the coordinates of vertex $B$ be $(x_1, y_1)$ and vertex $C$ be $(x_2, y_2)$.

Since the mid-point of $AB$ is $(5, -1)$, we have:
$\dfrac{1 + x_1}{2} = 5 \Rightarrow x_1 = 9$
$\dfrac{2 + y_1}{2} = -1 \Rightarrow y_1 = -4$
Thus, $B \equiv (9, -4)$.

Given the centroid of $\triangle ABC$ is $(3, 4)$, we get:
$\dfrac{1 + 9 + x_2}{3} = 3 \Rightarrow x_2 = -1$
$\dfrac{2 - 4 + y_2}{3} = 4 \Rightarrow y_2 = 14$
Thus, $C \equiv (-1, 14)$.

The circumcenter $(\alpha, \beta)$ is the intersection of the perpendicular bisectors of the sides of the triangle.

For side $AB$, the mid-point is $(5, -1)$ and the slope is $\dfrac{-4 - 2}{9 - 1} = -\dfrac{3}{4}$.
The slope of its perpendicular bisector is $\dfrac{4}{3}$.
Equation of the perpendicular bisector of $AB$ is:
$y - (-1) = \dfrac{4}{3}(x - 5) \Rightarrow 4x - 3y = 23$

For side $AC$, the mid-point is $\left(\dfrac{1 - 1}{2}, \dfrac{2 + 14}{2}\right) = (0, 8)$ and the slope is $\dfrac{14 - 2}{-1 - 1} = -6$.
The slope of its perpendicular bisector is $\dfrac{1}{6}$.
Equation of the perpendicular bisector of $AC$ is:
$y - 8 = \dfrac{1}{6}(x - 0) \Rightarrow x - 6y = -48$

Solving the equations $4x - 3y = 23$ and $x - 6y = -48$:
Multiplying the first equation by $2$ gives $8x - 6y = 46$.
Subtracting the second equation from this gives:
$7x = 94 \Rightarrow x = \dfrac{94}{7}$
Substituting $x$ into the second equation:
$\dfrac{94}{7} - 6y = -48 \Rightarrow 6y = \dfrac{430}{7} \Rightarrow y = \dfrac{215}{21}$

Therefore, the circumcenter is $(\alpha, \beta) = \left(\dfrac{94}{7}, \dfrac{215}{21}\right)$.

Finally, calculating $21(\alpha + \beta)$:
$21(\alpha + \beta) = 21\left(\dfrac{94}{7} + \dfrac{215}{21}\right) = 3(94) + 215 = 282 + 215 = 497$.

Answer: $497$

</details>

---

### Q5. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the mid points of the sides of a triangle $ABC$ be $\left(\dfrac{5}{2}, 7\right)$, $\left(\dfrac{5}{2}, 3\right)$ and $(4, 5)$. If its incentre is $(h, k)$, then $3h + k$ is equal to :

**Options:**

- **(A)** $11$
- **(B)** $12$
- **(C)** $13$
- **(D)** $14$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $13$**

**Detailed Solution:**

Let the vertices of the triangle $ABC$ be $A(x_1, y_1)$, $B(x_2, y_2)$, and $C(x_3, y_3)$.

Let the given midpoints be of sides $BC$, $CA$, and $AB$ respectively:
Midpoint of $BC = \left(\dfrac{5}{2}, 7\right) \Rightarrow x_2 + x_3 = 5$ and $y_2 + y_3 = 14$
Midpoint of $CA = \left(\dfrac{5}{2}, 3\right) \Rightarrow x_3 + x_1 = 5$ and $y_3 + y_1 = 6$
Midpoint of $AB = (4, 5) \Rightarrow x_1 + x_2 = 8$ and $y_1 + y_2 = 10$

Adding the three equations for the $x$-coordinates:
$2(x_1 + x_2 + x_3) = 5 + 5 + 8 = 18$
$x_1 + x_2 + x_3 = 9$

Substituting the known sums:
$x_1 = 9 - 5 = 4$
$x_2 = 9 - 5 = 4$
$x_3 = 9 - 8 = 1$

Similarly, for $y$-coordinates:
$2(y_1 + y_2 + y_3) = 14 + 6 + 10 = 30$
$y_1 + y_2 + y_3 = 15$

$y_1 = 15 - 14 = 1$
$y_2 = 15 - 6 = 9$
$y_3 = 15 - 10 = 5$

So, the vertices are $A(4, 1)$, $B(4, 9)$, and $C(1, 5)$.

Lengths of the sides:
$a = BC = \sqrt{(4 - 1)^2 + (9 - 5)^2} = \sqrt{9 + 16} = 5$
$b = CA = \sqrt{(4 - 1)^2 + (1 - 5)^2} = \sqrt{9 + 16} = 5$
$c = AB = \sqrt{(4 - 4)^2 + (9 - 1)^2} = \sqrt{0 + 64} = 8$

Coordinates of the incentre $(h, k)$:
$I(x, y) = \left(\dfrac{ax_1 + bx_2 + cx_3}{a + b + c}, \dfrac{ay_1 + by_2 + cy_3}{a + b + c}\right)$

$h = \dfrac{5(4) + 5(4) + 8(1)}{5 + 5 + 8} = \dfrac{20 + 20 + 8}{18} = \dfrac{48}{18} = \dfrac{8}{3}$

$k = \dfrac{5(1) + 5(9) + 8(5)}{5 + 5 + 8} = \dfrac{5 + 45 + 40}{18} = \dfrac{90}{18} = 5$

So, the incentre is $(h, k) = \left(\dfrac{8}{3}, 5\right)$.

Therefore:
$3h + k = 3 \cdot \dfrac{8}{3} + 5 = 8 + 5 = 13$

Hence, the correct option is $(3)\ 13$.

</details>

---

### Q6. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let ABC be an equilateral triangle with orthocenter at the origin and the side BC on the line $x+2 \sqrt{2} y=4$. If the co-ordinates of the vertex A are $(\alpha, \beta)$, then the greatest integer less than or equal to $|\alpha+\sqrt{2} \beta|$ is

**Options:**

- **(A)** 2
- **(B)** 5
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

Let ABC be an equilateral triangle with orthocenter at the origin O(0,0) and side BC on the line $x + 2\sqrt{2}y = 4$.
Since $m_{BC} \cdot m_{AD} = -1$:
$\left(-\frac{1}{2\sqrt{2}}\right)\left(\frac{\beta}{\alpha}\right) = -1 \Rightarrow \beta = 2\sqrt{2}\alpha$ ...(1)
Distance from O to BC: $OD = \frac{|-4|}{\sqrt{1+8}} = \frac{4}{3}$
For equilateral triangle: $AO = \frac{8}{3}$, so $AD = \frac{4}{3} + \frac{8}{3} = 4$
$\frac{|\alpha + 2\sqrt{2}\beta - 4|}{3} = 4 \Rightarrow \alpha = \frac{16}{9}$ or $-\frac{8}{9}$
Since $A(\alpha, \beta)$ and $O(0,0)$ lie on the same side of BC (origin gives $0+0-4 < 0$), we need $\alpha + 2\sqrt{2}\beta - 4 < 0$.
$(\alpha, \beta) = \left(-\frac{8}{9}, -\frac{16\sqrt{2}}{9}\right)$
$\lfloor |\alpha + \sqrt{2}\beta| \rfloor = \left\lfloor \left|\frac{-8-32}{9}\right| \right\rfloor = \left\lfloor \frac{40}{9} \right\rfloor = 4$

</details>

---

### Q7. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{A}(1,2)$ and $\mathrm{C}(-3,-6)$ be two diagonally opposite vertices of a rhombus, whose sides AD and BC are parallel to the line $7 x-y=14$. If $\mathrm{B}(\alpha, \beta)$ and $\mathrm{D}(\gamma, \delta)$ are the other two vertices, then $|\alpha+\beta+\gamma+\delta|$ is equal to

**Options:**

- **(A)** 6
- **(B)** 9
- **(C)** 3
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 6**

**Detailed Solution:**

Midpoint of diagonal $AC$ is $M = (-1,-2)$. Slope of $AC = \frac{-6-2}{-3-1} = 2$.
In a rhombus, diagonals are perpendicular bisectors. So $BD$ has slope $-\frac{1}{2}$ and passes through $M$: $y + 2 = -\frac{1}{2}(x+1)$.
$AD$ has slope 7: $\frac{\delta - 2}{\gamma - 1} = 7 \Rightarrow \delta = 7\gamma - 5$.
$D$ lies on $BD$: $\delta = -\frac{\gamma}{2} - \frac{5}{2}$.
Solving: $7\gamma - 5 = -\frac{\gamma}{2} - \frac{5}{2} \Rightarrow \gamma = \frac{1}{3}$, $\delta = -\frac{8}{3}$.
$B = (2(-1)-\frac{1}{3},\, 2(-2)+\frac{8}{3}) = (-\frac{7}{3}, -\frac{4}{3})$.
$|\alpha+\beta+\gamma+\delta| = \left|-\frac{7}{3}-\frac{4}{3}+\frac{1}{3}-\frac{8}{3}\right| = |-6| = 6$.

</details>

---

### Q8. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Among the statements 
 $(S 1)$ : If $A(5,-1)$ and $B(-2,3)$ are two vertices of a triangle, whose orthocentre is $(0,0)$, then its third vertex is $(-4,-7)$ 
 and 
 (S2) : If positive numbers 2a, b, c are three consecutive terms of an A.P., then the lines $\mathrm{ax}+\mathrm{by}+\mathrm{c}=0$ are concurrent at $(2,-2)$,

**Options:**

- **(A)** both are incorrect
- **(B)** only (S2) is correct
- **(C)** only (S1) is correct
- **(D)** both are correct

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) both are correct**

**Detailed Solution:**

<b>Statement 1</b>
$m_{AO} \cdot m_{BC} = -1$
$B(-2, 3)$
$A(5, -1) \qquad C(h, k)$
<img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/22S2_s_5_1.png">
$\Rightarrow 5h - k + 13 = 0$ ....(1)
& $m_{AB} \cdot m_{OC} = -1$
$\Rightarrow 4k = 7h$ ....(2)
$\Rightarrow$ third vertex is $(-4, -7)$
$\therefore$ Statement 1 is correct.
<b>Statement 2</b>
$2a, b, c \rightarrow$ A.P.
$b = \dfrac{2a + c}{2}$
$\Rightarrow 2a - 2b + c = 0$
$\therefore$ lines $ax + by + c = 0$ are concurrent then
$\dfrac{x}{2} = \dfrac{y}{-2} = \dfrac{1}{1}$
$x = 2$ and $y = -2$
$\therefore$ Point of concurrency is $(2, -2)$
$\therefore$ Statement 2 is correct.

</details>

---

### Q9. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let a point $A$ lie between the parallel lines $L_{1}$ and $L_{2}$ such that its distances from $L_{1}$ and $L_{2}$ are 6 and 3 units, respectively. Then the area (in sq. units) of the equilateral triangle $A B C$, where the points $B$ and C lie on the lines $\mathrm{L}_{1}$ and $\mathrm{L}_{2}$, respectively, is :

**Options:**

- **(A)** $15 \sqrt{6}$
- **(B)** $21 \sqrt{3}$
- **(C)** $12 \sqrt{2}$
- **(D)** 27

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $21 \sqrt{3}$**

**Detailed Solution:**

Let $L_2: y = 0$, $L_1: y = 9$.
Point A at $(0, 3)$, B at $(x_B, 9)$, C at $(x_C, 0)$.
$AB^2 = x_B^2 + 36$, $AC^2 = x_C^2 + 9$, $BC^2 = (x_B - x_C)^2 + 81$.
From $AB = AC$: $x_B^2 - x_C^2 = -27$.
From $AB = BC$: $2x_Bx_C = x_C^2 + 45$.
Solving: $3x_C^4 - 198x_C^2 - 2025 = 0$.
Let $u = x_C^2$: $u^2 - 66u - 675 = 0 \Rightarrow u = 75$.
$a^2 = x_C^2 + 9 = 84$.
Area $= \frac{\sqrt{3}}{4} \times 84 = 21\sqrt{3}$.

</details>

---

### Q10. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A line passing through the point $\mathrm{P}(\mathrm{a}, \theta)$ makes an acute angle $\alpha$ with the positive x -axis. Let this line be rotated about the point $P$ through an angle $\frac{\alpha}{2}$ in the clock-wise direction. If in the new position, the slope of the line is $2-\sqrt{3}$ and its distance from the origin is $\frac{1}{\sqrt{2}}$, then the value of $3 a^2 \tan ^2 \alpha-2 \sqrt{3}$ is

**Options:**

- **(A)** 4
- **(B)** 6
- **(C)** 5
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 4**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/BmOPGL4iKo1GOYACHNwnlEt5GvQ906CIx1mqypQG-FY.original.fullsize.png"/>
$\begin{aligned}
& \mathrm{m}_{\mathrm{PR}}=2-\sqrt{3}=\tan 15^{\circ} \\
& \therefore \frac{\alpha}{2}=15^{\circ} \quad \Rightarrow \alpha=30^{\circ}
\end{aligned}$
equation of PR :
$\begin{aligned}
& y=\tan 15^{\circ}(x-a) \\
& y=(2-\sqrt{3})(x-a)
\end{aligned}$
$\perp$ distance from origin $=\frac{1}{\sqrt{2}}$
$\begin{aligned} & \left|\frac{\sqrt{3} a-2 a}{\sqrt{4+3-4 \sqrt{3}+1}}\right|=\frac{1}{\sqrt{2}} \\ & \frac{|a|(2-\sqrt{3})}{2 \sqrt{(2-\sqrt{3})}}=\frac{1}{\sqrt{2}} \\ & |a|=\frac{\sqrt{2}}{\sqrt{2-\sqrt{3}}}=\sqrt{2}(\sqrt{2+\sqrt{3}}) \\ & a^2=2(2+\sqrt{3}) \\ & 3 a^2 \tan ^2 \alpha-2 \sqrt{3} \\ & 3 \times(4+2 \sqrt{3}) \cdot \frac{1}{3}-2 \sqrt{3}=4\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the orthocentre of the triangle formed by the lines $y=x+1, y=4 x-8$ and $y=m x+c$ is at $(3,-1)$, then $\mathrm{m}-\mathrm{c}$ is :

**Options:**

- **(A)** 0
- **(B)** -2
- **(C)** 4
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dMXKVEEkjw-zP2jKrqurNtiiqoQpUhHRgF3AZxImDZM.original.fullsize.png"/>
Solve line PQ \& QR Point $\mathrm{Q}\left(\frac{1-\mathrm{c}}{\mathrm{m}-1}, \frac{1-\mathrm{c}}{\mathrm{m}-1}+1\right)$
$m_{2 H}=\frac{\frac{1-c}{m-1}+2}{\frac{1-c}{m-1}-3}=\frac{1-c+2 m-2}{1-c-3 m+3}=-\frac{1}{4}$
$\mathrm{m}_{2 \mathrm{H}}=\frac{\frac{1-\mathrm{c}}{\mathrm{m}-1}+2}{\frac{1-\mathrm{c}}{\mathrm{m}-1}-3}=\frac{1-\mathrm{c}+2 \mathrm{~m}-2}{1-\mathrm{c}-3 \mathrm{~m}+3}=-\frac{1}{4}$...(1)
$\because \mathrm{m}_{\mathrm{PH}}=\frac{5}{0} \rightarrow \infty$
$\Rightarrow$ Slope of line QR (m) $=0$
Put value of $m$ in equation (1)
$\frac{1-c-2}{1-c+3}=-\frac{1}{4} \Rightarrow c=0$
so $\mathrm{m}-\mathrm{c}=0$ Ans.

</details>

---

### Q12. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let ABC be the triangle such that the equations of lines $A B$ and $A C$ be $3 y-x=2$ and $x+y=2$, respectively, and the points B and C lie on x -axis. If $P$ is the orthocentre of the triangle $A B C$, then the area of the triangle PBC is equal to

**Options:**

- **(A)** 4
- **(B)** 10
- **(C)** 8
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 6**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/idKeWgctGCJ4g8n1rdR_vDPlTMkfs3FARsVhcO4AAx8.original.fullsize.png"/>
$\begin{aligned} & \text { Equation of Altitude } \mathrm{AP}: \mathrm{x}=1 \\ & \text { Equation of Altitude } \mathrm{BP}: \mathrm{y}-0=1(\mathrm{x}+2) \\ & \Rightarrow \mathrm{x}=1 \& \\ & \mathrm{x}-\mathrm{y}+2=0 \\ & \mathrm{P}(1,3) \\ & \text { Area of } \triangle \mathrm{PBC}=\frac{1}{2} \times 4 \times 3=6\end{aligned}$

</details>

---

### Q13. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the three sides of a triangle are on the lines $4 x-7 y+10=0, x+y=5$ and $7 x+4 y=15$. Then the distance of its orthocentre from the orthocentre of the triangle formed by the lines $x=0, y=0$ and $x+y=1$ is

**Options:**

- **(A)** 5
- **(B)** $\sqrt{5}$
- **(C)** $\sqrt{20}$
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{5}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/FV-OWocee6uX-rDVOCAbcDS2VEhtkddEQ4RIqHIWFXY.original.fullsize.png"/>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/SEvH3aB_eA67ptzAjXIItpDEdqp70Pm-UxgycjMe2OQ.original.fullsize.png"/>
$\begin{gathered}
7 x+4 y=15 \\
7 x+7 y+10=0
\end{gathered}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a6oimRIfuQ4RSFmGHTm7_J_DaR1RIwPNqbviZpGD1tw.original.fullsize.png"/>
distance between P and $\mathrm{B}=\sqrt{5}$

</details>

---

### Q14. JEE Main 2025 (2 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

Let $\mathrm{A}(4,-2), \mathrm{B}(1,1)$ and $\mathrm{C}(9,-3)$ be the vertices of a triangle $A B C$. Then the maximum area of the parallelogram AFDE , formed with vertices $\mathrm{D}, \mathrm{E}$ and F on the sides $\mathrm{BC}, \mathrm{CA}$ and AB of the triangle ABC respectively, is ______ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

Area of $\triangle \mathrm{ABC}=\frac{1}{2}\left|\begin{array}{ccc}4 & -2 & 1 \\ 1 & 1 & 1 \\ 9 & -3 & 1\end{array}\right|$
$=6$ square units
Maximum area of $\operatorname{AFDE}=\frac{1}{2} \times 6=3$ sq. units

</details>

---

### Q15. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let the line $x+y=1$ meet the axes of $x$ and $y$ at A and B, respectively. A right angled triangle AMN is inscribed in the triangle OAB , where O is the origin and the points M and N lie on the lines $O B$ and $A B$, respectively. If the area of the triangle $A M N$ is $\frac{4}{9}$ of the area of the triangle $O A B$ and AN : NB $=\lambda: 1$, then the sum of all possible value(s) of is $\lambda$ :

**Options:**

- **(A)** 2
- **(B)** $\frac{5}{2}$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{13}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/k_I9E0Z5C84f48H4jKmebCb08jty1flBuvAuCi_k9Dk.original.fullsize.png">



$\begin{aligned}
& \text { Area of } \triangle \mathrm{AOB}=\frac{1}{2} \\
& \text { Area of } \triangle \mathrm{AMN}=\frac{4}{9} \times \frac{1}{2}=\frac{2}{9}
\end{aligned}$

Equation of AB is $\mathrm{x}+\mathrm{y}=1$
$\begin{aligned}
& \mathrm{OA}=1, \mathrm{AM}=\sec \left(45^{\circ}-\theta\right) \\
& \mathrm{AN}=\sec \left(45^{\circ}-\theta\right) \cos \theta \\
& \mathrm{MN}=\sec \left(45^{\circ}-\theta\right) \sin \theta
\end{aligned}$

$\begin{aligned} & \operatorname{Ar}(\triangle \mathrm{AMN})=\frac{1}{2} \times \sec ^2\left(45^{\circ}-\theta\right) \sin \theta \cdot \cos \theta=\frac{2}{9} \\ & \Rightarrow \tan \theta=2, \frac{1}{2} \\ & \tan \theta=2 \text { is rejected } \\ & \frac{\mathrm{AN}}{\mathrm{NB}}=\frac{\lambda}{1}=\cot \theta=2\end{aligned}$

</details>

---

### Q16. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let \(A B C\) be a triangle formed by the lines \(7 x-6 y+3=0, x+2 y-31=0\) and \(9 x-2 y-19=0\). Let the point \((h, k)\) be the image of the centroid of \(\Delta A B C\) in the line \(3 x+6 y-53=0\). Then \(h^2+k^2+h k\) is equal to:

**Options:**

- **(A)** 47
- **(B)** 37
- **(C)** 36
- **(D)** 40

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 37**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/-VAWBsCQ4bb2XgbDr3QOpC1K5Mdf8WnEcSVh9yHtQmE.original.fullsize.png">




$\begin{aligned} \therefore \text { centroid of } \triangle \mathrm{ABC} & =\left(\frac{9+3+5}{3}, \frac{11+4+13}{3}\right) \\ & =\left(\frac{17}{3}, \frac{28}{3}\right)\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3teajokCGEEt-A28idHnOOsaGb7ugxK6BdaAoImb0jM.original.fullsize.png">




Let image of centroid with respect to line mirror is
$\begin{aligned}
& (\mathrm{h}, \mathrm{k}) \\
& \therefore\left(\frac{\mathrm{k}-\frac{28}{3}}{\mathrm{~h}-\frac{17}{3}}\right)\left(-\frac{1}{2}\right)=-1 \\
& \& 3\left(\frac{\mathrm{~h}+\frac{17}{3}}{2}\right)+6 \cdot\left(\frac{\frac{\mathrm{k}+28}{3}}{2}\right)=53
\end{aligned}$

Solving (1) \& (2) we get $\mathrm{h}=3, \mathrm{k}=4$
$\therefore \mathrm{h}^2+\mathrm{k}^2+\mathrm{hk}=37$

</details>

---

### Q17. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let ${ }^{\mathrm{n}} \mathrm{C}_{\mathrm{r}-1}=28,{ }^{\mathrm{n}} \mathrm{C}_{\mathrm{r}}=56$ and ${ }^{\mathrm{n}} \mathrm{C}_{\mathrm{r}+1}=70$. Let $\mathrm{A}(4 \cos t, 4 \sin t), \mathrm{B}(2 \sin t,-2 \cos \mathrm{t})$ and $C\left(3 r-n, r^2-n-1\right)$ be the vertices of a triangle $A B C$, where $t$ is a parameter. If $(3 x-1)^2+(3 y)^2$ $=\alpha$, is the locus of the centroid of triangle ABC , then $\alpha$ equals

**Options:**

- **(A)** 6
- **(B)** 18
- **(C)** 8
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 20**

**Detailed Solution:**

$\left.\begin{array}{l}{ }^n C_{r-1}=28 \\ { }^n C_r=56 \\ { }^n C_{r+1}=70 \\ \begin{array}{l}{ }^n C_{r-1} \\ { }^n C_r\end{array}=\frac{28}{56} \Rightarrow \frac{r}{n-r+1}=\frac{1}{2} \\ \frac{{ }^n C_r}{{ }^n C_{r+1}}=\frac{56}{70} \Rightarrow \frac{r+1}{n-r}=\frac{70}{56}\end{array}\right\} n=8=3$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/wlvrugjPd3gfU8jAtY3cTMXE3PtrJViJejcfORnLiSs.original.fullsize.png">

$h=\frac{4 \cos t+2 \sin t+1}{3} \quad k=\frac{4 \sin t-2 \cos t}{3}$
$3 h-1=4 \cos t+2 \sin t$
$3 k-1=4 \sin t-2 \cos t$
$\begin{aligned}
& (1)^2+(2)^2 \\
& (3 h-1)^2+(3 k)^2=20
\end{aligned}$
Locus of centroid: $(3 x-1)^2+(3 y)^2=20$
$\Rightarrow \alpha=20$

</details>

---

### Q18. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let the area of a $\triangle P Q R$ with vertices $P(5,4), Q(-2,4)$ and $R(a, b)$ be 35 square units. If its orthocenter and centroid are $O\left(2, \frac{14}{5}\right)$ and $C(c, d)$ respectively, then $c+2 d$ is equal to

**Options:**

- **(A)** $\frac{8}{3}$
- **(B)** $\frac{7}{3}$
- **(C)** $2$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ox-km7OXlUKG8nkZgw7XyMpW-I4vw1dss6RbIm_XN18.original.fullsize.png">




$\begin{aligned} & \text { Equation of lines } Q R=5 x+2 y+2=0 \\ & \text { Equation of lines } P R=10 x-3 y-38=0 \\ & \therefore \text { Point } R(2,-6) \\ & \text { Centroid }=\left(\frac{5-2+2}{3}, \frac{4+4-6}{3}\right) \\ & =\left(\frac{5}{3}, \frac{2}{3}\right) \\ & c+2 d=\frac{5}{3}+\frac{4}{3}=3\end{aligned}$

</details>

---

### Q19. JEE Main 2025 (22 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $A(6,8), B(10 \cos \alpha,-10 \sin \alpha)$ and $C(-10 \sin \alpha, 10 \cos \alpha)$, be the vertices of a triangle. If $L(a, 9)$ and $G(h, k)$ be its orthocenter and centroid respectively, then $(5 a-3 h+6 k+100 \sin 2 \alpha)$ is equal to ______ -.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **145**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/SvVZf6RQRzEw-LfDl2kMFhyXFMWrQPQYnkW26P3i2WY.original.fullsize.png">

$\begin{aligned}
& \frac{a+0}{3}=h \Rightarrow a=3 h \\
& \frac{9+0}{3}=k \Rightarrow k=3 \\
& \because(h, k)=\left(\frac{6+10 \cos \alpha-10 \sin \alpha}{3}, \frac{8-10 \sin \alpha-10 \cos \alpha}{3}\right) \\
& 6+10 \cos \alpha-10 \sin \alpha=3 h \\
& 10 \cos \alpha-10 \sin \alpha=3 h-6 \\
& 10(\cos \alpha-\sin \alpha)=1 \\
& \frac{8-10 \sin \alpha+10 \cos \alpha}{3}=k \\
& \Rightarrow 100 \sin 2 \alpha=99 \\
& h=\frac{7}{3} \\
& \Rightarrow a=7
\end{aligned}$
$\text { Now, } 5 a-3 h+6 k+100 \sin 2 \alpha=35-7+18+99$
$=145$

</details>

---

### Q20. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let the triangle PQR be the image of the triangle with vertices $(1,3),(3,1)$ and $(2,4)$ in the line $x+2 y=2$. If the centroid of $\triangle \mathrm{PQR}$ is the point $(\alpha, \beta)$, then $15(\alpha-\beta)$ is equal to :

**Options:**

- **(A)** $19$
- **(B)** $24$
- **(C)** $21$
- **(D)** $22$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $22$**

**Detailed Solution:**

The centroid $G^{\prime \prime}(\alpha, \beta)$ of $\triangle P Q R$ be image of centroid of given triangle $P^{\prime} Q^{\prime} R^{\prime}$.
<img src="https://cdn.quizrr.in/question-assets/jee_main_pyq/Ix1KwZ1fxaGIUaCTa0cDJwt1h7yNqCeyB5EwaVGuD08.original.fullsize_2.png">
Centroid of $\Delta P^{\prime} Q^{\prime} R^{\prime}=\left(\frac{1+3+2}{3}, \frac{3+1+4}{3}\right)=$ $G^{\prime}\left(2, \frac{8}{3}\right)$.
Image of $G\left(2, \frac{8}{3}\right)$, w.r.t. line $x+2 y=2$ is $(\alpha, \beta)$
Then $\frac{\alpha-2}{1}=\frac{\beta-\frac{8}{3}}{2}=\frac{-2\left(2+\frac{16}{3}-2\right)}{1+4}$
$\therefore \quad \frac{\alpha-2}{1}=\frac{\beta-\frac{8}{3}}{2}=-\frac{32}{15}$
$\therefore \quad \alpha=-\frac{2}{15}$ and $\beta=-\frac{8}{5}$
Then $15(\alpha-\beta)=15\left(-\frac{2}{15}+\frac{24}{15}\right)=22$

</details>

---

### Q21. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Two vertices of a triangle $\mathrm{ABC}$ are $\mathrm{A}(3,-1)$ and $\mathrm{B}(-2,3)$, and its orthocentre is $\mathrm{P}(1,1)$. If the coordinates of the point $\mathrm{C}$ are $(\alpha, \beta)$ and the centre of the of the circle circumscribing the triangle $\mathrm{PAB}$ is $(\mathrm{h}, \mathrm{k})$, then the value of $(\alpha+\beta)+2(\mathrm{~h}+\mathrm{k})$ equals

**Options:**

- **(A)** 5
- **(B)** 81
- **(C)** 15
- **(D)** 51

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 5**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/WdGDxszYLPSCIuGJItXE6pewl7cspKWisJhXbroDOyA.original.fullsize.png">
$\mathrm{M}_{\mathrm{AB}}=\frac{4}{-5} \Rightarrow \mathrm{M}_{\mathrm{DP}}=\frac{5}{4}$
Equation of $\mathrm{PC}$ is $\mathrm{y}-1=\frac{5}{4}(\mathrm{x}-1) \ldots(1)$
$\mathrm{M}_{\mathrm{AP}}=\frac{2}{-2}=-1 \Rightarrow \mathrm{M}_{\mathrm{BC}}=+1$
Equation of $\mathrm{BC}$ is $\mathrm{y}-3=(\mathrm{x}+2)\ldots(2)$
On solving (1) and (2)
$\begin{aligned}
& x+4=\frac{5}{4}(x-1) \Rightarrow 4 x+16=5 x-5 \Rightarrow \alpha=21 \\
& \Rightarrow \beta=y=x+5=26 \\
& \alpha+\beta=47
\end{aligned}$
Equation of $\perp$ bisector of AP
$y-0=(x-2)\ldots(3)$
Equation of $\perp$ bisector of $\mathrm{AB}$
$y-1=\frac{5}{4}\left(x-\frac{1}{2}\right)\ldots(4)$
$\begin{aligned} & \text { On solving (3) \& (4) } \\ & (\mathrm{x}-3) 4=5 \mathrm{x}-\frac{5}{2} \\ & \mathrm{x}=\frac{-19}{2}=\mathrm{h} \\ & \mathrm{y}=\frac{-23}{2}=\mathrm{k} \\ & \Rightarrow 2(\mathrm{~h}+\mathrm{k})=-42\end{aligned}$

</details>

---

### Q22. JEE Main 2024 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

If the orthocentre of the triangle formed by the lines $2 x+3 y-1=0, x+2 y-1=0$ and $a x+b y-1=0$, is the centroid of another triangle, whose circumcentre and orthocentre respectively are $(3,4)$ and $(-6,-8)$, then the value of $|a-b|$ is_______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

$\begin{aligned} & 2 x+3 y-1=0 \\ & x+2 y-1=0 \\ & a x+b y-1=0\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/qrHQmAQJ4qPI8jFtM27Ml6GfRFjri8NANa56UH5EoFw.original.fullsize.png">
$\begin{aligned} & \left(\frac{6-6}{3}, \frac{8-8}{3}\right) \\ & =(0,0)\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/pLVFOKpcUwYjajWRS1TIKPu0bWWWsHyjDDwPw0UYx1k.original.fullsize.png">
$\begin{aligned} & a x+b y-1=0 \\ & \left(\frac{1-0}{-1-0}\right)\left(\frac{-a}{b}\right)=-1 \\ & \Rightarrow-\mathrm{a}=\mathrm{b} \\ & \Rightarrow \quad \mathrm{ax}-\mathrm{ay}-1=0 \\ & a x-a\left(1-\frac{2 x}{3}\right)-1 \\ & x\left(a+\frac{2 a}{3}\right)=\frac{a}{3} \\ & \mathrm{x}=\frac{\mathrm{a}+3}{5 \mathrm{a}} \\ & 2\left(\frac{a+3}{5 a}\right)+3 y-1=0 \\ & y=\frac{1-\frac{2 a+6}{5 a}}{3}=\frac{3 a-6}{3 \times 5 a} \\ & y=\frac{a-2}{5 a} \\ & \frac{\left(\frac{a-2}{5 a}\right)}{\left(\frac{a+3}{5 a}\right)}=2 \Rightarrow a-2=2 a+6 \\ & a=-8 \\ & \mathrm{~b}=8 \\ & -8 \mathrm{x}+8 \mathrm{y}-1=0 \\ & |a-b|=16 \\ & \end{aligned}$

</details>

---

### Q23. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The equations of two sides $\mathrm{AB}$ and $\mathrm{AC}$ of a triangle $\mathrm{ABC}$ are $4 x+y=14$ and $3 x-2 y=5$, respectively. The point $\left(2,-\frac{4}{3}\right)$ divides the third side $\mathrm{BC}$ internally in the ratio $2: 1$. the equation of the side $\mathrm{BC}$ is

**Options:**

- **(A)** $x+3 y+2=0$
- **(B)** $x-6 y-10=0$
- **(C)** $x-3 y-6=0$
- **(D)** $x+6 y+6=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x+3 y+2=0$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/MJ9PFLTTXdRKX3Yil-jeBYpJMmhoqpZ_7Taduf42e_w.original.fullsize.png">
$\begin{aligned}
& \frac{2 \mathrm{x}_2+\mathrm{x}_1}{3}=2, \frac{2\left(\frac{3 \mathrm{x}_2-5}{2}\right)+\left(14-4 \mathrm{x}_1\right)}{3}=\frac{-4}{3} \\
& 2 \mathrm{x}_2+\mathrm{x}_1=6,3 \mathrm{x}_2-4 \mathrm{x}_1=-13 \\
& \mathrm{x}_2=1, \mathrm{x}_1=4
\end{aligned}$
So, $\mathrm{C}(1,-1), \mathrm{B}(4,-2)$
$\mathrm{m}=\frac{-1}{3}$
Equation of $\mathrm{BC}: \mathrm{y}+1=\frac{-1}{3}(\mathrm{x}-1)$
$\begin{aligned} & 3 y+3=-x+1 \\ & x+3 y+2=0\end{aligned}$

</details>

---

### Q24. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{P}(6,1)$ be the orthocentre of the triangle whose vertices are $\mathrm{A}(5,-2), \mathrm{B}(8,3)$ and $\mathrm{C}(\mathrm{h}, \mathrm{k})$, then the point $C$ lies on the circle:

**Options:**

- **(A)** $x^2+y^2-61=0$
- **(B)** $x^2+y^2-52=0$
- **(C)** $x^2+y^2-65=0$
- **(D)** $x^2+y^2-74=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x^2+y^2-65=0$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2uBkY6hGScQvj5xH0ps05Ye6HG6d7xXAWJx1bmtx3oc.original.fullsize.png">
Slope of $A D=3$
Slope of $\mathrm{BC}=-\frac{1}{3}$
equation of $\mathrm{BC}=3 \mathrm{y}+\mathrm{x}-17=0$
slope of $\mathrm{BE}=1$
Slope of $\mathrm{AC}=-1$
equation of $\mathrm{AC}$ is $\mathrm{x}+\mathrm{y}-3=0$
point $C$ is $(-4,7)$

</details>

---

### Q25. JEE Main 2024 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mo>−</mo><mn>2</mn><mo>,</mo><mo>−</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo> </mo><mi>B</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo> </mo><mi>C</mi><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mfenced><mrow><mi>γ</mi><mo>,</mo><mi>δ</mi></mrow></mfenced></math> be the vertices of a parallelogram <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi></math>. If the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>−</mo><mi>y</mi><mo>=</mo><mn>5</mn></math> and the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>−</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>6</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi><mo>+</mo><mi>δ</mi></mrow></mfenced></math> is equal to ______.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **32**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mo>−</mo><mn>2</mn><mo>,</mo><mo>−</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo> </mo><mi>B</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo> </mo><mi>C</mi><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mfenced><mrow><mi>γ</mi><mo>,</mo><mi>δ</mi></mrow></mfenced></math> be the vertices of a parallelogram <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi></math></p><p>And the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>−</mo><mi>y</mi><mo>=</mo><mn>5</mn></math> and the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>−</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>6</mn></math>,</p><p>Now, plotting the diagram we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e02fb1ae-397d-4a05-86bf-e81c7447ae83.png" style="width: 500px; height: 257px;"/></p><p>Now, using the midpoint formula we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>≡</mo><mfenced><mrow><mfrac><mrow><mi>α</mi><mo>−</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mi>β</mi><mo>−</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>≡</mo><mfenced><mrow><mfrac><mrow><mi>γ</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mi>δ</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Now, on comparing we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>α</mi><mo>−</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>γ</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>β</mi><mo>−</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>δ</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>−</mo><mi>γ</mi><mo>=</mo><mn>3</mn><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo> </mo><mo>(</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo> </mo><mi>β</mi><mo>−</mo><mi>δ</mi><mo>=</mo><mn>1</mn><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo> </mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p>Also, given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>γ</mi><mo>,</mo><mi>δ</mi></mrow></mfenced></math> lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>−</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><mi>γ</mi><mo>−</mo><mn>2</mn><mi>δ</mi><mo>=</mo><mn>6</mn><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi></mrow></mfenced></math> lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>−</mo><mi>y</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>α</mi><mo>−</mo><mi>β</mi><mo>=</mo><mn>5</mn><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>4</mn><mo>)</mo></math></p><p>On solving equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo> </mo><mo>(</mo><mn>2</mn><mo>)</mo><mo>,</mo><mo> </mo><mo>(</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo> </mo><mo>(</mo><mn>4</mn><mo>)</mo></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mo>−</mo><mn>3</mn><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mo>−</mo><mn>11</mn><mo>,</mo><mo> </mo><mi>γ</mi><mo>=</mo><mo>−</mo><mn>6</mn><mo>,</mo><mo> </mo><mi>δ</mi><mo>=</mo><mo>−</mo><mn>12</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi><mo>+</mo><mi>δ</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mo>-</mo><mn>3</mn><mo>-</mo><mn>11</mn><mo>-</mo><mn>6</mn><mo>-</mo><mn>12</mn></mrow></mfenced><mo>=</mo><mn>32</mn></math></p>

</details>

---

### Q26. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mo> </mo><mi>b</mi></mrow></mfenced><mo>,</mo><mo> </mo><mi>B</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mo> </mo><mn>4</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>−</mo><mn>6</mn><mo>,</mo><mo> </mo><mo>−</mo><mn>8</mn></mrow></mfenced></math> respectively denote the centroid, circumcentre and orthocentre of a triangle. Then, the distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mo>,</mo><mn>7</mn><mi>b</mi><mo>+</mo><mn>5</mn></mrow></mfenced></math> from the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>−</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> measured parallel to the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>−</mo><mn>2</mn><mi>y</mi><mo>−</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>15</mn><msqrt><mn>5</mn></msqrt></mrow><mn>7</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>17</mn><msqrt><mn>5</mn></msqrt></mrow><mn>6</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>17</mn><msqrt><mn>5</mn></msqrt></mrow><mn>7</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>5</mn></msqrt><mn>17</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>17</mn><msqrt><mn>5</mn></msqrt></mrow><mn>7</mn></mfrac></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mo> </mo><mi>B</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo> </mo><mi>C</mi><mfenced><mrow><mo>−</mo><mn>6</mn><mo>,</mo><mo>−</mo><mn>8</mn></mrow></mfenced></math> denotes centroid, circumcentre and orthocentre respectively.</p><p>We know that, the line joining orthocentre and circumcentre is divided by centroid in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>1</mn></math>, where distance from orthocentre being the larger part.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/926113ca-80c9-4c7d-80cb-322f7405bfac.png" style="width: 250px; height: 97px;"/></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mo>×</mo><mn>3</mn><mo>+</mo><mn>1</mn><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced></mrow><mrow><mn>2</mn><mo>+</mo><mn>1</mn></mrow></mfrac><mo>,</mo><mo> </mo><mi>b</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mo>×</mo><mn>4</mn><mo>+</mo><mn>1</mn><mfenced><mrow><mo>-</mo><mn>8</mn></mrow></mfenced></mrow><mrow><mn>2</mn><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><mi>b</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mo>≡</mo><mfenced><mrow><mn>2</mn><mo>×</mo><mn>0</mn><mo>+</mo><mn>3</mn><mo>,</mo><mo> </mo><mn>7</mn><mo>×</mo><mn>0</mn><mo>+</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mo>≡</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo> </mo><mn>5</mn></mrow></mfenced></math></p><p>Distance from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> measured along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>−</mo><mn>2</mn><mi>y</mi><mo>−</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>3</mn><mo>+</mo><mi>r</mi><mi>cos</mi><mi>θ</mi><mo>,</mo><mo> </mo><mi>y</mi><mo>=</mo><mn>5</mn><mo>+</mo><mi>r</mi><mi>sin</mi><mi>θ</mi></math></p><p>Where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>θ</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>So, the distance of point from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>−</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mn>3</mn><mo>+</mo><mi>r</mi><mi>cos</mi><mi>θ</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mrow><mn>5</mn><mo>+</mo><mi>r</mi><mi>sin</mi><mi>θ</mi></mrow></mfenced><mo>−</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mfenced><mrow><mn>2</mn><mi>cos</mi><mi>θ</mi><mo>+</mo><mn>3</mn><mi>sin</mi><mi>θ</mi></mrow></mfenced><mo>=</mo><mo>−</mo><mn>17</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mo>−</mo><mfrac><mn>17</mn><mfenced><mrow><mn>2</mn><mo>·</mo><mfrac><mn>2</mn><msqrt><mn>5</mn></msqrt></mfrac><mo>+</mo><mn>3</mn><mo>·</mo><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac></mrow></mfenced></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mo>−</mo><mn>17</mn><msqrt><mn>5</mn></msqrt></mrow><mn>7</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>=</mo><mfrac><mrow><mn>17</mn><msqrt><mn>5</mn></msqrt></mrow><mn>7</mn></mfrac></math></p>

</details>

---

### Q27. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>,</mo><mo> </mo><mi>β</mi><mo>,</mo><mo> </mo><mi>γ</mi><mo>,</mo><mo> </mo><mi>δ</mi><mo>∈</mo><mi>Z</mi></math> and let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mi>α</mi><mo>,</mo><mo> </mo><mi>β</mi></mrow></mfenced><mo>,</mo><mo> </mo><mi>B</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mo> </mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo> </mo><mi>C</mi><mfenced><mrow><mi>γ</mi><mo>,</mo><mo> </mo><mi>δ</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mo> </mo><mn>2</mn></mrow></mfenced></math> be the vertices of a parallelogram <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><msqrt><mn>10</mn></msqrt></math> and the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> lie on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi><mo>+</mo><mi>δ</mi></mrow></mfenced></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<p>Plotting the diagram of the given data we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e00ce334-c408-40ac-81bc-c59d73a43ac0.png" style="width: 250px; height: 163px;"/></p><p>We know that diagonals of a parallelogram bisect each other.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mtext>Mid-point of</mtext><mo> </mo><mi>A</mi><mi>C</mi><mo>=</mo><mtext>Mid-point of</mtext><mo> </mo><mi>B</mi><mi>D</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mfrac><mrow><mi>α</mi><mo>+</mo><mi>γ</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mi>β</mi><mo>+</mo><mi>δ</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mfenced><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>0</mn><mo>+</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mfrac><mrow><mi>α</mi><mo>+</mo><mi>γ</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mi>β</mi><mo>+</mo><mi>δ</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>+</mo><mi>γ</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo> </mo><mi>β</mi><mo>+</mo><mi>δ</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mfenced><mrow><mi>α</mi><mo>+</mo><mi>γ</mi><mo>+</mo><mo> </mo><mi>β</mi><mo>+</mo><mi>δ</mi></mrow></mfenced><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q28. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mfrac><mi>a</mi><mn>4</mn></mfrac></mrow></mfenced></math>, be the circumcenter of a triangle with vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mi>a</mi><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>,</mo><mo> </mo><mi>B</mi><mo>(</mo><mi>a</mi><mo>,</mo><mo> </mo><mn>6</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mfrac><mi>a</mi><mn>4</mn></mfrac><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math> denote the circumradius, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi></math> denote the area and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>γ</mi></math> denote the perimeter of the triangle. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>53</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>62</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>53</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo> </mo><mi>B</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mn>6</mn></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mi>C</mi><mfenced><mrow><mfrac><mi>a</mi><mn>4</mn></mfrac><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><msup><mi>B</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>6</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><msup><mi>B</mi><mn>2</mn></msup><mo>=</mo><mn>64</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>B</mi><msup><mi>C</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mfrac><mi>a</mi><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>6</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>B</mi><msup><mi>C</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>9</mn><msup><mi>a</mi><mn>2</mn></msup></mrow><mn>16</mn></mfrac><mo>+</mo><mn>64</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><msup><mi>C</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mfrac><mi>a</mi><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>2</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><msup><mi>C</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>9</mn><msup><mi>a</mi><mn>2</mn></msup></mrow><mn>16</mn></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><msup><mi>C</mi><mn>2</mn></msup><mo>+</mo><mi>A</mi><msup><mi>B</mi><mn>2</mn></msup><mo>=</mo><mi>B</mi><msup><mi>C</mi><mn>2</mn></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>△</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> is right angled at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>.</p><p>So, circumcentre will be mid-point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>S</mi><mo>≡</mo><mfenced><mrow><mfrac><mrow><mi>a</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mi>a</mi><mn>4</mn></mfrac></mstyle></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>6</mn><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>S</mi><mo>≡</mo><mfenced><mrow><mfrac><mrow><mn>5</mn><mi>a</mi></mrow><mn>8</mn></mfrac><mo>,</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mfrac><mi>a</mi><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>B</mi><mi>C</mi><mo>=</mo><msqrt><mfrac><mrow><mn>9</mn><mo>×</mo><mn>64</mn></mrow><mn>16</mn></mfrac><mo>+</mo><mn>64</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>B</mi><mi>C</mi><mo>=</mo><msqrt><mn>100</mn></msqrt><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mi>B</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mi>C</mi><mo>=</mo><msqrt><mfrac><mrow><mn>9</mn><mo>×</mo><mn>64</mn></mrow><mn>16</mn></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mi>C</mi><mo>=</mo><mn>6</mn></math></p><p>Now, circumradius is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mrow><mi>B</mi><mi>C</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mn>5</mn><mo>⇒</mo><mi>α</mi><mo>=</mo><mn>5</mn></math></p><p>Now, area of triangle will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>×</mo><mn>6</mn><mo>×</mo><mn>8</mn><mo>=</mo><mn>24</mn></math> and perimeter will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>γ</mi><mo>=</mo><mn>6</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>10</mn><mo>=</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mn>24</mn><mo>,</mo><mo> </mo><mi>γ</mi><mo>=</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi><mo>=</mo><mn>53</mn></math></p>

</details>

---

### Q29. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></mrow></mfenced></math> is the orthocenter of the triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> with vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mo>&#8211;</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>B</mi><mfenced><mrow><mo>&#8211;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>&#945;</mi><mo>-</mo><mn>6</mn><mi>&#946;</mi><mo>+</mo><mn>60</mn></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>**

**Detailed Solution:**

<blockquote><p>The required diagram will be: </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e16a2feb-e799-47e2-9c30-70e4c61fd3e9.png" style="width: 350px; height: 295px;" /></p><p>Equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>D</mi><mo>:</mo><mi>y</mi><mo>+</mo><mn>7</mn><mo>=</mo><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mn>3</mn></mfrac><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>21</mn><mo>=</mo><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>E</mi><mo>:</mo><mi>y</mi><mo>-</mo><mn>2</mn><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>12</mn></mfrac><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>12</mn><mi>y</mi><mo>-</mo><mn>24</mn><mo>=</mo><mo>&#8211;</mo><mi>x</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>23</mn><mo>-</mo><mn>12</mn><mi>y</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>)</mo></math></p><p>by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>115</mn><mo>-</mo><mn>60</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>57</mn><mi>y</mi><mo>=</mo><mn>121</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>121</mn><mn>57</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>23</mn><mo>-</mo><mn>12</mn><mo>&#215;</mo><mfrac><mn>121</mn><mn>57</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mn>9</mn><mi>&#945;</mi><mo>-</mo><mn>6</mn><mi>&#946;</mi><mo>+</mo><mn>60</mn><mo>=</mo><mn>9</mn><mo>&#215;</mo><mn>23</mn><mo>-</mo><mn>108</mn><mo>&#215;</mo><mfrac><mn>121</mn><mn>57</mn></mfrac><mo>-</mo><mn>6</mn><mo>&#215;</mo><mfrac><mn>121</mn><mn>57</mn></mfrac><mo>+</mo><mn>60</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>207</mn><mo>-</mo><mn>242</mn><mo>+</mo><mn>60</mn><mo>=</mo><mn>25</mn></math></p><p>Hence this is the required option.</p></blockquote>

</details>

---

### Q30. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>)</mo></math> be the centroid of the triangle formed by the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>82</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>5</mn><mi>y</mi><mo>=</mo><mo>-</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>=</mo><mn>17</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mn>2</mn><mi>&#946;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></math> are the roots of the equation

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>12</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>14</mn><mi>x</mi><mo>+</mo><mn>48</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>13</mn><mi>x</mi><mo>+</mo><mn>42</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>25</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>13</mn><mi>x</mi><mo>+</mo><mn>42</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>The given set of equations are:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>82</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>x</mi><mo>-</mo><mn>5</mn><mi>y</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>=</mo><mn>17</mn></math></p><p>Now on solving the above equation by taking two at a time and plotting the diagram we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2d107299-afa0-490e-9fc5-33b1cd1b9f61.png" style="width: 300px; height: 171px;" /></p><p> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>)</mo><mo>&#8801;</mo><mfenced><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>6</mn></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mo>-</mo><mn>7</mn><mo>+</mo><mn>8</mn></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>&#8801;</mo><mo>(</mo><mn>4</mn><mo>,</mo><mn>1</mn><mo>)</mo></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mn>2</mn><mi>&#946;</mi><mo>=</mo><mn>6</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>=</mo><mn>7</mn></math></p><p>The required equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>13</mn><mi>x</mi><mo>+</mo><mn>42</mn><mo>=</mo><mn>0</mn></math></p><p>Hence this is the required option.</p></blockquote>

</details>

---

### Q31. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>(</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>(</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo></math> be the mid-points of the sides of a triangle with incentre at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math>. If the focus of the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>a</mi><mi>x</mi></math> passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><msqrt><mn>2</mn></msqrt><mo>,</mo><mn>0</mn><mo>)</mo></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are rational numbers, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>(</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>(</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo></math> be the mid-points of the sides of a triangle with incentre at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math>,</p><p>Now finding the vertices of the triangle by using midpoint formula and plotting the diagram we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8d08a83a-9154-4eb9-9317-7d740b93312b.png" style="width: 306px; height: 197px;" /></p><p>Now finding the incentre of the above triangle using the formula,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>&#8801;</mo><mfenced><mrow><mfrac><mrow><mi>a</mi><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><mi>b</mi><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mi>c</mi><msub><mi>x</mi><mn>3</mn></msub></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfrac><mo>,</mo><mfrac><mrow><mi>a</mi><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><mi>b</mi><msub><mi>y</mi><mn>2</mn></msub><mo>+</mo><mi>c</mi><msub><mi>y</mi><mn>3</mn></msub></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfrac></mrow></mfenced></math></p><p>We get, Incentre <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced><mrow><mfrac><mn>4</mn><mrow><mn>4</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>,</mo><mfrac><mn>4</mn><mrow><mn>4</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced></math></p><p>Now given parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>a</mi><mi>x</mi></math> passes through the incentre <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mn>4</mn><mrow><mn>4</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>a</mi><mfenced><mfrac><mn>4</mn><mrow><mn>4</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math></p><p>Now we know that focus of parabola is given by, focus <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>)</mo></math></p><p>Hence, focus will be,<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>1</mn><mrow><mn>4</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mfenced><mrow><mfrac><mrow><mn>4</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow><mn>8</mn></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>
Now comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><msqrt><mn>2</mn></msqrt><mo>,</mo><mn>0</mn><mo>)</mo></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mn>4</mn><mn>8</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>16</mn><mn>2</mn></mfrac><mo>=</mo><mn>8</mn></math></p></blockquote>

</details>

---

### Q32. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>(</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>)</mo></math> be the circumcentre of the triangle formed by the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>69</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>y</mi><mo>-</mo><mn>3</mn><mi>x</mi><mo>=</mo><mn>17</mn></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>7</mn><mi>y</mi><mo>=</mo><mn>61</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>(</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>)</mo></math> be the circumcentre of the triangle formed by the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>69</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>y</mi><mo>-</mo><mn>3</mn><mi>x</mi><mo>=</mo><mn>17</mn></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>7</mn><mi>y</mi><mo>=</mo><mn>61</mn></math>,</p><p>Now plotting the diagram of the above equations and finding the intersection point we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cba25b99-b4ba-4bbd-b387-c472417d4013.png" style="width: 300px; height: 220px;" /></p><p>Now from diagram we can see that it is a right-angled triangle, so the circumcentre is given by midpoint of the hypotenuse,</p><p>Hence, circumcentre will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mfrac><mrow><mn>12</mn><mo>+</mo><mn>5</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mo>+</mo><mn>8</mn></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mfenced><mrow><mfrac><mn>17</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>15</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mo>(</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>)</mo></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mfrac><mn>17</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>15</mn><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mfrac><mn>17</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>15</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mn>16</mn><mo>=</mo><mn>17</mn></math></p></blockquote>

</details>

---

### Q33. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the orthocentre of the triangle, whose vertices are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced></math>, then the quadratic equation whose roots are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mn>4</mn><mi>&#946;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>19</mn><mi>x</mi><mo>+</mo><mn>90</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>18</mn><mi>x</mi><mo>+</mo><mn>80</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>22</mn><mi>x</mi><mo>+</mo><mn>120</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>20</mn><mi>x</mi><mo>+</mo><mn>99</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>20</mn><mi>x</mi><mo>+</mo><mn>99</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>We have,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/05c0ab3f-4404-41fd-82ae-7e4d30530417-9896566.png" style="width: 400px; height: 230px;" /></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mrow><mi>B</mi><mi>H</mi></mrow></msub><mo>&#215;</mo><msub><mi>m</mi><mrow><mi>A</mi><mi>C</mi></mrow></msub><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mfrac><mrow><mi>&#946;</mi><mo>-</mo><mn>3</mn></mrow><mrow><mi>&#945;</mi><mo>-</mo><mn>2</mn></mrow></mfrac></mfenced><mfenced><mfrac><mn>1</mn><mrow><mo>-</mo><mn>2</mn></mrow></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>1</mn></math>        ....(1)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mrow><mi>A</mi><mi>H</mi></mrow></msub><mo>&#215;</mo><msub><mi>m</mi><mrow><mi>B</mi><mi>C</mi></mrow></msub><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mfrac><mrow><mi>&#946;</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#946;</mi><mo>-</mo><mn>4</mn><mo>=</mo><mi>&#945;</mi><mo>-</mo><mn>1</mn></math></p><p>Using (1), we can write:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>(</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>-</mo><mn>4</mn><mo>=</mo><mi>&#945;</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>&#945;</mi><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>&#945;</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>7</mn><mn>3</mn></mfrac><mo>&#8658;</mo><mi mathvariant="normal">H</mi><mfenced><mrow><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>,</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mn>4</mn><mi>&#946;</mi><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>28</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>33</mn><mn>3</mn></mfrac><mo>=</mo><mn>11</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>+</mo><mn>4</mn><mi>&#945;</mi><mo>=</mo><mfrac><mn>7</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>20</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>27</mn><mn>3</mn></mfrac><mo>=</mo><mn>9</mn></math></p><p>Required equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>20</mn><mi>x</mi><mo>+</mo><mn>99</mn><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q34. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> be the two points on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>+</mo><mi>x</mi><mo>=0</mo></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> are symmetric with respect to the origin. Suppose <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is a point on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo>=</mo><mn>2</mn></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> is an equilateral triangle. Then, the area of the <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><msqrt><mn>3</mn></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><msqrt><mn>3</mn></msqrt></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><msqrt><mn>3</mn></msqrt></mfrac></math>**

**Detailed Solution:**

<p>On plotting the diagram of the given data we get,</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0f2d1c1d-0502-42f4-834e-2c3f92859310-9894745_re.PNG" style="width: 249px; height: 210px;" /></p><p>Now given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mi mathvariant="normal">y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>2</mn><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p>On solving we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo></math></p><p>Now height <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> Distance of point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> to origin,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><msqrt><msup><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>(</mo><mo>-</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>h</mi><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> is an equilateral triangle,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mfrac><mi>h</mi><mrow><mi>A</mi><mi>B</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mfenced><msup><mn>60</mn><mo>&#176;</mo></msup></mfenced><mo>=</mo><mfrac><mi>h</mi><mrow><mi>A</mi><mi>B</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>(</mo><mo>&#8757;</mo><mo>&#8736;</mo><mi>A</mi><mo>=</mo><mo>&#8736;</mo><mi>B</mi><mo>=</mo><mo>&#8736;</mo><mi>C</mi><mo>=</mo><msup><mn>60</mn><mrow><mo>&#176;</mo><mo>)</mo></mrow></msup></math></p><p>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac><msup><mfenced><mrow><mi>A</mi><mi>B</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac><mfrac><msup><mi>h</mi><mn>2</mn></msup><mrow><msup><mi>sin</mi><mn>2</mn></msup><msup><mn>60</mn><mo>&#8728;</mo></msup></mrow></mfrac><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac><mo>&#215;</mo><mfrac><mn>32</mn><mn>3</mn></mfrac></math></p><p>So, Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi><mo>=</mo><mfrac><mn>8</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p>

</details>

---

### Q35. JEE Main 2023 (24 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

The equations of the sides <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mi>C</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>C</mi><mi>A</mi></math> of a triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>p</mi><mi>y</mi><mo>=</mo><mn>21</mn><mi>a</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>&#8800;</mo><mn>0</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>3</mn></math> respectively. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mi>a</mi></mrow></mfenced></math> be the centroid of the triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>B</mi><mi>C</mi></mrow></mfenced><mn>2</mn></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **122**

**Detailed Solution:**

<p>We have,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/637eb460-6c28-4715-b89a-a9c8a8c91b3b-9894400.png" style="width: 400px; height: 292px;" /></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mi>a</mi></mrow></mfenced></math>, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mn>3</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>3</mn><mi>a</mi><mo>+</mo><mn>2</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>2</mn><mo>+</mo><mi>a</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8801;</mo><mfenced><mrow><mo>-</mo><mi>a</mi><mo>,</mo><mn>2</mn><mi>a</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>C</mi><mo>&#8801;</mo><mfenced><mrow><mn>5</mn><mo>+</mo><mi>a</mi><mo>,</mo><mn>2</mn><mo>+</mo><mi>a</mi></mrow></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> lies on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>p</mi><mi>y</mi><mo>=</mo><mn>21</mn><mi>a</mi></math>, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>a</mi><mo>+</mo><mn>2</mn><mi>p</mi><mi>a</mi><mo>=</mo><mn>21</mn><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mo>=</mo><mn>11</mn></math></p><p>Also,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>+</mo><mi>a</mi><mo>+</mo><mn>11</mn><mfenced><mrow><mn>2</mn><mo>+</mo><mi>a</mi></mrow></mfenced><mo>=</mo><mn>21</mn><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>27</mn><mo>=</mo><mn>9</mn><mi>a</mi><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>3</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8801;</mo><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>C</mi><mo>&#8801;</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><msup><mi>C</mi><mn>2</mn></msup><mo>=</mo><mn>121</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>122</mn></math></p>

</details>

---

### Q36. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mi>B</mi><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mn>6</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mfrac><mi>&#945;</mi><mn>4</mn></mfrac><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math> be vertices of a <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mfrac><mi>&#945;</mi><mn>4</mn></mfrac></mrow></mfenced></math> is the circumcentre of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math>, then which of the following is NOT correct about <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math>

**Options:**

- **(A)** ares is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(B)** perimeter is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(C)** circumradius is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** inradius is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) perimeter is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mi mathvariant="normal">&#945;</mi><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>B</mi><mfenced><mrow><mi mathvariant="normal">&#945;</mi><mo>,</mo><mn>6</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>C</mi><mfenced><mrow><mfrac><mi>&#945;</mi><mn>4</mn></mfrac><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p>Now slope of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi><mo>=</mo><mn>0</mn></math> and slope of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mfrac><mn>8</mn><mn>0</mn></mfrac><mo>&#8594;</mo><mo>&#8734;</mo></math></p><p>Now we can see <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math>.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> is right angled at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>.</p><p>So, Circumcentre <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math>mid point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mo>=</mo><mfenced><mrow><mfrac><mrow><mn>5</mn><mi>&#945;</mi></mrow><mn>8</mn></mfrac><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>Now given circumcentre <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8801;</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mfrac><mi>&#945;</mi><mn>4</mn></mfrac></mrow></mfenced></math></p><p>So on comparing we get,<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mi>&#945;</mi></mrow><mn>8</mn></mfrac><mo>=</mo><mn>5</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfrac><mi>&#945;</mi><mn>4</mn></mfrac><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>8</mn></math></p><p>Now plotting the diagram and finding the sides with distance formula we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/00bde0b4-e7a7-40dc-b841-eef8cd7cf1bd-image.png" style="width: 294px; height: 180px;" /></p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mn>6</mn></mfenced><mfenced><mn>8</mn></mfenced><mo>=</mo><mn>24</mn></math></p><p>Perimeter <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>24</mn></math></p><p>Circumradius <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>10</mn><mn>2</mn></mfrac><mo>=</mo><mn>5</mn></math></p><p>Inradius <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#916;</mi><mi>s</mi></mfrac><mo>=</mo><mfrac><mn>24</mn><mn>12</mn></mfrac><mo>=</mo><mn>2</mn></math></p></blockquote>

</details>

---

### Q37. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the circumcentre of a triangle with vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mi>B</mi><mfenced><mrow><mi>b</mi><mo>,</mo><mn>5</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mi>a</mi><mi>b</mi><mo>&#62;</mo><mn>0</mn></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>. If the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>P</mi></math> intersects the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math> at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><msub><mi>k</mi><mn>1</mn></msub><mo>,</mo><msub><mi>k</mi><mn>2</mn></msub></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>k</mi><mn>1</mn></msub><mo>+</mo><msub><mi>k</mi><mn>2</mn></msub></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>7</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>7</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>7</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>On plotting the graph we get,</p><p> </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6565c938-f3ca-4994-a1bc-937119eb4bf3-image.png" style="width: 344px; height: 280px;" /></p><p>Now by diagram <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mrow><mi>A</mi><mi>C</mi></mrow></msub><mo>&#10230;</mo><mo>&#8734;</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mrow><mi>P</mi><mi>D</mi></mrow></msub><mo>=</mo><mn>0</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>D</mi></math> is perpendicular bisector, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mfenced><mrow><mfrac><mrow><mi>a</mi><mo>+</mo><mi>a</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mi>b</mi><mo>+</mo><mn>3</mn></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8801;</mo><mi>D</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mfrac><mrow><mi>b</mi><mo>+</mo><mn>3</mn></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Now since <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mrow><mi>P</mi><mi>D</mi></mrow></msub><mo>=</mo><mn>0</mn></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>b</mi><mo>+</mo><mn>3</mn></mrow><mn>2</mn></mfrac><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>+</mo><mn>3</mn><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Now similarly finding the coordinates of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mfenced><mrow><mfrac><mrow><mi>b</mi><mo>+</mo><mi>a</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mo>+</mo><mi>b</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mfenced><mrow><mfrac><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo>&#160;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Now we know that product of perpendicular slopes is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mrow><mi>C</mi><mi>B</mi></mrow></msub><mo>&#183;</mo><msub><mi>m</mi><mrow><mi>E</mi><mi>P</mi></mrow></msub><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mfrac><mrow><mn>5</mn><mo>-</mo><mi>b</mi></mrow><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mfrac></mfenced><mo>=</mo><mfenced><mfrac><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow><mrow><mfrac><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mfrac><mn>6</mn><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfrac></mfenced><mo>=</mo><mfenced><mfrac><mn>2</mn><mrow><mi>a</mi><mo>-</mo><mn>3</mn></mrow></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>12</mn><mo>=</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>12</mn><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>a</mi><mo>+</mo><mi>a</mi><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>a</mi><mo>-</mo><mn>15</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>5</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>Now given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mo>&#62;</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>&#60;</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><mn>3</mn></math> </p><p>Now equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>P</mi></math> by two point form will be,  {where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>P</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>}</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mfenced><mfrac><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>2</mn><mo>=</mo><mi>x</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>3</mn></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math> {where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>} will be, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>y</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mfrac><mn>6</mn><mn>2</mn></mfrac><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>-</mo><mn>5</mn><mo>=</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>8</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mfenced><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>8</mn></mrow></mfenced><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>16</mn><mo>=</mo><mn>3</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><mi>x</mi><mo>=</mo><mo>-</mo><mn>13</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>13</mn><mn>7</mn></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>3</mn><mfenced><mrow><mo>-</mo><mfrac><mn>13</mn><mn>7</mn></mfrac></mrow></mfenced><mo>+</mo><mn>8</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>39</mn><mo>+</mo><mn>56</mn></mrow><mn>7</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>17</mn><mn>7</mn></mfrac></math></p><p>So the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>k</mi><mn>1</mn></msub><mo>,</mo><msub><mi>k</mi><mn>2</mn></msub></mrow></mfenced></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>13</mn><mo>+</mo><mn>17</mn></mrow><mn>7</mn></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>7</mn></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>where</mtext><mo>&#160;</mo><msub><mi>k</mi><mn>1</mn></msub><mo>&#160;</mo><mtext>is</mtext><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>k</mi><mn>2</mn></msub><mo>&#160;</mo><mtext>is&#160;</mtext><mi>y</mi></mrow></mfenced></math></p></blockquote>

</details>

---

### Q38. JEE Main 2022 (28 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi></mrow></mfenced></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> is an equilateral triangle with vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mi>sin</mi><mi>t</mi><mo>,</mo><mo>-</mo><mi>cos</mi><mi>t</mi></mrow></mfenced><mo>,</mo><mi>B</mi><mfenced><mrow><mi>cos</mi><mi>t</mi><mo>,</mo><mi>sin</mi><mi>t</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math> such that its orthocentre lies on a circle with centre <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>77</mn><mn>9</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>80</mn><mn>9</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<blockquote><p>We know that for an equilateral triangle the orthocentre and centroid coincide.</p><p>Here, centroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>h</mi><mo>,</mo><mi>k</mi></mrow></mfenced><mo>&#8801;</mo><mfenced><mrow><mfrac><mrow><mi>cos</mi><mi>t</mi><mo>+</mo><mi>sin</mi><mi>t</mi><mo>+</mo><mi>a</mi></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mi>sin</mi><mi>t</mi><mo>-</mo><mi>cos</mi><mi>t</mi><mo>+</mo><mi>b</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>h</mi><mo>-</mo><mi>a</mi><mo>=</mo><mi>cos</mi><mi>t</mi><mo>+</mo><mi>sin</mi><mi>t</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>k</mi><mo>-</mo><mi>b</mi><mo>=</mo><mi>sin</mi><mi>t</mi><mo>-</mo><mi>cos</mi><mi>t</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Eliminating <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> from above two equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mi>ii</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>h</mi><mo>-</mo><mfrac><mi>a</mi><mn>3</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>k</mi><mo>-</mo><mfrac><mi>b</mi><mn>3</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>2</mn><mn>9</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>h</mi><mo>,</mo><mi>k</mi></mrow></mfenced></math> lies on the circle whose centre is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mi>a</mi><mn>3</mn></mfrac><mo>,</mo><mfrac><mi>b</mi><mn>3</mn></mfrac></mrow></mfenced></math>, now comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math> we get,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>1</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn></math></p></blockquote>

</details>

---

### Q39. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The equations of the sides <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>,</mo><mi>B</mi><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mi>A</mi></math> of a triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mi>p</mi><mi>y</mi><mo>=</mo><mn>39</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>3</mn></math> respectively and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> is its circumcentre. Then which of the following is NOT true

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>A</mi><mi>C</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>9</mn><mi>p</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>A</mi><mi>C</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>p</mi><mn>2</mn></msup><mo>=</mo><mn>136</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn><mo>&#60;</mo></math>area <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></mrow></mfenced><mo>&#60;</mo><mn>36</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn><mo>&#60;</mo></math> area <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></mrow></mfenced><mo>&#60;</mo><mn>38</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn><mo>&#60;</mo></math> area <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></mrow></mfenced><mo>&#60;</mo><mn>38</mn></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9922ef16-dc6a-414f-aaf1-0076d54f7530-image.png" style="width: 276px; height: 250px;" />Intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>3</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p>Perpendicular bisector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>3</mn><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>&#8658;</mo><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p>Take image of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> along the perpendicular bisector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math>, we get </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mfenced><mn>9</mn></mfenced></mrow><mn>5</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>18</mn><mn>5</mn></mfrac></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>13</mn><mn>5</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mfrac><mn>26</mn><mn>5</mn></mfrac></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced><mrow><mo>-</mo><mfrac><mn>13</mn><mn>5</mn></mfrac><mo>,</mo><mfrac><mn>26</mn><mn>5</mn></mfrac></mrow></mfenced></math></p><p>This point lies on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>p</mi><mi>y</mi><mo>=</mo><mn>39</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>13</mn><mn>5</mn></mfrac><mo>+</mo><mi>p</mi><mfenced><mfrac><mn>26</mn><mn>5</mn></mfrac></mfenced><mo>=</mo><mn>39</mn><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>p</mi><mo>=</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mo>=</mo><mn>8</mn></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>8</mn><mi>y</mi><mo>=</mo><mn>39</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>3</mn></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mn>7</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>A</mi><mi>C</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>72</mn><mo>=</mo><mn>9</mn><mi>p</mi></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msup><mi>C</mi><mn>2</mn></msup><mo>+</mo><msup><mi>p</mi><mn>2</mn></msup><mo>=</mo><mn>72</mn><mo>+</mo><mn>64</mn><mo>=</mo><mn>136</mn></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>A</mi><mi>B</mi><mi>C</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>7</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mfrac><mrow><mo>-</mo><mn>13</mn></mrow><mn>5</mn></mfrac></mtd><mtd><mfrac><mn>26</mn><mn>5</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>18</mn><mo>+</mo><mn>18</mn><mo>&#215;</mo><mfrac><mn>13</mn><mn>5</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mfenced open="[" close="]"><mfrac><mn>18</mn><mn>5</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>162</mn><mn>5</mn></mfrac><mo>=</mo><mn>32</mn><mo>.</mo><mn>4</mn><mo>&#8713;</mo><mfenced><mrow><mn>34</mn><mo>,</mo><mn>38</mn></mrow></mfenced></math></p></blockquote>

</details>

---

### Q40. JEE Main 2022 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>B</mi><mfenced><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mi>C</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>5</mn></mrow></mfenced></math> be vertices of a triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mo>,</mo><mo>&#160;</mo><mi>P</mi></math> be a point on side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mn>2</mn></msub></math> be the areas of triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>P</mi><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math>.</p><p>Respectively.</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mn>1</mn></msub><mo>:</mo><msub><mi>&#916;</mi><mn>2</mn></msub><mo>=</mo><mn>4</mn><mo>:</mo><mn>7</mn></math>, then the area enclosed by the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>P</mi><mo>,</mo><mi>A</mi><mi>C</mi></math> and the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Plotting the given value in diagram we have,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/29623864-de49-4db6-bc14-f129e9b85b54-8830dd11-ba7d-4220-8ea4-4d75674dfba9-714a691b-6f46-4053-ba21-a1b8f2e77ead-image.png" style="width: 383px; height: 338px;" /></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced></math> be a point on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math>, so area formed by <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#9651;</mo><mi>A</mi><mi>B</mi><mi>P</mi></math> will be,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><mi>x</mi></mtd><mtd><mi>y</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>7</mn></mrow></mfenced></math></p><p>And area of triangle formed by <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#9651;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfrac><mn>36</mn><mn>2</mn></mfrac></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>&#916;</mi><mn>1</mn></msub><msub><mi>&#916;</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>7</mn></mfrac><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>7</mn></mrow><mn>36</mn></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>14</mn><mi>x</mi><mo>+</mo><mn>35</mn><mi>y</mi><mo>=</mo><mo>-</mo><mn>95</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math> by two point form will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>13</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Solving equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> we get,</p><p>Point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>20</mn></mrow><mn>7</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>11</mn></mrow><mn>7</mn></mfrac></mrow></mfenced></math></p><p>Now equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>P</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>11</mn><mn>7</mn></mfrac></mstyle></mrow><mrow><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>20</mn><mn>7</mn></mfrac></mstyle></mrow></mfrac><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn><mi>x</mi><mo>=</mo><mn>1</mn></math>,</p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>intercept will be point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced></math> and similarly from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>So Area of triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>Q</mi><mi>R</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>1</mn><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p></blockquote>

</details>

---

### Q41. JEE Main 2022 (26 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

The equations of the sides <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>,</mo><mi>B</mi><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mi>A</mi></math> of a triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>+</mo><mi>p</mi><mi>y</mi><mo>=</mo><mn>15</mn><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>3</mn></math> respectively. If its orthocentre is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mi>a</mi></mrow></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#60;</mo><mi>a</mi><mo>&#60;</mo><mn>2</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<blockquote><p>Given the equations of the sides <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>,</mo><mi>B</mi><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mi>A</mi></math> of a triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>+</mo><mi>p</mi><mi>y</mi><mo>=</mo><mn>15</mn><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>3</mn></math> respectively.</p><p>Now on solving equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>+</mo><mi>p</mi><mi>y</mi><mo>=</mo><mn>15</mn><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>3</mn></math> we get coordinates of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mi>B</mi><mfenced><mrow><mfrac><mrow><mn>15</mn><mi>a</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>p</mi></mrow></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>30</mn><mi>a</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>p</mi></mrow></mfrac></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mfenced><mrow><mfrac><mrow><mn>18</mn><mi>p</mi><mo>-</mo><mn>30</mn></mrow><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>15</mn><mi>p</mi><mo>-</mo><mn>33</mn></mrow><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9ff66caf-4a3f-4400-a2d4-4a57766b9bdc-image.png" style="width: 380px; height: 230px;" /></p><p>And let orthocentre be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mi>a</mi></mrow></mfenced></math></p><p>Slope of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>H</mi><mo>=</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac></math></p><p>Sloe of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mi>p</mi></mfrac></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>H</mi><mo>&#8869;</mo><mi>B</mi><mi>C</mi></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mi>a</mi><mo>+</mo><mn>2</mn></math></p><p>Now coordinate of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mfenced><mrow><mfrac><mrow><mn>18</mn><mi>p</mi><mo>-</mo><mn>30</mn></mrow><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>15</mn><mi>p</mi><mo>-</mo><mn>33</mn></mrow><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></math></p><p>So, slope of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfrac><mrow><mn>15</mn><mi>p</mi><mo>-</mo><mn>33</mn></mrow><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mi>a</mi></mrow><mrow><mfrac><mrow><mn>18</mn><mi>p</mi><mo>-</mo><mn>30</mn></mrow><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>15</mn><mi>p</mi><mo>-</mo><mn>33</mn><mo>-</mo><mfenced><mrow><mi>p</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>18</mn><mi>p</mi><mo>-</mo><mn>30</mn><mo>-</mo><mn>2</mn><mi>p</mi><mo>-</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>16</mn><mi>p</mi><mo>-</mo><msup><mi>p</mi><mn>2</mn></msup><mo>-</mo><mn>31</mn></mrow><mrow><mn>16</mn><mi>p</mi><mo>-</mo><mn>32</mn></mrow></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi><mi>C</mi><mo>&#8869;</mo><mi>A</mi><mi>B</mi></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>slope&#160;of</mtext><mo>&#160;</mo><mi>H</mi><mi>C</mi><mo>&#215;</mo><mo>&#160;</mo><mtext>slope&#160;of&#160;</mtext><mi>A</mi><mi>B</mi><mtext>=-1</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>16</mn><mi>p</mi><mo>-</mo><msup><mi>p</mi><mn>2</mn></msup><mo>-</mo><mn>31</mn></mrow><mrow><mn>16</mn><mi>p</mi><mo>-</mo><mn>32</mn></mrow></mfrac><mo>&#215;</mo><mo>-</mo><mn>2</mn><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>p</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>p</mi><mo>+</mo><mn>15</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi>or</mi><mo>&#160;</mo><mn>5</mn></math></p><p>But if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>5</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn></math> not acceptable as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mi>a</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>p</mi><mo>=</mo><mn>3</mn></math></p></blockquote>

</details>

---

### Q42. JEE Main 2022 (29 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The distance of the origin from the centroid of the triangle whose two sides have the equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> and whose orthocenter is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>7</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></mrow></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>&#8801;</mo><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi><mo>&#8801;</mo><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p>Now, altitude from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> which is perpendicular to line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> and which passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>7</mn><mn>3</mn></mfrac><mo>,</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></mrow></mfenced></math> is  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>H</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>0</mn></math>,</p><p>Now intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>H</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>A</mi><mi>B</mi></math> will give point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math></p><p>Similarly, altitude from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mi>H</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>C</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math></p><p>Centroid of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#9651;</mo><mi>A</mi><mi>B</mi><mi>C</mi><mo>=</mo><mi>E</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>O</mi><mi>E</mi><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p><p>where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> is origin.</p>

</details>

---

### Q43. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let a triangle be bounded by the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>=</mo><mn>10</mn></math>; <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>12</mn></math> and the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub></math>, which passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>, intersect <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>. If the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> divides the line-segment <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math>, internally in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>3</mn></math>, then the area of the triangle is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>110</mn><mn>13</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>132</mn><mn>13</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>142</mn><mn>13</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>151</mn><mn>13</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>132</mn><mn>13</mn></mfrac></math>**

**Detailed Solution:**

<p>Given, point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>12</mn></math></p><p>Take <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mtext>so</mtext><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>4</mn><mo>+</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#945;</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mn>4</mn><mo>+</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#945;</mi></mrow></mfenced></math></p><p>Points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>=</mo><mn>10</mn></math></p><p>Take <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mtext>so</mtext><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>2</mn><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>&#946;</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced><mrow><mi>&#946;</mi><mo>,</mo><mn>2</mn><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>&#946;</mi></mrow></mfenced></math></p><p>Now point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> divides <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> internally in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mi mathvariant="normal">P</mi><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mfenced><mrow><mn>4</mn><mo>+</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#945;</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mn>2</mn><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>&#946;</mi></mrow></mfenced></mrow><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>3</mn><mn>13</mn></mfrac><mo>,</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>95</mn><mn>13</mn></mfrac></math></p><p>We get, point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mfrac><mn>3</mn><mn>13</mn></mfrac><mo>,</mo><mfrac><mn>56</mn><mn>13</mn></mfrac></mrow></mfenced><mo>,</mo><mi>B</mi><mfenced><mrow><mfrac><mn>95</mn><mn>13</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mn>12</mn><mn>13</mn></mfrac></mrow></mfenced></math></p><p>Vertex <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> of triangle is the point of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mfenced><mrow><mo>-</mo><mfrac><mn>15</mn><mn>13</mn></mfrac><mo>,</mo><mfrac><mn>32</mn><mn>13</mn></mfrac></mrow></mfenced></math></p><p>area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mfenced close="|" open="|"><mtable><mtr><mtd><mfrac><mn>3</mn><mn>13</mn></mfrac></mtd><mtd><mfrac><mn>56</mn><mn>13</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mfrac><mn>95</mn><mn>13</mn></mfrac></mtd><mtd><mo>-</mo><mfrac><mn>12</mn><mn>13</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mn>15</mn><mn>13</mn></mfrac></mtd><mtd><mfrac><mn>32</mn><mn>13</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>&#215;</mo><msup><mn>13</mn><mn>3</mn></msup></mrow></mfrac><mfenced close="||" open="||"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>56</mn></mtd><mtd><mn>13</mn></mtd></mtr><mtr><mtd><mn>95</mn></mtd><mtd><mo>-</mo><mn>12</mn></mtd><mtd><mn>13</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>15</mn></mtd><mtd><mn>32</mn></mtd><mtd><mn>13</mn></mtd></mtr></mtable></mfenced></math></p><p>area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi><mo>=</mo><mfrac><mn>132</mn><mn>13</mn></mfrac></math>sq. units</p>

</details>

---

### Q44. JEE Main 2022 (27 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In an isosceles triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math>, the vertex <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>6</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> and the equation of the base <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>4</mn></math>. Let the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> lie on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>7</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced></math> is the centroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>51</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>39</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>41</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>51</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fdeeb63a-f8cb-43ed-874e-23d1a4a2b252-image.png" style="width: 213px; height: 170px;" /></p><p>In <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#9651;</mo><mi>A</mi><mi>B</mi><mi>C</mi><mo>,</mo><mo>&#160;</mo><mi>A</mi><mi>B</mi><mo>=</mo><mi>A</mi><mi>C</mi></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>7</mn></math>, we get </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8801;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>&#8801;</mo><mfenced><mrow><mi>h</mi><mo>,</mo><mi>k</mi></mrow></mfenced></math> and as it lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>4</mn></math></p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>h</mi><mo>+</mo><mi>k</mi><mo>=</mo><mn>4</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msup><mi>B</mi><mn>2</mn></msup><mo>=</mo><mi>A</mi><msup><mi>C</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>26</mn><mo>=</mo><mo>(</mo><mi>h</mi><mo>-</mo><mn>6</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>26</mn><mo>=</mo><msup><mfenced><mrow><mi>h</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn><mi>h</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>26</mn><mo>=</mo><mn>5</mn><msup><mi>h</mi><mn>2</mn></msup><mo>-</mo><mn>24</mn><mi>h</mi><mo>+</mo><mn>45</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>h</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>5</mn><mi>h</mi><mo>-</mo><mn>19</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>h</mi><mo>=</mo><mfrac><mn>19</mn><mn>5</mn></mfrac></math>    (as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><mn>1</mn></math>rejected)</p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mo>-</mo><mfrac><mn>18</mn><mn>5</mn></mfrac></math></p><p>Hence, centroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mfrac><mrow><mn>6</mn><mo>+</mo><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>19</mn><mn>5</mn></mfrac></mstyle></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>18</mn><mn>5</mn></mfrac></mstyle></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>&#8801;</mo><mfenced><mrow><mfrac><mn>18</mn><mn>5</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></mrow></mfenced></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>15</mn><mo>&#215;</mo><mfrac><mn>17</mn><mn>5</mn></mfrac><mo>=</mo><mn>51</mn></math></p>

</details>

---

### Q45. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let the area of the triangle with vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mi>&#945;</mi></mrow></mfenced><mo>,</mo><mi>B</mi><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mn>0</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mn>0</mn><mo>,</mo><mi>&#945;</mi></mrow></mfenced></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> sq. units. If the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mo>-</mo><mi>&#945;</mi><mo>,</mo><mi>&#945;</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>,</mo><mi>&#946;</mi></mrow></mfenced></math> are collinear, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>64</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>512</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>64</mn></math>**

**Detailed Solution:**

Given, the area of the triangle with vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mi>&#945;</mi></mrow></mfenced><mo>,</mo><mi>B</mi><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mn>0</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mn>0</mn><mo>,</mo><mi>&#945;</mi></mrow></mfenced></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> sq. units <p>Now applying formula for area we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>&#177;</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>&#177;</mo><mn>8</mn></math></p><p>Now given points will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>8</mn><mo>,</mo><mo>-</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mo>-</mo><mn>8</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>64</mn><mo>,</mo><mi>&#946;</mi></mrow></mfenced></math></p><p>OR <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>8</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mo>-</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>64</mn><mo>,</mo><mi>&#946;</mi></mrow></mfenced></math></p><p>Given above points are collinear, so their slope will be equal, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>slope=</mtext><mfrac><mrow><mn>8</mn><mo>+</mo><mn>8</mn></mrow><mrow><mo>-</mo><mn>8</mn><mo>-</mo><mn>8</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>&#946;</mi><mo>-</mo><mn>8</mn></mrow><mrow><mn>64</mn><mo>+</mo><mn>8</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>64</mn></math></p>

</details>

---

### Q46. JEE Main 2022 (24 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mfrac><mn>3</mn><msqrt><mi>a</mi></msqrt></mfrac><mo>,</mo><msqrt><mi>a</mi></msqrt></mrow></mfenced><mo>,</mo><mi>a</mi><mo>&#62;</mo><mn>0</mn></math>, be a fixed point in the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi></math>-plane. The image of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> and the image of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mfenced><mrow><mn>3</mn><mi>cos</mi><mi>&#952;</mi><mo>,</mo><mi>a</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math>,  is a point in the fourth quadrant such that the maximum area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>C</mi><mi>D</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> square units, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is equal to _____

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced><mrow><mfrac><mn>3</mn><msqrt><mi>a</mi></msqrt></mfrac><mo>,</mo><msqrt><mi>a</mi></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><msqrt><mi>a</mi></msqrt></mfrac><mo>,</mo><msqrt><mi>a</mi></msqrt></mrow></mfenced></math> is the image of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> on y-axis</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><msqrt><mi>a</mi></msqrt></mfrac><mo>,</mo><mo>-</mo><msqrt><mi>a</mi></msqrt></mrow></mfenced></math> is the image of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> in x-axis</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mfenced><mrow><mn>3</mn><mi>cos</mi><mi>&#952;</mi><mo>,</mo><mi>a</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math></p><p>Area of triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi><mi>D</mi></math> will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><mfrac><mn>3</mn><msqrt><mi>a</mi></msqrt></mfrac></mtd><mtd><msqrt><mi>a</mi></msqrt></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mn>3</mn><msqrt><mi>a</mi></msqrt></mfrac></mtd><mtd><mo>-</mo><msqrt><mi>a</mi></msqrt></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn><mi>cos</mi><mi>&#952;</mi></mtd><mtd><mi>a</mi><mi>sin</mi><mi>&#952;</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><msqrt><mi>a</mi></msqrt><mfenced><mrow><mi>cos</mi><mi>&#952;</mi><mo>-</mo><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math></p><p>The maximum area of triangle is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mi>a</mi></msqrt><msqrt><mn>2</mn></msqrt></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mi>a</mi></msqrt><msqrt><mn>2</mn></msqrt><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q47. JEE Main 2021 (01 Sep Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the points of intersections of the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>11</mn><mo>=</mo><mn>0</mn></math> are the mid points of the sides of a triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ABC</mi><mo>.</mo></math> Then the area of the triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ABC</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>,</mo><mo>&#160;</mo><mi>Q</mi><mo>,</mo><mo>&#160;</mo><mi>R</mi></math> are mid-points of sides of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> then  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#215;</mo><mi>A</mi><mi>r</mi><mi>e</mi><mi>a</mi><mo>(</mo><mi>&#916;PQR</mi><mo>)</mo><mo>=</mo><mi>A</mi><mi>r</mi><mi>e</mi><mi>a</mi><mo>(</mo><mo>&#8710;</mo><mi>ABC</mi><mo>)</mo></math></p><p>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>&#916;</mi><mi>ABC</mi><mo>=</mo><mn>4</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mfrac><msup><mfenced close="|" open="|"><mtable columnalign="left left left"><mtr><mtd><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub></mtd><mtd><msub><mrow><mo>&#160;</mo><mi mathvariant="normal">b</mi></mrow><mn>1</mn></msub></mtd><mtd><msub><mi mathvariant="normal">c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">a</mi><mn>2</mn></msub></mtd><mtd><msub><mrow><mo>&#160;</mo><mi mathvariant="normal">b</mi></mrow><mn>2</mn></msub></mtd><mtd><msub><mi mathvariant="normal">c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">a</mi><mn>3</mn></msub></mtd><mtd><msub><mrow><mo>&#160;</mo><mi mathvariant="normal">b</mi></mrow><mn>3</mn></msub></mtd><mtd><msub><mi mathvariant="normal">c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mn>2</mn></msup><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><msub><mi mathvariant="normal">C</mi><mn>3</mn></msub></mrow></mfrac></mfenced></math> </p><p>Where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>,</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><mo>,</mo><msub><mi mathvariant="normal">C</mi><mn>3</mn></msub></math> are cofactors of<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><msub><mi>c</mi><mn>1</mn></msub><mo>,</mo><msub><mi>c</mi><mn>2</mn></msub><mo>,</mo><msub><mi>c</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>&#916;</mi><mi>ABC</mi><mo>=</mo><mn>4</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mfrac><msup><mfenced close="|" open="|"><mtable columnalign="left left left"><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mn>11</mn></mtd></mtr></mtable></mfenced><mn>2</mn></msup><mrow><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>3</mn><mo>)</mo><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>9</mn><mo>&#247;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q48. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be the set of all points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></mrow></mfenced></math> such that the area of triangle formed by the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></mrow></mfenced><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> square units. Then the least possible length of a line segment joining the origin to a point in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><msqrt><mn>5</mn></msqrt></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>12</mn><msqrt><mn>5</mn></msqrt></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>16</mn><msqrt><mn>5</mn></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><msqrt><mn>5</mn></msqrt></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><msqrt><mn>5</mn></msqrt></mfrac></math>**

**Detailed Solution:**

<p>Given:Area of triangle formed by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>12</mn><mo>&#160;</mo><mi>square</mi><mo>&#160;</mo><mi>units</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mn>6</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mn>6</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mfenced><mrow><mn>6</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mi>&#946;</mi><mfenced><mrow><mn>5</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mn>10</mn><mo>-</mo><mn>18</mn></mrow></mfenced><mo>=</mo><mo>&#177;</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>&#945;</mi><mo>-</mo><mn>2</mn><mi>&#946;</mi><mo>-</mo><mn>8</mn><mo>=</mo><mo>&#177;</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>&#945;</mi><mo>-</mo><mn>2</mn><mi>&#946;</mi><mo>=</mo><mn>32</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mi>&#945;</mi><mo>-</mo><mn>2</mn><mi>&#946;</mi><mo>+</mo><mn>16</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>-</mo><mn>16</mn><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn></math></p><p>So point will be either <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>8</mn></mrow></mfenced><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>16</mn></mrow></mfenced></math></p><p>For the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>8</mn></mrow></mfenced></math>,</p><p>Distance from origin
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><msqrt><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mo>(</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>8</mn><msup><mo>)</mo><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>5</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>32</mn><mi>&#945;</mi><mo>+</mo><mn>64</mn></msqrt><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mi>&#946;</mi><mo>=</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>8</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>D</mi><mn>2</mn></msup><mo>=</mo><mn>5</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>32</mn><mi>&#945;</mi><mo>+</mo><mn>64</mn></math></p><p>For maximum or minimum length,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mfenced><msup><mi>D</mi><mn>2</mn></msup></mfenced></mrow><mrow><mi>d</mi><mi>&#945;</mi></mrow></mfrac><mo>=</mo><mn>10</mn><mi>&#945;</mi><mo>+</mo><mn>32</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mfrac><mn>16</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>32</mn></mrow><mn>5</mn></mfrac><mo>+</mo><mn>8</mn><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>D</mi><mo>=</mo><msqrt><msup><mfenced><mrow><mo>-</mo><mfrac><mn>16</mn><mn>5</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mfrac><mn>8</mn><mn>5</mn></mfrac></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><msqrt><mn>5</mn></msqrt><mo>=</mo><mfrac><mn>8</mn><msqrt><mn>5</mn></msqrt></mfrac></math></p><p>Similarly if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>16</mn><mo>,</mo><mo>&#160;</mo><mi>D</mi><mo>=</mo><msqrt><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>16</mn></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>5</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>64</mn><mi>&#945;</mi><mo>+</mo><mn>256</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>D</mi><mn>2</mn></msup><mo>=</mo><mn>5</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>64</mn><mi>&#945;</mi><mo>+</mo><mn>256</mn></math></p><p>For maximum or minimum length,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mfenced><msup><mi>D</mi><mn>2</mn></msup></mfenced></mrow><mrow><mi>d</mi><mi>&#945;</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>10</mn><mi>&#945;</mi><mo>-</mo><mn>64</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>32</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>D</mi><mo>=</mo><msqrt><msup><mfenced><mfrac><mn>32</mn><mn>5</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mfrac><mn>64</mn><mn>5</mn></mfrac><mo>-</mo><mn>16</mn></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><mfrac><mn>16</mn><msqrt><mn>5</mn></msqrt></mfrac><mo>&#160;</mo></math>at <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>32</mn><mn>5</mn></mfrac></math>
So, least possible length of line segment is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><msqrt><mn>5</mn></msqrt></mfrac></math></p>

</details>

---

### Q49. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>(</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>b</mi><mo>+</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>(</mo><mn>0</mn><mo>,</mo><mi>b</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>&#8800;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>|</mo><mi>b</mi><mo>|</mo><mo>&#8800;</mo><mn>1</mn></math>, be points such that the area of triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> sq. unit, then the sum of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>2</mn><mi>b</mi></mrow><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup></mrow><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup></mrow><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>b</mi></mrow><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup></mrow><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given coordinates of triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>(</mo><mi mathvariant="normal">a</mi><mo>,</mo><mn>0</mn><mo>)</mo><mo>,</mo><mi mathvariant="normal">B</mi><mo>(</mo><mi mathvariant="normal">b</mi><mo>,</mo><mn>2</mn><mi mathvariant="normal">b</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>,</mo><mi mathvariant="normal">C</mi><mo>(</mo><mn>0</mn><mo>,</mo><mi mathvariant="normal">b</mi><mo>)</mo></math></p><p>Area<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mn>2</mn><mi>b</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>b</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="[" separators="|"><mrow><mi mathvariant="normal">a</mi><mo>(</mo><mi mathvariant="normal">b</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>+</mo><msup><mi mathvariant="normal">b</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mo>&#177;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mo>+</mo><mi>a</mi><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mo>&#177;</mo><mn>2</mn></math></p><p>If  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> is positive </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#8722;</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>If  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo></math>is negative</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mrow><mo>&#8722;</mo><mn>2</mn><mo>&#8722;</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>Sum of possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup></mrow><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p>

</details>

---

### Q50. JEE Main 2021 (26 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> be a triangle with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8736;</mo><mi>A</mi><mi>C</mi><mi>B</mi><mo>=</mo><mi>&#952;</mi><mo>,</mo><mn>0</mn><mo>&#60;</mo><mi>&#952;</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>. If the equation of the median through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math> and the equation of angle bisector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mi>x</mi><mo>-</mo><mn>4</mn><mi mathvariant="normal">y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#952;</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a28c2936-aa16-46d1-9e4b-e988cff2ef5f-image.png" style="width: 372px; height: 223px;" /></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>coordinate of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math>, So coordinate of the point   <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac></mrow></mfenced></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>(</mo><mi mathvariant="normal">C</mi><mtext>&#160;lies on&#160;</mtext><mn>7</mn><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>)</mo></math></p><p> Hence, mid point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mfenced><mrow><mfrac><mrow><mi>&#945;</mi><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#945;</mi><mo>+</mo><mn>3</mn></mrow><mn>8</mn></mfrac></mrow></mfenced></math></p><p>As, point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> lies on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>, Substituting, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn></math>.</p><p>So. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>(</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>)</mo></math></p><p>Hence, slope of AC is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math> and slope of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> is<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mfrac><mn>7</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow><mrow><mn>1</mn><mo>+</mo><mfrac><mn>7</mn><mn>4</mn></mfrac><mo>&#215;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#183;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#8658;</mo><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q51. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math> undergoes the following three transformations successively:
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>a</mi></mfenced></math> reflection about the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>x</mi><mo>.</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>b</mi></mfenced></math> translation through <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> units along the positive direction of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math> axis.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>c</mi></mfenced></math> rotation through angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math> about the origin in the anti-clockwise direction.</p><p>If the co-ordinates of the final position of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>,</mo><mfrac><mn>7</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi></math> is equal to:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>**

**Detailed Solution:**

<p>Image of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math> along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>x</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mo>&#39;</mo></msup><mfenced><mrow><mi>b</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>.</mo></math></p><p>Translating it <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> units along positive direction of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis it becomes <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mo>&#34;</mo></msup><mfenced><mrow><mi>b</mi><mo>+</mo><mn>2</mn><mo>,</mo><mi>a</mi></mrow></mfenced><mo>.</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e67808c7-89d7-4ab1-86c9-fe613d87c730-image.png" style="width: 306px; height: 250px;" /></p><p>Now, applying Rotation theorem</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mfrac><mn>7</mn><msqrt><mn>2</mn></msqrt></mfrac><mi>i</mi><mo>=</mo><mfenced><mrow><mfenced><mrow><mi>b</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>a</mi><mi>i</mi></mrow></mfenced><mfenced><mrow><mi>cos</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mi>i</mi><mi>sin</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math></p><p>Multiplying the complex numbers we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mfrac><mn>7</mn><msqrt><mn>2</mn></msqrt></mfrac><mi>i</mi><mo>=</mo><mfenced><mrow><mfrac><mrow><mi>b</mi><mo>+</mo><mn>2</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac><mo>-</mo><mfrac><mi>a</mi><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mo>+</mo><mi>i</mi><mfenced><mrow><mfrac><mrow><mi>b</mi><mo>+</mo><mn>2</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mfrac><mi>a</mi><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>-</mo><mi>a</mi><mo>+</mo><mn>2</mn><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>+</mo><mn>2</mn><mo>+</mo><mi>a</mi><mo>=</mo><mn>7</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>4</mn><mo>;</mo><mi>b</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>9</mn></math></p>

</details>

---

### Q52. JEE Main 2021 (20 Jul Shift 2)

*Type:* `numerical` | *Level:* `1`

Consider a triangle having vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>(</mo><mn>1</mn><mo>,</mo><mn>9</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>(</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn><mo>)</mo><mo>.</mo></math> If a line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> passing through the circum-centre of triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mo>,</mo></math> bisects line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mo>,</mo></math> and intersects <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#945;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo></math> then the value of real number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p>We have,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/064346ca-2970-4030-9eb8-222581b9694b-image.png" style="width: 328px; height: 188px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><msqrt><msup><mfenced><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>9</mn></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>45</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi><mo>=</mo><msqrt><msup><mfenced><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>8</mn></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>50</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mo>=</mo><msqrt><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>8</mn><mo>-</mo><mn>9</mn></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>5</mn></msqrt></math></p><p>Here,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msup><mi>C</mi><mn>2</mn></msup><mo>=</mo><mi>A</mi><msup><mi>B</mi><mn>2</mn></msup><mo>+</mo><mi>B</mi><msup><mi>C</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><msqrt><mn>50</mn></msqrt><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mo>(</mo><msqrt><mn>45</mn></msqrt><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><msqrt><mn>5</mn></msqrt><msup><mo>)</mo><mn>2</mn></msup></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8736;</mo><mi>B</mi><mo>=</mo><mn>90</mn><mo>&#176;</mo></math>, so circumcentre is the mid-point of hypotenuse i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi></math>.</p><p>Circumcenter <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8801;</mo><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>11</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Mid-point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mo>=</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mfrac><mn>17</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>y</mi><mo>-</mo><mfrac><mn>11</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mfenced><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>11</mn><mn>2</mn></mfrac></mstyle><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>17</mn><mn>2</mn></mfrac></mstyle></mrow><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle><mo>-</mo><mn>2</mn></mrow></mfrac></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></math></p><p>Passing though <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#945;</mi><mn>2</mn></mfrac></mrow></mfenced></math>, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>9</mn></math></p>

</details>

---

### Q53. JEE Main 2021 (18 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the centroid of an equilateral triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> be at the origin. Let one of the sides of the equilateral triangle be along the straight line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> be the radius of circumcircle and incircle respectively of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>A</mi><mi>B</mi><mi>C</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>R</mi><mo>+</mo><mi>r</mi><mo>)</mo></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><msqrt><mn>2</mn></msqrt></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><msqrt><mn>2</mn></msqrt></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2b39506b-36ec-441d-9f00-b4635be92603-image.png" style="width: 295px; height: 250px;" /><gwmw style="display:none;"></gwmw></p><p>Distance from origin to line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn></math> is inradius.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mi>O</mi><mi>M</mi><mo>=</mo><mfrac><mn>3</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#38;</mo><mo>&#160;</mo><mi>sin</mi><mn>30</mn><mo>&#176;</mo><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>r</mi><mi>R</mi></mfrac><mo>&#8658;</mo><mi>R</mi><mo>=</mo><mfrac><mn>6</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>r</mi><mo>+</mo><mi>R</mi><mo>=</mo><mfrac><mn>9</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p>

</details>

---

### Q54. JEE Main 2021 (17 Mar Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>tan</mi><mi>&#946;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#947;</mi><mo>;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi><mo>&#8800;</mo><mfrac><mrow><mo>(</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math> be the slopes of the three line segments <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>O</mi><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>C</mi><mo>,</mo></math> respectively, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> is origin. If circumcentre of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>A</mi><mi>B</mi><mi>C</mi></math> coincides with origin and its orthocentre lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mrow><mi>cos</mi><mn>3</mn><mi>&#945;</mi><mo>+</mo><mi>cos</mi><mn>3</mn><mi>&#946;</mi><mo>+</mo><mi>cos</mi><mn>3</mn><mi>&#947;</mi></mrow><mrow><mi>cos</mi><mi>&#945;</mi><mo>&#183;</mo><mi>cos</mi><mi>&#946;</mi><mo>&#183;</mo><mi>cos</mi><mi>&#947;</mi></mrow></mfrac></mfenced><mn>2</mn></msup></math> is equal to :

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **144**

**Detailed Solution:**

<p>Given, the slopes of the line segments <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>O</mi><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>C</mi></math> are respectively, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>tan</mi><mi>&#946;</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>tan</mi><mi>&#947;</mi><mo>,</mo></math> then by parametric form the coordinates of the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>C</mi></math> can be taken respectively as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>O</mi><mi>A</mi><mi>cos</mi><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>O</mi><mi>A</mi><mi>sin</mi><mi>&#945;</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>O</mi><mi>B</mi><mi>cos</mi><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mi>O</mi><mi>B</mi><mi>sin</mi><mi>&#946;</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>O</mi><mi>C</mi><mi>cos</mi><mi>&#947;</mi><mo>,</mo><mo>&#160;</mo><mi>O</mi><mi>C</mi><mi>sin</mi><mi>&#947;</mi></mrow></mfenced><mo>.</mo></math></p><p>Given, the circumcentre of the <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> is at origin and we know that the circumcentre is equidistant from the vertices of the triangle, hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>A</mi><mo>=</mo><mi>O</mi><mi>B</mi><mo>=</mo><mi>O</mi><mi>C</mi><mo>.</mo></math></p><p>The centroid of a triangle with vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>3</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>3</mn></msub></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub></mrow><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>2</mn></msub><mo>+</mo><msub><mi>y</mi><mn>3</mn></msub></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>,</mo></math> thus the centroid of the <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mrow><mi>O</mi><mi>A</mi><mfenced><mrow><mo>&#8721;</mo><mi>cos</mi><mi>&#945;</mi></mrow></mfenced></mrow><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mi>O</mi><mi>A</mi><mfenced><mrow><mo>&#8721;</mo><mi>sin</mi><mi>&#945;</mi></mrow></mfenced></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>.</mo></math></p><p>We know that for any triangle the circumcentre, orthocentre and centroid lie on a line.</p><p>Since, the orthocentre and circumcentre both lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis, hence the centroid also lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis, hence the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-coordinate of the centroid is zero.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8721;</mo><mi>cos</mi><mi>&#945;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>&#945;</mi><mo>+</mo><mi>cos</mi><mi>&#946;</mi><mo>+</mo><mi>cos</mi><mi>&#947;</mi><mo>=</mo><mn>0</mn></math></p><p>We know that, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>3</mn></msup><mo>+</mo><msup><mi>b</mi><mn>3</mn></msup><mo>+</mo><msup><mi>c</mi><mn>3</mn></msup><mo>=</mo><mn>3</mn><mi>a</mi><mi>b</mi><mi>c</mi><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>&#945;</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>&#946;</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>&#947;</mi><mo>=</mo><mn>3</mn><mo>&#183;</mo><mi>cos</mi><mi>&#945;</mi><mo>&#183;</mo><mi>cos</mi><mi>&#946;</mi><mo>&#183;</mo><mi>cos</mi><mi>&#947;</mi></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>3</mn><mi>A</mi><mo>=</mo><mn>4</mn><msup><mi>cos</mi><mn>3</mn></msup><mi>A</mi><mo>-</mo><mn>3</mn><mi>cos</mi><mi>A</mi><mo>,</mo></math> we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mrow><mi>cos</mi><mn>3</mn><mi>&#945;</mi><mo>+</mo><mi>cos</mi><mn>3</mn><mi>&#946;</mi><mo>+</mo><mi>cos</mi><mn>3</mn><mi>&#947;</mi></mrow><mrow><mi>cos</mi><mi>&#945;</mi><mo>&#183;</mo><mi>cos</mi><mi>&#946;</mi><mo>&#183;</mo><mi>cos</mi><mi>&#947;</mi></mrow></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mfrac><mrow><mn>4</mn><mfenced><mrow><msup><mi>cos</mi><mn>3</mn></msup><mi>&#945;</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>&#946;</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>&#947;</mi></mrow></mfenced><mo>-</mo><mn>3</mn><mo>(</mo><mi>cos</mi><mi>&#945;</mi><mo>+</mo><mi>cos</mi><mi>&#946;</mi><mo>+</mo><mi>cos</mi><mi>&#947;</mi><mo>)</mo></mrow><mrow><mi>cos</mi><mi>&#945;</mi><mo>&#183;</mo><mi>cos</mi><mi>&#946;</mi><mo>&#183;</mo><mi>cos</mi><mi>&#947;</mi></mrow></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mfrac><mrow><mn>4</mn><mfenced><mrow><mn>3</mn><mo>&#183;</mo><mi>cos</mi><mi>&#945;</mi><mo>&#183;</mo><mi>cos</mi><mi>&#946;</mi><mo>&#183;</mo><mi>cos</mi><mi>&#947;</mi></mrow></mfenced><mo>-</mo><mn>3</mn><mfenced><mn>0</mn></mfenced></mrow><mrow><mi>cos</mi><mi>&#945;</mi><mo>&#183;</mo><mi>cos</mi><mi>&#946;</mi><mo>&#183;</mo><mi>cos</mi><mi>&#947;</mi></mrow></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mn>12</mn></mfenced><mn>2</mn></msup><mo>=</mo><mn>144</mn><mo>.</mo></math></p>

</details>

---

### Q55. JEE Main 2021 (17 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In a triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mi>R</mi><mo mathvariant="italic">,</mo></math> the co-ordinates of the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math> respectively. If the equation of the perpendicular bisector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>R</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>,</mo></math> then the centre of the circumcircle of the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#916;</mi><mi>P</mi><mi>Q</mi><mi>R</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8211;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8211;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>&#8211;</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8211;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>&#8211;</mo><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0421154e-0d6f-4552-abec-4954ea3eb530-image.png" style="width: 310px; height: 160px;" /></p><p>Perpendicular bisector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>R</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math> </p><p>Midpoint of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>Equation of perpendicular bisector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>x</mi></math>.</p><p>Point of intersection of equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> is circumcentre.</p><p>So, circumcentre is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math></p>

</details>

---

### Q56. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>B</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">C</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> be given three points. A line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>&#62;</mo><mn>0</mn></math> , intersects lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math> at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> respectively. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub></math> be the areas of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>A</mi><mi>B</mi><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>P</mi><mi>Q</mi><mi>C</mi></math> respectively, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><msub><mi>A</mi><mn>2</mn></msub></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>15</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3db16443-942f-4c29-aa83-5721f5e0a28b-image.png" style="width: 227px; height: 120px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8801;</mo><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mi>m</mi><msub><mi>x</mi><mn>1</mn></msub></mrow></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>&#8801;</mo><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mi>m</mi><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfrac><mn>13</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>x</mi><mn>1</mn></msub></mtd><mtd><mi>m</mi><msub><mi>x</mi><mn>1</mn></msub></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><msub><mi>x</mi><mn>2</mn></msub></mtd><mtd><mi>m</mi><msub><mi>x</mi><mn>2</mn></msub></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mrow><mn>2</mn><mfenced><mrow><mi>m</mi><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mi>m</mi><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>m</mi><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><msub><mrow><mo>&#160;</mo><mi>A</mi></mrow><mn>2</mn></msub><mo>&#8658;</mo><mfrac><mn>13</mn><mn>2</mn></mfrac><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi>m</mi><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>16</mn><mrow><mn>6</mn><mo>&#160;</mo><mi>m</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi><mo>:</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mo>:</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>:</mo><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>&#8658;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>m</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>:</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>8</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>&#8658;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>8</mn><mrow><mn>4</mn><mo>-</mo><mi>m</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>m</mi></mrow></mfrac><mo>-</mo><mfrac><mn>8</mn><mrow><mn>4</mn><mo>-</mo><mi>m</mi></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mo>-</mo><mn>26</mn><mo>&#160;</mo><mi>m</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>m</mi></mrow></mfenced><mfenced><mrow><mn>4</mn><mo>-</mo><mi>m</mi></mrow></mfenced></mrow></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>26</mn><mo>&#160;</mo><mi>m</mi></mrow><mrow><mfenced><mrow><mn>3</mn><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced close="|" open="|"><mrow><mi>m</mi><mo>-</mo><mn>4</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>26</mn><mo>&#160;</mo><mi>m</mi></mrow><mrow><mfenced><mrow><mn>3</mn><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>4</mn><mo>-</mo><mi>m</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>13</mn><mrow><mn>6</mn><mo>&#160;</mo><mi>m</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>26</mn><mo>&#160;</mo><mi>m</mi></mrow><mrow><mfenced><mrow><mn>3</mn><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>4</mn><mo>-</mo><mi>m</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>13</mn><mrow><mn>6</mn><mo>&#160;</mo><mi>m</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>12</mn><msup><mi>m</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mfenced><mrow><mn>3</mn><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>m</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>12</mn><msup><mi>m</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mfenced><mrow><mn>3</mn><msup><mi>m</mi><mn>2</mn></msup><mo>-</mo><mn>11</mn><mi>m</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>15</mn><msup><mi>m</mi><mn>2</mn></msup><mo>-</mo><mn>11</mn><mi>m</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>15</mn><msup><mi>m</mi><mn>2</mn></msup><mo>-</mo><mn>15</mn><mi>m</mi><mo>+</mo><mn>4</mn><mi>m</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfenced><mrow><mn>15</mn><mi>m</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>m</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q57. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The intersection of three lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>6</mn></math> is a/an

**Options:**

- **(A)** Isosceles triangle
- **(B)** Equilateral triangle
- **(C)** Right angled triangle
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Isosceles triangle**

**Detailed Solution:**

<p>.<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c3ab3c66-0ea4-4537-92c6-25dbce08368a-ef734513-08ac-49ba-a00c-9107bc1a3bea-image.png" style="width: 212px; height: 200px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub><mo>:</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>6</mn></math></p><p>On solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mi>y</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p>On solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub></math>:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>6</mn></math></p><p>On solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>L</mi><mn>3</mn></msub></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi><mo>=</mo><msqrt><mn>4</mn><mo>+</mo><mn>1</mn></msqrt><mo>=</mo><msqrt><mn>5</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mo>=</mo><msqrt><mn>4</mn><mo>+</mo><mn>1</mn></msqrt><mo>=</mo><msqrt><mn>5</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><msqrt><mn>1</mn><mo>+</mo><mn>1</mn></msqrt><mo>=</mo><msqrt><mn>2</mn></msqrt></math></p><p>so it is an isosceles triangle</p>

</details>

---

### Q58. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If a <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> has vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mo>&#8211;</mo><mn>1</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>B</mi><mfenced><mrow><mo>&#8211;</mo><mn>7</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mn>5</mn><mo>,</mo><mo>&#8211;</mo><mn>5</mn></mrow></mfenced></math>, then its orthocentre has coordinates:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8211;</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mo>-</mo><mn>3</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mo>,</mo><mfrac><mn>3</mn><mn>5</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>3</mn><mn>5</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mn>3</mn><mn>5</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8211;</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0ac1216b-f29c-4bf7-a386-73b674a8250d-image.png" style="width: 317px; height: 217px;" /></p><p>Slope of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mrow><mi>B</mi><mi>C</mi></mrow></msub><mo>=</mo><mfrac><mn>6</mn><mrow><mo>-</mo><mn>12</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Slope of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>D</mi><mo>=</mo><mfrac><mn>1</mn><msub><mi>m</mi><mrow><mi>B</mi><mi>C</mi></mrow></msub></mfrac><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>D</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>9</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Slope of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mrow><mi>A</mi><mi>C</mi></mrow></msub><mo>=</mo><mfrac><mn>12</mn><mrow><mo>-</mo><mn>6</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>Slope of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>E</mi><mo>=</mo><mfrac><mn>1</mn><msub><mi>m</mi><mrow><mi>A</mi><mi>C</mi></mrow></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>E</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>x</mi><mo>+</mo><mn>7</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Comparing equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>9</mn><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>9</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>18</mn><mo>=</mo><mi>x</mi><mo>+</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>x</mi><mo>=</mo><mo>-</mo><mn>9</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>9</mn><mo>=</mo><mn>3</mn></math></p><p>Therefore, orthocentre has co-ordinates <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>.</p>

</details>

---

### Q59. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let two points be <math><mi>A</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi></mi><mo>-</mo><mn>1</mn></mrow></mfenced></math> and <math><mi>B</mi><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi></mi><mn>2</mn></mrow></mfenced><mo>.</mo></math> If a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mi>x</mi><mtext>'</mtext><mo>,</mo><mo>&#160;</mo><mi>y</mi><mtext>'</mtext></mrow></mfenced></math> be such that the area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>P</mi><mi>A</mi><mi>B</mi><mo>=</mo><mn>5</mn></math> sq. units and it lies on the line <math><mn>3</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> then a value of <math><mi>&#955;</mi></math> is

**Options:**

- **(A)** <math><mn>4</mn></math>
- **(B)** <math><mn>3</mn></math>
- **(C)** <math><mn>1</mn></math>
- **(D)** <math><mo>-</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>3</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi><mtext>&#39;</mtext></mtd><mtd><mi>y</mi><mtext>&#39;</mtext></mtd><mtd><mn>1</mn></mtd></mtr></mtable><mo>&#8201;</mo></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mtext>'</mtext></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>y</mi><mtext>'</mtext><mo>+</mo><mi>x</mi><mtext>'</mtext></mrow></mfenced><mo>=</mo><mo>&#177;</mo><mn>10</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mo>+</mo><mn>2</mn><mi>x</mi><mtext>&#39;</mtext><mo>+</mo><mi>y</mi><mtext>&#39;</mtext><mo>+</mo><mi>x</mi><mtext>&#39;</mtext><mo>=</mo><mo>&#177;</mo><mn>10</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>x</mi><mtext>&#39;</mtext><mo>+</mo><mi>y</mi><mtext>&#39;</mtext><mo>=</mo><mn>12</mn></math> Or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mtext>'</mtext><mo>+</mo><mi>y</mi><mtext>'</mtext><mo>=</mo><mo>-</mo><mn>8</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mtext>'</mtext><mo>,</mo><mo>&#160;</mo><mi>y</mi><mtext>'</mtext></mrow></mfenced></math> lies on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mtext>'</mtext><mo>+</mo><mi>y</mi><mtext>'</mtext><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>, we get,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>&#955;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#8201;</mo><mo>-</mo><mn>2</mn></math></p>

</details>

---

### Q60. JEE Main 2020 (07 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math><mi>A</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi></mi><mn>0</mn></mrow></mfenced><mo>,</mo><mi></mi><mi>B</mi><mfenced separators="|"><mrow><mn>6</mn><mo>,</mo><mi></mi><mn>2</mn></mrow></mfenced></math> and <math><mi>C</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi></mi><mn>6</mn></mrow></mfenced></math> be the vertices of a triangle <math><mi>A</mi><mi>B</mi><mi>C</mi><mo>.</mo></math> If <math><mi>P</mi></math> is a point inside the triangle <math><mi>A</mi><mi>B</mi><mi>C</mi></math> such that the triangles <math><mi>A</mi><mi>P</mi><mi>C</mi><mo>,</mo><mi></mi><mi>A</mi><mi>P</mi><mi>B</mi><mi></mi></math> and <math><mi>B</mi><mi>P</mi><mi>C</mi></math> have equal areas, then the length of the line segment <math><mi>P</mi><mi>Q</mi><mo>,</mo><mi></mi></math> where <math><mi>Q</mi></math> is the point <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>,</mo><mi></mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>,</mo><mi></mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<math><mi mathvariant="normal">P</mi></math> must be centroid of <math><mo>&#8710;</mo><mi mathvariant="normal">A</mi><mi mathvariant="normal">B</mi><mi mathvariant="normal">C</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi mathvariant="normal">P</mi><mfenced separators="|"><mrow><mfrac><mn>17</mn><mn>6</mn></mfrac><mo>,</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></mrow></mfenced><mo>&#8658;</mo><mi>P</mi><mi>Q</mi><mo>=</mo><msqrt><msup><mfenced separators="|"><mfrac><mn>24</mn><mn>6</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mfenced separators="|"><mfrac><mn>9</mn><mn>3</mn></mfrac></mfenced></msqrt><mo>=</mo><mn>5</mn></math> units

</details>

---

### Q61. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A triangle has a vertex at <math><mo>(</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>)</mo></math> and the mid points of the two sides through it are <math><mo>(</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>)</mo></math> and <math><mo>(</mo><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn><mo>)</mo></math> . Then the centroid of this triangle is:

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi> </mi><mfrac><mrow><mn>7</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mi> </mi><mn>2</mn></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mi> </mi><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mi> </mi><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/598ca96e-b4ce-46dc-8263-aec637eedb1f-image4.png" />
Let co-ordinates of <math><mi>B</mi><mo>=</mo><mfenced separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced></math>
<math><mo>&#8756;</mo><mi>&#160;</mi><mfrac><mrow><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mi>&#160;</mi><mo>-</mo><mn>1</mn><mi>&#160;</mi><mi>&#160;</mi><mo>&#38;</mo><mi>&#160;</mi><mi>&#160;</mi><mfrac><mrow><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>2</mn><mi>&#160;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mn>1</mn></math>
<math><mo>&#8658;</mo><mi>&#160;</mi><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0</mn></math>
<math><mo>&#8756;</mo><mi>B</mi><mo>=</mo><mo>(</mo><mo>-</mo><mn>3</mn><mo>,</mo><mi>&#160;</mi><mn>0</mn><mo>)</mo></math>
Let co-ordinates of <math><mi>C</mi><mo>=</mo><mfenced separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfenced></math>
<math><mo>&#8756;</mo><mi>&#160;</mi><mfrac><mrow><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mn>2</mn><mi>&#160;</mi><mi>&#160;</mi><mo>&#38;</mo><mi>&#160;</mi><mi>&#160;</mi><mfrac><mrow><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mn>3</mn></math>
<math><mo>&#8756;</mo><mi>&#160;</mi><mi>C</mi><mo>=</mo><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mi>&#160;</mi><mn>4</mn></mrow></mfenced></math>
Let centroid <math><mi>G</mi><mo>=</mo><mfenced separators="|"><mrow><mi>h</mi><mo>,</mo><mi>k</mi></mrow></mfenced></math>
<math><mi>h</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mo>+</mo><mn>3</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>&#160;</mi><mi>&#160;</mi></math>
<math><mi>k</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mo>+</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>+</mo><mn>0</mn><mo>+</mo><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mn>2</mn></math>
<math><mo>&#8756;</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#160;</mi></math> Centroid, <math><mi mathvariant="normal">G</mi><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mn>2</mn></mrow></mfenced></math>

</details>

---

### Q62. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If in a parallelogram $\mathrm{ABDC}$, the coordinates of $\mathrm{A}, \mathrm{B}$ and $\mathrm{C}$ are respectively (1,2),(3,4) and $(2,5),$ then the equation of the diagonal $\mathrm{AD}$ is :

**Options:**

- **(A)** $5 x-3 y+1=0$
- **(B)** $5 x+3 y-11=0$
- **(C)** $3 x-5 y+7=0$
- **(D)** $3 x+5 y-13=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $5 x-3 y+1=0$**

**Detailed Solution:**

Since, in parallelogram mid points of both diagonals

coinsides.

$\therefore$ mid-point of $A D=$ mid-point of $B C$

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/BKKZMNN-dDGVSh9X7xx5JWtAgaS6zr89_tOa2GMnnjM.original.fullsize.png">


$\left(\frac{x_{1}+1}{2}, \frac{y_{1}+2}{2}\right)=\left(\frac{3+2}{2}, \frac{4+5}{2}\right)$

$\therefore \quad\left(x_{1}, y_{1}\right)=(4,7)$

Then, equation of $A D$ is,

$y-7=\frac{2-7}{1-4}(x-4)$

$y-7=\frac{5}{3}(x-4)$

$3 y-21=5 x-20$

$5 x-3 y+1=0$

</details>

---

### Q63. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle, the sum of lengths of two sides is $\mathrm{x}$ and the product of the lengths of the same two sides is $y$. if $x^{2}-c^{2}=y,$ where $c$ is the length of the third side of the triangle, then the circumradius of the triangle is

**Options:**

- **(A)** $\frac{3}{2} y$
- **(B)** $\frac{c}{\sqrt{3}}$
- **(C)** $\frac{c}{3}$
- **(D)** $\frac{y}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{c}{\sqrt{3}}$**

**Detailed Solution:**

Let two sides of triangle are $a$ and $b$.

$$

\begin{aligned}

& a+b=x \\

& a b=y \\

& x^{2}-c^{2}=y \Rightarrow(a+b)^{2}-c^{2}=a b \\

\Rightarrow &(a+b-c)(a+b+c)=a b \\

\Rightarrow & 2(s-c)(2 s)=a b \\

\Rightarrow & 4 s(s-c)=a b \\

\Rightarrow & \frac{s(s-c)}{a b}=\frac{1}{4} \\

\Rightarrow & \cos ^{2} \frac{c}{2}=\frac{1}{4} \\

\Rightarrow & \cos c=-\frac{1}{2} \Rightarrow c=120^{\circ}

\end{aligned}

$$

$\therefore$ Area of triangle is,

$\Delta=\frac{1}{2} a b\left(\sin 120^{\circ}\right)=\frac{\sqrt{3}}{4} a b$

$\because \quad R=\frac{a b c}{4 \Delta}$

$\because \quad \mathrm{R}=\frac{a b c}{\sqrt{3} a b}=\frac{c}{\sqrt{3}}$

</details>

---

### Q64. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Two sides of a parallelogram are along the lines, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn><mo>.</mo></math> If its diagonals intersect at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo></math> then one of its vertex is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/521c6085-9024-4f85-b6df-25d8e41a70d7-image.png" style="width: 330px; height: 168px;" /></p><p> As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mo>&#8741;</mo><mi>A</mi><mi>D</mi><mo>&#8658;</mo><msub><mi>Slope</mi><mrow><mi>B</mi><mi>C</mi></mrow></msub><mo>=</mo><msub><mi>Slope</mi><mrow><mi>A</mi><mi>D</mi></mrow></msub></math></p><p>Hence, slope of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mi>h</mi><mo>-</mo><mn>5</mn></mrow><mrow><mi>h</mi><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mi>h</mi><mo>-</mo><mn>2</mn><mo>=</mo><mi>h</mi><mo>-</mo><mn>4</mn><mo>&#8658;</mo><mi>&#160;</mi><mn>2</mn><mi>h</mi><mo>=</mo><mn>2</mn><mo>&#8658;</mo><mi>h</mi><mo>=</mo><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>B</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math></p>

</details>

---

### Q65. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two vertices of a triangle are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>.</mo></math> If its orthocenter is at the origin, then its third vertex lies in which quadrant?

**Options:**

- **(A)** Fourth
- **(B)** Second
- **(C)** Third
- **(D)** First

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Second**

**Detailed Solution:**

<blockquote><p>Let the third vertex be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>h</mi><mo>,</mo><mi>k</mi></mrow></mfenced></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/90a0f36d-8e7d-44a8-9846-4a0d2e539da7-image.png" style="width: 330px; height: 220px;" />

Since <math><mi>H</mi></math> is orthocenter of <math><mi>&#916;</mi><mi>A</mi><mi>B</mi><mi>C</mi></math>

Since the slope of <math><mi>B</mi><mi>H</mi></math> is <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math> hence the slope of <math><mi>A</mi><mi>C</mi></math> will be <math><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math></p><p><math><mo>&#8658;</mo></math> Equation of line <math><mi>A</mi><mi>C</mi></math> is

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>6</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math>

Similarly, since <math><mi>A</mi><mi>H</mi></math> is parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo></math>axis hence <math><mi>B</mi><mi>C</mi></math> will be parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis and

Equation of line <math><mi>B</mi><mi>C</mi></math> is

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math>

On solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>k</mi><mo>=</mo><mn>3</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo></math>The point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced separators="|"><mrow><mi>h</mi><mo>,</mo><mi>k</mi></mrow></mfenced><mo>&#8801;</mo><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>,</mo><mn>3</mn></mrow></mfenced></math> lies in the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>nd</mi></msup></math> quadrant.</p></blockquote>

</details>

---

### Q66. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the line <math><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>24</mn><mo>=</mo><mn>0</mn></math> intersects the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis is at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>,</mo></math> then the incentre of the triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>A</mi><mi>B</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mo>&#160;</mo></math>is the origin, is:

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mi> </mi><mn>4</mn></mrow></mfenced><mi> </mi></math>
- **(B)** <math><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mi> </mi><mn>4</mn></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mi> </mi><mn>3</mn></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mi> </mi><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mi> </mi><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>The <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> intercept of the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>24</mn><mo>=</mo><mn>0</mn></math> can be obtained by putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mn>24</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>8</mn></math></p><p>Hence, the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>8</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>.</mo></math></p><p>Now, the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> intercept of the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>24</mn><mo>=</mo><mn>0</mn></math> can be obtained by putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>y</mi><mo>-</mo><mn>24</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>6</mn></math></p><p>Hence, the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></mrow></mfenced><mo>.</mo></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b759fe84-57ff-48bb-a1c7-0b7f7ef8fd71-138.png" style="width: 361px; height: 245px;" /></p><p>In <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>O</mi><mi>A</mi><mi>B</mi><mo>,</mo></math> we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>A</mi><mo>=</mo><mi>b</mi><mo>=</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mi>O</mi><mi>B</mi><mo>=</mo><mi>a</mi><mo>=</mo><mn>6</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mi>c</mi><mo>=</mo><msqrt><msup><mfenced><mrow><mn>8</mn><mo>-</mo><mn>0</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>0</mn><mo>-</mo><mn>6</mn></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>64</mn><mo>+</mo><mn>36</mn></msqrt><mo>=</mo><mn>10</mn></math> units.</p><p>And, we know that the co-ordinates of incentre <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> of a triangle with vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>3</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>3</mn></msub></mrow></mfenced></math> and having length of the sides opposite to these vertices as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>,</mo></math> respectively,  is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>&#8801;</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>a</mi><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><mi>b</mi><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mi>c</mi><msub><mi>x</mi><mn>3</mn></msub></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mi>a</mi><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><mi>b</mi><msub><mi>y</mi><mn>2</mn></msub><mo>+</mo><mi>c</mi><msub><mi>y</mi><mn>3</mn></msub></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>&#8801;</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>6</mn><mfenced separators="|"><mn>8</mn></mfenced><mo>+</mo><mn>8</mn><mfenced separators="|"><mn>0</mn></mfenced><mo>+</mo><mn>10</mn><mfenced separators="|"><mn>0</mn></mfenced></mrow><mn>24</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mn>6</mn><mfenced separators="|"><mn>0</mn></mfenced><mo>+</mo><mn>8</mn><mfenced separators="|"><mn>6</mn></mfenced><mo>+</mo><mn>10</mn><mfenced separators="|"><mn>0</mn></mfenced></mrow><mn>24</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn></mrow></mfenced><mo>.</mo></math></p>

</details>

---

### Q67. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let the equations of two sides of a triangle be <math><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math> and <math><mn>4</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>-</mo><mn>20</mn><mo>=</mo><mn>0</mn><mo>.</mo></math> If the orthocenter of this triangle is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math> then the equation of it&#39;s third side is:

**Options:**

- **(A)** <math><mn>122</mn><mi>y</mi><mo>+</mo><mn>26</mn><mi>x</mi><mo>+</mo><mn>1675</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math><mn>26</mn><mi>x</mi><mo>-</mo><mn>122</mn><mi>y</mi><mo>-</mo><mn>1675</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mn>26</mn><mi>x</mi><mo>+</mo><mn>61</mn><mi>y</mi><mo>+</mo><mn>1675</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>122</mn><mi>y</mi><mo>-</mo><mn>26</mn><mi>x</mi><mo>-</mo><mn>1675</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>26</mn><mi>x</mi><mo>-</mo><mn>122</mn><mi>y</mi><mo>-</mo><mn>1675</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>To find equation of <math><mi>B</mi><mi>C</mi><mo>,</mo></math> first we will find coordinates of <math><mi>B</mi></math> and <math><mi>C</mi><mo>.</mo></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/40f38032-8bf2-4e08-aa24-9a24e88eed77-image.png" style="width: 350px; height: 186px;" />
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mrow><mi>A</mi><mi>C</mi></mrow></msub><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><msup><mi>B</mi><mo>&#39;</mo></msup></math> are perpendicular to each other </p><p>hence <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mrow><mi>B</mi><msup><mi>B</mi><mo>&#39;</mo></msup></mrow></msub><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>Equation of line passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced></math> and having slope <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub><mo>=</mo><mi>m</mi><mfenced><mrow><mi>x</mi><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow></mfenced></math></p><p>For equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><msup><mi>B</mi><mo>&#39;</mo></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math> 

Point of intersection of <math><mi>A</mi><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><msup><mi>B</mi><mo>&#39;</mo></msup></math> <math><mo>&#8658;</mo><mi>B</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>35</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi>&#160;</mi><mo>-</mo><mn>10</mn></mrow></mfenced></math>

Similarly point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced separators="|"><mrow><mo>-</mo><mn>13</mn><mo>,</mo><mi>&#160;</mi><mo>-</mo><mfrac><mn>33</mn><mn>2</mn></mfrac></mrow></mfenced></math>

Equation of <math><mi>B</mi><mi>C</mi></math> is, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow></mfrac><mfenced><mrow><mi>x</mi><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>+</mo><mn>10</mn><mo>=</mo><mfrac><mn>13</mn><mn>61</mn></mfrac><mi>&#160;</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mn>35</mn><mn>2</mn></mfrac></mrow></mfenced></math>

<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mn>26</mn><mi>x</mi><mo>-</mo><mn>122</mn><mi>y</mi><mo>-</mo><mn>1675</mn><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q68. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>S</mi></math> be the set of all triangles in the <math><mi>x</mi><mi>y</mi></math> -plane, each having one vertex at the origin and the other two vertices lie on coordinate axes with integral coordinates. If each triangle in <math><mi>S</mi></math> has area <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> sq. units, then the number of elements in the set <math><mi>S</mi></math> is:

**Options:**

- **(A)** <math><mn>36</mn></math>
- **(B)** <math><mn>32</mn></math>
- **(C)** <math><mn>9</mn></math>
- **(D)** <math><mn>18</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>36</mn></math>**

**Detailed Solution:**

Since the vertex of given triangle is <math><mi>O</mi></math> (origin) and other two vertices <math><mi>A</mi></math> and <math><mi>B</mi></math> lies on the coordinate axes, hence triangle must be a right-angled triangle.

Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>x</mi><mo>.</mo><mi>y</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>(</mo><mi>&#160;</mi><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>y</mi><mo>&#8712;</mo><mi>I</mi><mo>)</mo></math>

As per given condition

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>x</mi><mo>.</mo><mi>y</mi><mo>=</mo><mn>50</mn><mo>&#8658;</mo><mi>x</mi><mo>.</mo><mi>&#160;</mi><mi>y</mi><mo>=</mo><mn>100</mn></math>

Possible ordered pairs of <math><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>y</mi></mrow></mfenced></math> when <math><mo>&#8710;</mo></math> formed in <math><msup><mrow><mn>1</mn></mrow><mrow><mi>s</mi><mi>t</mi></mrow></msup></math> quadrant are <math><mn>9</mn></math> i. e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mn>100</mn></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mn>50</mn></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mn>25</mn></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mn>5</mn><mo>,</mo><mn>20</mn></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mn>10</mn><mo>,</mo><mn>10</mn></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mn>25</mn><mo>,</mo><mi>&#160;</mi><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mn>50</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mn>100</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>

<math><mo>&#8710;</mo></math> can be formed in any of the quadrants, hence total number of cases <math><mn>9</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>36</mn><mo>.</mo></math>

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/mjsmledjczbtmoxsryzfqwhihshkxrurxtfcxgacwbuvbqsoyd.png" />

</details>

---

### Q69. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

A straight line through origin <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> meets the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>y</mi><mo>=</mo><mn>10</mn><mo>-</mo><mn>4</mn><mi>x</mi><mi>&#160;</mi></math>and <math><mn>8</mn><mi>x</mi><mo>+</mo><mn>6</mn><mi>y</mi><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math> at points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> respectively. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> divides the segment <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> in the ratio

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>:</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>:</mo><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>:</mo><mn>1</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7465427f-5062-46e6-9678-976c8f083538-image.png" style="width: 300px; height: 235px;" /></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><msub><mi>r</mi><mn>1</mn></msub><mi>cos</mi><mi>&#952;</mi><mo>,</mo><mi>&#160;</mi><msub><mi>r</mi><mn>1</mn></msub><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> Lies on straight line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mfenced><mrow><msub><mi>r</mi><mn>1</mn></msub><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mrow><msub><mi>r</mi><mn>1</mn></msub><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>r</mi><mn>1</mn></msub><mfenced><mrow><mn>4</mn><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mn>3</mn><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>10</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>10</mn><mrow><mn>4</mn><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mn>3</mn><mi>sin</mi><mi>&#952;</mi></mrow></mfrac></math>

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced><mrow><mo>-</mo><msub><mi>r</mi><mn>2</mn></msub><mi>cos</mi><mi>&#952;</mi><mo>,</mo><mo>&#160;</mo><mo>-</mo><msub><mi>r</mi><mn>2</mn></msub><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> lies on line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>x</mi><mo>+</mo><mn>6</mn><mi>y</mi><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mfenced><mrow><mo>-</mo><msub><mi>r</mi><mn>2</mn></msub><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mn>6</mn><mfenced><mrow><mo>-</mo><msub><mi>r</mi><mn>2</mn></msub><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>r</mi><mn>2</mn></msub><mfenced><mrow><mn>8</mn><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mn>6</mn><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>-</mo><mn>5</mn><mo>=</mo><mn>0</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>5</mn><mrow><mn>8</mn><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mn>6</mn><mi>sin</mi><mi>&#952;</mi></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><msub><mi>r</mi><mn>1</mn></msub><msub><mi>r</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>1</mn></mfrac></math></p>

</details>

---

### Q70. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>coordinate of the incentre of the triangle that has the coordinates of midpoints of its sides as<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math> <mrow> <mn>1</mn> <mo>-</mo> <msqrt> <mn>2</mn> </msqrt> </mrow> </math>
- **(C)** <math> <mrow> <mn>2</mn> <mo>+</mo> <msqrt> <mn>2</mn> </msqrt> </mrow> </math>
- **(D)** <math> <mrow> <mn>2</mn> <mo>-</mo> <msqrt> <mn>2</mn> </msqrt> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math> <mrow> <mn>2</mn> <mo>-</mo> <msqrt> <mn>2</mn> </msqrt> </mrow> </math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/01aed4e3-f095-46df-92f5-02a74b88ee6b-image.png" style="width: 240px; height: 216px;" />

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mi>&#160;</mi><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mfenced separators="|"><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mi>&#160;</mi><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>3</mn></msub><mo>,</mo><mi>&#160;</mi><msub><mi>y</mi><mn>3</mn></msub></mrow></mfenced></math> be the vertices of a triangle,</p><p>So,
<math><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn></math> [mid point formula <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub></mrow><mn>2</mn></mfrac></math> ]

Similarly,</p><p><math><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0</mn></math>

So, the vertices are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>0</mn><mo>,0</mo></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mn>0</mn><mo>,2</mo></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>.

We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-coordinate of incentre <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mrow><mi>a</mi><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><mi>b</mi><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mi>c</mi><msub><mi>x</mi><mn>3</mn></msub></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfrac></math>   </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>b</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>c</mi><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>,</mo><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mrow><mn>0</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>0</mn></mrow><mrow><mn>2</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfenced><mrow><mn>2</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced></math></p>

</details>

---

### Q71. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `2`

If the line $2 x+y=k$ passes through the point which divides the line segment joining the points $(1,1)$ and $(2,4)$ in the ratio $3: 2$, then $k$ equals

**Options:**

- **(A)** $\frac{29}{5}$
- **(B)** $5$
- **(C)** $6$
- **(D)** $\frac{11}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $6$**

**Detailed Solution:**

Point $p=\left(\frac{6+2}{5}, \frac{12+2}{5}\right)$
$\mathrm{p}=\left(\frac{8}{5}, \frac{14}{5}\right)$
$p\left(\frac{8}{5}, \frac{14}{5}\right)$ lies on $2 x+y=k \quad \Rightarrow \frac{16}{5}+\frac{14}{5}=k \quad \Rightarrow k=\frac{30}{5}=6$

</details>

---

