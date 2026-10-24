# MHT CET Mathematics - Limits

## Topic 3: Trigonometric and Inverse Trigonometric limits

**Total Questions:** 25

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\lim_{x \to \frac{\pi}{4}} \left[\dfrac{4 - (\cos x + \sin x)^4}{1 - \sin 2x}\right]$ is equal to

**Options:**

- **(A)** $2$
- **(B)** $4$
- **(C)** $6$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4$**

**Detailed Solution:**

Let $L = \lim_{x \to \dfrac{\pi}{4}} \dfrac{4 - (\cos x + \sin x)^4}{1 - \sin 2x}$

We know that $(\cos x + \sin x)^2 = \cos^2 x + \sin^2 x + 2\sin x \cos x = 1 + \sin 2x$

Therefore, $(\cos x + \sin x)^4 = (1 + \sin 2x)^2$

Substituting this in the limit, we get:

$L = \lim_{x \to \dfrac{\pi}{4}} \dfrac{4 - (1 + \sin 2x)^2}{1 - \sin 2x}$

Using $a^2 - b^2 = (a - b)(a + b)$, the numerator can be factored as:

$4 - (1 + \sin 2x)^2 = (2 - (1 + \sin 2x))(2 + (1 + \sin 2x)) = (1 - \sin 2x)(3 + \sin 2x)$

So the limit becomes:

$L = \lim_{x \to \dfrac{\pi}{4}} \dfrac{(1 - \sin 2x)(3 + \sin 2x)}{1 - \sin 2x}$

Canceling the common factor $(1 - \sin 2x)$ for $x \neq \dfrac{\pi}{4}$:

$L = \lim_{x \to \dfrac{\pi}{4}} (3 + \sin 2x)$

Substituting $x = \dfrac{\pi}{4}$:

$L = 3 + \sin\left(2 \times \dfrac{\pi}{4}\right) = 3 + \sin\left(\dfrac{\pi}{2}\right)$

$L = 3 + 1 = 4$

Answer: $4$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim\limits_{x \to \frac{\pi}{2}} \dfrac{[1 - \tan(\frac{x}{2})](1 - \sin x)}{[1 + \tan(\frac{x}{2})](\pi - 2x)^3} =$

**Options:**

- **(A)** $\dfrac{1}{32}$
- **(B)** $\dfrac{1}{16}$
- **(C)** $\dfrac{1}{8}$
- **(D)** $\dfrac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{32}$**

**Detailed Solution:**

Let $L = \lim\limits_{x \to \dfrac{\pi}{2}} \dfrac{1 - \tan\left(\dfrac{x}{2}\right)}{1 + \tan\left(\dfrac{x}{2}\right)} \cdot \dfrac{1 - \sin x}{(\pi - 2x)^3}$

Using the trigonometric identity \dfrac{1 - \tan \theta}{1 + \tan \theta} = \tan\left(\dfrac{\pi}{4} - \theta\right), we can rewrite the expression as:

$L = \lim\limits_{x \to \dfrac{\pi}{2}} \dfrac{\tan\left(\dfrac{\pi}{4} - \dfrac{x}{2}\right) (1 - \sin x)}{(\pi - 2x)^3}$

Substitute $x = \dfrac{\pi}{2} - y$. As $x \to \dfrac{\pi}{2}$, $y \to 0$.

The terms in the limit become:

$\dfrac{\pi}{4} - \dfrac{x}{2} = \dfrac{\pi}{4} - \dfrac{1}{2}\left(\dfrac{\pi}{2} - y\right) = \dfrac{y}{2}$

$1 - \sin x = 1 - \sin\left(\dfrac{\pi}{2} - y\right) = 1 - \cos y$

$\pi - 2x = \pi - 2\left(\dfrac{\pi}{2} - y\right) = 2y$

Substituting these into the limit:

$L = \lim\limits_{y \to 0} \dfrac{\tan\left(\dfrac{y}{2}\right) (1 - \cos y)}{(2y)^3}$

Using $1 - \cos y = 2\sin^2\left(\dfrac{y}{2}\right)$:

$L = \lim\limits_{y \to 0} \dfrac{\tan\left(\dfrac{y}{2}\right) \cdot 2\sin^2\left(\dfrac{y}{2}\right)}{8y^3}$

$L = \lim\limits_{y \to 0} \dfrac{1}{4} \cdot \dfrac{\tan\left(\dfrac{y}{2}\right)}{y} \cdot \dfrac{\sin^2\left(\dfrac{y}{2}\right)}{y^2}$

$L = \dfrac{1}{4} \cdot \lim\limits_{y \to 0} \left( \dfrac{1}{2} \dfrac{\tan\left(\dfrac{y}{2}\right)}{\dfrac{y}{2}} \right) \cdot \lim\limits_{y \to 0} \left( \dfrac{1}{2} \dfrac{\sin\left(\dfrac{y}{2}\right)}{\dfrac{y}{2}} \right)^2$

Since $\lim\limits_{\theta \to 0} \dfrac{\tan \theta}{\theta} = 1$ and $\lim\limits_{\theta \to 0} \dfrac{\sin \theta}{\theta} = 1$:

$L = \dfrac{1}{4} \cdot \dfrac{1}{2} \cdot \left(\dfrac{1}{2}\right)^2 = \dfrac{1}{4} \cdot \dfrac{1}{2} \cdot \dfrac{1}{4} = \dfrac{1}{32}$

Answer: $\dfrac{1}{32}$

</details>

---

### Q3. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)$ be a function continuous at $x = 0$, defined for $x \neq 0$ as $f(x) = \dfrac{1 - \cos(1 - \cos(6x))}{x^2 \sin^2(3x)}$. Then the value of $f(0)$ is...

**Options:**

- **(A)** $9$
- **(B)** $18$
- **(C)** $36$
- **(D)** $162$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $18$**

**Detailed Solution:**

Since $f(x)$ is continuous at $x = 0$, $f(0) = \lim_{x \rightarrow 0} f(x)$.

$f(x) = \dfrac{1 - \cos(1 - \cos(6x))}{x^2 \sin^2(3x)}$

Using the trigonometric identity $1 - \cos \theta = 2 \sin^2\left(\dfrac{\theta}{2}\right)$, we get $1 - \cos(6x) = 2 \sin^2(3x)$.

Substituting this into the numerator:

$1 - \cos(2 \sin^2(3x)) = 2 \sin^2(\sin^2(3x))$

The function becomes:

$f(x) = \dfrac{2 \sin^2(\sin^2(3x))}{x^2 \sin^2(3x)}$

Multiplying and dividing the expression by $\sin^2(3x)$:

$f(x) = 2 \left( \dfrac{\sin(\sin^2(3x))}{\sin^2(3x)} \right)^2 \times \dfrac{\sin^2(3x)}{x^2}$

Taking the limit as $x \rightarrow 0$:

$\lim_{x \rightarrow 0} \dfrac{\sin(\sin^2(3x))}{\sin^2(3x)} = 1$

$\lim_{x \rightarrow 0} \dfrac{\sin^2(3x)}{x^2} = \lim_{x \rightarrow 0} \left( \dfrac{\sin(3x)}{3x} \times 3 \right)^2 = 9$

Therefore, $f(0) = 2 \times (1)^2 \times 9 = 18$.

Answer: $18$

</details>

---

### Q4. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\lim_{x \to 0} \dfrac{1 - \cos(1 - \cos x)}{x^4} = $

**Options:**

- **(A)** $\dfrac{1}{2}$
- **(B)** $\dfrac{1}{6}$
- **(C)** $\dfrac{1}{10}$
- **(D)** $\dfrac{1}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{8}$**

**Detailed Solution:**

$\lim_{x \to 0} \dfrac{1 - \cos(1 - \cos x)}{x^4}$

Multiplying and dividing by $(1 - \cos x)^2$:

$= \lim_{x \to 0} \dfrac{1 - \cos(1 - \cos x)}{(1 - \cos x)^2} \times \dfrac{(1 - \cos x)^2}{x^4}$

$= \lim_{x \to 0} \dfrac{1 - \cos(1 - \cos x)}{(1 - \cos x)^2} \times \left( \dfrac{1 - \cos x}{x^2} \right)^2$

Using the standard limit $\lim_{\theta \to 0} \dfrac{1 - \cos \theta}{\theta^2} = \dfrac{1}{2}$, where $\theta = 1 - \cos x \to 0$ as $x \to 0$:

$= \dfrac{1}{2} \times \left( \dfrac{1}{2} \right)^2$

$= \dfrac{1}{2} \times \dfrac{1}{4} = \dfrac{1}{8}$

Answer: $\dfrac{1}{8}$

</details>

---

### Q5. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim_{x\to 1}\left[\dfrac{2^{2x-2}-2^x+1}{\sin^2(x-1)}\right]=$

**Options:**

- **(A)** $1$
- **(B)** $(\log 2)^2$
- **(C)** $\log 2$
- **(D)** $2\log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(\log 2)^2$**

**Detailed Solution:**

Let $x - 1 = t$. As $x \rightarrow 1$, $t \rightarrow 0$.

Substituting $x = t + 1$ in the given limit, we get:

$\lim_{t\to 0} \dfrac{2^{2(t+1)-2} - 2^{t+1} + 1}{\sin^2 t}$

$= \lim_{t\to 0} \dfrac{2^{2t} - 2 \cdot 2^t + 1}{\sin^2 t}$

$= \lim_{t\to 0} \dfrac{(2^t - 1)^2}{\sin^2 t}$

Multiplying and dividing by $t^2$:

$= \lim_{t\to 0} \left( \dfrac{2^t - 1}{t} \right)^2 \left( \dfrac{t}{\sin t} \right)^2$

Using the standard limits $\lim_{t\to 0} \dfrac{a^t - 1}{t} = \log a$ and $\lim_{t\to 0} \dfrac{t}{\sin t} = 1$:

$= (\log 2)^2 \times (1)^2$

$= (\log 2)^2$

Answer: $(\log 2)^2$

</details>

---

### Q6. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\lim\limits_{x \to 0}\left(\dfrac{8}{x^8}\right)\left[1 - \cos\dfrac{x^2}{2} - \cos\dfrac{x^2}{4} + \cos\dfrac{x^2}{2}\cdot\cos\dfrac{x^2}{4}\right]$ is equal to ...

**Options:**

- **(A)** $\dfrac{1}{8}$
- **(B)** $\dfrac{1}{32}$
- **(C)** $\dfrac{1}{16}$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{32}$**

**Detailed Solution:**

The given expression inside the limit can be factored as:

$\left(1 - \cos\dfrac{x^2}{2}\right)\left(1 - \cos\dfrac{x^2}{4}\right)$

The limit becomes:

$\lim\limits_{x \to 0} \dfrac{8}{x^8} \left(1 - \cos\dfrac{x^2}{2}\right)\left(1 - \cos\dfrac{x^2}{4}\right)$

Using the standard limit $\lim\limits_{\theta \to 0} \dfrac{1 - \cos \theta}{\theta^2} = \dfrac{1}{2}$, we can rewrite the expression as:

$\lim\limits_{x \to 0} \dfrac{8}{x^8} \left( \dfrac{1 - \cos\dfrac{x^2}{2}}{\left(\dfrac{x^2}{2}\right)^2} \cdot \dfrac{x^4}{4} \right) \left( \dfrac{1 - \cos\dfrac{x^2}{4}}{\left(\dfrac{x^2}{4}\right)^2} \cdot \dfrac{x^4}{16} \right)$

Evaluating the standard limits:

$= \lim\limits_{x \to 0} \dfrac{8}{x^8} \left( \dfrac{1}{2} \cdot \dfrac{x^4}{4} \right) \left( \dfrac{1}{2} \cdot \dfrac{x^4}{16} \right)$

$= \lim\limits_{x \to 0} \dfrac{8}{x^8} \left( \dfrac{x^4}{8} \right) \left( \dfrac{x^4}{32} \right)$

$= \lim\limits_{x \to 0} \dfrac{8}{x^8} \cdot \dfrac{x^8}{256}$

$= \dfrac{8}{256} = \dfrac{1}{32}$

Answer: $\dfrac{1}{32}$

</details>

---

### Q7. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\displaystyle\lim_{x \to 0}\dfrac{(5^x - 1)^4\,\text{cosec}\,(x\log 5)}{\tan(x\log 5) \cdot \log(1 + x^2\log 25)} = \ldots\ldots$

**Options:**

- **(A)** $5\log 5$
- **(B)** $\log\sqrt{5}$
- **(C)** $(\log 5)^2$
- **(D)** $\dfrac{1}{4}\log 5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log\sqrt{5}$**

**Detailed Solution:**

The given limit is:

$\displaystyle\lim_{x \to 0}\dfrac{(5^x - 1)^4\,\text{cosec}\,(x\log 5)}{\tan(x\log 5) \cdot \log(1 + x^2\log 25)}$

Rewriting $\text{cosec}\,(x\log 5)$ as $\dfrac{1}{\sin(x\log 5)}$, we get:

$\displaystyle\lim_{x \to 0}\dfrac{(5^x - 1)^4}{\sin(x\log 5) \cdot \tan(x\log 5) \cdot \log(1 + x^2\log 25)}$

Dividing the numerator and the denominator by $x^4$:

$\displaystyle\lim_{x \to 0}\dfrac{\left(\dfrac{5^x - 1}{x}\right)^4}{\left(\dfrac{\sin(x\log 5)}{x}\right) \cdot \left(\dfrac{\tan(x\log 5)}{x}\right) \cdot \left(\dfrac{\log(1 + x^2\log 25)}{x^2}\right)}$

Using the standard limits $\displaystyle\lim_{x \to 0}\dfrac{a^x - 1}{x} = \log a$, $\displaystyle\lim_{x \to 0}\dfrac{\sin(kx)}{x} = k$, $\displaystyle\lim_{x \to 0}\dfrac{\tan(kx)}{x} = k$, and $\displaystyle\lim_{x \to 0}\dfrac{\log(1 + kx)}{x} = k$, we evaluate the limits of the individual terms:

Numerator limit $= (\log 5)^4$

Denominator limit $= (\log 5) \cdot (\log 5) \cdot (\log 25)$

Since $\log 25 = \log(5^2) = 2\log 5$, the denominator limit becomes:

$(\log 5) \cdot (\log 5) \cdot (2\log 5) = 2(\log 5)^3$

Substituting these back into the expression:

$\text{Limit} = \dfrac{(\log 5)^4}{2(\log 5)^3} = \dfrac{1}{2}\log 5$

Using the property of logarithms $m\log n = \log(n^m)$:

$\text{Limit} = \log(5^{1/2}) = \log\sqrt{5}$

Answer: $\log\sqrt{5}$

</details>

---

### Q8. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\lim _{x \rightarrow \frac{\pi}{2}} \frac{\left(1-\tan \left(\frac{x}{2}\right)\right)(1-\sin x)}{\left(1+\tan \left(\frac{x}{2}\right)\right)(\pi-2 x)^3}$ is

**Options:**

- **(A)** 0
- **(B)** $\frac{1}{32}$
- **(C)** $\frac{1}{8}$
- **(D)** $\frac{1}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{32}$**

**Detailed Solution:**

Let $x = \dfrac{\pi}{2} - h$. As $x \rightarrow \dfrac{\pi}{2}$, $h \rightarrow 0$.

We can simplify the expression using trigonometric identities:

$\dfrac{1-\tan\left(\dfrac{x}{2}\right)}{1+\tan\left(\dfrac{x}{2}\right)} = \tan\left(\dfrac{\pi}{4} - \dfrac{x}{2}\right)$

Substituting $x = \dfrac{\pi}{2} - h$, we get:

$\tan\left(\dfrac{\pi}{4} - \left(\dfrac{\pi}{4} - \dfrac{h}{2}\right)\right) = \tan\left(\dfrac{h}{2}\right)$

For the other terms in the limit:

$1 - \sin x = 1 - \sin\left(\dfrac{\pi}{2} - h\right) = 1 - \cos h = 2\sin^2\left(\dfrac{h}{2}\right)$

$(\pi - 2x)^3 = (\pi - (\pi - 2h))^3 = (2h)^3 = 8h^3$

Substituting these into the original limit:

$L = \lim_{h \rightarrow 0} \dfrac{\tan\left(\dfrac{h}{2}\right) \cdot 2\sin^2\left(\dfrac{h}{2}\right)}{8h^3}$

$L = \dfrac{1}{4} \lim_{h \rightarrow 0} \left(\dfrac{\tan\left(\dfrac{h}{2}\right)}{h}\right) \left(\dfrac{\sin\left(\dfrac{h}{2}\right)}{h}\right)^2$

$L = \dfrac{1}{4} \lim_{h \rightarrow 0} \left(\dfrac{\tan\left(\dfrac{h}{2}\right)}{\dfrac{h}{2}} \cdot \dfrac{1}{2}\right) \left(\dfrac{\sin\left(\dfrac{h}{2}\right)}{\dfrac{h}{2}} \cdot \dfrac{1}{2}\right)^2$

Using the standard limits $\lim_{\theta \rightarrow 0} \dfrac{\tan \theta}{\theta} = 1$ and $\lim_{\theta \rightarrow 0} \dfrac{\sin \theta}{\theta} = 1$:

$L = \dfrac{1}{4} \left(1 \cdot \dfrac{1}{2}\right) \left(1 \cdot \dfrac{1}{2}\right)^2$

$L = \dfrac{1}{4} \cdot \dfrac{1}{2} \cdot \dfrac{1}{4} = \dfrac{1}{32}$

Answer: $\frac{1}{32}$

</details>

---

### Q9. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\lim _{x \rightarrow 0} \frac{x \tan 2 x-2 x \tan x}{(1-\cos 2 x)^2}$ is

**Options:**

- **(A)** 2
- **(B)** -2
- **(C)** $\frac{1}{2}$
- **(D)** $-\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2}$**

**Detailed Solution:**

Let $L = \lim_{x \rightarrow 0} \dfrac{x \tan 2x - 2x \tan x}{(1 - \cos 2x)^2}$

Using the trigonometric identity $1 - \cos 2x = 2 \sin^2 x$, the denominator becomes:

$(2 \sin^2 x)^2 = 4 \sin^4 x$

For the numerator, using the formula $\tan 2x = \dfrac{2 \tan x}{1 - \tan^2 x}$:

$x \tan 2x - 2x \tan x = x \left( \dfrac{2 \tan x}{1 - \tan^2 x} - 2 \tan x \right)$

$= 2x \tan x \left( \dfrac{1 - (1 - \tan^2 x)}{1 - \tan^2 x} \right)$

$= \dfrac{2x \tan^3 x}{1 - \tan^2 x}$

Substituting these back into the limit:

$L = \lim_{x \rightarrow 0} \dfrac{\dfrac{2x \tan^3 x}{1 - \tan^2 x}}{4 \sin^4 x}$

$L = \lim_{x \rightarrow 0} \dfrac{2x \tan^3 x}{4 \sin^4 x (1 - \tan^2 x)}$

$L = \lim_{x \rightarrow 0} \dfrac{1}{2 (1 - \tan^2 x)} \cdot \left( \dfrac{x}{\sin x} \right) \cdot \left( \dfrac{\tan x}{\sin x} \right)^3$

Since $\lim_{x \rightarrow 0} \dfrac{x}{\sin x} = 1$ and $\lim_{x \rightarrow 0} \dfrac{\tan x}{\sin x} = \lim_{x \rightarrow 0} \dfrac{1}{\cos x} = 1$:

$L = \dfrac{1}{2(1 - 0)} \cdot 1 \cdot 1^3 = \dfrac{1}{2}$

Answer: $\frac{1}{2}$

</details>

---

### Q10. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\lim _{x \rightarrow \dfrac{\pi}{2}} \dfrac{(1-\sin x)\left(8 x^3-\pi^3\right) \cos x}{(\pi-2 x)^4}$

**Options:**

- **(A)** $\dfrac{\pi^2}{16}$
- **(B)** $\dfrac{3 \pi^2}{16}$
- **(C)** $\dfrac{-3 \pi^2}{16}$
- **(D)** $\dfrac{-\pi^2}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{-3 \pi^2}{16}$**

**Detailed Solution:**

Let $x = \dfrac{\pi}{2} - t$. As $x \rightarrow \dfrac{\pi}{2}$, $t \rightarrow 0$.

The given limit can be rewritten by substituting $x$:

$L = \lim_{t \rightarrow 0} \dfrac{(1-\cos t)\left(8\left(\dfrac{\pi}{2}-t\right)^3-\pi^3\right)\sin t}{(2t)^4}$

Using the identity $a^3 - b^3 = (a-b)(a^2+ab+b^2)$, we can factor $8x^3 - \pi^3$ as $(2x)^3 - \pi^3 = (2x-\pi)(4x^2+2\pi x+\pi^2)$.

Substituting $2x-\pi = -2t$ and evaluating the limit of the quadratic factor as $x \rightarrow \dfrac{\pi}{2}$:

$\lim_{x \rightarrow \dfrac{\pi}{2}} (4x^2+2\pi x+\pi^2) = 4\left(\dfrac{\pi^2}{4}\right) + 2\pi\left(\dfrac{\pi}{2}\right) + \pi^2 = 3\pi^2$

Now, substituting these into the limit expression:

$L = \lim_{t \rightarrow 0} \dfrac{(1-\cos t)(-2t)(3\pi^2)\sin t}{16t^4}$

$L = \dfrac{-6\pi^2}{16} \lim_{t \rightarrow 0} \left(\dfrac{1-\cos t}{t^2}\right) \left(\dfrac{\sin t}{t}\right)$

Using the standard limits $\lim_{t \rightarrow 0} \dfrac{1-\cos t}{t^2} = \dfrac{1}{2}$ and $\lim_{t \rightarrow 0} \dfrac{\sin t}{t} = 1$:

$L = \dfrac{-3\pi^2}{8} \times \dfrac{1}{2} \times 1 = \dfrac{-3\pi^2}{16}$

Answer: $\dfrac{-3 \pi^2}{16}$

</details>

---

### Q11. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0} \dfrac{(1-\cos 2 x)(3+\cos x)}{x \tan 4 x}$ has the value

**Options:**

- **(A)** 2
- **(B)** $\dfrac{1}{2}$
- **(C)** 4
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

The given limit is $\lim _{x \rightarrow 0} \dfrac{(1-\cos 2 x)(3+\cos x)}{x \tan 4 x}$

Using the trigonometric identity $1 - \cos 2x = 2 \sin^2 x$, the expression becomes:

$\lim _{x \rightarrow 0} \dfrac{2 \sin^2 x (3+\cos x)}{x \tan 4 x}$

Multiplying and dividing by $x$ and $4$, we can rearrange the terms as:

$\lim _{x \rightarrow 0} 2 \left(\dfrac{\sin x}{x}\right)^2 \cdot \dfrac{4x}{\tan 4 x} \cdot \dfrac{1}{4} \cdot (3+\cos x)$

Using the standard limits $\lim _{x \rightarrow 0} \dfrac{\sin x}{x} = 1$ and $\lim _{x \rightarrow 0} \dfrac{\tan kx}{kx} = 1$, we get:

$2 \times (1)^2 \times 1 \times \dfrac{1}{4} \times (3+\cos 0)$

$= 2 \times 1 \times \dfrac{1}{4} \times (3+1)$

$= 2 \times \dfrac{1}{4} \times 4 = 2$

Answer: 2

</details>

---

### Q12. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0} \dfrac{\sin \left(\pi \cos ^2 x\right)}{x^2}$ is equal to

**Options:**

- **(A)** 1
- **(B)** $-\pi$
- **(C)** $\pi$
- **(D)** $\dfrac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\pi$**

**Detailed Solution:**

$\lim_{x \rightarrow 0} \dfrac{\sin (\pi \cos^2 x)}{x^2}$

Using the identity $\cos^2 x = 1 - \sin^2 x$, we get:

$\sin(\pi \cos^2 x) = \sin(\pi(1 - \sin^2 x)) = \sin(\pi - \pi \sin^2 x)$

Since $\sin(\pi - \theta) = \sin \theta$, this simplifies to:

$\sin(\pi \cos^2 x) = \sin(\pi \sin^2 x)$

The limit becomes:

$\lim_{x \rightarrow 0} \dfrac{\sin(\pi \sin^2 x)}{x^2}$

Multiplying and dividing the expression by $\pi \sin^2 x$:

$\lim_{x \rightarrow 0} \left( \dfrac{\sin(\pi \sin^2 x)}{\pi \sin^2 x} \right) \cdot \pi \cdot \left( \dfrac{\sin x}{x} \right)^2$

As $x \rightarrow 0$, $\pi \sin^2 x \rightarrow 0$. Using the standard limit $\lim_{\theta \rightarrow 0} \dfrac{\sin \theta}{\theta} = 1$:

$1 \cdot \pi \cdot (1)^2 = \pi$

Answer: $\pi$

</details>

---

### Q13. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$$
\lim _{x \rightarrow 0} \frac{\sqrt{1+x \sin x}-\sqrt{\cos x}}{\tan ^2 \frac{x}{2}}=
$$

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 0} \frac{\sqrt{1+x \sin x}-\sqrt{\cos x}}{\tan ^2 \frac{x}{2}} \\ & =\lim _{x \rightarrow 0} \frac{1+x \sin x-\cos x}{\tan ^2 \frac{x}{2}(\sqrt{1+x \sin x}+\sqrt{\cos x})}\end{aligned}$
$\begin{aligned} & =\lim _{x \rightarrow 0} \frac{x \sin x+2 \sin ^2 \frac{x}{2}}{\tan ^2 \frac{x}{2}(\sqrt{1+x \sin x}+\sqrt{\cos x})} \\ & =\lim _{x \rightarrow 0} \frac{\frac{\sin x}{x}+\frac{2 \sin ^2 \frac{x}{2}}{x^2}}{\frac{\tan ^2 \frac{x}{2}}{x^2}(\sqrt{1+x \sin x}+\sqrt{\cos x})}\end{aligned}$
$=\lim _{x \rightarrow 0}\left(\frac{\frac{\sin x}{x}+\frac{2 \sin ^2 \frac{x}{2}}{\frac{x^2}{4}} \times \frac{1}{4}}{\frac{\tan ^2 \frac{x}{2}}{\frac{x^2}{4}} \times \frac{1}{4}(\sqrt{1+x \sin x}+\sqrt{\cos x})}\right)$
$\begin{aligned} & =\frac{1+2 \times 1 \times \frac{1}{4}}{1 \times \frac{1}{4}(\sqrt{1+0}+\sqrt{1})} \\ & =3\end{aligned}$

</details>

---

### Q14. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0} \frac{x \cot 4 x}{\sin ^2 x \cdot \cot ^2(2 x)}$ is equal to

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $4$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1$**

**Detailed Solution:**

$\begin{aligned} \lim _{x \rightarrow 0} \frac{x \cot 4 x}{\sin ^2 x \cot ^2(2 x)} & =\lim _{x \rightarrow 0} \frac{x \tan ^2 2 x}{\sin ^2 x \tan 4 x} \\ & =\lim _{x \rightarrow 0} \frac{4\left(\frac{\tan 2 x}{2 x}\right)^2}{4\left(\frac{\sin x}{x}\right)^2\left(\frac{\tan 4 x}{4 x}\right)} \\ & =1\end{aligned}$

</details>

---

### Q15. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 4} \frac{\cos 7 x^{\circ}-\cos 2 x^{\circ}}{x^2}$ is

**Options:**

- **(A)** $\frac{-45}{2} \pi^2$
- **(B)** $\frac{-45}{2} \pi$
- **(C)** $\frac{-\pi^2}{1440}$
- **(D)** $\frac{-\pi^2}{2880}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{-\pi^2}{1440}$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 0} \frac{\cos 7 x^{\circ}-\cos 2 x^{\circ}}{x^2} \\ & =\lim _{x \rightarrow 0} \frac{\cos \left(\frac{7 \pi}{180}\right) x-\cos \left(\frac{2 \pi}{180}\right) x}{x^2} \\ & =\frac{\left(\frac{2 \pi}{180}\right)^2-\left(\frac{7 \pi}{180}\right)^2}{2} \\ & \quad \ldots\left[\because \lim _{x \rightarrow 0} \frac{\cos m x-\cos n x}{x^2}=\frac{n^2-m^2}{2}\right] \\ & =\frac{-\pi^2}{1440}\end{aligned}$

</details>

---

### Q16. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow \frac{\pi}{2}} \frac{\cot x-\cos x}{(\pi-2 x)^3}$ equals

**Options:**

- **(A)** $\frac{1}{24}$
- **(B)** $\frac{1}{16}$
- **(C)** $\frac{1}{8}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{16}$**

**Detailed Solution:**

$\begin{aligned} \text { Let } \mathrm{I} & =\lim _{x \rightarrow \frac{\pi}{2}} \frac{\cot x-\cos x}{(\pi-2 x)^3} \\ & =\lim _{x \rightarrow \frac{\pi}{2}} \frac{\cos x(1-\sin x)}{\sin x(\pi-2 x)^3} \\ \text { Put } x & =\frac{\pi}{2}-\mathrm{h} \\ \therefore \quad \pi-2 x & =2 \mathrm{~h} \\ \text { As } x & \rightarrow \frac{\pi}{2}, \mathrm{~h} \rightarrow 0\end{aligned}$
$\begin{aligned} \therefore \quad I & =\lim _{h \rightarrow 0} \frac{\cos \left(\frac{\pi}{2}-h\right)\left(1-\sin \left(\frac{\pi}{2}-h\right)\right)}{\sin \left(\frac{\pi}{2}-h\right)(2 h)^3} \\ & =\lim _{h \rightarrow 0} \frac{\sin h \cdot 2 \sin ^2\left(\frac{h}{2}\right)}{\cosh \cdot 8 h^3} \\ & =\frac{2}{8} \lim _{h \rightarrow 0} \frac{\sin h}{h} \times \lim _{h \rightarrow 0} \frac{\sin ^2 \frac{h}{2}}{\frac{h^2}{4} \cdot 4} \\ & =\frac{2}{8}(1) \times(1) \times \frac{1}{4} \\ & =\frac{1}{16}\end{aligned}$

</details>

---

### Q17. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0} \frac{\sin \left(\pi \cos ^2 x\right)}{x^2}$ is equal to

**Options:**

- **(A)** $-\pi$
- **(B)** $\pi$
- **(C)** $\frac{\pi}{2}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\pi$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 0} \frac{\sin \left(\pi \cos ^2 x\right)}{x^2}=\lim _{\substack{x \rightarrow 0}} \frac{\sin \left(\pi\left\{1-\sin ^2 x\right\}\right)}{x^2} \\ & =\lim _{x \rightarrow 0} \frac{\sin \left(\pi-\pi \sin ^2 x\right)}{x^2}=\lim _{\substack{2}} \frac{\sin \left(\pi \sin ^2 x\right)}{x^2} \\ & =\lim _{x \rightarrow 0} \frac{\sin \left(\pi \sin ^2 x\right)}{\pi \sin ^2 x} \cdot \frac{\pi \sin ^2 x}{x^2}=\pi\end{aligned}$

</details>

---

### Q18. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow 0} \frac{\sin ^2 x}{\sqrt{2}-\sqrt{1+\cos x}}$ equals

**Options:**

- **(A)** $\sqrt{2}$
- **(B)** $4 \sqrt{2}$
- **(C)** $2 \sqrt{2}$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4 \sqrt{2}$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 0} \frac{\sin ^2 x}{\sqrt{2}-\sqrt{1+\cos x}}=\lim _{x \rightarrow 0} \frac{\sin ^2 x\{\sqrt{2}+\sqrt{1+\cos x}\}}{2-(1+\cos x)} \\ & =\lim _{x \rightarrow 0} \frac{(1-\cos x)(1+\cos x)(\sqrt{2}+\sqrt{1+\cos x})}{1-\cos x} \\ & =(1+\cos 0)(\sqrt{2}+\sqrt{1+\cos 0}) \\ & =2 \times 2 \sqrt{2} \\ & =4 \sqrt{2}\end{aligned}$

</details>

---

### Q19. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\lim _{x \rightarrow 0} \frac{\sqrt{1-\cos x^2}}{1-\cos x}=$

**Options:**

- **(A)** $\sqrt{2}$
- **(B)** $\frac{1}{\sqrt{2}}$
- **(C)** 0
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{2}$**

**Detailed Solution:**

$\begin{aligned}
& \lim _{x \rightarrow 0} \frac{\sqrt{1-\cos x^2}}{1-\cos x} \\
& =\lim _{x \rightarrow 0} \frac{\sqrt{2 \sin ^2 \frac{x^2}{2}}}{2 \sin ^2 \frac{x}{2}}=\lim _{x \rightarrow 0} \frac{\sqrt{2} \sin \frac{x^2}{2}}{2 \sin ^2 \frac{x}{2}}
\end{aligned}$
Dividing numerator and denominator by $\frac{x^2}{4}$, we get
$\frac{\frac{1}{\sqrt{2}} \lim _{x \rightarrow 0}\left[\frac{\sin \left(\frac{x^2}{2}\right)}{\left(\frac{x^2}{4}\right)}\right]}{\frac{\sin \left(\frac{x}{2}\right)}{\left(\frac{x}{2}\right)} \times \frac{1}{\sqrt{2}} \lim _{x \rightarrow 0} \frac{\sin \left(\frac{x^2}{2}\right)}{\left(\frac{x}{2}\right)}}=\frac{\left.x^2\right) \times \frac{1}{2}}{\left[\frac{x}{2}\right)}=\frac{1}{\sqrt{2}} \times \frac{2}{1}=\sqrt{2}$

</details>

---

### Q20. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow 0} \frac{\cos (m x)-\cos (n x)}{x^2}=$

**Options:**

- **(A)** $\frac{\mathrm{m}^2-\mathrm{n}^2}{2}$
- **(B)** $m^2-n^2$
- **(C)** $\frac{\mathrm{n}^2-\mathrm{m}^2}{2}$
- **(D)** $n^2-m^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\mathrm{n}^2-\mathrm{m}^2}{2}$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 0} \frac{\cos (m x)-\cos (n x)}{x^2} \\ & =\lim _{x \rightarrow 0} \frac{\left[-2 \sin \frac{(m+n) x}{2} \sin \frac{(m-n) x}{2}\right]}{x^2} \\ & =-2 \lim _{x \rightarrow 0}\left[\frac{\sin \left(\frac{m+n}{2}\right) x}{\left(\frac{m+n}{2}\right) x} \times\left(\frac{m+n}{2}\right)\right]\left[\frac{\sin \left(\frac{m-n}{2}\right) x}{\left(\frac{m-n}{2}\right) x} \times\left(\frac{m-n}{2}\right)\right] \\ & =(-2)\left(\frac{m+n}{2}\right)\left(\frac{m-n}{2}\right)=\frac{m^2-n^2}{-2}=\frac{n^2-m^2}{2}\end{aligned}$

</details>

---

### Q21. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mrow></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup><mo>,</mo><mi>x</mi><mo>≠</mo><mn>0</mn></math> at <math><mo>=</mo><mtext> </mtext><mi>k</mi><mo>,</mo><mtext>  </mtext><mi>x</mi><mo>=</mo><mn>0</mn></math> is continuous <math><mi>x</mi><mo>=</mo><mn>0</mn></math> Then <math><mi>k</mi><mo>=</mo></math> …

**Options:**

- **(A)** <math><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(B)** <math><mn>1</mn></math>
- **(C)** e
- **(D)** <math><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

We have,
<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mrow></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup><mo>,</mo><mi>x</mi><mo>≠</mo><mn>0</mn></math>
<math><mo>=</mo><mi>k</mi><mo>,</mo><mi>x</mi><mo>=</mo><mn>0</mn></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn></math>
<math><mo>∴</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced></math>
<math><mo>⇒</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><msup><mrow><mfenced close="}" open="{" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mrow></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup><mo>=</mo><mi>k</mi></math>
<math><mo>⇒</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></msup></mrow></munder><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>.</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>=</mo><mi>k</mi></math>
<math><mo>⇒</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></msup></mrow></munder><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mo>.</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>=</mo><mi>k</mi></math>
<math><mo>⇒</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></msup></mrow></munder><mfrac><mrow><mn>2</mn><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mrow><mi>x</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mi>k</mi></math>
<math><mo>⇒</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn><mi>x</mi><mo>→</mo><mn>0</mn></mrow></msup></mrow></munder><mfrac><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mrow><mi>x</mi></mrow></mfrac><mo>.</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><msup><mrow><mi></mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></msup></mrow></munder><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mi>k</mi></math>
<math><mo>⇒</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn><mo>×</mo><mn>1</mn><mo>×</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>k</mi></math>
<math><mo>⇒</mo><mi>k</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

</details>

---

### Q22. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow \pi / 2}(\sec x-\tan x)$ is equal to

**Options:**

- **(A)** 2
- **(B)** $-1$
- **(C)** 1
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

$\lim _{x \rightarrow \frac{\pi}{2}}(\sec x-\tan x)$
$\Rightarrow \quad \lim _{x \rightarrow \frac{\pi}{2}}\left(\frac{1-\sin x}{\cos x}\right) \quad\left(\frac{0}{0}\right.$ form $)$
Using 'L' hospital rule, $\Rightarrow \quad \lim _{x \rightarrow \frac{\pi}{2}} \frac{-\cos x}{-\sin x}$
$=\lim _{x \rightarrow \frac{\pi}{2}} \cot x=\cot \frac{\pi}{2}=0$

</details>

---

### Q23. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\sqrt{\frac{x-\sin x}{x+\cos ^{2} x}}$, then $\lim _{x \rightarrow \infty} f(x)$ is

**Options:**

- **(A)** 0
- **(B)** $\alpha$
- **(C)** 1
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

$\lim _{x \rightarrow \infty} f(x)=\lim _{x \rightarrow \infty} \sqrt{\frac{x-\sin x}{x+\cos ^{2} x}}$
$=\lim _{x \rightarrow \infty} \sqrt{\frac{1-\frac{\sin x}{x}}{1+\frac{\cos ^{2} x}{x}}}$
$=\sqrt{\frac{1-0}{1+0}}$
$\left[\because \frac{\sin x}{x} \rightarrow 0, \frac{\cos ^{2} x}{x} \rightarrow 0\right.$ as $\left.x \rightarrow \infty\right]$
$=1$

</details>

---

### Q24. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0} \frac{\cos a x-\cos b x}{x^{2}}$ is equal to

**Options:**

- **(A)** $\frac{a^{2}-b^{2}}{2}$
- **(B)** $\frac{b^{2}-a^{2}}{2}$
- **(C)** $a^{2}-b^{2}$
- **(D)** $b^{2}-a^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{b^{2}-a^{2}}{2}$**

**Detailed Solution:**

$\lim _{x \rightarrow 0} \frac{\cos a x-\cos b x}{x^{2}}$
$=\lim _{x \rightarrow 0} \frac{-a \sin a x+b \sin b x}{2 x}$ (using L'Hospital's rule)
$=\lim _{x \rightarrow 0} \frac{-a^{2} \cos a x+b^{2} \sin b x}{2}$
$=\frac{b^{2}-a^{2}}{2}$ (using L'Hospital's rule)

</details>

---

### Q25. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `3`

The value of $\lim _{x \rightarrow 0} \frac{\cos (\sin x)-\cos x}{x^{4}}$ is equal to

**Options:**

- **(A)** $1 / 5$
- **(B)** $1 / 6$
- **(C)** $1 / 4$
- **(D)** $1 / 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1 / 6$**

**Detailed Solution:**

$$
\begin{array}{l}
\lim _{x \rightarrow 0} \frac{\cos (\sin x)-\cos x}{x^{4}} \\
=\lim _{x \rightarrow 0} \frac{2 \sin \left(\frac{x+\sin x}{2}\right) \sin \left(\frac{x-\sin x}{2}\right)}{x^{4}} \\
=2 \lim _{x \rightarrow 0}\left[\frac{\sin \left(\frac{x+\sin x}{2}\right)}{\left(\frac{x+\sin x}{2}\right)} \times \frac{\sin \left(\frac{x-\sin x}{2}\right)}{\left(\frac{x-\sin x}{2}\right)}\right. \\
\left.\times\left(\frac{x+\sin x}{2 x}\right)\left(\frac{x-\sin x}{2 x^{3}}\right)\right] \\
=2 \lim _{x \rightarrow 0}\left[\frac{\sin \left(\frac{x+\sin x}{2}\right)}{\frac{x+\sin x}{2}} \times \frac{\sin \left(\frac{x-\sin x}{2}\right)}{\frac{x-\sin x}{2}}\right. \\
=\lim _{x \rightarrow 0} \frac{x-\sin x}{x^{3}}=\lim _{x \rightarrow 0} \frac{x-\left(x-\frac{x^{3}}{3 !}+\frac{x^{5}}{5 !}-\ldots\right)}{x^{3}} \\
=\lim _{x \rightarrow 0}\left(\frac{1}{3 !}-\frac{x^{2}}{5 !}+\ldots\right)=\frac{1}{6}
\end{array}
$$

</details>

---

