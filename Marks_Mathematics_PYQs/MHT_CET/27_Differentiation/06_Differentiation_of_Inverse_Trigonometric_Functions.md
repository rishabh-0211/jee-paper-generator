# MHT CET Mathematics - Differentiation

## Topic 6: Differentiation of Inverse Trigonometric Functions

**Total Questions:** 62

---

### Q1. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \sin^{-1}(y \cdot \cos 2x)$ such that $\dfrac{dy}{dx} = \dfrac{2y \cdot f(x)}{g(x) - \cos y}$ then $\{f(x)\}^2 - \{g(x)\}^2 = $

**Options:**

- **(A)** $-\cos 4x$
- **(B)** $1$
- **(C)** $\sin 4x$
- **(D)** $\cos 4x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\cos 4x$**

**Detailed Solution:**

Given $y = \sin^{-1}(y \cdot \cos 2x)$

$\sin y = y \cos 2x$

Differentiating both sides with respect to $x$:

$\cos y \cdot \dfrac{dy}{dx} = \dfrac{dy}{dx} \cos 2x - 2y \sin 2x$

$\dfrac{dy}{dx} (\cos y - \cos 2x) = -2y \sin 2x$

$\dfrac{dy}{dx} = \dfrac{-2y \sin 2x}{\cos y - \cos 2x}$

$\dfrac{dy}{dx} = \dfrac{2y \sin 2x}{\cos 2x - \cos y}$

Comparing this with the given expression $\dfrac{dy}{dx} = \dfrac{2y \cdot f(x)}{g(x) - \cos y}$ gives:

$f(x) = \sin 2x$

$g(x) = \cos 2x$

Evaluating $\{f(x)\}^2 - \{g(x)\}^2$:

$\{f(x)\}^2 - \{g(x)\}^2 = \sin^2 2x - \cos^2 2x$

$\{f(x)\}^2 - \{g(x)\}^2 = -(\cos^2 2x - \sin^2 2x)$

$\{f(x)\}^2 - \{g(x)\}^2 = -\cos 4x$

Answer: $-\cos 4x$

</details>

---

### Q2. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \sin(\tan^{-1} x)$, then $\int_{0}^{1} xf''(x)dx$ is:

**Options:**

- **(A)** $\dfrac{\sqrt{3}}{2}$
- **(B)** $-\dfrac{1}{2\sqrt{2}}$
- **(C)** $\dfrac{1}{\sqrt{2}}$
- **(D)** $\dfrac{1}{2\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\dfrac{1}{2\sqrt{2}}$**

**Detailed Solution:**

Given $f(x) = \sin(\tan^{-1} x)$

Let $\theta = \tan^{-1} x \Rightarrow \tan \theta = x$

$f(x) = \sin \theta = \dfrac{x}{\sqrt{1+x^2}}$

Using integration by parts on the given integral:

$I = \int_{0}^{1} x f''(x) dx = [x f'(x)]_{0}^{1} - \int_{0}^{1} f'(x) dx$

$I = f'(1) - [f(x)]_{0}^{1} = f'(1) - f(1) + f(0)$

Differentiating $f(x)$:

$f'(x) = \dfrac{d}{dx} \left( \dfrac{x}{\sqrt{1+x^2}} \right) = \dfrac{\sqrt{1+x^2} \cdot 1 - x \cdot \dfrac{x}{\sqrt{1+x^2}}}{1+x^2} = \dfrac{1}{(1+x^2)^{3/2}}$

Evaluating the values at $x = 1$ and $x = 0$:

$f'(1) = \dfrac{1}{(1+1)^{3/2}} = \dfrac{1}{2\sqrt{2}}$

$f(1) = \dfrac{1}{\sqrt{1+1}} = \dfrac{1}{\sqrt{2}}$

$f(0) = 0$

Substituting these values into the expression for $I$:

$I = \dfrac{1}{2\sqrt{2}} - \dfrac{1}{\sqrt{2}} + 0 = -\dfrac{1}{2\sqrt{2}}$

Answer: $-\dfrac{1}{2\sqrt{2}}$

</details>

---

### Q3. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \cos^{-1} x$, then $\dfrac{d^2y}{dx^2} =$

**Options:**

- **(A)** $\sec^2 y \cdot \tan y$
- **(B)** $-\sec^2 y \cdot \tan y$
- **(C)** $\csc^2 y \cdot \cot y$
- **(D)** $-\csc^2 y \cdot \cot y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\csc^2 y \cdot \cot y$**

**Detailed Solution:**

Given $y = \cos^{-1} x$

$x = \cos y$

Differentiating both sides with respect to $x$:

$1 = -\sin y \cdot \dfrac{dy}{dx}$

$\dfrac{dy}{dx} = -\csc y$

Differentiating again with respect to $x$:

$\dfrac{d^2y}{dx^2} = \dfrac{d}{dx}(-\csc y)$

$\dfrac{d^2y}{dx^2} = \dfrac{d}{dy}(-\csc y) \cdot \dfrac{dy}{dx}$

$\dfrac{d^2y}{dx^2} = (\csc y \cdot \cot y) \cdot (-\csc y)$

$\dfrac{d^2y}{dx^2} = -\csc^2 y \cdot \cot y$

Answer: $-\csc^2 y \cdot \cot y$

</details>

---

### Q4. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \cos^2\left[\cot^{-1}\left(\sqrt{\dfrac{1 - x}{1 + x}}\right)\right]$ then $\dfrac{dy}{dx} = $ ........

**Options:**

- **(A)** $\dfrac{-1}{2}$
- **(B)** $\dfrac{1}{2}$
- **(C)** $1$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{-1}{2}$**

**Detailed Solution:**

Let $x = \cos \theta$.

Substituting this in the given expression:

$\sqrt{\dfrac{1 - x}{1 + x}} = \sqrt{\dfrac{1 - \cos \theta}{1 + \cos \theta}} = \sqrt{\dfrac{2 \sin^2(\theta/2)}{2 \cos^2(\theta/2)}} = \tan\left(\dfrac{\theta}{2}\right)$

The expression for $y$ becomes:

$y = \cos^2\left[\cot^{-1}\left(\tan\left(\dfrac{\theta}{2}\right)\right)\right]$

Using the identity $\tan\left(\dfrac{\theta}{2}\right) = \cot\left(\dfrac{\pi}{2} - \dfrac{\theta}{2}\right)$:

$y = \cos^2\left[\cot^{-1}\left(\cot\left(\dfrac{\pi}{2} - \dfrac{\theta}{2}\right)\right)\right]$

$y = \cos^2\left(\dfrac{\pi}{2} - \dfrac{\theta}{2}\right)$

$y = \sin^2\left(\dfrac{\theta}{2}\right)$

Using the half-angle formula $\sin^2\left(\dfrac{\theta}{2}\right) = \dfrac{1 - \cos \theta}{2}$:

$y = \dfrac{1 - x}{2}$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = \dfrac{d}{dx}\left(\dfrac{1}{2} - \dfrac{x}{2}\right) = -\dfrac{1}{2}$

Answer: $\dfrac{-1}{2}$

</details>

---

### Q5. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \sin^{-1}\left(\dfrac{25 - x^2}{25 + x^2}\right)$, then $y'(1)$ is...

**Options:**

- **(A)** $-\dfrac{5}{13}$
- **(B)** $\dfrac{5}{13}$
- **(C)** $\dfrac{13}{5}$
- **(D)** $\dfrac{2}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\dfrac{5}{13}$**

**Detailed Solution:**

Given $y = \sin^{-1}\left(\dfrac{25 - x^2}{25 + x^2}\right)$

Substitute $x = 5 \tan \theta$, which gives $\theta = \tan^{-1}\left(\dfrac{x}{5}\right)$

$y = \sin^{-1}\left(\dfrac{25 - 25 \tan^2 \theta}{25 + 25 \tan^2 \theta}\right)$

$y = \sin^{-1}\left(\dfrac{1 - \tan^2 \theta}{1 + \tan^2 \theta}\right)$

$y = \sin^{-1}(\cos 2\theta)$

$y = \sin^{-1}\left(\sin\left(\dfrac{\pi}{2} - 2\theta\right)\right)$

For $x = 1$, $\theta = \tan^{-1}\left(\dfrac{1}{5}\right)$, so $2\theta \in \left(0, \dfrac{\pi}{2}\right)$, which lies in the principal domain of $\sin^{-1}$.

$y = \dfrac{\pi}{2} - 2\theta = \dfrac{\pi}{2} - 2 \tan^{-1}\left(\dfrac{x}{5}\right)$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = -2 \cdot \dfrac{1}{1 + \left(\dfrac{x}{5}\right)^2} \cdot \dfrac{1}{5} = -\dfrac{10}{25 + x^2}$

Substituting $x = 1$:

$y'(1) = -\dfrac{10}{25 + 1} = -\dfrac{10}{26} = -\dfrac{5}{13}$

Answer: $-\dfrac{5}{13}$

</details>

---

### Q6. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \cot^{-1}\left(\dfrac{1 + \sin 5x}{\cos 5x}\right)$, then the value of $\dfrac{dy}{dx}$ is

**Options:**

- **(A)** $-5$
- **(B)** $5$
- **(C)** $-\dfrac{2}{5}$
- **(D)** $-\dfrac{5}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\dfrac{5}{2}$**

**Detailed Solution:**

Given $y = \cot^{-1}\left(\dfrac{1 + \sin 5x}{\cos 5x}\right)$

We can simplify the expression inside the inverse trigonometric function using half-angle formulas:

$\dfrac{1 + \sin 5x}{\cos 5x} = \dfrac{\left(\cos \dfrac{5x}{2} + \sin \dfrac{5x}{2}\right)^2}{\cos^2 \dfrac{5x}{2} - \sin^2 \dfrac{5x}{2}}$

$\Rightarrow \dfrac{1 + \sin 5x}{\cos 5x} = \dfrac{\cos \dfrac{5x}{2} + \sin \dfrac{5x}{2}}{\cos \dfrac{5x}{2} - \sin \dfrac{5x}{2}}$

Dividing the numerator and the denominator by $\cos \dfrac{5x}{2}$:

$\dfrac{1 + \sin 5x}{\cos 5x} = \dfrac{1 + \tan \dfrac{5x}{2}}{1 - \tan \dfrac{5x}{2}} = \tan\left(\dfrac{\pi}{4} + \dfrac{5x}{2}\right)$

Using the complementary angle identity $\tan \theta = \cot\left(\dfrac{\pi}{2} - \theta\right)$:

$\tan\left(\dfrac{\pi}{4} + \dfrac{5x}{2}\right) = \cot\left(\dfrac{\pi}{2} - \left(\dfrac{\pi}{4} + \dfrac{5x}{2}\right)\right) = \cot\left(\dfrac{\pi}{4} - \dfrac{5x}{2}\right)$

Substituting this back into the original equation:

$y = \cot^{-1}\left[\cot\left(\dfrac{\pi}{4} - \dfrac{5x}{2}\right)\right]$

$y = \dfrac{\pi}{4} - \dfrac{5x}{2}$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = \dfrac{d}{dx}\left(\dfrac{\pi}{4} - \dfrac{5x}{2}\right) = -\dfrac{5}{2}$

Answer: $-\dfrac{5}{2}$

</details>

---

### Q7. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \cot^{-1}\left(\dfrac{3x - x^3}{1 - 3x^2}\right)$ and $g(x) = \cos^{-1}\left(\dfrac{1 - x^2}{1 + x^2}\right)$, then $\lim\limits_{x \to a}\dfrac{f(x) - f(a)}{g(x) - g(a)}$, $\left(0 < a < \dfrac{1}{2}\right)$ is

**Options:**

- **(A)** $\dfrac{3}{2}$
- **(B)** $\dfrac{1}{2}$
- **(C)** $-\dfrac{3}{2}$
- **(D)** $-\dfrac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\dfrac{3}{2}$**

**Detailed Solution:**

We need to evaluate $\lim\limits_{x \to a}\dfrac{f(x) - f(a)}{g(x) - g(a)}$. This is the definition of the derivative of $f(x)$ with respect to $g(x)$ at $x = a$, which is equal to $\dfrac{f'(a)}{g'(a)}$.

Given $f(x) = \cot^{-1}\left(\dfrac{3x - x^3}{1 - 3x^2}\right)$.
Let $x = \tan \theta$. Since $0 < x < \dfrac{1}{2}$, we have $0 < \theta < \tan^{-1}\left(\dfrac{1}{2}\right) < \dfrac{\pi}{6}$.
$\dfrac{3x - x^3}{1 - 3x^2} = \dfrac{3\tan \theta - \tan^3 \theta}{1 - 3\tan^2 \theta} = \tan 3\theta$
Since $0 < 3\theta < \dfrac{\pi}{2}$, $\tan 3\theta > 0$.
$f(x) = \cot^{-1}(\tan 3\theta) = \cot^{-1}\left(\cot\left(\dfrac{\pi}{2} - 3\theta\right)\right)$
Since $\dfrac{\pi}{2} - 3\theta \in \left(0, \dfrac{\pi}{2}\right)$, it lies in the principal range of $\cot^{-1}$.
$f(x) = \dfrac{\pi}{2} - 3\theta = \dfrac{\pi}{2} - 3\tan^{-1}x$
Differentiating with respect to $x$:
$f'(x) = \dfrac{-3}{1 + x^2}$

Now, $g(x) = \cos^{-1}\left(\dfrac{1 - x^2}{1 + x^2}\right)$.
Substitute $x = \tan \theta$ again:
$\dfrac{1 - x^2}{1 + x^2} = \dfrac{1 - \tan^2 \theta}{1 + \tan^2 \theta} = \cos 2\theta$
Since $0 < 2\theta < \dfrac{\pi}{3}$, it lies in the principal range of $\cos^{-1}$.
$g(x) = \cos^{-1}(\cos 2\theta) = 2\theta = 2\tan^{-1}x$
Differentiating with respect to $x$:
$g'(x) = \dfrac{2}{1 + x^2}$

Therefore, the required limit is:
$\lim\limits_{x \to a}\dfrac{f(x) - f(a)}{g(x) - g(a)} = \dfrac{f'(a)}{g'(a)} = \dfrac{\dfrac{-3}{1 + a^2}}{\dfrac{2}{1 + a^2}} = -\dfrac{3}{2}$

Answer: $-\dfrac{3}{2}$

</details>

---

### Q8. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \cos^{-1}\left(\dfrac{1 - 4^x}{1 + 4^x}\right)$, then $\dfrac{dy}{dx}$ at $x = 1$ is

**Options:**

- **(A)** $\dfrac{4\log 2}{5}$
- **(B)** $\dfrac{\log 2}{5}$
- **(C)** $\dfrac{2\log 8}{5}$
- **(D)** $\dfrac{5\log 8}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{4\log 2}{5}$**

**Detailed Solution:**

Given $y = \cos^{-1}\left(\dfrac{1 - 4^x}{1 + 4^x}\right)$

Let $2^x = \tan \theta$. Then $4^x = (2^x)^2 = \tan^2 \theta$.

Substituting this in the given expression:

$y = \cos^{-1}\left(\dfrac{1 - \tan^2 \theta}{1 + \tan^2 \theta}\right)$

$y = \cos^{-1}(\cos 2\theta)$

Since $2^x > 0$, $\tan \theta > 0 \Rightarrow \theta \in \left(0, \dfrac{\pi}{2}\right) \Rightarrow 2\theta \in (0, \pi)$.

Thus, $y = 2\theta = 2\tan^{-1}(2^x)$.

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = 2 \cdot \dfrac{1}{1 + (2^x)^2} \cdot \dfrac{d}{dx}(2^x)$

$\dfrac{dy}{dx} = \dfrac{2}{1 + 4^x} \cdot 2^x \log 2$

At $x = 1$:

$\dfrac{dy}{dx} = \dfrac{2}{1 + 4^1} \cdot 2^1 \log 2 = \dfrac{4\log 2}{5}$

Answer: $\dfrac{4\log 2}{5}$

</details>

---

### Q9. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \cos^{-1}(\sin x)$, where $\dfrac{\pi}{2} < x < \pi$, then $\dfrac{dy}{dx} = ...$

**Options:**

- **(A)** $-1$
- **(B)** $0$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

Given $y = \cos^{-1}(\sin x)$

Differentiating with respect to $x$ using the chain rule:

$\dfrac{dy}{dx} = \dfrac{-1}{\sqrt{1 - \sin^2 x}} \cdot \dfrac{d}{dx}(\sin x)$

$\dfrac{dy}{dx} = \dfrac{-\cos x}{\sqrt{\cos^2 x}} = \dfrac{-\cos x}{|\cos x|}$

Since $\dfrac{\pi}{2} < x < \pi$, $x$ lies in the second quadrant where $\cos x < 0$.

Therefore, $|\cos x| = -\cos x$.

Substituting this into the derivative:

$\dfrac{dy}{dx} = \dfrac{-\cos x}{-\cos x} = 1$

Answer: $1$

</details>

---

### Q10. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\dfrac{d}{dx}\left[\sin^2\left\{\cot^{-1}\sqrt{\dfrac{1-x}{1+x}}\right\}\right] =$ ...

**Options:**

- **(A)** $-1$
- **(B)** $\dfrac{1}{2}$
- **(C)** $\dfrac{-1}{2}$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{2}$**

**Detailed Solution:**

Let $y = \sin^2\left\{\cot^{-1}\sqrt{\dfrac{1-x}{1+x}}\right\}$

Let $\cot^{-1}\sqrt{\dfrac{1-x}{1+x}} = \theta$

$\Rightarrow \cot \theta = \sqrt{\dfrac{1-x}{1+x}}$

$\Rightarrow \cot^2 \theta = \dfrac{1-x}{1+x}$

We know that $\sin^2 \theta = \dfrac{1}{\csc^2 \theta} = \dfrac{1}{1 + \cot^2 \theta}$

Substituting the value of $\cot^2 \theta$:

$\sin^2 \theta = \dfrac{1}{1 + \dfrac{1-x}{1+x}} = \dfrac{1+x}{1+x+1-x} = \dfrac{1+x}{2}$

Therefore, $y = \dfrac{1+x}{2}$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = \dfrac{d}{dx}\left(\dfrac{1+x}{2}\right) = \dfrac{1}{2}$

</details>

---

### Q11. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the derivative of $\tan^{-1}(a + bx)$ with respect to x at $x = 0$ is $1$, then $a^6 - b^3 = $

**Options:**

- **(A)** $3a^2 b - 1$
- **(B)** $-3ab^2 + 1$
- **(C)** $-1 - 3a^2 b$
- **(D)** $1 + 3ab^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-1 - 3a^2 b$**

**Detailed Solution:**

Let $y = \tan^{-1}(a + bx)$

Differentiating with respect to $x$, we get:

$\dfrac{dy}{dx} = \dfrac{1}{1 + (a + bx)^2} \cdot b$

Given that at $x = 0$, $\dfrac{dy}{dx} = 1$:

$\dfrac{b}{1 + a^2} = 1 \Rightarrow b = 1 + a^2 \Rightarrow a^2 - b = -1$

Cubing both sides, we get:

$(a^2 - b)^3 = (-1)^3$

$a^6 - b^3 - 3a^2b(a^2 - b) = -1$

Substituting $a^2 - b = -1$:

$a^6 - b^3 - 3a^2b(-1) = -1$

$a^6 - b^3 + 3a^2b = -1$

$a^6 - b^3 = -1 - 3a^2b$

Answer: $-1 - 3a^2 b$

</details>

---

### Q12. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\cot ^{-1}\left(\frac{x^x-x^{-x}}{2}\right)$, then the value of $\mathrm{f}^{\prime}(1)$ is equal to

**Options:**

- **(A)** -1
- **(B)** 1
- **(C)** -2
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -1**

**Detailed Solution:**

Given $\mathrm{f}(x) = \cot^{-1}\left(\dfrac{x^x - x^{-x}}{2}\right)$

Let $x^x = \tan \theta$. Then $x^{-x} = \cot \theta$.

Substituting this in the function, we get:

$\mathrm{f}(x) = \cot^{-1}\left(\dfrac{\tan \theta - \cot \theta}{2}\right)$

$\mathrm{f}(x) = \cot^{-1}\left(\dfrac{\tan^2 \theta - 1}{2\tan \theta}\right)$

$\mathrm{f}(x) = \cot^{-1}(-\cot 2\theta)$

$\mathrm{f}(x) = \pi - 2\theta$

$\mathrm{f}(x) = \pi - 2\tan^{-1}(x^x)$

Differentiating with respect to $x$:

$\mathrm{f}^{\prime}(x) = \dfrac{-2}{1 + (x^x)^2} \cdot \dfrac{d}{dx}(x^x)$

$\mathrm{f}^{\prime}(x) = \dfrac{-2}{1 + x^{2x}} \cdot x^x(1 + \ln x)$

Substituting $x = 1$:

$\mathrm{f}^{\prime}(1) = \dfrac{-2}{1 + 1^{2}} \cdot 1^1(1 + \ln 1)$

$\mathrm{f}^{\prime}(1) = \dfrac{-2}{2} \cdot 1(1 + 0) = -1$

Answer: -1

</details>

---

### Q13. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{y}=\tan ^{-1}\left(\frac{12 x-64 x^3}{1-48 x^2}\right)$, then $\frac{\mathrm{dy}}{\mathrm{d} x}=$

**Options:**

- **(A)** $\frac{3}{1+16 x^2}$
- **(B)** $\frac{4}{1+16 x^2}$
- **(C)** $\frac{12}{1+16 x^2}$
- **(D)** $\frac{1}{1+16 x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{12}{1+16 x^2}$**

**Detailed Solution:**

Given $y = \tan^{-1}\left(\dfrac{12x - 64x^3}{1 - 48x^2}\right)$

Rewrite the expression inside the bracket as:

$y = \tan^{-1}\left(\dfrac{3(4x) - (4x)^3}{1 - 3(4x)^2}\right)$

Substitute $4x = \tan\theta$, which gives $\theta = \tan^{-1}(4x)$.

$y = \tan^{-1}\left(\dfrac{3\tan\theta - \tan^3\theta}{1 - 3\tan^2\theta}\right)$

Using the trigonometric identity $\tan(3\theta) = \dfrac{3\tan\theta - \tan^3\theta}{1 - 3\tan^2\theta}$:

$y = \tan^{-1}(\tan(3\theta))$

$y = 3\theta$

Substituting back $\theta = \tan^{-1}(4x)$:

$y = 3\tan^{-1}(4x)$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = 3 \times \dfrac{1}{1 + (4x)^2} \times \dfrac{d}{dx}(4x)$

$\dfrac{dy}{dx} = 3 \times \dfrac{1}{1 + 16x^2} \times 4$

$\dfrac{dy}{dx} = \dfrac{12}{1 + 16x^2}$

Answer: $\frac{12}{1+16 x^2}$

</details>

---

### Q14. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{y}=\tan ^{-1}\left(\frac{4 x}{1+5 x^2}\right)+\cot ^{-1}\left(\frac{3-2 x}{2+3 x}\right)$, then $\frac{\mathrm{dy}}{\mathrm{d} x}$ is equal to

**Options:**

- **(A)** $\frac{5}{1+25 x^2}$
- **(B)** $\frac{1}{1+25 x^2}$
- **(C)** $\frac{1}{1+5 x^2}$
- **(D)** $\frac{5}{1+5 x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{5}{1+25 x^2}$**

**Detailed Solution:**

Given function is $y = \tan^{-1}\left(\dfrac{4x}{1+5x^2}\right) + \cot^{-1}\left(\dfrac{3-2x}{2+3x}\right)$

We can rewrite the first term by splitting the numerator and denominator:
$\tan^{-1}\left(\dfrac{4x}{1+5x^2}\right) = \tan^{-1}\left(\dfrac{5x - x}{1 + (5x)(x)}\right)$

Using the formula $\tan^{-1}\left(\dfrac{a-b}{1+ab}\right) = \tan^{-1}(a) - \tan^{-1}(b)$, we get:
$\tan^{-1}\left(\dfrac{5x - x}{1 + (5x)(x)}\right) = \tan^{-1}(5x) - \tan^{-1}(x)$

For the second term, using $\cot^{-1}(z) = \tan^{-1}\left(\dfrac{1}{z}\right)$, we have:
$\cot^{-1}\left(\dfrac{3-2x}{2+3x}\right) = \tan^{-1}\left(\dfrac{2+3x}{3-2x}\right)$

Dividing the numerator and the denominator by $3$:
$\tan^{-1}\left(\dfrac{\dfrac{2}{3} + x}{1 - \dfrac{2}{3}x}\right)$

Using the formula $\tan^{-1}\left(\dfrac{a+b}{1-ab}\right) = \tan^{-1}(a) + \tan^{-1}(b)$, we get:
$\tan^{-1}\left(\dfrac{\dfrac{2}{3} + x}{1 - \dfrac{2}{3}x}\right) = \tan^{-1}\left(\dfrac{2}{3}\right) + \tan^{-1}(x)$

Substituting these back into the original equation for $y$:
$y = \tan^{-1}(5x) - \tan^{-1}(x) + \tan^{-1}\left(\dfrac{2}{3}\right) + \tan^{-1}(x)$

$y = \tan^{-1}(5x) + \tan^{-1}\left(\dfrac{2}{3}\right)$

Differentiating with respect to $x$:
$\dfrac{dy}{dx} = \dfrac{d}{dx}[\tan^{-1}(5x)] + \dfrac{d}{dx}\left[\tan^{-1}\left(\dfrac{2}{3}\right)\right]$

$\dfrac{dy}{dx} = \dfrac{1}{1+(5x)^2} \cdot \dfrac{d}{dx}(5x) + 0$

$\dfrac{dy}{dx} = \dfrac{5}{1+25x^2}$

Answer: $\frac{5}{1+25 x^2}$

</details>

---

### Q15. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\tan ^{-1}\left(\frac{2+3 x}{3-2 x}\right)+\tan ^{-1}\left(\frac{4 x}{1+5 x^2}\right)$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}=$

**Options:**

- **(A)** $\frac{1}{1+25 x^2}$
- **(B)** $\frac{5}{1+25 x^2}$
- **(C)** $\frac{1}{1+5 x^2}$
- **(D)** $\frac{5}{1+5 x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{5}{1+25 x^2}$**

**Detailed Solution:**

Given function is $y = \tan^{-1}\left(\dfrac{2+3x}{3-2x}\right) + \tan^{-1}\left(\dfrac{4x}{1+5x^2}\right)$

Dividing the numerator and denominator of the first term by $3$, we get:

$y = \tan^{-1}\left(\dfrac{\dfrac{2}{3}+x}{1-\dfrac{2}{3}x}\right) + \tan^{-1}\left(\dfrac{5x-x}{1+(5x)(x)}\right)$

Using the inverse trigonometric identities $\tan^{-1}\left(\dfrac{a+b}{1-ab}\right) = \tan^{-1}a + \tan^{-1}b$ and $\tan^{-1}\left(\dfrac{a-b}{1+ab}\right) = \tan^{-1}a - \tan^{-1}b$:

$y = \tan^{-1}\left(\dfrac{2}{3}\right) + \tan^{-1}(x) + \tan^{-1}(5x) - \tan^{-1}(x)$

$y = \tan^{-1}\left(\dfrac{2}{3}\right) + \tan^{-1}(5x)$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = 0 + \dfrac{1}{1+(5x)^2} \cdot \dfrac{d}{dx}(5x)$

$\dfrac{dy}{dx} = \dfrac{5}{1+25x^2}$

Answer: $\frac{5}{1+25 x^2}$

</details>

---

### Q16. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\sec \left(\tan ^{-1} x\right)$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}$ at $x=1$ is equal to

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{1}{\sqrt{2}}$
- **(C)** $\sqrt{2}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{\sqrt{2}}$**

**Detailed Solution:**

Given $y = \sec(\tan^{-1} x)$

Let $\tan^{-1} x = \theta \Rightarrow \tan \theta = x$

Using the identity $\sec \theta = \sqrt{1 + \tan^2 \theta}$, we get:

$y = \sqrt{1 + x^2}$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = \dfrac{d}{dx}(\sqrt{1 + x^2}) = \dfrac{1}{2\sqrt{1 + x^2}} \cdot 2x = \dfrac{x}{\sqrt{1 + x^2}}$

Substituting $x = 1$:

$\dfrac{dy}{dx} = \dfrac{1}{\sqrt{1 + 1^2}} = \dfrac{1}{\sqrt{2}}$

Answer: $\frac{1}{\sqrt{2}}$

</details>

---

### Q17. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\sin ^{-1}\left(\frac{\log x^2}{1+(\log x)^2}\right)$, then $\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)_{x=1}=$

**Options:**

- **(A)** 2
- **(B)** $\frac{1}{2}$
- **(C)** $-\frac{2}{3}$
- **(D)** -2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

Given $y = \sin^{-1}\left(\dfrac{\log x^2}{1+(\log x)^2}\right)$

Using the property of logarithms, $\log x^2 = 2 \log x$, the equation becomes:

$y = \sin^{-1}\left(\dfrac{2 \log x}{1+(\log x)^2}\right)$

Substitute $\log x = \tan \theta$, which gives $\theta = \tan^{-1}(\log x)$.

$y = \sin^{-1}\left(\dfrac{2 \tan \theta}{1+\tan^2 \theta}\right)$

Using the trigonometric identity $\sin 2\theta = \dfrac{2 \tan \theta}{1+\tan^2 \theta}$:

$y = \sin^{-1}(\sin 2\theta) = 2\theta$

Substituting back $\theta = \tan^{-1}(\log x)$:

$y = 2 \tan^{-1}(\log x)$

Differentiating with respect to $x$:

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = 2 \cdot \dfrac{1}{1+(\log x)^2} \cdot \dfrac{\mathrm{d}}{\mathrm{d} x}(\log x)$

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = \dfrac{2}{1+(\log x)^2} \cdot \dfrac{1}{x}$

To find the value at $x = 1$, substitute $x = 1$ and $\log 1 = 0$:

$\left(\dfrac{\mathrm{d} y}{\mathrm{d} x}\right)_{x=1} = \dfrac{2}{1+(0)^2} \cdot \dfrac{1}{1} = 2$

Answer: 2

</details>

---

### Q18. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Derivative of $\tan ^{-1} \sqrt{\dfrac{1-x}{1+x}}$ w.r.t. $\cos ^{-1}\left(4 x^3-3 x\right)$ is

**Options:**

- **(A)** $\dfrac{-1}{3}$
- **(B)** $\dfrac{2}{3}$
- **(C)** $\dfrac{3}{2}$
- **(D)** $\dfrac{1}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{6}$**

**Detailed Solution:**

Let $u = \tan^{-1} \sqrt{\dfrac{1-x}{1+x}}$ and $v = \cos^{-1}(4x^3 - 3x)$

Substituting $x = \cos \theta$, we get:

$u = \tan^{-1} \sqrt{\dfrac{1-\cos \theta}{1+\cos \theta}}$

$u = \tan^{-1} \sqrt{\dfrac{2\sin^2(\dfrac{\theta}{2})}{2\cos^2(\dfrac{\theta}{2})}}$

$u = \tan^{-1} \left(\tan \dfrac{\theta}{2}\right) = \dfrac{\theta}{2} = \dfrac{1}{2} \cos^{-1} x$

Differentiating $u$ with respect to $x$:

$\dfrac{du}{dx} = \dfrac{-1}{2\sqrt{1-x^2}}$

Now, for $v$:

$v = \cos^{-1}(4\cos^3 \theta - 3\cos \theta)$

$v = \cos^{-1}(\cos 3\theta) = 3\theta = 3 \cos^{-1} x$

Differentiating $v$ with respect to $x$:

$\dfrac{dv}{dx} = \dfrac{-3}{\sqrt{1-x^2}}$

The derivative of $u$ with respect to $v$ is given by:

$\dfrac{du}{dv} = \dfrac{\dfrac{du}{dx}}{\dfrac{dv}{dx}}$

$\dfrac{du}{dv} = \dfrac{\dfrac{-1}{2\sqrt{1-x^2}}}{\dfrac{-3}{\sqrt{1-x^2}}} = \dfrac{1}{6}$

Answer: $\dfrac{1}{6}$

</details>

---

### Q19. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\sin ^2\left(\cot ^{-1} \sqrt{\dfrac{1+x}{1-x}}\right)$, then $\dfrac{\mathrm{d} y}{\mathrm{~d} x}$ has the value

**Options:**

- **(A)** $\dfrac{-1}{2}$
- **(B)** $\dfrac{1}{2}$
- **(C)** -1
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{-1}{2}$**

**Detailed Solution:**

Let $x = \cos 2\theta$.

Substituting this into the given expression:

$\sqrt{\dfrac{1+x}{1-x}} = \sqrt{\dfrac{1+\cos 2\theta}{1-\cos 2\theta}} = \sqrt{\dfrac{2\cos^2\theta}{2\sin^2\theta}} = \cot \theta$

The given function becomes:

$y = \sin^2(\cot^{-1}(\cot \theta)) = \sin^2 \theta$

Using the trigonometric identity $\sin^2 \theta = \dfrac{1 - \cos 2\theta}{2}$:

$y = \dfrac{1 - x}{2}$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = -\dfrac{1}{2}$

Answer: $\dfrac{-1}{2}$

</details>

---

### Q20. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $x^2y^2 = \mathrm{\dfrac{8}{\pi}}( \sin^{-1}x + \cos^{-1}x )$, then $\dfrac{dy}{dx}$ at $x = 1$ and $y = 2$ is

**Options:**

- **(A)** $\dfrac{1}{2}$
- **(B)** 2
- **(C)** $-\dfrac{1}{2}$
- **(D)** -2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -2**

**Detailed Solution:**

Given equation is $x^2y^2 = \dfrac{8}{\pi}( \sin^{-1}x + \cos^{-1}x )$

Using the inverse trigonometric identity $\sin^{-1}x + \cos^{-1}x = \dfrac{\pi}{2}$, the equation becomes:

$x^2y^2 = \dfrac{8}{\pi} \times \dfrac{\pi}{2}$

$x^2y^2 = 4$

Differentiating both sides with respect to $x$:

$2xy^2 + 2x^2y \dfrac{dy}{dx} = 0$

$\dfrac{dy}{dx} = -\dfrac{2xy^2}{2x^2y} = -\dfrac{y}{x}$

Substituting $x = 1$ and $y = 2$:

$\dfrac{dy}{dx} = -\dfrac{2}{1} = -2$

Answer: -2

</details>

---

### Q21. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\sin ^{-1}\left(\dfrac{3 x}{2}-\dfrac{x^3}{2}\right)$, then $\dfrac{\mathrm{d} y}{\mathrm{~d} x}$ is equal to

**Options:**

- **(A)** $\dfrac{3}{2 \sqrt{x^2-4}}$
- **(B)** $\dfrac{3}{\sqrt{4-x^2}}$
- **(C)** $\dfrac{3}{2 \sqrt{1-x^2}}$
- **(D)** $\dfrac{4}{\sqrt{4-x^2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{3}{\sqrt{4-x^2}}$**

**Detailed Solution:**

Given $y = \sin^{-1}\left(\dfrac{3x}{2} - \dfrac{x^3}{2}\right)$

Substitute $x = 2 \sin \theta \Rightarrow \theta = \sin^{-1}\left(\dfrac{x}{2}\right)$

$y = \sin^{-1}\left(\dfrac{3(2 \sin \theta)}{2} - \dfrac{(2 \sin \theta)^3}{2}\right)$

$y = \sin^{-1}(3 \sin \theta - 4 \sin^3 \theta)$

Using the trigonometric identity $\sin 3\theta = 3 \sin \theta - 4 \sin^3 \theta$, we get:

$y = \sin^{-1}(\sin 3\theta) = 3\theta$

Substituting back $\theta = \sin^{-1}\left(\dfrac{x}{2}\right)$:

$y = 3 \sin^{-1}\left(\dfrac{x}{2}\right)$

Differentiating with respect to $x$:

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = 3 \cdot \dfrac{1}{\sqrt{1 - \left(\dfrac{x}{2}\right)^2}} \cdot \dfrac{\mathrm{d}}{\mathrm{d}x}\left(\dfrac{x}{2}\right)$

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = 3 \cdot \dfrac{1}{\sqrt{1 - \dfrac{x^2}{4}}} \cdot \dfrac{1}{2}$

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{3}{2} \cdot \dfrac{2}{\sqrt{4 - x^2}} = \dfrac{3}{\sqrt{4 - x^2}}$

Answer: $\dfrac{3}{\sqrt{4-x^2}}$

</details>

---

### Q22. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If for $x \in\left(0, \dfrac{1}{4}\right)$, the derivative of $\tan ^{-1}\left(\dfrac{6 x \sqrt{x}}{1-9 x^3}\right)$ is $\sqrt{x} \cdot g(x)$, then $g(x)$ equals

**Options:**

- **(A)** $\dfrac{3 x \sqrt{x}}{1-9 x^3}$
- **(B)** $\dfrac{3 x}{1-9 x^3}$
- **(C)** $\dfrac{3}{1+9 x^3}$
- **(D)** $\dfrac{9}{1+9 x^3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{9}{1+9 x^3}$**

**Detailed Solution:**

Let $y = \tan^{-1}\left(\dfrac{6 x \sqrt{x}}{1-9 x^3}\right)$.

This can be rewritten as:

$y = \tan^{-1}\left(\dfrac{2(3 x^{3/2})}{1-(3 x^{3/2})^2}\right)$

Substitute $3 x^{3/2} = \tan \theta$. Since $x \in \left(0, \dfrac{1}{4}\right)$, we have $3 x^{3/2} \in \left(0, \dfrac{3}{8}\right)$, which means $\tan \theta < 1$ and $2\theta \in \left(0, \dfrac{\pi}{2}\right)$.

$y = \tan^{-1}\left(\dfrac{2 \tan \theta}{1-\tan^2 \theta}\right) = \tan^{-1}(\tan 2\theta) = 2\theta$

Substituting back $\theta = \tan^{-1}(3 x^{3/2})$:

$y = 2 \tan^{-1}(3 x^{3/2})$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = 2 \cdot \dfrac{1}{1+(3 x^{3/2})^2} \cdot \dfrac{d}{dx}(3 x^{3/2})$

$\dfrac{dy}{dx} = \dfrac{2}{1+9 x^3} \cdot 3 \cdot \dfrac{3}{2} x^{1/2}$

$\dfrac{dy}{dx} = \dfrac{9 \sqrt{x}}{1+9 x^3}$

Given that $\dfrac{dy}{dx} = \sqrt{x} \cdot g(x)$, we get:

$\sqrt{x} \cdot g(x) = \dfrac{9 \sqrt{x}}{1+9 x^3}$

$g(x) = \dfrac{9}{1+9 x^3}$

Answer: $\dfrac{9}{1+9 x^3}$

</details>

---

### Q23. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For $x > 0$, $\dfrac{\mathrm{d}}{\mathrm{d} x}\left(\cos ^{-1}\left(\dfrac{x-\dfrac{1}{x}}{x+\dfrac{1}{x}}\right)\right)=$

**Options:**

- **(A)** $\dfrac{x^2+1}{x^2-1}$
- **(B)** $\dfrac{2}{1+x^2}$
- **(C)** $\dfrac{-1}{1+x^2}$
- **(D)** $\dfrac{-2}{1+x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{-2}{1+x^2}$**

**Detailed Solution:**

Let $y = \cos^{-1}\left(\dfrac{x - \dfrac{1}{x}}{x + \dfrac{1}{x}}\right)$.

Simplifying the argument, we get:

$y = \cos^{-1}\left(\dfrac{x^2 - 1}{x^2 + 1}\right)$

Using the property $\cos^{-1}(-z) = \pi - \cos^{-1}(z)$, we can write:

$y = \pi - \cos^{-1}\left(\dfrac{1 - x^2}{1 + x^2}\right)$

Substitute $x = \tan \theta$. Since $x > 0$, we have $\theta \in \left(0, \dfrac{\pi}{2}\right)$.

$y = \pi - \cos^{-1}\left(\dfrac{1 - \tan^2 \theta}{1 + \tan^2 \theta}\right)$

$y = \pi - \cos^{-1}(\cos 2\theta)$

Since $0 < \theta < \dfrac{\pi}{2}$, we have $0 < 2\theta < \pi$. In this principal range, $\cos^{-1}(\cos 2\theta) = 2\theta$.

$y = \pi - 2\theta$

Substituting back $\theta = \tan^{-1} x$:

$y = \pi - 2\tan^{-1} x$

Differentiating with respect to $x$:

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = 0 - 2\left(\dfrac{1}{1 + x^2}\right) = \dfrac{-2}{1 + x^2}$

Answer: $\dfrac{-2}{1+x^2}$

</details>

---

### Q24. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\tan ^{-1}\left(\dfrac{3+2 x}{2-3 x}\right)+\tan ^{-1}\left(\dfrac{3 x}{1+4 x^2}\right)$, then $\dfrac{\mathrm{d} y}{\mathrm{~d} x}$ is equal to

**Options:**

- **(A)** $\dfrac{1}{1+16 x^2}$
- **(B)** $\dfrac{4}{1+16 x^2}$
- **(C)** $\dfrac{1}{1+4 x^2}$
- **(D)** $\dfrac{4}{1+4 x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{4}{1+16 x^2}$**

**Detailed Solution:**

Given $y = \tan^{-1}\left(\dfrac{3+2x}{2-3x}\right) + \tan^{-1}\left(\dfrac{3x}{1+4x^2}\right)$

Dividing the numerator and denominator of the first term by $2$, we get:

$y = \tan^{-1}\left(\dfrac{\dfrac{3}{2}+x}{1-\dfrac{3}{2}x}\right) + \tan^{-1}\left(\dfrac{4x-x}{1+(4x)(x)}\right)$

Using the inverse trigonometric identities $\tan^{-1}\left(\dfrac{a+b}{1-ab}\right) = \tan^{-1}(a) + \tan^{-1}(b)$ and $\tan^{-1}\left(\dfrac{a-b}{1+ab}\right) = \tan^{-1}(a) - \tan^{-1}(b)$, the equation simplifies to:

$y = \tan^{-1}\left(\dfrac{3}{2}\right) + \tan^{-1}(x) + \tan^{-1}(4x) - \tan^{-1}(x)$

$y = \tan^{-1}\left(\dfrac{3}{2}\right) + \tan^{-1}(4x)$

Differentiating both sides with respect to $x$:

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = 0 + \dfrac{1}{1+(4x)^2} \cdot \dfrac{\mathrm{d}}{\mathrm{d}x}(4x)$

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{4}{1+16x^2}$

Answer: $\dfrac{4}{1+16 x^2}$

</details>

---

### Q25. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\sec \left(\tan ^{-1} x\right)$, then $\dfrac{\mathrm{d} y}{\mathrm{~d} x}$ at $x=1$ is equal to

**Options:**

- **(A)** $\dfrac{-1}{\sqrt{2}}$
- **(B)** $\dfrac{1}{2}$
- **(C)** $\dfrac{1}{\sqrt{2}}$
- **(D)** $\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{\sqrt{2}}$**

**Detailed Solution:**

Given $y = \sec(\tan^{-1} x)$

Let $\tan^{-1} x = \theta \Rightarrow \tan \theta = x$

Since $\sec \theta = \sqrt{1 + \tan^2 \theta}$ for $\theta \in \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$, we can write:

$y = \sqrt{1 + x^2}$

Differentiating with respect to $x$:

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = \dfrac{\mathrm{d}}{\mathrm{d} x} \left( \sqrt{1 + x^2} \right) = \dfrac{1}{2\sqrt{1 + x^2}} \cdot 2x = \dfrac{x}{\sqrt{1 + x^2}}$

Substituting $x = 1$:

$\left. \dfrac{\mathrm{d} y}{\mathrm{d} x} \right|_{x=1} = \dfrac{1}{\sqrt{1 + 1^2}} = \dfrac{1}{\sqrt{2}}$

Answer: $\dfrac{1}{\sqrt{2}}$

</details>

---

### Q26. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{f}(x)=\sin ^{-1}\left(\dfrac{2.3^x}{1+9^x}\right)$, then $\mathrm{f}^{\prime}\left(\dfrac{1}{2}\right)$ equals

**Options:**

- **(A)** $-\sqrt{3} \log (\sqrt{3})$
- **(B)** $\sqrt{3} \log (\sqrt{3})$
- **(C)** $-\sqrt{3} \log 3$
- **(D)** $\sqrt{3} \log 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\sqrt{3} \log (\sqrt{3})$**

**Detailed Solution:**

Given $\mathrm{f}(x) = \sin^{-1}\left(\dfrac{2 \cdot 3^x}{1 + (3^x)^2}\right)$

Let $3^x = \tan \theta$, which gives $\theta = \tan^{-1}(3^x)$.

Then, $\mathrm{f}(x) = \sin^{-1}\left(\dfrac{2 \tan \theta}{1 + \tan^2 \theta}\right) = \sin^{-1}(\sin 2\theta)$

At $x = \dfrac{1}{2}$, we have $3^x = \sqrt{3}$.

So, $\tan \theta = \sqrt{3} \Rightarrow \theta = \dfrac{\pi}{3}$ and $2\theta = \dfrac{2\pi}{3}$.

Since $2\theta = \dfrac{2\pi}{3}$ lies in the interval $\left[\dfrac{\pi}{2}, \dfrac{3\pi}{2}\right]$, we use the property $\sin^{-1}(\sin 2\theta) = \pi - 2\theta$.

Thus, in the neighborhood of $x = \dfrac{1}{2}$, the function simplifies to:

$\mathrm{f}(x) = \pi - 2\tan^{-1}(3^x)$

Differentiating with respect to $x$:

$\mathrm{f}^{\prime}(x) = -2 \cdot \dfrac{1}{1 + (3^x)^2} \cdot \dfrac{d}{dx}(3^x)$

$\mathrm{f}^{\prime}(x) = -2 \cdot \dfrac{1}{1 + 9^x} \cdot 3^x \log 3$

Substituting $x = \dfrac{1}{2}$:

$\mathrm{f}^{\prime}\left(\dfrac{1}{2}\right) = -2 \cdot \dfrac{1}{1 + 3} \cdot \sqrt{3} \log 3$

$\mathrm{f}^{\prime}\left(\dfrac{1}{2}\right) = -\dfrac{2\sqrt{3}}{4} \log 3 = -\dfrac{\sqrt{3}}{2} \log 3$

Using the property of logarithms, $\dfrac{1}{2} \log 3 = \log(3^{1/2}) = \log(\sqrt{3})$:

$\mathrm{f}^{\prime}\left(\dfrac{1}{2}\right) = -\sqrt{3} \log(\sqrt{3})$

Answer: $-\sqrt{3} \log (\sqrt{3})$

</details>

---

### Q27. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x=\sqrt{\mathrm{e}^{\sin ^{-1} \mathrm{t}}}$ and $y=\sqrt{\mathrm{e}^{\cos ^{-1} \mathrm{t}}}$, then $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}$ is

**Options:**

- **(A)** $\frac{-y}{x^2}$
- **(B)** $\frac{y^2}{2 x^2}$
- **(C)** $\frac{2y}{x^2}$
- **(D)** $\frac{-2y}{x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2y}{x^2}$**

**Detailed Solution:**

$\begin{aligned}
x y & =\sqrt{\mathrm{e}^{\sin ^{-1} \mathrm{t}}} \cdot \sqrt{\mathrm{e}^{\cos ^{-1} \mathrm{t}}} \\
& =\sqrt{\mathrm{e}^{\sin ^{-1} \mathrm{t}+\cos ^{-1} \mathrm{t}}} \\
\therefore \quad x y & =\sqrt{\mathrm{e}^{\frac{\pi}{2}}}
\end{aligned}$
Differentiating both sides w.r.t. $x$, we get
$\begin{aligned}
& x \frac{\mathrm{d} y}{\mathrm{~d} x}+y \cdot 1=0 \\
& \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=-\frac{y}{x}...(i)
\end{aligned}$
$\begin{aligned} \Rightarrow \frac{\mathrm{d}^2 y}{\mathrm{~d} x^2} & =-\left(\frac{x \frac{\mathrm{d} y}{\mathrm{~d} x}-y \cdot 1}{x^2}\right) \\ \Rightarrow \frac{\mathrm{d}^2 y}{\mathrm{~d}^2} & =-\left(\frac{x\left(-\frac{y}{x}\right)-y}{x^2}\right)... [From (i)] \\ & =\frac{2 y}{x^2}\end{aligned}$

</details>

---

### Q28. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}^{\prime}(x)=\tan ^{-1}(\sec x+\tan x),-\frac{\pi}{2} < x < \frac{\pi}{2}$ and $f(0)=0$, then $f(1)$ is

**Options:**

- **(A)** $\frac{\pi+1}{4}$
- **(B)** $\frac{\pi+2}{4}$
- **(C)** $\pi+\frac{1}{4}$
- **(D)** $\frac{\pi-1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi+1}{4}$**

**Detailed Solution:**

$\begin{aligned} f^{\prime}(x) & =\tan ^{-1}(\sec x+\tan x) \\ & =\tan ^{-1}\left(\frac{1+\sin x}{\cos x}\right) \\ & =\tan ^{-1}\left[\frac{\left(\cos \frac{x}{2}+\sin \frac{x}{2}\right)^2}{\cos ^2 \frac{x}{2}-\sin ^2 \frac{x}{2}}\right] \\ & =\tan ^{-1}\left(\frac{\cos \frac{x}{2}+\sin \frac{x}{2}}{\cos \frac{x}{2}-\sin \frac{x}{2}}\right) \\ & =\tan ^{-1}\left[\frac{1+\tan \frac{x}{2}}{1-\tan \frac{x}{2}}\right) \\ & =\tan ^{-1}\left[\tan \left(\frac{\pi}{4}+\frac{x}{2}\right)\right]\end{aligned}$
$\begin{aligned} \therefore \quad \mathrm{f}^{\prime}(x) & =\frac{\pi}{4}+\frac{x}{2} \\ \Rightarrow \mathrm{f}(x) & =\int\left(\frac{\pi}{4}+\frac{x}{2}\right) \mathrm{d} x \\ & =\frac{\pi x}{4}+\frac{1}{2} \cdot \frac{x^2}{2}+\mathrm{c}\end{aligned}$
$\begin{array}{ll}\therefore \quad f(0)=c & \\ \Rightarrow c=0 & \ldots[\because f(0)=0 \text { (given) }]\end{array}$
$\begin{array}{r}\therefore \quad \mathrm{f}(x)=\frac{\pi x}{4}+\frac{x^2}{4} \\ \Rightarrow \mathrm{f}(1)=\frac{\pi+1}{4}\end{array}$

</details>

---

### Q29. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $y=\left(\sin ^{-1} x\right)^2+\left(\cos ^{-1} x\right)^2$, then $\left(1-x^2\right) y_2-x y_1=$

**Options:**

- **(A)** $1$
- **(B)** $4$
- **(C)** $-4$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4$**

**Detailed Solution:**

$\begin{aligned} & y=\left(\sin ^{-1} x\right)^2+\left(\cos ^{-1} x\right)^2 \\ \therefore \quad & \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{2 \sin ^{-1} x}{\sqrt{1-x^2}}-\frac{2 \cos ^{-1} x}{\sqrt{1-x^2}} \\ & \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{2\left(\sin ^{-1} x-\cos ^{-1} x\right)}{\sqrt{1-x^2}} \\ & \Rightarrow \sqrt{1-x^2} \frac{\mathrm{d} y}{\mathrm{~d} x}=2\left(\sin ^{-1} x-\cos ^{-1} x\right)\end{aligned}$
Differentiating both sides w.r.t. $x$, we get
$$
\begin{aligned}
& \quad \sqrt{1-x^2} \cdot \frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}+\frac{\mathrm{d} y}{\mathrm{~d} x} \cdot \frac{1}{2 \sqrt{1-x^2}} \cdot(-2 x) \\
& =2\left(\frac{1}{\sqrt{1-x^2}}-\frac{(-1)}{\sqrt{1-x^2}}\right)=\frac{4}{\sqrt{1-x^2}} \\
& \therefore \quad\left(1-x^2\right) \frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}-x \frac{\mathrm{d} y}{\mathrm{~d} x}=4
\end{aligned}
$$

</details>

---

### Q30. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $y=\tan ^{-1}\left(\frac{4 \sin 2 x}{\cos 2 x-6 \sin ^2 x}\right)$, then $\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)$ at $x=0$ is

**Options:**

- **(A)** 3
- **(B)** 5
- **(C)** 8
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 8**

**Detailed Solution:**

$\begin{aligned} & y=\tan ^{-1}\left(\frac{4 \sin 2 x}{\cos 2 x-6 \sin ^2 x}\right) \\ & =\tan ^{-1}\left[\frac{4(2 \sin x \cos x)}{\left(\cos ^2 x-\sin ^2 x\right)-6 \sin ^2 x}\right] \\ & =\tan ^{-1}\left(\frac{8 \sin x \cos x}{\cos ^2 x-7 \sin ^2 x}\right)\end{aligned}$
$\begin{aligned} & =\tan ^{-1}\left(\frac{8 \tan x}{1-7 \tan ^2 x}\right) \\ & =\tan ^{-1}\left(\frac{7 \tan x+\tan x}{1-7 \tan x \cdot \tan x}\right) \\ & =\tan ^{-1}(7 \tan x)+\tan ^{-1}(\tan x) \\ \therefore \quad & y=\tan ^{-1}(7 \tan x)+x \\ \therefore \quad & \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1}{1+(7 \tan x)^2} \cdot 7 \sec ^2 x+1\end{aligned}$
$\begin{gathered}=\frac{7 \sec ^2 x}{1+49 \tan ^2 x}+1 \\ \therefore \quad\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)_{x=0}= \\ =\frac{7 \sec ^2 0}{1+49 \tan ^2 0}+1 \\ =\frac{7}{1+0}+1 \\ =8\end{gathered}$

</details>

---

### Q31. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\sin ^{-1}\left(\frac{2 \log x}{1+(\log x)^2}\right)$, then $\mathrm{f}^{\prime}(\mathrm{e})$ is

**Options:**

- **(A)** $\frac{2}{\mathrm{e}}$
- **(B)** $\frac{1}{2 \mathrm{e}}$
- **(C)** $e$
- **(D)** $\frac{1}{\mathrm{e}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{\mathrm{e}}$**

**Detailed Solution:**

$\begin{aligned} & f(x)=\sin ^{-1}\left(\frac{2 \log x}{1+(\log x)^2}\right) \\ \therefore \quad f^{\prime}(x) & =\frac{1}{\sqrt{1-\left(\frac{2 \log x}{1+(\log x)^2}\right)^2}}\end{aligned}$
$\begin{aligned} & =\frac{1+(\log x)^2}{\sqrt{1+(\log x)^4+2(\log x)^2-4(\log x)^2}} \\ & \times \frac{\mathrm{d}}{\mathrm{d} x}\left(\frac{2 \log x}{1+(\log x)^2}\right) \\ & =\frac{1+(\log x)^2}{\sqrt{1-2(\log x)^2+(\log x)^4}} \\ & \times \frac{\left[1+(\log x)^2\right] \times \frac{2}{x}-(2 \log x)\left(\frac{2 \log x}{x}\right)}{\left[1+(\log x)^2\right]^2} \\ & =\frac{1}{1-(\log x)^2} \times \frac{2+2(\log x)^2-4(\log x)^2}{x\left[1+(\log x)^2\right]} \\ & =\frac{1}{1-(\log x)^2} \times \frac{2\left[1-(\log x)^2\right]}{x\left[1+(\log x)^2\right]} \\ & =\frac{2}{x\left[1+(\log x)^2\right]} \\ & \therefore \quad \mathrm{f}^{\prime}(\mathrm{e})=\frac{1}{\mathrm{e}} \\ & \end{aligned}$

</details>

---

### Q32. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\sqrt{\frac{1-\sin ^{-1}(x)}{1+\sin ^{-1}(x)}}$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}$ at $x=0$ and $y=1$ is

**Options:**

- **(A)** $-2$
- **(B)** $-1$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-1$**

**Detailed Solution:**

$$
y=\sqrt{\frac{1-\sin ^{-1}(x)}{1+\sin ^{-1}(x)}}
$$

Taking log on both sides, we get
$$
\log y=\frac{1}{2}\left[\log \left(1-\sin ^{-1} x\right)-\log \left(1+\sin ^{-1} x\right)\right]
$$
Differentiating w. r. t. $x$, we get
$$
\begin{aligned}
& \frac{1}{y} \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1}{2}\left[\frac{1}{1-\sin ^{-1} x} \cdot \frac{-1}{\sqrt{1-x^2}}-\frac{1}{1+\sin ^{-1} x} \cdot \frac{1}{\sqrt{1-x^2}}\right] \\
& \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{-y}{2 \sqrt{1-x^2}}\left(\frac{1}{1-\sin ^{-1} x}+\frac{1}{1+\sin ^{-1} x}\right) \\
& \left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)_{(0,1)}=\frac{1}{2(1)}\left(\frac{1}{1-0}+\frac{1}{1+0}\right)=-1
\end{aligned}
$$

</details>

---

### Q33. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\tan ^{-1}\left(\frac{\log \left(\frac{\mathrm{e}}{x^2}\right)}{\log \left(e x^2\right)}\right)+\tan ^{-1}\left(\frac{4+2 \log x}{1-8 \log x}\right)$, then $\frac{d y}{d x}$ is

**Options:**

- **(A)** $0$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{1}{4}$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0$**

**Detailed Solution:**

$\begin{aligned} & y=\tan ^{-1}\left(\frac{\log \left(\frac{\mathrm{e}}{x^2}\right)}{\log \left(\mathrm{ex}^2\right)}\right)+\tan ^{-1}\left(\frac{4+2 \log x}{1-8 \log x}\right) \\ & =\tan ^{-1}\left(\frac{\log \mathrm{e}-\log x^2}{\log \mathrm{e}+\log x^2}\right)+\tan ^{-1}(4)+\tan ^{-1}(2 \log x) \\ & =\tan ^{-1}\left(\frac{1-2 \log x}{1+2 \log x}\right)+\tan ^{-1}(4)+\tan ^{-1}(2 \log x) \\ & \quad=\tan ^{-1}(1)-\tan ^{-1}(2 \log x)+\tan ^{-1}(4)+\tan ^{-1}(2 \log x) \\ & \therefore \quad y=\tan ^{-1}(1)+\tan ^{-1}(4) \\ & \therefore \quad \frac{\mathrm{d} y}{\mathrm{~d} x}=0\end{aligned}$

</details>

---

### Q34. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\cos ^{-1}\left(\frac{\mathrm{a}^2}{\sqrt{x^4+\mathrm{a}^4}}\right)$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}$ is

**Options:**

- **(A)** $\frac{2 \mathrm{a}^2 x}{x^4+\mathrm{a}^4}$
- **(B)** $\frac{2 a^2 x^2}{\sqrt{x^4+a^4}}$
- **(C)** $\frac{a^4 x^4}{x^4+a^4}$
- **(D)** $\frac{a^4 x^2}{2 \sqrt{x^4+a^4}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2 \mathrm{a}^2 x}{x^4+\mathrm{a}^4}$**

**Detailed Solution:**

$y=\cos ^{-1}\left(\frac{\mathrm{a}^2}{\sqrt{x^4+\mathrm{a}^4}}\right)$
Put $x^2=\mathrm{a}^2 \tan \theta$
$\begin{aligned}
& \therefore \quad \theta=\tan ^{-1}\left(\frac{x^2}{\mathrm{a}^2}\right) \\
& \therefore \quad y=\cos ^{-1}\left(\frac{\mathrm{a}^2}{\sqrt{\mathrm{a}^4 \tan ^2 \theta+\mathrm{a}^4}}\right) \\
& \Rightarrow y=\cos ^{-1}\left(\frac{\mathrm{a}^2}{\sqrt{\mathrm{a}^4\left(1+\tan ^2 \theta\right)}}\right) \\
& \Rightarrow y=\cos ^{-1}\left(\frac{1}{\sec \theta}\right) \\
& \Rightarrow y=\cos ^{-1}(\cos \theta) \\
& \Rightarrow y=\theta \\
& \Rightarrow y=\tan ^{-1}\left(\frac{x^2}{\mathrm{a}^2}\right)
\end{aligned}$
Differentiating w.r.t. $x$, we get
$\begin{aligned}
\frac{\mathrm{d} y}{\mathrm{~d} x} & =\frac{1}{1+\left(\frac{x^2}{\mathrm{a}^2}\right)^2} \cdot \frac{\mathrm{d}}{\mathrm{d} x}\left(\frac{x^2}{\mathrm{a}^2}\right) \\
& =\frac{\mathrm{a}^4}{\mathrm{a}^4+x^4} \cdot \frac{2 x}{\mathrm{a}^2} \\
& =\frac{2 \mathrm{a}^2 x}{x^4+\mathrm{a}^4}
\end{aligned}$

</details>

---

### Q35. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For $x \in\left(0, \frac{1}{4}\right)$, if the derivative of $\tan ^{-1}\left(\frac{6 x \sqrt{x}}{1-9 x^3}\right)$ is $\sqrt{x} \cdot g(x)$, then $g(x)$ equals

**Options:**

- **(A)** $\frac{9}{1+9 x^3}$
- **(B)** $\frac{3 x}{1-9 x^3}$
- **(C)** $\frac{3 x \sqrt{x}}{1-9 x^3}$
- **(D)** $\frac{3}{1+9 x^3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{9}{1+9 x^3}$**

**Detailed Solution:**

$\begin{aligned} & y=\tan ^{-1}\left(\frac{6 x \sqrt{x}}{1-9 x^3}\right)=\tan ^{-1}\left\{\frac{2\left(3 x^{\frac{3}{2}}\right)}{1-\left(3 x^{\frac{3}{2}}\right)^2}\right\}=2 \tan ^{-1}\left(3 x^{\frac{3}{2}}\right) \\ & \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=2 \times \frac{1}{1+9 x^3} \times 3 \times \frac{3}{2} \sqrt{x}=\frac{9}{1+9 x^3} \cdot \sqrt{x} \\ & \Rightarrow g(x)=\frac{9}{1+9 x^3}\end{aligned}$

</details>

---

### Q36. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The domain of the derivative of the functions $f(x)\left\{\begin{array}{cc}\tan ^{-1} x, & \text { if }|x| \leq 1 \\ \frac{1}{2}(|x|-1), & \text { if }|x|>1\end{array}\right.$ is given by

**Options:**

- **(A)** $R-\{1\}$
- **(B)** $R-\{0\}$
- **(C)** $R-\{-1,1\}$
- **(D)** $R-\{-1\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $R-\{-1,1\}$**

**Detailed Solution:**

$\begin{aligned} & f(x) \begin{cases}\frac{1}{2}(-x-1) & x<-1 \\ \tan ^{-1} x & -1 \leq x \leq 1 \\ \frac{1}{2}(x-1) & x>1\end{cases} \\ & \Rightarrow f^{\prime}(x) \begin{cases}-\frac{1}{2} & x<-1 \\ \frac{1}{1+x^2} & -1<x<1 \\ \frac{1}{2} & x>1\end{cases} \end{aligned}$
$\because f(x)$ discontinuous at $x=-1$ and $x=1$
Hence $f(x)$ is not differentiable at $x=-1$ and $x=1$

</details>

---

### Q37. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\sin ^{-1}\left(\frac{2 x}{1+x^2}\right)+\cos ^{-1}\left(\frac{1-x^2}{1+x^2}\right), x \in(1, \infty)$, then $f^{\prime}(x)$

**Options:**

- **(A)** $\frac{-4}{1+x^2}$
- **(B)** 0
- **(C)** $\frac{2 x}{1-x^2}$
- **(D)** $\frac{4}{1+x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0**

**Detailed Solution:**

$\begin{aligned} & f(x)=\sin ^{-1}\left(\frac{2 x}{1+x^2}\right)+\cos ^{-1}\left(\frac{1-x^2}{1+x^2}\right) \\ & \Rightarrow f(x)=\sin ^{-1}\left(\frac{2 \tan \theta}{1+\tan ^2 \theta}\right)+\cos ^{-1}\left(\frac{1-\tan ^2 \theta}{1+\tan ^2 \theta}\right) \\ & \Rightarrow f(x)=\sin ^{-1}(\sin 2 \theta)+\cos ^{-1}(\cos 2 \theta) \\ & \Rightarrow f(x)=\pi-2 \theta+2 \theta=\pi \\ & \Rightarrow f^{\prime}(x)=0\end{aligned}$

</details>

---

### Q38. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\tan ^{-1}\left(\frac{5 x+1}{3-x-6 x^2}\right)$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{3}{9 x^2+12 x+5}+\frac{1}{2 x^2-2 x+1}$
- **(B)** $\frac{1}{9 x^2+12 x+5}+\frac{1}{4 x^2-4 x+2}$
- **(C)** $\frac{1}{9 x^2+12 x+5}-\frac{1}{4 x^2-4 x+2}$
- **(D)** $\frac{3}{9 x^2+12 x+5}-\frac{1}{2 x^2-2 x+1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3}{9 x^2+12 x+5}+\frac{1}{2 x^2-2 x+1}$**

**Detailed Solution:**

$\begin{aligned} & y=\tan ^{-1}\left(\frac{5 x+1}{3-x-6 x^2}\right)=\tan ^{-1} \frac{(3 x+2)+(2 x-1)}{1-(3 x+2)(2 x-1)} \\ & \Rightarrow y=\tan ^{-1}(3 x+2)+\tan ^{-1}(2 x-1) \\ & \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1}{1+(3 x+2)} \times 3+\frac{1}{1+(2 x-1)^2} \times 2 \\ & \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{3}{9 x^2+12 x+5}+\frac{2}{4 x^2-4 x+2} \\ & \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{3}{9 x^2+12 x+5}+\frac{1}{2 x^2-2 x+1}\end{aligned}$

</details>

---

### Q39. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\tan ^{-1}\left(\frac{4 x}{1+5 x^2}\right)+\tan ^{-1}\left(\frac{3+8 x}{3-3 x}\right)$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{1}{1+25 x^2}$
- **(B)** $\frac{5}{1+25 x^2}$
- **(C)** $\frac{1}{1+5 x^2}$
- **(D)** $\frac{5}{1+5 x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{5}{1+25 x^2}$**

**Detailed Solution:**

$\begin{aligned} & y=\tan ^{-1}\left(\frac{4 x}{1+5 x^2}\right)+\tan ^{-1}\left(\frac{3+8 x}{8-3 x}\right)=\tan ^{-1}\left(\frac{5 x-x}{1+5 x \cdot x}\right)+\tan ^{-1}\left(\frac{\frac{3}{8}+x}{1-\frac{3}{8} \cdot x}\right) \\ & =\tan ^{-1}(5 x)-\tan ^{-1}(x)+\tan ^{-1}\left(\frac{3}{8}\right)+\tan ^{-1}(x) \\ & \Rightarrow y=\tan ^{-1}(5 x)+\tan ^{-1}\left(\frac{3}{8}\right) \\ & \Rightarrow \frac{d y}{d x}=\frac{1}{1+(5 x)^2} \times 5+0=\frac{5}{1+25 x^2}\end{aligned}$

</details>

---

### Q40. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $y=\sin ^{-1}\left(\frac{5 x+12 \sqrt{1-x^2}}{13}\right)$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{2}{\sqrt{1-x^2}}$
- **(B)** $\frac{x}{\sqrt{1-x^2}}$
- **(C)** $\frac{-1}{\sqrt{1-x^2}}$
- **(D)** $\frac{-x}{\sqrt{1-x^2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{-1}{\sqrt{1-x^2}}$**

**Detailed Solution:**

$\begin{aligned} & y=\sin ^{-1}\left(\frac{5 x+12 \sqrt{1-x^2}}{13}\right) \\ & \Rightarrow y=\sin -1\left(x \cdot \frac{5}{13}+\frac{12}{13} \sqrt{1-x^2}\right)\end{aligned}$
[let $x=\sin \theta$ i.e., $\theta=\sin ^{-1} X$ and $\cos \theta=\sqrt{1-X^2}$
also let $\frac{5}{13}=\cos \alpha$ i.e. $\left.\frac{12}{13}=\sin \alpha\right]$
$\begin{aligned} & \Rightarrow y=\sin ^{-1}(\sin \theta \cdot \cos \alpha+\cos \theta \cdot \sin \alpha) \\ & \Rightarrow y=\sin -1 \sin (\theta+\alpha) \\ & \Rightarrow \frac{d y}{d x}=\frac{1}{\sqrt{1-x^2}}+0=\frac{1}{\sqrt{1-x^2}}\end{aligned}$

</details>

---

### Q41. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $y=\sec ^{-1}\left(\frac{x+x^{-1}}{x-x^{-1}}\right)$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{-1}{1+x^2}$
- **(B)** $\frac{-2}{1+x^2}$
- **(C)** $\frac{2}{1-x^2}$
- **(D)** $\frac{1}{1+x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-2}{1+x^2}$**

**Detailed Solution:**

$\begin{aligned} & y=\sec ^{-1}\left(\frac{x+x^{-1}}{x-x^{-1}}\right)=\sec ^{-1}\left(\frac{x^2+1}{x^2-1}\right)=\sec ^{-1}\left(-\frac{1+x^2}{1-x^2}\right) \\ & \Rightarrow y=\sec ^{-1}\left(-\frac{1+\tan ^2 \theta}{1-\tan ^2 \theta}\right)=\sec ^{-1}\left(\frac{-1}{\cos 2 \theta}\right)=\sec ^{-1}(-\sec 2 \theta) \\ & \Rightarrow y=\pi-2 \theta=\pi-2 \tan ^{-1} x \\ & \Rightarrow \frac{d y}{d x}=0-\frac{2}{1+x^2}\end{aligned}$

</details>

---

### Q42. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\sin \left(2 \tan ^{-1} \sqrt{\frac{1+x}{1-x}}\right)$, then $\frac{d y}{d x}$ is equal to

**Options:**

- **(A)** $\frac{-1}{\sqrt{1-x^2}}$
- **(B)** $\frac{-x}{\sqrt{1-x^2}}$
- **(C)** $\frac{1}{\sqrt{1-x^2}}$
- **(D)** $\frac{-2 x}{\sqrt{1-x^2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-x}{\sqrt{1-x^2}}$**

**Detailed Solution:**

$\begin{aligned} & y=\sin \left(2 \tan ^{-1} \sqrt{\frac{1+x}{1-x}}\right) \\ & \Rightarrow y=\sin \left(2 \tan ^{-1}\left(\cot \frac{\theta}{2}\right)\right)[\text { let } x=\cos \theta] \\ & \Rightarrow y=\sin \left(2 \tan ^{-1}\left\{\tan \left(\frac{\pi}{2}-\frac{\theta}{2}\right)\right\}\right) \\ & \Rightarrow y=\sin \left(2\left(\frac{\pi}{2}-\frac{\theta}{2}\right)\right) \\ & \Rightarrow y=\sin (\pi-\theta)=\sin \theta=\sqrt{1-x^2}\end{aligned}$
$\Rightarrow \frac{d y}{d x}=\frac{1}{2 \sqrt{1-x^2}} \times(-2 x)=\frac{-x}{\sqrt{1-x^2}}$

</details>

---

### Q43. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\tan ^{-1}(\sec x-\tan x)$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $2$
- **(B)** $-\frac{1}{2}$
- **(C)** $\frac{1}{2}$
- **(D)** $-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{1}{2}$**

**Detailed Solution:**

$\begin{aligned} & y=\tan ^{-1}(\sec x-\tan x)=\tan ^{-1}\left(\frac{1-\sin x}{\cos x}\right)=\tan ^{-1}\left(\frac{\cos \frac{x}{2}-\sin \frac{x}{2}}{\cos \frac{x}{2}+\sin \frac{x}{2}}\right) \\ & \Rightarrow y=\tan ^{-1}\left(\frac{1-\tan \frac{x}{2}}{1+\tan \frac{x}{2}}\right)=\tan ^{-1}\left(\tan \left(\frac{\pi}{4}-\frac{x}{2}\right)\right)=\frac{\pi}{4}-\frac{x}{2} \\ & \Rightarrow \frac{d y}{d x}=\frac{-1}{2}\end{aligned}$

</details>

---

### Q44. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}^{\prime}(\mathrm{x})=\tan ^{-1}(\sec \mathrm{x} \tan \mathrm{x}), \frac{-\pi}{2}<\mathrm{x}<\frac{\pi}{2}$ and $\mathrm{f}(0)=0$, then $\mathrm{f}(1)=$

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{\pi-1}{4}$
- **(C)** $\frac{\pi+1}{4}$
- **(D)** $\frac{\pi+2}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi+1}{4}$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{f}^{\prime}(\mathrm{x})=\tan ^{-1}(\sec \mathrm{x}+\tan \mathrm{x})=\tan ^{-1}\left(\frac{1+\sin \mathrm{x}}{\cos \mathrm{x}}\right) \\ & =\tan ^{-1}\left(\frac{\cos \frac{\mathrm{x}}{2}+\sin \frac{\mathrm{x}}{2}}{\cos \frac{\mathrm{x}}{2}-\sin \frac{\mathrm{x}}{2}}\right)=\tan ^{-1}\left(\tan \left(\frac{\pi}{4}+\frac{\mathrm{x}}{2}\right)\right) \\ & =\frac{\pi}{4}+\frac{\mathrm{x}}{2}\end{aligned}$
Now $f(x)=\int f^{\prime}(x) d x=\int\left(\frac{\pi}{4}+\frac{x}{2}\right) d x=\frac{\pi}{4} x+\frac{x^2}{4}+C$
$$
\because \mathrm{f}(0)=0 \Rightarrow \mathrm{c}=0
$$
Hence, $f(x)=\frac{x^2+\pi x}{4}$
$$
\Rightarrow \mathrm{f}(1)=\frac{1^2+\pi \times 1}{4}=\frac{\pi+1}{4}
$$

</details>

---

### Q45. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $y=\tan ^{-1} \sqrt{\frac{1+\cos x}{1-\cos x}}$, then $\frac{d y}{d x}$ is

**Options:**

- **(A)** $\frac{3}{2}$
- **(B)** $\frac{-1}{2}$
- **(C)** $-1$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-1}{2}$**

**Detailed Solution:**

$\begin{aligned} & y=\tan ^{-1} \sqrt{\frac{1+\cos x}{1-x \cos x}}=\tan ^{-1} \sqrt{\frac{2 \cos ^2 \frac{x}{2}}{2 \sin ^2 \frac{x}{2}}}=\tan ^{-1}\left(\cot \frac{x}{2}\right) \\ & \Rightarrow y=\tan ^{-1} \tan \left(\frac{\pi}{2}-\frac{x}{2}\right)=\frac{\pi}{2}-\frac{x}{2}\end{aligned}$
Differentiating
$\frac{\mathrm{dy}}{\mathrm{dx}}=0-\frac{1}{2}=\frac{-1}{2}$

</details>

---

### Q46. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\frac{d}{d x}\left(\sin ^{-1}\left(3 x-4 x^3\right)\right), \frac{1}{2}<x<1$ is

**Options:**

- **(A)** $\frac{1}{3 \sqrt{1-x^2}}$
- **(B)** $\frac{-3}{\sqrt{1-x^2}}$
- **(C)** $\frac{-1}{3 \sqrt{1-x^2}}$
- **(D)** $\frac{3}{\sqrt{1-x^2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-3}{\sqrt{1-x^2}}$**

**Detailed Solution:**

$\begin{aligned} & \frac{\mathrm{d}\left(\sin ^{-1}\left(3 \mathrm{x}-4 \mathrm{x}^3\right)\right)}{\mathrm{dx}} \\ & =\frac{\mathrm{d}\left(\pi-3 \sin ^{-1} \mathrm{x}\right)}{\mathrm{dx}}\left[\text { as } \frac{1}{2}<\mathrm{x}<1\right]=\frac{-3}{\sqrt{1-\mathrm{x}^2}}\end{aligned}$

</details>

---

### Q47. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{y}=y=e^{\cos ^{-1}\left(\sqrt{1-x^2}\right)}$, then $\frac{1}{y} \frac{d y}{d x}$

**Options:**

- **(A)** $\frac{\sqrt{1-x^2}}{2}$
- **(B)** $\sqrt{1-x^2}$
- **(C)** $\frac{1}{\sqrt{1-x^2}}$
- **(D)** $\frac{1}{2 \sqrt{1-x^2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{\sqrt{1-x^2}}$**

**Detailed Solution:**

$\begin{aligned} & y=e^{\cos ^{-1}\left(\sqrt{1-x^2}\right)} \\ & \Rightarrow \log _e y=\cos ^{-1} \sqrt{1-x^2}\end{aligned}$
Diff. w.r.t. $\mathrm{x}$
$\frac{1}{y} \cdot \frac{d y}{d x}=\frac{-1}{\sqrt{1-\left(1-x^2\right)}} \times \frac{1}{2 \sqrt{1-x^2}} \times(-2 x)=\frac{2 x}{2 \sqrt{x^2} \sqrt{1-x^2}}=\frac{1}{\sqrt{1-x^2}}$

</details>

---

### Q48. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of the function $\cot ^{-1}[\cos 2 x]^{1 / 2}$ at $x=\pi / 6$ is

**Options:**

- **(A)** $\left(\frac{1}{3}\right)^{1 / 2}$
- **(B)** $\left(\frac{2}{3}\right)^{1 / 2}$
- **(C)** $\left(\frac{3}{2}\right)^{1 / 2}$
- **(D)** $(3)^{1 / 2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\frac{2}{3}\right)^{1 / 2}$**

**Detailed Solution:**

$\begin{aligned} & f(x)=\cot ^{-1}\left[(\cot 2 x)^{\frac{1}{2}}\right]=\cot ^{-1}(\sqrt{\cos 2 x}) \\ & \therefore \quad f^{\prime}(x)=\frac{-1}{1+(\sqrt{\cos 2 x})^2} \times \frac{d}{d x}(\sqrt{\cos 2 x}) \\ & =\frac{-1}{1+\cos 2 x} \times \frac{1}{2 \sqrt{\cos 2 x}} \times(-2 \sin 2 x)=\frac{2 \sin 2 x}{2(1+\cos 2 x) \sqrt{\cos 2 x}} \\ & \therefore \quad\left[f^{\prime}(x)\right]_{x=\frac{\pi}{6}}=\frac{\sin \left(\frac{\pi}{3}\right)}{\left(1+\cos \frac{\pi}{3}\right) \sqrt{\cos \frac{\pi}{3}}}=\left(\frac{2}{3}\right)^{\frac{1}{2}}\end{aligned}$

</details>

---

### Q49. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $y=\tan ^{-1}\left[\frac{\log \left(\frac{\mathrm{e}}{\mathrm{x}^2}\right)}{\log \left(\mathrm{ex}^2\right)}\right]+\tan ^{-1}\left[\frac{3+2 \log \mathrm{x}}{1-6 \log \mathrm{x}}\right]$, then $\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{dx}^2}=$

**Options:**

- **(A)** $\frac{2}{1+x^2}$
- **(B)** $\frac{1}{1+x^2}$
- **(C)** $\frac{3}{1+x^2}$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

$\begin{aligned} & y=\tan ^{-1}\left[\frac{\log \left(\frac{\mathrm{e}}{\mathrm{x}^2}\right)}{\log \left(\mathrm{ex}^2\right)}\right]+\tan ^{-1}\left[\frac{3+2 \log x}{1-6 \log x}\right] \\ & =\tan ^{-1}\left[\frac{\log \mathrm{e}-\log \mathrm{x}^2}{\log \mathrm{e}+\log \mathrm{x}^2}\right]+\tan ^{-1} 3+\tan ^{-1}(2 \log \mathrm{x}) \\ & =\tan ^{-1}\left[\frac{1-\log \mathrm{x}^2}{1+\log \mathrm{x}^2}\right]+\tan ^{-1} 3+\tan ^{-1}\left(\log \mathrm{x}^2\right) \\ & =\tan ^{-1}(1)-\tan ^{-1}\left(\log \mathrm{x}^2\right)+\tan ^{-1} 3+\tan ^{-1}\left(\log \mathrm{x}^2\right) \\ & =\tan ^{-1}(1)+\tan ^{-1}(3) \\ & \therefore \frac{\mathrm{dy}}{\mathrm{dx}}=0 \Rightarrow \frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{dx}^2}=0\end{aligned}$

</details>

---

### Q50. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\tan ^{-1} \sqrt{\frac{1+\cos x}{1-\cos x}}$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $1$
- **(B)** $\frac{3}{2}$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{-1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2}$**

**Detailed Solution:**

$\begin{aligned} & y=\tan ^{-1} \sqrt{\frac{1+\cos x}{1-\cos x}} \\ & =\tan ^{-1} \sqrt{\frac{2 \cos ^2 \frac{x}{2}}{2 \sin ^2 \frac{x}{2}}}=\tan ^{-1}\left(\cot \frac{x}{2}\right)=\tan ^{-1}\left[\tan \left(\frac{\pi}{2}-\frac{x}{2}\right)\right]=\frac{\pi}{2}-\frac{x}{2} \\ & \therefore \frac{d y}{d x}=0-\frac{1}{2}=\frac{-1}{2}\end{aligned}$

</details>

---

### Q51. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\tan ^{-1}\left(\sqrt{\frac{1+\sin x}{1-\sin x}}\right), 0 \leq x < \frac{\pi}{2}$, then $\frac{d y}{d x}$ at $x=\frac{\pi}{6}$ is

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{-1}{4}$
- **(C)** $\frac{-3}{2}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{2}$**

**Detailed Solution:**

$\begin{aligned} & y=\tan ^{-1}\left(\sqrt{\frac{1+\sin x}{1-\sin x}}\right) \\ & =\tan ^{-1}\left[\sqrt{\frac{\left(\cos \frac{x}{2}+\sin \frac{x}{2}\right)^2}{\left(\cos \frac{x}{2}-\sin \frac{x}{2}\right)^2}}\right]=\tan ^{-1}\left[\frac{\left(\cos \frac{x}{2}+\sin \frac{x}{2}\right)^2}{\left(\cos \frac{x}{2}-\sin \frac{x}{2}\right)^2}\right] \\ & =\tan ^{-1}\left(\frac{1+\tan \frac{x}{2}}{1-\tan \frac{x}{2}}\right) \\ & =\tan ^{-1}\left(\frac{\tan \frac{\pi}{4}+\tan \frac{x}{2}}{1-\tan \frac{\pi}{4} \cdot \tan \frac{x}{2}}\right) \\ & =\tan ^{-1}\left[\tan \left(\frac{\pi}{4}+\frac{x}{2}\right)\right]=\frac{\pi}{4}+\frac{x}{2} \\ & \therefore \frac{\mathrm{dy}}{\mathrm{dx}}=\frac{1}{2} \\ & \end{aligned}$

</details>

---

### Q52. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\tan ^{-1}\left[\frac{1}{1+x+x^2}\right]+\tan ^{-1}\left[\frac{1}{x^2+3 x+3}\right], x>0$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{1}{1+x^2}-\frac{1}{1+(x+2)^2}$
- **(B)** $\frac{-1}{1+x^2}+\frac{1}{1+(x+2)^2}$
- **(C)** $\frac{1}{1+x^2}+\frac{1}{1+(x+2)^2}$
- **(D)** $\frac{-1}{1+\mathrm{x}^2}-\frac{1}{1+(\mathrm{x}+2)^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-1}{1+x^2}+\frac{1}{1+(x+2)^2}$**

**Detailed Solution:**

$\begin{aligned} & y=\tan ^{-1}\left[\frac{1}{1+x+x^2}\right]+\tan ^{-1}\left[\frac{1}{x^2+3 x+3}\right] \\ & =\tan ^{-1}\left[\frac{1}{1+x(1+x)}\right]+\tan ^{-1}\left[\frac{1}{1+(x+2)(x+1)}\right] \\ & =\tan ^{-1}\left[\frac{(x+1)-1}{1+(x+1) x)}\right]+\tan ^{-1}\left[\frac{(x+2)-(x+1)}{1+(x+2)(x+1)}\right] \\ & =\tan ^{-1}(\mathrm{x}+1)-\tan ^{-1}(\mathrm{x}+2)-\tan ^{-1}(\mathrm{x}+1) \\ & =\tan ^{-1}(\mathrm{x}+2)-\tan ^{-1}(\mathrm{x}) \\ & \therefore \frac{\mathrm{dy}}{\mathrm{dx}}=\frac{1}{1+(\mathrm{x}+2)^2}-\frac{1}{1+\mathrm{x}^2} \\ & \end{aligned}$

</details>

---

### Q53. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\tan ^{-1}\left\{\frac{a \cos x-b \sin x}{b \cos x+a \sin x}\right\}$, then $\frac{d y}{d x}$

**Options:**

- **(A)** $\frac{1}{1+x^2}$
- **(B)** $\frac{1}{\sqrt{1-x^2}}$
- **(C)** -1
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) -1**

**Detailed Solution:**

$$
y=\tan ^{-1}\left\{\frac{a \cos x-b \sin x}{b \cos x+a \sin x}\right\}
$$
Put $a=r \cos \alpha, b=r \sin \alpha$
$$
\begin{aligned}
& \therefore y=\tan ^{-1}\left\{\frac{r(\cos x \cos \alpha-\sin x \sin \alpha)}{r(\sin \alpha \cos x+\cos \alpha \sin x)}\right\} \\
& =\tan ^{-1}\left[\frac{\cos (x+\alpha)}{\sin (x+\alpha)}\right]=\tan ^{-1}[\cot (x+\alpha)] \\
& =\tan ^{-1}\left\{\tan \left[\frac{\pi}{2}-(x+\alpha)\right]\right\}=\frac{\pi}{2}-(x+\alpha) \\
& \therefore \frac{d y}{d x}=0-(1+0)=-1
\end{aligned}
$$

</details>

---

### Q54. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\operatorname{cosec}^1\left[\frac{\sqrt{x}+1}{\sqrt{x-1}}\right]+\cos ^{-1}\left[\frac{\sqrt{x}-1}{\sqrt{x}+1}\right]$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** $\frac{2}{\sqrt{x}+1}$
- **(D)** $\frac{1}{2(\sqrt{\mathrm{x}}+1)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

$$
\begin{aligned}
& y=\operatorname{cosec}^{-1}\left(\frac{\sqrt{x}+1}{\sqrt{x}-1}\right)+\cos ^{-1}\left(\frac{\sqrt{x}-1}{\sqrt{x}+1}\right)=\sin ^{-1}\left(\frac{\sqrt{x}-1}{\sqrt{x}+1}\right)+\cos ^{-1}\left(\frac{\sqrt{x}-1}{\sqrt{x}+1}\right)=\frac{\pi}{2} \\
& \therefore \frac{d y}{d x}=0
\end{aligned}
$$

</details>

---

### Q55. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$$
\text { If } y=\sin ^{-1}\left[\cos \sqrt{\frac{1+x}{2}}\right]+x^x \text {, then } \frac{d y}{d x} \text { at } x=1 \text { is }
$$

**Options:**

- **(A)** $\frac{5}{4}$
- **(B)** $\frac{-1}{4}$
- **(C)** $\frac{3}{4}$
- **(D)** $\frac{-5}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{4}$**

**Detailed Solution:**

$$
\begin{aligned}
& \sin ^{-1}\left[\cos \sqrt{\frac{1+x}{2}}\right]+x^x \\
& =\sin ^{-1}\left[\sin \left(\frac{\pi}{2}-\sqrt{\frac{1+x}{2}}\right)\right]+x^x \\
& =\frac{\pi}{2}-\sqrt{\frac{1+x}{2}+x^x} \\
& \therefore \frac{d y}{d x}=0-\frac{1}{\sqrt{2}} \cdot \frac{d}{d x}(\sqrt{1+x})+\frac{d}{d x}\left(x^x\right)
\end{aligned}
$$
Let $\mathrm{u}=\mathrm{x}^{\mathrm{x}} \Rightarrow \log \mathrm{u}=\mathrm{x} \log \mathrm{x}$


$$
\begin{aligned}
& \therefore \frac{1}{u} \frac{d u}{d x}=\frac{x}{x}+\log x \Rightarrow \frac{d y}{d x}=x^x(1+\log x) \\
& \therefore \frac{d y}{d x}=\frac{-1}{\sqrt{2}}\left[\frac{1}{2 \sqrt{1+x}}\right]+x^x(1+\log x) \\
& \therefore\left[\frac{d y}{d x}\right]_{x=1}=\left(\frac{-1}{\sqrt{2}}\right)\left(\frac{1}{2 \sqrt{2}}\right)+1=\frac{-1}{4}+1=\frac{3}{4}
\end{aligned}
$$

</details>

---

### Q56. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\sec \left(\tan ^{-1} x\right)$, then $\frac{d y}{d x}$ at $x=1$ is

**Options:**

- **(A)** $\sqrt{2}$
- **(B)** $\frac{1}{2}$
- **(C)** $1$
- **(D)** $\frac{1}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{\sqrt{2}}$**

**Detailed Solution:**

$$
\begin{array}{l}
y=\sec \left(\tan ^{-1} x\right) \\
\therefore \frac{d y}{d x}=\sec \left(\tan ^{-1} x\right) \tan \left(\tan ^{-1} x\right) \cdot \frac{1}{1+x^{2}} \\
\text { At } x=1, \frac{d y}{d x}=\sec \frac{\pi}{4} \tan \frac{\pi}{4}\left(\frac{1}{2}\right) \\
=\frac{1}{2} \times \sqrt{2} \times 1=\frac{1}{\sqrt{2}}
\end{array}
$$
This problem can also be solved as follows :
$$
\begin{array}{l}
y=\sec \left(\tan ^{-1} x\right)=\sec \left(\sec ^{-1} \sqrt{1+x^{2}}\right)=\sqrt{1+x^{2}} \\
\therefore \frac{d y}{d x}=\frac{1}{2 \sqrt{1+x^{2}}} \times 2 x=\frac{x}{\sqrt{1+x^{2}}} \\
\therefore\left(\frac{d y}{d x}\right)_{x=1}=\frac{1}{\sqrt{2}}
\end{array}
$$

</details>

---

### Q57. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{y}=\sin ^{-1}\left[\frac{\sqrt{1+x}+\sqrt{1-x}}{2}\right]$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\left(-\frac{1}{2}\right) \frac{1}{\sqrt{1-x^{2}}}$
- **(B)** $\left(-\frac{1}{2}\right) \frac{1}{\sqrt{x^{2}-1}}$
- **(C)** $\left(\frac{1}{4}\right) \frac{1}{\sqrt{x^{2}-1}}$
- **(D)** $\left(\frac{1}{4}\right) \frac{1}{\sqrt{1-x^{2}}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(-\frac{1}{2}\right) \frac{1}{\sqrt{1-x^{2}}}$**

**Detailed Solution:**

The equation of tangent at $P(-4,-4)$ on the curve $x^{2}=-4 y$ is
(A) $3 x-y+8=0$
(B) $2 x+y+4=0$
(C) $2 x+y-4=0$
(D) $2 x-y+4=0$

</details>

---

### Q58. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\sin ^{-1}\left(\sqrt{\frac{1-x}{2}}\right)$, then $f^{\prime}(x)=$

**Options:**

- **(A)** $\frac{-1}{2 \sqrt{1-x^{2}}}$
- **(B)** $\frac{1}{\sqrt{1-x^{2}}}$
- **(C)** $\frac{-1}{2 \sqrt{1+x^{2}}}$
- **(D)** $\frac{1}{2 \sqrt{1+x^{2}}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{-1}{2 \sqrt{1-x^{2}}}$**

**Detailed Solution:**

(B)
$\frac{d}{d x}\left[\sin ^{-1}\left(\sqrt{\frac{1-x}{2}}\right)\right]=\frac{1}{\sqrt{1-\left(\sqrt{\frac{1-x}{2}}\right)^{2}}} \cdot \frac{d}{d x}\left(\sqrt{\frac{1-x}{2}}\right)$
$=\frac{1}{\sqrt{1-\frac{1-x}{2}}} \times \frac{1}{2 \sqrt{\frac{1-x}{2}}} \times \frac{d}{d x}\left(\frac{1-x}{2}\right)=\frac{1}{\sqrt{\frac{2-1+x}{2}}} \times \frac{1}{\sqrt{2} \cdot \sqrt{1-x}} \times \frac{-1}{2}$
$=\frac{\sqrt{2}}{\sqrt{1+x}} \times \frac{1}{\sqrt{2} \cdot \sqrt{1-x}} \times \frac{-1}{2}=\frac{-1}{2 \sqrt{1-x^{2}}}$
This problem can also be solved as follows
$\begin{array}{l}
f(x)=\sin ^{-1}\left(\sqrt{\frac{1-x}{2}}\right) \\
\text { Put } x=\cos \theta \Rightarrow \sqrt{\frac{1-x}{2}}=\sqrt{\frac{1-\cos \theta}{2}}=\sqrt{\frac{2 \sin ^{2} \frac{\theta}{2}}{2}}=\sin \frac{\theta}{2} \\
\therefore f(x)=\sin ^{-1}\left(\sin \frac{\theta}{2}\right)=\frac{\theta}{2}=\frac{\cos ^{-1} x}{2} \\
\therefore f^{\prime}(x)=\frac{-1}{2 \sqrt{1-x^{2}}}
\end{array}$

</details>

---

### Q59. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{y}=\tan ^{-1}\left[\frac{x-\sqrt{1-x^{2}}}{x+\sqrt{1-x^{2}}}\right]$, then $\left(\frac{d y}{d x}\right)=$

**Options:**

- **(A)** $\frac{-1}{\sqrt{1-x^{2}}}$
- **(B)** $\frac{-x}{\sqrt{1-x^{2}}}$
- **(C)** $\frac{1}{\sqrt{1-x^{2}}}$
- **(D)** $\frac{x}{\sqrt{1-x^{2}}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{\sqrt{1-x^{2}}}$**

**Detailed Solution:**

Given $y=\tan ^{-1}\left[\frac{x-\sqrt{1-x^{2}}}{x+\sqrt{1-x^{2}}}\right]$
Put $x=\cos \theta \Rightarrow \theta=\cos ^{-1} x$
$y=\tan ^{-1}\left[\frac{\cos \theta-\sin \theta}{\cos \theta+\sin \theta}\right]=\tan ^{-1}\left[\frac{1-\tan \theta}{1+\tan \theta}\right]$
$\quad=\tan ^{-1}\left[\tan \left(\frac{\pi}{4}-\theta\right)\right]=\frac{\pi}{4}-\theta$
$\therefore \frac{d y}{d x}=\frac{\pi}{4}-\cos ^{-1} x$
$$
\begin{aligned} y &=\frac{1}{\sqrt{1-x^{2}}} \\ y &=\frac{1}{\sqrt{1-x^{2}}} \end{aligned}
$$

</details>

---

### Q60. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mo>,</mo></mrow></mrow></math> then <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>e</mi></mrow></mfenced><mo>=</mo></math> ________

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math>
- **(D)** <math><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math>**

**Detailed Solution:**

Given <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math>  
<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>2</mn><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow></mfenced></math>  
<math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></math>  
<math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mo>(</mo><mi mathvariant="normal">e</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mo>+</mo><mn>2</mn></mrow><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfrac><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math>  
Note: lnx is better option in place of log x

</details>

---

### Q61. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Derivative of <math><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mi>t</mi></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></mrow></mfenced></math> with respect to <math><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></mrow></mfenced></math> is

**Options:**

- **(A)** 1
- **(B)** cot 1
- **(C)** tan t
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

Let <math><mi>y</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mi>t</mi></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></mrow></mfenced></math>
Put <math><mi>t</mi><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mo>⇒</mo><mi>θ</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi></math>
<math><mo>=</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></msqrt></mrow></mfrac></mrow></mfenced><mo>=</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi>θ</mi></mrow></mfrac></mrow></mfenced></math>
<math><mo>=</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mrow></mfenced><mo>=</mo><mi>θ</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi></math>
and <math><mi>z</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></mrow></mfenced><mo>=</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></msqrt></mrow></mfrac></mrow></mfenced></math>
<math><mo>=</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mrow></mfenced></math>
<math><mo>=</mo><mi>θ</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi></math>
<math><mo>∴</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>z</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></mrow><mrow><mfrac><mrow><mi>d</mi><mi>z</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mfrac></mrow></mfrac><mo>=</mo><mn>1</mn></math>

</details>

---

### Q62. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

$y=\log \tan x / 2+\sin ^{-1}(\cos x)$, then $d y / d x$ is

**Options:**

- **(A)** $\operatorname{cosec} x-1$
- **(B)** $\operatorname{cosec} x$
- **(C)** $\operatorname{cosec} x+1$
- **(D)** $x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\operatorname{cosec} x-1$**

**Detailed Solution:**

$\begin{aligned} \frac{d y}{d x} &=\frac{1}{\tan x / 2} \sec ^{2} \frac{x}{2} \cdot \frac{1}{2}+\frac{1}{\sqrt{1-\cos ^{2} x}}(-\sin x) \\ &=\frac{1}{2 \sin \frac{x}{2} \cdot \cos \frac{x}{2}}-1=\operatorname{cosec} x-1 \end{aligned}$

</details>

---

