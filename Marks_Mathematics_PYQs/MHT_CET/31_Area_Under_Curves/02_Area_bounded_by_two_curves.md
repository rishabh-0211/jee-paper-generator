# MHT CET Mathematics - Area Under Curves

## Topic 2: Area bounded by two curves

**Total Questions:** 66

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area bounded by the curves $y = |x|$ and $y = 4 - |x|$ is ..... sq units.

**Options:**

- **(A)** $4$
- **(B)** $8$
- **(C)** $4\sqrt{2}$
- **(D)** $16$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $8$**

**Detailed Solution:**

The given curves are $y = |x|$ and $y = 4 - |x|$.

To find the points of intersection, we equate the two equations:

$|x| = 4 - |x|$

$2|x| = 4 \Rightarrow |x| = 2 \Rightarrow x = \pm 2$

The required area is bounded between $x = -2$ and $x = 2$. Since both functions are even, the area is symmetric about the y-axis.

Area $= \int_{-2}^{2} ((4 - |x|) - |x|) dx$

Area $= 2 \int_{0}^{2} (4 - 2x) dx$

Area $= 2 \left[ 4x - x^2 \right]_{0}^{2}$

Area $= 2 (8 - 4) = 8$ sq units.

Answer: $8$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area bounded by the curve $y = x^2 + 4, x = y, x = 3$, and Y-axis is

**Options:**

- **(A)** $\dfrac{51}{2}\ \text{unit}^2$
- **(B)** $\dfrac{33}{2}\ \text{unit}^2$
- **(C)** $\dfrac{27}{2}\ \text{unit}^2$
- **(D)** $\dfrac{21}{2}\ \text{unit}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{33}{2}\ \text{unit}^2$**

**Detailed Solution:**

The given curves are $y = x^2 + 4$ and $y = x$.

The region is bounded by these curves, the Y-axis ($x = 0$), and the line $x = 3$.

For all $x \in [0, 3]$, $x^2 + 4 > x$, so the parabola lies above the line.

The required area is given by the definite integral of the difference between the upper curve and the lower curve from $x = 0$ to $x = 3$:

$A = \int_{0}^{3} (x^2 + 4 - x) dx$

$A = \left[ \dfrac{x^3}{3} + 4x - \dfrac{x^2}{2} \right]_{0}^{3}$

$A = \left( \dfrac{3^3}{3} + 4(3) - \dfrac{3^2}{2} \right) - 0$

$A = 9 + 12 - \dfrac{9}{2}$

$A = 21 - \dfrac{9}{2}$

$A = \dfrac{42 - 9}{2} = \dfrac{33}{2}\ \text{unit}^2$

Answer: $\dfrac{33}{2}\ \text{unit}^2$

</details>

---

### Q3. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by the curves $y^2 = 9x$ and $x^2 = 9y$

**Options:**

- **(A)** $81$
- **(B)** $27$
- **(C)** $54$
- **(D)** $21$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $27$**

**Detailed Solution:**

The given curves are $y^2 = 9x$ and $x^2 = 9y$.

Solving the equations to find the points of intersection:

$\left(\dfrac{x^2}{9}\right)^2 = 9x$

$x^4 = 729x$

$x(x^3 - 729) = 0$

$x = 0$ or $x = 9$

The corresponding values of $y$ are $0$ and $9$. The points of intersection are $(0, 0)$ and $(9, 9)$.

The area of the bounded region is given by:

$A = \int_{0}^{9} \left( \sqrt{9x} - \dfrac{x^2}{9} \right) dx$

$A = \left[ 3 \cdot \dfrac{2}{3} x^{3/2} - \dfrac{x^3}{27} \right]_{0}^{9}$

$A = 2(9)^{3/2} - \dfrac{9^3}{27}$

$A = 2(27) - 27 = 27$

Alternatively, the area bounded by the parabolas $y^2 = 4ax$ and $x^2 = 4by$ is $\dfrac{16ab}{3}$.

Here, $4a = 9$ and $4b = 9$, so $a = \dfrac{9}{4}$ and $b = \dfrac{9}{4}$.

Area $= \dfrac{16}{3} \left(\dfrac{9}{4}\right) \left(\dfrac{9}{4}\right) = \dfrac{81}{3} = 27$

Answer: $27$

</details>

---

### Q4. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area between the curves $y = 1 - |x|$ and $y = |x| - 1$ is ..... square units.

**Options:**

- **(A)** $\dfrac{1}{2}$
- **(B)** $2$
- **(C)** $3$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$**

**Detailed Solution:**

The given curves are $y = 1 - |x|$ and $y = |x| - 1$.

To find the points of intersection, we equate the two equations:

$1 - |x| = |x| - 1$

$2|x| = 2$

$|x| = 1 \Rightarrow x = \pm 1$

The area between the curves is given by the integral:

$A = \int_{-1}^{1} ((1 - |x|) - (|x| - 1)) dx$

$A = \int_{-1}^{1} (2 - 2|x|) dx$

Since the integrand $2 - 2|x|$ is an even function, we can write:

$A = 2 \int_{0}^{1} (2 - 2x) dx$

$A = 2 \left[ 2x - x^2 \right]_{0}^{1}$

$A = 2 (2 - 1) = 2$ square units.

Alternatively, the region bounded by these curves is a square with vertices at $(1, 0)$, $(0, 1)$, $(-1, 0)$, and $(0, -1)$. The area of this square is $4 \times \left( \dfrac{1}{2} \times 1 \times 1 \right) = 2$ square units.

Answer: $2$

</details>

---

### Q5. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area bounded by $5x^2 - y = 0$ and $2x^2 - y + 9 = 0$ is (in sq.units)...

**Options:**

- **(A)** $12\sqrt{3}$
- **(B)** $6\sqrt{3}$
- **(C)** $8\sqrt{3}$
- **(D)** $4\sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $12\sqrt{3}$**

**Detailed Solution:**

The given curves are $y = 5x^2$ and $y = 2x^2 + 9$.

To find the points of intersection, equate the values of $y$:

$5x^2 = 2x^2 + 9$

$3x^2 = 9$

$x^2 = 3$

$x = \pm \sqrt{3}$

The required area $A$ is given by the integral of the upper curve minus the lower curve between the points of intersection:

$A = \int_{-\sqrt{3}}^{\sqrt{3}} ((2x^2 + 9) - 5x^2) dx$

$A = \int_{-\sqrt{3}}^{\sqrt{3}} (9 - 3x^2) dx$

Since the integrand is an even function:

$A = 2 \int_{0}^{\sqrt{3}} (9 - 3x^2) dx$

$A = 2 \left[ 9x - x^3 \right]_{0}^{\sqrt{3}}$

$A = 2 (9\sqrt{3} - 3\sqrt{3})$

$A = 2 (6\sqrt{3}) = 12\sqrt{3}$ sq. units.

Answer: $12\sqrt{3}$

</details>

---

### Q6. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by the parabola $y^2 = 4x - 2$ and the line $y = 2x - 1$ is...(in sq. units)

**Options:**

- **(A)** $2$
- **(B)** $\dfrac{1}{2}$
- **(C)** $\dfrac{1}{3}$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{3}$**

**Detailed Solution:**

To find the points of intersection, substitute $x$ from the line equation into the parabola equation.

From the line equation $y = 2x - 1$, we get $x = \dfrac{y+1}{2}$.

Substituting this into the parabola equation $y^2 = 4x - 2$:

$y^2 = 4\left(\dfrac{y+1}{2}\right) - 2$

$y^2 = 2y + 2 - 2$

$y^2 - 2y = 0$

$y(y - 2) = 0 \Rightarrow y = 0, y = 2$

The area of the bounded region is given by integrating the difference of the $x$-coordinates from $y = 0$ to $y = 2$:

$A = \int_{0}^{2} (x_{\text{line}} - x_{\text{parabola}}) dy$

$A = \int_{0}^{2} \left( \dfrac{y+1}{2} - \dfrac{y^2+2}{4} \right) dy$

$A = \dfrac{1}{4} \int_{0}^{2} (2y + 2 - y^2 - 2) dy$

$A = \dfrac{1}{4} \int_{0}^{2} (2y - y^2) dy$

$A = \dfrac{1}{4} \left[ y^2 - \dfrac{y^3}{3} \right]_{0}^{2}$

$A = \dfrac{1}{4} \left( 4 - \dfrac{8}{3} \right)$

$A = \dfrac{1}{4} \left( \dfrac{4}{3} \right) = \dfrac{1}{3}$ sq. units.

Answer: $\dfrac{1}{3}$

</details>

---

### Q7. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The area bounded by the curves $y = |x| - 1$ and $y = -|x| + 1$ is

**Options:**

- **(A)** $1$ sq.unit
- **(B)** $2$ sq. units
- **(C)** $2\sqrt{2}$ sq.units
- **(D)** $4$ sq.units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$ sq. units**

**Detailed Solution:**

The given curves are $y = |x| - 1$ and $y = -|x| + 1$.

To find the points of intersection, we equate the two equations:

$|x| - 1 = -|x| + 1$

$2|x| = 2 \Rightarrow |x| = 1 \Rightarrow x = \pm 1$

The required area $A$ is the region bounded between these two curves from $x = -1$ to $x = 1$.

$A = \int_{-1}^{1} [(-|x| + 1) - (|x| - 1)] dx$

$A = \int_{-1}^{1} (2 - 2|x|) dx$

Since the integrand is an even function:

$A = 2 \int_{0}^{1} (2 - 2x) dx$

$A = 2 \left[ 2x - x^2 \right]_{0}^{1}$

$A = 2 (2 - 1) = 2$ sq. units.

Answer: $2$ sq. units

</details>

---

### Q8. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The area (in square units) of the region bounded by the circle $x^2 + y^2 = 9$ and the parabola $y^2 \leq 8x$ is...

**Options:**

- **(A)** $\dfrac{8\sqrt{2}}{3} + \dfrac{9\pi}{2} - 2\sqrt{2} - 9\sin^{-1}\dfrac{1}{3}$
- **(B)** $\dfrac{8\sqrt{2}}{3} + \dfrac{9\pi}{2} + 2\sqrt{2} + 9\sin^{-1}\dfrac{1}{3}$
- **(C)** $\dfrac{4\sqrt{2}}{3} + \dfrac{9\pi}{4} - \sqrt{2} - \dfrac{9}{2}\sin^{-1}\dfrac{1}{3}$
- **(D)** $\dfrac{4\sqrt{2}}{3} + \dfrac{9\pi}{4} + \sqrt{2} + \dfrac{9}{2}\sin^{-1}\dfrac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{8\sqrt{2}}{3} + \dfrac{9\pi}{2} - 2\sqrt{2} - 9\sin^{-1}\dfrac{1}{3}$**

**Detailed Solution:**

To find the points of intersection of the circle $x^2 + y^2 = 9$ and the parabola $y^2 = 8x$, substitute $y^2 = 8x$ into the equation of the circle:

$x^2 + 8x - 9 = 0$

$(x + 9)(x - 1) = 0$

Since $x \geq 0$ for the parabola, we get $x = 1$.

The required region is bounded by $x^2 + y^2 \leq 9$ and $y^2 \leq 8x$. This region is symmetric with respect to the x-axis. The total area $A$ is given by:

$A = 2 \left( \int_{0}^{1} \sqrt{8x} \, dx + \int_{1}^{3} \sqrt{9 - x^2} \, dx \right)$

Evaluating the first integral:

$\int_{0}^{1} \sqrt{8x} \, dx = 2\sqrt{2} \left[ \dfrac{2}{3} x^{3/2} \right]_{0}^{1} = \dfrac{4\sqrt{2}}{3}$

Evaluating the second integral:

$\int_{1}^{3} \sqrt{9 - x^2} \, dx = \left[ \dfrac{x}{2} \sqrt{9 - x^2} + \dfrac{9}{2} \sin^{-1} \left( \dfrac{x}{3} \right) \right]_{1}^{3}$

Substituting the limits:

$= \left( 0 + \dfrac{9}{2} \sin^{-1}(1) \right) - \left( \dfrac{1}{2} \sqrt{8} + \dfrac{9}{2} \sin^{-1} \left( \dfrac{1}{3} \right) \right)$

$= \dfrac{9\pi}{4} - \sqrt{2} - \dfrac{9}{2} \sin^{-1} \left( \dfrac{1}{3} \right)$

Adding the two integrals and multiplying by 2:

$A = 2 \left( \dfrac{4\sqrt{2}}{3} + \dfrac{9\pi}{4} - \sqrt{2} - \dfrac{9}{2} \sin^{-1} \left( \dfrac{1}{3} \right) \right)$

$A = \dfrac{8\sqrt{2}}{3} + \dfrac{9\pi}{2} - 2\sqrt{2} - 9\sin^{-1} \left( \dfrac{1}{3} \right)$

Answer: $\dfrac{8\sqrt{2}}{3} + \dfrac{9\pi}{2} - 2\sqrt{2} - 9\sin^{-1}\dfrac{1}{3}$

</details>

---

### Q9. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region enclosed by $\{(x, y) \mid y \leq x^2, xy \leq 8, y \geq 1\}$ is...

**Options:**

- **(A)** $8\log 2 - \dfrac{14}{3}$
- **(B)** $8\log 2 + \dfrac{7}{3}$
- **(C)** $16\log 2 + \dfrac{7}{3}$
- **(D)** $16\log 2 - \dfrac{14}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $16\log 2 - \dfrac{14}{3}$**

**Detailed Solution:**

The region is bounded by the curves $y = x^2$, $xy = 8$, and $y = 1$ in the first quadrant (as the area must be finite).

To find the intersection points of the curves:
Intersection of $y = x^2$ and $xy = 8$:
$x(x^2) = 8 \Rightarrow x^3 = 8 \Rightarrow x = 2$
At $x = 2$, $y = 4$.

Intersection of $y = x^2$ and $y = 1$:
$x^2 = 1 \Rightarrow x = 1$ (taking $x > 0$).

Intersection of $xy = 8$ and $y = 1$:
$x(1) = 8 \Rightarrow x = 8$.

The area can be calculated by integrating with respect to $y$ from $y = 1$ to $y = 4$. For a given $y$, the value of $x$ ranges from the parabola $x = \sqrt{y}$ to the hyperbola $x = \dfrac{8}{y}$.

Required Area $= \displaystyle \int_{1}^{4} \left( \dfrac{8}{y} - \sqrt{y} \right) dy$

$= \left[ 8 \log y - \dfrac{2}{3} y^{3/2} \right]_{1}^{4}$

$= \left( 8 \log 4 - \dfrac{2}{3} (4)^{3/2} \right) - \left( 8 \log 1 - \dfrac{2}{3} (1)^{3/2} \right)$

$= \left( 16 \log 2 - \dfrac{2}{3} (8) \right) - \left( 0 - \dfrac{2}{3} \right)$

$= 16 \log 2 - \dfrac{16}{3} + \dfrac{2}{3}$

$= 16 \log 2 - \dfrac{14}{3}$

Answer: $16\log 2 - \dfrac{14}{3}$

</details>

---

### Q10. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by curves $y = \sin x, y = \cos x$ and the lines $x = 0$, $x = \dfrac{\pi}{4}$ is

**Options:**

- **(A)** $2\sqrt{2} - 1$
- **(B)** $\sqrt{2} - 1$
- **(C)** $2 - \sqrt{2}$
- **(D)** $\dfrac{1 - \sqrt{2}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{2} - 1$**

**Detailed Solution:**

The required area is given by the integral of the upper curve minus the lower curve between the given limits.

In the interval $x \in [0, \dfrac{\pi}{4}]$, $\cos x \ge \sin x$.

Area $= \int_{0}^{\pi/4} (\cos x - \sin x) dx$

$= [\sin x + \cos x]_{0}^{\pi/4}$

$= (\sin \dfrac{\pi}{4} + \cos \dfrac{\pi}{4}) - (\sin 0 + \cos 0)$

$= (\dfrac{1}{\sqrt{2}} + \dfrac{1}{\sqrt{2}}) - (0 + 1)$

$= \sqrt{2} - 1$

Answer: $\sqrt{2} - 1$

</details>

---

### Q11. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Area enclosed by curve $y = 2x^2$ and lines $x \geq 1,\ y \leq 4$ is ..... sq. units

**Options:**

- **(A)** $\dfrac{8\sqrt{2}-10}{3}$
- **(B)** $\dfrac{8(\sqrt{2}-1)}{3}$
- **(C)** $\dfrac{4\sqrt{2}-5}{3}$
- **(D)** $\dfrac{4(\sqrt{2}-1)}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{8\sqrt{2}-10}{3}$**

**Detailed Solution:**

The region is bounded by the curve $y = 2x^2$, the vertical line $x = 1$, and the horizontal line $y = 4$.

The intersection of $y = 2x^2$ and $y = 4$ in the region $x \geq 1$ is given by:

$2x^2 = 4 \Rightarrow x^2 = 2 \Rightarrow x = \sqrt{2}$

The required area $A$ is the integral of the upper boundary minus the lower boundary from $x = 1$ to $x = \sqrt{2}$:

$A = \int_{1}^{\sqrt{2}} (4 - 2x^2) dx$

$A = \left[ 4x - \dfrac{2x^3}{3} \right]_{1}^{\sqrt{2}}$

$A = \left( 4\sqrt{2} - \dfrac{4\sqrt{2}}{3} \right) - \left( 4 - \dfrac{2}{3} \right)$

$A = \dfrac{8\sqrt{2}}{3} - \dfrac{10}{3} = \dfrac{8\sqrt{2} - 10}{3}$

Answer: $\dfrac{8\sqrt{2}-10}{3}$

</details>

---

### Q12. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area of the region enclosed by the lines $y = 2x, 2y = x$ and $x = 2$ (in sq.units) is...

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $3$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3$**

**Detailed Solution:**

The given lines are $y = 2x$, $y = \dfrac{x}{2}$, and $x = 2$.

The points of intersection of the lines are $(0,0)$, $(2,4)$, and $(2,1)$.

The region is bounded by the upper line $y = 2x$ and the lower line $y = \dfrac{x}{2}$ from $x = 0$ to $x = 2$.

The area of the region is given by the integral of the difference between the upper and lower curves:

$\text{Area} = \int_{0}^{2} \left(2x - \dfrac{x}{2}\right) dx$

$\text{Area} = \int_{0}^{2} \dfrac{3x}{2} dx$

$\text{Area} = \left[ \dfrac{3x^2}{4} \right]_{0}^{2}$

$\text{Area} = \dfrac{3(2)^2}{4} - 0 = 3$

Answer: $3$

</details>

---

### Q13. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region common to the parabolas $4y^2 = 9x$ and $3x^2 = 16y$ is...

**Options:**

- **(A)** 2 sq. units
- **(B)** 4 sq. units
- **(C)** 8 sq. units
- **(D)** 16 sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 4 sq. units**

**Detailed Solution:**

The given equations of the parabolas are $4y^2 = 9x$ and $3x^2 = 16y$.

From the second equation, we have $y = \dfrac{3x^2}{16}$. Substituting this into the first equation:

$4\left(\dfrac{3x^2}{16}\right)^2 = 9x$

$\dfrac{9x^4}{64} = 9x$

$x^4 - 64x = 0$

$x(x^3 - 64) = 0$

The real roots are $x = 0$ and $x = 4$.

The required area $A$ is the integral of the upper curve minus the lower curve from $x = 0$ to $x = 4$:

$A = \int_{0}^{4} \left( \dfrac{3}{2}\sqrt{x} - \dfrac{3x^2}{16} \right) dx$

$A = \left[ x^{3/2} - \dfrac{x^3}{16} \right]_{0}^{4}$

$A = \left( 4^{3/2} - \dfrac{4^3}{16} \right) - 0$

$A = 8 - 4 = 4$ sq. units.

Answer: 4 sq. units

</details>

---

### Q14. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the smaller region bounded by the circle $x^2 + y^2 = 4$ and the line $x = 1$ is...

**Options:**

- **(A)** $\dfrac{4\pi}{3} - \sqrt{3}$
- **(B)** $\dfrac{\pi}{3} - \sqrt{3}$
- **(C)** $\dfrac{4\pi}{3} + \sqrt{3}$
- **(D)** $\dfrac{\pi}{3} + \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{4\pi}{3} - \sqrt{3}$**

**Detailed Solution:**

The equation of the circle is $x^2 + y^2 = 4$.

The area of the smaller region bounded by the circle and the line $x = 1$ is given by:

$A = 2 \int_{1}^{2} \sqrt{4 - x^2} \, dx$

Using the standard integral formula $\int \sqrt{a^2 - x^2} \, dx = \dfrac{x}{2} \sqrt{a^2 - x^2} + \dfrac{a^2}{2} \sin^{-1}\left(\dfrac{x}{a}\right)$, we get:

$A = 2 \left[ \dfrac{x}{2} \sqrt{4 - x^2} + 2 \sin^{-1}\left(\dfrac{x}{2}\right) \right]_{1}^{2}$

Substituting the limits:

$A = 2 \left[ \left( 0 + 2 \sin^{-1}(1) \right) - \left( \dfrac{1}{2} \sqrt{3} + 2 \sin^{-1}\left(\dfrac{1}{2}\right) \right) \right]$

$A = 2 \left[ 2 \left(\dfrac{\pi}{2}\right) - \dfrac{\sqrt{3}}{2} - 2 \left(\dfrac{\pi}{6}\right) \right]$

$A = 2 \left[ \pi - \dfrac{\sqrt{3}}{2} - \dfrac{\pi}{3} \right]$

$A = 2 \left[ \dfrac{2\pi}{3} - \dfrac{\sqrt{3}}{2} \right]$

$A = \dfrac{4\pi}{3} - \sqrt{3}$

Answer: $\dfrac{4\pi}{3} - \sqrt{3}$

</details>

---

### Q15. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the area enclosed between the curves $y^2 = 4kx$ and $y = kx, k > 0$ is $\dfrac{2k}{3}$ sq. units then $k = $

**Options:**

- **(A)** $1$
- **(B)** $1.5$
- **(C)** $2$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2$**

**Detailed Solution:**

Intersection points of $y^2 = 4kx$ and $y = kx$ are obtained by substituting $y = kx$ into $y^2 = 4kx$.

$(kx)^2 = 4kx$

$k^2x^2 - 4kx = 0$

$kx(kx - 4) = 0$

Since $k > 0$, $x = 0$ or $x = \dfrac{4}{k}$.

The area enclosed between the curves is given by:

$A = \int_{0}^{4/k} (2\sqrt{kx} - kx) dx$

$A = \left[ \dfrac{4}{3}\sqrt{k} x^{3/2} - \dfrac{k}{2} x^2 \right]_{0}^{4/k}$

$A = \dfrac{4}{3}\sqrt{k} \left(\dfrac{4}{k}\right)^{3/2} - \dfrac{k}{2} \left(\dfrac{4}{k}\right)^2$

$A = \dfrac{32}{3k} - \dfrac{8}{k} = \dfrac{8}{3k}$

Given that the area is \dfrac{2k}{3} sq. units:

$\dfrac{8}{3k} = \dfrac{2k}{3}$

$2k^2 = 8$

$k^2 = 4$

Since $k > 0$, $k = 2$.

Answer: $2$

</details>

---

### Q16. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area bounded by the parabolas $\mathrm{y}=9 x^2, \mathrm{y}=\frac{x^2}{16}$ and the line $\mathrm{y}=1$ is

**Options:**

- **(A)** $\frac{22}{9}$ sq. units
- **(B)** $\frac{44}{9}$ sq. units
- **(C)** $\frac{8}{9}$ sq. units
- **(D)** $\frac{26}{9}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{44}{9}$ sq. units**

**Detailed Solution:**

The given curves are $y = 9x^2$, $y = \dfrac{x^2}{16}$, and the line $y = 1$.

Since both parabolas are symmetric about the y-axis, the total area bounded by the curves is twice the area in the first quadrant.

Let us integrate with respect to $y$. For a given $y$ in the first quadrant, the x-coordinates on the parabolas are:
For $y = \dfrac{x^2}{16} \Rightarrow x = 4\sqrt{y}$ (outer curve)
For $y = 9x^2 \Rightarrow x = \dfrac{\sqrt{y}}{3}$ (inner curve)

The required area $A$ is given by:
$A = 2 \int_{0}^{1} \left( 4\sqrt{y} - \dfrac{\sqrt{y}}{3} \right) dy$

$A = 2 \int_{0}^{1} \left( \dfrac{11}{3}\sqrt{y} \right) dy$

$A = \dfrac{22}{3} \left[ \dfrac{y^{3/2}}{3/2} \right]_{0}^{1}$

$A = \dfrac{22}{3} \times \dfrac{2}{3} = \dfrac{44}{9}$ sq. units

Answer: $\frac{44}{9}$ sq. units

</details>

---

### Q17. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area bounded by the curve $\mathrm{y}=x^2+3, \mathrm{y}=x, x=3$ and y -axis is...

**Options:**

- **(A)** $\frac{9}{2}$ sq. units
- **(B)** 18 sq. units
- **(C)** $\frac{27}{2}$ sq. units
- **(D)** $\frac{27}{3}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{27}{2}$ sq. units**

**Detailed Solution:**

The required area is bounded by the upper curve $y = x^2 + 3$, the lower curve $y = x$, the y-axis ($x = 0$), and the line $x = 3$.

The area $A$ is given by the definite integral:

$A = \int_{0}^{3} (y_1 - y_2) dx$

$A = \int_{0}^{3} (x^2 + 3 - x) dx$

Integrating with respect to $x$:

$A = \left[ \dfrac{x^3}{3} - \dfrac{x^2}{2} + 3x \right]_{0}^{3}$

Substituting the limits:

$A = \left( \dfrac{3^3}{3} - \dfrac{3^2}{2} + 3(3) \right) - 0$

$A = 9 - \dfrac{9}{2} + 9$

$A = 18 - \dfrac{9}{2} = \dfrac{27}{2}$ sq. units

Answer: $\frac{27}{2}$ sq. units

</details>

---

### Q18. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area bounded by the curve $x^2=8 \mathrm{y}$ and the straight line $x-8 y+2=0$ is

**Options:**

- **(A)** $\frac{9}{8}$ sq. units
- **(B)** $\frac{15}{16}$ sq. units
- **(C)** $\frac{9}{16}$ sq. units
- **(D)** $\frac{15}{8}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{9}{16}$ sq. units**

**Detailed Solution:**

Given equations are $x^2 = 8y$ and $x - 8y + 2 = 0$.

From the line equation, we have $8y = x + 2$.

Substituting this into the equation of the parabola, we get:

$x^2 = x + 2$

$x^2 - x - 2 = 0$

$(x - 2)(x + 1) = 0$

The points of intersection are at $x = -1$ and $x = 2$.

The required area $A$ bounded by the line and the parabola is given by:

$A = \int_{-1}^{2} (y_{\text{line}} - y_{\text{parabola}}) dx$

$A = \int_{-1}^{2} \left( \dfrac{x + 2}{8} - \dfrac{x^2}{8} \right) dx$

$A = \dfrac{1}{8} \left[ \dfrac{x^2}{2} + 2x - \dfrac{x^3}{3} \right]_{-1}^{2}$

$A = \dfrac{1}{8} \left( \left( \dfrac{2^2}{2} + 2(2) - \dfrac{2^3}{3} \right) - \left( \dfrac{(-1)^2}{2} + 2(-1) - \dfrac{(-1)^3}{3} \right) \right)$

$A = \dfrac{1}{8} \left( \left( 2 + 4 - \dfrac{8}{3} \right) - \left( \dfrac{1}{2} - 2 + \dfrac{1}{3} \right) \right)$

$A = \dfrac{1}{8} \left( \dfrac{10}{3} - \left( -\dfrac{7}{6} \right) \right)$

$A = \dfrac{1}{8} \left( \dfrac{20}{6} + \dfrac{7}{6} \right)$

$A = \dfrac{1}{8} \left( \dfrac{27}{6} \right) = \dfrac{1}{8} \times \dfrac{9}{2} = \dfrac{9}{16}$ sq. units.

Answer: $\frac{9}{16}$ sq. units

</details>

---

### Q19. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

AOB is the positive quadrant of the ellipse $\frac{x^2}{25}+\frac{y^2}{9}=1$ in which $\mathrm{OA}=5, \mathrm{OB}=3$. The area between the $\operatorname{arc} \mathrm{AB}$ and the chord AB of the ellipse in sq.units is

**Options:**

- **(A)** $\frac{3}{5}(\pi-2)$
- **(B)** $\frac{15}{2}(\pi-2)$
- **(C)** $\frac{3}{10}(\pi-2)$
- **(D)** $\frac{15}{4}(\pi-2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{15}{4}(\pi-2)$**

**Detailed Solution:**

The given equation of the ellipse is $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$.

Comparing with the standard form $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$, we get $a = 5$ and $b = 3$.

The area of the ellipse in the first quadrant (bounded by the arc AB and the coordinate axes) is given by $\dfrac{1}{4} \pi a b$.

Area of the quarter ellipse $= \dfrac{1}{4} \pi (5)(3) = \dfrac{15\pi}{4}$ sq. units.

The points A and B are the intercepts on the positive x and y axes, respectively, so $A = (5, 0)$ and $B = (0, 3)$.

The area of the right-angled triangle OAB formed by the chord AB and the coordinate axes is $\dfrac{1}{2} \times OA \times OB$.

Area of $\Delta OAB = \dfrac{1}{2} \times 5 \times 3 = \dfrac{15}{2}$ sq. units.

The required area between the arc AB and the chord AB is the difference between the area of the quarter ellipse and the area of the triangle OAB.

Required area $= \dfrac{15\pi}{4} - \dfrac{15}{2} = \dfrac{15}{4}(\pi - 2)$ sq. units.

Answer: $\frac{15}{4}(\pi-2)$

</details>

---

### Q20. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by $\frac{x^2}{9}+\frac{y^2}{4}=1$ and the line $\frac{x}{3}+\frac{y}{2}=1$ is

**Options:**

- **(A)** $\frac{1}{2}(\pi-2)$ sq. units
- **(B)** $\frac{3}{2}(\pi-2)$ sq. units
- **(C)** $\frac{5}{4}(\pi-2)$ sq. units
- **(D)** $\frac{2}{3}(\pi-2)$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3}{2}(\pi-2)$ sq. units**

**Detailed Solution:**

The given equations are $\dfrac{x^2}{9}+\dfrac{y^2}{4}=1$ and $\dfrac{x}{3}+\dfrac{y}{2}=1$.

The line intersects the ellipse at $(3, 0)$ and $(0, 2)$, which are the vertices of the ellipse in the first quadrant.

The required area is the region in the first quadrant bounded by the ellipse and the line.

Area of the ellipse in the first quadrant is $\dfrac{1}{4} \pi a b = \dfrac{1}{4} \pi (3)(2) = \dfrac{3\pi}{2}$.

Area of the triangle formed by the line and the coordinate axes is $\dfrac{1}{2} \times \text{base} \times \text{height} = \dfrac{1}{2} \times 3 \times 2 = 3$.

The required area is the difference between these two areas:

Area $= \dfrac{3\pi}{2} - 3 = \dfrac{3}{2}(\pi - 2)$ sq. units.

Answer: $\frac{3}{2}(\pi-2)$ sq. units

</details>

---

### Q21. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area enclosed between the curves $\mathrm{y}^2=4 x$ and $\mathrm{y}=|x|$ is

**Options:**

- **(A)** $\frac{8}{3}$ sq. units
- **(B)** $\frac{5}{3}$ sq. units
- **(C)** $\frac{4}{3}$ sq. units
- **(D)** $\frac{2}{3}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{8}{3}$ sq. units**

**Detailed Solution:**

The given curves are $y^2 = 4x$ and $y = |x|$.

Since $y^2 = 4x$ is defined only for $x \ge 0$, we consider the line $y = |x| = x$ for $x \ge 0$.

To find the points of intersection, substitute $y = x$ into $y^2 = 4x$:

$x^2 = 4x$

$x^2 - 4x = 0$

$x(x - 4) = 0$

This gives $x = 0$ and $x = 4$.

In the interval $[0, 4]$, the parabola $y = 2\sqrt{x}$ lies above the line $y = x$.

The required area $A$ is given by:

$A = \int_{0}^{4} (2\sqrt{x} - x) dx$

$A = \left[ 2 \left( \dfrac{x^{3/2}}{3/2} \right) - \dfrac{x^2}{2} \right]_{0}^{4}$

$A = \left[ \dfrac{4}{3}x^{3/2} - \dfrac{x^2}{2} \right]_{0}^{4}$

Substituting the limits:

$A = \left( \dfrac{4}{3}(4)^{3/2} - \dfrac{4^2}{2} \right) - 0$

$A = \dfrac{4}{3}(8) - \dfrac{16}{2}$

$A = \dfrac{32}{3} - 8$

$A = \dfrac{32 - 24}{3} = \dfrac{8}{3}$ sq. units

Answer: $\frac{8}{3}$ sq. units

</details>

---

### Q22. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area (in sq. units) bounded between the parabolas $x^2=\frac{y}{4}$ and $x^2=9 y$ and the line $y=2$ is

**Options:**

- **(A)** $20 \sqrt{2}$
- **(B)** $\frac{10 \sqrt{2}}{3}$
- **(C)** $\frac{20 \sqrt{2}}{3}$
- **(D)** $10 \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{20 \sqrt{2}}{3}$**

**Detailed Solution:**

The given parabolas are $x^2 = \dfrac{y}{4}$ and $x^2 = 9y$.

Since both parabolas are symmetric about the y-axis, the required area is twice the area in the first quadrant.

In the first quadrant, the equations can be written in terms of $y$ as $x = \dfrac{\sqrt{y}}{2}$ and $x = 3\sqrt{y}$.

The area bounded by these curves and the line $y = 2$ is given by integrating with respect to $y$ from $0$ to $2$:

$A = 2 \int_{0}^{2} \left( 3\sqrt{y} - \dfrac{\sqrt{y}}{2} \right) dy$

$A = 2 \int_{0}^{2} \dfrac{5}{2}\sqrt{y} dy$

$A = 5 \int_{0}^{2} y^{1/2} dy$

$A = 5 \left[ \dfrac{2}{3} y^{3/2} \right]_{0}^{2}$

$A = \dfrac{10}{3} (2)^{3/2}$

$A = \dfrac{10}{3} (2\sqrt{2}) = \dfrac{20\sqrt{2}}{3}$ sq. units.

Answer: $\frac{20 \sqrt{2}}{3}$

</details>

---

### Q23. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area enclosed between the parabola $y^2=4 x$ and the line $y=2 x-4$ is

**Options:**

- **(A)** $\frac{17}{3}$ sq. units
- **(B)** 15 sq. units
- **(C)** $\frac{19}{3}$ sq. units
- **(D)** 9 sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 9 sq. units**

**Detailed Solution:**

Given the equations of the parabola $y^2 = 4x$ and the line $y = 2x - 4$.

From the equation of the line, we have $x = \dfrac{y+4}{2}$.

Substituting this into the equation of the parabola to find the points of intersection:

$y^2 = 4\left(\dfrac{y+4}{2}\right)$

$y^2 = 2y + 8$

$y^2 - 2y - 8 = 0$

$(y - 4)(y + 2) = 0$

$y = -2, 4$

The area enclosed between the curves is given by integrating with respect to $y$ from $y = -2$ to $y = 4$:

$A = \int_{-2}^{4} \left( x_{\text{line}} - x_{\text{parabola}} \right) dy$

$A = \int_{-2}^{4} \left( \dfrac{y+4}{2} - \dfrac{y^2}{4} \right) dy$

$A = \left[ \dfrac{y^2}{4} + 2y - \dfrac{y^3}{12} \right]_{-2}^{4}$

$A = \left( \dfrac{16}{4} + 8 - \dfrac{64}{12} \right) - \left( \dfrac{4}{4} - 4 - \dfrac{-8}{12} \right)$

$A = \left( 4 + 8 - \dfrac{16}{3} \right) - \left( 1 - 4 + \dfrac{2}{3} \right)$

$A = \left( 12 - \dfrac{16}{3} \right) - \left( -3 + \dfrac{2}{3} \right)$

$A = \dfrac{20}{3} - \left( -\dfrac{7}{3} \right)$

$A = \dfrac{27}{3} = 9$ sq. units

Answer: 9 sq. units

</details>

---

### Q24. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by curves $y=3 x+1, y=4 x+1$ and $x=2$ is

**Options:**

- **(A)** 1 sq. units
- **(B)** 2 sq. units
- **(C)** 3 sq. units
- **(D)** 4 sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2 sq. units**

**Detailed Solution:**

The given curves are $y = 3x + 1$ and $y = 4x + 1$.

To find the point of intersection, equate the two equations:

$3x + 1 = 4x + 1$

$x = 0$

The region is bounded by $x = 0$ and $x = 2$. In the interval $[0, 2]$, $4x + 1 \geq 3x + 1$.

The required area is given by:

$A = \int_{0}^{2} ((4x + 1) - (3x + 1)) dx$

$A = \int_{0}^{2} x dx$

$A = \left[ \dfrac{x^2}{2} \right]_{0}^{2}$

$A = \dfrac{2^2}{2} - 0 = 2$ sq. units.

Answer: 2 sq. units

</details>

---

### Q25. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region bounded by $y-x=2$ and $x^2=y$ is equal to

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{4}{3}$
- **(C)** $\frac{9}{2}$
- **(D)** $\frac{16}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{9}{2}$**

**Detailed Solution:**

Given equations of the curves are $y - x = 2 \Rightarrow y = x + 2$ and $x^2 = y$.

To find the points of intersection, substitute $y = x^2$ in $y = x + 2$:

$x^2 = x + 2$

$x^2 - x - 2 = 0$

$(x - 2)(x + 1) = 0$

$x = -1, 2$

The required area $A$ is bounded by the line and the parabola between $x = -1$ and $x = 2$.

$A = \int_{-1}^{2} (y_{\text{line}} - y_{\text{parabola}}) dx$

$A = \int_{-1}^{2} (x + 2 - x^2) dx$

$A = \left[ \dfrac{x^2}{2} + 2x - \dfrac{x^3}{3} \right]_{-1}^{2}$

$A = \left( \dfrac{4}{2} + 4 - \dfrac{8}{3} \right) - \left( \dfrac{1}{2} - 2 + \dfrac{1}{3} \right)$

$A = \left( 6 - \dfrac{8}{3} \right) - \left( \dfrac{5}{6} - 2 \right)$

$A = \dfrac{10}{3} - \left( -\dfrac{7}{6} \right)$

$A = \dfrac{20}{6} + \dfrac{7}{6} = \dfrac{27}{6} = \dfrac{9}{2}$ sq. units.

Answer: $\frac{9}{2}$

</details>

---

### Q26. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The area bounded between the curves $y=a x^2$ and $x=\mathrm{a} y^2(\mathrm{a}\gt0)$ is 1 sq. units, then the value of $a$ is

**Options:**

- **(A)** $\dfrac{1}{\sqrt{3}}$
- **(B)** $\dfrac{1}{2}$
- **(C)** 1
- **(D)** $\dfrac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{\sqrt{3}}$**

**Detailed Solution:**

The given curves are $y = a x^2$ and $x = a y^2$.

To find the points of intersection, substitute $y = a x^2$ into $x = a y^2$:

$x = a(a x^2)^2$

$x = a^3 x^4$

$x(a^3 x^3 - 1) = 0$

Since $a > 0$, the points of intersection are $x = 0$ and $x = \dfrac{1}{a}$.

The area bounded by the curves is given by:

$A = \int_{0}^{1/a} \left( \sqrt{\dfrac{x}{a}} - a x^2 \right) dx$

$A = \left[ \dfrac{1}{\sqrt{a}} \dfrac{x^{3/2}}{3/2} - a \dfrac{x^3}{3} \right]_{0}^{1/a}$

$A = \dfrac{2}{3\sqrt{a}} \left( \dfrac{1}{a} \right)^{3/2} - \dfrac{a}{3} \left( \dfrac{1}{a} \right)^3$

$A = \dfrac{2}{3a^2} - \dfrac{1}{3a^2} = \dfrac{1}{3a^2}$

Given that the area is $1$ sq. unit:

$\dfrac{1}{3a^2} = 1$

$a^2 = \dfrac{1}{3}$

Since $a > 0$, we get $a = \dfrac{1}{\sqrt{3}}$.

Answer: $\dfrac{1}{\sqrt{3}}$

</details>

---

### Q27. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The maximum value of $\mathrm{Z}=x+y$, subjected to $x+y \leq 10,5 x+3 y \geq 15, x \leq 6, x, y \geq 0$

**Options:**

- **(A)** occurs only at unique point
- **(B)** occurs only at two distinct points
- **(C)** occurs at infinitely many points
- **(D)** does not exist

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) occurs at infinitely many points**

**Detailed Solution:**

The objective function to be maximized is $Z = x + y$.

The given constraints are:
$x + y \leq 10$
$5x + 3y \geq 15$
$x \leq 6$
$x \geq 0, y \geq 0$

We find the vertices of the feasible region by solving the boundary equations of the constraints. The vertices are:
$(0, 5)$ from the intersection of $x = 0$ and $5x + 3y = 15$
$(0, 10)$ from the intersection of $x = 0$ and $x + y = 10$
$(6, 4)$ from the intersection of $x = 6$ and $x + y = 10$
$(6, 0)$ from the intersection of $x = 6$ and $y = 0$
$(3, 0)$ from the intersection of $y = 0$ and $5x + 3y = 15$

Evaluating the objective function $Z = x + y$ at each vertex:
At $(0, 5)$, $Z = 0 + 5 = 5$
At $(0, 10)$, $Z = 0 + 10 = 10$
At $(6, 4)$, $Z = 6 + 4 = 10$
At $(6, 0)$, $Z = 6 + 0 = 6$
At $(3, 0)$, $Z = 3 + 0 = 3$

The maximum value of $Z$ is $10$, which occurs at two distinct vertices: $(0, 10)$ and $(6, 4)$.

Since the maximum value occurs at two distinct vertices, it will also occur at every point on the line segment joining these two vertices (which lies on the line $x + y = 10$). Because a line segment contains an infinite number of points, the maximum value occurs at infinitely many points.

Answer: occurs at infinitely many points

</details>

---

### Q28. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area of the region, bounded by the parabola $y=x^2+2$ and the lines $y=x, x=0$ and $x=3$, is

**Options:**

- **(A)** $\dfrac{9}{2}$ sq. units
- **(B)** $\dfrac{11}{2}$ sq. units
- **(C)** $\dfrac{15}{2}$ sq. units
- **(D)** $\dfrac{21}{2}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{21}{2}$ sq. units**

**Detailed Solution:**

The area of the region is bounded by the upper curve $y = x^2 + 2$ and the lower curve $y = x$ between $x = 0$ and $x = 3$.

To confirm which curve is above the other, we check $x^2 + 2 - x = x^2 - x + 2$. Since the discriminant $D = 1 - 8 = -7 < 0$ and the coefficient of $x^2$ is positive, $x^2 + 2 > x$ for all real $x$.

The required area $A$ is given by the definite integral:

$A = \int_{0}^{3} ((x^2 + 2) - x) \, dx$

$A = \int_{0}^{3} (x^2 - x + 2) \, dx$

Integrating the function, we get:

$A = \left[ \dfrac{x^3}{3} - \dfrac{x^2}{2} + 2x \right]_{0}^{3}$

Substituting the limits:

$A = \left( \dfrac{3^3}{3} - \dfrac{3^2}{2} + 2(3) \right) - 0$

$A = 9 - \dfrac{9}{2} + 6$

$A = 15 - \dfrac{9}{2} = \dfrac{30 - 9}{2} = \dfrac{21}{2}$ sq. units

Answer: $\dfrac{21}{2}$ sq. units

</details>

---

### Q29. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The area (in sq. units) of the region bounded by the curve $x^2=4 y$ and the straight line $x=4 y-2$ is

**Options:**

- **(A)** $\dfrac{9}{8}$
- **(B)** $\dfrac{7}{8}$
- **(C)** $\dfrac{5}{4}$
- **(D)** $\dfrac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{9}{8}$**

**Detailed Solution:**

Given equations of the curves are $x^2 = 4y$ and $x = 4y - 2$.

To find the points of intersection, substitute $4y = x + 2$ into the equation of the parabola:

$x^2 = x + 2$

$x^2 - x - 2 = 0$

$(x - 2)(x + 1) = 0$

$x = -1, 2$

The required area is bounded between $x = -1$ and $x = 2$. In this interval, the line lies above the parabola.

Area $= \int_{-1}^{2} \left( \dfrac{x + 2}{4} - \dfrac{x^2}{4} \right) dx$

Area $= \dfrac{1}{4} \left[ \dfrac{x^2}{2} + 2x - \dfrac{x^3}{3} \right]_{-1}^{2}$

Area $= \dfrac{1}{4} \left( \left( \dfrac{4}{2} + 4 - \dfrac{8}{3} \right) - \left( \dfrac{1}{2} - 2 + \dfrac{1}{3} \right) \right)$

Area $= \dfrac{1}{4} \left( \left( 6 - \dfrac{8}{3} \right) - \left( -\dfrac{7}{6} \right) \right)$

Area $= \dfrac{1}{4} \left( \dfrac{10}{3} + \dfrac{7}{6} \right)$

Area $= \dfrac{1}{4} \left( \dfrac{27}{6} \right) = \dfrac{9}{8}$ sq. units.

Answer: $\dfrac{9}{8}$

</details>

---

### Q30. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The area bounded by the curves $y=(x-1)^2$, $y=(x+1)^2$ and $y=\frac{1}{4}$ is

**Options:**

- **(A)** $\frac{1}{3}$ sq. units.
- **(B)** $\frac{2}{3}$ sq. units.
- **(C)** $\frac{1}{4}$ sq. units.
- **(D)** $\frac{1}{5}$ sq. units.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{3}$ sq. units.**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/AU6jXkpNC9zI7GoPGLpOL7AW_ZBlPs4JOG8wpG9aUKM.original.fullsize.png">

$\begin{aligned} \text { Required area } & =2 \int_0^{\frac{1}{2}}\left[(x-1)^2-\frac{1}{4}\right] \mathrm{d} x \\ & =2\left[\frac{(x-1)^3}{3}\right]_0^{\frac{1}{2}}-\frac{1}{2}[x]_0^{\frac{1}{2}} \\ & =\frac{2}{3}\left(-\frac{1}{8}+1\right)-\frac{1}{2}\left(\frac{1}{2}-0\right) \\ & =\frac{1}{3} \text { sq. units }\end{aligned}$

</details>

---

### Q31. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If a curve $y=\mathrm{a} \sqrt{x}+\mathrm{b} x$ passes through the point $(1,2)$ and the area bounded by the curve, line $x=4$ and $\mathrm{X}$-axis is 8 sq. units, then

**Options:**

- **(A)** $\mathrm{a}=3, \mathrm{~b}=-1$
- **(B)** $\mathrm{a}=3, \mathrm{~b}=1$
- **(C)** $\mathrm{a}=-3, \mathrm{~b}=1$
- **(D)** $\mathrm{a}=-3, \mathrm{~b}=-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{a}=3, \mathrm{~b}=-1$**

**Detailed Solution:**

The given curve passes through $(1,2)$.
$\therefore \quad 2=a+b$
According to the given condition,
$\int_0^4(a \sqrt{x}+b x) d x=8$                    ...(i)
$\Rightarrow \frac{2 \mathrm{a}}{3}\left[x^{3 / 2}\right]_0^4+\frac{\mathrm{b}}{2}\left[x^2\right]_0^4=8 \Rightarrow \frac{2 \mathrm{a}}{3} \cdot 8+8 \mathrm{~b}=8$
$\Rightarrow 2 a+3 b=3$             ...(ii)
From (i) and (ii), we get
$\mathrm{a}=3, \mathrm{~b}=-1$

</details>

---

### Q32. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region bounded by curves $y=3 x+1, y=4 x+1$ and $x=3$ is

**Options:**

- **(A)** $\frac{7}{2}$
- **(B)** $\frac{9}{5}$
- **(C)** $\frac{9}{2}$
- **(D)** $\frac{7}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{9}{2}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/cAoVwjHz4sNTHIMmk6SFHcC3oM0p5v3kEnPHTYkRWz4.original.fullsize.png">


$\begin{aligned} \text { Required area } & =\cdot \int_0^3[4 x+1-(3 x+1)] \mathrm{d} x \\ & =\int_0^3 x \mathrm{~d} x \\ & =\left[\frac{x^2}{2}\right]_0^3 \\ & =\frac{9}{2} \text { sq. units }\end{aligned}$

</details>

---

### Q33. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the smaller part of the circle $x^2+y^2=\mathrm{a}^2$ cut off by the line $x=\frac{\mathrm{a}}{\sqrt{2}}$ is

**Options:**

- **(A)** $\frac{\mathrm{a}^2}{4}\left|\frac{\pi}{2}-1\right|$
- **(B)** $a^2\left|\frac{\pi}{4}-1\right|$
- **(C)** $\frac{\mathrm{a}^2}{2}\left|\frac{\pi}{2}-1\right|$
- **(D)** $\frac{a^2}{4}\left|\frac{\pi}{4}-1\right|$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\mathrm{a}^2}{2}\left|\frac{\pi}{2}-1\right|$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/q2znFCRKlbyo-IxowLLV6325QWDfnBA5VZ0yTX--jc8.original.fullsize.png">

Substitute $x=\frac{\mathrm{a}}{\sqrt{2}}$ in $x^2+y^2=\mathrm{a}^2$, we get $\frac{\mathrm{a}^2}{2}+y^2=\mathrm{a}^2 \Rightarrow y= \pm \frac{\mathrm{a}}{\sqrt{2}}$
$\therefore \quad$ Required area
$$
\begin{aligned}
& =2 \int_{\frac{a}{\sqrt{2}}}^a \sqrt{a^2-x^2} d x \\
& =2\left[\frac{x}{2} \sqrt{a^2-x^2}+\frac{a^2}{2} \sin ^{-1}\left(\frac{x}{a}\right)\right]_{\frac{a}{\sqrt{2}}}^2 \\
& =2\left\{\left[0+\frac{a^2}{2} \times \frac{\pi}{2}\right]-\left[\frac{a}{2 \sqrt{2}} \sqrt{a^2-\frac{a^2}{2}}+\frac{a^2}{2} \times \frac{\pi}{4}\right]\right\} \\
& =2\left[\frac{a^2 \pi}{4}-\frac{a^2}{4}-\frac{a^2 \pi}{8}\right] \\
& =\frac{a^2}{2}\left|\pi-1-\frac{\pi}{2}\right| \\
& =\frac{a^2}{2}\left|\frac{\pi}{2}-1\right|
\end{aligned}
$$

</details>

---

### Q34. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by the parabola $y=x^2$ and the curve $y=|x|$ is

**Options:**

- **(A)** $\frac{1}{2}$ sq. units
- **(B)** $\frac{1}{3}$ sq. units
- **(C)** $\frac{1}{4}$ sq. units
- **(D)** $\frac{1}{6}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{3}$ sq. units**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/WtimhRIUj0mZ9yhMcH0SPrQXUEwouHtal8OcUEAvtqU.original.fullsize.png">

$\begin{aligned} \text { Required area } & =2 \int_0^1\left(x-x^2\right) \mathrm{d} x \\ & =2\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_0^1 \\ & =2\left(\frac{1}{2}-\frac{1}{3}\right)=\frac{1}{3} \text { sq.units }\end{aligned}$

</details>

---

### Q35. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region $\mathrm{A}=\left\{(x, y) / \frac{y^2}{2} \leq x \leq y+4\right\}$

**Options:**

- **(A)** 30
- **(B)** $\frac{53}{3}$
- **(C)** 16
- **(D)** 18

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 18**

**Detailed Solution:**

Given that $\frac{y^2}{2} \leq x \leq y+4$
$\begin{array}{ll}
\therefore \quad & x=\frac{y^2}{2} \text { and } x=y+4 \\
& \frac{y^2}{2}=y+4^2 \\
\therefore \quad & y^2-2 y-8=0 \\
\therefore \quad & y=4 \text { or }-2 \\
& \Rightarrow x=8 \text { or } 2
\end{array}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ODGcd4leaihHiUp2WnPgJBlpz4uhwQFJakViCbqCPBo.original.fullsize.png">

$\therefore \quad \mathrm{A}=\int_{-2}^4\left(y+4-\frac{y^2}{2}\right) \mathrm{d} y$
$\begin{aligned} & \therefore \quad \mathrm{A}=\left[\frac{y^2}{2}+4 y-\frac{y^3}{6}\right]_{-2}^4 \\ & \therefore \quad A=\left(8+16-\frac{64}{6}\right)-\left(2-8+\frac{8}{6}\right) \\ & \therefore \quad \mathrm{A}=18 \\ & \end{aligned}$

</details>

---

### Q36. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The area bounded by the curve $y^2=2 x+1$ and the line $x-y=1$ is

**Options:**

- **(A)** $\frac{2}{3}$ sq. units
- **(B)** $\frac{4}{3}$ sq. units
- **(C)** $\frac{8}{3}$ sq. units
- **(D)** $\frac{16}{3}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{16}{3}$ sq. units**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/QT4U61bykSbjPTEzLgyKhqdaNQgpX3InV2WjCzveFH0.original.fullsize.png">
$\begin{aligned} & \text { Required area }=\int_{-1}^3\left\{(1+y)-\left(\frac{y^2-1}{2}\right)\right\} \mathrm{d} y \\ & =\int_{-1}^3\left(\frac{3}{2}+y-\frac{y^2}{2}\right) \mathrm{d} y \\ & =\left[\frac{3}{2} y+\frac{y^2}{2}-\frac{y^3}{6}\right]_{-1}^3 \\ & =\left(\frac{9}{2}+\frac{9}{2}-\frac{27}{6}\right)-\left(\frac{-3}{2}+\frac{1}{2}+\frac{1}{6}\right)=\frac{16}{3}\end{aligned}$

</details>

---

### Q37. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

There are (in square units) of the region bounded by the parabola $y=x^2+2$ and the lines $y=x+1, x=0$ and $x=3$ is

**Options:**

- **(A)** $\frac{15}{4}$
- **(B)** $\frac{15}{2}$
- **(C)** $\frac{21}{2}$
- **(D)** $\frac{17}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{15}{2}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Llx3ppT4Ev2b7EsTkTHSlttpdv0sV3a3gV7y3yF7wjg.original.fullsize.png">

Required area
$\begin{aligned}
& =\int_0^3\left\{\left(x^2+2\right)-(x+1)\right\} d x \\
& =\left[\frac{x^3}{3}+2 x-\frac{x^2}{2}-x\right]_0^3 \\
& =\left(9+6-\frac{9}{2}-3\right)-0=\frac{15}{2}
\end{aligned}$

</details>

---

### Q38. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The angle between the curves $y=\sin x$ and $y=\cos x 0<x<\frac{\pi}{2}$, is

**Options:**

- **(A)** $\tan ^{-1}(\sqrt{2})$
- **(B)** $\tan ^{-1}(3 \sqrt{2})$
- **(C)** $\tan ^{-1}(2 \sqrt{2})$
- **(D)** $\tan ^{-1}(3 \sqrt{3})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\tan ^{-1}(2 \sqrt{2})$**

**Detailed Solution:**

$y=\sin x$ and $y=\cos x$ intersects at $x=\frac{\pi}{4}$
$\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)_{\text {for first curve at } x=\frac{\pi}{4}}=\cos \frac{\pi}{4}=\frac{1}{\sqrt{2}}$
$\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)_{\text {for second curve at } x=\frac{\pi}{4}}=-\sin \frac{\pi}{4}=-\frac{1}{\sqrt{2}}$
Required angle $=\theta=\tan ^{-1}\left\{\frac{\frac{1}{\sqrt{2}}-\left(-\frac{1}{\sqrt{2}}\right)}{1+\left(\frac{1}{\sqrt{2}}\right)\left(-\frac{1}{\sqrt{2}}\right)}\right\}=\tan ^{-1}\left(\frac{\sqrt{2}}{\frac{1}{2}}\right)$
$=\tan ^{-1}(2 \sqrt{2})$

</details>

---

### Q39. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Area of the region bounded by the curve $y=x^2+2$ and the lines $y=x, x=0$ and $x=3$ is

**Options:**

- **(A)** $\frac{19}{2}$ sq $\cdot$ units
- **(B)** $\frac{21}{2} \mathrm{sq} \cdot$ units
- **(C)** $15 s q \cdot$ units
- **(D)** $\frac{9}{2} \mathrm{sq} \cdot \mathrm{units}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{21}{2} \mathrm{sq} \cdot$ units**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/FnVeoCp87c1F-piJsKWhODT4J8yLvEnFEzFSth4cbww.original.fullsize.png">
$\begin{aligned} & \text { Required area }=\int_0^3\left(x^2+2-x\right) d x=\left[\frac{x^3}{3}+2 x-\frac{x^2}{2}\right]_0^3 \\ & =\frac{27}{3}+6-\frac{9}{2}=\frac{21}{2}\end{aligned}$

</details>

---

### Q40. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by the $y$-axis, $y=\cos x, y=\sin x$, when $0 \leq x \leq \frac{\pi}{4}$, is

**Options:**

- **(A)** $(\sqrt{2}-1)$ sq. units
- **(B)** $2(\sqrt{2}-1)$ sq. units
- **(C)** $(\sqrt{2}+1)$ sq. units
- **(D)** $\sqrt{2}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(\sqrt{2}-1)$ sq. units**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/RV_H3WqJoqRCTeOFE73HN_MMCnhalKNpIZJ5RJyvJT4.original.fullsize.png">
$\begin{aligned} & =\left(\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{2}}\right)-(0+1) \\ & =\sqrt{2}-1\end{aligned}$

</details>

---

### Q41. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region described by $A=\left[(x, y) / x^2+y^2 \leq 1-x\right]$ is

**Options:**

- **(A)** $\left(\frac{\pi}{2}-\frac{2}{3}\right)$
- **(B)** $\left(\frac{\pi}{2}+\frac{4}{3}\right)$
- **(C)** $\left(\frac{\pi}{2}-\frac{4}{3}\right)$
- **(D)** $\left(\frac{\pi}{2}+\frac{2}{3}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\frac{\pi}{2}+\frac{4}{3}\right)$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/RlQ0D6s05gBfD5Bc-BTqGf3Fkr-FktWvHSqWVqZ1_T8.original.fullsize.png">
$\begin{aligned} & A=\left\{(x, y): x^2+y^2 \leq 1 \text { and } y^2 \leq 1-x\right\} \\ & =\text { Area of semicircle }+ \text { Area of the region bounded by parabola and } \\ & \text { y-axis } \\ & =\frac{\pi \times 1^2}{2}+2 \int_0^1 \sqrt{1-x} d x \\ & =\frac{\pi}{2}+2 \times \frac{2}{3}\left[-(1-x)^{3 / 2}\right]_0^1 \\ & =\frac{\pi}{2}+\frac{4}{3}\left[-0^{3 / 2}+1^{3 / 2}\right] \\ & =\frac{\pi}{2}+\frac{4}{3}\end{aligned}$

</details>

---

### Q42. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The area of the region bounded by the curve $y^2=9 x$ and the line $y=3 x$ is

**Options:**

- **(A)** $\frac{3}{2}$ sq.units
- **(B)** 1 sq.units
- **(C)** $\frac{1}{2}$ sq.units
- **(D)** $\frac{1}{4}$ sq.units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2}$ sq.units**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/c7ZKTKMHhFoO-ygR8F2zGW9xpjx5oFL2bUhi4hvZ7Ro.original.fullsize.png">
$\begin{aligned} & \text { Required area }=\int_0^1(3 \sqrt{x}-3 x) d x \\ & =3\left[\frac{2}{3} x^{3 / 2}-\frac{x^2}{2}\right]_0^1 \\ & =3\left(\frac{2}{3}-\frac{1}{2}\right) \\ & =3 \times \frac{1}{6}=\frac{1}{2}\end{aligned}$

</details>

---

### Q43. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by the curve $y=2 x-x^2$ and $\mathrm{X}$-axis is

**Options:**

- **(A)** $\frac{2}{3}$ sq. units
- **(B)** $\frac{4}{3}$ sq. units
- **(C)** $\frac{5}{3}$ sq. units
- **(D)** $\frac{8}{3}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{4}{3}$ sq. units**

**Detailed Solution:**

Point of intersection of curve $y=2 x-x^2$ and $x$ axis, is $0=2 \mathrm{x}-\mathrm{x}^2 \Rightarrow \mathrm{x}(\mathrm{x}-2)=0 \Rightarrow \mathrm{x}=0,2$
When $\mathrm{x}=0, \mathrm{y}=0$ and when $\mathrm{x}=2, \mathrm{y}=0$
Refer figure
Required area is shaded
$\begin{aligned}
& A=\int_0^2\left(2 x-x^2\right) d x \\
& =2\left[\frac{x^2}{2}\right]_0^2-\left[\frac{x^2}{3}\right]_0^2 \\
& =(4)-\left(\frac{8}{3}\right)=\frac{4}{3}
\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/NspAqrK8pyIuKca6npzWxpDR0mLxsmuEhzuqQS5lOag.original.fullsize.png">

</details>

---

### Q44. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The area of the region include between the parabolas $y^2=8 x$ and $\mathrm{x}^2=8 \mathrm{y}$, is

**Options:**

- **(A)** $\frac{128}{3}$ sq. units
- **(B)** $\frac{64}{3}$ sq. units
- **(C)** $\frac{32 \sqrt{8}}{3}$ sq. units
- **(D)** $\frac{16 \sqrt{8}}{3}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{64}{3}$ sq. units**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/px9tGNNB3LxK-jOXzECOsWjTq_y-DmeM7Ww3mSPtqGU.original.fullsize.png">

Refer figure
Required area is shaded. Point of intersection of given curves are $\mathrm{y}^2=8 \mathrm{x}$ and $\mathrm{x}^2=8 \mathrm{y}$ i.e.
$$
\begin{aligned}
& \left(\frac{x^2}{8}\right)^2=8 x \Rightarrow x\left(x^3-512\right)=0 \\
& \therefore O \equiv(0,0) \text { and } P \equiv(8,8) \\
& A=\int_0^8(2 \sqrt{2})(\sqrt{x}) d x-\int_0^8 \frac{x^2}{8} d x \\
& \left.=\frac{2 \sqrt{2}}{\left(\frac{3}{2}\right)} x^{\frac{3}{2}}\right]_0^8-\frac{1}{24}\left[x^3\right]_0^8=\left(\frac{4 \sqrt{2}}{3}\right)(8 \sqrt{8})-\frac{1}{24}(512)=\frac{64}{3} \text { sq. units }
\end{aligned}
$$

</details>

---

### Q45. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area bounded by the parabola $y^2=x$ and the line $x+y=2$ in the first quadrant is

**Options:**

- **(A)** $\frac{7}{6}$ aq. units
- **(B)** $\frac{1}{6}$ sq. units
- **(C)** $\frac{2}{3}$ sq. units
- **(D)** $\frac{6}{7}$ aq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{7}{6}$ aq. units**

**Detailed Solution:**

The point of intersection of $y^2=x$ and $x+y=2$ is, $(2-x)^2=x \Rightarrow x^2-5 x+4=0 \Rightarrow(x-4)(x-1)=0$
Let $\mathrm{A}=(1,1)$ in first quadrant and $\mathrm{B}=(4,-2)$ in fourth quadrant The line $\mathrm{x}+\mathrm{y}=2$ cuts $\mathrm{X}$ axis at $\mathrm{P}(2,0)$ 
Refer figure
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/RvgmiA2Xuuu7fP1W4cCmHT_YlxIdAmvJNXyvPfYRJVI.original.fullsize.png">

Required area is shaded
$$
\begin{aligned}
& \therefore \mathrm{A}=\int_0^1 \sqrt{\mathrm{x}} \mathrm{dx}+\int_1^2(2-\mathrm{x}) \mathrm{dx} \\
& =\left[\frac{\mathrm{x}^{\frac{2}{3}}}{\left(\frac{3}{2}\right)}\right]_0^1+[2 \mathrm{x}]_1^2-\left[\frac{\mathrm{x}^2}{2}\right]_1^2 \\
& =\left[\left(\frac{2}{3}\right)(1)\right]+[2(2-1)]-\left[\left(\frac{4-1}{2}\right)\right]=\frac{2}{3}+2-\frac{3}{2} \\
& =\frac{7}{6} \text { sq. units }
\end{aligned}
$$

</details>

---

### Q46. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The area bounded between the curve $x^2=y$ and the line $y=4 x$ is

**Options:**

- **(A)** $\frac{32}{3}$ sq. units
- **(B)** $\frac{8}{3}$ sq. units
- **(C)** $\frac{1}{3}$ sq. units
- **(D)** $\frac{16}{3}$sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{32}{3}$ sq. units**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/pXJ1GXcXyEZlNRUlSOqhGUxatJR6Czt_GJ7hrUYMhto.original.fullsize.png">

Required area is shaded.
Point of intersection of given curves are $(0,0)$ and $(4,16)$
$$
\begin{aligned}
& \therefore A=\int_0^4\left(4 x-x^2\right) d x \\
& =4 \int_0^4 x d x-\int_0^4 x^2 d x=4\left[\frac{x^2}{2}\right]_0^4-\left[\frac{x^3}{3}\right]_0^4 \\
& =2(16)-\frac{(4)^2}{3}=32-\frac{64}{3}=\frac{32}{3} \text { sq. units }
\end{aligned}
$$

</details>

---

### Q47. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area bounded by the parabola $y^2=x$, the straight line $y=4$ and $\mathrm{Y}$ axis is

**Options:**

- **(A)** $2 \sqrt{7}$ sq. unit
- **(B)** $\frac{64}{3}$ sq. units
- **(C)** $\frac{16}{3}$ sq. units
- **(D)** $7 \sqrt{2}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{64}{3}$ sq. units**

**Detailed Solution:**

Refer figure
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/qNxQRrlDG_R83Nsv3uFQjnmB-V3a2H4QBoBDIfXHFHo.original.fullsize.png">

Required area is shaded.
Point of intersection of $y^2=x$ and $y=4$ is $A \equiv(16,4)$
$$
\begin{aligned}
\therefore A & =\int_0^4 y^2 d y \\
& =\left[\frac{y^3}{3}\right]_0^4=\frac{64}{3} \text { sq. units }
\end{aligned}
$$

</details>

---

### Q48. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The area of the region bounded by the curve $y^2=4 x$ and the line $y=x$ is

**Options:**

- **(A)** $\frac{8}{3}$ sq. units
- **(B)** $\frac{5}{8}$ sq. units
- **(C)** $\frac{3}{8}$ sq. units
- **(D)** $\frac{3}{5}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{8}{3}$ sq. units**

**Detailed Solution:**

Refer figure, point of intersection of given curves are $\mathrm{x}^2=4 \mathrm{x}$ $\Rightarrow \mathrm{x}(\mathrm{x}-4)=0$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/zWRPuN2NRT2XN6BkvRJfJI9Ivn2cPUq39guOiC399nI.original.fullsize.png">


$$
\therefore \mathrm{O} \equiv(0,0) \text { and } \mathrm{P} \equiv(4,4)
$$
Required area is shaded.
$$
\begin{aligned}
& \therefore A=\int_0^4(\sqrt{4 x}-x) d x=2 \int_0^4 x^{\frac{1}{2}} d x-\int_0^4 x d x \\
& =2\left[\frac{x^{\frac{3}{2}}}{\left(\frac{3}{2}\right)}\right]_0^4-\left[\frac{x^2}{2}\right]_0^4-\left(\frac{4}{3}\right)(4 \times 2)-\frac{16}{2} \\
& =\frac{32}{3}-\frac{16}{2}=\frac{16}{6}=\frac{8}{3} \text { sq. units. }
\end{aligned}
$$

</details>

---

### Q49. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The area bounded by the parabola $y=x^2$ and the line $y=x$ is

**Options:**

- **(A)** $\frac{1}{2}$ sq. units
- **(B)** $\frac{1}{3}$ sq. units
- **(C)** $\frac{2}{3}$ sq. units
- **(D)** $\frac{1}{6}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{6}$ sq. units**

**Detailed Solution:**

The required area is shaded The point of intersection of the curves are $x^2=x \Rightarrow x(x-1)=0$ i.e. $O(0,0)$ and $P(1,1)$

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Xwg7FViJEMMxSjwhKcaJ09t6HmYE8z4Mlkohk5QFWL8.original.fullsize.png">


$$
\begin{aligned}
& \therefore A=\int_0^1\left(x-x^2\right) d x \\
& =\left[\frac{x^2}{2}\right]_0^1-\left[\frac{x^3}{3}\right]_0^1=\frac{1}{2}-\frac{1}{3}=\frac{1}{6}
\end{aligned}
$$

</details>

---

### Q50. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area bounded by the parabola $y=x^2$ and the line $y=x$ is

**Options:**

- **(A)** $\frac{1}{2}$ sq. units
- **(B)** $\frac{1}{3}$ sq. units
- **(C)** $\frac{2}{3}$ sq. units
- **(D)** $\frac{1}{6}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{6}$ sq. units**

**Detailed Solution:**

The required area is shaded
The point of intersection of the curves are $x^2=x \Rightarrow x(x-1)=0$ i.e. $O(0,0)$ and $P(1,1)$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/xJJn8Y0x1m3UG1doYeB7La_7VwA9GDZJ8b2n4rgqVNE.original.fullsize.png">

$\begin{aligned} & \therefore A=\int_0^1\left(x-x^2\right) d x \\ & =\left[\frac{x^2}{2}\right]_0^1-\left[\frac{x^3}{3}\right]_0^1=\frac{1}{2}-\frac{1}{3}=\frac{1}{6}\end{aligned}$

</details>

---

### Q51. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region included between the parabola $y^{2}=x$ and the line $x+y=2$ in the first quardrant is

**Options:**

- **(A)** $\frac{1}{6}$ sq. units
- **(B)** $2 \frac{7}{6} \mathrm{sq} .$ units
- **(C)** $\frac{1}{2} \mathrm{sq}$. units
- **(D)** $\frac{2}{3}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \frac{7}{6} \mathrm{sq} .$ units**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/1GojwibaartrHirh762selFLOT5AIPmx9n29JF2fzoc.original.fullsize.png">

Point of intersection of $y^{2}=x$ and $x+y=2$ is
$$
(2-x)^{2}=x \quad \Rightarrow x^{2}-4 x-x+4=0
$$
$$
x^{2}-5 x+4=0 \Rightarrow(x-4)(x-1)=0 \Rightarrow x=1,4
$$
But since we want area in $1^{\text {st }}$ quadrant only, we take $x=1$ $\therefore y^{2}=1 \Rightarrow y=\pm 1 \Rightarrow y=1$ in $1^{\text {st }}$ quadrant.
$\therefore A \equiv(1,1)$ and $P \equiv(1,0)$
Point of intersection of $x+y=2$ with $X$ axis is $B=(2,0)$
Hence area required is
$$
\begin{array}{l}
=\int_{0}^{1} \sqrt{x} d x+\int_{1}^{2}(2-x) d x \\
=\frac{2}{3}[x \sqrt{x}]_{0}^{1}+2[x]_{1}^{2}-\frac{1}{2}\left[x^{2}\right]_{1}^{2} \\
=\frac{2}{3}+2-\left(\frac{1}{2} \times 3\right)=\frac{2}{3}+2-\frac{3}{2}=\frac{4+12-9}{6}=\frac{7}{6}
\end{array}
$$

</details>

---

### Q52. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area of the triangle formed by the lines joining vertex of the parabola $x^{2}=12 y$
to the extremities of its latus rectum is

**Options:**

- **(A)** 38 sq. units
- **(B)** 18 sq. units
- **(C)** 12 sq. units
- **(D)** 28 sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 18 sq. units**

**Detailed Solution:**

(D)
$x^{2}=12 y \Rightarrow 4 b=12 \Rightarrow b=3$
Co-ordinates of latus return are $(\pm 2 b, b)$
$\therefore \mathrm{L}_{1} \equiv(6,3)$ and $\mathrm{L}_{2} \equiv(-6,3)$
Coordinates of focus $S \equiv(0,3)$
$\therefore \mathrm{A}\left(\Delta \mathrm{OL}_{1} \mathrm{~L}_{2}\right)=\frac{1}{2} \times 12 \times 3=18$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/nwMB1bA9Ejcj4AmcGbE2dWcXSwOLHYFnZwipKgnmIwM.original.fullsize.png">

</details>

---

### Q53. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area included between the parabolas $y^{2}=5 x$ and $x^{2}=5 y$ is

**Options:**

- **(A)** $\frac{25}{7}$ sq. units
- **(B)** $\frac{25}{3}$ sq. units
- **(C)** $\frac{25}{4}$ sq. units
- **(D)** $25 \mathrm{sq}$. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{25}{3}$ sq. units**

**Detailed Solution:**

(C)
Prabolas$y^{2}=5 x$ and $x^{2}=5 y$ intersect at
$\frac{x^{2}}{5}=5 x \Rightarrow x^{*}=5^{3} x \Rightarrow x\left(x^{3}-125\right)=0 \Rightarrow x=0.5 \Rightarrow y=0,5$
Let points of intersection be $Q(0,0)$ and $A(5.5)$. Required area is shaded. Ares included becween the parabolas
$=\int \sqrt{5 x}-\frac{x}{5} d x$
$\left.=\frac{\sqrt{5} x}{3}-\frac{x^{3}}{15}=\frac{2}{3}\right)(\sqrt{5})(5 \sqrt{5})-\frac{125}{15}$
$=\frac{50}{3}-\frac{125}{15}=\frac{25}{3}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/3LXsyTob-oAVtq0IqU9HY-3pK8nmnI77EXdl16fbY7Q.original.fullsize.png">

</details>

---

### Q54. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by the curve $y=4 x^{3}-6 x^{2}+4 x+1$ and the lines $x=1, x=5$ and $x$ axis is

**Options:**

- **(A)** 428 sq. units
- **(B)** 400 sq. units
- **(C)** 334 sq. units
- **(D)** 378 sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 428 sq. units**

**Detailed Solution:**

(C)
Required area is shaded.
$\begin{array}{l}
\int_{1}^{5} 4 x^{3}-6 x^{2}+4 x+1 d x \\
=\left[\frac{4 x^{4}}{4}-\frac{6 x^{3}}{3}+\frac{4 x^{2}}{2}+x\right]_{1}^{5} \\
=\left[x^{4}-2 x^{3}+2 x^{2}+x\right]_{1}^{5} \\
=\left[5^{4}-2(5)^{3}+2(5)^{2}+5\right]-\left[1^{4}-2(1)^{3}+2(1)^{2}+1\right] \\
=[625-250+50+5]-[1-2+2+1] \\
=430-2=428 \text { sq. units }
\end{array}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/l3sRApn8PUFF4xKZhSXj62ovnlN7GAK8qvu1qyr0FIc.original.fullsize.png">

</details>

---

### Q55. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area of the region bounded by the curve $\mathrm{y}=x^{2}+1$, the lines $\mathrm{x}=1, \mathrm{x}=2$ and the $\mathrm{X}$ - axis is

**Options:**

- **(A)** $\frac{13}{3}$ sq. units
- **(B)** $\frac{10}{3}$ sq. units
- **(C)** $\frac{16}{3}$ sq. units
- **(D)** $\frac{19}{3}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{10}{3}$ sq. units**

**Detailed Solution:**

$\begin{aligned} A &=\int_{1}^{2}\left(x^{2}+1\right) d x \\ &=\left[\frac{x^{3}}{3}+x\right]_{1}^{2}=\left(\frac{8}{3}+2\right)-\left(\frac{1}{3}+1\right)=\frac{10}{3} \end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/0ul2d96Jv3tJ7jtK7Fgtl1QHE_RJH0KbMFmgSH3LKs4.original.fullsize.png">

</details>

---

### Q56. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area bounded by the parabola $y^{2}=16 x$ and its latus - rectum in the first quadrant is

**Options:**

- **(A)** $128$ sq. units
- **(B)** $\frac{64}{3}$ sq. units
- **(C)** $\frac{128}{3}$ sq. units
- **(D)** $64$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{64}{3}$ sq. units**

**Detailed Solution:**

We have parabola $y^{2}=16 x \Rightarrow 4 a=16 \Rightarrow a=4$.
Hence coordinates of end points of latus rectum are $(4, \pm 8)$
Required area is shaded.
$$
\begin{aligned}
\text { Area } &=4 \int_{0}^{4} \sqrt{x} \mathrm{dx}=4\left[\frac{x^{\frac{3}{2}}}{\frac{3}{2}}\right]_{0}^{4} \\
&=4 \times \frac{2}{3}\left[4^{\frac{3}{2}}-0\right]=4 \times \frac{2}{3} \times 8=\frac{64}{3} \text { sq. units }
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/f7l7SSgh6_AVFZrRIJuzwRzLHIPxLPuxQibiR8ToYtQ.original.fullsize.png">

</details>

---

### Q57. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area bounded by the circle  $x^{2}+y^{2}=16$ and lines x=0 and  x=2 is

**Options:**

- **(A)** $\left[4 \sqrt{3}+\frac{8 \pi}{3}\right]$ sq. units
- **(B)** $\frac{1}{2}\left[4 \sqrt{3}+\frac{8 \pi}{3}\right]$ sq. units
- **(C)** $\left[4 \sqrt{3}-\frac{8 \pi}{3}\right]$ sq. units
- **(D)** $\frac{1}{2}\left[4 \sqrt{3}-\frac{8 \pi}{3}\right]$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[4 \sqrt{3}+\frac{8 \pi}{3}\right]$ sq. units**

**Detailed Solution:**

Given equation of circle is $x^{2}+y^{2}=16$
$\therefore y^{2}=16-x^{2} \therefore y=\sqrt{16-x^{2}}$
Required area is shaded.
$A=2 \mathrm{~A}(\mathrm{OABCO})$
$\begin{aligned} \text { Area } &=2 \int_{0}^{2} \sqrt{16-x^{2}} \mathrm{dx} \\ &=2\left[\frac{x}{2} \sqrt{16-x^{2}}+\frac{16}{2} \sin ^{-1} \frac{x}{4}\right]_{0}^{2} \\ &=2\left\{\frac{2}{2} \sqrt{12}+8 \sin ^{-1} \frac{1}{2}-0\right\}=2\left[2 \sqrt{3}+8\left(\frac{\pi}{6}\right)\right]=4 \sqrt{3}+\frac{8 \pi}{3} \end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ZRBl9kDyWpzMu2rykqGRRc6XvCHj2oVf3xyVGl9MoDI.original.fullsize.png">

</details>

---

### Q58. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by the parabola $y^{2}=8 x$ and its latus rectum is

**Options:**

- **(A)** $\frac{16}{3}$ sq. units
- **(B)** $\frac{8}{3}$ sq. units
- **(C)** $\frac{32}{3}$ sq. units
- **(D)** $\frac{4}{3}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{32}{3}$ sq. units**

**Detailed Solution:**

We have parabola $\mathrm{y}^{2}=8 \mathrm{x} \Rightarrow 4 \mathrm{a}=8 \Rightarrow \mathrm{a}=2$
Hence coordinates of latus rectum are
$=(\mathrm{a}, \pm 2 \mathrm{a}) \text { i.e. }(2,4) \text { and }(2,-4)$
Required area is shaded in figure.
$\begin{aligned}
\therefore A &=2 \int_{0}^{2} \sqrt{8 x} d x=4 \sqrt{2} \int_{0}^{2} x^{\frac{1}{2}} d x \\
&=4 \sqrt{2}\left[\frac{x^{\frac{3}{2}}}{\left(\frac{3}{2}\right)}\right]_{0}^{2}=\frac{8 \sqrt{2}}{3}(2 \sqrt{2})=\frac{32}{3}
\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/_O2sRr9Fqzy582lVFN4afe7fVukvp5WEPSZ6I2nWowE.original.fullsize.png">

</details>

---

### Q59. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by the curve <math><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math> and the line <math><mi>y</mi><mo>=</mo><mi>x</mi></math> is ________ square units.

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>**

**Detailed Solution:**

Given curves <math><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math> and <math><mi>y</mi><mo>=</mo><mi>x</mi></math>  
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/6a36e769-129f-497b-a14a-445cb27f1316.png"> 
<math><mi>y</mi><mo>=</mo><mi>x</mi></math>  
<math><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math>  
Points of intersection of curve 
<math><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math> and <math><mi>y</mi><mo>=</mo><mi>x</mi></math> is <math><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> and   <math><mi>x</mi><mo>=</mo><mn>1</mn></math>  
Hence, required area <math><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup><mrow><mfenced separators="|"><mrow><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></math>  
<math><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mrow><mi>d</mi><mi>x</mi></math>  
<math><msubsup><mrow><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math> sq. unit

</details>

---

### Q60. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region enclosed between pair of line <math><mi>x</mi><mi>y</mi><mo>=</mo><mn>0</mn></math> and the lines <math><mi>x</mi><mi>y</mi><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>20</mn><mo>=</mo><mn>0</mn></math> is …..

**Options:**

- **(A)** 20 square units
- **(B)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math> square units
- **(C)** <math><mn>10</mn><mi></mi></math> square units
- **(D)** <math><mn>6</mn><mi></mi></math> square units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 20 square units**

**Detailed Solution:**

Given pair of lines 
<math><mi>x</mi><mi>y</mi><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>20</mn><mo>=</mo><mn>0</mn></math>  
<math><mo>&#8658;</mo><mi>x</mi><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mn>4</mn><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>  
<math><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>  
<math><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>4</mn><mo>,</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>5</mn></math>  
and also, <math><mi>x</mi><mi>y</mi><mo>=</mo><mn>0</mn></math>  
<math><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>y</mi><mo>=</mo><mn>0</mn></math>  
Now, draw the graph of the pairs of line 
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/f24c4e85-7e95-4464-a8a5-a8058d218c66.png"> 
<math><mo>∴</mo></math> Required area of bounded region 
<math><mo>=</mo><mn>4</mn><mo>×</mo><mn>5</mn><mo>=</mo><mn>20</mn><mi>s</mi><mi>q</mi><mo>.</mo><mi>u</mi><mi>n</mi><mi>i</mi><mi>t</mi><mi>s</mi></math>

</details>

---

### Q61. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn><mi>y</mi><mo>,</mo><mi> </mi><mi>y</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi> </mi><mi>y</mi><mo>=</mo><mn>4</mn></math> and the <math><mo>y-</mo></math>axis lying in the first quadrant is _______ square units.

**Options:**

- **(A)** <math><mfrac><mrow><mn>22</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>28</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mn>30</mn></math>
- **(D)** <math><mfrac><mrow><mn>21</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>28</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/2786.png" style="width: 171px; height: 135px;" />
Required area <math> <mrow> <mi>A=</mi><mstyle displaystyle="true"> <mrow><munderover> <mo>∫</mo> <mn>1</mn> <mn>4</mn> </munderover> <mrow> <mi>x</mi><mi>d</mi><mi>y</mi><mo>=</mo><mn>2</mn></mrow> </mrow> </mstyle><mstyle displaystyle="true"> <mrow><munderover> <mo>∫</mo> <mn>1</mn> <mn>4</mn> </munderover> <mrow> <msqrt> <mi>y</mi> </msqrt> <mi>d</mi><mi>y</mi></mrow> </mrow> </mstyle></mrow> </math>
<math> <mrow> <mi>A</mi><mo>=</mo><mn>2</mn><msubsup> <mrow> <mrow><mo>(</mo> <mrow> <mfrac> <mrow> <msup> <mi>y</mi> <mrow> <mfrac> <mn>3</mn> <mn>2</mn> </mfrac> </mrow> </msup> </mrow> <mrow> <mfrac> <mn>3</mn> <mn>2</mn> </mfrac> </mrow> </mfrac> </mrow> <mo>)</mo></mrow></mrow> <mn>1</mn> <mn>4</mn> </msubsup> </mrow> </math>
<math> <mrow> <mi>A</mi><mo>=</mo><mfrac> <mn>4</mn> <mn>3</mn> </mfrac> <mrow><mo>(</mo> <mrow> <mn>8</mn><mo>−</mo><mn>1</mn></mrow> <mo>)</mo></mrow><mo>=</mo><mfrac> <mn>4</mn> <mn>3</mn> </mfrac> <mrow><mo>(</mo> <mn>7</mn> <mo>)</mo></mrow><mo>=</mo><mfrac> <mrow> <mn>28</mn></mrow> <mn>3</mn> </mfrac> </mrow> </math>

</details>

---

### Q62. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `1`

The area of the region bounded by the curves, $y^{2}=8 x$ and $y=x$ is

**Options:**

- **(A)** $\frac{64}{3}$
- **(B)** $\frac{32}{3}$
- **(C)** $\frac{16}{3}$
- **(D)** $\frac{8}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{32}{3}$**

**Detailed Solution:**

Given curves,
$$
y^{2}=8x...(i)
$$
and
$$
y=x...(ii)
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/OfPwuv5cJB8vGG27kSvKbCcoUEhvO3-boE4rY2lFdhA.original.fullsize.png">

On solving Eqs. (i) and (ii), we get 
$\begin{aligned} x^{2}-8 x &=0 \\ x(x-8) &=0 \\ \Rightarrow \quad x &=0,8 \end{aligned}$
and $\quad y=0,8$
$\begin{aligned} \therefore \text { Required area, }(O P A) &=\int_{0}^{8}(\sqrt{8 x}-x) d x \\ &=\left[2 \sqrt{2} \cdot \frac{2}{3} \cdot x^{3 / 2}-\frac{x^{2}}{2}\right]_{0}^{8} \end{aligned}$
$=\frac{4 \sqrt{2}}{3} \cdot(8)^{3 / 2}-\frac{(8)^{2}}{2}$
$=\frac{4 \sqrt{2}}{3} \cdot(2)^{3} \cdot 2 \sqrt{2}-\frac{64}{2}$
$=\frac{16}{3} \times 8-\frac{64}{2}=64\left(\frac{2}{3}-\frac{1}{2}\right)$
$=64 \times \frac{(4-3)}{6}=64 \times \frac{1}{6}=\frac{32}{3}$

</details>

---

### Q63. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

The area of the region bounded by the curves $x^{2}+y^{2}=8$ and
$y^{2}=2 x$ is

**Options:**

- **(A)** $2 \pi+\frac{1}{3}$
- **(B)** $\pi+\frac{1}{3}$
- **(C)** $2 \pi+\frac{4}{3}$
- **(D)** $\pi+\frac{4}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 \pi+\frac{4}{3}$**

**Detailed Solution:**

Given curves,
$$
\begin{aligned}
x^{2}+y^{2} &=8...(i)\\
and\quad
y^{2} &=2 x...(ii)
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/2tMUyhuPJflHvdPW2a7_z8xDy68J7_el-AkC6PHfqcg.original.fullsize.png">

On solving Eqs. (i) and (ii), we get
$\therefore$
$$
\begin{aligned}
x^{2}+2 x-8 &=0 \\
x^{2}+4 x-2 x-8 &=0 \\
x(x+4)-2(x+4) &=0 \\
(x-2)(x+4) &=0 \\
x=2 \text { and } y &=\pm 2
\end{aligned}
$$
$\therefore$ Required area
$$
\begin{array}{l}
=2[\text { Area of } O A P+\text { Area of } P A B] \\
=2\left[\int_{0}^{2} \sqrt{2 x} d x+\int_{2}^{2 \sqrt{2}} \sqrt{8-x^{2}} d x\right] \\
=2\left[\sqrt{2}\left(x^{3 / 2} \cdot \frac{2}{3}\right)_{0}^{2}+\left(\frac{x}{2} \sqrt{8-x^{2}}\right.\right. \\
\left.\left.+\frac{8}{2} \sin ^{-1} \frac{x}{2 \sqrt{2}}\right)_{2}^{2 \sqrt{2}}\right] \\
=2\left[\frac{2 \sqrt{2}}{3}\left(2^{3 / 2}\right)+4 \times \frac{\pi}{2}-2-4 \times \frac{\pi}{4}\right]
\end{array}
$$
$=2\left[\frac{2 \sqrt{2}}{3} \cdot 2 \sqrt{2}+2 \pi-2-\pi\right]$
$=2\left[\frac{8}{3}-2+\pi\right]=2\left(\frac{2}{3}+\pi\right)=2 \pi+\frac{4}{3}$

</details>

---

### Q64. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

The area bounded by the parabola $y^{2}=x$, straight line $y=4$ and $y$ -axis is square units is

**Options:**

- **(A)** $16 / 3$ sq. unit
- **(B)** $64 / 3$ sq. unit
- **(C)** $7 \sqrt{2}$ sq. unit
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $64 / 3$ sq. unit**

**Detailed Solution:**

Line $y=4$ meets the parabola $y^{2}=x$ at $A$
$\therefore \quad 16=x$ and $A$ is $(16,4)$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/RvIpFbAkd77tMbJovtTli5PFOcfb2nl35XgTAQbadMo.original.fullsize.png">

$\therefore$ Required area
$$
\begin{array}{l}
=\int_{y=0}^{4} x d y \\
=\int_{y=0}^{4} y^{2} d y \\
=\left[y^{3} / 3\right]_{0}^{4} \\
=\frac{64}{3} \text { sq units }
\end{array}
$$

</details>

---

### Q65. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

Area bounded between the curve $x^{2}=y$ and the line $y=4 x$ is

**Options:**

- **(A)** $\frac{32}{3} \mathrm{sq}$ unit
- **(B)** $\frac{1}{3} \mathrm{sq}$ unit
- **(C)** $\frac{8}{3}$ sq unit
- **(D)** $\frac{16}{3} \mathrm{sq}$ unit

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{32}{3} \mathrm{sq}$ unit**

**Detailed Solution:**

Given curves are $x^{2}=y$ and $y=4 x$
Intersection points are $(0,0)$ and $(4,16)$ $\begin{aligned} \therefore \text { Required area } &=\int_{0}^{4}\left(4 x-x^{2}\right) d x \\ &=\left[\frac{4 x^{2}}{2}-\frac{x^{3}}{3}\right]_{0}^{4} \\ &=\left[32-\frac{64}{3}\right] \\ &=\frac{32}{3} \mathrm{sq} \text { unit } \end{aligned}$

</details>

---

### Q66. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `1`

The volume of solid generated by revolving about the $y$ -axis the figure bounded by the parabola $y=x^{2}$ and $x=y^{2}$ is

**Options:**

- **(A)** $\frac{21}{5} \pi$
- **(B)** $\frac{24}{5} \pi$
- **(C)** $\frac{2}{15} \pi$
- **(D)** $\frac{5}{24} \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{15} \pi$**

**Detailed Solution:**

$V=\int_{0}^{1} \pi x^{2} d y$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ppRY2-Y9rv6YC7Pn-jyMe8g_ljEhNIdLA48zJM-qeJY.original.fullsize.png">

$=\left|\pi \int_{0}^{1}\left(y^{4}-y\right) d y\right|$
$=\left|\pi\left[\frac{y^{5}}{5}-\frac{y^{2}}{2}\right]_{0}^{1}\right|$
$=\left|\pi\left[\frac{1}{5}-\frac{1}{3}\right]\right|$
$=\left|\frac{-2 \pi}{15}\right|=\frac{2 \pi}{15}$

</details>

---

