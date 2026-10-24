# MHT CET Mathematics - Inverse Trigonometric Functions

## Topic 1: Principal Value and Basics

**Total Questions:** 41

---

### Q1. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\alpha \leq 2\sin^{-1} x + \cos^{-1} x \leq \beta$, then the values of $\alpha$ and $\beta$ are

**Options:**

- **(A)** $\alpha = 0, \beta = 2\pi$
- **(B)** $\alpha = \pi, \beta = 2\pi$
- **(C)** $\alpha = 0, \beta = \pi$
- **(D)** $\alpha = -\pi, \beta = \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\alpha = 0, \beta = \pi$**

**Detailed Solution:**

Let $f(x) = 2\sin^{-1} x + \cos^{-1} x$.

We know that $\sin^{-1} x + \cos^{-1} x = \dfrac{\pi}{2}$ for $x \in [-1, 1]$.

Substituting this into the expression, we get:

$f(x) = \sin^{-1} x + (\sin^{-1} x + \cos^{-1} x) = \sin^{-1} x + \dfrac{\pi}{2}$

The principal value branch of $\sin^{-1} x$ has the range $\left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]$.

Therefore, $-\dfrac{\pi}{2} \leq \sin^{-1} x \leq \dfrac{\pi}{2}$.

Adding $\dfrac{\pi}{2}$ to all parts of the inequality:

$-\dfrac{\pi}{2} + \dfrac{\pi}{2} \leq \sin^{-1} x + \dfrac{\pi}{2} \leq \dfrac{\pi}{2} + \dfrac{\pi}{2}$

$0 \leq f(x) \leq \pi$

Comparing this with $\alpha \leq 2\sin^{-1} x + \cos^{-1} x \leq \beta$, we get $\alpha = 0$ and $\beta = \pi$.

Answer: $\alpha = 0, \beta = \pi$

</details>

---

### Q2. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\cos^{-1} x + \cos^{-1} y + \cos^{-1} z = 3\pi$, then $xy + yz + zx$ is equal to

**Options:**

- **(A)** $3$
- **(B)** $-3$
- **(C)** $2$
- **(D)** $-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3$**

**Detailed Solution:**

The principal value branch of $\cos^{-1} \theta$ is $[0, \pi]$.

Therefore, the maximum value of $\cos^{-1} \theta$ is $\pi$, which occurs at $\theta = -1$.

Given the equation $\cos^{-1} x + \cos^{-1} y + \cos^{-1} z = 3\pi$, the sum of three terms, each with a maximum value of $\pi$, is equal to $3\pi$. This is only possible if each term attains its maximum value.

Thus, $\cos^{-1} x = \pi$, $\cos^{-1} y = \pi$, and $\cos^{-1} z = \pi$.

This implies $x = -1$, $y = -1$, and $z = -1$.

Substituting these values into the expression $xy + yz + zx$:

$xy + yz + zx = (-1)(-1) + (-1)(-1) + (-1)(-1) = 1 + 1 + 1 = 3$.

Answer: $3$

</details>

---

### Q3. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\sum\limits_{k=1}^{2026} \sin^{-1}\left(\cos\dfrac{k\pi}{4}\right) =$

**Options:**

- **(A)** $-\dfrac{\pi}{4}$
- **(B)** $0$
- **(C)** $\dfrac{\pi}{4}$
- **(D)** $\dfrac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{\pi}{4}$**

**Detailed Solution:**

Let $f(k) = \sin^{-1}\left(\cos\dfrac{k\pi}{4}\right)$.

The function $\cos\dfrac{k\pi}{4}$ is periodic with a period of $8$.

Let us evaluate the sum of $f(k)$ over one complete period, from $k=1$ to $k=8$:

$f(1) = \sin^{-1}\left(\cos\dfrac{\pi}{4}\right) = \sin^{-1}\left(\dfrac{1}{\sqrt{2}}\right) = \dfrac{\pi}{4}$

$f(2) = \sin^{-1}\left(\cos\dfrac{2\pi}{4}\right) = \sin^{-1}(0) = 0$

$f(3) = \sin^{-1}\left(\cos\dfrac{3\pi}{4}\right) = \sin^{-1}\left(-\dfrac{1}{\sqrt{2}}\right) = -\dfrac{\pi}{4}$

$f(4) = \sin^{-1}\left(\cos\dfrac{4\pi}{4}\right) = \sin^{-1}(-1) = -\dfrac{\pi}{2}$

$f(5) = \sin^{-1}\left(\cos\dfrac{5\pi}{4}\right) = \sin^{-1}\left(-\dfrac{1}{\sqrt{2}}\right) = -\dfrac{\pi}{4}$

$f(6) = \sin^{-1}\left(\cos\dfrac{6\pi}{4}\right) = \sin^{-1}(0) = 0$

$f(7) = \sin^{-1}\left(\cos\dfrac{7\pi}{4}\right) = \sin^{-1}\left(\dfrac{1}{\sqrt{2}}\right) = \dfrac{\pi}{4}$

$f(8) = \sin^{-1}\left(\cos\dfrac{8\pi}{4}\right) = \sin^{-1}(1) = \dfrac{\pi}{2}$

Summing these values, we get:

$\sum\limits_{k=1}^{8} f(k) = \dfrac{\pi}{4} + 0 - \dfrac{\pi}{4} - \dfrac{\pi}{2} - \dfrac{\pi}{4} + 0 + \dfrac{\pi}{4} + \dfrac{\pi}{2} = 0$

Since the sum over any $8$ consecutive terms is $0$, we divide the total number of terms by $8$:

$2026 = 8 \times 253 + 2$

This means there are $253$ complete periods whose sum is $0$, leaving only the first $2$ terms of the next period.

$\sum\limits_{k=1}^{2026} f(k) = 253 \times 0 + f(1) + f(2)$

$\sum\limits_{k=1}^{2026} f(k) = \dfrac{\pi}{4} + 0 = \dfrac{\pi}{4}$

Answer: $\dfrac{\pi}{4}$

</details>

---

### Q4. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin^{-1}\left(\tan\dfrac{\pi}{4}\right) - \sin^{-1}\left(\sqrt{\dfrac{3}{x}}\right) = \dfrac{\pi}{6}$ then $x$ is a root of the equation

**Options:**

- **(A)** $x^2 - x - 6 = 0$
- **(B)** $x^2 - x - 12 = 0$
- **(C)** $x^2 + x - 12 = 0$
- **(D)** $x^2 + x - 6 = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^2 - x - 12 = 0$**

**Detailed Solution:**

Given equation is $\sin^{-1}\left(\tan\dfrac{\pi}{4}\right) - \sin^{-1}\left(\sqrt{\dfrac{3}{x}}\right) = \dfrac{\pi}{6}$

Since $\tan\dfrac{\pi}{4} = 1$, we have:

$\sin^{-1}(1) - \sin^{-1}\left(\sqrt{\dfrac{3}{x}}\right) = \dfrac{\pi}{6}$

$\dfrac{\pi}{2} - \sin^{-1}\left(\sqrt{\dfrac{3}{x}}\right) = \dfrac{\pi}{6}$

$\sin^{-1}\left(\sqrt{\dfrac{3}{x}}\right) = \dfrac{\pi}{2} - \dfrac{\pi}{6} = \dfrac{\pi}{3}$

$\sqrt{\dfrac{3}{x}} = \sin\left(\dfrac{\pi}{3}\right) = \dfrac{\sqrt{3}}{2}$

Squaring both sides, we get:

$\dfrac{3}{x} = \dfrac{3}{4}$

$x = 4$

Substituting $x = 4$ into the given options, we find that it satisfies the equation $x^2 - x - 12 = 0$ since $4^2 - 4 - 12 = 16 - 16 = 0$.

Answer: $x^2 - x - 12 = 0$

</details>

---

### Q5. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin^{-1}(x - 2) + \cos^{-1}(x) + \tan^{-1}(x + 2) + \cot^{-1}(x + 4) = \sec^{-1}(\sqrt{k}) - \dfrac{\pi}{2}$, then $\cos(2\,\text{cosec}^{-1}\sqrt{k - 1}) = \ldots$

**Options:**

- **(A)** $\dfrac{15}{16}$
- **(B)** $\dfrac{31}{32}$
- **(C)** $\dfrac{63}{64}$
- **(D)** $\dfrac{7}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{31}{32}$**

**Detailed Solution:**

For the equation to be defined, the arguments of the inverse trigonometric functions must lie within their respective domains.

For $\sin^{-1}(x - 2)$, we require $-1 \le x - 2 \le 1 \Rightarrow 1 \le x \le 3$.

For $\cos^{-1}(x)$, we require $-1 \le x \le 1$.

The intersection of these two domains is $x = 1$.

Substituting $x = 1$ into the given equation:

$\sin^{-1}(1 - 2) + \cos^{-1}(1) + \tan^{-1}(1 + 2) + \cot^{-1}(1 + 4) = \sec^{-1}(\sqrt{k}) - \dfrac{\pi}{2}$

$\sin^{-1}(-1) + \cos^{-1}(1) + \tan^{-1}(3) + \cot^{-1}(5) = \sec^{-1}(\sqrt{k}) - \dfrac{\pi}{2}$

$-\dfrac{\pi}{2} + 0 + \tan^{-1}(3) + \tan^{-1}\left(\dfrac{1}{5}\right) = \sec^{-1}(\sqrt{k}) - \dfrac{\pi}{2}$

$\tan^{-1}(3) + \tan^{-1}\left(\dfrac{1}{5}\right) = \sec^{-1}(\sqrt{k})$

Using the formula $\tan^{-1}x + \tan^{-1}y = \tan^{-1}\left(\dfrac{x + y}{1 - xy}\right)$ for $xy < 1$:

$\tan^{-1}\left(\dfrac{3 + \dfrac{1}{5}}{1 - 3 \times \dfrac{1}{5}}\right) = \sec^{-1}(\sqrt{k})$

$\tan^{-1}\left(\dfrac{16/5}{2/5}\right) = \sec^{-1}(\sqrt{k})$

$\tan^{-1}(8) = \sec^{-1}(\sqrt{k})$

Let $\theta = \tan^{-1}(8)$, then $\tan \theta = 8$.

$\sec \theta = \sqrt{1 + \tan^2 \theta} = \sqrt{1 + 64} = \sqrt{65}$.

Therefore, $\sec^{-1}(\sqrt{65}) = \sec^{-1}(\sqrt{k}) \Rightarrow k = 65$.

We need to find the value of $\cos(2\text{cosec}^{-1}\sqrt{k - 1})$:

$\cos(2\text{cosec}^{-1}\sqrt{65 - 1}) = \cos(2\text{cosec}^{-1}8)$

Let $\alpha = \text{cosec}^{-1}8$, then $\text{cosec} \alpha = 8 \Rightarrow \sin \alpha = \dfrac{1}{8}$.

Using the double angle formula $\cos(2\alpha) = 1 - 2\sin^2 \alpha$:

$\cos(2\alpha) = 1 - 2\left(\dfrac{1}{8}\right)^2 = 1 - 2\left(\dfrac{1}{64}\right) = 1 - \dfrac{1}{32} = \dfrac{31}{32}$.

Answer: $\dfrac{31}{32}$

</details>

---

### Q6. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\cos^{-1}\left(\cos\dfrac{4\pi}{3}\right) + \sin^{-1}\left(\sin\dfrac{4\pi}{3}\right) = \ldots$

**Options:**

- **(A)** $\dfrac{4\pi}{3}$
- **(B)** $\dfrac{8\pi}{3}$
- **(C)** $\dfrac{\pi}{3}$
- **(D)** $\dfrac{3\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{\pi}{3}$**

**Detailed Solution:**

The principal value branch of $\cos^{-1}x$ is $[0, \pi]$.

$\cos^{-1}\left(\cos\dfrac{4\pi}{3}\right) = \cos^{-1}\left(\cos\left(2\pi - \dfrac{2\pi}{3}\right)\right) = \cos^{-1}\left(\cos\dfrac{2\pi}{3}\right) = \dfrac{2\pi}{3}$

The principal value branch of $\sin^{-1}x$ is $\left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]$.

$\sin^{-1}\left(\sin\dfrac{4\pi}{3}\right) = \sin^{-1}\left(\sin\left(\pi + \dfrac{\pi}{3}\right)\right) = \sin^{-1}\left(-\sin\dfrac{\pi}{3}\right) = \sin^{-1}\left(\sin\left(-\dfrac{\pi}{3}\right)\right) = -\dfrac{\pi}{3}$

Adding the two values:

$\dfrac{2\pi}{3} - \dfrac{\pi}{3} = \dfrac{\pi}{3}$

Answer: $\dfrac{\pi}{3}$

</details>

---

### Q7. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\cot^{-1}\left[\dfrac{\sqrt{1 - \sin x} + \sqrt{1 + \sin x}}{\sqrt{1 - \sin x} - \sqrt{1 + \sin x}}\right]$, where $x \in \left(0, \dfrac{\pi}{2}\right)$ is...

**Options:**

- **(A)** $\pi - x$
- **(B)** $2\pi - x$
- **(C)** $\dfrac{\pi}{2} - \dfrac{x}{2}$
- **(D)** $\pi - \dfrac{x}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\pi - \dfrac{x}{2}$**

**Detailed Solution:**

We know that $1 \pm \sin x = \left(\cos \dfrac{x}{2} \pm \sin \dfrac{x}{2}\right)^2$.

Since $x \in \left(0, \dfrac{\pi}{2}\right)$, we have $\dfrac{x}{2} \in \left(0, \dfrac{\pi}{4}\right)$.

In this interval, $\cos \dfrac{x}{2} > \sin \dfrac{x}{2} > 0$.

Therefore, $\sqrt{1 - \sin x} = \cos \dfrac{x}{2} - \sin \dfrac{x}{2}$ and $\sqrt{1 + \sin x} = \cos \dfrac{x}{2} + \sin \dfrac{x}{2}$.

Substituting these values into the given expression:

$\dfrac{\sqrt{1 - \sin x} + \sqrt{1 + \sin x}}{\sqrt{1 - \sin x} - \sqrt{1 + \sin x}} = \dfrac{\left(\cos \dfrac{x}{2} - \sin \dfrac{x}{2}\right) + \left(\cos \dfrac{x}{2} + \sin \dfrac{x}{2}\right)}{\left(\cos \dfrac{x}{2} - \sin \dfrac{x}{2}\right) - \left(\cos \dfrac{x}{2} + \sin \dfrac{x}{2}\right)}$

$= \dfrac{2\cos \dfrac{x}{2}}{-2\sin \dfrac{x}{2}} = -\cot \dfrac{x}{2}$

The given expression becomes $\cot^{-1}\left(-\cot \dfrac{x}{2}\right)$.

Using the property $\cot^{-1}(-y) = \pi - \cot^{-1}y$:

$\cot^{-1}\left(-\cot \dfrac{x}{2}\right) = \pi - \cot^{-1}\left(\cot \dfrac{x}{2}\right)$

Since $\dfrac{x}{2} \in \left(0, \dfrac{\pi}{4}\right)$, $\cot^{-1}\left(\cot \dfrac{x}{2}\right) = \dfrac{x}{2}$.

Thus, the value is $\pi - \dfrac{x}{2}$.

Answer: $\pi - \dfrac{x}{2}$

</details>

---

### Q8. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\cos\left(\cos^{-1}\left(-\dfrac{1}{2}\right) + \dfrac{\pi}{3}\right) =$

**Options:**

- **(A)** $0$
- **(B)** $-1$
- **(C)** $1$
- **(D)** $\dfrac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-1$**

**Detailed Solution:**

The principal value branch of $\cos^{-1}(x)$ is $[0, \pi]$.

We know that $\cos\left(\dfrac{2\pi}{3}\right) = -\dfrac{1}{2}$.

Therefore, $\cos^{-1}\left(-\dfrac{1}{2}\right) = \dfrac{2\pi}{3}$.

Substituting this into the given expression:

$\cos\left(\cos^{-1}\left(-\dfrac{1}{2}\right) + \dfrac{\pi}{3}\right) = \cos\left(\dfrac{2\pi}{3} + \dfrac{\pi}{3}\right)$

$= \cos(\pi)$

$= -1$

Answer: $-1$

</details>

---

### Q9. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\tan^{-1}\left(\dfrac{\cos\left(\frac{19\pi}{4}\right) - 1}{\sin\left(\frac{\pi}{4}\right)}\right)$ is equal to

**Options:**

- **(A)** $-\dfrac{\pi}{4}$
- **(B)** $-\dfrac{5\pi}{12}$
- **(C)** $-\dfrac{3\pi}{8}$
- **(D)** $-\dfrac{4\pi}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\dfrac{3\pi}{8}$**

**Detailed Solution:**

$\cos\left(\dfrac{19\pi}{4}\right) = \cos\left(4\pi + \dfrac{3\pi}{4}\right) = \cos\left(\dfrac{3\pi}{4}\right) = -\dfrac{1}{\sqrt{2}}$

$\sin\left(\dfrac{\pi}{4}\right) = \dfrac{1}{\sqrt{2}}$

Substituting these values into the given expression:

$\tan^{-1}\left(\dfrac{-\dfrac{1}{\sqrt{2}} - 1}{\dfrac{1}{\sqrt{2}}}\right) = \tan^{-1}\left(\dfrac{-1 - \sqrt{2}}{1}\right) = \tan^{-1}(-(\sqrt{2} + 1))$

Using the property $\tan^{-1}(-x) = -\tan^{-1}(x)$:

$-\tan^{-1}(\sqrt{2} + 1)$

Since $\tan\left(\dfrac{3\pi}{8}\right) = \sqrt{2} + 1$, we get:

$-\tan^{-1}\left(\tan\left(\dfrac{3\pi}{8}\right)\right) = -\dfrac{3\pi}{8}$

Answer: $-\dfrac{3\pi}{8}$

</details>

---

### Q10. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\dfrac{\tan^{-1}(1) + \cos^{-1}\left(\dfrac{1}{2}\right) + \sin^{-1}\left(\dfrac{1}{2}\right)}{\tan^{-1}(\sqrt{3}) - \sec^{-1}(-2)}$ is equal to

**Options:**

- **(A)** $\dfrac{3}{4}$
- **(B)** $\dfrac{-1}{3}$
- **(C)** $-4$
- **(D)** $\dfrac{-9}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{-9}{4}$**

**Detailed Solution:**

The given expression is $\dfrac{\tan^{-1}(1) + \cos^{-1}\left(\dfrac{1}{2}\right) + \sin^{-1}\left(\dfrac{1}{2}\right)}{\tan^{-1}(\sqrt{3}) - \sec^{-1}(-2)}$

Evaluating the terms in the numerator:
$\tan^{-1}(1) = \dfrac{\pi}{4}$
Using the identity $\sin^{-1}(x) + \cos^{-1}(x) = \dfrac{\pi}{2}$, we have $\cos^{-1}\left(\dfrac{1}{2}\right) + \sin^{-1}\left(\dfrac{1}{2}\right) = \dfrac{\pi}{2}$
Numerator $= \dfrac{\pi}{4} + \dfrac{\pi}{2} = \dfrac{3\pi}{4}$

Evaluating the terms in the denominator:
$\tan^{-1}(\sqrt{3}) = \dfrac{\pi}{3}$
$\sec^{-1}(-2) = \pi - \sec^{-1}(2) = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$
Denominator $= \dfrac{\pi}{3} - \dfrac{2\pi}{3} = -\dfrac{\pi}{3}$

Substituting these values back into the expression:
$\dfrac{\dfrac{3\pi}{4}}{-\dfrac{\pi}{3}} = \dfrac{3\pi}{4} \times \left(-\dfrac{3}{\pi}\right) = -\dfrac{9}{4}$

Answer: $\dfrac{-9}{4}$

</details>

---

### Q11. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\tan^{-1}(\sqrt{3}) + \sec^{-1}(-2) - \sin^{-1}\left(-\dfrac{1}{2}\right)$ is

**Options:**

- **(A)** $\dfrac{5\pi}{6}$
- **(B)** $\dfrac{2\pi}{3}$
- **(C)** $\dfrac{7\pi}{6}$
- **(D)** $\dfrac{4\pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{7\pi}{6}$**

**Detailed Solution:**

The principal value of $\tan^{-1}(\sqrt{3})$ is $\dfrac{\pi}{3}$.

The principal value of $\sec^{-1}(-2)$ is $\pi - \sec^{-1}(2) = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$.

The principal value of $\sin^{-1}\left(-\dfrac{1}{2}\right)$ is $-\dfrac{\pi}{6}$.

Substituting these values into the given expression:

$\dfrac{\pi}{3} + \dfrac{2\pi}{3} - \left(-\dfrac{\pi}{6}\right)$

$= \pi + \dfrac{\pi}{6}$

$= \dfrac{7\pi}{6}$

Answer: $\dfrac{7\pi}{6}$

</details>

---

### Q12. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\cot ^{-1}\left(2 \cos \left(2 \operatorname{cosec}^{-1}(\sqrt{2})\right)\right)=\ldots$

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{\pi}{3}$
- **(C)** $\frac{\pi}{4}$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{2}$**

**Detailed Solution:**

Let $x = \operatorname{cosec}^{-1}(\sqrt{2})$.

$\operatorname{cosec} x = \sqrt{2} \Rightarrow x = \dfrac{\pi}{4}$

Substituting this in the given expression:

$\cot^{-1}\left(2 \cos \left(2 \times \dfrac{\pi}{4}\right)\right)$

$= \cot^{-1}\left(2 \cos \left(\dfrac{\pi}{2}\right)\right)$

Since $\cos \left(\dfrac{\pi}{2}\right) = 0$:

$= \cot^{-1}(2 \times 0)$

$= \cot^{-1}(0)$

Since $\cot \left(\dfrac{\pi}{2}\right) = 0$:

$= \dfrac{\pi}{2}$

Answer: $\frac{\pi}{2}$

</details>

---

### Q13. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\sin ^{-1}\left(-\frac{1}{\sqrt{2}}\right)+\cos ^{-1}\left(-\frac{1}{2}\right)-\cot ^{-1}\left(-\frac{1}{\sqrt{3}}\right)+\tan ^{-1}(+\sqrt{3})$

**Options:**

- **(A)** $\frac{\pi}{12}$
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{\pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{12}$**

**Detailed Solution:**

The principal value branches for the inverse trigonometric functions are:
$\sin^{-1} x \in \left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]$
$\cos^{-1} x \in [0, \pi]$
$\cot^{-1} x \in (0, \pi)$
$\tan^{-1} x \in \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$

Evaluating each term individually:
$\sin^{-1}\left(-\dfrac{1}{\sqrt{2}}\right) = -\dfrac{\pi}{4}$

$\cos^{-1}\left(-\dfrac{1}{2}\right) = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$

$\cot^{-1}\left(-\dfrac{1}{\sqrt{3}}\right) = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$

$\tan^{-1}(\sqrt{3}) = \dfrac{\pi}{3}$

Substituting these values into the given expression:
$\sin^{-1}\left(-\dfrac{1}{\sqrt{2}}\right) + \cos^{-1}\left(-\dfrac{1}{2}\right) - \cot^{-1}\left(-\dfrac{1}{\sqrt{3}}\right) + \tan^{-1}(\sqrt{3})$

$= -\dfrac{\pi}{4} + \dfrac{2\pi}{3} - \dfrac{2\pi}{3} + \dfrac{\pi}{3}$

$= -\dfrac{\pi}{4} + \dfrac{\pi}{3}$

$= \dfrac{-3\pi + 4\pi}{12}$

$= \dfrac{\pi}{12}$

Answer: $\frac{\pi}{12}$

</details>

---

### Q14. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\sin ^{-1}\left(\frac{x}{13}\right)+\operatorname{cosec}^{-1}\left(\frac{13}{12}\right)=\frac{\pi}{2}$, then the value of $x$ is

**Options:**

- **(A)** 4
- **(B)** 12
- **(C)** 5
- **(D)** 11

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 5**

**Detailed Solution:**

The given equation is $\sin^{-1}\left(\dfrac{x}{13}\right) + \operatorname{cosec}^{-1}\left(\dfrac{13}{12}\right) = \dfrac{\pi}{2}$

Using the property $\operatorname{cosec}^{-1}(y) = \sin^{-1}\left(\dfrac{1}{y}\right)$, we get:

$\sin^{-1}\left(\dfrac{x}{13}\right) + \sin^{-1}\left(\dfrac{12}{13}\right) = \dfrac{\pi}{2}$

$\sin^{-1}\left(\dfrac{x}{13}\right) = \dfrac{\pi}{2} - \sin^{-1}\left(\dfrac{12}{13}\right)$

Using the identity $\sin^{-1}(y) + \cos^{-1}(y) = \dfrac{\pi}{2}$, we have:

$\sin^{-1}\left(\dfrac{x}{13}\right) = \cos^{-1}\left(\dfrac{12}{13}\right)$

Let $\cos^{-1}\left(\dfrac{12}{13}\right) = \theta \Rightarrow \cos \theta = \dfrac{12}{13}$

Then $\sin \theta = \sqrt{1 - \cos^2 \theta} = \sqrt{1 - \left(\dfrac{12}{13}\right)^2} = \sqrt{\dfrac{169 - 144}{169}} = \dfrac{5}{13}$

Therefore, $\theta = \sin^{-1}\left(\dfrac{5}{13}\right)$

Substituting this back, we get:

$\sin^{-1}\left(\dfrac{x}{13}\right) = \sin^{-1}\left(\dfrac{5}{13}\right)$

Comparing both sides, we get:

$\dfrac{x}{13} = \dfrac{5}{13} \Rightarrow x = 5$

Answer: 5

</details>

---

### Q15. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Considering only the Principal values of inverse functions, the set
$A=\left\{x \geq 0 \left\lvert\, \tan ^{-1}(2 x)+\tan ^{-1}(3 x)=\dfrac{\pi}{4}\right.\right\}$

**Options:**

- **(A)** contains two elements.
- **(B)** contains more than two elements.
- **(C)** is an empty set.
- **(D)** is a singleton set.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) is a singleton set.**

**Detailed Solution:**

Given $\tan^{-1}(2x) + \tan^{-1}(3x) = \dfrac{\pi}{4}$ and $x \geq 0$.

Taking tangent on both sides, we get:

$\dfrac{2x + 3x}{1 - (2x)(3x)} = \tan\left(\dfrac{\pi}{4}\right)$

$\dfrac{5x}{1 - 6x^2} = 1$

$5x = 1 - 6x^2$

$6x^2 + 5x - 1 = 0$

$(6x - 1)(x + 1) = 0$

$x = \dfrac{1}{6}$ or $x = -1$

Since $x \geq 0$, we have $x = \dfrac{1}{6}$.

For $x = \dfrac{1}{6}$, $2x \times 3x = 6x^2 = \dfrac{1}{6} < 1$, which satisfies the condition for the formula $\tan^{-1}A + \tan^{-1}B = \tan^{-1}\left(\dfrac{A+B}{1-AB}\right)$.

Thus, the set $A$ contains exactly one element.

Therefore, $A$ is a singleton set.

Answer: is a singleton set.

</details>

---

### Q16. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Considering only the principal values of inverse function, the set $A=\left\{x \geq 0, \tan ^{-1}(2 x)+\tan ^{-1}(3 x)=\dfrac{\pi}{4}\right\}$

**Options:**

- **(A)** is an empty set.
- **(B)** is a singleton set.
- **(C)** contains more than two elements.
- **(D)** contains two elements.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) is a singleton set.**

**Detailed Solution:**

Given equation:

$\tan^{-1}(2x) + \tan^{-1}(3x) = \dfrac{\pi}{4}$ with $x \ge 0$

Using the identity $\tan^{-1}a + \tan^{-1}b = \tan^{-1}\left(\dfrac{a+b}{1-ab}\right)$ for $ab < 1$:

$\tan^{-1}\left(\dfrac{2x + 3x}{1 - (2x)(3x)}\right) = \dfrac{\pi}{4}$

$\dfrac{5x}{1 - 6x^2} = \tan\left(\dfrac{\pi}{4}\right)$

$\dfrac{5x}{1 - 6x^2} = 1$

$5x = 1 - 6x^2$

$6x^2 + 5x - 1 = 0$

$(6x - 1)(x + 1) = 0$

This gives $x = \dfrac{1}{6}$ or $x = -1$

Since it is given that $x \ge 0$, we reject $x = -1$.

For $x = \dfrac{1}{6}$, the product of arguments is $(2x)(3x) = 6\left(\dfrac{1}{6}\right)^2 = \dfrac{1}{6} < 1$, which is valid.

Thus, $x = \dfrac{1}{6}$ is the only solution.

The set $A = \left\{\dfrac{1}{6}\right\}$, which contains exactly one element.

Therefore, set $A$ is a singleton set.

</details>

---

### Q17. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\cos ^{-1} x+\cos ^{-1} y+\cos ^{-1} z=3 \pi$, then the value of $x^{2025}+x^{2026}+x^{2027}$ is

**Options:**

- **(A)** $-1$
- **(B)** $0$
- **(C)** $1$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-1$**

**Detailed Solution:**

$\begin{aligned} & \cos ^{-1} x+\cos ^{-1} y+\cos ^{-1} z=3 \pi \\ & \text { Since } 0 \leq \cos ^{-1} x \leq \pi \\ & \\ & 0 \leq \cos ^{-1} y \leq \pi \text { and } 0 \leq \cos ^{-1} z \leq \pi \\ & \\ & \text { Here, } \cos ^{-1} x=\cos ^{-1} y=\cos ^{-1} z=\pi \\ & \Rightarrow x=y=z=\cos \pi=-1 \\ & \therefore \quad x^{2005}+x^{2026}+x^{2027} \\ & =(-1)^{2025}+(-1)^{2026}+(-1)^{2027} \\ & =-1+1-1 \\ & =-1\end{aligned}$

</details>

---

### Q18. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The principal value of $\sin ^{-1}\left(\sin \frac{3 \pi}{4}\right)$ is

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{3 \pi}{4}$
- **(C)** $\frac{-\pi}{4}$
- **(D)** $\frac{5 \pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{4}$**

**Detailed Solution:**

$\begin{aligned} \sin ^{-1}\left(\sin \frac{3 \pi}{4}\right) & =\sin ^{-1}\left[\sin \left(\pi-\frac{\pi}{4}\right)\right] \\ & =\sin ^{-1}\left(\sin \frac{\pi}{4}\right) \\ & =\frac{\pi}{4}\end{aligned}$

</details>

---

### Q19. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\sin \left(\cot ^{-1} x\right)$ is

**Options:**

- **(A)** $\frac{1}{\sqrt{1+x^2}}$
- **(B)** $\sqrt{1+x^2}$
- **(C)** $\frac{1}{x \sqrt{1+x^2}}$
- **(D)** $x \sqrt{1+x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{\sqrt{1+x^2}}$**

**Detailed Solution:**

$\begin{array}{ll} & \sin \left(\cot ^{-1} x\right) \\ & \text { Let } \cot ^{-1} x=\mathrm{t} \\ \therefore \quad & x=\cot \mathrm{t} \\ \therefore \quad & 1+\cot ^2 \mathrm{t}=1+x^2 \\ \therefore \quad & \operatorname{cosec}^2 \mathrm{t}=1+x^2 \\ \therefore \quad & \operatorname{cosec} \mathrm{t}=\sqrt{1+x^2} \\ \therefore \quad & \sin \mathrm{t}=\frac{1}{\sqrt{1+x^2}} \\ \therefore \quad & \mathrm{t}=\sin ^{-1}\left(\frac{1}{\sqrt{1+x^2}}\right) \\ \therefore \quad & \sin \left(\cot ^{-1} x\right)=\sin \left(\sin ^{-1}\left(\frac{1}{\sqrt{1+x^2}}\right)\right) \\ & =\frac{1}{\sqrt{1+x^2}}\end{array}$

</details>

---

### Q20. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\alpha=3 \sin ^{-1} \frac{6}{11}$ and $\beta=3 \cos ^{-1}\left(\frac{4}{9}\right)$, where the inverse trigonometric functions take only the principal values, then the incorrect option is

**Options:**

- **(A)** $\cos \beta>0$
- **(B)** $\sin \beta < 0$
- **(C)** $\cos (\alpha+\beta)>0$
- **(D)** $\cos \alpha < 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\cos \beta>0$**

**Detailed Solution:**

$\alpha=3 \sin ^{-1} \frac{6}{11}$ and $\beta=3 \cos ^{-1}\left(\frac{4}{9}\right)$
Since $\frac{6}{11}>\frac{6}{12}$
Taking $\sin ^{-1}$ on both sides, we get
$$
\sin ^{-1}\left(\frac{6}{11}\right)>\sin ^{-1}\left(\frac{6}{12}\right)
$$
$\ldots\left[\because \sin ^{-1} x\right.$ is an increasing function $]$
$\Rightarrow 3 \sin ^{-1}\left(\frac{6}{11}\right)>3 \sin ^{-1}\left(\frac{1}{2}\right)$
$\Rightarrow \alpha>3\left(\frac{\pi}{6}\right)$
$\Rightarrow \alpha>\frac{\pi}{2}$
Now, $\frac{4}{9} < \frac{4}{8}$
Taking $\cos ^{-1}$ on both sides, we get $\cos ^{-1}\left(\frac{4}{9}\right)>\cos ^{-1}\left(\frac{4}{8}\right)$
$\ldots\left[\because \cos ^{-1} x\right.$ is a decreasing function $]$
$\Rightarrow 3 \cos ^{-1}\left(\frac{4}{9}\right)>3 \cos ^{-1}\left(\frac{1}{2}\right)$
$\Rightarrow \beta>3\left(\frac{\pi}{3}\right)$
$\Rightarrow \beta>\pi$
From (i) and (ii), we have $\alpha$ lies in II $^{\text {nd }}$ quadrant and $\beta$ lies in III $^{\text {rd }}$ quadrant.
$$
\therefore \quad \cos \alpha < 0, \cos \beta < 0 \text { and } \sin \beta < 0
$$

Also, $\alpha+\beta>\frac{\pi}{2}+\pi$
....[From (i) and (ii)]
$$
\therefore \quad \alpha+\beta>\frac{3 \pi}{2}
$$

Thus, $\alpha+\beta$ lies in IV $^{\text {th }}$ quadrant.
So, $\cos (\alpha+\beta)>0$
[Note: Options (B), (C) and (D) are correct.]

</details>

---

### Q21. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\tan ^{-1} a+\tan ^{-1} b+\tan ^{-1} c=\pi$, then which of the following statement is true?

**Options:**

- **(A)** $a+b-c=a b c$
- **(B)** $a+b+c=2 a b c$
- **(C)** $a b c=1$
- **(D)** $a+b+c=a b c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $a+b+c=a b c$**

**Detailed Solution:**

$\begin{aligned} & \tan ^{-1} a+\tan ^{-1} b+\tan ^{-1} c=\pi \\ & \Rightarrow \tan ^{-1}\left(\frac{a+b+c-a b c}{1-a b-b c-c a}\right)=\pi \\ & \Rightarrow \frac{a+b+c-a b c}{1-a b-b c-c a}=\tan \pi=0 \\ & \Rightarrow a+b+c-a b c=0 \\ & \Rightarrow a+b+c=a b c\end{aligned}$

</details>

---

### Q22. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\tan ^{-1}\left(\frac{\sqrt{1+x^2}+\sqrt{1-x^2}}{\sqrt{1+x^2}-\sqrt{1-x^2}}\right)$, $|x| < \frac{1}{2}, x \neq 0$

**Options:**

- **(A)** $\frac{\pi}{4}+\frac{1}{2} \cos ^{-1} x^2$
- **(B)** $\frac{\pi}{4}+\cos ^{-1} x^2$
- **(C)** $\frac{\pi}{4}-\frac{1}{2} \cos ^{-1} x^2$
- **(D)** $\frac{\pi}{4}-\cos ^{-1} x^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{4}+\frac{1}{2} \cos ^{-1} x^2$**

**Detailed Solution:**

Let $\mathrm{T}=\tan ^{-1}\left(\frac{\sqrt{1+x^2}+\sqrt{1-x^2}}{\sqrt{1+x^2}-\sqrt{1-x^2}}\right)$
Put $x^2=\cos 2 \theta \Rightarrow \theta=\frac{1}{2} \cos ^{-1} x^2$
$\begin{aligned}
\therefore \quad \mathrm{T} & =\tan ^{-1}\left(\frac{\sqrt{1+\cos 2 \theta}+\sqrt{1-\cos 2 \theta}}{\sqrt{1+\cos 2 \theta}-\sqrt{1-\cos 2 \theta}}\right) \\
& =\tan ^{-1}\left(\frac{\sqrt{2} \cos \theta+\sqrt{2} \sin \theta}{\sqrt{2} \cos \theta-\sqrt{2} \sin \theta}\right) \\
& =\tan ^{-1}\left(\frac{\cos \theta+\sin \theta}{\cos \theta-\sin \theta}\right) \\
& =\tan ^{-1}\left(\frac{1+\tan \theta}{1-\tan \theta}\right) \\
& =\tan ^{-1}\left(\tan \left(\frac{\pi}{4}+\theta\right)\right) \\
& =\frac{\pi}{4}+\theta \\
& =\frac{\pi}{4}+\frac{1}{2} \cos ^{-1} x^2
\end{aligned}$

</details>

---

### Q23. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of $\tan \left\{\frac{1}{2} \sin ^{-1}\left(\frac{2 x}{1+x^2}\right)+\frac{1}{2} \cos ^{-1}\left(\frac{1-y^2}{1+y^2}\right)\right\}$ is

**Options:**

- **(A)** $\frac{x+y}{1-x y}$
- **(B)** $\frac{x-y}{1+x y}$
- **(C)** $\frac{x-y}{1-x y}$
- **(D)** $\frac{x+y}{1+x y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{x+y}{1-x y}$**

**Detailed Solution:**

Let $x=\tan \theta$ and $y=\tan \phi$
$\begin{aligned}
& \Rightarrow \tan \left\{\frac{1}{2} \sin ^{-1} \sin 2 \theta+\frac{1}{2} \cos ^{-1} \cos 2 \phi\right\} \\
& =\tan (\theta+\phi) \\
& =\frac{\tan \theta+\tan \phi}{1-\tan \theta \cdot \tan \phi}=\frac{x+y}{1-x y}
\end{aligned}$

</details>

---

### Q24. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The principal value of $\cot ^{-1}\left(\frac{-1}{\sqrt{3}}\right)$ is

**Options:**

- **(A)** $\frac{2 \pi}{3}$
- **(B)** $\frac{\pi}{3}$
- **(C)** $\frac{-\pi}{3}$
- **(D)** $\frac{\pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2 \pi}{3}$**

**Detailed Solution:**

$\cot ^{-1}\left(\frac{-1}{\sqrt{3}}\right)=\pi-\cot ^{-1}\left(\frac{1}{\sqrt{3}}\right)=\pi-\frac{\pi}{3}=\frac{2 \pi}{3}$

</details>

---

### Q25. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\tan ^{-1} \sqrt{x^2+x}+\sin ^{-1} \sqrt{x^2+x+1}=\frac{\pi}{2}$, then the value of $x$ is

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $-\frac{1}{2}$
- **(C)** 1
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Ot2yPGxlvtZh5A3dT61ofFUqu-nHIzx0KwRnQWWospE.original.fullsize.png">

$\begin{aligned} & \tan ^{-1} \sqrt{x^2+x}+\sin ^{-1} \sqrt{x^2+x+1}=\frac{\pi}{2} \\ & \Rightarrow \tan ^{-1} \sqrt{x^2+x}=\frac{\pi}{2}-\sin ^{-1} \sqrt{x^2+x+1}=\cos ^{-1} \sqrt{x^2+x+1} \\ & \Rightarrow \tan ^{-1} \sqrt{x^2+x}=\tan ^{-1} \frac{\sqrt{-\left(x^2+x\right)}}{\sqrt{x^2+x+1}} ; \sqrt{-\left(x^2+x\right)} \\ & \Rightarrow x^2+x=\frac{-\left(x^2+x\right)}{x^2+x+1} \\ & \Rightarrow\left(x^2+x\right)\left(x^2+x+1\right)=-\left(x^2+x\right)\left[\text { let } x^2+x=y\right] \\ & \Rightarrow y(y+1)=-y \\ & \Rightarrow y^2+2 y=0 \\ & \Rightarrow y(y+2)=0 \\ & \Rightarrow y=0 \text { or } y=-2 \\ & \Rightarrow x^2+x=0 \text { or } x^2+x=-2 \\ & \Rightarrow x(x+1)=0 \text { or } x^2+x+2=0 \\ & \Rightarrow(x=0,-1) \text { or } \text { (No solution) }\end{aligned}$

</details>

---

### Q26. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\sin \left(2 \sin ^{-1} 0.8\right)$ is equal to

**Options:**

- **(A)** $0.48$
- **(B)** $0.16$
- **(C)** $0.96$
- **(D)** $0.12$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.96$**

**Detailed Solution:**

$\begin{aligned} & \sin \left(2 \sin ^{-1} 0.8\right)=\sin \left[\sin ^{-1}\left\{2 \times 0.8 \sqrt{1-(0.8)^2}\right\}\right] \\ & =\sin \left\{\sin ^{-1}\{2 \times 0.8 \sqrt{1-0.64}\}\right\} \\ & =\sin \left\{\sin ^{-1}\{2 \times 0.8 \sqrt{0.36}\}\right\} \\ & =\sin \left\{\sin ^{-1}\{2 \times 0.8 \times 0.6\}\right\} \\ & =\sin \left(\sin ^{-1}(0.96)\right) \\ & =0.96\end{aligned}$

</details>

---

### Q27. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The principal value of $\sin ^{-1}\left(\sin \left(\frac{2 \pi}{3}\right)\right)$ is

**Options:**

- **(A)** $-\left(\frac{2 \pi}{3}\right)$
- **(B)** $\left(\frac{5 \pi}{3}\right)$
- **(C)** $\left(\frac{\pi}{3}\right)$
- **(D)** $\left(\frac{2 \pi}{3}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(\frac{\pi}{3}\right)$**

**Detailed Solution:**

$\sin ^{-1}\left(\sin \left(\frac{2 \pi}{3}\right)\right)=\sin ^{-1}\left(\sin \left(\pi-\frac{2 \pi}{3}\right)\right)=\sin ^{-1}\left(\sin \left(\frac{\pi}{3}\right)\right)=\frac{\pi}{3}$

</details>

---

### Q28. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Considering only the Principal values of inverse function, the set
$$
\left\{x \geq 0 / \tan ^{-1}(2 x)+\tan ^{-1} 3 x=\frac{\pi}{4}\right\}
$$

**Options:**

- **(A)** is a singleton set.
- **(B)** contains more than two elements.
- **(C)** contains two elements.
- **(D)** is an empty set.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) is a singleton set.**

**Detailed Solution:**

$\begin{aligned} & \tan ^{-1}(2 x)+\tan ^{-1}(3 x)=\frac{\pi}{4} \\ & \Rightarrow \tan ^{-1} \frac{2 x+3 x}{1-2 x \times 3 x}=\tan ^{-1}(1) \\ & \Rightarrow \frac{5 x}{1-6 x^2}=1 \\ & \Rightarrow 5 x=1-6 x^2 \\ & \Rightarrow 6 x^2+5 x-1=0 \\ & \Rightarrow(x+1)(6 x-1)=0\end{aligned}$
$\Rightarrow x=-1$ or $x=\frac{1}{6}$
But $x \geq 0$
Hence $x=\frac{1}{6}$ (only) i.e., single ton set

</details>

---

### Q29. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\sin ^{-1}\left(\frac{-1}{2}\right)+\sin ^{-1}\left(\frac{-\sqrt{3}}{2}\right)$ is

**Options:**

- **(A)** $\frac{\pi}{3}$
- **(B)** $\frac{-\pi}{6}$
- **(C)** $\frac{-\pi}{3}$
- **(D)** $\frac{-\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{-\pi}{2}$**

**Detailed Solution:**

$\sin ^{-1}\left(\frac{-1}{2}\right)+\sin ^{-1}\left(\frac{-\sqrt{3}}{2}\right)=\frac{-\pi}{3}-\frac{\pi}{6}=\frac{-\pi}{2}$

</details>

---

### Q30. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\tan ^{-1}\left(\tan \frac{5 \pi}{6}\right)+\cos ^{-1}\left(\cos \frac{13 \pi}{6}\right)=$

**Options:**

- **(A)** 0
- **(B)** $3 \pi$
- **(C)** $\frac{-\pi}{6}$
- **(D)** $\frac{\pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

$\begin{aligned} & \tan ^{-1}\left(\tan \frac{5 \pi}{6}\right)+\cos ^{-1}\left(\cos \frac{13 \pi}{6}\right) \\ & =\tan ^{-1}\left[\tan \left(\pi-\frac{\pi}{6}\right)\right]+\cos ^{-1}\left[\cos \left(2 \pi+\frac{\pi}{6}\right)\right] \\ & =\tan ^{-1}\left[-\tan \frac{\pi}{6}\right]+\cos ^{-1}\left[\cos \left(\frac{\pi}{6}\right)\right] \\ & =\tan ^{-1}\left[\tan \left(-\frac{\pi}{6}\right)\right]+\cos ^{-1}\left[\cos \left(\frac{\pi}{6}\right)\right]=-\frac{\pi}{6}+\frac{\pi}{6}=0\end{aligned}$

</details>

---

### Q31. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin ^{-1}\left(\frac{3}{5}\right)+\cos ^{-1}\left(\frac{12}{13}\right)=\sin ^{-1} \alpha$, then $\alpha=$

**Options:**

- **(A)** $\frac{56}{65}$
- **(B)** $\frac{61}{65}$
- **(C)** $\frac{63}{65}$
- **(D)** $\frac{62}{65}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{56}{65}$**

**Detailed Solution:**

We have $\sin ^{-1}\left(\frac{3}{5}\right)+\cos ^{-1}\left(\frac{12}{13}\right)=\sin ^{-1} \alpha$
$$
\begin{aligned}
& \therefore \tan ^{-1}\left(\frac{3}{4}\right)+\tan ^{-1}\left(\frac{5}{12}\right)=\tan ^{-1}\left(\frac{\alpha}{\sqrt{1-\alpha^2}}\right) \\
& \therefore \tan ^{-1}\left[\frac{\left(\frac{3}{4}\right)+\left(\frac{5}{12}\right)}{1-\left(\frac{3}{4}\right)\left(\frac{5}{12}\right)}\right]=\tan ^{-1}\left(\frac{\alpha}{\sqrt{1-\alpha^2}}\right) \\
& \therefore \tan ^{-1}\left[\frac{\left(\frac{14}{12}\right)}{\left(\frac{11}{16}\right)}\right]=\tan ^{-1}\left(\frac{\alpha}{\sqrt{1-\alpha^2}}\right) \\
& \therefore \frac{56}{33}=\frac{\alpha}{\sqrt{1-\alpha^2}} \Rightarrow(56)^2(1-\alpha)^2=(33)^2 \alpha^2 \\
& \alpha^2=\frac{(56)^2}{(56)^2+(33)^2}=\frac{(56)^2}{(65)^2} \Rightarrow \alpha=\frac{56}{65}
\end{aligned}
$$

</details>

---

### Q32. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan ^{-1}\left(\frac{x-1}{x-2}\right)+\tan ^{-1}\left(\frac{x+1}{x+2}\right)=\frac{\pi}{4}$, then the values of $x$ are

**Options:**

- **(A)** $\pm \frac{3}{\sqrt{2}}$
- **(B)** $\pm \frac{1}{2}$
- **(C)** $\pm \frac{1}{\sqrt{2}}$
- **(D)** $\pm \frac{\sqrt{3}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\pm \frac{1}{\sqrt{2}}$**

**Detailed Solution:**

$$
\begin{aligned}
& \tan ^{-1}\left(\frac{x-1}{x+2}\right)+\tan ^{-1}\left(\frac{x+1}{x+2}\right)=\frac{\pi}{4} \\
& \therefore \tan ^{-1}\left[\frac{\left(\frac{x-1}{x-2}\right)+\left(\frac{x+1}{x+2}\right)}{1-\left(\frac{x-1}{x-2}\right)+\left(\frac{x+1}{x+2}\right)}\right]=\frac{\pi}{4} \\
& \therefore \frac{(x-1)(x+2)+(x+1)(x-2)}{(x-2)(x+2)-(x-1)(x+1)}=\tan \frac{\pi}{4} \\
& \therefore \frac{\left(x^2+x-2\right)+\left(x^2-x-2\right)}{\left(x^2-4\right)-\left(x^2-1\right)}=1 \\
& \therefore 2 x^2-4=-3 \Rightarrow 2 x^2=1
\end{aligned}
$$
$\Rightarrow \mathrm{x}= \pm \frac{1}{\sqrt{2}}$

</details>

---

### Q33. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$$
\cos ^{-1}\left(\frac{4}{5}\right)+\cos ^{-1}\left(\frac{12}{13}\right)=
$$

**Options:**

- **(A)** $\cos ^{-1}\left(\frac{24}{25}\right)$
- **(B)** $\cos ^{-1}\left(\frac{33}{65}\right)$
- **(C)** $\cos ^{-1}\left(\frac{5}{13}\right)$
- **(D)** $\cos ^{-1}\left(\frac{3}{5}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\cos ^{-1}\left(\frac{33}{65}\right)$**

**Detailed Solution:**

$$
\begin{aligned}
& \cos ^{-1}\left(\frac{4}{5}\right)+\cos ^{-1}\left(\frac{12}{13}\right) \\
& =\tan ^{-1}\left(\frac{3}{4}\right)+\tan ^{-1}\left(\frac{5}{12}\right) \\
& =\tan ^{-1}\left[\frac{\left(\frac{3}{4}\right)+\left(\frac{5}{12}\right)}{1-\left(\frac{3}{12}\right)\left(\frac{5}{12}\right)}\right] \\
& =\tan ^{-1}\left(\frac{36+20}{48-15}\right)=\tan ^{-1}\left(\frac{56}{13}\right)=\cos ^{-1}\left(\frac{33}{65}\right)
\end{aligned}
$$

</details>

---

### Q34. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\sin ^{-1}\left(-\frac{1}{2}\right)+\cos ^{-1}\left(-\frac{\sqrt{3}}{2}\right)$ is

**Options:**

- **(A)** $\cos ^{-1}\left(\frac{1}{2}\right)$
- **(B)** $\sin ^{-1}\left(-\frac{1}{2}\right)$
- **(C)** $\cos ^{-1}\left(-\frac{1}{2}\right)$
- **(D)** $\cos ^{-1}\left(-\frac{\sqrt{3}}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\cos ^{-1}\left(-\frac{1}{2}\right)$**

**Detailed Solution:**

(D)
Let $\sin ^{-1}\left(\frac{-1}{2}\right)=\alpha$, where $\frac{-\pi}{2} \leq \alpha \leq \frac{\pi}{2}$
$\sin \alpha=\frac{-1}{2}=-\sin \frac{\pi}{6}=\sin \left(\frac{-\pi}{6}\right) \Rightarrow \alpha=-\pi / 6$
Let $\cos ^{-1}\left(\frac{-\sqrt{3}}{2}\right)=\beta$, where $0 \leq \beta \leq \pi$
$\cos \beta=\frac{-\sqrt{3}}{2}=\frac{-\cos \pi}{6} \Rightarrow \cos \left(\pi-\frac{\pi}{6}\right)=\frac{\cos 5 \pi}{6} \Rightarrow \beta=\frac{5 \pi}{6}$
$\therefore \sin ^{-1}\left(\frac{-1}{2}\right)+\cos ^{-1}\left(\frac{-\sqrt{3}}{2}\right)=\frac{-\pi}{6}+\frac{5 \pi}{6} \quad=\frac{4 \pi}{6}=\frac{2 \pi}{3}=\cos ^{-1}\left(\frac{-1}{2}\right)$

</details>

---

### Q35. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The principal value of $\sin ^{-1}\left(-\frac{1}{2}\right)$ is

**Options:**

- **(A)** $\frac{\pi}{3}$
- **(B)** $\frac{\pi}{6}$
- **(C)** $-\frac{\pi}{3}$
- **(D)** $-\frac{\pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\frac{\pi}{6}$**

**Detailed Solution:**

$\sin ^{-1}\left(-\frac{1}{2}\right)=-\sin ^{-1} \frac{1}{2}=\frac{-\pi}{6}$

</details>

---

### Q36. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\sin ^{-1}\left(\frac{1}{2}\right)+\cos ^{-1}\left(\frac{\sqrt{3}}{2}\right)+\cot ^{-1}\left(-\frac{1}{\sqrt{3}}\right)=$

**Options:**

- **(A)** $\frac{2 \pi}{3}$
- **(B)** $\mathrm{\pi}$
- **(C)** $\frac{\pi}{6}$
- **(D)** $\frac{\pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{\pi}$**

**Detailed Solution:**

$\sin ^{-1}\left(\frac{1}{2}\right)+\cos ^{-1}\left(\frac{\sqrt{3}}{2}\right)+\cot ^{-1}\left(\frac{-1}{\sqrt{3}}\right)$
$=30^{\circ}+30^{\circ}+120^{\circ}$
$=\pi$

</details>

---

### Q37. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of <math><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>7</mn></mrow></mfrac><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></mrow></mrow></mrow></mrow></mrow></mrow></mrow></mrow></math> is ________

**Options:**

- **(A)** <math><mfrac><mrow><mn>11</mn><mi>π</mi></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(C)** <math><mi>π</mi></math>
- **(D)** <math><mfrac><mrow><mn>3</mn><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

Let <math><mi>L</mi><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mn>1</mn></mrow><mrow><mn>7</mn></mrow></mfrac><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>  
<math><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>.</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfrac></mrow></mfenced><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>7</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>7</mn></mrow></mfrac><mo>.</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></mrow></mfrac></mrow></mfenced></math>  
<math><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>8</mn></mrow><mrow><mn>14</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>15</mn></mrow><mrow><mn>55</mn></mrow></mfrac></mrow></mfenced></math>  
<math><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>7</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>11</mn></mrow></mfrac></mrow></mfenced></math>  
<math><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>7</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>11</mn></mrow></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>7</mn></mrow></mfrac><mo>.</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>11</mn></mrow></mfrac></mrow></mfrac></mrow></mfenced><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>44</mn><mo>+</mo><mn>21</mn></mrow><mrow><mn>77</mn><mo>-</mo><mn>12</mn></mrow></mfrac></mrow></mfenced></math>  
<math><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>65</mn></mrow><mrow><mn>65</mn></mrow></mfrac></mrow></mfenced></math>  
<math><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>

</details>

---

### Q38. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mn>4</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><mn>6</mn><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>=</mo><mn>3</mn><mi>π</mi></math> then x = …..

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** 0
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

We have, <math><mn>4</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><mn>6</mn><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>=</mo><mn>3</mn><mi>π</mi></math>  
<math><mo>&#8658;</mo><mn>4</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><mn>6</mn><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mn>3</mn><mi>π</mi></math>  
<math><mo>&#8658;</mo><mn>4</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><mn>3</mn><mi>π</mi><mo>-</mo><mn>6</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>=</mo><mn>3</mn><mi>π</mi></math>  
<math><mo>&#8658;</mo><mo>-</mo><mn>2</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>=</mo><mn>0</mn></math>  
<math><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math>

</details>

---

### Q39. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `2`

If <math><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mn>3</mn><mi>x</mi><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mrow></mrow></mrow></math> , then <math><mi>x</mi><mo>=</mo><mi mathvariant="normal"> </mi></math>

**Options:**

- **(A)** <math><mo>-</mo><mn>1</mn></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math> <mrow> <msup> <mrow> <mi>tan</mi></mrow> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> <mn>2</mn><mi>x</mi><mo>+</mo><msup> <mrow> <mi>tan</mi></mrow> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> <mn>3</mn><mi>x</mi><mo>=</mo><mfrac> <mi>π</mi> <mn>4</mn> </mfrac> </mrow> <math> </math></math>
<math> <mrow> <msup> <mrow> <mi>tan</mi></mrow> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> <mrow><mo>(</mo> <mrow> <mfrac> <mrow> <mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>x</mi></mrow> <mrow> <mn>1</mn><mo>−</mo><mn>6</mn><msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> <mo>)</mo></mrow><mo>=</mo><mfrac> <mi>π</mi> <mn>4</mn> </mfrac> <mo>;</mo><mtext> </mtext><mtext> </mtext><mi>x</mi><mo>&gt;</mo><mn>0</mn></mrow> </math>
<math> <mrow> <mfrac> <mrow> <mn>5</mn><mi>x</mi></mrow> <mrow> <mn>1</mn><mo>−</mo><mn>6</mn><msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> <mo>=</mo><mn>1</mn></mrow> </math>
<math> <mrow> <mn>5</mn><mi>x</mi><mo>=</mo><mn>1</mn><mo>−</mo><mn>6</mn><msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </math>
<math> <mrow> <mn>6</mn><msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>5</mn><mi>x</mi><mo>−</mo><mn>1</mn><mo>=</mo><mn>0</mn></mrow> </math>
<math> <mrow> <mn>6</mn><msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>6</mn><mi>x</mi><mo>−</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo>=</mo><mn>0</mn></mrow> </math>
<math> <mrow> <mn>6</mn><mi>x</mi><mrow><mo>(</mo> <mrow> <mi>x</mi><mo>+</mo><mn>1</mn></mrow> <mo>)</mo></mrow><mo>−</mo><mn>1</mn><mrow><mo>(</mo> <mrow> <mi>x</mi><mo>+</mo><mn>1</mn></mrow> <mo>)</mo></mrow><mo>=</mo><mn>0</mn></mrow> </math>
<math> <mrow> <mrow><mo>(</mo> <mrow> <mn>6</mn><mi>x</mi><mo>−</mo><mn>1</mn></mrow> <mo>)</mo></mrow><mrow><mo>(</mo> <mrow> <mi>x</mi><mo>+</mo><mn>1</mn></mrow> <mo>)</mo></mrow><mo>=</mo><mn>0</mn></mrow> </math>
<math> <mrow> <mi>x</mi><mo>≠</mo><mo>−</mo><mn>1</mn><mo>;</mo><mtext> </mtext><mi>x</mi><mo>=</mo><mfrac> <mn>1</mn> <mn>6</mn> </mfrac> </mrow> </math>

</details>

---

### Q40. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

The value of <math><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></mrow></mfenced><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></mrow></mfenced></mrow></mrow></mrow></mrow></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mi>π</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow></mrow></mfenced><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mrow></mrow></mfenced><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></mrow></mrow></mrow></mrow></mrow></mrow></math>
<math><mo>=</mo><mi> </mi><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac></math>
<math><mo>=</mo><mi> </mi><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac></math>
<math><mo>=</mo><mi> </mi><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>

</details>

---

### Q41. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `2`

If <math><mn>2</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mo>(</mo><mn>2</mn><mrow><mrow><mi mathvariant="normal">cosce</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>)</mo></mrow></mrow></mrow></mrow><mi> </mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">n</mi><mi> </mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>=</mo></mrow></mrow></mrow></mrow></math>

**Options:**

- **(A)** <math><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

As given, <math><mn>2</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfenced><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mo>(</mo><mn>2</mn><mrow><mrow><mi mathvariant="normal">cosce</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow><mo>)</mo></mrow></mrow></mrow></mrow></math>
<math><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfenced><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfenced><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mo>(</mo><mn>2</mn><mrow><mrow><mi mathvariant="normal">cosce</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow><mo>)</mo></mrow></mrow></mrow></mrow></mrow></mrow></math>
Since <math> <mrow> <mfenced close="|" open="|" separators=","> <mrow> <mtext>cos x</mtext> </mrow> </mfenced> <mo>≤</mo> <mn>1</mn> </mrow> </math>
<math><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>2</mn><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow><mrow><mn>1</mn><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></mfenced><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mo>(</mo><mn>2</mn><mrow><mrow><mi mathvariant="normal">cosce</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow><mo>)</mo></mrow></mrow></mrow></mrow></math>
<math><mo>&rArr;</mo><mi> </mi><mi> </mi><mfrac><mrow><mn>2</mn><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfrac><mo>=</mo><mn>2</mn><mrow><mrow><mi mathvariant="normal">cosce</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></math>
<math><mo>&rArr;</mo><mi> </mi><mn>2</mn><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi><mo>=</mo><mn>2</mn></mrow></mrow></math>
<math><mo>&rArr;</mo><mi> </mi><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mrow></math>
<math><mo>&rArr;</mo><mi> </mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>
Hence,
<math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mrow></mrow></mrow></mrow></mrow></mrow></mrow></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
<math><mo>=</mo><msqrt><mn>2</mn></msqrt></math>

</details>

---

