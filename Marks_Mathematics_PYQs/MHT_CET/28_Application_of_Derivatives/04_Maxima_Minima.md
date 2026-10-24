# MHT CET Mathematics - Application of Derivatives

## Topic 4: Maxima Minima

**Total Questions:** 83

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = 5x^3 + 2x^2 - 3x + 1$ has a local maxima and a local minima at $x = \sin\theta, \pi < \theta < \dfrac{3\pi}{2}$ and $x = \cos\phi, \dfrac{3\pi}{2} < \phi < 2\pi$ respectively, then $(\tan\theta)(\tan\phi) = \ldots$

**Options:**

- **(A)** $\dfrac{3\sqrt{3}}{2}$
- **(B)** $\dfrac{-3\sqrt{3}}{2}$
- **(C)** $\dfrac{3\sqrt{2}}{2}$
- **(D)** $\dfrac{-3\sqrt{2}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{-3\sqrt{2}}{2}$**

**Detailed Solution:**

Given $f(x) = 5x^3 + 2x^2 - 3x + 1$

Differentiating with respect to $x$:

$f'(x) = 15x^2 + 4x - 3$

For local maxima and minima, $f'(x) = 0$:

$15x^2 + 9x - 5x - 3 = 0$

$3x(5x + 3) - 1(5x + 3) = 0$

$(3x - 1)(5x + 3) = 0$

$x = \dfrac{1}{3}$ or $x = -\dfrac{3}{5}$

Finding the second derivative:

$f''(x) = 30x + 4$

At $x = -\dfrac{3}{5}$, $f''\left(-\dfrac{3}{5}\right) = -14 < 0$, so $x = -\dfrac{3}{5}$ is a point of local maxima.

At $x = \dfrac{1}{3}$, $f''\left(\dfrac{1}{3}\right) = 14 > 0$, so $x = \dfrac{1}{3}$ is a point of local minima.

Given that local maxima is at $x = \sin\theta$ for $\pi < \theta < \dfrac{3\pi}{2}$:

$\sin\theta = -\dfrac{3}{5}$

Since $\theta$ is in the third quadrant, $\tan\theta$ is positive:

$\tan\theta = \dfrac{3}{4}$

Given that local minima is at $x = \cos\phi$ for $\dfrac{3\pi}{2} < \phi < 2\pi$:

$\cos\phi = \dfrac{1}{3}$

Since $\phi$ is in the fourth quadrant, $\tan\phi$ is negative:

$\tan\phi = -\sqrt{\sec^2\phi - 1} = -\sqrt{9 - 1} = -2\sqrt{2}$

Therefore, $(\tan\theta)(\tan\phi) = \left(\dfrac{3}{4}\right)(-2\sqrt{2}) = \dfrac{-3\sqrt{2}}{2}$

Answer: $\dfrac{-3\sqrt{2}}{2}$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The maximum volume (in cubic units) of a right circular cylinder for which the sum of the square of its height and the square of its radius of base $48$, is

**Options:**

- **(A)** $48\pi$
- **(B)** $64\pi$
- **(C)** $128\pi$
- **(D)** $16\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $128\pi$**

**Detailed Solution:**

Let $r$ be the radius of the base and $h$ be the height of the cylinder.

Given that the sum of the squares of the height and the radius is $48$:

$r^2 + h^2 = 48 \Rightarrow r^2 = 48 - h^2$

The volume of the cylinder is given by:

$V = \pi r^2 h$

Substituting the value of $r^2$:

$V = \pi (48 - h^2) h = \pi (48h - h^3)$

To find the maximum volume, differentiate $V$ with respect to $h$ and equate it to zero:

$\dfrac{dV}{dh} = \pi (48 - 3h^2) = 0$

$3h^2 = 48 \Rightarrow h^2 = 16 \Rightarrow h = 4$

Differentiating again to check for maxima:

$\dfrac{d^2V}{dh^2} = -6\pi h$

At $h = 4$, $\dfrac{d^2V}{dh^2} = -24\pi < 0$, which confirms that the volume is maximum.

Substituting $h = 4$ into the equation for $r^2$:

$r^2 = 48 - 16 = 32$

The maximum volume is:

$V = \pi (32)(4) = 128\pi$

Answer: $128\pi$

</details>

---

### Q3. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A rectangular sheet of paper has its area $32$ meters$^2$. The margins at the top and bottom are $50$ cm each and at the sides $25$ cm each. If the area of the printed space is maximum, then the dimensions of the paper are

**Options:**

- **(A)** $16$ meters and $2$ meters
- **(B)** $30$ meters and $2$ meters
- **(C)** $8$ meters and $4$ meters
- **(D)** $25$ meters and $7$ meters

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $8$ meters and $4$ meters**

**Detailed Solution:**

Let the dimensions of the rectangular sheet of paper be $x$ meters and $y$ meters.

The area of the paper is given as $xy = 32 \Rightarrow y = \dfrac{32}{x}$.

The margins at the top and bottom are $50$ cm $= 0.5$ m each, so the total vertical margin is $1$ m.

The margins at the sides are $25$ cm $= 0.25$ m each, so the total horizontal margin is $0.5$ m.

The dimensions of the printed space are $(x - 0.5)$ and $(y - 1)$.

The area of the printed space is $A = (x - 0.5)(y - 1)$.

Substituting $y = \dfrac{32}{x}$, we get:

$A = (x - 0.5)\left(\dfrac{32}{x} - 1\right)$

$A = 32 - x - \dfrac{16}{x} + 0.5$

$A = 32.5 - \left(x + \dfrac{16}{x}\right)$

For the printed area $A$ to be maximum, the term $\left(x + \dfrac{16}{x}\right)$ must be minimum.

Using the AM-GM inequality for positive numbers $x$ and $\dfrac{16}{x}$:

$\dfrac{x + \dfrac{16}{x}}{2} \geq \sqrt{x \times \dfrac{16}{x}}$

$x + \dfrac{16}{x} \geq 2 \times 4 = 8$

The minimum value is attained when $x = \dfrac{16}{x} \Rightarrow x^2 = 16 \Rightarrow x = 4$ meters.

When $x = 4$, $y = \dfrac{32}{4} = 8$ meters.

Thus, the dimensions of the paper are $8$ meters and $4$ meters.

Answer: $8$ meters and $4$ meters

</details>

---

### Q4. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

On the interval $[0, 1]$, the function $f(x) = x^{25}(1 - x)^{75}$ attains its maximum value at the point $x = $....

**Options:**

- **(A)** $0$
- **(B)** $\dfrac{1}{4}$
- **(C)** $\dfrac{1}{2}$
- **(D)** $\dfrac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{4}$**

**Detailed Solution:**

Given $f(x) = x^{25}(1 - x)^{75}$

Differentiating with respect to $x$:

$f'(x) = 25x^{24}(1 - x)^{75} - 75x^{25}(1 - x)^{74}$

$f'(x) = 25x^{24}(1 - x)^{74} [ (1 - x) - 3x ]$

$f'(x) = 25x^{24}(1 - x)^{74} (1 - 4x)$

For maximum or minimum, $f'(x) = 0$

$25x^{24}(1 - x)^{74} (1 - 4x) = 0$

$x = 0, 1, \dfrac{1}{4}$

At $x = 0$ and $x = 1$, $f(x) = 0$.

For $x \in (0, 1)$, $f(x) > 0$.

Thus, $f(x)$ attains its maximum value at $x = \dfrac{1}{4}$.

Answer: $\dfrac{1}{4}$

</details>

---

### Q5. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A tank with a rectangular base and rectangular sides, open at the top is made. Depth of the tank is $4$ m and its volume is $36$ cubic meters. For making a tank cost of base material used is Rs. $100$ per sq. meter and that of sides is Rs. $50$ per sq. meter. Then minimum cost of tank is ..............

**Options:**

- **(A)** Rs. $1100$
- **(B)** Rs. $2200$
- **(C)** Rs. $3300$
- **(D)** Rs. $4400$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Rs. $3300$**

**Detailed Solution:**

Let the length and breadth of the base of the tank be $x$ and $y$ respectively.

Given depth $h = 4$ m and volume $V = 36$ m$^3$.

$V = x \times y \times h \Rightarrow 4xy = 36 \Rightarrow xy = 9$

Cost of the base $= 100 \times xy = 100 \times 9 = 900$

Area of the four sides $= 2(xh + yh) = 2(4)(x + y) = 8(x + y)$

Cost of the sides $= 50 \times 8(x + y) = 400(x + y)$

Total cost $C = 900 + 400(x + y)$

To minimize $C$, we need to minimize $x + y$.

Using AM-GM inequality for $x, y > 0$:

$\dfrac{x + y}{2} \geq \sqrt{xy}$

$x + y \geq 2\sqrt{9} = 6$

Minimum value of $x + y$ is $6$, which occurs when $x = y = 3$.

Minimum cost $C = 900 + 400(6) = 900 + 2400 = 3300$

Answer: Rs. $3300$

</details>

---

### Q6. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The coordinates of the points on the curve $4y = x^2$ that are nearest to the point $(0,5)$ are ...

**Options:**

- **(A)** $(-2\sqrt{3}, 3)$
- **(B)** $(2\sqrt{3}, -3)$
- **(C)** $(3, 2\sqrt{3})$
- **(D)** $(2\sqrt{3}, 2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(-2\sqrt{3}, 3)$**

**Detailed Solution:**

Let the point on the curve be $(x, y)$.

The square of the distance $S$ between $(x, y)$ and $(0, 5)$ is given by:

$S = x^2 + (y - 5)^2$

Since the point lies on the curve $4y = x^2$, we substitute $x^2 = 4y$ into the equation for $S$:

$S = 4y + (y - 5)^2$

$S = y^2 - 6y + 25$

To find the minimum distance, we differentiate $S$ with respect to $y$ and equate it to zero:

$\dfrac{dS}{dy} = 2y - 6 = 0$

$y = 3$

Since $\dfrac{d^2S}{dy^2} = 2 > 0$, the distance is minimum at $y = 3$.

Substituting $y = 3$ in $x^2 = 4y$, we get:

$x^2 = 12 \Rightarrow x = \pm 2\sqrt{3}$

The points on the curve nearest to $(0, 5)$ are $(2\sqrt{3}, 3)$ and $(-2\sqrt{3}, 3)$.

Answer: $(-2\sqrt{3}, 3)$

</details>

---

### Q7. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number 28 is divided into two positive parts such that the sum of the cube of one part and the square of the other part is minimum, then the absolute difference between the two parts is

**Options:**

- **(A)** $24$
- **(B)** $12$
- **(C)** $8$
- **(D)** $20$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $20$**

**Detailed Solution:**

Let the two positive parts of $28$ be $x$ and $28 - x$, where $0 < x < 28$.

Let $S$ be the sum of the cube of one part and the square of the other part. Then,

$S = x^3 + (28 - x)^2$

To find the minimum value of $S$, we differentiate $S$ with respect to $x$ and equate it to zero:

$\dfrac{dS}{dx} = 3x^2 + 2(28 - x)(-1)$

$\dfrac{dS}{dx} = 3x^2 + 2x - 56$

Setting $\dfrac{dS}{dx} = 0$, we get:

$3x^2 + 2x - 56 = 0$

$3x^2 + 14x - 12x - 56 = 0$

$x(3x + 14) - 4(3x + 14) = 0$

$(x - 4)(3x + 14) = 0$

Since $x$ must be positive, we have $x = 4$.

Now, we check the second derivative to confirm it is a minimum:

$\dfrac{d^2S}{dx^2} = 6x + 2$

At $x = 4$, $\dfrac{d^2S}{dx^2} = 6(4) + 2 = 26 > 0$, which confirms that $S$ is minimum at $x = 4$.

The two parts are $4$ and $28 - 4 = 24$.

The absolute difference between the two parts is $|24 - 4| = 20$.

Answer: $20$

</details>

---

### Q8. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A cylindrical tank without a top lid is being manufactured to hold a fixed volume of $125\pi$ cubic cm. The minimum surface area required to construct this tank is ............square cm

**Options:**

- **(A)** $75\pi$
- **(B)** $50\pi$
- **(C)** $25\pi$
- **(D)** $125\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $75\pi$**

**Detailed Solution:**

Let $r$ be the radius and $h$ be the height of the cylindrical tank.

Given the volume $V = \pi r^2 h = 125\pi$

$\Rightarrow h = \dfrac{125}{r^2}$

The surface area of the tank without a top lid is $S = 2\pi r h + \pi r^2$

Substituting the value of $h$, we get:

$S = 2\pi r \left(\dfrac{125}{r^2}\right) + \pi r^2 = \dfrac{250\pi}{r} + \pi r^2$

To find the minimum surface area, we differentiate $S$ with respect to $r$ and equate it to zero:

$\dfrac{dS}{dr} = -\dfrac{250\pi}{r^2} + 2\pi r = 0$

$\Rightarrow 2\pi r = \dfrac{250\pi}{r^2}$

$\Rightarrow r^3 = 125 \Rightarrow r = 5$

Also, $\dfrac{d^2S}{dr^2} = \dfrac{500\pi}{r^3} + 2\pi > 0$ for $r = 5$, which confirms a minimum.

The minimum surface area is:

$S = \dfrac{250\pi}{5} + \pi (5)^2 = 50\pi + 25\pi = 75\pi$

Answer: $75\pi$

</details>

---

### Q9. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The minimum value of $\dfrac{\log x}{x}$ in the interval $(2, \infty)$ is

**Options:**

- **(A)** $0$
- **(B)** $e$
- **(C)** $\dfrac{1}{e}$
- **(D)** Does not exist

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Does not exist**

**Detailed Solution:**

Let $f(x) = \dfrac{\log x}{x}$ for $x \in (2, \infty)$.

Differentiating with respect to $x$, we get $f'(x) = \dfrac{1 - \log x}{x^2}$.

Setting $f'(x) = 0$ gives $\log x = 1 \Rightarrow x = e$.

For $x \in (2, e)$, $f'(x) > 0$, so $f(x)$ is strictly increasing.

For $x \in (e, \infty)$, $f'(x) < 0$, so $f(x)$ is strictly decreasing.

Thus, $f(x)$ attains its maximum value at $x = e$.

To find the minimum value, we check the behavior at the boundaries of the interval.

At $x = 2$, $f(2) = \dfrac{\log 2}{2} > 0$.

As $x \rightarrow \infty$, $\lim_{x \rightarrow \infty} \dfrac{\log x}{x} = 0$.

Since $f(x) > 0$ for all $x \in (2, \infty)$ and $f(x) \rightarrow 0$ as $x \rightarrow \infty$, the infimum of $f(x)$ is $0$.

However, there is no finite $x \in (2, \infty)$ for which $f(x) = 0$.

Therefore, the minimum value of $f(x)$ does not exist.

Answer: Does not exist

</details>

---

### Q10. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The maximum value of $\left(\dfrac{1}{x}\right)^x$, $x > 0$ is

**Options:**

- **(A)** $e^e$
- **(B)** $e^{-e}$
- **(C)** $e^{1/e}$
- **(D)** $\left(\dfrac{1}{e}\right)^{1/e}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $e^{1/e}$**

**Detailed Solution:**

Let $y = \left(\dfrac{1}{x}\right)^x = x^{-x}$

Taking natural logarithm on both sides:

$\ln y = -x \ln x$

Differentiating with respect to $x$:

$\dfrac{1}{y} \dfrac{dy}{dx} = - \left( \ln x + x \cdot \dfrac{1}{x} \right) = -(\ln x + 1)$

$\dfrac{dy}{dx} = -x^{-x}(\ln x + 1)$

For maximum or minimum value, $\dfrac{dy}{dx} = 0$

$-x^{-x}(\ln x + 1) = 0$

Since $x^{-x} \neq 0$ for $x > 0$, we have $\ln x + 1 = 0 \Rightarrow x = \dfrac{1}{e}$

For $0 < x < \dfrac{1}{e}$, $\dfrac{dy}{dx} > 0$ and for $x > \dfrac{1}{e}$, $\dfrac{dy}{dx} < 0$

Thus, $y$ attains its maximum value at $x = \dfrac{1}{e}$

The maximum value is $y_{max} = \left(\dfrac{1}{1/e}\right)^{1/e} = e^{1/e}$

Answer: $e^{1/e}$

</details>

---

### Q11. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A wire 40 metre in length is to be cut into two pieces. One piece is formed into a square and the other piece into a circle. The lengths of the two pieces so that the combined area of the square and the circle is minimum, are respectively

**Options:**

- **(A)** $\dfrac{160}{\pi + 4}, \dfrac{40\pi}{\pi + 4}$
- **(B)** $\dfrac{\pi + 4}{160}, \dfrac{40\pi}{\pi + 4}$
- **(C)** $\dfrac{160}{\pi + 4}, \dfrac{\pi + 4}{40\pi}$
- **(D)** $30, 10$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{160}{\pi + 4}, \dfrac{40\pi}{\pi + 4}$**

**Detailed Solution:**

Let the length of the piece for the square be $x$ and for the circle be $40 - x$.

Perimeter of the square $= x \Rightarrow$ side $= \dfrac{x}{4}$

Area of the square, $A_1 = \dfrac{x^2}{16}$

Circumference of the circle $= 40 - x \Rightarrow$ radius $r = \dfrac{40 - x}{2\pi}$

Area of the circle, $A_2 = \pi r^2 = \dfrac{(40 - x)^2}{4\pi}$

Total area, $A = \dfrac{x^2}{16} + \dfrac{(40 - x)^2}{4\pi}$

For minimum area, $\dfrac{dA}{dx} = 0$

$\dfrac{2x}{16} - \dfrac{2(40 - x)}{4\pi} = 0$

$\dfrac{x}{8} = \dfrac{40 - x}{2\pi}$

$\pi x = 160 - 4x$

$x(\pi + 4) = 160 \Rightarrow x = \dfrac{160}{\pi + 4}$

Length of the other piece $= 40 - x = 40 - \dfrac{160}{\pi + 4} = \dfrac{40\pi}{\pi + 4}$

Since $\dfrac{d^2A}{dx^2} = \dfrac{1}{8} + \dfrac{1}{2\pi} > 0$, the area is minimum for these lengths.

Answer: $\dfrac{160}{\pi + 4}, \dfrac{40\pi}{\pi + 4}$

</details>

---

### Q12. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The difference between the local extreme values of the function $f(x) = 2x^3 - 15x^2 + 36x + 40$ is ......

**Options:**

- **(A)** $4$
- **(B)** $3$
- **(C)** $2$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1$**

**Detailed Solution:**

Given $f(x) = 2x^3 - 15x^2 + 36x + 40$

Differentiating with respect to $x$:

$f'(x) = 6x^2 - 30x + 36$

For local extrema, $f'(x) = 0$:

$6(x^2 - 5x + 6) = 0$

$(x - 2)(x - 3) = 0$

$x = 2, 3$

Evaluating the function at the critical points:

$f(2) = 2(2)^3 - 15(2)^2 + 36(2) + 40 = 16 - 60 + 72 + 40 = 68$

$f(3) = 2(3)^3 - 15(3)^2 + 36(3) + 40 = 54 - 135 + 108 + 40 = 67$

The difference between the local extreme values is $68 - 67 = 1$.

Answer: $1$

</details>

---

### Q13. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A wire of length $64$ m is to be bent to form a rectangle such that its area is maximum, then its area is.....

**Options:**

- **(A)** $156$ sq.m
- **(B)** $324$ sq.m
- **(C)** $256$ sq.m
- **(D)** $320$ sq.m

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $256$ sq.m**

**Detailed Solution:**

Let the length and breadth of the rectangle be $x$ and $y$ respectively.

The perimeter of the rectangle is equal to the length of the wire.

$2(x + y) = 64$

$x + y = 32$

The area of the rectangle is $A = xy$.

Using the AM-GM inequality for positive numbers $x$ and $y$:

$\dfrac{x + y}{2} \ge \sqrt{xy}$

$\dfrac{32}{2} \ge \sqrt{A}$

$16 \ge \sqrt{A}$

$A \le 256$

The maximum area of the rectangle is $256$ sq.m, which occurs when $x = y = 16$ m (when the rectangle is a square).

</details>

---

### Q14. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The minimum value of the slope of the tangent to curve $\mathrm{y}=x^3-3 x^2+2 x+93$ is

**Options:**

- **(A)** 1
- **(B)** -1
- **(C)** 2
- **(D)** -2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -1**

**Detailed Solution:**

The slope of the tangent to the curve is given by the derivative of $y$ with respect to $x$.

$m = \dfrac{dy}{dx} = \dfrac{d}{dx}(x^3 - 3x^2 + 2x + 93)$

$m = 3x^2 - 6x + 2$

To find the minimum value of the slope $m$, we can complete the square or use derivatives.

$m = 3(x^2 - 2x) + 2$

$m = 3(x^2 - 2x + 1) - 3 + 2$

$m = 3(x - 1)^2 - 1$

Since the square of a real number is always non-negative, $3(x - 1)^2 \ge 0$ for all real $x$.

Therefore, the minimum value of $m$ is $-1$, which occurs at $x = 1$.

Answer: -1

</details>

---

### Q15. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The Maximum value of $\left(\frac{1}{x}\right)^x$ is

**Options:**

- **(A)** $\mathrm{e}^{1/\mathrm{e}}$
- **(B)** $\mathrm{e}$
- **(C)** $\frac{1}{\mathrm{e}}$
- **(D)** $\mathrm{e}^{-1/\mathrm{e}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{e}^{1/\mathrm{e}}$**

**Detailed Solution:**

Let $y = \left(\dfrac{1}{x}\right)^x = x^{-x}$

Taking logarithm on both sides, we get:

$\ln y = -x \ln x$

Differentiating with respect to $x$:

$\dfrac{1}{y} \dfrac{dy}{dx} = - \left(x \cdot \dfrac{1}{x} + \ln x \cdot 1\right)$

$\dfrac{dy}{dx} = -y (1 + \ln x)$

For maximum or minimum value, $\dfrac{dy}{dx} = 0$

$-y (1 + \ln x) = 0$

Since $y = x^{-x} > 0$ for $x > 0$, we have:

$1 + \ln x = 0$

$\ln x = -1$

$x = \mathrm{e}^{-1} = \dfrac{1}{\mathrm{e}}$

For $x < \dfrac{1}{\mathrm{e}}$, $\dfrac{dy}{dx} > 0$ and for $x > \dfrac{1}{\mathrm{e}}$, $\dfrac{dy}{dx} < 0$. Thus, $y$ is maximum at $x = \dfrac{1}{\mathrm{e}}$.

The maximum value is:

$y_{max} = \left(\dfrac{1}{1/\mathrm{e}}\right)^{1/\mathrm{e}} = \mathrm{e}^{1/\mathrm{e}}$

Answer: $\mathrm{e}^{1/\mathrm{e}}$

</details>

---

### Q16. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x+\mathrm{y}=6, x \geqslant 0, y \geqslant 0$, then the maximum value of $x^2 \mathrm{y}$ is

**Options:**

- **(A)** 32
- **(B)** 30
- **(C)** 34
- **(D)** 36

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 32**

**Detailed Solution:**

Given $x + y = 6 \Rightarrow y = 6 - x$

Let $P = x^2 y = x^2(6 - x) = 6x^2 - x^3$

Differentiating with respect to $x$, we get:

$\dfrac{dP}{dx} = 12x - 3x^2$

For maximum or minimum value, $\dfrac{dP}{dx} = 0$

$12x - 3x^2 = 0 \Rightarrow 3x(4 - x) = 0 \Rightarrow x = 0$ or $x = 4$

Differentiating again with respect to $x$:

$\dfrac{d^2P}{dx^2} = 12 - 6x$

At $x = 4$, $\dfrac{d^2P}{dx^2} = 12 - 6(4) = -12 < 0$

Thus, $P$ is maximum at $x = 4$.

When $x = 4$, $y = 6 - 4 = 2$

Maximum value of $x^2 y = (4)^2(2) = 32$

Answer: 32

</details>

---

### Q17. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The minimum value of $ax + by$ where $xy = c^2$ and $a, b, c, x, y > 0$ is

**Options:**

- **(A)** $2 c \sqrt{a b}$
- **(B)** $2 a b \sqrt{c}$
- **(C)** $-2 c \sqrt{a b}$
- **(D)** $2 c(a b)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 c \sqrt{a b}$**

**Detailed Solution:**

Using the AM-GM inequality for positive numbers $ax$ and $by$:

$\dfrac{ax + by}{2} \ge \sqrt{(ax)(by)}$

$\dfrac{ax + by}{2} \ge \sqrt{abxy}$

Substituting $xy = c^2$ into the inequality:

$\dfrac{ax + by}{2} \ge \sqrt{abc^2}$

Since $a, b, c > 0$, we get:

$\dfrac{ax + by}{2} \ge c\sqrt{ab}$

$ax + by \ge 2c\sqrt{ab}$

The minimum value of $ax + by$ is $2c\sqrt{ab}$.

Answer: $2 c \sqrt{a b}$

</details>

---

### Q18. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{y}=\alpha \log |x|+\beta x^3-x$ has extreme values at $x=-1$ and $x=1$, then $\alpha$ and $\beta$ are respectively

**Options:**

- **(A)** 0 and $\frac{1}{3}$
- **(B)** 0 and $\frac{-1}{3}$
- **(C)** $\frac{-1}{3}$ and $\frac{1}{3}$
- **(D)** $\frac{1}{3}$ and $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0 and $\frac{1}{3}$**

**Detailed Solution:**

Given function is $y = \alpha \log |x| + \beta x^3 - x$

Differentiating with respect to $x$, we get:

$\dfrac{dy}{dx} = \dfrac{\alpha}{x} + 3\beta x^2 - 1$

Since the function has extreme values at $x = -1$ and $x = 1$, the derivative must be zero at these points.

At $x = -1$:

$\dfrac{\alpha}{-1} + 3\beta (-1)^2 - 1 = 0$

$-\alpha + 3\beta = 1$  ... (i)

At $x = 1$:

$\dfrac{\alpha}{1} + 3\beta (1)^2 - 1 = 0$

$\alpha + 3\beta = 1$  ... (ii)

Adding equations (i) and (ii):

$6\beta = 2 \Rightarrow \beta = \dfrac{1}{3}$

Subtracting equation (i) from (ii):

$2\alpha = 0 \Rightarrow \alpha = 0$

Therefore, $\alpha = 0$ and $\beta = \dfrac{1}{3}$.

Answer: 0 and $\frac{1}{3}$

</details>

---

### Q19. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A manufacturer sells $x$ items at a price of rupees $\left(6-\frac{x}{40}\right)$ each. The cost price of $x$ items is Rs. $\left(\frac{x}{5}+193\right)$. The maximum profit in Rs. _______ is

**Options:**

- **(A)** 134.4
- **(B)** 144.3
- **(C)** 143.4
- **(D)** 133.4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 143.4**

**Detailed Solution:**

The revenue function $R(x)$ for selling $x$ items is given by:

$R(x) = x \left(6 - \dfrac{x}{40}\right) = 6x - \dfrac{x^2}{40}$

The cost function $C(x)$ is given by:

$C(x) = \dfrac{x}{5} + 193$

The profit function $P(x)$ is the difference between revenue and cost:

$P(x) = R(x) - C(x) = 6x - \dfrac{x^2}{40} - \left(\dfrac{x}{5} + 193\right)$

$P(x) = \dfrac{29x}{5} - \dfrac{x^2}{40} - 193$

For maximum profit, we set the first derivative $P'(x)$ to zero:

$P'(x) = \dfrac{29}{5} - \dfrac{2x}{40} = \dfrac{29}{5} - \dfrac{x}{20} = 0$

$\dfrac{x}{20} = \dfrac{29}{5} \Rightarrow x = 116$

Checking the second derivative:

$P''(x) = -\dfrac{1}{20} < 0$

Since $P''(x) < 0$, the profit is maximum at $x = 116$.

Substituting $x = 116$ into the profit function:

$P(116) = \dfrac{29(116)}{5} - \dfrac{(116)^2}{40} - 193$

$P(116) = 672.8 - 336.4 - 193$

$P(116) = 336.4 - 193 = 143.4$

The maximum profit is Rs. $143.4$.

Answer: 143.4

</details>

---

### Q20. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum of two positive numbers is 4 . The minimum value of the sum of their reciprocals is

**Options:**

- **(A)** $\frac{3}{4}$
- **(B)** $\frac{6}{5}$
- **(C)** $1$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

Let the two positive numbers be $x$ and $y$.

Given $x + y = 4$.

We need to find the minimum value of $\dfrac{1}{x} + \dfrac{1}{y}$.

Using the relation between Arithmetic Mean (AM) and Harmonic Mean (HM) for two positive numbers:

$\text{AM} \ge \text{HM}$

$\dfrac{x + y}{2} \ge \dfrac{2}{\dfrac{1}{x} + \dfrac{1}{y}}$

Substituting $x + y = 4$:

$\dfrac{4}{2} \ge \dfrac{2}{\dfrac{1}{x} + \dfrac{1}{y}}$

$2 \ge \dfrac{2}{\dfrac{1}{x} + \dfrac{1}{y}}$

$\dfrac{1}{x} + \dfrac{1}{y} \ge 1$

The minimum value of the sum of their reciprocals is $1$, which occurs when $x = y = 2$.

Answer: $1$

</details>

---

### Q21. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The maximum value of $x^{2 / 3}+(x-2)^{2 / 3}$ on $[0, 2]$ is

**Options:**

- **(A)** 0
- **(B)** 2
- **(C)** $2^{\frac{2}{3}}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2**

**Detailed Solution:**

Let $f(x) = x^{2/3} + (x-2)^{2/3}$

Differentiating with respect to $x$, we get:

$f'(x) = \dfrac{2}{3}x^{-1/3} + \dfrac{2}{3}(x-2)^{-1/3}$

For critical points, $f'(x) = 0$:

$\dfrac{1}{x^{1/3}} + \dfrac{1}{(x-2)^{1/3}} = 0$

$\dfrac{1}{x^{1/3}} = -\dfrac{1}{(x-2)^{1/3}}$

$x^{1/3} = -(x-2)^{1/3}$

Cubing both sides:

$x = -(x-2)$

$2x = 2 \Rightarrow x = 1$

Now, we evaluate $f(x)$ at the critical point $x = 1$ and the endpoints $x = 0$ and $x = 2$:

$f(0) = 0^{2/3} + (-2)^{2/3} = 2^{2/3}$

$f(2) = 2^{2/3} + 0^{2/3} = 2^{2/3}$

$f(1) = 1^{2/3} + (1-2)^{2/3} = 1 + (-1)^{2/3} = 1 + 1 = 2$

Comparing the values, since $2 > 2^{2/3}$, the maximum value of the function on $[0, 2]$ is $2$.

Answer: 2

</details>

---

### Q22. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An open tank with a square bottom is to contain 4000 cubic cm . of liquid. The dimensions of the tank so that the surface area of the tank is minimum, is

**Options:**

- **(A)** side $=20 \mathrm{~cm}$, height $=10 \mathrm{~cm}$
- **(B)** side $=10 \mathrm{~cm}$, height $=20 \mathrm{~cm}$
- **(C)** side $=10 \mathrm{~cm}$, height $=40 \mathrm{~cm}$
- **(D)** side $=20 \mathrm{~cm}$, height $=05 \mathrm{~cm}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) side $=20 \mathrm{~cm}$, height $=10 \mathrm{~cm}$**

**Detailed Solution:**

Let the side of the square base be $x$ and the height be $y$.

Volume of the tank, $V = x^2y = 4000 \Rightarrow y = \dfrac{4000}{x^2}$

Surface area of the open tank, $S = x^2 + 4xy$

Substituting the value of $y$, we get:

$S = x^2 + 4x\left(\dfrac{4000}{x^2}\right) = x^2 + \dfrac{16000}{x}$

For minimum surface area, $\dfrac{dS}{dx} = 0$

$\dfrac{dS}{dx} = 2x - \dfrac{16000}{x^2} = 0$

$2x^3 = 16000 \Rightarrow x^3 = 8000 \Rightarrow x = 20$

Now, $y = \dfrac{4000}{(20)^2} = \dfrac{4000}{400} = 10$

Also, $\dfrac{d^2S}{dx^2} = 2 + \dfrac{32000}{x^3} > 0$ at $x = 20$, which confirms the minimum.

Thus, side $= 20$ cm and height $= 10$ cm.

Answer: side $=20 \mathrm{~cm}$, height $=10 \mathrm{~cm}$

</details>

---

### Q23. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A wire of length 8 units is cut into two parts which are bent respectively in the form of a square and a circle. The least value of the sum of the areas so formed is

**Options:**

- **(A)** $\frac{8}{\pi+4}$
- **(B)** $\frac{64}{\pi+4}$
- **(C)** $\frac{2}{\pi+4}$
- **(D)** $\frac{16}{\pi+4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{16}{\pi+4}$**

**Detailed Solution:**

Let the length of the wire used for the square be $x$ and for the circle be $8 - x$.

Side of the square $= \dfrac{x}{4}$

Radius of the circle $= \dfrac{8 - x}{2\pi}$

Sum of their areas, $A = \left(\dfrac{x}{4}\right)^2 + \pi\left(\dfrac{8 - x}{2\pi}\right)^2 = \dfrac{x^2}{16} + \dfrac{(8 - x)^2}{4\pi}$

For minimum area, $\dfrac{dA}{dx} = 0$

$\dfrac{2x}{16} - \dfrac{2(8 - x)}{4\pi} = 0$

$\dfrac{x}{8} = \dfrac{8 - x}{2\pi}$

$\pi x = 32 - 4x \Rightarrow x = \dfrac{32}{\pi + 4}$

The minimum area is obtained by substituting $x$ back into $A$:

$A = \dfrac{1}{16}\left(\dfrac{32}{\pi + 4}\right)^2 + \dfrac{1}{4\pi}\left(8 - \dfrac{32}{\pi + 4}\right)^2$

$A = \dfrac{64}{(\pi + 4)^2} + \dfrac{1}{4\pi}\left(\dfrac{8\pi}{\pi + 4}\right)^2$

$A = \dfrac{64}{(\pi + 4)^2} + \dfrac{16\pi}{(\pi + 4)^2}$

$A = \dfrac{16(4 + \pi)}{(\pi + 4)^2} = \dfrac{16}{\pi + 4}$

Answer: $\frac{16}{\pi+4}$

</details>

---

### Q24. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The function $x^5-5 x^4+5 x^3-10$ has a maximum, when $x$ is equal to

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $2$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1$**

**Detailed Solution:**

Let $f(x) = x^5 - 5x^4 + 5x^3 - 10$

Differentiating with respect to $x$, we get:
$f'(x) = 5x^4 - 20x^3 + 15x^2$

For maximum or minimum, $f'(x) = 0$
$\Rightarrow 5x^2(x^2 - 4x + 3) = 0$
$\Rightarrow 5x^2(x - 1)(x - 3) = 0$
$\Rightarrow x = 0, 1, 3$

Now, finding the second derivative:
$f''(x) = 20x^3 - 60x^2 + 30x$

Checking the sign of $f''(x)$ at the critical points:
At $x = 1$, $f''(1) = 20(1)^3 - 60(1)^2 + 30(1) = -10 < 0$
At $x = 3$, $f''(3) = 20(3)^3 - 60(3)^2 + 30(3) = 90 > 0$
At $x = 0$, $f''(0) = 0$

Since $f''(1) < 0$, the function $f(x)$ has a local maximum at $x = 1$.

Answer: $1$

</details>

---

### Q25. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A manufacturer produces $x$ items per week at a total cost of Rs $\left(x^2+78 x+2500\right)$. The price per unit is given by $8 x=600-\mathrm{p}$ where ' p ' is the price of each unit. Then the maximum profit obtained is

**Options:**

- **(A)** Rs. 5069
- **(B)** Rs. 15138
- **(C)** Rs. 7569
- **(D)** Rs. 2500

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Rs. 5069**

**Detailed Solution:**

Total cost $C(x) = x^2 + 78x + 2500$

Price per unit $p = 600 - 8x$

Total revenue $R(x) = p \times x = (600 - 8x)x = 600x - 8x^2$

Profit $P(x) = R(x) - C(x)$

$P(x) = (600x - 8x^2) - (x^2 + 78x + 2500) = -9x^2 + 522x - 2500$

For maximum profit, $P'(x) = 0$

$-18x + 522 = 0 \Rightarrow x = 29$

$P''(x) = -18 < 0$, which confirms a maximum at $x = 29$.

Maximum profit $P(29) = -9(29)^2 + 522(29) - 2500$

$P(29) = -7569 + 15138 - 2500 = 5069$

Answer: Rs. 5069

</details>

---

### Q26. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

20 is divided into two parts so that the product of the cube of one part and the square of the other part is maximum, then these two parts are

**Options:**

- **(A)** 15,5
- **(B)** 16,4
- **(C)** 12,8
- **(D)** 14,6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 12,8**

**Detailed Solution:**

Let the two parts be $x$ and $20 - x$.

Let the product be $f(x) = x^3(20 - x)^2$.

Differentiating with respect to $x$, we get:

$f'(x) = 3x^2(20 - x)^2 + x^3 \cdot 2(20 - x)(-1)$

$f'(x) = x^2(20 - x)[3(20 - x) - 2x]$

$f'(x) = x^2(20 - x)(60 - 5x)$

For maximum or minimum, $f'(x) = 0$.

$x^2(20 - x)(60 - 5x) = 0$

Since the parts are non-zero, $x \neq 0$ and $x \neq 20$.

$60 - 5x = 0 \Rightarrow x = 12$

The other part is $20 - 12 = 8$.

Thus, the two parts are $12$ and $8$.

Answer: 12,8

</details>

---

### Q27. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A population $\mathrm{p}(\mathrm{t})$ of 1000 bacteria introduced into a nutrient medium grows according to the relation $\mathrm{p}(\mathrm{t})=1000+\frac{1000 \mathrm{t}}{100+\mathrm{t}^2}$. The maximum size of this bacterial population is

**Options:**

- **(A)** $1100$
- **(B)** $1250$
- **(C)** $1050$
- **(D)** $950$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1050$**

**Detailed Solution:**

Given the population function:

$\mathrm{p}(\mathrm{t}) = 1000 + \dfrac{1000 \mathrm{t}}{100 + \mathrm{t}^2}$

To find the maximum size of the population, we differentiate $\mathrm{p}(\mathrm{t})$ with respect to $\mathrm{t}$ and equate it to zero:

$\dfrac{d\mathrm{p}}{d\mathrm{t}} = \dfrac{d}{d\mathrm{t}} \left( 1000 + \dfrac{1000 \mathrm{t}}{100 + \mathrm{t}^2} \right)$

Using the quotient rule:

$\dfrac{d\mathrm{p}}{d\mathrm{t}} = 1000 \left[ \dfrac{(100 + \mathrm{t}^2)(1) - \mathrm{t}(2\mathrm{t})}{(100 + \mathrm{t}^2)^2} \right]$

$\dfrac{d\mathrm{p}}{d\mathrm{t}} = \dfrac{1000(100 - \mathrm{t}^2)}{(100 + \mathrm{t}^2)^2}$

For maximum population, $\dfrac{d\mathrm{p}}{d\mathrm{t}} = 0$:

$\dfrac{1000(100 - \mathrm{t}^2)}{(100 + \mathrm{t}^2)^2} = 0$

$100 - \mathrm{t}^2 = 0$

$\mathrm{t}^2 = 100$

$\mathrm{t} = 10$ (since time $\mathrm{t} \ge 0$)

Substituting $\mathrm{t} = 10$ into the original function to find the maximum population:

$\mathrm{p}(10) = 1000 + \dfrac{1000(10)}{100 + (10)^2}$

$\mathrm{p}(10) = 1000 + \dfrac{10000}{100 + 100}$

$\mathrm{p}(10) = 1000 + \dfrac{10000}{200}$

$\mathrm{p}(10) = 1000 + 50 = 1050$

Answer: $1050$

</details>

---

### Q28. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\mathrm{a} \log |x|+\mathrm{b} x^2+x$ has its extremum values at $x=-1$ and $x=2$, then

**Options:**

- **(A)** $\mathrm{a}=2, \mathrm{~b}=-1$
- **(B)** $\mathrm{a}=2, \mathrm{~b}=-\frac{1}{2}$
- **(C)** $\mathrm{a}=-2, \mathrm{~b}=\frac{1}{2}$
- **(D)** $\mathrm{a}=2, \mathrm{~b}=\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{a}=2, \mathrm{~b}=-\frac{1}{2}$**

**Detailed Solution:**

Given $y = \mathrm{a} \log |x| + \mathrm{b} x^2 + x$

Differentiating with respect to $x$, we get

$\dfrac{dy}{dx} = \dfrac{\mathrm{a}}{x} + 2\mathrm{b}x + 1$

Since the function has extremum values at $x = -1$ and $x = 2$, we have $\dfrac{dy}{dx} = 0$ at these points.

At $x = -1$:

$\dfrac{\mathrm{a}}{-1} + 2\mathrm{b}(-1) + 1 = 0$

$-\mathrm{a} - 2\mathrm{b} + 1 = 0$

$\mathrm{a} + 2\mathrm{b} = 1$

At $x = 2$:

$\dfrac{\mathrm{a}}{2} + 2\mathrm{b}(2) + 1 = 0$

$\mathrm{a} + 8\mathrm{b} + 2 = 0$

$\mathrm{a} + 8\mathrm{b} = -2$

Subtracting the first equation from the second equation:

$6\mathrm{b} = -3 \Rightarrow \mathrm{b} = -\dfrac{1}{2}$

Substituting $\mathrm{b} = -\dfrac{1}{2}$ in $\mathrm{a} + 2\mathrm{b} = 1$:

$\mathrm{a} + 2\left(-\dfrac{1}{2}\right) = 1$

$\mathrm{a} - 1 = 1 \Rightarrow \mathrm{a} = 2$

Therefore, $\mathrm{a} = 2$ and $\mathrm{b} = -\dfrac{1}{2}$.

Answer: $\mathrm{a}=2, \mathrm{~b}=-\frac{1}{2}$

</details>

---

### Q29. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An open tank with a square bottom, to contain 4000 cubic cm . of liquid, is to be constructed. The dimensions of the tank, so that the surface area of the tank is minimum, are

**Options:**

- **(A)** side of square bottom $=40 \mathrm{~cm}$, height $=10 \mathrm{~cm}$.
- **(B)** side of square bottom $=20 \mathrm{~cm}$, height $=10 \mathrm{~cm}$.
- **(C)** side of square bottom $=10 \mathrm{~cm}$, height $=40 \mathrm{~cm}$.
- **(D)** side. of square bottom $=5 \mathrm{~cm}$, height $=160 \mathrm{~cm}$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) side of square bottom $=20 \mathrm{~cm}$, height $=10 \mathrm{~cm}$.**

**Detailed Solution:**

Let $x$ be the side of the square base and $y$ be the height of the tank.

The volume of the tank is given by:
$V = x^2 y = 4000$
$\Rightarrow y = \dfrac{4000}{x^2}$

Since the tank is open at the top, its surface area $S$ consists of the base and four sides:
$S = x^2 + 4xy$

Substituting the value of $y$ into the surface area equation:
$S = x^2 + 4x \left( \dfrac{4000}{x^2} \right)$
$S = x^2 + \dfrac{16000}{x}$

To find the minimum surface area, we differentiate $S$ with respect to $x$ and equate it to zero:
$\dfrac{dS}{dx} = 2x - \dfrac{16000}{x^2} = 0$
$\Rightarrow 2x = \dfrac{16000}{x^2}$
$\Rightarrow x^3 = 8000$
$\Rightarrow x = 20$

To confirm it is a minimum, we check the second derivative:
$\dfrac{d^2S}{dx^2} = 2 + \dfrac{32000}{x^3}$
At $x = 20$, $\dfrac{d^2S}{dx^2} = 2 + \dfrac{32000}{8000} = 6 > 0$, which confirms the surface area is minimum.

Now, substituting $x = 20$ to find $y$:
$y = \dfrac{4000}{(20)^2} = \dfrac{4000}{400} = 10$

Thus, the side of the square bottom is $20$ cm and the height is $10$ cm.

Answer: side of square bottom $=20 \mathrm{~cm}$, height $=10 \mathrm{~cm}$.

</details>

---

### Q30. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of the function $\mathrm{f}(x)=2 x^3-15 x^2+36 x-48$ on the set $\mathrm{A}=\left\{x |x^2+20 \leq 9 x\right\}$ is

**Options:**

- **(A)** -16
- **(B)** -7
- **(C)** 16
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 7**

**Detailed Solution:**

The given set is $\mathrm{A}=\left\{x \mid x^2+20 \leq 9 x\right\}$.

Solving the inequality:

$x^2 - 9x + 20 \leq 0$

$(x - 4)(x - 5) \leq 0$

This gives $x \in [4, 5]$.

Now, consider the function $\mathrm{f}(x) = 2x^3 - 15x^2 + 36x - 48$.

Differentiating with respect to $x$:

$\mathrm{f}'(x) = 6x^2 - 30x + 36$

$\mathrm{f}'(x) = 6(x^2 - 5x + 6) = 6(x - 2)(x - 3)$

For $x \in [4, 5]$, both $(x - 2)$ and $(x - 3)$ are positive, which means $\mathrm{f}'(x) > 0$.

Since $\mathrm{f}'(x) > 0$ for all $x \in [4, 5]$, the function $\mathrm{f}(x)$ is strictly increasing on the interval $[4, 5]$.

Therefore, the maximum value of $\mathrm{f}(x)$ on this interval occurs at the upper bound, $x = 5$.

Substituting $x = 5$ into the function:

$\mathrm{f}(5) = 2(5)^3 - 15(5)^2 + 36(5) - 48$

$\mathrm{f}(5) = 2(125) - 15(25) + 180 - 48$

$\mathrm{f}(5) = 250 - 375 + 180 - 48$

$\mathrm{f}(5) = 430 - 423 = 7$

The maximum value of the function is $7$.

Answer: 7

</details>

---

### Q31. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\mathrm{a} \log |x|+\mathrm{b} x^2+x$ has its extreme values at $x=-1$ and $x=2$, then the value of $\left(\frac{\mathrm{a}}{\mathrm{b}}+\frac{\mathrm{b}}{\mathrm{a}}\right)$ is

**Options:**

- **(A)** $-\frac{7}{4}$
- **(B)** $-\frac{15}{4}$
- **(C)** $-\frac{17}{4}$
- **(D)** $-\frac{5}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\frac{17}{4}$**

**Detailed Solution:**

Given $y = \mathrm{a} \log |x| + \mathrm{b} x^2 + x$

Differentiating with respect to $x$, we get:

$\dfrac{dy}{dx} = \dfrac{\mathrm{a}}{x} + 2\mathrm{b}x + 1$

Since the function has extreme values at $x = -1$ and $x = 2$, $\dfrac{dy}{dx} = 0$ at these points.

For $x = -1$:

$\dfrac{\mathrm{a}}{-1} + 2\mathrm{b}(-1) + 1 = 0$

$\Rightarrow \mathrm{a} + 2\mathrm{b} = 1$

For $x = 2$:

$\dfrac{\mathrm{a}}{2} + 2\mathrm{b}(2) + 1 = 0$

$\Rightarrow \mathrm{a} + 8\mathrm{b} = -2$

Subtracting the first equation from the second equation:

$(\mathrm{a} + 8\mathrm{b}) - (\mathrm{a} + 2\mathrm{b}) = -2 - 1$

$\Rightarrow 6\mathrm{b} = -3$

$\Rightarrow \mathrm{b} = -\dfrac{1}{2}$

Substituting $\mathrm{b} = -\dfrac{1}{2}$ into the first equation:

$\mathrm{a} + 2\left(-\dfrac{1}{2}\right) = 1$

$\Rightarrow \mathrm{a} - 1 = 1$

$\Rightarrow \mathrm{a} = 2$

Now, we need to find the value of $\left(\dfrac{\mathrm{a}}{\mathrm{b}} + \dfrac{\mathrm{b}}{\mathrm{a}}\right)$:

$\dfrac{\mathrm{a}}{\mathrm{b}} = \dfrac{2}{-\dfrac{1}{2}} = -4$

$\dfrac{\mathrm{b}}{\mathrm{a}} = \dfrac{-\dfrac{1}{2}}{2} = -\dfrac{1}{4}$

$\dfrac{\mathrm{a}}{\mathrm{b}} + \dfrac{\mathrm{b}}{\mathrm{a}} = -4 - \dfrac{1}{4} = -\dfrac{17}{4}$

Answer: $-\frac{17}{4}$

</details>

---

### Q32. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A poster is to be printed on a rectangular sheet of paper of area $18 \mathrm{~m}^2$. The margins at the top and bottom of 75 cm each and at the sides 50 cm each are to be left. Then the dimensions i.e. height and breadth of the sheet so that the space available for printing is maximum, are _________ respectively.

**Options:**

- **(A)** $2 \sqrt{3} \mathrm{~m}, 3 \sqrt{3} \mathrm{~m}$
- **(B)** $3 \sqrt{3} \mathrm{~m}, 2 \sqrt{3} \mathrm{~m}$
- **(C)** $3 \mathrm{~m}, 6 \mathrm{~m}$
- **(D)** $6 \mathrm{~m}, 3 \mathrm{~m}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3 \sqrt{3} \mathrm{~m}, 2 \sqrt{3} \mathrm{~m}$**

**Detailed Solution:**

Let $h$ be the height and $b$ be the breadth of the sheet in meters.

Given the area of the sheet is $18 \mathrm{~m}^2$, we have $h \times b = 18 \Rightarrow b = \dfrac{18}{h}$.

The margins at the top and bottom are $75 \mathrm{~cm} = 0.75 \mathrm{~m}$ each, so the height of the printing space is $h - 2(0.75) = h - 1.5$.

The margins at the sides are $50 \mathrm{~cm} = 0.5 \mathrm{~m}$ each, so the breadth of the printing space is $b - 2(0.5) = b - 1$.

The area of the printed space is $A = (h - 1.5)(b - 1)$.

Substituting $b = \dfrac{18}{h}$, we get:

$A = (h - 1.5)\left(\dfrac{18}{h} - 1\right)$

$A = 18 - h - \dfrac{27}{h} + 1.5 = 19.5 - \left(h + \dfrac{27}{h}\right)$

For $A$ to be maximum, its derivative with respect to $h$ must be zero:

$\dfrac{dA}{dh} = -1 + \dfrac{27}{h^2} = 0$

$h^2 = 27 \Rightarrow h = 3\sqrt{3} \mathrm{~m}$

To confirm it is a maximum, we check the second derivative:

$\dfrac{d^2A}{dh^2} = -\dfrac{54}{h^3} < 0$ (since $h > 0$), which confirms a maximum.

The breadth is $b = \dfrac{18}{3\sqrt{3}} = 2\sqrt{3} \mathrm{~m}$.

Thus, the height and breadth are $3\sqrt{3} \mathrm{~m}$ and $2\sqrt{3} \mathrm{~m}$ respectively.

Answer: $3 \sqrt{3} \mathrm{~m}, 2 \sqrt{3} \mathrm{~m}$

</details>

---

### Q33. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of $\dfrac{\log x}{x}$ is

**Options:**

- **(A)** e
- **(B)** $2 \mathrm{e}$
- **(C)** $\dfrac{1}{\mathrm{e}}$
- **(D)** $\dfrac{2}{\mathrm{e}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{\mathrm{e}}$**

**Detailed Solution:**

Let $f(x) = \dfrac{\log x}{x}$

Differentiating with respect to $x$, we get

$f'(x) = \dfrac{x \cdot \dfrac{1}{x} - \log x \cdot 1}{x^2} = \dfrac{1 - \log x}{x^2}$

For maximum or minimum value, $f'(x) = 0$

$\dfrac{1 - \log x}{x^2} = 0$

$1 - \log x = 0$

$\log x = 1 \Rightarrow x = e$

Now, finding the second derivative:

$f''(x) = \dfrac{x^2 \left(-\dfrac{1}{x}\right) - (1 - \log x)(2x)}{x^4} = \dfrac{2 \log x - 3}{x^3}$

At $x = e$, $f''(e) = \dfrac{2(1) - 3}{e^3} = -\dfrac{1}{e^3} < 0$

Therefore, $f(x)$ attains its maximum value at $x = e$.

The maximum value is $f(e) = \dfrac{\log e}{e} = \dfrac{1}{e}$

Answer: $\dfrac{1}{\mathrm{e}}$

</details>

---

### Q34. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{f}(x)=\left(\sin ^4 x+\cos ^4 x\right), 0 \lt x \lt \dfrac{\pi}{2}$, then the function has minimum value _______ at $x=$ ________.

**Options:**

- **(A)** $0.7934, \dfrac{\pi}{9}$
- **(B)** $\dfrac{1}{2}, \dfrac{\pi}{4}$
- **(C)** $\dfrac{5}{8}, \dfrac{\pi}{3}$
- **(D)** $0.75, \dfrac{\pi}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{2}, \dfrac{\pi}{4}$**

**Detailed Solution:**

$f(x) = \sin^4 x + \cos^4 x$

$f(x) = (\sin^2 x + \cos^2 x)^2 - 2\sin^2 x \cos^2 x$

$f(x) = 1 - \dfrac{1}{2}(2\sin x \cos x)^2$

$f(x) = 1 - \dfrac{1}{2}\sin^2(2x)$

For the minimum value of $f(x)$, the term $\sin^2(2x)$ must be maximum.

The maximum value of $\sin^2(2x)$ is $1$.

Minimum value of $f(x) = 1 - \dfrac{1}{2}(1) = \dfrac{1}{2}$

This occurs when $\sin^2(2x) = 1$.

Since $0 \lt x \lt \dfrac{\pi}{2}$, we have $0 \lt 2x \lt \pi$.

$\sin(2x) = 1 \Rightarrow 2x = \dfrac{\pi}{2} \Rightarrow x = \dfrac{\pi}{4}$

Answer: $\dfrac{1}{2}, \dfrac{\pi}{4}$

</details>

---

### Q35. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If sum of two positive integers is 3 , then the maximum value of the product of first number and square of the second number is

**Options:**

- **(A)** 6
- **(B)** 4
- **(C)** 5
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 4**

**Detailed Solution:**

Let the two positive integers be $x$ and $y$.

Given $x + y = 3$.

Since $x$ and $y$ are positive integers, the only possible pairs $(x, y)$ are $(1, 2)$ and $(2, 1)$.

The product of the first number and the square of the second number is $x y^2$.

For $x = 1$ and $y = 2$, the product is $1 \times 2^2 = 4$.

For $x = 2$ and $y = 1$, the product is $2 \times 1^2 = 2$.

The maximum value of the product is $4$.

Answer: 4

</details>

---

### Q36. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A wire of length 2 units is cut into two parts, which are bent respectively to form a square of side $x$ units and a circle of radius of r units. If the sum of the areas of square and the circle so formed is minimum, then

**Options:**

- **(A)** $2 x=(\pi+4) \mathrm{r}$
- **(B)** $(4-\pi) x=\pi \mathrm{r}$
- **(C)** $x=2 r$
- **(D)** $2 x=\mathrm{r}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x=2 r$**

**Detailed Solution:**

Let the length of the wire be $2$ units.

The wire is cut into two parts to form a square of side $x$ and a circle of radius $r$.

Sum of their perimeters is equal to the total length of the wire:

$4x + 2\pi r = 2$

$2x + \pi r = 1$

$x = \dfrac{1 - \pi r}{2}$

The sum of the areas of the square and the circle is:

$A = x^2 + \pi r^2$

Substituting the value of $x$:

$A = \left(\dfrac{1 - \pi r}{2}\right)^2 + \pi r^2$

For the area to be minimum, $\dfrac{dA}{dr} = 0$:

$\dfrac{dA}{dr} = 2\left(\dfrac{1 - \pi r}{2}\right) \left(-\dfrac{\pi}{2}\right) + 2\pi r = 0$

$-\pi \left(\dfrac{1 - \pi r}{2}\right) + 2\pi r = 0$

Dividing by $\pi$:

$-\left(\dfrac{1 - \pi r}{2}\right) + 2r = 0$

Since $x = \dfrac{1 - \pi r}{2}$, we get:

$-x + 2r = 0$

$x = 2r$

Answer: $x=2 r$

</details>

---

### Q37. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A triangular park is enclosed on two sides by a fence and on the third side a straight river bank. The two sides having fence are of same length $x$.
The maximum area (in sq. units) enclosed by the park is

**Options:**

- **(A)** $\dfrac{3}{2} x^2$
- **(B)** $\sqrt{\dfrac{x^3}{8}}$
- **(C)** $\dfrac{1}{2} x^2$
- **(D)** $\pi x^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{2} x^2$**

**Detailed Solution:**

Let the angle between the two fenced sides of length $x$ be $\theta$.

The area of the triangular park is given by $A = \dfrac{1}{2} x \cdot x \cdot \sin \theta = \dfrac{1}{2} x^2 \sin \theta$.

For maximum area, $\sin \theta$ must be maximum.

The maximum value of $\sin \theta$ is $1$, which occurs at $\theta = 90^{\circ}$.

Therefore, the maximum area enclosed by the park is $A_{\max} = \dfrac{1}{2} x^2 (1) = \dfrac{1}{2} x^2$.

Answer: $\dfrac{1}{2} x^2$

</details>

---

### Q38. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of the function
$f(x)=3 x^3-18 x^2+27 x-40$
on the set $\mathrm{S}=\left\{x \in \mathbb{R} / x^2+30 \leq 11 x\right\}$ is

**Options:**

- **(A)** -122
- **(B)** -222
- **(C)** 222
- **(D)** 122

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 122**

**Detailed Solution:**

The given set is $S = \{x \in \mathbb{R} \mid x^2 + 30 \leq 11x\}$.

Solving the inequality:
$x^2 - 11x + 30 \leq 0$
$(x - 5)(x - 6) \leq 0$
$\Rightarrow x \in [5, 6]$

The given function is $f(x) = 3x^3 - 18x^2 + 27x - 40$.

Differentiating with respect to $x$:
$f'(x) = 9x^2 - 36x + 27$
$f'(x) = 9(x^2 - 4x + 3)$
$f'(x) = 9(x - 1)(x - 3)$

For $x \in [5, 6]$, both $(x - 1)$ and $(x - 3)$ are positive, which means $f'(x) > 0$.

Since $f'(x) > 0$ for all $x \in [5, 6]$, the function $f(x)$ is strictly increasing on this interval.

Therefore, the maximum value of $f(x)$ on the set $S$ occurs at the upper bound of the interval, which is $x = 6$.

Substituting $x = 6$ into $f(x)$:
$f(6) = 3(6)^3 - 18(6)^2 + 27(6) - 40$
$f(6) = 3(216) - 18(36) + 162 - 40$
$f(6) = 648 - 648 + 162 - 40$
$f(6) = 122$

Answer: 122

</details>

---

### Q39. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{f}(x)=5-|x-2|$ and $\mathrm{g}(x)=|x+1|, x \in \mathrm{R}$ If $\mathrm{f}(x)$ attains maximum value at $\alpha$ and $\mathrm{g}(x)$ attains minimum value at $\beta$, then $\lim _{x \rightarrow-\alpha \beta} \frac{(x-1)\left(x^2-5 x+6\right)}{x^2-6 x+8}$ is equal to

**Options:**

- **(A)** $\frac {1}{2}$
- **(B)** $\frac {-3}{2}$
- **(C)** $\frac {-1}{2}$
- **(D)** $\frac {3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac {1}{2}$**

**Detailed Solution:**

$\begin{aligned}
& |x-2| \geq 0 \\
& \Rightarrow-|x-2| \leq 0 \\
& \Rightarrow 5-|x-2| \leq 5
\end{aligned}$
Maximum value of $\mathrm{f}(x)$ is 5 .
$\begin{aligned}
\therefore \quad & 5-|x-2|=5 \\
& \Rightarrow|x-2|=0 \\
& \Rightarrow x=2 \\
& \Rightarrow \alpha=2 \\
& |x+1| \geq 0
\end{aligned}$
Minimum value of $\mathrm{g}(x)$ is 0 .
$\begin{aligned}
\therefore \quad & |x+1|=0 \\
& \Rightarrow x=-1 \\
& \Rightarrow \beta=-1
\end{aligned}$
$\begin{aligned}
\therefore \quad & \lim _{x \rightarrow-\alpha \beta} \frac{(x-1)\left(x^2-5 x+6\right)}{x^2-6 x+8} \\
= & \lim _{x \rightarrow 2} \frac{(x-1)(x-2)(x-3)}{(x-2)(x-4)} \\
= & \lim _{x \rightarrow 2} \frac{(x-1)(x-3)}{x-4} \\
= & \frac{(1)(-1)}{-2} \\
= & \frac{1}{2}
\end{aligned}$

</details>

---

### Q40. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The function $\mathrm{f}(x)=x^3-6 x^2+9 x+2$ has maximum value when $x$ is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{f}(x)=x^3-6 x^2+9 x+2 \\
\therefore \quad & \mathrm{f}^{\prime}(x)=3 x^2-12 x+9
\end{aligned}$
For maximum or minimum,
$\begin{aligned}
& \mathrm{f}^{\prime}(x)=0 \\
& \Rightarrow 3 x^2-12 x+9=0 \\
& \Rightarrow 3(x-1)(x-3)=0 \\
& \Rightarrow x=1,3
\end{aligned}$
Now, $\mathrm{f}^{\prime \prime}(x)=6 x-12$
$\therefore \quad \mathrm{f}^{\prime \prime}(1)=-6 < 0$
$\therefore \quad \mathrm{f}(x)$ is maximum at $x=1$.

</details>

---

### Q41. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of the function $f(x)=3 x^3-18 x^2+27 x-40$ on the set $\mathrm{S}=\left\{x \in \mathrm{R} / x^2+30 \leq 11 x\right\}$ is

**Options:**

- **(A)** $122$
- **(B)** $-122$
- **(C)** $-222$
- **(D)** $222$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $122$**

**Detailed Solution:**

$$
\begin{aligned}
\mathrm{S} & =\left\{x \in \mathrm{R} / x^2+30 \leq 11 x\right\} \\
& =\left\{x \in \mathrm{R} / x^2-11 x+30 \leq 0\right\} \\
& =\{x \in \mathrm{R} /(x-5)(x-6) \leq 0\} \\
& =\{x \in \mathrm{R} / x \in[5,6]\} \\
\mathrm{f}(x) & =3 x^3-18 x^2+27 x-40 \\
\therefore \quad \mathrm{f}^{\prime}(x) & =9 x^2-36 x+27 \\
& =9(x-1)(x-3)>0 \quad \forall x \in[5,6]
\end{aligned}
$$
$\Rightarrow \mathrm{f}(x)$ is increasing in $[5,6]$.
$$
\begin{aligned}
\therefore \quad \text { Maximum value } & =\mathrm{f}(6) \\
& =3(6)^3-18(6)^2+27(6)-40 \\
& =122
\end{aligned}
$$

</details>

---

### Q42. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

In a triangle, the sum of lengths of two sides is $x$ and the product of the lengths of the same two sides is $y$. If $x^2-\mathrm{c}^2-y$, where $\mathrm{c}$ is the length of the third side of the triangle, then the circumradius of the triangle is

**Options:**

- **(A)** $\frac{c}{3}$
- **(B)** $\frac{c}{\sqrt{3}}$
- **(C)** $\frac{3}{2} y$
- **(D)** $\frac{y}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{c}{\sqrt{3}}$**

**Detailed Solution:**

Let $\mathrm{a}$ and $\mathrm{b}$ be the lengths of two sides of $\mathrm{a}$ triangle.
$\therefore \quad$ According to the given condition,
$$
\begin{aligned}
& \mathrm{a}+\mathrm{b}=x \text { and } \mathrm{ab}=y \\
& \therefore \quad x^2-\mathrm{c}^2=y \Rightarrow(\mathrm{a}+\mathrm{b})^2-\mathrm{c}^2=\mathrm{ab} \\
& \Rightarrow a^2+b^2+2 a b-c^2=a b \\
& \Rightarrow a^2+b^2-c^2=-a b \\
& \Rightarrow \frac{\mathrm{a}^2+\mathrm{b}^2-\mathrm{c}^2}{2 \mathrm{ab}}=-\frac{1}{2} \\
& \Rightarrow \cos \mathrm{C}=\frac{1}{2} \\
& \Rightarrow \mathrm{C}=\frac{2 \pi}{3} \\
& \Rightarrow \text { circumradius }=\frac{\mathrm{c}}{2 \sin \mathrm{C}}=\frac{\mathrm{c}}{2 \sin \left(\frac{2 \pi}{3}\right)}=\frac{\mathrm{c}}{\sqrt{3}} \\
&
\end{aligned}
$$

</details>

---

### Q43. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $x=-1$ and $x=2$ are extreme points of $\mathrm{f}(x)=\alpha \log x+\beta x^2+x, \alpha$ and $\beta$ are constants, then the value of $\alpha^2+2 \beta$ is

**Options:**

- **(A)** $-3$
- **(B)** $3$
- **(C)** $\frac{3}{2}$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3$**

**Detailed Solution:**

According to the given condition, $\mathrm{f}^{\prime}(1)=0$ and $\mathrm{f}^{\prime}(2)=0$
$$
\mathrm{f}(x)=\alpha \log x+\beta x^2+x
$$
$$
\begin{array}{ll}
\therefore & \mathrm{f}^{\prime}(x)=\frac{\alpha}{x}+2 \beta x+1 \\
\therefore & \mathrm{f}^{\prime}(-1)=0 \Rightarrow \alpha+2 \beta=1 \\
& \text { and } \mathrm{f}^{\prime}(2)=0 \Rightarrow \alpha+8 \beta=-2
\end{array}
$$
$\therefore \quad$ From (i) and (ii), we get
$$
\begin{aligned}
& \beta=\frac{-1}{2} \text { and } \alpha=2 \\
\therefore \quad & \alpha^2+2 \beta=4-1=3
\end{aligned}
$$

</details>

---

### Q44. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

An open metallic tank is to be constructed, with a square base and vertical sides, having volume 500 cubic meter. Then the dimensions of the tank, for minimum area of the sheet metal used in its construction, are

**Options:**

- **(A)** $5 \mathrm{~m}, 5 \mathrm{~m}, 10 \mathrm{~m}$
- **(B)** $10 \mathrm{~m}, 10 \mathrm{~m}, 5 \mathrm{~m}$
- **(C)** $2 \mathrm{~m}, 2 \mathrm{~m}, 8 \mathrm{~m}$
- **(D)** $15 \mathrm{~m}, 15 \mathrm{~m}, 5 \mathrm{~m}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $10 \mathrm{~m}, 10 \mathrm{~m}, 5 \mathrm{~m}$**

**Detailed Solution:**

Let the length, breadth and depth of open tank be $x, x$ and $y$ respectively.
Volume $(\mathrm{V})=x^2 y$
$\therefore \quad 500=x^2 y$... (i)
Total surface area of open tank is given by
$\mathrm{S}=x^2+4 x y$... (ii)
From (i), $y=\frac{500}{x^2}$
From (ii), $\mathrm{S}=x^2+4 x \times \frac{500}{x^2}$
$=x^2+\frac{2000}{x}$
Differentiating w.r.t. $x$, we get
$\frac{\mathrm{dS}}{\mathrm{d} x}=2 x-\frac{2000}{x^2}$
For minimum area, $\frac{\mathrm{dS}}{\mathrm{d} x}=0$
$\begin{aligned}
\therefore \quad & 2 x-\frac{2000}{x^2}=0 \\
& \Rightarrow 2000=2 x^3 \\
& \Rightarrow x^3=1000
\end{aligned}$
$\begin{aligned}
& \Rightarrow x=10 \mathrm{~m} \\
& \frac{\mathrm{d}^2 \mathrm{~S}}{\mathrm{~d} x^2}=2+\frac{4000}{x^3} \\
& \Rightarrow\left(\frac{\mathrm{d}^2 \mathrm{~S}}{\mathrm{~d} x^2}\right)_{x=10}>0
\end{aligned}$
$\mathrm{S}$ is minimum when $x=10 \mathrm{~m}$ and $y=5 \mathrm{~m}$
...[From (i)]

</details>

---

### Q45. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f^{\prime}(0)=-3$ and $f^{\prime}(x) \leq 5$ for all real values of $x$. The $\mathrm{f}(2)$ can have possible maximum value as

**Options:**

- **(A)** 10
- **(B)** 5
- **(C)** 7
- **(D)** 13

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 7**

**Detailed Solution:**

Applying Lagrange's mean value theorem on interval $[0,2]$, we get there exist atleast one ' $c$ ' $\in(0,2)$ such that
$\begin{array}{ll} 
& \frac{\mathrm{f}(2)-\mathrm{f}(0)}{2-0}=\mathrm{f}^{\prime}(\mathrm{c}) \\
\therefore & \mathrm{f}(2)-\mathrm{f}(0)=2 \mathrm{f}^{\prime}(\mathrm{c}) \\
\therefore & \mathrm{f}(2)=\mathrm{f}(0)+2 \mathrm{f}^{\prime}(\mathrm{c}) \\
\therefore & \mathrm{f}(2)=-3+2 \mathrm{f}^{\prime}(\mathrm{c})
\end{array}$
Given that $\mathrm{f}^{\prime}(x) \leq 5$ for all $x$
$\begin{array}{ll}
\therefore & \mathrm{f}(2) \leq-3+10 \\
\therefore & \mathrm{f}(2) \leq 7
\end{array}$
$\therefore \quad$ Largest possible value of $\mathrm{f}(2)$ is 7 .

</details>

---

### Q46. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The maximum value of the function $f(x)=3 x^3-18 x^2+27 x-40$ on the set $\mathrm{S}=\left\{x \in \mathbb{R} / x^2+30 \leq 11 x\right\}$ is

**Options:**

- **(A)** 122
- **(B)** 132
- **(C)** 112
- **(D)** 222

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 122**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{S}=\left\{x \in \mathbb{R} / x^2+30 \leq 11 x\right\} \\
& x^2+30 \leq 11 x \\
& x^2-11 x+30 \leq 0 \\
& (x-5)(x-6) \leq 0 \\
& x \in[5,6]
\end{aligned}$
Now, $\mathrm{f}(x)=3 x^3-18 x^2+27 x-40$
$\begin{aligned}
\mathrm{f}^{\prime}(x) & =9 x^2-36 x+27 \\
\mathrm{f}^{\prime}(x) & =9\left(x^2-4 x+3\right) \\
& =9\left[\left(x^2-4 x+4\right)-1\right] \\
& =9(x-2)^2-9
\end{aligned}$
$\therefore \quad \mathrm{f}^{\prime}(x)>0 \forall x \in[5,6]$
$\therefore \mathrm{f}(x)$ is strictly increasing in the interval $[5,6]$
$\therefore \quad$ Maximum value of $\mathrm{f}(x)$ when $x \in[5,6]$ is
$f(6)=122$

</details>

---

### Q47. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The range of values of $x$ for which $f(x)=x^3+6 x^2-36 x+7$ is increasing in

**Options:**

- **(A)** $(-\infty,-6) \cup(2, \infty)$
- **(B)** $(-6,2)$
- **(C)** $(-\infty,-2) \cup(6, \infty)$
- **(D)** $(-6,2]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(-\infty,-6) \cup(2, \infty)$**

**Detailed Solution:**

$\begin{aligned}
\mathrm{f}(x) & =x^3+6 x^2-36 x+7 \\
\mathrm{f}^{\prime}(x) & =3 x^2+12 x-36 \\
& =3\left(x^2+4 x-12\right)
\end{aligned}$
For $\mathrm{f}(x)$ to be increasing,
$\begin{aligned}
& \mathrm{f}^{\prime}(x)>0 \\
& \Rightarrow 3\left(x^2+4 x-12\right)>0 \\
& \Rightarrow x^2+4 x-12>0 \\
& \Rightarrow(x+6)(x-2)>0 \\
& \Rightarrow x \in(-\infty,-6) \cup(2, \infty)
\end{aligned}$

</details>

---

### Q48. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The equation $x^3+x-1=0$ has

**Options:**

- **(A)** no real root.
- **(B)** exactly two real roots.
- **(C)** exactly one real root.
- **(D)** all three real roots.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) exactly one real root.**

**Detailed Solution:**

Given equation $x^3+x-1=0$
Let $\mathrm{f}(x)=x^3+x-1$
$\begin{array}{ll}
\therefore \quad & \mathrm{f}^{\prime}(x)=3 x^2+1 \\
& \Rightarrow \mathrm{f}^{\prime}(x)>0 \forall x \in \mathrm{R}
\end{array}$
$\Rightarrow \mathrm{f}(x) \text { is increasing }$
$\therefore \quad$ for $x_2>x_1, \mathrm{f}\left(x_2\right)>\mathrm{f}\left(x_1\right)$
Now, $\mathrm{f}(0)=-1$ and $\mathrm{f}(1)=1$
$\therefore \quad \mathrm{f}(x)=0$ for some $x \in(0,1)$
$\therefore \quad$ Equation has one real root.

</details>

---

### Q49. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of $x y$ when $x+2 y=8$ is

**Options:**

- **(A)** 20
- **(B)** 16
- **(C)** 24
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 8**

**Detailed Solution:**

$\begin{aligned}
& x+2 y=8 \\
\therefore \quad & 2 y=8-x \\
\therefore \quad & y=\frac{8-x}{2}
\end{aligned}$
Let $\mathrm{f}(x)=x y$
$\therefore \quad \mathrm{f}(x)=x \cdot \frac{(8-x)}{2}$
Differentiating w.r.t $x$, we get
$\begin{aligned}
\mathrm{f}^{\prime}(x) & =\frac{(8-x)-x}{2} \\
\mathrm{f}^{\prime}(x) & =4-x
\end{aligned}$
To find critical points,
$\begin{array}{ll} 
& \mathrm{f}^{\prime}(x)=0 \\
\therefore \quad & 4-x=0 \\
\therefore \quad & x=4
\end{array}$
critical point at $x=4$
$\therefore \quad \mathrm{f}(4)=\frac{4(8-4)}{2}=8$
$\therefore \quad$ Maximum value of the given function is 8 .

</details>

---

### Q50. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A D$ and $B C$ be two vertical poles at $A$ and $B$ respectively on a horizontal ground. If $A D=8 \mathrm{~m}, B C=11 \mathrm{~m}$ and $A B=10 \mathrm{~m}$, then the distance (in meters) of point $M$ on $A B$ from the point $A$ such that $M D^2+M C^2$ is minimum, is

**Options:**

- **(A)** 8
- **(B)** 5
- **(C)** 4
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 5**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/PpP9zurAtGCtDPPwPGmudGM2OR1d11e4vyffOVL8T-k.original.fullsize.png">

$\begin{aligned} & f(x)=M D^2+M C^2 \\ & \Rightarrow f(x)=x^2+8^2+(10-x)^2+11^2 \\ & \Rightarrow f^{\prime}(x)=2 x-2(10-x) \\ & \Rightarrow f^{\prime}(x)=4 x-20 \\ & \text { for } f(x) \text { to be minimum } x=5\end{aligned}$

</details>

---

### Q51. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

On the interval $[0,1]$, the function $x^{25}(1-x)^{75}$ takes its maximum value at the point

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** 0
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{4}$**

**Detailed Solution:**

$\begin{aligned} & f(x)=x^{25}(1-x)^{75} \\ & \Rightarrow f^{\prime}(x)=25 x^{24}(1-x)^{75}-x^{25} \cdot 75(1-x)^{74} \\ & =25 \cdot x^{24} \cdot(1-x)^{74}(1-4 x)\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/VA_yVD8Dlh4Nswo-TaqtorByKiCO1Cn1Br-UZF915lI.original.fullsize.png">

$\begin{aligned} & \Rightarrow f(x) \text { takes maximum value at } x=\frac{1}{4} \\ & \end{aligned}$

</details>

---

### Q52. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The function, $f(x)=x \sqrt{1-x}$, where $x \in(0,1)$, has local maximum at $x=$

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{1}{4}$
- **(C)** $\frac{2}{3}$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{3}$**

**Detailed Solution:**

$\begin{aligned}
& f(x)=x \sqrt{1-x} \\
& \Rightarrow f^{\prime}(x)=1 \sqrt{1-x}+\frac{x}{2 \sqrt{1-x}} x(-1)=\frac{2-3 x}{2 \sqrt{1-x}}
\end{aligned}$
sign scheme of $f^{\prime}(x)$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/cK1GaDRWiWCwB3sWp09-j1UOeoLnCEfeBrZcAfRjzIM.original.fullsize.png">

Hence, local maxima at $x=\frac{2}{3}$

</details>

---

### Q53. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Local maximum and local minimum values respectively of the function $f(x)=(x-1)(x+2)^2$ are

**Options:**

- **(A)** $-4,0$
- **(B)** $0,-4$
- **(C)** $-4,4$
- **(D)** $4,-4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0,-4$**

**Detailed Solution:**

$\begin{aligned} & f(x)=(x-1)(x+2)^2 \\ & f^{\prime}(x)=(x+2)^2+(x-1) 2(x+2)=(x+2)(x+2+2 x-2)=3 x(x+2) \\ & \stackrel{+}{+}-0_{-2}^{+} \\ & f_{\max }=f(-2)=0 \\ & f_{\min }=f(0)=-4\end{aligned}$

</details>

---

### Q54. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The maximum value of the function $f(x)=3 x^3-18 x 2+27 x-40$ on the set $S=\left\{x \in R x^2+30 \leq 11 x\right\}$ is

**Options:**

- **(A)** $122$
- **(B)** $222$
- **(C)** $810$
- **(D)** $162$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $122$**

**Detailed Solution:**

$\begin{aligned} & f(x)=3 x^3-18 x^2+27 x-40 \\ & \Rightarrow f^{\prime}(x)=9 x^2-36 x+27 \\ & =9(x-1)(x-3)\end{aligned}$
Sign scheme for $f^{\prime}(x)$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/wbQMkti8OhmQVWaBrMn9VsI5H6FOdmgyb-Co2SDJW94.original.fullsize.png">
Now, $x^2+30 \leq 11 x$
$\begin{aligned} & \Rightarrow(x-5)(x-6) \leq 0 \\ & \Rightarrow x \in[5,6]\end{aligned}$
For the interval $[5,6] f(x)$ is increasing
Hence $f_{\max }=f(6)$
$\forall x \in[5,6]$ i.e. on the set S
$=3 \times 6^3-18 \times 6^2+27 \times 6-40=122$

</details>

---

### Q55. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The minimum value of the function $f(x)=x \log x$ is

**Options:**

- **(A)** -e
- **(B)** e
- **(C)** $\frac{1}{\mathrm{e}}$
- **(D)** $-\frac{1}{\mathrm{e}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\frac{1}{\mathrm{e}}$**

**Detailed Solution:**

$f(x)=x \log x$
$\therefore \quad \mathrm{f}^{\prime}(\mathrm{x})=\frac{\mathrm{x}}{\mathrm{x}}+\log \mathrm{x}=1+\log \mathrm{x}$
When $1+\log \mathrm{x}=0 \Rightarrow \mathrm{x}=\frac{1}{\mathrm{e}}$
$\mathrm{f}^{\prime \prime}(\mathrm{x})=\frac{1}{\mathrm{x}} \Rightarrow\left[\mathrm{f}^{\prime \prime}(\mathrm{x})\right]_{\mathrm{x}=\frac{1}{\mathrm{e}}}=\mathrm{e}>0$
Thus $\mathrm{f}(\mathrm{x})$ is minimum at $\mathrm{x}=\frac{1}{\mathrm{e}}$ and
$f(x)=\left(\frac{1}{e}\right) \log \left(\frac{1}{e}\right)=\frac{-1}{e}$

</details>

---

### Q56. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For all real $x$, the minimum value of the function $f(x)=\frac{1-x+x^2}{1+x+x^2}$ is

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** 0
- **(C)** 3
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{3}$**

**Detailed Solution:**

We have $f(x)=\frac{1-x+x^2}{1+x+x^2}$
$$
f^{\prime}(x)=\frac{\left(1+x+x^2\right)(2 x-1)-\left(1-x+x^2\right)(2 x+1)}{\left(1+x+x^2\right)^2}
$$
$$
=\frac{\left(2 x+2 x^2+2 x^3-x-1-x^2\right)-\left(2 x-2 x^2+2 x^3+1-x+x^2\right)}{\left(1+x+x^2\right)^2}
$$
$$
=\frac{\left(x+x^2+2 x^3-1\right)-\left(x-x^2+2 x^3+1\right)}{\left(1+x+x^2\right)^2}
$$
$=\frac{2 x^2-2}{\left(1+x+x^2\right)^2}$ and when $f^{\prime}(x)=0$, we get
$$
2\left(\mathrm{x}^2-1\right)=0 \Rightarrow \mathrm{x}= \pm 1
$$
When $x=1, f(x)=\frac{1}{3}$ and when $x=-1, f(x)=3$
Hence minimum value of $f(x)$ is $\frac{1}{3}$.

</details>

---

### Q57. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x=-2$ and $x=4$ are the extreme points of $y=x^3-\alpha x^2-\beta x+5$, then

**Options:**

- **(A)** $\alpha=3, \beta=24$
- **(B)** $\alpha=-24m \beta=-3$
- **(C)** $\alpha=-3, \beta=-24$
- **(D)** $\alpha=24 \beta, \beta=3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\alpha=3, \beta=24$**

**Detailed Solution:**

$$
\begin{aligned}
& y=x^3-\alpha x^2-\beta x+5 \\
& \therefore \frac{d y}{d x}=3 x^2-2 \alpha x-\beta
\end{aligned}
$$
We have $\mathrm{x}=-2$ and $\mathrm{x}=4$ as extreme points.
$$
\begin{aligned}
& \therefore\left(\frac{d y}{d x}\right)_{x=-2}=3(-2)^2-2 \alpha(-2)-\beta=0 \\
& \therefore 12+4 \alpha-\beta=0 \Rightarrow 4 \alpha-\beta=-12 \\
& \left(\frac{d y}{d x}\right)_{x=4}=3(4)^2-2 \alpha(4)-\beta=0 \\
& \therefore 48-8 \alpha-\beta=0 \Rightarrow 8 \alpha+\beta=48
\end{aligned}
$$
Solving eq. (1) and (2), we get $\alpha=3, \beta=24$

</details>

---

### Q58. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

10 is divided into two parts such that the sum of double of the first and square of the other is minimum, then the numbers are respectively

**Options:**

- **(A)** 9,1
- **(B)** 8,2
- **(C)** 6,4
- **(D)** 7,3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 9,1**

**Detailed Solution:**

Let the two parts of 10 be $x$ and $(10-x)$.
$$
f(x)=2(10-x)+x^2=x^2-2 x+20
$$
$f^{\prime}(x)=2 x-2$ and when $f^{\prime}(x)=0$, we get $x=1$
$$
\mathrm{f}^{\prime \prime}(\mathrm{x})=2>0
$$
$\therefore \mathrm{f}(\mathrm{x})$ is minimum at $\mathrm{x}=1$.
Thus the parts are 1,9 .

</details>

---

### Q59. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The maximum area of the rectangle that can be inscribed in a circle of radius $r$ is

**Options:**

- **(A)** $2 r^2$ sq. units
- **(B)** $\frac{\pi \mathrm{r}^2}{4}$ sq. units
- **(C)** $\pi \mathrm{r}^2$ units
- **(D)** $r^3 \text { sq units }$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 r^2$ sq. units**

**Detailed Solution:**

Refer figure
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/2ElFZUUvUg7grMYjJoBdvMS5v8_dyvdR5NQpUVBIZ_M.original.fullsize.png">

$$
\begin{aligned}
& \mathrm{B}=(\mathrm{r} \cos \theta, \mathrm{r} \sin \theta) \\
& \therefore \mathrm{Ab} 2 \mathrm{r} \cos \theta \text { and } \mathrm{BC}=2 \mathrm{r} \sin \theta \\
& \text { Area }(\mathrm{ABCD})=\mathrm{AB} \times \mathrm{BC} \\
& \therefore \mathrm{f}(\theta)=(2 \mathrm{r} \cos \theta)(2 \mathrm{r} \sin \theta)=2 \mathrm{r}^2 \sin 2 \theta \\
& \mathrm{f}^{\prime}(\theta)=4 \mathrm{r}^2 \cos 2 \theta \text { and when } \mathrm{f}^{\prime}(\theta)=0 \text {, we write } \\
& \cos 2 \theta=0 \Rightarrow \cos 2 \theta=\cos \frac{\pi}{2} \Rightarrow \theta=\frac{\pi}{4} \\
& \mathrm{f}^{\prime \prime}(\theta)=-8 \mathrm{r}^2 \sin 2 \theta \text { and } \mathrm{f}^{\prime \prime}(\theta)_{\left[\theta=\frac{\pi}{4}\right]}=-8 \mathrm{r}^2 < 0 \backslash
\end{aligned}
$$
Thus, area of required rectangle is maximum when $\theta=\frac{\pi}{4}$
$$
\begin{aligned}
& \therefore \mathrm{AB}=2 \mathrm{r} \cos \frac{\pi}{4}=2 \mathrm{r}\left(\frac{1}{\sqrt{2}}\right)=\sqrt{2} \mathrm{r} \text { and } \\
& \mathrm{BC}=2 \mathrm{r} \sin \frac{\pi}{4}=2 \mathrm{r}\left(\frac{1}{\sqrt{2}}\right)=\sqrt{2} \mathrm{r}
\end{aligned}
$$
$\therefore$ Maximum Area $(\mathrm{ABCD})==(\sqrt{2} \mathrm{r})(\sqrt{2} \mathrm{r})=2 \mathrm{r}^2$

</details>

---

### Q60. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The slant height of a right circular cone is $3 \mathrm{~cm}$. The height of the cone for maximum volume is

**Options:**

- **(A)** $5 \mathrm{~cm}$
- **(B)** $\sqrt{5} \mathrm{~cm}$
- **(C)** $3 \mathrm{~cm}$
- **(D)** $\sqrt{3} \mathrm{~cm}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{3} \mathrm{~cm}$**

**Detailed Solution:**

Volume of cone $=\frac{1}{3} \pi \mathrm{r}^2 \mathrm{~h}$
We have slant height $\ell=3 \mathrm{~cm}$ and we know that $\ell^2=\mathrm{r}^2+\mathrm{h}^2$
$$
\begin{aligned}
& \therefore 9=\mathrm{r}^2+\mathrm{h}^2 \Rightarrow \mathrm{r}^2=9-\mathrm{h}^2 \\
& \therefore \mathrm{v}=\frac{1}{3} \pi\left(9-\mathrm{h}^2\right) \mathrm{h}=(3 \pi) \mathrm{h}-\left(\frac{\pi}{3}\right) \mathrm{h}^3 \\
& \frac{\mathrm{dv}}{\mathrm{dh}}=3 \pi-\left(\frac{\pi}{3}\right)\left(3 \mathrm{~h}^2\right)=3 \pi-\pi \mathrm{h}^2
\end{aligned}
$$
When $\frac{\mathrm{dv}}{\mathrm{dh}}=0$, we get $3 \pi=\pi \mathrm{h}^2 \Rightarrow \mathrm{h}=\sqrt{3}$
$$
\frac{\mathrm{d}^2 \mathrm{v}}{\mathrm{dh}^2}=0-2 \pi \mathrm{h} \quad \Rightarrow\left(\frac{\mathrm{d}^2 \mathrm{v}}{\mathrm{dh}^2}\right)_{\mathrm{b}-\sqrt{3}}=-2 \sqrt{3} \pi < 0
$$
$\therefore$ Volume of cone is maximum when $\mathrm{h}=\sqrt{3}$

</details>

---

### Q61. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=x^2+a x+b$ has minima at $x=3$ whose value is 5 , then the values of $a$ and $b$ are respectively.

**Options:**

- **(A)** -6,-14
- **(B)** -6,14
- **(C)** 14,-6
- **(D)** 6,14

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -6,14**

**Detailed Solution:**

$$
f(x)=x^2+a x+b
$$
$\therefore \mathrm{f}^{\prime}(\mathrm{x})=2 \mathrm{x}+\mathrm{a}$ and when $\mathrm{f}^{\prime}(\mathrm{x})=0$, we get $\mathrm{x}=\frac{-\mathrm{a}}{2}$
Now $\mathrm{f}^{\prime}(\mathrm{x})=2$ and $2>0$
$\therefore \mathrm{f}(\mathrm{x})$ has minima at $\mathrm{x}=\frac{-\mathrm{a}}{2}=3 \quad \ldots$ [as per given data]
$$
\therefore \mathrm{a}=-6
$$
Since Minimum value of $f(x)$ is 5 at $x=3$, we write
$$
5=(3)^2+(-6)(3)+b \quad \Rightarrow b=14
$$

</details>

---

### Q62. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A rectangle of maximum area is inscribed in an ellipse $\frac{x^2}{25}+\frac{y^2}{16}=1$, then its dimensions are

**Options:**

- **(A)** $4 \sqrt{2}, 6 \sqrt{2}$
- **(B)** $\sqrt{2}, 5 \sqrt{2}$
- **(C)** $4 \sqrt{2}, 5 \sqrt{2}$
- **(D)** $4 \sqrt{2}, \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4 \sqrt{2}, 5 \sqrt{2}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/4-WRcAvsrUmC_IWjB3y5Zh80Hj6M_6zxHfiTtdTbPVk.original.fullsize.png">

Length of rectangle $=10 \cos \theta$ and
breadth of rectangle $=8 \sin \theta$
$\therefore$ Area of rectangle $=(10 \cos \theta)(8 \sin \theta)=40(\sin \theta)$
Maximum area will occur when $\sin 2 \theta=1$
$$
\begin{aligned}
& \therefore \sin 2 \theta=\sin \frac{\pi}{2} \quad \Rightarrow \theta=\frac{\pi}{4} \\
& \therefore P=\left(\frac{5}{\sqrt{2}}, \frac{4}{\sqrt{2}}\right) \Rightarrow \text { Dimensions of rectangle are } 5 \sqrt{2}, 4 \sqrt{2}
\end{aligned}
$$

</details>

---

### Q63. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For all real $\mathrm{x}$, the minimum value of the function $f(x)=\frac{1-x+x^2}{1+x+x^2}$ is

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** 0
- **(C)** 3
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{3}$**

**Detailed Solution:**

We have $f(x)=\frac{1-x+x^2}{1+x+x^2}$
$$
f^{\prime}(x)=\frac{\left(1+x+x^2\right)(2 x-1)-\left(1-x+x^2\right)(2 x+1)}{\left(1+x+x^2\right)^2}
$$
$$
=\frac{\left(2 x+2 x^2+2 x^3-x-1-x^2\right)-\left(2 x-2 x^2+2 x^3+1-x+x^2\right)}{\left(1+x+x^2\right)^2}
$$
$$
=\frac{\left(x+x^2+2 x^3-1\right)-\left(x-x^2+2 x^3+1\right)}{\left(1+x+x^2\right)^2}
$$
$=\frac{2 x^2-2}{\left(1+x+x^2\right)^2}$ and when $f^{\prime}(x)=0$, we get
$$
2\left(\mathrm{x}^2-1\right)=0 \Rightarrow \mathrm{x}= \pm 1
$$
When $\mathrm{x}=1, \mathrm{f}(\mathrm{x})=\frac{1}{3}$ and when $\mathrm{x}=-1, \mathrm{f}(\mathrm{x})=3$
Hence minimum value of $f(x)$ is $\frac{1}{3}$.

</details>

---

### Q64. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=2 x^3-15 x^2-144 x-7$, then $f(x)$ is strictly decreasing in

**Options:**

- **(A)** $(-8,3)$
- **(B)** $(-3,8)$
- **(C)** $(3,8)$
- **(D)** $(-8,-3)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(-3,8)$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{f}(\mathrm{x})=2 \mathrm{x}^3-15 \mathrm{x}^2-144 \mathrm{x}-7 \\
& \mathrm{f}^{\prime}(\mathrm{x})=6 \mathrm{x}^2-30 \mathrm{x}-144 \\
& \text { When } \mathrm{f}^{\prime}(\mathrm{x}) < 0, \text { we get } \mathrm{x}^2-5 \mathrm{x}-24 < 0 \\
& \therefore(\mathrm{x}-8)(\mathrm{x}+3) < 0 \Rightarrow-3 < \mathrm{x} < 8
\end{aligned}
$$

</details>

---

### Q65. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A wire of length 20 units is divided into two parts such that the product of one part and cube of the other part is maximum, then product of these parts is

**Options:**

- **(A)** 5
- **(B)** 75
- **(C)** 15
- **(D)** 70

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 75**

**Detailed Solution:**

Let $x$ be the one part and $y$ be the other part.
We have $\mathrm{x}+\mathrm{y}=20 \Rightarrow \mathrm{y}=20-\mathrm{x}$
As per condition given, we write
$$
\begin{aligned}
& \mathrm{f}(\mathrm{x})=(20-\mathrm{x}) \mathrm{x}^3 \\
& =20 \mathrm{x}^3-\mathrm{x}^4 \\
& \therefore \mathrm{f}^{\prime}(\mathrm{x})=60 \mathrm{x}^2-4 \mathrm{x}^3
\end{aligned}
$$
When $\mathrm{f}^{\prime}(\mathrm{x})$, we get
$$
\begin{aligned}
& 4 x^2(15-x)=0 \Rightarrow x=0,15 \\
& f^{\prime}(x)=120 x-12 x^2 \\
& {\left[f^{\prime}(x)\right]_{x=15}=(120)(15)-(12)(15)^2=-900 < 0}
\end{aligned}
$$
$\therefore \mathrm{f}[\mathrm{x}]$ is maximum when $\mathrm{x}=15$.
$$
\therefore \mathrm{y}=5 \Rightarrow \mathrm{xy}=(15)(5)=75
$$

</details>

---

### Q66. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $P$ is a point on the segment $A B$ of length $12 \mathrm{~cm}$, then the position of $P$ for $A P^{2}+B P^{2}$ to be minimum is such that

**Options:**

- **(A)** $P$ divides $A B$ in the ratio $2: 3$ internally
- **(B)** $P$ divides $A B$ in the ratio $4: 3$ internally
- **(C)** $P$ is the midpoint of segment $A B$
- **(D)** $P$ divides $B A$ in the ratio $2: 1$ internally

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $P$ is the midpoint of segment $A B$**

**Detailed Solution:**

A
$\begin{aligned} \text { Let } \mathrm{d}(\mathrm{AP}) &=\mathrm{x} \Rightarrow \mathrm{d}(\mathrm{BP})=12-\mathrm{x} \\ \mathrm{f}(\mathrm{x}) &=\mathrm{AP}^{2}+\mathrm{BP}^{2} \\ &=\mathrm{x}^{2}+(12-\mathrm{x})^{2} \\ &=2 \mathrm{x}^{2}-24 \mathrm{x}+144 \\ \therefore \quad \mathrm{f}^{\prime}(\mathrm{x}) &=4 \mathrm{x}-24 \text { and when } \mathrm{f}^{\prime}(\mathrm{x})=0, \text { we get } \mathrm{x}=6 . \\ \mathrm{f}^{\prime \prime}(\mathrm{x}) &=4>0 \\ \text { Hence } \mathrm{f}(\mathrm{x}) \text { is minimum at } \mathrm{x}=6 & \end{aligned}$

</details>

---

### Q67. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The minimum value of $f(x)=a^{2} \cos ^{2} x+b^{2} \sin ^{2} x$ if $a^{2}>b^{2}$, is

**Options:**

- **(A)** $a^{2}-b^{2}$
- **(B)** $b^{2}$
- **(C)** $a^{2}+b^{2}$
- **(D)** $a^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $a^{2}$**

**Detailed Solution:**

Given $f(x)$
$=a^{2} \cos ^{2} x+b^{2} \sin ^{2} x$
$=a^{2}\left(\frac{1+\cos 2 x}{2}\right)+b^{2}\left(\frac{1-\cos 2 x}{2}\right)$
$=\left(\frac{a^{2}+b^{2}}{2}\right)+\left(\frac{a^{2}-b^{2}}{2}\right) \cos 2 x$
$f(x)$ will be maximum when $\cos 2 x=1$
$\mathrm{f}(\mathrm{x})$ will be minimum when $\cos 2 \mathrm{x}=-1$
Hence minimum value of $f(x)$ is
$$
\begin{aligned}
f(x) &=\frac{a^{2}+b^{2}}{2}+\left(\frac{a^{2}-b^{2}}{2}\right)(-1) \\
&=\frac{a^{2}+b^{2}}{2}-\frac{a^{2}-b^{2}}{2}=b^{2}
\end{aligned}
$$

</details>

---

### Q68. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The maximum volume of a right circular cylinder if the sum of its radius and height is
$6 \mathrm{~m}$ is

**Options:**

- **(A)** $16 \pi m^{3}$
- **(B)** $32 \pi m^{3}$
- **(C)** $4 \pi m^{3}$
- **(D)** $64 \pi m^{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $32 \pi m^{3}$**

**Detailed Solution:**

(A)
Let height of cylinder be $\mathrm{h}$ and radius be $\mathrm{r} \Rightarrow \mathrm{r}+\mathrm{h}=6 \Rightarrow \mathrm{h}=6-\mathrm{r}$
Volume of cylinder $\mathrm{V}=\pi \mathrm{r}^{2} \mathrm{~h}$
$=\pi \cdot r^{2} \cdot(6-r)=\pi\left(6 r^{2}-r^{3}\right)$
For the maximum volume, $\frac{\mathrm{dV}}{\mathrm{dr}}=0$
$\pi\left(12 r-3 r^{2}\right)=0 \Rightarrow 12 r=3 r^{2} \Rightarrow r=4 \Rightarrow h=6-4=2$.
$\therefore$ Volume of cylinder $=\pi \times 4^{2} \times 2=32 \pi \cdot \mathrm{m}^{3}$

</details>

---

### Q69. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The function $f(x)=(x+2) e^{-x}$ is

**Options:**

- **(A)** decreasing in $(-\infty,-1)$ and increasing in $(-1, \infty)$
- **(B)** decreasing for all $x$
- **(C)** increasing in $(-\infty,-1)$ and decreasing in $(-1, \infty)$
- **(D)** increasing for all $x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) increasing in $(-\infty,-1)$ and decreasing in $(-1, \infty)$**

**Detailed Solution:**

(C)
Given
$\begin{array}{l}
f(x)=(x+2) e^{-x} \\
\begin{aligned}
\therefore f^{\prime}(x) &=(x+2)\left(e^{-x}\right)(-1)+e^{-x}(1) \\
&=e^{-x}[1-(x+2)]=e^{-x}(-x-1) \\
&=-e^{-x}(x+1)
\end{aligned}
\end{array}$
Here $e^{-x}$ is always positive.
$\begin{array}{l}
\text { Now }-(x+1)>0 \Rightarrow-x>1 \Rightarrow x < -1 \\
\text { Also }-(x+1) < 0 \Rightarrow-x < 1 \Rightarrow x>-1
\end{array}$
Thus $\mathrm{f}(\mathrm{x})$ increases in $(-\infty,-1)$ and decreases in $(-1, \infty)$

</details>

---

### Q70. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $x+y=\frac{\pi}{2}$, then the maximum value of $\sin x$.siny is

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{-1}{2}$
- **(C)** $\frac{-1}{\sqrt{2}}$
- **(D)** $\frac{1}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

(C)
$x+y=\frac{\pi}{2} \quad \Rightarrow \quad y=\frac{\pi}{2}-x$
$\begin{array}{l}
\sin x \cdot \sin y=\sin x \cdot \sin \left(\frac{\pi}{2}-x\right)=\sin x \cos x=\frac{2 \sin x \cdot \cos x}{2}=\frac{\sin 2 x}{2} \\
\text { We know, }-1 \leq \sin 2 x \leq 1 \Rightarrow \frac{-1}{2} \leq \frac{\sin 2 x}{2} \leq \frac{1}{2}
\end{array}$
So maximum value is $\frac{1}{2}$

</details>

---

### Q71. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If rectangles are inscribed in a circle of radius r units. Then the dimensions of the rectangle which has maximum area are

**Options:**

- **(A)** $2 \mathrm{r}$ units, $\mathrm{r}$ units,
- **(B)** 2r units, $\sqrt{2} \mathrm{r}$ units,
- **(C)** r units, $\sqrt{2} \mathrm{r}$ units,
- **(D)** $\sqrt{2} \mathrm{r}$ units,$\sqrt{2} \mathrm{r}$ units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{2} \mathrm{r}$ units,$\sqrt{2} \mathrm{r}$ units**

**Detailed Solution:**

Let $A B C D$ be the rectangle inscribed in a circle of radius 'r'.
$\Rightarrow \mathrm{AC}=\mathrm{BD}=2 \mathrm{r}=$ diameter
Let $x$ and $y$ be the length and breath of rectangle.
$\therefore x^{2}+y^{2}=(2 r)^{2} \Rightarrow y=\sqrt{4 r^{2}-x^{2}}$
Now Area of rectangle $=\mathrm{A}=\mathrm{xy}$
$$
\begin{aligned}
\therefore & A=x \sqrt{4 r^{2}-x^{2}} \\
\therefore & \frac{d A}{d x}=\sqrt{4 r^{2}-x^{2}}+\frac{x}{2 \sqrt{4 r^{2}-x^{2}}} \times(-2 x)=\sqrt{4 r^{2}-x^{2}}-\frac{x^{2}}{\sqrt{4 r^{2}-x^{2}}} \\
& \frac{d A}{d x}=\frac{4 r^{2}-2 x^{2}}{\sqrt{4 r^{2}-x^{2}}}
\end{aligned}
$$
For maximum Area, $\frac{\mathrm{dA}}{\mathrm{dx}}=0 \Rightarrow 4 \mathrm{r}^{2}-2 \mathrm{x}^{2}=0 \Rightarrow \mathrm{x}=\sqrt{2} \mathrm{r}$
$$
\frac{\mathrm{d}^{2} \mathrm{~A}}{\mathrm{dx}^{2}}>0 \text { for } \mathrm{x}=\sqrt{2} \mathrm{r}
$$
Therefore area is maximum when $x=\sqrt{2} r \Rightarrow y=\sqrt{4 r^{2}-2 r^{2}}=\sqrt{2} r$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/bwcmbp-N_xIfa4PMrBrcYMioxelKpNCIUcvKiq3rSwg.original.fullsize.png">

</details>

---

### Q72. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

20 meters wire is available to fence a flower bed in the form of a circular sector. If the flower bed should have the greatest possible surface area, then the radius of the circle is

**Options:**

- **(A)** $2 \mathrm{~m}$
- **(B)** $4 \mathrm{~m}$
- **(C)** $5 \mathrm{~m}$
- **(D)** $10 \mathrm{~m}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5 \mathrm{~m}$**

**Detailed Solution:**

Let $\ell$ and $\mathrm{r}$ be as shown in figure.
We have $20=2 r+\ell$
$$
\ell=20-2 \mathrm{r}
$$
Area of flower bed
$$
\begin{array}{l}
A=\frac{1}{2} \times \ell r=\frac{1}{2}(20-2 r) \cdot r \\
A=10 r-r^{2}
\end{array}
$$
$$
\begin{array}{l}
\frac{\mathrm{d} \mathrm{A}}{\mathrm{dr}}=10-2 \mathrm{r} \text { and } \frac{\mathrm{d}^{2} \mathrm{~A}}{\mathrm{dr}^{2}}=-2 < 0 \\
\text { When } \frac{\mathrm{d} \mathrm{A}}{\mathrm{dr}}=0 \Rightarrow 10-2 \mathrm{r}=0 \Rightarrow \mathrm{r}=5
\end{array}
$$
Hence area of flower bed will be maximum when $r=5$.<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/UFgtXWAYV6Xi3fB7PaOJZc8gZyPUkGkJ0AmSmel8G7w.original.fullsize.png">

</details>

---

### Q73. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A metal wire 108 meters long is bent to form a rectangle. If the area of the rectangle
is maximum, then its dimensions are

**Options:**

- **(A)** $28 \mathrm{~m}, 28 \mathrm{~m}$
- **(B)** 27 m, $27 \mathrm{~m}$
- **(C)** $25 \mathrm{~m}, 25 \mathrm{~m}$
- **(D)** $26 \mathrm{~m}, 26 \mathrm{~m}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 27 m, $27 \mathrm{~m}$**

**Detailed Solution:**

Let sides of rectangle be $x$ and $y$
Thus $2 x+2 y=108 \Rightarrow x+y=54 \Rightarrow y=54-x$
Now Area $=A=x y$
$\therefore \quad=x(54-x)=54 x-x^{2}$
Differentiating w.r.t. $\mathrm{x}$, we get
$\frac{\mathrm{d} \mathrm{A}}{\mathrm{dx}}=54 \times 1-2 \mathrm{x}$ and $\frac{\mathrm{d}^{2} \mathrm{~A}}{\mathrm{dx}^{2}}=-2 < 0$
When $\frac{d A}{d x}=0$, we get $54-2 x=0 \Rightarrow x=27 \Rightarrow y=54-x=27$

</details>

---

### Q74. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The maximum value of the function $\frac{\log x}{x}, x \neq 0$ is

**Options:**

- **(A)** $e^{2}$
- **(B)** $\frac{1}{e}$
- **(C)** $\frac{1}{e^{2}}$
- **(D)** $e$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{e}$**

**Detailed Solution:**

Let $y=\frac{\log x}{x}$
$\therefore \frac{\mathrm{dy}}{\mathrm{dx}}=\frac{\mathrm{x} \cdot \frac{1}{\mathrm{x}}-\log \mathrm{x}}{\mathrm{x}^{2}}=\frac{1-\log \mathrm{x}}{\mathrm{x}^{2}}$
Put $\frac{d y}{d x}=0$, we get
$\begin{aligned}
1-\log x=0 & \Rightarrow \log x=1 \Rightarrow \log x=\log e \Rightarrow x=e \\
\text { Now } \frac{d^{2} y}{d x^{2}} &=\frac{x^{2}\left(-\frac{1}{x}\right)-(1-\log x)(2 x)}{x^{4}}=\frac{-x-2 x+2 x \log x}{x^{4}} \\
&=\frac{2 \log x-3}{x^{3}}
\end{aligned}$
$\text { At } x=e, \frac{d^{2} y}{d x^{2}} < 0$
from (1), maximum value is $y=\frac{1}{\mathrm{e}}$

</details>

---

### Q75. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The perimeter of a triangle is $10 \mathrm{~cm}$. If one of its side is $4 \mathrm{~cm}$, then remaining sides of the triangle, when area of triangle is maximum are

**Options:**

- **(A)** $5 \mathrm{~cm}, 1 \mathrm{~cm}$
- **(B)** $3 \cdot 6 \mathrm{~cm}, 2 \cdot 4 \mathrm{~cm}$
- **(C)** $3 \mathrm{~cm}, 3 \mathrm{~cm}$
- **(D)** $2 \mathrm{~cm}, 4 \mathrm{~cm}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3 \mathrm{~cm}, 3 \mathrm{~cm}$**

**Detailed Solution:**

Let $\mathrm{a}, \mathrm{b}, \mathrm{c}$ be the sides of the triangle.
The perimeter of triangle $(2 \mathrm{~s})=\mathrm{a}+\mathrm{b}+\mathrm{c}$
Let $\mathrm{a}=4$ and $2 \mathrm{~s}=10$ i.e. $\mathrm{s}=5$
$\therefore 10=4+b+c \Rightarrow b=6-c$
Now, area of triangle $=\Delta=\sqrt{s(s-a)(s-b)(s-c)}=\sqrt{5(5-4)(5-6+c)(5-c)}$
$\Delta=\sqrt{5(1)(\mathrm{c}-1)(5-\mathrm{c})} \Rightarrow \Delta^{2}=5(\mathrm{c}-1)(5-\mathrm{c})$
$=5\left(5 c-c^{2}-5+c\right)=5\left(-c^{2}+6 c-5\right)$
Let $f(c)=5\left(-c^{2}+6 c-5\right) \Rightarrow f^{\prime}(c)=5(-2 c+6) \Rightarrow f^{\prime \prime}(c)=5(-2)=-10$
For extreme value, $f^{\prime}(c)=0$ i.e. $5(-2 c+6)=0 \Rightarrow c=3$
Thus $f^{\prime \prime}(3)=-10 < 0 \Rightarrow f(c)$ has maximum value at $c=3$
$\therefore \mathrm{b}=6-3=3$ i.e. the lengths of the remaining sides are $3 \mathrm{~cm}$ and $3 \mathrm{~cm}$.

</details>

---

### Q76. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>9</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>27</mn><mi>x</mi><mo>+</mo><mn>15</mn><mo>,</mo></math> then the maximum value of <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is ________

**Options:**

- **(A)** <math><mo>-</mo><mn>66</mn></math>
- **(B)** <math><mn>30</mn></math>
- **(C)** <math><mo>-</mo><mn>30</mn></math>
- **(D)** <math><mn>66</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>30</mn></math>**

**Detailed Solution:**

If <math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>9</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>27</mn><mi>x</mi><mo>+</mo><mn>15</mn></math>  
<math><mi>f</mi><mi mathvariant="normal">'</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>9</mn><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>9</mn><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>  
<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> maximum at <math><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>3</mn><mo>-</mo><mn>9</mn><mo>+</mo><mn>27</mn><mo>+</mo><mn>15</mn><mo>=</mo><mn>30</mn></math>

</details>

---

### Q77. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>,</mo><mi>x</mi><mo>≠</mo><mn>0</mn></math> , then local maximum and minimum values of function f are respectively….

**Options:**

- **(A)** – 1 and 1
- **(B)** – 2 and 2
- **(C)** 2 and – 2
- **(D)** 1 and – 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) – 2 and 2**

**Detailed Solution:**

We have, <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>,</mo><mi>x</mi><mo>≠</mo><mn>0</mn></math>
On differentiating w.r.t.x, we get
<math><mi>f</mi><mi>'</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mi>f</mi><mo>"</mo><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo></math>
For maxima or minima, we put <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math><mo>⇒</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>0</mn></math>
<math><mo>⇒</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>⇒</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></math>
Now, since <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&gt;</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mi>h</mi><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> and <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&lt;</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>+</mo><mi>h</mi></mrow></mfenced></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/934998e6-81ff-434e-871d-803a9fc82b26.png" />
<math><mo>⇒</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> is point of local maxima.
and local maxima value is <math><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn></math>
and <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&lt;</mo><mn>0</mn></math> when <math><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>h</mi><mo>,</mo><mn>1</mn></mrow></mfenced></math>
and <math><mi>f</mi><mi>”</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&gt;</mo><mn>0</mn></math> when <math><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mn>1,1</mn><mo>+</mo><mi>h</mi></mrow></mfenced></math>
<math><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>1</mn><mi></mi></math> Is point of minima.
and local minima value, <math><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mn>2</mn></math>

</details>

---

### Q78. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `2`

The minimum value of the function <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math> is

**Options:**

- **(A)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math>
- **(B)** <math><mo>-</mo><mi>e</mi></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math>
- **(D)** <math><mi>e</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math>**

**Detailed Solution:**

<math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mi>x</mi><mtext> </mtext><mi>log</mi><mi>x</mi></mrow> </math>
<math> <mo>&rArr;</mo><mrow> <mi>f</mi><mo>'</mo><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mi>x</mi><mo>×</mo><mfrac> <mn>1</mn> <mi>x</mi> </mfrac> <mo>+</mo><mi>log</mi><mi>x</mi><mo>×</mo><mn>1</mn></mrow> </math>
<math> <mo>&rArr;</mo><mrow> <mi>f</mi><mo>'</mo><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mn>1</mn><mo>+</mo><mi>log</mi><mi>x</mi></mrow> </math>
Now for f(x) to be minimum,
<math> <mrow> <mi>f</mi><mo>'</mo><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mn>0</mn></mrow> </math>
<math> <mo>&rArr;</mo><mrow> <mn>1</mn><mo>+</mo><mi>log</mi><mi>x</mi><mo>=</mo><mn>0</mn></mrow> </math>
<math> <mo>&rArr;</mo><mrow> <msub> <mrow> <mi>log</mi></mrow> <mi>e</mi> </msub> <mi>x</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow> </math>
<math> <mo>&rArr;</mo><mrow> <mi>x</mi><mo>=</mo><msup> <mi>e</mi> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> <mo>=</mo><mfrac> <mn>1</mn> <mi>e</mi> </mfrac> </mrow> </math>
Also <math> <mrow> <mi>f</mi><mo>"</mo><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mfrac> <mn>1</mn> <mi>x</mi> </mfrac> </mrow> </math>
<math> <mrow> <mo>&rArr;</mo><mi>f</mi><mo>"</mo><mrow><mo>(</mo> <mrow> <mfrac> <mn>1</mn> <mi>e</mi> </mfrac> </mrow> <mo>)</mo></mrow><mo>=</mo><mfrac> <mn>1</mn> <mrow> <mfrac> <mn>1</mn> <mi>e</mi> </mfrac> </mrow> </mfrac> <mo>=</mo><mn>3</mn><mo>&gt;</mo><mn>0</mn></mrow> </math>
<math> <mrow> <mo>&rArr;</mo><mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow></mrow> </math> is minimum at <math><mrow>  <mi>x</mi>  <mo>=</mo>  <mfrac>    <mrow>      <mn>1</mn>    </mrow>    <mrow>      <mo>e</mo>    </mrow>  </mfrac></mrow></math> and the minimum value is <math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mrow> <mfrac> <mn>1</mn> <mi>e</mi> </mfrac> </mrow> <mo>)</mo></mrow><mo>=</mo><mfrac> <mn>1</mn> <mi>e</mi> </mfrac> <mi>log</mi><mfrac> <mn>1</mn> <mi>e</mi> </mfrac> <mo>=</mo><mfrac> <mrow> <mo>−</mo><mn>1</mn></mrow> <mi>e</mi> </mfrac>  </math>

</details>

---

### Q79. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

The objective function of LPP defined over the convex set attains its optimum value at

**Options:**

- **(A)** At least two of the corner points
- **(B)** All the corner points
- **(C)** At least one of the corner points
- **(D)** None of the corner points

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) At least one of the corner points**

**Detailed Solution:**

Let \(Z=a x+\) by be the objective function
When Z has optimum value(maximum or minimum), where the variables \(x\) and \(y\) are subject to constraints described by linear inequalities, this optimum value must occur at a corner points of the feasible region.
Thus, the function attains its optimum value at one of the corner points.

</details>

---

### Q80. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mi>x</mi></mrow></mfrac><mi> </mi><mo>(</mo><mi>x</mi><mo>≠</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>≠</mo><mn>1</mn><mo>)</mo></math> is

**Options:**

- **(A)** <math > <mi>e</mi></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math>
- **(C)** <math><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mi>x</mi></mrow></mfrac></math>
<math> <mrow> <msup> <mi>f</mi> <mo>′</mo> </msup> <mo stretchy="false">(</mo><mi>x</mi><mo stretchy="false">)</mo><mo>=</mo><mfrac> <mrow> <mi>x</mi><mfrac> <mn>1</mn> <mi>x</mi> </mfrac> <mo>−</mo><mi>log</mi><mi>x</mi> </mrow> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> <mo>=</mo><mfrac> <mrow> <mn>1</mn><mo>−</mo><mi>log</mi><mi>x</mi> </mrow> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </math>
<math> <mrow> <msup> <mi>f</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mn>0</mn><mo>⇒</mo><mfrac> <mrow> <mn>1</mn><mo>−</mo><mi>log</mi><mi>x</mi> </mrow> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> <mo>=</mo><mn>0</mn> </mrow> </math>
<math><mo>⇒</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mrow><mi> </mi><mi> </mi></math>
<math><mo>⇒</mo><mi>x</mi><mo>=</mo><mi>e</mi></math>
<math> <mrow> <mo>⇒</mo> </mrow> </math> Max value is <math><mi>f</mi><mfenced separators="|"><mrow><mi>e</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>e</mi></mrow></mrow></mrow><mrow><mi>e</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math>

</details>

---

### Q81. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

The maximum value of function $x^{3}-12 x^{2}+36 x+17$ in the interval $[1,10]$ is

**Options:**

- **(A)** 17
- **(B)** 177
- **(C)** 77
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 177**

**Detailed Solution:**

Let $f(x)=x^{3}-12 x^{2}+36 x+17$
$\therefore f^{\prime}(x)=3 x^{2}-24 x+36=0$
For maxima, put $f^{\prime}(x)=0$ $\Rightarrow \quad 3 x^{2}-24 x+36=0$
$\Rightarrow \quad(x-2)(x-6)=0$
$\Rightarrow \quad x=2,6$
Again, $f^{\prime \prime}(x)=6 x-24$ is negative at $x=2$ So that, $f(6)=17, f(2)=49$
At the end points, $f(1)=42, f(10)=177$ So that, $f(x)$ has its maximum value 177 .

</details>

---

### Q82. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `2`

On the interval $[0,1]$ the function $x^{25}(1-x)^{75}$ takes its maximum value at the point

**Options:**

- **(A)** 0
- **(B)** $1 / 4$
- **(C)** $1 / 2$
- **(D)** $1 / 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1 / 4$**

**Detailed Solution:**

Given, $f(x)=x^{25}(1-x)^{75}$
$$
\begin{aligned}
\Rightarrow f^{\prime}(x) &=25 x^{24}(1-x)^{75}-75 x^{25}(1-x)^{74} \\
&=25 x^{24}(1-x)^{74}(1-4 x) \\
\therefore \quad f^{\prime}(x) &=0 \\
\Rightarrow \quad x &=0,1,1 / 4
\end{aligned}
$$
If $x < 1 / 4$, then
$$
f^{\prime}(x)=25 x^{24}(1-x)^{74}(1-4 x)>0 .
$$
and if $x>1 / 4$, then
$$
f^{\prime}(x)=25 x^{24}(1-x)^{74}(1-4 x) < 0 .
$$
Thus, $f^{\prime}(x)$ changes its sign from positive to negative as $x$ passes through $1 / 4$ from left to right. Hence, $f(x)$ attains its maximum at $x=1 / 4$.

</details>

---

### Q83. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `2`

If the function $f(x)=2 x^{3}-9 a x^{2}+12 a^{2} x+1$ attains its maximum and minimum at $p$ and $q$ respectively such that $p^{2}=q$, then $a$ equals

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** 2
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

Given, $f(x)=2 x^{3}-9 a x^{2}+12 a^{2} x+1$ attains maximum and minimum at $p$ and $q$ respectively. $\therefore$
$$
f^{\prime}(p)=0, f^{\prime}(q)=0
$$
Now,
$$
\begin{array}{c}
f^{\prime \prime}(p) < 0 \text { and } f^{\prime \prime}(q)>0 \\
f^{\prime}(p)=0
\end{array}
$$
and
$$
\begin{array}{r}
f^{\prime}(q)=0 \\
6 p^{2}-18 a p+12 a^{2}=0 \\
6 q^{2}-18 a q+12 a^{2}=0
\end{array}
$$
and
$$
\begin{array}{ll}
\Rightarrow & p^{2}-3 a p+2 a^{2}=0 \\
\text { and } & q^{2}-3 a q+2 a^{2}=0
\end{array}
$$
$p=a, 2 a, q=a, 2 a$
$\begin{array}{lrl}\Rightarrow & p=a, 2 a, q=a, \\ \text { Now, } & f^{\prime \prime}(p) < 0\end{array}$
$\Rightarrow \quad 12 p-18 a < 0$
$\Rightarrow \quad p < \frac{3}{2} a$
and $f^{\prime \prime}(q)>0 \Rightarrow 12 q-18 a>0$
$\Rightarrow \quad q>\frac{3}{2} a$
From Eqs. (i), (ii) and (iii), we get $\begin{aligned} p &=a, q=2 a \\ \text { Now, } \quad p^{2} &=q \end{aligned}$
$$
\begin{array}{lc}
\Rightarrow & a^{2}=2 a \\
\Rightarrow & a=0,2
\end{array}
$$
But for $a=0, f(x)=2 x^{3}+1$ which does not
attains a maximum or minimum for any value of $x$. Hence, $a=2$.
$$

</details>

---

