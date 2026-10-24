# MHT CET Mathematics - Inverse Trigonometric Functions

## Topic 2: T inverse T property

**Total Questions:** 50

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\displaystyle\sum_{x=1}^{2025} \tan^2(\sec^{-1} x) = \dfrac{2024 \times 2025 \times k}{6}$, then $k = \ldots$

**Options:**

- **(A)** $2027$
- **(B)** $2030$
- **(C)** $4055$
- **(D)** $4061$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4055$**

**Detailed Solution:**

Using the trigonometric identity $\tan^2 \theta = \sec^2 \theta - 1$, the general term of the summation simplifies to:

$\tan^2(\sec^{-1} x) = \sec^2(\sec^{-1} x) - 1 = x^2 - 1$

The given summation can be written as:

$\sum_{x=1}^{n} (x^2 - 1) = \sum_{x=1}^{n} x^2 - \sum_{x=1}^{n} 1$

where $n = 2025$. Using the standard formula for the sum of squares of the first $n$ natural numbers:

$\sum_{x=1}^{n} x^2 - n = \dfrac{n(n+1)(2n+1)}{6} - n$

$\Rightarrow \dfrac{n}{6} [ (n+1)(2n+1) - 6 ]$

$\Rightarrow \dfrac{n}{6} [ 2n^2 + 3n + 1 - 6 ]$

$\Rightarrow \dfrac{n}{6} [ 2n^2 + 3n - 5 ]$

Factoring the quadratic expression:

$\Rightarrow \dfrac{n}{6} [ (n-1)(2n+5) ]$

$\Rightarrow \dfrac{(n-1) n (2n+5)}{6}$

Substituting $n = 2025$ into the expression:

$\dfrac{(2025 - 1) \times 2025 \times (2 \times 2025 + 5)}{6}$

$\Rightarrow \dfrac{2024 \times 2025 \times 4055}{6}$

Comparing this result with the given expression $\dfrac{2024 \times 2025 \times k}{6}$ yields:

$k = 4055$

Answer: $4055$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\sin^{-1}(\cos(\sin^{-1} x)) + \cos^{-1}(\sin(\cos^{-1} x)) = \ldots$

**Options:**

- **(A)** $0$
- **(B)** $\dfrac{\pi}{6}$
- **(C)** $\dfrac{\pi}{3}$
- **(D)** $\dfrac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{\pi}{2}$**

**Detailed Solution:**

Let $\sin^{-1} x = \theta$, where $\theta \in [-\dfrac{\pi}{2}, \dfrac{\pi}{2}]$.

Then $\cos(\sin^{-1} x) = \cos \theta = \sqrt{1 - \sin^2 \theta} = \sqrt{1 - x^2}$.

Thus, the first term becomes $\sin^{-1}(\sqrt{1 - x^2})$.

Similarly, let $\cos^{-1} x = \phi$, where $\phi \in [0, \pi]$.

Then $\sin(\cos^{-1} x) = \sin \phi = \sqrt{1 - \cos^2 \phi} = \sqrt{1 - x^2}$.

Thus, the second term becomes $\cos^{-1}(\sqrt{1 - x^2})$.

Adding the two terms, we get:

$\sin^{-1}(\sqrt{1 - x^2}) + \cos^{-1}(\sqrt{1 - x^2})$

Using the inverse trigonometric identity $\sin^{-1} y + \cos^{-1} y = \dfrac{\pi}{2}$ for $y \in [-1, 1]$, and noting that $\sqrt{1 - x^2} \in [0, 1]$ for $x \in [-1, 1]$, we have:

$\sin^{-1}(\sqrt{1 - x^2}) + \cos^{-1}(\sqrt{1 - x^2}) = \dfrac{\pi}{2}$

Answer: $\dfrac{\pi}{2}$

</details>

---

### Q3. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $u = \tan^{-1}\left(\dfrac{\sqrt{1+x^2}-1}{x}\right)$ and $v = \tan^{-1}\left(\dfrac{2x\sqrt{1-x^2}}{1-2x^2}\right)$ then $\dfrac{du}{dv} = \ldots$

**Options:**

- **(A)** $\dfrac{\sqrt{1+x^2}}{4(1-x^2)}$
- **(B)** $\dfrac{\sqrt{1-x^2}}{4(1+x^2)}$
- **(C)** $\dfrac{\sqrt{1-x^2}}{2(1+x^2)}$
- **(D)** $\dfrac{2\sqrt{1+x^2}}{(1-x^2)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\sqrt{1-x^2}}{4(1+x^2)}$**

**Detailed Solution:**

For $u$, substitute $x = \tan \theta \Rightarrow \theta = \tan^{-1} x$

$u = \tan^{-1}\left(\dfrac{\sec \theta - 1}{\tan \theta}\right) = \tan^{-1}\left(\dfrac{1 - \cos \theta}{\sin \theta}\right)$

$u = \tan^{-1}\left(\dfrac{2 \sin^2(\theta/2)}{2 \sin(\theta/2) \cos(\theta/2)}\right) = \tan^{-1}\left(\tan \dfrac{\theta}{2}\right) = \dfrac{\theta}{2}$

$u = \dfrac{1}{2} \tan^{-1} x$

Differentiating with respect to $x$:

$\dfrac{du}{dx} = \dfrac{1}{2(1+x^2)}$

For $v$, substitute $x = \sin \phi \Rightarrow \phi = \sin^{-1} x$

$v = \tan^{-1}\left(\dfrac{2\sin \phi \cos \phi}{1 - 2\sin^2 \phi}\right) = \tan^{-1}\left(\dfrac{\sin 2\phi}{\cos 2\phi}\right)$

$v = \tan^{-1}(\tan 2\phi) = 2\phi = 2 \sin^{-1} x$

Differentiating with respect to $x$:

$\dfrac{dv}{dx} = \dfrac{2}{\sqrt{1-x^2}}$

Now, finding $\dfrac{du}{dv}$:

$\dfrac{du}{dv} = \dfrac{\dfrac{du}{dx}}{\dfrac{dv}{dx}} = \dfrac{\dfrac{1}{2(1+x^2)}}{\dfrac{2}{\sqrt{1-x^2}}} = \dfrac{\sqrt{1-x^2}}{4(1+x^2)}$

Answer: $\dfrac{\sqrt{1-x^2}}{4(1+x^2)}$

</details>

---

### Q4. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $-1 \leq x \leq -\dfrac{1}{\sqrt{2}}$ then $\sin^{-1}(2x\sqrt{1-x^2}) = $

**Options:**

- **(A)** $-2\pi + 2\cos^{-1} x$
- **(B)** $2\pi + 2\cos^{-1} x$
- **(C)** $-2\pi - 2\cos^{-1} x$
- **(D)** $2\pi - 2\cos^{-1} x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-2\pi + 2\cos^{-1} x$**

**Detailed Solution:**

Let $x = \cos \theta$. Since $-1 \leq x \leq -\dfrac{1}{\sqrt{2}}$, we have $\theta \in [\dfrac{3\pi}{4}, \pi]$.

Then $\sqrt{1-x^2} = \sqrt{1-\cos^2\theta} = \sin \theta$, since $\sin \theta \geq 0$ for $\theta \in [\dfrac{3\pi}{4}, \pi]$.

Substituting $x$ in the given expression:

$\sin^{-1}(2x\sqrt{1-x^2}) = \sin^{-1}(2\cos\theta\sin\theta) = \sin^{-1}(\sin 2\theta)$

Since $\theta \in [\dfrac{3\pi}{4}, \pi]$, the range of $2\theta$ is $[\dfrac{3\pi}{2}, 2\pi]$.

For any angle $\alpha \in [\dfrac{3\pi}{2}, 2\pi]$, the principal value is given by $\sin^{-1}(\sin \alpha) = \alpha - 2\pi$.

Therefore, $\sin^{-1}(\sin 2\theta) = 2\theta - 2\pi$.

Substituting back $\theta = \cos^{-1} x$, we get:

$2\cos^{-1} x - 2\pi = -2\pi + 2\cos^{-1} x$

Answer: $-2\pi + 2\cos^{-1} x$

</details>

---

### Q5. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\sin^{-1}\left(\sin\dfrac{5\pi}{6}\right) + \cos^{-1}\left(\cos\dfrac{7\pi}{6}\right) + \tan^{-1}\left(\tan\dfrac{2\pi}{3}\right)$ is equal to...

**Options:**

- **(A)** $\dfrac{2\pi}{3}$
- **(B)** $\dfrac{4\pi}{3}$
- **(C)** $\dfrac{5\pi}{3}$
- **(D)** $\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{2\pi}{3}$**

**Detailed Solution:**

The principal value branch of $\sin^{-1}x$ is $\left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]$.

$\sin^{-1}\left(\sin\dfrac{5\pi}{6}\right) = \sin^{-1}\left(\sin\left(\pi - \dfrac{\pi}{6}\right)\right) = \sin^{-1}\left(\sin\dfrac{\pi}{6}\right) = \dfrac{\pi}{6}$

The principal value branch of $\cos^{-1}x$ is $[0, \pi]$.

$\cos^{-1}\left(\cos\dfrac{7\pi}{6}\right) = \cos^{-1}\left(\cos\left(2\pi - \dfrac{5\pi}{6}\right)\right) = \cos^{-1}\left(\cos\dfrac{5\pi}{6}\right) = \dfrac{5\pi}{6}$

The principal value branch of $\tan^{-1}x$ is $\left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$.

$\tan^{-1}\left(\tan\dfrac{2\pi}{3}\right) = \tan^{-1}\left(\tan\left(\pi - \dfrac{\pi}{3}\right)\right) = \tan^{-1}\left(-\tan\dfrac{\pi}{3}\right) = \tan^{-1}\left(\tan\left(-\dfrac{\pi}{3}\right)\right) = -\dfrac{\pi}{3}$

Adding the three values:

$\dfrac{\pi}{6} + \dfrac{5\pi}{6} - \dfrac{\pi}{3} = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$

Answer: $\dfrac{2\pi}{3}$

</details>

---

### Q6. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\sec^2(\tan^{-1}3) - \tan^2(\sec^{-1}3) = $

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $2$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2$**

**Detailed Solution:**

Using the identity $\sec^2 \theta = 1 + \tan^2 \theta$, we get:

$\sec^2(\tan^{-1} 3) = 1 + \tan^2(\tan^{-1} 3) = 1 + (3)^2 = 10$

Using the identity $\tan^2 \theta = \sec^2 \theta - 1$, we get:

$\tan^2(\sec^{-1} 3) = \sec^2(\sec^{-1} 3) - 1 = (3)^2 - 1 = 8$

Substituting these values into the given expression:

$\sec^2(\tan^{-1} 3) - \tan^2(\sec^{-1} 3) = 10 - 8 = 2$

</details>

---

### Q7. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $t \in (0, 1)$ and $\alpha \in \left(0, \dfrac{\pi}{4}\right)$. If $x = \text{cosec}^{-1}\left(\dfrac{1+t^2}{2t}\right)$, $y = \cot^{-1}\left(\dfrac{\sqrt{1-t^2}}{t}\right)$ and $\dfrac{dy}{dx} = f(t)$, then the value of $f(\tan\alpha)$ is

**Options:**

- **(A)** $\dfrac{\sec\alpha}{\sqrt{\cos 2\alpha}}$
- **(B)** $\dfrac{\sec\alpha}{2\sqrt{\cos 2\alpha}}$
- **(C)** $\dfrac{\cos\alpha}{2\sqrt{\cos 2\alpha}}$
- **(D)** $\dfrac{\cos\alpha}{\sqrt{\cos 2\alpha}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\sec\alpha}{2\sqrt{\cos 2\alpha}}$**

**Detailed Solution:**

Given $x = \text{cosec}^{-1}\left(\dfrac{1+t^2}{2t}\right) = \sin^{-1}\left(\dfrac{2t}{1+t^2}\right)$

Since $t \in (0, 1)$, we can write $x = 2\tan^{-1}t$

Differentiating with respect to $t$, we get:

$\dfrac{dx}{dt} = \dfrac{2}{1+t^2}$

Also given $y = \cot^{-1}\left(\dfrac{\sqrt{1-t^2}}{t}\right)$

Let $t = \sin\theta$, then $\dfrac{\sqrt{1-t^2}}{t} = \dfrac{\cos\theta}{\sin\theta} = \cot\theta$

So, $y = \cot^{-1}(\cot\theta) = \theta = \sin^{-1}t$

Differentiating with respect to $t$, we get:

$\dfrac{dy}{dt} = \dfrac{1}{\sqrt{1-t^2}}$

Now, $f(t) = \dfrac{dy}{dx} = \dfrac{\dfrac{dy}{dt}}{\dfrac{dx}{dt}} = \dfrac{\dfrac{1}{\sqrt{1-t^2}}}{\dfrac{2}{1+t^2}} = \dfrac{1+t^2}{2\sqrt{1-t^2}}$

Substituting $t = \tan\alpha$:

$f(\tan\alpha) = \dfrac{1+\tan^2\alpha}{2\sqrt{1-\tan^2\alpha}}$

$f(\tan\alpha) = \dfrac{\sec^2\alpha}{2\sqrt{\dfrac{\cos^2\alpha - \sin^2\alpha}{\cos^2\alpha}}}$

$f(\tan\alpha) = \dfrac{\sec^2\alpha}{2\dfrac{\sqrt{\cos 2\alpha}}{\cos\alpha}}$

$f(\tan\alpha) = \dfrac{\sec^2\alpha \cdot \cos\alpha}{2\sqrt{\cos 2\alpha}} = \dfrac{\sec\alpha}{2\sqrt{\cos 2\alpha}}$

Answer: $\dfrac{\sec\alpha}{2\sqrt{\cos 2\alpha}}$

</details>

---

### Q8. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \tan^{-1}\left[\dfrac{x - \sqrt{1 - x^2}}{x + \sqrt{1 - x^2}}\right]$ , then $\dfrac{dy}{dx} =$

**Options:**

- **(A)** $\dfrac{-1}{\sqrt{1 - x^2}}$
- **(B)** $\dfrac{1}{\sqrt{1 - x^2}}$
- **(C)** $1$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{\sqrt{1 - x^2}}$**

**Detailed Solution:**

Let $x = \sin \theta$, which implies $\theta = \sin^{-1} x$.

Substituting this into the given expression, we get:

$y = \tan^{-1}\left[\dfrac{\sin \theta - \sqrt{1 - \sin^2 \theta}}{\sin \theta + \sqrt{1 - \sin^2 \theta}}\right]$

$y = \tan^{-1}\left[\dfrac{\sin \theta - \cos \theta}{\sin \theta + \cos \theta}\right]$

Dividing the numerator and the denominator by $\cos \theta$, we obtain:

$y = \tan^{-1}\left[\dfrac{\tan \theta - 1}{\tan \theta + 1}\right]$

Using the trigonometric identity $\tan(A - B) = \dfrac{\tan A - \tan B}{1 + \tan A \tan B}$ with $A = \theta$ and $B = \dfrac{\pi}{4}$:

$y = \tan^{-1}\left[\tan\left(\theta - \dfrac{\pi}{4}\right)\right]$

$y = \theta - \dfrac{\pi}{4}$

Substituting back $\theta = \sin^{-1} x$:

$y = \sin^{-1} x - \dfrac{\pi}{4}$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = \dfrac{1}{\sqrt{1 - x^2}} - 0$

$\dfrac{dy}{dx} = \dfrac{1}{\sqrt{1 - x^2}}$

Answer: $\dfrac{1}{\sqrt{1 - x^2}}$

</details>

---

### Q9. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \tan^{-1}\sqrt{\dfrac{1 + \sin 2x}{1 - \sin 2x}}$, then $\dfrac{\text{d}y}{\text{d}x}$ at $x = \dfrac{\pi}{6}$ is

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $\dfrac{1}{2}$
- **(D)** $\dfrac{\sqrt{3}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1$**

**Detailed Solution:**

We have $y = \tan^{-1}\sqrt{\dfrac{1 + \sin 2x}{1 - \sin 2x}}$.

Using the trigonometric identities $1 + \sin 2x = (\cos x + \sin x)^2$ and $1 - \sin 2x = (\cos x - \sin x)^2$, we get:

$y = \tan^{-1}\sqrt{\dfrac{(\cos x + \sin x)^2}{(\cos x - \sin x)^2}} = \tan^{-1}\left| \dfrac{\cos x + \sin x}{\cos x - \sin x} \right|$

At $x = \dfrac{\pi}{6}$, $\cos \dfrac{\pi}{6} = \dfrac{\sqrt{3}}{2}$ and $\sin \dfrac{\pi}{6} = \dfrac{1}{2}$. Since $\cos x > \sin x$, the expression inside the modulus is positive.

$y = \tan^{-1}\left( \dfrac{\cos x + \sin x}{\cos x - \sin x} \right)$

Dividing the numerator and the denominator by $\cos x$:

$y = \tan^{-1}\left( \dfrac{1 + \tan x}{1 - \tan x} \right)$

$y = \tan^{-1}\left( \tan\left( \dfrac{\pi}{4} + x \right) \right)$

For $x = \dfrac{\pi}{6}$, $\dfrac{\pi}{4} + x = \dfrac{5\pi}{12}$, which lies in the principal branch $\left( -\dfrac{\pi}{2}, \dfrac{\pi}{2} \right)$.

$y = \dfrac{\pi}{4} + x$

Differentiating with respect to $x$:

$\dfrac{\text{d}y}{\text{d}x} = 1$

Answer: $1$

</details>

---

### Q10. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan^{-1}\left[\dfrac{\sqrt{5-2\sqrt{6}}}{1+\sqrt{6}}\right] = \dfrac{\pi}{3} - \tan^{-1}(k)$, then $\sec^{-1}(k) = ...$

**Options:**

- **(A)** $\dfrac{\pi}{6}$
- **(B)** $\dfrac{\pi}{4}$
- **(C)** $\dfrac{\pi}{3}$
- **(D)** $\dfrac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\pi}{4}$**

**Detailed Solution:**

Simplify the expression inside the inverse tangent function:

$\sqrt{5-2\sqrt{6}} = \sqrt{3 + 2 - 2\sqrt{3}\sqrt{2}} = \sqrt{(\sqrt{3} - \sqrt{2})^2} = \sqrt{3} - \sqrt{2}$

Substitute this back into the given equation:

$\tan^{-1}\left[\dfrac{\sqrt{5-2\sqrt{6}}}{1+\sqrt{6}}\right] = \tan^{-1}\left[\dfrac{\sqrt{3}-\sqrt{2}}{1+\sqrt{3}\sqrt{2}}\right]$

Using the identity $\tan^{-1}\left(\dfrac{x-y}{1+xy}\right) = \tan^{-1}(x) - \tan^{-1}(y)$, we get:

$\tan^{-1}\left[\dfrac{\sqrt{3}-\sqrt{2}}{1+\sqrt{3}\sqrt{2}}\right] = \tan^{-1}(\sqrt{3}) - \tan^{-1}(\sqrt{2})$

Since $\tan^{-1}(\sqrt{3}) = \dfrac{\pi}{3}$, the expression becomes:

$\dfrac{\pi}{3} - \tan^{-1}(\sqrt{2})$

Equating this to the given right-hand side:

$\dfrac{\pi}{3} - \tan^{-1}(\sqrt{2}) = \dfrac{\pi}{3} - \tan^{-1}(k)$

$\Rightarrow k = \sqrt{2}$

Now, find the value of $\sec^{-1}(k)$:

$\sec^{-1}(\sqrt{2}) = \dfrac{\pi}{4}$

Answer: $\dfrac{\pi}{4}$

</details>

---

### Q11. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \tan^{-1}\left\{\dfrac{\sqrt{1 + x^2} - \sqrt{1 - x^2}}{\sqrt{1 + x^2} + \sqrt{1 - x^2}}\right\}$, where $|x| < 1$, then $\dfrac{dy}{dx}$ is equal to

**Options:**

- **(A)** $\dfrac{-x}{\sqrt{1 - x^4}}$
- **(B)** $\dfrac{x}{\sqrt{1 - x^4}}$
- **(C)** $\dfrac{-2x}{\sqrt{1 - x^4}}$
- **(D)** $\dfrac{2x}{\sqrt{1 - x^4}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{x}{\sqrt{1 - x^4}}$**

**Detailed Solution:**

Let $x^2 = \cos 2\theta$. Then $\theta = \dfrac{1}{2}\cos^{-1}(x^2)$.

Substituting this into the given expression, we get:

$\sqrt{1 + x^2} = \sqrt{1 + \cos 2\theta} = \sqrt{2\cos^2\theta} = \sqrt{2}\cos\theta$

$\sqrt{1 - x^2} = \sqrt{1 - \cos 2\theta} = \sqrt{2\sin^2\theta} = \sqrt{2}\sin\theta$

Now, substitute these into $y$:

$y = \tan^{-1}\left\{\dfrac{\sqrt{2}\cos\theta - \sqrt{2}\sin\theta}{\sqrt{2}\cos\theta + \sqrt{2}\sin\theta}\right\}$

Dividing the numerator and the denominator by $\sqrt{2}\cos\theta$:

$y = \tan^{-1}\left\{\dfrac{1 - \tan\theta}{1 + \tan\theta}\right\}$

$y = \tan^{-1}\left\{\tan\left(\dfrac{\pi}{4} - \theta\right)\right\}$

$y = \dfrac{\pi}{4} - \theta$

Substituting back $\theta = \dfrac{1}{2}\cos^{-1}(x^2)$:

$y = \dfrac{\pi}{4} - \dfrac{1}{2}\cos^{-1}(x^2)$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = 0 - \dfrac{1}{2}\left(\dfrac{-1}{\sqrt{1 - (x^2)^2}}\right) \cdot \dfrac{d}{dx}(x^2)$

$\dfrac{dy}{dx} = \dfrac{1}{2} \cdot \dfrac{1}{\sqrt{1 - x^4}} \cdot 2x$

$\dfrac{dy}{dx} = \dfrac{x}{\sqrt{1 - x^4}}$

Answer: $\dfrac{x}{\sqrt{1 - x^4}}$

</details>

---

### Q12. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\cot ^{-1}(\sqrt{\cos \alpha})-\tan ^{-1}(\sqrt{\cos \alpha})=x$, then the value of $\sin x$ is

**Options:**

- **(A)** $\cot ^2 \frac{\alpha}{2}$
- **(B)** $\cot \frac{\alpha}{2}$
- **(C)** $\tan \frac{\alpha}{2}$
- **(D)** $\tan ^2 \frac{\alpha}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\tan ^2 \frac{\alpha}{2}$**

**Detailed Solution:**

Given $x = \cot^{-1}(\sqrt{\cos \alpha}) - \tan^{-1}(\sqrt{\cos \alpha})$

Using the identity $\cot^{-1} y + \tan^{-1} y = \dfrac{\pi}{2}$, we get $\cot^{-1}(\sqrt{\cos \alpha}) = \dfrac{\pi}{2} - \tan^{-1}(\sqrt{\cos \alpha})$

Substituting this in the given equation:

$x = \dfrac{\pi}{2} - 2\tan^{-1}(\sqrt{\cos \alpha})$

Taking sine on both sides:

$\sin x = \sin\left(\dfrac{\pi}{2} - 2\tan^{-1}(\sqrt{\cos \alpha})\right)$

$\sin x = \cos(2\tan^{-1}(\sqrt{\cos \alpha}))$

Let $\tan^{-1}(\sqrt{\cos \alpha}) = \theta \Rightarrow \tan \theta = \sqrt{\cos \alpha}$

$\sin x = \cos(2\theta) = \dfrac{1 - \tan^2 \theta}{1 + \tan^2 \theta}$

Substituting $\tan \theta = \sqrt{\cos \alpha}$:

$\sin x = \dfrac{1 - \cos \alpha}{1 + \cos \alpha}$

Using the half-angle formulas $1 - \cos \alpha = 2\sin^2 \dfrac{\alpha}{2}$ and $1 + \cos \alpha = 2\cos^2 \dfrac{\alpha}{2}$:

$\sin x = \dfrac{2\sin^2 \dfrac{\alpha}{2}}{2\cos^2 \dfrac{\alpha}{2}} = \tan^2 \dfrac{\alpha}{2}$

Answer: $\tan ^2 \frac{\alpha}{2}$

</details>

---

### Q13. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\tan ^{-1}\left(\sqrt{\frac{1+\sin x}{1-\sin x}}\right), \quad 0 \leqslant x < \frac{\pi}{2}$, then $y^{\prime}\left(\frac{\pi}{6}\right)=$

**Options:**

- **(A)** $-\frac{1}{4}$
- **(B)** $\frac{1}{6}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{2}$**

**Detailed Solution:**

Given $y = \tan^{-1}\left(\sqrt{\dfrac{1+\sin x}{1-\sin x}}\right)$

We can write $1 + \sin x = \left(\cos \dfrac{x}{2} + \sin \dfrac{x}{2}\right)^2$ and $1 - \sin x = \left(\cos \dfrac{x}{2} - \sin \dfrac{x}{2}\right)^2$.

Substituting these into the expression under the square root:

$\sqrt{\dfrac{1+\sin x}{1-\sin x}} = \sqrt{\dfrac{\left(\cos \dfrac{x}{2} + \sin \dfrac{x}{2}\right)^2}{\left(\cos \dfrac{x}{2} - \sin \dfrac{x}{2}\right)^2}}$

Since $0 \leqslant x < \dfrac{\pi}{2}$, we have $\cos \dfrac{x}{2} > \sin \dfrac{x}{2} \geqslant 0$, so the square root simplifies to:

$\dfrac{\cos \dfrac{x}{2} + \sin \dfrac{x}{2}}{\cos \dfrac{x}{2} - \sin \dfrac{x}{2}}$

Dividing the numerator and the denominator by $\cos \dfrac{x}{2}$:

$\dfrac{1 + \tan \dfrac{x}{2}}{1 - \tan \dfrac{x}{2}} = \tan\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right)$

Now, substitute this back into the original equation for $y$:

$y = \tan^{-1}\left(\tan\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right)\right)$

For $0 \leqslant x < \dfrac{\pi}{2}$, the angle $\dfrac{\pi}{4} + \dfrac{x}{2}$ lies in the principal value branch of $\tan^{-1}$, so:

$y = \dfrac{\pi}{4} + \dfrac{x}{2}$

Differentiating with respect to $x$:

$y^{\prime} = \dfrac{d}{dx}\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right) = \dfrac{1}{2}$

Since the derivative is a constant, its value at $x = \dfrac{\pi}{6}$ is also $\dfrac{1}{2}$.

$y^{\prime}\left(\dfrac{\pi}{6}\right) = \dfrac{1}{2}$

Answer: $\frac{1}{2}$

</details>

---

### Q14. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of positive integral solutions of $\tan ^{-1} x+\cos ^{-1}\left(\frac{y}{\sqrt{1+y^2}}\right)=\sin ^{-1}\left(\frac{3}{\sqrt{10}}\right)$ are

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2**

**Detailed Solution:**

Given equation is $\tan^{-1} x + \cos^{-1}\left(\dfrac{y}{\sqrt{1+y^2}}\right) = \sin^{-1}\left(\dfrac{3}{\sqrt{10}}\right)$.

Let $\theta = \cos^{-1}\left(\dfrac{y}{\sqrt{1+y^2}}\right) \Rightarrow \cos \theta = \dfrac{y}{\sqrt{1+y^2}}$.

Since $y > 0$, $\tan \theta = \dfrac{1}{y} \Rightarrow \theta = \tan^{-1}\left(\dfrac{1}{y}\right)$.

Let $\phi = \sin^{-1}\left(\dfrac{3}{\sqrt{10}}\right) \Rightarrow \sin \phi = \dfrac{3}{\sqrt{10}}$.

Then $\tan \phi = 3 \Rightarrow \phi = \tan^{-1}(3)$.

Substituting these into the given equation, we get:

$\tan^{-1} x + \tan^{-1}\left(\dfrac{1}{y}\right) = \tan^{-1}(3)$

$\Rightarrow \tan^{-1}\left(\dfrac{1}{y}\right) = \tan^{-1}(3) - \tan^{-1} x$

Using the formula $\tan^{-1} A - \tan^{-1} B = \tan^{-1}\left(\dfrac{A - B}{1 + AB}\right)$:

$\tan^{-1}\left(\dfrac{1}{y}\right) = \tan^{-1}\left(\dfrac{3 - x}{1 + 3x}\right)$

$\Rightarrow \dfrac{1}{y} = \dfrac{3 - x}{1 + 3x}$

$\Rightarrow y = \dfrac{1 + 3x}{3 - x}$

For $y$ to be a positive integer, we must have $y > 0$, which implies $3 - x > 0 \Rightarrow x < 3$.

Since $x$ is a positive integer, the possible values for $x$ are $1$ and $2$.

For $x = 1$, $y = \dfrac{1 + 3(1)}{3 - 1} = \dfrac{4}{2} = 2$.

For $x = 2$, $y = \dfrac{1 + 3(2)}{3 - 2} = \dfrac{7}{1} = 7$.

Both values of $y$ are positive integers. Thus, the positive integral solutions $(x, y)$ are $(1, 2)$ and $(2, 7)$.

Therefore, there are exactly 2 positive integral solutions.

Answer: 2

</details>

---

### Q15. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin ^{-1}(4 x)+\sin ^{-1}(4 \sqrt{3} x)=-\frac{\pi}{2}$, then the absolute value of $x$ is

**Options:**

- **(A)** $\frac{1}{8}$
- **(B)** $\frac{1}{6}$
- **(C)** $\frac{2}{3}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{8}$**

**Detailed Solution:**

Given equation: $\sin^{-1}(4x) + \sin^{-1}(4\sqrt{3}x) = -\dfrac{\pi}{2}$

$\Rightarrow \sin^{-1}(4\sqrt{3}x) = -\dfrac{\pi}{2} - \sin^{-1}(4x)$

Taking sine on both sides:

$\sin(\sin^{-1}(4\sqrt{3}x)) = \sin\left(-\dfrac{\pi}{2} - \sin^{-1}(4x)\right)$

$4\sqrt{3}x = -\cos(\sin^{-1}(4x))$

Using $\cos(\sin^{-1}\theta) = \sqrt{1 - \theta^2}$:

$4\sqrt{3}x = -\sqrt{1 - (4x)^2}$

Squaring both sides:

$48x^2 = 1 - 16x^2$

$64x^2 = 1$

$x^2 = \dfrac{1}{64}$

$x = \pm \dfrac{1}{8}$

Since the sum of the principal values of the inverse sine functions is negative ($-\dfrac{\pi}{2}$), $x$ must be negative. Thus, $x = -\dfrac{1}{8}$.

The absolute value of $x$ is $|x| = \dfrac{1}{8}$.

Answer: $\frac{1}{8}$

</details>

---

### Q16. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\left(\tan ^{-1} x\right)^2+\left(\cot ^{-1} x\right)^2=\frac{5 \pi^2}{8}$, then $x^2+1=$

**Options:**

- **(A)** $-1$
- **(B)** 2
- **(C)** 1
- **(D)** $-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2**

**Detailed Solution:**

Given $\left(\tan^{-1} x\right)^2 + \left(\cot^{-1} x\right)^2 = \dfrac{5\pi^2}{8}$

We know that $\tan^{-1} x + \cot^{-1} x = \dfrac{\pi}{2}$

Using the algebraic identity $a^2 + b^2 = (a+b)^2 - 2ab$, we get:

$\left(\tan^{-1} x + \cot^{-1} x\right)^2 - 2\tan^{-1} x \cot^{-1} x = \dfrac{5\pi^2}{8}$

$\left(\dfrac{\pi}{2}\right)^2 - 2\tan^{-1} x \left(\dfrac{\pi}{2} - \tan^{-1} x\right) = \dfrac{5\pi^2}{8}$

$\dfrac{\pi^2}{4} - \pi \tan^{-1} x + 2\left(\tan^{-1} x\right)^2 = \dfrac{5\pi^2}{8}$

$2\left(\tan^{-1} x\right)^2 - \pi \tan^{-1} x + \dfrac{\pi^2}{4} - \dfrac{5\pi^2}{8} = 0$

$2\left(\tan^{-1} x\right)^2 - \pi \tan^{-1} x - \dfrac{3\pi^2}{8} = 0$

Multiplying the entire equation by $8$:

$16\left(\tan^{-1} x\right)^2 - 8\pi \tan^{-1} x - 3\pi^2 = 0$

$16\left(\tan^{-1} x\right)^2 - 12\pi \tan^{-1} x + 4\pi \tan^{-1} x - 3\pi^2 = 0$

$4\tan^{-1} x (4\tan^{-1} x - 3\pi) + \pi (4\tan^{-1} x - 3\pi) = 0$

$(4\tan^{-1} x + \pi)(4\tan^{-1} x - 3\pi) = 0$

$\tan^{-1} x = -\dfrac{\pi}{4}$ or $\tan^{-1} x = \dfrac{3\pi}{4}$

Since the principal value branch of $\tan^{-1} x$ is $\left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$, $\tan^{-1} x = \dfrac{3\pi}{4}$ is rejected.

Therefore, $\tan^{-1} x = -\dfrac{\pi}{4}$

$x = \tan\left(-\dfrac{\pi}{4}\right) = -1$

We need to find the value of $x^2 + 1$:

$x^2 + 1 = (-1)^2 + 1 = 1 + 1 = 2$

Answer: 2

</details>

---

### Q17. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The principal value of $\cos ^{-1}\left[\frac{1}{\sqrt{2}}\left(\cos \frac{9 \pi}{10}-\sin \frac{9 \pi}{10}\right)\right]$ is

**Options:**

- **(A)** $\frac{3 \pi}{20}$
- **(B)** $\frac{17 \pi}{20}$
- **(C)** $\frac{7 \pi}{10}$
- **(D)** $\frac{\pi}{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{17 \pi}{20}$**

**Detailed Solution:**

Let $E = \cos ^{-1}\left[\dfrac{1}{\sqrt{2}}\left(\cos \dfrac{9 \pi}{10}-\sin \dfrac{9 \pi}{10}\right)\right]$

$E = \cos ^{-1}\left[\cos \dfrac{\pi}{4} \cos \dfrac{9 \pi}{10} - \sin \dfrac{\pi}{4} \sin \dfrac{9 \pi}{10}\right]$

Using the identity $\cos A \cos B - \sin A \sin B = \cos(A + B)$:

$E = \cos ^{-1}\left[\cos \left(\dfrac{\pi}{4} + \dfrac{9 \pi}{10}\right)\right]$

$E = \cos ^{-1}\left[\cos \left(\dfrac{5\pi + 18\pi}{20}\right)\right] = \cos ^{-1}\left[\cos \left(\dfrac{23\pi}{20}\right)\right]$

Since the principal value branch of $\cos^{-1}x$ is $[0, \pi]$, and $\dfrac{23\pi}{20} \notin [0, \pi]$, we use $\cos \theta = \cos(2\pi - \theta)$:

$\cos \left(\dfrac{23\pi}{20}\right) = \cos \left(2\pi - \dfrac{23\pi}{20}\right) = \cos \left(\dfrac{17\pi}{20}\right)$

$E = \cos ^{-1}\left[\cos \left(\dfrac{17\pi}{20}\right)\right]$

Since $\dfrac{17\pi}{20} \in [0, \pi]$:

$E = \dfrac{17\pi}{20}$

Answer: $\frac{17 \pi}{20}$

</details>

---

### Q18. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $0 \leqslant \cos ^{-1} x \leqslant \pi$ and $\frac{-\pi}{2} \leqslant \sin ^{-1} x \leqslant \frac{\pi}{2}$, then at $x=\frac{1}{5}$ the value of $\cos \left(2 \cos ^{-1} x+\sin ^{-1} x\right)$ is

**Options:**

- **(A)** $-\sqrt{\frac{24}{25}}$
- **(B)** $\sqrt{\frac{24}{25}}$
- **(C)** $\frac{\sqrt{24}}{25}$
- **(D)** $\frac{-\sqrt{24}}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\sqrt{\frac{24}{25}}$**

**Detailed Solution:**

Let the given expression be $y = \cos \left(2 \cos ^{-1} x+\sin ^{-1} x\right)$.

We know that $\cos ^{-1} x + \sin ^{-1} x = \dfrac{\pi}{2}$.

Substituting this into the expression, we get:

$y = \cos \left(\cos ^{-1} x + \cos ^{-1} x + \sin ^{-1} x\right)$

$y = \cos \left(\cos ^{-1} x + \dfrac{\pi}{2}\right)$

Using the trigonometric identity $\cos \left(\dfrac{\pi}{2} + \theta\right) = -\sin \theta$, we have:

$y = -\sin (\cos ^{-1} x)$

Since $\sin (\cos ^{-1} x) = \sqrt{1 - x^2}$ for $x \in [-1, 1]$, the expression becomes:

$y = -\sqrt{1 - x^2}$

Substitute $x = \dfrac{1}{5}$ into the equation:

$y = -\sqrt{1 - \left(\dfrac{1}{5}\right)^2}$

$y = -\sqrt{1 - \dfrac{1}{25}}$

$y = -\sqrt{\dfrac{24}{25}}$

Answer: $-\sqrt{\frac{24}{25}}$

</details>

---

### Q19. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\left(\cos ^{-1} x\right)^2-\left(\sin ^{-1} x\right)^2>0$, then

**Options:**

- **(A)** $x < \frac{1}{2}$
- **(B)** $-1 < x < \sqrt{2}$
- **(C)** $0 \leqslant x < \frac{1}{\sqrt{2}}$
- **(D)** $-1 \leqslant x < \frac{1}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-1 \leqslant x < \frac{1}{\sqrt{2}}$**

**Detailed Solution:**

The given inequality is $(\cos^{-1} x)^2 - (\sin^{-1} x)^2 > 0$.

Using the identity $a^2 - b^2 = (a-b)(a+b)$, we get:

$(\cos^{-1} x - \sin^{-1} x)(\cos^{-1} x + \sin^{-1} x) > 0$

We know that $\cos^{-1} x + \sin^{-1} x = \dfrac{\pi}{2}$ for $x \in [-1, 1]$.

Substituting this into the inequality, we get:

$(\cos^{-1} x - \sin^{-1} x) \left(\dfrac{\pi}{2}\right) > 0$

$\cos^{-1} x - \sin^{-1} x > 0$

Using the relation $\cos^{-1} x = \dfrac{\pi}{2} - \sin^{-1} x$, we get:

$\dfrac{\pi}{2} - \sin^{-1} x - \sin^{-1} x > 0$

$\dfrac{\pi}{2} - 2\sin^{-1} x > 0$

$2\sin^{-1} x < \dfrac{\pi}{2}$

$\sin^{-1} x < \dfrac{\pi}{4}$

Since the principal value branch of $\sin^{-1} x$ is $\left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]$, we have:

$-\dfrac{\pi}{2} \leqslant \sin^{-1} x < \dfrac{\pi}{4}$

Applying the sine function, which is strictly increasing in this interval, we get:

$\sin\left(-\dfrac{\pi}{2}\right) \leqslant x < \sin\left(\dfrac{\pi}{4}\right)$

$-1 \leqslant x < \dfrac{1}{\sqrt{2}}$

Answer: $-1 \leqslant x < \frac{1}{\sqrt{2}}$

</details>

---

### Q20. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\tan ^2\left(\sec ^{-1} 4\right)+\cot ^2\left(\operatorname{cosec}^{-1} 3\right)$ is

**Options:**

- **(A)** 15
- **(B)** 25
- **(C)** 23
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 23**

**Detailed Solution:**

Using the fundamental trigonometric identities $\tan^2 \theta = \sec^2 \theta - 1$ and $\cot^2 \theta = \operatorname{cosec}^2 \theta - 1$.

For the first term:

$\tan^2(\sec^{-1} 4) = \sec^2(\sec^{-1} 4) - 1 = 4^2 - 1 = 15$

For the second term:

$\cot^2(\operatorname{cosec}^{-1} 3) = \operatorname{cosec}^2(\operatorname{cosec}^{-1} 3) - 1 = 3^2 - 1 = 8$

Adding the two values:

$15 + 8 = 23$

Answer: 23

</details>

---

### Q21. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $\tan ^{-1}\left(\frac{\sqrt{1+x^2}-1}{x}\right)$ w.r.t. $\tan ^{-1}\left(\frac{2 x \sqrt{1-x^2}}{1-2 x^2}\right)$ at $x=0$ is

**Options:**

- **(A)** $\frac{1}{8}$
- **(B)** $\frac{1}{4}$
- **(C)** $\frac{1}{2}$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{4}$**

**Detailed Solution:**

Let $u = \tan^{-1}\left(\dfrac{\sqrt{1+x^2}-1}{x}\right)$ and $v = \tan^{-1}\left(\dfrac{2x\sqrt{1-x^2}}{1-2x^2}\right)$.

For $u$, substitute $x = \tan \theta$:

$u = \tan^{-1}\left(\dfrac{\sec \theta - 1}{\tan \theta}\right) = \tan^{-1}\left(\dfrac{1 - \cos \theta}{\sin \theta}\right)$

$u = \tan^{-1}\left(\dfrac{2 \sin^2(\theta/2)}{2 \sin(\theta/2) \cos(\theta/2)}\right) = \tan^{-1}\left(\tan \dfrac{\theta}{2}\right) = \dfrac{\theta}{2} = \dfrac{1}{2} \tan^{-1} x$

Differentiating $u$ with respect to $x$:

$\dfrac{du}{dx} = \dfrac{1}{2(1+x^2)}$

At $x = 0$, $\dfrac{du}{dx} = \dfrac{1}{2(1+0)} = \dfrac{1}{2}$.

For $v$, substitute $x = \sin \phi$:

$v = \tan^{-1}\left(\dfrac{2 \sin \phi \cos \phi}{1 - 2 \sin^2 \phi}\right) = \tan^{-1}\left(\dfrac{\sin 2\phi}{\cos 2\phi}\right) = \tan^{-1}(\tan 2\phi) = 2\phi = 2 \sin^{-1} x$

Differentiating $v$ with respect to $x$:

$\dfrac{dv}{dx} = \dfrac{2}{\sqrt{1-x^2}}$

At $x = 0$, $\dfrac{dv}{dx} = \dfrac{2}{\sqrt{1-0}} = 2$.

The derivative of $u$ with respect to $v$ is given by:

$\dfrac{du}{dv} = \dfrac{\dfrac{du}{dx}}{\dfrac{dv}{dx}}$

At $x = 0$, $\dfrac{du}{dv} = \dfrac{\dfrac{1}{2}}{2} = \dfrac{1}{4}$.

Answer: $\frac{1}{4}$

</details>

---

### Q22. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\sin ^{-1}\left(\frac{2 x}{1+x^2}\right)+\sec ^{-1}\left(\frac{1+x^2}{1-x^2}\right)$ then the value of $\frac{\mathrm{dy}}{\mathrm{d} x}$ at $x=\sqrt{3}$ is

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0$**

**Detailed Solution:**

Given $y = \sin^{-1}\left(\dfrac{2x}{1+x^2}\right) + \sec^{-1}\left(\dfrac{1+x^2}{1-x^2}\right)$

We can rewrite the second term using the property $\sec^{-1}\left(\dfrac{1}{z}\right) = \cos^{-1}(z)$:

$y = \sin^{-1}\left(\dfrac{2x}{1+x^2}\right) + \cos^{-1}\left(\dfrac{1-x^2}{1+x^2}\right)$

Substitute $x = \tan \theta$. Since we need the derivative at $x = \sqrt{3} > 1$, we have $\theta \in \left(\dfrac{\pi}{4}, \dfrac{\pi}{2}\right)$.

$y = \sin^{-1}\left(\dfrac{2\tan \theta}{1+\tan^2 \theta}\right) + \cos^{-1}\left(\dfrac{1-\tan^2 \theta}{1+\tan^2 \theta}\right)$

$y = \sin^{-1}(\sin 2\theta) + \cos^{-1}(\cos 2\theta)$

Since $\theta \in \left(\dfrac{\pi}{4}, \dfrac{\pi}{2}\right)$, the angle $2\theta \in \left(\dfrac{\pi}{2}, \pi\right)$. 

In this interval, the principal value of $\sin^{-1}(\sin 2\theta)$ is $\pi - 2\theta$, and the principal value of $\cos^{-1}(\cos 2\theta)$ is $2\theta$.

Therefore, the expression for $y$ becomes:

$y = (\pi - 2\theta) + 2\theta$

$y = \pi$

Since $y$ is a constant for all $x > 1$, its derivative with respect to $x$ is zero.

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = 0$

Thus, at $x = \sqrt{3}$, $\dfrac{\mathrm{d}y}{\mathrm{d}x} = 0$.

Answer: $0$

</details>

---

### Q23. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{y}=\sin ^2\left(\cot ^{-1}\left(\sqrt{\frac{1-x}{1+x}}\right)\right)$, then $\frac{\mathrm{dy}}{\mathrm{d} x}=$

**Options:**

- **(A)** $-1$
- **(B)** $1$
- **(C)** $-\frac{1}{4}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{2}$**

**Detailed Solution:**

Let $x = \cos \theta$, which implies $\theta = \cos^{-1} x$.

Consider the expression inside the inverse cotangent:

$\sqrt{\dfrac{1-x}{1+x}} = \sqrt{\dfrac{1-\cos \theta}{1+\cos \theta}} = \sqrt{\dfrac{2\sin^2(\theta/2)}{2\cos^2(\theta/2)}} = \tan\left(\dfrac{\theta}{2}\right)$

Substituting this back into the inverse cotangent function:

$\cot^{-1}\left(\sqrt{\dfrac{1-x}{1+x}}\right) = \cot^{-1}\left(\tan\left(\dfrac{\theta}{2}\right)\right)$

Since $\tan\left(\dfrac{\theta}{2}\right) = \cot\left(\dfrac{\pi}{2} - \dfrac{\theta}{2}\right)$, we get:

$\cot^{-1}\left(\cot\left(\dfrac{\pi}{2} - \dfrac{\theta}{2}\right)\right) = \dfrac{\pi}{2} - \dfrac{\theta}{2}$

Now, substitute this into the expression for $y$:

$y = \sin^2\left(\dfrac{\pi}{2} - \dfrac{\theta}{2}\right)$

Using the identity $\sin\left(\dfrac{\pi}{2} - \alpha\right) = \cos \alpha$, we have:

$y = \cos^2\left(\dfrac{\theta}{2}\right)$

Using the half-angle formula $\cos^2\left(\dfrac{\theta}{2}\right) = \dfrac{1 + \cos \theta}{2}$:

$y = \dfrac{1 + \cos \theta}{2}$

Since $x = \cos \theta$, this simplifies to:

$y = \dfrac{1 + x}{2} = \dfrac{1}{2} + \dfrac{x}{2}$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = \dfrac{1}{2}$

Answer: $\frac{1}{2}$

</details>

---

### Q24. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\sin \left[\tan ^{-1}\left(\frac{1-x^2}{2 x}\right)+\cos ^{-1}\left(\frac{1-x^2}{1+x^2}\right)\right]$ for $x > 0$ is

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $-1$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1$**

**Detailed Solution:**

Let $x = \tan \theta$. Since $x > 0$, we have $\theta \in \left(0, \dfrac{\pi}{2}\right)$.

Consider the first term:
$\tan^{-1}\left(\dfrac{1-x^2}{2x}\right) = \tan^{-1}\left(\dfrac{1-\tan^2\theta}{2\tan\theta}\right)$

$\Rightarrow \tan^{-1}(\cot 2\theta) = \tan^{-1}\left[\tan\left(\dfrac{\pi}{2} - 2\theta\right)\right]$

Since $\theta \in \left(0, \dfrac{\pi}{2}\right)$, $2\theta \in (0, \pi)$, which means $\dfrac{\pi}{2} - 2\theta \in \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$. Thus, the principal value is:
$\tan^{-1}\left[\tan\left(\dfrac{\pi}{2} - 2\theta\right)\right] = \dfrac{\pi}{2} - 2\theta$

Now consider the second term:
$\cos^{-1}\left(\dfrac{1-x^2}{1+x^2}\right) = \cos^{-1}\left(\dfrac{1-\tan^2\theta}{1+\tan^2\theta}\right)$

$\Rightarrow \cos^{-1}(\cos 2\theta)$

Since $2\theta \in (0, \pi)$, the principal value is:
$\cos^{-1}(\cos 2\theta) = 2\theta$

Substituting these back into the original expression:
$\sin \left[\tan^{-1}\left(\dfrac{1-x^2}{2x}\right) + \cos^{-1}\left(\dfrac{1-x^2}{1+x^2}\right)\right] = \sin \left(\dfrac{\pi}{2} - 2\theta + 2\theta\right)$

$\Rightarrow \sin\left(\dfrac{\pi}{2}\right) = 1$

Answer: $1$

</details>

---

### Q25. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin ^{-1} x+\sin ^{-1} y=\frac{\pi}{3}$ and $\cot ^{-1}\left(\frac{1}{x}\right)-\cot ^{-1}\left(\frac{1}{y}\right)=0$ then $2 x^2+y^2-x y=$ $\qquad$

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $1$
- **(C)** $\frac{1}{2}$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2}$**

**Detailed Solution:**

Given $\cot^{-1}\left(\dfrac{1}{x}\right) - \cot^{-1}\left(\dfrac{1}{y}\right) = 0$

$\Rightarrow \cot^{-1}\left(\dfrac{1}{x}\right) = \cot^{-1}\left(\dfrac{1}{y}\right)$

$\Rightarrow \dfrac{1}{x} = \dfrac{1}{y} \Rightarrow x = y$

Substitute $x = y$ in the first equation $\sin^{-1} x + \sin^{-1} y = \dfrac{\pi}{3}$:

$\sin^{-1} x + \sin^{-1} x = \dfrac{\pi}{3}$

$\Rightarrow 2\sin^{-1} x = \dfrac{\pi}{3}$

$\Rightarrow \sin^{-1} x = \dfrac{\pi}{6}$

$\Rightarrow x = \sin\left(\dfrac{\pi}{6}\right) = \dfrac{1}{2}$

Since $x = y$, we have $y = \dfrac{1}{2}$.

Now, we need to find the value of $2x^2 + y^2 - xy$:

$2\left(\dfrac{1}{2}\right)^2 + \left(\dfrac{1}{2}\right)^2 - \left(\dfrac{1}{2}\right)\left(\dfrac{1}{2}\right)$

$= 2\left(\dfrac{1}{4}\right) + \dfrac{1}{4} - \dfrac{1}{4}$

$= \dfrac{2}{4} = \dfrac{1}{2}$

Answer: $\frac{1}{2}$

</details>

---

### Q26. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $\tan ^{-1}\left(\sqrt{1+x^2}-1\right)$ is

**Options:**

- **(A)** $\frac{x}{\sqrt{1+x^2}\left(x^2-2 \sqrt{x+1}+1\right)}$
- **(B)** $\frac{x}{\sqrt{1+x^2}\left(x^2-2 \sqrt{1+x^2}+3\right)}$
- **(C)** $\frac{x}{\sqrt{1+x^2}\left(x^2-2 \sqrt{x^2+1}+2\right)}$
- **(D)** $\frac{x}{\sqrt{1+x^2}\left(x^2+2 \sqrt{1+x^2}-3\right)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{x}{\sqrt{1+x^2}\left(x^2-2 \sqrt{1+x^2}+3\right)}$**

**Detailed Solution:**

Let $y = \tan^{-1}\left(\sqrt{1+x^2}-1\right)$.

Differentiating with respect to $x$ using the chain rule:

$\dfrac{dy}{dx} = \dfrac{1}{1 + \left(\sqrt{1+x^2}-1\right)^2} \cdot \dfrac{d}{dx}\left(\sqrt{1+x^2}-1\right)$

$\dfrac{dy}{dx} = \dfrac{1}{1 + \left(1+x^2 - 2\sqrt{1+x^2} + 1\right)} \cdot \dfrac{1}{2\sqrt{1+x^2}} \cdot 2x$

$\dfrac{dy}{dx} = \dfrac{1}{x^2 - 2\sqrt{1+x^2} + 3} \cdot \dfrac{x}{\sqrt{1+x^2}}$

$\dfrac{dy}{dx} = \dfrac{x}{\sqrt{1+x^2}\left(x^2 - 2\sqrt{1+x^2} + 3\right)}$

Answer: $\frac{x}{\sqrt{1+x^2}\left(x^2-2 \sqrt{1+x^2}+3\right)}$

</details>

---

### Q27. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $4 \sin ^{-1} x+\cos ^{-1} x=\pi$ then $x=$

**Options:**

- **(A)** $\frac{\sqrt{3}}{2}$
- **(B)** $0$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{1}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2}$**

**Detailed Solution:**

Given equation is $4 \sin^{-1} x + \cos^{-1} x = \pi$

Using the identity $\sin^{-1} x + \cos^{-1} x = \dfrac{\pi}{2}$, we can write $\cos^{-1} x = \dfrac{\pi}{2} - \sin^{-1} x$.

Substituting this in the given equation:

$4 \sin^{-1} x + \dfrac{\pi}{2} - \sin^{-1} x = \pi$

$3 \sin^{-1} x = \pi - \dfrac{\pi}{2}$

$3 \sin^{-1} x = \dfrac{\pi}{2}$

$\sin^{-1} x = \dfrac{\pi}{6}$

$x = \sin\left(\dfrac{\pi}{6}\right)$

$x = \dfrac{1}{2}$

Answer: $\frac{1}{2}$

</details>

---

### Q28. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin ^{-1}\left(\frac{x}{5}\right)+\operatorname{cosec}^{-1}\left(\frac{5}{4}\right)=\frac{\pi}{2}$, then the value of $x$ is

**Options:**

- **(A)** 4
- **(B)** 1
- **(C)** 5
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

The given equation is $\sin^{-1}\left(\dfrac{x}{5}\right) + \operatorname{cosec}^{-1}\left(\dfrac{5}{4}\right) = \dfrac{\pi}{2}$

Using the property $\operatorname{cosec}^{-1}(y) = \sin^{-1}\left(\dfrac{1}{y}\right)$, we get $\operatorname{cosec}^{-1}\left(\dfrac{5}{4}\right) = \sin^{-1}\left(\dfrac{4}{5}\right)$

Substituting this in the given equation:

$\sin^{-1}\left(\dfrac{x}{5}\right) + \sin^{-1}\left(\dfrac{4}{5}\right) = \dfrac{\pi}{2}$

$\sin^{-1}\left(\dfrac{x}{5}\right) = \dfrac{\pi}{2} - \sin^{-1}\left(\dfrac{4}{5}\right)$

Using the identity $\sin^{-1}(y) + \cos^{-1}(y) = \dfrac{\pi}{2}$, we have $\dfrac{\pi}{2} - \sin^{-1}\left(\dfrac{4}{5}\right) = \cos^{-1}\left(\dfrac{4}{5}\right)$

Therefore, $\sin^{-1}\left(\dfrac{x}{5}\right) = \cos^{-1}\left(\dfrac{4}{5}\right)$

We know that $\cos^{-1}\left(\dfrac{4}{5}\right) = \sin^{-1}\left(\sqrt{1 - \left(\dfrac{4}{5}\right)^2}\right) = \sin^{-1}\left(\dfrac{3}{5}\right)$

Equating the two expressions:

$\sin^{-1}\left(\dfrac{x}{5}\right) = \sin^{-1}\left(\dfrac{3}{5}\right)$

$\dfrac{x}{5} = \dfrac{3}{5}$

$x = 3$

Answer: 3

</details>

---

### Q29. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\cot ^{-1}(\sqrt{\cos \alpha})-\tan ^{-1}(\sqrt{\cos \alpha})=x$, then the value of $\sin x$ is

**Options:**

- **(A)** $\cot ^2\left(\frac{\alpha}{2}\right)$
- **(B)** $\tan ^2\left(\frac{\alpha}{2}\right)$
- **(C)** $\tan \alpha$
- **(D)** $\cot \left(\frac{\alpha}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\tan ^2\left(\frac{\alpha}{2}\right)$**

**Detailed Solution:**

Given equation is $\cot^{-1}(\sqrt{\cos \alpha}) - \tan^{-1}(\sqrt{\cos \alpha}) = x$

Using the identity $\cot^{-1} y + \tan^{-1} y = \dfrac{\pi}{2}$, we have $\cot^{-1}(\sqrt{\cos \alpha}) = \dfrac{\pi}{2} - \tan^{-1}(\sqrt{\cos \alpha})$

Substituting this in the given equation:

$\dfrac{\pi}{2} - \tan^{-1}(\sqrt{\cos \alpha}) - \tan^{-1}(\sqrt{\cos \alpha}) = x$

$\dfrac{\pi}{2} - 2\tan^{-1}(\sqrt{\cos \alpha}) = x$

Taking sine on both sides:

$\sin x = \sin\left(\dfrac{\pi}{2} - 2\tan^{-1}(\sqrt{\cos \alpha})\right)$

$\sin x = \cos\left(2\tan^{-1}(\sqrt{\cos \alpha})\right)$

Using the formula $\cos(2\theta) = \dfrac{1 - \tan^2 \theta}{1 + \tan^2 \theta}$ where $\theta = \tan^{-1}(\sqrt{\cos \alpha})$ and $\tan \theta = \sqrt{\cos \alpha}$:

$\sin x = \dfrac{1 - (\sqrt{\cos \alpha})^2}{1 + (\sqrt{\cos \alpha})^2}$

$\sin x = \dfrac{1 - \cos \alpha}{1 + \cos \alpha}$

Using the half-angle formulas $1 - \cos \alpha = 2\sin^2\left(\dfrac{\alpha}{2}\right)$ and $1 + \cos \alpha = 2\cos^2\left(\dfrac{\alpha}{2}\right)$:

$\sin x = \dfrac{2\sin^2\left(\dfrac{\alpha}{2}\right)}{2\cos^2\left(\dfrac{\alpha}{2}\right)}$

$\sin x = \tan^2\left(\dfrac{\alpha}{2}\right)$

Answer: $\tan ^2\left(\frac{\alpha}{2}\right)$

</details>

---

### Q30. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$2 \pi-\left(\sin ^{-1} \frac{4}{5}+\sin ^{-1} \frac{5}{13}+\sin ^{-1} \frac{16}{65}\right)$ is equal to

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{5 \pi}{4}$
- **(C)** $\frac{7 \pi}{4}$
- **(D)** $\frac{3 \pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{3 \pi}{2}$**

**Detailed Solution:**

Let $x = \sin^{-1} \dfrac{4}{5}$ and $y = \sin^{-1} \dfrac{5}{13}$.

$\sin x = \dfrac{4}{5} \Rightarrow \cos x = \dfrac{3}{5}$

$\sin y = \dfrac{5}{13} \Rightarrow \cos y = \dfrac{12}{13}$

$\cos(x+y) = \cos x \cos y - \sin x \sin y$

$\cos(x+y) = \left(\dfrac{3}{5} \times \dfrac{12}{13}\right) - \left(\dfrac{4}{5} \times \dfrac{5}{13}\right)$

$\cos(x+y) = \dfrac{36}{65} - \dfrac{20}{65} = \dfrac{16}{65}$

Since $x, y \in \left(0, \dfrac{\pi}{2}\right)$ and $\cos(x+y) > 0$, we have $x+y \in \left(0, \dfrac{\pi}{2}\right)$.

Thus, $x+y = \cos^{-1} \dfrac{16}{65}$.

The given expression becomes:

$2 \pi - \left(x + y + \sin^{-1} \dfrac{16}{65}\right)$

$= 2 \pi - \left(\cos^{-1} \dfrac{16}{65} + \sin^{-1} \dfrac{16}{65}\right)$

Using the standard inverse trigonometric identity $\sin^{-1} \theta + \cos^{-1} \theta = \dfrac{\pi}{2}$, we get:

$= 2 \pi - \dfrac{\pi}{2} = \dfrac{3 \pi}{2}$

Answer: $\frac{3 \pi}{2}$

</details>

---

### Q31. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $0 \lt x \lt 1$; then
$\sqrt{1+x^2}\left[\left\{x \cos \left(\cot ^{-1} x\right)+\sin \left(\cot ^{-1} x\right)\right\}^2-1\right]^{\dfrac{1}{2}}=$

**Options:**

- **(A)** $\dfrac{x}{\sqrt{1+x^2}}$
- **(B)** $x$
- **(C)** $\sqrt{1+x^2}$
- **(D)** $x \sqrt{1+x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x \sqrt{1+x^2}$**

**Detailed Solution:**

Let $\theta = \cot^{-1} x$. Then $\cot \theta = x$.

From this, we can find $\sin \theta = \dfrac{1}{\sqrt{1+x^2}}$ and $\cos \theta = \dfrac{x}{\sqrt{1+x^2}}$.

Substitute these into the expression $x \cos (\cot^{-1} x) + \sin (\cot^{-1} x)$:

$x \cos \theta + \sin \theta = x \left(\dfrac{x}{\sqrt{1+x^2}}\right) + \dfrac{1}{\sqrt{1+x^2}} = \dfrac{x^2+1}{\sqrt{1+x^2}} = \sqrt{1+x^2}$

Now, substitute this back into the given expression:

$\sqrt{1+x^2} \left[ \left( \sqrt{1+x^2} \right)^2 - 1 \right]^{\dfrac{1}{2}}$

$= \sqrt{1+x^2} \left[ 1+x^2 - 1 \right]^{\dfrac{1}{2}}$

$= \sqrt{1+x^2} \left[ x^2 \right]^{\dfrac{1}{2}}$

Since $0 \lt x \lt 1$, $(x^2)^{\dfrac{1}{2}} = x$.

$= x \sqrt{1+x^2}$

Answer: $x \sqrt{1+x^2}$

</details>

---

### Q32. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $x=\operatorname{cosec}\left(\tan ^{-1}\left(\cos \left(\cot ^{-1}\left(\sec \left(\sin ^{-1} a\right)\right)\right)\right)\right)$, $\mathrm{a} \in[0,1]$

**Options:**

- **(A)** $x^2-\mathrm{a}^2=3$
- **(B)** $x^2+\mathrm{a}^2=3$
- **(C)** $x^2-\mathrm{a}^2=2$
- **(D)** $x^2+\mathrm{a}^2=2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^2+\mathrm{a}^2=3$**

**Detailed Solution:**

$\begin{aligned} & x=\operatorname{cosec}\left(\tan ^{-1}\left(\cos \left(\cot ^{-1}\left(\sec \left(\sin ^{-1} \mathrm{a}\right)\right)\right)\right)\right) \\ & =\operatorname{cosec}\left(\tan ^{-1}\left(\cos \left(\cot ^{-1}\left(\sec \left(\sec ^{-1} \frac{1}{\sqrt{1-\mathrm{a}^2}}\right)\right)\right)\right)\right) \\ & =\operatorname{cosec}\left(\tan ^{-1}\left(\cos \left(\cot ^{-1}\left(\frac{1}{\sqrt{1-\mathrm{a}^2}}\right)\right)\right)\right) \\ & =\operatorname{cosec}\left(\tan ^{-1}\left(\cos \left(\cos ^{-1} \frac{1}{\sqrt{2-\mathrm{a}^2}}\right)\right)\right) \\ & =\operatorname{cosec}\left(\tan ^{-1}\left(\frac{1}{\sqrt{2-\mathrm{a}^2}}\right)\right) \\ & =\operatorname{cosec}\left(\operatorname{cosec}^{-1}\left(\sqrt{3-\mathrm{a}^2}\right)\right) \\ \therefore \quad & x=\sqrt{3-\mathrm{a}^2} \\ \therefore \quad & x^2+\mathrm{a}^2=3\end{aligned}$

</details>

---

### Q33. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The solution of the equation $\tan ^{-1}(1+x)+\tan ^{-1}(1-x)=\frac{\pi}{2}$ is

**Options:**

- **(A)** $x=1$
- **(B)** $x=0$
- **(C)** $x=-1$
- **(D)** $x=\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x=0$**

**Detailed Solution:**

$\begin{aligned} & \tan ^{-1}(1+x)+\tan ^{-1}(1-x)=\frac{\pi}{2} \\ & \Rightarrow \tan ^{-1}(1+x)=\frac{\pi}{2}-\tan ^{-1}(1-x) \\ & \Rightarrow \tan ^{-1}(1+x)=\cot ^{-1}(1-x) \\ & \Rightarrow \tan ^{-1}(1+x)=\tan ^{-1}\left(\frac{1}{1-x}\right) \\ & \Rightarrow 1+x=\frac{1}{1-x} \Rightarrow 1-x^2=1 \Rightarrow x=0\end{aligned}$

</details>

---

### Q34. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\cos ^{-1} x-\cos ^{-1} \frac{y}{2}=\alpha$, where $-1 \leq x \leq 1,-2 \leq y \leq 2, x \leq \frac{y}{2}$, then for all $x, y 4 x^2-4 x y \cos a+y^2$ is equal to

**Options:**

- **(A)** $2 \sin ^2 a$
- **(B)** $4 \sin ^2 a$
- **(C)** $4 \cos ^2 a+2 x^2 y^2$
- **(D)** $4 \sin ^2 a-2 x^2 y^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4 \sin ^2 a$**

**Detailed Solution:**

$\begin{aligned} & \cos ^{-1} x-\cos ^{-1} \frac{y}{2}=a \\ & \Rightarrow \cos ^{-1}\left(x \cdot \frac{y}{2}+\sqrt{1-x^2} \sqrt{1-\frac{y^2}{4}}\right)=a \\ & \Rightarrow \frac{x y}{2}+\frac{\sqrt{\left(1-x^2\right)\left(4-y^2\right)}}{2}=\cos a \\ & \Rightarrow\left(1-x^2\right)\left(4-y^2\right)=2 \cos a-x y \\ & \Rightarrow 4-y^2-4 x^2+x^2 y^2=4 \cos ^2 a+x^2 y^2-4 \cos a \cdot x y \\ & \Rightarrow 4-4 \cos ^2 a=4 x^2-4 x y \cos ^2 a+y^2 \\ & \Rightarrow 4 x^2-4 x y \cos a+y^2=4 \sin ^2 a\end{aligned}$

</details>

---

### Q35. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\tan ^{-1} 2 x+\tan ^{-1} 3 x=\frac{\pi}{4}$, then value of $x$ is

**Options:**

- **(A)** $\frac{1}{6}$
- **(B)** $-\frac{1}{6}$
- **(C)** 1
- **(D)** $\frac{5}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{6}$**

**Detailed Solution:**

$\begin{aligned} & \tan ^{-1} 2 x+\tan ^{-1} 3 x=\frac{\pi}{4} \\ & \Rightarrow \tan ^{-1}\left(\frac{2 x+3 x}{1-2 x \times 3 x}\right)=\tan ^{-1}(1) \\ & \Rightarrow \frac{5 x}{1-6 x^2}=1 \\ & \Rightarrow 6 x^2+5 x-1=0 \\ & \Rightarrow(6 x-1)(x+1)=0 \\ & \Rightarrow x=\frac{1}{6} \text { or } x=-1 \\ & \Rightarrow x=\frac{1}{6} \text { satisfies the equation }\end{aligned}$

</details>

---

### Q36. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

With reference to the principal values, if $\sin ^{-1} x+\sin ^{-1} y+\sin ^{-1} z=\frac{3 \pi}{2}$, then $x^{100}+y^{100}+z^{100}=$

**Options:**

- **(A)** 2
- **(B)** 3
- **(C)** 1
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3**

**Detailed Solution:**

$\begin{aligned} & \sin ^{-1} x+\sin ^{-1} y+\sin ^{-1} z=\frac{3 \pi}{2}=\frac{\pi}{2}+\frac{\pi}{2}+\frac{\pi}{2}=\sin ^{-1}(1)+\sin ^{-1}(1)+\sin ^{-1}(1) \\ & \Rightarrow x=y=z=1 \\ & \Rightarrow x^{100}+y^{100}+z^{100}=1^{100}+1^{100}+1^{100}=3\end{aligned}$

</details>

---

### Q37. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan ^{-1}\left(\frac{1-x}{1+x}\right)=\frac{1}{2} \tan ^{-1} x$, then $x$ has the value

**Options:**

- **(A)** $1$
- **(B)** $\sqrt{3}$
- **(C)** $3$
- **(D)** $\frac{1}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{\sqrt{3}}$**

**Detailed Solution:**

$\begin{aligned} & \tan ^{-1}\left(\frac{1-x}{1+x}\right)=\frac{1}{2} \tan ^{-1} x \\ & \Rightarrow \tan ^{-1}\left(\frac{1-\tan \theta}{1+\tan \theta}\right)=\frac{1}{2} \tan ^{-1}(\tan \theta) \\ & \Rightarrow \tan ^{-1}\left(\tan \left(\frac{\pi}{4}-\theta\right)\right)=\frac{1}{2} \theta \\ & \Rightarrow \frac{\pi}{4}-\theta=\frac{1}{2} \theta \\ & \Rightarrow \frac{\pi}{4}=\frac{3 \theta}{2} \\ & \Rightarrow \theta=\frac{\pi}{6} \\ & \Rightarrow x=\tan \frac{\pi}{6}=\frac{1}{\sqrt{3}}\end{aligned}$

</details>

---

### Q38. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\operatorname{cosec}^{-1}(\sqrt{2})+\cos ^{-1}\left(\frac{-1}{2}\right)-\sec ^{-1}\left(\frac{2}{\sqrt{3}}\right)$ is equal to

**Options:**

- **(A)** $\frac{3 \pi}{4}$
- **(B)** $\frac{\pi}{6}$
- **(C)** $\frac{2 \pi}{3}$
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3 \pi}{4}$**

**Detailed Solution:**

$\begin{aligned} & \operatorname{cosec}^{-1}(\sqrt{2})+\cos ^{-1}\left(\frac{-1}{2}\right)-\sec ^{-1}\left(\frac{2}{\sqrt{3}}\right) \\ & =\frac{\pi}{4}+\frac{2 \pi}{3}-\frac{\pi}{6}=\frac{3 \pi}{4}\end{aligned}$

</details>

---

### Q39. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan ^{-1} a+\tan ^{-1} b+\tan ^{-1} c=\pi$, then which of the following is true?

**Options:**

- **(A)** $a b c=1$
- **(B)** $a+b-c=\frac{a b}{c}$
- **(C)** $a+b+c=a b c$
- **(D)** $a+b+c=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $a+b+c=a b c$**

**Detailed Solution:**

$\begin{aligned} & \tan ^{-1} a+\tan ^{-1} b+\tan ^{-1} c=\pi \\ & \Rightarrow \tan ^{-1}\left(\frac{a+b+c-a b c}{1-a b-b c-c a}\right)=\pi \\ & \Rightarrow \frac{a+b+c-a b c}{1-a b-b c-c a}=\tan \pi=0 \\ & \Rightarrow a+b+c=a b c\end{aligned}$

</details>

---

### Q40. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $A=2 \tan ^{-1}\left(\frac{1+x}{1-x}\right)$ and $B=\cos ^{-1}\left(\frac{1-x^2}{1+x^2}\right)$, where $x \in(0,1)$, then $A-B=$

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $4 \tan ^{-1} x$
- **(C)** $\tan ^{-1} x$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{2}$**

**Detailed Solution:**

Let $x=\tan \theta$ then
$\begin{aligned} & A=2 \tan ^{-1}\left(\tan \left(\frac{\pi}{4}+\theta\right)\right) \text { and } B=\cos ^{-1}(\cos 2 \theta) \\ & \Rightarrow A=2\left\{\frac{\pi}{4}+\theta\right\} \text { and } B=2 \theta \\ & \Rightarrow A-B=\frac{\pi}{2}\end{aligned}$

</details>

---

### Q41. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $2 \sin ^{-1}\left(\frac{1}{2}\right)+\cot ^{-1}\left(\frac{1}{\sqrt{3}}\right)$ is

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{3}$
- **(C)** $\frac{\pi}{6}$
- **(D)** $\frac{2 \pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2 \pi}{3}$**

**Detailed Solution:**

$2 \sin ^{-1}\left(\frac{1}{2}\right)+\cos ^{-1}\left(\frac{1}{\sqrt{3}}\right)=2 \times \frac{\pi}{6}+\frac{\pi}{3}=\frac{2 \pi}{3}$

</details>

---

### Q42. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\sin \left(\sin ^{-1} \frac{1}{5}+\cos ^{-1} x\right)=1$, then the value of $x$ is

**Options:**

- **(A)** $\frac{\pi}{2}+\frac{1}{5}$
- **(B)** $\frac{\pi}{2}-\frac{1}{5}$
- **(C)** $-\frac{1}{5}$
- **(D)** $\frac{1}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{5}$**

**Detailed Solution:**

<p>Given that $\sin\left(\sin^{-1} \frac{1}{5} + \cos^{-1} x\right) = 1$, the argument must satisfy $\sin^{-1} \frac{1}{5} + \cos^{-1} x = \frac{\pi}{2}$.</p><p>Using the identity $\sin^{-1} y + \cos^{-1} y = \frac{\pi}{2}$ for $y \in [-1, 1]$, we identify $x = \frac{1}{5}$.</p><p>Since $\frac{1}{5}$ lies within the domain of $\cos^{-1} x$, this solution is valid.</p>

</details>

---

### Q43. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $2 \tan ^{-1}(\cos x)=\tan ^{-1}(2 \operatorname{cosec} x)$, then the value of $x$ is

**Options:**

- **(A)** $\frac{\pi^c}{6}$
- **(B)** $\frac{\pi^c}{4}$
- **(C)** $\frac{\pi^c}{3}$
- **(D)** $\frac{\pi^\epsilon}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi^c}{4}$**

**Detailed Solution:**

We have $2 \tan ^{-1}(\cos x)=\tan ^{-1}(2 \operatorname{cosec} x)$
$$
\begin{aligned}
& \therefore \tan ^{-1}\left(\frac{2 \cos x}{1-\cos ^2 x}\right)=\tan ^{-1}\left(\frac{2}{\sin x}\right) \\
& \therefore \frac{2 \cos x}{\sin ^2 x}=\frac{2}{\sin x} \Rightarrow \sin x \cos x=\sin ^2 x \\
& \therefore \sin x(\sin x-\cos x)=0 \Rightarrow \sin x=0 \text { or } \tan x=1 \\
& \therefore x=0 \text { or } x=\frac{\pi}{4}
\end{aligned}
$$

</details>

---

### Q44. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$$
\sin ^{-1}\left[\sin \left(-600^{\circ}\right)\right]+\cot ^{-1}(-\sqrt{3})=
$$

**Options:**

- **(A)** $\frac{\pi}{6}$
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{7 \pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{6}$**

**Detailed Solution:**

$$
\begin{aligned}
& \sin ^{-1}\left[\sin (-600)^{\circ}\right]+\cot ^{-1}(\sqrt{3}) \\
& =\sin ^{-1}\left[-\sin \left(360^{\circ}+180^{\circ}+60^{\circ}\right)\right]+\left[-\cot ^{-1}(\sqrt{3})\right] \\
& =\sin ^{-1}\left[\sin \left(60^{\circ}\right)\right]+\left[-\tan ^{-1}\left(\frac{1}{\sqrt{3}}\right)\right] \\
& =\sin ^{-1}\left[\sin 60^{\circ}\right]-\frac{\pi}{6}=\frac{\pi}{3}-\frac{\pi}{6}=\frac{\pi}{6}
\end{aligned}
$$

</details>

---

### Q45. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $4 \sin ^{-1} x+6 \cos ^{-1} x=3 \pi$, where $-1 \leq x \leq 1$, then $x=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{1}{\sqrt{2}}$
- **(C)** $\frac{-1}{2}$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

$\begin{aligned} & 4 \sin ^{-1} x+6 \cos ^{-1} x=3 \pi \\ & \therefore 4\left(\sin ^{-1} x+\cos ^{-1} x\right)+2 \cos ^{-1} x=3 \pi \\ & \therefore 4\left(\frac{\pi}{2}\right)+2 \cos ^{-1} x=3 \pi \quad \Rightarrow 2 \cos ^{-1} x=\pi \\ & \therefore \cos ^{-1} x=\frac{\pi}{2} \Rightarrow x=\cos \frac{\pi}{2}=0\end{aligned}$

</details>

---

### Q46. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\cos ^{-1}\left(\cos \frac{8 \pi}{3}\right)$ is

**Options:**

- **(A)** $\frac{8 \pi}{3}$
- **(B)** $\frac{\pi}{3}$
- **(C)** $\frac{2 \pi}{3}$
- **(D)** $\frac{3 \pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2 \pi}{3}$**

**Detailed Solution:**

No Solution

</details>

---

### Q47. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\cos ^{-1}\left(\cos \left(\frac{7 \pi}{6}\right)\right)$ is

**Options:**

- **(A)** $\frac{5 \pi}{6}$
- **(B)** $\frac{\pi}{3}$
- **(C)** $\frac{7 \pi}{6}$
- **(D)** $\frac{\pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{5 \pi}{6}$**

**Detailed Solution:**

Let $\alpha$ and $\beta$ are roots of quadratic equation Given, $\frac{\alpha+\beta}{2}=34$ $\alpha+\beta=68$
and $\sqrt{\alpha \beta}=16$ $\alpha \beta=256$
$\therefore$ Required quadratic equation is, $x^{2}-(\alpha+\beta) x+\alpha \beta=0$ $x^{2}-68 x+256=0$

</details>

---

### Q48. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\tan ^{-1}\left[\sqrt{\frac{1+\cos \frac{x}{2}}{1-\cos \frac{x}{2}}}\right]$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{-1}{3}$
- **(B)** $\frac{-1}{4}$
- **(C)** $\frac{1}{3}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-1}{4}$**

**Detailed Solution:**

Given $y=\tan ^{-1}\left[\sqrt{\frac{1+\cos \frac{x}{2}}{1-\cos \frac{x}{2}}}\right]$
$$
=\tan ^{-1} \sqrt{\frac{2 \cos ^{2} \frac{x}{4}}{2 \sin ^{2} \frac{x}{4}}}=\tan ^{-1}\left(\cot \frac{x}{4}\right)=\tan ^{-1}\left[\tan \left(\frac{\pi}{2}-\frac{x}{4}\right)\right]
$$
$\therefore y=-\frac{x}{4} \Rightarrow \frac{d y}{d x}=\frac{-1}{4}$

</details>

---

### Q49. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $u=\tan ^{-1}\left(\frac{\sqrt{1+x^{2}}-1}{x}\right)$ and $v=\tan ^{-1}\left(\frac{2 x \sqrt{1-x^{2}}}{1-2 x^{2}}\right)$, then $\frac{d u}{d v}$ at $x=0$ is

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{1}{8}$
- **(C)** 1
- **(D)** $\frac{-1}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{4}$**

**Detailed Solution:**

Given $u=\tan ^{-1}\left(\frac{\sqrt{1+x^{2}}-1}{x}\right)$
Put $x=\tan \theta$
$u=\tan ^{-1}\left(\frac{\sec \theta-1}{\tan \theta}\right) \quad=\tan ^{-1}\left(\frac{1-\cos \theta}{\sin \theta}\right)=\tan ^{-1}\left(\frac{2 \sin ^{2} \frac{\theta}{2}}{2 \sin \frac{\theta}{2} \cos }\right)$
$\therefore u=\frac{\tan ^{-1} x}{2} \Rightarrow \frac{d u}{d x}=\frac{1}{2\left(1+x^{2}\right)}$
We have, $v=\tan ^{-1}\left(\frac{2 x \sqrt{1-x^{2}}}{1-2 x^{2}}\right)$
Put $x=\sin \theta$
$\therefore v=\tan ^{-1}\left(\frac{2 \sin \theta \cdot \cos \theta}{\cos 2 \theta}\right)=\tan ^{-1}\left(\frac{\sin 2 \theta}{\cos 2 \theta}\right)=\tan ^{-1}(\tan 2 \theta)=2 \theta$
$\therefore v=2 \tan ^{-1} x \Rightarrow \frac{d v}{d x}=\frac{2}{1+x^{2}}$
$\left.\frac{d u}{d v}=\frac{d u}{d x}\right)=\frac{1}{2\left(1+x^{2}\right)} \times \frac{\left(1+x^{2}\right)}{2}=\frac{1}{4}$

</details>

---

### Q50. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\tan ^{-1}(\sec x+\tan x), \quad$ then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** 1
- **(C)** $\frac{-1}{2}$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

Given 
$\begin{aligned} y &=\tan ^{-1}\left(\frac{1}{\cos x}+\frac{\sin x}{\cos x}\right)=\tan ^{-1}\left(\frac{1+\sin x}{\cos x}\right) \\ &=\tan ^{-1}\left[\frac{\left(\cos ^{2} \frac{x}{2}+\sin ^{2} \frac{x}{2}\right)+2 \sin \frac{x}{2} \cos \frac{x}{2}}{\cos ^{2} \frac{x}{2}-\sin ^{2} \frac{x}{2}}\right) \\ &=\tan ^{-1}\left\{\frac{x}{\left(\cos \frac{x}{2}+\sin \frac{x}{2}\right)\left(\cos \frac{x}{2}-\sin \frac{x}{2}\right)}\right\} \\ &=\tan ^{-1}\left\{\frac{\cos \frac{x}{2}+\sin \frac{x}{2}}{\cos \frac{x}{2}-\sin \frac{x}{2}}\right\}=\tan ^{-1}\left(\frac{1+\tan \frac{x}{2}}{1-\tan \frac{x}{2}}\right) \\ &=\tan ^{-1}\left(\tan \left(\frac{\pi}{4}+\frac{x}{2}\right)\right) \end{aligned}$
$\begin{aligned} \mathrm{y} &=\frac{\pi}{4}+\frac{\mathrm{x}}{2} \\ \therefore \frac{\mathrm{dy}}{\mathrm{dx}} &=0+\frac{1}{2}=\frac{1}{2} \end{aligned}$

</details>

---

