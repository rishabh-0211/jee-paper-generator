# MHT CET Mathematics - Differentiation

## Topic 1: Differentiation of composite functions

**Total Questions:** 85

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = f\left(\dfrac{2x-1}{x^2+1}\right)$ and $f'(x) = \sin x^2$, then $\dfrac{dy}{dx}$ is equal to

**Options:**

- **(A)** $\sin\left(\dfrac{2x-1}{x^2+1}\right)^2 \left[\dfrac{2+2x+x^2}{(x^2+1)^2}\right]$
- **(B)** $\sin\left(\dfrac{2x-1}{x^2+1}\right)^2 \left[\dfrac{2+2x-2x^2}{(x^2+1)^2}\right]$
- **(C)** $\sin\left(\dfrac{2x-1}{x^2+1}\right)^2 \left[\dfrac{2+2x-x^2}{(x^2+1)^2}\right]$
- **(D)** $\sin\left(\dfrac{2x-1}{x^2+1}\right)^2 \left[\dfrac{2+2x+2x^2}{(x^2+1)^2}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sin\left(\dfrac{2x-1}{x^2+1}\right)^2 \left[\dfrac{2+2x-2x^2}{(x^2+1)^2}\right]$**

**Detailed Solution:**

Given $y = f\left(\dfrac{2x-1}{x^2+1}\right)$

Differentiating with respect to $x$ using the chain rule:

$\dfrac{dy}{dx} = f'\left(\dfrac{2x-1}{x^2+1}\right) \cdot \dfrac{d}{dx}\left(\dfrac{2x-1}{x^2+1}\right)$

Since $f'(x) = \sin x^2$, we have:

$f'\left(\dfrac{2x-1}{x^2+1}\right) = \sin\left(\dfrac{2x-1}{x^2+1}\right)^2$

Applying the quotient rule for the derivative of the inner function:

$\dfrac{d}{dx}\left(\dfrac{2x-1}{x^2+1}\right) = \dfrac{(x^2+1)(2) - (2x-1)(2x)}{(x^2+1)^2}$

$\dfrac{d}{dx}\left(\dfrac{2x-1}{x^2+1}\right) = \dfrac{2x^2 + 2 - 4x^2 + 2x}{(x^2+1)^2}$

$\dfrac{d}{dx}\left(\dfrac{2x-1}{x^2+1}\right) = \dfrac{2 + 2x - 2x^2}{(x^2+1)^2}$

Substituting these back, we obtain:

$\dfrac{dy}{dx} = \sin\left(\dfrac{2x-1}{x^2+1}\right)^2 \left[\dfrac{2+2x-2x^2}{(x^2+1)^2}\right]$

Answer: $\sin\left(\dfrac{2x-1}{x^2+1}\right)^2 \left[\dfrac{2+2x-2x^2}{(x^2+1)^2}\right]$

</details>

---

### Q2. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $h(x) = 2g\{3g[4g(5g(x))]\}$ such that $g(0) = 0$ and $g'(0) = 2$ then $h'(0) =$

**Options:**

- **(A)** $1920$
- **(B)** $0$
- **(C)** $120$
- **(D)** $1900$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1920$**

**Detailed Solution:**

Given $h(x) = 2g(3g(4g(5g(x))))$.

Using the chain rule to differentiate $h(x)$ with respect to $x$, we get:

$h'(x) = 2g'(3g(4g(5g(x)))) \cdot \dfrac{d}{dx}[3g(4g(5g(x)))]$

$h'(x) = 2g'(3g(4g(5g(x)))) \cdot 3g'(4g(5g(x))) \cdot \dfrac{d}{dx}[4g(5g(x))]$

$h'(x) = 2g'(3g(4g(5g(x)))) \cdot 3g'(4g(5g(x))) \cdot 4g'(5g(x)) \cdot \dfrac{d}{dx}[5g(x)]$

$h'(x) = 2g'(3g(4g(5g(x)))) \cdot 3g'(4g(5g(x))) \cdot 4g'(5g(x)) \cdot 5g'(x)$

We are given $g(0) = 0$. Substituting $x = 0$ into the inner functions:

$5g(0) = 5(0) = 0$

$4g(5g(0)) = 4g(0) = 0$

$3g(4g(5g(0))) = 3g(0) = 0$

Now, substituting $x = 0$ into the expression for $h'(x)$:

$h'(0) = 2g'(0) \cdot 3g'(0) \cdot 4g'(0) \cdot 5g'(0)$

$h'(0) = 120(g'(0))^4$

We are also given $g'(0) = 2$. Substituting this value:

$h'(0) = 120(2)^4$

$h'(0) = 120 \times 16 = 1920$

Answer: $1920$

</details>

---

### Q3. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \sqrt{1 + \cos^2(x^2)}$, then $f'\left(\dfrac{\sqrt{\pi}}{2}\right) = \ldots$

**Options:**

- **(A)** $\sqrt{\dfrac{\pi}{6}}$
- **(B)** $\sqrt{\dfrac{\pi}{4}}$
- **(C)** $-\sqrt{\dfrac{\pi}{6}}$
- **(D)** $-\sqrt{\dfrac{\pi}{4}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\sqrt{\dfrac{\pi}{6}}$**

**Detailed Solution:**

Given $f(x) = \sqrt{1 + \cos^2(x^2)}$

Differentiating with respect to $x$ using the chain rule:

$f'(x) = \dfrac{1}{2\sqrt{1 + \cos^2(x^2)}} \cdot \dfrac{d}{dx}(1 + \cos^2(x^2))$

$f'(x) = \dfrac{1}{2\sqrt{1 + \cos^2(x^2)}} \cdot 2\cos(x^2) \cdot (-\sin(x^2)) \cdot 2x$

$f'(x) = \dfrac{-2x \cos(x^2) \sin(x^2)}{\sqrt{1 + \cos^2(x^2)}}$

Substitute $x = \dfrac{\sqrt{\pi}}{2}$, which gives $x^2 = \dfrac{\pi}{4}$:

$f'\left(\dfrac{\sqrt{\pi}}{2}\right) = \dfrac{-2 \left(\dfrac{\sqrt{\pi}}{2}\right) \cos\left(\dfrac{\pi}{4}\right) \sin\left(\dfrac{\pi}{4}\right)}{\sqrt{1 + \cos^2\left(\dfrac{\pi}{4}\right)}}$

Since $\cos\left(\dfrac{\pi}{4}\right) = \dfrac{1}{\sqrt{2}}$ and $\sin\left(\dfrac{\pi}{4}\right) = \dfrac{1}{\sqrt{2}}$:

$f'\left(\dfrac{\sqrt{\pi}}{2}\right) = \dfrac{-\sqrt{\pi} \cdot \dfrac{1}{\sqrt{2}} \cdot \dfrac{1}{\sqrt{2}}}{\sqrt{1 + \left(\dfrac{1}{\sqrt{2}}\right)^2}}$

$f'\left(\dfrac{\sqrt{\pi}}{2}\right) = \dfrac{-\dfrac{\sqrt{\pi}}{2}}{\sqrt{1 + \dfrac{1}{2}}}$

$f'\left(\dfrac{\sqrt{\pi}}{2}\right) = \dfrac{-\dfrac{\sqrt{\pi}}{2}}{\sqrt{\dfrac{3}{2}}} = -\dfrac{\sqrt{\pi}}{2} \cdot \dfrac{\sqrt{2}}{\sqrt{3}} = -\sqrt{\dfrac{\pi}{6}}$

Answer: $-\sqrt{\dfrac{\pi}{6}}$

</details>

---

### Q4. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \log\left(\dfrac{1+x}{1-x}\right)$ and $g(x) = \left(\dfrac{3x + x^3}{1 + 3x^2}\right)$, then $\dfrac{d}{dx}(f(g(x))) = $

**Options:**

- **(A)** $f'(x)$
- **(B)** $g'(x)$
- **(C)** $3g'(x)$
- **(D)** $3f'(x)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3f'(x)$**

**Detailed Solution:**

$f(g(x)) = \log\left(\dfrac{1+g(x)}{1-g(x)}\right)$

Substituting $g(x) = \dfrac{3x + x^3}{1 + 3x^2}$:

$\dfrac{1+g(x)}{1-g(x)} = \dfrac{1 + \dfrac{3x + x^3}{1 + 3x^2}}{1 - \dfrac{3x + x^3}{1 + 3x^2}}$

$\dfrac{1+g(x)}{1-g(x)} = \dfrac{1 + 3x^2 + 3x + x^3}{1 + 3x^2 - 3x - x^3}$

$\dfrac{1+g(x)}{1-g(x)} = \dfrac{(1+x)^3}{(1-x)^3} = \left(\dfrac{1+x}{1-x}\right)^3$

Therefore, $f(g(x)) = \log\left(\left(\dfrac{1+x}{1-x}\right)^3\right)$

$f(g(x)) = 3\log\left(\dfrac{1+x}{1-x}\right) = 3f(x)$

Differentiating both sides with respect to $x$:

$\dfrac{d}{dx}(f(g(x))) = \dfrac{d}{dx}(3f(x)) = 3f'(x)$

Answer: $3f'(x)$

</details>

---

### Q5. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x = \dfrac{1 - \sqrt{y}}{1 + \sqrt{y}}$, then $\dfrac{dy}{dx} = $

**Options:**

- **(A)** $\dfrac{4(x-1)}{(x+1)^3}$
- **(B)** $\dfrac{4(x+1)}{(x-1)^3}$
- **(C)** $\dfrac{(x-1)}{(x+1)^3}$
- **(D)** $\dfrac{4(1-x)}{(x+1)^3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{4(x-1)}{(x+1)^3}$**

**Detailed Solution:**

Given $x = \dfrac{1 - \sqrt{y}}{1 + \sqrt{y}}$

Applying componendo and dividendo, we get:

$\dfrac{x + 1}{x - 1} = \dfrac{(1 - \sqrt{y}) + (1 + \sqrt{y})}{(1 - \sqrt{y}) - (1 + \sqrt{y})}$

$\dfrac{x + 1}{x - 1} = \dfrac{2}{-2\sqrt{y}}$

$\sqrt{y} = \dfrac{1 - x}{1 + x}$

Squaring both sides:

$y = \left(\dfrac{1 - x}{1 + x}\right)^2$

Differentiating with respect to $x$ using the chain rule and quotient rule:

$\dfrac{dy}{dx} = 2\left(\dfrac{1 - x}{1 + x}\right) \cdot \dfrac{d}{dx}\left(\dfrac{1 - x}{1 + x}\right)$

$\dfrac{dy}{dx} = 2\left(\dfrac{1 - x}{1 + x}\right) \cdot \left[\dfrac{(-1)(1 + x) - (1 - x)(1)}{(1 + x)^2}\right]$

$\dfrac{dy}{dx} = 2\left(\dfrac{1 - x}{1 + x}\right) \cdot \left[\dfrac{-1 - x - 1 + x}{(1 + x)^2}\right]$

$\dfrac{dy}{dx} = 2\left(\dfrac{1 - x}{1 + x}\right) \cdot \left[\dfrac{-2}{(1 + x)^2}\right]$

$\dfrac{dy}{dx} = \dfrac{-4(1 - x)}{(1 + x)^3}$

$\dfrac{dy}{dx} = \dfrac{4(x - 1)}{(x + 1)^3}$

Answer: $\dfrac{4(x-1)}{(x+1)^3}$

</details>

---

### Q6. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $g$ is a differentiable function of $x$ such that $g(x^5) = 3x^7$, for $x \neq 0$, $x \in \mathbb{R}$ then $g'(3125) = \ldots$

**Options:**

- **(A)** $125$
- **(B)** $210$
- **(C)** $105$
- **(D)** $441$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $105$**

**Detailed Solution:**

Given $g(x^5) = 3x^7$

Differentiating both sides with respect to $x$, we get:

$g'(x^5) \cdot 5x^4 = 21x^6$

$g'(x^5) = \dfrac{21x^6}{5x^4} = \dfrac{21}{5}x^2$

To find $g'(3125)$, we set $x^5 = 3125$, which gives $x = 5$.

Substituting $x = 5$ in the equation for $g'(x^5)$:

$g'(3125) = \dfrac{21}{5}(5)^2 = 21 \cdot 5 = 105$

Answer: $105$

</details>

---

### Q7. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)$ be a twice differentiable function such that $f''(x) = -f(x)$, and $f'(x) = g(x)$.
Let $h(x) = \{f(x)\}^2 + \{g(x)\}^2$. If $h(2) = 7$, then $h(8)$ is equal to:

**Options:**

- **(A)** $7$
- **(B)** $14$
- **(C)** $0$
- **(D)** not defined

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $7$**

**Detailed Solution:**

Given $h(x) = \{f(x)\}^2 + \{g(x)\}^2$

Differentiating with respect to $x$:

$h'(x) = 2f(x)f'(x) + 2g(x)g'(x)$

Given $f'(x) = g(x)$, differentiating this gives $g'(x) = f''(x)$.

Also given $f''(x) = -f(x)$, so $g'(x) = -f(x)$.

Substituting $f'(x)$ and $g'(x)$ in $h'(x)$:

$h'(x) = 2f(x)g(x) + 2g(x)(-f(x)) = 0$

Since $h'(x) = 0$, $h(x)$ is a constant function.

Given $h(2) = 7$, we have $h(x) = 7$ for all $x$.

Therefore, $h(8) = 7$

Answer: $7$

</details>

---

### Q8. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f'\left(\dfrac{1}{2}\right) = \sqrt{3}$ and $g'\left(\dfrac{\sqrt{3}}{2}\right) = -2$, then the derivative of $f(\sin x)$ with respect to $g(\cos x)$ at $x = \dfrac{\pi}{6}$ is:

**Options:**

- **(A)** $1$
- **(B)** $\dfrac{\sqrt{3}}{2}$
- **(C)** $\dfrac{1}{2}$
- **(D)** $\dfrac{3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{3}{2}$**

**Detailed Solution:**

Let $u = f(\sin x)$ and $v = g(\cos x)$.

Differentiating $u$ and $v$ with respect to $x$:

$\dfrac{du}{dx} = f'(\sin x) \cos x$

$\dfrac{dv}{dx} = -g'(\cos x) \sin x$

The derivative of $u$ with respect to $v$ is:

$\dfrac{du}{dv} = \dfrac{\dfrac{du}{dx}}{\dfrac{dv}{dx}} = \dfrac{f'(\sin x) \cos x}{-g'(\cos x) \sin x}$

At $x = \dfrac{\pi}{6}$:

$\sin\left(\dfrac{\pi}{6}\right) = \dfrac{1}{2}$ and $\cos\left(\dfrac{\pi}{6}\right) = \dfrac{\sqrt{3}}{2}$

Substituting these values into the expression for $\dfrac{du}{dv}$:

$\dfrac{du}{dv} = \dfrac{f'\left(\dfrac{1}{2}\right) \cdot \dfrac{\sqrt{3}}{2}}{-g'\left(\dfrac{\sqrt{3}}{2}\right) \cdot \dfrac{1}{2}}$

Given $f'\left(\dfrac{1}{2}\right) = \sqrt{3}$ and $g'\left(\dfrac{\sqrt{3}}{2}\right) = -2$:

$\dfrac{du}{dv} = \dfrac{\sqrt{3} \cdot \dfrac{\sqrt{3}}{2}}{-(-2) \cdot \dfrac{1}{2}} = \dfrac{\dfrac{3}{2}}{1} = \dfrac{3}{2}$

Answer: $\dfrac{3}{2}$

</details>

---

### Q9. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the derivative of $\tan^{-1}(a + bx)$ at $x = 0$ is $1$, then $1 - b^3 + a^6$ is:

**Options:**

- **(A)** $3b^2 a$
- **(B)** $-6a^2 b$
- **(C)** $-3b^2 a$
- **(D)** $-3a^2 b$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-3a^2 b$**

**Detailed Solution:**

Let $y = \tan^{-1}(a + bx)$

Differentiating with respect to $x$, we get:

$\dfrac{dy}{dx} = \dfrac{1}{1 + (a + bx)^2} \cdot b$

At $x = 0$, $\dfrac{dy}{dx} = \dfrac{b}{1 + a^2}$

Given that the derivative at $x = 0$ is $1$:

$\dfrac{b}{1 + a^2} = 1 \Rightarrow b = 1 + a^2$

We need to find the value of $1 - b^3 + a^6$

Substituting $b = 1 + a^2$:

$1 - b^3 + a^6 = 1 - (1 + a^2)^3 + a^6$

$= 1 - (1 + 3a^2 + 3a^4 + a^6) + a^6$

$= -3a^2 - 3a^4$

$= -3a^2(1 + a^2)$

Since $1 + a^2 = b$, we get:

$1 - b^3 + a^6 = -3a^2 b$

Answer: $-3a^2 b$

</details>

---

### Q10. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \dfrac{x-1}{4} + \dfrac{(x-1)^3}{12} + \dfrac{(x-1)^5}{20} + \dfrac{(x-1)^7}{28} + \ldots$ where $0 < x < 2$, then $f'(x) =$

**Options:**

- **(A)** $\dfrac{1}{2x(2+x)}$
- **(B)** $\dfrac{1}{4x(2+x)}$
- **(C)** $\dfrac{1}{4x(2-x)}$
- **(D)** $\dfrac{1}{2x(2-x)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{4x(2-x)}$**

**Detailed Solution:**

Given $f(x) = \dfrac{x-1}{4} + \dfrac{(x-1)^3}{12} + \dfrac{(x-1)^5}{20} + \ldots$

Differentiating both sides with respect to $x$:

$f'(x) = \dfrac{1}{4} + \dfrac{3(x-1)^2}{12} + \dfrac{5(x-1)^4}{20} + \ldots$

$f'(x) = \dfrac{1}{4} + \dfrac{(x-1)^2}{4} + \dfrac{(x-1)^4}{4} + \ldots$

$f'(x) = \dfrac{1}{4} [1 + (x-1)^2 + (x-1)^4 + \ldots]$

The series in the bracket is an infinite geometric progression with first term $1$ and common ratio $(x-1)^2$.

Since $0 < x < 2$, we have $-1 < x-1 < 1$, which implies $0 \le (x-1)^2 < 1$.

Using the sum of an infinite geometric progression $S = \dfrac{a}{1-r}$:

$f'(x) = \dfrac{1}{4} \left[ \dfrac{1}{1 - (x-1)^2} \right]$

$f'(x) = \dfrac{1}{4} \left[ \dfrac{1}{1 - (x^2 - 2x + 1)} \right]$

$f'(x) = \dfrac{1}{4(2x - x^2)}$

$f'(x) = \dfrac{1}{4x(2-x)}$

Answer: $\dfrac{1}{4x(2-x)}$

</details>

---

### Q11. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = 4^{\log_4(x+2) - \log_4(x-2)}$, then $\dfrac{dy}{dx} =$

**Options:**

- **(A)** $-\dfrac{4}{(x-2)^2}$
- **(B)** $\dfrac{4}{(x-2)^2}$
- **(C)** $-\dfrac{4}{(x+2)^2}$
- **(D)** $\dfrac{4}{(x+2)^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\dfrac{4}{(x-2)^2}$**

**Detailed Solution:**

Given $y = 4^{\log_4(x+2) - \log_4(x-2)}$

Using the logarithmic property $\log_a m - \log_a n = \log_a \left(\dfrac{m}{n}\right)$, we get:

$y = 4^{\log_4\left(\dfrac{x+2}{x-2}\right)}$

Using the property $a^{\log_a z} = z$, the expression simplifies to:

$y = \dfrac{x+2}{x-2}$

Differentiating with respect to $x$ using the quotient rule:

$\dfrac{dy}{dx} = \dfrac{(x-2) \cdot \dfrac{d}{dx}(x+2) - (x+2) \cdot \dfrac{d}{dx}(x-2)}{(x-2)^2}$

$\dfrac{dy}{dx} = \dfrac{(x-2)(1) - (x+2)(1)}{(x-2)^2}$

$\dfrac{dy}{dx} = \dfrac{x - 2 - x - 2}{(x-2)^2}$

$\dfrac{dy}{dx} = -\dfrac{4}{(x-2)^2}$

Answer: $-\dfrac{4}{(x-2)^2}$

</details>

---

### Q12. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \sin(2\sin^{-1} x)$, then $\dfrac{dy}{dx} = $ ______

**Options:**

- **(A)** $\dfrac{2 - 4x^2}{\sqrt{1 - x^2}}$
- **(B)** $\dfrac{2 + 4x^2}{\sqrt{1 - x^2}}$
- **(C)** $\dfrac{4x^2 - 1}{2\sqrt{1 - x^2}}$
- **(D)** $\dfrac{1 - 2x^2}{\sqrt{1 - x^2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{2 - 4x^2}{\sqrt{1 - x^2}}$**

**Detailed Solution:**

Given $y = \sin(2\sin^{-1} x)$

Differentiating with respect to $x$ using the chain rule:

$\dfrac{dy}{dx} = \cos(2\sin^{-1} x) \cdot \dfrac{d}{dx}(2\sin^{-1} x)$

$\dfrac{dy}{dx} = \cos(2\sin^{-1} x) \cdot \dfrac{2}{\sqrt{1 - x^2}}$

Using the trigonometric identity $\cos(2\theta) = 1 - 2\sin^2\theta$, substituting $\theta = \sin^{-1} x$:

$\cos(2\sin^{-1} x) = 1 - 2\sin^2(\sin^{-1} x) = 1 - 2x^2$

Substituting this back into the derivative:

$\dfrac{dy}{dx} = (1 - 2x^2) \cdot \dfrac{2}{\sqrt{1 - x^2}}$

$\dfrac{dy}{dx} = \dfrac{2 - 4x^2}{\sqrt{1 - x^2}}$

Answer: $\dfrac{2 - 4x^2}{\sqrt{1 - x^2}}$

</details>

---

### Q13. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)$ is a differentiable function of $x$, then $\lim_{h \to 0} \dfrac{[f(x+h)]^2 - [f(x)]^2}{2h} = $

**Options:**

- **(A)** $[f(x)]^2$
- **(B)** $f(x) \cdot f'(x)$
- **(C)** $f(x) + f'(x)$
- **(D)** $[f(x) \cdot f'(x)]^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $f(x) \cdot f'(x)$**

**Detailed Solution:**

$\lim_{h \to 0} \dfrac{[f(x+h)]^2 - [f(x)]^2}{2h}$

$= \lim_{h \to 0} \left( \dfrac{f(x+h) - f(x)}{h} \right) \cdot \left( \dfrac{f(x+h) + f(x)}{2} \right)$

$= f'(x) \cdot \dfrac{f(x) + f(x)}{2}$

$= f(x) \cdot f'(x)$

Answer: $f(x) \cdot f'(x)$

</details>

---

### Q14. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = 2^{2x-1}$ and $\phi(x) = -2^x + x \log 4$, such that $f'(x) > \phi'(x)$, then the set of all possible values of $x$ is...

**Options:**

- **(A)** $(-\infty, 0)$
- **(B)** $(0, \infty)$
- **(C)** $[0, \infty)$
- **(D)** $(0, 1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(0, \infty)$**

**Detailed Solution:**

Given $f(x) = 2^{2x-1}$ and $\phi(x) = -2^x + x \log_{e} 4$.

Differentiating both functions with respect to $x$:

$f'(x) = 2^{2x-1} \cdot 2 \cdot \log_{e} 2 = 2^{2x} \log_{e} 2$

$\phi'(x) = -2^x \log_{e} 2 + \log_{e} 4 = -2^x \log_{e} 2 + 2 \log_{e} 2$

Given that $f'(x) > \phi'(x)$:

$2^{2x} \log_{e} 2 > -2^x \log_{e} 2 + 2 \log_{e} 2$

Since $\log_{e} 2 > 0$, dividing the entire inequality by $\log_{e} 2$ gives:

$2^{2x} > -2^x + 2$

$2^{2x} + 2^x - 2 > 0$

$(2^x + 2)(2^x - 1) > 0$

Since $2^x > 0$ for all real $x$, the term $(2^x + 2)$ is always positive. Therefore, we must have:

$2^x - 1 > 0$

$2^x > 1$

$2^x > 2^0$

$x > 0$

The set of all possible values of $x$ is $(0, \infty)$.

Answer: $(0, \infty)$

</details>

---

### Q15. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\dfrac{d}{dx}\left(\dfrac{1 + x^4 + x^8}{1 + x^2 + x^4}\right) = ax^3 + bx$, then the values of $a$ and $b$ are respectively...

**Options:**

- **(A)** $a = 4, b = 2$
- **(B)** $a = 4, b = -2$
- **(C)** $a = -2, b = 4$
- **(D)** $a = -4, b = 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $a = 4, b = -2$**

**Detailed Solution:**

The expression inside the derivative can be simplified by factoring the numerator.

Consider the term $1 + x^4 + x^8$. By adding and subtracting $x^4$, we get:

$1 + x^4 + x^8 = (x^8 + 2x^4 + 1) - x^4$

$= (x^4 + 1)^2 - (x^2)^2$

Using the difference of squares formula $A^2 - B^2 = (A - B)(A + B)$:

$1 + x^4 + x^8 = (x^4 - x^2 + 1)(x^4 + x^2 + 1)$

Substituting this back into the given expression:

$\dfrac{1 + x^4 + x^8}{1 + x^2 + x^4} = \dfrac{(x^4 - x^2 + 1)(x^4 + x^2 + 1)}{1 + x^2 + x^4} = x^4 - x^2 + 1$

Now, differentiating with respect to $x$:

$\dfrac{d}{dx}(x^4 - x^2 + 1) = 4x^3 - 2x$

Comparing this result with $ax^3 + bx$, we get:

$a = 4$ and $b = -2$

Answer: $a = 4, b = -2$

</details>

---

### Q16. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y = \left(\sqrt{x} + \dfrac{1}{\sqrt{x}}\right)^2$ and $\dfrac{dy}{dx} = \dfrac{3}{4}$, then the value of $x$ is...

**Options:**

- **(A)** $\sqrt{2}$
- **(B)** $2$
- **(C)** $\dfrac{1}{\sqrt{3}}$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$**

**Detailed Solution:**

$y = \left(\sqrt{x} + \dfrac{1}{\sqrt{x}}\right)^2$

$y = x + 2 + \dfrac{1}{x}$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = 1 - \dfrac{1}{x^2}$

Given $\dfrac{dy}{dx} = \dfrac{3}{4}$:

$1 - \dfrac{1}{x^2} = \dfrac{3}{4}$

$\dfrac{1}{x^2} = \dfrac{1}{4}$

$x^2 = 4$

$x = \pm 2$

Since $\sqrt{x}$ is defined only for $x > 0$, we have $x = 2$.

Answer: $2$

</details>

---

### Q17. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=(x-1)(x-2)(x-3)\cdots(x-100)$ and the value of $\dfrac{dy}{dx}$ at $x=5$ is equal to $\lambda\left(\dfrac{100!}{{}^{100}C_5}\right)$, then $\lambda=$ ...

**Options:**

- **(A)** $-5$
- **(B)** $-\dfrac{1}{5}$
- **(C)** $5$
- **(D)** $\dfrac{1}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\dfrac{1}{5}$**

**Detailed Solution:**

Given $y = (x-1)(x-2)(x-3)\cdots(x-100)$

Differentiating with respect to $x$ using the product rule, we get a sum of $100$ terms. At $x=5$, all terms containing the factor $(x-5)$ will become zero.

The only non-zero term is the one where $(x-5)$ is differentiated.

$\dfrac{dy}{dx} \Big|_{x=5} = (5-1)(5-2)(5-3)(5-4)(5-6)\cdots(5-100)$

$= (4)(3)(2)(1)(-1)(-2)\cdots(-95)$

$= 4! \times (-1)^{95} \times 95! = -4! \times 95!$

We are given that $\dfrac{dy}{dx} \Big|_{x=5} = \lambda \left( \dfrac{100!}{^{100}C_5} \right)$

Using the formula $^{n}C_{r} = \dfrac{n!}{r!(n-r)!}$, we have $^{100}C_5 = \dfrac{100!}{5! \times 95!}$

$\Rightarrow \dfrac{100!}{^{100}C_5} = 5! \times 95!$

Equating the two expressions:

$-4! \times 95! = \lambda \times 5! \times 95!$

$-4! = \lambda \times 5!$

$\lambda = -\dfrac{4!}{5!} = -\dfrac{1}{5}$

Answer: $-\dfrac{1}{5}$

</details>

---

### Q18. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $f(\sin x)$ with respect to $g(\sec x)$ at $x = \dfrac{\pi}{4}$, given that $f'\left(\dfrac{1}{\sqrt{2}}\right) = 3$ and $g'(\sqrt{2}) = 1$ is.....

**Options:**

- **(A)** $\dfrac{\sqrt{3}}{2}$
- **(B)** $\dfrac{3}{2}$
- **(C)** $\dfrac{1}{3}$
- **(D)** $\dfrac{-1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{3}{2}$**

**Detailed Solution:**

Let $u = f(\sin x)$ and $v = g(\sec x)$

$\dfrac{du}{dx} = f'(\sin x) \cos x$

$\dfrac{dv}{dx} = g'(\sec x) \sec x \tan x$

$\dfrac{du}{dv} = \dfrac{\dfrac{du}{dx}}{\dfrac{dv}{dx}} = \dfrac{f'(\sin x) \cos x}{g'(\sec x) \sec x \tan x}$

At $x = \dfrac{\pi}{4}$:

$\dfrac{du}{dv} = \dfrac{f'\left(\dfrac{1}{\sqrt{2}}\right) \cdot \dfrac{1}{\sqrt{2}}}{g'(\sqrt{2}) \cdot \sqrt{2} \cdot 1}$

Substituting $f'\left(\dfrac{1}{\sqrt{2}}\right) = 3$ and $g'(\sqrt{2}) = 1$:

$\dfrac{du}{dv} = \dfrac{3 \cdot \dfrac{1}{\sqrt{2}}}{1 \cdot \sqrt{2}} = \dfrac{3}{2}$

Answer: $\dfrac{3}{2}$

</details>

---

### Q19. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \sin(2\sin^{-1} x)$ then $\dfrac{dy}{dx} =$..

**Options:**

- **(A)** $\dfrac{2 - 4x^2}{\sqrt{1 - x^2}}$
- **(B)** $\dfrac{2 + 4x^2}{\sqrt{1 - x^2}}$
- **(C)** $\dfrac{2 - 4x^2}{\sqrt{1 + x^2}}$
- **(D)** $\dfrac{2 + 4x^2}{\sqrt{1 + x^2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{2 - 4x^2}{\sqrt{1 - x^2}}$**

**Detailed Solution:**

Given $y = \sin(2\sin^{-1} x)$

Differentiating with respect to $x$ using the chain rule:

$\dfrac{dy}{dx} = \cos(2\sin^{-1} x) \cdot \dfrac{d}{dx}(2\sin^{-1} x)$

$\dfrac{dy}{dx} = \cos(2\sin^{-1} x) \cdot \dfrac{2}{\sqrt{1 - x^2}}$

Using the trigonometric identity $\cos(2\theta) = 1 - 2\sin^2\theta$, we can write:

$\cos(2\sin^{-1} x) = 1 - 2\sin^2(\sin^{-1} x) = 1 - 2x^2$

Substituting this back into the derivative:

$\dfrac{dy}{dx} = (1 - 2x^2) \cdot \dfrac{2}{\sqrt{1 - x^2}}$

$\dfrac{dy}{dx} = \dfrac{2 - 4x^2}{\sqrt{1 - x^2}}$

</details>

---

### Q20. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int f'(x) \cdot e^{x^2}\,dx = (x - 1) \cdot e^{x^2} + k$, where $k$ is constant of integration, then $f(x) = \ldots$

**Options:**

- **(A)** $2x^3 - \dfrac{x^2}{2} + x + c$, where $c$ is constant of integration.
- **(B)** $\dfrac{x^3}{2} + 3x^2 + 4x + c$, where $c$ is constant of integration.
- **(C)** $x^3 + 4x^2 + 6x + c$, where $c$ is constant of integration.
- **(D)** $\dfrac{2x^3}{3} - x^2 + x + c$, where $c$ is constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{2x^3}{3} - x^2 + x + c$, where $c$ is constant of integration.**

**Detailed Solution:**

Differentiating both sides of the given equation with respect to $x$:

$\dfrac{d}{dx} \left[ \int f'(x) \cdot e^{x^2}\,dx \right] = \dfrac{d}{dx} \left[ (x - 1) \cdot e^{x^2} + k \right]$

$f'(x) \cdot e^{x^2} = 1 \cdot e^{x^2} + (x - 1) \cdot e^{x^2} \cdot (2x)$

$f'(x) \cdot e^{x^2} = e^{x^2} (1 + 2x^2 - 2x)$

Dividing both sides by $e^{x^2}$:

$f'(x) = 2x^2 - 2x + 1$

Integrating both sides with respect to $x$ to find $f(x)$:

$f(x) = \int (2x^2 - 2x + 1)\,dx$

$f(x) = \dfrac{2x^3}{3} - x^2 + x + c$

where $c$ is the constant of integration.

Answer: $\dfrac{2x^3}{3} - x^2 + x + c$, where $c$ is constant of integration.

</details>

---

### Q21. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f'(x) = \sin^2 x$ and $y = f\left(\dfrac{2x-1}{x^2+1}\right)$, then $\dfrac{dy}{dx}$ at $x = 1$ is

**Options:**

- **(A)** $\dfrac{1}{4}\sin\left(\dfrac{1}{2}\right)$
- **(B)** $\dfrac{1}{4}\sin^2\left(\dfrac{1}{2}\right)$
- **(C)** $\sin^2\left(\dfrac{1}{4}\right)$
- **(D)** $\dfrac{1}{2}\sin^2\left(\dfrac{1}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{2}\sin^2\left(\dfrac{1}{2}\right)$**

**Detailed Solution:**

Given $y = f\left(\dfrac{2x-1}{x^2+1}\right)$

Differentiating with respect to $x$ using the chain rule:

$\dfrac{dy}{dx} = f'\left(\dfrac{2x-1}{x^2+1}\right) \cdot \dfrac{d}{dx}\left(\dfrac{2x-1}{x^2+1}\right)$

$\dfrac{dy}{dx} = f'\left(\dfrac{2x-1}{x^2+1}\right) \cdot \left[ \dfrac{(x^2+1)(2) - (2x-1)(2x)}{(x^2+1)^2} \right]$

Substituting $x = 1$:

$\left. \dfrac{dy}{dx} \right|_{x=1} = f'\left(\dfrac{2(1)-1}{1^2+1}\right) \cdot \left[ \dfrac{(1^2+1)(2) - (2(1)-1)(2(1))}{(1^2+1)^2} \right]$

$\left. \dfrac{dy}{dx} \right|_{x=1} = f'\left(\dfrac{1}{2}\right) \cdot \left[ \dfrac{4 - 2}{4} \right]$

$\left. \dfrac{dy}{dx} \right|_{x=1} = f'\left(\dfrac{1}{2}\right) \cdot \dfrac{1}{2}$

Since $f'(x) = \sin^2 x$, we have $f'\left(\dfrac{1}{2}\right) = \sin^2\left(\dfrac{1}{2}\right)$

$\left. \dfrac{dy}{dx} \right|_{x=1} = \dfrac{1}{2}\sin^2\left(\dfrac{1}{2}\right)$

Answer: $\dfrac{1}{2}\sin^2\left(\dfrac{1}{2}\right)$

</details>

---

### Q22. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $g(x) = (x^2 + 2x + 1)\cdot f(x)$ such that $f(0) = 5$ and $\lim\limits_{x \to 0}\dfrac{f(x)-5}{x} = 4$ then $g'(0) = $

**Options:**

- **(A)** $20$
- **(B)** $12$
- **(C)** $18$
- **(D)** $14$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $14$**

**Detailed Solution:**

Given $g(x) = (x^2 + 2x + 1) f(x)$

Differentiating with respect to $x$ using the product rule:

$g'(x) = (2x + 2) f(x) + (x^2 + 2x + 1) f'(x)$

Substituting $x = 0$:

$g'(0) = 2 f(0) + f'(0)$

From the given limit, $\lim\limits_{x \to 0}\dfrac{f(x)-5}{x} = 4$, which represents the derivative of $f(x)$ at $x = 0$.

Thus, $f'(0) = 4$.

Also given $f(0) = 5$.

Substituting these values:

$g'(0) = 2(5) + 4 = 14$

Answer: $14$

</details>

---

### Q23. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \cos x\,\cos 2x\,\cos 4x\,\cos 8x\,\cos 16x$, then $f'\left(\dfrac{\pi}{4}\right) =$

**Options:**

- **(A)** $\text{cosec}\left(\dfrac{\pi}{4}\right)$
- **(B)** $\cos\left(\dfrac{\pi}{4}\right)$
- **(C)** $\tan\left(\dfrac{\pi}{4}\right)$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\text{cosec}\left(\dfrac{\pi}{4}\right)$**

**Detailed Solution:**

Using the trigonometric identity $\cos x \cos 2x \cos 2^2x \dots \cos 2^{n-1}x = \dfrac{\sin(2^n x)}{2^n \sin x}$

For $n=5$, the given function can be written as:

$f(x) = \dfrac{\sin(32x)}{32 \sin x}$

Differentiating with respect to $x$ using the quotient rule:

$f'(x) = \dfrac{32 \sin x \cdot 32 \cos(32x) - \sin(32x) \cdot 32 \cos x}{(32 \sin x)^2}$

$f'(x) = \dfrac{32 \cos(32x) \sin x - \sin(32x) \cos x}{32 \sin^2 x}$

Substituting $x = \dfrac{\pi}{4}$:

$32x = 32 \times \dfrac{\pi}{4} = 8\pi$

Since $\cos(8\pi) = 1$ and $\sin(8\pi) = 0$, we get:

$f'\left(\dfrac{\pi}{4}\right) = \dfrac{32(1)\sin\left(\dfrac{\pi}{4}\right) - 0}{32 \sin^2\left(\dfrac{\pi}{4}\right)}$

$f'\left(\dfrac{\pi}{4}\right) = \dfrac{1}{\sin\left(\dfrac{\pi}{4}\right)}$

$f'\left(\dfrac{\pi}{4}\right) = \text{cosec}\left(\dfrac{\pi}{4}\right)$

Answer: $\text{cosec}\left(\dfrac{\pi}{4}\right)$

</details>

---

### Q24. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \sqrt{\cos x^2 + \sqrt{\cos x^2 + \sqrt{\cos x^2 + \ldots \infty}}}$ and $\dfrac{dy}{dx} = \dfrac{f(x)}{2y - 1}$ then, $\int f(x)\, dx = \ldots$

**Options:**

- **(A)** $\sin x^2 + c$
- **(B)** $-\sin x^2 + c$
- **(C)** $\cos x^2 + c$
- **(D)** $-\cos x^2 + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\cos x^2 + c$**

**Detailed Solution:**

Given $y = \sqrt{\cos x^2 + \sqrt{\cos x^2 + \sqrt{\cos x^2 + \ldots \infty}}}$

Squaring both sides:

$y^2 = \cos x^2 + y$

Differentiating both sides with respect to $x$:

$2y \dfrac{dy}{dx} = -2x \sin x^2 + \dfrac{dy}{dx}$

$(2y - 1) \dfrac{dy}{dx} = -2x \sin x^2$

$\dfrac{dy}{dx} = \dfrac{-2x \sin x^2}{2y - 1}$

Comparing with $\dfrac{dy}{dx} = \dfrac{f(x)}{2y - 1}$:

$f(x) = -2x \sin x^2$

Evaluating the integral:

$\int f(x) \, dx = \int -2x \sin x^2 \, dx$

Substituting $x^2 = t \Rightarrow 2x \, dx = dt$:

$\int -\sin t \, dt = \cos t + c$

$\int f(x) \, dx = \cos x^2 + c$

Answer: $\cos x^2 + c$

</details>

---

### Q25. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y = x \cdot 7^x$, then the value of $\dfrac{dx}{dy}$ when $x = 1$ is

**Options:**

- **(A)** $7(\log 7 + 1)$
- **(B)** $\log 7 + 1$
- **(C)** $\dfrac{1}{7(\log 7 + 1)}$
- **(D)** $\dfrac{1}{\log 7 + 1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{7(\log 7 + 1)}$**

**Detailed Solution:**

Given $y = x \cdot 7^x$

Differentiating with respect to $x$ using the product rule:

$\dfrac{dy}{dx} = 1 \cdot 7^x + x \cdot 7^x \log 7$

$\dfrac{dy}{dx} = 7^x(1 + x \log 7)$

Substituting $x = 1$:

$\left. \dfrac{dy}{dx} \right|_{x=1} = 7^1(1 + 1 \cdot \log 7) = 7(1 + \log 7)$

Since $\dfrac{dx}{dy} = \dfrac{1}{\dfrac{dy}{dx}}$:

$\left. \dfrac{dx}{dy} \right|_{x=1} = \dfrac{1}{7(1 + \log 7)}$

Answer: $\dfrac{1}{7(\log 7 + 1)}$

</details>

---

### Q26. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \cos x \cos 2x \cos 4x \cos 8x \cos 16x$, then $f'\left(\dfrac{\pi}{4}\right)$ is equal to

**Options:**

- **(A)** $1$
- **(B)** $0$
- **(C)** $\sqrt{2}$
- **(D)** $\dfrac{1}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{2}$**

**Detailed Solution:**

Using the standard trigonometric identity $\cos x \cos 2x \cos 4x \dots \cos 2^{n-1}x = \dfrac{\sin 2^n x}{2^n \sin x}$, we can simplify the given function for $n=5$:

$f(x) = \dfrac{\sin 32x}{32 \sin x}$

Differentiating $f(x)$ with respect to $x$ using the quotient rule:

$f'(x) = \dfrac{32 \cos 32x \cdot 32 \sin x - \sin 32x \cdot 32 \cos x}{(32 \sin x)^2}$

$f'(x) = \dfrac{32 \cos 32x \sin x - \sin 32x \cos x}{32 \sin^2 x}$

Substituting $x = \dfrac{\pi}{4}$:

$32x = 32 \left(\dfrac{\pi}{4}\right) = 8\pi$

We know that $\sin 8\pi = 0$, $\cos 8\pi = 1$, and $\sin\left(\dfrac{\pi}{4}\right) = \dfrac{1}{\sqrt{2}}$.

$f'\left(\dfrac{\pi}{4}\right) = \dfrac{32(1)\left(\dfrac{1}{\sqrt{2}}\right) - 0}{32 \left(\dfrac{1}{\sqrt{2}}\right)^2}$

$f'\left(\dfrac{\pi}{4}\right) = \dfrac{\dfrac{32}{\sqrt{2}}}{\dfrac{32}{2}} = \dfrac{2}{\sqrt{2}} = \sqrt{2}$

Answer: $\sqrt{2}$

</details>

---

### Q27. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of the function $f(x) = \cos^4 x + \sin^4 x,\ 0 \leq x \leq 2\pi$ is positive for

**Options:**

- **(A)** $0 < x < \dfrac{\pi}{8}$
- **(B)** $\dfrac{\pi}{4} < x < \dfrac{\pi}{2}$
- **(C)** $\dfrac{\pi}{2} < x < \dfrac{5\pi}{8}$
- **(D)** $\dfrac{5\pi}{8} < x < \dfrac{3\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\pi}{4} < x < \dfrac{\pi}{2}$**

**Detailed Solution:**

Given $f(x) = \cos^4 x + \sin^4 x$

Rewriting the function:

$f(x) = (\cos^2 x + \sin^2 x)^2 - 2\sin^2 x \cos^2 x$

$f(x) = 1 - \dfrac{1}{2}(2\sin x \cos x)^2 = 1 - \dfrac{1}{2}\sin^2(2x)$

Differentiating with respect to $x$:

$f'(x) = -\dfrac{1}{2} \times 2\sin(2x) \times \cos(2x) \times 2$

$f'(x) = -2\sin(2x)\cos(2x) = -\sin(4x)$

For the derivative to be positive, $f'(x) > 0$:

$-\sin(4x) > 0 \Rightarrow \sin(4x) < 0$

The sine function is negative when its argument lies in the intervals $(\pi, 2\pi), (3\pi, 4\pi), (5\pi, 6\pi), \dots$

Taking the first interval:

$\pi < 4x < 2\pi$

$\dfrac{\pi}{4} < x < \dfrac{\pi}{2}$

Answer: $\dfrac{\pi}{4} < x < \dfrac{\pi}{2}$

</details>

---

### Q28. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let f(x) be a twice differentiable function such that $f''(x) = -f(x)$, $f'(x) = g(x)$ and $h(x) = \{f(x)\}^2 + \{g(x)\}^2$. If $h(5) = 11$, then $h(10)$ is equal to ...

**Options:**

- **(A)** $11$
- **(B)** $22$
- **(C)** $0$
- **(D)** Not defined

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $11$**

**Detailed Solution:**

Given $h(x) = (f(x))^2 + (g(x))^2$

Differentiating with respect to $x$:

$h'(x) = 2f(x)f'(x) + 2g(x)g'(x)$

Given $f'(x) = g(x)$, differentiating gives $f''(x) = g'(x)$.

Also given $f''(x) = -f(x)$, so $g'(x) = -f(x)$.

Substituting these into $h'(x)$:

$h'(x) = 2f(x)g(x) + 2g(x)(-f(x)) = 0$

Since $h'(x) = 0$, $h(x)$ is a constant function.

Given $h(5) = 11$, it follows that $h(10) = 11$.

Answer: $11$

</details>

---

### Q29. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $\log_8(\log_5 x)$ w. r. t. $x$ is

**Options:**

- **(A)** $\dfrac{1}{\log_5 8\log x}$
- **(B)** $\dfrac{1}{x\log 5\log x}$
- **(C)** $\dfrac{1}{x\log x\log 8\log 5}$
- **(D)** $\dfrac{1}{x\log 8\log x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{x\log 8\log x}$**

**Detailed Solution:**

Let $y = \log_8(\log_5 x)$

Using the change of base formula, we can write:

$y = \dfrac{\log_e(\log_5 x)}{\log_e 8}$

Differentiating with respect to $x$ using the chain rule:

$\dfrac{dy}{dx} = \dfrac{1}{\log_e 8} \cdot \dfrac{1}{\log_5 x} \cdot \dfrac{d}{dx}(\log_5 x)$

$\dfrac{dy}{dx} = \dfrac{1}{\log_e 8} \cdot \dfrac{1}{\log_5 x} \cdot \dfrac{1}{x \log_e 5}$

Substitute $\log_5 x = \dfrac{\log_e x}{\log_e 5}$:

$\dfrac{dy}{dx} = \dfrac{1}{\log_e 8} \cdot \dfrac{\log_e 5}{\log_e x} \cdot \dfrac{1}{x \log_e 5}$

$\dfrac{dy}{dx} = \dfrac{1}{x \log_e 8 \log_e x}$

Assuming $\log$ represents the natural logarithm $\log_e$, we get:

$\dfrac{dy}{dx} = \dfrac{1}{x \log 8 \log x}$

Answer: $\dfrac{1}{x\log 8\log x}$

</details>

---

### Q30. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $\sin\left(\log\left(\dfrac{x+3}{x}\right)\right)$ is

**Options:**

- **(A)** $\dfrac{3}{x+3}\cos\left(\log\left(\dfrac{x+3}{x}\right)\right)$
- **(B)** $\dfrac{3}{x(x+3)}\cos\left(\log\left(\dfrac{x+3}{x}\right)\right)$
- **(C)** $\dfrac{-3}{x(x+3)}\cos\left(\log\left(\dfrac{x+3}{x}\right)\right)$
- **(D)** $\dfrac{-1}{x(x+3)}\cos\left(\log\left(\dfrac{x+3}{x}\right)\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{-3}{x(x+3)}\cos\left(\log\left(\dfrac{x+3}{x}\right)\right)$**

**Detailed Solution:**

Let $y = \sin\left(\log\left(\dfrac{x+3}{x}\right)\right)$

Using the chain rule, differentiating with respect to $x$ gives:

$\dfrac{dy}{dx} = \cos\left(\log\left(\dfrac{x+3}{x}\right)\right) \cdot \dfrac{d}{dx}\left(\log\left(\dfrac{x+3}{x}\right)\right)$

$\dfrac{dy}{dx} = \cos\left(\log\left(\dfrac{x+3}{x}\right)\right) \cdot \dfrac{d}{dx}(\log(x+3) - \log x)$

$\dfrac{dy}{dx} = \cos\left(\log\left(\dfrac{x+3}{x}\right)\right) \cdot \left(\dfrac{1}{x+3} - \dfrac{1}{x}\right)$

$\dfrac{dy}{dx} = \cos\left(\log\left(\dfrac{x+3}{x}\right)\right) \cdot \left(\dfrac{x - (x+3)}{x(x+3)}\right)$

$\dfrac{dy}{dx} = \dfrac{-3}{x(x+3)}\cos\left(\log\left(\dfrac{x+3}{x}\right)\right)$

</details>

---

### Q31. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y = \log x^x$, then the value of $\left(\dfrac{dy}{dx}\right)^2$ at $x = e^2$ is

**Options:**

- **(A)** $4$
- **(B)** $e$
- **(C)** $e^2$
- **(D)** $9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $9$**

**Detailed Solution:**

Given $y = \log x^x$

Using the property of logarithms, this can be written as:

$y = x \log x$

Differentiating both sides with respect to $x$ using the product rule:

$\dfrac{dy}{dx} = x \cdot \dfrac{1}{x} + \log x \cdot 1$

$\dfrac{dy}{dx} = 1 + \log x$

Substituting $x = e^2$ into the derivative:

$\dfrac{dy}{dx} = 1 + \log(e^2)$

$\dfrac{dy}{dx} = 1 + 2\log e$

Since $\log e = 1$, we get:

$\dfrac{dy}{dx} = 1 + 2 = 3$

Therefore, the value of $\left(\dfrac{dy}{dx}\right)^2$ is:

$\left(\dfrac{dy}{dx}\right)^2 = 3^2 = 9$

Answer: $9$

</details>

---

### Q32. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \sqrt{x^2+1}, g(x) = \dfrac{x+1}{x^2+1}, h(x) = 2x - 3$, then $f'\left(h'(g'(x))\right) =$

**Options:**

- **(A)** $0$
- **(B)** $\dfrac{1}{\sqrt{x^2+1}}$
- **(C)** $\dfrac{2}{\sqrt{5}}$
- **(D)** $\dfrac{x}{\sqrt{x^2+1}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{2}{\sqrt{5}}$**

**Detailed Solution:**

Given $f(x) = \sqrt{x^2+1}$, differentiating with respect to $x$ gives:

$f'(x) = \dfrac{1}{2\sqrt{x^2+1}} \cdot 2x = \dfrac{x}{\sqrt{x^2+1}}$

Given $h(x) = 2x - 3$, differentiating with respect to $x$ gives:

$h'(x) = 2$

Since $h'(x)$ is a constant function, its value is $2$ for any input. Therefore, for any $x$ where $g'(x)$ is defined:

$h'(g'(x)) = 2$

We need to find $f'(h'(g'(x)))$, which simplifies to $f'(2)$.

Substituting $x = 2$ into the expression for $f'(x)$:

$f'(2) = \dfrac{2}{\sqrt{2^2+1}} = \dfrac{2}{\sqrt{5}}$

</details>

---

### Q33. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x) = x - 5$.
If $g(x) = [f(4h(x) + 3)]^2$ and $h(1) = 4, h'(1) = -2$, then $g'(1) =$ .....

**Options:**

- **(A)** $-242$
- **(B)** $-224$
- **(C)** $-112$
- **(D)** $-640$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-224$**

**Detailed Solution:**

Given $f(x) = x - 5$ and $g(x) = [f(4h(x) + 3)]^2$.

Substituting the expression for $f(x)$ into $g(x)$:

$g(x) = [(4h(x) + 3) - 5]^2 = [4h(x) - 2]^2$

Differentiating both sides with respect to $x$ using the chain rule:

$g'(x) = 2[4h(x) - 2] \cdot \dfrac{d}{dx}[4h(x) - 2]$

$g'(x) = 2[4h(x) - 2] \cdot 4h'(x) = 8[4h(x) - 2]h'(x)$

Substitute $x = 1$ into the derivative:

$g'(1) = 8[4h(1) - 2]h'(1)$

Given $h(1) = 4$ and $h'(1) = -2$, we get:

$g'(1) = 8[4(4) - 2](-2)$

$g'(1) = 8[16 - 2](-2)$

$g'(1) = 8[14](-2) = -224$

Answer: $-224$

</details>

---

### Q34. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = f\left(\dfrac{3 + 2x}{3 - 2x}\right)$, where $f(x) = \tan(\log x)$ and $\dfrac{dy}{dx} = \left(\dfrac{A}{B + C x^2}\right) \cdot \sec^2\left(\log\left(\dfrac{3 + 2x}{3 - 2x}\right)\right)$, then the respective values of A, B and C are ......

**Options:**

- **(A)** $3, 2, -4$
- **(B)** $12, -9, 4$
- **(C)** $6, 6, -2$
- **(D)** $12, 9, -4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $12, 9, -4$**

**Detailed Solution:**

Given $y = f\left(\dfrac{3 + 2x}{3 - 2x}\right)$ and $f(x) = \tan(\log x)$

$y = \tan\left(\log\left(\dfrac{3 + 2x}{3 - 2x}\right)\right)$

Differentiating with respect to $x$ using the chain rule:

$\dfrac{dy}{dx} = \sec^2\left(\log\left(\dfrac{3 + 2x}{3 - 2x}\right)\right) \cdot \dfrac{d}{dx}\left(\log\left(\dfrac{3 + 2x}{3 - 2x}\right)\right)$

$\dfrac{dy}{dx} = \sec^2\left(\log\left(\dfrac{3 + 2x}{3 - 2x}\right)\right) \cdot \dfrac{3 - 2x}{3 + 2x} \cdot \dfrac{d}{dx}\left(\dfrac{3 + 2x}{3 - 2x}\right)$

$\dfrac{dy}{dx} = \sec^2\left(\log\left(\dfrac{3 + 2x}{3 - 2x}\right)\right) \cdot \dfrac{3 - 2x}{3 + 2x} \cdot \left(\dfrac{2(3 - 2x) - (-2)(3 + 2x)}{(3 - 2x)^2}\right)$

$\dfrac{dy}{dx} = \sec^2\left(\log\left(\dfrac{3 + 2x}{3 - 2x}\right)\right) \cdot \dfrac{3 - 2x}{3 + 2x} \cdot \dfrac{12}{(3 - 2x)^2}$

$\dfrac{dy}{dx} = \dfrac{12}{(3 + 2x)(3 - 2x)} \cdot \sec^2\left(\log\left(\dfrac{3 + 2x}{3 - 2x}\right)\right)$

$\dfrac{dy}{dx} = \dfrac{12}{9 - 4x^2} \cdot \sec^2\left(\log\left(\dfrac{3 + 2x}{3 - 2x}\right)\right)$

Comparing with the given expression $\dfrac{dy}{dx} = \left(\dfrac{A}{B + C x^2}\right) \cdot \sec^2\left(\log\left(\dfrac{3 + 2x}{3 - 2x}\right)\right)$

We get $A = 12$, $B = 9$, $C = -4$.

Answer: $12, 9, -4$

</details>

---

### Q35. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \sqrt{x + \sqrt{x^2 + 1}}$, then the value of $\dfrac{dy}{dx}$ is

**Options:**

- **(A)** $\dfrac{\sqrt{x^2 + 1} + x}{2y\sqrt{x^2 + 1}}$
- **(B)** $\dfrac{\sqrt{x^2 + 1} + x}{y\sqrt{x^2 + 1}}$
- **(C)** $\dfrac{\sqrt{x^2 + 1} - x}{2y\sqrt{x^2 + 1}}$
- **(D)** $\dfrac{\sqrt{x^2 + 1} + x}{2y\sqrt{x^2 - 1}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\sqrt{x^2 + 1} + x}{2y\sqrt{x^2 + 1}}$**

**Detailed Solution:**

Given $y = \sqrt{x + \sqrt{x^2 + 1}}$

Squaring both sides:

$y^2 = x + \sqrt{x^2 + 1}$

Differentiating both sides with respect to $x$:

$2y \dfrac{dy}{dx} = 1 + \dfrac{1}{2\sqrt{x^2 + 1}} \cdot 2x$

$2y \dfrac{dy}{dx} = 1 + \dfrac{x}{\sqrt{x^2 + 1}}$

$2y \dfrac{dy}{dx} = \dfrac{\sqrt{x^2 + 1} + x}{\sqrt{x^2 + 1}}$

$\dfrac{dy}{dx} = \dfrac{\sqrt{x^2 + 1} + x}{2y\sqrt{x^2 + 1}}$

Answer: $\dfrac{\sqrt{x^2 + 1} + x}{2y\sqrt{x^2 + 1}}$

</details>

---

### Q36. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y = \sin(e^{\log 2x})$, then the value of $\dfrac{dy}{dx}$ at $x = \dfrac{\pi}{2}$ is

**Options:**

- **(A)** $2$
- **(B)** $-2$
- **(C)** $1$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-2$**

**Detailed Solution:**

Given $y = \sin(e^{\log 2x})$

Using the property $e^{\log a} = a$, we get $e^{\log 2x} = 2x$

Therefore, $y = \sin(2x)$

Differentiating with respect to $x$, we get:

$\dfrac{dy}{dx} = 2\cos(2x)$

Substituting $x = \dfrac{\pi}{2}$:

$\dfrac{dy}{dx} = 2\cos\left(2 \times \dfrac{\pi}{2}\right) = 2\cos(\pi)$

Since $\cos(\pi) = -1$, we have:

$\dfrac{dy}{dx} = 2(-1) = -2$

Answer: $-2$

</details>

---

### Q37. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{u}=\log (\sqrt{x+1}-\sqrt{x-1})$ and $\mathrm{v}=\sqrt{x+1}+\sqrt{x-1}$ then $\frac{\mathrm{du}}{\mathrm{dv}}=\ldots$.

**Options:**

- **(A)** u
- **(B)** v
- **(C)** $\frac{-1}{\mathrm{u}}$
- **(D)** $\frac{-1}{\mathrm{v}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{-1}{\mathrm{v}}$**

**Detailed Solution:**

Given $u = \log (\sqrt{x+1}-\sqrt{x-1})$ and $v = \sqrt{x+1}+\sqrt{x-1}$.

$(\sqrt{x+1}-\sqrt{x-1})(\sqrt{x+1}+\sqrt{x-1}) = (x+1) - (x-1) = 2$

$\sqrt{x+1}-\sqrt{x-1} = \dfrac{2}{\sqrt{x+1}+\sqrt{x-1}} = \dfrac{2}{v}$

Substituting this into the expression for $u$:

$u = \log \left(\dfrac{2}{v}\right) = \log 2 - \log v$

Differentiating $u$ with respect to $v$:

$\dfrac{du}{dv} = \dfrac{d}{dv}(\log 2 - \log v) = -\dfrac{1}{v}$

Answer: $\frac{-1}{\mathrm{v}}$

</details>

---

### Q38. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\frac{\sin ^2 x}{1+\cot x}+\frac{\cos ^2 x}{1+\tan x}$, then the value of $\mathrm{f}^{\prime}\left(\frac{\pi}{6}\right)$ is equal to

**Options:**

- **(A)** 0
- **(B)** $\frac{1}{2}$
- **(C)** $-\frac{1}{2}$
- **(D)** $\frac{\sqrt{3}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\frac{1}{2}$**

**Detailed Solution:**

$f(x) = \dfrac{\sin^2 x}{1 + \cot x} + \dfrac{\cos^2 x}{1 + \tan x}$

$f(x) = \dfrac{\sin^2 x}{1 + \dfrac{\cos x}{\sin x}} + \dfrac{\cos^2 x}{1 + \dfrac{\sin x}{\cos x}}$

$f(x) = \dfrac{\sin^3 x}{\sin x + \cos x} + \dfrac{\cos^3 x}{\cos x + \sin x}$

$f(x) = \dfrac{\sin^3 x + \cos^3 x}{\sin x + \cos x}$

Using the identity $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$:

$f(x) = \dfrac{(\sin x + \cos x)(\sin^2 x - \sin x \cos x + \cos^2 x)}{\sin x + \cos x}$

$f(x) = \sin^2 x - \sin x \cos x + \cos^2 x$

$f(x) = 1 - \sin x \cos x$

$f(x) = 1 - \dfrac{1}{2} \sin 2x$

Differentiating with respect to $x$:

$f'(x) = -\dfrac{1}{2} \times 2 \cos 2x = -\cos 2x$

Substituting $x = \dfrac{\pi}{6}$:

$f'\left(\dfrac{\pi}{6}\right) = -\cos\left(2 \times \dfrac{\pi}{6}\right) = -\cos\left(\dfrac{\pi}{3}\right) = -\dfrac{1}{2}$

Answer: $-\frac{1}{2}$

</details>

---

### Q39. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\sqrt{1+\cos ^2\left(x^2\right)}$, then $\mathrm{f}^{\prime}\left(\frac{\sqrt{\pi}}{2}\right)$ is

**Options:**

- **(A)** $\frac{\sqrt{\pi}}{6}$
- **(B)** $-\sqrt{\frac{\pi}{6}}$
- **(C)** $\frac{\pi}{\sqrt{6}}$
- **(D)** $\sqrt{\frac{\pi}{6}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\sqrt{\frac{\pi}{6}}$**

**Detailed Solution:**

Given $f(x) = \sqrt{1+\cos^2(x^2)}$

Differentiating with respect to $x$ using the chain rule:

$f'(x) = \dfrac{1}{2\sqrt{1+\cos^2(x^2)}} \cdot \dfrac{d}{dx}(1+\cos^2(x^2))$

$f'(x) = \dfrac{1}{2\sqrt{1+\cos^2(x^2)}} \cdot 2\cos(x^2)(-\sin(x^2)) \cdot 2x$

$f'(x) = \dfrac{-2x\sin(x^2)\cos(x^2)}{\sqrt{1+\cos^2(x^2)}}$

Substitute $x = \dfrac{\sqrt{\pi}}{2}$, which gives $x^2 = \dfrac{\pi}{4}$:

$f'\left(\dfrac{\sqrt{\pi}}{2}\right) = \dfrac{-2\left(\dfrac{\sqrt{\pi}}{2}\right)\sin\left(\dfrac{\pi}{4}\right)\cos\left(\dfrac{\pi}{4}\right)}{\sqrt{1+\cos^2\left(\dfrac{\pi}{4}\right)}}$

$f'\left(\dfrac{\sqrt{\pi}}{2}\right) = \dfrac{-\sqrt{\pi} \cdot \dfrac{1}{\sqrt{2}} \cdot \dfrac{1}{\sqrt{2}}}{\sqrt{1+\left(\dfrac{1}{\sqrt{2}}\right)^2}}$

$f'\left(\dfrac{\sqrt{\pi}}{2}\right) = \dfrac{-\dfrac{\sqrt{\pi}}{2}}{\sqrt{1+\dfrac{1}{2}}} = \dfrac{-\dfrac{\sqrt{\pi}}{2}}{\sqrt{\dfrac{3}{2}}}$

$f'\left(\dfrac{\sqrt{\pi}}{2}\right) = -\dfrac{\sqrt{\pi}}{2} \cdot \dfrac{\sqrt{2}}{\sqrt{3}} = -\dfrac{\sqrt{\pi}}{\sqrt{2}\sqrt{3}} = -\sqrt{\dfrac{\pi}{6}}$

Answer: $-\sqrt{\frac{\pi}{6}}$

</details>

---

### Q40. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{y}=\log _3\left(\log _3 x\right)$ then $\frac{\mathrm{dy}}{\mathrm{d} x}$ at $x=3$ is $\ldots \ldots$

**Options:**

- **(A)** $\frac{1}{3}(\log 3)^{-3}$
- **(B)** $\frac{1}{3}(\log 3)$
- **(C)** $\frac{1}{3} \frac{1}{(\log 3)^{-3}}$
- **(D)** $\frac{1}{3}(\log 3)^{-2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{3}(\log 3)^{-2}$**

**Detailed Solution:**

Given $y = \log_3(\log_3 x)$

Differentiating with respect to $x$ using the chain rule:

$\dfrac{dy}{dx} = \dfrac{1}{\log_3 x \cdot \log 3} \cdot \dfrac{d}{dx}(\log_3 x)$

$\dfrac{dy}{dx} = \dfrac{1}{\log_3 x \cdot \log 3} \cdot \dfrac{1}{x \log 3}$

$\dfrac{dy}{dx} = \dfrac{1}{x \log_3 x (\log 3)^2}$

Substitute $x = 3$ into the derivative:

$\left. \dfrac{dy}{dx} \right|_{x=3} = \dfrac{1}{3 \cdot \log_3 3 \cdot (\log 3)^2}$

Since $\log_3 3 = 1$:

$\left. \dfrac{dy}{dx} \right|_{x=3} = \dfrac{1}{3 \cdot 1 \cdot (\log 3)^2} = \dfrac{1}{3}(\log 3)^{-2}$

Answer: $\frac{1}{3}(\log 3)^{-2}$

</details>

---

### Q41. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x=\mathrm{e}^{\tan ^{-1}\left(\frac{\mathrm{y}-x^2}{x^2}\right)}$, then $\left(\frac{\mathrm{dy}}{\mathrm{d} x}\right)$ at $x=1$ is

**Options:**

- **(A)** 1
- **(B)** 0
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

Given $x = \mathrm{e}^{\tan^{-1}\left(\dfrac{y-x^2}{x^2}\right)}$

Taking the natural logarithm on both sides, we get:

$\ln x = \tan^{-1}\left(\dfrac{y-x^2}{x^2}\right)$

$\tan(\ln x) = \dfrac{y-x^2}{x^2}$

$\tan(\ln x) = \dfrac{y}{x^2} - 1$

$y = x^2(1 + \tan(\ln x))$

Differentiating both sides with respect to $x$ using the product rule:

$\dfrac{\mathrm{dy}}{\mathrm{d}x} = \dfrac{\mathrm{d}}{\mathrm{d}x}[x^2] \cdot (1 + \tan(\ln x)) + x^2 \cdot \dfrac{\mathrm{d}}{\mathrm{d}x}[1 + \tan(\ln x)]$

$\dfrac{\mathrm{dy}}{\mathrm{d}x} = 2x(1 + \tan(\ln x)) + x^2 \left( \sec^2(\ln x) \cdot \dfrac{1}{x} \right)$

$\dfrac{\mathrm{dy}}{\mathrm{d}x} = 2x(1 + \tan(\ln x)) + x \sec^2(\ln x)$

Substituting $x = 1$:

$\left(\dfrac{\mathrm{dy}}{\mathrm{d}x}\right)_{x=1} = 2(1)(1 + \tan(\ln 1)) + 1 \cdot \sec^2(\ln 1)$

Since $\ln 1 = 0$, $\tan(0) = 0$, and $\sec(0) = 1$, we get:

$\left(\dfrac{\mathrm{dy}}{\mathrm{d}x}\right)_{x=1} = 2(1 + 0) + 1(1)^2$

$\left(\dfrac{\mathrm{dy}}{\mathrm{d}x}\right)_{x=1} = 2 + 1 = 3$

Answer: 3

</details>

---

### Q42. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{y}=\tan ^{-1}\left[\frac{4 \sin 2 x}{\cos 2 x-6 \sin ^2 x}\right]$, then $\frac{\mathrm{dy}}{\mathrm{d} x}$ at $x=0$ is

**Options:**

- **(A)** $\frac{1}{8}$
- **(B)** $-8$
- **(C)** $8$
- **(D)** $-\frac{1}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $8$**

**Detailed Solution:**

Given $y = \tan^{-1}\left[\dfrac{4 \sin 2x}{\cos 2x - 6 \sin^2 x}\right]$

Let $u = \dfrac{4 \sin 2x}{\cos 2x - 6 \sin^2 x}$. Then $y = \tan^{-1}(u)$.

Differentiating with respect to $x$ using the chain rule:

$\dfrac{dy}{dx} = \dfrac{1}{1+u^2} \cdot \dfrac{du}{dx}$

At $x = 0$, we have $\sin 0 = 0$ and $\cos 0 = 1$.

Substituting these values into $u$:

$u(0) = \dfrac{4(0)}{1 - 6(0)} = 0$

So, at $x = 0$, $\dfrac{dy}{dx} = \dfrac{1}{1+0^2} \cdot \dfrac{du}{dx} = \dfrac{du}{dx}$.

Now, we find $\dfrac{du}{dx}$ using the quotient rule:

$\dfrac{du}{dx} = \dfrac{(\cos 2x - 6 \sin^2 x)(8 \cos 2x) - (4 \sin 2x)(-2 \sin 2x - 12 \sin x \cos x)}{(\cos 2x - 6 \sin^2 x)^2}$

Evaluating this derivative at $x = 0$:

$\dfrac{du}{dx}\Bigg|_{x=0} = \dfrac{(1 - 0)(8) - (0)(0)}{(1 - 0)^2} = \dfrac{8}{1} = 8$

Therefore, $\dfrac{dy}{dx}$ at $x = 0$ is $8$.

Answer: $8$

</details>

---

### Q43. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(1)=3, \mathrm{f}^{\prime}(1)=2$, then $\frac{\mathrm{d}}{\mathrm{d} x}\left\{\log \left[\mathrm{f}\left(\mathrm{e}^x+2 x\right)\right]\right\}$ at $x=0$ is

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{3}{2}$
- **(C)** $2$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2$**

**Detailed Solution:**

Let $y = \log \left[\mathrm{f}\left(\mathrm{e}^x+2 x\right)\right]$

Differentiating with respect to $x$ using the chain rule:

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{1}{\mathrm{f}\left(\mathrm{e}^x+2 x\right)} \cdot \mathrm{f}^{\prime}\left(\mathrm{e}^x+2 x\right) \cdot \dfrac{\mathrm{d}}{\mathrm{d}x}\left(\mathrm{e}^x+2 x\right)$

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{1}{\mathrm{f}\left(\mathrm{e}^x+2 x\right)} \cdot \mathrm{f}^{\prime}\left(\mathrm{e}^x+2 x\right) \cdot \left(\mathrm{e}^x+2\right)$

Substituting $x=0$:

$\left. \dfrac{\mathrm{d}y}{\mathrm{d}x} \right|_{x=0} = \dfrac{1}{\mathrm{f}\left(\mathrm{e}^0+0\right)} \cdot \mathrm{f}^{\prime}\left(\mathrm{e}^0+0\right) \cdot \left(\mathrm{e}^0+2\right)$

$\left. \dfrac{\mathrm{d}y}{\mathrm{d}x} \right|_{x=0} = \dfrac{1}{\mathrm{f}(1)} \cdot \mathrm{f}^{\prime}(1) \cdot (1+2)$

Given $\mathrm{f}(1)=3$ and $\mathrm{f}^{\prime}(1)=2$:

$\left. \dfrac{\mathrm{d}y}{\mathrm{d}x} \right|_{x=0} = \dfrac{1}{3} \cdot 2 \cdot 3 = 2$

Answer: $2$

</details>

---

### Q44. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{u}=\frac{\tan ^{-1} x}{\tan ^{-1} x+1}$ and $\mathrm{v}=\tan ^{-1}\left(\tan ^{-1} x\right)$ then $\frac{\mathrm{du}}{\mathrm{dv}}=\ldots \ldots$

**Options:**

- **(A)** 1
- **(B)** $\frac{1+\left(\tan ^{-1} x\right)^2}{\left(1+\tan ^{-1} x\right)^2}$
- **(C)** $\frac{\tan ^{-1} x}{\left(1+\tan ^{-1} x\right)^2}$
- **(D)** $\frac{1}{\left(1+\tan ^{-1} x\right)^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1+\left(\tan ^{-1} x\right)^2}{\left(1+\tan ^{-1} x\right)^2}$**

**Detailed Solution:**

Let $t = \tan^{-1} x$.

Then $u = \dfrac{t}{t+1}$ and $v = \tan^{-1} t$.

Differentiating $u$ with respect to $t$:

$\dfrac{du}{dt} = \dfrac{(t+1)(1) - t(1)}{(t+1)^2} = \dfrac{1}{(t+1)^2}$

Differentiating $v$ with respect to $t$:

$\dfrac{dv}{dt} = \dfrac{1}{1+t^2}$

Now, $\dfrac{du}{dv} = \dfrac{\dfrac{du}{dt}}{\dfrac{dv}{dt}}$

$\dfrac{du}{dv} = \dfrac{\dfrac{1}{(t+1)^2}}{\dfrac{1}{1+t^2}} = \dfrac{1+t^2}{(1+t)^2}$

Substituting $t = \tan^{-1} x$:

$\dfrac{du}{dv} = \dfrac{1+(\tan^{-1} x)^2}{(1+\tan^{-1} x)^2}$

Answer: $\frac{1+\left(\tan ^{-1} x\right)^2}{\left(1+\tan ^{-1} x\right)^2}$

</details>

---

### Q45. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $a\left(4+x^2\right)=x$ and $\mathrm{y}-x^3=a^2$ then $\frac{\mathrm{dy}}{\mathrm{d} x}$ at $x=1$ is ...

**Options:**

- **(A)** $\frac{441}{125}$
- **(B)** $\frac{18}{125}$
- **(C)** $\frac{378}{125}$
- **(D)** $\frac{381}{125}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{381}{125}$**

**Detailed Solution:**

Given $a(4+x^2) = x$, we can write $a = \dfrac{x}{4+x^2}$.

Also given $y - x^3 = a^2$, which gives $y = x^3 + a^2$.

Differentiating $y$ with respect to $x$, we get:

$\dfrac{\mathrm{dy}}{\mathrm{d} x} = 3x^2 + 2a \dfrac{\mathrm{da}}{\mathrm{d} x}$

Now, differentiating $a = \dfrac{x}{4+x^2}$ with respect to $x$ using the quotient rule:

$\dfrac{\mathrm{da}}{\mathrm{d} x} = \dfrac{(4+x^2)(1) - x(2x)}{(4+x^2)^2} = \dfrac{4 - x^2}{(4+x^2)^2}$

At $x = 1$, the value of $a$ is:

$a = \dfrac{1}{4+1^2} = \dfrac{1}{5}$

At $x = 1$, the value of $\dfrac{\mathrm{da}}{\mathrm{d} x}$ is:

$\dfrac{\mathrm{da}}{\mathrm{d} x} = \dfrac{4 - 1^2}{(4+1^2)^2} = \dfrac{3}{25}$

Substituting these values into the expression for $\dfrac{\mathrm{dy}}{\mathrm{d} x}$ at $x = 1$:

$\dfrac{\mathrm{dy}}{\mathrm{d} x} = 3(1)^2 + 2\left(\dfrac{1}{5}\right)\left(\dfrac{3}{25}\right)$

$\dfrac{\mathrm{dy}}{\mathrm{d} x} = 3 + \dfrac{6}{125}$

$\dfrac{\mathrm{dy}}{\mathrm{d} x} = \dfrac{375 + 6}{125} = \dfrac{381}{125}$

Answer: $\frac{381}{125}$

</details>

---

### Q46. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{y}=\log _{\mathrm{e}} x^3+3 \sin ^{-1} x+\mathrm{k} x^2$ and $\mathrm{y}^{\prime}\left(\frac{1}{2}\right)=2 \sqrt{3}$, then $\mathrm{k}=$

**Options:**

- **(A)** $6$
- **(B)** $-6$
- **(C)** $2 \sqrt{3}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-6$**

**Detailed Solution:**

Given $y = \log_e x^3 + 3 \sin^{-1} x + k x^2$

$y = 3 \log_e x + 3 \sin^{-1} x + k x^2$

Differentiating with respect to $x$:

$y' = \dfrac{3}{x} + \dfrac{3}{\sqrt{1 - x^2}} + 2kx$

Substituting $x = \dfrac{1}{2}$:

$y'\left(\dfrac{1}{2}\right) = \dfrac{3}{1/2} + \dfrac{3}{\sqrt{1 - (1/2)^2}} + 2k\left(\dfrac{1}{2}\right)$

$y'\left(\dfrac{1}{2}\right) = 6 + \dfrac{3}{\sqrt{3/4}} + k$

$y'\left(\dfrac{1}{2}\right) = 6 + \dfrac{6}{\sqrt{3}} + k$

$y'\left(\dfrac{1}{2}\right) = 6 + 2\sqrt{3} + k$

Given $y'\left(\dfrac{1}{2}\right) = 2\sqrt{3}$:

$6 + 2\sqrt{3} + k = 2\sqrt{3}$

$k = -6$

Answer: $-6$

</details>

---

### Q47. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(1)=1, f^{\prime}(1)=3$, then the derivative of $f(f(f(x)))+(f(x))^2$ at $x=1$ is

**Options:**

- **(A)** $9$
- **(B)** $12$
- **(C)** $15$
- **(D)** $33$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $33$**

**Detailed Solution:**

Let $y = f(f(f(x))) + (f(x))^2$

Differentiating with respect to $x$ using the chain rule:

$\dfrac{dy}{dx} = f'(f(f(x))) \cdot f'(f(x)) \cdot f'(x) + 2f(x)f'(x)$

Substituting $x = 1$:

$\left. \dfrac{dy}{dx} \right|_{x=1} = f'(f(f(1))) \cdot f'(f(1)) \cdot f'(1) + 2f(1)f'(1)$

Given $f(1) = 1$ and $f'(1) = 3$:

$\left. \dfrac{dy}{dx} \right|_{x=1} = f'(f(1)) \cdot f'(1) \cdot f'(1) + 2(1)(3)$

$\left. \dfrac{dy}{dx} \right|_{x=1} = f'(1) \cdot f'(1) \cdot f'(1) + 6$

$\left. \dfrac{dy}{dx} \right|_{x=1} = 3 \cdot 3 \cdot 3 + 6$

$\left. \dfrac{dy}{dx} \right|_{x=1} = 27 + 6 = 33$

Answer: $33$

</details>

---

### Q48. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The first derivative of the function $\left(\cos ^{-1}\left(\sin \sqrt{\frac{1+x}{2}}\right)+x^x\right)$ with respect to $x$ at $x=1$ is

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{5}{4}$
- **(C)** $\frac{-1}{2}$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{3}{4}$**

**Detailed Solution:**

Let $y = u + v$, where $u = \cos^{-1}\left(\sin \sqrt{\dfrac{1+x}{2}}\right)$ and $v = x^x$.

We can simplify $u$ using the identity $\sin \theta = \cos\left(\dfrac{\pi}{2} - \theta\right)$:

$u = \cos^{-1}\left(\cos\left(\dfrac{\pi}{2} - \sqrt{\dfrac{1+x}{2}}\right)\right) = \dfrac{\pi}{2} - \sqrt{\dfrac{1+x}{2}}$

Differentiating $u$ with respect to $x$:

$\dfrac{du}{dx} = 0 - \dfrac{1}{2\sqrt{\dfrac{1+x}{2}}} \times \dfrac{d}{dx}\left(\dfrac{1+x}{2}\right)$

$\dfrac{du}{dx} = -\dfrac{1}{2\sqrt{\dfrac{1+x}{2}}} \times \dfrac{1}{2} = -\dfrac{1}{4\sqrt{\dfrac{1+x}{2}}}$

At $x = 1$:

$\dfrac{du}{dx} = -\dfrac{1}{4\sqrt{\dfrac{1+1}{2}}} = -\dfrac{1}{4}$

Now for $v = x^x$, taking the natural logarithm on both sides:

$\ln v = x \ln x$

Differentiating with respect to $x$:

$\dfrac{1}{v} \dfrac{dv}{dx} = x \times \dfrac{1}{x} + \ln x \times 1 = 1 + \ln x$

$\dfrac{dv}{dx} = x^x(1 + \ln x)$

At $x = 1$:

$\dfrac{dv}{dx} = 1^1(1 + \ln 1) = 1(1 + 0) = 1$

The first derivative of the given function is $\dfrac{dy}{dx} = \dfrac{du}{dx} + \dfrac{dv}{dx}$.

At $x = 1$:

$\dfrac{dy}{dx} = -\dfrac{1}{4} + 1 = \dfrac{3}{4}$

Answer: $\frac{3}{4}$

</details>

---

### Q49. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/WOVgPSnmh0JzBr0SmYHsJNCB4F2ddYP_nAfEVGq06GY.original.fullsize.png">

**Options:**

- **(A)** $(n-1)!$
- **(B)** $\mathrm{n}!$
- **(C)** $(-1)(n-1)!$
- **(D)** $(-n)(n-1)!$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(-1)(n-1)!$**

**Detailed Solution:**

Given $y = (1 - x)(2 - x)(3 - x) \dots (n - x)$.

Let $P(x) = (2 - x)(3 - x) \dots (n - x)$.

Then, $y = (1 - x)P(x)$.

Differentiating both sides with respect to $x$ using the product rule, we get:

$\dfrac{dy}{dx} = \dfrac{d}{dx}(1 - x) \cdot P(x) + (1 - x) \cdot \dfrac{d}{dx}P(x)$

$\dfrac{dy}{dx} = -1 \cdot P(x) + (1 - x)P'(x)$

To find the derivative at $x = 1$, substitute $x = 1$ into the equation:

$\left. \dfrac{dy}{dx} \right|_{x=1} = -1 \cdot P(1) + (1 - 1)P'(1)$

$\left. \dfrac{dy}{dx} \right|_{x=1} = -P(1) + 0$

Now, calculate $P(1)$ by substituting $x = 1$ into $P(x)$:

$P(1) = (2 - 1)(3 - 1)(4 - 1) \dots (n - 1)$

$P(1) = 1 \cdot 2 \cdot 3 \dots (n - 1)$

$P(1) = (n - 1)!$

Therefore, the derivative at $x = 1$ is:

$\left. \dfrac{dy}{dx} \right|_{x=1} = -1 \cdot (n - 1)! = (-1)(n - 1)!$

Answer: $(-1)(n-1)!$

</details>

---

### Q50. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{g}(x)=[\mathrm{f}(2 \mathrm{f}(x)+2)]^2$ and $\mathrm{f}(0)=-1, \mathrm{f}^{\prime}(0)=1$, then $g^{\prime}(0)$ is

**Options:**

- **(A)** -4
- **(B)** 4
- **(C)** -3
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -4**

**Detailed Solution:**

Given $\mathrm{g}(x)=[\mathrm{f}(2 \mathrm{f}(x)+2)]^2$

Differentiating both sides with respect to $x$ using the chain rule:

$\mathrm{g}^{\prime}(x) = 2[\mathrm{f}(2 \mathrm{f}(x)+2)] \cdot \dfrac{d}{dx}[\mathrm{f}(2 \mathrm{f}(x)+2)]$

$\mathrm{g}^{\prime}(x) = 2[\mathrm{f}(2 \mathrm{f}(x)+2)] \cdot \mathrm{f}^{\prime}(2 \mathrm{f}(x)+2) \cdot \dfrac{d}{dx}[2 \mathrm{f}(x)+2]$

$\mathrm{g}^{\prime}(x) = 2[\mathrm{f}(2 \mathrm{f}(x)+2)] \cdot \mathrm{f}^{\prime}(2 \mathrm{f}(x)+2) \cdot 2\mathrm{f}^{\prime}(x)$

$\mathrm{g}^{\prime}(x) = 4 \cdot \mathrm{f}(2 \mathrm{f}(x)+2) \cdot \mathrm{f}^{\prime}(2 \mathrm{f}(x)+2) \cdot \mathrm{f}^{\prime}(x)$

Substitute $x = 0$ into the derivative:

$\mathrm{g}^{\prime}(0) = 4 \cdot \mathrm{f}(2 \mathrm{f}(0)+2) \cdot \mathrm{f}^{\prime}(2 \mathrm{f}(0)+2) \cdot \mathrm{f}^{\prime}(0)$

Using the given values $\mathrm{f}(0) = -1$ and $\mathrm{f}^{\prime}(0) = 1$, we first evaluate the inner term:

$2 \mathrm{f}(0) + 2 = 2(-1) + 2 = 0$

Substituting this back into the expression for $\mathrm{g}^{\prime}(0)$:

$\mathrm{g}^{\prime}(0) = 4 \cdot \mathrm{f}(0) \cdot \mathrm{f}^{\prime}(0) \cdot \mathrm{f}^{\prime}(0)$

$\mathrm{g}^{\prime}(0) = 4 \cdot (-1) \cdot (1) \cdot (1)$

$\mathrm{g}^{\prime}(0) = -4$

Answer: -4

</details>

---

### Q51. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

After $t$ seconds, the acceleration of a particle, which starts from rest and moves in a straight line is $\left(8-\frac{\mathrm{t}}{5}\right) \mathrm{cm} / \mathrm{s}^2$, then velocity of the particle at the instant, when the acceleration is zero, is

**Options:**

- **(A)** $160 \mathrm{~cm} / \mathrm{s}$
- **(B)** $80 \mathrm{~cm} / \mathrm{s}$
- **(C)** $320 \mathrm{~cm} / \mathrm{s}$
- **(D)** $480 \mathrm{~cm} / \mathrm{s}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $160 \mathrm{~cm} / \mathrm{s}$**

**Detailed Solution:**

Given acceleration $a = 8 - \dfrac{t}{5}$

When acceleration is zero, $8 - \dfrac{t}{5} = 0 \Rightarrow t = 40 \text{ s}$

We know that $a = \dfrac{dv}{dt}$

$\dfrac{dv}{dt} = 8 - \dfrac{t}{5}$

$dv = \left(8 - \dfrac{t}{5}\right) dt$

Integrating both sides, we get:

$v = 8t - \dfrac{t^2}{10} + C$

Since the particle starts from rest, at $t = 0$, $v = 0$, which gives $C = 0$.

$v = 8t - \dfrac{t^2}{10}$

Substituting $t = 40 \text{ s}$:

$v = 8(40) - \dfrac{(40)^2}{10}$

$v = 320 - \dfrac{1600}{10}$

$v = 320 - 160 = 160 \text{ cm/s}$

Answer: $160 \mathrm{~cm} / \mathrm{s}$

</details>

---

### Q52. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The equation of motion of a particle is $s=a t^2+b t+c$. If the displacement after 1 second is 20 m , velocity after 2 seconds is $30 \mathrm{~m} / \mathrm{sec}$ and the acceleration is $10 \mathrm{~m} / \mathrm{sec}^2$, then

**Options:**

- **(A)** $a+c=2 b$
- **(B)** $a+c=b$
- **(C)** $\quad \mathrm{a}-\mathrm{c}=\mathrm{b}$
- **(D)** $a+c=3 b$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $a+c=b$**

**Detailed Solution:**

Given the equation of motion: $s = a t^2 + b t + c$

Velocity is the first derivative of displacement with respect to time:
$v = \dfrac{ds}{dt} = 2at + b$

Acceleration is the second derivative of displacement with respect to time:
$\text{Acceleration} = \dfrac{dv}{dt} = 2a$

Given that the acceleration is $10 \text{ m/s}^2$:
$2a = 10 \Rightarrow a = 5$

Given that the velocity after $2$ seconds is $30 \text{ m/s}$:
$v(2) = 2a(2) + b = 30$
$4a + b = 30$
Substituting $a = 5$:
$4(5) + b = 30 \Rightarrow 20 + b = 30 \Rightarrow b = 10$

Given that the displacement after $1$ second is $20 \text{ m}$:
$s(1) = a(1)^2 + b(1) + c = 20$
$a + b + c = 20$
Substituting $a = 5$ and $b = 10$:
$5 + 10 + c = 20 \Rightarrow 15 + c = 20 \Rightarrow c = 5$

Now we have $a = 5$, $b = 10$, and $c = 5$.

Checking the given options, we find:
$a + c = 5 + 5 = 10$
Since $b = 10$, we get $a + c = b$.

Answer: $a+c=b$

</details>

---

### Q53. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $k$, if the slope of one of the lines given by $4 x^2+\mathrm{k} x y+y^2=0$ is four times that of the other, is given by

**Options:**

- **(A)** 4
- **(B)** 2.5
- **(C)** 5
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 5**

**Detailed Solution:**

Comparing the given equation $4x^2 + kxy + y^2 = 0$ with the standard form $ax^2 + 2hxy + by^2 = 0$, we get:
$a = 4$, $2h = k$, and $b = 1$

Let $m_1$ and $m_2$ be the slopes of the lines represented by the equation. We know that:
$m_1 + m_2 = -\dfrac{2h}{b} = -k$
$m_1 m_2 = \dfrac{a}{b} = 4$

It is given that the slope of one line is four times that of the other, so let $m_2 = 4m_1$.

Substituting $m_2$ into the sum of the slopes:
$m_1 + 4m_1 = -k$
$5m_1 = -k \Rightarrow m_1 = -\dfrac{k}{5}$

Substituting $m_2$ into the product of the slopes:
$m_1(4m_1) = 4$
$4m_1^2 = 4 \Rightarrow m_1^2 = 1$

Now, substitute $m_1 = -\dfrac{k}{5}$ into $m_1^2 = 1$:
$\left(-\dfrac{k}{5}\right)^2 = 1$
$\dfrac{k^2}{25} = 1$
$k^2 = 25$
$k = \pm 5$

From the given options, the value of $k$ is $5$.

Answer: 5

</details>

---

### Q54. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{f}(x)=\mathrm{e}^x, \mathrm{~g}(x)=\sin ^{-1} x$ and $\mathrm{h}(x)=\mathrm{f}(\mathrm{g}(x))$, then $\left(\dfrac{\mathrm{h}^{\prime}(x)}{\mathrm{h}(x)}\right)^2$ is equal to

**Options:**

- **(A)** $\dfrac{1}{\sqrt{1-x^2}}$
- **(B)** $\left(1-x^2\right)^2$
- **(C)** $\dfrac{1}{1-x^2}$
- **(D)** $\left(1-x^2\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{1-x^2}$**

**Detailed Solution:**

Given $f(x) = e^x$ and $g(x) = \sin^{-1} x$.

The composite function $h(x)$ is given by:

$h(x) = f(g(x)) = e^{\sin^{-1} x}$

Differentiating $h(x)$ with respect to $x$ using the chain rule:

$h'(x) = e^{\sin^{-1} x} \cdot \dfrac{1}{\sqrt{1-x^2}}$

Substituting $h(x) = e^{\sin^{-1} x}$ back into the equation:

$h'(x) = h(x) \cdot \dfrac{1}{\sqrt{1-x^2}}$

Rearranging the terms:

$\dfrac{h'(x)}{h(x)} = \dfrac{1}{\sqrt{1-x^2}}$

Squaring both sides:

$\left(\dfrac{h'(x)}{h(x)}\right)^2 = \dfrac{1}{1-x^2}$

Answer: $\dfrac{1}{1-x^2}$

</details>

---

### Q55. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\cos ^{-1} x, \mathrm{~g}(x)=\mathrm{e}^x$ and $\mathrm{h}(x)=\mathrm{g}(\mathrm{f}(x))$, then $\dfrac{\mathrm{h}^{\prime}(x)}{\mathrm{h}(x)}=$

**Options:**

- **(A)** $\dfrac{-1}{\sqrt{1-x^2}}$
- **(B)** $\dfrac{-(e)^{\left(\cos ^{-1} x\right)}}{\sqrt{1-x^2}}$
- **(C)** $\dfrac{-1}{\sqrt{1-x^2}} \mathrm{e}^x$
- **(D)** $-\sqrt{1-x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{-1}{\sqrt{1-x^2}}$**

**Detailed Solution:**

Given $f(x) = \cos^{-1} x$ and $g(x) = e^x$.

The composite function $h(x)$ is given by:

$h(x) = g(f(x)) = e^{\cos^{-1} x}$

Taking the natural logarithm on both sides:

$\ln(h(x)) = \cos^{-1} x$

Differentiating both sides with respect to $x$:

$\dfrac{1}{h(x)} h^{\prime}(x) = \dfrac{-1}{\sqrt{1-x^2}}$

$\dfrac{h^{\prime}(x)}{h(x)} = \dfrac{-1}{\sqrt{1-x^2}}$

Answer: $\dfrac{-1}{\sqrt{1-x^2}}$

</details>

---

### Q56. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The curve $y=\mathrm{a} x^3+\mathrm{b} x^2+\mathrm{c} x+5$ touches the x -axis at $(-2,0)$ and cuts the $y$-axis at a point Q where its gradient is 3 , then the value of $\mathrm{a}+\mathrm{b}+\mathrm{c}$ is

**Options:**

- **(A)** $\dfrac{7}{8}$
- **(B)** $\dfrac{7}{4}$
- **(C)** $\dfrac{7}{2}$
- **(D)** $\dfrac{7}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{7}{4}$**

**Detailed Solution:**

The equation of the curve is $y = a x^3 + b x^2 + c x + 5$.

Differentiating with respect to $x$, we get:

$\dfrac{dy}{dx} = 3a x^2 + 2b x + c$

The curve cuts the $y$-axis at point Q, which means the $x$-coordinate of Q is $0$. The gradient at Q is given as $3$.

$\left. \dfrac{dy}{dx} \right|_{x=0} = c = 3$

The curve touches the $x$-axis at $(-2, 0)$, which implies that the point lies on the curve and the gradient at this point is $0$.

Substituting $x = -2$ and $y = 0$ in the curve's equation:

$-8a + 4b - 2c + 5 = 0$

Substituting $c = 3$:

$-8a + 4b - 6 + 5 = 0 \Rightarrow 8a - 4b = -1$

Now, substituting $x = -2$ in the gradient equation and equating it to $0$:

$\left. \dfrac{dy}{dx} \right|_{x=-2} = 12a - 4b + c = 0$

Substituting $c = 3$:

$12a - 4b + 3 = 0 \Rightarrow 12a - 4b = -3$

Subtracting the first equation from the second equation:

$(12a - 4b) - (8a - 4b) = -3 - (-1)$

$4a = -2 \Rightarrow a = -\dfrac{1}{2}$

Substituting the value of $a$ in $8a - 4b = -1$:

$8\left(-\dfrac{1}{2}\right) - 4b = -1 \Rightarrow -4 - 4b = -1 \Rightarrow 4b = -3 \Rightarrow b = -\dfrac{3}{4}$

Finally, calculating $a + b + c$:

$a + b + c = -\dfrac{1}{2} - \dfrac{3}{4} + 3 = \dfrac{-2 - 3 + 12}{4} = \dfrac{7}{4}$

Answer: $\dfrac{7}{4}$

</details>

---

### Q57. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y=a \sin x+b \cos x$ (where a and b are constants), then $y^2+\left(\dfrac{\mathrm{d} y}{\mathrm{~d} x}\right)^2$ is

**Options:**

- **(A)** a function of $x$.
- **(B)** a function of $x$ and $y$.
- **(C)** a function of $y$.
- **(D)** a constant.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) a constant.**

**Detailed Solution:**

Given $y = a \sin x + b \cos x$

Differentiating with respect to $x$, we get:

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = a \cos x - b \sin x$

Squaring both equations and adding them:

$y^2 + \left(\dfrac{\mathrm{d} y}{\mathrm{d} x}\right)^2 = (a \sin x + b \cos x)^2 + (a \cos x - b \sin x)^2$

$y^2 + \left(\dfrac{\mathrm{d} y}{\mathrm{d} x}\right)^2 = a^2 \sin^2 x + b^2 \cos^2 x + 2ab \sin x \cos x + a^2 \cos^2 x + b^2 \sin^2 x - 2ab \sin x \cos x$

$y^2 + \left(\dfrac{\mathrm{d} y}{\mathrm{d} x}\right)^2 = a^2(\sin^2 x + \cos^2 x) + b^2(\cos^2 x + \sin^2 x)$

Using the identity $\sin^2 x + \cos^2 x = 1$, we get:

$y^2 + \left(\dfrac{\mathrm{d} y}{\mathrm{d} x}\right)^2 = a^2 + b^2$

Since $a$ and $b$ are constants, $a^2 + b^2$ is a constant.

Answer: a constant.

</details>

---

### Q58. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\quad y=\sqrt{(x-\sin x)+\sqrt{(x-\sin x)+\sqrt{(x-\sin x) \ldots .}}}$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}=$

**Options:**

- **(A)** $\frac{1-\cos x}{2 y-1}$
- **(B)** $\frac{1+\cos x}{2 y-1}$
- **(C)** $\frac{1-\cos x}{2 y+1}$
- **(D)** $\frac{1-\sin x}{2 y-1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1-\cos x}{2 y-1}$**

**Detailed Solution:**

$\begin{aligned} & \quad \text { If } y=\sqrt{\mathrm{f}(x)+\sqrt{\mathrm{f}(x)+\sqrt{\mathrm{f}(x)+\ldots}}}, \text { then } \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{\mathrm{f}^{\prime}(x)}{2 y-1} \\ & \quad y=\sqrt{(x-\sin x)+\sqrt{(x-\sin x)+\sqrt{(x-\sin x)+\ldots}}} \\ & \therefore \quad \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1-\cos x}{2 y-1}\end{aligned}$

</details>

---

### Q59. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}^{\prime}(x)=\sin (\log x)$ and $y=\mathrm{f}\left(\frac{2 x+3}{3-2 x}\right)$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}$ at $x=1$ is

**Options:**

- **(A)** $6 \sin (\log 5)$
- **(B)** $5 \sin (\log 6)$
- **(C)** $12 \sin (\log 5)$
- **(D)** $5 \sin (\log 12)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $12 \sin (\log 5)$**

**Detailed Solution:**

$\begin{aligned} & y=\mathrm{f}\left(\frac{2 x+3}{3-2 x}\right) \\ & \therefore \quad \frac{\mathrm{d} y}{\mathrm{~d} x}=\mathrm{f}^{\prime}\left(\frac{2 x+3}{3-2 x}\right) \cdot \frac{\mathrm{d}}{\mathrm{d} x}\left(\frac{2 x+3}{3-2 x}\right) \\ & =\mathrm{f}^{\prime}\left(\frac{2 x+3}{3-2 x}\right) \cdot \frac{(3-2 x) \cdot 2-(2 x+3)(-2)}{(3-2 x)^2} \\ & =\sin \left[\log \left(\frac{2 x+3}{3-2 x}\right)\right] \cdot \frac{12}{(3-2 x)^2} \\ & \therefore \quad\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)_{x=1}=\sin (\log 5) \cdot 12=12 \sin (\log 5) \\ & \end{aligned}$

</details>

---

### Q60. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=[(x+1)(2 x+1)(3 x+1) \ldots .(\mathrm{n} x+1)]^{\mathrm{n}}$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}$ at $x=0$ is

**Options:**

- **(A)** $\frac{\mathrm{n}(\mathrm{n}+1)}{2}$
- **(B)** $\frac{\mathrm{n}^2(\mathrm{n}+1)}{2}$
- **(C)** $\frac{\mathrm{n}(\mathrm{n}+1)}{4}$
- **(D)** $\frac{\mathrm{n}^2(\mathrm{n}-1)}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\mathrm{n}^2(\mathrm{n}+1)}{2}$**

**Detailed Solution:**

$$
\begin{aligned}
& y=[(x+1)(2 x+1)(3 x+1) \ldots(\mathrm{n} x+1)]^{\mathrm{n}} \\
& \Rightarrow \log y=\operatorname{nlog}[(x+1)(2 x+1)(3 x+1) \\
& \Rightarrow \log y=\mathrm{n}[\log (x+1)+\log (2 x+1) \\
& \quad+\log (3 x+1)+\ldots+\log (\mathrm{n} x+1)]
\end{aligned}
$$
Differentiating both sides w.r.t. $x$, we get
$$
\begin{aligned}
& \frac{1}{y} \cdot \frac{\mathrm{d} y}{\mathrm{~d} x}=\mathrm{n}\left(\frac{1}{x+1}+\frac{2}{2 x+1}+\frac{3}{3 x+1}+\ldots+\frac{\mathrm{n}}{\mathrm{n} x+1}\right) \\
& \Rightarrow \frac{1}{1} \cdot\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)_{x=0}=\mathrm{n}(1+2+3+\ldots+\mathrm{n})
\end{aligned}
$$
$\ldots[$ At $x=0, y=1]$
$\Rightarrow\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)_{x=0}=\mathrm{n}\left[\frac{\mathrm{n}(\mathrm{n}+1)}{2}\right]=\frac{\mathrm{n}^2(\mathrm{n}+1)}{2}$

</details>

---

### Q61. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$y=\frac{\sqrt[3]{1+3 x} \sqrt[4]{1+4 x} \sqrt[5]{1+5 x}}{\sqrt[7]{1+7 x} \sqrt[8]{1+8 x}}$. Then $\frac{\mathrm{d} y}{\mathrm{~d} x}$ at $x=0$ is

**Options:**

- **(A)** 3
- **(B)** $-1$
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

$y=\frac{\sqrt[3]{1+3 x} \sqrt[4]{1+4 x} \sqrt[5]{1+5 x}}{\sqrt[7]{1+7 x} \sqrt[8]{1+8 x}}$
$\therefore \quad \log y=\frac{1}{3} \log (1+3 x)+\frac{1}{4} \log (1+4 x)$
$\begin{aligned}+\frac{1}{5} \log (1+5 x) & -\frac{1}{7} \log (1+7 x) \\ & -\frac{1}{8} \log (1+8 x)\end{aligned}$
Differentiating both sides w.r.t. $x$, we get
$$
\begin{array}{r}
\frac{1}{y} \cdot \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1}{3} \cdot \frac{1}{1+3 x} \cdot 3+\frac{1}{4} \cdot \frac{1}{1+4 x} \cdot 4+\frac{1}{5} \cdot \frac{1}{1+5 x} \cdot 5 \\
-\frac{1}{7} \cdot \frac{1}{1+7 x} \cdot 7-\frac{1}{8} \cdot \frac{1}{1+8 x} \cdot 8
\end{array}
$$
$\begin{aligned} & \therefore \quad \frac{1}{y} \cdot \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1}{1+3 x}+\frac{1}{1+4 x}+\frac{1}{1+5 x}-\frac{1}{1+7 x}-\frac{1}{1+8 x} \\ & \therefore \quad \frac{1}{1} \cdot\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)_{x=0}=\frac{1}{1+0}+\frac{1}{1+0}+\frac{1}{1+0}-\frac{1}{1+0}-\frac{1}{1+0} \\ & \ldots[\text { At } x=0, y=1]\end{aligned}$
$\Rightarrow\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)_{x=0}=1$

</details>

---

### Q62. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan y=\frac{x \sin \alpha}{1-x \cos \alpha}$ and $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{\mathrm{m}}{x^2+2 \mathrm{n} x+1}$, then $m^2+n^2$ is

**Options:**

- **(A)** $2$
- **(B)** $3$
- **(C)** $1$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

$\begin{aligned} & \tan y=\frac{x \sin \alpha}{1-x \cos \alpha} \\ & \therefore \quad y=\tan ^{-1}\left(\frac{x \sin \alpha}{1-x \cos \alpha}\right) \\ & \therefore \quad \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1}{1+\left(\frac{x \sin \alpha}{1-x \cos \alpha}\right)^2} \frac{\mathrm{d}}{\mathrm{d} x}\left(\frac{x \sin \alpha}{1-x \cos \alpha}\right) \\ & =\frac{\frac{1}{1-2 x \cos \alpha+x^2 \cos ^2 \alpha+x^2 \sin ^2 \alpha}}{(1-x \cos \alpha)^2} \\ & \times \frac{(1-x \cos \alpha) \sin \alpha+(x \sin \alpha) \cos \alpha}{(1-x \cos \alpha)^{2^{\prime}}} \\ & =\frac{\sin \alpha-x \sin \alpha \cos \alpha+x \sin \alpha \cos \alpha}{1+2(-\cos \alpha) x+x^2} \\ & =\frac{\sin \alpha}{x^2+2(-\cos \alpha)+1} \\ & =\frac{\mathrm{m}}{x^2+2 \mathrm{n} x+1} \\ & \Rightarrow \mathrm{n}=-\cos \alpha \text { and } \mathrm{m}=\sin \alpha \\ & \Rightarrow m^2+n^2=1 \\ & \end{aligned}$

</details>

---

### Q63. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$$
y=(1+x)\left(1+x^2\right)\left(1+x^4\right) \ldots \ldots \ldots\left(1+x^{2 n}\right) \text {, }
$$
then the value of $\frac{d y}{d x}$ at $x=0$ is

**Options:**

- **(A)** 0
- **(B)** -1
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

$$
y=(1+x)\left(1+x^2\right)\left(1+x^4\right) \ldots\left(1+x^{2 n}\right)
$$
Taking ' $\log$ ' on both sides, we get
$$
\begin{aligned}
\log y=\log (1+x)+\log \left(1+x^2\right) & +\log \left(1+x^4\right) \\
& +\ldots+\log \left(1+x^{2 \mathrm{n}}\right)
\end{aligned}
$$
Differentiating w.r.t. $x$, we get
$$
\frac{1}{y} \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1}{1+x}+\frac{2 x}{1+x^2}+\frac{4 x^3}{1+x^4}+\ldots+\frac{2 \mathrm{n} \times x^{2 \mathrm{n}-1}}{1+x^{2 \mathrm{n}}}
$$
At $x=0$, (i) $\Rightarrow y=1$
$\therefore \quad\left(\right.$ ii) $\left.\Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}\right|_{x=0}=1+0+0+\ldots+0=1$

</details>

---

### Q64. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y=[(x+1)(2 x+1)(3 x+1) \ldots \ldots(\mathrm{n} x+1)]^{\frac{3}{2}}$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}$ at $x=0$ is

**Options:**

- **(A)** $\frac{3 \mathrm{n}(\mathrm{n}+1)}{4}$
- **(B)** $\frac{\mathrm{n}(\mathrm{n}+1)}{2}$
- **(C)** $\frac{3 \mathrm{n}(\mathrm{n}+1)}{2}$
- **(D)** $\frac{\mathrm{n}(\mathrm{n}+1)}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3 \mathrm{n}(\mathrm{n}+1)}{4}$**

**Detailed Solution:**

$y=[(x+1)(2 x+1)(3 x+1) \ldots(\mathrm{n} x+1)]^{\frac{3}{2}}$
Taking 'log' on both sides, we get
$\begin{array}{r}
\log y=\frac{3}{2}[\log (x+1)+\log (2 x+1)+\log (3 x+1) \\
+\ldots+\log (n x+1)]
\end{array}$
Differentiating w.r.t. $x$, we get
$\begin{aligned}
& \quad \frac{1}{y} \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{3}{2}\left[\frac{1}{x+1}+\frac{2}{2 x+1}+\frac{3}{3 x+1}+\ldots+\frac{\mathrm{n}}{\mathrm{n} x+1}\right] \\
& \therefore \quad \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{3 y}{2}\left[\frac{1}{x+1}+\frac{2}{2 x+1}+\frac{3}{3 x+1}+\ldots+\frac{\mathrm{n}}{\mathrm{n} x+1}\right] \\
& \text { Now at } x=0, y=[\underbrace{(1)(1)(1) \ldots(1)}_{\mathrm{n} \text { times }}]^{\frac{3}{2}}=1
\end{aligned}$
$\begin{aligned}\left.\therefore \quad \frac{\mathrm{d} y}{\mathrm{~d} x}\right|_{x=0} & =\frac{3(1)}{2}\left[\frac{1}{0+1}+\frac{2}{0+1}+\frac{3}{0+1}+\ldots+\frac{\mathrm{n}}{0+1}\right] \\ & =\frac{3}{2}(1+2+3+\ldots+\mathrm{n}) \\ & =\frac{3}{2} \times \frac{\mathrm{n}(\mathrm{n}+1)}{2} \\ & =\frac{3 \mathrm{n}(\mathrm{n}+1)}{4}\end{aligned}$

</details>

---

### Q65. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\log _{\sin x} \tan x$, then $\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)_{x=\frac{\pi}{4}}$ has the value

**Options:**

- **(A)** $\frac{4}{\log 2}$
- **(B)** $-3 \log 2$
- **(C)** $\frac{-4}{\log 2}$
- **(D)** $3 \log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{-4}{\log 2}$**

**Detailed Solution:**

$$
\begin{aligned}
& y=\frac{\log \tan x}{\log \sin x} \\
& \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{(\log \sin x)\left(\frac{1}{\tan x}\right) \cdot \sec ^2 x-(\log \tan x)\left(\frac{1}{\sin x}\right)(\cos x)}{(\log \sin x)^2}
\end{aligned}
$$

At $x=\frac{\pi}{4}$
$$
\begin{aligned}
& \left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)_{x=\frac{\pi}{4}}=\frac{\log \left(\frac{1}{\sqrt{2}}\right)\left(\frac{1}{1}\right)(\sqrt{2})^2-(\log 1)\left(\frac{\sqrt{2}}{1}\right)\left(\frac{1}{\sqrt{2}}\right)}{\left[\log \left(\frac{1}{\sqrt{2}}\right)\right]^2} \\
& =\frac{-2 \times \frac{1}{2}(\log 2)-0}{\frac{1}{4}(\log 2)^2} \quad \ldots[\because \log 1=0] \\
& =\frac{-4}{\log 2}
\end{aligned}
$$

</details>

---

### Q66. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(1)=1, \mathrm{f}^{\prime}(1)=3$, then the derivative of $\mathrm{f}(\mathrm{f}(\mathrm{f}(x)))+(\mathrm{f}(x))^2$ at $x=1$ is

**Options:**

- **(A)** 12
- **(B)** 19
- **(C)** 23
- **(D)** 33

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 33**

**Detailed Solution:**

Let $y=\mathrm{f}(\mathrm{f}(\mathrm{f}(x)))+(\mathrm{f}(x))^2$
$\therefore \quad \frac{\mathrm{d} y}{\mathrm{~d} x}=\mathrm{f}^{\prime}(\mathrm{f}(\mathrm{f}(x))) \cdot \mathrm{f}^{\prime}(\mathrm{f}(x)) \cdot \mathrm{f}^{\prime}(x)+2 \mathrm{f}(x) \mathrm{f}^{\prime}(x)$
$\begin{aligned}\left.\frac{\mathrm{d} y}{\mathrm{~d} x}\right|_{x=1} & =\mathrm{f}^{\prime}(\mathrm{f}(\mathrm{f}(1))) \cdot \mathrm{f}^{\prime}(\mathrm{f}(1)) \cdot \mathrm{f}^{\prime}(1)+2 \mathrm{f}(1) \mathrm{f}^{\prime}(1) \\ & =3 \cdot 3 \cdot 3+2 \cdot 1 \cdot 3 \\ & =33\end{aligned}$

</details>

---

### Q67. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

For $x \in R, f(x)=|\log 2-\sin x|$ and $g(x)=f(f(x))$, then

**Options:**

- **(A)** $g^{\prime}(0)=-\cos (\log 2)$
- **(B)** $g$ is not differentiable at $x=0$.
- **(C)** $g^{\prime}(0)=\cos (\log 2)$
- **(D)** $g$ is differentiable at $x=0$ and $g^{\prime}(0)=-\sin (\log 2)$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $g^{\prime}(0)=\cos (\log 2)$**

**Detailed Solution:**

for $x \rightarrow 0^{-}$
$g(x)=\log 2-\sin (\log 2-\sin x)$
for $x \rightarrow 0^{+}$
$g(x)=\log 2-\sin (\log 2-\sin x)$
[as $\log 2>\sin 0$ and $x>\sin x$ ]
and $g(x)$ is continuous at $x=0$
$\begin{aligned} & \text { now } g^{\prime}(x)=0-\cos (\log 2-\sin x)(0-\cos x) \\ & \Rightarrow g^{\prime}(0)=\cos (\log 2)\end{aligned}$

</details>

---

### Q68. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=15-|x-10| ; x \in R$. Then, the set of all values of $x$, at which the function $g(x)=f(f(x))$ is not differentiable, is

**Options:**

- **(A)** $\{10\}$
- **(B)** $\{10,15\}$
- **(C)** $\{5,10,15,20\}$
- **(D)** $\{5,10,15\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\{5,10,15\}$**

**Detailed Solution:**

$\begin{aligned} & f(x)=15-|x-10| \\ & \Rightarrow f(f(x))=f(15-|x-10|) \\ & =15-|15-| x-10|-10| \\ & =15-|5-| x-10||\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/babD0ewE7i4d-FWECrj2XmaqAiSb9cnANs0B0TwHLTs.original.fullsize.png">
graph has 3 corner points $x=5, x=10$ and $x=15$
So, it is not differentiable at $x \in\{5,10,15\}$

</details>

---

### Q69. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\operatorname{cosec}^{-1}\left[\frac{10}{6 \sin \left(2^x\right)-8 \cos \left(2^x\right)}\right]$, then $f^{\prime}(x)$

**Options:**

- **(A)** $2^x \log 2$
- **(B)** $-1$
- **(C)** $\log 2$
- **(D)** $2^x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2^x \log 2$**

**Detailed Solution:**

$\begin{aligned} & f(x)=\operatorname{cosec}^{-1}\left[\frac{10}{6 \sin \left(2^x\right)-8 \cos \left(2^x\right)}\right]=\sin ^{-1}\left[\frac{6 \sin \left(2^x\right)-8 \cos \left(2^x\right)}{10}\right] \\ & \text { Here }(6)^2+(-8)^2=(10)^2 \\ & \therefore \text { Let } \cos \alpha=\frac{6}{10} \text { and } \sin \alpha=\frac{8}{10} \\ & \therefore f(x)=\sin ^{-1}\left[\sin \left(2^x\right) \cos \alpha-\cos \left(2^x\right) \sin \alpha\right]=\sin ^{-1}\left[\sin \left(2^x-\alpha\right)\right] \\ & \therefore f(x)=2^x-\alpha \Rightarrow f^{\prime}(x)=2^x \log 2\end{aligned}$

</details>

---

### Q70. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\log \sqrt{\tan x}$, then the value of $\frac{d y}{d x}$ at $x=\frac{\pi}{4}$ is

**Options:**

- **(A)** 1
- **(B)** $-1$
- **(C)** $\frac{1}{2}$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

$\begin{aligned} & y=\log \sqrt{\tan x} \\ & \therefore \quad \frac{d y}{d x}=\frac{1}{\sqrt{\tan x}} \times \frac{1}{2 \sqrt{\tan x}} \times \sec ^2 x=\frac{\sec ^2 x}{2 \tan x} \\ & \therefore \quad\left(\frac{d y}{d x}\right)_{x=\frac{\pi}{4}}=\frac{(\sqrt{2})^2}{2}=1\end{aligned}$

</details>

---

### Q71. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\sqrt{e^{\sqrt{x}}}$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{e^{\sqrt{x}}}{4 \sqrt{x}}$
- **(B)** $\frac{e^{\sqrt{x}}}{4 x}$
- **(C)** $\frac{e^{\frac{\sqrt{x}}{2}}}{4 \sqrt{x}}$
- **(D)** $\frac{\mathrm{e}^{\sqrt{\mathrm{x}}}}{2 \sqrt{\mathrm{x}}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{e^{\frac{\sqrt{x}}{2}}}{4 \sqrt{x}}$**

**Detailed Solution:**

$$
\begin{aligned}
& 2 \log y=\sqrt{x} \log e \Rightarrow 2 \log y=\sqrt{x} \\
& \frac{2}{y} \frac{d y}{d x}=\frac{1}{2 \sqrt{x}} \Rightarrow \frac{d y}{d x}=y\left[\frac{1}{4 \sqrt{x}}\right]=\frac{\sqrt{e^{\sqrt{x}}}}{4 \sqrt{x}}
\end{aligned}
$$
Taking $\log$ on both sides,
$$
2 \log \mathrm{y}=\sqrt{\mathrm{x}} \log \mathrm{e} \Rightarrow 2 \log \mathrm{y}=\sqrt{\mathrm{x}}
$$
Differentiating both sides w.r.t. $x$, we get
$$
\frac{2}{y} \frac{d y}{d x}=\frac{1}{2 \sqrt{x}} \Rightarrow \frac{d y}{d x}=y\left[\frac{1}{4 \sqrt{x}}\right]=\frac{\sqrt{e^{\sqrt{x}}}}{4 \sqrt{x}}
$$

</details>

---

### Q72. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $h(x)=\sqrt{4 f(x)+3 g(x)}, f(1)=4, g(1)=3, f^{\prime}(1)=4$, then $\mathrm{h}(1)=$

**Options:**

- **(A)** $\frac{5}{12}$
- **(B)** $\frac{12}{5}$
- **(C)** $\frac{-5}{12}$
- **(D)** $\frac{-12}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{12}{5}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/QXBy0MzD5-ZvgxHDRZ7x8quygIz7YeGSOpjd91IBGxY.original.fullsize.png">

</details>

---

### Q73. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\log \tan \left(\frac{x}{2}\right)+\sin ^1(\cos x)$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\operatorname{cosec} x$
- **(B)** $\sin x+1$
- **(C)** x
- **(D)** $\operatorname{cosec} x-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\operatorname{cosec} x-1$**

**Detailed Solution:**

$\begin{aligned} & y=\log \tan \left(\frac{x}{2}\right)+\sin ^{-1}(\cos x) \\ & =\log \tan \left(\frac{x}{2}\right)+\sin ^{-1}\left[\sin \left(\frac{\pi}{2}-x\right)\right]=\log \tan \left(\frac{x}{2}\right)+\frac{\pi}{2}-x \\ & \therefore \frac{d y}{d x}=\frac{1}{\tan \left(\frac{x}{2}\right)} \times \sec ^2 \times\left(\frac{x}{2}\right) \times\left(\frac{1}{2}\right)+0-1 \\ & =\frac{\cos \frac{x}{2}}{\sin \frac{x}{2}} \times \frac{1}{\cos ^2 \frac{x}{2}} \times \frac{1}{2}-1 \\ & =\frac{1}{2 \sin \frac{x}{2} \cos \frac{x}{2}}-1=\frac{1}{\sin x}-1=\operatorname{cosec} x-1\end{aligned}$

</details>

---

### Q74. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\log \left[a^{3 x}\left(\frac{5-x}{x+4}\right)^{\frac{3}{4}}\right]$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $3+\frac{3}{4(5-x)}-\frac{3}{4(x+4)}$
- **(B)** $\frac{3}{a}+\frac{3}{4(5-x)}-\frac{3}{4(x+4)}$
- **(C)** $\frac{3}{\log a}-\frac{3}{4(5-x)}-\frac{3}{4(x+4)}$
- **(D)** $3 \log a-\frac{3}{4(5-x)}-\frac{3}{4(x+4)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3 \log a-\frac{3}{4(5-x)}-\frac{3}{4(x+4)}$**

**Detailed Solution:**

$y=\log \left[a^{3 x}\left(\frac{5-x}{x+4}\right)^{\frac{3}{4}}\right]$
$\begin{aligned} \therefore y &=\log _{a} 3 x+\log \left(\frac{5-x}{x+4}\right)^{\frac{3}{4}} \\ &=3 x \log a+\frac{3}{4} \log (5-x)-\frac{3}{4} \log (x+4) \end{aligned}$
$\therefore \frac{d y}{d x}=3 \log a+\frac{3(-1)}{4(5-x)}-\frac{3}{4(x+4)}$
$=3 \log a-\frac{3}{4(5-x)}-\frac{3}{4(x+4)}$

</details>

---

### Q75. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=\log (\sec x+\tan x)$, then $f^{\prime}\left(\frac{\pi}{4}\right)=$

**Options:**

- **(A)** 1
- **(B)** $\frac{2}{\sqrt{3}}$
- **(C)** $\frac{1}{\sqrt{2}}$
- **(D)** $\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{2}$**

**Detailed Solution:**

(B)
$y=\log (\sec x+\tan x)$
Differentially w.r.t. $x$
$\begin{array}{l}
\frac{\mathrm{dy}}{\mathrm{dx}}=\frac{1}{\sec \mathrm{x}+\tan \mathrm{x}} \cdot\left(\sec \mathrm{x} \cdot \tan \mathrm{x}+\sec ^{2} \mathrm{x}\right)=\frac{\sec \mathrm{x}(\tan \mathrm{x}+\sec \mathrm{x})}{(\sec \mathrm{x}+\tan \mathrm{x})} \\
\frac{\mathrm{dy}}{\mathrm{dx}}=\sec \mathrm{x} \Rightarrow \mathrm{f}^{\prime}(\mathrm{x})=\sec \mathrm{x} \\
\mathrm{f}^{\prime}\left(\frac{\pi}{4}\right)=\sec \frac{\pi}{4}=\sqrt{2}
\end{array}$

</details>

---

### Q76. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}$ and $\mathrm{g}$ are differentiable functions satisfying $\mathrm{g}^{\prime}(\mathrm{a})=2, \mathrm{~g}(\mathrm{a})=\mathrm{b}$ and $\mathrm{fog}=\mathrm{I}$, where is an identity function, then $\mathrm{f}^{\prime}(\mathrm{b})$ is equal to

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{3}{2}$
- **(C)** $\frac{2}{3}$
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

Given
$$
g(a)=b, g^{\prime}(a)=2, f[g(x)]=x
$$
Now $f^{\prime}[g(x)] g^{\prime}(x)=1 \Rightarrow f^{\prime}(g(x))=\frac{1}{g^{\prime}(x)}$
Put $x=a$, we get
$$
f^{\prime}[g(a)]=\frac{1}{g^{\prime}(a)} \Rightarrow f^{\prime}(b)=\frac{1}{2}
$$

</details>

---

### Q77. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=e^{\sin \left(\operatorname{cosec}^{-1} x\right)}$ , then  $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{e^{\frac{1}{x}}}{x^{2}}$
- **(B)** $-\frac{e^{\frac{1}{x}}}{x^{2}}$
- **(C)** 0
- **(D)** $e^{\cos \left(\operatorname{cosec}^{-1} x\right)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{e^{\frac{1}{x}}}{x^{2}}$**

**Detailed Solution:**

Given $y=e^{\sin \left(\operatorname{cosec}^{-1} x\right)}$
$\quad=e^{\sin \left(\sin ^{-1} \frac{1}{x}\right)} \Rightarrow y=e^{\frac{1}{x}}$
$\frac{d y}{d x}=e^{\frac{1}{x}}\left(-\frac{1}{x^{2}}\right)$

</details>

---

### Q78. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\cot ^{-1}\left(\sqrt{\frac{1-\sin x}{1+\sin x}}\right)$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $-1$
- **(C)** $\frac{1}{3}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

$\begin{aligned}
y &=\cot ^{-1} \sqrt{\frac{\left(\cos \frac{x}{2}-\sin \frac{x}{2}\right)^{2}}{\left(\cos \frac{x}{2}+\sin \frac{x}{2}\right)^{2}}}=\cot ^{-1}\left(\frac{\cos \frac{x}{2}-\sin \frac{x}{2}}{\cos \frac{x}{2}+\sin \frac{x}{2}}\right) \\
&=\cot ^{-1}\left[\frac{1-\tan \frac{x}{2}}{\left.1+\tan \frac{x}{2}\right)}=\tan ^{-1}\left(\frac{1+\tan \frac{x}{2}}{1-\tan \frac{x}{2}}\right)=\tan ^{-1}\left[\frac{\tan \frac{\pi}{4}+\tan \frac{x}{2}}{1-\tan \frac{\pi}{4} \tan \frac{x}{2}}\right]\right.\\
\therefore \frac{d y}{d x} &=0+\frac{1}{2}=\frac{1}{2}
\end{aligned}$

</details>

---

### Q79. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y=3 e^{5 x}+5 e^{3 x}, \quad$ then $\frac{d^{2} y}{d x^{2}}-8 \frac{d y}{d x}=$

**Options:**

- **(A)** $-10 y$
- **(B)** $15 y$
- **(C)** $-15 y$
- **(D)** $10 y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-15 y$**

**Detailed Solution:**

$\begin{aligned} & y=3 e^{5 x}+5 e^{3 x} \\ \therefore & \frac{d y}{d x}=3 e^{5 x} \times 5+5 e^{3 x} \times 3=15 e^{5 x}+15 e^{3 x} \\ \frac{d^{2} y}{d x^{2}} &=15 e^{5 x} \times 5+15 e^{3 x} \times 3 \\ &=75 e^{5 x}+45 e^{3 x} \\ \therefore \frac{d^{2} y}{d x^{2}}-8 \frac{d y}{d x} &=75 e^{5 x}+45 e^{3 x}-8\left(15 e^{5 x}+15 e^{3 x}\right) \\ &=75 e^{5 x}+45 e^{3 x}-120 e^{5 x}-120 e^{3 x} \\ &=-45 e^{5 x}-75 e^{3 x} \\ &=-15\left(3 e^{5 x}+5 e^{3 x}\right) \\ &=-15 y \end{aligned}$

</details>

---

### Q80. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The displacement of a particle at the time $\mathrm{t}$ is given by $\quad s=\sqrt{1+t}$, then its
acceleration 'a' is proportional to

**Options:**

- **(A)** square of the velocity
- **(B)** $\sqrt[3]{S}$
- **(C)** $\sqrt{S}$
- **(D)** cube of the velocity

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) cube of the velocity**

**Detailed Solution:**

Given $s=\sqrt{1+t}$
Differentiating with respect to $\mathrm{t}$, we get
$\begin{aligned}
\mathrm{v} &=\frac{\mathrm{ds}}{\mathrm{dt}}=\frac{1}{2 \sqrt{1+\mathrm{t}}} \\
\mathrm{a} &=\frac{\mathrm{d}^{2} \mathrm{~s}}{\mathrm{dt}^{2}}=\frac{1}{2} \frac{\mathrm{d}}{\mathrm{dt}}(1+\mathrm{t})^{\frac{-1}{2}}=\frac{1}{2}\left(-\frac{1}{2}\right)(1+\mathrm{t})^{\frac{-3}{2}} \\
&=\left(\frac{-1}{4}\right)\left(\frac{1}{(1+\mathrm{t})^{\frac{3}{2}}}\right)=-2\left(\frac{1}{\left[(1+\mathrm{t})^{\frac{1}{2}}\right]^{3}}\right)=-2\left(\frac{1}{2 \sqrt{1+\mathrm{t}^{2}}}\right)^{3}=-2 \mathrm{v}^{3}
\end{aligned}$

</details>

---

### Q81. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>x</mi><mo>=</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mo>,</mo><mi>y</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>3</mn></mrow></msup><mi>θ</mi></math> then <math><mfrac><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math> at <math><mi>θ</mi></math> = <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math> is ….

**Options:**

- **(A)** 3
- **(B)** 6
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 6**

**Detailed Solution:**

We have , <math><mi>x</mi><mo>=</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mo>,</mo><mi>y</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>3</mn></mrow></msup><mi>θ</mi></math>  
<math><mo>∴</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>θ</mi></mrow></mfrac></mrow><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>θ</mi></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi><mfenced separators="|"><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mrow></mfenced></mrow><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mrow></mfrac></math>  
<math><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>3</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></math>  
Now, <math><mfrac><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>3</mn><mfenced separators="|"><mrow><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>θ</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math>  
<math><mo>=</mo><mn>3</mn><mfenced separators="|"><mrow><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mrow></mfenced><mfrac><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mrow></mfrac><mo>=</mo><mn>6</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></math>  
at <math><mi>θ</mi><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>6</mn><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mn>6</mn><mo>×</mo><mn>1</mn><mo>=</mo><mn>6</mn></math>

</details>

---

### Q82. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

A particle moves along a straight line according to the law $s=16-2 t+3 t^{3}$, where $s$ metres is the distance of the particle from a fixed point at the end of $t$ second. The acceleration of the particle at the end of $2 \mathrm{~s}$ is

**Options:**

- **(A)** $3.6 \mathrm{~m} / \mathrm{s}^{2}$
- **(B)** $36 \mathrm{~m} / \mathrm{s}^{2}$
- **(C)** $36 \mathrm{~km} / \mathrm{s}^{2}$
- **(D)** $360 \mathrm{~m} / \mathrm{s}^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $36 \mathrm{~m} / \mathrm{s}^{2}$**

**Detailed Solution:**

Given, $s=16-2 t+3 t^{3}$
$$
\begin{array}{lc}
\Rightarrow & \frac{d s}{d t}=-2+9 t^{2} \\
\Rightarrow \quad \frac{d^{2} s}{d t^{2}}=18 t
\end{array}
$$
Now, the acceleration of the particle at the end of $t=2 \mathrm{~s}$ is
$f=\frac{d^{2} s}{d t^{2}}=18 \times 2$
$=36 \mathrm{~m} / \mathrm{s}^{2}$

</details>

---

### Q83. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

The equation of motion of a particle moving along a straight line is $s=2 t^{3}-9 t^{2}+12 t$, where the units of $s$ and $t$ are centimetre and second. The acceleration of the particle will be zero after

**Options:**

- **(A)** $\frac{3}{2} \mathrm{~s}$
- **(B)** $\frac{2}{3} \mathrm{~s}$
- **(C)** $\frac{1}{2} \mathrm{~s}$
- **(D)** $1 \mathrm{~s}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3}{2} \mathrm{~s}$**

**Detailed Solution:**

$\frac{d s}{d t}=6 t^{2}-18 t+12$
Again, $\frac{d^{2} s}{d t^{2}}=12 t-18=$ acceleration
If acceleration becomes zero, then
$$
\begin{aligned}
0 &=12 t-18 \\
\Rightarrow \quad t &=\frac{3}{2} \mathrm{~s}
\end{aligned}
$$
Hence, acceleration will be zero after $\frac{3}{2} \mathrm{~s}$

</details>

---

### Q84. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

If $x^{3}+y^{3}-3 a x y=0$, then $\frac{d y}{d x}$ equals

**Options:**

- **(A)** $\frac{a y-x^{2}}{y^{2}-a x}$
- **(B)** $\frac{a y-x^{2}}{a y-y^{2}}$
- **(C)** $\frac{x^{2}+a y}{y^{2}+a x}$
- **(D)** $\frac{x^{2}+a y}{a x-y^{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{a y-x^{2}}{y^{2}-a x}$**

**Detailed Solution:**

Given, $x^{3}+y^{3}-3 a x y=0$
On differentiating w.r.t. $x$, we get $3 x^{2}+3 y^{2} \cdot \frac{d y}{d x}-3 a\left(x \frac{d y}{d x}+y\right)=0$
$\Rightarrow 3\left(x^{2}-a y\right)+3 \frac{d y}{d x}\left(y^{2}-a x\right)=0$
$\Rightarrow$
$\frac{d y}{d x}=\frac{a y-x^{2}}{y^{2}-a x}$

</details>

---

### Q85. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `1`

The velocity of a particle at time $t$ is given by the relation $v=6 t-\frac{t^{2}}{6}$. The distance traveled in $3 \mathrm{~s}$ is, if $s=0$ at $t=0$

**Options:**

- **(A)** $\frac{39}{2}$
- **(B)** $\frac{57}{2}$
- **(C)** $\frac{51}{2}$
- **(D)** $\frac{33}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{51}{2}$**

**Detailed Solution:**

Given, $v=\frac{d s}{d t}=6 t-\frac{t^{2}}{6}$
On integrating both sides, we get
$$
s=3 t^{2}-\frac{t^{3}}{18}+\text { constant }
$$
Now, put $s=0$ at $t=0$, we get constant $=0$
$$
\therefore \quad s=3 t^{2}-\frac{t^{3}}{18}
$$
Now, distance traveled in $3 s=3(3)^{2}-\frac{(3)^{3}}{18}$
$$
=27-\frac{27}{18}=\frac{51}{2}
$$

</details>

---

