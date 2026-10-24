# MHT CET Mathematics - Application of Derivatives

## Topic 5: Mean Value Theorem

**Total Questions:** 38

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)$ satisfy the condition of Rolle's Theorm in $[1, 2]$ and $f(x)$ is continuous in $[1, 2]$ then $\int_1^2 f'(x)\,dx$ is equal to _____

**Options:**

- **(A)** $3$
- **(B)** $0$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0$**

**Detailed Solution:**

Since $f(x)$ satisfies the conditions of Rolle's Theorem on $[1, 2]$, we have $f(1) = f(2)$.

The given integral is $\int_1^2 f'(x)\,dx$.

Using the Fundamental Theorem of Calculus, we get:

$\int_1^2 f'(x)\,dx = [f(x)]_1^2 = f(2) - f(1)$

Substituting $f(1) = f(2)$, we get:

$f(2) - f(1) = 0$

Answer: $0$

</details>

---

### Q2. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If Rolle's theorem holds for the function $f(x) = x^2 - px + 10$, $x \in [0, 4]$ with $c = 2$, then $p = $

**Options:**

- **(A)** $4$
- **(B)** $2$
- **(C)** $-4$
- **(D)** $-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $4$**

**Detailed Solution:**

For Rolle's theorem to hold for $f(x)$ on $[0, 4]$, the derivative $f'(x)$ must be zero at $x = c$.

Given $f(x) = x^2 - px + 10$, differentiating with respect to $x$ gives:

$f'(x) = 2x - p$

Since $c = 2$ is the point where $f'(c) = 0$:

$f'(2) = 2(2) - p = 0$

$4 - p = 0$

$p = 4$

Additionally, checking the condition $f(0) = f(4)$:

$10 = 16 - 4p + 10$

$4p = 16 \Rightarrow p = 4$

Answer: $4$

</details>

---

### Q3. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $c$ for which the function $f(x) = \log\left(\dfrac{x^2 + 6}{5x}\right)$ satisfies Rolle's theorem in the interval $[2, 3]$ is ____

**Options:**

- **(A)** $\sqrt{5}$
- **(B)** $\sqrt{7}$
- **(C)** $\sqrt{8}$
- **(D)** $\sqrt{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{6}$**

**Detailed Solution:**

Given $f(x) = \log\left(\dfrac{x^2 + 6}{5x}\right)$ on the interval $[2, 3]$.

$f(2) = \log\left(\dfrac{4 + 6}{10}\right) = \log(1) = 0$

$f(3) = \log\left(\dfrac{9 + 6}{15}\right) = \log(1) = 0$

Since $f(2) = f(3)$, Rolle's theorem is applicable.

Differentiating $f(x)$ with respect to $x$:

$f'(x) = \dfrac{d}{dx} (\log(x^2 + 6) - \log(5x))$

$f'(x) = \dfrac{2x}{x^2 + 6} - \dfrac{1}{x}$

$f'(x) = \dfrac{2x^2 - (x^2 + 6)}{x(x^2 + 6)} = \dfrac{x^2 - 6}{x(x^2 + 6)}$

By Rolle's theorem, there exists $c \in (2, 3)$ such that $f'(c) = 0$.

$\dfrac{c^2 - 6}{c(c^2 + 6)} = 0$

$c^2 - 6 = 0 \Rightarrow c = \pm\sqrt{6}$

Since $c \in (2, 3)$, we have $c = \sqrt{6}$.

Answer: $\sqrt{6}$

</details>

---

### Q4. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In the Lagrange's Mean Value Theorem, $f(b) - f(a) = (b - a)f'(c);\ (a < c < b)$. If $a = 2, b = 4$ and $f(x) = \sqrt{x^2 - 4}$, then the value of $c$ is

**Options:**

- **(A)** $\sqrt{2}$
- **(B)** $\sqrt{7}$
- **(C)** $\sqrt{5}$
- **(D)** $\sqrt{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{6}$**

**Detailed Solution:**

Given $f(x) = \sqrt{x^2 - 4}$ and the interval $[2, 4]$.

$f(2) = \sqrt{2^2 - 4} = 0$

$f(4) = \sqrt{4^2 - 4} = \sqrt{12} = 2\sqrt{3}$

Differentiating $f(x)$ with respect to $x$:

$f'(x) = \dfrac{x}{\sqrt{x^2 - 4}}$

By Lagrange's Mean Value Theorem:

$f'(c) = \dfrac{f(b) - f(a)}{b - a}$

$\dfrac{c}{\sqrt{c^2 - 4}} = \dfrac{2\sqrt{3} - 0}{4 - 2}$

$\dfrac{c}{\sqrt{c^2 - 4}} = \sqrt{3}$

Squaring both sides:

$\dfrac{c^2}{c^2 - 4} = 3$

$c^2 = 3c^2 - 12$

$2c^2 = 12$

$c^2 = 6$

$c = \sqrt{6}$ (since $c \in (2, 4)$)

Answer: $\sqrt{6}$

</details>

---

### Q5. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If Rolle's theorem holds for the function $f(x) = x^3 + px^2 + qx + 5, x \in [1, 3]$ with $c = 2 + \dfrac{1}{\sqrt{3}}$, then the values of $p$ and $q$ are respectively...

**Options:**

- **(A)** $6, -11$
- **(B)** $6, 11$
- **(C)** $-6, 11$
- **(D)** $-6, -11$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-6, 11$**

**Detailed Solution:**

For Rolle's theorem to hold for $f(x)$ on $[1, 3]$, we must have $f(1) = f(3)$.

$f(1) = 1^3 + p(1)^2 + q(1) + 5 = p + q + 6$

$f(3) = 3^3 + p(3)^2 + q(3) + 5 = 9p + 3q + 32$

Equating $f(1)$ and $f(3)$:

$p + q + 6 = 9p + 3q + 32$

$8p + 2q + 26 = 0 \Rightarrow 4p + q + 13 = 0$

Also, by Rolle's theorem, $f'(c) = 0$ for the given $c \in (1, 3)$.

$f'(x) = 3x^2 + 2px + q$

Given $c = 2 + \dfrac{1}{\sqrt{3}}$, we have:

$f'\left(2 + \dfrac{1}{\sqrt{3}}\right) = 3\left(2 + \dfrac{1}{\sqrt{3}}\right)^2 + 2p\left(2 + \dfrac{1}{\sqrt{3}}\right) + q = 0$

$3\left(4 + \dfrac{1}{3} + \dfrac{4}{\sqrt{3}}\right) + 4p + \dfrac{2p}{\sqrt{3}} + q = 0$

$12 + 1 + \dfrac{12}{\sqrt{3}} + 4p + \dfrac{2p}{\sqrt{3}} + q = 0$

$(4p + q + 13) + \dfrac{12 + 2p}{\sqrt{3}} = 0$

From the first condition, $4p + q + 13 = 0$. Substituting this gives:

$0 + \dfrac{12 + 2p}{\sqrt{3}} = 0$

$12 + 2p = 0 \Rightarrow p = -6$

Substituting $p = -6$ into $4p + q + 13 = 0$:

$4(-6) + q + 13 = 0$

$-24 + q + 13 = 0 \Rightarrow q = 11$

The values of $p$ and $q$ are $-6$ and $11$ respectively.

Answer: $-6, 11$

</details>

---

### Q6. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For which of the following functions is Rolle's theorem not applicable?

**Options:**

- **(A)** $f(x)=\log(x^2+2)-\log 3, on\,[-1,1]$
- **(B)** $f(x)=3+(x-1)^{2/3}, on\,[0,3]$
- **(C)** $f(x)=e^{1-x^2}, on\,[-1,1]$
- **(D)** $f(x)=\sqrt{4-x^2}, on\,[-2,2]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $f(x)=3+(x-1)^{2/3}, on\,[0,3]$**

**Detailed Solution:**

For Rolle's theorem to be applicable for a function $f(x)$ on $[a, b]$, the function must be continuous on $[a, b]$, differentiable on $(a, b)$, and $f(a) = f(b)$.

Checking the function $f(x) = 3 + (x-1)^{2/3}$ on $[0, 3]$:

Differentiating with respect to $x$, we get $f'(x) = \dfrac{2}{3(x-1)^{1/3}}$.

At $x = 1 \in (0, 3)$, $f'(x)$ is undefined. Thus, $f(x)$ is not differentiable on $(0, 3)$.

Also, $f(0) = 3 + (-1)^{2/3} = 4$ and $f(3) = 3 + (2)^{2/3} \neq 4$, so $f(0) \neq f(3)$.

Since the conditions of Rolle's theorem are not satisfied, it is not applicable for this function.

Answer: $f(x)=3+(x-1)^{2/3}, on\,[0,3]$

</details>

---

### Q7. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The function $f(x) = x(x + 3)e^{-\left(\frac{1}{2}\right)x}$ satisfies all the conditions of Rolle's theorem in $[-3, 0]$, then $c =$

**Options:**

- **(A)** $-3$
- **(B)** $-2$
- **(C)** $-1$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-2$**

**Detailed Solution:**

Given $f(x) = (x^2 + 3x)e^{-\dfrac{x}{2}}$

Differentiating with respect to $x$:

$f'(x) = (2x + 3)e^{-\dfrac{x}{2}} + (x^2 + 3x)e^{-\dfrac{x}{2}} \left(-\dfrac{1}{2}\right)$

$f'(x) = e^{-\dfrac{x}{2}} \left( 2x + 3 - \dfrac{x^2 + 3x}{2} \right)$

$f'(x) = e^{-\dfrac{x}{2}} \left( \dfrac{-x^2 + x + 6}{2} \right)$

By Rolle's theorem, there exists $c \in (-3, 0)$ such that $f'(c) = 0$.

$\dfrac{-c^2 + c + 6}{2} = 0$

$c^2 - c - 6 = 0$

$(c - 3)(c + 2) = 0$

$c = 3$ or $c = -2$

Since $c \in (-3, 0)$, we get $c = -2$.

Answer: $-2$

</details>

---

### Q8. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Rolle's theorem holds for monic quadratic polynomial $f(x)$ on the interval $[\alpha, \alpha + 3]$ where $f(\alpha) = 0$. Similarly, $g(x) = f(x) + 2$ also follows Rolle's theorem in the interval $[\beta, 3]$ where $g(3) = 0$, such that the value of $c$ is the same for both $f(x)$ and $g(x)$. Then the value of $(f \circ g)(\alpha)$ is...

**Options:**

- **(A)** $-4$
- **(B)** $4$
- **(C)** $-2$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-2$**

**Detailed Solution:**

Since $f(x)$ is a monic quadratic polynomial and Rolle's theorem holds on $[\alpha, \alpha + 3]$ with $f(\alpha) = 0$, we have $f(\alpha + 3) = f(\alpha) = 0$.

Thus, $f(x) = (x - \alpha)(x - \alpha - 3)$.

The value of $c$ for $f(x)$ is the midpoint of the interval, $c = \alpha + \dfrac{3}{2}$.

For $g(x) = f(x) + 2$, Rolle's theorem holds on $[\beta, 3]$. The value of $c$ is the same, so the midpoint of $[\beta, 3]$ is also $\alpha + \dfrac{3}{2}$.

$\dfrac{\beta + 3}{2} = \alpha + \dfrac{3}{2} \Rightarrow \beta = 2\alpha$.

We are given $g(3) = 0$, which means $f(3) + 2 = 0 \Rightarrow f(3) = -2$.

Substituting $x = 3$ in $f(x)$, we get:

$(3 - \alpha)(3 - \alpha - 3) = -2 \Rightarrow -\alpha(3 - \alpha) = -2 \Rightarrow \alpha^2 - 3\alpha + 2 = 0$.

This gives $\alpha = 1$ or $\alpha = 2$.

If $\alpha = 2$, then $\beta = 4$, making the interval $[4, 3]$, which is invalid. Thus, $\alpha = 1$ and $\beta = 2$.

So, $f(x) = (x - 1)(x - 4)$ and $g(x) = f(x) + 2$.

We need to find $(f \circ g)(\alpha) = f(g(1))$.

Since $f(1) = 0$, $g(1) = f(1) + 2 = 2$.

Then, $f(g(1)) = f(2) = (2 - 1)(2 - 4) = -2$.

Answer: $-2$

</details>

---

### Q9. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $c$ satisfied by the Rolle's theorem for the function $f(x) = x^2(1 - x)^2$, $x \in [0, 1]$ is...

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $\dfrac{1}{2}$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{2}$**

**Detailed Solution:**

Given function is $f(x) = x^2(1 - x)^2$ on the interval $[0, 1]$.

The function is a polynomial, so it is continuous on $[0, 1]$ and differentiable on $(0, 1)$.

Also, $f(0) = 0$ and $f(1) = 0$, so $f(0) = f(1)$.

By Rolle's theorem, there exists at least one $c \in (0, 1)$ such that $f'(c) = 0$.

Differentiating $f(x)$ with respect to $x$:

$f'(x) = \dfrac{d}{dx}[x^2(1 - x)^2] = 2x(1 - x)^2 + x^2 \cdot 2(1 - x)(-1)$

$f'(x) = 2x(1 - x)[(1 - x) - x] = 2x(1 - x)(1 - 2x)$

Setting $f'(c) = 0$:

$2c(1 - c)(1 - 2c) = 0$

The possible values are $c = 0$, $c = 1$, and $c = \dfrac{1}{2}$.

Since $c$ must lie in the open interval $(0, 1)$, the only valid value is $c = \dfrac{1}{2}$.

Answer: $\dfrac{1}{2}$

</details>

---

### Q10. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the function $f(x) = ax^2 + bx + \sin x$ satisfies all the conditions of Rolle's theorem on $[0, \pi]$ and the slope of the tangent to the curve $y = f(x)$ at $x = \dfrac{\pi}{4}$ is zero, then $a - b = $

**Options:**

- **(A)** $\dfrac{\sqrt{2}(1-\pi)}{\pi}$
- **(B)** $\dfrac{\sqrt{2}(2+\pi)}{\pi}$
- **(C)** $\dfrac{\sqrt{2}(\pi-1)}{\pi}$
- **(D)** $\dfrac{\sqrt{2}(\pi+1)}{\pi}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{\sqrt{2}(\pi+1)}{\pi}$**

**Detailed Solution:**

Since $f(x)$ satisfies Rolle's theorem on $[0, \pi]$, we have $f(0) = f(\pi)$.

$a(0)^2 + b(0) + \sin 0 = a\pi^2 + b\pi + \sin \pi$

$0 = a\pi^2 + b\pi$

$b = -a\pi$

The slope of the tangent at $x = \dfrac{\pi}{4}$ is zero, so $f'\left(\dfrac{\pi}{4}\right) = 0$.

$f'(x) = 2ax + b + \cos x$

$f'\left(\dfrac{\pi}{4}\right) = 2a\left(\dfrac{\pi}{4}\right) + b + \cos\left(\dfrac{\pi}{4}\right) = 0$

$\dfrac{a\pi}{2} + b + \dfrac{1}{\sqrt{2}} = 0$

Substituting $b = -a\pi$:

$\dfrac{a\pi}{2} - a\pi + \dfrac{1}{\sqrt{2}} = 0$

$-\dfrac{a\pi}{2} + \dfrac{1}{\sqrt{2}} = 0$

$a = \dfrac{\sqrt{2}}{\pi}$

Using $b = -a\pi$, we get $b = -\sqrt{2}$.

Therefore, $a - b = \dfrac{\sqrt{2}}{\pi} - (-\sqrt{2}) = \dfrac{\sqrt{2}(\pi+1)}{\pi}$.

Answer: $\dfrac{\sqrt{2}(\pi+1)}{\pi}$

</details>

---

### Q11. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function $f(x) = ax^3 - bx^2 - 8x - 4$ satisfies Roll's theorem in $[1,3]$, if $f'(2) = 0$ then $a - b$ is equal to...

**Options:**

- **(A)** $2$
- **(B)** $-2$
- **(C)** $0$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2$**

**Detailed Solution:**

Since $f(x)$ satisfies Rolle's theorem in $[1, 3]$, we have $f(1) = f(3)$.

$a(1)^3 - b(1)^2 - 8(1) - 4 = a(3)^3 - b(3)^2 - 8(3) - 4$

$a - b - 12 = 27a - 9b - 28$

$26a - 8b = 16 \Rightarrow 13a - 4b = 8$

Also, $f'(x) = 3ax^2 - 2bx - 8$.

Given $f'(2) = 0$, we have:

$3a(2)^2 - 2b(2) - 8 = 0$

$12a - 4b = 8$

Subtracting the second equation from the first:

$(13a - 4b) - (12a - 4b) = 8 - 8$

$a = 0$

Substituting $a = 0$ into $12a - 4b = 8$:

$-4b = 8 \Rightarrow b = -2$

Therefore, $a - b = 0 - (-2) = 2$.

</details>

---

### Q12. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If Rolle's theorem is applicable for the function $f(x) = \log\left(\dfrac{x^2+a}{x}\right)$ on $[3, 4]$ with $c \in (3, 4)$ such that $f'(c) = 0$, then the value of $f''(c)$ is

**Options:**

- **(A)** $\dfrac{1}{48}$
- **(B)** $\dfrac{1}{36}$
- **(C)** $\dfrac{1}{24}$
- **(D)** $\dfrac{1}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{12}$**

**Detailed Solution:**

Since Rolle's theorem is applicable for $f(x)$ on $[3, 4]$, we have $f(3) = f(4)$.

$\log\left(\dfrac{9+a}{3}\right) = \log\left(\dfrac{16+a}{4}\right)$

$\dfrac{9+a}{3} = \dfrac{16+a}{4}$

$36 + 4a = 48 + 3a \Rightarrow a = 12$

The function becomes $f(x) = \log(x^2+12) - \log x$.

Differentiating with respect to $x$:

$f'(x) = \dfrac{2x}{x^2+12} - \dfrac{1}{x}$

For $f'(c) = 0$:

$\dfrac{2c}{c^2+12} - \dfrac{1}{c} = 0 \Rightarrow 2c^2 = c^2 + 12 \Rightarrow c^2 = 12$

Differentiating $f'(x)$ again to find $f''(x)$:

$f''(x) = \dfrac{2(x^2+12) - 2x(2x)}{(x^2+12)^2} + \dfrac{1}{x^2} = \dfrac{24-2x^2}{(x^2+12)^2} + \dfrac{1}{x^2}$

Substituting $c^2 = 12$:

$f''(c) = \dfrac{24 - 2(12)}{(12+12)^2} + \dfrac{1}{12} = 0 + \dfrac{1}{12} = \dfrac{1}{12}$

Answer: $\dfrac{1}{12}$

</details>

---

### Q13. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)$ be the differentiable function for all $x$ such that $f'(x) \leq 5$ and $f(1) = 4$. The maximum value of $f(5)$ is...

**Options:**

- **(A)** $16$
- **(B)** $20$
- **(C)** $24$
- **(D)** $25$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $24$**

**Detailed Solution:**

By Lagrange's Mean Value Theorem on the interval $[1, 5]$, there exists some $c \in (1, 5)$ such that

$f'(c) = \dfrac{f(5) - f(1)}{5 - 1}$

Given that $f'(x) \leq 5$ for all $x$, we have $f'(c) \leq 5$.

$\dfrac{f(5) - 4}{4} \leq 5$

$f(5) - 4 \leq 20$

$f(5) \leq 24$

The maximum value of $f(5)$ is $24$.

Answer: $24$

</details>

---

### Q14. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the function $f(x) = ax^3 + bx^2 + 11x - 6$, defined on $[1, 3]$, satisfies all the conditions of Rolle's theorem for $c = 2 + \dfrac{1}{\sqrt{3}}$, then

**Options:**

- **(A)** $a = -1, b = \dfrac{1}{2}$
- **(B)** $a = 1, b = -6$
- **(C)** $a = -1, b = 6$
- **(D)** $a = -2, b = 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $a = 1, b = -6$**

**Detailed Solution:**

Since $f(x)$ satisfies Rolle's theorem on $[1, 3]$, we must have $f(1) = f(3)$.

$f(1) = a(1)^3 + b(1)^2 + 11(1) - 6 = a + b + 5$

$f(3) = a(3)^3 + b(3)^2 + 11(3) - 6 = 27a + 9b + 27$

Equating $f(1)$ and $f(3)$:

$a + b + 5 = 27a + 9b + 27$

$26a + 8b + 22 = 0 \Rightarrow 13a + 4b + 11 = 0$

By Rolle's theorem, $f'(c) = 0$ for $c = 2 + \dfrac{1}{\sqrt{3}}$.

$f'(x) = 3ax^2 + 2bx + 11$

$f'\left(2 + \dfrac{1}{\sqrt{3}}\right) = 3a\left(2 + \dfrac{1}{\sqrt{3}}\right)^2 + 2b\left(2 + \dfrac{1}{\sqrt{3}}\right) + 11 = 0$

$3a\left(4 + \dfrac{1}{3} + \dfrac{4}{\sqrt{3}}\right) + 4b + \dfrac{2b}{\sqrt{3}} + 11 = 0$

$13a + 4\sqrt{3}a + 4b + \dfrac{2b}{\sqrt{3}} + 11 = 0$

$(13a + 4b + 11) + \dfrac{1}{\sqrt{3}}(12a + 2b) = 0$

Substituting $13a + 4b + 11 = 0$ into the above equation:

$\dfrac{1}{\sqrt{3}}(12a + 2b) = 0 \Rightarrow 12a + 2b = 0 \Rightarrow b = -6a$

Substituting $b = -6a$ into $13a + 4b + 11 = 0$:

$13a + 4(-6a) + 11 = 0$

$-11a + 11 = 0 \Rightarrow a = 1$

$b = -6(1) = -6$

Answer: $a = 1, b = -6$

</details>

---

### Q15. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The function $\mathrm{f}(x)=x^3-6 x^2+a x+b$ satisfies the conditions of Rolle's theorem in $[1,3]$. Then the values of $a$ and $b$ are respectively

**Options:**

- **(A)** $11,-6$
- **(B)** $-6,11$
- **(C)** $-11,6$
- **(D)** $6, -11$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $11,-6$**

**Detailed Solution:**

For a function to satisfy the conditions of Rolle's theorem in the interval $[1, 3]$, we must have $f(1) = f(3)$.

Given $f(x) = x^3 - 6x^2 + ax + b$, we find $f(1)$ and $f(3)$:

$f(1) = (1)^3 - 6(1)^2 + a(1) + b = a + b - 5$

$f(3) = (3)^3 - 6(3)^2 + a(3) + b = 27 - 54 + 3a + b = 3a + b - 27$

Equating $f(1)$ and $f(3)$:

$a + b - 5 = 3a + b - 27$

$2a = 22 \Rightarrow a = 11$

The value of $b$ can be any real number. Looking at the given options, the only option with $a = 11$ is $11, -6$.

Thus, $a = 11$ and $b = -6$.

Answer: $11,-6$

</details>

---

### Q16. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If Rolle's theorem holds for the function $x^3+a x^2+b x, 1 \leqslant x \leqslant 2$ at the point $\frac{4}{3}$, then the values of $a$ and $b$ are respectively.

**Options:**

- **(A)** $5,8$
- **(B)** $-8,5$
- **(C)** $8,-5$
- **(D)** $-5,8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-5,8$**

**Detailed Solution:**

For Rolle's theorem to hold for $f(x) = x^3 + ax^2 + bx$ on $[1, 2]$, we must have $f(1) = f(2)$ and $f'(c) = 0$ where $c = \dfrac{4}{3}$.

Using $f(1) = f(2)$:

$1^3 + a(1)^2 + b(1) = 2^3 + a(2)^2 + b(2)$

$1 + a + b = 8 + 4a + 2b$

$3a + b = -7$

Using $f'(c) = 0$ at $c = \dfrac{4}{3}$:

$f'(x) = 3x^2 + 2ax + b$

$f'\left(\dfrac{4}{3}\right) = 3\left(\dfrac{4}{3}\right)^2 + 2a\left(\dfrac{4}{3}\right) + b = 0$

$\dfrac{16}{3} + \dfrac{8a}{3} + b = 0$

$8a + 3b = -16$

Solving the two equations $3a + b = -7$ and $8a + 3b = -16$:

From the first equation, $b = -7 - 3a$. Substituting into the second equation:

$8a + 3(-7 - 3a) = -16$

$8a - 21 - 9a = -16$

$-a = 5 \Rightarrow a = -5$

Substituting $a = -5$ into $b = -7 - 3a$:

$b = -7 - 3(-5) = 8$

The values of $a$ and $b$ are $-5$ and $8$ respectively.

Answer: $-5,8$

</details>

---

### Q17. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let f be a function which is continuous and differentiable for all $x$. If $\mathrm{f}(1)=1$ and $\mathrm{f}^{\prime}(\mathrm{x}) \leq 5$ for all $x$ in $[1,5]$, then the maximum value of $f(5)$ is

**Options:**

- **(A)** $5$
- **(B)** $20$
- **(C)** $6$
- **(D)** $21$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $21$**

**Detailed Solution:**

By Lagrange's Mean Value Theorem for the function $f(x)$ on the interval $[1, 5]$, there exists at least one $c \in (1, 5)$ such that

$f'(c) = \dfrac{f(5) - f(1)}{5 - 1}$

It is given that $f'(x) \leq 5$ for all $x \in [1, 5]$. Therefore, $f'(c) \leq 5$.

$\dfrac{f(5) - 1}{4} \leq 5$

$f(5) - 1 \leq 20$

$f(5) \leq 21$

The maximum value of $f(5)$ is $21$.

Answer: $21$

</details>

---

### Q18. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The abscissae of the points of the curve $\mathrm{y}=x^3$ are in the interval $[-2,2]$, where the slope of the tangents can be obtained by mean value theorem for the interval $[-2,2]$ are

**Options:**

- **(A)** $0$
- **(B)** $\pm \sqrt{3}$
- **(C)** $\pm \frac{2}{\sqrt{3}}$
- **(D)** $\frac{\sqrt{3}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\pm \frac{2}{\sqrt{3}}$**

**Detailed Solution:**

Given $f(x) = x^3$ and the interval $[-2, 2]$.

By Lagrange's Mean Value Theorem, there exists at least one point $c \in (-2, 2)$ such that $f'(c) = \dfrac{f(b) - f(a)}{b - a}$.

Here, $a = -2$ and $b = 2$.

$f(2) = 2^3 = 8$

$f(-2) = (-2)^3 = -8$

$f'(x) = 3x^2 \Rightarrow f'(c) = 3c^2$

Substituting these values into the Mean Value Theorem formula:

$3c^2 = \dfrac{8 - (-8)}{2 - (-2)}$

$3c^2 = \dfrac{16}{4} = 4$

$c^2 = \dfrac{4}{3}$

$c = \pm \dfrac{2}{\sqrt{3}}$

Since $\pm \dfrac{2}{\sqrt{3}} \in (-2, 2)$, the required abscissae are $\pm \dfrac{2}{\sqrt{3}}$.

Answer: $\pm \frac{2}{\sqrt{3}}$

</details>

---

### Q19. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the function $\mathrm{f}(x)=x(x+3) \mathrm{e}^{-\frac{x}{2}}$ satisfies all the conditions of Rolle's theorem in $[-3,0]$, then c is

**Options:**

- **(A)** $0$
- **(B)** $-1$
- **(C)** $-2$
- **(D)** $-3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-2$**

**Detailed Solution:**

Given $\mathrm{f}(x) = (x^2 + 3x) \mathrm{e}^{-\dfrac{x}{2}}$

Differentiating with respect to $x$ using the product rule:

$\mathrm{f}'(x) = (2x + 3) \mathrm{e}^{-\dfrac{x}{2}} + (x^2 + 3x) \mathrm{e}^{-\dfrac{x}{2}} \left(-\dfrac{1}{2}\right)$

$\mathrm{f}'(x) = \mathrm{e}^{-\dfrac{x}{2}} \left( 2x + 3 - \dfrac{x^2}{2} - \dfrac{3x}{2} \right)$

$\mathrm{f}'(x) = \mathrm{e}^{-\dfrac{x}{2}} \left( \dfrac{-x^2 + x + 6}{2} \right)$

By Rolle's theorem, there exists $c \in (-3, 0)$ such that $\mathrm{f}'(c) = 0$.

$\mathrm{e}^{-\dfrac{c}{2}} \left( \dfrac{-c^2 + c + 6}{2} \right) = 0$

Since $\mathrm{e}^{-\dfrac{c}{2}} \neq 0$, we have:

$-c^2 + c + 6 = 0$

$c^2 - c - 6 = 0$

$(c - 3)(c + 2) = 0$

$c = 3$ or $c = -2$

Since $c \in (-3, 0)$, we get $c = -2$.

Answer: $-2$

</details>

---

### Q20. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In the mean value theorem, $\mathrm{f}^{\prime}(\mathrm{c})=\frac{\mathrm{f}(\mathrm{b})-\mathrm{f}(\mathrm{a})}{\mathrm{b}-\mathrm{a}}$, if $a=0, \mathrm{~b}=\frac{1}{2}$ and $\mathrm{f}(x)=x(x-1)(x-2)$, then the value of c is

**Options:**

- **(A)** $1-\frac{\sqrt{15}}{6}$
- **(B)** $1-\frac{\sqrt{13}}{6}$
- **(C)** $1-\frac{\sqrt{21}}{6}$
- **(D)** $1+\frac{\sqrt{21}}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1-\frac{\sqrt{21}}{6}$**

**Detailed Solution:**

Given $f(x) = x(x-1)(x-2) = x^3 - 3x^2 + 2x$

Differentiating with respect to $x$, we get:

$f'(x) = 3x^2 - 6x + 2$

For the given interval $[a, b] = \left[0, \dfrac{1}{2}\right]$:

$f(a) = f(0) = 0$

$f(b) = f\left(\dfrac{1}{2}\right) = \left(\dfrac{1}{2}\right)^3 - 3\left(\dfrac{1}{2}\right)^2 + 2\left(\dfrac{1}{2}\right) = \dfrac{1}{8} - \dfrac{3}{4} + 1 = \dfrac{3}{8}$

By the Mean Value Theorem:

$f'(c) = \dfrac{f(b) - f(a)}{b - a}$

$3c^2 - 6c + 2 = \dfrac{\dfrac{3}{8} - 0}{\dfrac{1}{2} - 0}$

$3c^2 - 6c + 2 = \dfrac{3}{4}$

Multiplying by $4$ on both sides:

$12c^2 - 24c + 8 = 3$

$12c^2 - 24c + 5 = 0$

Using the quadratic formula:

$c = \dfrac{24 \pm \sqrt{(-24)^2 - 4(12)(5)}}{2(12)}$

$c = \dfrac{24 \pm \sqrt{576 - 240}}{24}$

$c = \dfrac{24 \pm \sqrt{336}}{24}$

$c = \dfrac{24 \pm 4\sqrt{21}}{24}$

$c = 1 \pm \dfrac{\sqrt{21}}{6}$

Since $c$ must lie in the open interval $(a, b) = \left(0, \dfrac{1}{2}\right)$, we reject $c = 1 + \dfrac{\sqrt{21}}{6}$ as it is greater than $1$.

Therefore, $c = 1 - \dfrac{\sqrt{21}}{6}$.

Answer: $1-\frac{\sqrt{21}}{6}$

</details>

---

### Q21. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{f}(x)=(x-1)(x-2)(x-3), x \in[0,4]$, Values of C will be _______ [if L.M.V.T. (Lagrange's Mean Value Theorem) can be applied].

**Options:**

- **(A)** $\dfrac{4-2 \sqrt{3}}{3}, \dfrac{4+2 \sqrt{3}}{3}$
- **(B)** $\dfrac{6-2 \sqrt{3}}{3}, \dfrac{6+2 \sqrt{3}}{3}$
- **(C)** $\dfrac{6-\sqrt{3}}{3}, \dfrac{6+\sqrt{3}}{3}$
- **(D)** $2-\sqrt{3}, 2+\sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{6-2 \sqrt{3}}{3}, \dfrac{6+2 \sqrt{3}}{3}$**

**Detailed Solution:**

Given $f(x) = (x-1)(x-2)(x-3) = x^3 - 6x^2 + 11x - 6$

Differentiating with respect to $x$, we get:

$f'(x) = 3x^2 - 12x + 11$

By Lagrange's Mean Value Theorem, there exists $c \in (0, 4)$ such that:

$f'(c) = \dfrac{f(4) - f(0)}{4 - 0}$

Evaluating the function at the endpoints:

$f(4) = (4-1)(4-2)(4-3) = 3 \times 2 \times 1 = 6$

$f(0) = (0-1)(0-2)(0-3) = -1 \times -2 \times -3 = -6$

Substituting these values into the LMVT formula:

$3c^2 - 12c + 11 = \dfrac{6 - (-6)}{4}$

$3c^2 - 12c + 11 = \dfrac{12}{4} = 3$

$3c^2 - 12c + 8 = 0$

Solving for $c$ using the quadratic formula:

$c = \dfrac{12 \pm \sqrt{(-12)^2 - 4(3)(8)}}{2(3)}$

$c = \dfrac{12 \pm \sqrt{144 - 96}}{6}$

$c = \dfrac{12 \pm \sqrt{48}}{6} = \dfrac{12 \pm 4\sqrt{3}}{6}$

$c = \dfrac{6 \pm 2\sqrt{3}}{3}$

Since both values $\dfrac{6 - 2\sqrt{3}}{3} \approx 0.845$ and $\dfrac{6 + 2\sqrt{3}}{3} \approx 3.155$ lie in the interval $(0, 4)$, they are valid values for $c$.

Answer: $\dfrac{6-2 \sqrt{3}}{3}, \dfrac{6+2 \sqrt{3}}{3}$

</details>

---

### Q22. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If Mean value theorem holds for the function $\mathrm{f}(x)=(x-1)(x-2)(x-3), x \in[0,4] \quad$ then the values of c as per the theorem are

**Options:**

- **(A)** $2 \pm \dfrac{4}{\sqrt{3}}$
- **(B)** $2 \pm \dfrac{2}{\sqrt{3}}$
- **(C)** $2 \pm \sqrt{2}$
- **(D)** $2 \pm \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \pm \dfrac{2}{\sqrt{3}}$**

**Detailed Solution:**

Given $\mathrm{f}(x) = (x-1)(x-2)(x-3) = x^3 - 6x^2 + 11x - 6$

$\mathrm{f}'(x) = 3x^2 - 12x + 11$

By Mean Value Theorem, there exists $c \in (0, 4)$ such that $\mathrm{f}'(c) = \dfrac{\mathrm{f}(4) - \mathrm{f}(0)}{4 - 0}$

$\mathrm{f}(4) = (4-1)(4-2)(4-3) = 3 \times 2 \times 1 = 6$

$\mathrm{f}(0) = (0-1)(0-2)(0-3) = -1 \times -2 \times -3 = -6$

$\mathrm{f}'(c) = \dfrac{6 - (-6)}{4} = \dfrac{12}{4} = 3$

$3c^2 - 12c + 11 = 3$

$3c^2 - 12c + 8 = 0$

$c = \dfrac{12 \pm \sqrt{(-12)^2 - 4(3)(8)}}{2(3)}$

$c = \dfrac{12 \pm \sqrt{144 - 96}}{6}$

$c = \dfrac{12 \pm \sqrt{48}}{6} = \dfrac{12 \pm 4\sqrt{3}}{6}$

$c = 2 \pm \dfrac{2}{\sqrt{3}}$

Both values lie in the interval $(0, 4)$.

Answer: $2 \pm \dfrac{2}{\sqrt{3}}$

</details>

---

### Q23. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of c for which Rolle's theorem for the function $\mathrm{f}(x)=x^3-3 x^2+2 x$ in the interval $[0,2]$ are

**Options:**

- **(A)** $\pm 1$
- **(B)** $\pm 2$
- **(C)** $1 \pm \dfrac{1}{\sqrt{3}}$
- **(D)** $\sqrt{3}(1 \pm \sqrt{3})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1 \pm \dfrac{1}{\sqrt{3}}$**

**Detailed Solution:**

Given function is $f(x) = x^3 - 3x^2 + 2x$ on the interval $[0, 2]$.

$f(x)$ is a polynomial, so it is continuous on $[0, 2]$ and differentiable on $(0, 2)$.

$f(0) = 0^3 - 3(0)^2 + 2(0) = 0$

$f(2) = 2^3 - 3(2)^2 + 2(2) = 8 - 12 + 4 = 0$

Since $f(0) = f(2)$, Rolle's theorem is applicable.

By Rolle's theorem, there exists at least one $c \in (0, 2)$ such that $f'(c) = 0$.

$f'(x) = 3x^2 - 6x + 2$

$f'(c) = 3c^2 - 6c + 2 = 0$

$c = \dfrac{6 \pm \sqrt{36 - 24}}{6} = \dfrac{6 \pm \sqrt{12}}{6} = \dfrac{6 \pm 2\sqrt{3}}{6} = 1 \pm \dfrac{1}{\sqrt{3}}$

Both values $1 + \dfrac{1}{\sqrt{3}}$ and $1 - \dfrac{1}{\sqrt{3}}$ lie in the interval $(0, 2)$.

Answer: $1 \pm \dfrac{1}{\sqrt{3}}$

</details>

---

### Q24. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of C for which Mean value Theorem holds for the function $\mathrm{f}(x)=\log _{\mathrm{e}} x$ on the interval $[1,3]$ is

**Options:**

- **(A)** $\log _3 \mathrm{e}$
- **(B)** $\log _{\mathrm{e}} 3$
- **(C)** $\quad \dfrac{1}{2} \log _{\mathrm{e}} 3$
- **(D)** $2 \log _3 \mathrm{e}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 \log _3 \mathrm{e}$**

**Detailed Solution:**

Given function is $f(x) = \log_e x$ on the interval $[1, 3]$.

By Lagrange's Mean Value Theorem, there exists $c \in (1, 3)$ such that $f'(c) = \dfrac{f(3) - f(1)}{3 - 1}$.

Differentiating $f(x)$ with respect to $x$, we get $f'(x) = \dfrac{1}{x}$, which gives $f'(c) = \dfrac{1}{c}$.

We have $f(3) = \log_e 3$ and $f(1) = \log_e 1 = 0$.

Substituting these values into the Mean Value Theorem formula:

$\dfrac{1}{c} = \dfrac{\log_e 3 - 0}{2}$

$\dfrac{1}{c} = \dfrac{\log_e 3}{2}$

$c = \dfrac{2}{\log_e 3}$

$c = 2 \log_3 e$

Since $e \approx 2.718$, $\log_3 e < 1$, and $2 \log_3 e \approx 1.82$, which lies in the interval $(1, 3)$.

Answer: $2 \log _3 \mathrm{e}$

</details>

---

### Q25. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If Rolle's theorem holds for the function $\mathrm{f}(x)=x^3+\mathrm{b} x^2+\mathrm{ax}+5$ on $[1,3]$ with $\mathrm{c}=2+\dfrac{1}{\sqrt{3}}$, then the values of $a$ and $b$ respectively are

**Options:**

- **(A)** $-11,6$
- **(B)** 11,6
- **(C)** $-11,-6$
- **(D)** $11,-6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $11,-6$**

**Detailed Solution:**

For Rolle's theorem to hold on the interval $[1, 3]$, we must have $\mathrm{f}(1) = \mathrm{f}(3)$.

$\mathrm{f}(1) = 1^3 + \mathrm{b}(1)^2 + \mathrm{a}(1) + 5 = \mathrm{a} + \mathrm{b} + 6$

$\mathrm{f}(3) = 3^3 + \mathrm{b}(3)^2 + \mathrm{a}(3) + 5 = 3\mathrm{a} + 9\mathrm{b} + 32$

Equating $\mathrm{f}(1)$ and $\mathrm{f}(3)$:

$\mathrm{a} + \mathrm{b} + 6 = 3\mathrm{a} + 9\mathrm{b} + 32$

$2\mathrm{a} + 8\mathrm{b} + 26 = 0$

$\mathrm{a} + 4\mathrm{b} + 13 = 0$  --- (1)

Also, by Rolle's theorem, $\mathrm{f}'(\mathrm{c}) = 0$ for some $\mathrm{c} \in (1, 3)$.

$\mathrm{f}'(x) = 3x^2 + 2\mathrm{b}x + \mathrm{a}$

Substituting $\mathrm{c} = 2 + \dfrac{1}{\sqrt{3}}$:

$\mathrm{f}'\left(2 + \dfrac{1}{\sqrt{3}}\right) = 3\left(2 + \dfrac{1}{\sqrt{3}}\right)^2 + 2\mathrm{b}\left(2 + \dfrac{1}{\sqrt{3}}\right) + \mathrm{a} = 0$

$3\left(4 + \dfrac{1}{3} + \dfrac{4}{\sqrt{3}}\right) + 4\mathrm{b} + \dfrac{2\mathrm{b}}{\sqrt{3}} + \mathrm{a} = 0$

$12 + 1 + \dfrac{12}{\sqrt{3}} + 4\mathrm{b} + \dfrac{2\mathrm{b}}{\sqrt{3}} + \mathrm{a} = 0$

$(\mathrm{a} + 4\mathrm{b} + 13) + \dfrac{12 + 2\mathrm{b}}{\sqrt{3}} = 0$

From equation (1), $\mathrm{a} + 4\mathrm{b} + 13 = 0$, so we get:

$\dfrac{12 + 2\mathrm{b}}{\sqrt{3}} = 0$

$12 + 2\mathrm{b} = 0 \Rightarrow \mathrm{b} = -6$

Substituting $\mathrm{b} = -6$ into equation (1):

$\mathrm{a} + 4(-6) + 13 = 0$

$\mathrm{a} - 24 + 13 = 0 \Rightarrow \mathrm{a} = 11$

The values of $\mathrm{a}$ and $\mathrm{b}$ respectively are $11, -6$.

Answer: $11,-6$

</details>

---

### Q26. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(\mathrm{a})=2, \mathrm{f}^{\prime}(\mathrm{a})=1, \mathrm{~g}(\mathrm{a})=-1, \mathrm{~g}^{\prime}(\mathrm{a})=2$, then as $x$ approaches a, $\frac{\mathrm{g}(x) \mathrm{f}(\mathrm{a})-\mathrm{g}(\mathrm{a}) \mathrm{f}(x)}{(x-\mathrm{a})}$ approaches

**Options:**

- **(A)** 3
- **(B)** 5
- **(C)** 0
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 5**

**Detailed Solution:**

Applying L-Hospital's rule, we get
$\begin{aligned}
& \lim _{x \rightarrow a} \frac{g(x) f(a)-g(a) f(x)}{(x-a)} \\
& =\lim _{x \rightarrow a} \frac{g^{\prime}(x) f(a)-g(a) f^{\prime}(x)}{1} \\
& =g^{\prime}(a) f(a)-g(a) f^{\prime}(a) \\
& =2(2)-(-1)(1) \\
& =4+1 \\
& =5
\end{aligned}$

</details>

---

### Q27. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If Rolle's theorem holds for the function $f(x)=x^3+b x^2+a x+5$ on $[1,3]$ with $c=2+\frac{1}{\sqrt{3}}$, then the values of $a$ and $b$ respectively are

**Options:**

- **(A)** $-11,-6$
- **(B)** 11,6
- **(C)** $11,-6$
- **(D)** 6,11

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $11,-6$**

**Detailed Solution:**

Since $\mathrm{f}(x)$ satisfies the Rolle's theorem,
$f(1)=f(3)$
$\therefore \quad 1+b+a+5=27+9 b+3 a+5$
$\Rightarrow 2 a+8 b=-26$
$\Rightarrow a+4 b=-13$                                ...(i)
$\vec{f}(x)=x^3+b x^2+a x+5$
$\therefore \quad \mathrm{f}^{\prime}(x)=3 x^2+2 \mathrm{~b} x+\mathrm{a}$
Now, $\mathrm{f}^{\prime}(\mathrm{c})=0$
$$
\begin{aligned}
& \Rightarrow \mathrm{f}^{\prime}\left(2+\frac{1}{\sqrt{3}}\right)=0 \\
& \Rightarrow 3\left(2+\frac{1}{\sqrt{3}}\right)^2+2 \mathrm{~b}\left(2+\frac{1}{\sqrt{3}}\right)+\mathrm{a}=0 \\
& \Rightarrow 3\left(4+\frac{4}{\sqrt{3}}+\frac{1}{3}\right)+4 \mathrm{~b}+\frac{2 \mathrm{~b}}{\sqrt{3}}+\mathrm{a}=0 \\
& \Rightarrow \mathrm{a}+4 \mathrm{~b}+\frac{2 \mathrm{~b}+12}{\sqrt{3}}+13=0 \\
& \Rightarrow-13+\frac{2 \mathrm{~b}+12}{\sqrt{3}}+13=0 \\
& \Rightarrow \frac{2 \mathrm{~b}+12}{\sqrt{3}}=0 \\
& \Rightarrow \mathrm{b}=-6
\end{aligned}
$$
Substituting $b=-6$ in (i), we get $a=11$

</details>

---

### Q28. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Values of $\mathrm{c}$ as per Rolle's theorem for $f(x)=\sin x+\cos x+6$ on $[0,2 \pi]$ are

**Options:**

- **(A)** $\frac{\pi}{3}, \frac{5 \pi}{3}$
- **(B)** $\frac{\pi}{6}, \frac{5 \pi}{6}$
- **(C)** $\frac{\pi}{4}, \frac{5 \pi}{4}$
- **(D)** $\frac{\pi}{4}, \frac{7 \pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{4}, \frac{5 \pi}{4}$**

**Detailed Solution:**

$\begin{array}{ll} & \mathrm{f}(x)=\sin x+\cos x+6 \\ \therefore \quad & \mathrm{f}^{\prime}(x)=\cos x-\sin x \\ & \text { Now, } \mathrm{f}^{\prime}(\mathrm{c})=0 \\ \Rightarrow \cos \mathrm{c}-\sin \mathrm{c}=0 \\ \Rightarrow \cos \mathrm{c}=\sin \mathrm{c} \\ \Rightarrow \tan \mathrm{c}=1 \\ \Rightarrow \mathrm{c}=\frac{\pi}{4}, \frac{5 \pi}{4} \quad \ldots[\because x \in[0,2 \pi]]\end{array}$

</details>

---

### Q29. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the function $f$ is given by $\mathrm{f}(x)=x^3-3(\mathrm{a}-2) x^2+3 \mathrm{a} x+7$, for some a $\in \mathbb{R}$, is increasing in $(0,1]$ and decreasing in $[1,5)$, then a root of the equation $\frac{\mathrm{f}(x)-14}{(x-1)^2}=0(x \neq 1)$ is

**Options:**

- **(A)** $-7$
- **(B)** $6$
- **(C)** $7$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $7$**

**Detailed Solution:**

$f(x)=x^3-3(a-2) x^2+3 a x+7$
As $\mathrm{f}(x)$ is increasing in $(0,1]$ and decreasing in $[1,5)$, we get that $\mathrm{f}(x)$ has critical point at $x=1$ $\Rightarrow \mathrm{f}^{\prime}(1)=0$
$\mathrm{f}^{\prime}(x)=3 x^2-6(\mathrm{a}-2) x+3 \mathrm{a}$
$\begin{aligned}
& \therefore \quad 3(1)^2-6(a-2)+3 a=0 \\
& \therefore \quad \mathrm{a}=5 \\
& \therefore \quad \frac{\mathrm{f}(x)-14}{(x-1)^2}=\frac{x^3-9 x^2+15 x-7}{(x-1)^2} \\
& =\frac{(x-1)^2(x-7)}{(x-1)^2} \\
& =x-7 \\
&
\end{aligned}$
$\therefore \quad$ The required root is 7 .

</details>

---

### Q30. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Value of $c$ satisfying the conditions and conclusions of Rolle's theorem for the function $\mathrm{f}(x)=x \sqrt{x+6}, x \in[-6,0]$ is

**Options:**

- **(A)** $-4$
- **(B)** $4$
- **(C)** $3$
- **(D)** $-3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-4$**

**Detailed Solution:**

$$
\begin{aligned}
\mathrm{f}(x) & =x \sqrt{x+6} \\
\therefore \quad \mathrm{f}^{\prime}(x) & =x\left(\frac{1}{2 \sqrt{x+6}}\right)+\sqrt{x+6}(1) \\
& =\frac{x}{2 \sqrt{x+6}}+\sqrt{x+6}
\end{aligned}
$$

Since $\mathrm{f}(x)$ satisfies all the conditions of Rolle's Theorem,

There exists $c \in(-6,0)$ such that
$$
\begin{aligned}
& \mathrm{f}^{\prime}(\mathrm{c})=0 \\
& \Rightarrow \frac{\mathrm{c}}{2 \sqrt{\mathrm{c}+6}}+\sqrt{\mathrm{c}+6}=0 \\
& \Rightarrow \mathrm{c}+2 \mathrm{c}+12=0 \\
& \Rightarrow \mathrm{c}=-4
\end{aligned}
$$

</details>

---

### Q31. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $c$ of Lagrange's mean value theorem for $\mathrm{f}(x)=\sqrt{25-x^2}$ on $[1,5]$ is

**Options:**

- **(A)** $\sqrt {15}$
- **(B)** $5$
- **(C)** $\sqrt{10}$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt {15}$**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{f}(x)=\sqrt{25-x^2} \\
& \therefore \quad \mathrm{f}^{\prime}(x=\mathrm{c})=\frac{-2 \mathrm{c}}{2 \sqrt{25-\mathrm{c}^2}} \\
&=\frac{-\mathrm{c}}{\sqrt{25-\mathrm{c}^2}}
\end{aligned}$
Applying Lagrange's mean value theorem, we get
$\begin{aligned}
& \mathrm{f}^{\prime}(\mathrm{c})=\frac{\mathrm{f}(1)-\mathrm{f}(5)}{1-5} \\
& \therefore \quad \frac{\mathrm{c}}{\sqrt{25-\mathrm{c}^2}}=\frac{\sqrt{25-1}-\sqrt{25-5^2}}{1-5} \\
& \therefore \quad \frac{-\mathrm{c}}{\sqrt{25-\mathrm{c}^2}}=\frac{-\sqrt{24}}{4}
\end{aligned}$
$\begin{array}{ll}
\therefore & 4 \mathrm{c}=\sqrt{24} \cdot \sqrt{25-\mathrm{c}^2} \\
\therefore & 16 \mathrm{c}^2=24\left(25-\mathrm{c}^2\right) \\
\therefore & \mathrm{c}^2=15 \\
\therefore & \mathrm{c}= \pm \sqrt{15}
\end{array}$
Since $c=-\sqrt{15}$ does not lie in $[1,5]$ $c=\sqrt{15}$

</details>

---

### Q32. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two positive numbers $\mathrm{x}$ and $\mathrm{y}$ such that $(x+y)=60$ and $x y^3$ is maximum, then the numbers are respectively

**Options:**

- **(A)** 45,15
- **(B)** 30,30
- **(C)** 20,40
- **(D)** 40,20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 45,15**

**Detailed Solution:**

$x+y=60 \Rightarrow x=60-y$
Now let $z=x y^3=(60-y) y^3=60 y^3-y^4$
$$
\Rightarrow \frac{d z}{d y}=180 y^2-4 y^3=4 y^2(45-y)
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/6ljFfCrpcY3-RYEicLYNEmM1LkQNsiBRYEkDawt960I.original.fullsize.png">
i.e., $x y^3$ is maximum $y=45$ and $x=60-45=15$

</details>

---

### Q33. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If L.M.V.T. is applicable for the function $f(x)=x+\frac{1}{x}, x \in[1,3]$, then $c=$

**Options:**

- **(A)** $-\sqrt{3}$
- **(B)** $\sqrt{3}$
- **(C)** 2
- **(D)** $\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{3}$**

**Detailed Solution:**

(C)
Given $\mathrm{f}(\mathrm{x})=\mathrm{x}+\frac{1}{\mathrm{x}}$ and LMVT holds
$\begin{array}{l}
f^{\prime}(x)=1-\frac{1}{x^{2}} \Rightarrow f^{\prime}(c)=1-\frac{1}{c^{2}} \\
f(1)=1+1=2 \text { and } f(3)=3+\frac{1}{3}=\frac{10}{3}
\end{array}$
$\therefore \quad f^{\prime}(c)=1-\frac{1}{c^{2}}=\frac{\frac{10}{3}-2}{(3-1)} \Rightarrow 1-\frac{1}{c^{2}}=\frac{4}{3(2)}=\frac{2}{3}$
$\therefore \quad \frac{1}{c^{2}}=1-\frac{2}{3}=\frac{1}{3} \Rightarrow c^{2}=3 \Rightarrow c=\pm \sqrt{3}$

</details>

---

### Q34. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=\log (\sin x), x \in\left[\frac{\pi}{6}, \frac{5 \pi}{6}\right]$, then value of 'c'by applyng L.mv.T. is

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{2 \pi}{3}$
- **(C)** $\frac{3 \pi}{4}$
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{2}$**

**Detailed Solution:**

(B)
Value of ' ' by applying L.M.V.T. is to be found out
$\begin{aligned}
f(x) &=\log (\sin x) \text { on }\left[\frac{\pi}{6}, \frac{5 \pi}{6}\right] \Rightarrow \operatorname{lot} a=\frac{\pi}{6}, b=\frac{5 \pi}{6} \\
f^{\prime}(x) &=\frac{\cos x}{\sin x}=\cot x \Rightarrow f^{\prime}(c)=\cot c \\
f^{\prime}(c) &=\frac{f(b)-f(a)}{b-a}=\frac{f\left(\frac{5 \pi}{6}\right)-f\left(\frac{\pi}{6}\right)}{5 \frac{\pi}{6}-\frac{\pi}{6}} \\
\cot c &=\frac{\log \left[\sin \left(\frac{5 \pi}{6}\right)\right]-\log \left[\sin \left(\frac{\pi}{6}\right)\right]}{\frac{2 \pi}{3}}=\frac{\log \frac{1}{2}-\log \left(\frac{1}{2}\right)}{2 \frac{\pi}{3}} \\
\cot c=0 & \Rightarrow c=\frac{\pi}{2}
\end{aligned}$

</details>

---

### Q35. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the L. M. V. T. holds for the function $f(x)=x+\frac{1}{x}, x \in[1,3]$, then c=

**Options:**

- **(A)** $\sqrt{3}$
- **(B)** 3
- **(C)** 2
- **(D)** $-\sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{3}$**

**Detailed Solution:**

Given $f(x)=x+\frac{1}{x}$ and LMVT holds
$f^{\prime}(x)=1-\frac{1}{x^{2}} \Rightarrow f^{\prime}(c)=1-\frac{1}{c^{2}}$
$f(1)=1+1=2 \text { and } f(3)=3+\frac{1}{3}=\frac{10}{3}$
$\therefore \quad f^{\prime}(c)=1-\frac{1}{c^{2}}=\frac{\frac{10}{3}-2}{(3-1)} \Rightarrow 1-\frac{1}{c^{2}}=\frac{4}{3(2)}=\frac{2}{3}$
$\therefore \quad \frac{1}{c^{2}}=1-\frac{2}{3}=\frac{1}{3} \Rightarrow c^{2}=3 \Rightarrow c=\pm \sqrt{3}$

</details>

---

### Q36. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=|x-2|, x \in[0,4]$ then the Rolle's theorem cannot be applied to the
function because

**Options:**

- **(A)** The function is not differentiable at every point in the $(0,4)$.
- **(B)** $f(4) \neq f(0)$
- **(C)** Function is not well-defined in the domain.
- **(D)** The function is not continuous at every point in the $[0,4]$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) The function is not differentiable at every point in the $(0,4)$.**

**Detailed Solution:**

Here $f(0)=|0-2|=-2$ and $f(4)=|4-2|=2$
Thus $\mathrm{f}(4) \neq \mathrm{f}(0)$
Hence Rolle's Theorem cannot be applied.

</details>

---

### Q37. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `2`

If Rolle's theorem for a function <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>-</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mfenced></math> is verified on <math><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></math> then the value of <math> <mi>c</mi> </math> is

**Options:**

- **(A)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>3</mn><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mi>π</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi>π</mi></math>**

**Detailed Solution:**

Given, <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>(</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi><mo>-</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mrow><mo>)</mo></math> 
 <math><mo>∴</mo><mi> </mi><mi> </mi><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mfenced><mo>+</mo><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi><mo>-</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mfenced><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></math> 
 <math><mo>∴</mo><mi> </mi><mi> </mi><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></math>  
To verify Rolle's Theorem.
 <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>c</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> 
 <math><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>c</mi></mrow></msup><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>c</mi><mo>=</mo><mn>0</mn></mrow></mrow></math> 
 <math><mo>⇒</mo><mi> </mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>c</mi><mo>=</mo><mn>0</mn></mrow></mrow></math> 
 <math><mo>∴</mo><mi> </mi><mi> </mi><mi>c</mi><mo>=</mo><mi>π</mi></math>

</details>

---

### Q38. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `3`

For all real $x$, the minimum value of $\frac{1-x+x^{2}}{1+x+x^{2}}$ is

**Options:**

- **(A)** 0
- **(B)** $1 / 3$
- **(C)** 1
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1 / 3$**

**Detailed Solution:**

Let $y=\frac{1-x+x^{2}}{1+x+x^{2}}=1-\frac{2 x}{1+x+x^{2}}$
$$
\begin{aligned}
&=1-\frac{2}{\frac{1}{x}+1+x} \\
\Rightarrow \quad y &=1-\frac{2}{t}
\end{aligned}
$$
where
$$
t=\frac{1}{x}+1+x
$$
Now, $y$ is minimum, when $\frac{2}{t}$ is $\max \Rightarrow t$ is $\mathrm{min}$.
$$
\begin{array}{lc}
\therefore & \frac{d t}{d x}=-\frac{1}{x^{2}}+1=0 \\
\Rightarrow \quad x=\pm 1 \\
\frac{d^{2} t}{d x^{2}}=\frac{2}{x^{3}}>0, \text { for } x=1
\end{array}
$$
$\therefore$ Minimum value of $y$ is
$$
\begin{aligned}
1-\frac{2}{1+1+1} &=1-\frac{2}{3} \\
&=\frac{1}{3}
\end{aligned}
$$

</details>

---

