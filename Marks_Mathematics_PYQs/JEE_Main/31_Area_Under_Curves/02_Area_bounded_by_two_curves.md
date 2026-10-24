# JEE Main Mathematics - Area Under Curves

## Topic 2: Area bounded by two curves

**Total Questions:** 130

---

### Q1. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region $\{(x, y) : x^2 - 8x \leq y \leq -x\}$ is :

**Options:**

- **(A)** $\dfrac{343}{6}$
- **(B)** $\dfrac{637}{6}$
- **(C)** $\dfrac{437}{6}$
- **(D)** $\dfrac{523}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{343}{6}$**

**Detailed Solution:**

The given region is bounded by the parabola $y = x^2 - 8x$ and the line $y = -x$.

To find the points of intersection, equate the two equations:

$x^2 - 8x = -x$

$x^2 - 7x = 0$

$x(x - 7) = 0$

The points of intersection are $x = 0$ and $x = 7$.

In the interval $[0, 7]$, the line $y = -x$ lies above the parabola $y = x^2 - 8x$.

The required area $A$ is given by:

$A = \int_{0}^{7} (-x - (x^2 - 8x)) dx$

$A = \int_{0}^{7} (7x - x^2) dx$

Evaluating the integral:

$A = \left[ \dfrac{7x^2}{2} - \dfrac{x^3}{3} \right]_{0}^{7}$

$A = \dfrac{7(49)}{2} - \dfrac{343}{3}$

$A = \dfrac{343}{2} - \dfrac{343}{3}$

$A = 343 \left( \dfrac{1}{2} - \dfrac{1}{3} \right)$

$A = \dfrac{343}{6}$

Answer: $\dfrac{343}{6}$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region $\{(x, y) : 0 \leq y \leq 6 - x, y^2 \geq 4x - 3, x \geq 0\}$ is:

**Options:**

- **(A)** $8$
- **(B)** $9$
- **(C)** $12$
- **(D)** $15$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $9$**

**Detailed Solution:**

The given region is defined by the inequalities:
$x \geq 0$
$0 \leq y \leq 6 - x \Rightarrow y \geq 0$ and $x \leq 6 - y$
$y^2 \geq 4x - 3 \Rightarrow x \leq \dfrac{y^2 + 3}{4}$

From these inequalities, for a given $y \geq 0$, the value of $x$ ranges from $0$ to $\min\left(6 - y, \dfrac{y^2 + 3}{4}\right)$.

To find the point where the two bounding curves intersect, we equate them:
$6 - y = \dfrac{y^2 + 3}{4}$

$24 - 4y = y^2 + 3$

$y^2 + 4y - 21 = 0$

$(y + 7)(y - 3) = 0$

Since $y \geq 0$, the intersection occurs at $y = 3$.

For $0 \leq y \leq 3$, the right boundary is the parabola $x = \dfrac{y^2 + 3}{4}$.
For $3 \leq y \leq 6$, the right boundary is the line $x = 6 - y$.

The total area $A$ can be calculated by integrating with respect to $y$:
$A = \int_{0}^{3} \dfrac{y^2 + 3}{4} dy + \int_{3}^{6} (6 - y) dy$

Evaluating the first integral:
$\int_{0}^{3} \dfrac{y^2 + 3}{4} dy = \dfrac{1}{4} \left[ \dfrac{y^3}{3} + 3y \right]_{0}^{3} = \dfrac{1}{4} (9 + 9) = \dfrac{18}{4} = \dfrac{9}{2}$

Evaluating the second integral:
$\int_{3}^{6} (6 - y) dy = \left[ 6y - \dfrac{y^2}{2} \right]_{3}^{6} = (36 - 18) - \left(18 - \dfrac{9}{2}\right) = 18 - 13.5 = \dfrac{9}{2}$

Total Area = $\dfrac{9}{2} + \dfrac{9}{2} = 9$

Answer: $9$

</details>

---

### Q3. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region $R = \{(x, y): xy \leq 27, 1 \leq y \leq x^2\}$ is equal to:

**Options:**

- **(A)** $78\log_e 3 - \dfrac{52}{3}$
- **(B)** $54\log_e 3 - \dfrac{52}{3}$
- **(C)** $54\log_e 3 - \dfrac{26}{3}$
- **(D)** $54\log_e 3 + \dfrac{26}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $54\log_e 3 - \dfrac{52}{3}$**

**Detailed Solution:**

The given region is bounded by the curves $y = 1$, $y = x^2$, and $xy = 27$ in the first quadrant.

Let us find the points of intersection of these curves:
Intersection of $y = 1$ and $y = x^2$ gives $x = 1$.
Intersection of $y = x^2$ and $xy = 27$ gives $x(x^2) = 27 \Rightarrow x^3 = 27 \Rightarrow x = 3$, so $y = 9$.
Intersection of $y = 1$ and $xy = 27$ gives $x = 27$.

We can find the area by integrating with respect to $y$ from $y = 1$ to $y = 9$. For a given $y$, the value of $x$ ranges from the parabola $x = \sqrt{y}$ to the hyperbola $x = \dfrac{27}{y}$.

The area $A$ is given by:
$A = \int_{1}^{9} \left( \dfrac{27}{y} - \sqrt{y} \right) dy$

Integrating the terms:
$A = \left[ 27 \ln y - \dfrac{2}{3} y^{3/2} \right]_{1}^{9}$

Substituting the limits:
$A = \left( 27 \ln 9 - \dfrac{2}{3} (9)^{3/2} \right) - \left( 27 \ln 1 - \dfrac{2}{3} (1)^{3/2} \right)$

$A = \left( 27 \ln(3^2) - \dfrac{2}{3} (27) \right) - \left( 0 - \dfrac{2}{3} \right)$

$A = 54 \ln 3 - 18 + \dfrac{2}{3}$

$A = 54 \ln 3 - \dfrac{54}{3} + \dfrac{2}{3}$

$A = 54 \ln 3 - \dfrac{52}{3}$

Answer: $54\log_e 3 - \dfrac{52}{3}$

</details>

---

### Q4. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by the curves $x+3y^2=0$ and $x+4y^2=1$ is equal to:

**Options:**

- **(A)** $\dfrac{1}{3}$
- **(B)** $\dfrac{2}{3}$
- **(C)** $\dfrac{4}{3}$
- **(D)** $\dfrac{5}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{4}{3}$**

**Detailed Solution:**

The equations of the given curves are $x = -3y^2$ and $x = 1 - 4y^2$.

To find the points of intersection, equate the values of $x$:

$-3y^2 = 1 - 4y^2$

$y^2 = 1 \Rightarrow y = \pm 1$

The region is bounded between $y = -1$ and $y = 1$. In this interval, $1 - 4y^2 \ge -3y^2$.

The required area $A$ is given by:

$A = \int_{-1}^{1} \left( (1 - 4y^2) - (-3y^2) \right) dy$

$A = \int_{-1}^{1} (1 - y^2) dy$

Since $1 - y^2$ is an even function:

$A = 2 \int_{0}^{1} (1 - y^2) dy$

$A = 2 \left[ y - \dfrac{y^3}{3} \right]_{0}^{1}$

$A = 2 \left( 1 - \dfrac{1}{3} \right) = 2 \left( \dfrac{2}{3} \right) = \dfrac{4}{3}$

Answer: $\dfrac{4}{3}$

</details>

---

### Q5. JEE Main 2026 (02 April Shift 2)

*Type:* `numerical` | *Level:* `3`

If the area of the region bounded by $16x^2 - 9y^2 = 144$ and $8x - 3y = 24$ is A, then $3(A + 6 \log_e(3))$ is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **24**

**Detailed Solution:**

The given equations are:

Hyperbola: $16x^2 - 9y^2 = 144 \Rightarrow \dfrac{x^2}{9} - \dfrac{y^2}{16} = 1$

Line: $8x - 3y = 24 \Rightarrow y = \dfrac{8}{3}(x - 3)$

To find the points of intersection, substitute $y$ from the line equation into the hyperbola equation:

$16x^2 - 9\left(\dfrac{8}{3}(x - 3)\right)^2 = 144$

$16x^2 - 64(x^2 - 6x + 9) = 144$

$x^2 - 4(x^2 - 6x + 9) = 9$

$-3x^2 + 24x - 45 = 0$

$x^2 - 8x + 15 = 0$

$(x - 3)(x - 5) = 0 \Rightarrow x = 3, x = 5$

For $x \in [3, 5]$, the upper curve is the hyperbola $y = \dfrac{4}{3}\sqrt{x^2 - 9}$ and the lower curve is the line $y = \dfrac{8}{3}(x - 3)$.

The area $A$ of the bounded region is:

$A = \int_{3}^{5} \left( \dfrac{4}{3}\sqrt{x^2 - 9} - \dfrac{8}{3}(x - 3) \right) dx$

Using the standard integral formula $\int \sqrt{x^2 - a^2} dx = \dfrac{x}{2}\sqrt{x^2 - a^2} - \dfrac{a^2}{2}\ln|x + \sqrt{x^2 - a^2}|$:

$\int_{3}^{5} \sqrt{x^2 - 9} dx = \left[ \dfrac{x}{2}\sqrt{x^2 - 9} - \dfrac{9}{2}\ln|x + \sqrt{x^2 - 9}| \right]_{3}^{5}$

$= \left( \dfrac{5}{2}(4) - \dfrac{9}{2}\ln 9 \right) - \left( 0 - \dfrac{9}{2}\ln 3 \right)$

$= 10 - 9\ln 3 + \dfrac{9}{2}\ln 3 = 10 - \dfrac{9}{2}\ln 3$

For the linear part:

$\int_{3}^{5} (x - 3) dx = \left[ \dfrac{(x - 3)^2}{2} \right]_{3}^{5} = \dfrac{4}{2} - 0 = 2$

Substituting these back into the area equation:

$A = \dfrac{4}{3}\left( 10 - \dfrac{9}{2}\ln 3 \right) - \dfrac{8}{3}(2)$

$A = \dfrac{40}{3} - 6\ln 3 - \dfrac{16}{3}$

$A = 8 - 6\ln 3$

We need to find the value of $3(A + 6\log_e 3)$:

$A + 6\ln 3 = 8$

$3(A + 6\ln 3) = 3 \times 8 = 24$

Answer: $24$

</details>

---

### Q6. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $P_{1}: y=4 x^{2}$ and $P_{2}: y=x^{2}+27$ be two parabolas. If the area of the bounded region enclosed between $P_{1}$ and $P_{2}$ is six times the area of the bounded region enclosed between the line $y=\alpha x, \alpha>0$ and $P_{1}$, then $\alpha$ is equal to :

**Options:**

- **(A)** 12
- **(B)** 6
- **(C)** 15
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 12**

**Detailed Solution:**

<img style="width:200px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/28S2_s_14_1.png">
Area bounded between $P_1$ & $P_2$ is
$\int_{-3}^{3} ((x^2 + 27) - (4x^2)) \, dx$
(P.O.I. of $P_1$ & $P_2$ is $x = \pm 3$)
$= 2\int_{0}^{3} (27 - 3x^2) \, dx = 2[27x - x^3]_{0}^{3}$
$= 2[81 - 27] = 108$
$\therefore$ Area bounded between $P_1$ & L is 18 sq. units
(Area between $x^2 = 4ay$ & line $x = my$) is $\dfrac{8a^2}{3m^3}$
$\therefore$ Area between $x^2 = \dfrac{y}{4}$ & $x = \dfrac{y}{\alpha}$ is
$\dfrac{8 \cdot \left(\dfrac{1}{16}\right)^2}{3 \cdot \left(\dfrac{1}{\alpha}\right)^3} = 18$
$\Rightarrow \dfrac{\dfrac{8}{16 \cdot 16}}{\dfrac{3}{\alpha^3}} = 18 \Rightarrow \alpha^3 = 2^6 \cdot 3^3$
$\Rightarrow \alpha = 12$

</details>

---

### Q7. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The area of the region $\mathrm{R}=\left\{(x, y): x y \leq 8,1 \leq y \leq x^{2}, x \geq 0\right\}$ is

**Options:**

- **(A)** $\frac{2}{3}\left(24 \log _{e}(2)-7\right)$
- **(B)** $\frac{1}{3}\left(40 \log _{e}(2)+27\right)$
- **(C)** $\frac{2}{3}\left(20 \log _{e}(2)+9\right)$
- **(D)** $\frac{1}{3}\left(49 \log _{e}(2)-15\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2}{3}\left(24 \log _{e}(2)-7\right)$**

**Detailed Solution:**

The region $R$ is defined by $xy \le 8$, $1 \le y \le x^2$, and $x \ge 0$.
First, find the intersection points of the curves.
Intersection of $y = 1$ and $y = x^2$: $x^2 = 1 \implies x = 1$ (since $x \ge 0$).
Intersection of $y = x^2$ and $xy = 8$: $x(x^2) = 8 \implies x^3 = 8 \implies x = 2$. At $x=2$, $y=4$.
Intersection of $xy = 8$ and $y = 1$: $x(1) = 8 \implies x = 8$.
The region is bounded below by $y = 1$ from $x = 1$ to $x = 8$.
The upper boundary consists of two parts:
From $x = 1$ to $x = 2$, the upper curve is $y = x^2$.
From $x = 2$ to $x = 8$, the upper curve is $y = \frac{8}{x}$.
The area $A$ is given by:
$A = \int_{1}^{2} (x^2 - 1) dx + \int_{2}^{8} (\frac{8}{x} - 1) dx$
$A = [\frac{x^3}{3} - x]_1^2 + [8 \log_e x - x]_2^8$
$A = (\frac{8}{3} - 2) - (\frac{1}{3} - 1) + (8 \log_e 8 - 8) - (8 \log_e 2 - 2)$
$A = (\frac{2}{3}) - (-\frac{2}{3}) + 8(3 \log_e 2) - 8 - 8 \log_e 2 + 2$
$A = \frac{4}{3} + 24 \log_e 2 - 8 \log_e 2 - 6$
$A = 16 \log_e 2 + \frac{4}{3} - 6$
$A = 16 \log_e 2 - \frac{14}{3}$
$A = \frac{2}{3} (24 \log_e 2 - 7)$

</details>

---

### Q8. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(\alpha)$ denote the area of the region in the first quadrant bounded by $x=0, x=1, y^{2}=x$ and $y=|\alpha x-5|-|1-\alpha x|+\alpha x^{2}$. Then $(f(0)+f(1))$ is equal to

**Options:**

- **(A)** 12
- **(B)** 14
- **(C)** 7
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 7**

**Detailed Solution:**

For $\alpha = 0$: curve is $y = 5 - 1 = 4$ (horizontal line), area $= \int_0^1 (4 - \sqrt{x}) dx = 4 - \frac{2}{3} = \frac{10}{3}$
For $\alpha = 1$ and $0 \leq x \leq 1$: $|x-5| = 5-x$, $|1-x| = 1-x$, so $y = 4 + x^2$
Area $= \int_0^1 (4 + x^2 - \sqrt{x}) dx = 4 + \frac{1}{3} - \frac{2}{3} = \frac{11}{3}$
$f(0) + f(1) = \frac{10}{3} + \frac{11}{3} = 7$

</details>

---

### Q9. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{A}_{1}$ be the bounded area enclosed by the curves $y=x^{2}+2, x+y=8$ and $y$-axis that lies in the first quadrant. Let $\mathrm{A}_{2}$ be the bounded area enclosed by the curves $y=x^{2}+2, y^{2}=x, x=2$, and $y$-axis that lies in the first quadrant. Then $\mathrm{A}_{1}-\mathrm{A}_{2}$ is equal to

**Options:**

- **(A)** $\frac{2}{3}(3 \sqrt{2}+1)$
- **(B)** $\frac{2}{3}(2 \sqrt{2}+1)$
- **(C)** $\frac{2}{3}(\sqrt{2}+1)$
- **(D)** $\frac{2}{3}(4 \sqrt{2}+1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{3}(2 \sqrt{2}+1)$**

**Detailed Solution:**

For $A_1$: intersection of $y = x^2 + 2$ and $x + y = 8$ at $x = 2, y = 6$
$A_1 = \int_0^2 (8-x-(x^2+2)) dx = \int_0^2 (6-x-x^2) dx = \left[6x - \frac{x^2}{2} - \frac{x^3}{3}\right]_0^2 = 12 - 2 - \frac{8}{3} = \frac{22}{3}$
For $A_2$: bounded by $y = x^2 + 2$, $y^2 = x$ (i.e., $x = y^2$), $x = 2$, and $y$-axis.
In first quadrant, $y^2 = x$ goes from (0,0) to (2,$\sqrt{2}$).
The parabola $y = x^2 + 2$ passes through (0,2) and (2,6).
$A_2 = \int_0^{\sqrt{2}} (2 - y^2) dy = \left[2y - \frac{y^3}{3}\right]_0^{\sqrt{2}} = 2\sqrt{2} - \frac{2\sqrt{2}}{3} = \frac{4\sqrt{2}}{3}$
$A_1 - A_2 = \frac{22}{3} - \frac{4\sqrt{2}}{3} = \frac{2}{3}(2\sqrt{2}+1)$

</details>

---

### Q10. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The area of the region enclosed between the circles $x^{2}+y^{2}=4$ and $x^{2}+(y-2)^{2}=4$ is:

**Options:**

- **(A)** $\frac{4}{3}(2 \pi-3 \sqrt{3})$
- **(B)** $\frac{2}{3}(2 \pi-3 \sqrt{3})$
- **(C)** $\frac{2}{3}(4 \pi-3 \sqrt{3})$
- **(D)** $\frac{4}{3}(2 \pi-\sqrt{3})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{3}(4 \pi-3 \sqrt{3})$**

**Detailed Solution:**

Circle 1: centre $(0,0)$, $r=2$. Circle 2: centre $(0,2)$, $r=2$. Distance between centres $d=2$.
Intersection: $y^2 = (y-2)^2 \Rightarrow y = 1$, giving $x = \pm\sqrt{3}$.
Angle subtended at centre of circle 1 by the chord: $\theta = 2\pi/3$.
Segment area $= \frac{1}{2}(4)\left(\frac{2\pi}{3}\right) - \frac{1}{2}(4)\sin\frac{2\pi}{3} = \frac{4\pi}{3} - \sqrt{3}$.
By symmetry, total intersection area $= 2\left(\frac{4\pi}{3} - \sqrt{3}\right) = \frac{8\pi - 6\sqrt{3}}{3} = \frac{2}{3}(4\pi - 3\sqrt{3})$.

</details>

---

### Q11. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The area of the region $\mathrm{A}=\left\{(x, y): 4 x^{2}+y^{2} \leqslant 8\right.$ and $\left.y^{2} \leqslant 4 x\right\}$ is:

**Options:**

- **(A)** $\pi+4$
- **(B)** $\pi+\frac{2}{3}$
- **(C)** $\frac{\pi}{2}+2$
- **(D)** $\frac{\pi}{2}+\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\pi+\frac{2}{3}$**

**Detailed Solution:**

<img style="width:200px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/22S2_s_19_1.png">
$A = \int_{0}^{2} 2\sqrt{x} \, dx + 2\int_{1}^{\sqrt{2}} \sqrt{8 - 4x^2} \, dx$
$= \dfrac{8}{3} \left( x^{\frac{3}{2}} \right) \bigg|_{0}^{1} + 4\int_{1}^{\sqrt{2}} \sqrt{2 - x^2} \, dx$
$= \dfrac{8}{3} + 4 \times \dfrac{1}{2} \left[ x\sqrt{2 - x^2} + 2\sin^{-1}\left( \dfrac{x}{\sqrt{2}} \right) \right] \bigg|_{1}^{\sqrt{2}}$
$= \dfrac{8}{3} + 2 \left[ 2 \times \dfrac{\pi}{2} - 1 - 2 \times \dfrac{\pi}{4} \right]$
$= \dfrac{8}{3} + 2\pi - 2 - \pi = \pi + \dfrac{2}{3}$ sq. units

</details>

---

### Q12. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the line $x=-1$ divide the area of the region $\left\{(x, y): 1+x^{2} \leq y \leq 3-x\right\}$ in the ratio $m: n, \operatorname{gcd}(m, n)=1$. Then $m+n$ is equal to

**Options:**

- **(A)** 27
- **(B)** 25
- **(C)** 28
- **(D)** 26

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 27**

**Detailed Solution:**

<img style="width:250px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/22S1_s_3_1.png">
$\dfrac{m}{n} = \dfrac{\int_{-1}^{1} [(3-x) - (1+x^2)] \, dx}{\int_{-2}^{1} [(3-x) - (1+x^2)] \, dx} = \dfrac{20}{7}$
$\therefore m + n = 20 + 7$
$= 27$

</details>

---

### Q13. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If the area of the region $\left\{(x, y): 1-2 x \leqslant y \leqslant 4-x^{2}, x \geqslant 0, y \geqslant 0\right\}$ is $\frac{\alpha}{\beta}, \alpha, \beta \in \mathbf{N}, \operatorname{gcd}(\alpha, \beta)=1$, then the value of $(\alpha+\beta)$ is :

**Options:**

- **(A)** $67$
- **(B)** $91$
- **(C)** 73
- **(D)** 85

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 73**

**Detailed Solution:**

<img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/21S2_s_12_1.png">
Required area $= \dfrac{2}{3} \times 8 - \dfrac{1}{2} \times \dfrac{1}{2} \times 1$
$= \dfrac{16}{3} - \dfrac{1}{4} = \dfrac{61}{12} = \dfrac{\alpha}{\beta}$
$\Rightarrow \alpha + \beta = 73$

</details>

---

### Q14. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region, inside the ellipse $x^{2}+4 y^{2}=4$ and outside the region bounded by the curves $y=|x|-1$ and $y=1-|x|$, is :

**Options:**

- **(A)** $2 \pi-1$
- **(B)** $3(\pi-1)$
- **(C)** $2 \pi-\frac{1}{2}$
- **(D)** 2($\pi-1$)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2($\pi-1$)**

**Detailed Solution:**

Ellipse: $\frac{x^2}{4} + y^2 = 1$ with $a = 2$, $b = 1$. Area $= \pi ab = 2\pi$.
Curves $y = |x| - 1$ and $y = 1 - |x|$ intersect at $x = \pm 1$, forming a rhombus with vertices $(0, 1)$, $(1, 0)$, $(0, -1)$, $(-1, 0)$.
Vertices $(0, \pm 1)$ lie on ellipse; $(\pm 1, 0)$ are inside ellipse.
Area of rhombus $= \frac{1}{2} \times 2 \times 2 = 2$.
Required area $= 2\pi - 2 = 2(\pi - 1)$.

</details>

---

### Q15. JEE Main 2025 (8 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the area of the bounded region $\left\{(x, y): 0 \leq 9 x \leq y^2, y \geq 3 x-6\right\}$ be A. Then 6 A is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **15**

**Detailed Solution:**

$0 \leq 9 x \leq y^2 \& y \geq 3 x-6$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Da8qHrCALHOGwq_3pBACHXdtKT7b5kLf84a16lbmci8.original.fullsize.png"/>
$\begin{aligned} & A=\text { Required Area }=\left[\int_0^1(-3 \sqrt{x}) d x-\int_0^1(3 x-6) d x\right] \\ & A=-\left.3\left(\frac{x^{\frac{3}{2}}}{\frac{3}{2}}\right)\right|_0 ^1-\left.\left(\frac{3 x^2}{2}-6 x\right)\right|_0 ^1 \\ & A=-2[1-0]\left[\frac{3}{2}-6\right] \\ & A=-2-\frac{3}{2}+6=\frac{5}{2} \text { Sq. unit } \\ & \therefore 6 A=6 \times \frac{5}{2}=15\end{aligned}$

</details>

---

### Q16. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the area of the region $\left\{(\mathrm{x}, \mathrm{y}): 1+\mathrm{x}^2 \leq \mathrm{y} \leq \min \{\mathrm{x}+7,11-3 \mathrm{x}\}\right\}$ is A , then 3 A is equal to

**Options:**

- **(A)** 50
- **(B)** 49
- **(C)** 46
- **(D)** 47

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 50**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/PYV_cwUoHEyN8m1xerfnLMKiPYkVMOhkh3i_OKwo0x8.original.fullsize.png"/>
$\begin{aligned} & A=\int_{-2}^1\left(x+7-x^2-1\right) d x+\int_1^2\left(11+3 x-x^2-1\right) d x \\ & =\left[\frac{x^2}{2}+6 x-\frac{x^3}{3}\right]_{-2}^1+\left[10 x-\frac{3 x^2}{2}-\frac{x^3}{3}\right]_1^2 \\ & =\frac{50}{3} \Rightarrow 3 A=50 \quad \text { Option (1) }\end{aligned}$

</details>

---

### Q17. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the area of the region bounded by the curves \(y=4-\frac{x^2}{4}\) and \(y=\frac{x-4}{2}\) is equal to \(\alpha\), then \(6 \alpha\) equals

**Options:**

- **(A)** 250
- **(B)** 210
- **(C)** 240
- **(D)** 220

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 250**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/qL8ni4XCuBaCfgzDrt9Uq9ZqjuJ3OMLjJDJULJLWamg.original.fullsize.png"/>
$\begin{aligned} & \text { Area }=\int_{-6}^4\left\{\left(4-\frac{x^2}{4}\right)-\left(\frac{x-4}{2}\right)\right\} d x \\ & =\int_{-6}^4\left\{-\frac{x^2}{4}-\frac{x-6}{2}\right\} d x \\ & \alpha=-\frac{x^3}{12}-\frac{x^2}{4}+\left.6 x\right|_{-6} ^4=\frac{125}{3} \\ & \therefore 6 \alpha=250\end{aligned}$

</details>

---

### Q18. JEE Main 2025 (4 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

If the area of the region $\{(x, y):|x-5| \leq y \leq 4 \sqrt{x}\}$ is A , then 3 A is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **368**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/HvdZ_CyVHJzYZUO4bKb9DvC69ZY76y3TUVPoO-voQ9w.original.fullsize.png"/>
$\begin{aligned} & A=\int_1^{25} 4 \sqrt{x} d x-\frac{1}{2} \times 4 \times 4-\frac{1}{2} \times 20 \times 20 \\ & A=\left[\frac{4 x^{3 / 2}}{\frac{3}{2}}\right]^{25}-8-200 \\ & A=\frac{8}{3}(125-1)-208 \\ & A=\frac{368}{3} \Rightarrow 3 A=368\end{aligned}$

</details>

---

### Q19. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region $\{(x, y):|x-y| \leq y \leq 4 \sqrt{x}\}$ is

**Options:**

- **(A)** $512$
- **(B)** $\frac{1024}{3}$
- **(C)** $\frac{512}{3}$
- **(D)** $\frac{2048}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1024}{3}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/uDlfzYA5BRRtF4DSpHcut-DD2s_998_5pG96Eh8NQrk.original.fullsize.png"/>
$\begin{aligned} & |x-y| \leq y \leq 4 \sqrt{x} \\ & \text { Now } y=|x-y| \\ & y^2=(x-y)^2 \\ & \Rightarrow y=\frac{x}{2} \text { and } x=0\end{aligned}$
$\begin{aligned} & \text { Now area }=\int_0^{64}\left(4 \sqrt{\mathrm{x}}-\frac{\mathrm{x}}{2}\right) \mathrm{dx} \\ & =\left[\frac{4 \mathrm{x}^{3 / 2}}{3 / 2}-\frac{\mathrm{x}^2}{4}\right]_0^{64}=\frac{8}{3} \cdot 8^3-\frac{64^2}{4}=64^2\left(\frac{1}{12}\right) \\ & =\frac{1024}{3}\end{aligned}$

</details>

---

### Q20. JEE Main 2025 (3 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

The area of the region bounded by the curve $y=\max \{|x|, x|x-2|\}$, then $x$-axis and the lines $x=-2$ and $x=4$ is equal to _______ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ZAORk50s0lcQI7sRAdHl4N_DJSUcRHOTjaxCpVZdMyU.original.fullsize.png"/>
$\begin{aligned} & \text { Required Area }=\frac{1}{2} \times 2 \times 2+\frac{1}{2} \times 3 \times 3+\frac{1}{2} \times 1 \times 11 \\ & =12\end{aligned}$

</details>

---

### Q21. JEE Main 2025 (2 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

If the area of the region
$\left\{(x, y):\left|4-x^2\right| \leq y \leq x^2, y \leq 4, x \geq 0\right\}$
is $\left(\frac{80 \sqrt{2}}{\alpha}-\beta\right), \boldsymbol{\alpha}, \boldsymbol{\beta} \in \mathbf{N}$, then $\alpha+\beta$ is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **22**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1OsYtCfd5SMFGJbgPAuZ8cKrqXqKzlyVw_dh-vmCi_s.original.fullsize.png"/>
$\mathrm{A}=\int_0^4 \sqrt{4+\mathrm{y}} \mathrm{dy}-\int_0^2 \sqrt{4-\mathrm{y}} \mathrm{dy}-\int_2^4 \sqrt{\mathrm{y}} \mathrm{dy}$
$=\left(\frac{(4+y)^{\frac{3}{2}}}{\frac{3}{2}}\right)_0^4+\left(\frac{(4-y)^{\frac{3}{2}}}{\frac{3}{2}}\right)_0^2-\left(\frac{\mathrm{y}^{\frac{3}{2}}}{\frac{3}{2}}\right)_0^4$
$\frac{80 \sqrt{2}}{3}-16=\frac{40 \sqrt{2}}{3}-16$
$\alpha=6, \beta=16$
$\alpha+\beta=22$

</details>

---

### Q22. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the area enclosed between the curves $|y|=1-x^2$ and $x^2+y^2=1$ be $\alpha$. If $9 \alpha=\beta \pi+\gamma ; \beta, \gamma$ are integers, then the value of $|\beta-\gamma|$ equals.

**Options:**

- **(A)** 27
- **(B)** 33
- **(C)** 15
- **(D)** 18

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 33**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/v1aMbTlvzmK2iqpp-k7ldBFHMIyosyetWO-gYe-AkgQ.original.fullsize.png">

$\begin{aligned} & \text { Required area }=\pi-4 \int_0^1\left(1-x^2\right) d x \\ & =\pi-4\left[x-\frac{x^3}{3}\right]_0^1 \\ & =\pi-4 \times \frac{2}{3}=\pi-\frac{8}{3} \\ & \therefore \alpha=\pi-\frac{8}{3} \\ & 9 \alpha=9 \pi-24 \rightarrow \beta=9, \gamma=-24 \\ & |\beta-\gamma|=|9+24|=33\end{aligned}$

</details>

---

### Q23. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area of the region bounded by the curves $x\left(1+y^2\right)=1$ and $y^2=2 x$ is:

**Options:**

- **(A)** $2\left(\frac{\pi}{2}-\frac{1}{3}\right)$
- **(B)** $\frac{\pi}{2}-\frac{1}{3}$
- **(C)** $\frac{\pi}{4}-\frac{1}{3}$
- **(D)** $\frac{1}{2}\left(\frac{\pi}{2}-\frac{1}{3}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{2}-\frac{1}{3}$**

**Detailed Solution:**

$\begin{aligned}
& x\left(1+y^2\right)=1 \\
& y^2=2 x
\end{aligned}$

From equation (1) \& (2)
$\begin{aligned}
x(1+2 x)=1 & \Rightarrow 2 x^2+x-1=0 \\
& \Rightarrow x=\frac{1}{2}, x=-1 \text { (Reject) } \\
& \Rightarrow y^2=2\left(\frac{1}{2}\right) \\
& \Rightarrow y= \pm 1
\end{aligned}$



<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6X7_oonfV008fb8YzDu68cVXBrvdK8nbqoFps5zZCMg.original.fullsize.png">




$\begin{aligned} \text { Area bounded } & =\int_{-1}^1\left(\frac{1}{1+y^2}-\frac{y^2}{2}\right) d y \\ & =\left.\left(\tan ^{-1} y-\frac{y^3}{6}\right)\right|_{-1} ^1 \\ & =\frac{\pi}{2}-\frac{1}{3}\end{aligned}$

</details>

---

### Q24. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region
$\left\{(x, y): 0 \leq \mathrm{y} \leq 2|x|+1,0 \leq \mathrm{y} \leq x^2+1,|x| \leq 3\right\}$ is

**Options:**

- **(A)** $\frac{80}{3}$
- **(B)** $\frac{64}{3}$
- **(C)** $\frac{32}{3}$
- **(D)** $\frac{17}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{64}{3}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/G0Z_4FSmE3cVYJ3lFZBPE5pHJkk5nUNBwWU6aXRonYw.original.fullsize.png">

$\begin{aligned} & \text { Area }=2\left[\int_0^2\left(x^2+1\right) d x+\frac{1}{2}[5+7] \times 1\right] \\ & =\frac{64}{3}\end{aligned}$

</details>

---

### Q25. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Consider the region $R=\left\{(x, y): x \leq y \leq 9-\frac{11}{3} x^2, x \geq 0\right\}$.
The area, of the largest rectangle of sides parallel to the coordinate axes and inscribed in R , is:

**Options:**

- **(A)** $\frac{730}{119}$
- **(B)** $\frac{625}{111}$
- **(C)** $\frac{821}{123}$
- **(D)** $\frac{567}{121}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{567}{121}$**

**Detailed Solution:**

$\mathrm{t} .\left(9-\frac{11 \mathrm{t}^2}{3}-\mathrm{t}\right)$

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/-fmqPBqYEjxt2mXhKwMGuC7U2efZQrQN66p2Rn2jo0o.original.fullsize.png">




$\begin{aligned} & \mathrm{A}=9 \mathrm{t}-\mathrm{t}^2-\frac{11}{3} \mathrm{t}^3 \\ & \frac{\mathrm{dA}}{\mathrm{dt}}=9-2 \mathrm{t}-11 \mathrm{t}^2 \\ & \Rightarrow 11 \mathrm{t}^2+2 \mathrm{t}-9=0 \\ & 11 \mathrm{t}^2+11 \mathrm{t}-9 \mathrm{t}-9=0 \\ & \mathrm{t}=-1 \& \mathrm{t}=\frac{9}{11}\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/BStwGSccrW__mRzM8nKCdyUIMC3cNJ0aqQ6HtCVh6zs.original.fullsize.png">


$\begin{aligned} & \therefore \text { largest area }=\frac{9}{11}\left(9-\frac{11}{3}, \frac{81}{121}-\frac{9}{11}\right) \\ & =\frac{9}{11} \cdot \frac{63}{11}=\frac{567}{121}\end{aligned}$

</details>

---

### Q26. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The area of the region $\left\{(x, y): x^2+4 x+2 \leq y \leq|x+2|\right\}$ is equal to

**Options:**

- **(A)** $7$
- **(B)** $5$
- **(C)** $24 / 5$
- **(D)** $20 / 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $20 / 3$**

**Detailed Solution:**

$x^2+4 x+2 \leq y \leq|x+2|$
<img src="https://cdn.quizrr.in/question-assets/jee_main_pyq/8zqX43zxtI8F365ZPYNKx3yMfeEUGI27LSyQB6Kfw0U.original.fullsize_2.png">
$\begin{aligned} & A_1=\int_{-4}^0\left[2-\left(x^2+4 x+2\right)\right] d x-\frac{1}{2} \times 4 \times 2 \\ & =\left(\frac{-x^3}{3}-2 x^2\right)_{-4}^0-4 \\ & =0-\left(\frac{64}{3}-32\right)-4 \\ & =32-\frac{64}{3}-4=\frac{20}{3}\end{aligned}$

</details>

---

### Q27. JEE Main 2025 (23 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

If the area of the larger portion bounded between the curves $x^2+y^2=25$ and $y=|x-1|$ is $\frac{1}{4}(b \pi+c), b, c \in N$, then $b+c$ is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **77**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/DFbKk3NjDPGzXwXAf_4ptoiZKtDtZmYrkN_udPgAu6w.original.fullsize.png">




$\begin{aligned} & \mathrm{x}^2+\mathrm{y}^2=5 \\ & \mathrm{x}^2+(\mathrm{x}-1)^2=25 \Rightarrow \mathrm{x}=4 \\ & \mathrm{x}^2+(-\mathrm{x}+1)^2=5 \Rightarrow \mathrm{x}=-3 \\ & \mathrm{~A}=25 \pi-\int_{-3}^4 \sqrt{25-\mathrm{x}^2} \mathrm{dx}+\frac{1}{2} \times 4 \times 4+\frac{1}{2} \times 3 \times 3 \\ & \mathrm{~A}=25 \pi+\frac{25}{2}-\left[\frac{\mathrm{x}}{2} \sqrt{25-\mathrm{x}^2}+\frac{25}{2} \sin ^{-1} \frac{\mathrm{x}}{5}\right]_{-3}^4 \\ & \mathrm{~A}=25 \pi+\frac{25}{2}-\left[6+\frac{25}{2} \sin ^{-1} \frac{4}{5}+6+\frac{25}{2} \sin ^{-1} \frac{3}{5}\right] \\ & \mathrm{A}=25 \pi+\frac{1}{2}-\frac{25}{2} \cdot \frac{\pi}{2} \\ & \mathrm{~A}=\frac{75 \pi}{4}+\frac{1}{2} \\ & \mathrm{~A}=\frac{1}{4}(75 \pi+2) \\ & \mathrm{b}=75, \mathrm{c}=2 \\ & \mathrm{~b}+\mathrm{c}=75+2=77\end{aligned}$

</details>

---

### Q28. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region enclosed by the curves $y=x^2-4 x+4$ and $y^2=16-8 x$ is :

**Options:**

- **(A)** $\frac{8}{3}$
- **(B)** $\frac{4}{3}$
- **(C)** 8
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{8}{3}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1_jYEcxFbOuu0w4BbjMWmeZGfErds5nUzuLElpwyO_w.original.fullsize.png">

$\begin{aligned} \text { Area } & =\int_0^2\left(\sqrt{16-8 x}-\left(x^2-4 x+4\right)\right) d x \\ & \left.=\frac{-(16-8 x)^{3 / 2}}{12}-\frac{x^3}{3}+2 x^2+4 x\right]_0^2 \\ & =\frac{8}{3}\end{aligned}$

</details>

---

### Q29. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region, inside the circle $(x-2 \sqrt{3})^2+y^2=12$ and outside the parabola $y^2=2 \sqrt{3} x$ is :

**Options:**

- **(A)** $3 \pi+8$
- **(B)** $6 \pi-16$
- **(C)** $3 \pi-8$
- **(D)** $6 \pi-8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $6 \pi-16$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/rQTw_nIFyNU_s37f49dRGnVXC8XAlzNA8eCJjDL5RUs.original.fullsize.png">

$\begin{aligned} & \text { Required area }=2 \int_0^{2 \sqrt{3}}\left(\sqrt{4 \sqrt{3} x-x^2}-\sqrt{2 \sqrt{3} x}\right) d x \\ & =2 \int_0^{2 \sqrt{3}}\left(\sqrt{12-(x-2 \sqrt{3})^2}-\sqrt{2 \sqrt{3} x}\right) d x \\ & =2\left[\frac{x-2 \sqrt{3}}{2} \sqrt{12-(x-2 \sqrt{3})^2}+\frac{12}{2} \sin ^{-1}\left(\frac{x-2 \sqrt{3}}{2 \sqrt{3}}\right)\right. \\ & \left.-\frac{\sqrt{2 \sqrt{3}} x^{\frac{3}{2}}}{\frac{3}{2}}\right]_0^{2 \sqrt{3}} \\ & =2\{3 \pi-8\} \\ & =6 \pi-16 \text { sq. units. }\end{aligned}$

</details>

---

### Q30. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area (in square units) of the region enclosed by the ellipse $x^2+3 y^2=18$ in the first quadrant below the line $y=x$ is

**Options:**

- **(A)** $\sqrt{3} \pi-\frac{3}{4}$
- **(B)** $\sqrt{3} \pi+1$
- **(C)** $\sqrt{3} \pi$
- **(D)** $\sqrt{3} \pi+\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{3} \pi$**

**Detailed Solution:**

$\frac{x^2}{18}+\frac{y^2}{6}=1$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Zmn6qVYXw7yTR4iiMKi_lqlBDzjYFi2kdIpYR8tJbqM.original.fullsize.png">
$\begin{aligned}
& \frac{x^2}{18}+\frac{3 x^2}{18}=1 \Rightarrow 4 x^2=18 \Rightarrow x^2=\frac{9}{2} \\
& \int_{\frac{3}{\sqrt{2}}}^{\sqrt[3]{2}} \frac{\sqrt{18-x^2}}{\sqrt{3}} d x \\
& =\frac{1}{\sqrt{3}}\left(\frac{x \sqrt{18-x^2}}{2}+\frac{18}{2} \sin ^{-1} \frac{x}{3 \sqrt{2}}\right)_{\frac{3}{\sqrt{2}}}^{3 \sqrt{2}} \\
& =\frac{1}{\sqrt{3}}\left(9 \times \frac{\pi}{2}-\frac{3}{2 \sqrt{2}} \times \frac{3 \sqrt{3}}{\sqrt{2}}-9 \times \frac{\pi}{6}\right)
\end{aligned}$
Required Area
$\begin{aligned}
& =\frac{1}{2} \times \frac{9}{2}+\left(\frac{18 \pi}{6}-\frac{9 \sqrt{3}}{4}\right) \frac{1}{\sqrt{3}} \\
& =\sqrt{3} \pi
\end{aligned}$

</details>

---

### Q31. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The parabola $y^2=4 x$ divides the area of the circle $x^2+y^2=5$ in two parts. The area of the smaller part is equal to:

**Options:**

- **(A)** $\frac{1}{3}+5 \sin ^{-1}\left(\frac{2}{\sqrt{5}}\right)$
- **(B)** $\frac{1}{3}+\sqrt{5} \sin ^{-1}\left(\frac{2}{\sqrt{5}}\right)$
- **(C)** $\frac{2}{3}+5 \sin ^{-1}\left(\frac{2}{\sqrt{5}}\right)$
- **(D)** $\frac{2}{3}+\sqrt{5} \sin ^{-1}\left(\frac{2}{\sqrt{5}}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{3}+5 \sin ^{-1}\left(\frac{2}{\sqrt{5}}\right)$**

**Detailed Solution:**

$\begin{aligned} & y^2=4 x \\ & x^2+y^2=5\end{aligned}$
$\therefore$ Area of shaded region as shown in the figure will be
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/gKVyOTchvX_w2wMbGCosb_83vqFKbJLAlV0LLTmZSTI.original.fullsize.png">
$\begin{aligned} & \mathrm{A}_1=\int_0^1 \sqrt{4 \mathrm{x}} \mathrm{dx}+\int_1^{\sqrt{5}} \sqrt{5-\mathrm{x}^2} \mathrm{dx} \\ & =\frac{4}{3} \cdot\left[\mathrm{x}^{\frac{3}{2}}\right]_0^1+\left[\frac{\mathrm{x}}{2} \sqrt{5-\mathrm{x}^2}+\frac{5}{2} \sin ^{-1} \frac{\mathrm{x}}{\sqrt{5}}\right]_1^{\sqrt{5}} \\ & =\frac{1}{3}+\frac{5 \pi}{4}-\frac{5}{2} \sin ^{-1}\left(\frac{1}{\sqrt{5}}\right) \\ & \therefore \text { Required Area }=2 \mathrm{~A}_1 \\ & =\frac{2}{3}+\frac{5 \pi}{2}-5 \sin ^{-1}\left(\frac{1}{\sqrt{5}}\right) \\ & =\frac{2}{3}+5\left(\frac{\pi}{2}-\sin ^{-1} \frac{1}{\sqrt{5}}\right) \\ & =\frac{2}{3}+5 \cos ^{-1} \frac{1}{\sqrt{5}} \\ & =\frac{2}{3}+5 \sin ^{-1}\left(\frac{2}{\sqrt{5}}\right)\end{aligned}$

</details>

---

### Q32. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The area of the region in the first quadrant inside the circle $x^2+y^2=8$ and outside the parabola $y^2=2 x$ is equal to :

**Options:**

- **(A)** $\frac{\pi}{2}-\frac{1}{3}$
- **(B)** $\pi-\frac{1}{3}$
- **(C)** $\frac{\pi}{2}-\frac{2}{3}$
- **(D)** $\pi-\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\pi-\frac{2}{3}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/w6cOjvZpHTfjgYU43ogBZBYj1y3HwYhXP88O0qezktg.original.fullsize.png">
Required area $=\operatorname{Ar}($ circle from 0 to 2$)-$ $\operatorname{ar}($ para from 0 to 2$)$
$\begin{aligned} & =\int_0^2 \sqrt{8-x^2} d x-\int_0^2 \sqrt{2 x} d x \\ & =\left[\frac{x}{2} \sqrt{8-x^2}+\frac{8}{2} \sin ^{-1} \frac{x}{2 \sqrt{2}}\right]_0^2-\sqrt{2}\left[\frac{x \sqrt{x}}{3 / 2}\right]_0^2 \\ & =\frac{2}{2} \sqrt{8-4}+\frac{8}{2} \sin ^{-1} \frac{2}{2 \sqrt{2}}-\frac{2 \sqrt{2}}{3}(2 \sqrt{2}-0) \\ & \Rightarrow 2+4 \cdot \frac{\pi}{4}-\frac{8}{3}=\pi-\frac{2}{3}\end{aligned}$

</details>

---

### Q33. JEE Main 2024 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let the area of the region enclosed by the curve $y=\min \{\sin x, \cos x\}$ and the $x$ axis between $x=-\pi$ to $x=\pi$ be $A$. Then $A^2$ is equal to ___________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

$\begin{aligned} & y=\min \{\sin x, \cos x\} \\ & x-\text { axis } \quad x-\pi \quad x=\pi\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Oqo3JdVvfN2myZndLD0E5i6l8qmPPltKBXrzPrVyzGs.original.fullsize.png">
$\begin{aligned} & \int_0^{\pi / 4} \sin x=(\cos x)_{\pi / 4}^0=1-\frac{1}{\sqrt{2}} \\ & \int_{-\pi}^{-3 \pi / 4}(\sin x-\cos x)=(-\cos x-\sin x)_{-\pi}^{-3 \pi / 4} \\ & =(\cos x+\sin x)_{-3 \pi / 4}^{-\pi} \\ & =(-1+0)-\left(-\frac{1}{\sqrt{2}}-\frac{1}{\sqrt{2}}\right) \\ & =-1+\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{2}} \\ & \int_{\pi / 4}^{\pi / 2} \cos x d x=(\sin x)_{\pi / 4}^{\pi / 2}=1-\frac{1}{\sqrt{2}} \\ & A=4 \\ & A^2=16\end{aligned}$

</details>

---

### Q34. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If the area of the region $\left\{(x, y): \frac{\mathrm{a}}{x^2} \leq y \leq \frac{1}{x}, 1 \leq x \leq 2,0 < \mathrm{a} < 1\right\}$ is $\left(\log _{\mathrm{e}} 2\right)-\frac{1}{7}$ then the value of $7 \mathrm{a}-3$ is equal to:

**Options:**

- **(A)** 0
- **(B)** 2
- **(C)** -1
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) -1**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/waE9ACf4p9b5YuvFIu57YnpiZxKO-xE0OF17PLg86ag.original.fullsize.png">
$\begin{aligned} & \text { area } \int_1^2\left(\frac{1}{x}-\frac{a}{x^2}\right) d x \\ & {\left[\ell n x+\frac{a}{x}\right]_1^2} \\ & \ell \operatorname{nn} 2+\frac{a}{2}-a=\log _e 2-\frac{1}{7} \\ & \frac{-a}{2}=-\frac{1}{7} \\ & a=\frac{2}{7} \\ & 7 a=2 \\ & 7 a-3=-1\end{aligned}$

</details>

---

### Q35. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area enclosed between the curves $y=x|x|$ and $y=x-|x|$ is :

**Options:**

- **(A)** $\frac{4}{3}$
- **(B)** 1
- **(C)** $\frac{2}{3}$
- **(D)** $\frac{8}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{4}{3}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Q0SgqoJPnQR8WxGvDT1OEgc2L1ICPv9Bp2weeeJqSuw.original.fullsize.png">
$A=\int_{-2}^0-x^2-2 x=\frac{4}{3}$

</details>

---

### Q36. JEE Main 2024 (05 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

The area of the region enclosed by the parabolas $y=x^2-5 x$ and $y=7 x-x^2$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **72**

**Detailed Solution:**

$y=x^2-5 x$ and $y=7 x-x^2$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/NLoYceQZxgz9JzxxBKW-lui5ZtYcpDG0Lw4PkYRBFzI.original.fullsize.png">
$\begin{aligned} & \int_0^6(g(x)-f(x)) d x \\ & \int_0^6\left(\left(7 x-x^2\right)-\left(x^2-5 x\right)\right) d x \\ & \int_0^6\left(12 x-2 x^2\right) d x=\left[12 \frac{x^2}{2}-\frac{2 x^3}{3}\right]_0^6 \\ & \Rightarrow 6(6)^2-\frac{2}{3}(6)^3 \\ & =216-144=72 \text { unit }^2 \\ & \end{aligned}$

</details>

---

### Q37. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area (in sq. units) of the region described by $\left\{(x, y): y^2 \leq 2 x\right.$, and $\left.y \geq 4 x-1\right\}$ is

**Options:**

- **(A)** $\frac{11}{32}$
- **(B)** $\frac{8}{9}$
- **(C)** $\frac{11}{12}$
- **(D)** $\frac{9}{32}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{9}{32}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EB4V2moWTRLoV_b6GTurOQk0e8k7KVNlCmLGArngsJ8.original.fullsize.png">
$\begin{aligned} & \text { Shaded area }=\int_{-\frac{1}{2}}^1\left(x_{\text {Right }}-x_{\text {Left }}\right) d y \\ & y^2=2 x \\ & y=4 x-1 \quad \text { Solve } \\ & y=1, y=-\frac{1}{2} \\ & \text { Shaded area }=\int_{-\frac{1}{2}}^1\left(\frac{y+1}{4}-\frac{y^2}{2}\right) d y \\ & =\left(\frac{1}{4}\left(\frac{y^2}{2}+y\right)-\frac{y^3}{6}\right)_{-\frac{1}{2}}^1=\frac{9}{32}\end{aligned}$

</details>

---

### Q38. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

One of the points of intersection of the curves $y=1+3 x-2 x^2$ and $y=\frac{1}{x}$ is $\left(\frac{1}{2}, 2\right)$. Let the area of the region enclosed by these curves be $\frac{1}{24}(l \sqrt{5}+\mathrm{m})-\mathrm{n} \log _{\mathrm{e}}(1+\sqrt{5})$, where $l, \mathrm{~m}, \mathrm{n} \in \mathbf{N}$. Then $l+\mathrm{m}+\mathrm{n}$ is equal to

**Options:**

- **(A)** 29
- **(B)** 31
- **(C)** 30
- **(D)** 32

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 30**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/JxRJet-kMjWZn3iXdSO6nLGmB3QZn6khs7Ov-kYkx5E.original.fullsize.png">
$\begin{aligned} & A=\int_{\frac{1}{2}}^{\frac{1+\sqrt{5}}{2}}\left(1+3 x-2 x^2-\frac{1}{x}\right) \mathrm{dx} \\ & A=\left[x+\frac{3 x^2}{2}-\frac{2 x^3}{3}-\ln x\right]_{\frac{1}{2}}^{1+\sqrt{5}} \\ & A=\frac{1+\sqrt{5}}{2}+\frac{3}{2}\left(\frac{1+\sqrt{5}}{2}\right)^2-\frac{2}{3}\left(\frac{1+\sqrt{5}}{2}\right)^3-\ln \left(\frac{1+\sqrt{5}}{2}\right) \\ & -\frac{1}{2}-\frac{3}{2}\left(\frac{1}{4}\right)+\frac{2}{3}\left(\frac{1}{8}\right)+\ln \left(\frac{1}{2}\right) \\ & A=\frac{1}{2}+\frac{\sqrt{5}}{2}+\frac{3}{8}+\frac{3}{4} \sqrt{5}+\frac{15}{8}-\frac{4}{3}-\frac{2}{3} \sqrt{5} \\ & -\frac{1}{2}-\frac{3}{8}+\frac{1}{12}-\ln (1+\sqrt{5}) \\ & =\sqrt{5}\left(\frac{1}{2}+\frac{3}{4}-\frac{2}{3}\right)+\frac{15}{8}-\frac{4}{3}+\frac{1}{12}-\ln (1+\sqrt{5}) \\ & =\frac{14}{24} \sqrt{5}+\frac{15}{24}-\ln (1+\sqrt{5})\end{aligned}$

</details>

---

### Q39. JEE Main 2024 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>The sum of squares of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math>, for which area of the region bounded by the parabolas <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mi>k</mi><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mfenced><mrow><mi>y</mi><mo>−</mo><mi>x</mi></mrow></mfenced></math> is maximum, is equal to:</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mfenced><mrow><mi>y</mi><mo>−</mo><mi>x</mi></mrow></mfenced><mo>,</mo><mo> </mo><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mi>k</mi><mi>x</mi></math></p><p>Finding the point of intersection,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>k</mi><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mfenced><mrow><mi>y</mi><mo>−</mo><mfrac><mrow><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup></mrow><mi>k</mi></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mi>y</mi><mo>=</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>−</mo><mfrac><mrow><mn>2</mn><mi>y</mi></mrow><mi>k</mi></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>k</mi><mi>y</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi>y</mi></mrow><mi>k</mi></mfrac><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfrac><mn>2</mn><mrow><mi>k</mi><mo>+</mo><mfrac><mn>4</mn><mi>k</mi></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>k</mi></mrow><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfrac></math></p><p>So, the required area is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><munderover><mo>∫</mo><mn>0</mn><mfrac><mrow><mn>2</mn><mi>k</mi></mrow><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfrac></munderover><mfenced><mrow><mfenced><mrow><mi>y</mi><mo>−</mo><mfrac><mrow><mi>k</mi><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>−</mo><mfenced><mfrac><mrow><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup></mrow><mi>k</mi></mfrac></mfenced></mrow></mfenced><mo>⋅</mo><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>−</mo><mfenced><mrow><mfrac><mi>k</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mi>k</mi></mfrac></mrow></mfenced><mo>⋅</mo><mfrac><msup><mi>y</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mn>0</mn><mfrac><mrow><mn>2</mn><mi>k</mi></mrow><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>=</mo><msup><mfenced><mfrac><mrow><mn>2</mn><mi>k</mi></mrow><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfrac></mfenced><mn>2</mn></msup><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>−</mo><mfrac><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow><mrow><mn>2</mn><mi>k</mi></mrow></mfrac><mo>×</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>×</mo><mfrac><mrow><mn>2</mn><mi>k</mi></mrow><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>×</mo><mn>4</mn><mo>×</mo><msup><mfenced><mfrac><mn>1</mn><mrow><mi>k</mi><mo>+</mo><mfrac><mn>4</mn><mi>k</mi></mfrac></mrow></mfrac></mfenced><mn>2</mn></msup></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>M</mi><mo>≥</mo><mi>G</mi><mi>M</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mfenced><mrow><mi>k</mi><mo>+</mo><mfrac><mn>4</mn><mi>k</mi></mfrac></mrow></mfenced><mn>2</mn></mfrac><mo>≥</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>k</mi><mo>+</mo><mfrac><mn>4</mn><mi>k</mi></mfrac><mo>≥</mo><mn>4</mn></math></p><p>So, area is maximum when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mfrac><mn>4</mn><mi>k</mi></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>k</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>−</mo><mn>2</mn></math></p><p>Hence, the sum of squares of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>.</p>

</details>

---

### Q40. JEE Main 2024 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>Three points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo> </mo><mi>P</mi><mfenced><mrow><mi>a</mi><mo>,</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfenced><mo>,</mo><mo> </mo><mi>Q</mi><mfenced><mrow><mo>−</mo><mi>b</mi><mo>,</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced><mo>,</mo><mo> </mo><mi>a</mi><mo>&gt;</mo><mn>0</mn><mo>,</mo><mo> </mo><mi>b</mi><mo>&gt;</mo><mn>0</mn><mo>,</mo></math> are on the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math> be the area of the region bounded by the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> and the parabola, and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> be the area of the triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>P</mi><mi>Q</mi></math>. If the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>S</mi><mn>1</mn></msub><msub><mi>S</mi><mn>2</mn></msub></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>m</mi><mi>n</mi></mfrac><mo>,</mo><mo> </mo><mi>gcd</mi><mfenced><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></mfenced><mo>=</mo><mn>1</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi></math> is equal to:</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

<p>Plotting the diagram of the given data we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b82aa06c-65d1-4f55-b638-d138162fdd72.png" style="width: 350px; height: 267px;"/></p><p>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>△</mo><mi>O</mi><mi>P</mi><mi>Q</mi></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><msup><mi>a</mi><mn>2</mn></msup></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>−</mo><mi>b</mi></mtd><mtd><msup><mi>b</mi><mn>2</mn></msup></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>a</mi><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mi>b</mi></mrow></mfenced><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Now, equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>:</mo><mi>y</mi><mo>−</mo><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>−</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfrac><mfenced><mrow><mi>x</mi><mo>−</mo><mi>a</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>−</mo><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mfenced><mrow><mi>a</mi><mo>−</mo><mi>b</mi></mrow></mfenced><mi>x</mi><mo>−</mo><mfenced><mrow><mi>a</mi><mo>−</mo><mi>b</mi></mrow></mfenced><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfenced><mrow><mi>a</mi><mo>−</mo><mi>b</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mi>a</mi><mi>b</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Area bounded by the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> and the parabola is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><munderover><mo>∫</mo><mrow><mo>−</mo><mi>b</mi></mrow><mi>a</mi></munderover><mfenced><mrow><mfenced><mrow><mi>a</mi><mo>−</mo><mi>b</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mi>a</mi><mi>b</mi><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfenced><mrow><mi>a</mi><mo>−</mo><mi>b</mi></mrow></mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfenced><mrow><mi>a</mi><mi>b</mi></mrow></mfenced><mi>x</mi><mo>−</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mrow><mo>−</mo><mi>b</mi></mrow><mi>a</mi></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><msup><mfenced><mrow><mi>a</mi><mo>−</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>+</mo><mi>a</mi><mi>b</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mo>−</mo><mfrac><mfenced><mrow><msup><mi>a</mi><mn>3</mn></msup><mo>+</mo><msup><mi>b</mi><mn>3</mn></msup></mrow></mfenced><mn>3</mn></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><msub><mi>S</mi><mn>1</mn></msub><msub><mi>S</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mfrac><msup><mfenced><mrow><mi>a</mi><mo>−</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mi>a</mi><mi>b</mi><mo>−</mo><mfrac><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>−</mo><mi>a</mi><mi>b</mi></mrow></mfenced><mn>3</mn></mfrac></mrow><mfrac><mrow><mi>a</mi><mi>b</mi></mrow><mn>2</mn></mfrac></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><msub><mi>S</mi><mn>1</mn></msub><msub><mi>S</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><msup><mfenced><mrow><mi>a</mi><mo>−</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>a</mi><mi>b</mi><mo>−</mo><mn>2</mn><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>−</mo><mi>a</mi><mi>b</mi></mrow></mfenced></mrow><mrow><mn>3</mn><mi>a</mi><mi>b</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><msub><mi>S</mi><mn>1</mn></msub><msub><mi>S</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>a</mi><mi>b</mi></mrow></mfenced><mo>+</mo><mn>6</mn><mi>a</mi><mi>b</mi><mo>−</mo><mn>2</mn><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>−</mo><mi>a</mi><mi>b</mi></mrow></mfenced></mrow><mrow><mn>3</mn><mi>a</mi><mi>b</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><msub><mi>S</mi><mn>1</mn></msub><msub><mi>S</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>a</mi><mi>b</mi><mo>+</mo><mn>6</mn><mi>a</mi><mi>b</mi><mo>-</mo><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>a</mi><mi>b</mi></mrow><mrow><mn>3</mn><mi>a</mi><mi>b</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><msub><mi>S</mi><mn>1</mn></msub><msub><mi>S</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>a</mi><mi>b</mi></mrow><mrow><mn>3</mn><mi>a</mi><mi>b</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><msub><mi>S</mi><mn>1</mn></msub><msub><mi>S</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mi>a</mi><mi>b</mi></mfrac><mo>+</mo><mfrac><mi>b</mi><mi>a</mi></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mfenced><mfrac><msub><mi>S</mi><mn>1</mn></msub><msub><mi>S</mi><mn>2</mn></msub></mfrac></mfenced><mi>min</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><mfrac><mi>a</mi><mi>b</mi></mfrac><mo>+</mo><mfrac><mi>b</mi><mi>a</mi></mfrac><mo>≥</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mfenced><mfrac><msub><mi>S</mi><mn>1</mn></msub><msub><mi>S</mi><mn>2</mn></msub></mfrac></mfenced><mi>min</mi></msub><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>7</mn></math></p>

</details>

---

### Q41. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region enclosed by the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>4</mn><mi>x</mi><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>y</mi><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>−</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>32</mn><mn>9</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>14</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>4</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo> </mo><mtext>and</mtext><mo> </mo><mn>3</mn><mi>y</mi><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mfrac><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>12</mn><mi>x</mi><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><mo>-</mo><mn>8</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>20</mn><mi>x</mi><mo>+</mo><mn>16</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo> </mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><mn>3</mn></math></p><p>So, the intersection points are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2b25f3b7-8514-49aa-b022-e9f96770aab7.png" style="width: 300px; height: 222px;"/></p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>∫</mo><mn>1</mn><mn>4</mn></msubsup><mfenced close="]" open="["><mrow><mfenced><mrow><mn>4</mn><mi>x</mi><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>−</mo><mfrac><msup><mfenced><mrow><mi>x</mi><mo>−</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="|" open="|"><mrow><mfrac><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>−</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>−</mo><mfrac><msup><mfenced><mrow><mi>x</mi><mo>−</mo><mn>4</mn></mrow></mfenced><mn>3</mn></msup><mn>9</mn></mfrac></mrow></mfenced><mn>1</mn><mn>4</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mfenced><mrow><mfrac><mn>64</mn><mn>2</mn></mfrac><mo>−</mo><mfrac><mn>64</mn><mn>3</mn></mfrac><mo>−</mo><mfrac><mn>4</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>−</mo><mfrac><mn>27</mn><mn>9</mn></mfrac></mrow></mfenced></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>27</mn><mo>−</mo><mn>21</mn></mrow></mfenced><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q42. JEE Main 2024 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

The area of the region enclosed by the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>y</mi><mo>-</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mi>x</mi><mo>-</mo><mn>1</mn></math>, the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mo> </mo><mi>y</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> and the positive coordinate axes is __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>y</mi><mo>-</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mi>x</mi><mo>-</mo><mn>1</mn><mtext> and </mtext><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p>Now, plotting the graph of the above equation, we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/63f31ba1-d18e-406d-bfff-fbfd873431ba.png" style="width: 368px; height: 251px;"/></p><p>Now, from above diagram we get,</p><p>Required area  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mn>3</mn></msubsup><mi>x</mi><mi>d</mi><mi>y</mi><mo>-</mo></math> Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Δ</mi><mi>A</mi><mi>B</mi><mi>C</mi></math>.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mn>3</mn></msubsup><mfenced><mrow><mo>(</mo><mi>y</mi><mo>-</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>y</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>×</mo><mn>1</mn><mo>×</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mn>3</mn></msubsup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mi>d</mi><mi>y</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>y</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>y</mi></mrow></mfenced><mn>0</mn><mn>3</mn></msubsup><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>-</mo><mn>18</mn><mo>+</mo><mn>15</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q43. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The area (in square units) of the region bounded by the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo></math> and the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>8</mn></math>.

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>**

**Detailed Solution:**

<p>Given curve is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math> and line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>8</mn></math></p><p>Finding the point of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>x</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>8</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn></mstyle><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>16</mn><mo>=</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>6</mn><mo>,</mo><mn>3</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4bcc8f87-2e3b-4b16-8c89-38867954f43b.png" style="width: 400px; height: 256px;"/></p><p>Area of the bounded region is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>4</mn></msubsup><mfenced><mrow><mfrac><mrow><mi>y</mi><mo>+</mo><mn>8</mn></mrow><mn>2</mn></mfrac><mo>-</mo><mfenced><mrow><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mfrac><msup><mi>y</mi><mn>3</mn></msup><mn>12</mn></mfrac></mrow></mfenced><mrow><mo>-</mo><mn>2</mn></mrow><mn>4</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>=</mo><mn>4</mn><mo>+</mo><mn>8</mn><mo>-</mo><mfrac><mn>16</mn><mn>3</mn></mfrac><mo>-</mo><mn>1</mn><mo>+</mo><mn>4</mn><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>=</mo><mn>9</mn><mo> </mo><mi>sq</mi><mo>.</mo><mo> </mo><mi>units</mi></math>.</p>

</details>

---

### Q44. JEE Main 2024 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

The area (in sq. units) of the part of circle <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>169</mn></math> which is below the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>13</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>π</mi><mi>α</mi></mrow><mrow><mn>2</mn><mi>β</mi></mrow></mfrac><mo>-</mo><mfrac><mn>65</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>α</mi><mi>β</mi></mfrac><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>12</mn><mn>13</mn></mfrac></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>,</mo><mi>β</mi></math> are coprime numbers. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>+</mo><mi>β</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **171**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>169</mn><mo>,</mo><mo> </mo><mn>5</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>13</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>5</mn><mi>x</mi><mo>-</mo><mn>13</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>169</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>25</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>169</mn><mo>-</mo><mn>130</mn><mi>x</mi><mo>-</mo><mn>169</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>26</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>130</mn><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>13</mn><mo>,</mo><mo> </mo><mn>12</mn></math></p><p>So, the points of intersection are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mn>13</mn></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>12</mn></mrow></mfenced></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7c2a25f8-2af4-4c12-890f-d36aefb3bfe0.png" style="width: 375px; height: 258px;"/></p><p>So, the required area is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mn>13</mn></mrow><mn>12</mn></msubsup><msqrt><mn>169</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mi>dy</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>×</mo><mn>25</mn><mo>×</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><msqrt><mn>169</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mfrac><mn>169</mn><mn>2</mn></mfrac><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>x</mi><mn>13</mn></mfrac></mrow></mfenced><mrow><mo>-</mo><mn>13</mn></mrow><mn>12</mn></msubsup><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>×</mo><mn>25</mn><mo>×</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>=</mo><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>×</mo><mfrac><mn>169</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>65</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>169</mn><mn>2</mn></mfrac><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>12</mn><mn>13</mn></mfrac></math></p><p>Hence, on comparing with given value we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mn>169</mn><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>+</mo><mi>β</mi><mo>=</mo><mn>171</mn></math></p>

</details>

---

### Q45. JEE Main 2024 (27 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let the area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>:</mo><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>4</mn><mo>≥</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open=""><mrow><mi>x</mi><mo>+</mo><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>≥</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>+</mo><mn>4</mn><msup><mi>y</mi><mn>2</mn></msup><mo>≤</mo><mn>8</mn><mo>,</mo><mi>y</mi><mo>≥</mo><mn>0</mn></mrow></mfenced></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>m</mi><mi>n</mi></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> are coprime numbers. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi><mo>+</mo><mi mathvariant="normal">n</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **119**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>4</mn><mo>≥</mo><mn>0</mn><mo>,</mo><mo> </mo><mi>x</mi><mo>+</mo><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>≥</mo><mn>0</mn><mo>,</mo><mo> </mo><mi>x</mi><mo>+</mo><mn>4</mn><msup><mi>y</mi><mn>2</mn></msup><mo>≤</mo><mn>8</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>≥</mo><mn>0</mn></math></p><p>Now, finding the point of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mi>x</mi><mo>+</mo><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>≡</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>And point of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mi>x</mi><mo>+</mo><mn>4</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn></math> will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>≡</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Now, plotting the diagramw we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a9bb1e5c-73a3-4182-ae5a-5161f50d003e.png" style="width: 500px; height: 275px;"/></p><p>Now, from the above diagram, the required area will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msubsup><mfenced><mrow><mfrac><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mn>2</mn></mfrac><mo>-</mo><msqrt><mfrac><mrow><mo>-</mo><mi>x</mi></mrow><mn>2</mn></mfrac></msqrt></mrow></mfenced><mo>+</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><mfenced><mrow><mfrac><msqrt><mn>8</mn><mo>-</mo><mi>x</mi></msqrt><mn>2</mn></mfrac><mo>-</mo><msqrt><mfrac><mrow><mo>-</mo><mi>x</mi></mrow><mn>2</mn></mfrac></msqrt></mrow></mfenced><mo>d</mo><mi>x</mi><mo>+</mo><msubsup><mo>∫</mo><mn>0</mn><mn>8</mn></msubsup><mfrac><msqrt><mn>8</mn><mo>-</mo><mi>x</mi></msqrt><mn>2</mn></mfrac><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mfenced close="]" open="["><mfrac><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msubsup><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msubsup><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mfenced><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></mfenced></mrow></mfenced><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msubsup><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mn>8</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mfenced><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></mfenced></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msubsup><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mfenced><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></mfenced></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mn>8</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mfenced><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></mfenced></mrow></mfenced><mn>0</mn><mn>8</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>=</mo><mn>9</mn><mo>+</mo><mfrac><mn>5</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>=</mo><mfrac><mn>107</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>119</mn></math></p>

</details>

---

### Q46. JEE Main 2023 (15 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

If the area bounded by the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mi>x</mi></math>, lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>0</mn></math> and outside the circle <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></math> is A, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mfenced><mrow><mi>&#960;</mi><mo>+</mo><mo>&#160;</mo><mn>4</mn><mi>A</mi></mrow></mfenced></math> is equal to __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **42**

**Detailed Solution:**

<blockquote><p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn><mfenced><mrow><mi>slope</mi><mo>&#160;</mo><mi>is</mi><mo>&#160;</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></math></p><p>Now plotting the diagram of the above function we have,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/06ea0618-e2a8-4ac5-beca-50d39fc57fb9.png" style="width: 300px; height: 273px;" /></p><p>So, required area is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>3</mn><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>3</mn><mo>-</mo><mi>y</mi><mo>-</mo><mfrac><mrow><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>3</mn></mfrac></mrow></mfenced><mi>d</mi><mi>y</mi><mo>-</mo><mfrac><mrow><mi mathvariant="normal">&#960;</mi><msup><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mn>2</mn></msup><mo>&#215;</mo><msup><mn>45</mn><mo>&#176;</mo></msup></mrow><msup><mn>360</mn><mo>&#176;</mo></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mn>3</mn><mi>y</mi><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mn>0</mn><mfrac><mn>3</mn><mn>2</mn></mfrac></msubsup><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msubsup><mfenced close="]" open="["><mfrac><msup><mi>y</mi><mn>3</mn></msup><mn>3</mn></mfrac></mfenced><mn>0</mn><mfrac><mn>3</mn><mn>2</mn></mfrac></msubsup><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><mn>21</mn><mn>8</mn></mfrac><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><mfrac><mn>21</mn><mn>2</mn></mfrac><mo>-</mo><mi mathvariant="normal">&#960;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">&#960;</mi><mo>+</mo><mn>4</mn><mi>A</mi><mo>=</mo><mfrac><mn>21</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>+</mo><mn>4</mn><mi>A</mi></mrow></mfenced><mo>=</mo><mn>42</mn></math></p></blockquote>

</details>

---

### Q47. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mi>y</mi><mo>:</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mi>y</mi><mo>&#8805;</mo><mn>1</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>(</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>(</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>(</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>(</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>(</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn><mo>)</mo></math>**

**Detailed Solution:**

<blockquote><p>The required diagram is:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7ba84c44-95ca-4a9b-aefa-24a3f98eb32c.png" style="width: 300px; height: 226px;" /></p><p>The shaded region is symmetric about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo></math>axis.</p><p>Required area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><msqrt><mi>y</mi></msqrt><mi>d</mi><mi>y</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>4</mn></msubsup><msqrt><mn>4</mn><mo>-</mo><mi>y</mi></msqrt><mi>d</mi><mi>y</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mfrac><msup><mi>y</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mfrac><mn>3</mn><mn>2</mn></mfrac></mfrac></mfenced><mn>1</mn><mn>2</mn></msubsup><mo>-</mo><msubsup><mfenced close="]" open="["><mfrac><mrow><mn>2</mn><mo>(</mo><mn>4</mn><mo>-</mo><mi>y</mi><msup><mo>)</mo><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><mn>3</mn></mfrac></mfenced><mn>2</mn><mn>4</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>(</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn><mo>)</mo></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q48. JEE Main 2023 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region enclosed by the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup></math> and its tangent at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>&#8211;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#8211;</mo><mn>1</mn><mo>)</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>23</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>31</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>27</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>27</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn></mrow></mfenced></msub><mo>=</mo><mn>3</mn></math></p><p>Equation of tangent at <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>&#8211;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#8211;</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>y</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>3</mn><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>&#160;</mo><mo>(</mo><mi>ii</mi><mo>)</mo></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>3</mn></msup><mo>=</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn></math></p><p>Another point of intersection is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>(</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn><mo>)</mo></math></p><p>So, now plotting the diagram we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9c83caf9-e706-4ce9-9047-ac9a5f324688.png" style="width: 314px; height: 237px;" /></p><p>Required area from the above diagram will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></msubsup><mfenced><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mfenced><mrow><mn>4</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><mn>16</mn><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>27</mn><mn>4</mn></mfrac></math></p><p>Hence this is the required option.</p>

</details>

---

### Q49. JEE Main 2023 (11 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is the area in the first quadrant enclosed by the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>:</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>y</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>, the tangent to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math> and the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mi>A</mi></math> is................

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></math></p><p>Now tangent to above equation at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>4</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>1</mn></math></p><p>Now plotting the diagram we get,
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/53322922-5fbf-4b5c-a785-a38019933fae.png" style="width: 350px; height: 329px;" />
Required area of bounded region will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>-</mo><mtext>area&#160;of</mtext><mo>&#160;</mo><mo>&#9651;</mo><mi>Q</mi><mi>O</mi><mi>T</mi><mo>&#160;</mo><mo>-</mo><mtext>area&#160;of</mtext><mo>&#160;</mo><mo>&#9651;</mo><mi>P</mi><mi>Q</mi><mi>R</mi><mo>&#160;</mo><mo>+</mo><mtext>area&#160;of</mtext><mo>&#160;</mo><mo>&#9651;</mo><mi>Q</mi><mi>R</mi><mi>S</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfenced><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>9</mn><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>9</mn><mn>40</mn></mfrac><mo>=</mo><mfrac><mn>16</mn><mn>40</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>60</mn><mi>A</mi><mo>=</mo><mn>16</mn></math></p>

</details>

---

### Q50. JEE Main 2023 (11 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>&#8804;</mo><mn>4</mn><mo>,</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8805;</mo><mn>2</mn><mi>y</mi></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>+</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#960;</mi><mo>+</mo><mfrac><mn>16</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>-</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#960;</mi><mo>-</mo><mfrac><mn>16</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#960;</mi><mo>-</mo><mfrac><mn>16</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>&#8804;</mo><mn>4</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8805;</mo><mn>2</mn><mi>y</mi></math></p><p>Now on solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>y</mi></math> we get intersecting point of the curves as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#177;</mo><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math>,</p><p>Now plotting the diagram we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9bd57b61-d058-4515-8af2-fcd621dfe142-image.png" style="width: 300px; height: 207px;" /></p><p>So, from above diagram area of required region will be,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><mi>&#960;</mi><mo>&#215;</mo><msup><mn>2</mn><mn>2</mn></msup></mrow></mfenced><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><msqrt><mn>2</mn></msqrt><mo>&#183;</mo><msqrt><mi>y</mi></msqrt><mi>d</mi><mi>y</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><mi>&#960;</mi><mo>&#8722;</mo><msubsup><mfenced close="]" open="["><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>&#8901;</mo><msup><mi>y</mi><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></msup></mrow><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></mfrac></mfenced><mn>0</mn><mn>2</mn></msubsup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><mi>&#960;</mi><mo>-</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac><mo>&#183;</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><mi>&#960;</mi><mo>-</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>&#960;</mi><mo>-</mo><mfrac><mn>16</mn><mn>3</mn></mfrac></math></p></blockquote>

</details>

---

### Q51. JEE Main 2023 (10 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

If the area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mi>x</mi></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>A</mi><mo>+</mo><mn>16</mn><msqrt><mn>2</mn></msqrt></math> is equal to ______________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **27**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>&#8804;</mo><mi>y</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>&#8804;</mo><mi>x</mi></math></p><p>Now on finding the intersection point we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8801;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>Now plotting the curve of the above function we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2f60ecd7-918c-4d46-bb3d-88e6e1bfae54.png" style="width: 250px; height: 232px;" /></p><p>Now from above diagram required bounded area will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mfenced close="]" open="["><mrow><msubsup><mo>&#8747;</mo><mn>1</mn><msqrt><mn>2</mn></msqrt></msubsup><mfenced><mrow><mi>x</mi><mo>-</mo><mfenced><mrow><mn>2</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><msqrt><mn>2</mn></msqrt><mn>2</mn></msubsup><mfenced><mrow><mi>x</mi><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mn>1</mn><msqrt><mn>2</mn></msqrt></msubsup><mo>+</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><msqrt><mn>2</mn></msqrt><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>-</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>+</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">A</mi><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi mathvariant="normal">A</mi><mo>=</mo><mn>27</mn><mo>-</mo><mn>16</mn><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>6</mn><mi mathvariant="normal">A</mi><mo>+</mo><mn>16</mn><msqrt><mn>2</mn></msqrt><mo>=</mo><mn>27</mn></math></p></blockquote>

</details>

---

### Q52. JEE Main 2023 (10 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>p</mi><mfenced><mi>x</mi></mfenced></math> be the parabola passing through the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8211;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math>. If the area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>:</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>&#8804;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8804;</mo><mi>p</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mn>4</mn><mi>A</mi></mrow></mfenced></math> is equal to ________ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<blockquote><p>Let, the parabola be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></math>,</p><p>Now given parabola is passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>Now putting the value in the above equation of parabola we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>Now solving above three equations we get,</p><p>Parabola as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p>Now area of region between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>&#8804;</mo><mn>1</mn></math> is given by,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5f6a2e8d-9d16-4fee-bdda-5b832bc2d93b.png" style="width: 350px; height: 251px;" /></p><p>Now from above diagram, required area will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><mfenced><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></msqrt></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>(</mo><mi>&#960;</mi><mo>-</mo><mn>4</mn><mi>A</mi><mo>)</mo><mo>=</mo><mn>16</mn></math></p></blockquote>

</details>

---

### Q53. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mn>8</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo><mi>y</mi><mo>&#8804;</mo><mn>7</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>**

**Detailed Solution:**

<blockquote><p>The given curves are <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8804;</mo><mn>8</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>y</mi><mo>&#8804;</mo><mn>7</mn></math></p><p>The point of intersection of the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mi>y</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>y</mi><mo>&#8804;</mo><mn>8</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></math> is obtained by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>&#177;</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>4</mn></math>.</p><p>Hence the points are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>.</p><p>The points of intersection of the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8804;</mo><mn>8</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>y</mi><mo>&#8804;</mo><mn>7</mn></math> is obtained by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>7</mn></math></p><p>Hence the points are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math>.</p><p>The required graph is </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1559b7c7-dafd-416a-b28a-b9f5dd5efd48-9925356.png" style="width: 400px; height: 354px;" /></p><p>The required area is symmetrical about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo></math>axis.</p><p>Hence required area is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>4</mn></msubsup><msqrt><mi>y</mi></msqrt><mo>d</mo><mi>y</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>4</mn><mn>7</mn></msubsup><msqrt><mn>8</mn><mo>-</mo><mi>y</mi></msqrt><mo>d</mo><mi>y</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><msubsup><mfenced close="]" open="["><mfrac><msup><mi>y</mi><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></msup><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></mfrac></mfenced><mn>0</mn><mn>4</mn></msubsup><mo>-</mo><msubsup><mfenced close="]" open="["><mfrac><msup><mfenced><mrow><mn>8</mn><mo>-</mo><mi>y</mi><mo>&#160;</mo></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></msup><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></mfrac></mfenced><mn>4</mn><mn>7</mn></msubsup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mfenced close="]" open="["><mrow><msup><mfenced><mn>4</mn></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mfenced><mn>0</mn></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>-</mo><mfenced close="}" open="{"><mrow><msup><mfenced><mrow><mn>8</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mfenced><mrow><mn>8</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mfenced><mrow><mn>8</mn><mo>-</mo><mn>0</mn><mo>-</mo><mn>1</mn><mo>+</mo><mn>8</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>20</mn></math> sq units.</p><p>Hence, the required area is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> sq units.</p></blockquote>

</details>

---

### Q54. JEE Main 2023 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

If the area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo mathvariant="italic">=</mo><mfenced close="}" open="{"><mrow><mo mathvariant="italic">(</mo><mi>x</mi><mo mathvariant="italic">,</mo><mi>y</mi><mo mathvariant="italic">)</mo><mo mathvariant="italic">:</mo><mn>2</mn><mi>y</mi><mo mathvariant="italic">-</mo><msup><mi>y</mi><mn>2</mn></msup><mo mathvariant="italic">&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo mathvariant="italic">&#8804;</mo><mn>2</mn><mi>y</mi><mo mathvariant="italic">,</mo><mi>x</mi><mo mathvariant="italic">&#8805;</mo><mi>y</mi></mrow></mfenced></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo mathvariant="italic">-</mo><mfrac><mi>&#960;</mi><mrow><mi>n</mi><mo mathvariant="italic">-</mo><mn>1</mn></mrow></mfrac><mo mathvariant="italic">,</mo></math> then the natural number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo mathvariant="italic">=</mo><mfenced close="}" open="{"><mrow><mo mathvariant="italic">(</mo><mi>x</mi><mo mathvariant="italic">,</mo><mi>y</mi><mo mathvariant="italic">)</mo><mo mathvariant="italic">:</mo><mn>2</mn><mi>y</mi><mo mathvariant="italic">-</mo><msup><mi>y</mi><mn>2</mn></msup><mo mathvariant="italic">&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo mathvariant="italic">&#8804;</mo><mn>2</mn><mi>y</mi><mo mathvariant="italic">,</mo><mi>x</mi><mo mathvariant="italic">&#8805;</mo><mi>y</mi></mrow></mfenced></math>,</p><p>Now plotting the diagram, we get</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7f7f282d-8627-44b1-bf10-4207f4d53963-image.png" style="width: 300px; height: 206px;" /></p><p>Now from above diagram, given region are,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>2</mn><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mi>y</mi></math></p><p>Now the intersecting point of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mi>y</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>y</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mi>y</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>So, required area will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><msubsup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>6</mn></mfrac></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>+</mo><msubsup><mfenced><mrow><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>6</mn></mfrac></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><mn>7</mn><mn>6</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p>So, on comparing we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q55. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mi>x</mi><mi>y</mi><mo>&#8804;</mo><mn>8</mn><mo>,</mo><mn>1</mn><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>-</mo><mfrac><mn>13</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>-</mo><mfrac><mn>14</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>+</mo><mfrac><mn>7</mn><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>&#160;</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn><mo>+</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>-</mo><mfrac><mn>14</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mo>&#8804;</mo><mn>8</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>1</mn><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p>On solving above curve we get intersecting point as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>Now on plotting the diagram of the given curves we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6d9b522a-6fb5-47f7-b02d-c0186ce2e87b-9889862.png" style="width: 400px; height: 208px;" /></p><p>Required area</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>8</mn></msubsup><mfenced><mrow><mfrac><mn>8</mn><mi>x</mi></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>8</mn></msubsup><mfrac><mn>8</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>8</mn></msubsup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mfenced><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><mn>8</mn><msubsup><mfenced close="]" open="["><mrow><mi>ln</mi><mi>x</mi></mrow></mfenced><mn>2</mn><mn>8</mn></msubsup><mo>-</mo><msubsup><mfenced close="]" open="["><mi>x</mi></mfenced><mn>1</mn><mn>8</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mn>8</mn><mi>ln</mi><mn>4</mn><mo>-</mo><mfrac><mn>14</mn><mn>3</mn></mfrac></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mn>16</mn><mi>ln</mi><mn>2</mn><mo>-</mo><mfrac><mn>14</mn><mn>3</mn></mfrac></math> sq. units</p>

</details>

---

### Q56. JEE Main 2023 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let the area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mfenced close="|" open="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mo>,</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn></mrow></mfenced></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>6</mn><mi>A</mi><mo>+</mo><mn>11</mn></mrow></mfenced><mn>2</mn></msup></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **125**

**Detailed Solution:**

<p>Given,</p><p>The area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mfenced close="|" open="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mo>,</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn></mrow></mfenced></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>,</p><p>Now solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>&#177;</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p>And equating <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mo>&#177;</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p>Now plotting the diagram of  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8805;</mo><mfenced close="|" open="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8804;</mo><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced></math>,</p><p> </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cd08dde2-203a-4bff-bc6a-8b883674ddef-9896425.png" style="width: 400px; height: 349px;" /></p><p> </p><p>Now from diagram, both curve are symmetric about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Hence, area of the bounded region is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="|" close="|"><mrow><mn>2</mn><msubsup><mo>&#8747;</mo><mfrac><mrow><mn>3</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfenced><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfenced open="|" close="|"><mrow><mn>2</mn><msubsup><mo>&#8747;</mo><mfrac><mrow><mn>3</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfenced><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfenced open="|" close="|"><mrow><mn>2</mn><msubsup><mfenced><mrow><mfrac><mrow><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mfrac><mrow><mn>3</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><mrow><mn>5</mn><msqrt><mn>5</mn></msqrt><mo>-</mo><mn>11</mn></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi>A</mi><mo>+</mo><mn>11</mn><mo>=</mo><mn>5</mn><msqrt><mn>5</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>6</mn><mi>A</mi><mo>+</mo><mn>11</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>125</mn></math>.</p>

</details>

---

### Q57. JEE Main 2023 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be the area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>:</mo><mi>y</mi><mo>&#8805;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8805;</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8804;</mo><mn>2</mn><mi>x</mi><mo>(</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>)</mo></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>540</mn><mi>A</mi></math> is equal to</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be the area of the region</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>:</mo><mi>y</mi><mo>&#8805;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo><mi>y</mi><mo>&#8805;</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup><mo>,</mo><mi>y</mi><mo>&#8804;</mo><mn>2</mn><mi>x</mi><mo>(</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>)</mo></mrow></mfenced></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>And solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>Now on plotting the diagram of the above region we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b5210be6-68c5-4a37-9ddf-7e9c63368b21-9896001.png" style="width: 500px; height: 437px;" /></p><p>Now from the above diagram area of the shaded region will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfrac><mn>2</mn><mn>3</mn></mfrac></msubsup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>-</mo><mfenced close="}" open="{"><mrow><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfrac><mn>2</mn><mn>3</mn></mfrac></msubsup><msup><mi>x</mi><mn>2</mn></msup><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac><mfrac><mn>2</mn><mn>3</mn></mfrac></msubsup><mo>-</mo><mfenced close="}" open="{"><mrow><msubsup><mfenced close="]" open="["><mfrac><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup><mn>3</mn></mfrac></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mo>+</mo><msubsup><mfenced close="]" open="["><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac><mfrac><mn>2</mn><mn>3</mn></mfrac></msubsup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><mn>5</mn><mn>108</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>A</mi><mo>=</mo><mfrac><mn>5</mn><mn>108</mn></mfrac><mo>&#8658;</mo><mn>540</mn><mo>&#160;</mo><mi>A</mi><mo>=</mo><mfrac><mn>5</mn><mn>108</mn></mfrac><mo>&#215;</mo><mn>540</mn><mo>=</mo><mn>25</mn></math></p>

</details>

---

### Q58. JEE Main 2023 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> be the maximum integral value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mn>10</mn></mrow></mfenced></math> for which the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>p</mi><mi>x</mi><mo>+</mo><mfrac><mn>5</mn><mn>4</mn></mfrac><mi>p</mi><mo>=</mo><mn>0</mn></math> are rational. Then the area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mn>0</mn><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mo>(</mo><mi>x</mi><mo>-</mo><mi>q</mi><msup><mo>)</mo><mn>2</mn></msup><mo>,</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mi>q</mi></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>243</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>125</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>164</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>243</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>p</mi><mi>x</mi><mo>+</mo><mfrac><mrow><mn>5</mn><mi>p</mi></mrow><mn>4</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p>For rational roots, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> must be a perfect square.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><msup><mi>p</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>p</mi><mo>=</mo><mi>p</mi><mfenced><mrow><mi>p</mi><mo>-</mo><mn>5</mn></mrow></mfenced></math></p><p>Now put values in reverse order as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> is the maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>10</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mn>50</mn><mo>&#8594;</mo><mtext>not&#160;a&#160;perfect&#160;square</mtext></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>9</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mn>36</mn><mo>&#8594;</mo><mtext>perfect&#160;square</mtext></math></p><p>So, the maximum integral value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>q</mi><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>9</mn></mrow></mfenced><mn>2</mn></msup></math></p><p> </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/37c1b0b7-0d80-4db8-9f2a-2fcb835972f4-9896074.png" style="width: 400px; height: 345px;" /></p><p>Area of shaded region <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>9</mn></msubsup><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>9</mn></mrow></mfenced><mn>2</mn></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced open="[" close="]"><mfrac><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>9</mn></mrow></mfenced><mn>3</mn></msup><mn>3</mn></mfrac></mfenced><mn>0</mn><mn>9</mn></msubsup><mo>=</mo><mn>243</mn><mo>&#160;</mo><msup><mtext>unit</mtext><mn>2</mn></msup></math></p>

</details>

---

### Q59. JEE Main 2023 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> be the area of the larger region bounded by the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi></math> and the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>, which lies in the first quadrant. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>&#945;</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **22**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>x</mi></math></p><p>Point of intersection of curve and a line is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>8</mn><mo>,</mo><mn>8</mn></mrow></mfenced></math>.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fb056749-aed9-4d50-b0ca-7e3c962209ac-9887686.png" style="width: 300px; height: 259px;" /></p><p>Required area</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>8</mn></msubsup><mfenced><mrow><msqrt><mn>8</mn><mi>x</mi></msqrt><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><msubsup><mfenced open="[" close="]"><mrow><mfrac><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt><msup><mi>x</mi><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn><mn>8</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfenced open="[" close="]"><mrow><mfenced><mrow><mfrac><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt><msup><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>3</mn></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>64</mn><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt><msup><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mn>3</mn></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>4</mn><mn>2</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>112</mn><mn>3</mn></mfrac><mo>-</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>22</mn><mn>3</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>&#945;</mi><mo>=</mo><mn>22</mn></math></p>

</details>

---

### Q60. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mfenced close="|" open="|"><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mi>sin</mi><mi>x</mi><mo>,</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfrac><mn>3</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mfrac><mn>4</mn><msqrt><mn>5</mn></msqrt></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>5</mn></msqrt><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>4</mn><mo>.</mo><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><msqrt><mn>5</mn></msqrt></mfrac><mo>-</mo><mfrac><mn>3</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>5</mn></msqrt><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>5</mn></msqrt><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Given,<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>cos</mi><mo>&#160;</mo><mi>x</mi><mo>-</mo><mi>sin</mi><mo>&#160;</mo><mi>x</mi></mrow></mfenced><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mi>sin</mi><mo>&#160;</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#10877;</mo><mi>x</mi><mo>&#10877;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math></p><p>For intersection point:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mi>sin</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#968;</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mo>&#160;</mo><mi>&#968;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mspace linebreak="newline"/><mi>sin</mi><mo>&#160;</mo><mi>&#968;</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac><mspace linebreak="newline"/><mi>cos</mi><mo>&#160;</mo><mi>&#968;</mi><mo>=</mo><mfrac><mn>2</mn><msqrt><mn>5</mn></msqrt></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e660f201-d6c8-4009-bc35-0436219615be-9895256.png" style="width: 300px; height: 251px;" /></p><p>Required area is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mi>&#968;</mi><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mfenced open="|" close="|"><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mi>&#968;</mi><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></msubsup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mi>y</mi><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></msubsup><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mo>(</mo><mi>cos</mi><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced open="[" close="]"><mrow><mo>-</mo><mn>2</mn><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mi>&#968;</mi><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></msubsup><mo>+</mo><msubsup><mfenced open="[" close="]"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mn>2</mn><mi>cos</mi><mi>&#968;</mi><mo>+</mo><mi>sin</mi><mi>&#968;</mi><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><mfrac><mn>2</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mn>2</mn><mfenced><mfrac><mn>2</mn><msqrt><mn>5</mn></msqrt></mfrac></mfenced><mo>+</mo><mfenced><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mfrac><mn>5</mn><msqrt><mn>5</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><msqrt><mn>5</mn></msqrt><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></math> sq. units</p>

</details>

---

### Q61. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#916;</mi></math> be the area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><msup><mi mathvariant="normal">&#8477;</mi><mn>2</mn></msup><mo>:</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>21</mn><mo>,</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>4</mn><mi>x</mi><mo>,</mo><mi>x</mi><mo>&#8805;</mo><mn>1</mn></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi mathvariant="normal">&#916;</mi><mo>-</mo><mn>21</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>2</mn><msqrt><mn>7</mn></msqrt></mfrac></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Plotting the diagram of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>21</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>4</mn><mi>x</mi></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>1</mn></math> we get,</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5bb76340-8db7-40ea-98a3-d6ab4df070b7-1bcdf55b-8f93-4d0f-835b-84fe45a09346-9886959.png" style="width: 265px; height: 250px;" /></p><p>Now from above diagram required Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#916;</mi><mo>=</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msubsup><mo>&#8747;</mo><mn>1</mn><mn>3</mn></msubsup><mn>2</mn><msqrt><mi>x</mi></msqrt><mi>d</mi><mi>x</mi><mo>+</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>3</mn><msqrt><mn>21</mn></msqrt></msubsup><msqrt><mn>21</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">&#916;</mi><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mfenced><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>21</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>2</mn><msqrt><mn>7</mn></msqrt></mfrac></mfenced><mo>-</mo><mn>6</mn><msqrt><mn>3</mn></msqrt></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi mathvariant="normal">&#916;</mi><mo>-</mo><mn>21</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>2</mn><msqrt><mn>7</mn></msqrt></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfrac><mn>8</mn><mn>3</mn></mfrac><mfenced><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>21</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>2</mn><msqrt><mn>7</mn></msqrt></mfrac></mfenced><mo>-</mo><mn>6</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>21</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>2</mn><msqrt><mn>7</mn></msqrt></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfrac><mn>8</mn><mn>3</mn></mfrac><mfenced><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>6</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q62. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><msup><mi mathvariant="normal">&#8477;</mi><mn>2</mn></msup><mo>:</mo><mi>y</mi><mo>&#8805;</mo><mn>0</mn><mo>,</mo><mn>2</mn><mi>x</mi><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><msqrt><mn>4</mn><mo>-</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></msqrt></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi><mo>&#215;</mo><mi mathvariant="normal">&#8477;</mi><mo>:</mo><mn>0</mn><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mi>min</mi><mfenced open="{" close="}"><mrow><mn>2</mn><mi>x</mi><mo>,</mo><msqrt><mn>4</mn><mo>-</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></msqrt></mrow></mfenced></mrow></mfenced></math>. Then the ratio of the area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> to the area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>&#960;</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mrow><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mrow><mi>&#960;</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#960;</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>&#960;</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><msqrt><mn>4</mn><mo>-</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></msqrt><mo>&#160;</mo><mo>:</mo><mi>y</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi></math></p><p>Now plotting the diagram we get,</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/26dee46e-dbfb-45c3-8938-02e6f41cac05-9895075re.PNG" style="width: 317px; height: 200px;" /></p><p>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>: area of shaded region as shown in the above figure,</p><p>Shaded portion <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> circular <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>O</mi><mi>A</mi><mi>B</mi><mi>C</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mo>Ar</mo><mfenced><mrow><mo>&#8710;</mo><mi>O</mi><mi>A</mi><mi>B</mi></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>&#960;</mi><mfenced><mn>4</mn></mfenced></mrow><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mn>2</mn></mfenced><mfenced><mn>1</mn></mfenced></math></p><p>Hence, Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Now, plotting the diagram of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mi>min</mi><mfenced open="{" close="}"><mrow><mn>2</mn><mi>x</mi><mo>,</mo><msqrt><mn>4</mn><mo>-</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></msqrt></mrow></mfenced></math> we get,</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5a717159-199c-42aa-a5cc-fe2ce03b6428-9895075_1re.PNG" style="width: 310px; height: 200px;" /></p><p>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>: area of shaded region as shown in the above figure,</p><p>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi><mo>=</mo><mi>Ar</mi><mfenced><mrow><mo>&#8710;</mo><mi>A</mi><mi>O</mi><mi>B</mi></mrow></mfenced><mo>+</mo></math> Area of arc of circle <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>A</mi><mi>B</mi><mi>C</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mn>1</mn></mfenced><mfenced><mn>2</mn></mfenced><mo>+</mo><mfrac><mrow><mi>&#960;</mi><msup><mfenced><mn>2</mn></mfenced><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>=</mo><mi>&#960;</mi><mo>+</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>A</mi><mi>B</mi></mfrac><mo>=</mo><mfrac><mrow><mtext>area</mtext><mo>&#160;</mo><mi>o</mi><mi>f</mi><mo>&#160;</mo><mi>A</mi></mrow><mrow><mtext>area</mtext><mo>&#160;</mo><mi>o</mi><mi>f</mi><mo>&#160;</mo><mi>B</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>&#960;</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p>

</details>

---

### Q63. JEE Main 2023 (25 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

If the area enclosed by the parabolas <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><mo>:</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub><mo>:</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>y</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math> is equal to the area enclosed by <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>&#945;</mi><mi>x</mi><mo>,</mo><mi>&#945;</mi><mo>&#62;</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>3</mn></msup></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **600**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><mo>:</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub><mo>:</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>y</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p>On solving both equations, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mo>=</mo><mn>5</mn><mfenced><mrow><mi>y</mi><mo>-</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>&#177;</mo><mn>2</mn></math></p><p>So, points of intersection are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>10</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>10</mn></mrow></mfenced></math>.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9203ecdb-dd8d-4202-8d3d-a8d66610a327-9894325_re.PNG" style="width: 303px; height: 202px;" /></p><p>Also, solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>&#945;</mi><mi>x</mi></math>, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mn>2</mn><mi>&#945;</mi></mrow><mn>5</mn></mfrac></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3b595a5e-541f-492b-8b4a-b8e550e7a052-9894325_1_re.PNG" style="width: 329px; height: 230px;" /></p><p>According to question <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mo>-</mo><mfrac><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mrow><mn>2</mn><mi>&#945;</mi></mrow><mn>5</mn></mfrac></msubsup><mfenced><mrow><mi>&#945;</mi><mi>x</mi><mo>-</mo><mfrac><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mn>6</mn><mi>x</mi><mo>-</mo><mfrac><mrow><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>6</mn></mfrac></mrow></mfenced><mn>0</mn><mn>2</mn></msubsup><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><mrow><mi>&#945;</mi><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>-</mo><mfrac><mrow><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>6</mn></mfrac></mrow></mfenced><mn>0</mn><mfrac><mrow><mn>2</mn><mi>&#945;</mi></mrow><mn>5</mn></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><mn>12</mn><mo>+</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>20</mn><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mfrac><mrow><mn>2</mn><msup><mi>&#945;</mi><mn>3</mn></msup></mrow><mn>25</mn></mfrac><mo>-</mo><mfrac><mrow><mn>8</mn><msup><mi>&#945;</mi><mn>3</mn></msup></mrow><mrow><mn>6</mn><mo>&#215;</mo><mn>25</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><msup><mi>&#945;</mi><mn>3</mn></msup></mrow><mn>75</mn></mfrac><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>&#945;</mi><mn>3</mn></msup><mo>=</mo><mn>600</mn></math></p>

</details>

---

### Q64. JEE Main 2023 (24 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

If the area of the region bounded by the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>y</mi><mo>=</mo><mo>-</mo><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>A</mi><mo>=</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **36**

**Detailed Solution:**

<p>Given,</p><p>Equations of curve <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>y</mi><mo>=</mo><mo>-</mo><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p>Now solving above equations we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>-</mo><mn>3</mn></math></p><p>Now plotting the area we get, </p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f1f35d8f-b7ef-4c4c-877a-04c4b4701de3-b15b6a74-f8e7-4f5c-8b6b-d50f2c5801e1-24-01-2023.png" style="width: 350px; height: 219px;" /></p><p>Now from above diagram required area will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mfenced><mrow><mfenced><mrow><mn>2</mn><mi>y</mi><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mi>y</mi></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mfenced><mrow><mn>3</mn><mi>y</mi><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><msubsup><mfenced open="[" close="]"><mrow><mfrac><mrow><mn>3</mn><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>-</mo><mfrac><msup><mi>y</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mn>0</mn><mn>3</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mrow><mfrac><mn>27</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>27</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><mn>27</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></math> sq. units</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mn>8</mn><mi>A</mi><mo>=</mo><mn>9</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>36</mn></math>.</p>

</details>

---

### Q65. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The area enclosed between the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>=</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>2</mn><mi>x</mi><mo>=</mo><mn>2</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>22</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>23</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a92f8018-9b1b-45a0-95d8-ac84717fe4b1-9884719.png" style="width: 350px; height: 294px;" /></p><p>Required area</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>4</mn></mrow><mn>2</mn></msubsup><mfenced><mrow><mfrac><mrow><mn>4</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>-</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>4</mn></mrow><mn>2</mn></msubsup><mfenced><mrow><mn>2</mn><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>-</mo><mfrac><mi>y</mi><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mn>2</mn><mi>y</mi><mo>-</mo><mfrac><msup><mi>y</mi><mn>3</mn></msup><mn>12</mn></mfrac><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced><mrow><mo>-</mo><mn>4</mn></mrow><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><mfenced><mrow><mn>4</mn><mo>-</mo><mfrac><mn>8</mn><mn>12</mn></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mo>-</mo><mn>8</mn><mo>+</mo><mfrac><mn>64</mn><mn>12</mn></mfrac><mo>-</mo><mfrac><mn>16</mn><mn>4</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>15</mn><mo>-</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn></math> sq. units</p>

</details>

---

### Q66. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><msqrt><mn>5</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>3</mn><mn>5</mn></mfrac></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Plotting region for <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><msqrt><mn>5</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></math>, we get, </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f21d6b8d-bcaf-4897-a92a-bd5ae7ba8ee1-image.png" style="width: 378px; height: 250px;" /></p><p>The intersection points of the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>Here chord <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> subtends a right angle at the centre of the circle.
So, required area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi><mo>+</mo></math> area of segment of circle on chord <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>A</mi><mi>C</mi><mo>&#183;</mo><mi>B</mi><mi>C</mi><mo>+</mo></math> [area of quarter circle <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo></math> area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>O</mi><mi>B</mi></math>]</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><msqrt><mn>2</mn></msqrt><mo>&#215;</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mfenced><mrow><mfrac><mrow><mn>90</mn><mo>&#176;</mo></mrow><mrow><mn>360</mn><mo>&#176;</mo></mrow></mfrac><mo>&#215;</mo><mi mathvariant="normal">&#960;</mi><msup><mfenced><msqrt><mn>5</mn></msqrt></mfenced><mn>2</mn></msup><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><msup><mfenced><msqrt><mn>5</mn></msqrt></mfenced><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p></blockquote>

</details>

---

### Q67. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area of the region enclosed by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8804;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>9</mn><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8804;</mo><mn>4</mn></math>, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>40</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>56</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>112</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>80</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>80</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Plotting the required region</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/551d0997-09be-44fe-bdba-5d4b482d3c49-image.png" style="width: 350px; height: 211px;" /></p><p>Enclosed area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>4</mn></msubsup><mfenced><mrow><mn>3</mn><msqrt><mi>y</mi></msqrt><mo>-</mo><mfrac><msqrt><mi>y</mi></msqrt><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>4</mn></msubsup><mfrac><mrow><mn>5</mn><msqrt><mi>y</mi></msqrt></mrow><mn>2</mn></mfrac><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><msubsup><mfenced close="]" open="["><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>y</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mrow></mfenced><mn>0</mn><mn>4</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>10</mn><mn>3</mn></mfrac><mo>(</mo><mn>4</mn><msup><mo>)</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>=</mo><mfrac><mn>80</mn><mn>3</mn></mfrac></math></p></blockquote>

</details>

---

### Q68. JEE Main 2022 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the smaller region enclosed by the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msqrt><mn>3</mn></msqrt><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced><mrow><mn>2</mn><mo>-</mo><mn>12</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>8</mn><mi>&#960;</mi></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced><mrow><mn>2</mn><mo>-</mo><mn>12</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>6</mn><mi>&#960;</mi></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced><mrow><mn>4</mn><mo>-</mo><mn>12</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>8</mn><mi>&#960;</mi></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced><mrow><mn>4</mn><mo>-</mo><mn>12</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>6</mn><mi>&#960;</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced><mrow><mn>4</mn><mo>-</mo><mn>12</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>8</mn><mi>&#960;</mi></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Plotting the area of the smaller region enclosed by the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msqrt><mn>3</mn></msqrt><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2d0c096b-5eca-473b-932e-c5e45958a2ad-image.png" style="width: 413px; height: 280px;" /></p><p>Now finding point of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msqrt><mn>3</mn></msqrt><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> and </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>4</mn></math></p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p>Both are symmetric about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis</p><p>So, area will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced><mrow><msqrt><mn>16</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced><mo>-</mo><mfenced><mfrac><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow><mn>8</mn></mfrac></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>y</mi><msqrt><mn>16</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>+</mo><mn>16</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>y</mi><mn>4</mn></mfrac></mfenced></mrow></mfenced><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mi>y</mi><mo>-</mo><mfrac><msup><mi>y</mi><mn>3</mn></msup><mn>24</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>y</mi></mrow></mfenced><mn>0</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced close="]" open="["><mrow><mn>8</mn><mi>&#960;</mi><mo>+</mo><mn>4</mn><mo>-</mo><mn>12</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced></math></p></blockquote>

</details>

---

### Q69. JEE Main 2022 (26 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area bounded by the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>3</mn></mfrac><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>3</mn></mfrac><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Plotting the diagram of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn></math>, we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4051539d-cc34-4812-891d-cf5d36bcaabb-image.png" style="width: 301px; height: 180px;" /></p><p>Area of the region between the two curves</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><msqrt><mn>2</mn></msqrt></msubsup><mfenced><mrow><mn>1</mn><mo>-</mo><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><msqrt><mn>2</mn></msqrt></msubsup><mfenced><mrow><mn>1</mn><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>+</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mn>1</mn><msqrt><mn>2</mn></msqrt></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math></p></blockquote>

</details>

---

### Q70. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mi>min</mi><mfenced close="}" open="{"><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mo>,</mo><mn>4</mn><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>31</mn><mn>8</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>17</mn><mn>6</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>27</mn><mn>8</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>17</mn><mn>6</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>The graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>min</mi><mfenced open="{" close="}"><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mo>,</mo><mn>4</mn><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced></math> will be</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0ba05350-40c0-44fd-a1b5-4db5a6ddf5ba-image.png" style="width: 309px; height: 230px;" /></p><p>From the graph,</p><p>required area <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>1</mn></msubsup><mfenced><mrow><mn>4</mn><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced><mrow><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mo>+</mo><msubsup><mfenced><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mn>3</mn><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>1</mn></msubsup><mo>=</mo><mfrac><mn>17</mn><mn>6</mn></mfrac></math></p></blockquote>

</details>

---

### Q71. JEE Main 2022 (29 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>For real numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mfenced><mrow><mi>a</mi><mo>&#62;</mo><mi>b</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math>, let</p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close=""><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>:</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="" close="}"><mrow><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>&#8805;</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>30</mn><mi>&#960;</mi></math></p><p>and</p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close=""><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>:</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8805;</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="" close="}"><mrow><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>&#8804;</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>18</mn><mi>&#960;</mi></math></p><p>Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><msup><mrow/><mn>2</mn></msup></math> is equal to _____.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<p>We know that area of circle <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>&#960;r</mi><mn>2</mn></msup></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> is radius of circle) and area of ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#960;ab</mi></math> (where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>b</mi></math> are length of semi major and semi minor axis)</p><p>Now given area between circle and ellipse  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#960;</mi><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mi>&#960;</mi><mi>a</mi><mi>b</mi><mo>=</mo><mn>30</mn><mi>&#960;</mi></math>  .....(i)</p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#960;</mi><mi>a</mi><mi>b</mi><mo>-</mo><mi>&#960;</mi><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>18</mn><mi>&#960;</mi></math> ....(ii)</p><p>On subtracting equation (i) - (ii), we get <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>a</mi><mi>b</mi><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>12</mn></math>.</p>

</details>

---

### Q72. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area enclosed by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mi>x</mi></math> that lies outside the triangle formed by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>,</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>y</mi><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math>, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>16</mn><msqrt><mn>2</mn></msqrt></mrow><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>11</mn><msqrt><mn>2</mn></msqrt></mrow><mn>6</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>13</mn><msqrt><mn>2</mn></msqrt></mrow><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><msqrt><mn>2</mn></msqrt></mrow><mn>6</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>13</mn><msqrt><mn>2</mn></msqrt></mrow><mn>6</mn></mfrac></math>**

**Detailed Solution:**

<p>Intersection point of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mi>x</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>&#160;</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a48a9bc1-bf0f-4448-8c8d-66154c4f9153-image.png" style="width: 297px; height: 229px;" /></p><p>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mo>&#183;</mo><mn>1</mn><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p>So required area<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math>area between the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi></math> and the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mi>x</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>ar</mi><mo mathvariant="italic">&#9651;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="[" close="]"><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>4</mn></msubsup><mfenced><mrow><msqrt><mn>8</mn><mi>x</mi></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>32</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac><mo>-</mo><mn>8</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>=</mo><mfrac><mrow><mn>13</mn><msqrt><mn>2</mn></msqrt></mrow><mn>6</mn></mfrac></math></p>

</details>

---

### Q73. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>8</mn><mi>x</mi><mo>,</mo><mi>y</mi><mo>&#8805;</mo><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>,</mo><mi>x</mi><mo>&#8805;</mo><mn>1</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><msqrt><mn>2</mn></msqrt></mrow><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>19</mn><msqrt><mn>2</mn></msqrt></mrow><mn>6</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>13</mn><msqrt><mn>2</mn></msqrt></mrow><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>11</mn><msqrt><mn>2</mn></msqrt></mrow><mn>6</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>11</mn><msqrt><mn>2</mn></msqrt></mrow><mn>6</mn></mfrac></math>**

**Detailed Solution:**

<p>Plotting the region for the given inequalities <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>8</mn><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8805;</mo><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn></math>, we get</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/70d39a46-cc4e-47bb-9532-992ada09025e-image.png" style="width: 200px; height: 162px;" /></p><p> </p><p>Required area will be <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>1</mn><mn>4</mn></msubsup><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msqrt><mi>x</mi></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><msubsup><mfenced><mfrac><msup><mi>x</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></mfrac></mfenced><mn>1</mn><mn>4</mn></msubsup><mo>-</mo><msqrt><mn>2</mn></msqrt><msubsup><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mn>1</mn><mn>4</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac><mfenced><mrow><mn>8</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfrac><msqrt><mn>2</mn></msqrt><mn>3</mn></mfrac><mfenced><mrow><mn>16</mn><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>28</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mn>15</mn><msqrt><mn>2</mn></msqrt></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>11</mn><msqrt><mn>2</mn></msqrt></mrow><mn>6</mn></mfrac></math></p>

</details>

---

### Q74. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area of the region bounded by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>16</mn><mfenced><mrow><mn>3</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>32</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>40</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>**

**Detailed Solution:**

Given curves are <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>16</mn><mfenced><mrow><mn>3</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mi>x</mi><mo>=</mo><mn>48</mn><mo>-</mo><mn>16</mn><mi>x</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>2</mn></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>&#177;</mo><mn>4</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/aaa28580-246c-4053-8714-4ea2ef64a6f3-image.png" style="width: 303px; height: 180px;" /></p><p>Required area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>4</mn></msubsup><mfenced><mrow><mfenced><mrow><mn>3</mn><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>16</mn></mfrac></mrow></mfenced><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>8</mn></mfrac></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mrow><mn>3</mn><mi>y</mi><mo>-</mo><mfrac><msup><mi>y</mi><mn>3</mn></msup><mn>48</mn></mfrac><mo>-</mo><mfrac><msup><mi>y</mi><mn>3</mn></msup><mn>24</mn></mfrac></mrow></mfenced><mn>0</mn><mn>4</mn></msubsup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><mn>12</mn><mo>-</mo><mfrac><mn>64</mn><mn>48</mn></mfrac><mo>-</mo><mfrac><mn>64</mn><mn>24</mn></mfrac></mrow></mfenced><mo>=</mo><mn>16</mn></math>  </p>

</details>

---

### Q75. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area bounded by the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn></mrow></mfenced></math> and the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>3</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msqrt><mn>6</mn></msqrt><mo>-</mo><mn>16</mn><msqrt><mn>12</mn></msqrt><mo>-</mo><mn>72</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msqrt><mn>6</mn></msqrt><mo>+</mo><mn>8</mn><msqrt><mn>12</mn></msqrt><mo>-</mo><mn>72</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><msqrt><mn>6</mn></msqrt><mo>+</mo><mn>16</mn><msqrt><mn>12</mn></msqrt><mo>-</mo><mn>72</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><msqrt><mn>6</mn></msqrt><mo>-</mo><mn>16</mn><msqrt><mn>12</mn></msqrt><mo>-</mo><mn>64</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><msqrt><mn>6</mn></msqrt><mo>+</mo><mn>16</mn><msqrt><mn>12</mn></msqrt><mo>-</mo><mn>72</mn></math>**

**Detailed Solution:**

<p>We first find the points of intersection of the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>3</mn></math></p><p>which gives, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn></mrow></mfenced><mo>=</mo><mn>3</mn></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mo>=</mo><mo>&#177;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>12</mn></math> (or) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>6</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>&#177;</mo><msqrt><mn>12</mn></msqrt></math> (or) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>&#177;</mo><msqrt><mn>6</mn></msqrt></math></p><p>The graphs of the two curves are shown in figure</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/31f98fea-dd53-4345-bed9-cc24aff51813-image.png" style="width: 442px; height: 230px;" /></p><p>We have to find the area of the shaded region.</p><p>Required area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msub><mi>A</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>A</mi><mn>2</mn></msub></math>  (<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo></math> The areas <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub></math> are symmetrical about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo></math> axis )</p><p>where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><msqrt><mn>6</mn></msqrt></munderover><mfenced close="]" open="["><mrow><mfenced><mrow><mn>9</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>&#8722;</mo><mfenced><mn>3</mn></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><msqrt><mn>6</mn></msqrt></munderover><mfenced><mrow><mn>6</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mn>6</mn><mi>x</mi><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mn>0</mn><msqrt><mn>6</mn></msqrt></msubsup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><msqrt><mn>6</mn></msqrt><mo>-</mo><mfrac><mrow><mn>6</mn><msqrt><mn>6</mn></msqrt></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>12</mn><msqrt><mn>6</mn></msqrt></mrow><mn>3</mn></mfrac><mo>=</mo><mn>4</mn><msqrt><mn>6</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><munderover><mo>&#8747;</mo><msqrt><mn>6</mn></msqrt><mn>3</mn></munderover><mfenced close="]" open="["><mrow><mn>3</mn><mo>&#8722;</mo><mfenced><mrow><mn>9</mn><mo>&#8722;</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><munderover><mo>&#8747;</mo><mn>3</mn><msqrt><mn>12</mn></msqrt></munderover><mfenced close="]" open="["><mrow><mn>3</mn><mo>&#8722;</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>9</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><msqrt><mn>6</mn></msqrt><mn>3</mn></msubsup><mfenced><mrow><mo>-</mo><mn>6</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>3</mn><msqrt><mn>12</mn></msqrt></msubsup><mfenced><mrow><mn>12</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><msqrt><mn>6</mn></msqrt><mn>3</mn></msubsup><mo>+</mo><msubsup><mfenced close="]" open="["><mrow><mn>12</mn><mi>x</mi><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mn>3</mn><msqrt><mn>12</mn></msqrt></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mo>-</mo><mn>18</mn><mo>+</mo><mn>9</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mo>-</mo><mn>6</mn><msqrt><mn>6</mn></msqrt><mo>+</mo><mn>2</mn><msqrt><mn>6</mn></msqrt><mo>)</mo></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>12</mn><msqrt><mn>12</mn></msqrt><mo>-</mo><mn>4</mn><msqrt><mn>12</mn></msqrt></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>36</mn><mo>-</mo><mn>9</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>36</mn><mo>+</mo><mn>4</mn><msqrt><mn>6</mn></msqrt><mo>+</mo><mn>8</mn><msqrt><mn>12</mn></msqrt></math></p><p>Hence, required area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msub><mi>A</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>A</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><mn>4</mn><msqrt><mn>6</mn></msqrt></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mn>36</mn><mo>+</mo><mn>4</mn><msqrt><mn>6</mn></msqrt><mo>+</mo><mn>8</mn><msqrt><mn>12</mn></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><msqrt><mn>6</mn></msqrt><mo>-</mo><mn>72</mn><mo>+</mo><mn>8</mn><msqrt><mn>6</mn></msqrt><mo>+</mo><mn>16</mn><msqrt><mn>12</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>16</mn><msqrt><mn>6</mn></msqrt><mo>+</mo><mn>16</mn><msqrt><mn>12</mn></msqrt><mo>-</mo><mn>72</mn></math></p>

</details>

---

### Q76. JEE Main 2022 (25 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area of the region enclosed between the parabolas <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>3</mn></math> is.

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>We first find the points of intersection of the given parabolas by solving the equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>simultaneously.</p><p>This gives, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>2</mn><mi>x</mi><mo>=</mo><mn>2</mn></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p>Now, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn></math>.</p><p>Now, the equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced></math> respectively.</p><p>The graphs of these two curves are shown in figure.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5c0efdd7-b840-4e55-b17f-11ad4750d950-image.png" style="width: 323px; height: 220px;" /></p><p>We have to find the area of the shaded region.</p><p>Now, the equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow><mn>4</mn></mfrac></math> respectively.</p><p>It is clear from the figure, required area <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow></mfenced><mi>d</mi><mi>y</mi></math>  (<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo></math> Area is symmetrical about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math> axis)</p><p>where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mfrac><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>-</mo><mfrac><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>y</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2</mn><mn>4</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mfenced close="]" open="["><mrow><mi>y</mi><mo>-</mo><mfrac><msup><mi>y</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math> sq.units.</p>

</details>

---

### Q77. JEE Main 2022 (24 Jun Shift 2)

*Type:* `numerical` | *Level:* `1`

The area (in sq. units) of the region enclosed between the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>x</mi></math> and the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>4</mn></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e838549e-7d54-41ca-b5c8-544995f34ee1-image.png" style="width: 232px; height: 220px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>x</mi><mo>&#160;</mo><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mfenced><mrow><mn>4</mn><mo>-</mo><mi>y</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>4</mn><mo>,</mo><mn>2</mn></math></p><p>The point of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>4</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>8</mn><mo>,</mo><mo>-</mo><mn>4</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>4</mn></mrow><mn>2</mn></msubsup><mfenced><mrow><mfenced><mrow><mn>4</mn><mo>-</mo><mi>y</mi></mrow></mfenced><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>y</mi><mo>&#160;</mo><mo>=</mo><msubsup><mfenced><mrow><mn>4</mn><mi>y</mi><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><msup><mi>y</mi><mn>3</mn></msup><mn>6</mn></mfrac></mrow></mfenced><mrow><mo>-</mo><mn>4</mn></mrow><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>8</mn><mo>-</mo><mn>2</mn><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced><mrow><mo>-</mo><mn>16</mn><mo>-</mo><mn>8</mn><mo>+</mo><mfrac><mn>32</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>54</mn><mn>3</mn></mfrac><mo>=</mo><mn>18</mn></math> Sq.units.</p>

</details>

---

### Q78. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>y</mi><mo>-</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></math>, the tangent to it at the point whose ordinate is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> and the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis, is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>**

**Detailed Solution:**

<p>Given, the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>3</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p>So, point is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></math> Differentiate given equation w.r.t. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>(</mo><mi>y</mi><mo>-</mo><mn>2</mn><mo>)</mo><msup><mi>y</mi><mo>&#39;</mo></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mi mathvariant="normal">&#8242;</mi></msup><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>(</mo><mi>y</mi><mo>&#8722;</mo><mn>2</mn><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced close="|" open="" separators="|"><msup><mi>y</mi><mi mathvariant="normal">&#8242;</mi></msup></mfenced><mrow><mo>(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></mrow></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>So, the equation of tangent at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>3</mn><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0a31cad0-b18a-48b6-a436-3fd3607fd023-image.png" style="width: 337px; height: 276px;" /></p><p>Required area  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mo>[</mo><mo>(</mo><mi>y</mi><mo>-</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>]</mo><mi>d</mi><mi>y</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mo>(</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>4</mn><mo>)</mo><mi>d</mi><mi>y</mi></math>
Required area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mi>d</mi><mi>y</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mfenced><mrow><mn>2</mn><mi>y</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mi>d</mi><mi>y</mi></math>
Required area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>y</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>y</mi></mrow></mfenced><mn>0</mn><mn>3</mn></msubsup><mo>-</mo><msubsup><mfenced close="]" open="["><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>y</mi></mrow></mfenced><mn>0</mn><mn>3</mn></msubsup></math> </p><p>Required area<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>&#160;</mo></math>sq units</p>

</details>

---

### Q79. JEE Main 2021 (26 Aug Shift 1)

*Type:* `numerical` | *Level:* `1`

The area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>:</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>4</mn><mi>y</mi><mo>&#8804;</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>24</mn></mrow></mfenced></math> is______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **27**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>:</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>4</mn><mi>y</mi><mo>&#8804;</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>24</mn></mrow></mfenced></math></p><p>Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mspace width="1em"></mspace></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>y</mi><mo>=</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>24</mn></math></p><p>Solving both equations, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mn>12</mn></mrow></mfenced></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0a8114da-f21b-4f81-bb81-6398b075b00b-image.png" style="width: 405px; height: 265px;" /></p><p>Required area</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>&#8722;</mo><mn>2</mn></mrow><mn>4</mn></msubsup><mo>&#8202;</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>6</mn><mi>x</mi><mo>+</mo><mn>24</mn></mrow><mn>4</mn></mfrac><mo>&#8722;</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><msubsup><mo>&#8747;</mo><mrow><mo>&#8722;</mo><mn>2</mn></mrow><mn>4</mn></msubsup><mo>&#8202;</mo><mfenced separators="|"><mrow><mn>6</mn><mi>x</mi><mo>+</mo><mn>24</mn><mo>&#8722;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><msubsup><mfenced separators="|"><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>&#8722;</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>4</mn></mfrac></mrow></mfenced><mrow><mo>&#8722;</mo><mn>2</mn></mrow><mn>4</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfenced separators="|"><mrow><mn>12</mn><mo>+</mo><mn>24</mn><mo>&#8722;</mo><mn>16</mn><mo>-</mo><mn>3</mn><mo>+</mo><mn>12</mn><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mn>27</mn><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mi>units</mi></math></p>

</details>

---

### Q80. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area of the region bounded by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mi>x</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>y</mi></math> is equal to :-

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>16</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5251f333-9168-4888-92d1-3ccbfb6169eb-image.png" style="width: 313px; height: 250px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>y</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mo>+</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn></math></p><p>Required area<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></msubsup><mfenced><mrow><mn>2</mn><mo>+</mo><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="|" open="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>4</mn><mo>+</mo><mn>2</mn><mo>-</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>-</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></math> square units</p>

</details>

---

### Q81. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the area of the bounded region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mi>max</mi><mfenced open="{" close="}"><mrow><mn>0</mn><mo>,</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><msup><mn>2</mn><mi>x</mi></msup><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mrow></mfenced></math> is, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mi>&#946;</mi><mfenced><mrow><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></mrow></mfenced><mo>+</mo><mi>&#947;</mi></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>-</mo><mn>2</mn><mi>&#947;</mi></mrow></mfenced><mn>2</mn></msup></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mi>max</mi><mfenced><mrow><mn>0</mn><mo>,</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><msup><mn>2</mn><mi>x</mi></msup><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/650c0487-bb2c-4bad-9380-15ce5a34926d-image.png" style="width: 345px; height: 300px;" /></p><p>So, the area of the region is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>2</mn></msubsup><msup><mn>2</mn><mi>x</mi></msup><mi>d</mi><mi>x</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>&#8467;</mi><mi>n</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mfrac><msup><mn>2</mn><mi>x</mi></msup><mrow><mi>ln</mi><mn>2</mn></mrow></mfrac></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mo>-</mo><msubsup><mfenced close="]" open="["><mrow><mi>x</mi><mi>ln</mi><mi>x</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><msup><mn>2</mn><mn>2</mn></msup></mfenced><mo>-</mo><msup><mn>2</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><mrow><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></mrow></mfrac><mo>-</mo><mfenced><mrow><mn>2</mn><mi>ln</mi><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mrow><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></mrow></mfrac><mo>-</mo><mn>2</mn><mi>ln</mi><mn>2</mn><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><msup><mn>2</mn><mn>2</mn></msup><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mi>&#947;</mi><mo>=</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>-</mo><mn>2</mn><mi>&#947;</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q82. JEE Main 2021 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The area (in sq. units) of the region, given by the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi><mo>&#215;</mo><mi>R</mi><mo>&#8739;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn><mo>,</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mn>4</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>17</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>13</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cdcc227e-faed-4b47-8455-ef609c21214f-image.png" style="width: 285px; height: 230px;" /></p><p>Given curves are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>4</mn><mo>-</mo><mn>2</mn><mi>x</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>-</mo><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-coordinate of the intersection point is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>&#60;</mo><mn>0</mn></math></p><p>Required area <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>4</mn><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><menclose notation="right"><mfenced close="]" open="["><mrow><mn>4</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac></mrow></mfenced></menclose><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>-</mo><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q83. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub></math> be the area of the region bounded by the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>sin</mi><mi>x</mi><mo>,</mo><mi>y</mi><mo>=</mo><mi>cos</mi><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis in the first quadrant. Also, let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub></math> be the area of the region bounded by the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>sin</mi><mi>x</mi><mo>,</mo><mi>y</mi><mo>=</mo><mi>cos</mi><mi>x</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math> in the first quadrant. Then,

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><msub><mi>A</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>+</mo><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>:</mo><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>:</mo><msqrt><mn>2</mn></msqrt></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>+</mo><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>:</mo><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>:</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>+</mo><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><msub><mi>A</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>+</mo><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>:</mo><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>:</mo><msqrt><mn>2</mn></msqrt></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>+</mo><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/905f2c0c-73fd-4e66-83f9-6de2a730c3ed-image.png" style="width: 340px; height: 200px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></msubsup><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><msubsup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></msubsup><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></msubsup><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced><mrow><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></msubsup><mo>+</mo><msubsup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mo>=</mo><mn>2</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>:</mo><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>:</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mo>&#160;</mo><msub><mi>A</mi><mn>1</mn></msub><mo>+</mo><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q84. JEE Main 2021 (25 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

The graphs of sine and cosine functions, intersect each other at a number of points and between two consecutive points of intersection, the two graphs enclose the same area <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>4</mn></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **64**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2a09577c-7815-4a85-aae7-c00b44ed59a8-image.png" style="width: 338px; height: 220px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow><mrow><mn>5</mn><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></msubsup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mo>-</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mfenced close="" open="|"><msubsup><mrow></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow><mrow><mn>5</mn><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></msubsup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mo>-</mo><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mo>-</mo><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac></mfenced></mrow></mfenced><mo>-</mo><mfenced><mrow><mo>-</mo><mfenced><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mo>-</mo><mfenced><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mfrac><mn>2</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mfrac><mn>2</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math> sq. units</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>4</mn></msup><mo>=</mo><mn>16</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>64</mn></math></p>

</details>

---

### Q85. JEE Main 2021 (24 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msqrt><mn>3</mn></msqrt></math> square units
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><msqrt><mn>3</mn></msqrt></math> square units
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><msqrt><mn>3</mn></msqrt></math> square units
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msqrt><mn>3</mn></msqrt></math> square units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><msqrt><mn>3</mn></msqrt></math> square units**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dd562d52-1135-4c75-9ee6-f35ea8dc49de-image.png" style="width: 244px; height: 165px;" /></p><p>Required area<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><msqrt><mn>3</mn></msqrt></msubsup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn><mo>-</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mrow><mn>9</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mn>0</mn><msqrt><mn>3</mn></msqrt></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><mn>9</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced><mo>=</mo><mn>12</mn><msqrt><mn>3</mn></msqrt></math> square units</p>

</details>

---

### Q86. JEE Main 2021 (24 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the part of the circle <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>36</mn></math>, which is outside the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn><mi>x</mi></math>, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>&#960;</mi><mo>+</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn><mi>&#960;</mi><mo>+</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn><mi>&#960;</mi><mo>-</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>&#960;</mi><mo>-</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn><mi>&#960;</mi><mo>-</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/37dc8739-e477-4afb-b82f-844df5f0ea45-image.png" style="width: 375px; height: 270px;" /></p><p>Required area</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#960;</mi><mo>&#215;</mo><msup><mfenced><mn>6</mn></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><msqrt><mn>9</mn><mi>x</mi></msqrt><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>3</mn><mn>6</mn></msubsup><msqrt><mn>36</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>36</mn><mi>&#960;</mi><mo>-</mo><mn>6</mn><msubsup><mfenced close="]" open="["><mfrac><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></mfrac></mfenced><mn>0</mn><mn>3</mn></msubsup><mo>-</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><msqrt><mn>36</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mn>18</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>x</mi><mn>6</mn></mfrac></mrow></mfenced><mn>3</mn><mn>6</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>36</mn><mi>&#960;</mi><mo>-</mo><mn>12</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>2</mn><mfenced><mrow><mn>0</mn><mo>-</mo><mfrac><mrow><mn>9</mn><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac><mo>+</mo><mn>9</mn><mi>&#960;</mi><mo>-</mo><mn>3</mn><mi>&#960;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>24</mn><mi>&#960;</mi><mo>-</mo><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mi>units</mi></math></p>

</details>

---

### Q87. JEE Main 2020 (06 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region enclosed by the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>16</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4e89510d-fb25-4da2-83bc-e54cc200f593-image.png" style="width: 290px; height: 267px;" />  </p><p>Given curves are</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math></p><p>and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p>so intersection point are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#177;</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> bounded area</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><msubsup><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi>sq</mi><mo>&#183;</mo><mi>units</mi></math></p>

</details>

---

### Q88. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mn>0</mn><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>23</mn><mn>16</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>79</mn><mn>24</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>79</mn><mn>16</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>23</mn><mn>6</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>79</mn><mn>24</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn></math></p><p>Drawing the graph according to the given information,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/72b2a5d9-7fbd-4e30-932a-4679bc85f574-image.png" style="width: 379px; height: 363px;" /></p><p>Area is, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>1</mn></msubsup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>d</mo><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>1</mn></msubsup><mo>+</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced close="]" open="["><mrow><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>3</mn></msup><mo>&#183;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mfrac><mn>4</mn><mn>2</mn></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>-</mo><mfenced><mrow><mfrac><mn>1</mn><mn>24</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>13</mn><mn>24</mn></mfrac><mo>+</mo><mn>4</mn><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mrow><mn>32</mn><mo>-</mo><mn>13</mn><mo>+</mo><mn>96</mn><mo>-</mo><mn>36</mn></mrow><mn>24</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>79</mn><mn>24</mn></mfrac></math> sq. units.</p>

</details>

---

### Q89. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Consider a region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><msup><mi>R</mi><mn>2</mn></msup><mo>:</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mn>2</mn><mi>x</mi></mrow></mfenced></math>. If a line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>&#945;</mi></math> divides the area of region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> into two equal parts, then which of the following is true ?</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>3</mn></msup><mo>-</mo><mn>6</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><msup><mi>&#945;</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>&#945;</mi><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>3</mn></msup><mo>-</mo><mn>6</mn><msup><mi>&#945;</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>-</mo><mn>16</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><msup><mi>&#945;</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4ee18ba7-5412-41d8-8337-1f471243d725-image.png" style="width: 268px; height: 200px;" /> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>4</mn></msubsup><mfenced><mrow><msqrt><mi>y</mi></msqrt><mo>-</mo><mfrac><mi>y</mi><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#945;</mi></msubsup><mfenced><mrow><msqrt><mi>y</mi></msqrt><mo>-</mo><mfrac><mi>y</mi><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><menclose notation="right"><mfenced><mrow><mfrac><mrow><mn>2</mn><msup><mi>y</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced></menclose><mn>0</mn><mn>4</mn></msubsup><mo>=</mo><msubsup><menclose notation="right"><mn>2</mn><mfenced><mrow><mfrac><mrow><mn>2</mn><msup><mi>y</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced></menclose><mn>0</mn><mi>&#945;</mi></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>16</mn><mn>3</mn></mfrac><mo>-</mo><mn>4</mn><mo>=</mo><mn>2</mn><mfenced><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>&#945;</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>-</mo><mfrac><msup><mi>&#945;</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>=</mo><mn>2</mn><mfenced><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>&#945;</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>-</mo><mfrac><msup><mi>&#945;</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>8</mn><msup><mi>&#945;</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>-</mo><mn>3</mn><msup><mi>&#945;</mi><mn>2</mn></msup></mrow><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>8</mn><msup><mi>&#945;</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>-</mo><mn>3</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><msup><mi>&#945;</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q90. JEE Main 2020 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given: <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mrow><maligngroup></maligngroup><mtable><mtr><mtd><mrow><maligngroup></maligngroup><mi>x</mi><mo>,</mo><mi></mi><mi></mi><malignmark></malignmark><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi></mi><mi></mi><malignmark></malignmark><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mtd></mtr></mtable></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mn>1</mn><mo>-</mo><mi>x</mi><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn></mrow></mtd></mtr></mtable></mrow></mfenced></math>
and <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>,</mo><mi></mi><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>.</mo></math> Then, the area (in sq. units) of the region bounded by the curves, <math><mi>y</mi><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> and <math><mi>y</mi><mo>=</mo><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> between the lines <math><mn>2</mn><mi>x</mi><mo>=</mo><mn>1</mn></math> and <math><mn>2</mn><mi>x</mi><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>,</mo></math> is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bd6219cd-b911-40ee-858d-3a7ceb45ea49.jpeg" />
Required area = Area of trapezium ABCD <math><mo>-</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow><mrow><msqrt><mn>3</mn></msqrt><mo>/</mo><mn>2</mn></mrow></munderover><mrow><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mi>d</mi><mi>x</mi></mrow></mrow></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced separators="|"><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>1</mn><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><msubsup><mfenced separators="|"><msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mn>3</mn></msup></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></msubsup></math>
<math><mo>=</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

</details>

---

### Q91. JEE Main 2020 (08 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}" separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mtext>&#8201;</mtext><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><msup><mi>R</mi><mn>2</mn></msup><mo>:</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mn>3</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced></math>, is.

**Options:**

- **(A)** <math><mfrac><mrow><mn>32</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>34</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>29</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>31</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>32</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Point of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></math>, is obtained by <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math><math><mo>&#10233;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo><mi mathvariant="normal"></mi><mn>1</mn></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/26ea9fb3-18df-4495-8bf8-ed4fd825f197-image.png" style="width: 223px; height: 285px;" /></p><p>So, area of the required region is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>3</mn></mrow><mn>1</mn></msubsup><mfenced><mrow><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>&#160;</mo><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mn>3</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mrow><mo>-</mo><mn>3</mn></mrow><mn>1</mn></msubsup><mo>=</mo><mfrac><mn>32</mn><mn>3</mn></mfrac></math>.</p>

</details>

---

### Q92. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region <math><mfenced close="}" open="{" separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced close="" open="|" separators="|"><mrow><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>12</mn></mrow></mfenced></mrow></mfenced></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>125</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>128</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>124</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>127</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>128</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>y</mi></math>
<math><mi>y</mi><mo>=</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>12</mn></math>
<math><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>12</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>3</mn></math>
<math><mi>A</mi><mo>=</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn></mrow></munderover><mrow><mfenced separators="|"><mrow><mn>8</mn><mi>x</mi><mo>+</mo><mn>12</mn><mo>-</mo><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><menclose notation="right"><mfrac><mrow><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mn>12</mn><mi>x</mi><mo>-</mo><mfrac><mrow><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac></menclose><mtable><mtr><mtd><mn>3</mn></mtd></mtr><mtr><mtd/></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable><mo>=</mo><mfenced separators="|"><mrow><mn>4</mn><mfenced separators="|"><mn>9</mn></mfenced><mo>+</mo><mn>36</mn><mo>-</mo><mn>36</mn></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mn>4</mn><mo>-</mo><mn>12</mn><mo>+</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mn>36</mn><mo>+</mo><mn>8</mn><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math>
<math><mo>=</mo><mn>44</mn><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>132</mn><mo>-</mo><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>128</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

</details>

---

### Q93. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region (in sq. units), enclosed by the circle <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></math> which is not common to the region bounded by the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mi>x</mi></math> and the straight line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>x</mi></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac><mfenced separators="|"><mrow><mn>24</mn><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced separators="|"><mrow><mn>6</mn><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced separators="|"><mrow><mn>12</mn><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac><mfenced separators="|"><mrow><mn>12</mn><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac><mfenced separators="|"><mrow><mn>12</mn><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9bd373a2-a40b-48aa-afa1-614df2fe1d4c-1.png" style="width: 320px; height: 278px;" /><p>Required area</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>&#960;</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><msqrt><mi>x</mi></msqrt><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>&#960;</mi><mo>-</mo><msubsup><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>&#960;</mi><mo>-</mo><mfenced separators="|"><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>&#960;</mi><mo>-</mo><mfenced separators="|"><mfrac><mn>1</mn><mn>6</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>12</mn><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow><mn>6</mn></mfrac><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mi>units</mi></math></p>

</details>

---

### Q94. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the area (in sq. units) bounded by the parabola <math><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn><mi>&#955;</mi><mi>x</mi></math> and the line <math><mi>y</mi><mo>=</mo><mi>&#955;</mi><mi>x</mi><mo>,</mo><mtext>&#8201;</mtext><mi>&#955;</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> is <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>9</mn></mrow></mfrac></math>, then <math><mi>&#955;</mi></math> is equal to

**Options:**

- **(A)** <math><mn>4</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math><mn>2</mn><msqrt><mn>6</mn></msqrt></math>
- **(C)** <math><mn>48</mn></math>
- **(D)** <math><mn>24</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>24</mn></math>**

**Detailed Solution:**

<p>The given equations are <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>&#955;</mi><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>&#955;</mi><mi>x</mi></math></p><p>Using above equations, we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>&#955;</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>&#955;</mi><mi>x</mi><mo>&#8658;</mo><msup><mi>&#955;</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>&#955;</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mi>x</mi><mfenced><mrow><mi>&#955;</mi><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mfrac><mn>4</mn><mi>&#955;</mi></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c2cfafb4-f818-42b9-a4da-d48162790b0f-image3.png" /></p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo>=</mo><munderover><mo stretchy="true">&#8747;</mo><mn>0</mn><mfrac><mn>4</mn><mi>&#955;</mi></mfrac></munderover><mfenced separators="|"><mrow><msqrt><mn>4</mn><mi>&#955;</mi><mi>x</mi></msqrt><mo>-</mo><mi>&#955;</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mfenced><mrow><mfrac><mrow><msqrt><mn>4</mn><mi>&#955;</mi></msqrt><msup><mi>x</mi><mstyle displaystyle="true"><mfrac bevelled="true"><mn>3</mn><mn>2</mn></mfrac></mstyle></msup></mrow><mstyle displaystyle="true"><mfrac bevelled="true"><mn>3</mn><mn>2</mn></mfrac></mstyle></mfrac><mo>-</mo><mfrac><mrow><mi>&#955;</mi><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mrow></mfenced><mn>0</mn><mfrac><mn>4</mn><mi>&#955;</mi></mfrac></msubsup><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math></p><p><math><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>24</mn></math></p><p>Hence, the required value is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>.</p>

</details>

---

### Q95. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the area (in sq. units) of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}" separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mo>&#160;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>4</mn><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>&#8804;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8805;</mo><mn>0</mn></mrow></mfenced></math> is <math><mi>a</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>b</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mi>b</mi></math> is equal to

**Options:**

- **(A)** <math><mn>6</mn></math>
- **(B)** <math><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>6</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f65245f2-7002-4496-a433-674f0d2e75f6-image.png" style="width: 395px; height: 263px;" />
The given equations are,</p><p><math><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn><mi>x</mi><mi>&#160;</mi><mo>&#38;</mo><mi>&#160;</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn></math></p><p><math><mo>&#8658;</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>y</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></math></p><p><math><mo>&#8756;</mo></math> Required Area <math><mo>=</mo><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></mrow></munderover><mrow><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>y</mi></mrow></mfenced><mo>-</mo><mfrac><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mrow><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mfrac><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></mrow></msubsup></math></p><p><math><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac><mo>-</mo><mn>0</mn></mrow></mfenced></math></p><p><math><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced close="]" open="[" separators="|"><mrow><mn>1</mn><mo>-</mo><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfrac><mn>10</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac><mo>=</mo><mi>a</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>b</mi><mo>&#160;</mo><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mfrac><mn>10</mn><mn>3</mn></mfrac></math>
<math><mo>&#8756;</mo><mtext>&#8201;</mtext><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q96. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region bounded by the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mn>2</mn><mi mathvariant="italic">x</mi></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced open="|" close="|" separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>, in the first quadrant is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><mn>2</mn><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left" columnspacing="1.4ex"><mtr><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left" columnspacing="1.4ex"><mtr><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math>
The graph of the given functions is</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/84bf6e36-db8a-4fe3-8a54-2d62bd8bd79d-WhatsAppImage2021-08-21at7.43.38AM.jpeg" style="width: 380px; height: 196px;" />
The shaded area is the required area.</p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced separators="|"><mrow><msub><mi>y</mi><mrow><mi>l</mi><mi>i</mi><mi>n</mi><mi>e</mi></mrow></msub><mo>-</mo><msub><mi>y</mi><mrow><mi>c</mi><mi>u</mi><mi>r</mi><mi>v</mi><mi>e</mi></mrow></msub></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn><mo>-</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>x</mi><mi>n</mi></msup><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><msup><mi>x</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>&#8747;</mo><msup><mi>a</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><msup><mi>a</mi><mi>x</mi></msup><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>a</mi></mrow></mfrac><mo>,</mo></math> we get</p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="[" separators="|"><mrow><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mi>x</mi><mo>-</mo><mfrac><msup><mn>2</mn><mi>x</mi></msup><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>-</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mn>0</mn><mo>+</mo><mn>0</mn><mo>-</mo><mfrac><mn>1</mn><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac></mrow></mfenced></math></p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac></math> sq units.</p>

</details>

---

### Q97. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The region represented by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mo>&#8804;</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>&#8804;</mo><mn>2</mn></math> is bounded by a

**Options:**

- **(A)** rhombus of area <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msqrt><mn>2</mn></msqrt><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mo>&#160;</mo><mi>units</mi></math>.
- **(B)** rhombus of side length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> units.
- **(C)** square of area <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mo>&#160;</mo><mi>units</mi></math>.
- **(D)** square of side length <math><mn>2</mn><msqrt><mn>2</mn></msqrt></math> units.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) square of side length <math><mn>2</mn><msqrt><mn>2</mn></msqrt></math> units.**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mo>&#8658;</mo><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">y</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mo>&#8211;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>x</mi><mo>&#8211;</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mi>&#160;</mi><mo>&#8658;</mo><mi mathvariant="normal">x</mi><mi mathvariant="normal">&#160;</mi><mo>&#8211;</mo><mi mathvariant="normal">y</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8211;</mo><mi>y</mi><mo>=</mo><mo>&#8211;</mo><mn>2</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/af3a082d-ce90-4b79-9895-4604f106b06d-image.png" style="width: 515px; height: 391px;" /></p><p>So, the region bounded by the given curves, i.e., pairs of straight lines, is a square.</p><p>Now, length of side of square<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math>distance between parallel lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced close="|" open="|"><mrow><mn>2</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><msqrt><mn>1</mn><mo>+</mo><mn>1</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>4</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p>

</details>

---

### Q98. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mi>y</mi><mo>+</mo><mn>4</mn></mrow></mfenced></math> is:

**Options:**

- **(A)** <math><mn>30</mn></math>
- **(B)** <math><mn>18</mn></math>
- **(C)** <math><mfrac><mrow><mn>53</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mn>16</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>18</mn></math>**

**Detailed Solution:**

<p>We have to find the area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mi>y</mi><mo>+</mo><mn>4</mn></mrow></mfenced></math></p><p>Now, to find the point of intersection of the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>y</mi><mo>+</mo><mn>4</mn><mo>,</mo></math> we equate the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo></math> to get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>=</mo><mi>y</mi><mo>+</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>4</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>And, the graph of the given functions is as</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/55ab0f66-2ac5-432b-8e18-f7c112d82f48-image.png" style="width: 210px; height: 223px;" /></p><p>The shaded area is the required area, and </p><p>Area<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>4</mn></msubsup><mfenced separators="|"><mrow><msub><mi>x</mi><mrow><mi>l</mi><mi>i</mi><mi>n</mi><mi>e</mi></mrow></msub><mo>-</mo><msub><mi>x</mi><mrow><mi>p</mi><mi>a</mi><mi>r</mi><mi>a</mi><mi>b</mi><mi>o</mi><mi>l</mi><mi>a</mi></mrow></msub></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>4</mn></msubsup><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>4</mn><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>x</mi><mi>n</mi></msup><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><msup><mi>x</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>,</mo></math> we get</p><p>Area<math><mo>=</mo><msubsup><mrow><mfenced close="|" open="" separators="|"><mrow><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mn>4</mn><mi>y</mi><mo>-</mo><mfrac><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced></mrow></mfenced></mrow><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mn>4</mn></mrow></msubsup></math></p><p><math><mo>=</mo><mfenced separators="|"><mrow><mn>8</mn><mo>+</mo><mn>16</mn><mo>-</mo><mfrac><mrow><mn>32</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mn>8</mn><mo>+</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math></p><p><math><mo>=</mo><mn>18</mn></math> sq units.</p>

</details>

---

### Q99. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The area (in sq. units) of the region <math><mi>A</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>31</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>The two given curves are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p>To find their points of intersection, we equate the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> to get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>.</mo></math></p><p>The graphs of the curves are given below.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2faa7755-ada7-4533-bbc7-b12300c52121-image.png" style="width: 379px; height: 280px;" />
Required area is the area of the shaded portion.</p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></msubsup><mfenced><mrow><msub><mi>y</mi><mrow><mi>l</mi><mi>i</mi><mi>n</mi><mi>e</mi></mrow></msub><mo>-</mo><msub><mi>y</mi><mrow><mi>p</mi><mi>a</mi><mi>r</mi><mi>a</mi><mi>b</mi><mi>o</mi><mi>l</mi><mi>a</mi></mrow></msub></mrow></mfenced><mi>d</mi><mi>x</mi></math>
<math><mo>=</mo><mrow><msubsup><mo stretchy="false">&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>x</mi><mi>n</mi></msup><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><msup><mi>x</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math><mo>=</mo><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mi>&#160;</mi><mn>2</mn><mi>x</mi><mo>-</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mn>4</mn><mo>-</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math><mo>=</mo><mn>6</mn><mo>-</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mi>&#160;</mi><mn>2</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math></p><p><math><mo>=</mo><mn>8</mn><mo>-</mo><mn>3</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math></p><p><math><mo>=</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> sq units.</p>

</details>

---

### Q100. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The area (in sq. units) of the region <math><mi>A</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi><mo>&#215;</mo><mi>R</mi></mrow><mrow><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>3</mn><mo>,</mo><mi>&#160;</mi><mn>0</mn><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mn>4</mn><mo>,</mo><mi>y</mi><mo>&#8804;</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>3</mn><mi>x</mi></mrow></mfenced></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>26</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mi> </mi><mn>8</mn></math>
- **(C)** <math><mfrac><mrow><mn>53</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>59</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>59</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7f464a09-b596-4920-a814-c193cf3bedaf-image7.png" />
The area of the region <math><mi>O</mi><mi>C</mi><mi>D</mi></math> is
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo stretchy="true">&#8747;</mo><mn>0</mn><mn>1</mn></munderover><mfenced open="[" close="]" separators="|"><mrow><mn>4</mn><mo>-</mo><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mfenced open="[" close="]" separators="|"><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>=</mo><mn>4</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>13</mn><mn>6</mn></mfrac></math>
So, the area of the given region <math><mi>O</mi><mi>A</mi><mi>B</mi><mi>C</mi></math> is
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> Area of <math><mi>O</mi><mi>A</mi><mi>B</mi><mi>D</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo></math> Area of <math><mi>O</mi><mi>C</mi><mi>D</mi></math>
<math><mo>=</mo><mn>3</mn><mo>&#215;</mo><mn>4</mn><mo>-</mo><mfrac><mrow><mn>13</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mn>59</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>

</details>

---

### Q101. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region bounded by the parabola, <math><mi>y</mi><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn></math> and the lines, <math><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math>, is

**Options:**

- **(A)** <math><mfrac><mrow><mn>17</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>21</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>15</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>15</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>15</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/11a01659-1d1e-4306-99ce-4740cad14f9c-image.png" style="width: 443px; height: 443px;" /></p><p>Area of region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi><mi>A</mi><mo>=</mo><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mfenced close="]" open="[" separators="|"><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mn>0</mn><mn>3</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>27</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>+</mo><mn>3</mn></math></p><p><math><mo>=</mo><mn>12</mn><mo>-</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>15</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math></p>

</details>

---

### Q102. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) in the first quadrant bounded by the parabola, $y=x^{2}+1$, the tangent to it at the point (2,5) and the coordinate axes is :

**Options:**

- **(A)** $\frac{8}{3}$
- **(B)** $\frac{37}{24}$
- **(C)** $\frac{187}{24}$
- **(D)** $\frac{14}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{37}{24}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fYoggIIYGTN6xBD6Qx3VBLkKetcriHuvr-bQe0fp3es.original.fullsize.png">


The equation of parabola $x^{2}=y-1$

The equation of tangent at (2,5) to parabola is

$y-5=\left(\frac{d y}{d x}\right)_{(2,5)}(x-2)$

$y-5=4(x-2)$

$4 x-y=3$

Then, the required area

$=\int_{0}^{2}\left\{\left(x^{2}+1\right)-(4 x-3)\right\} d x-$ Area of $\Delta A O D$

$=\int_{0}^{2}\left(x^{2}-4 x+4\right) d x-\frac{1}{2} \times \frac{3}{4} \times 3$

$=\left[\frac{(x-2)^{3}}{3}\right]_{0}^{2}-\frac{9}{8}=\frac{37}{24}$

</details>

---

### Q103. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region bounded by the curve $x^{2}=4 y$ and the straight line $x=4 y-2$ is :

**Options:**

- **(A)** $\frac{5}{4}$
- **(B)** $\frac{9}{8}$
- **(C)** $\frac{7}{8}$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{9}{8}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/rlMJ6CC3lOq6tClVsG7jaXtCd1AA0ppl6i_tFAiV3rY.original.fullsize.png">


Let points of intersection of the curve and the line be

$P$ and $Q$

$x^{2}=4\left(\frac{x+2}{4}\right)$

$x^{2}-x-2=0$

$x=2,-1$

Point are (2,1) and $\left(-1, \frac{1}{4}\right)$

$\text { Area }=\int_{-1}^{2}\left[\left(\frac{x+2}{4}\right)-\left(\frac{x^{2}}{4}\right)\right] d x=\left[\frac{x^{2}}{8}+\frac{1}{2} x-\frac{x^{3}}{12}\right]_{-1}^{2}$

$=\left(\frac{1}{2}+1-\frac{2}{3}\right)-\left(\frac{1}{8}-\frac{1}{2}+\frac{1}{12}\right)=\frac{9}{8}$

</details>

---

### Q104. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the area enclosed between the curves <math><mi>y</mi><mo>=</mo><mi>k</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>k</mi><msup><mi>y</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>k</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced><mo>,</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>s</mi><mi>q</mi><mo>.</mo><mo>&#160;</mo><mi>u</mi><mi>n</mi><mi>i</mi><mi>t</mi><mo>.</mo></math> Then <math><mi>k</mi></math> is

**Options:**

- **(A)** <math><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p>The given curves are, <math><mi>y</mi><mo>=</mo><mi>k</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>=</mo><mi>k</mi><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></math></p><p>To find the point of intersection of the curves, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> from the first curve into second, to get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>k</mi><mfenced separators="|"><mrow><msup><mi>k</mi><mn>2</mn></msup><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>=</mo><msup><mfenced separators="|"><mfrac><mn>1</mn><mi>k</mi></mfrac></mfenced><mn>3</mn></msup><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mi>k</mi></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>k</mi><msup><mfenced><mfrac><mn>1</mn><mi>k</mi></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mi>k</mi></mfrac></math></p><p>Therefore, point of intersection is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mfrac><mn>1</mn><mi>k</mi></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mi>k</mi></mfrac></mrow></mfenced><mo>.</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/gbhijmiscyzgtsmittgegdvsifflkjlflcrteinbowkrzvjwge.png" style="width: 250px; height: 216px;" />

Hence, the required area is <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mi>k</mi></mfrac></msubsup><mfenced><mrow><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mi>k</mi></mfrac></msubsup><mfenced separators="|"><mrow><msqrt><mfrac><mi>x</mi><mi>k</mi></mfrac></msqrt><mo>-</mo><mi>k</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mfenced separators="|"><mrow><mfrac><mn>1</mn><msqrt><mi>k</mi></msqrt></mfrac><mfrac><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>k</mi><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac></mrow></mfenced><mn>0</mn><mfrac><mn>1</mn><mi>k</mi></mfrac></msubsup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>2</mn><mrow><mn>3</mn><msup><mi>k</mi><mn>2</mn></msup></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><msup><mi>k</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mo>&#177;</mo><msqrt><mfrac><mn>1</mn><mn>3</mn></mfrac></msqrt></math></p><p>But, given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#62;</mo><mn>0</mn></math>

So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>.</mo></math></p>

</details>

---

### Q105. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>y</mi></mrow></mfenced><mo>:</mo><mi>&#160;</mi><mn>0</mn><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mi>x</mi><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced><mo>+</mo><mn>1</mn><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn><mo>}</mo></math> in sq. units, is

**Options:**

- **(A)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mn>2</mn></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p> </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/vizujsdugodmmsdjxqsqdybdqsrbnxrxedvxxcloeyknfvthcs.png" />

Area enclosed <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></munderover><mfenced separators="|"><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math>

<math><mo>=</mo><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>0</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup></math>

<math><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q106. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The area (in sq. units) bounded by the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>,</mo></math> the tangent at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> to it and the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>14</mn><mn>3</mn></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>32</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>56</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi>x</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7eb83742-796c-4cbe-bd65-e1dd259c8487-image.png" style="width: 345px; height: 431px;" /></p><p><math><mo>&#8756;</mo></math> Slope of tangent at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> is</p><p><math><mi>m</mi><mo>=</mo><mn>4</mn></math></p><p><math><mo>&#8756;</mo></math> Equation of tangent is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>4</mn><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math><mo>&#8756;</mo></math> Point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>&#8801;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mn>5</mn></mrow></mfenced></math></p><p><math><mo>&#8756;</mo></math> Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#916;</mi><mi>P</mi><mi>T</mi><mi>M</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>8</mn></math></p><p>Area of curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>A</mi><mi>M</mi><mi>P</mi><mo>=</mo><msubsup><mo stretchy="true">&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></msubsup><msqrt><mi>y</mi><mo>+</mo><mn>1</mn></msqrt><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msubsup><mfenced close="]" open="[" separators="|"><msup><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mfenced><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></msubsup><mo>=</mo><mfrac><mn>16</mn><mn>3</mn></mfrac></math></p><p><math><mo>&#8756;</mo></math> Required shaded area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><mo>-</mo><mfrac><mn>16</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q107. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If the area of the region bounded by the curves, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></math> and the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>t</mi><mfenced separators="|"><mrow><mi>t</mi><mo>&#62;</mo><mn>1</mn></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mo>&#160;</mo><mi>unit</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> is equal to

**Options:**

- **(A)** <math><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></math>
- **(B)** <math><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></math>
- **(C)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></math>**

**Detailed Solution:**

<p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8747;</mo><mi>0</mi><mn>1</mn></munderover><msup><mi>x</mi><mn>2</mn></msup><mi>d</mi><mi>x</mi><mo>+</mo><munderover><mo>&#8747;</mo><mi>1</mi><mi>t</mi></munderover><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mn>1</mn></math>

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9e82d627-5029-4a48-8ee7-61db79e14f6b-image.png" style="width: 298px; height: 200px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mi>ln</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>t</mi><mo>=</mo><msup><mi>e</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></math></p>

</details>

---

### Q108. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>:</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn><mo>,&#160;</mo><mi>y</mi><mo>&#8805;</mo><mn>0</mn><mo>,&#160;</mo><mi>y</mi><mo>&#8805;</mo><mi>x</mi><mo>-</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8804;</mo><msqrt><mi>x</mi></msqrt><mo>}</mo></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mi> </mi><mfrac><mrow><mn>8</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mi> </mi><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mi> </mi><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi> </mi><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e314d7d7-eec7-4df2-a9bf-e692c62570af-image.png" style="width: 400px; height: 244px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msqrt><mi>x</mi></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>x</mi></msqrt><mo>=</mo><mi>x</mi><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msqrt><mi>x</mi></msqrt><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mo>(</mo><msqrt><mi>x</mi></msqrt><mo>)</mo><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msqrt><mi>x</mi></msqrt><mo>-</mo><mn>2</mn><mo>)</mo><mo>(</mo><msqrt><mi>x</mi></msqrt><mo>+</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>x</mi></msqrt><mo>=</mo><mn>2</mn><mo>&rArr;</mo><mi>x</mi><mo>=</mo><mn>4</mn></math>
Therefore, the area of the region is
<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&int;</mo><mn>0</mn><mn>4</mn></msubsup><msqrt><mi>x</mi></msqrt><mi>d</mi><mi>x</mi><mo>-</mo><mo> </mo><mi>Area</mi><mo> </mo><mi>of</mi><mo> </mo><mo>∆</mo><mi>A</mi><mi>B</mi><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><msubsup><menclose notation="left"><mo> </mo></menclose><mn>0</mn><mn>4</mn></msubsup><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&times;</mo><mn>2</mn><mo>&times;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&times;</mo><msup><mn>4</mn><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>16</mn><mn>3</mn></mfrac><mo>-</mo><mn>2</mn><mo>=</mo><mfrac><mn>10</mn><mn>3</mn></mfrac><mi>sq</mi><mo>.</mo><mo> </mo><mi>unit</mi></math></p>

</details>

---

### Q109. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the smaller portion enclosed between the curves, <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn></math> and <math><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>3</mn><mi>x</mi></math>, is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bcd8a015-5b77-45d1-adf6-ed7d722cf1d9-image.png" style="width: 293px; height: 230px;" /></p><p>To find point of intersection, eliminate <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> from both the equation, we get

<math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>4</mn><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>=</mo><mn>1</mn></math>

Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><msqrt><mn>3</mn></msqrt><mo>&#183;</mo><msqrt><mi>x</mi></msqrt><mo>&#183;</mo><mi>d</mi><mi>x</mi><mo>+</mo><munderover><mo>&#8747;</mo><mn>1</mn><mn>2</mn></munderover><msqrt><mn>4</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>&#183;</mo><mi>d</mi><mi>x</mi></mrow></mfenced><mo>&#215;</mo><mn>2</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><msqrt><mn>3</mn></msqrt><msubsup><mfenced separators="|"><mfrac><msup><mi>x</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mfrac><mn>3</mn><mn>2</mn></mfrac></mfrac></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>+</mo><msubsup><mfenced separators="|"><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><msqrt><mn>4</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup></mrow></mfenced><mo>&#215;</mo><mn>2</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><msqrt><mn>3</mn></msqrt><mfenced separators="|"><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mo>+</mo><mfenced close="}" open="{" separators="|"><mrow><mn>2</mn><mo>&#183;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mfenced separators="|"><mrow><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>&#215;</mo><mn>2</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>&#215;</mo><mn>2</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>&#215;</mo><mn>2</mn><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math> sq. units</p>

</details>

---

### Q110. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region described by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mo>&#160;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>2</mn><mi>x</mi><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mi>y</mi><mo>&#8805;</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>32</mn></mfrac><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mi>units</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mrow><mn>3</mn><mn>2</mn></mrow></mfrac><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mi>units</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mrow><mn>6</mn><mn>4</mn></mrow></mfrac><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mi>units</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><mrow><mn>6</mn><mn>4</mn></mrow></mfrac><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mi>units</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>32</mn></mfrac><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mi>units</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7bde306a-69b3-4e64-8d80-b7610626528a-image.png" style="width: 303px; height: 250px;" /> </p><p>Let us find the points intersections of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mn>0</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>8</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8658;</mi><mo>&#160;</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;&#8658;</mo><mi>y</mi><mo>=</mo><mn>4</mn><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>-</mo><mn>1</mn><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#8658;</mo><mi>A</mi><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>&#160;&#8658;</mo><mi>y</mi><mo>=</mo><mn>4</mn><mfenced><mfrac><mn>1</mn><mn>8</mn></mfrac></mfenced><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>&#8658;</mo><mi>B</mi><mfenced><mrow><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>8</mn></mfrac></msubsup><msqrt><mn>2</mn><mi>x</mi></msqrt><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><msqrt><mn>2</mn></msqrt><msubsup><mfenced close="]" open="["><mfrac><msup><mi>x</mi><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></msup><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></mfrac></mfenced><mn>0</mn><mfrac><mn>1</mn><mn>8</mn></mfrac></msubsup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>32</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>24</mn></mfrac><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>32</mn></mfrac><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mi>units</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><msqrt><mn>2</mn><mi>x</mi></msqrt><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><msqrt><mn>2</mn></msqrt><msubsup><mfenced close="]" open="["><mfrac><msup><mi>x</mi><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></msup><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></mfrac></mfenced><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>5</mn><mn>24</mn></mfrac><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mi>units</mi></math></p><p>Therefore, the required area is, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><mn>24</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>32</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>24</mn></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>32</mn></mfrac><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mi>units</mi></math></p>

</details>

---

### Q111. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo></math>in square units<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo></math> above the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis bounded by the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>tan</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math> and the tangent to the curve at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>log</mi><mn>2</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mi>log</mi><mn>2</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mi>log</mi><mn>2</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>log</mi><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>log</mi><mn>2</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p>The given curve is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>tan</mi><mi>x</mi></math> and at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>tan</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>1</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>s</mi><mi>e</mi><msup><mi>c</mi><mn>2</mn></msup><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mrow><mi>x</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></msub><mo>=</mo><mi>s</mi><mi>e</mi><msup><mi>c</mi><mn>2</mn></msup><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><msup><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mn>2</mn></msup><mo>=</mo><mn>2</mn></math></p><p>We know that the equation of the tangent to a curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> at a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub><mo>=</mo><msub><mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mrow><mi>x</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></msub><mfenced><mrow><mi>x</mi><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow></mfenced></math></p><p>Hence, the equation of the tangent to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>tan</mi><mi>x</mi></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>-</mo><mn>1</mn><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>=</mo><mn>2</mn><mi>x</mi></math></p><p>To find the point where this line cuts the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> to get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Thus, the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8801;</mo><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>.</mo></math></p><p>Now, the graph for the given information is</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/73283292-fd4f-4e8d-ac0f-9933576f6d5d-Untitled-tanx.png" style="width: 221px; height: 250px;" /></p><p>And, the required Area

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></msubsup><mfenced separators="|"><mrow><mi>tan</mi><mi>x</mi></mrow></mfenced><mi mathvariant="normal">d</mi><mi>x</mi><mo>-</mo><mi>a</mi><mi>r</mi><mfenced separators="|"><mrow><mo>&#8710;</mo><mi>P</mi><mi>A</mi><mi>B</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mi>log</mi><mfenced separators="|"><mrow><mi>sec</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></msubsup><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfenced><mrow><mi>P</mi><mi>B</mi><mo>&#215;</mo><mi>A</mi><mi>B</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><mi>log</mi><mfenced separators="|"><mrow><mi>sec</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>-</mo><mi>log</mi><mfenced separators="|"><mrow><mi>sec</mi><mn>0</mn></mrow></mfenced></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mfenced separators="|"><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mi>log</mi><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mo>-</mo><mi>log</mi><mfenced><mn>1</mn></mfenced></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mi>log</mi><msup><mfenced><mn>2</mn></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><mn>0</mn></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>log</mi><mn>2</mn><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>log</mi><mn>2</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math> sq units.</p>

</details>

---

### Q112. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>4</mn><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>-</mo><mn>2</mn><mi>x</mi><mo>&#8805;</mo><mo>-</mo><mn>4</mn></mrow></mfenced></math>. The area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> in square units is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>&#8722;</mo><mn>4</mn><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mo>=</mo><mi>y</mi><mo>+</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Solving equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>,</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>4</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn></math> and if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/402d0597-708d-477c-8c76-2b2559f9b168-image.png" style="width: 320px; height: 266px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mrow><munderover><mo>&#8747;</mo><mn>0</mn><mn>4</mn></munderover><mfenced><msqrt><mn>4</mn><mi>x</mi></msqrt></mfenced><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><msqrt><mn>4</mn><mi>x</mi></msqrt><mi>d</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mfrac><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mfrac><mn>3</mn><mn>2</mn></mfrac></mfrac></mfenced><mn>0</mn><mn>4</mn></msubsup><mo>-</mo><mn>4</mn><mo>+</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mfrac><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mfrac><mn>3</mn><mn>2</mn></mfrac></mfrac></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mfenced close="]" open="["><mn>8</mn></mfenced><mo>-</mo><mn>4</mn><mo>+</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mfenced close="]" open="["><mn>1</mn></mfenced><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>3</mn><mn>6</mn></mrow><mn>3</mn></mfrac><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn></math></p>

</details>

---

### Q113. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. unit) of the region described by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>1</mn><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mi>&#960;</mi> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>-</mo> <mfrac> <mrow> <mn>4</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3847616a-4993-42b1-9ca7-a4b781ff36c9-image.png" style="width: 261px; height: 246px;" />
Area of shaded region <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> area of semicircle <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo></math> area of region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mo>&#183;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><msubsup><mfenced close="]" open="["><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math> <mrow> <mo>=</mo> <mfrac> <mrow> <mi>&#960;</mi> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>+</mo> <mfrac> <mrow> <mn>4</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </math> sq. unit</p>

</details>

---

### Q114. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The area under the curve $y=|\cos x-\sin x|$, $0 \leq x \leq \frac{\pi}{2}$, and above $x$-axis is :

**Options:**

- **(A)** $2 \sqrt{2}$
- **(B)** $2 \sqrt{2}-2$
- **(C)** $2 \sqrt{2}+2$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \sqrt{2}-2$**

**Detailed Solution:**

$$
\text { } y=|\cos x-\sin x|
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/atKCB74ZkroXBJdbLPn56sHqx0yarr6ySaTBFMpxDh4.original.fullsize.png">

$$
\begin{aligned}
\text { Required area } & =2 \int_0^{\pi / 4}(\cos x-\sin x) d x \\
& =2\left[\sin x+\cos x 0_0^{\pi / 4}\right] \\
& =2\left[\frac{2}{\sqrt{2}}-1\right]=(2 \sqrt{2}-2) \text { sq. units }
\end{aligned}
$$

</details>

---

### Q115. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The area of the region (in sq. units), in the first quadrant bounded by the parabola $y=9 x^2$ and the lines $x=0, y=1$ and $y=4$, is :

**Options:**

- **(A)** $7 / 9$
- **(B)** $14 / 3$
- **(C)** $7 / 3$
- **(D)** $14 / 9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $14 / 9$**

**Detailed Solution:**

$$
\begin{aligned}
& \text { Required area }=\int_{y=1}^4 \sqrt{\frac{y}{9}} d y \\
& =\frac{1}{3} \int_{y=1}^4 y^{1 / 2} d y=\frac{1}{3} \times\left.\frac{2}{3}\left(y^{3 / 2}\right)\right|_1 ^4 \\
& =\frac{2}{9}\left[\left(4^{1 / 2}\right)^3-\left(1^{1 / 2}\right)^3\right]=\frac{2}{9}[8-1]
\end{aligned}
$$

$$
=\frac{2}{9} \times 7=\frac{14}{9} \text { sq. units. }
$$

</details>

---

### Q116. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The area bounded by the curve $y=\ln (x)$ and the lines $y=0, y=\ln (3)$ and $x=0$ is equal to:

**Options:**

- **(A)** 3
- **(B)** $3 \ln (3)-2$
- **(C)** $3 \ln (3)+2$
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2**

**Detailed Solution:**

To find the point of intersection of curves
$$
\begin{aligned}
& y=\ln (x) \text { and } y=\ln (3), \text { put } \ln (x)=\ln (3) \\
\Rightarrow & \ln (x)-\ln (3)=0 \\
\Rightarrow & \ln (x)-\ln (3)=\ln (1) \\
\Rightarrow & \frac{x}{3}=1, \Rightarrow x=3
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/TCSAheZShxa-gIwL3bXzTJ7hXNJ59QnJynq4IRjt12M.original.fullsize.png">

$\begin{aligned} \text { Required area } & =\int_0^3 \ln (3) d x-\int_1^3 \ln (x) d x \\ = & {[x \ln (3)]_0^3-\left[x \ln (x)-x_1^3=2\right.}\end{aligned}$

</details>

---

### Q117. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `2`

<p>The area (in square units) bounded by the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mi>=</mi><msqrt><mi>x</mi></msqrt><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>y</mi><mo>-</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>-axis and lying in the first quadrant is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mn>8</mn><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mo>&#160;</mo><mi>units</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mn>7</mn></mrow><mn>4</mn></mfrac><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mo>&#160;</mo><mi>units</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mo>&#160;</mo><mi>units</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mn>6</mn><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mo>&#160;</mo><mi>units</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mo>&#160;</mo><mi>units</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c59486df-fadc-4ac9-99fb-f6e281949caf-image.png" style="width: 303px; height: 230px;" />
First draw the given curves and represent the required area.

Eliminate <math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">x</mo></math> to find point of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msqrt><mi>x</mi></msqrt></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">2</mi><mi>y</mi><mo>-</mo><mi>x</mi><mo>+</mo><mi mathvariant="normal">3</mi><mo>=</mo><mi mathvariant="normal">0</mi></math>

<math><mo>&#8658;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mi>-</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>Required area <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mn>9</mn></munderover><msqrt><mi>x</mi></msqrt><mi>d</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>3</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mfenced close="]" open="[" separators="|"><mrow><mfrac><msup><mi>x</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mfrac><mn>3</mn><mn>2</mn></mfrac></mfrac><mi>&#160;</mi></mrow></mfenced><mn>0</mn><mn>9</mn></msubsup><mo>-</mo><mn>9</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi mathvariant="normal">A</mi><mo>=</mo><mo>-</mo><mn>9</mn></math></p><p>Hence, area is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mo>&#160;</mo><mi>units</mi></math></p>

</details>

---

### Q118. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `2`

The area bounded by the parabola $y^2=4 x$ and the line $2 x-3 y+4=0$, in square unit, is

**Options:**

- **(A)** $\frac{2}{5}$
- **(B)** $\frac{1}{3}$
- **(C)** 1
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{3}$**

**Detailed Solution:**

Intersecting points are $x=1,4$
$$
\begin{aligned}
& \therefore \text { Required area }=\int_1^4\left[2 \sqrt{x}-\left(\frac{2 x+4}{3}\right)\right] d x \\
& =\left.\frac{2 x^{3 / 2}}{3 / 2}\right|_1 ^4-\left.\frac{2 x^2}{3 \times 2}\right|_1 ^4-\left.\frac{4}{3} x\right|_1 ^4
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{4}{3}\left(4^{3 / 2}-1^{3 / 2}\right)-\frac{1}{3}(16-1)\left[\frac{4}{3}(4)-\frac{4}{3}\right] \\
& =\frac{4}{3}(7)-5-4=\frac{28}{3}-9=\frac{28-27}{3}=\frac{1}{3}
\end{aligned}
$$

</details>

---

### Q119. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `2`

If a straight line $y-x=2$ divides the region $x^2+y^2 \leq 4$ into two parts, then the ratio of the area of the smaller part to the area of the greater part is

**Options:**

- **(A)** $3 \pi-8: \pi+8$
- **(B)** $\pi-3: 3 \pi+3$
- **(C)** $3 \pi-4: \pi+4$
- **(D)** $\pi-2: 3 \pi+2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\pi-2: 3 \pi+2$**

**Detailed Solution:**

Let I be the smaller portion and II be the greater portion of the given figure then,
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/JbvFxsNE9Uu0hcprLR8MOp72G0CtZTy30tjJWmkQXzQ.original.fullsize.png">

Area of $I=\int_{-2}^0\left[\sqrt{4-x^2}-(x+2] d x\right.$
$$
\begin{aligned}
& =\left[\frac{x}{2} \sqrt{4-x^2}+\frac{4}{2} \sin ^{-1}\left(\frac{x}{2}\right)\right]_{-2}^0-\left[\frac{x^2}{2}+2 x\right]_{-2}^0 \\
& =\left[2 \sin ^{-1}(-1)\right]-\left[-\frac{4}{2}+4\right]=2 \times \frac{\pi}{2}-2=\pi-2
\end{aligned}
$$
Now, area of $\mathrm{II}=$ Area of circle $-$ area of $\mathrm{I}$.
$$
\begin{aligned}
& =4 \pi-(\pi-2) \\
& =3 \pi+2
\end{aligned}
$$
Hence, required ratio $=\frac{\text { area of I }}{\text { area of II }}=\frac{\pi-2}{3 \pi+2}$

</details>

---

### Q120. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `2`

The area enclosed by the curves $y=x^2, y=x^3$, $x=0$ and $x=p$, where $p>1$, is $1 / 6$. The $\mathrm{p}$ equals

**Options:**

- **(A)** $8 / 3$
- **(B)** $16 / 3$
- **(C)** 2
- **(D)** $4 / 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4 / 3$**

**Detailed Solution:**

Given curves are $y=x^2$ and $y=x^3$ Also, $x=0$ and $x=p, p>1$ Now, intersecting point is $(1,1)$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/NOjMfJD_aJMO6h0oDJSKErm6eGAjZUmGp__TJw6EFWM.original.fullsize.png">

Required Area
$$
\begin{aligned}
& =\int_0^1\left(x^2-x^3 d x+\int_1^p x^3\right)-x^2 d x \\
& \frac{1}{6}=\frac{x^3}{3}-\left.\frac{x^4}{4}\right|_0 ^1+\frac{x^4}{4}-\left.\frac{x^3}{3}\right|_1 ^p \\
& \Rightarrow \frac{1}{6}=\left(\frac{1}{3}-\frac{1}{4}\right)+\left(\frac{p^4}{4}-\frac{p^3}{3}-\frac{1}{4}+\frac{1}{3}\right) \\
& \Rightarrow \frac{1}{6}-\frac{1}{3}+\frac{1}{4}+\frac{1}{4}-\frac{1}{3}=\frac{3 p^4-4 p^3}{12} \\
& \left.\Rightarrow \frac{p^3(3 p-4}{12}\right)=0 \Rightarrow p^3(3 p-4)=0 \\
& \Rightarrow p=0 \text { or } \frac{4}{3} \\
& \text { Since, it is given that } p>1 \\
& \therefore p \text { can not be zero. } \\
& \text { Hence, } p=\frac{4}{3}
\end{aligned}
$$

</details>

---

### Q121. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `3`

The parabola $y^2=x$ divides the circle $x^2+y^2=2$ into two parts whose areas are in the ratio

**Options:**

- **(A)** $9 \pi+2: 3 \pi-2$
- **(B)** $9 \pi-2: 3 \pi+2$
- **(C)** $7 \pi-2: 2 \pi-3$
- **(D)** $7 \pi+2: 3 \pi+2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $9 \pi-2: 3 \pi+2$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fzwddGOwHhq--X3Tgnp7CruPrIsOB3NvUibsBnhclpE.original.fullsize.png">

$$
\begin{aligned}
& \text { Area of circle }=\pi(\sqrt{2})^2=2 \pi \\
& \text { Area of } O C A D O=2\{\text { Area of } O C A O\} \\
& \quad=2 \text { area of } O C B+\text { area of } B C A\} \\
& =2 \int_0^1 y_p d x+2 \int_1^{\sqrt{2}} y_c d x \\
& \text { where } y_p=\sqrt{x} \text { and } y_c=\sqrt{2-x^2} \\
& \therefore \text { Required Area } \\
& =2 \int \frac{1}{x} d x+2 \int_0^{\sqrt{2}} \sqrt{2-x^2} d x \\
& =2\left[\frac{2}{3} \cdot 1-0\right]+2\left[\frac{x \sqrt{2-x^2}}{2}+\sin ^{-1} \frac{x}{\sqrt{2}}\right]_1^{\sqrt{2}}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{4}{3}+2\left\{\frac{\pi}{2}-\frac{\pi}{4}-\frac{1}{2}\right\}=\frac{4}{3}+2\left\{\frac{\pi}{4}-\frac{1}{2}\right\}=\frac{3 \pi+2}{6} \\
& \text { Bigger area }=2 \pi-\frac{3 \pi+2}{6}=\frac{9 \pi-2}{6} \\
& \therefore \text { Required Ratio }=\frac{9 \pi-2}{3 \pi+2} \text { i.e., } 9 \pi-2: 3 \pi+2
\end{aligned}
$$

</details>

---

### Q122. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `1`

The area bounded between the parabolas $x^2=\frac{y}{4}$ and $x^2=9 y$, and the straight line $y=2$ is

**Options:**

- **(A)** $20 \sqrt{2}$
- **(B)** $\frac{10 \sqrt{2}}{3}$
- **(C)** $\frac{20 \sqrt{2}}{3}$
- **(D)** $10 \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{20 \sqrt{2}}{3}$**

**Detailed Solution:**

Required area
$\begin{aligned}
& A=2\left[\int_0^2\left(3 \sqrt{y}-\frac{\sqrt{y}}{2}\right) d y\right]=2 \int_0^2 \frac{5 \sqrt{y}}{2} d y \\
& =5\left[\frac{y^{3 / 2}}{3 / 2}\right]_0^2=\frac{10}{3}\left[2^{3 / 2}-0\right]=\frac{20 \sqrt{2}}{3}
\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fWHtA4DS4sWU-eu8q4PM8bS_o6_CztJVndJntFL6rpM.original.fullsize.png">

</details>

---

### Q123. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `1`

The area bounded by the curves $y=\cos x$ and $y=\sin x$ between the ordinates $x=0$ and $x=\frac{3 \pi}{2}$ is

**Options:**

- **(A)** $4 \sqrt{2}+2$
- **(B)** $4 \sqrt{2}-1$
- **(C)** $4 \sqrt{2}+1$
- **(D)** $4 \sqrt{2}-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4 \sqrt{2}-2$**

**Detailed Solution:**

$\int_0^{\frac{\pi}{4}}(\cos x-\sin x) d x+\int_{\frac{\pi}{4}}^{\frac{5 \pi}{4}}(\sin x-\cos x) d x+\int_{\frac{5 \pi}{4}}^{\frac{3 \pi}{2}}(\cos x-\sin x)=4 \sqrt{2}-2$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/hDVXhcGrk8n_4SsHJ20WO09-8lTHnbLiTX1G-zOjg2c.original.fullsize.png">

</details>

---

### Q124. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by the parabola $(y-2)^2=x-1$, the tangent to the parabola at the point $(2,3)$ and the $x$-axis is

**Options:**

- **(A)** 3
- **(B)** 6
- **(C)** 9
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 9**

**Detailed Solution:**

Equation of tangent at $(2,3)$ to
$$
\begin{aligned}
& (y-2)^2=x-1 \text { is } S_1=0 \\
& \Rightarrow x-2 y+4=0
\end{aligned}
$$
Required Area $=$ Area of $\triangle O C B+$ Area of OAPD - Area of $\triangle P C D$
$$
\begin{aligned}
& =\frac{1}{2}(4 \times 2)+\int_0^3\left(y^2-4 y+5\right) d y-\frac{1}{2}(1 \times 2) \\
& =4+\left[\frac{y^3}{3}-2 y^2+5 y\right]_0^3-1=4-9-18+15-1 \\
& =28-19=9 \text { sq. units }
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/R4JZ6unjbZ0eLecweDYM2Q5_TFikGBm1Ykf9v2IdkM4.original.fullsize.png">

$$
\text { (or) }
$$

$$
\text { Area }=\int_0^3\left(2 y-4-y^2+4 y-5\right) d y=\int_0^3\left(-y^2+6 y-5\right) d y=-\int_0^3(3-y)^2 d y=\left[\frac{(y-3)^3}{3}\right]_0^3=\frac{27}{3}=9 \text { sq.units }
$$

</details>

---

### Q125. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `2`

The area of the plane region bounded by the curves $x+2 y^2=0$ and $x+3 y^2=1$ is equal to

**Options:**

- **(A)** $\frac{5}{3}$
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{2}{3}$
- **(D)** $\frac{4}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{4}{3}$**

**Detailed Solution:**

Solving the equations we get the points of intersection $(-2,1)$ and $(-2,-1)$
The bounded region is shown as shaded region.
$$
\begin{aligned}
& \text { The required area }=2 \int_0^1\left(1-3 y^2\right)-\left(-2 y^2\right) \\
& =2 \int_0^1\left(1-y^2\right) d y=2\left[y-\frac{y^3}{3}\right]_0^1=2 \times \frac{2}{3}=\frac{4}{3} .
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6ks_u_C7uIfyc-XwmaLvr7-H92Y9SsLT-6bf_vVoZyk.original.fullsize.png">

</details>

---

### Q126. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `2`

The area enclosed between the curves $y^2=x$ and $y=|x|$ is

**Options:**

- **(A)** $2 / 3$
- **(B)** $1$
- **(C)** $1 / 6$
- **(D)** $1 / 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1 / 6$**

**Detailed Solution:**

$A=\int_0^1(\sqrt{x}-x) d x$
$=\left[\frac{2}{3} x^{3 / 2}-\frac{x^2}{2}\right]_0^1$
$=\frac{2}{3}-\frac{1}{2}=\frac{1}{6}$.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/N4iFODxA066V2v36QU3cbbTNBQqtpPsvT5-CnCoXmFc.original.fullsize.png">

</details>

---

### Q127. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)$ be a non-negative continuous function such that the area bounded by the curve $y=f(x), x$-axis and the ordinates $x=\frac{\pi}{4}$ and $x=\beta>\frac{\pi}{4}$ is $\left(\beta \sin \beta+\frac{\pi}{4} \cos \beta+\sqrt{2} \beta\right)$. Then $f\left(\frac{\pi}{2}\right)$ is

**Options:**

- **(A)** $\left(\frac{\pi}{4}+\sqrt{2}-1\right)$
- **(B)** $\left(\frac{\pi}{4}-\sqrt{2}+1\right)$
- **(C)** $\left(1-\frac{\pi}{4}-\sqrt{2}\right)$
- **(D)** $\left(1-\frac{\pi}{4}+\sqrt{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(1-\frac{\pi}{4}+\sqrt{2}\right)$**

**Detailed Solution:**

Given that $\int_{\pi / 4}^\beta f(x) d x=\beta \sin \beta+\frac{\pi}{4} \cos \beta+2 \beta$
Differentiating w. r. t $\beta$
$f(\beta)=\beta \cos \beta+\sin \beta-\frac{\pi}{4} \sin \beta+\sqrt{2}$
$f\left(\frac{\pi}{2}\right)=\left(1-\frac{\pi}{4}\right) \sin \frac{\pi}{2}+\sqrt{2}=1-\frac{\pi}{2}+\sqrt{2}$.

</details>

---

### Q128. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

The parabolas $\mathrm{y}^2=4 \mathrm{x}$ and $\mathrm{x}^2=4 \mathrm{y}$ divide the square region bounded by the lines $\mathrm{x}=$ $4, y=4$ and the coordinate axes. If $S_1, S_2, S_3$ are respectively the areas of these parts numbered from top to bottom; then $\mathrm{S}_1: \mathrm{S}_2: \mathrm{S}_3$ is

**Options:**

- **(A)** $1: 2: 1$
- **(B)** $1: 2: 3$
- **(C)** $2: 1: 2$
- **(D)** $1: 1: 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1: 1: 1$**

**Detailed Solution:**

$\mathrm{y}^2=4 \mathrm{x}$ and $\mathrm{x}^2=4 \mathrm{y}$ are symmetric about line $\mathrm{y}=\mathrm{x}$
$\Rightarrow$ area bounded between $y^2=4 x$ and $y=x$ is $\int_0^4(2 \sqrt{x}-x) d x=\frac{8}{3}$
$\Rightarrow \mathrm{A}_{\mathrm{s}_2}=\frac{16}{3}$ and $\mathrm{A}_{\mathrm{s}_1}=\mathrm{A}_{\mathrm{s}_3}=\frac{16}{3}$
$\Rightarrow A_{s_1}: A_{s_2}: A_{s_3}:: 1: 1: 1$.

</details>

---

### Q129. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by the curves $y=|x-2|, x=1, x=3$ and the $x$-axis is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

Area $=\int_1^2(2-x) d x+\int_2^3(x-2) d x=1$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/yt3wxHAfgDRsqLL2O6Zseluz9FcWsK0XGRrcNKrsZDE.original.fullsize.png">

</details>

---

### Q130. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by the curves $y=|x-1|$ and $y=3-|x|$ is

**Options:**

- **(A)** 6 sq. units
- **(B)** 2 sq. units
- **(C)** 3 sq. units
- **(D)** 4 sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4 sq. units**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Br25KL-OShwGlcMedA4xxPAVYHJDjhf3hTTC1fS98Us.original.fullsize.png">

$A=\int_{-1}^0\{(3+x)-(-x+1)\} d x+\int_0^1\{(3-x)-(-x+1)\} d x+\int_1^2\{(3-x)-(-x-1)\} d x$
$=\int_{-1}^0(2+2 x) d x+\int_0^1 2 d x+\int_1^2(4-2 x) d x$
$=\left[2 x-x^2\right]_{-1}^0+[2 x]_0^1+\left[4 x-x^2\right]_1^2$
$=0-(-2+1)+(2-0)+(8-4)-(4-1)$
$=1+2+4-3=4$ sq. units

</details>

---

