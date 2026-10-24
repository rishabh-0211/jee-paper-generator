# MHT CET Mathematics - Trigonometric Ratios & Identities

## Topic 8: Trigonometric Series

**Total Questions:** 3

---

### Q1. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $33\theta = \pi$, then the value of $\cos\theta \cos2\theta \cos4\theta \cos8\theta \cos16\theta$ is

**Options:**

- **(A)** $\dfrac{1}{16}$
- **(B)** $\dfrac{1}{32}$
- **(C)** $\dfrac{1}{64}$
- **(D)** $\dfrac{-1}{32}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{32}$**

**Detailed Solution:**

Let $P = \cos\theta \cos2\theta \cos4\theta \cos8\theta \cos16\theta$

Multiplying and dividing by $2\sin\theta$, we get:

$P = \dfrac{2\sin\theta \cos\theta \cos2\theta \cos4\theta \cos8\theta \cos16\theta}{2\sin\theta}$

Using the identity $\sin(2x) = 2\sin x \cos x$ repeatedly:

$P = \dfrac{\sin2\theta \cos2\theta \cos4\theta \cos8\theta \cos16\theta}{2\sin\theta}$

$P = \dfrac{\sin4\theta \cos4\theta \cos8\theta \cos16\theta}{4\sin\theta}$

$P = \dfrac{\sin8\theta \cos8\theta \cos16\theta}{8\sin\theta}$

$P = \dfrac{\sin16\theta \cos16\theta}{16\sin\theta}$

$P = \dfrac{\sin32\theta}{32\sin\theta}$

Given $33\theta = \pi$, we have $32\theta = \pi - \theta$

Therefore, $\sin32\theta = \sin(\pi - \theta) = \sin\theta$

Substituting this back into the expression for $P$:

$P = \dfrac{\sin\theta}{32\sin\theta} = \dfrac{1}{32}$

Answer: $\dfrac{1}{32}$

</details>

---

### Q2. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The maximum value of $\left(\cos \alpha_1\right) \cdot\left(\cos \alpha_2\right) \ldots\left(\cos \alpha_n\right)$ under the constraints $0 \leq \alpha_1, \alpha_2, \ldots, \alpha_n \leq \frac{\pi}{2}$ and $\left(\cot \alpha_1\right) \cdot\left(\cot \alpha_2\right) \ldots\left(\cot \alpha_n\right)=1$ is

**Options:**

- **(A)** $\frac{1}{2^{\left(\frac{\mathrm{n}}{2}\right)}}$
- **(B)** $\frac{1}{2^{\mathrm{n}}}$
- **(C)** $2^n$
- **(D)** $2^{\frac{n}{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2^{\left(\frac{\mathrm{n}}{2}\right)}}$**

**Detailed Solution:**

Given $\prod_{i=1}^{n} \cot \alpha_i = 1$.

The expression to be maximized is $P = \prod_{i=1}^{n} \cos \alpha_i$.

Using the identity $\cos^2 \alpha_i = \dfrac{\cot^2 \alpha_i}{1 + \cot^2 \alpha_i}$.

Let $y_i = \cot^2 \alpha_i$. Since $\prod_{i=1}^{n} \cot \alpha_i = 1$, we have $\prod_{i=1}^{n} y_i = 1$.

The square of the expression is:

$P^2 = \prod_{i=1}^{n} \dfrac{y_i}{1 + y_i} = \dfrac{\prod_{i=1}^{n} y_i}{\prod_{i=1}^{n} (1 + y_i)} = \dfrac{1}{\prod_{i=1}^{n} (1 + y_i)}$

To maximize $P^2$, the denominator $\prod_{i=1}^{n} (1 + y_i)$ must be minimized.

Using the AM-GM inequality for $1$ and $y_i$ (since $y_i \geq 0$):

$\dfrac{1 + y_i}{2} \geq \sqrt{y_i} \Rightarrow 1 + y_i \geq 2\sqrt{y_i}$

Multiplying these inequalities for $i = 1, 2, \ldots, n$:

$\prod_{i=1}^{n} (1 + y_i) \geq 2^n \prod_{i=1}^{n} \sqrt{y_i}$

$\prod_{i=1}^{n} (1 + y_i) \geq 2^n \sqrt{\prod_{i=1}^{n} y_i}$

Since $\prod_{i=1}^{n} y_i = 1$, we get:

$\prod_{i=1}^{n} (1 + y_i) \geq 2^n$

Therefore, the maximum value of $P^2$ is:

$P^2 \leq \dfrac{1}{2^n}$

Taking the square root (since $P > 0$):

$P \leq \dfrac{1}{2^{\left(\dfrac{n}{2}\right)}}$

Equality holds when $y_i = 1$ for all $i$, which means $\cot \alpha_i = 1 \Rightarrow \alpha_i = \dfrac{\pi}{4}$.

Answer: $\frac{1}{2^{\left(\frac{\mathrm{n}}{2}\right)}}$

</details>

---

### Q3. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For the triangle ABC , with usual notations, if the angles $A, B, C$ are in A.P. and $\mathrm{m} \angle \mathrm{A}=30^{\circ}, \mathrm{c}=3$, then the values of a and b are respectively

**Options:**

- **(A)** $\dfrac{\sqrt{3}}{2}, \dfrac{3}{2}$
- **(B)** $\dfrac{3}{2}, \dfrac{3 \sqrt{3}}{2}$
- **(C)** $\dfrac{3 \sqrt{3}}{2}, \dfrac{3}{2}$
- **(D)** $\dfrac{3}{2}, \dfrac{\sqrt{3}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{3}{2}, \dfrac{3 \sqrt{3}}{2}$**

**Detailed Solution:**

Given that the angles $A, B, C$ are in A.P.

$2B = A + C$

Since $A + B + C = 180^{\circ}$, we have $3B = 180^{\circ} \Rightarrow B = 60^{\circ}$.

Given $\angle A = 30^{\circ}$, we can find $C$ as:

$C = 180^{\circ} - (30^{\circ} + 60^{\circ}) = 90^{\circ}$

Using the sine rule:

$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C}$

Substituting the known values:

$\dfrac{a}{\sin 30^{\circ}} = \dfrac{b}{\sin 60^{\circ}} = \dfrac{3}{\sin 90^{\circ}}$

$\dfrac{a}{\dfrac{1}{2}} = \dfrac{b}{\dfrac{\sqrt{3}}{2}} = \dfrac{3}{1} = 3$

Solving for $a$ and $b$:

$a = 3 \times \dfrac{1}{2} = \dfrac{3}{2}$

$b = 3 \times \dfrac{\sqrt{3}}{2} = \dfrac{3\sqrt{3}}{2}$

Answer: $\dfrac{3}{2}, \dfrac{3 \sqrt{3}}{2}$

</details>

---

