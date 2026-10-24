# MHT CET Mathematics - Differentiation

## Topic 3: Parametric differentiation

**Total Questions:** 46

---

### Q1. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x = \dfrac{1 + \log t}{t^2}$ and $y = \dfrac{3 + 2\log t}{t}$, then the value of $\dfrac{dy}{dx}$ is

**Options:**

- **(A)** $t$
- **(B)** $1$
- **(C)** $0$
- **(D)** $\dfrac{y}{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $t$**

**Detailed Solution:**

Given $x = \dfrac{1 + \log t}{t^2}$

Differentiating with respect to $t$ using the quotient rule:

$\dfrac{dx}{dt} = \dfrac{t^2 \cdot \dfrac{1}{t} - (1 + \log t) \cdot 2t}{(t^2)^2}$

$\dfrac{dx}{dt} = \dfrac{t - 2t - 2t \log t}{t^4} = \dfrac{-t(1 + 2\log t)}{t^4} = \dfrac{-(1 + 2\log t)}{t^3}$

Given $y = \dfrac{3 + 2\log t}{t}$

Differentiating with respect to $t$ using the quotient rule:

$\dfrac{dy}{dt} = \dfrac{t \cdot \dfrac{2}{t} - (3 + 2\log t) \cdot 1}{t^2}$

$\dfrac{dy}{dt} = \dfrac{2 - 3 - 2\log t}{t^2} = \dfrac{-(1 + 2\log t)}{t^2}$

Now, finding $\dfrac{dy}{dx}$ by dividing $\dfrac{dy}{dt}$ by $\dfrac{dx}{dt}$:

$\dfrac{dy}{dx} = \dfrac{\dfrac{-(1 + 2\log t)}{t^2}}{\dfrac{-(1 + 2\log t)}{t^3}} = \dfrac{t^3}{t^2} = t$

Answer: $t$

</details>

---

### Q2. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $x = \dfrac{e^m + e^{-m}}{2}$ and $y = \dfrac{e^m - e^{-m}}{2}$ then $\dfrac{dy}{dx} =$

**Options:**

- **(A)** $\dfrac{y}{x}$
- **(B)** $\dfrac{x}{y}$
- **(C)** $\dfrac{-x}{y}$
- **(D)** $\dfrac{-y}{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{x}{y}$**

**Detailed Solution:**

Given $x = \dfrac{e^m + e^{-m}}{2}$ and $y = \dfrac{e^m - e^{-m}}{2}$

Differentiating $x$ and $y$ with respect to $m$:

$\dfrac{dx}{dm} = \dfrac{e^m - e^{-m}}{2} = y$

$\dfrac{dy}{dm} = \dfrac{e^m + e^{-m}}{2} = x$

Using the chain rule for parametric functions:

$\dfrac{dy}{dx} = \dfrac{\dfrac{dy}{dm}}{\dfrac{dx}{dm}} = \dfrac{x}{y}$

Answer: $\dfrac{x}{y}$

</details>

---

### Q3. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The second derivative of $a \sin^3 t$ with respect to $a \cos^3 t$ at $t = \dfrac{\pi}{4}$ is...

**Options:**

- **(A)** $\dfrac{4\sqrt{2}}{3a}$
- **(B)** $\dfrac{3a}{4\sqrt{2}}$
- **(C)** $\dfrac{4a}{3\sqrt{2}}$
- **(D)** $\dfrac{3\sqrt{2}}{4a}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{4\sqrt{2}}{3a}$**

**Detailed Solution:**

Let $y = a \sin^3 t$ and $x = a \cos^3 t$

$\dfrac{dy}{dt} = 3a \sin^2 t \cos t$

$\dfrac{dx}{dt} = -3a \cos^2 t \sin t$

$\dfrac{dy}{dx} = \dfrac{\dfrac{dy}{dt}}{\dfrac{dx}{dt}} = \dfrac{3a \sin^2 t \cos t}{-3a \cos^2 t \sin t} = -\tan t$

$\dfrac{d^2 y}{dx^2} = \dfrac{d}{dx} \left( \dfrac{dy}{dx} \right) = \dfrac{d}{dt} (-\tan t) \cdot \dfrac{dt}{dx}$

$\dfrac{d^2 y}{dx^2} = -\sec^2 t \cdot \dfrac{1}{-3a \cos^2 t \sin t} = \dfrac{1}{3a \cos^4 t \sin t}$

Substituting $t = \dfrac{\pi}{4}$:

$\dfrac{d^2 y}{dx^2} = \dfrac{1}{3a \left( \dfrac{1}{\sqrt{2}} \right)^4 \left( \dfrac{1}{\sqrt{2}} \right)} = \dfrac{1}{3a \left( \dfrac{1}{4} \right) \left( \dfrac{1}{\sqrt{2}} \right)} = \dfrac{4\sqrt{2}}{3a}$

Answer: $\dfrac{4\sqrt{2}}{3a}$

</details>

---

### Q4. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x=at^2$ and $y=2at, t\neq 0$ then ...

**Options:**

- **(A)** $x\dfrac{d^2x}{dy^2}+a=0$
- **(B)** $2a\dfrac{d^2x}{dy^2}-1=0$
- **(C)** $\dfrac{d^2x}{dy^2}-2a=0$
- **(D)** $\dfrac{d^2x}{dy^2}-1=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2a\dfrac{d^2x}{dy^2}-1=0$**

**Detailed Solution:**

Given $x = at^2$ and $y = 2at$.

From the second equation, $t = \dfrac{y}{2a}$.

Substituting the value of $t$ in the first equation:

$x = a\left(\dfrac{y}{2a}\right)^2 = \dfrac{y^2}{4a}$

Differentiating both sides with respect to $y$:

$\dfrac{dx}{dy} = \dfrac{d}{dy}\left(\dfrac{y^2}{4a}\right) = \dfrac{2y}{4a} = \dfrac{y}{2a}$

Differentiating again with respect to $y$:

$\dfrac{d^2x}{dy^2} = \dfrac{d}{dy}\left(\dfrac{y}{2a}\right) = \dfrac{1}{2a}$

Rearranging the terms:

$2a\dfrac{d^2x}{dy^2} = 1$

$2a\dfrac{d^2x}{dy^2} - 1 = 0$

Answer: $2a\dfrac{d^2x}{dy^2}-1=0$

</details>

---

### Q5. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x=a\sin t-b\cos t, y=a\cos t+b\sin t$ and it is given that $\dfrac{d^2y}{dx^2}=0$, then

**Options:**

- **(A)** $x^2+y^2=a$
- **(B)** $x^2+y^2=b$
- **(C)** $x^2+y^2=1$
- **(D)** $x^2+y^2=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x^2+y^2=0$**

**Detailed Solution:**

Given $x = a\sin t - b\cos t$ and $y = a\cos t + b\sin t$.

Differentiating $x$ and $y$ with respect to $t$:

$\dfrac{dx}{dt} = a\cos t + b\sin t = y$

$\dfrac{dy}{dt} = -a\sin t + b\cos t = -x$

Now, finding $\dfrac{dy}{dx}$:

$\dfrac{dy}{dx} = \dfrac{\dfrac{dy}{dt}}{\dfrac{dx}{dt}} = -\dfrac{x}{y}$

Differentiating again with respect to $x$:

$\dfrac{d^2y}{dx^2} = \dfrac{d}{dx}\left(-\dfrac{x}{y}\right)$

$\dfrac{d^2y}{dx^2} = -\left(\dfrac{y \cdot 1 - x \cdot \dfrac{dy}{dx}}{y^2}\right)$

Substituting $\dfrac{dy}{dx} = -\dfrac{x}{y}$ into the equation:

$\dfrac{d^2y}{dx^2} = -\left(\dfrac{y - x\left(-\dfrac{x}{y}\right)}{y^2}\right)$

$\dfrac{d^2y}{dx^2} = -\left(\dfrac{y + \dfrac{x^2}{y}}{y^2}\right) = -\dfrac{x^2 + y^2}{y^3}$

It is given that $\dfrac{d^2y}{dx^2} = 0$.

Therefore, $-\dfrac{x^2 + y^2}{y^3} = 0$

$x^2 + y^2 = 0$

Answer: $x^2+y^2=0$

</details>

---

### Q6. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x = 4t^3 + 3, y = 3t^4 + 4$ and $\dfrac{\frac{d^2x}{dy^2}}{\left(\frac{dx}{dy}\right)^n}$ is constant then the value of $n$ is

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $6$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5$**

**Detailed Solution:**

Given $x = 4t^3 + 3$ and $y = 3t^4 + 4$.

Differentiating with respect to $t$:

$\dfrac{dx}{dt} = 12t^2$

$\dfrac{dy}{dt} = 12t^3$

$\dfrac{dx}{dy} = \dfrac{\dfrac{dx}{dt}}{\dfrac{dy}{dt}} = \dfrac{12t^2}{12t^3} = \dfrac{1}{t} = t^{-1}$

Now, finding the second derivative $\dfrac{d^2x}{dy^2}$:

$\dfrac{d^2x}{dy^2} = \dfrac{d}{dy}\left(\dfrac{dx}{dy}\right) = \dfrac{d}{dt}\left(t^{-1}\right) \cdot \dfrac{dt}{dy}$

$\dfrac{d^2x}{dy^2} = -t^{-2} \cdot \dfrac{1}{12t^3} = -\dfrac{1}{12}t^{-5}$

Substituting these into the given expression:

$\dfrac{\dfrac{d^2x}{dy^2}}{\left(\dfrac{dx}{dy}\right)^n} = \dfrac{-\dfrac{1}{12}t^{-5}}{(t^{-1})^n} = -\dfrac{1}{12}t^{n-5}$

For this expression to be a constant, it must be independent of $t$. Therefore, the exponent of $t$ must be zero:

$n - 5 = 0 \Rightarrow n = 5$

Answer: $5$

</details>

---

### Q7. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x = a\sin^3 t$ and $y = a\cos^3 t$, then the value of $\dfrac{d^2y}{dx^2}$ at $t = \dfrac{\pi}{3}$ is equal to

**Options:**

- **(A)** $\dfrac{-32}{27a}$
- **(B)** $\dfrac{-32}{3\sqrt{3}a}$
- **(C)** $\dfrac{32}{27a}$
- **(D)** $\dfrac{-32}{9a}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{32}{27a}$**

**Detailed Solution:**

Given $x = a\sin^3 t$ and $y = a\cos^3 t$.

Differentiating with respect to $t$:

$\dfrac{dx}{dt} = 3a\sin^2 t \cos t$

$\dfrac{dy}{dt} = -3a\cos^2 t \sin t$

Now, $\dfrac{dy}{dx} = \dfrac{\dfrac{dy}{dt}}{\dfrac{dx}{dt}} = \dfrac{-3a\cos^2 t \sin t}{3a\sin^2 t \cos t} = -\cot t$

Differentiating again with respect to $x$:

$\dfrac{d^2y}{dx^2} = \dfrac{d}{dt}(-\cot t) \cdot \dfrac{dt}{dx}$

$\dfrac{d^2y}{dx^2} = \csc^2 t \cdot \dfrac{1}{3a\sin^2 t \cos t} = \dfrac{1}{3a\sin^4 t \cos t}$

Substituting $t = \dfrac{\pi}{3}$:

$\sin\left(\dfrac{\pi}{3}\right) = \dfrac{\sqrt{3}}{2}$ and $\cos\left(\dfrac{\pi}{3}\right) = \dfrac{1}{2}$

$\dfrac{d^2y}{dx^2} = \dfrac{1}{3a \left(\dfrac{\sqrt{3}}{2}\right)^4 \left(\dfrac{1}{2}\right)} = \dfrac{1}{3a \left(\dfrac{9}{16}\right) \left(\dfrac{1}{2}\right)} = \dfrac{32}{27a}$

Answer: $\dfrac{32}{27a}$

</details>

---

### Q8. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $x = at^2 - 1$, where $a > 0$ and $y = t^3 + 1$. If at $t = 1$, $\dfrac{d^2y}{dx^2} = \dfrac{3}{16}$, then the value of $a$ is...

**Options:**

- **(A)** $3$
- **(B)** $-2$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2$**

**Detailed Solution:**

Given $x = at^2 - 1$ and $y = t^3 + 1$

Differentiating with respect to $t$, we get

$\dfrac{dx}{dt} = 2at$ and $\dfrac{dy}{dt} = 3t^2$

$\dfrac{dy}{dx} = \dfrac{\dfrac{dy}{dt}}{\dfrac{dx}{dt}} = \dfrac{3t^2}{2at} = \dfrac{3t}{2a}$

Differentiating again with respect to $x$, we get

$\dfrac{d^2y}{dx^2} = \dfrac{d}{dt}\left(\dfrac{3t}{2a}\right) \cdot \dfrac{dt}{dx}$

$\dfrac{d^2y}{dx^2} = \dfrac{3}{2a} \cdot \dfrac{1}{2at} = \dfrac{3}{4a^2t}$

At $t = 1$, $\dfrac{d^2y}{dx^2} = \dfrac{3}{4a^2}$

Given that at $t = 1$, $\dfrac{d^2y}{dx^2} = \dfrac{3}{16}$

$\dfrac{3}{4a^2} = \dfrac{3}{16}$

$4a^2 = 16 \Rightarrow a^2 = 4$

Since $a > 0$, we get $a = 2$

Answer: $2$

</details>

---

### Q9. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x = \sin(t), y = \cos(pt)$, then $(1 - x^2)\dfrac{d^2 y}{dx^2} - x\dfrac{dy}{dx} = $

**Options:**

- **(A)** $0$
- **(B)** $-p^2 y$
- **(C)** $p^2 y$
- **(D)** $p$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-p^2 y$**

**Detailed Solution:**

Given $x = \sin(t)$ and $y = \cos(pt)$

$t = \sin^{-1}(x)$

Substituting $t$ in $y$:

$y = \cos(p \sin^{-1}(x))$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = -\sin(p \sin^{-1}(x)) \cdot \dfrac{p}{\sqrt{1 - x^2}}$

$\sqrt{1 - x^2} \dfrac{dy}{dx} = -p \sin(p \sin^{-1}(x))$

Differentiating again with respect to $x$:

$\sqrt{1 - x^2} \dfrac{d^2 y}{dx^2} + \dfrac{dy}{dx} \left( \dfrac{-x}{\sqrt{1 - x^2}} \right) = -p \cos(p \sin^{-1}(x)) \cdot \dfrac{p}{\sqrt{1 - x^2}}$

Multiplying the entire equation by $\sqrt{1 - x^2}$:

$(1 - x^2) \dfrac{d^2 y}{dx^2} - x \dfrac{dy}{dx} = -p^2 \cos(p \sin^{-1}(x))$

Since $y = \cos(p \sin^{-1}(x))$, we get:

$(1 - x^2) \dfrac{d^2 y}{dx^2} - x \dfrac{dy}{dx} = -p^2 y$

Answer: $-p^2 y$

</details>

---

### Q10. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x=\tan ^{-1}\left\{\frac{\sqrt{1+\mathrm{t}^2}-1}{\mathrm{t}}\right\}, \mathrm{y}=\cos ^{-1}\left\{\frac{1-\mathrm{t}^2}{1+\mathrm{t}^2}\right\}$ for $\mathrm{t} > 0$, then $\frac{\mathrm{dy}}{\mathrm{d} x}$ is equal to

**Options:**

- **(A)** 2
- **(B)** $\frac{1}{2}$
- **(C)** 4
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

Let $t = \tan \theta$. Since $t > 0$, we have $\theta \in \left(0, \dfrac{\pi}{2}\right)$.

For $x$:
$x = \tan^{-1}\left(\dfrac{\sqrt{1+\tan^2\theta}-1}{\tan\theta}\right)$

$x = \tan^{-1}\left(\dfrac{\sec\theta-1}{\tan\theta}\right)$

$x = \tan^{-1}\left(\dfrac{1-\cos\theta}{\sin\theta}\right)$

$x = \tan^{-1}\left(\dfrac{2\sin^2(\theta/2)}{2\sin(\theta/2)\cos(\theta/2)}\right)$

$x = \tan^{-1}(\tan(\theta/2)) = \dfrac{\theta}{2}$

For $y$:
$y = \cos^{-1}\left(\dfrac{1-\tan^2\theta}{1+\tan^2\theta}\right)$

$y = \cos^{-1}(\cos 2\theta) = 2\theta$

Now, differentiating $y$ with respect to $x$:
$\dfrac{\mathrm{dy}}{\mathrm{d}x} = \dfrac{\dfrac{\mathrm{dy}}{\mathrm{d}\theta}}{\dfrac{\mathrm{d}x}{\mathrm{d}\theta}}$

$\dfrac{\mathrm{dy}}{\mathrm{d}x} = \dfrac{2}{\dfrac{1}{2}} = 4$

Answer: 4

</details>

---

### Q11. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x=\mathrm{t}^2+\mathrm{t}+1, \mathrm{y}=\sin \left(\frac{\mathrm{t} \pi}{2}\right)+\cos \left(\frac{\mathrm{t} \pi}{2}\right)$, then $\frac{\mathrm{dy}}{\mathrm{d} x}$ at $\mathrm{t}=1$ is

**Options:**

- **(A)** $\frac{-\pi}{6}$
- **(B)** $\frac{\pi}{3}$
- **(C)** $\frac{-\pi}{4}$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{-\pi}{6}$**

**Detailed Solution:**

Given $x = t^2 + t + 1$

Differentiating with respect to $t$, we get

$\dfrac{\mathrm{d}x}{\mathrm{d}t} = 2t + 1$

At $t = 1$, $\dfrac{\mathrm{d}x}{\mathrm{d}t} = 2(1) + 1 = 3$

Given $y = \sin\left(\dfrac{t\pi}{2}\right) + \cos\left(\dfrac{t\pi}{2}\right)$

Differentiating with respect to $t$, we get

$\dfrac{\mathrm{d}y}{\mathrm{d}t} = \dfrac{\pi}{2}\cos\left(\dfrac{t\pi}{2}\right) - \dfrac{\pi}{2}\sin\left(\dfrac{t\pi}{2}\right)$

At $t = 1$, $\dfrac{\mathrm{d}y}{\mathrm{d}t} = \dfrac{\pi}{2}\cos\left(\dfrac{\pi}{2}\right) - \dfrac{\pi}{2}\sin\left(\dfrac{\pi}{2}\right) = \dfrac{\pi}{2}(0) - \dfrac{\pi}{2}(1) = -\dfrac{\pi}{2}$

Now, $\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{\dfrac{\mathrm{d}y}{\mathrm{d}t}}{\dfrac{\mathrm{d}x}{\mathrm{d}t}}$

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{-\dfrac{\pi}{2}}{3} = -\dfrac{\pi}{6}$

Answer: $\frac{-\pi}{6}$

</details>

---

### Q12. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x=\sin \mathrm{t}$ and $\mathrm{y}=\sin \mathrm{pt}$, then the value of $\left(1-x^2\right) \frac{d^2 y}{d x^2}-x \frac{d y}{d x}+\mathrm{p}^2 \mathrm{y}=$

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** $-1$
- **(D)** $\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Given $x = \sin t \Rightarrow t = \sin^{-1} x$

Also, $y = \sin pt$

Substituting $t = \sin^{-1} x$ in $y$, we get:

$y = \sin(p \sin^{-1} x)$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = \cos(p \sin^{-1} x) \cdot \dfrac{p}{\sqrt{1-x^2}}$

$\sqrt{1-x^2} \dfrac{dy}{dx} = p \cos(p \sin^{-1} x)$

Squaring both sides:

$(1-x^2) \left(\dfrac{dy}{dx}\right)^2 = p^2 \cos^2(p \sin^{-1} x)$

$(1-x^2) \left(\dfrac{dy}{dx}\right)^2 = p^2 (1 - \sin^2(p \sin^{-1} x))$

Since $y = \sin(p \sin^{-1} x)$, we can write:

$(1-x^2) \left(\dfrac{dy}{dx}\right)^2 = p^2 (1 - y^2)$

Differentiating again with respect to $x$:

$(1-x^2) \cdot 2 \dfrac{dy}{dx} \dfrac{d^2 y}{dx^2} + (-2x) \left(\dfrac{dy}{dx}\right)^2 = p^2 \left(-2y \dfrac{dy}{dx}\right)$

Dividing throughout by $2 \dfrac{dy}{dx}$:

$(1-x^2) \dfrac{d^2 y}{dx^2} - x \dfrac{dy}{dx} = -p^2 y$

$(1-x^2) \dfrac{d^2 y}{dx^2} - x \dfrac{dy}{dx} + p^2 y = 0$

Answer: 0

</details>

---

### Q13. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x=\sin \theta, y=\sin ^3 \theta$, then $\frac{d^2 y}{d x^2}$ at $\theta=\frac{\pi}{6}$ is

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{\sqrt{3}}{2}$
- **(C)** 3
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

Given $x = \sin \theta$ and $y = \sin^3 \theta$.

Substituting $x$ into $y$, we get $y = x^3$.

Differentiating with respect to $x$, we get:

$\dfrac{dy}{dx} = 3x^2$

Differentiating again with respect to $x$, we get:

$\dfrac{d^2 y}{d x^2} = 6x$

At $\theta = \dfrac{\pi}{6}$, $x = \sin \left(\dfrac{\pi}{6}\right) = \dfrac{1}{2}$.

Substituting $x = \dfrac{1}{2}$ into the second derivative:

$\dfrac{d^2 y}{d x^2} = 6 \times \dfrac{1}{2} = 3$

Answer: 3

</details>

---

### Q14. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x=a \sin 2 t(1+\cos 2 t), y=b \cos 2 t(1-\cos 2 t)$ then $\frac{d y}{d x}$ is equal to

**Options:**

- **(A)** $\frac{\mathrm{b}}{\mathrm{a}} \tan \mathrm{t}$
- **(B)** $\frac{a}{b} \tan t$
- **(C)** $\frac{\mathrm{b}}{a \tan \mathrm{t}}$
- **(D)** $\frac{a}{b \tan t}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\mathrm{b}}{\mathrm{a}} \tan \mathrm{t}$**

**Detailed Solution:**

Given $x = a \sin 2t (1 + \cos 2t)$

Differentiating with respect to $t$:

$\dfrac{dx}{dt} = a \left[ 2 \cos 2t (1 + \cos 2t) + \sin 2t (-2 \sin 2t) \right]$

$\dfrac{dx}{dt} = 2a \left[ \cos 2t + \cos^2 2t - \sin^2 2t \right]$

$\dfrac{dx}{dt} = 2a (\cos 2t + \cos 4t)$

Given $y = b \cos 2t (1 - \cos 2t)$

Differentiating with respect to $t$:

$\dfrac{dy}{dt} = b \left[ -2 \sin 2t (1 - \cos 2t) + \cos 2t (2 \sin 2t) \right]$

$\dfrac{dy}{dt} = 2b \left[ -\sin 2t + \sin 2t \cos 2t + \sin 2t \cos 2t \right]$

$\dfrac{dy}{dt} = 2b (-\sin 2t + 2 \sin 2t \cos 2t)$

$\dfrac{dy}{dt} = 2b (\sin 4t - \sin 2t)$

Now, $\dfrac{dy}{dx} = \dfrac{\dfrac{dy}{dt}}{\dfrac{dx}{dt}}$

$\dfrac{dy}{dx} = \dfrac{2b (\sin 4t - \sin 2t)}{2a (\cos 4t + \cos 2t)}$

Using the sum-to-product formulas $\sin A - \sin B = 2 \cos\left(\dfrac{A+B}{2}\right) \sin\left(\dfrac{A-B}{2}\right)$ and $\cos A + \cos B = 2 \cos\left(\dfrac{A+B}{2}\right) \cos\left(\dfrac{A-B}{2}\right)$:

$\dfrac{dy}{dx} = \dfrac{b}{a} \left( \dfrac{2 \cos 3t \sin t}{2 \cos 3t \cos t} \right)$

$\dfrac{dy}{dx} = \dfrac{b}{a} \tan t$

Answer: $\frac{\mathrm{b}}{\mathrm{a}} \tan \mathrm{t}$

</details>

---

### Q15. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x=a \cos ^3 \theta \quad y=a \sin ^3 \theta$
Then $\sqrt{1+\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)^2}=$

**Options:**

- **(A)** $\tan ^2 \theta$
- **(B)** $\sec ^2 \theta$
- **(C)** $|\sec \theta|$
- **(D)** $\tan \theta$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $|\sec \theta|$**

**Detailed Solution:**

Given $x = a \cos^3 \theta$ and $y = a \sin^3 \theta$

Differentiating with respect to $\theta$:

$\dfrac{\mathrm{d}x}{\mathrm{d}\theta} = -3a \cos^2 \theta \sin \theta$

$\dfrac{\mathrm{d}y}{\mathrm{d}\theta} = 3a \sin^2 \theta \cos \theta$

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{\dfrac{\mathrm{d}y}{\mathrm{d}\theta}}{\dfrac{\mathrm{d}x}{\mathrm{d}\theta}} = \dfrac{3a \sin^2 \theta \cos \theta}{-3a \cos^2 \theta \sin \theta} = -\tan \theta$

Substituting this into the given expression:

$\sqrt{1 + \left(\dfrac{\mathrm{d}y}{\mathrm{d}x}\right)^2} = \sqrt{1 + (-\tan \theta)^2}$

$\sqrt{1 + \tan^2 \theta} = \sqrt{\sec^2 \theta} = |\sec \theta|$

Answer: $|\sec \theta|$

</details>

---

### Q16. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{y}=\frac{\mathrm{K}^{\Large \cos ^{-1} x}}{1+\mathrm{K}^{\Large \cos ^{-1} x}}$ and $\mathrm{t}=\mathrm{K}^{\Large \cos ^{-1} x}$, then $\frac{\mathrm{dy}}{\mathrm{dt}}$

**Options:**

- **(A)** $\frac{1}{1+\mathrm{K}^{\Large {\cos ^{-1} x}}}$
- **(B)** $\frac{-1}{1+\mathrm{K}^{\Large \cos ^{-1} x}}$
- **(C)** $\frac{1}{\left(1+\mathrm{K}^{\Large \cos ^{-1} x}\right)^2}$
- **(D)** $\frac{-1}{\left(1+\mathrm{K}^{\Large \cos ^{-1} x}\right)^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{\left(1+\mathrm{K}^{\Large \cos ^{-1} x}\right)^2}$**

**Detailed Solution:**

Given $y = \dfrac{K^{\cos^{-1} x}}{1 + K^{\cos^{-1} x}}$ and $t = K^{\cos^{-1} x}$.

Substituting $t$ in the expression for $y$, we get:

$y = \dfrac{t}{1+t}$

Differentiating $y$ with respect to $t$ using the quotient rule:

$\dfrac{dy}{dt} = \dfrac{(1+t) \cdot 1 - t \cdot 1}{(1+t)^2}$

$\dfrac{dy}{dt} = \dfrac{1}{(1+t)^2}$

Substituting $t = K^{\cos^{-1} x}$ back into the equation:

$\dfrac{dy}{dt} = \dfrac{1}{\left(1 + K^{\cos^{-1} x}\right)^2}$

Answer: $\frac{1}{\left(1+\mathrm{K}^{\Large \cos ^{-1} x}\right)^2}$

</details>

---

### Q17. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x=\log t, t>0$ and $\mathrm{y}=\frac{1}{\mathrm{t}}$ then $\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2}=$

**Options:**

- **(A)** $\frac{\mathrm{dy}}{\mathrm{d} x}$
- **(B)** $\frac{-\mathrm{dy}}{\mathrm{d} x}$
- **(C)** 2y
- **(D)** $\frac{\mathrm{y}}{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-\mathrm{dy}}{\mathrm{d} x}$**

**Detailed Solution:**

Given $x = \log t \Rightarrow t = e^x$

Also $y = \dfrac{1}{t} \Rightarrow y = \dfrac{1}{e^x} = e^{-x}$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = -e^{-x}$

Differentiating again with respect to $x$:

$\dfrac{d^2 y}{dx^2} = -(-e^{-x}) = e^{-x}$

From the first derivative, we have $e^{-x} = -\dfrac{dy}{dx}$

Therefore, $\dfrac{d^2 y}{dx^2} = -\dfrac{dy}{dx}$

Answer: $\frac{-\mathrm{dy}}{\mathrm{d} x}$

</details>

---

### Q18. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $x=\sin \theta, y=\sin ^3 \theta$, then $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}$ at $\theta=\frac{\pi}{2}$ is

**Options:**

- **(A)** 0
- **(B)** 2
- **(C)** 3
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 6**

**Detailed Solution:**

Given $x = \sin \theta$ and $y = \sin^3 \theta$

Substituting $x$ in the equation for $y$, we get $y = x^3$

Differentiating with respect to $x$:

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = 3x^2$

Differentiating again with respect to $x$:

$\dfrac{\mathrm{d}^2y}{\mathrm{d}x^2} = 6x$

At $\theta = \dfrac{\pi}{2}$, $x = \sin \dfrac{\pi}{2} = 1$

Substituting $x = 1$:

$\dfrac{\mathrm{d}^2y}{\mathrm{d}x^2} = 6(1) = 6$

Answer: 6

</details>

---

### Q19. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x=2 \cos \theta-\cos 2 \theta$ and $y=2 \sin \theta-\sin 2 \theta$, then $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}$ is equal to

**Options:**

- **(A)** $\frac{3}{2} \tan \frac{3 \theta}{2}$
- **(B)** $\frac{3}{2} \sec \frac{3 \theta}{2} \tan \frac{3 \theta}{2}$
- **(C)** $\frac{3}{8} \sec ^3 \frac{3 \theta}{2} \csc \frac{\theta}{2}$
- **(D)** $\sec ^2 \frac{3 \theta}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{8} \sec ^3 \frac{3 \theta}{2} \csc \frac{\theta}{2}$**

**Detailed Solution:**

Given $x = 2 \cos \theta - \cos 2 \theta$ and $y = 2 \sin \theta - \sin 2 \theta$.

Differentiating with respect to $\theta$:

$\dfrac{\mathrm{d}x}{\mathrm{d}\theta} = -2 \sin \theta + 2 \sin 2 \theta = 2(\sin 2 \theta - \sin \theta)$

Using the formula $\sin A - \sin B = 2 \cos\left(\dfrac{A+B}{2}\right) \sin\left(\dfrac{A-B}{2}\right)$:

$\dfrac{\mathrm{d}x}{\mathrm{d}\theta} = 4 \cos\left(\dfrac{3\theta}{2}\right) \sin\left(\dfrac{\theta}{2}\right)$

$\dfrac{\mathrm{d}y}{\mathrm{d}\theta} = 2 \cos \theta - 2 \cos 2 \theta = 2(\cos \theta - \cos 2 \theta)$

Using the formula $\cos A - \cos B = 2 \sin\left(\dfrac{A+B}{2}\right) \sin\left(\dfrac{B-A}{2}\right)$:

$\dfrac{\mathrm{d}y}{\mathrm{d}\theta} = 4 \sin\left(\dfrac{3\theta}{2}\right) \sin\left(\dfrac{\theta}{2}\right)$

Now, $\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{\dfrac{\mathrm{d}y}{\mathrm{d}\theta}}{\dfrac{\mathrm{d}x}{\mathrm{d}\theta}} = \dfrac{4 \sin\left(\dfrac{3\theta}{2}\right) \sin\left(\dfrac{\theta}{2}\right)}{4 \cos\left(\dfrac{3\theta}{2}\right) \sin\left(\dfrac{\theta}{2}\right)} = \tan\left(\dfrac{3\theta}{2}\right)$

Differentiating again with respect to $x$:

$\dfrac{\mathrm{d}^2 y}{\mathrm{d}x^2} = \dfrac{\mathrm{d}}{\mathrm{d}\theta} \left( \tan\left(\dfrac{3\theta}{2}\right) \right) \cdot \dfrac{\mathrm{d}\theta}{\mathrm{d}x}$

$\dfrac{\mathrm{d}^2 y}{\mathrm{d}x^2} = \dfrac{3}{2} \sec^2\left(\dfrac{3\theta}{2}\right) \cdot \dfrac{1}{4 \cos\left(\dfrac{3\theta}{2}\right) \sin\left(\dfrac{\theta}{2}\right)}$

$\dfrac{\mathrm{d}^2 y}{\mathrm{d}x^2} = \dfrac{3}{8} \sec^3\left(\dfrac{3\theta}{2}\right) \csc\left(\dfrac{\theta}{2}\right)$

Answer: $\frac{3}{8} \sec ^3 \frac{3 \theta}{2} \csc \frac{\theta}{2}$

</details>

---

### Q20. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $(a+\sqrt{2} b \cos x)(a-\sqrt{2} b \cos y)=a^2-b^2$, where $\mathrm{a}\gt\mathrm{b}\gt0$, then $\frac{\mathrm{d} x}{\mathrm{~d} y}$ at $\left(\frac{\pi}{4}, \frac{\pi}{4}\right)$ is

**Options:**

- **(A)** $\frac{a-b}{a+b}$
- **(B)** $\frac{a+b}{a-b}$
- **(C)** $\frac{2 a+b}{2 a-b}$
- **(D)** $\frac{a-2 b}{a+2 b}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{a+b}{a-b}$**

**Detailed Solution:**

Given equation: $(a+\sqrt{2} b \cos x)(a-\sqrt{2} b \cos y)=a^2-b^2$

Differentiating both sides with respect to $y$ using the product rule:

$(a+\sqrt{2} b \cos x)(\sqrt{2} b \sin y) + (a-\sqrt{2} b \cos y)\left(-\sqrt{2} b \sin x \dfrac{dx}{dy}\right) = 0$

Substitute $x = \dfrac{\pi}{4}$ and $y = \dfrac{\pi}{4}$:

$\cos\left(\dfrac{\pi}{4}\right) = \dfrac{1}{\sqrt{2}}$ and $\sin\left(\dfrac{\pi}{4}\right) = \dfrac{1}{\sqrt{2}}$

$\left(a+\sqrt{2} b \left(\dfrac{1}{\sqrt{2}}\right)\right)\left(\sqrt{2} b \left(\dfrac{1}{\sqrt{2}}\right)\right) + \left(a-\sqrt{2} b \left(\dfrac{1}{\sqrt{2}}\right)\right)\left(-\sqrt{2} b \left(\dfrac{1}{\sqrt{2}}\right) \dfrac{dx}{dy}\right) = 0$

$(a+b)(b) + (a-b)\left(-b \dfrac{dx}{dy}\right) = 0$

Since $b > 0$, dividing the entire equation by $b$ gives:

$(a+b) - (a-b)\dfrac{dx}{dy} = 0$

$\dfrac{dx}{dy} = \dfrac{a+b}{a-b}$

Answer: $\frac{a+b}{a-b}$

</details>

---

### Q21. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Derivative of $\sin ^2 x$ with respect to $\mathrm{e}^{\cos x}$ is

**Options:**

- **(A)** $2 \sin x \cos ^2 x \mathrm{e}^{\cos x}$
- **(B)** $\dfrac{2 \cos x}{\mathrm{e}^{\cos x}}$
- **(C)** $\dfrac{2 \sin x}{\mathrm{e}^{\cos x}}$
- **(D)** $\dfrac{-2 \cos x}{e^{\cos x}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{-2 \cos x}{e^{\cos x}}$**

**Detailed Solution:**

Let $u = \sin^2 x$ and $v = \mathrm{e}^{\cos x}$

Differentiating $u$ with respect to $x$:

$\dfrac{du}{dx} = 2 \sin x \cos x$

Differentiating $v$ with respect to $x$:

$\dfrac{dv}{dx} = \mathrm{e}^{\cos x} (-\sin x) = -\sin x \mathrm{e}^{\cos x}$

The derivative of $u$ with respect to $v$ is given by:

$\dfrac{du}{dv} = \dfrac{\dfrac{du}{dx}}{\dfrac{dv}{dx}}$

$\dfrac{du}{dv} = \dfrac{2 \sin x \cos x}{-\sin x \mathrm{e}^{\cos x}}$

$\dfrac{du}{dv} = \dfrac{-2 \cos x}{\mathrm{e}^{\cos x}}$

Answer: $\dfrac{-2 \cos x}{e^{\cos x}}$

</details>

---

### Q22. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $y=\left[\mathrm{e}^{4 x}\left(\dfrac{x-4}{x+3}\right)^{\dfrac{3}{4}}\right]$ then $\dfrac{\mathrm{d} y}{\mathrm{~d} x}=$

**Options:**

- **(A)** $\dfrac{\mathrm{d} y}{\mathrm{~d} x}=y\left[4+\dfrac{21}{4(x-4)(x+3)}\right]$
- **(B)** $\dfrac{\mathrm{d} y}{\mathrm{~d} x}=\left[4+\dfrac{21}{4(x-4)(x+3)}\right]$
- **(C)** $\dfrac{\mathrm{d} y}{\mathrm{~d} x}=\dfrac{1}{y}\left[4+\dfrac{21}{4(x-4)(x+3)}\right]$
- **(D)** $\dfrac{\mathrm{d} y}{\mathrm{~d} x}=y\left[4+\dfrac{21}{4(x+4)(x+3)}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\mathrm{d} y}{\mathrm{~d} x}=y\left[4+\dfrac{21}{4(x-4)(x+3)}\right]$**

**Detailed Solution:**

Given $y = \mathrm{e}^{4x} \left( \dfrac{x-4}{x+3} \right)^{\dfrac{3}{4}}$

Taking natural logarithm on both sides:

$\ln y = \ln \left( \mathrm{e}^{4x} \right) + \dfrac{3}{4} \ln \left( \dfrac{x-4}{x+3} \right)$

$\ln y = 4x + \dfrac{3}{4} \ln(x-4) - \dfrac{3}{4} \ln(x+3)$

Differentiating with respect to $x$:

$\dfrac{1}{y} \dfrac{\mathrm{d}y}{\mathrm{d}x} = 4 + \dfrac{3}{4(x-4)} - \dfrac{3}{4(x+3)}$

$\dfrac{1}{y} \dfrac{\mathrm{d}y}{\mathrm{d}x} = 4 + \dfrac{3}{4} \left[ \dfrac{x+3 - (x-4)}{(x-4)(x+3)} \right]$

$\dfrac{1}{y} \dfrac{\mathrm{d}y}{\mathrm{d}x} = 4 + \dfrac{3}{4} \left[ \dfrac{7}{(x-4)(x+3)} \right]$

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = y \left[ 4 + \dfrac{21}{4(x-4)(x+3)} \right]$

Answer: $\dfrac{\mathrm{d} y}{\mathrm{~d} x}=y\left[4+\dfrac{21}{4(x-4)(x+3)}\right]$

</details>

---

### Q23. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x^2+y^2=\mathrm{t}+\frac{1}{\mathrm{t}}$ and $x^4+y^4=\mathrm{t}^2+\frac{1}{\mathrm{t}^2}$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}$ is equal to

**Options:**

- **(A)** $\frac{y}{x}$
- **(B)** $\frac{-y}{x}$
- **(C)** $\frac{x}{y}$
- **(D)** $\frac{-x}{y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-y}{x}$**

**Detailed Solution:**

$x^2+y^2=\mathrm{t}+\frac{1}{\mathrm{t}}$
Squaring on both sides, we get
$x^4+y^4+2 x^2 y^2=t^2+\frac{1}{t^2}+2$
$\begin{aligned} \therefore \quad \mathrm{t}^2+\frac{1}{\mathrm{t}^2}+2 x^2 y^2=\mathrm{t}^2 & +\frac{1}{\mathrm{t}^2}+2 \\ & \ldots\left[\because x^4+y^4=\mathrm{t}^2+\frac{1}{\mathrm{t}^2}, \text { given }\right]\end{aligned}$
$\begin{aligned}
& 2 x^2 y^2=2 \\
& x^2 y^2=1
\end{aligned}$
differentiating w.r.t. $x$, we get
$\begin{aligned}
& x^2 2 y \frac{\mathrm{d} y}{\mathrm{~d} x}+2 x y^2=0 \\
& x^2 2 y \frac{\mathrm{d} y}{\mathrm{~d} x}=-2 x y^2 \\
& \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{-2 x y^2}{2 x^2 y}=\frac{-y}{x}
\end{aligned}$

</details>

---

### Q24. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $x=\cos ^{-1}\left(\frac{1}{\sqrt{1+t^2}}\right), y=\sin ^{-1}\left(\frac{1}{\sqrt{1+t^2}}\right)$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}$ is

**Options:**

- **(A)** $0$
- **(B)** $\frac{\sin t}{\cos t}$
- **(C)** 1
- **(D)** $\sin t \cdot \cos t$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

let $t=\tan \theta$, then
$\begin{aligned} & x=\cos ^{-1}\left(\frac{1}{\sqrt{1+\tan ^2 \theta}}\right)=\cos ^{-1}\left(\frac{1}{\sec \theta}\right)=\cos ^{-1} \cos \theta=\theta \\ & y=\sin ^{-1}\left(\frac{\tan \theta}{\sqrt{1+\tan ^2 \theta}}\right)=\sin ^{-1}\left(\frac{\tan \theta}{\sec \theta}\right)=\sin ^{-1} \sin \theta=\theta \\ & \Rightarrow \frac{d y}{d x}=\frac{d(\theta)}{d \theta}=1\end{aligned}$

</details>

---

### Q25. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $x=t+\frac{1}{t}$ and $y=t-\frac{1}{t}$, the $\frac{\mathrm{d} y}{\mathrm{~d} x}=$

**Options:**

- **(A)** $\frac{1-t^2}{1+t^2}$
- **(B)** $\frac{t^2+1}{t^2-1}$
- **(C)** $\frac{1+t^2}{1-t^2}$
- **(D)** $\frac{t^2-1}{t^2+1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{t^2+1}{t^2-1}$**

**Detailed Solution:**

$\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{\frac{\mathrm{d} y}{\mathrm{~d} t}}{\frac{\mathrm{d} x}{\mathrm{~d} t}}=\frac{1+\frac{1}{t^2}}{1-\frac{1}{t^2}}=\frac{t^2+1}{t^2-1}$

</details>

---

### Q26. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $x=\sqrt{a^{\sin ^{-1} t}}$ and $y=\sqrt{a^{\cos ^{-1} t}}$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}=$

**Options:**

- **(A)** $\frac{y}{x}$
- **(B)** $\frac{-x}{y}$
- **(C)** $\frac{x}{y}$
- **(D)** $-\frac{y}{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\frac{y}{x}$**

**Detailed Solution:**

$\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{\frac{\mathrm{d} \sqrt{a^{\cos ^{-1} t}}}{\mathrm{dt}}}{\frac{\mathrm{d} \sqrt{a^{\sin ^{-1} t}}}{\mathrm{~d} t}}=\frac{\frac{1}{2 \sqrt{a^{\cos ^{-1} t}}} \cdot a^{\cos ^{-1} t} \cdot \log a \cdot \frac{-1}{\sqrt{1-t^2}}}{\frac{1}{2 \sqrt{a^{\sin ^{-1} t}}} \cdot a^{\sin ^{-1}} \cdot \log a \cdot \frac{1}{\sqrt{1-t^2}}}=\frac{-\sqrt{a^{\cos ^{-1} t}}}{\sqrt{a^{\sin ^{-1} t}}}=\frac{-y}{x}$

</details>

---

### Q27. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $x=\sec \theta-\cos \theta$ and $y=\sec ^n \theta-\cos ^n \theta$, then $\left(\frac{d y}{d x}\right)^2$ is equal to

**Options:**

- **(A)** $\frac{\mathrm{n}^2\left(\mathrm{y}^2-4\right)}{\mathrm{x}^2}$
- **(B)** $\frac{\mathrm{n}^2\left(\mathrm{y}^2+4\right)}{\mathrm{x}^2+4}$
- **(C)** $\frac{n^2 y^2}{x^2}-4$
- **(D)** $\frac{\mathrm{n}^2\left(\mathrm{y}^2-4\right)}{\mathrm{x}^2-4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\mathrm{n}^2\left(\mathrm{y}^2+4\right)}{\mathrm{x}^2+4}$**

**Detailed Solution:**

$\begin{aligned} & =\left(\frac{d y}{d x}\right)^2=\left(\frac{\frac{d y}{d \theta}}{\frac{d x}{d \theta}}\right)^2=\left\{\frac{\frac{d\left(\sec ^n \theta-\cos ^n \theta\right)}{d \theta}}{\frac{d(\sec \theta-\cos \theta)}{d \theta}}\right\}^2 \\ & =\left\{\frac{n \sec ^{\mathrm{n}-1} \theta \cdot \sec \theta \cdot \tan \theta-\mathrm{n} \cos ^{\mathrm{n}-1} \theta \cdot(-\sin \theta)}{\sec \theta \cdot \tan \theta-(-\sin \theta)}\right\}^2 \\ & =\left\{\frac{\mathrm{n} \sec ^{\mathrm{n}} \theta \cdot \tan \theta+\mathrm{n} \cos ^{\mathrm{n}} \theta \cdot \tan \theta}{\sec \theta \cdot \tan \theta+\cos \theta \cdot \tan \theta}\right\}^2 \\ & =\left\{\frac{n \tan \theta\left(\sec ^n \theta+\cos ^n \theta\right.}{\tan \theta(\sec \theta+\cos \theta)}\right\}^2 \\ & =\frac{\mathrm{n}^2\left(\sec ^{\mathrm{n}} \theta+\cos ^{\mathrm{n}} \theta\right)^2}{(\sec \theta+\cos \theta)^2} \\ & \end{aligned}$
$=\frac{\mathrm{n}^2\left[\mathrm{y}^2+4\right]}{\mathrm{x}^2+4}$

</details>

---

### Q28. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{x}=\mathrm{e}^{\mathrm{t}}(\sin \mathrm{t}-\cos \mathrm{t})$ and $\mathrm{y}=\mathrm{e}^{\mathrm{t}}(\sin \mathrm{t}+\cos \mathrm{t})$, then $\frac{\mathrm{dy}}{\mathrm{dx}}$ at $\mathrm{t}=\frac{\pi}{3}$ is

**Options:**

- **(A)** $\sqrt{3}$
- **(B)** $\frac{1}{\sqrt{3}}$
- **(C)** $\frac{\sqrt{3}}{2}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{\sqrt{3}}$**

**Detailed Solution:**

$\begin{aligned} & x=e^t(\sin t-\cos t) \text { and } y=e^t(\sin t+\cos t) \\ & \therefore \quad \frac{d x}{d t}=e^t(\sin t-\cos t)+e^t(\cos t+\sin t)=2 e^t \sin t \\ & \frac{d y}{d t}=e^t(\sin t+\cos t)+e^t(\cos t-\sin t)=2 e^t \sin t \\ & \therefore \quad \frac{d y}{d x}=\frac{2 e^t \cos t}{2 e^t \sin t} \Rightarrow\left(\frac{d y}{d x}\right)_{t=\frac{\pi}{3}}=\cot \left(\frac{\pi}{3}\right)=\frac{1}{\sqrt{3}} \\ & \end{aligned}$

</details>

---

### Q29. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $x=a(\theta+\sin \theta)$ and $y=a(1-\cos \theta)$ then $\left(\frac{d^2 y}{dx^2}\right)_{a t \theta=\pi / 2}=$

**Options:**

- **(A)** $\frac{a}{2}$
- **(B)** $\frac{1}{\mathrm{a}}$
- **(C)** a
- **(D)** 2a

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{\mathrm{a}}$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{x}=\mathrm{a}(\theta+\sin \theta) \text { and } \mathrm{y}=\mathrm{a}(1-\cos \theta) \\ & \therefore \quad \frac{d x}{d \theta}=a(1+\cos \theta) \text { and } \frac{d y}{d \theta}=a(\sin \theta) \\ & \therefore \quad \frac{d y}{d x}=\frac{a \sin \theta}{a(1+\cos \theta)}=\frac{\sin \theta}{1+\cos \theta} \\ & \therefore \quad \frac{d^2 y}{d x^2}=\frac{d}{d \theta}\left(\frac{d y}{d x}\right)\left(\frac{d \theta}{d x}\right)=\frac{d}{d \theta}\left(\frac{\sin \theta}{1+\cos \theta}\right) \times \frac{1}{\left(\frac{d x}{d \theta}\right)} \\ & =\frac{(1+\cos \theta)(\cos \theta)-\sin \theta(-\sin \theta)}{(1+\cos \theta)^2 \mathrm{a}(1+\cos \theta)} \\ & =\frac{\cos \theta+\cos ^2 \theta+\sin ^2 \theta}{\mathrm{a}(1+\cos \theta)^3}=\frac{1+\cos \theta}{\mathrm{a}(1+\cos \theta)^3}=\frac{1}{\mathrm{a}(1+\cos \theta)^2} \\ & \therefore \quad\left(\frac{\mathrm{d}^2 y}{\mathrm{dx}^2}\right)_{\theta=\frac{\pi}{2}}=\frac{1}{\mathrm{a}\left(1+\cos \frac{\pi}{2}\right)^2}=\frac{1}{\mathrm{a}} \\ & \end{aligned}$

</details>

---

### Q30. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{x}=\mathrm{a}\left(\mathrm{t}-\frac{1}{\mathrm{t}}\right)$ and $\mathrm{y}=\mathrm{b}\left(\mathrm{t}+\frac{1}{\mathrm{t}}\right)$, then $\frac{\mathrm{dy}}{\mathrm{dx}}=$

**Options:**

- **(A)** $\frac{a^2 x}{b^2 y}$
- **(B)** $\frac{a^2 y}{b^2 x}$
- **(C)** $\frac{-b^2 x}{a^2 y}$
- **(D)** $\frac{b^2 x}{a^2 y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{b^2 x}{a^2 y}$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{x}=\mathrm{a}\left(\mathrm{t}-\frac{1}{\mathrm{t}}\right) \text { and } \mathrm{y}=\mathrm{b}\left(\mathrm{t}+\frac{1}{\mathrm{t}}\right) \\
& \therefore \frac{\mathrm{dx}}{\mathrm{dt}}=\mathrm{a}\left(1+\frac{1}{\mathrm{t}^2}\right) \text { and } \frac{\mathrm{dy}}{\mathrm{dt}}=\mathrm{b}\left(1-\frac{1}{\mathrm{t}^2}\right) \\
& \therefore \frac{\mathrm{dy}}{\mathrm{dx}}=\frac{\mathrm{b}\left(1-\frac{1}{\mathrm{t}^2}\right)}{\mathrm{a}\left(1+\frac{1}{\mathrm{t}^2}\right)}=\left(\frac{\mathrm{b}}{\mathrm{a}}\right)\left(\frac{\mathrm{t}^2-1}{\mathrm{t}^2+1}\right)
\end{aligned}
$$
Now $\mathrm{x}=\mathrm{a}\left(\frac{\mathrm{t}^2-1}{\mathrm{t}}\right)$ and $\mathrm{y}=\mathrm{b}\left(\frac{\mathrm{t}^2+1}{\mathrm{t}}\right)$
...[From (1)]
$$
\therefore\left(\mathrm{t}^2-1\right)=\left(\frac{\mathrm{x}}{\mathrm{a}}\right) \mathrm{t} \text { and }\left(\mathrm{t}^2+1\right)=\left(\frac{\mathrm{y}}{\mathrm{b}}\right)(\mathrm{t})
$$
$\therefore$ Eq. (2) becomes
$$
\frac{d y}{d x}=\left(\frac{b}{a}\right)\left(\frac{x}{a}\right)(t) \times \frac{1}{\left(\frac{y}{b}\right) \times t}=\frac{b^2 x}{a^2 y}
$$

</details>

---

### Q31. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $u=\cos ^3 x, v=\sin ^3 x$, then $\left(\frac{d v}{d u}\right)_{x=\frac{\pi}{4}}$ is equal to

**Options:**

- **(A)** -2
- **(B)** 2
- **(C)** 1
- **(D)** -1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -1**

**Detailed Solution:**

$\begin{aligned} & u=\cos ^3 x, v=\sin ^3 x \\ & \therefore \frac{d u}{d x}=3 \cos ^2 x(-\sin x) \text { and } \frac{d v}{d x}=3 \sin ^2 x(\cos x) \\ & \therefore \frac{d v}{d u}=\frac{3 \sin ^2 x \cos x}{-3 \sin x \cos ^2 x}=-\tan x \\ & \therefore\left(\frac{d v}{d u}\right)_{x=\frac{\pi}{4}}=-\tan \left(\frac{\pi}{4}=-1\right)\end{aligned}$

</details>

---

### Q32. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x=\frac{1-t^2}{1+t^2}$ and $y=\frac{2 a t}{1+t^2}$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{\mathrm{a}\left(\mathrm{t}^2+1\right)}{2 \mathrm{t}}$
- **(B)** $\frac{a\left(t^2-1\right)}{t}$
- **(C)** $\frac{a\left(1-t^2\right)}{2 t}$
- **(D)** $\frac{a\left(t^2-1\right)}{2 t}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{a\left(t^2-1\right)}{2 t}$**

**Detailed Solution:**

We have $\mathrm{x}=\frac{1-\mathrm{t}^2}{1+\mathrm{t}^2}$ and $\mathrm{y}=\frac{2 \mathrm{at}}{1+\mathrm{t}^2}$
Put $\mathrm{t}=\tan \theta \Rightarrow \mathrm{x}=\cos 2 \theta$ and $\mathrm{y}=\mathrm{a} \sin 2 \theta$
$$
\frac{d x}{d \theta}=-2 \sin 2 \theta \text { and } \frac{d y}{d \theta}=2 a \cos 2 \theta
$$
$$
\therefore \frac{d y}{d x}=\frac{2 a \cos 2 \theta}{-2 \sin 2 \theta}=\frac{-a}{\tan 2 \theta}=\frac{-a}{\left(\frac{2 \tan \theta}{1-\tan ^2 \theta}\right)}
$$
$$
=\frac{-\mathrm{a}}{\left(\frac{2 \mathrm{t}}{1-\mathrm{t}^2}\right)}=\frac{-\mathrm{a}\left(1-\mathrm{t}^2\right)}{2 \mathrm{t}}=\frac{\mathrm{a}\left(\mathrm{t}^2-1\right)}{2 \mathrm{t}}
$$

</details>

---

### Q33. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $x=a(t+\sin t), y=a(1-\cos t)$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\tan \frac{t}{2}$
- **(B)** $-\frac{t}{2} \tan t$
- **(C)** $\frac{1}{2} \tan t$
- **(D)** $-\tan \frac{t}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\tan \frac{t}{2}$**

**Detailed Solution:**

$$
\begin{aligned}
& x=a(t+\sin t) \text { and } y=a(1-\cos t) \\
& \therefore \frac{d x}{d t}=a(1+\cos t) \text { and } \frac{d y}{d t}=a(\sin t) \\
& \therefore \frac{d y}{d x}=\frac{\left(\frac{d y}{d t}\right)}{\left(\frac{d x}{d t}\right)}=\frac{a \sin t}{a(1+\cos t)}=\frac{2 \sin \frac{t}{2} \cos \frac{t}{2}}{2 \cos ^2 \frac{t}{2}}=\tan \frac{t}{2}
\end{aligned}
$$

</details>

---

### Q34. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $x=a \cos \theta, y=b \sin \theta$, then $\left[\frac{d^2 y}{d x^2}\right]_{\theta=\frac{\pi}{4}}=$

**Options:**

- **(A)** $2\left(\frac{\mathrm{a}^2}{\mathrm{~b}}\right)$
- **(B)** $\sqrt{2}\left(\frac{\mathrm{a}^2}{\mathrm{~b}}\right)$
- **(C)** $-2 \sqrt{2}\left(\frac{b}{a^2}\right)$
- **(D)** $2 \sqrt{2}\left(\frac{\mathrm{b}}{\mathrm{a}^2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-2 \sqrt{2}\left(\frac{b}{a^2}\right)$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{x}=\mathrm{a} \cos \theta, \mathrm{y}=\mathrm{b} \sin \theta \\ & \therefore \frac{\mathrm{dx}}{\mathrm{d} \theta}=-\mathrm{a} \sin \theta, \frac{\mathrm{dx}}{\mathrm{d} \theta}=\mathrm{b} \cos \theta \\ & \therefore \frac{\mathrm{dy}}{\mathrm{dx}}=\frac{\mathrm{b} \cos \theta}{-\mathrm{a} \sin \theta}=\left(\frac{-\mathrm{b}}{\mathrm{a}}\right) \cot \theta \\ & \therefore \frac{\mathrm{d}^2}{\mathrm{dx}}=\frac{\mathrm{d}}{\mathrm{dx}}\left(\frac{\mathrm{dy}}{\mathrm{dx}}\right)=\frac{\mathrm{d}}{\mathrm{d} \theta}\left(\frac{\mathrm{dy}}{\mathrm{dx}}\right) \cdot \frac{\mathrm{d} \theta}{\mathrm{dx}} \\ & =\frac{\mathrm{d}}{\mathrm{d} \theta}\left[\left(\frac{-\mathrm{b}}{2}\right) \cot \theta\right] \times \frac{1}{\left(\frac{\mathrm{dx}}{\mathrm{d} \theta}\right)} \\ & =\frac{\left(\frac{-\mathrm{b}}{\mathrm{a}}\right)\left(-\operatorname{cosec}{ }^2 \theta\right)}{-\mathrm{a} \sin \theta}=\left(\frac{-\mathrm{b}}{\mathrm{a}}\right) \times \frac{1}{\mathrm{a}} \times \frac{1}{\sin ^3 \theta} \\ & \therefore\left(\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{dx}}\right)_{\theta=\frac{\pi}{4}}=\left(\frac{-\mathrm{b}}{\mathrm{a}^2}\right)\left[\frac{1}{\left(\sin \frac{\pi}{4}\right)^3}\right]=\left(\frac{-\mathrm{b}}{\mathrm{a}^2}\right)(\sqrt{2})^3=2 \sqrt{2}\left(\frac{\mathrm{b}}{\mathrm{a}^2}\right)\end{aligned}$

</details>

---

### Q35. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x^{2}+y^{2}=t+\frac{1}{t}, x^{4}+y^{4}=t^{2}+\frac{1}{t^{2}}$ then $\frac{d y}{d x}=$

**Options:**

- **(A)** $-\frac{y}{x}$
- **(B)** $\frac{y}{x}$
- **(C)** $\frac{x}{2 y}$
- **(D)** $-\frac{x}{2 y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\frac{y}{x}$**

**Detailed Solution:**

(A)
We have,
$x^{2}+y^{2}=t+\frac{1}{t}$$\cdots$ (1) $\quad$ and $\quad x^{4}+y^{4}=t^{2}+\frac{1}{t^{2}}$...(2)
Squaring (1), we get
$\begin{array}{l}
x^{4}+y^{4}+2 x^{2} y^{2}=t^{2}+\frac{1}{t^{2}}+2 \Rightarrow x^{4}+y^{4}+2 x^{2} y^{2}=x^{4}+y^{4}+2 \text {..(from (2)) } \\
\therefore x^{2} y^{2}=1
\end{array}$
Differentiating w.r.t. $x$, we get
$\begin{aligned}
& x^{2}\left(2 y \frac{d y}{d x}\right)+y^{2}(2 x)=0 \\
\therefore & \frac{d y}{d x}=\frac{-2 x y^{2}}{2 x^{2} y}=\frac{-y}{x}
\end{aligned}$

</details>

---

### Q36. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y=1+x+\frac{x^{2}}{2 !}+\frac{x^{3}}{3 !}+\ldots \ldots$ then $\frac{d y}{d x}=$

**Options:**

- **(A)** $y-1$
- **(B)** $y+1$
- **(C)** $y^{2}-1$
- **(D)** $y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y$**

**Detailed Solution:**

Given
$$
\begin{aligned}
& y=1+x+\frac{x^{2}}{2 !}+\frac{x^{3}}{3 !}+\ldots \\
\therefore & \frac{d y}{d x}=e^{x}=y
\end{aligned} \quad \Rightarrow y=e^{x}
$$

</details>

---

### Q37. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan u=\sqrt{\frac{1-x}{1+x}}, \cos v=4 x^{3}-3 x$, then $\frac{d u}{d v}=$

**Options:**

- **(A)** $\frac{1}{6}$
- **(B)** 1
- **(C)** 2
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{6}$**

**Detailed Solution:**

Given $\tan u=\sqrt{\frac{1-x}{1+x}}$
Put $x=\cos \theta \Rightarrow \theta=\cos ^{-1} x$
Now, $\tan u=\sqrt{\frac{1-\cos \theta}{1+\cos \theta}}=\sqrt{\frac{2 \sin ^{2} \frac{\theta}{2}}{2 \cos ^{2} \frac{\theta}{2}}}=\tan \frac{\theta}{2}$
$\therefore \mathrm{u}=\frac{1}{2} \theta \Rightarrow \mathrm{u}=\frac{1}{2} \cos ^{-1} \mathrm{x}$
$\therefore \frac{\mathrm{du}}{\mathrm{dx}}=\frac{-1}{2 \sqrt{1-\mathrm{x}^{2}}}$
We have $\cos v=4 x^{3}-3 x$
Put $x=\cos \theta$
$\cos v=4 \cos ^{3} \theta-3 \cos \theta$
$\cos \mathrm{v}=\cos 3 \theta \Rightarrow \mathrm{v}=3 \theta$
$\therefore v=3 \cos ^{-1} x$
$\therefore \frac{\mathrm{dv}}{\mathrm{dx}}=\frac{-3}{\sqrt{1-\mathrm{x}^{2}}}$
$\therefore \frac{\mathrm{du}}{\mathrm{dv}}=\frac{\left(\frac{\mathrm{du}}{\mathrm{dx}}\right)}{\left(\frac{\mathrm{dv}}{\mathrm{dx}}\right)}=\frac{-1}{2 \sqrt{1-\mathrm{x}^{2}}} \times \frac{\sqrt{1-\mathrm{x}^{2}}}{-3}=\frac{1}{6}$

</details>

---

### Q38. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>x</mi><mo>=</mo><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>t</mi></mrow></mrow></mrow></msup></msqrt><mo>,</mo><mi></mi><mi>y</mi><mo>=</mo><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>t</mi></mrow></mrow></mrow></msup></msqrt><mo>,</mo></math> then <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo></math> ………

**Options:**

- **(A)** <math><mfrac><mrow><mo>-</mo><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mo>-</mo><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mo>-</mo><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></math>**

**Detailed Solution:**

If <math><mi>x</mi><mo>=</mo><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi></mrow></msup></msqrt><mi>y</mi><mo>=</mo><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><msup><mrow><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi></mrow></msup></msqrt></math>  
Then, <math><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi><mo>=</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mrow><mi mathvariant="normal">g</mi></mrow><mrow><mi>a</mi></mrow></msub><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math> and <math><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><msup><mrow><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi><mo>=</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mrow><mi mathvariant="normal">g</mi></mrow><mrow><mi>a</mi></mrow></msub><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></math>  
Then, <math><mfrac><mrow><mn>2</mn></mrow><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mrow><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mi>a</mi></mrow></mfrac><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mrow><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mi>x</mi><mo>+</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mrow><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mi>y</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>  
Differentiate both sides w.r.t. <math><mi>x</mi></math>  
We get, <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>a</mi><mi mathvariant="normal"></mi><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></math>

</details>

---

### Q39. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>x</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>θ</mi></mrow></msup><mfenced separators="|"><mrow><mi>s</mi><mi>i</mi><mi>n</mi><mi>θ</mi><mo>-</mo><mi>c</mi><mi>o</mi><mi>s</mi><mi>θ</mi></mrow></mfenced></math> , <math><mi>y</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>θ</mi></mrow></msup><mi mathvariant="normal"> </mi><mfenced separators="|"><mrow><mi>s</mi><mi>i</mi><mi>n</mi><mi>θ</mi><mo>+</mo><mi>c</mi><mi>o</mi><mi>s</mi><mi>θ</mi></mrow></mfenced></math> then <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math> at <math><mi>θ</mi><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math> is

**Options:**

- **(A)** <math><mn>1</mn></math>
- **(B)** <math><mn>0</mn></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(D)** <math><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>1</mn></math>**

**Detailed Solution:**

<math> <mrow> <mfrac> <mrow> <mtext>dx</mtext> </mrow> <mrow> <mtext>d</mtext> <mi>θ</mi> </mrow> </mfrac> <mo>=</mo> <msup> <mtext>e</mtext> <mi>θ</mi> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mtext>cos</mtext> <mi>θ</mi> <mo>+</mo> <mtext>sin</mtext> <mi>θ</mi> </mrow> </mfenced> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mtext>sin</mtext> <mi>θ</mi> <mo>-</mo> <mtext>cos</mtext> <mi>θ</mi> </mrow> </mfenced> <msup> <mtext>e</mtext> <mi>θ</mi> </msup> <mo>=</mo> <mn>2</mn> <msup> <mtext>e</mtext> <mi>θ</mi> </msup> <mtext>sin</mtext> <mi>θ</mi> </mrow> </math>
<math> <mrow> <mfrac> <mrow> <mtext>dy</mtext> </mrow> <mrow> <mtext>d</mtext> <mi>θ</mi> </mrow> </mfrac> <mo>=</mo> <msup> <mtext>e</mtext> <mi>θ</mi> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mtext>cos</mtext> <mi>θ</mi> <mo>-</mo> <mtext>sin</mtext> <mi>θ</mi> </mrow> </mfenced> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mtext>sin</mtext> <mi>θ</mi> <mo>+</mo> <mtext>cos</mtext> <mi>θ</mi> </mrow> </mfenced> <msup> <mtext>e</mtext> <mi>θ</mi> </msup> <mo>=</mo> <mn>2</mn> <msup> <mtext>e</mtext> <mi>θ</mi> </msup> <mtext>cos</mtext> <mi>θ</mi> </mrow> </math>
<math> <mrow> <mfrac> <mrow> <mtext>dy</mtext> </mrow> <mrow> <mtext>dx</mtext> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mfrac> <mrow> <mtext>dy</mtext> </mrow> <mrow> <mtext>d</mtext> <mi>θ</mi> </mrow> </mfrac> </mrow> <mrow> <mfrac> <mrow> <mtext>dx</mtext> </mrow> <mrow> <mtext>d</mtext> <mi>θ</mi> </mrow> </mfrac> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <msup> <mtext>2e</mtext> <mi>θ</mi> </msup> <mtext>cos</mtext> <mi>θ</mi> </mrow> <mrow> <msup> <mtext>2e</mtext> <mi>θ</mi> </msup> <mtext>sin</mtext> <mi>θ</mi> </mrow> </mfrac> <mo>=</mo> <mtext>cot</mtext> <mi>θ</mi> </mrow> </math>
<math> <mrow> <mfrac> <mrow> <mtext>dy</mtext> </mrow> <mrow> <mtext>dx</mtext> </mrow> </mfrac> <msub> <mo>|</mo> <mrow> <mi>θ</mi> <mo>=</mo> <mfrac> <mrow> <mi>π</mi> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </msub> <mo>=</mo> <mtext>cot</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mi>π</mi> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </mfenced> <mo>=</mo> <mn>1</mn> </mrow> </math>
<math> <mrow> <mfrac> <mrow> <mtext>dy</mtext> </mrow> <mrow> <mtext>dx</mtext> </mrow> </mfrac> <mo>=</mo> <mn>1</mn> </mrow> </math>

</details>

---

### Q40. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>x</mi><mo>=</mo><mi>a</mi><mfenced separators="|"><mrow><mi>t</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>t</mi></mrow></mfrac></mrow></mfenced><mo>,</mo><mi> </mi><mi>y</mi><mo>=</mo><mi>a</mi><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>t</mi></mrow></mfrac></mrow></mfenced></math> where <math><mi>t</mi></math> be the parameter then <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>?</mo></math>

**Options:**

- **(A)** <math><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mo>-</mo><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mo>-</mo><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>x</mi><mo>=</mo><mi>a</mi><mfenced separators="|"><mrow><mi>t</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>t</mi></mrow></mfrac></mrow></mfenced><mo>,</mo><mi> </mi><mi> </mi><mi> </mi><mi>y</mi><mo>=</mo><mi>a</mi><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>t</mi></mrow></mfrac></mrow></mfenced></math> 
 <math><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>t</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mi>t</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>t</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math> 
 <math><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></math> 
Differentiate w.r.t. x
 <math><mn>2</mn><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>2</mn><mi>x</mi><mo>=</mo><mn>0</mn></math> 
 <math><mo>∴</mo><mi> </mi><mi> </mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac></math>

</details>

---

### Q41. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `1`

If $\tan x=\frac{2 t}{1-t^{2}}$ and $\sin y=\frac{2 t}{1+t^{2}}$, then the value of $\frac{d y}{d x}$ is

**Options:**

- **(A)** 1
- **(B)** $t$
- **(C)** $\frac{1}{1-t}$
- **(D)** $\frac{1}{1+t}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

Given, $\tan x=\frac{2 t}{1-t^{2}}$ and $\sin y=\frac{2 t}{1+t^{2}}$
Now, $x=\tan ^{-1}\left(\frac{2 t}{1-t^{2}}\right)$
$x=2 \tan ^{-1} t$..(i)
and $\quad y=\sin ^{-1}\left(\frac{2 t}{1+t^{2}}\right)$
$y=2 \tan ^{-1} t$...(ii)
From Eq. (i), $\frac{d x}{d t}=\frac{2}{1+t^{2}}$
From Eq. (ii), $\frac{d y}{d t}=\frac{2}{1+t^{2}}$
$\therefore \frac{d y}{d x}=\frac{d y}{d t} \times \frac{d t}{d x}=\frac{2}{\left(1+t^{2}\right)} \times \frac{\left(1+t^{2}\right)}{2}=1$

</details>

---

### Q42. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

If $x=2 \cos t-\cos 2 t, \quad y=2 \sin t-\sin 2 t$, then
the value of $\left.\frac{d^{2} y}{d x^{2}}\right|_{t=\pi / 2}$ is

**Options:**

- **(A)** $3 / 2$
- **(B)** $5 / 2$
- **(C)** $5 / 2$
- **(D)** $-3 / 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-3 / 2$**

**Detailed Solution:**

$\frac{d x}{d t}=-2 \sin t+2 \sin 2 t$
$$
\begin{aligned}
\frac{d y}{d t} &=2 \cos t-2 \cos 2 t \\
\therefore \quad \frac{d y}{d x} &=\frac{2 \cos t-2 \cos 2 t}{-2 \sin t+2 \sin 2 t} \\
&=\frac{\cos t-\cos 2 t}{\sin 2 t-\sin t} \\
&=\frac{2 \sin \frac{3 t}{2} \cdot \sin \frac{t}{2}}{2 \cos \frac{3 t}{2} \cdot \sin \frac{t}{2}} \\
&=\tan \frac{3 t}{2}
\end{aligned}
$$
$\begin{aligned} \frac{d^{2} y}{d x^{2}} &=\sec ^{2} \frac{3 t}{2} \cdot \frac{3}{2} \cdot \frac{d t}{d x} \\ &=\frac{3}{2} \sec ^{2} \frac{3 t}{2} \frac{1}{(2 \sin 2 t-2 \sin t)} \\ \Rightarrow \quad &\left.\frac{d^{2} y}{d x^{2}}\right|_{t=\pi / 2}=-3 / 2 \end{aligned}$

</details>

---

### Q43. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

If $x=\sec \theta, y=\tan \theta$, then the value of $\frac{d^{2} y}{d x^{2}}$ at
$\theta=\frac{\pi}{4}$ is

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** $-1$
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-1$**

**Detailed Solution:**

Given, $\begin{aligned} x &=\sec \theta, y=\tan \theta \\ \frac{d x}{d \theta} &=\sec \theta \tan \theta, \frac{d y}{d \theta}=\sec ^{2} \theta \\ \therefore \quad \frac{d y}{d x} &=\frac{\sec ^{2} \theta}{\sec \theta \tan \theta}=\operatorname{cosec} \theta \\ \text { Now, } \frac{d^{2} y}{d x^{2}} &=\frac{d}{d x}\left(\frac{d y}{d x}\right) \\ &=\frac{d}{d \theta}(\operatorname{cosec} \theta) \frac{d \theta}{d x} \\ &=-\operatorname{cosec} \theta \cot \theta \times \frac{1}{\sec 0 \tan 0} \\ &=-\frac{1}{\tan ^{3} \theta} \\ \text { At } \theta=\frac{\pi}{4}, &\left(\frac{d^{2} y}{d x^{2}}\right)_{\theta=\frac{\pi}{4}}=-\frac{1}{\left(\tan \frac{\pi}{4}\right)^{3}}=-1 \end{aligned}$

</details>

---

### Q44. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

Find $\frac{d y}{d x}$, if $x=2 \cos \theta-\cos 2 \theta$ and
$y=2 \sin \theta-\sin 2 \theta .$

**Options:**

- **(A)** $\tan \frac{3 \theta}{2}$
- **(B)** $-\tan \frac{3 \theta}{2}$
- **(C)** $\cot \frac{3 \theta}{2}$
- **(D)** $-\cot \frac{3 \theta}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\tan \frac{3 \theta}{2}$**

**Detailed Solution:**

Given, $x=2 \cos \theta-\cos 2 \theta$
and $y=2 \sin \theta-\sin 2 \theta$
$$
\begin{aligned} \frac{d x}{d \theta} &=-2 \sin \theta+2 \sin 2 \theta \\ \text { and } \frac{d y}{d \theta} &=2 \cos \theta-2 \cos 2 \theta \\ \therefore \quad \frac{d y}{d x} &=\frac{2 \cos \theta-2 \cos 2 \theta}{-2 \sin \theta+2 \sin 2 \theta} \\ &=\frac{\cos \theta-\cos 2 \theta}{\sin 2 \theta-\sin \theta} \\ &=\frac{2 \sin \left(\frac{\theta+2 \theta}{2}\right) \sin \left(\frac{2 \theta-\theta}{2}\right)}{2 \cos \left(\frac{\theta+2 \theta}{2}\right) \sin \left(\frac{2 \theta-\theta}{2}\right)} \\ &=\tan \frac{3 \theta}{2} \end{aligned}
$$

</details>

---

### Q45. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

If $x=\frac{1-t^{2}}{1+t^{2}}$ and $y=\frac{2 a t}{1+t^{2}}$, then $\frac{d y}{d x}$ is equal to

**Options:**

- **(A)** $\frac{a\left(1-t^{2}\right)}{2 t}$
- **(B)** $\frac{a\left(t^{2}-1\right)}{2 t}$
- **(C)** $\frac{a\left(t^{2}+1\right)}{2 t}$
- **(D)** $\frac{a\left(t^{2}-1\right)}{t}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{a\left(t^{2}-1\right)}{2 t}$**

**Detailed Solution:**

Given, $x=\frac{1-t^{2}}{1+t^{2}}$ and $y=\frac{2 a t}{1+t^{2}}$
On differentiating w.r.t. $t$, respectively, we get
$$
\begin{aligned}
\frac{d x}{d t} &=\frac{\left(1+t^{2}\right)(0-2 t)-\left(1-t^{2}\right)(0+2 t)}{\left(1+t^{2}\right)^{2}} \\
&=\frac{-4 t}{\left(1+t^{2}\right)^{2}}
\end{aligned}
$$
and $\frac{d y}{d t}=\frac{\left(1+t^{2}\right) 2 a-2 a t(2 t)}{\left(1+t^{2}\right)^{2}}=\frac{2 a\left(1-t^{2}\right)}{\left(1+t^{2}\right)^{2}}$
$\therefore \quad \frac{d y}{d x}=\frac{d y / d t}{d x / d t}=\frac{a\left(1-t^{2}\right)}{-2 t}$
$\Rightarrow \quad \frac{d y}{d x}=\frac{a\left(t^{2}-1\right)}{2 t}$

</details>

---

### Q46. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

If $x=\phi(t), y=\psi(t)$, then $\frac{d^{2} y}{d x^{2}}$ is equal to

**Options:**

- **(A)** $\frac{\phi^{\prime} \psi^{\prime \prime}-\psi^{\prime} \phi^{\prime \prime}}{\left(\phi^{\prime}\right)^{2}}$
- **(B)** $\frac{\phi^{\prime} \psi^{\prime \prime}-\psi^{\prime} \phi^{\prime \prime}}{\left(\phi^{\prime}\right)^{3}}$
- **(C)** $\frac{\phi^{\prime \prime}}{\psi^{\prime \prime}}$
- **(D)** $\frac{\psi^{\prime \prime}}{\phi^{\prime \prime}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\phi^{\prime} \psi^{\prime \prime}-\psi^{\prime} \phi^{\prime \prime}}{\left(\phi^{\prime}\right)^{3}}$**

**Detailed Solution:**

We have, $x=\phi(t), y=\psi(t)$
$$
\begin{array}{l}
\therefore \quad \frac{d y}{d x}=\frac{d y / d t}{d x / d t}=\frac{\psi^{\prime}}{\phi^{\prime}} \\
\Rightarrow \quad \frac{d^{2} y}{d x^{2}}=\frac{d}{d x}\left(\frac{\psi^{\prime}}{\phi^{\prime}}\right)=\frac{d}{d t}\left(\frac{\psi^{\prime}}{\phi^{\prime}}\right) \frac{d t}{d x} \\
=\frac{\phi^{\prime} \psi^{\prime \prime}-\psi^{\prime} \phi^{\prime \prime}}{\left(\phi^{\prime}\right)^{2}} \cdot \frac{1}{\phi^{\prime}}=\frac{\phi^{\prime} \psi^{\prime \prime}-\psi^{\prime} \phi^{\prime \prime}}{\left(\phi^{\prime}\right)^{3}}
\end{array}
$$

</details>

---

