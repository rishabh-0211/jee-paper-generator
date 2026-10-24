# MHT CET Mathematics - Area Under Curves

## Topic 3: Area bounded by Miscellaneous Curves

**Total Questions:** 21

---

### Q1. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The area (in sq. units) of the region described by $\left\{(x, y) / y^2 \leq 2 x\right.$ and $\left.y \geq(4 x-1)\right\}$ is

**Options:**

- **(A)** $\frac{15}{64}$
- **(B)** $\frac{9}{32}$
- **(C)** $\frac{7}{32}$
- **(D)** $\frac{5}{64}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{9}{32}$**

**Detailed Solution:**

To find the points of intersection, we solve the equations $y^2 = 2x$ and $y = 4x - 1$ simultaneously.

From the equation of the line, we have $x = \dfrac{y + 1}{4}$.

Substituting this into the equation of the parabola gives:

$y^2 = 2\left(\dfrac{y + 1}{4}\right)$

$2y^2 = y + 1$

$2y^2 - y - 1 = 0$

$(2y + 1)(y - 1) = 0$

This gives the $y$-coordinates of the intersection points as $y = -\dfrac{1}{2}$ and $y = 1$.

The region is bounded by the curves $x = \dfrac{y^2}{2}$ and $x = \dfrac{y + 1}{4}$. For $y \in \left[-\dfrac{1}{2}, 1\right]$, the line lies to the right of the parabola, so $\dfrac{y + 1}{4} \geq \dfrac{y^2}{2}$.

The area $A$ of the region is given by integrating with respect to $y$:

$A = \int_{-1/2}^{1} \left( \dfrac{y + 1}{4} - \dfrac{y^2}{2} \right) dy$

$A = \left[ \dfrac{y^2}{8} + \dfrac{y}{4} - \dfrac{y^3}{6} \right]_{-1/2}^{1}$

Evaluating at the upper limit $y = 1$:

$\dfrac{1}{8} + \dfrac{1}{4} - \dfrac{1}{6} = \dfrac{3 + 6 - 4}{24} = \dfrac{5}{24}$

Evaluating at the lower limit $y = -\dfrac{1}{2}$:

$\dfrac{1}{8}\left(-\dfrac{1}{2}\right)^2 + \dfrac{1}{4}\left(-\dfrac{1}{2}\right) - \dfrac{1}{6}\left(-\dfrac{1}{2}\right)^3 = \dfrac{1}{32} - \dfrac{1}{8} + \dfrac{1}{48}$

The least common multiple of $32, 8,$ and $48$ is $96$.

$\dfrac{3}{96} - \dfrac{12}{96} + \dfrac{2}{96} = -\dfrac{7}{96}$

Subtracting the lower limit value from the upper limit value:

$A = \dfrac{5}{24} - \left( -\dfrac{7}{96} \right) = \dfrac{20}{96} + \dfrac{7}{96} = \dfrac{27}{96}$

Simplifying the fraction gives:

$A = \dfrac{9}{32}$ sq. units.

Answer: $\frac{9}{32}$

</details>

---

### Q2. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The area of the region lying in the first quadrant by $y=4 x^2, x=0, y=2, y=4$ is

**Options:**

- **(A)** $\frac{1}{6}[8-2 \sqrt{2}]$ sq.units
- **(B)** $\frac{1}{3}[8-2 \sqrt{2}]$ sq.units
- **(C)** $[8-2 \sqrt{2}]$ sq.units
- **(D)** $[8+2 \sqrt{2}]$ sq.units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{3}[8-2 \sqrt{2}]$ sq.units**

**Detailed Solution:**

The given curve is $y = 4x^2$. In the first quadrant, $x = \dfrac{\sqrt{y}}{2}$.

The area of the region bounded by the curve, the y-axis ($x=0$), and the lines $y=2$ and $y=4$ is given by:

$A = \int_{2}^{4} x \, dy$

$A = \int_{2}^{4} \dfrac{\sqrt{y}}{2} \, dy$

$A = \dfrac{1}{2} \left[ \dfrac{y^{3/2}}{3/2} \right]_{2}^{4}$

$A = \dfrac{1}{3} \left[ 4^{3/2} - 2^{3/2} \right]$

$A = \dfrac{1}{3} [8 - 2\sqrt{2}]$ sq. units.

Answer: $\frac{1}{3}[8-2 \sqrt{2}]$ sq.units

</details>

---

### Q3. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The area (in sq. units) of the region $\left\{(x, y) / x \geq 0, x+y \leq 3, x^2 \leq 4 y\right.$ and $\left.y \leq 1+\sqrt{x}\right\}$ is

**Options:**

- **(A)** $\dfrac{9}{2}$
- **(B)** $\dfrac{3}{2}$
- **(C)** $\dfrac{7}{2}$
- **(D)** $\dfrac{5}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{5}{2}$**

**Detailed Solution:**

The given region is bounded by the curves $y = \dfrac{x^2}{4}$, $y = 3 - x$, and $y = 1 + \sqrt{x}$ for $x \geq 0$.

First, we find the points of intersection of the upper bounding curves $y = 1 + \sqrt{x}$ and $y = 3 - x$:
$1 + \sqrt{x} = 3 - x \Rightarrow x + \sqrt{x} - 2 = 0$
$(\sqrt{x} + 2)(\sqrt{x} - 1) = 0 \Rightarrow \sqrt{x} = 1 \Rightarrow x = 1$

Next, we find the intersection of $y = 3 - x$ and the lower bounding curve $y = \dfrac{x^2}{4}$:
$3 - x = \dfrac{x^2}{4} \Rightarrow x^2 + 4x - 12 = 0$
$(x + 6)(x - 2) = 0 \Rightarrow x = 2$ (since $x \geq 0$)

From the intersections, the region is bounded above by $y = 1 + \sqrt{x}$ for $0 \leq x \leq 1$ and by $y = 3 - x$ for $1 \leq x \leq 2$. The region is bounded below by $y = \dfrac{x^2}{4}$ for $0 \leq x \leq 2$.

The required area $A$ is given by the sum of two integrals:
$A = \int_0^1 \left(1 + \sqrt{x} - \dfrac{x^2}{4}\right) dx + \int_1^2 \left(3 - x - \dfrac{x^2}{4}\right) dx$

Evaluating the first integral:
$\int_0^1 \left(1 + x^{1/2} - \dfrac{x^2}{4}\right) dx = \left[ x + \dfrac{2}{3}x^{3/2} - \dfrac{x^3}{12} \right]_0^1 = 1 + \dfrac{2}{3} - \dfrac{1}{12} = \dfrac{19}{12}$

Evaluating the second integral:
$\int_1^2 \left(3 - x - \dfrac{x^2}{4}\right) dx = \left[ 3x - \dfrac{x^2}{2} - \dfrac{x^3}{12} \right]_1^2$
$= \left(6 - 2 - \dfrac{8}{12}\right) - \left(3 - \dfrac{1}{2} - \dfrac{1}{12}\right)$
$= \dfrac{10}{3} - \dfrac{29}{12} = \dfrac{40}{12} - \dfrac{29}{12} = \dfrac{11}{12}$

Adding the two areas:
$A = \dfrac{19}{12} + \dfrac{11}{12} = \dfrac{30}{12} = \dfrac{5}{2}$ sq. units.

Answer: $\dfrac{5}{2}$

</details>

---

### Q4. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Area (in sq.units) lying in the first quadrant and bounded by the circle $x^2+y^2=4$ and the lines $x=0$ and $x=2$ is

**Options:**

- **(A)** $\pi$
- **(B)** $\dfrac{\pi}{2}$
- **(C)** $\dfrac{\pi}{3}$.
- **(D)** $\dfrac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\pi$**

**Detailed Solution:**

The equation of the circle is $x^2+y^2=4$, which represents a circle with centre at $(0,0)$ and radius $2$.

The required area lies in the first quadrant and is bounded by $x=0$ and $x=2$. This region is exactly one-fourth of the total area of the circle.

Area $= \int_{0}^{2} \sqrt{4-x^2} \, dx$

Area $= \left[ \dfrac{x}{2}\sqrt{4-x^2} + \dfrac{4}{2}\sin^{-1}\left(\dfrac{x}{2}\right) \right]_{0}^{2}$

Area $= \left( 0 + 2\sin^{-1}(1) \right) - \left( 0 + 2\sin^{-1}(0) \right)$

Area $= 2 \times \dfrac{\pi}{2} = \pi$ sq. units.

Answer: $\pi$

</details>

---

### Q5. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area (in sq. units), in the first quadrant bounded by the curve $y=x^2+2$ and the lines $y=x+1, x=0$ and $x=2$, is

**Options:**

- **(A)** $\dfrac{1}{3}$
- **(B)** $\dfrac{2}{3}$
- **(C)** $\dfrac{5}{3}$
- **(D)** $\dfrac{8}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{8}{3}$**

**Detailed Solution:**

The required area is bounded by the upper curve $y = x^2 + 2$ and the lower curve $y = x + 1$ between $x = 0$ and $x = 2$.

The area $A$ is given by the integral:

$A = \int_{0}^{2} ((x^2 + 2) - (x + 1)) \, dx$

$A = \int_{0}^{2} (x^2 - x + 1) \, dx$

Integrating with respect to $x$:

$A = \left[ \dfrac{x^3}{3} - \dfrac{x^2}{2} + x \right]_{0}^{2}$

Substituting the limits:

$A = \left( \dfrac{8}{3} - \dfrac{4}{2} + 2 \right) - 0$

$A = \dfrac{8}{3} - 2 + 2 = \dfrac{8}{3}$ sq. units.

Answer: $\dfrac{8}{3}$

</details>

---

### Q6. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The area (in sq. units) bounded by the curves $y=(x+1)^2, y=(x-1)^2$ and the line $y=\dfrac{1}{4}$ is

**Options:**

- **(A)** $\dfrac{2}{3}$
- **(B)** $\dfrac{1}{6}$
- **(C)** $\dfrac{1}{3}$
- **(D)** $\dfrac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{3}$**

**Detailed Solution:**

The given curves are $y = (x+1)^2$, $y = (x-1)^2$, and the line $y = \dfrac{1}{4}$.

First, finding the point of intersection of the two parabolas:

$(x+1)^2 = (x-1)^2$

$x^2 + 2x + 1 = x^2 - 2x + 1 \Rightarrow 4x = 0 \Rightarrow x = 0$

At $x = 0$, $y = 1$. Thus, the parabolas intersect at $(0, 1)$.

Next, finding the points of intersection of the parabolas with the line $y = \dfrac{1}{4}$:

For $y = (x+1)^2$, $(x+1)^2 = \dfrac{1}{4} \Rightarrow x+1 = \pm \dfrac{1}{2} \Rightarrow x = -\dfrac{1}{2}$ or $x = -\dfrac{3}{2}$. The relevant intersection for the bounded region is $x = -\dfrac{1}{2}$.

For $y = (x-1)^2$, $(x-1)^2 = \dfrac{1}{4} \Rightarrow x-1 = \pm \dfrac{1}{2} \Rightarrow x = \dfrac{1}{2}$ or $x = \dfrac{3}{2}$. The relevant intersection is $x = \dfrac{1}{2}$.

The bounded region is symmetric about the y-axis, lying between $x = -\dfrac{1}{2}$ and $x = \dfrac{1}{2}$, bounded above by the parabolas and below by $y = \dfrac{1}{4}$.

The required area $A$ can be calculated by integrating with respect to $x$:

$A = \int_{-1/2}^{0} \left( (x+1)^2 - \dfrac{1}{4} \right) dx + \int_{0}^{1/2} \left( (x-1)^2 - \dfrac{1}{4} \right) dx$

By symmetry, this simplifies to:

$A = 2 \int_{0}^{1/2} \left( (x-1)^2 - \dfrac{1}{4} \right) dx$

Evaluating the integral:

$A = 2 \left[ \dfrac{(x-1)^3}{3} - \dfrac{x}{4} \right]_{0}^{1/2}$

$A = 2 \left( \left( \dfrac{(-1/2)^3}{3} - \dfrac{1/2}{4} \right) - \left( \dfrac{(-1)^3}{3} - 0 \right) \right)$

$A = 2 \left( \left( -\dfrac{1}{24} - \dfrac{1}{8} \right) - \left( -\dfrac{1}{3} \right) \right)$

$A = 2 \left( -\dfrac{4}{24} + \dfrac{1}{3} \right) = 2 \left( -\dfrac{1}{6} + \dfrac{1}{3} \right)$

$A = 2 \left( \dfrac{1}{6} \right) = \dfrac{1}{3}$ sq. units.

Answer: $\dfrac{1}{3}$

</details>

---

### Q7. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area (in square units) in the first quadrant bounded by the curve $y=x^2+2$ and the lines $y=x+1, x=0$ and $x=3$, is

**Options:**

- **(A)** $\dfrac{15}{4}$
- **(B)** $\dfrac{21}{2}$
- **(C)** $\dfrac{17}{4}$
- **(D)** $\dfrac{15}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{15}{2}$**

**Detailed Solution:**

The given curves are $y = x^2 + 2$ and $y = x + 1$.

To find the points of intersection, we equate the two equations:

$x^2 + 2 = x + 1$

$x^2 - x + 1 = 0$

Since the discriminant $D = (-1)^2 - 4(1)(1) = -3 < 0$, the curves do not intersect. For all real $x$, $x^2 + 2 > x + 1$, meaning the parabola lies strictly above the line.

The required area is bounded by these curves between the vertical lines $x = 0$ and $x = 3$. Both curves lie in the first quadrant for $x \in [0, 3]$.

The area $A$ is given by the integral of the upper curve minus the lower curve:

$A = \int_{0}^{3} ((x^2 + 2) - (x + 1)) dx$

$A = \int_{0}^{3} (x^2 - x + 1) dx$

Integrating with respect to $x$:

$A = \left[ \dfrac{x^3}{3} - \dfrac{x^2}{2} + x \right]_{0}^{3}$

$A = \left( \dfrac{3^3}{3} - \dfrac{3^2}{2} + 3 \right) - 0$

$A = 9 - \dfrac{9}{2} + 3$

$A = 12 - \dfrac{9}{2} = \dfrac{24 - 9}{2} = \dfrac{15}{2}$

Answer: $\dfrac{15}{2}$

</details>

---

### Q8. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The shaded region in the following figure is the solution set of the inequations
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/tji-nDg3PHdmwO_FEGiwvX3yYCZKhs-n7NlpdTIFf8c.original.fullsize_2.png"/>

**Options:**

- **(A)** $\begin{aligned} & x+2 y \geq 6,5 x+3 y \geq 15, x \leq 7, y \leq 6, x \\ & y \geq 0\end{aligned}$
- **(B)** $\begin{aligned} & x+2 y \leq 6,5 x+3 y \geq 15, x \leq 7, y \leq 6, x \text {, } \\ & y \geq 0\end{aligned}$
- **(C)** $\begin{aligned} & x+2 y \geq 6,5 x+3 y \leq 15, x \geq 7, y \leq 6, x, \\ & y \geq 0\end{aligned}$
- **(D)** $\begin{aligned} & x+2 y \leq 6,5 x+3 y \leq 15, x \leq 7, y \geq 6, x, \\ & y \geq 0\end{aligned}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\begin{aligned} & x+2 y \geq 6,5 x+3 y \geq 15, x \leq 7, y \leq 6, x \\ & y \geq 0\end{aligned}$**

**Detailed Solution:**

From the given graph, we can identify the boundary lines of the shaded region.

The line passing through $(0, 5)$ and $(3, 0)$ has the equation $\dfrac{x}{3} + \dfrac{y}{5} = 1 \Rightarrow 5x + 3y = 15$. The shaded region lies above this line (away from the origin), so the inequality is $5x + 3y \geq 15$.

The line passing through $(0, 3)$ and $(6, 0)$ has the equation $\dfrac{x}{6} + \dfrac{y}{3} = 1 \Rightarrow x + 2y = 6$. The shaded region lies above this line, so the inequality is $x + 2y \geq 6$.

The vertical boundary line is at $x = 7$, and the shaded region is to its left, giving $x \leq 7$.

The horizontal boundary line is at $y = 6$, and the shaded region is below it, giving $y \leq 6$.

Since the region is in the first quadrant, we also have $x \geq 0$ and $y \geq 0$.

Combining all these, the system of inequalities is $x + 2y \geq 6$, $5x + 3y \geq 15$, $x \leq 7$, $y \leq 6$, $x, y \geq 0$.

Answer: $\begin{aligned} & x+2 y \geq 6,5 x+3 y \geq 15, x \leq 7, y \leq 6, x \\ & y \geq 0\end{aligned}$

</details>

---

### Q9. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area (in sq. units) bounded by the curves $y=\sqrt{x}, 2 y-x+3=0, \mathrm{X}$-axis and lying in the first quadrant is

**Options:**

- **(A)** 36
- **(B)** 18
- **(C)** $\dfrac{27}{4}$
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 9**

**Detailed Solution:**

The given curves are $y = \sqrt{x}$ and $2y - x + 3 = 0$.

To find the point of intersection, substitute $x = y^2$ into the equation of the line:

$2y - y^2 + 3 = 0$

$y^2 - 2y - 3 = 0$

$(y - 3)(y + 1) = 0$

Since the region lies in the first quadrant, $y \ge 0$, which gives $y = 3$. The corresponding $x$-coordinate is $x = 9$.

The line $2y - x + 3 = 0$ intersects the X-axis at $x = 3$.

The required area can be found by integrating with respect to $y$ from $y = 0$ to $y = 3$. The right boundary is the line $x = 2y + 3$ and the left boundary is the curve $x = y^2$.

Required Area $= \int_{0}^{3} ((2y + 3) - y^2) dy$

$= \left[ y^2 + 3y - \dfrac{y^3}{3} \right]_{0}^{3}$

$= \left( 3^2 + 3(3) - \dfrac{3^3}{3} \right) - 0$

$= 9 + 9 - 9 = 9$ sq. units.

Answer: 9

</details>

---

### Q10. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The area of the region bounded by the curves $y=\mathrm{e}^x, y=\log x$ and lines $x=1, x=2$ is

**Options:**

- **(A)** $(\mathrm{e}-1)^2 \mathrm{sq}$. units
- **(B)** $\left(\mathrm{e}^2-\mathrm{e}+1\right) \mathrm{sq}$. units
- **(C)** $\left(\mathrm{e}^2-\mathrm{e}+1-2 \log 2\right) \mathrm{sq}$. units
- **(D)** $\left(\mathrm{e}^2+\mathrm{e}-2 \log 2\right)$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(\mathrm{e}^2-\mathrm{e}+1-2 \log 2\right) \mathrm{sq}$. units**

**Detailed Solution:**

$\begin{aligned} & \text { Required Area } \\ & =\int_1^2\left(\mathrm{e}^x-\log x\right) \mathrm{d} x \\ & =\left[\mathrm{e}^x\right]_1^2-\int_1^2 1 \log x \mathrm{~d} x \\ & =\left(\mathrm{e}^2-\mathrm{e}\right)-\left[x \log x-\int_1^2 1 \mathrm{~d} x\right] \\ & =\left(\mathrm{e}^2-\mathrm{e}\right)-[x \log x-x]_1^2 \\ & =\left(\mathrm{e}^2-\mathrm{e}\right)-[(2 \log 2-2)-(1 \log 1-1)] \\ & =\mathrm{e}^2-\mathrm{e}-(2 \log 2-2-0+1) \\ & =\mathrm{e}^2-\mathrm{e}-(2 \log 2-1) \\ & =\left(\mathrm{e}^2-\mathrm{e}+1-2 \log 2\right) \text { sq. units }\end{aligned}$

</details>

---

### Q11. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area bounded by the parabola $\mathrm{y}^2=4 \mathrm{ax}$ and its latus-rectum $x=a$ is

**Options:**

- **(A)** $\frac{8}{3} a^2$ sq. units
- **(B)** $\frac{2}{3} a^2$ sq. units
- **(C)** $\frac{4}{3} a^2$ sq. units
- **(D)** $8 \mathrm{a}^2$ aq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{8}{3} a^2$ sq. units**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/cZ-l0QyjLbU5nUf-fVf9-uO1XITkoVVul_yosu7Hl5o.original.fullsize.png">

Required area is shaded.
Point of intersection of $x=a$ and $y^2=4 a x$, is
$$
y^2=4 a^2 \Rightarrow y= \pm 2 a \text { and } x=a \Rightarrow(a, \pm 2 a)
$$
$$
\begin{aligned}
& \therefore \mathrm{A}=2 \int_0^{\mathrm{a}}(2 \sqrt{\mathrm{a}} \sqrt{\mathrm{x}}) \mathrm{dx} \\
& =4 \sqrt{\mathrm{a}} \int_0^{\mathrm{a}} \mathrm{x}^{\frac{1}{2}} \mathrm{dx}=4 \sqrt{\mathrm{a}}\left[\frac{\mathrm{x}^{\frac{3}{2}}}{\left(\frac{3}{2}\right)}\right]_0^{\mathrm{a}}=(4 \sqrt{\mathrm{a}})\left(\frac{2}{3}\right)(\mathrm{a} \sqrt{\mathrm{a}})=\frac{8}{3} \mathrm{a}^2 \text { sq. units }
\end{aligned}
$$

</details>

---

### Q12. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by the curve $y=\log x, x$ -axis and the lines
$x=1, x=e$ is

**Options:**

- **(A)** $\frac{1}{e}$ Sq. Units
- **(B)** 1 Sq. Units
- **(C)** 4 sq. Units
- **(D)** $\frac{1}{2}$ Sq. Units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1 Sq. Units**

**Detailed Solution:**

Required area is shaded.
$$
\begin{aligned}
\therefore \mathrm{A} &=\int_{1}^{\mathrm{e}} \log \mathrm{x} \mathrm{dx}=\int_{1}^{\mathrm{e}}(\log \mathrm{x})(1) \mathrm{dx} \\
&=[\mathrm{x} \log (\mathrm{x})]_{1}^{\mathrm{e}}-\int_{1}^{\mathrm{e}} \frac{1}{\mathrm{x}} \times \mathrm{x} \mathrm{dx} \\
&=[\mathrm{e}(\log \mathrm{e})-0]-[\mathrm{x}]_{1}^{\mathrm{e}}=\mathrm{e}-(\mathrm{e}-1)=1
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Pn9SweWQ_ssX_Jz38B3_9MKekHY4d3z3LO5K7kZfVUw.original.fullsize.png">

</details>

---

### Q13. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The minimum value of <math><mi>z</mi><mo>=</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>25</mn><mi>y</mi></math> subject to <math><mn>0</mn><mo>≤</mo><mi>x</mi><mo>≤</mo><mn>3</mn><mo>,</mo><mi></mi><mi></mi><mn>0</mn><mo>≤</mo><mi>y</mi><mo>≤</mo><mn>3</mn><mo>,</mo><mi></mi><mi></mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>≥</mo><mn>5</mn></math> is ________

**Options:**

- **(A)** <math><mn>80</mn></math>
- **(B)** <math><mn>95</mn></math>
- **(C)** <math><mn>105</mn></math>
- **(D)** <math><mn>30</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>80</mn></math>**

**Detailed Solution:**

Given, 
Minimize <math><mi>z</mi><mo>=</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>25</mn><mi>y</mi></math>  
Subject to conditions 
<math><mn>0</mn><mo>≤</mo><mi>x</mi><mo>≤</mo><mn>3</mn><mo>,</mo><mi mathvariant="normal"></mi><mn>0</mn><mo>≤</mo><mi>y</mi><mo>≤</mo><mn>3</mn><mo>,</mo><mi mathvariant="normal"></mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>≥</mo><mn>5</mn></math>  
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/adc1c33d-5ccf-4232-9372-9655deff6de5.png"> 
<math><msub><mrow><mi>z</mi></mrow><mrow><mo>(</mo><mn>3,2</mn><mo>)</mo></mrow></msub><mo>=</mo><mn>80</mn><mi mathvariant="normal"></mi><msub><mrow><mi>z</mi></mrow><mrow><mo>(</mo><mn>3,3</mn><mo>)</mo></mrow></msub><mo>=</mo><mn>105</mn><mi mathvariant="normal"></mi><msub><mrow><mi>z</mi></mrow><mrow><mfenced separators="|"><mrow><mn>2,3</mn></mrow></mfenced></mrow></msub><mo>=</mo><mn>95</mn></math>

</details>

---

### Q14. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The maximum value of <math><mi>z</mi><mo>=</mo><mn>9</mn><mi>x</mi><mo>+</mo><mn>11</mn><mi>y</mi></math> subject to <math><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>≤</mo><mn>12</mn><mo>,</mo><mi></mi><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>≤</mo><mn>12</mn><mo>,</mo><mi></mi><mi>x</mi><mo>≥</mo><mn>0</mn><mo>,</mo><mi></mi><mi>y</mi><mo>≥</mo><mn>0</mn></math> is ________

**Options:**

- **(A)** <math><mn>44</mn></math>
- **(B)** <math><mn>54</mn></math>
- **(C)** <math><mn>36</mn></math>
- **(D)** <math><mn>48</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>48</mn></math>**

**Detailed Solution:**

Given: <math><mi>z</mi><mo>=</mo><mn>9</mn><mi>x</mi><mo>+</mo><mn>11</mn><mi>y</mi></math> (Maximize) 
Given: condition <math><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>≤</mo><mn>12</mn></math>  
<math><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>≤</mo><mn>12</mn><mo>,</mo></math> <math><mi>x</mi><mo>≥</mo><mn>0</mn><mo>,</mo><mi></mi><mi>y</mi><mo>≥</mo><mn>0</mn></math>  
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/f1aad6a2-2e49-4c60-9036-4110e18628fc.png"> 
Then 
<math><msub><mrow><mi>z</mi></mrow><mrow><mfenced separators="|"><mrow><mn>0,0</mn></mrow></mfenced></mrow></msub><mo>=</mo><mn>0</mn><msub><mrow><mi>z</mi></mrow><mrow><mfenced separators="|"><mrow><mn>4,0</mn></mrow></mfenced></mrow></msub><mo>=</mo><mn>36</mn></math> , <math><msub><mrow><mi>z</mi></mrow><mrow><mo>(</mo><mn>0,4</mn><mo>)</mo></mrow></msub><mo>=</mo><mn>44</mn></math>

</details>

---

### Q15. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

For L. P. P, maximize <math><mi>z</mi><mo>=</mo><mn>4</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>2</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub></math> subject to <math><mn>3</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>2</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≥</mo><mn>9</mn><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≤</mo><mn>3</mn><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>≥</mo><mn>0</mn><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≥</mo><mn>0</mn></math> has ….

**Options:**

- **(A)** Infinite number of optimal solutions
- **(B)** Unbounded solution
- **(C)** No solution
- **(D)** One optimal solution

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Unbounded solution**

**Detailed Solution:**

We have, maximise <math><mi>z</mi><mo>=</mo><mn>4</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>2</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub></math>  
Subject to constracts, <math><mn>3</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>2</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≥</mo><mn>9</mn><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≤</mo><mn>3</mn><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>≥</mo><mn>0</mn><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≥</mo><mn>0</mn></math>  
On taking given constraints as equation, we get the following graphs 
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/f8f5c5ad-0558-4081-9cd2-bd76712178df.png"> 
Here, we get feasible region is unbounded.

</details>

---

### Q16. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The maximum value of <math><mi>Z</mi><mo>=</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>,</mo></math> Subject to <math><mi>y</mi><mo>≤</mo><mn>2</mn><mi>x</mi><mo>,</mo><mi>x</mi><mo>≤</mo><mn>2</mn><mi>y</mi><mo>,</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>≤</mo><mn>3</mn><mo>,</mo><mi>x</mi><mo>≥</mo><mn>0</mn><mo>,</mo><mi>y</mi><mo>≥</mo><mn>0</mn><mi></mi></math> is ..

**Options:**

- **(A)** 14
- **(B)** 12
- **(C)** 13
- **(D)** 18

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 14**

**Detailed Solution:**

We have, <math><mi>z</mi><mo>=</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi></math>  
Subject to contraints <math><mi>y</mi><mo>≤</mo><mn>2</mn><mi>x</mi><mo>,</mo><mi>x</mi><mo>≤</mo><mn>2</mn><mi>y</mi><mo>,</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>≤</mo><mn>3</mn><mo>,</mo><mi>x</mi><mo>≥</mo><mn>0</mn><mo>,</mo><mi>y</mi><mo>≥</mo><mn>0</mn></math>  
On taking given constraints as equations, we get the following3 graph. 
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/24194e73-88df-4045-b92d-1e98735e75ed.png"> 
Intersecting point of line <math><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi></math> and <math><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn></math> is <math><mi>A</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi></mi><mn>2</mn></mrow></mfenced></math> and intersecting point of line <math><mi>y</mi><mo>=</mo><mn>2</mn><mi>y</mi></math> and <math><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn></math> is <math><mi>B</mi><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mi></mi><mn>1</mn></mrow></mfenced></math>  
Here OABO is the required feasible region whose corner points are <math><mi>O</mi><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi></mi><mn>0</mn></mrow></mfenced><mo>,</mo><mi>A</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi></mi><mn>2</mn></mrow></mfenced></math> and <math><mi>B</mi><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mi></mi><mn>1</mn></mrow></mfenced></math>  
<table border='1px solid'> <thead> <tr> <th>Corner points</th> <th> <math><mi>z</mi><mo>=</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi></math> </th> </tr> </thead> <tbody> <tr> <td> <math><mi>O</mi><mo>,</mo><mfenced separators="|"><mrow><mn>0,0</mn></mrow></mfenced></math> </td> <td> <math><mn>5</mn><mo>×</mo><mn>0</mn><mo>+</mo><mn>4</mn><mo>×</mo><mn>0</mn><mo>=</mo><mn>0</mn></math> </td> </tr> <tr> <td> <math><mi>A</mi><mfenced separators="|"><mrow><mn>1,2</mn></mrow></mfenced></math> </td> <td> <math><mn>5</mn><mo>×</mo><mn>1</mn><mo>+</mo><mn>4</mn><mo>×</mo><mn>2</mn><mo>=</mo><mn>13</mn></math> </td> </tr> <tr> <td> <math><mi>B</mi><mfenced separators="|"><mrow><mn>2,1</mn></mrow></mfenced></math> </td> <td> 
<math><mn>5</mn><mo>×</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>×</mo><mn>1</mn><mo>=</mo><mn>14</mn></math>  
(maximum) </td> </tr> </tbody> </table>

</details>

---

### Q17. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math><mi>z</mi><mo>=</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><mi>y</mi><mo>;</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>&gt;</mo><mn>0</mn><mi mathvariant="normal"></mi></math> subject to <math><mi>x</mi><mo>≤</mo><mn>2</mn><mo>,</mo><mi>y</mi><mo>≤</mo><mn>2</mn><mo>,</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>≥</mo><mn>3</mn><mo>,</mo><mi>x</mi><mo>≥</mo><mn>0</mn><mo>,</mo><mi>y</mi><mo>≥</mo><mn>0</mn></math> has minimum value at <math><mfenced separators="|"><mrow><mn>2,1</mn></mrow></mfenced></math> only, then…

**Options:**

- **(A)** <math><mi>a</mi><mo>&gt;</mo><mi>b</mi></math>
- **(B)** <math><mi>a</mi><mo>=</mo><mi>b</mi></math>
- **(C)** <math><mi>a</mi><mo>&lt;</mo><mi>b</mi></math>
- **(D)** <math><mi>a</mi><mo>=</mo><mn>1</mn><mo>+</mo><mi>b</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>a</mi><mo>&lt;</mo><mi>b</mi></math>**

**Detailed Solution:**

We have, <math><mi>z</mi><mo>=</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><mi>y</mi><mo>,</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>&gt;</mo><mn>0</mn></math>
Subject to constraints <math><mi>x</mi><mo>≤</mo><mn>2</mn><mo>,</mo><mi>y</mi><mo>≤</mo><mn>2</mn><mo>,</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>≥</mo><mn>3</mn><mi>x</mi><mo>,</mo><mi>y</mi><mo>≥</mo><mn>0</mn></math>
On taking given constraints as equation, we get the following graph
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/1d5ab897-b3b2-4a8d-887f-5d754332be48.png" />
Here, ABCA is the required feasible region whose corner points are <math><mi>A</mi><mfenced separators="|"><mrow><mn>2,1</mn></mrow></mfenced><mo>,</mo><mi>B</mi><mfenced separators="|"><mrow><mn>1,2</mn></mrow></mfenced></math> and <math><mi>C</mi><mfenced separators="|"><mrow><mn>2,2</mn></mrow></mfenced></math> .
Since, It is given that <math><mi>z</mi><mo>=</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><mi>y</mi><mo>;</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>&gt;</mo><mn>0</mn></math>
has minimum value at <math><mfenced separators="|"><mrow><mn>2,1</mn></mrow></mfenced></math>
<math><mo>∴</mo><mi></mi></math> Value of z at <math><mfenced separators="|"><mrow><mn>2,1</mn></mrow></mfenced><mo>&lt;</mo></math> value of z at <math><mfenced separators="|"><mrow><mn>1,2</mn></mrow></mfenced></math>
<math><mo>⇒</mo><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>&lt;</mo><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi></math>
<math><mo>⇒</mo><mi>a</mi><mo>&lt;</mo><mi>b</mi></math>

</details>

---

### Q18. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `3`

The maximum value of <math><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi></math> subject to <math><mn>3</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>≤</mo><mn>26</mn></math> and <math><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>≤</mo><mn>30</mn><mo>,</mo><mi> </mi><mi>x</mi><mo>≥</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>y</mi><mo>≥</mo><mn>0</mn></math> is

**Options:**

- **(A)** <math><mn>12</mn></math>
- **(B)** <math><mn>11.5</mn></math>
- **(C)** <math><mn>10</mn></math>
- **(D)** <math><mn>17.33</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>12</mn></math>**

**Detailed Solution:**

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/3327891.png" style="width: 270px; height: 209px;" />
<math> <mrow> <mn>3</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>=</mo><mn>26....</mn><mrow><mo>(</mo> <mi>i</mi> <mo>)</mo></mrow><mo>×</mo><mn>5</mn></mrow> </math>
<math> <mrow> <mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>30....</mn><mrow><mo>(</mo> <mrow> <mi>i</mi><mi>i</mi></mrow> <mo>)</mo></mrow><mo>×</mo><mn>3</mn></mrow> </math>
<math> <mrow> <mn>15</mn><mi>x</mi><mo>+</mo><mn>25</mn><mi>y</mi><mo>=</mo><mn>130</mn></mrow> </math>
<math> <mrow> <mn>15</mn><mi>x</mi><mo>+</mo><mn>9</mn><mi>y</mi><mo>=</mo><mn>90</mn></mrow> </math>
<math> <mrow> <mn>16</mn><mi>y</mi><mo>=</mo><mn>40</mn></mrow> </math>
<math> <mrow> <mi>y</mi><mo>=</mo><mfrac> <mrow> <mn>40</mn></mrow> <mrow> <mn>16</mn></mrow> </mfrac> <mo>=</mo><mfrac> <mn>5</mn> <mn>2</mn> </mfrac> </mrow> </math>
<math> <mrow> <mo>∴</mo><mn>3</mn><mi>x</mi><mo>+</mo><mfrac> <mrow> <mn>5</mn><mo>×</mo><mn>5</mn></mrow> <mn>2</mn> </mfrac> <mo>=</mo><mn>26</mn></mrow> </math>
<math> <mrow> <mn>3</mn><mi>x</mi><mo>=</mo><mn>26</mn><mo>−</mo><mfrac> <mrow> <mn>25</mn></mrow> <mn>2</mn> </mfrac> </mrow> </math>
<math> <mrow> <mi>x</mi><mo>=</mo><mfrac> <mn>9</mn> <mn>2</mn> </mfrac> </mrow> </math>
<math> <mrow> <mi>z</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi></mrow> </math>
Now check values of objective function at corner points of the shaded region
  <math> <mrow> <msub><mi>Z</mi><mi>A</mi></msub><mo>=</mo><mn>2</mn><mo>×</mo><mn>6</mn><mo>+</mo><mn>0</mn><mo>=</mo><mn>12</mn></mrow> </math>
<math> <mrow> <msub><mi>Z</mi><mi>B</mi></msub><mo>=</mo><mn>2</mn><mo>×</mo><mfrac> <mn>9</mn> <mn>2</mn> </mfrac> <mo>+</mo><mfrac> <mn>5</mn> <mn>2</mn> </mfrac> <mo>=</mo><mn>9</mn><mo>+</mo><mn>2.5</mn><mo>=</mo><mn>11.5</mn></mrow> </math>
<math> <mrow> <msub><mi>Z</mi><mi>C</mi></msub><mo>=</mo><mn>2</mn><mo>×</mo><mn>0</mn><mo>+</mo><mfrac> <mrow> <mn>26</mn></mrow> <mn>5</mn> </mfrac> <mo>=</mo><mfrac> <mrow> <mn>26</mn></mrow> <mn>5</mn> </mfrac> <mo>=</mo><mn>5.2</mn></mrow> </math>
Hence <math> <mrow> <msub> <mi>Z</mi> <mrow> <mi>max</mi></mrow> </msub> <mo>=</mo><mn>12</mn></mrow> </math>   at  <math> <mrow> <mi>x</mi><mo>=</mo><mn>6</mn></mrow> </math>  and  <math> <mrow> <mi>y</mi><mo>=</mo><mn>0</mn></mrow> </math>

</details>

---

### Q19. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `3`

The objective function <math><mi>Z</mi><mo>=</mo><mn>4</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>5</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo></math> subject to <math><mn>2</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≥</mo><mn>7</mn><mo>,</mo><mi> </mi><mn>2</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>3</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≤</mo><mn>15</mn><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≤</mo><mn>3</mn><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≥</mo><mn>0</mn></math> has minimum value at the point

**Options:**

- **(A)** On <math> <mrow> <mi>x</mi><mo>−</mo> </mrow> </math> axis
- **(B)** On <math > <mrow>  <mi>y</mi><mo>&#x2212;</mo> </mrow></math> axis
- **(C)** At the origin
- **(D)** On the line parallel to <math> <mrow> <mi>x</mi><mo>−</mo> </mrow> </math> axis

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) On <math> <mrow> <mi>x</mi><mo>−</mo> </mrow> </math> axis**

**Detailed Solution:**

Value of \(\mathrm{z}=4 \mathrm{x}_{1}+5 \mathrm{x}_{2}\)
Convert the given inequalities into equalities to get the corner points \(2 x_{1}+x_{2}=7 \ldots \ldots\) (i)
At \(x_{1}=0, x_{2}=7\) and \(x_{2}=0, x_{1}=3.5\)
So, the corner points of (i) are \((0,7)\) and \((3.5,0)\)
\(2 \mathrm{x}_{1}+3 \mathrm{x}_{2}=15 \ldots \ldots\) (ii)
At \(\mathrm{x}_{1}=0, \mathrm{x}_{2}=5\) and \(\mathrm{x}_{2}=0, \mathrm{x}_{1}=7.5\)
So, the corner points of (i) are \((0,5)\) and \((7.5,0)\)
\(\mathrm{x}_{2}=3\)..... (iii)
Plot these corner points on the graph paper and the line given in (iii)
The shaded part shows the feasible region.
At \(x_{2}=3, x_{1}=2\) in (i) and \(x_{1}=3\) in (ii)
The corner points of the feasible region are \((3.5,0),(7.5,0),(3,3)\) and \((2,3)\)
Corner points \(Z=4 x_{2}+5 x_{2}\)
\(\begin{array}{ll}(3.5,0) & 14 \\ (7.5,0) & 30 \\ (3,3) & 27 \\ (2,3) & 23\end{array}\)
Minimum value of \(Z=14\) and it lies on \(x\)-axis.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/wnlmnhwamyngcvvjbukxbtvhnthlbnqzkbfyxxxabcjhpthstr.jpeg" />

</details>

---

### Q20. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `3`

The objective function <math><mi>z</mi><mo>=</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub></math> , subject to <math><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≤</mo><mn>10</mn><mo>,</mo><mo>-</mo><mn>2</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>3</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≤</mo><mn>15</mn><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>≤</mo><mn>6</mn><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≥</mo><mn>0</mn></math> has maximum value _________ of the feasible region.

**Options:**

- **(A)** at only one point
- **(B)** at only two points
- **(C)** at every points of the segment joining two points
- **(D)** at every points of the line joining two points

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) at every points of the segment joining two points**

**Detailed Solution:**

The graph of the feasible region for the given L.P.P is
<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/3178231.png" style="width: 286px; height: 189px;" />
 
The value of objective function at corner points are
<math> <mrow> <mi>z</mi><mo>=</mo><msub> <mrow> <mrow><mo>[</mo> <mrow> <msub> <mi>x</mi> <mn>1</mn> </msub> <mo>+</mo><msub> <mi>x</mi> <mn>2</mn> </msub> </mrow> <mo>]</mo></mrow></mrow> <mi>O</mi> </msub> <mo>=</mo><mn>0</mn></mrow> </math>
<math> <mrow> <mi>z</mi><mo>=</mo><msub> <mrow> <mrow><mo>[</mo> <mrow> <msub> <mi>x</mi> <mn>1</mn> </msub> <mo>+</mo><msub> <mi>x</mi> <mn>2</mn> </msub> </mrow> <mo>]</mo></mrow></mrow> <mi>E</mi> </msub> <mo>=</mo><mn>6</mn></mrow> </math>
<math> <mrow> <mi>z</mi><mo>=</mo><msub> <mrow> <mrow><mo>[</mo> <mrow> <msub> <mi>x</mi> <mn>1</mn> </msub> <mo>+</mo><msub> <mi>x</mi> <mn>2</mn> </msub> </mrow> <mo>]</mo></mrow></mrow> <mi>F</mi> </msub> <mo>=</mo><mn>10</mn></mrow> </math>
<math> <mrow> <mi>z</mi><mo>=</mo><msub> <mrow> <mrow><mo>[</mo> <mrow> <msub> <mi>x</mi> <mn>1</mn> </msub> <mo>+</mo><msub> <mi>x</mi> <mn>2</mn> </msub> </mrow> <mo>]</mo></mrow></mrow> <mi>G</mi> </msub> <mo>=</mo><mn>10</mn></mrow> </math>
<math> <mrow> <mi>z</mi><mo>=</mo><msub> <mrow> <mrow><mo>[</mo> <mrow> <msub> <mi>x</mi> <mn>1</mn> </msub> <mo>+</mo><msub> <mi>x</mi> <mn>2</mn> </msub> </mrow> <mo>]</mo></mrow></mrow> <mi>D</mi> </msub> <mo>=</mo><mn>5</mn></mrow> </math>
Since the objective function is maximized at both points F and G, hence it will have a maximum value at every points of the segment joining points F and G

</details>

---

### Q21. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `3`

The volume of the solid formed by rotating the area enclosed between the curve $y^{2}=4 x, x=4$ and $x=5$ about $x$ -axis is (in cubic units)

**Options:**

- **(A)** $18 \pi$
- **(B)** $36 \pi$
- **(C)** $9 \pi$
- **(D)** $24 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $18 \pi$**

**Detailed Solution:**

Volume of the solid $=\int_{4}^{5} \pi y^{2} d x$
$=\pi \int_{4}^{5} 4 x d x$
$=4 \pi\left[\frac{x^{2}}{2}\right]_{4}^{5}$
$=2 x(25-16)$
$=18 \pi$ cu unit

</details>

---

