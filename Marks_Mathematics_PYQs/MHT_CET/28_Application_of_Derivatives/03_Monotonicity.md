# MHT CET Mathematics - Application of Derivatives

## Topic 3: Monotonicity

**Total Questions:** 50

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x) = (a+2)x^3 - 3ax^2 + 9ax - 5$. If $f(x)$ is strictly decreasing for all $x \in R$, then the interval in which $a$ lies is

**Options:**

- **(A)** $(-\infty, -3)$
- **(B)** $(-\infty, -2)$
- **(C)** $(0, \infty)$
- **(D)** $(-\infty, -5)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(-\infty, -3)$**

**Detailed Solution:**

Given $f(x) = (a+2)x^3 - 3ax^2 + 9ax - 5$

Differentiating with respect to $x$, we get:

$f'(x) = 3(a+2)x^2 - 6ax + 9a$

For $f(x)$ to be strictly decreasing for all $x \in R$, $f'(x) \le 0$ for all $x \in R$.

For a quadratic expression $Ax^2 + Bx + C \le 0$ for all $x \in R$, the leading coefficient must be negative ($A < 0$) and the discriminant must be less than or equal to zero ($D \le 0$).

Condition 1: Leading coefficient is negative

$3(a+2) < 0 \Rightarrow a < -2$

Condition 2: Discriminant $D \le 0$

$D = (-6a)^2 - 4(3(a+2))(9a) \le 0$

$36a^2 - 108a(a+2) \le 0$

$36a^2 - 108a^2 - 216a \le 0$

$-72a^2 - 216a \le 0$

Dividing by $-72$ and reversing the inequality sign:

$a^2 + 3a \ge 0$

$a(a+3) \ge 0$

$a \in (-\infty, -3] \cup [0, \infty)$

Taking the intersection of Condition 1 and Condition 2, we get:

$a \in (-\infty, -3]$

From the given options, the interval in which $a$ lies is $(-\infty, -3)$.

Answer: $(-\infty, -3)$

</details>

---

### Q2. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)$ be the cubic polynomial having one of its roots as $x = -1$. If $f(0) = 4, f'(0) = 0, f''(1) = 0$, then...

**Options:**

- **(A)** $f(x)$ is increasing in $(-\infty, 0) \cup (2, \infty)$
- **(B)** $f(x)$ is decreasing in $(-\infty, 0) \cup (2, \infty)$
- **(C)** $f(x)$ is increasing in $(0, 2)$
- **(D)** $f(x)$ is decreasing in $(2, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $f(x)$ is increasing in $(-\infty, 0) \cup (2, \infty)$**

**Detailed Solution:**

Let the cubic polynomial be $f(x) = ax^3 + bx^2 + cx + d$.

Given $f(0) = 4$, we have $d = 4$.

Differentiating $f(x)$ with respect to $x$, we get:
$f'(x) = 3ax^2 + 2bx + c$

Given $f'(0) = 0$, we have $c = 0$.

Differentiating again, we get:
$f''(x) = 6ax + 2b$

Given $f''(1) = 0$, we have $6a + 2b = 0 \Rightarrow b = -3a$.

Since $x = -1$ is a root of $f(x)$, $f(-1) = 0$:
$-a + b - c + d = 0$

Substituting $b = -3a$, $c = 0$, and $d = 4$:
$-a - 3a - 0 + 4 = 0 \Rightarrow 4a = 4 \Rightarrow a = 1$

Thus, $b = -3(1) = -3$.

The polynomial is $f(x) = x^3 - 3x^2 + 4$.

To find the intervals of monotonicity, we find $f'(x)$:
$f'(x) = 3x^2 - 6x = 3x(x - 2)$

Setting $f'(x) = 0$ gives critical points $x = 0$ and $x = 2$.

For $x \in (-\infty, 0) \cup (2, \infty)$, $f'(x) > 0$, so $f(x)$ is strictly increasing.
For $x \in (0, 2)$, $f'(x) < 0$, so $f(x)$ is strictly decreasing.

Therefore, $f(x)$ is increasing in $(-\infty, 0) \cup (2, \infty)$.

Answer: $f(x)$ is increasing in $(-\infty, 0) \cup (2, \infty)$

</details>

---

### Q3. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $g(x) = f(x) + f(1-x)$ and $f''(x) < 0, 0 \leq x \leq 1$, then $\ldots$

**Options:**

- **(A)** $g(x)$ increases on $\left[\dfrac{1}{2}, 1\right]$ and $g(x)$ decreases on $\left[0, \dfrac{1}{2}\right]$
- **(B)** $g(x)$ decreases on $[0, 1]$
- **(C)** $g(x)$ increases on $[0, 1]$
- **(D)** $g(x)$ decreases on $\left[\dfrac{1}{2}, 1\right]$ and $g(x)$ increases on $\left[0, \dfrac{1}{2}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $g(x)$ decreases on $\left[\dfrac{1}{2}, 1\right]$ and $g(x)$ increases on $\left[0, \dfrac{1}{2}\right]$**

**Detailed Solution:**

Given $g(x) = f(x) + f(1-x)$

Differentiating with respect to $x$, we get:

$g'(x) = f'(x) - f'(1-x)$

It is given that $f''(x) < 0$ for $0 \leq x \leq 1$, which implies that $f'(x)$ is a strictly decreasing function on $[0, 1]$.

For $g(x)$ to be increasing, $g'(x) > 0$:

$f'(x) - f'(1-x) > 0$

$f'(x) > f'(1-x)$

Since $f'(x)$ is strictly decreasing, the input values must satisfy the reverse inequality:

$x < 1 - x$

$2x < 1 \Rightarrow x < \dfrac{1}{2}$

Thus, $g(x)$ is increasing on $\left[0, \dfrac{1}{2}\right]$.

For $g(x)$ to be decreasing, $g'(x) < 0$:

$f'(x) - f'(1-x) < 0$

$f'(x) < f'(1-x)$

Again, since $f'(x)$ is strictly decreasing, the input values must satisfy:

$x > 1 - x$

$2x > 1 \Rightarrow x > \dfrac{1}{2}$

Thus, $g(x)$ is decreasing on $\left[\dfrac{1}{2}, 1\right]$.

Answer: $g(x)$ decreases on $\left[\dfrac{1}{2}, 1\right]$ and $g(x)$ increases on $\left[0, \dfrac{1}{2}\right]$

</details>

---

### Q4. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The function $f(x) = \int \dfrac{x+3}{x^2-9x+20}\,dx$, then $f(x)$ is

**Options:**

- **(A)** increases on R
- **(B)** decreases on R - (4, 5)
- **(C)** decreases on $(-\infty, -3] \cup (4, 5)$
- **(D)** increases on $(-3, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) decreases on $(-\infty, -3] \cup (4, 5)$**

**Detailed Solution:**

Given $f(x) = \int \dfrac{x+3}{x^2-9x+20}\,dx$

Differentiating with respect to $x$, we get:

$f'(x) = \dfrac{x+3}{x^2-9x+20} = \dfrac{x+3}{(x-4)(x-5)}$

For $f(x)$ to be decreasing, $f'(x) \le 0$.

$\dfrac{x+3}{(x-4)(x-5)} \le 0$

The critical points are $x = -3$, $x = 4$, and $x = 5$.

Using the wavy curve method to determine the sign of $f'(x)$ in different intervals:

For $x \in (5, \infty)$, $f'(x) > 0$

For $x \in (4, 5)$, $f'(x) < 0$

For $x \in (-3, 4)$, $f'(x) > 0$

For $x \in (-\infty, -3)$, $f'(x) < 0$

Therefore, $f'(x) \le 0$ for $x \in (-\infty, -3] \cup (4, 5)$.

Hence, $f(x)$ decreases on $(-\infty, -3] \cup (4, 5)$.

Answer: decreases on $(-\infty, -3] \cup (4, 5)$

</details>

---

### Q5. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \log(1 + x) - \dfrac{x}{1+x}$, then the values of $x$ for which $f(x)$ is monotonically increasing and monotonically decreasing are respectively.....

**Options:**

- **(A)** $(-\infty, 0), (0, \infty)$
- **(B)** $(0, \infty), (-\infty, 0)$
- **(C)** $(-1, 0), (0, \infty)$
- **(D)** $(0, \infty), (-1, 0)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(0, \infty), (-1, 0)$**

**Detailed Solution:**

The given function is $f(x) = \log(1 + x) - \dfrac{x}{1+x}$

The domain of the function is $1 + x > 0 \Rightarrow x > -1$

Differentiating $f(x)$ with respect to $x$:

$f'(x) = \dfrac{1}{1+x} - \dfrac{(1+x) \cdot 1 - x \cdot 1}{(1+x)^2}$

$f'(x) = \dfrac{1}{1+x} - \dfrac{1}{(1+x)^2}$

$f'(x) = \dfrac{1+x-1}{(1+x)^2} = \dfrac{x}{(1+x)^2}$

For $f(x)$ to be monotonically increasing, $f'(x) > 0$

$\dfrac{x}{(1+x)^2} > 0 \Rightarrow x > 0$

Thus, $f(x)$ is monotonically increasing on $(0, \infty)$

For $f(x)$ to be monotonically decreasing, $f'(x) < 0$

$\dfrac{x}{(1+x)^2} < 0 \Rightarrow x < 0$

Considering the domain $x > -1$, $f(x)$ is monotonically decreasing on $(-1, 0)$

The intervals for monotonically increasing and decreasing are $(0, \infty)$ and $(-1, 0)$ respectively.

Answer: $(0, \infty), (-1, 0)$

</details>

---

### Q6. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The function $f(x) = \tan^{-1}(\sin x + \cos x)$ is an increasing function in the interval.....

**Options:**

- **(A)** $\left(0, \dfrac{\pi}{2}\right)$
- **(B)** $\left(\dfrac{-\pi}{2}, \dfrac{\pi}{2}\right)$
- **(C)** $\left(\dfrac{\pi}{4}, \dfrac{\pi}{2}\right)$
- **(D)** $\left(\dfrac{-\pi}{2}, \dfrac{\pi}{4}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(\dfrac{-\pi}{2}, \dfrac{\pi}{4}\right)$**

**Detailed Solution:**

Given $f(x) = \tan^{-1}(\sin x + \cos x)$

Differentiating with respect to $x$, we get:

$f'(x) = \dfrac{1}{1 + (\sin x + \cos x)^2} \times \dfrac{d}{dx}(\sin x + \cos x)$

$f'(x) = \dfrac{\cos x - \sin x}{1 + (\sin x + \cos x)^2}$

For $f(x)$ to be an increasing function, $f'(x) > 0$.

Since the denominator $1 + (\sin x + \cos x)^2$ is always positive for all real $x$, the sign of $f'(x)$ depends entirely on the numerator.

$\Rightarrow \cos x - \sin x > 0$

$\Rightarrow \cos x > \sin x$

From the standard trigonometric graphs, the inequality $\cos x > \sin x$ holds true in the interval $\left(\dfrac{-\pi}{2}, \dfrac{\pi}{4}\right)$.

Therefore, the function is increasing in the interval $\left(\dfrac{-\pi}{2}, \dfrac{\pi}{4}\right)$.

Answer: $\left(\dfrac{-\pi}{2}, \dfrac{\pi}{4}\right)$

</details>

---

### Q7. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $k$ such that the function $f(x) = \sin x - \cos x - kx + b$ is strictly decreasing for all real $x$ is

**Options:**

- **(A)** $k < 1$
- **(B)** $k > 1$
- **(C)** $k < \sqrt{2}$
- **(D)** $k > \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $k > \sqrt{2}$**

**Detailed Solution:**

Given $f(x) = \sin x - \cos x - kx + b$

Differentiating with respect to $x$, we get:

$f'(x) = \cos x + \sin x - k$

For $f(x)$ to be strictly decreasing for all real $x$, we must have $f'(x) \le 0$ for all $x \in \mathbb{R}$ (with equality holding only at discrete points).

$\cos x + \sin x - k \le 0$

$k \ge \cos x + \sin x$

We know that the maximum value of $a \cos x + b \sin x$ is $\sqrt{a^2 + b^2}$.

Maximum value of $\cos x + \sin x = \sqrt{1^2 + 1^2} = \sqrt{2}$

Therefore, for the inequality to hold for all $x$, we must have:

$k \ge \sqrt{2}$

Among the given options, $k > \sqrt{2}$ satisfies this condition.

Answer: $k > \sqrt{2}$

</details>

---

### Q8. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The function $\mathrm{f}(x)=[x(x-2)]^2$ is increasing in the set

**Options:**

- **(A)** $(-\infty, 0) \cup(2, \infty)$
- **(B)** $(-\infty, 1)$
- **(C)** $(1,2)$
- **(D)** $(0,1) \cup(2, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(0,1) \cup(2, \infty)$**

**Detailed Solution:**

Given $\mathrm{f}(x) = [x(x-2)]^2$

$\mathrm{f}(x) = (x^2 - 2x)^2$

Differentiating with respect to $x$, we get:

$\mathrm{f}'(x) = 2(x^2 - 2x)(2x - 2)$

$\mathrm{f}'(x) = 4x(x - 2)(x - 1)$

For the function to be increasing, $\mathrm{f}'(x) > 0$.

$4x(x - 1)(x - 2) > 0$

The critical points are $x = 0$, $x = 1$, and $x = 2$.

Using the wavy curve method, the sign of $\mathrm{f}'(x)$ in different intervals is:
For $x \in (2, \infty)$, $\mathrm{f}'(x) > 0$
For $x \in (1, 2)$, $\mathrm{f}'(x) < 0$
For $x \in (0, 1)$, $\mathrm{f}'(x) > 0$
For $x \in (-\infty, 0)$, $\mathrm{f}'(x) < 0$

Thus, $\mathrm{f}(x)$ is increasing in the interval $(0, 1) \cup (2, \infty)$.

Answer: $(0,1) \cup(2, \infty)$

</details>

---

### Q9. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\log (1+x)-\frac{2 x}{2+x}$ then $\mathrm{f}(x)$ is increasing in

**Options:**

- **(A)** $(-1, \infty)$
- **(B)** $(-\infty, \infty)$
- **(C)** $(0, \infty)$
- **(D)** $(1, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(-1, \infty)$**

**Detailed Solution:**

Given $\mathrm{f}(x) = \log(1+x) - \dfrac{2x}{2+x}$

For the function to be defined, $1+x > 0 \Rightarrow x > -1$. Thus, the domain of $\mathrm{f}(x)$ is $(-1, \infty)$.

Differentiating $\mathrm{f}(x)$ with respect to $x$:

$\mathrm{f}'(x) = \dfrac{1}{1+x} - \left[ \dfrac{(2+x)(2) - (2x)(1)}{(2+x)^2} \right]$

$\mathrm{f}'(x) = \dfrac{1}{1+x} - \dfrac{4}{(2+x)^2}$

$\mathrm{f}'(x) = \dfrac{(2+x)^2 - 4(1+x)}{(1+x)(2+x)^2}$

$\mathrm{f}'(x) = \dfrac{4 + 4x + x^2 - 4 - 4x}{(1+x)(2+x)^2}$

$\mathrm{f}'(x) = \dfrac{x^2}{(1+x)(2+x)^2}$

For $\mathrm{f}(x)$ to be increasing, $\mathrm{f}'(x) \geq 0$.

Since $x^2 \geq 0$ and $(2+x)^2 > 0$ for all $x \neq -2$, the sign of $\mathrm{f}'(x)$ depends on $1+x$.

In the domain $x > -1$, $1+x > 0$, which implies $\mathrm{f}'(x) \geq 0$ for all $x \in (-1, \infty)$.

Therefore, $\mathrm{f}(x)$ is increasing in $(-1, \infty)$.

Answer: $(-1, \infty)$

</details>

---

### Q10. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\mathrm{f}(x)=\frac{x}{2}+\frac{2}{x}, x \neq 0$ is strictly decreasing in

**Options:**

- **(A)** $(2,3)$
- **(B)** $(1,3)$
- **(C)** $(-2, 0) \cup (0, 2)$
- **(D)** $(1,4)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(-2, 0) \cup (0, 2)$**

**Detailed Solution:**

Given $f(x) = \dfrac{x}{2} + \dfrac{2}{x}$

Differentiating with respect to $x$:

$f'(x) = \dfrac{1}{2} - \dfrac{2}{x^2}$

For a strictly decreasing function, $f'(x) < 0$.

$\dfrac{1}{2} - \dfrac{2}{x^2} < 0$

$\dfrac{x^2 - 4}{2x^2} < 0$

Since $2x^2 > 0$ for all $x \neq 0$, we have:

$x^2 - 4 < 0$

$(x - 2)(x + 2) < 0$

$-2 < x < 2$

Since $x \neq 0$, the interval in which the function is strictly decreasing is $(-2, 0) \cup (0, 2)$.

Answer: $(-2, 0) \cup (0, 2)$

</details>

---

### Q11. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The function $\mathrm{f}(x)=\sin ^4 x+\cos ^4 x$ increases if

**Options:**

- **(A)** $0 < x < \frac{\pi}{8}$
- **(B)** $\frac{\pi}{4} < x < \frac{\pi}{2}$
- **(C)** $\frac{3 \pi}{8} < x < \frac{5 \pi}{8}$
- **(D)** $\frac{5 \pi}{8} < x < \frac{3 \pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{4} < x < \frac{\pi}{2}$**

**Detailed Solution:**

Given $f(x) = \sin^4 x + \cos^4 x$

Differentiating with respect to $x$, we get:

$f'(x) = 4\sin^3 x \cos x - 4\cos^3 x \sin x$

$f'(x) = -4\sin x \cos x (\cos^2 x - \sin^2 x)$

$f'(x) = -2(2\sin x \cos x) \cos 2x$

$f'(x) = -2\sin 2x \cos 2x$

$f'(x) = -\sin 4x$

For the function to be increasing, $f'(x) > 0$.

$-\sin 4x > 0$

$\sin 4x < 0$

The sine function is negative in the third and fourth quadrants. Therefore, for the principal interval:

$\pi < 4x < 2\pi$

Dividing by $4$, we get:

$\dfrac{\pi}{4} < x < \dfrac{\pi}{2}$

Answer: $\frac{\pi}{4} < x < \frac{\pi}{2}$

</details>

---

### Q12. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=x \cdot \mathrm{e}^{x(1-x)}$, then $\mathrm{f}(x)$ is

**Options:**

- **(A)** increasing in $\mathbb{R}$
- **(B)** increasing in $\left(-\frac{1}{2}, 1\right)$
- **(C)** decreasing in $\mathbb{R}$
- **(D)** decreasing in $\left[-\frac{1}{2}, 1\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) increasing in $\left(-\frac{1}{2}, 1\right)$**

**Detailed Solution:**

Given $\mathrm{f}(x) = x \cdot \mathrm{e}^{x(1-x)}$

Differentiating with respect to $x$ using the product rule:

$\mathrm{f}'(x) = 1 \cdot \mathrm{e}^{x(1-x)} + x \cdot \mathrm{e}^{x(1-x)} \cdot \dfrac{d}{dx}(x - x^2)$

$\mathrm{f}'(x) = \mathrm{e}^{x(1-x)} + x \cdot \mathrm{e}^{x(1-x)} \cdot (1 - 2x)$

$\mathrm{f}'(x) = \mathrm{e}^{x(1-x)} [1 + x(1 - 2x)]$

$\mathrm{f}'(x) = \mathrm{e}^{x(1-x)} (1 + x - 2x^2)$

$\mathrm{f}'(x) = -\mathrm{e}^{x(1-x)} (2x^2 - x - 1)$

$\mathrm{f}'(x) = -\mathrm{e}^{x(1-x)} (2x + 1)(x - 1)$

For $\mathrm{f}(x)$ to be increasing, $\mathrm{f}'(x) > 0$.

Since $\mathrm{e}^{x(1-x)} > 0$ for all $x \in \mathbb{R}$, we must have:

$-(2x + 1)(x - 1) > 0$

$(2x + 1)(x - 1) < 0$

The critical points are $x = -\dfrac{1}{2}$ and $x = 1$.

The inequality holds for $x \in \left(-\dfrac{1}{2}, 1\right)$.

Thus, $\mathrm{f}(x)$ is increasing in $\left(-\dfrac{1}{2}, 1\right)$.

Answer: increasing in $\left(-\frac{1}{2}, 1\right)$

</details>

---

### Q13. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x$ is real, then the difference between the greatest and least values of $\frac{x^2-x+1}{x^2+x+1}$ is

**Options:**

- **(A)** $\frac{10}{3}$
- **(B)** $\frac{8}{3}$
- **(C)** $\frac{5}{3}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{8}{3}$**

**Detailed Solution:**

Let $y = \dfrac{x^2-x+1}{x^2+x+1}$

Cross-multiplying, we get:

$y(x^2+x+1) = x^2-x+1$

$yx^2 + yx + y - x^2 + x - 1 = 0$

$(y-1)x^2 + (y+1)x + (y-1) = 0$

Since $x$ is real, the discriminant of this quadratic equation must be greater than or equal to zero ($\Delta \ge 0$).

$(y+1)^2 - 4(y-1)(y-1) \ge 0$

$y^2 + 2y + 1 - 4(y^2 - 2y + 1) \ge 0$

$-3y^2 + 10y - 3 \ge 0$

$3y^2 - 10y + 3 \le 0$

$(3y-1)(y-3) \le 0$

$\dfrac{1}{3} \le y \le 3$

The greatest value of the expression is $3$ and the least value is $\dfrac{1}{3}$.

The difference between the greatest and least values is:

$3 - \dfrac{1}{3} = \dfrac{8}{3}$

Answer: $\frac{8}{3}$

</details>

---

### Q14. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(\mathrm{x})=\frac{\mathrm{k} \sin \mathrm{x}+2 \cos \mathrm{x}}{\sin \mathrm{x}+\cos \mathrm{x}}$ is strictly increasing for all $x$ in its domain, then

**Options:**

- **(A)** $k=1$
- **(B)** $k>1$
- **(C)** $\mathrm{k} < 2$
- **(D)** $k>2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $k>2$**

**Detailed Solution:**

Given $f(x) = \dfrac{k \sin x + 2 \cos x}{\sin x + \cos x}$

Differentiating with respect to $x$ using the quotient rule:

$f'(x) = \dfrac{(k \cos x - 2 \sin x)(\sin x + \cos x) - (k \sin x + 2 \cos x)(\cos x - \sin x)}{(\sin x + \cos x)^2}$

Expanding the numerator:

$(k \sin x \cos x + k \cos^2 x - 2 \sin^2 x - 2 \sin x \cos x) - (k \sin x \cos x - k \sin^2 x + 2 \cos^2 x - 2 \sin x \cos x)$

Simplifying the terms, we get:

$k \cos^2 x - 2 \sin^2 x + k \sin^2 x - 2 \cos^2 x$

$= k(\cos^2 x + \sin^2 x) - 2(\sin^2 x + \cos^2 x)$

$= k - 2$

Thus, $f'(x) = \dfrac{k - 2}{(\sin x + \cos x)^2}$

For $f(x)$ to be strictly increasing for all $x$ in its domain, $f'(x) > 0$.

Since $(\sin x + \cos x)^2 > 0$ for all $x$ in the domain, the numerator must be positive.

$k - 2 > 0$

$k > 2$

Answer: $k>2$

</details>

---

### Q15. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The function f defined by $\mathrm{f}(x)=(x+2) \mathrm{e}^{-x}$ is

**Options:**

- **(A)** decreasing for all $x \in \mathbb{R}$
- **(B)** decreasing in $(-\infty,-1)$ and increasing in $(-1, \infty)$
- **(C)** decreasing in $(-1, \infty)$ and increasing in $(-\infty,-1)$
- **(D)** increasing for all $x \in \mathbb{R}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) decreasing in $(-1, \infty)$ and increasing in $(-\infty,-1)$**

**Detailed Solution:**

Given $f(x) = (x+2)e^{-x}$

Differentiating with respect to $x$ using the product rule:

$f'(x) = \dfrac{d}{dx}[(x+2)e^{-x}]$

$f'(x) = 1 \cdot e^{-x} + (x+2)(-e^{-x})$

$f'(x) = e^{-x}(1 - x - 2)$

$f'(x) = -(x+1)e^{-x}$

For $f(x)$ to be increasing, $f'(x) > 0$:

$-(x+1)e^{-x} > 0$

Since $e^{-x} > 0$ for all $x \in \mathbb{R}$, we have $-(x+1) > 0 \Rightarrow x < -1$.

Thus, $f(x)$ is increasing in $(-\infty, -1)$.

For $f(x)$ to be decreasing, $f'(x) < 0$:

$-(x+1)e^{-x} < 0 \Rightarrow -(x+1) < 0 \Rightarrow x > -1$.

Thus, $f(x)$ is decreasing in $(-1, \infty)$.

Answer: decreasing in $(-1, \infty)$ and increasing in $(-\infty,-1)$

</details>

---

### Q16. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $2 \mathrm{f}(x)+3 \mathrm{f}\left(\frac{1}{x}\right)=x^2+1, x \neq 0$ and $\mathrm{y}=5 x^2 \mathrm{f}(x)$, then y is strictly increasing in

**Options:**

- **(A)** $\left(0, \frac{1}{2}\right)$
- **(B)** $\left(\frac{-2}{5}, 0\right)$
- **(C)** $\left(\frac{1}{2}, \frac{\sqrt{5}}{2}\right)$
- **(D)** $\left(\frac{-1}{2}, 0\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(0, \frac{1}{2}\right)$**

**Detailed Solution:**

Given equation:

$2 \mathrm{f}(x) + 3 \mathrm{f}\left(\dfrac{1}{x}\right) = x^2 + 1$  ... (1)

Replacing $x$ with $\dfrac{1}{x}$ in equation (1), we get:

$2 \mathrm{f}\left(\dfrac{1}{x}\right) + 3 \mathrm{f}(x) = \dfrac{1}{x^2} + 1$  ... (2)

To eliminate $\mathrm{f}\left(\dfrac{1}{x}\right)$, multiply equation (1) by 2 and equation (2) by 3:

$4 \mathrm{f}(x) + 6 \mathrm{f}\left(\dfrac{1}{x}\right) = 2x^2 + 2$

$9 \mathrm{f}(x) + 6 \mathrm{f}\left(\dfrac{1}{x}\right) = \dfrac{3}{x^2} + 3$

Subtracting the first from the second gives:

$5 \mathrm{f}(x) = \dfrac{3}{x^2} - 2x^2 + 1$

We are given $\mathrm{y} = 5 x^2 \mathrm{f}(x)$. Substituting the value of $5 \mathrm{f}(x)$:

$\mathrm{y} = x^2 \left( \dfrac{3}{x^2} - 2x^2 + 1 \right)$

$\mathrm{y} = 3 - 2x^4 + x^2$

For $\mathrm{y}$ to be strictly increasing, $\dfrac{d\mathrm{y}}{dx} > 0$.

$\dfrac{d\mathrm{y}}{dx} = -8x^3 + 2x$

$-8x^3 + 2x > 0$

$2x(1 - 4x^2) > 0$

$x(4x^2 - 1) < 0$

$x(2x - 1)(2x + 1) < 0$

The critical points are $x = -\dfrac{1}{2}, 0, \dfrac{1}{2}$.

Using the wavy curve method, the inequality holds true for:

$x \in \left(-\infty, -\dfrac{1}{2}\right) \cup \left(0, \dfrac{1}{2}\right)$

From the given options, the interval $\left(0, \dfrac{1}{2}\right)$ is correct.

Answer: $\left(0, \frac{1}{2}\right)$

</details>

---

### Q17. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $x=-1$ and $\cdot x=2$ are extreme points of $f(x)=\alpha \log |x|+\beta x^2+x$, then

**Options:**

- **(A)** $\alpha=-6, \beta=\frac{1}{2}$
- **(B)** $\alpha=-6, \beta=-\frac{1}{2}$
- **(C)** $\alpha=2, \beta=-\frac{1}{2}$
- **(D)** $\alpha=2, \beta=\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\alpha=2, \beta=-\frac{1}{2}$**

**Detailed Solution:**

Given $f(x) = \alpha \log |x| + \beta x^2 + x$

Differentiating with respect to $x$, we get

$f'(x) = \dfrac{\alpha}{x} + 2\beta x + 1$

Since $x = -1$ and $x = 2$ are extreme points, $f'(-1) = 0$ and $f'(2) = 0$.

For $x = -1$:

$f'(-1) = -\alpha - 2\beta + 1 = 0$

$\alpha + 2\beta = 1$ ... (i)

For $x = 2$:

$f'(2) = \dfrac{\alpha}{2} + 4\beta + 1 = 0$

$\alpha + 8\beta = -2$ ... (ii)

Subtracting equation (i) from (ii), we get

$6\beta = -3 \Rightarrow \beta = -\dfrac{1}{2}$

Substituting $\beta = -\dfrac{1}{2}$ in equation (i), we get

$\alpha + 2\left(-\dfrac{1}{2}\right) = 1$

$\alpha - 1 = 1 \Rightarrow \alpha = 2$

Thus, $\alpha = 2$ and $\beta = -\dfrac{1}{2}$.

Answer: $\alpha=2, \beta=-\frac{1}{2}$

</details>

---

### Q18. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\frac{\mathrm{a} \sin x+b \cos x}{\mathrm{c} \sin x+\mathrm{d} \cos x}$ is decreasing for all $x$, then

**Options:**

- **(A)** $\mathrm{ad}-\mathrm{bc}\gt0$
- **(B)** $\mathrm{ad}-\mathrm{bc} \lt 0$
- **(C)** $\mathrm{ab}-\mathrm{cd}\gt0$
- **(D)** ab $-\mathrm{cd} \lt 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{ad}-\mathrm{bc} \lt 0$**

**Detailed Solution:**

Given $f(x) = \dfrac{a \sin x + b \cos x}{c \sin x + d \cos x}$

Differentiating with respect to $x$ using the quotient rule:

$f'(x) = \dfrac{(a \cos x - b \sin x)(c \sin x + d \cos x) - (a \sin x + b \cos x)(c \cos x - d \sin x)}{(c \sin x + d \cos x)^2}$

Expanding the numerator:

$ac \sin x \cos x + ad \cos^2 x - bc \sin^2 x - bd \sin x \cos x - (ac \sin x \cos x - ad \sin^2 x + bc \cos^2 x - bd \sin x \cos x)$

$= ad(\cos^2 x + \sin^2 x) - bc(\sin^2 x + \cos^2 x)$

$= ad - bc$

Therefore, $f'(x) = \dfrac{ad - bc}{(c \sin x + d \cos x)^2}$

For the function $f(x)$ to be decreasing for all $x$ in its domain, we must have $f'(x) \lt 0$.

Since $(c \sin x + d \cos x)^2 \gt 0$ for all $x$ in the domain, the numerator must be negative.

$ad - bc \lt 0$

Answer: $\mathrm{ad}-\mathrm{bc} \lt 0$

</details>

---

### Q19. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The set of all points, for which $\mathrm{f}(x)=x^2 \mathrm{e}^{-x}$ strictly increases, is

**Options:**

- **(A)** $(0,2)$
- **(B)** $(2, \infty)$
- **(C)** $(-2,0)$
- **(D)** $(-\infty, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(0,2)$**

**Detailed Solution:**

Given $\mathrm{f}(x) = x^2 \mathrm{e}^{-x}$

Differentiating with respect to $x$, we get

$\mathrm{f}'(x) = \dfrac{\mathrm{d}}{\mathrm{d}x}(x^2 \mathrm{e}^{-x})$

$\mathrm{f}'(x) = 2x \mathrm{e}^{-x} + x^2 (-\mathrm{e}^{-x})$

$\mathrm{f}'(x) = x(2 - x)\mathrm{e}^{-x}$

For $\mathrm{f}(x)$ to be strictly increasing, $\mathrm{f}'(x) > 0$

Since $\mathrm{e}^{-x} > 0$ for all real $x$, we must have

$x(2 - x) > 0$

$x(x - 2) < 0$

This inequality holds for $x \in (0, 2)$.

Therefore, the set of all points for which $\mathrm{f}(x)$ strictly increases is $(0, 2)$.

Answer: $(0,2)$

</details>

---

### Q20. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The function $\mathrm{f}(x)=2 x^3-9 x^2+12 x+2$ is decreasing in

**Options:**

- **(A)** $1 \lt x \lt 2$
- **(B)** $x \lt 1$ or $x \gt 2$
- **(C)** $x \lt -1$ or $x \gt -2$
- **(D)** $-2 \lt x \lt -1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1 \lt x \lt 2$**

**Detailed Solution:**

Given $\mathrm{f}(x) = 2x^3 - 9x^2 + 12x + 2$

Differentiating with respect to $x$, we get:

$\mathrm{f}'(x) = \dfrac{d}{dx}(2x^3 - 9x^2 + 12x + 2)$

$\mathrm{f}'(x) = 6x^2 - 18x + 12$

For the function to be decreasing, $\mathrm{f}'(x) < 0$.

$6x^2 - 18x + 12 < 0$

Dividing by $6$, we get:

$x^2 - 3x + 2 < 0$

$(x - 1)(x - 2) < 0$

Using the method of intervals, the inequality holds true when $x$ lies between the roots $1$ and $2$.

Therefore, $1 < x < 2$.

Answer: $1 \lt x \lt 2$

</details>

---

### Q21. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(x)=x^3-10 x^2+200 x-10$, then

**Options:**

- **(A)** $\mathrm{f}(x)$ is decreasing in $(-\infty, 10]$ and increasing in $[10, \infty)$
- **(B)** $\mathrm{f}(x)$ is increasing in $(-\infty, 10]$ and decreasing in $[10, \infty)$
- **(C)** $\mathrm{f}(x)$ is increasing throughout real line
- **(D)** $\mathrm{f}(x)$ is decreasing throughout real line

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{f}(x)$ is increasing throughout real line**

**Detailed Solution:**

Given $\mathrm{f}(x) = x^3 - 10x^2 + 200x - 10$

Differentiating with respect to $x$, we get:

$\mathrm{f}'(x) = 3x^2 - 20x + 200$

To check the sign of $\mathrm{f}'(x)$, we find the discriminant of the quadratic expression $3x^2 - 20x + 200$.

$\Delta = b^2 - 4ac = (-20)^2 - 4(3)(200) = 400 - 2400 = -2000$

Since $\Delta < 0$ and the coefficient of $x^2$ is $3 > 0$, the quadratic expression is strictly positive for all real values of $x$.

Alternatively, we can write:

$\mathrm{f}'(x) = 3\left(x^2 - \dfrac{20}{3}x\right) + 200 = 3\left(x - \dfrac{10}{3}\right)^2 - \dfrac{100}{3} + 200 = 3\left(x - \dfrac{10}{3}\right)^2 + \dfrac{500}{3}$

Since $3\left(x - \dfrac{10}{3}\right)^2 \ge 0$ and $\dfrac{500}{3} > 0$, we have $\mathrm{f}'(x) > 0$ for all $x \in \mathbb{R}$.

Therefore, $\mathrm{f}(x)$ is increasing throughout the real line.

Answer: $\mathrm{f}(x)$ is increasing throughout real line

</details>

---

### Q22. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{f}(x)=\frac{x}{\sqrt{\mathrm{a}^2+x^2}}-\frac{\mathrm{d}-x}{\sqrt{\mathrm{~b}^2+(\mathrm{d}-x)^2}}, x \in \mathbb{R}$ where $a, b, d$ are non-zero real constants. Then

**Options:**

- **(A)** $\mathrm{f}^{\prime}$ is not a continuous function of $x$.
- **(B)** f is neither increasing nor decreasing function of $x$.
- **(C)** f is an increasing function of $x$.
- **(D)** f is a decreasing function of $x$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) f is an increasing function of $x$.**

**Detailed Solution:**

Given function is $\mathrm{f}(x)=\dfrac{x}{\sqrt{\mathrm{a}^2+x^2}}-\dfrac{\mathrm{d}-x}{\sqrt{\mathrm{b}^2+(\mathrm{d}-x)^2}}$.

Differentiating $\mathrm{f}(x)$ with respect to $x$, we get:

$\mathrm{f}^{\prime}(x) = \dfrac{d}{dx}\left(\dfrac{x}{\sqrt{\mathrm{a}^2+x^2}}\right) - \dfrac{d}{dx}\left(\dfrac{\mathrm{d}-x}{\sqrt{\mathrm{b}^2+(\mathrm{d}-x)^2}}\right)$

Using the quotient rule for the first term:

$\dfrac{d}{dx}\left(\dfrac{x}{\sqrt{\mathrm{a}^2+x^2}}\right) = \dfrac{1 \cdot \sqrt{\mathrm{a}^2+x^2} - x \cdot \dfrac{x}{\sqrt{\mathrm{a}^2+x^2}}}{\mathrm{a}^2+x^2} = \dfrac{\mathrm{a}^2+x^2-x^2}{(\mathrm{a}^2+x^2)^{3/2}} = \dfrac{\mathrm{a}^2}{(\mathrm{a}^2+x^2)^{3/2}}$

Similarly, for the second term, let $u = \mathrm{d}-x$, so $\dfrac{du}{dx} = -1$:

$\dfrac{d}{dx}\left(\dfrac{\mathrm{d}-x}{\sqrt{\mathrm{b}^2+(\mathrm{d}-x)^2}}\right) = \dfrac{d}{du}\left(\dfrac{u}{\sqrt{\mathrm{b}^2+u^2}}\right) \cdot \dfrac{du}{dx} = \dfrac{\mathrm{b}^2}{(\mathrm{b}^2+u^2)^{3/2}} \cdot (-1) = -\dfrac{\mathrm{b}^2}{(\mathrm{b}^2+(\mathrm{d}-x)^2)^{3/2}}$

Substituting these back into the derivative of $\mathrm{f}(x)$:

$\mathrm{f}^{\prime}(x) = \dfrac{\mathrm{a}^2}{(\mathrm{a}^2+x^2)^{3/2}} - \left( -\dfrac{\mathrm{b}^2}{(\mathrm{b}^2+(\mathrm{d}-x)^2)^{3/2}} \right)$

$\mathrm{f}^{\prime}(x) = \dfrac{\mathrm{a}^2}{(\mathrm{a}^2+x^2)^{3/2}} + \dfrac{\mathrm{b}^2}{(\mathrm{b}^2+(\mathrm{d}-x)^2)^{3/2}}$

Since $\mathrm{a}, \mathrm{b}$ are non-zero real constants, $\mathrm{a}^2 > 0$ and $\mathrm{b}^2 > 0$. Also, $(\mathrm{a}^2+x^2)^{3/2} > 0$ and $(\mathrm{b}^2+(\mathrm{d}-x)^2)^{3/2} > 0$ for all $x \in \mathbb{R}$.

Therefore, $\mathrm{f}^{\prime}(x) > 0$ for all $x \in \mathbb{R}$.

Since the derivative is strictly positive, $\mathrm{f}(x)$ is an increasing function of $x$. Also, $\mathrm{f}^{\prime}(x)$ is continuous for all $x \in \mathbb{R}$.

Answer: f is an increasing function of $x$.

</details>

---

### Q23. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(x)=x^3-6 x^2+9 x+3$ is monotonically decreasing function, then $x$ lies in

**Options:**

- **(A)** $(3, \infty)$
- **(B)** $(1,3)$
- **(C)** $[3, \infty)$
- **(D)** $[0,3]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(1,3)$**

**Detailed Solution:**

Given $\mathrm{f}(x) = x^3 - 6x^2 + 9x + 3$

Differentiating with respect to $x$, we get

$\mathrm{f}'(x) = 3x^2 - 12x + 9$

For a monotonically decreasing function, $\mathrm{f}'(x) < 0$

$3x^2 - 12x + 9 < 0$

$3(x^2 - 4x + 3) < 0$

$3(x - 1)(x - 3) < 0$

This inequality holds true when $x$ lies between $1$ and $3$.

Therefore, $x \in (1, 3)$.

Answer: $(1,3)$

</details>

---

### Q24. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The function $\mathrm{f}(x)=2 x^3-6 x+5$ is an increasing function, if

**Options:**

- **(A)** $0 \lt x \lt 1$
- **(B)** $-1 \lt x \lt 1$
- **(C)** $x \lt -1$ or $x\gt1$
- **(D)** $-1 \lt x \lt -\dfrac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x \lt -1$ or $x\gt1$**

**Detailed Solution:**

Given $f(x) = 2x^3 - 6x + 5$

Differentiating with respect to $x$, we get

$f'(x) = 6x^2 - 6$

For $f(x)$ to be an increasing function, $f'(x) \gt 0$

$6x^2 - 6 \gt 0$

$x^2 - 1 \gt 0$

$(x - 1)(x + 1) \gt 0$

This inequality holds true for $x \lt -1$ or $x \gt 1$.

Answer: $x \lt -1$ or $x\gt1$

</details>

---

### Q25. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(x)=\dfrac{\log x}{x}(x\gt0)$, then it is increasing in

**Options:**

- **(A)** $(0, \mathrm{e})$
- **(B)** $(\mathrm{e}, \infty)$
- **(C)** $(0, \infty)$
- **(D)** $(-\infty, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(0, \mathrm{e})$**

**Detailed Solution:**

Given $\mathrm{f}(x) = \dfrac{\log x}{x}$ for $x \gt 0$.

Differentiating with respect to $x$ using the quotient rule:

$\mathrm{f}'(x) = \dfrac{x \cdot \dfrac{1}{x} - \log x \cdot 1}{x^2}$

$\mathrm{f}'(x) = \dfrac{1 - \log x}{x^2}$

For the function to be increasing, $\mathrm{f}'(x) \gt 0$.

$\dfrac{1 - \log x}{x^2} \gt 0$

Since $x \gt 0$, $x^2 \gt 0$. Therefore, the numerator must be positive:

$1 - \log x \gt 0$

$\log x \lt 1$

$x \lt \mathrm{e}$

Considering the domain $x \gt 0$, the function is increasing in the interval $(0, \mathrm{e})$.

Answer: $(0, \mathrm{e})$

</details>

---

### Q26. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The function $f(x)=\dfrac{\log _e(\pi+x)}{\log _e(e+x)}$ is

**Options:**

- **(A)** increasing on $(0, \infty)$.
- **(B)** increasing on $\left(0, \dfrac{\pi}{\mathrm{e}}\right)$, decreasing on $\left(\dfrac{\pi}{\mathrm{e}}, \infty\right)$.
- **(C)** decreasing on $(0, \infty)$.
- **(D)** decreasing on $\left(0, \dfrac{\pi}{\mathrm{e}}\right)$, increasing on $\left(\dfrac{\pi}{\mathrm{e}}, \infty\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) decreasing on $(0, \infty)$.**

**Detailed Solution:**

Given $f(x) = \dfrac{\log_e(\pi+x)}{\log_e(e+x)}$

Differentiating with respect to $x$, we get:

$f'(x) = \dfrac{\dfrac{1}{\pi+x} \log_e(e+x) - \dfrac{1}{e+x} \log_e(\pi+x)}{(\log_e(e+x))^2}$

$f'(x) = \dfrac{(e+x)\log_e(e+x) - (\pi+x)\log_e(\pi+x)}{(\pi+x)(e+x)(\log_e(e+x))^2}$

Consider the function $g(t) = t \log_e t$.

Differentiating with respect to $t$, we get:

$g'(t) = 1 + \log_e t$

For $t > 1$, $g'(t) > 0$, which means $g(t)$ is strictly increasing.

For $x > 0$, we have $\pi+x > e+x > e > 1$.

Since $g(t)$ is strictly increasing for $t > 1$, we have $g(\pi+x) > g(e+x)$.

Therefore, $(e+x)\log_e(e+x) - (\pi+x)\log_e(\pi+x) < 0$.

Since the denominator $(\pi+x)(e+x)(\log_e(e+x))^2 > 0$ for all $x > 0$, we conclude that $f'(x) < 0$ for all $x \in (0, \infty)$.

Thus, $f(x)$ is strictly decreasing on $(0, \infty)$.

Answer: decreasing on $(0, \infty)$.

</details>

---

### Q27. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The minimum value of the function $\mathrm{f}(x)=2 x^3-15 x^2+36 x-48 \quad$ on the set $\mathrm{A}=\left\{x \mid x^2+20 \leqslant 9 x\right\}$ is

**Options:**

- **(A)** -16
- **(B)** -7
- **(C)** 16
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -16**

**Detailed Solution:**

The given set is $\mathrm{A}=\left\{x \mid x^2+20 \leqslant 9 x\right\}$.

Solving the inequality:
$x^2 - 9x + 20 \leqslant 0$
$(x - 4)(x - 5) \leqslant 0$
$\Rightarrow x \in [4, 5]$

The given function is $f(x) = 2x^3 - 15x^2 + 36x - 48$.

Finding the derivative of $f(x)$ with respect to $x$:
$f'(x) = 6x^2 - 30x + 36$
$f'(x) = 6(x^2 - 5x + 6)$
$f'(x) = 6(x - 2)(x - 3)$

For $x \in [4, 5]$, both $(x - 2) > 0$ and $(x - 3) > 0$.
Thus, $f'(x) > 0$ for all $x \in [4, 5]$.

Since $f'(x) > 0$, the function $f(x)$ is strictly increasing on the interval $[4, 5]$.

Therefore, the minimum value of $f(x)$ on this interval occurs at the left endpoint, $x = 4$.

Calculating the minimum value:
$f(4) = 2(4)^3 - 15(4)^2 + 36(4) - 48$
$f(4) = 2(64) - 15(16) + 144 - 48$
$f(4) = 128 - 240 + 144 - 48$
$f(4) = 272 - 288 = -16$

Answer: -16

</details>

---

### Q28. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=x^3+\mathrm{b} x^2+\mathrm{c} x+\mathrm{d}$ and $0 \lt \mathrm{b}^2 \lt \mathrm{c}$, then in $(-\infty, \infty)$

**Options:**

- **(A)** $\mathrm{f}(x)$ is strictly increasing function
- **(B)** $\mathrm{f}(x)$ is bounded
- **(C)** $\mathrm{f}(x)$ has a local maxima
- **(D)** $\mathrm{f}(x)$ is a strictly decreasing function

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{f}(x)$ is strictly increasing function**

**Detailed Solution:**

Given $\mathrm{f}(x) = x^3 + \mathrm{b}x^2 + \mathrm{c}x + \mathrm{d}$

Differentiating with respect to $x$, we get:

$\mathrm{f}'(x) = 3x^2 + 2\mathrm{b}x + \mathrm{c}$

To find the nature of $\mathrm{f}'(x)$, we check its discriminant $D$:

$D = (2\mathrm{b})^2 - 4(3)(\mathrm{c}) = 4\mathrm{b}^2 - 12\mathrm{c} = 4(\mathrm{b}^2 - 3\mathrm{c})$

We are given $0 \lt \mathrm{b}^2 \lt \mathrm{c}$.

Since $\mathrm{b}^2 \lt \mathrm{c}$ and $\mathrm{c} \gt 0$, we have $\mathrm{b}^2 - 3\mathrm{c} \lt \mathrm{c} - 3\mathrm{c} = -2\mathrm{c} \lt 0$.

Therefore, $D \lt 0$.

Since the leading coefficient of $\mathrm{f}'(x)$ is $3 \gt 0$ and $D \lt 0$, $\mathrm{f}'(x) \gt 0$ for all $x \in (-\infty, \infty)$.

Thus, $\mathrm{f}(x)$ is a strictly increasing function.

Answer: $\mathrm{f}(x)$ is strictly increasing function

</details>

---

### Q29. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{f}(x)=\int \frac{x^2-3 x+2}{x^4+1} \mathrm{~d} x$, then function decreases in the interval

**Options:**

- **(A)** $(-\infty,-2)$
- **(B)** $(-2,-1)$
- **(C)** $(1,2)$
- **(D)** $(2, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(1,2)$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{f}(x)=\int \frac{x^2-3 x+2}{x^4+1} \mathrm{~d} x \\
& \Rightarrow \mathrm{f}^{\prime}(x)=\frac{x^2-3 x+2}{x^4+1}
\end{aligned}
$$

For $\mathrm{f}(x)$ to be decreasing,
$$
\begin{aligned}
& \mathrm{f}^{\prime}(x) < 0 \\
& \Rightarrow \frac{x^2-3 x+2}{x^4+1} < 0 \\
& \Rightarrow \frac{(x-1)(x-2)}{x^4+1} < 0 \\
& \Rightarrow(x-1)(x-2) < 0 \\
& \Rightarrow x \in(1,2)
\end{aligned}
$$

</details>

---

### Q30. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(x)=x^3+\mathrm{b} x^2+\mathrm{c} x+\mathrm{d}$ and $0 < \mathrm{b}^2 < \mathrm{c}$, then in $(-\infty, \infty)$

**Options:**

- **(A)** $\mathrm{f}(x)$ has a local maxima.
- **(B)** $\mathrm{f}(x)$ is strictly increasing function.
- **(C)** $\mathrm{f}(x)$ is bounded.
- **(D)** $\mathrm{f}(x)$ is strictly decreasing function.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{f}(x)$ is strictly increasing function.**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{f}(x)=x^3+\mathrm{b} x^2+\mathrm{c} x+\mathrm{d} \\
\therefore \quad & \mathrm{f}^{\prime}(x)=3 x^2+2 \mathrm{~b} x+\mathrm{c}
\end{aligned}
$$
Now its discriminant $=4\left(b^2-3 c\right)$ $\Rightarrow 4\left(\mathrm{~b}^2-\mathrm{c}\right)-8 \mathrm{c} < 0$, as $\mathrm{b}^2 < \mathrm{c}$ and $\mathrm{c}>0$
$\Rightarrow \mathrm{f}^{\prime}(x)>0$ for all $x \in \mathrm{R}$
$\Rightarrow f$ is strictly increasing on $R$.

</details>

---

### Q31. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The function $\mathrm{f}(x)=\sin ^4 x+\cos ^4 x$ is increasing in

**Options:**

- **(A)** $0 < x < \frac{\pi}{8}$
- **(B)** $\frac{\pi}{4} < x < \frac{\pi}{2}$
- **(C)** $\frac{3 \pi}{8} < x < \frac{5 \pi}{8}$
- **(D)** $\frac{5 \pi}{8} < x < \frac{3 \pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{4} < x < \frac{\pi}{2}$**

**Detailed Solution:**

$$
\begin{aligned}
\therefore \quad \mathrm{f}(x) & =\sin ^4 x+\cos ^4 x \\
\therefore \quad \mathrm{f}^{\prime}(x) & =4 \sin ^3 x \cos x-4 \cos ^3 x \sin x \\
& =4 \sin x \cos x\left(\sin ^2 x-\cos ^2 x\right) \\
& =+2 \sin 2 x \cos 2 x \\
& =-\sin 4 x
\end{aligned}
$$
$\therefore \quad$ If $\mathrm{f}(x)$ is increasing, then $\mathrm{f}^{\prime}(x)>0$
$$
\text { i.e., } \begin{aligned}
-\sin 4 x>0 & \Rightarrow \pi < 4 x < 2 \pi \\
& \Rightarrow \frac{\pi}{4} < x < \frac{\pi}{2}
\end{aligned}
$$

</details>

---

### Q32. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{f}(x)=x \mathrm{e}^{x(1-x)}, x \in \mathrm{R}$, then $\mathrm{f}(x)$ is

**Options:**

- **(A)** increasing in $\left[-\frac{1}{2}, 1\right]$
- **(B)** decreasing $\mathrm{R}$
- **(C)** increasing in $\mathrm{R}$
- **(D)** decreasing in $\left[-\frac{1}{2}, 1\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) increasing in $\left[-\frac{1}{2}, 1\right]$**

**Detailed Solution:**

$$
\begin{aligned}
\mathrm{f}(x) & =x \mathrm{e}^{x(1-x)} \\
\therefore \quad \mathrm{f}^{\prime}(x) & =x \mathrm{e}^{x(1-x)}[x(-1)+(1-x)]+\mathrm{e}^{x(1-x)} \\
& =\mathrm{e}^{x(1-x)}\left(x-2 x^2+1\right)
\end{aligned}
$$

For $\mathrm{f}(x)$ to be increasing, $\mathrm{f}^{\prime}(x) \geq 0$
$$
\begin{aligned}
& \Rightarrow \mathrm{e}^{x(1-x)}\left(x-2 x^2+1\right) \geq 0 \\
& \Rightarrow x-2 x^2+1 \geq 0 \\
& \Rightarrow 2 x^2-x-1 \leq 0 \\
& \Rightarrow(2 x+1)(x-1) \leq 0 \\
& \Rightarrow x \in\left[-\frac{1}{2}, 1\right]
\end{aligned}
$$
For $\mathrm{f}(x)$ to be decreasing, $\mathrm{f}^{\prime}(x) \leq 0$
$$
\begin{aligned}
& \Rightarrow(2 x+1)(x-1) \geq 0 \\
& \Rightarrow x \in\left(-\infty,-\frac{1}{2}\right] \cup[1, \infty)
\end{aligned}
$$

</details>

---

### Q33. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For every value of $x \in[1,3]$, the function $f(x)=\frac{1}{8^x}$ is

**Options:**

- **(A)** increasing for $x>2$ and decreasing for $x \leq 2$.
- **(B)** neither increasing nor decreasing.
- **(C)** decreasing.
- **(D)** increasing.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) decreasing.**

**Detailed Solution:**

$\begin{aligned} & f(x)=\frac{1}{8^x}=8^{-x} \\ & \Rightarrow f^{\prime}(x)=8^{-x} \log 8 \times(-1) \\ & \Rightarrow f^{\prime}(x)=\frac{-\log 8}{8^x}<0 \forall x \in[1,3] \\ & \Rightarrow f(x) \text { is decreasing } \forall x \in[1,3]\end{aligned}$

</details>

---

### Q34. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The set of all points, for which $f(x)=x^2 \cdot e^{-x}$ strictly increases, is

**Options:**

- **(A)** $(0,2)$
- **(B)** $(-\infty, \infty)$
- **(C)** $(-2,0)$
- **(D)** $(2, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(0,2)$**

**Detailed Solution:**

$$
f(x)=x^2 e^{-x}
$$
null
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/JGBQiXzeiYOu9XEgAJkSPxJbpY7aTjpCGT3wH5nysS4.original.fullsize.png">
$f(x)$ is strictly increasing in $(0,2)$

</details>

---

### Q35. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=\frac{x}{\log x}$, then $f(x)$ is increasing in

**Options:**

- **(A)** $(0, \infty)$
- **(B)** $(e, \infty)$
- **(C)** $(-\infty, 0)$
- **(D)** $[\mathrm{e}, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $[\mathrm{e}, \infty)$**

**Detailed Solution:**

$y=\frac{x}{\log x} \Rightarrow \frac{d y}{d x}=\frac{\log x \times 1-x \times \frac{1}{x}}{(\log x)^2}=\frac{(\log x)-1}{(\log x)^2}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/0JxzrQ5N4jm2Pphk8Tg0UOP1M_uSNRcAmDoufEmyBDM.original.fullsize.png">
$f(x)$ is increasing in $[e, \infty)$

</details>

---

### Q36. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The function $f(x)=2 x^3-9 x^2+12 x+29$ is monotonically increasing in the interval

**Options:**

- **(A)** $(-\infty, 1) \cup(2, \infty)$
- **(B)** $(-\infty, \infty)$
- **(C)** $(2, \infty)$
- **(D)** $(-\infty, 1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(-\infty, 1) \cup(2, \infty)$**

**Detailed Solution:**

$f(x)=2 x^3-9 x^2+12 x+29$
$\Rightarrow f^{\prime}(x)=6 x^2-18 x+12=6(x-1)(x-2)$ sign scheme
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/4e8-IZkV7_dik8b4050Dq7GolkmopmUJAwGavLUHgqQ.original.fullsize.png">
$\Rightarrow f(x)$ is increasing in the interval
$x \varepsilon(\infty-, 1) \cup(2, \infty)$

</details>

---

### Q37. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The function $f(x)=\frac{\log (\pi+x)}{\log (e+x)}$ is

**Options:**

- **(A)** decreasing on $\left(0, \frac{\pi}{\mathrm{e}}\right)$, increasing on $\left(\frac{\pi}{\mathrm{e}}, \infty\right)$
- **(B)** increasing on $\left(0, \frac{\pi}{\mathrm{e}}\right)$, decreasing on $\left(\frac{\pi}{\mathrm{e}}, \infty\right)$
- **(C)** increasing on $(0, \infty)$
- **(D)** decreasing on $(0, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) decreasing on $(0, \infty)$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{f}(\mathrm{x})=\frac{\log (\pi+\mathrm{x})}{\log (\mathrm{e}+\mathrm{x})} \\ & \Rightarrow \mathrm{f}^{\prime}(\mathrm{x})=\frac{\frac{1}{\pi+\mathrm{x}} \log (\mathrm{e}+\mathrm{x})-\log (\pi+\mathrm{x}) \times \frac{1}{\mathrm{e}+\mathrm{x}}}{\{\log (\mathrm{e}+\mathrm{x})\}^2} \\ & \Rightarrow \mathrm{f}^{\prime}(\mathrm{x})=\frac{(\mathrm{e}+\mathrm{x}) \log (\mathrm{e}+\mathrm{x})-(\pi+\mathrm{x}) \log (\pi+\mathrm{x})}{(\pi+\mathrm{x})(\mathrm{e}+\mathrm{x})\{\log (\mathrm{e}+\mathrm{x})\}^2}\end{aligned}$
Let $g(x)=(e+x) \log (e+x)-(\pi+x) \log (\pi+x)$
$\Rightarrow \mathrm{g}^{\prime}(\mathrm{x})=\log (\mathrm{e}+\mathrm{x})-\log (\pi+\mathrm{x})<0$
So, $\mathrm{g}(\mathrm{x})$ is decreasing
$$
\begin{aligned}
& \Rightarrow \mathrm{g}(\mathrm{x})<\mathrm{g}(0) \forall \mathrm{x} \in(0, \infty) \\
& \Rightarrow(\mathrm{e}+\mathrm{x}) \log (\mathrm{e}+\mathrm{x})-(\pi+\mathrm{x}) \log (\pi+\mathrm{x})<\mathrm{e} \log \mathrm{e}-\pi \log \pi<0 \\
& \Rightarrow \mathrm{f}^{\prime}(\mathrm{x})<0 \forall \mathrm{x} \in(0, \infty) \\
& \Rightarrow \mathrm{f}(\mathrm{x}) \text { is decreasing on }(0, \infty)
\end{aligned}
$$

</details>

---

### Q38. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The function $\mathrm{f}(\mathrm{x})$ is defined by $\mathrm{f}(\mathrm{x})=(\mathrm{x}+2) \mathrm{e}^{-\mathrm{x}}$ is

**Options:**

- **(A)** monotonically decreasing in $(-1, \infty)$ and monotonically increasing in $(-\infty,-1)$
- **(B)** decreasing for all $\mathrm{x}$
- **(C)** increasing for all $\mathrm{x}$
- **(D)** decreasing in $(-\infty,-1)$ and increasing in $(-1, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) monotonically decreasing in $(-1, \infty)$ and monotonically increasing in $(-\infty,-1)$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{f}(\mathrm{x})=(\mathrm{x}+2) \mathrm{e}^{-\mathrm{x}} \Rightarrow \mathrm{f} \mathrm{P}^{\prime}(\mathrm{x})=\mathrm{e}^{-\mathrm{x}}-(\mathrm{x}+2) \mathrm{e}^{-\mathrm{x}}=\mathrm{e}^{-\mathrm{x}}(1-\mathrm{x}-2) \\ & \Rightarrow \mathrm{f}^{\prime}(\mathrm{x})=-\mathrm{e}^{-\mathrm{x}}(1+\mathrm{x}) \text { sign scheme }\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/y_hFOOIzbDEezhqLMHQ0Eyf8kkieceWTvuQ5X4DUGOs.original.fullsize.png">

</details>

---

### Q39. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Function $\mathrm{f}(\mathrm{x})=\mathrm{e}^{-1 / \mathrm{x}}$ is strictly increasing for all $\mathrm{x}$ where

**Options:**

- **(A)** $\mathrm{x}$ is only positive real number
- **(B)** $\mathrm{x}$ is only negative real number
- **(C)** $\mathrm{x}$ is a real number
- **(D)** $\mathrm{x}$ is a non - zero real number

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{x}$ is a non - zero real number**

**Detailed Solution:**

$$
\begin{aligned}
& f(x)=e^{-\frac{1}{x}} \\
& f^{\prime}(x)=e^{-\frac{1}{x}}(-1)\left(\frac{-1}{x^2}\right)=\frac{1}{x^2 e^{\frac{1}{x}}}
\end{aligned}
$$
When $\mathrm{f}^{\prime}(\mathrm{x})>0, \mathrm{x}^2 \mathrm{e}^{\frac{1}{\mathrm{x}}}>0$ and $\mathrm{x} \neq 0$
Now $\mathrm{x}^2>0$ and $\mathrm{e}^{\frac{1}{\mathrm{x}}}>0$ for $\forall \mathrm{x} \in \mathrm{R}$
Hence $f(x)$ is an increasing function for $\forall x$, except $x=0$

</details>

---

### Q40. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\mathrm{F}(\mathrm{x})=\log |\sin \mathrm{x}|$, where $\mathrm{x} \in(0, \pi)$ is strictly increasing on

**Options:**

- **(A)** $\left(\frac{\pi}{2}, \pi\right)$ only
- **(B)** $(0, \pi)$ only
- **(C)** $\left(0, \frac{\pi}{2}\right)$ only
- **(D)** $\left(\frac{\pi}{4}, \frac{3 \pi}{4}\right)$ only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(0, \frac{\pi}{2}\right)$ only**

**Detailed Solution:**

$f(x)=\log |\sin x|$, where $x \in(0, \pi)$
$\therefore \mathrm{f}^{\prime}(\mathrm{x})=\frac{1}{\sin \mathrm{x}} \times \cos \mathrm{x}=\cot \mathrm{x}$
When $\mathrm{f}^{\prime}(\mathrm{x})>0$, we say $\frac{\cos \mathrm{x}}{\sin \mathrm{x}}>0$
Here $\sin x>0 \ldots[x \in(0, \pi)]$
for the function to be strictly increasing, $\cos x>0$
$\rightarrow \mathrm{x} \in\left(0, \frac{\pi}{2}\right)$ only.

</details>

---

### Q41. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The function $f(x)=\frac{\lambda \sin x+6 \cos x}{2 \sin x+3 \cos x}$ is increasing, if

**Options:**

- **(A)** $\lambda>2$
- **(B)** $\lambda < 4$
- **(C)** $\lambda \geq 4$
- **(D)** $\lambda>1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\lambda>2$**

**Detailed Solution:**

$$
\begin{aligned}
& f(x)=\frac{\lambda \sin x+6 \cos x}{2 \sin x+3 \cos x} \\
& f^{\prime}(x)=\frac{\{[(2 \sin x+3 \cos x)(\lambda \cos x-6 \sin x]-[\lambda \sin x+6 \cos x)(2 \cos x-3 \sin x)]\}}{(2 \sin x+3 \cos x)^2}
\end{aligned}
$$
When $\mathrm{f}^{\prime}(\mathrm{x}) \geq 0$, we get
$$
\begin{aligned}
& {\left[\left(2 \lambda \sin \mathrm{x} \cos \mathrm{x}+3 \lambda \cos ^2 \mathrm{x}-12 \sin ^2 \mathrm{x}-18 \sin \mathrm{x} \cos \mathrm{x}\right)\right.} \\
& \left.-\left(2 \lambda \sin \mathrm{x} \cos \mathrm{x}+12 \cos ^2 \mathrm{x}-3 \lambda \sin ^2 \mathrm{x}-18 \operatorname{sun} \mathrm{x} \cos \mathrm{x}\right)\right] \geq 0 \\
& \therefore 3 \lambda\left(\sin ^2 \mathrm{x}+\cos ^2 \mathrm{x}\right)-12\left(\sin ^2 \mathrm{x}+\cos ^2 \mathrm{x}\right) \geq 0 \\
& \therefore 3 \lambda-12 \geq 0 \Rightarrow \lambda \geq 4
\end{aligned}
$$

</details>

---

### Q42. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The function $\mathrm{f}(\mathrm{x})=\log (1+\mathrm{x})-\frac{2 \mathrm{x}}{2+\mathrm{x}}$ is increasing on

**Options:**

- **(A)** $(-\infty, \infty)$
- **(B)** $(-5, \infty)$
- **(C)** $(-\infty, 0)$
- **(D)** $(-1, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(-1, \infty)$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{f}(\mathrm{x})=\log (1+\mathrm{x})-\frac{2 \mathrm{x}}{2+\mathrm{x}} \Rightarrow \mathrm{x} \neq-2 \\
& \begin{aligned}
\therefore \mathrm{f}^{\prime}(\mathrm{x}) & =\frac{1}{(1+\mathrm{x})}-\left[\frac{(2+\mathrm{x})(2)-(2 \mathrm{x})(1)}{(2+\mathrm{x})^2}\right] \\
& =\frac{1}{1+\mathrm{x}}-\left[\frac{4}{(2+\mathrm{x})^2}\right]=\frac{(\mathrm{x}+2)^2-4(\mathrm{x}+1)}{(\mathrm{x}+2)^2(1+\mathrm{x})}
\end{aligned}
\end{aligned}
$$
When $f^{\prime}(x)>0$, we write
$$
\frac{x^2}{(x+2)^2(1+x)}>0
$$
Since $x^2>0$ and $(x+2)^2>0$, we write $(1+x)>0 \Rightarrow x>-1$

</details>

---

### Q43. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The function $f(x)=\cot ^{-1} x+x$ is increasing in the interval.

**Options:**

- **(A)** $(-\infty, \infty)$
- **(B)** $(0,3)$
- **(C)** $(1, \infty)$
- **(D)** $(-1, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(-\infty, \infty)$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{f}(\mathrm{x})=\cot ^{-1} \mathrm{x}+\mathrm{x} \\
& \therefore \mathrm{f}^{\prime}(\mathrm{x})=\frac{-1}{1+\mathrm{x}^2}+1=\frac{-1+1+\mathrm{x}^2}{1+\mathrm{x}^2}=\frac{\mathrm{x}^2}{1+\mathrm{x}^2} \\
& \text { Here } \mathrm{x}^2 \geq 0 \Rightarrow \frac{\mathrm{x}^2}{1+\mathrm{x}^2} \geq 0
\end{aligned}
$$
Hence $\mathrm{f}(\mathrm{x})$ is always increasing.

</details>

---

### Q44. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The function $f(x)=3 x^{4}+16 x^{3}-30 x^{2}+10$ is increasing for

**Options:**

- **(A)** every real value of $x$
- **(B)** $x=0, x=1$ only
- **(C)** $x \in(-5,0) \cup(1, \infty)$
- **(D)** $x \in[0,1]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x \in(-5,0) \cup(1, \infty)$**

**Detailed Solution:**

$f(x)=3 x^{4}+16 x^{3}-30 x^{2}+10$
$\therefore f^{\prime}(x)=12 x^{3}+48 x^{2}-60 x$
When $f^{\prime}(x)>0$, we write
$\quad x\left(12 x^{2}+48 x-60\right)>0$
$12 x\left(x^{2}+4 x-5\right)>0$
$\therefore f^{\prime}(x)>0$, when $x \in(-5,0) \cup(1, \infty)$

</details>

---

### Q45. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For every value of $x$, the function $f(x)=\frac{1}{a^{x}}, a>0$ is

**Options:**

- **(A)** decreasing
- **(B)** increasing
- **(C)** Constant
- **(D)** Neither increasing nor decreasing

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) decreasing**

**Detailed Solution:**

(D)
$\begin{aligned}
\mathrm{f}(\mathrm{x})=& \frac{1}{\mathrm{a}^{\mathrm{x}}}=\mathrm{a}^{-\mathrm{x}} \\
\therefore \quad \mathrm{f}^{\prime}(\mathrm{x}) &=-\mathrm{a}^{-\mathrm{x}} \cdot \log _{e} \mathrm{a}=-\frac{\log _{\mathrm{e}} \mathrm{a}}{\mathrm{a}^{\mathrm{x}}}= < 0
\end{aligned}$
So $\mathrm{f}(\mathrm{x})$ is decreasing for all $\mathrm{x}$.

</details>

---

### Q46. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The function $f(x)=\log x-\frac{2 x}{x+2}$

**Options:**

- **(A)** $x \in(-\infty, 1)$
- **(B)** $x \in(-1, \infty)$
- **(C)** $x \in(-\infty, 0)$
- **(D)** $x\in(0, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x\in(0, \infty)$**

**Detailed Solution:**

$$
\begin{aligned}
\text { Given } f(x) &=\log x-\frac{2 x}{x+2} \\
\therefore f^{\prime}(x) &=\frac{1}{x}-\left[\frac{(x+2)(2)-(2 x)(1)}{(x+2)^{2}}\right] \\
&=\frac{1}{x}-\left[\frac{4}{(x+2)^{2}}\right]=\frac{x^{2}+4 x}{x(x+2)^{2}} \\
&=\frac{x(x+4)}{x(x+2)^{2}}
\end{aligned}
$$
For $f^{\prime}(x)>0, x \neq 0$ and $x>-4$
Hence $x \in(0, \infty)$ is permissible.

</details>

---

### Q47. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The function <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>3</mn><mi>x</mi></math> is….

**Options:**

- **(A)** Increasing in <math><mfenced separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>∪</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>∞</mi></mrow></mfenced></math> and decreasing in <math><mfenced separators="|"><mrow><mo>-</mo><mn>1,1</mn></mrow></mfenced></math>
- **(B)** Increasing in <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>∞</mi></mrow></mfenced></math> and decreasing in <math><mfenced separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mn>0</mn></mrow></mfenced></math>
- **(C)** Decreasing in <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>∞</mi></mrow></mfenced></math> and increasing in <math><mfenced separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mn>0</mn></mrow></mfenced></math>
- **(D)** Decreasing in <math><mfenced separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>∪</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>∞</mi></mrow></mfenced></math> and increasing in <math><mfenced separators="|"><mrow><mo>-</mo><mn>1,1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Increasing in <math><mfenced separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>∪</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>∞</mi></mrow></mfenced></math> and decreasing in <math><mfenced separators="|"><mrow><mo>-</mo><mn>1,1</mn></mrow></mfenced></math>**

**Detailed Solution:**

We have, function <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>3</mn><mi>x</mi></math>  
<math><mo>&#8658;</mo><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>3</mn><mo>=</mo><mn>3</mn><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>  
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/b441718c-8ee8-4305-a727-bcab21175550.png"> 
Here, <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&gt;</mo><mn>0</mn><mi></mi><mi>i</mi><mi>n</mi><mfenced separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>∪</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>∞</mi></mrow></mfenced></math> and <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&lt;</mo><mn>0</mn></math> in (-1, 1). 
<math><mo>∴</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is increasing in <math><mfenced separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> , <math><mo>∪</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>∞</mi></mrow></mfenced></math> and decreasing in (-1, 1).

</details>

---

### Q48. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math> is increasing function then the value of <math><mi>x</mi></math> lies in

**Options:**

- **(A)** <math><mi>R</mi></math>
- **(B)** <math><mfenced separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mi> </mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi> </mi><mi>∞</mi></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mi> </mi><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mi> </mi><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mfrac> <mi>x</mi> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>1</mn></mrow> </mfrac> </mrow> </math>
<math> <mrow> <mi>f</mi><mo>'</mo><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mfrac> <mrow> <mrow><mo>(</mo> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>1</mn></mrow> <mo>)</mo></mrow><mo>−</mo><mi>x</mi><mrow><mo>(</mo> <mrow> <mn>2</mn><mi>x</mi></mrow> <mo>)</mo></mrow></mrow> <mrow> <msup> <mrow> <mrow><mo>(</mo> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>1</mn></mrow> <mo>)</mo></mrow></mrow> <mn>2</mn> </msup> </mrow> </mfrac> <mo>=</mo><mfrac> <mrow> <mo>−</mo><msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>1</mn></mrow> <mrow> <msup> <mrow> <mrow><mo>(</mo> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>1</mn></mrow> <mo>)</mo></mrow></mrow> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </math>
Since f(x) is increasing function,
<math> <mrow> <mi>f</mi><mo>'</mo><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>&gt;</mo><mn>0</mn></mrow> </math>
<math> <mrow> <mo>∴</mo><mrow><mo>(</mo> <mrow> <mo>−</mo><msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>1</mn></mrow> <mo>)</mo></mrow><mo>&gt;</mo><mn>0</mn></mrow> </math> as <math> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>1</mn></mrow> </math> is always positive
<math> <mrow> <mo>∴</mo><msup> <mi>x</mi> <mn>2</mn> </msup> <mo>−</mo><mn>1</mn><mo>&lt;</mo><mn>0</mn></mrow> </math>
<math> <mrow> <mo>∴</mo><mrow><mo>(</mo> <mrow> <mi>x</mi><mo>−</mo><mn>1</mn></mrow> <mo>)</mo></mrow><mrow><mo>(</mo> <mrow> <mi>x</mi><mo>+</mo><mn>1</mn></mrow> <mo>)</mo></mrow><mo>&lt;</mo><mn>0</mn></mrow> </math>
<math> <mrow> <mi>∴ x</mi><mo>∈</mo><mrow><mo>(</mo> <mrow> <mo>−</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow> <mo>)</mo></mrow></mrow> </math>

</details>

---

### Q49. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=k x-\sin x$ is monotonically increasing, then

**Options:**

- **(A)** $k>1$
- **(B)** $k>-1$
- **(C)** $k < 1$
- **(D)** $k < -1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $k>1$**

**Detailed Solution:**

Since, $f(x)=k x-\sin x$ is monotonically increasing for all $x \in R$. Therefore,
$$
f^{\prime}(x)>0 \text { for all } x \in R
$$
$\therefore \quad f^{\prime}(0)>0$
$$
\begin{array}{lr}
\Rightarrow & k-\cos 0>0 \\
\Rightarrow & k>1
\end{array}
$$

</details>

---

### Q50. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

The function $f(x)=\log (1+x)-\frac{2 x}{2+x}$ is increasing on

**Options:**

- **(A)** $(0, \infty)$
- **(B)** $(-\infty, 0)$
- **(C)** $(-\infty, \infty)$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(0, \infty)$**

**Detailed Solution:**

Given, $f(x)=\log (1+x)-\frac{2 x}{2+x}$
$$
\begin{aligned}
\therefore \quad f^{\prime}(x) &=\frac{1}{1+x}-\frac{(2+x) \cdot 2-2 x}{(2+x)^{2}} \\
&=\frac{x^{2}}{(1+x)(x+2)^{2}}
\end{aligned}
$$
Clearly, $f^{\prime}(x)>0$ for all $x>0$. Hence, $f(x)$ is increasing on $(0, \infty)$.

</details>

---

