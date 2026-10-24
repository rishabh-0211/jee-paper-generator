# MHT CET Mathematics - Definite Integration

## Topic 8: Leibnitz Rule of Differentiation

**Total Questions:** 4

---

### Q1. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int\limits_{0}^{f(x)} dt = x \cos(\pi x)$ then $f'(4) = \ldots$

**Options:**

- **(A)** $-1$
- **(B)** $0$
- **(C)** $1$
- **(D)** $4\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

Evaluating the integral on the left side:

$\int_{0}^{f(x)} dt = [t]_{0}^{f(x)} = f(x)$

Thus, the given equation simplifies to:

$f(x) = x \cos(\pi x)$

Differentiating both sides with respect to $x$ using the product rule:

$f'(x) = \cos(\pi x) - \pi x \sin(\pi x)$

Substituting $x = 4$ into the derivative:

$f'(4) = \cos(4\pi) - 4\pi \sin(4\pi)$

Since $\cos(4\pi) = 1$ and $\sin(4\pi) = 0$:

$f'(4) = 1 - 4\pi(0) = 1$

Answer: $1$

</details>

---

### Q2. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\displaystyle\int_{0}^{x} f(t)\,dt = x + \int_{x}^{0} t \cdot f(t)\,dt$ then the value of $f(1) =$

**Options:**

- **(A)** $\dfrac{1}{2}$
- **(B)** $2$
- **(C)** $1$
- **(D)** $\dfrac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{2}$**

**Detailed Solution:**

The given equation is $\displaystyle\int_{0}^{x} f(t)\,dt = x + \int_{x}^{0} t \cdot f(t)\,dt$

Using the property of definite integrals, this can be written as:

$\displaystyle\int_{0}^{x} f(t)\,dt = x - \int_{0}^{x} t \cdot f(t)\,dt$

Differentiating both sides with respect to $x$ using the Newton-Leibniz formula:

$f(x) = 1 - x \cdot f(x)$

$f(x) + x \cdot f(x) = 1$

$f(x)(1 + x) = 1$

$f(x) = \dfrac{1}{1 + x}$

Substituting $x = 1$:

$f(1) = \dfrac{1}{1 + 1} = \dfrac{1}{2}$

Answer: $\dfrac{1}{2}$

</details>

---

### Q3. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The function $f(x) = \int_0^x\dfrac{dt}{1 + \cos t}$ satisfies which of the following differential equations?

**Options:**

- **(A)** $2\dfrac{df}{dx} = 1 + [f(x)]^2$
- **(B)** $\dfrac{df}{dx} = 1 + [f(x)]^2$
- **(C)** $2\dfrac{df}{dx} = 1 - [f(x)]^2$
- **(D)** $\dfrac{df}{dx} = 1 - [f(x)]^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2\dfrac{df}{dx} = 1 + [f(x)]^2$**

**Detailed Solution:**

Given $f(x) = \int_0^x \dfrac{dt}{1 + \cos t}$

Using the half-angle formula $1 + \cos t = 2 \cos^2(t/2)$, we get:

$f(x) = \int_0^x \dfrac{dt}{2 \cos^2(t/2)} = \dfrac{1}{2} \int_0^x \sec^2(t/2) dt$

Integrating, we obtain:

$f(x) = \left[ \tan(t/2) \right]_0^x = \tan(x/2)$

Differentiating $f(x)$ with respect to $x$:

$\dfrac{df}{dx} = \dfrac{1}{2} \sec^2(x/2)$

Using the identity $\sec^2(x/2) = 1 + \tan^2(x/2)$:

$\dfrac{df}{dx} = \dfrac{1}{2} \left( 1 + \tan^2(x/2) \right)$

Substituting $f(x) = \tan(x/2)$:

$\dfrac{df}{dx} = \dfrac{1}{2} \left( 1 + [f(x)]^2 \right)$

$2\dfrac{df}{dx} = 1 + [f(x)]^2$

</details>

---

### Q4. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f: \mathbb{R} \rightarrow \mathbb{R}$ is differentiable function having $f(3)=3, f^{\prime}(3)=\frac{1}{27}$ and $\mathrm{g}(\mathrm{x})=\left\{\begin{array}{ccc}\int_3^{\mathrm{f}(x)} \frac{3 \mathrm{t}^2}{x-3} \mathrm{dt} & , & \text { if } x \neq 3 \\ \mathrm{~K} & , & \text { if } x=3\end{array}\right.$ is continuous at $x=3$, then $\mathrm{K}=$

**Options:**

- **(A)** 1
- **(B)** 3
- **(C)** $\frac{1}{3}$
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

Since $g(x)$ is continuous at $x=3$, we have $K = \lim_{x \to 3} g(x)$.

$K = \lim_{x \to 3} \dfrac{\int_3^{f(x)} 3t^2 dt}{x-3}$

As $f(3) = 3$, the numerator becomes $\int_3^3 3t^2 dt = 0$. Thus, it is of the form $\dfrac{0}{0}$.

Applying L'Hospital's rule and using the Newton-Leibniz formula for the derivative of the integral:

$K = \lim_{x \to 3} \dfrac{3(f(x))^2 f'(x)}{1}$

$K = 3(f(3))^2 f'(3)$

Substituting the given values $f(3) = 3$ and $f'(3) = \dfrac{1}{27}$:

$K = 3(3)^2 \left(\dfrac{1}{27}\right)$

$K = 27 \times \dfrac{1}{27} = 1$

Answer: 1

</details>

---

