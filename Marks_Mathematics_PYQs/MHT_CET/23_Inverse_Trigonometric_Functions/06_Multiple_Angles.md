# MHT CET Mathematics - Inverse Trigonometric Functions

## Topic 6: Multiple Angles

**Total Questions:** 15

---

### Q1. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \tan^{-1}\left(\dfrac{2x^{5/2}}{1 - x^5}\right)$, then $\dfrac{dy}{dx}$ is equal to ....

**Options:**

- **(A)** $\dfrac{5x^{3/2}}{1 - x^5}$
- **(B)** $\dfrac{2x^{3/2}}{1 + x^5}$
- **(C)** $\dfrac{5x^{3/2}}{1 + x^5}$
- **(D)** $\dfrac{5x^{2/3}}{1 + x^5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{5x^{3/2}}{1 + x^5}$**

**Detailed Solution:**

Given $y = \tan^{-1}\left(\dfrac{2x^{5/2}}{1 - x^5}\right)$

This can be rewritten as $y = \tan^{-1}\left(\dfrac{2x^{5/2}}{1 - (x^{5/2})^2}\right)$

Substituting $x^{5/2} = \tan \theta$, we get $\theta = \tan^{-1}(x^{5/2})$

$y = \tan^{-1}\left(\dfrac{2\tan \theta}{1 - \tan^2 \theta}\right)$

$y = \tan^{-1}(\tan 2\theta) = 2\theta$

$y = 2\tan^{-1}(x^{5/2})$

Differentiating both sides with respect to $x$:

$\dfrac{dy}{dx} = 2 \cdot \dfrac{1}{1 + (x^{5/2})^2} \cdot \dfrac{d}{dx}(x^{5/2})$

$\dfrac{dy}{dx} = \dfrac{2}{1 + x^5} \cdot \dfrac{5}{2}x^{3/2}$

$\dfrac{dy}{dx} = \dfrac{5x^{3/2}}{1 + x^5}$

Answer: $\dfrac{5x^{3/2}}{1 + x^5}$

</details>

---

### Q2. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $x \in [0, 1)$ then the value of $\tan\left\{\dfrac{1}{2}\sin^{-1}\left(\dfrac{2x}{1+x^2}\right) + \dfrac{1}{2}\cos^{-1}\left(\dfrac{1-x^2}{1+x^2}\right)\right\}$ is:

**Options:**

- **(A)** $\infty$
- **(B)** $1$
- **(C)** $\dfrac{2x}{1-x^2}$
- **(D)** $\dfrac{2x}{1+x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{2x}{1-x^2}$**

**Detailed Solution:**

Let $x = \tan\theta$. Since $x \in [0, 1)$, we have $\theta \in \left[0, \dfrac{\pi}{4}\right)$.

$\sin^{-1}\left(\dfrac{2x}{1+x^2}\right) = \sin^{-1}\left(\dfrac{2\tan\theta}{1+\tan^2\theta}\right) = \sin^{-1}(\sin 2\theta)$

Since $2\theta \in \left[0, \dfrac{\pi}{2}\right)$, $\sin^{-1}(\sin 2\theta) = 2\theta$.

Similarly, $\cos^{-1}\left(\dfrac{1-x^2}{1+x^2}\right) = \cos^{-1}\left(\dfrac{1-\tan^2\theta}{1+\tan^2\theta}\right) = \cos^{-1}(\cos 2\theta)$

Since $2\theta \in \left[0, \dfrac{\pi}{2}\right)$, $\cos^{-1}(\cos 2\theta) = 2\theta$.

Substituting these values into the given expression:

$\tan\left\{\dfrac{1}{2}(2\theta) + \dfrac{1}{2}(2\theta)\right\} = \tan(\theta + \theta) = \tan(2\theta)$

Using the double angle formula for tangent:

$\tan(2\theta) = \dfrac{2\tan\theta}{1-\tan^2\theta} = \dfrac{2x}{1-x^2}$

Answer: $\dfrac{2x}{1-x^2}$

</details>

---

### Q3. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solutions of the equation $\sin[2\cos^{-1}\{\cot(2\tan^{-1} x)\}] = 0$ are

**Options:**

- **(A)** $\pm 3$
- **(B)** $1 \pm \sqrt{2}$
- **(C)** $2 \pm \sqrt{2}$
- **(D)** $\pm\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1 \pm \sqrt{2}$**

**Detailed Solution:**

Let $\tan^{-1} x = \theta$, which implies $x = \tan \theta$.

The expression $\cot(2 \tan^{-1} x)$ can be written as $\cot(2\theta) = \dfrac{1 - \tan^2 \theta}{2 \tan \theta} = \dfrac{1 - x^2}{2x}$.

Substituting this into the given equation, we get $\sin\left[2 \cos^{-1}\left(\dfrac{1 - x^2}{2x}\right)\right] = 0$.

This implies $2 \cos^{-1}\left(\dfrac{1 - x^2}{2x}\right) = n\pi$, where $n$ is an integer.

Therefore, $\cos^{-1}\left(\dfrac{1 - x^2}{2x}\right) = \dfrac{n\pi}{2}$.

Since the principal value branch of $\cos^{-1}$ is $[0, \pi]$, the possible values for $\dfrac{n\pi}{2}$ are $0$, $\dfrac{\pi}{2}$, and $\pi$.

If $\cos^{-1}\left(\dfrac{1 - x^2}{2x}\right) = 0$, then $\dfrac{1 - x^2}{2x} = 1$, which gives $x^2 + 2x - 1 = 0$. Solving this quadratic equation yields $x = -1 \pm \sqrt{2}$.

If $\cos^{-1}\left(\dfrac{1 - x^2}{2x}\right) = \dfrac{\pi}{2}$, then $\dfrac{1 - x^2}{2x} = 0$, which gives $x^2 = 1$ yielding $x = \pm 1$.

If $\cos^{-1}\left(\dfrac{1 - x^2}{2x}\right) = \pi$, then $\dfrac{1 - x^2}{2x} = -1$, which gives $x^2 - 2x - 1 = 0$. Solving this yields $x = 1 \pm \sqrt{2}$.

The possible solutions are $\pm 1$, $-1 \pm \sqrt{2}$, and $1 \pm \sqrt{2}$. Among the given options, $1 \pm \sqrt{2}$ is correct.

</details>

---

### Q4. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$2\sin^{-1}\left(\dfrac{3}{5}\right) + \tan^{-1}\left(\dfrac{1}{5}\right) + \tan^{-1}\left(\dfrac{1}{7}\right) =$

**Options:**

- **(A)** $\tan^{-1}(18)$
- **(B)** $-\tan^{-1}(18)$
- **(C)** $\pi + \tan^{-1}(18)$
- **(D)** $\pi - \tan^{-1}(18)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\pi - \tan^{-1}(18)$**

**Detailed Solution:**

Let $\theta = \sin^{-1}\left(\dfrac{3}{5}\right)$. Then $\sin\theta = \dfrac{3}{5}$, which gives $\tan\theta = \dfrac{3}{4}$.

Thus, $2\sin^{-1}\left(\dfrac{3}{5}\right) = 2\tan^{-1}\left(\dfrac{3}{4}\right)$.

Using the formula $2\tan^{-1}x = \tan^{-1}\left(\dfrac{2x}{1-x^2}\right)$ for $x < 1$:

$2\tan^{-1}\left(\dfrac{3}{4}\right) = \tan^{-1}\left(\dfrac{2 \times \dfrac{3}{4}}{1 - \left(\dfrac{3}{4}\right)^2}\right) = \tan^{-1}\left(\dfrac{\dfrac{3}{2}}{\dfrac{7}{16}}\right) = \tan^{-1}\left(\dfrac{24}{7}\right)$

Next, evaluate $\tan^{-1}\left(\dfrac{1}{5}\right) + \tan^{-1}\left(\dfrac{1}{7}\right)$ using the formula $\tan^{-1}x + \tan^{-1}y = \tan^{-1}\left(\dfrac{x+y}{1-xy}\right)$ for $xy < 1$:

$\tan^{-1}\left(\dfrac{1}{5}\right) + \tan^{-1}\left(\dfrac{1}{7}\right) = \tan^{-1}\left(\dfrac{\dfrac{1}{5} + \dfrac{1}{7}}{1 - \dfrac{1}{35}}\right) = \tan^{-1}\left(\dfrac{\dfrac{12}{35}}{\dfrac{34}{35}}\right) = \tan^{-1}\left(\dfrac{12}{34}\right) = \tan^{-1}\left(\dfrac{6}{17}\right)$

Now, add the two results:

$\tan^{-1}\left(\dfrac{24}{7}\right) + \tan^{-1}\left(\dfrac{6}{17}\right)$

Here, $x = \dfrac{24}{7} > 0$, $y = \dfrac{6}{17} > 0$, and their product is $xy = \dfrac{144}{119} > 1$.

For $x > 0$, $y > 0$, and $xy > 1$, we use the formula $\tan^{-1}x + \tan^{-1}y = \pi + \tan^{-1}\left(\dfrac{x+y}{1-xy}\right)$:

$\pi + \tan^{-1}\left(\dfrac{\dfrac{24}{7} + \dfrac{6}{17}}{1 - \dfrac{144}{119}}\right) = \pi + \tan^{-1}\left(\dfrac{\dfrac{408 + 42}{119}}{\dfrac{119 - 144}{119}}\right)$

$= \pi + \tan^{-1}\left(\dfrac{450}{-25}\right) = \pi + \tan^{-1}(-18)$

Since $\tan^{-1}(-x) = -\tan^{-1}x$, we get:

$\pi - \tan^{-1}(18)$

Answer: $\pi - \tan^{-1}(18)$

</details>

---

### Q5. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin^{-1}(1 - x) - 2\sin^{-1} x = \dfrac{\pi}{2}$, then the value of $x$ is

**Options:**

- **(A)** $\pi$
- **(B)** $\dfrac{7\pi}{2}$
- **(C)** $0$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0$**

**Detailed Solution:**

Given equation is $\sin^{-1}(1 - x) - 2\sin^{-1} x = \dfrac{\pi}{2}$

$\sin^{-1}(1 - x) = \dfrac{\pi}{2} + 2\sin^{-1} x$

Taking sine on both sides:

$\sin(\sin^{-1}(1 - x)) = \sin(\dfrac{\pi}{2} + 2\sin^{-1} x)$

$1 - x = \cos(2\sin^{-1} x)$

Let $\sin^{-1} x = \theta \Rightarrow x = \sin \theta$

$1 - x = \cos 2\theta$

$1 - x = 1 - 2\sin^2 \theta$

$1 - x = 1 - 2x^2$

$2x^2 - x = 0$

$x(2x - 1) = 0$

$x = 0$ or $x = \dfrac{1}{2}$

Checking $x = 0$ in the original equation:

$\sin^{-1}(1) - 2\sin^{-1}(0) = \dfrac{\pi}{2} - 0 = \dfrac{\pi}{2}$ (Satisfies)

Checking $x = \dfrac{1}{2}$ in the original equation:

$\sin^{-1}(\dfrac{1}{2}) - 2\sin^{-1}(\dfrac{1}{2}) = \dfrac{\pi}{6} - 2(\dfrac{\pi}{6}) = -\dfrac{\pi}{6} \neq \dfrac{\pi}{2}$ (Does not satisfy)

Therefore, $x = 0$ is the only valid solution.

Answer: $0$

</details>

---

### Q6. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $3\sin^{-1}\left(\dfrac{2x}{1 + x^2}\right) - 4\cos^{-1}\left(\dfrac{1 - x^2}{1 + x^2}\right) + 2\tan^{-1}\left(\dfrac{2x}{1 - x^2}\right) = \dfrac{\pi}{3}$ then $x = ?$

**Options:**

- **(A)** $\sqrt{3}$
- **(B)** $1$
- **(C)** $\dfrac{1}{\sqrt{3}}$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{\sqrt{3}}$**

**Detailed Solution:**

Assuming $0 < x < 1$, the standard inverse trigonometric identities are:

$\sin^{-1}\left(\dfrac{2x}{1 + x^2}\right) = 2\tan^{-1}x$

$\cos^{-1}\left(\dfrac{1 - x^2}{1 + x^2}\right) = 2\tan^{-1}x$

$\tan^{-1}\left(\dfrac{2x}{1 - x^2}\right) = 2\tan^{-1}x$

Substituting these into the given equation yields:

$3(2\tan^{-1}x) - 4(2\tan^{-1}x) + 2(2\tan^{-1}x) = \dfrac{\pi}{3}$

$6\tan^{-1}x - 8\tan^{-1}x + 4\tan^{-1}x = \dfrac{\pi}{3}$

$2\tan^{-1}x = \dfrac{\pi}{3}$

$\tan^{-1}x = \dfrac{\pi}{6}$

$x = \tan\left(\dfrac{\pi}{6}\right) = \dfrac{1}{\sqrt{3}}$

Since $x = \dfrac{1}{\sqrt{3}}$ satisfies the condition $0 < x < 1$, it is the valid solution.

Answer: $\dfrac{1}{\sqrt{3}}$

</details>

---

### Q7. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\sin\left(3\sin^{-1}\left(\dfrac{1}{5}\right)\right) =$

**Options:**

- **(A)** $\dfrac{74}{125}$
- **(B)** $\dfrac{71}{125}$
- **(C)** $\dfrac{3}{5}$
- **(D)** $\dfrac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{71}{125}$**

**Detailed Solution:**

Let $\theta = \sin^{-1}\left(\dfrac{1}{5}\right)$.

Then, $\sin\theta = \dfrac{1}{5}$.

The given expression becomes $\sin(3\theta)$.

Using the identity $\sin(3\theta) = 3\sin\theta - 4\sin^3\theta$:

$\sin(3\theta) = 3\left(\dfrac{1}{5}\right) - 4\left(\dfrac{1}{5}\right)^3$

$\sin(3\theta) = \dfrac{3}{5} - \dfrac{4}{125}$

$\sin(3\theta) = \dfrac{75 - 4}{125}$

$\sin(3\theta) = \dfrac{71}{125}$

</details>

---

### Q8. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $3\tan^{-1}\left(\dfrac{1}{2}\right) = \ldots$

**Options:**

- **(A)** $\tan^{-1}\left(\dfrac{5}{2}\right)$
- **(B)** $\tan^{-1}\left(\dfrac{2}{5}\right)$
- **(C)** $\cot^{-1}\left(\dfrac{11}{2}\right)$
- **(D)** $\tan^{-1}\left(\dfrac{11}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\tan^{-1}\left(\dfrac{11}{2}\right)$**

**Detailed Solution:**

Using the formula $3\tan^{-1}x = \tan^{-1}\left(\dfrac{3x - x^3}{1 - 3x^2}\right)$ for $|x| < \dfrac{1}{\sqrt{3}}$.

Since $x = \dfrac{1}{2} < \dfrac{1}{\sqrt{3}}$, the formula can be applied directly.

$3\tan^{-1}\left(\dfrac{1}{2}\right) = \tan^{-1}\left(\dfrac{3\left(\dfrac{1}{2}\right) - \left(\dfrac{1}{2}\right)^3}{1 - 3\left(\dfrac{1}{2}\right)^2}\right)$

$= \tan^{-1}\left(\dfrac{\dfrac{3}{2} - \dfrac{1}{8}}{1 - \dfrac{3}{4}}\right)$

$= \tan^{-1}\left(\dfrac{\dfrac{12 - 1}{8}}{\dfrac{4 - 3}{4}}\right)$

$= \tan^{-1}\left(\dfrac{\dfrac{11}{8}}{\dfrac{1}{4}}\right)$

$= \tan^{-1}\left(\dfrac{11}{8} \times 4\right)$

$= \tan^{-1}\left(\dfrac{11}{2}\right)$

Answer: $\tan^{-1}\left(\dfrac{11}{2}\right)$

</details>

---

### Q9. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\tan \left[2 \tan ^{-1} \frac{1}{5}-\frac{\pi}{4}\right]$ is

**Options:**

- **(A)** $\frac{5}{4}$
- **(B)** $\frac{5}{16}$
- **(C)** $-\frac{7}{17}$
- **(D)** $\frac{7}{17}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\frac{7}{17}$**

**Detailed Solution:**

Let $\theta = \tan^{-1} \dfrac{1}{5}$, which gives $\tan \theta = \dfrac{1}{5}$.

We need to find the value of $\tan \left(2\theta - \dfrac{\pi}{4}\right)$.

First, calculate $\tan 2\theta$ using the double angle formula:

$\tan 2\theta = \dfrac{2 \tan \theta}{1 - \tan^2 \theta} = \dfrac{2 \left(\dfrac{1}{5}\right)}{1 - \left(\dfrac{1}{5}\right)^2} = \dfrac{\dfrac{2}{5}}{\dfrac{24}{25}} = \dfrac{5}{12}$

Now, apply the tangent subtraction formula:

$\tan \left(2\theta - \dfrac{\pi}{4}\right) = \dfrac{\tan 2\theta - \tan \dfrac{\pi}{4}}{1 + \tan 2\theta \tan \dfrac{\pi}{4}}$

Substitute $\tan 2\theta = \dfrac{5}{12}$ and $\tan \dfrac{\pi}{4} = 1$:

$\tan \left(2\theta - \dfrac{\pi}{4}\right) = \dfrac{\dfrac{5}{12} - 1}{1 + \dfrac{5}{12}(1)} = \dfrac{\dfrac{-7}{12}}{\dfrac{17}{12}} = -\dfrac{7}{17}$

Answer: $-\frac{7}{17}$

</details>

---

### Q10. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $3 \sin ^{-1}\left(\frac{2 x}{1+x^2}\right)-4 \cos ^{-1}\left(\frac{1-x^2}{1+x^2}\right)+2 \tan ^{-1}\left(\frac{2 x}{1-x^2}\right)=\frac{\pi}{3}$, then the value of $x=$

**Options:**

- **(A)** $\sqrt{3}$
- **(B)** $1$
- **(C)** $\frac{1}{\sqrt{3}}$
- **(D)** $\frac{1}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{\sqrt{3}}$**

**Detailed Solution:**

Substitute $x = \tan \theta$. Assuming $0 < x < 1$, we have $0 < \theta < \dfrac{\pi}{4}$, which implies $0 < 2\theta < \dfrac{\pi}{2}$.

The given equation becomes:

$3 \sin^{-1}\left(\dfrac{2 \tan \theta}{1+\tan^2 \theta}\right) - 4 \cos^{-1}\left(\dfrac{1-\tan^2 \theta}{1+\tan^2 \theta}\right) + 2 \tan^{-1}\left(\dfrac{2 \tan \theta}{1-\tan^2 \theta}\right) = \dfrac{\pi}{3}$

Using the double angle formulas, we get:

$3 \sin^{-1}(\sin 2\theta) - 4 \cos^{-1}(\cos 2\theta) + 2 \tan^{-1}(\tan 2\theta) = \dfrac{\pi}{3}$

Since $2\theta \in \left(0, \dfrac{\pi}{2}\right)$, the principal values are:

$3(2\theta) - 4(2\theta) + 2(2\theta) = \dfrac{\pi}{3}$

$6\theta - 8\theta + 4\theta = \dfrac{\pi}{3}$

$2\theta = \dfrac{\pi}{3}$

$\theta = \dfrac{\pi}{6}$

Therefore, $x = \tan \theta = \tan\left(\dfrac{\pi}{6}\right) = \dfrac{1}{\sqrt{3}}$.

This value satisfies the initial assumption $0 < x < 1$.

Answer: $\frac{1}{\sqrt{3}}$

</details>

---

### Q11. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $2 \tan ^{-1} \frac{1}{2}+\tan ^{-1} \frac{3}{8}$ is

**Options:**

- **(A)** $\tan ^{-1}\left(\frac{42}{24}\right)$
- **(B)** $2 \tan ^{-1}\left(\frac{42}{24}\right)$
- **(C)** $\tan ^{-1}\left(\frac{24}{41}\right)$
- **(D)** $\tan ^{-1}\left(\frac{41}{12}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\tan ^{-1}\left(\frac{41}{12}\right)$**

**Detailed Solution:**

Using the formula $2 \tan^{-1} x = \tan^{-1} \left( \dfrac{2x}{1 - x^2} \right)$ for $|x| < 1$:

$2 \tan^{-1} \dfrac{1}{2} = \tan^{-1} \left( \dfrac{2 \times \dfrac{1}{2}}{1 - \left(\dfrac{1}{2}\right)^2} \right) = \tan^{-1} \left( \dfrac{1}{1 - \dfrac{1}{4}} \right) = \tan^{-1} \dfrac{4}{3}$

Substituting this back into the given expression:

$\tan^{-1} \dfrac{4}{3} + \tan^{-1} \dfrac{3}{8}$

Using the formula $\tan^{-1} x + \tan^{-1} y = \tan^{-1} \left( \dfrac{x + y}{1 - xy} \right)$ for $xy < 1$:

$\tan^{-1} \dfrac{4}{3} + \tan^{-1} \dfrac{3}{8} = \tan^{-1} \left( \dfrac{\dfrac{4}{3} + \dfrac{3}{8}}{1 - \dfrac{4}{3} \times \dfrac{3}{8}} \right)$

$= \tan^{-1} \left( \dfrac{\dfrac{32 + 9}{24}}{1 - \dfrac{12}{24}} \right)$

$= \tan^{-1} \left( \dfrac{\dfrac{41}{24}}{\dfrac{12}{24}} \right)$

$= \tan^{-1} \left( \dfrac{41}{12} \right)$

Answer: $\tan ^{-1}\left(\frac{41}{12}\right)$

</details>

---

### Q12. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $2 \tan ^{-1}(\cos x)=\tan ^{-1}(2 \operatorname{cosec} x)$, then the value of $x$ is

**Options:**

- **(A)** $-\frac{\pi}{4}$
- **(B)** $0$
- **(C)** $\frac{\pi}{8}$
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{4}$**

**Detailed Solution:**

Given equation is $2 \tan^{-1}(\cos x) = \tan^{-1}(2 \operatorname{cosec} x)$

Using the formula $2 \tan^{-1} y = \tan^{-1} \left( \dfrac{2y}{1 - y^2} \right)$, we get:

$\tan^{-1} \left( \dfrac{2 \cos x}{1 - \cos^2 x} \right) = \tan^{-1} \left( \dfrac{2}{\sin x} \right)$

$\tan^{-1} \left( \dfrac{2 \cos x}{\sin^2 x} \right) = \tan^{-1} \left( \dfrac{2}{\sin x} \right)$

Equating the arguments on both sides:

$\dfrac{2 \cos x}{\sin^2 x} = \dfrac{2}{\sin x}$

Since $\operatorname{cosec} x$ is defined, $\sin x \neq 0$. Multiplying both sides by $\dfrac{\sin^2 x}{2}$ gives:

$\cos x = \sin x$

$\tan x = 1$

From the given options, the value satisfying this equation is $x = \dfrac{\pi}{4}$.

Answer: $\frac{\pi}{4}$

</details>

---

### Q13. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\tan \left(2 \tan ^{-1}\left(\dfrac{\sqrt{5}-1}{2}\right)\right)$ is

**Options:**

- **(A)** $2 \sqrt{5}$
- **(B)** 4
- **(C)** 2
- **(D)** $\sqrt{5}-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

Let $\theta = \tan^{-1}\left(\dfrac{\sqrt{5}-1}{2}\right)$

$\Rightarrow \tan \theta = \dfrac{\sqrt{5}-1}{2}$

We need to find the value of $\tan(2\theta)$.

Using the formula $\tan(2\theta) = \dfrac{2\tan\theta}{1 - \tan^2\theta}$

Substituting the value of $\tan\theta$:

$2\tan\theta = 2 \left(\dfrac{\sqrt{5}-1}{2}\right) = \sqrt{5}-1$

$\tan^2\theta = \left(\dfrac{\sqrt{5}-1}{2}\right)^2 = \dfrac{5 + 1 - 2\sqrt{5}}{4} = \dfrac{6 - 2\sqrt{5}}{4} = \dfrac{3 - \sqrt{5}}{2}$

$1 - \tan^2\theta = 1 - \left(\dfrac{3 - \sqrt{5}}{2}\right) = \dfrac{2 - 3 + \sqrt{5}}{2} = \dfrac{\sqrt{5} - 1}{2}$

Therefore, $\tan(2\theta) = \dfrac{\sqrt{5}-1}{\dfrac{\sqrt{5}-1}{2}} = 2$

Answer: 2

</details>

---

### Q14. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\sin \left(2 \cos ^{-1} \cdot\left(-\dfrac{3}{5}\right)\right)$ is

**Options:**

- **(A)** $\dfrac{24}{25}$
- **(B)** $-\dfrac{24}{25}$
- **(C)** $\dfrac{8}{25}$
- **(D)** $-\dfrac{8}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\dfrac{24}{25}$**

**Detailed Solution:**

Let $\theta = \cos^{-1} \left(-\dfrac{3}{5}\right)$.

This implies $\cos \theta = -\dfrac{3}{5}$. Since the principal value of $\cos^{-1}$ lies in $[0, \pi]$ and the argument is negative, $\theta$ lies in the second quadrant.

In the second quadrant, sine is positive. Thus, $\sin \theta = \sqrt{1 - \cos^2 \theta} = \sqrt{1 - \left(-\dfrac{3}{5}\right)^2} = \dfrac{4}{5}$.

We need to find the value of $\sin(2\theta)$.

Using the identity $\sin(2\theta) = 2 \sin \theta \cos \theta$, we get:

$\sin(2\theta) = 2 \left(\dfrac{4}{5}\right) \left(-\dfrac{3}{5}\right) = -\dfrac{24}{25}$.

Answer: $-\dfrac{24}{25}$

</details>

---

### Q15. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\sum_{r=1}^{50} \tan ^{-1} \frac{1}{2 r^2}=p$ then $\tan p$ is

**Options:**

- **(A)** $\frac {100}{101}$
- **(B)** $\frac {51}{50}$
- **(C)** $\frac {50}{51}$
- **(D)** $\frac {101}{102}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac {50}{51}$**

**Detailed Solution:**

$\begin{aligned} & \sum_{\mathrm{r}=1}^{50} \tan ^{-1} \frac{1}{2 \mathrm{r}^2}=\mathrm{p} \\ & \Rightarrow \sum_{\mathrm{r}=1}^{50} \tan ^{-1}\left(\frac{2}{4 \mathrm{r}^2}\right)=\mathrm{p} \\ & \Rightarrow \sum_{\mathrm{r}=1}^{50} \tan ^{-1}\left[\frac{(2 \mathrm{r}+1)-(2 \mathrm{r}-1)}{1+(2 \mathrm{r}+1)(2 \mathrm{r}-1)}\right]=\mathrm{p} \\ & \Rightarrow \sum_{\mathrm{r}=1}^{50}\left[\tan ^{-1}(2 \mathrm{r}+1)-\tan ^{-1}(2 \mathrm{r}-1)\right]=\mathrm{p} \\ & \Rightarrow \tan ^{-1}(101)-\tan ^{-1}(1)=\mathrm{p} \\ & \Rightarrow \tan ^{-1}\left(\frac{101-1}{1+101}\right)=\mathrm{p} \\ & \Rightarrow \frac{100}{102}=\tan \mathrm{p} \\ & \Rightarrow \tan \mathrm{p}=\frac{50}{51}\end{aligned}$

</details>

---

