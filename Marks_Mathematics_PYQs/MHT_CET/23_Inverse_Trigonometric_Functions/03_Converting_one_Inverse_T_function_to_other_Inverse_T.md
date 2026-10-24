# MHT CET Mathematics - Inverse Trigonometric Functions

## Topic 3: Converting one Inverse T function to other Inverse T

**Total Questions:** 22

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\cot\left(\operatorname{cosec}^{-1} \dfrac{5}{3} + \tan^{-1} \dfrac{2}{3}\right)$ is ...

**Options:**

- **(A)** $\dfrac{5}{17}$
- **(B)** $\dfrac{3}{17}$
- **(C)** $\dfrac{6}{17}$
- **(D)** $\dfrac{4}{17}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{6}{17}$**

**Detailed Solution:**

Let $\alpha = \operatorname{cosec}^{-1} \dfrac{5}{3}$ and $\beta = \tan^{-1} \dfrac{2}{3}$.

From $\operatorname{cosec} \alpha = \dfrac{5}{3}$, we get $\cot \alpha = \dfrac{4}{3}$.

From $\tan \beta = \dfrac{2}{3}$, we get $\cot \beta = \dfrac{3}{2}$.

We need to find the value of $\cot(\alpha + \beta)$.

Using the formula $\cot(\alpha + \beta) = \dfrac{\cot \alpha \cot \beta - 1}{\cot \alpha + \cot \beta}$:

$\cot(\alpha + \beta) = \dfrac{\dfrac{4}{3} \times \dfrac{3}{2} - 1}{\dfrac{4}{3} + \dfrac{3}{2}}$

$\cot(\alpha + \beta) = \dfrac{2 - 1}{\dfrac{8 + 9}{6}}$

$\cot(\alpha + \beta) = \dfrac{1}{\dfrac{17}{6}} = \dfrac{6}{17}$

Answer: $\dfrac{6}{17}$

</details>

---

### Q2. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin^{-1}\left(\dfrac{y}{2}\right) = \tan^{-1}\left(\dfrac{x}{2}\right),\ |y| < 2$, such that $\dfrac{dx}{dy} = k(4 + x^2)$, then $k = \ldots$

**Options:**

- **(A)** $\dfrac{x}{2y}$
- **(B)** $\dfrac{x}{4y}$
- **(C)** $\dfrac{x}{y}$
- **(D)** $\dfrac{y}{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{x}{4y}$**

**Detailed Solution:**

Given $\sin^{-1}\left(\dfrac{y}{2}\right) = \tan^{-1}\left(\dfrac{x}{2}\right)$.

Differentiating both sides with respect to $y$:

$\dfrac{1}{\sqrt{1 - \left(\dfrac{y}{2}\right)^2}} \cdot \dfrac{1}{2} = \dfrac{1}{1 + \left(\dfrac{x}{2}\right)^2} \cdot \dfrac{1}{2} \cdot \dfrac{dx}{dy}$

$\dfrac{1}{\sqrt{4 - y^2}} = \dfrac{2}{4 + x^2} \cdot \dfrac{dx}{dy}$

$\dfrac{dx}{dy} = \dfrac{4 + x^2}{2\sqrt{4 - y^2}}$

Comparing this with the given expression $\dfrac{dx}{dy} = k(4 + x^2)$, we get:

$k = \dfrac{1}{2\sqrt{4 - y^2}}$

Let $\theta = \sin^{-1}\left(\dfrac{y}{2}\right) = \tan^{-1}\left(\dfrac{x}{2}\right)$.

Then $\sin \theta = \dfrac{y}{2}$ and $\tan \theta = \dfrac{x}{2}$.

We know that $\cos \theta = \dfrac{\sin \theta}{\tan \theta} = \dfrac{y/2}{x/2} = \dfrac{y}{x}$.

Also, $\cos \theta = \sqrt{1 - \sin^2 \theta} = \sqrt{1 - \dfrac{y^2}{4}} = \dfrac{\sqrt{4 - y^2}}{2}$.

Equating the two expressions for $\cos \theta$:

$\dfrac{\sqrt{4 - y^2}}{2} = \dfrac{y}{x}$

$\Rightarrow 2\sqrt{4 - y^2} = \dfrac{4y}{x}$

Substituting this back into the expression for $k$:

$k = \dfrac{1}{\dfrac{4y}{x}} = \dfrac{x}{4y}$

Answer: $\dfrac{x}{4y}$

</details>

---

### Q3. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\cot(\cos^{-1} x) = \sec\left(\tan^{-1} \dfrac{a}{\sqrt{b^2 - a^2}}\right)$, then the value of $x$ is

**Options:**

- **(A)** $\dfrac{b}{\sqrt{2b^2 + a^2}}$
- **(B)** $\dfrac{\sqrt{2b^2 - a^2}}{b}$
- **(C)** $\dfrac{\sqrt{2b^2 + a^2}}{b}$
- **(D)** $\dfrac{b}{\sqrt{2b^2 - a^2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{b}{\sqrt{2b^2 - a^2}}$**

**Detailed Solution:**

Let $\cos^{-1} x = \theta \Rightarrow \cos \theta = x$

$\cot \theta = \dfrac{\cos \theta}{\sin \theta} = \dfrac{x}{\sqrt{1 - x^2}}$

Let $\tan^{-1} \dfrac{a}{\sqrt{b^2 - a^2}} = \phi \Rightarrow \tan \phi = \dfrac{a}{\sqrt{b^2 - a^2}}$

$\sec \phi = \sqrt{1 + \tan^2 \phi} = \sqrt{1 + \dfrac{a^2}{b^2 - a^2}} = \dfrac{b}{\sqrt{b^2 - a^2}}$

Given $\cot \theta = \sec \phi$, we have:

$\dfrac{x}{\sqrt{1 - x^2}} = \dfrac{b}{\sqrt{b^2 - a^2}}$

Squaring both sides:

$\dfrac{x^2}{1 - x^2} = \dfrac{b^2}{b^2 - a^2}$

$x^2(b^2 - a^2) = b^2(1 - x^2)$

$x^2 b^2 - x^2 a^2 = b^2 - x^2 b^2$

$x^2(2b^2 - a^2) = b^2$

$x^2 = \dfrac{b^2}{2b^2 - a^2}$

$x = \dfrac{b}{\sqrt{2b^2 - a^2}}$

Answer: $\dfrac{b}{\sqrt{2b^2 - a^2}}$

</details>

---

### Q4. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Considering only the principal values of the inverse trigonometric functions, the value of $\tan \left(\sin ^{-1}\left(\frac{3}{5}\right)-2 \cos ^{-1}\left(\frac{2}{\sqrt{5}}\right)\right)$ is

**Options:**

- **(A)** $\frac{7}{24}$
- **(B)** $\frac{-7}{24}$
- **(C)** $\frac{5}{24}$
- **(D)** $\frac{-5}{24}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-7}{24}$**

**Detailed Solution:**

Let $A = \sin^{-1}\left(\dfrac{3}{5}\right)$ and $B = \cos^{-1}\left(\dfrac{2}{\sqrt{5}}\right)$.

From $A = \sin^{-1}\left(\dfrac{3}{5}\right)$, we have $\sin A = \dfrac{3}{5}$. Since $A$ lies in the first quadrant, $\cos A = \dfrac{4}{5}$ and $\tan A = \dfrac{3}{4}$.

From $B = \cos^{-1}\left(\dfrac{2}{\sqrt{5}}\right)$, we have $\cos B = \dfrac{2}{\sqrt{5}}$. Since $B$ lies in the first quadrant, $\sin B = \sqrt{1 - \cos^2 B} = \sqrt{1 - \dfrac{4}{5}} = \dfrac{1}{\sqrt{5}}$, and $\tan B = \dfrac{1}{2}$.

We need to find the value of $\tan(A - 2B)$.

First, we calculate $\tan(2B)$:
$\tan(2B) = \dfrac{2 \tan B}{1 - \tan^2 B} = \dfrac{2 \left(\dfrac{1}{2}\right)}{1 - \left(\dfrac{1}{2}\right)^2} = \dfrac{1}{1 - \dfrac{1}{4}} = \dfrac{1}{\dfrac{3}{4}} = \dfrac{4}{3}$

Now, using the formula for $\tan(A - 2B)$:
$\tan(A - 2B) = \dfrac{\tan A - \tan(2B)}{1 + \tan A \tan(2B)}$

Substituting the values of $\tan A$ and $\tan(2B)$:
$\tan(A - 2B) = \dfrac{\dfrac{3}{4} - \dfrac{4}{3}}{1 + \left(\dfrac{3}{4}\right)\left(\dfrac{4}{3}\right)}$

$\tan(A - 2B) = \dfrac{\dfrac{9 - 16}{12}}{1 + 1} = \dfrac{\dfrac{-7}{12}}{2} = \dfrac{-7}{24}$

Answer: $\frac{-7}{24}$

</details>

---

### Q5. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Considering only the principal values of the inverse trigonometric function, the value of $\tan \left(\cos ^{-1} \frac{1}{5 \sqrt{2}}-\sin ^{-1} \frac{4}{\sqrt{17}}\right)$ is

**Options:**

- **(A)** $\frac{3}{34}$
- **(B)** $\frac{1}{34}$
- **(C)** $\frac{3}{29}$
- **(D)** $\frac{1}{29}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{29}$**

**Detailed Solution:**

Let $A = \cos^{-1} \dfrac{1}{5\sqrt{2}}$ and $B = \sin^{-1} \dfrac{4}{\sqrt{17}}$.

From $\cos A = \dfrac{1}{5\sqrt{2}}$, we can find $\tan A$ using a right-angled triangle:

$\tan A = \dfrac{\sqrt{(5\sqrt{2})^2 - 1^2}}{1} = \sqrt{50 - 1} = 7$

From $\sin B = \dfrac{4}{\sqrt{17}}$, we can find $\tan B$ similarly:

$\tan B = \dfrac{4}{\sqrt{(\sqrt{17})^2 - 4^2}} = \dfrac{4}{\sqrt{17 - 16}} = 4$

We need to evaluate $\tan(A - B)$. Using the trigonometric identity $\tan(A - B) = \dfrac{\tan A - \tan B}{1 + \tan A \tan B}$, we get:

$\tan(A - B) = \dfrac{7 - 4}{1 + (7)(4)}$

$\tan(A - B) = \dfrac{3}{1 + 28} = \dfrac{3}{29}$

Answer: $\frac{3}{29}$

</details>

---

### Q6. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $0 \lt x \lt 1$, then $\sqrt{1+x^2}\left[\left\{x \cos \left(\cot ^{-1} x\right)+\sin \left(\cot ^{-1} x\right)\right\}^2-1\right]^{\frac{1}{2}}$ is equal to

**Options:**

- **(A)** $x^2 \sqrt{1+x^2}$
- **(B)** $x$
- **(C)** $x \sqrt{1+x^2}$
- **(D)** $\sqrt{1+x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x \sqrt{1+x^2}$**

**Detailed Solution:**

Let $\theta = \cot^{-1} x$, which gives $\cot \theta = x$.

Since $0 < x < 1$, $\theta$ lies in the first quadrant.

From $\cot \theta = x$, we get $\sin \theta = \dfrac{1}{\sqrt{1+x^2}}$ and $\cos \theta = \dfrac{x}{\sqrt{1+x^2}}$.

Consider the expression inside the curly brackets:

$x \cos(\cot^{-1} x) + \sin(\cot^{-1} x) = x \cos \theta + \sin \theta$

$= x \left( \dfrac{x}{\sqrt{1+x^2}} \right) + \dfrac{1}{\sqrt{1+x^2}}$

$= \dfrac{x^2 + 1}{\sqrt{1+x^2}} = \sqrt{1+x^2}$

Now, substitute this back into the given expression:

$\sqrt{1+x^2} \left[ \left( \sqrt{1+x^2} \right)^2 - 1 \right]^{\dfrac{1}{2}}$

$= \sqrt{1+x^2} \left[ 1 + x^2 - 1 \right]^{\dfrac{1}{2}}$

$= \sqrt{1+x^2} \left[ x^2 \right]^{\dfrac{1}{2}}$

Since $x > 0$, $(x^2)^{\dfrac{1}{2}} = x$.

The expression becomes $x \sqrt{1+x^2}$.

Answer: $x \sqrt{1+x^2}$

</details>

---

### Q7. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\cos ^{-1} x=\alpha(0 \lt x \lt 1)$ and $\sin ^{-1}\left(2 x \sqrt{1-x^2}\right)+\sec ^{-1}\left(\frac{1}{2 x^2-1}\right)=\frac{2 \pi}{3}$, then $\alpha$ is

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{\pi}{6}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{6}$**

**Detailed Solution:**

Given $\cos^{-1} x = \alpha$, we have $x = \cos \alpha$.

Since $0 < x < 1$, it follows that $0 < \alpha < \dfrac{\pi}{2}$.

Substituting $x = \cos \alpha$ into the given equation:

$\sin^{-1}\left(2 \cos \alpha \sqrt{1-\cos^2 \alpha}\right) + \sec^{-1}\left(\dfrac{1}{2\cos^2 \alpha - 1}\right) = \dfrac{2\pi}{3}$

$\sin^{-1}(2 \sin \alpha \cos \alpha) + \cos^{-1}(2\cos^2 \alpha - 1) = \dfrac{2\pi}{3}$

$\sin^{-1}(\sin 2\alpha) + \cos^{-1}(\cos 2\alpha) = \dfrac{2\pi}{3}$

Since $0 < \alpha < \dfrac{\pi}{2}$, we have $0 < 2\alpha < \pi$. For this range, $\cos^{-1}(\cos 2\alpha) = 2\alpha$.

For $\sin^{-1}(\sin 2\alpha)$, we consider two cases:

Case 1: $0 < 2\alpha \le \dfrac{\pi}{2}$

$\sin^{-1}(\sin 2\alpha) = 2\alpha$

The equation becomes $2\alpha + 2\alpha = \dfrac{2\pi}{3}$

$4\alpha = \dfrac{2\pi}{3} \Rightarrow \alpha = \dfrac{\pi}{6}$

This satisfies the condition $0 < 2\alpha \le \dfrac{\pi}{2}$.

Case 2: $\dfrac{\pi}{2} < 2\alpha < \pi$

$\sin^{-1}(\sin 2\alpha) = \pi - 2\alpha$

The equation becomes $\pi - 2\alpha + 2\alpha = \dfrac{2\pi}{3}$

$\pi = \dfrac{2\pi}{3}$, which is not possible.

Therefore, the only valid solution is $\alpha = \dfrac{\pi}{6}$.

Answer: $\frac{\pi}{6}$

</details>

---

### Q8. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin \left(\cot ^{-1}(x+1)\right)=\cos \left(\tan ^{-1} x\right)$ then considering positive square roots, $x$ has the value $\qquad$

**Options:**

- **(A)** 0
- **(B)** $\dfrac{9}{4}$
- **(C)** $\dfrac{1}{2}$
- **(D)** $-\dfrac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\dfrac{1}{2}$**

**Detailed Solution:**

Let $\cot^{-1}(x+1) = \alpha$, which gives $\cot \alpha = x+1$.

Since $\alpha \in (0, \pi)$, we have $\sin \alpha = \dfrac{1}{\sqrt{1 + \cot^2 \alpha}} = \dfrac{1}{\sqrt{1 + (x+1)^2}} = \dfrac{1}{\sqrt{x^2 + 2x + 2}}$.

Let $\tan^{-1} x = \beta$, which gives $\tan \beta = x$.

Since $\beta \in \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$, we have $\cos \beta = \dfrac{1}{\sqrt{1 + \tan^2 \beta}} = \dfrac{1}{\sqrt{1 + x^2}}$.

Given that $\sin \alpha = \cos \beta$, we can equate the two expressions:

$\dfrac{1}{\sqrt{x^2 + 2x + 2}} = \dfrac{1}{\sqrt{1 + x^2}}$

Squaring both sides, we get:

$x^2 + 2x + 2 = 1 + x^2$

$2x + 2 = 1$

$2x = -1$

$x = -\dfrac{1}{2}$

Answer: $-\dfrac{1}{2}$

</details>

---

### Q9. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\cot \left(\operatorname{cosec}^{-1} \dfrac{5}{3}+\tan ^{-1} \dfrac{2}{3}\right)$ is

**Options:**

- **(A)** $\dfrac{5}{17}$
- **(B)** $\dfrac{6}{17}$
- **(C)** $\dfrac{3}{17}$
- **(D)** $\dfrac{4}{17}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{6}{17}$**

**Detailed Solution:**

Let $\alpha = \operatorname{cosec}^{-1} \dfrac{5}{3}$ and $\beta = \tan^{-1} \dfrac{2}{3}$.

From $\operatorname{cosec} \alpha = \dfrac{5}{3}$, we get $\sin \alpha = \dfrac{3}{5}$ and $\cos \alpha = \dfrac{4}{5}$.

This gives $\tan \alpha = \dfrac{3}{4}$, so $\alpha = \tan^{-1} \dfrac{3}{4}$.

The given expression becomes $\cot(\alpha + \beta)$.

Using the formula for $\tan(\alpha + \beta)$:

$\tan(\alpha + \beta) = \dfrac{\tan \alpha + \tan \beta}{1 - \tan \alpha \tan \beta}$

Substituting the values of $\tan \alpha$ and $\tan \beta$:

$\tan(\alpha + \beta) = \dfrac{\dfrac{3}{4} + \dfrac{2}{3}}{1 - \dfrac{3}{4} \times \dfrac{2}{3}}$

$\tan(\alpha + \beta) = \dfrac{\dfrac{9 + 8}{12}}{\dfrac{12 - 6}{12}} = \dfrac{17}{6}$

Therefore, $\cot(\alpha + \beta) = \dfrac{1}{\tan(\alpha + \beta)} = \dfrac{6}{17}$.

Answer: $\dfrac{6}{17}$

</details>

---

### Q10. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(\theta)=\sin \left(\tan ^{-1}\left(\dfrac{\sin \theta}{\sqrt{\cos 2 \theta}}\right)\right)$, where $\dfrac{-\pi}{4} \lt \theta \lt \dfrac{\pi}{4}$, then the value of $\dfrac{d}{d(\tan \theta)}(f(\theta))$ is

**Options:**

- **(A)** -1
- **(B)** 1
- **(C)** $\dfrac{1}{\sqrt{2}}$
- **(D)** $\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

Let $x = \tan \theta$. For $\theta \in \left(\dfrac{-\pi}{4}, \dfrac{\pi}{4}\right)$, $x \in (-1, 1)$.

We know that $\sin \theta = \dfrac{x}{\sqrt{1+x^2}}$ and $\cos 2\theta = \dfrac{1-x^2}{1+x^2}$.

Substituting these into the given function:

$f(\theta) = \sin \left(\tan^{-1}\left(\dfrac{\dfrac{x}{\sqrt{1+x^2}}}{\sqrt{\dfrac{1-x^2}{1+x^2}}}\right)\right)$

$f(\theta) = \sin \left(\tan^{-1}\left(\dfrac{x}{\sqrt{1-x^2}}\right)\right)$

Let $\alpha = \tan^{-1}\left(\dfrac{x}{\sqrt{1-x^2}}\right)$, which implies $\tan \alpha = \dfrac{x}{\sqrt{1-x^2}}$.

Using the identity $\sin \alpha = \dfrac{\tan \alpha}{\sqrt{1+\tan^2 \alpha}}$:

$\sin \alpha = \dfrac{\dfrac{x}{\sqrt{1-x^2}}}{\sqrt{1 + \dfrac{x^2}{1-x^2}}} = \dfrac{\dfrac{x}{\sqrt{1-x^2}}}{\sqrt{\dfrac{1}{1-x^2}}} = x$

Therefore, $f(\theta) = x = \tan \theta$.

We need to find the derivative of $f(\theta)$ with respect to $\tan \theta$:

$\dfrac{d(f(\theta))}{d(\tan \theta)} = \dfrac{d(\tan \theta)}{d(\tan \theta)} = 1$

Answer: 1

</details>

---

### Q11. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Given $0 \leq x \leq \frac{1}{2}$, then the value of $\tan \left(\sin ^{-1}\left(\frac{x}{\sqrt{2}}+\frac{\sqrt{1-x^2}}{\sqrt{2}}\right)-\sin ^{-1} x\right)$ is

**Options:**

- **(A)** $1$
- **(B)** $\sqrt 3$
- **(C)** $-1$
- **(D)** $\frac{1}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

$\begin{aligned} & \tan \left[\sin ^{-1}\left(\frac{x}{\sqrt{2}}+\frac{\sqrt{1-x^2}}{\sqrt{2}}\right)-\sin ^{-1} x\right] \\ & =\tan \left[\sin ^{-1}\left(\frac{x+\sqrt{1-x^2}}{\sqrt{2}}\right)-\sin ^{-1} x\right] \\ & =\tan \left[\sin ^{-1}\left(\frac{\sin \theta+\cos \theta}{\sqrt{2}}\right)-\theta\right] \quad \ldots\left[\begin{array}{l}\text { Put } \sin ^{-1} x=\theta \\ \Rightarrow x=\sin \theta\end{array}\right] \\ & =\tan \left[\sin ^{-1}\left[\sin \left(\theta+\frac{\pi}{4}\right)\right]-\theta\right] \\ & =\tan \left(\theta+\frac{\pi}{4}-\theta\right) \\ & =\tan \frac{\pi}{4}=1\end{aligned}$

</details>

---

### Q12. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\cos ^{-1} x-\cos ^{-1} \frac{y}{3}=\alpha$, where $-1 \leq x \leq 1$, $-3 \leq y \leq 3, x \leq \frac{y}{3}$, then for all $x, y$, $9 x^2-6 x y \cos \alpha+y^2$ is equal to

**Options:**

- **(A)** $\sin ^2 \alpha$
- **(B)** $3\sin ^2 \alpha$
- **(C)** $9\sin ^2 \alpha$
- **(D)** $\frac {4}{9}\sin ^2 \alpha$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $9\sin ^2 \alpha$**

**Detailed Solution:**

If $\cos ^{-1} \frac{x}{a}-\cos ^{-1} \frac{y}{b}=\theta$, then $\frac{x^2}{\mathrm{a}^2}-\frac{2 x y}{\mathrm{ab}} \cos \theta+\frac{y^2}{\mathrm{~b}^2}=\sin ^2 \theta$ Given, $\cos ^{-1} x-\cos ^{-1} \frac{y}{3}=\alpha$ Here, $\mathrm{a}=1, \mathrm{~b}=3$
$\begin{aligned}
\therefore \quad & \frac{x^2}{1^2}-\frac{2 x y}{(1)(3)} \cos \alpha+\frac{y^2}{3^2}=\sin ^2 \alpha \\
& \Rightarrow x^2-\frac{2 x y}{3} \cos \alpha+\frac{y^2}{9}=\sin ^2 \alpha \\
& \Rightarrow 9 x^2-6 x y \cos \alpha+y^2=9 \sin ^2 \alpha
\end{aligned}$

</details>

---

### Q13. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\left(\tan ^{-1} x\right)^2+\left(\cot ^{-1} x\right)^2=\frac{5 \pi^2}{8}$, then the value of $x$ is

**Options:**

- **(A)** $-2$
- **(B)** $-1$
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-1$**

**Detailed Solution:**

$\left(\tan ^{-1} x\right)^2+\left(\cot ^{-1} x\right)^2=\frac{5 \pi^2}{8}$
$\Rightarrow\left(\tan ^{-1} x+\cot ^{-1} x\right)^2-2 \tan ^{-1} x \cot ^{-1} x=\frac{5 \pi^2}{8}$
$\Rightarrow\left(\tan ^{-1} x+\cot ^{-1} x\right)^2$
$-2 \tan ^{-1} x\left(\frac{\pi}{2}-\tan ^{-1} x\right)=\frac{5 \pi^2}{8}$
$\begin{aligned} & \Rightarrow \frac{\pi^2}{4}-2 \times \frac{\pi}{2} \tan ^{-1} x+2\left(\tan ^{-1} x\right)^2=\frac{5 \pi^2}{8} \\ & \Rightarrow 2\left(\tan ^{-1} x\right)^2-\pi \tan ^{-1} x-\frac{3 \pi^2}{8}=0 \\ & \Rightarrow \tan ^{-1} x=-\frac{\pi}{4}, \frac{3 \pi}{4} \\ & \Rightarrow \tan ^{-1} x=-\frac{\pi}{4} \Rightarrow x=-1\end{aligned}$

</details>

---

### Q14. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\tan \left(\sin ^{-1}\left(\frac{3}{5}\right)+\tan ^{-1}\left(\frac{2}{3}\right)\right)$ is

**Options:**

- **(A)** $\frac{6}{17}$
- **(B)** $\frac{17}{6}$
- **(C)** $\frac{16}{7}$
- **(D)** $\frac{7}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{17}{6}$**

**Detailed Solution:**

$\tan \left[\sin ^{-1}\left(\frac{3}{5}\right)+\tan ^{-1}\left(\frac{2}{3}\right)\right]$
$=\tan \left[\tan ^{-1}\left(\frac{3}{4}\right)+\tan ^{-1}\left(\frac{2}{3}\right)\right]$
$\cdots\left[\because \sin ^{-1} x=\tan ^{-1} \frac{x}{\sqrt{1-x^2}}\right]$
$=\tan \left[\tan ^{-1}\left(\frac{\frac{3}{4}+\frac{2}{3}}{1-\frac{3}{4} \cdot \frac{2}{3}}\right)\right]$
$=\tan \left[\tan ^{-1}\left(\frac{17}{6}\right)\right]$
$=\frac{17}{6}$

</details>

---

### Q15. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\tan ^{-1}\left(\frac{1-x}{1+x}\right)=\frac{1}{2} \tan ^{-1} x$, then $x$ is

**Options:**

- **(A)** $1$
- **(B)** $\sqrt{3}$
- **(C)** $\frac{1}{\sqrt{3}}$
- **(D)** $\frac{1}{2 \sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{\sqrt{3}}$**

**Detailed Solution:**

$\begin{aligned} & \tan ^{-1}\left(\frac{1-x}{1+x}\right)=\frac{1}{2} \tan ^{-1} x \\ & \Rightarrow \tan ^{-1}(1)-\tan ^{-1}(x)=\frac{1}{2} \tan ^{-1} x \\ & \Rightarrow \frac{\pi}{4}=\frac{3}{2} \tan ^{-1} x \\ & \Rightarrow x=\tan \left(\frac{\pi}{6}\right)=\frac{1}{\sqrt{3}}\end{aligned}$

</details>

---

### Q16. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $x$, for which $\sin \left(\cot ^{-1}(x)\right)=\cos \left(\tan ^{-1}(1+x)\right)$, is

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $-\frac{1}{2}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\frac{1}{2}$**

**Detailed Solution:**

Note that $\cot ^{-1} x=\sin ^{-1}\left(\frac{1}{\sqrt{1+x^2}}\right)$ and
$$
\begin{aligned}
& \tan ^{-1}(1+x)=\cos ^{-1}\left(\frac{1}{\sqrt{1+(1+x)^2}}\right) \\
\therefore \quad & \sin \left(\cot ^{-1}(x)\right)=\cos \left(\tan ^{-1}(1+x)\right) \\
\Rightarrow & \sin \left(\sin ^{-1}\left(\frac{1}{\sqrt{1+x^2}}\right)\right)=\cos \left(\cos ^{-1}\left(\frac{1}{\sqrt{1+(1+x)^2}}\right)\right) \\
\Rightarrow & \frac{1}{\sqrt{1+x^2}}=\frac{1}{\sqrt{1+(1+x)^2}} \\
\Rightarrow & 1+(1+x)^2=1+x^2 \\
\Rightarrow & x=\frac{-1}{2}
\end{aligned}
$$

</details>

---

### Q17. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\sec ^2\left(\tan ^{-1} 2\right)+\operatorname{cosec}^2\left(\cot ^{-1} 3\right)$ is

**Options:**

- **(A)** $4$
- **(B)** $9$
- **(C)** $2$
- **(D)** $15$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $15$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \tan ^{-1} 2=\alpha \Rightarrow \tan \alpha=2 \\ & \quad \text { And } \cot ^{-1} 3=\beta \Rightarrow \cot \beta=3 \\ & \therefore \quad \sec ^2\left(\tan ^{-1} 2\right)+\operatorname{cosec}^2\left(\cot ^{-1} 3\right) \\ & =\sec ^2 \alpha+\operatorname{cosec}^2 \beta \\ & =1+\tan ^2 \alpha+1+\cot ^2 \beta \\ & =2+(2)^2+(3)^2 \\ & =15\end{aligned}$

</details>

---

### Q18. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\sin ^{-1} x+\cos ^{-1} y=\frac{3 \pi}{10}$, then the value of $\cos ^{-1} x+\sin ^{-1} y$ is

**Options:**

- **(A)** $\frac{\pi}{10}$
- **(B)** $\frac{7\pi}{10}$
- **(C)** $\frac{9\pi}{10}$
- **(D)** $\frac{3\pi}{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{7\pi}{10}$**

**Detailed Solution:**

$\begin{array}{ll} & \sin ^{-1} x+\cos ^{-1} y=\frac{3 \pi}{10} \\ \therefore \quad & \frac{\pi}{2}-\cos ^{-1} x+\frac{\pi}{2}-\sin ^{-1} y=\frac{3 \pi}{10} \\ \therefore \quad & \pi-\cos ^{-1} x-\sin ^{-1} y=\frac{3 \pi}{10} \\ \therefore \quad & \cos ^{-1} x+\sin ^{-1} y=\pi-\frac{3 \pi}{10}=\frac{7 \pi}{10}\end{array}$

</details>

---

### Q19. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\cos \left(\tan ^{-1}\left(\sin \left(\cot ^{-1} x\right)\right)\right)$ is

**Options:**

- **(A)** $\sqrt{\frac{x^2+1}{x^2-1}}$
- **(B)** $\sqrt{\frac{1-x^2}{2+x^2}}$
- **(C)** $\sqrt{\frac{1-x^2}{1+x^2}}$
- **(D)** $\sqrt{\frac{x^2+1}{x^2+2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{\frac{x^2+1}{x^2+2}}$**

**Detailed Solution:**

$\begin{aligned} & \cos \left(\tan ^{-1}\left(\sin \left(\cot ^{-1} x\right)\right)\right)=\cos \left(\tan ^{-1}\left(\sin \left(\sin ^{-1} \frac{1}{\sqrt{1+x^2}}\right)\right)\right) \\ & =\cos \left(\tan ^{-1} \frac{1}{\sqrt{1+x^2}}\right)=\operatorname{coscos}^{-1} \frac{\sqrt{1+x^2}}{\sqrt{2+x^2}}=\frac{\sqrt{x^2+1}}{\sqrt{x^2+2}}\end{aligned}$

</details>

---

### Q20. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\left[\sin \left(\tan ^{-1} \frac{3}{4}\right)\right]^{2}+\left[\sin \left(\tan ^{-1} \frac{4}{3}\right)\right]^{2}=$

**Options:**

- **(A)** 5
- **(B)** 1
- **(C)** -1
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

(D)
Let $\tan ^{-1} \frac{3}{4}=\theta \Rightarrow \tan \theta=\frac{3}{4} \Rightarrow \cot \theta=\frac{4}{3}$
$\therefore \operatorname{cosec}^{2} \theta=1+\frac{16}{9}=\frac{25}{9} \Rightarrow \operatorname{cosec} \theta=\frac{5}{3} \Rightarrow \sin \theta=\frac{3}{5}$
$\therefore \sin \left(\tan ^{-1} \frac{3}{4}\right)=\sin \left(\sin ^{-1} \frac{3}{5}\right)=\frac{3}{5}$
Let $\tan ^{-1} \frac{4}{3}=\phi \Rightarrow \tan \phi=\frac{4}{3} \Rightarrow \cot \phi=\frac{3}{4}$
$\therefore \operatorname{cosec}^{2} \phi=1+\frac{9}{16}=\frac{25}{16} \Rightarrow \operatorname{cosec} \phi=\frac{5}{4} \Rightarrow \sin \phi=\frac{4}{5}$
$\therefore \sin \left(\tan ^{-1} \frac{4}{3}\right)=\sin \left(\sin ^{-1} \frac{4}{5}\right)=\frac{4}{5}$
Hence given expression $=\left(\frac{3}{5}\right)^{2}+\left(\frac{4}{5}\right)^{2}=\frac{9+16}{25}=1$

</details>

---

### Q21. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

With usual notations in $\Delta \mathrm{ABC}$, if $C=90^{\circ}$, then $\tan ^{-1}\left(\frac{a}{b+c}\right)+\tan ^{-1}\left(\frac{b}{c+a}\right)=$

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{6}$
- **(C)** $\pi$
- **(D)** $\frac{\pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{4}$**

**Detailed Solution:**

$\therefore \quad \tan ^{-1}\left(\frac{a}{b+c}\right)+\tan ^{-1}\left(\frac{b}{c+a}\right)$
$=\tan ^{-1}\left[\frac{\frac{a}{b+c}+\frac{b}{c+a}}{1-\left(\frac{a}{b+c}\right)\left(\frac{b}{c+a}\right)}\right]$
$=\tan ^{-1}\left[\frac{a c+a^{2}+b c+b^{2}}{a c+b c+a b+c^{2}-a b}\right]=\tan ^{-1}\left(\frac{a c+b c+c^{2}}{a c+b c+c^{2}}\right) \quad \ldots\left[\because a^{2}+b^{2}=c^{2}\right.$, refer diagram $]$
$=\tan ^{-1}(1)=\frac{\pi}{4}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/xrNp3kDX55K6bXv7UZn8VoxehrZRHxaI9HNxo-id130.original.fullsize.png">

</details>

---

### Q22. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>y</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>3</mn><mi>x</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>3</mn><mi>x</mi></mrow></mfrac></mrow></mfenced><mi></mi></math> then <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>…</mo></math>

**Options:**

- **(A)** <math><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

We have, 
<math><mi>y</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>3</mn><mi>x</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>3</mn><mi>x</mi></mrow></mfrac></mrow></mfenced></math>  
<math><mo>&#8658;</mo><mi>y</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfrac></mrow></mfenced></math>  
<math><mo>&#8658;</mo><mi>y</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></mrow><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></mrow></mfrac></mrow></mfenced></math>  
<math><mo>&#8658;</mo><mi>y</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>  
<math><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>  
<math><mo>∴</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

</details>

---

