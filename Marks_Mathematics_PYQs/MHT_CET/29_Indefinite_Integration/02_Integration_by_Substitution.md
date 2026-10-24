# MHT CET Mathematics - Indefinite Integration

## Topic 2: Integration by Substitution

**Total Questions:** 260

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\displaystyle\int \dfrac{\cos\frac{x}{2} - \sin\frac{x}{2}}{\sqrt{8 - \sin x}}\,dx = 2\sin^{-1}\left(\dfrac{\phi(x)}{3}\right) + c$, then $[\phi(x)]^2$ is equal to _____

**Options:**

- **(A)** $1 + \cos x$
- **(B)** $1 + \sin x$
- **(C)** $1 - \sin x$
- **(D)** $1 - \cos x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1 + \sin x$**

**Detailed Solution:**

Let $I = \int \dfrac{\cos\dfrac{x}{2} - \sin\dfrac{x}{2}}{\sqrt{8 - \sin x}} \, dx$

Let $\sin\dfrac{x}{2} + \cos\dfrac{x}{2} = t$

Squaring both sides, we get $1 + \sin x = t^2 \Rightarrow \sin x = t^2 - 1$

Differentiating with respect to $x$, we get $\dfrac{1}{2}\left(\cos\dfrac{x}{2} - \sin\dfrac{x}{2}\right)dx = dt$

$\left(\cos\dfrac{x}{2} - \sin\dfrac{x}{2}\right)dx = 2dt$

Substituting these into the integral, we get:

$I = \int \dfrac{2dt}{\sqrt{8 - (t^2 - 1)}} = \int \dfrac{2dt}{\sqrt{9 - t^2}}$

$I = 2\sin^{-1}\left(\dfrac{t}{3}\right) + c$

Comparing with the given expression $2\sin^{-1}\left(\dfrac{\phi(x)}{3}\right) + c$, we get $\phi(x) = t$

Therefore, $[\phi(x)]^2 = t^2 = 1 + \sin x$

Answer: $1 + \sin x$

</details>

---

### Q2. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\displaystyle\int \dfrac{x+1}{x(1+xe^x)^2}\,dx = \log\left|\dfrac{xe^x}{1+xe^x}\right| + f(x) + c$, then $f(x) =$

**Options:**

- **(A)** $\dfrac{1}{1+xe^x}$
- **(B)** $\dfrac{x}{1+xe^x}$
- **(C)** $\dfrac{xe^x}{1+x}$
- **(D)** $\dfrac{xe^x}{1+e^x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{1+xe^x}$**

**Detailed Solution:**

Let $I = \displaystyle\int \dfrac{x+1}{x(1+xe^x)^2}\,dx$

Multiplying the numerator and the denominator by $e^x$, we get:

$I = \displaystyle\int \dfrac{(x+1)e^x}{xe^x(1+xe^x)^2}\,dx$

Let $t = xe^x$. Differentiating with respect to $x$, we get:

$dt = (1 \cdot e^x + x \cdot e^x)\,dx = (x+1)e^x\,dx$

Substituting this into the integral:

$I = \displaystyle\int \dfrac{dt}{t(1+t)^2}$

Using partial fractions:

$\dfrac{1}{t(1+t)^2} = \dfrac{1+t-t}{t(1+t)^2} = \dfrac{1}{t(1+t)} - \dfrac{1}{(1+t)^2}$

$\dfrac{1}{t(1+t)^2} = \dfrac{1+t-t}{t(1+t)} - \dfrac{1}{(1+t)^2} = \dfrac{1}{t} - \dfrac{1}{1+t} - \dfrac{1}{(1+t)^2}$

Integrating with respect to $t$:

$I = \displaystyle\int \left( \dfrac{1}{t} - \dfrac{1}{1+t} - \dfrac{1}{(1+t)^2} \right) dt$

$I = \log|t| - \log|1+t| + \dfrac{1}{1+t} + c$

$I = \log\left|\dfrac{t}{1+t}\right| + \dfrac{1}{1+t} + c$

Substituting back $t = xe^x$:

$I = \log\left|\dfrac{xe^x}{1+xe^x}\right| + \dfrac{1}{1+xe^x} + c$

Comparing this with the given expression $I = \log\left|\dfrac{xe^x}{1+xe^x}\right| + f(x) + c$, we get:

$f(x) = \dfrac{1}{1+xe^x}$

Answer: $\dfrac{1}{1+xe^x}$

</details>

---

### Q3. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\displaystyle\int g(x)\,dx = f(x)$ then $\displaystyle\int \dfrac{g(x)}{9 - [f(x)]^2}\,dx$ is equal to

**Options:**

- **(A)** $\dfrac{1}{6}\log\left|\dfrac{3 - g(x)}{3 - f(x)}\right| + c$
- **(B)** $\dfrac{1}{3}\log\left|\dfrac{3 + f(x)}{3 - f(x)}\right| + c$
- **(C)** $\dfrac{1}{6}\log\left|\dfrac{3 + f(x)}{3 - f(x)}\right| + c$
- **(D)** $\dfrac{1}{3}\log\left|\dfrac{3 + f(x)}{3 + g(x)}\right| + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{6}\log\left|\dfrac{3 + f(x)}{3 - f(x)}\right| + c$**

**Detailed Solution:**

Given $\displaystyle\int g(x)\,dx = f(x)$

Differentiating both sides with respect to $x$, we get $g(x) = f'(x)$

Let $I = \displaystyle\int \dfrac{g(x)}{9 - [f(x)]^2}\,dx$

Substituting $f(x) = t$, we get $f'(x)\,dx = dt \Rightarrow g(x)\,dx = dt$

$I = \displaystyle\int \dfrac{dt}{9 - t^2}$

Using the standard formula $\displaystyle\int \dfrac{dx}{a^2 - x^2} = \dfrac{1}{2a}\log\left|\dfrac{a + x}{a - x}\right| + c$

$I = \dfrac{1}{2(3)}\log\left|\dfrac{3 + t}{3 - t}\right| + c$

$I = \dfrac{1}{6}\log\left|\dfrac{3 + f(x)}{3 - f(x)}\right| + c$

Answer: $\dfrac{1}{6}\log\left|\dfrac{3 + f(x)}{3 - f(x)}\right| + c$

</details>

---

### Q4. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\displaystyle\int \dfrac{2\tan x + 3}{3\tan x + 4}\,dx = Ax + B\log|3\sin x + 4\cos x| + c$, then the values of $A$ and $B$ respectively are

**Options:**

- **(A)** $-\dfrac{18}{25}, \dfrac{1}{25}$
- **(B)** $-\dfrac{18}{25}, -\dfrac{1}{25}$
- **(C)** $\dfrac{18}{25}, -\dfrac{1}{25}$
- **(D)** $\dfrac{18}{25}, \dfrac{1}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{18}{25}, \dfrac{1}{25}$**

**Detailed Solution:**

Let $I = \displaystyle\int \dfrac{2\tan x + 3}{3\tan x + 4}\,dx$

Converting $\tan x$ into $\sin x$ and $\cos x$, we get:

$I = \displaystyle\int \dfrac{2\left(\dfrac{\sin x}{\cos x}\right) + 3}{3\left(\dfrac{\sin x}{\cos x}\right) + 4}\,dx = \displaystyle\int \dfrac{2\sin x + 3\cos x}{3\sin x + 4\cos x}\,dx$

Let the numerator be expressed as $A(\text{Denominator}) + B\left(\dfrac{d}{dx}(\text{Denominator})\right)$.

$2\sin x + 3\cos x = A(3\sin x + 4\cos x) + B(3\cos x - 4\sin x)$

Comparing the coefficients of $\sin x$ and $\cos x$ on both sides:

$3A - 4B = 2$

$4A + 3B = 3$

Multiplying the first equation by $3$ and the second by $4$, we get:

$9A - 12B = 6$

$16A + 12B = 12$

Adding both equations:

$25A = 18 \Rightarrow A = \dfrac{18}{25}$

Substituting $A$ in the first equation:

$3\left(\dfrac{18}{25}\right) - 4B = 2 \Rightarrow \dfrac{54}{25} - 2 = 4B \Rightarrow 4B = \dfrac{4}{25} \Rightarrow B = \dfrac{1}{25}$

Now, substituting $A$ and $B$ back into the integral:

$I = \displaystyle\int \dfrac{A(3\sin x + 4\cos x) + B(3\cos x - 4\sin x)}{3\sin x + 4\cos x}\,dx$

$I = \displaystyle\int A\,dx + B\displaystyle\int \dfrac{3\cos x - 4\sin x}{3\sin x + 4\cos x}\,dx$

$I = Ax + B\log|3\sin x + 4\cos x| + c$

Therefore, $A = \dfrac{18}{25}$ and $B = \dfrac{1}{25}$.

Answer: $\dfrac{18}{25}, \dfrac{1}{25}$

</details>

---

### Q5. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \sin^3 x \cos^3 x\,dx = \ldots$

**Options:**

- **(A)** $-\dfrac{1}{192}[9\cos 2x - \cos 6x] + c$
- **(B)** $\dfrac{1}{192}[9\cos 2x - \cos 6x] + c$
- **(C)** $-\dfrac{1}{32}[\cos 2x - \cos 6x] + c$
- **(D)** $\dfrac{1}{32}[\cos 2x - \cos 6x] + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\dfrac{1}{192}[9\cos 2x - \cos 6x] + c$**

**Detailed Solution:**

$I = \int \sin^3 x \cos^3 x \, dx$

Using the identity $\sin 2x = 2\sin x \cos x$, we can rewrite the integrand as:

$I = \int \left(\dfrac{\sin 2x}{2}\right)^3 \, dx$

$I = \dfrac{1}{8} \int \sin^3 2x \, dx$

Using the multiple angle identity $\sin 3\theta = 3\sin \theta - 4\sin^3 \theta$, we get $\sin^3 2x = \dfrac{3\sin 2x - \sin 6x}{4}$. Substituting this into the integral:

$I = \dfrac{1}{8} \int \left( \dfrac{3\sin 2x - \sin 6x}{4} \right) \, dx$

$I = \dfrac{1}{32} \int (3\sin 2x - \sin 6x) \, dx$

Integrating term by term:

$I = \dfrac{1}{32} \left( 3 \left( -\dfrac{\cos 2x}{2} \right) - \left( -\dfrac{\cos 6x}{6} \right) \right) + c$

$I = \dfrac{1}{32} \left( -\dfrac{3\cos 2x}{2} + \dfrac{\cos 6x}{6} \right) + c$

Taking the common denominator inside the bracket:

$I = \dfrac{1}{32} \left( \dfrac{-9\cos 2x + \cos 6x}{6} \right) + c$

$I = -\dfrac{1}{192} [9\cos 2x - \cos 6x] + c$

Answer: $-\dfrac{1}{192}[9\cos 2x - \cos 6x] + c$

</details>

---

### Q6. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{5x^{12} + 6x^{11}}{(x^6 + x + 1)^3}\,dx = $

**Options:**

- **(A)** $-\dfrac{x^{12}}{2(x^6 + x + 1)^2} + c$
- **(B)** $-\dfrac{1}{2(x^6 + x + 1)^2} + c$
- **(C)** $\dfrac{x^{12}}{2(x^6 + x + 1)^2} + c$
- **(D)** $\dfrac{1}{2(x^6 + x + 1)^2} + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{x^{12}}{2(x^6 + x + 1)^2} + c$**

**Detailed Solution:**

Let $I = \int \dfrac{5x^{12} + 6x^{11}}{(x^6 + x + 1)^3}\,dx$

Dividing the numerator and the denominator by $x^{18}$, we get:

$I = \int \dfrac{5x^{-6} + 6x^{-7}}{(1 + x^{-5} + x^{-6})^3}\,dx$

Let $1 + x^{-5} + x^{-6} = t$

Differentiating both sides with respect to $x$:

$(-5x^{-6} - 6x^{-7})\,dx = dt$

$(5x^{-6} + 6x^{-7})\,dx = -dt$

Substituting this into the integral:

$I = \int \dfrac{-dt}{t^3}$

$I = -\int t^{-3}\,dt$

$I = -\left(\dfrac{t^{-2}}{-2}\right) + c$

$I = \dfrac{1}{2t^2} + c$

Substituting back $t = 1 + x^{-5} + x^{-6} = \dfrac{x^6 + x + 1}{x^6}$:

$I = \dfrac{1}{2\left(\dfrac{x^6 + x + 1}{x^6}\right)^2} + c$

$I = \dfrac{x^{12}}{2(x^6 + x + 1)^2} + c$

Answer: $\dfrac{x^{12}}{2(x^6 + x + 1)^2} + c$

</details>

---

### Q7. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{x^3 + x^2 + 2x + 1}{x^2 - x + 1} dx = \ldots$

**Options:**

- **(A)** $\dfrac{x^2}{2} - 2x - \dfrac{3}{2}\log|x^2 - x + 1| + \dfrac{1}{\sqrt{3}}\tan^{-1}\left(\dfrac{2x-1}{\sqrt{3}}\right) + c$
- **(B)** $\dfrac{x^2}{2} + 2x + \dfrac{3}{2}\log|x^2 - x + 1| + \dfrac{1}{\sqrt{3}}\tan^{-1}\left(\dfrac{2x-1}{\sqrt{3}}\right) + c$
- **(C)** $\dfrac{x^2}{2} + 2x - \dfrac{3}{2}\log|x^2 - x + 1| - \dfrac{1}{\sqrt{3}}\tan^{-1}\left(\dfrac{2x-1}{\sqrt{3}}\right) + c$
- **(D)** $\dfrac{x^2}{2} - 2x - \dfrac{3}{2}\log|x^2 - x + 1| - \dfrac{1}{\sqrt{3}}\tan^{-1}\left(\dfrac{2x-1}{\sqrt{3}}\right) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{x^2}{2} + 2x + \dfrac{3}{2}\log|x^2 - x + 1| + \dfrac{1}{\sqrt{3}}\tan^{-1}\left(\dfrac{2x-1}{\sqrt{3}}\right) + c$**

**Detailed Solution:**

Using polynomial long division, we can express the integrand as:

$\dfrac{x^3 + x^2 + 2x + 1}{x^2 - x + 1} = x + 2 + \dfrac{3x - 1}{x^2 - x + 1}$

Integrating both sides with respect to $x$:

$\int \dfrac{x^3 + x^2 + 2x + 1}{x^2 - x + 1} dx = \int (x + 2) dx + \int \dfrac{3x - 1}{x^2 - x + 1} dx$

The first integral is:

$\int (x + 2) dx = \dfrac{x^2}{2} + 2x$

For the second integral, we express the numerator in terms of the derivative of the denominator:

$3x - 1 = \dfrac{3}{2}(2x - 1) + \dfrac{1}{2}$

Thus, the second integral becomes:

$\int \dfrac{3x - 1}{x^2 - x + 1} dx = \dfrac{3}{2} \int \dfrac{2x - 1}{x^2 - x + 1} dx + \dfrac{1}{2} \int \dfrac{1}{x^2 - x + 1} dx$

$= \dfrac{3}{2} \log|x^2 - x + 1| + \dfrac{1}{2} \int \dfrac{1}{(x - \dfrac{1}{2})^2 + (\dfrac{\sqrt{3}}{2})^2} dx$

$= \dfrac{3}{2} \log|x^2 - x + 1| + \dfrac{1}{2} \left( \dfrac{2}{\sqrt{3}} \right) \tan^{-1}\left( \dfrac{x - \dfrac{1}{2}}{\dfrac{\sqrt{3}}{2}} \right)$

$= \dfrac{3}{2} \log|x^2 - x + 1| + \dfrac{1}{\sqrt{3}} \tan^{-1}\left( \dfrac{2x - 1}{\sqrt{3}} \right)$

Combining all the terms, we get:

$\dfrac{x^2}{2} + 2x + \dfrac{3}{2} \log|x^2 - x + 1| + \dfrac{1}{\sqrt{3}} \tan^{-1}\left( \dfrac{2x - 1}{\sqrt{3}} \right) + c$

Answer: $\dfrac{x^2}{2} + 2x + \dfrac{3}{2}\log|x^2 - x + 1| + \dfrac{1}{\sqrt{3}}\tan^{-1}\left(\dfrac{2x-1}{\sqrt{3}}\right) + c$

</details>

---

### Q8. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \tan^{-1} \sqrt{x} \, dx = \ldots$

**Options:**

- **(A)** $x \tan^{-1} x - \dfrac{1}{2}\log(1 + x^2) + c$
- **(B)** $x \tan^{-1} x + \dfrac{1}{2}\log(1 + x^2) + c$
- **(C)** $(x+1)\tan^{-1}\sqrt{x} + \sqrt{x} + c$
- **(D)** $(x+1)\tan^{-1}\sqrt{x} - \sqrt{x} + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(x+1)\tan^{-1}\sqrt{x} - \sqrt{x} + c$**

**Detailed Solution:**

Let $I = \int \tan^{-1} \sqrt{x} \, dx$

Substitute $x = t^2$, which gives $dx = 2t \, dt$

$I = \int \tan^{-1}(t) \cdot 2t \, dt$

Using integration by parts, taking $\tan^{-1} t$ as the first function and $2t$ as the second function:

$I = \tan^{-1}(t) \cdot t^2 - \int \dfrac{1}{1+t^2} \cdot t^2 \, dt$

$I = t^2 \tan^{-1} t - \int \dfrac{t^2 + 1 - 1}{1+t^2} \, dt$

$I = t^2 \tan^{-1} t - \int \left(1 - \dfrac{1}{1+t^2}\right) \, dt$

$I = t^2 \tan^{-1} t - (t - \tan^{-1} t) + c$

$I = (t^2 + 1) \tan^{-1} t - t + c$

Substituting back $t = \sqrt{x}$:

$I = (x + 1) \tan^{-1} \sqrt{x} - \sqrt{x} + c$

Answer: $(x+1)\tan^{-1}\sqrt{x} - \sqrt{x} + c$

</details>

---

### Q9. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \sec^2 2x \cdot \text{cosec}^2 2x \, dx = \ldots$

**Options:**

- **(A)** $\dfrac{1}{2} \tan x + c$
- **(B)** $\cot 2x + \tan 2x + c$
- **(C)** $\sec 2x + c$
- **(D)** $\dfrac{1}{2}(\tan 2x - \cot 2x) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{2}(\tan 2x - \cot 2x) + c$**

**Detailed Solution:**

$\int \sec^2 2x \cdot \text{cosec}^2 2x \, dx$

$= \int \dfrac{1}{\cos^2 2x \sin^2 2x} \, dx$

$= \int \dfrac{\sin^2 2x + \cos^2 2x}{\cos^2 2x \sin^2 2x} \, dx$

$= \int \left( \dfrac{\sin^2 2x}{\cos^2 2x \sin^2 2x} + \dfrac{\cos^2 2x}{\cos^2 2x \sin^2 2x} \right) \, dx$

$= \int (\sec^2 2x + \text{cosec}^2 2x) \, dx$

$= \dfrac{\tan 2x}{2} - \dfrac{\cot 2x}{2} + c$

$= \dfrac{1}{2}(\tan 2x - \cot 2x) + c$

Answer: $\dfrac{1}{2}(\tan 2x - \cot 2x) + c$

</details>

---

### Q10. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int(\sqrt{\tan x} + \sqrt{\cot x})\,dx = a\tan^{-1}\left(\dfrac{\tan x - 1}{\sqrt{b\tan x}}\right) + c$, for $x \in \left(0, \dfrac{\pi}{2}\right)$, then $a^{10} + b^5 = \cdots$

**Options:**

- **(A)** $16$
- **(B)** $64$
- **(C)** $36$
- **(D)** $100$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $64$**

**Detailed Solution:**

Let $I = \int(\sqrt{\tan x} + \sqrt{\cot x})\,dx = \int \dfrac{\tan x + 1}{\sqrt{\tan x}} dx$

Let $\tan x = t^2 \Rightarrow \sec^2 x \, dx = 2t \, dt \Rightarrow dx = \dfrac{2t}{1+t^4} dt$

Substituting these into the integral, we get:

$I = \int \dfrac{t^2 + 1}{t} \dfrac{2t}{1+t^4} dt = 2 \int \dfrac{t^2 + 1}{t^4 + 1} dt$

Dividing the numerator and the denominator by $t^2$:

$I = 2 \int \dfrac{1 + \dfrac{1}{t^2}}{t^2 + \dfrac{1}{t^2}} dt = 2 \int \dfrac{1 + \dfrac{1}{t^2}}{\left(t - \dfrac{1}{t}\right)^2 + 2} dt$

Let $t - \dfrac{1}{t} = u \Rightarrow \left(1 + \dfrac{1}{t^2}\right) dt = du$

$I = 2 \int \dfrac{du}{u^2 + (\sqrt{2})^2} = \dfrac{2}{\sqrt{2}} \tan^{-1}\left(\dfrac{u}{\sqrt{2}}\right) + c$

$I = \sqrt{2} \tan^{-1}\left(\dfrac{t - \dfrac{1}{t}}{\sqrt{2}}\right) + c = \sqrt{2} \tan^{-1}\left(\dfrac{t^2 - 1}{\sqrt{2}t}\right) + c$

Substituting back $t = \sqrt{\tan x}$:

$I = \sqrt{2} \tan^{-1}\left(\dfrac(\tan x - 1){\sqrt{2\tan x}}\right) + c$

Comparing this with the given expression $a\tan^{-1}\left(\dfrac{\tan x - 1}{\sqrt{b\tan x}}\right) + c$, we get $a = \sqrt{2}$ and $b = 2$.

Therefore, $a^{10} + b^5 = (\sqrt{2})^{10} + 2^5 = 32 + 32 = 64$.

Answer: $64$

</details>

---

### Q11. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int x(a-x)^9\,dx = \dfrac{[f(x)]^{11}}{11} - a\dfrac{[f(x)]^{10}}{10} + c$, where $c$ is a constant of integration, then $f'(x) = \cdots$

**Options:**

- **(A)** $a$
- **(B)** $-1$
- **(C)** $-a$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-1$**

**Detailed Solution:**

Let $I = \int x(a-x)^9 \, dx$

Substitute $a-x = t$, which gives $dx = -dt$ and $x = a-t$

$I = \int (a-t) t^9 (-dt) = \int (t^{10} - a t^9) \, dt$

$I = \dfrac{t^{11}}{11} - a \dfrac{t^{10}}{10} + c$

Substituting back $t = a-x$, we get:

$I = \dfrac{(a-x)^{11}}{11} - a \dfrac{(a-x)^{10}}{10} + c$

Comparing this with the given expression $\dfrac{[f(x)]^{11}}{11} - a \dfrac{[f(x)]^{10}}{10} + c$, we get:

$f(x) = a-x$

Differentiating with respect to $x$, we obtain:

$f'(x) = -1$

Answer: $-1$

</details>

---

### Q12. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The integral $\int \dfrac{\csc x}{\cos^2[1 + \log(\tan \dfrac{x}{2})]}\ dx$ is equal to:

**Options:**

- **(A)** $\tan[1 + \log(\tan \dfrac{x}{2})] + c$
- **(B)** $\dfrac{1}{2}\tan[1 + \log(\tan \dfrac{x}{2})] + c$
- **(C)** $2\tan[1 + \log(\tan \dfrac{x}{2})] + c$
- **(D)** $\dfrac{1}{4}\tan[1 + \log(\tan \dfrac{x}{2})] + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\tan[1 + \log(\tan \dfrac{x}{2})] + c$**

**Detailed Solution:**

Let $t = 1 + \log(\tan \dfrac{x}{2})$

Differentiating with respect to $x$:

$dt = \dfrac{1}{\tan \dfrac{x}{2}} \cdot \sec^2 \dfrac{x}{2} \cdot \dfrac{1}{2} dx$

$dt = \dfrac{\cos \dfrac{x}{2}}{\sin \dfrac{x}{2}} \cdot \dfrac{1}{\cos^2 \dfrac{x}{2}} \cdot \dfrac{1}{2} dx$

$dt = \dfrac{1}{2 \sin \dfrac{x}{2} \cos \dfrac{x}{2}} dx$

$dt = \dfrac{1}{\sin x} dx = \csc x\ dx$

Substituting in the given integral:

$I = \int \dfrac{dt}{\cos^2 t} = \int \sec^2 t\ dt$

$I = \tan t + c$

$I = \tan[1 + \log(\tan \dfrac{x}{2})] + c$

Answer: $\tan[1 + \log(\tan \dfrac{x}{2})] + c$

</details>

---

### Q13. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{x}{x^{5/2} + 4x^{3/2}}\ dx = \ldots$

**Options:**

- **(A)** $3\log|x^{5/2} + 4x^{3/2}| + c$
- **(B)** $\dfrac{1}{2}\log|x + 4| + c$
- **(C)** $4\sec(x^{3/2}) + \log\left(\tan\left(\dfrac{x}{2}\right)\right) + c$
- **(D)** $\tan^{-1}\left(\dfrac{\sqrt{x}}{2}\right) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\tan^{-1}\left(\dfrac{\sqrt{x}}{2}\right) + c$**

**Detailed Solution:**

Let $I = \int \dfrac{x}{x^{5/2} + 4x^{3/2}}\ dx$

Factoring out $x^{3/2}$ from the denominator:

$I = \int \dfrac{x}{x^{3/2}(x + 4)}\ dx$

$I = \int \dfrac{1}{\sqrt{x}(x + 4)}\ dx$

Substitute $x = t^2 \Rightarrow dx = 2t\ dt$

$I = \int \dfrac{2t}{t(t^2 + 4)}\ dt$

$I = \int \dfrac{2}{t^2 + 4}\ dt$

Using the standard integral $\int \dfrac{1}{t^2 + a^2}\ dt = \dfrac{1}{a} \tan^{-1}\left(\dfrac{t}{a}\right) + c$ with $a = 2$:

$I = 2 \left( \dfrac{1}{2} \tan^{-1}\left(\dfrac{t}{2}\right) \right) + c$

$I = \tan^{-1}\left(\dfrac{t}{2}\right) + c$

Substituting back $t = \sqrt{x}$:

$I = \tan^{-1}\left(\dfrac{\sqrt{x}}{2}\right) + c$

Answer: $\tan^{-1}\left(\dfrac{\sqrt{x}}{2}\right) + c$

</details>

---

### Q14. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\displaystyle\int \sqrt{1 + \sec x}\, dx = 2\sin^{-1}(f(x)) + c$, then

**Options:**

- **(A)** $f(x) = \sqrt{2}\sin\left(\dfrac{x}{2}\right)$
- **(B)** $f(x) = \sqrt{2}\cos\left(\dfrac{x}{2}\right)$
- **(C)** $f(x) = \dfrac{1}{\sqrt{2}}\sin\left(\dfrac{x}{2}\right)$
- **(D)** $f(x) = \dfrac{1}{\sqrt{2}}\cos\left(\dfrac{x}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $f(x) = \sqrt{2}\sin\left(\dfrac{x}{2}\right)$**

**Detailed Solution:**

Let $I = \int \sqrt{1 + \sec x} \, dx = \int \sqrt{1 + \dfrac{1}{\cos x}} \, dx$

$I = \int \sqrt{\dfrac{1 + \cos x}{\cos x}} \, dx$

Using $1 + \cos x = 2\cos^2\left(\dfrac{x}{2}\right)$ and $\cos x = 1 - 2\sin^2\left(\dfrac{x}{2}\right)$:

$I = \int \dfrac{\sqrt{2}\cos\left(\dfrac{x}{2}\right)}{\sqrt{1 - 2\sin^2\left(\dfrac{x}{2}\right)}} \, dx$

Let $\sqrt{2}\sin\left(\dfrac{x}{2}\right) = t$

Differentiating both sides, we get $\dfrac{\sqrt{2}}{2}\cos\left(\dfrac{x}{2}\right) dx = dt \Rightarrow \sqrt{2}\cos\left(\dfrac{x}{2}\right) dx = 2dt$

Substituting in the integral:

$I = \int \dfrac{2dt}{\sqrt{1 - t^2}} = 2\sin^{-1}(t) + c$

$I = 2\sin^{-1}\left(\sqrt{2}\sin\left(\dfrac{x}{2}\right)\right) + c$

Comparing with $2\sin^{-1}(f(x)) + c$, we get $f(x) = \sqrt{2}\sin\left(\dfrac{x}{2}\right)$

Answer: $f(x) = \sqrt{2}\sin\left(\dfrac{x}{2}\right)$

</details>

---

### Q15. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\displaystyle\int \dfrac{x^3 \sin(\tan^{-1}(x^4))}{1 + x^8}\, dx = $

**Options:**

- **(A)** $\dfrac{1}{4}\cos(\tan^{-1}(x^4)) + c$
- **(B)** $\dfrac{1}{4}\sin(\tan^{-1}(x^4)) + c$
- **(C)** $\dfrac{1}{4}\sec(\tan^{-1}(x^4)) + c$
- **(D)** $-\dfrac{1}{4}\cos(\tan^{-1}(x^4)) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\dfrac{1}{4}\cos(\tan^{-1}(x^4)) + c$**

**Detailed Solution:**

Let $t = \tan^{-1}(x^4)$.

Differentiating both sides with respect to $x$, we get:

$dt = \dfrac{1}{1 + (x^4)^2} \cdot 4x^3 \, dx$

$dt = \dfrac{4x^3}{1 + x^8} \, dx$

$\dfrac{dt}{4} = \dfrac{x^3}{1 + x^8} \, dx$

Substituting this into the given integral:

$\displaystyle\int \dfrac{x^3 \sin(\tan^{-1}(x^4))}{1 + x^8} \, dx = \int \sin(t) \cdot \dfrac{dt}{4}$

$= \dfrac{1}{4} \int \sin(t) \, dt$

$= -\dfrac{1}{4} \cos(t) + c$

Substituting back $t = \tan^{-1}(x^4)$:

$= -\dfrac{1}{4} \cos(\tan^{-1}(x^4)) + c$

Answer: $-\dfrac{1}{4}\cos(\tan^{-1}(x^4)) + c$

</details>

---

### Q16. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\displaystyle\int \dfrac{1 + \cos a\cos x}{\cos a + \cos x}\,dx =$

**Options:**

- **(A)** $\sin a\,\log\left|\dfrac{\cot\frac{a}{2} + \tan\frac{x}{2}}{\cot\frac{a}{2} - \tan\frac{x}{2}}\right| + x\cos a + c$
- **(B)** $\sin a\,\log\left|\dfrac{\cot\frac{a}{2} - \tan\frac{x}{2}}{\cot\frac{a}{2} + \tan\frac{x}{2}}\right| + x\cos a + c$
- **(C)** $\sin a\,\log\left|\dfrac{\cot\frac{a}{2} + \tan\frac{x}{2}}{\cot\frac{a}{2} - \tan\frac{x}{2}}\right| + x\sin a + c$
- **(D)** $\sin a\,\log\left|\dfrac{\cot\frac{a}{2} - \tan\frac{x}{2}}{\cot\frac{a}{2} + \tan\frac{x}{2}}\right| + x\sin a + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sin a\,\log\left|\dfrac{\cot\frac{a}{2} + \tan\frac{x}{2}}{\cot\frac{a}{2} - \tan\frac{x}{2}}\right| + x\cos a + c$**

**Detailed Solution:**

Let $I = \displaystyle\int \dfrac{1 + \cos a\cos x}{\cos a + \cos x}\,dx$

We can rewrite the numerator as:

$1 + \cos a\cos x = 1 - \cos^2 a + \cos^2 a + \cos a\cos x = \sin^2 a + \cos a(\cos a + \cos x)$

Substituting this into the integral:

$I = \displaystyle\int \dfrac{\sin^2 a + \cos a(\cos a + \cos x)}{\cos a + \cos x}\,dx$

$I = \displaystyle\int \cos a \,dx + \sin^2 a \displaystyle\int \dfrac{1}{\cos a + \cos x}\,dx$

$I = x\cos a + \sin^2 a \displaystyle\int \dfrac{1}{\cos a + \dfrac{1 - \tan^2\dfrac{x}{2}}{1 + \tan^2\dfrac{x}{2}}}\,dx$

$I = x\cos a + \sin^2 a \displaystyle\int \dfrac{1 + \tan^2\dfrac{x}{2}}{\cos a\left(1 + \tan^2\dfrac{x}{2}\right) + 1 - \tan^2\dfrac{x}{2}}\,dx$

$I = x\cos a + \sin^2 a \displaystyle\int \dfrac{\sec^2\dfrac{x}{2}}{(\cos a + 1) - \tan^2\dfrac{x}{2}(1 - \cos a)}\,dx$

Let $\tan\dfrac{x}{2} = t \Rightarrow \dfrac{1}{2}\sec^2\dfrac{x}{2}\,dx = dt \Rightarrow \sec^2\dfrac{x}{2}\,dx = 2\,dt$

$I = x\cos a + \sin^2 a \displaystyle\int \dfrac{2\,dt}{2\cos^2\dfrac{a}{2} - 2t^2\sin^2\dfrac{a}{2}}$

$I = x\cos a + \dfrac{\sin^2 a}{\sin^2\dfrac{a}{2}} \displaystyle\int \dfrac{dt}{\dfrac{\cos^2\dfrac{a}{2}}{\sin^2\dfrac{a}{2}} - t^2}$

$I = x\cos a + \dfrac{4\sin^2\dfrac{a}{2}\cos^2\dfrac{a}{2}}{\sin^2\dfrac{a}{2}} \displaystyle\int \dfrac{dt}{\cot^2\dfrac{a}{2} - t^2}$

$I = x\cos a + 4\cos^2\dfrac{a}{2} \left( \dfrac{1}{2\cot\dfrac{a}{2}} \log\left|\dfrac{\cot\dfrac{a}{2} + t}{\cot\dfrac{a}{2} - t}\right| \right) + c$

$I = x\cos a + 4\cos^2\dfrac{a}{2} \left( \dfrac{\sin\dfrac{a}{2}}{2\cos\dfrac{a}{2}} \right) \log\left|\dfrac{\cot\dfrac{a}{2} + t}{\cot\dfrac{a}{2} - t}\right| + c$

$I = x\cos a + 2\sin\dfrac{a}{2}\cos\dfrac{a}{2} \log\left|\dfrac{\cot\dfrac{a}{2} + \tan\dfrac{x}{2}}{\cot\dfrac{a}{2} - \tan\dfrac{x}{2}}\right| + c$

$I = x\cos a + \sin a \log\left|\dfrac{\cot\dfrac{a}{2} + \tan\dfrac{x}{2}}{\cot\dfrac{a}{2} - \tan\dfrac{x}{2}}\right| + c$

Answer: $\sin a\,\log\left|\dfrac{\cot\frac{a}{2} + \tan\frac{x}{2}}{\cot\frac{a}{2} - \tan\frac{x}{2}}\right| + x\cos a + c$

</details>

---

### Q17. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \sqrt{e^x - 1}\,dx = a\sqrt{e^x - 1} + b\tan^{-1}(\sqrt{e^x - 1}) + c$, then

**Options:**

- **(A)** $a + b = 0$
- **(B)** $a - b = 0$
- **(C)** $a = 2b$
- **(D)** $2a = b$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $a + b = 0$**

**Detailed Solution:**

Let $e^x - 1 = t^2$

Differentiating both sides, $e^x dx = 2t dt$

$dx = \dfrac{2t}{e^x} dt = \dfrac{2t}{t^2 + 1} dt$

Substituting into the integral:

$\int \sqrt{e^x - 1} dx = \int t \cdot \dfrac{2t}{t^2 + 1} dt$

$= 2 \int \dfrac{t^2}{t^2 + 1} dt$

$= 2 \int \dfrac{t^2 + 1 - 1}{t^2 + 1} dt$

$= 2 \int \left(1 - \dfrac{1}{t^2 + 1}\right) dt$

$= 2t - 2\tan^{-1}(t) + c$

Substituting back $t = \sqrt{e^x - 1}$:

$= 2\sqrt{e^x - 1} - 2\tan^{-1}(\sqrt{e^x - 1}) + c$

Comparing with $a\sqrt{e^x - 1} + b\tan^{-1}(\sqrt{e^x - 1}) + c$, we get:

$a = 2$ and $b = -2$

Therefore, $a + b = 2 - 2 = 0$

Answer: $a + b = 0$

</details>

---

### Q18. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int f(x)\,dx = g(x) + c$, then $\int x\,f(x^2)\,dx =$

**Options:**

- **(A)** $2g(x^2) + c$
- **(B)** $2g(x) + c$
- **(C)** $\dfrac{1}{2}g(x^2) + c$
- **(D)** $\dfrac{1}{2}g(x) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{2}g(x^2) + c$**

**Detailed Solution:**

Let $I = \int x\,f(x^2)\,dx$

Substitute $x^2 = t$

Differentiating both sides, $2x\,dx = dt \Rightarrow x\,dx = \dfrac{1}{2}dt$

$I = \dfrac{1}{2}\int f(t)\,dt$

Given $\int f(x)\,dx = g(x) + c$

$I = \dfrac{1}{2}g(t) + C$

Substituting $t = x^2$, we get $I = \dfrac{1}{2}g(x^2) + C$

Answer: $\dfrac{1}{2}g(x^2) + c$

</details>

---

### Q19. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \dfrac{4x+5}{2x+1} dx = $

**Options:**

- **(A)** $2x + \dfrac{3}{2}\log|2x+1| + c$
- **(B)** $2x - \dfrac{3}{2}\log|2x+1| + c$
- **(C)** $x + \dfrac{3}{2}\log|2x+1| + c$
- **(D)** $x - \dfrac{3}{2}\log|2x+1| + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2x + \dfrac{3}{2}\log|2x+1| + c$**

**Detailed Solution:**

Let $I = \int \dfrac{4x+5}{2x+1} dx$

Rewriting the numerator in terms of the denominator:

$I = \int \dfrac{2(2x+1) + 3}{2x+1} dx$

$I = \int \left( 2 + \dfrac{3}{2x+1} \right) dx$

Integrating term by term:

$I = \int 2 dx + \int \dfrac{3}{2x+1} dx$

$I = 2x + \dfrac{3}{2}\log|2x+1| + c$

Answer: $2x + \dfrac{3}{2}\log|2x+1| + c$

</details>

---

### Q20. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \sqrt{x} \sec\left(x^{\dfrac{3}{2}}\right) \tan\left(x^{\dfrac{3}{2}}\right) dx = $

**Options:**

- **(A)** $\dfrac{2}{3}\sin\left(x^{\dfrac{3}{2}}\right) + c$
- **(B)** $\dfrac{2}{3}\tan\left(x^{\dfrac{3}{2}}\right) + c$
- **(C)** $\dfrac{2}{3}\cot\left(x^{\dfrac{3}{2}}\right) + c$
- **(D)** $\dfrac{2}{3}\sec\left(x^{\dfrac{3}{2}}\right) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{2}{3}\sec\left(x^{\dfrac{3}{2}}\right) + c$**

**Detailed Solution:**

Let $I = \int \sqrt{x} \sec\left(x^{\dfrac{3}{2}}\right) \tan\left(x^{\dfrac{3}{2}}\right) dx$

Substituting $t = x^{\dfrac{3}{2}}$

Differentiating with respect to $x$, we get

$dt = \dfrac{3}{2} x^{\dfrac{1}{2}} dx = \dfrac{3}{2} \sqrt{x} dx$

$\Rightarrow \sqrt{x} dx = \dfrac{2}{3} dt$

Substituting these values in the integral, we get

$I = \dfrac{2}{3} \int \sec(t) \tan(t) dt$

$I = \dfrac{2}{3} \sec(t) + c$

Substituting $t = x^{\dfrac{3}{2}}$, we get

$I = \dfrac{2}{3} \sec\left(x^{\dfrac{3}{2}}\right) + c$

Answer: $\dfrac{2}{3}\sec\left(x^{\dfrac{3}{2}}\right) + c$

</details>

---

### Q21. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \dfrac{\log(\log x)}{4x(\log x)^2} dx = k \left[\dfrac{1 + \log(\log x)}{\log x}\right] + c$, then the value of $k$ is...

**Options:**

- **(A)** $\dfrac{1}{4}$
- **(B)** $\dfrac{1}{2}$
- **(C)** $-\dfrac{1}{2}$
- **(D)** $-\dfrac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\dfrac{1}{4}$**

**Detailed Solution:**

Let $\log x = t$, then $\dfrac{1}{x} dx = dt$

$I = \dfrac{1}{4} \int \dfrac{\log t}{t^2} dt$

Using integration by parts, taking $\log t$ as the first function and $t^{-2}$ as the second function:

$I = \dfrac{1}{4} \left[ \log t \left(-\dfrac{1}{t}\right) - \int \dfrac{1}{t} \left(-\dfrac{1}{t}\right) dt \right]$

$I = \dfrac{1}{4} \left[ -\dfrac{\log t}{t} + \int t^{-2} dt \right]$

$I = \dfrac{1}{4} \left[ -\dfrac{\log t}{t} - \dfrac{1}{t} \right] + c$

$I = -\dfrac{1}{4} \left[ \dfrac{1 + \log t}{t} \right] + c$

Substituting $t = \log x$:

$I = -\dfrac{1}{4} \left[ \dfrac{1 + \log(\log x)}{\log x} \right] + c$

Comparing with the given expression, we get $k = -\dfrac{1}{4}$.

Answer: $-\dfrac{1}{4}$

</details>

---

### Q22. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int \dfrac{dx}{x \sqrt{1 - x^3}}$ is equal to...

**Options:**

- **(A)** $\dfrac{1}{3} \log\left|\dfrac{\sqrt{1 - x^3} + 1}{\sqrt{1 - x^3} - 1}\right| + c$
- **(B)** $\dfrac{1}{3} \log\left|\dfrac{\sqrt{1 - x^3} - 1}{\sqrt{1 - x^3} + 1}\right| + c$
- **(C)** $\dfrac{1}{3} \log\left|\dfrac{\sqrt{1 - x^3} - 1}{\sqrt{1 - x^3} - 1}\right| + c$
- **(D)** $\dfrac{2}{3} \log\left|\dfrac{\sqrt{1 - x^3} - 1}{\sqrt{1 - x^3} + 1}\right| + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{3} \log\left|\dfrac{\sqrt{1 - x^3} - 1}{\sqrt{1 - x^3} + 1}\right| + c$**

**Detailed Solution:**

Let $I = \int \dfrac{dx}{x \sqrt{1 - x^3}}$

Multiplying the numerator and the denominator by $x^2$, we get

$I = \int \dfrac{x^2 dx}{x^3 \sqrt{1 - x^3}}$

Let $1 - x^3 = t^2$

Differentiating both sides, we get

$-3x^2 dx = 2t dt \Rightarrow x^2 dx = -\dfrac{2}{3} t dt$

Substituting these values in the integral, we get

$I = \int \dfrac{-\dfrac{2}{3} t dt}{(1 - t^2) t}$

$I = -\dfrac{2}{3} \int \dfrac{dt}{1 - t^2}$

$I = \dfrac{2}{3} \int \dfrac{dt}{t^2 - 1}$

Using the standard integral formula $\int \dfrac{dx}{x^2 - a^2} = \dfrac{1}{2a} \log\left|\dfrac{x - a}{x + a}\right| + c$, we get

$I = \dfrac{2}{3} \left( \dfrac{1}{2} \log\left|\dfrac{t - 1}{t + 1}\right| \right) + c$

$I = \dfrac{1}{3} \log\left|\dfrac{t - 1}{t + 1}\right| + c$

Substituting $t = \sqrt{1 - x^3}$, we get

$I = \dfrac{1}{3} \log\left|\dfrac{\sqrt{1 - x^3} - 1}{\sqrt{1 - x^3} + 1}\right| + c$

Answer: $\dfrac{1}{3} \log\left|\dfrac{\sqrt{1 - x^3} - 1}{\sqrt{1 - x^3} + 1}\right| + c$

</details>

---

### Q23. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int \dfrac{dx}{3 + \sin 2x + \sin^2 x} = $ .........

**Options:**

- **(A)** $\dfrac{1}{\sqrt{13}} \tan^{-1}\left(\dfrac{4\tan x + 1}{\sqrt{13}}\right) + c$
- **(B)** $\dfrac{2}{\sqrt{11}} \tan^{-1}\left(\dfrac{4\tan x + 2}{\sqrt{11}}\right) + c$
- **(C)** $\dfrac{1}{11} \tan^{-1}\left(\dfrac{2\tan x + 1}{11}\right) + c$
- **(D)** $\dfrac{1}{\sqrt{11}} \tan^{-1}\left(\dfrac{4\tan x + 1}{\sqrt{11}}\right) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{\sqrt{11}} \tan^{-1}\left(\dfrac{4\tan x + 1}{\sqrt{11}}\right) + c$**

**Detailed Solution:**

Let $I = \int \dfrac{dx}{3 + \sin 2x + \sin^2 x}$

Dividing the numerator and the denominator by $\cos^2 x$:

$I = \int \dfrac{\sec^2 x \, dx}{3\sec^2 x + 2\tan x + \tan^2 x}$

$I = \int \dfrac{\sec^2 x \, dx}{3(1 + \tan^2 x) + 2\tan x + \tan^2 x}$

$I = \int \dfrac{\sec^2 x \, dx}{4\tan^2 x + 2\tan x + 3}$

Substituting $\tan x = t$, which gives $\sec^2 x \, dx = dt$:

$I = \int \dfrac{dt}{4t^2 + 2t + 3}$

$I = \dfrac{1}{4} \int \dfrac{dt}{t^2 + \dfrac{1}{2}t + \dfrac{3}{4}}$

Completing the square in the denominator:

$I = \dfrac{1}{4} \int \dfrac{dt}{\left(t + \dfrac{1}{4}\right)^2 + \dfrac{11}{16}}$

Using the standard integral $\int \dfrac{dx}{x^2 + a^2} = \dfrac{1}{a} \tan^{-1}\left(\dfrac{x}{a}\right) + c$:

$I = \dfrac{1}{4} \cdot \dfrac{1}{\dfrac{\sqrt{11}}{4}} \tan^{-1}\left(\dfrac{t + \dfrac{1}{4}}{\dfrac{\sqrt{11}}{4}}\right) + c$

$I = \dfrac{1}{\sqrt{11}} \tan^{-1}\left(\dfrac{4t + 1}{\sqrt{11}}\right) + c$

Substituting back $t = \tan x$:

$I = \dfrac{1}{\sqrt{11}} \tan^{-1}\left(\dfrac{4\tan x + 1}{\sqrt{11}}\right) + c$

Answer: $\dfrac{1}{\sqrt{11}} \tan^{-1}\left(\dfrac{4\tan x + 1}{\sqrt{11}}\right) + c$

</details>

---

### Q24. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int \dfrac{x^2 + 1}{(x + 1)^2} dx = $ ............

**Options:**

- **(A)** $x - 2\log|x + 1| - \dfrac{2}{x + 1} + c$
- **(B)** $x - 2\log|x + 1| + \dfrac{2}{x + 1} + c$
- **(C)** $x + 2\log|x + 1| + c$
- **(D)** $x - 2\log|x + 1| + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x - 2\log|x + 1| - \dfrac{2}{x + 1} + c$**

**Detailed Solution:**

Let $I = \int \dfrac{x^2 + 1}{(x + 1)^2} dx$

Adding and subtracting $2x$ in the numerator:

$I = \int \dfrac{x^2 + 2x + 1 - 2x}{(x + 1)^2} dx$

$I = \int \dfrac{(x + 1)^2 - 2x}{(x + 1)^2} dx$

$I = \int \left( 1 - \dfrac{2x}{(x + 1)^2} \right) dx$

Adding and subtracting $2$ in the numerator of the second term:

$I = \int \left( 1 - \dfrac{2(x + 1) - 2}{(x + 1)^2} \right) dx$

$I = \int \left( 1 - \dfrac{2}{x + 1} + \dfrac{2}{(x + 1)^2} \right) dx$

Integrating with respect to $x$:

$I = x - 2\log|x + 1| + 2\left(\dfrac{-1}{x + 1}\right) + c$

$I = x - 2\log|x + 1| - \dfrac{2}{x + 1} + c$

Answer: $x - 2\log|x + 1| - \dfrac{2}{x + 1} + c$

</details>

---

### Q25. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int \dfrac{1}{\cos x \cdot \log\left(\tan\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right)\right)} dx$ is....

**Options:**

- **(A)** $\csc\left(\dfrac{x}{2}\right) + \cot\left(\dfrac{x}{2}\right) + c$
- **(B)** $\sec^2(2x) + \log x + c$
- **(C)** $\log\left|\log\left|\tan\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right)\right|\right| + c$
- **(D)** $\tan\left[\log\left|\sec\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right)\right|\right] + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log\left|\log\left|\tan\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right)\right|\right| + c$**

**Detailed Solution:**

Let $t = \log\left(\tan\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right)\right)$

Differentiating with respect to $x$:

$dt = \dfrac{1}{\tan\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right)} \cdot \sec^2\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right) \cdot \dfrac{1}{2} dx$

$dt = \dfrac{\cos\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right)}{\sin\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right)} \cdot \dfrac{1}{\cos^2\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right)} \cdot \dfrac{1}{2} dx$

$dt = \dfrac{1}{2 \sin\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right) \cos\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right)} dx$

Using the identity $\sin(2\theta) = 2 \sin\theta \cos\theta$:

$dt = \dfrac{1}{\sin\left(\dfrac{\pi}{2} + x\right)} dx$

$dt = \dfrac{1}{\cos x} dx$

Substituting this into the given integral:

$\int \dfrac{1}{\cos x \cdot \log\left(\tan\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right)\right)} dx = \int \dfrac{1}{t} dt$

$= \log|t| + c$

$= \log\left|\log\left|\tan\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right)\right|\right| + c$

Answer: $\log\left|\log\left|\tan\left(\dfrac{\pi}{4} + \dfrac{x}{2}\right)\right|\right| + c$

</details>

---

### Q26. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int \dfrac{1}{\sin x - \sqrt{3} \cos x} dx$ is....

**Options:**

- **(A)** $\dfrac{1}{2}\log\left|\csc\left(x - \dfrac{\pi}{3}\right) + \cot\left(x - \dfrac{\pi}{3}\right)\right| + c$
- **(B)** $\dfrac{1}{2}\log\left|\csc\left(x - \dfrac{\pi}{3}\right) - \cot\left(x - \dfrac{\pi}{3}\right)\right| + c$
- **(C)** $\dfrac{1}{2}\log\left|\csc\left(x + \dfrac{\pi}{3}\right) - \cot\left(x - \dfrac{\pi}{3}\right)\right| + c$
- **(D)** $\dfrac{1}{2}\log\left|\csc\left(x + \dfrac{\pi}{3}\right) - \cot\left(x + \dfrac{\pi}{3}\right)\right| + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{2}\log\left|\csc\left(x - \dfrac{\pi}{3}\right) - \cot\left(x - \dfrac{\pi}{3}\right)\right| + c$**

**Detailed Solution:**

Given integral is $I = \int \dfrac{1}{\sin x - \sqrt{3} \cos x} dx$

Multiplying and dividing the denominator by $2$, we get:

$I = \int \dfrac{1}{2 \left( \dfrac{1}{2} \sin x - \dfrac{\sqrt{3}}{2} \cos x \right)} dx$

$I = \dfrac{1}{2} \int \dfrac{1}{\sin x \cos \dfrac{\pi}{3} - \cos x \sin \dfrac{\pi}{3}} dx$

Using the formula $\sin(A - B) = \sin A \cos B - \cos A \sin B$:

$I = \dfrac{1}{2} \int \dfrac{1}{\sin \left( x - \dfrac{\pi}{3} \right)} dx$

$I = \dfrac{1}{2} \int \csc \left( x - \dfrac{\pi}{3} \right) dx$

Using the standard integral $\int \csc \theta d\theta = \log |\csc \theta - \cot \theta| + c$:

$I = \dfrac{1}{2} \log \left| \csc \left( x - \dfrac{\pi}{3} \right) - \cot \left( x - \dfrac{\pi}{3} \right) \right| + c$

Answer: $\dfrac{1}{2}\log\left|\csc\left(x - \dfrac{\pi}{3}\right) - \cot\left(x - \dfrac{\pi}{3}\right)\right| + c$

</details>

---

### Q27. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \sin^3 x \cdot \cos^3 x \, dx = \dfrac{1}{32}\left[\dfrac{3}{2} f(x) + \dfrac{1}{6} g(x)\right] + C$, then $f(x)$ and $g(x)$ are respectively...

**Options:**

- **(A)** $-\sin 2x, \sin 6x$
- **(B)** $-\cos 2x, \cos 6x$
- **(C)** $\cos 6x, -\cos 2x$
- **(D)** $\sin 2x, \sin 6x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\cos 2x, \cos 6x$**

**Detailed Solution:**

$I = \int \sin^3 x \cos^3 x \, dx$

$I = \int (\sin x \cos x)^3 \, dx$

$I = \int \left(\dfrac{\sin 2x}{2}\right)^3 \, dx$

$I = \dfrac{1}{8} \int \sin^3 2x \, dx$

Using the identity $\sin 3\theta = 3\sin \theta - 4\sin^3 \theta$, we get $\sin^3 2x = \dfrac{3\sin 2x - \sin 6x}{4}$.

$I = \dfrac{1}{8} \int \left(\dfrac{3\sin 2x - \sin 6x}{4}\right) \, dx$

$I = \dfrac{1}{32} \int (3\sin 2x - \sin 6x) \, dx$

$I = \dfrac{1}{32} \left[ 3\left(-\dfrac{\cos 2x}{2}\right) - \left(-\dfrac{\cos 6x}{6}\right) \right] + C$

$I = \dfrac{1}{32} \left[ \dfrac{3}{2}(-\cos 2x) + \dfrac{1}{6}(\cos 6x) \right] + C$

Comparing with the given expression $\dfrac{1}{32}\left[\dfrac{3}{2} f(x) + \dfrac{1}{6} g(x)\right] + C$, we get:

$f(x) = -\cos 2x$

$g(x) = \cos 6x$

Answer: $-\cos 2x, \cos 6x$

</details>

---

### Q28. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For $x\neq 0$, the value of $I=\displaystyle\int\dfrac{x^2-1}{(x^4+3x^2+1)\tan^{-1}\left(x+\dfrac{1}{x}\right)}\,dx$ is ...

**Options:**

- **(A)** $\log\left(\tan^{-1}\left(x+\dfrac{1}{x}\right)\right)+c$
- **(B)** $\log\left(\tan^{-1}\left(x-\dfrac{1}{x}\right)\right)+c$
- **(C)** $\tan^{-1}\left(x+\dfrac{1}{x}\right)+c$
- **(D)** $\log\left(\tan^{-1}\left(\dfrac{1}{x}-x\right)\right)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\log\left(\tan^{-1}\left(x+\dfrac{1}{x}\right)\right)+c$**

**Detailed Solution:**

$I = \displaystyle\int\dfrac{x^2-1}{(x^4+3x^2+1)\tan^{-1}\left(x+\dfrac{1}{x}\right)}\,dx$

Dividing the numerator and the denominator by $x^2$, we get:

$I = \displaystyle\int\dfrac{1-\dfrac{1}{x^2}}{\left(x^2+3+\dfrac{1}{x^2}\right)\tan^{-1}\left(x+\dfrac{1}{x}\right)}\,dx$

Let $x+\dfrac{1}{x} = t$

Differentiating both sides with respect to $x$, we get:

$\left(1-\dfrac{1}{x^2}\right)dx = dt$

Also, $x^2+\dfrac{1}{x^2} = t^2-2$

Substituting these into the integral:

$I = \displaystyle\int\dfrac{dt}{(t^2-2+3)\tan^{-1}(t)} = \displaystyle\int\dfrac{dt}{(t^2+1)\tan^{-1}(t)}$

Let $\tan^{-1}(t) = u$

Differentiating with respect to $t$, we get:

$\dfrac{1}{t^2+1}dt = du$

The integral becomes:

$I = \displaystyle\int\dfrac{du}{u} = \log(u)+c$

Substituting back $u = \tan^{-1}(t)$ and $t = x+\dfrac{1}{x}$:

$I = \log\left(\tan^{-1}\left(x+\dfrac{1}{x}\right)\right)+c$

Answer: $\log\left(\tan^{-1}\left(x+\dfrac{1}{x}\right)\right)+c$

</details>

---

### Q29. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $I_1=\displaystyle\int\dfrac{e^x}{e^{2x}+e^x+1}\,dx$ and $I_2=\displaystyle\int\dfrac{1}{e^{-2x}+e^{-x}+1}\,dx$, then $I_1-I_2=$

**Options:**

- **(A)** $-\dfrac{1}{2}\log|e^{2x}+e^x+1|+\sqrt{3}\tan^{-1}\left(\dfrac{2e^x+1}{\sqrt{3}}\right)+c$
- **(B)** $-\dfrac{1}{2}\log|e^{2x}+e^x+1|+\dfrac{\sqrt{3}}{2}\log\left|\dfrac{2e^x+1-\sqrt{3}}{2e^x+1+\sqrt{3}}\right|+c$
- **(C)** $-\dfrac{1}{2}\log|e^{2x}+e^x+1|-\sqrt{3}\tan^{-1}\left(\dfrac{2e^x+1}{\sqrt{3}}\right)+c$
- **(D)** $-\dfrac{1}{2}\log|e^{2x}+e^x+1|-\dfrac{\sqrt{3}}{2}\log\left|\dfrac{2e^x+1-\sqrt{3}}{2e^x+1+\sqrt{3}}\right|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\dfrac{1}{2}\log|e^{2x}+e^x+1|+\sqrt{3}\tan^{-1}\left(\dfrac{2e^x+1}{\sqrt{3}}\right)+c$**

**Detailed Solution:**

We are given:

$I_1 = \displaystyle\int\dfrac{e^x}{e^{2x}+e^x+1}\,dx$

$I_2 = \displaystyle\int\dfrac{1}{e^{-2x}+e^{-x}+1}\,dx$

First, simplify $I_2$ by multiplying the numerator and denominator by $e^{2x}$:

$I_2 = \displaystyle\int\dfrac{e^{2x}}{1+e^x+e^{2x}}\,dx$

Now, subtract $I_2$ from $I_1$:

$I_1 - I_2 = \displaystyle\int\dfrac{e^x - e^{2x}}{e^{2x}+e^x+1}\,dx$

Substitute $e^x = t$, which gives $e^x dx = dt \Rightarrow dx = \dfrac{dt}{t}$:

$I_1 - I_2 = \displaystyle\int\dfrac{t - t^2}{t^2+t+1} \cdot \dfrac{dt}{t}$

$I_1 - I_2 = \displaystyle\int\dfrac{1 - t}{t^2+t+1}\,dt$

Rewrite the numerator $1 - t$ in terms of the derivative of the denominator, which is $2t + 1$:

$1 - t = -\dfrac{1}{2}(2t + 1) + \dfrac{3}{2}$

Substitute this back into the integral:

$I_1 - I_2 = \displaystyle\int\dfrac{-\dfrac{1}{2}(2t + 1) + \dfrac{3}{2}}{t^2+t+1}\,dt$

$I_1 - I_2 = -\dfrac{1}{2}\displaystyle\int\dfrac{2t + 1}{t^2+t+1}\,dt + \dfrac{3}{2}\displaystyle\int\dfrac{1}{t^2+t+1}\,dt$

The first integral is a standard logarithmic form. For the second integral, complete the square in the denominator:

$t^2 + t + 1 = \left(t + \dfrac{1}{2}\right)^2 + \left(\dfrac{\sqrt{3}}{2}\right)^2$

$I_1 - I_2 = -\dfrac{1}{2}\log|t^2+t+1| + \dfrac{3}{2}\displaystyle\int\dfrac{1}{\left(t + \dfrac{1}{2}\right)^2 + \left(\dfrac{\sqrt{3}}{2}\right)^2}\,dt$

$I_1 - I_2 = -\dfrac{1}{2}\log|t^2+t+1| + \dfrac{3}{2} \left(\dfrac{2}{\sqrt{3}}\right) \tan^{-1}\left(\dfrac{t + \dfrac{1}{2}}{\dfrac{\sqrt{3}}{2}}\right) + c$

$I_1 - I_2 = -\dfrac{1}{2}\log|t^2+t+1| + \sqrt{3}\tan^{-1}\left(\dfrac{2t + 1}{\sqrt{3}}\right) + c$

Finally, substitute $t = e^x$ back into the expression:

$I_1 - I_2 = -\dfrac{1}{2}\log|e^{2x}+e^x+1| + \sqrt{3}\tan^{-1}\left(\dfrac{2e^x+1}{\sqrt{3}}\right) + c$

Answer: $-\dfrac{1}{2}\log|e^{2x}+e^x+1|+\sqrt{3}\tan^{-1}\left(\dfrac{2e^x+1}{\sqrt{3}}\right)+c$

</details>

---

### Q30. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\displaystyle\int\dfrac{x^2}{(1-x^2)(1+\sqrt{1-x^2})}\,dx$ and $f(0)=2$, then $f\left(\dfrac{1}{2}\right)=$ ...

**Options:**

- **(A)** $\dfrac{1}{2}\log 3-\dfrac{\pi}{3}+2$
- **(B)** $\dfrac{1}{2}\log 3+\dfrac{\pi}{3}+2$
- **(C)** $\dfrac{1}{2}\log 3-\dfrac{\pi}{6}+2$
- **(D)** $\dfrac{1}{2}\log 3+\dfrac{\pi}{6}+2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{2}\log 3-\dfrac{\pi}{6}+2$**

**Detailed Solution:**

Substitute $x = \sin \theta$, which gives $dx = \cos \theta \,d\theta$.

The integral becomes:

$f(x) = \displaystyle\int \dfrac{\sin^2 \theta}{\cos^2 \theta (1+\cos \theta)} \cos \theta \,d\theta$

$f(x) = \displaystyle\int \dfrac{1-\cos^2 \theta}{\cos \theta (1+\cos \theta)} \,d\theta$

$f(x) = \displaystyle\int \dfrac{(1-\cos \theta)(1+\cos \theta)}{\cos \theta (1+\cos \theta)} \,d\theta$

$f(x) = \displaystyle\int \dfrac{1-\cos \theta}{\cos \theta} \,d\theta$

$f(x) = \displaystyle\int (\sec \theta - 1) \,d\theta$

$f(x) = \log |\sec \theta + \tan \theta| - \theta + C$

Substituting back $x = \sin \theta$, we have $\sec \theta = \dfrac{1}{\sqrt{1-x^2}}$ and $\tan \theta = \dfrac{x}{\sqrt{1-x^2}}$:

$f(x) = \log \left| \dfrac{1+x}{\sqrt{1-x^2}} \right| - \sin^{-1} x + C$

$f(x) = \dfrac{1}{2} \log \left( \dfrac{1+x}{1-x} \right) - \sin^{-1} x + C$

Given $f(0) = 2$, we substitute $x = 0$:

$\dfrac{1}{2} \log(1) - \sin^{-1}(0) + C = 2 \Rightarrow C = 2$

Thus, the function is:

$f(x) = \dfrac{1}{2} \log \left( \dfrac{1+x}{1-x} \right) - \sin^{-1} x + 2$

Now, substituting $x = \dfrac{1}{2}$:

$f\left(\dfrac{1}{2}\right) = \dfrac{1}{2} \log \left( \dfrac{1+1/2}{1-1/2} \right) - \sin^{-1} \left(\dfrac{1}{2}\right) + 2$

$f\left(\dfrac{1}{2}\right) = \dfrac{1}{2} \log 3 - \dfrac{\pi}{6} + 2$

Answer: $\dfrac{1}{2}\log 3-\dfrac{\pi}{6}+2$

</details>

---

### Q31. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\int\sin^4 x\cdot e^{\log(\cos x)}\,dx=\dfrac{1}{k}\sin^k x+C$, for $x\in\left(-\dfrac{\pi}{2},\dfrac{\pi}{2}\right)$, then ...

**Options:**

- **(A)** $k=4$
- **(B)** $k=0$
- **(C)** $k=1$
- **(D)** $k=5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $k=5$**

**Detailed Solution:**

Given integral is $\int \sin^4 x \cdot e^{\log(\cos x)} \, dx$.

Since $e^{\log(\cos x)} = \cos x$ for $x \in \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$, the integral becomes:

$\int \sin^4 x \cos x \, dx$

Let $\sin x = t$, then $\cos x \, dx = dt$.

The integral transforms to:

$\int t^4 \, dt = \dfrac{t^5}{5} + C$

Substituting back $t = \sin x$, we get:

$\dfrac{1}{5} \sin^5 x + C$

Comparing with $\dfrac{1}{k} \sin^k x + C$, we find $k = 5$.

Answer: $k=5$

</details>

---

### Q32. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int\dfrac{\log x}{(1 + \log x)^2}dx =$

**Options:**

- **(A)** $\dfrac{1}{1 + \log x} + c$
- **(B)** $-\dfrac{1}{1 + \log x} + c$
- **(C)** $\dfrac{x}{1 + \log x} + c$
- **(D)** $-\dfrac{x}{1 + \log x} + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{x}{1 + \log x} + c$**

**Detailed Solution:**

Let $\log x = t \Rightarrow x = e^t \Rightarrow dx = e^t dt$

Substituting in the integral:

$I = \int \dfrac{t}{(1 + t)^2} e^t dt$

$I = \int e^t \left( \dfrac{t + 1 - 1}{(1 + t)^2} \right) dt$

$I = \int e^t \left( \dfrac{1}{1 + t} - \dfrac{1}{(1 + t)^2} \right) dt$

This is of the form $\int e^t (f(t) + f'(t)) dt = e^t f(t) + c$, where $f(t) = \dfrac{1}{1 + t}$.

$I = \dfrac{e^t}{1 + t} + c$

Substituting $t = \log x$ and $e^t = x$:

$I = \dfrac{x}{1 + \log x} + c$

Answer: $\dfrac{x}{1 + \log x} + c$

</details>

---

### Q33. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int\dfrac{1}{\sqrt{2x - x^2}}dx =$

**Options:**

- **(A)** $\sin^{-1}(x - 1) + c$
- **(B)** $\cos^{-1}(x - 1) + c$
- **(C)** $\tan^{-1}(x - 1) + c$
- **(D)** $\sin^{-1}x + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sin^{-1}(x - 1) + c$**

**Detailed Solution:**

The given integral is $I = \int\dfrac{1}{\sqrt{2x - x^2}}dx$

Completing the square for the expression inside the square root:

$2x - x^2 = -(x^2 - 2x) = 1 - (x^2 - 2x + 1) = 1 - (x - 1)^2$

Substituting this into the integral:

$I = \int\dfrac{1}{\sqrt{1 - (x - 1)^2}}dx$

Using the standard integration formula $\int\dfrac{1}{\sqrt{a^2 - x^2}}dx = \sin^{-1}\left(\dfrac{x}{a}\right) + c$:

$I = \sin^{-1}(x - 1) + c$

Answer: $\sin^{-1}(x - 1) + c$

</details>

---

### Q34. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int(x^{21} + x^6 + x^3)(2x^{18} + 7x^3 + 14)^{\frac{1}{3}}\ dx =$

**Options:**

- **(A)** $\dfrac{1}{56}(2x^{18} + 7x^3 + 14)^{\frac{4}{3}} + c$
- **(B)** $(2x^{18} + 7x^3 + 14)^{\frac{4}{3}} + c$
- **(C)** $(2x^{21} + 7x^6 + 14x^3)^{\frac{4}{3}} + c$
- **(D)** $\dfrac{1}{56}(2x^{21} + 7x^6 + 14x^3)^{\frac{4}{3}} + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{56}(2x^{21} + 7x^6 + 14x^3)^{\frac{4}{3}} + c$**

**Detailed Solution:**

Let the given integral be $I = \int (x^{21} + x^6 + x^3)(2x^{18} + 7x^3 + 14)^{\dfrac{1}{3}}\ dx$.

Factoring out $x$ from the first polynomial, we get:

$I = \int x(x^{20} + x^5 + x^2)(2x^{18} + 7x^3 + 14)^{\dfrac{1}{3}}\ dx$

Moving $x$ inside the cube root as $x^3$, we obtain:

$I = \int (x^{20} + x^5 + x^2)(2x^{21} + 7x^6 + 14x^3)^{\dfrac{1}{3}}\ dx$

Let $2x^{21} + 7x^6 + 14x^3 = t$.

Differentiating both sides with respect to $x$:

$(42x^{20} + 42x^5 + 42x^2)\ dx = dt$

$42(x^{20} + x^5 + x^2)\ dx = dt$

$(x^{20} + x^5 + x^2)\ dx = \dfrac{dt}{42}$

Substituting this into the integral, we get:

$I = \int t^{\dfrac{1}{3}} \dfrac{dt}{42}$

$I = \dfrac{1}{42} \dfrac{t^{\dfrac{4}{3}}}{\dfrac{4}{3}} + c$

$I = \dfrac{1}{56} t^{\dfrac{4}{3}} + c$

Substituting back $t = 2x^{21} + 7x^6 + 14x^3$:

$I = \dfrac{1}{56} (2x^{21} + 7x^6 + 14x^3)^{\dfrac{4}{3}} + c$

</details>

---

### Q35. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \int \dfrac{x}{(x^2 + 4)(x^2 + 9)}\, dx$ and $f(0) = \dfrac{1}{5}\log\left(\dfrac{2}{3}\right)$, then $f(1) = $

**Options:**

- **(A)** $\dfrac{1}{5}\log(2)$
- **(B)** $\dfrac{1}{10}\log(2)$
- **(C)** $-\dfrac{1}{5}\log(2)$
- **(D)** $-\dfrac{1}{10}\log(2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\dfrac{1}{10}\log(2)$**

**Detailed Solution:**

Let $x^2 = t$, then $2x\, dx = dt$, which gives $x\, dx = \dfrac{dt}{2}$.

Substituting this into the integral, we get:

$f(x) = \dfrac{1}{2} \int \dfrac{dt}{(t + 4)(t + 9)}$

Using partial fractions:

$f(x) = \dfrac{1}{2} \int \dfrac{1}{5} \left( \dfrac{1}{t + 4} - \dfrac{1}{t + 9} \right) dt$

$f(x) = \dfrac{1}{10} \left( \log|t + 4| - \log|t + 9| \right) + C$

$f(x) = \dfrac{1}{10} \log\left( \dfrac{t + 4}{t + 9} \right) + C$

Substituting $t = x^2$:

$f(x) = \dfrac{1}{10} \log\left( \dfrac{x^2 + 4}{x^2 + 9} \right) + C$

Given $f(0) = \dfrac{1}{5}\log\left(\dfrac{2}{3}\right)$, we substitute $x = 0$:

$f(0) = \dfrac{1}{10} \log\left( \dfrac{4}{9} \right) + C$

$f(0) = \dfrac{1}{10} \log\left( \left(\dfrac{2}{3}\right)^2 \right) + C$

$f(0) = \dfrac{1}{5} \log\left( \dfrac{2}{3} \right) + C$

Comparing with the given value, we get $C = 0$.

Thus, the function is:

$f(x) = \dfrac{1}{10} \log\left( \dfrac{x^2 + 4}{x^2 + 9} \right)$

To find $f(1)$, substitute $x = 1$:

$f(1) = \dfrac{1}{10} \log\left( \dfrac{1^2 + 4}{1^2 + 9} \right)$

$f(1) = \dfrac{1}{10} \log\left( \dfrac{5}{10} \right)$

$f(1) = \dfrac{1}{10} \log\left( \dfrac{1}{2} \right)$

$f(1) = -\dfrac{1}{10} \log(2)$

Answer: $-\dfrac{1}{10}\log(2)$

</details>

---

### Q36. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{x^4(x^{10} - 1)}{x^{20} + 3x^{10} + 1}\, dx = \cdots$

**Options:**

- **(A)** $\tan^{-1}\left(x^5 + \dfrac{1}{x^5}\right) + c$
- **(B)** $\dfrac{1}{5}\tan^{-1}\left(x^5 + \dfrac{1}{x^5}\right) + c$
- **(C)** $\tan^{-1}\left(x^{10} + \dfrac{1}{x^{10}}\right) + c$
- **(D)** $\dfrac{1}{10}\tan^{-1}\left(x^{10} + \dfrac{1}{x^{10}}\right) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{5}\tan^{-1}\left(x^5 + \dfrac{1}{x^5}\right) + c$**

**Detailed Solution:**

$I = \int \dfrac{x^4(x^{10} - 1)}{x^{20} + 3x^{10} + 1}\, dx$

Dividing the numerator and the denominator by $x^{10}$:

$I = \int \dfrac{x^4 - \dfrac{1}{x^6}}{x^{10} + 3 + \dfrac{1}{x^{10}}}\, dx$

Let $x^5 + \dfrac{1}{x^5} = t$

Differentiating with respect to $x$:

$\left(5x^4 - \dfrac{5}{x^6}\right) dx = dt \Rightarrow \left(x^4 - \dfrac{1}{x^6}\right) dx = \dfrac{dt}{5}$

The denominator can be written as:

$x^{10} + \dfrac{1}{x^{10}} + 3 = \left(x^5 + \dfrac{1}{x^5}\right)^2 - 2 + 3 = t^2 + 1$

Substituting these into the integral:

$I = \int \dfrac{1}{t^2 + 1} \dfrac{dt}{5}$

$I = \dfrac{1}{5} \tan^{-1}(t) + c$

$I = \dfrac{1}{5} \tan^{-1}\left(x^5 + \dfrac{1}{x^5}\right) + c$

Answer: $\dfrac{1}{5}\tan^{-1}\left(x^5 + \dfrac{1}{x^5}\right) + c$

</details>

---

### Q37. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of integral $\displaystyle\int \dfrac{dx}{\sin^2 x + \tan^2 x}$ is...

**Options:**

- **(A)** $\dfrac{-1}{2\tan x} + \dfrac{1}{2\sqrt{2}}\tan^{-1}\left(\dfrac{\tan x}{\sqrt{2}}\right) + c$
- **(B)** $\dfrac{-1}{2\tan x} - \dfrac{1}{2\sqrt{2}}\tan^{-1}\left(\dfrac{\tan x}{\sqrt{2}}\right) + c$
- **(C)** $\dfrac{1}{2\tan x} - \dfrac{1}{2\sqrt{2}}\tan^{-1}\left(\dfrac{\tan x}{\sqrt{2}}\right) + c$
- **(D)** $\dfrac{1}{2\tan x} + \dfrac{1}{2\sqrt{2}}\tan^{-1}\left(\dfrac{\tan x}{\sqrt{2}}\right) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{-1}{2\tan x} - \dfrac{1}{2\sqrt{2}}\tan^{-1}\left(\dfrac{\tan x}{\sqrt{2}}\right) + c$**

**Detailed Solution:**

Given integral is $I = \displaystyle\int \dfrac{dx}{\sin^2 x + \tan^2 x}$

Rewriting the denominator:

$\sin^2 x + \tan^2 x = \sin^2 x + \dfrac{\sin^2 x}{\cos^2 x} = \sin^2 x \left( \dfrac{\cos^2 x + 1}{\cos^2 x} \right) = \tan^2 x (\cos^2 x + 1)$

Substituting this back into the integral:

$I = \displaystyle\int \dfrac{dx}{\tan^2 x (\cos^2 x + 1)}$

Multiplying the numerator and the denominator by $\sec^2 x$:

$I = \displaystyle\int \dfrac{\sec^2 x}{\tan^2 x (\cos^2 x + 1) \sec^2 x} dx$

$I = \displaystyle\int \dfrac{\sec^2 x}{\tan^2 x (1 + \sec^2 x)} dx$

Using the identity $\sec^2 x = 1 + \tan^2 x$:

$I = \displaystyle\int \dfrac{\sec^2 x}{\tan^2 x (2 + \tan^2 x)} dx$

Let $\tan x = t$, then $\sec^2 x dx = dt$. The integral becomes:

$I = \displaystyle\int \dfrac{dt}{t^2 (t^2 + 2)}$

Using partial fractions:

$\dfrac{1}{t^2 (t^2 + 2)} = \dfrac{1}{2} \left( \dfrac{1}{t^2} - \dfrac{1}{t^2 + 2} \right)$

$I = \dfrac{1}{2} \displaystyle\int \left( \dfrac{1}{t^2} - \dfrac{1}{t^2 + (\sqrt{2})^2} \right) dt$

Integrating with respect to $t$:

$I = \dfrac{1}{2} \left( -\dfrac{1}{t} - \dfrac{1}{\sqrt{2}} \tan^{-1} \left( \dfrac{t}{\sqrt{2}} \right) \right) + c$

$I = \dfrac{-1}{2t} - \dfrac{1}{2\sqrt{2}} \tan^{-1} \left( \dfrac{t}{\sqrt{2}} \right) + c$

Substituting $t = \tan x$ back into the expression:

$I = \dfrac{-1}{2\tan x} - \dfrac{1}{2\sqrt{2}} \tan^{-1} \left( \dfrac{\tan x}{\sqrt{2}} \right) + c$

Answer: $\dfrac{-1}{2\tan x} - \dfrac{1}{2\sqrt{2}}\tan^{-1}\left(\dfrac{\tan x}{\sqrt{2}}\right) + c$

</details>

---

### Q38. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of integral $\displaystyle\int \dfrac{\sqrt{x^2 + 1}\,[\log(x^2 + 1) - 2\log x]}{x^4}\,dx$ is equal to...

**Options:**

- **(A)** $\left(1 + \dfrac{1}{x^2}\right)^{3/2}\left[\dfrac{-1}{3}\log\left(1 + \dfrac{1}{x^2}\right) + \dfrac{2}{9}\right] + c$
- **(B)** $\left(1 + \dfrac{1}{x^2}\right)^{3/2}\left[\dfrac{-1}{3}\log\left(1 + \dfrac{1}{x^2}\right) - \dfrac{2}{9}\right] + c$
- **(C)** $\left(1 + \dfrac{1}{x^2}\right)^{3/2}\left[\dfrac{-1}{3}\log\left(1 + \dfrac{1}{x^2}\right) + \dfrac{2}{3}\right] + c$
- **(D)** $\left(1 + \dfrac{1}{x^2}\right)^{3/2}\left[\dfrac{-1}{3}\log\left(1 + \dfrac{1}{x^2}\right) - \dfrac{2}{3}\right] + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(1 + \dfrac{1}{x^2}\right)^{3/2}\left[\dfrac{-1}{3}\log\left(1 + \dfrac{1}{x^2}\right) + \dfrac{2}{9}\right] + c$**

**Detailed Solution:**

Let the given integral be $I = \int \dfrac{\sqrt{x^2+1} [\log(x^2+1) - 2\log x]}{x^4} dx$

$I = \int \dfrac{\sqrt{x^2(1+\dfrac{1}{x^2})}}{x^4} [\log(x^2+1) - \log x^2] dx$

$I = \int \dfrac{x\sqrt{1+\dfrac{1}{x^2}}}{x^4} \log\left(\dfrac{x^2+1}{x^2}\right) dx$

$I = \int \dfrac{1}{x^3}\sqrt{1+\dfrac{1}{x^2}} \log\left(1+\dfrac{1}{x^2}\right) dx$

Substituting $1+\dfrac{1}{x^2} = t$

Differentiating with respect to $x$, we get $-\dfrac{2}{x^3} dx = dt \Rightarrow \dfrac{1}{x^3} dx = -\dfrac{1}{2} dt$

$I = \int \sqrt{t} \log t \left(-\dfrac{1}{2}\right) dt$

$I = -\dfrac{1}{2} \int t^{1/2} \log t dt$

Using integration by parts, taking $\log t$ as the first function and $t^{1/2}$ as the second function:

$I = -\dfrac{1}{2} \left[ \log t \int t^{1/2} dt - \int \left( \dfrac{d}{dt}(\log t) \int t^{1/2} dt \right) dt \right]$

$I = -\dfrac{1}{2} \left[ \log t \left(\dfrac{t^{3/2}}{3/2}\right) - \int \dfrac{1}{t} \left(\dfrac{t^{3/2}}{3/2}\right) dt \right]$

$I = -\dfrac{1}{2} \left[ \dfrac{2}{3} t^{3/2} \log t - \dfrac{2}{3} \int t^{1/2} dt \right]$

$I = -\dfrac{1}{2} \left[ \dfrac{2}{3} t^{3/2} \log t - \dfrac{2}{3} \left(\dfrac{t^{3/2}}{3/2}\right) \right] + c$

$I = -\dfrac{1}{2} \left[ \dfrac{2}{3} t^{3/2} \log t - \dfrac{4}{9} t^{3/2} \right] + c$

$I = t^{3/2} \left[ -\dfrac{1}{3} \log t + \dfrac{2}{9} \right] + c$

Substituting $t = 1+\dfrac{1}{x^2}$ back into the expression:

$I = \left(1+\dfrac{1}{x^2}\right)^{3/2} \left[ -\dfrac{1}{3} \log\left(1+\dfrac{1}{x^2}\right) + \dfrac{2}{9} \right] + c$

</details>

---

### Q39. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \dfrac{1}{\log x}$ and $g(x) = \dfrac{1}{(\log x)^2}$, then the value of $\displaystyle\int [f(x) - g(x)]\,dx$ is...

**Options:**

- **(A)** $(\log x)^2 + c$
- **(B)** $x\log x + c$
- **(C)** $\dfrac{x}{\log x} + c$
- **(D)** $\dfrac{1}{\log x} + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{x}{\log x} + c$**

**Detailed Solution:**

Let $I = \int \left( \dfrac{1}{\log x} - \dfrac{1}{(\log x)^2} \right) dx$

Substitute $\log x = t \Rightarrow x = e^t \Rightarrow dx = e^t dt$

$I = \int e^t \left( \dfrac{1}{t} - \dfrac{1}{t^2} \right) dt$

Using the standard integral $\int e^t (h(t) + h'(t)) dt = e^t h(t) + c$

Here, $h(t) = \dfrac{1}{t}$ and $h'(t) = -\dfrac{1}{t^2}$

$I = e^t \left( \dfrac{1}{t} \right) + c$

Substituting back $t = \log x$ and $e^t = x$

$I = \dfrac{x}{\log x} + c$

Answer: $\dfrac{x}{\log x} + c$

</details>

---

### Q40. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\displaystyle\int \dfrac{dx}{x^{7/2}(x^4 + 1)^{3/8}} = m\left(\dfrac{x^4 + 1}{x^4}\right)^n + c$, where $c$ is a constant of integration, then the value of $\dfrac{n}{m}$ is...

**Options:**

- **(A)** $-\dfrac{1}{16}$
- **(B)** $-\dfrac{25}{16}$
- **(C)** $\dfrac{25}{4}$
- **(D)** $-\dfrac{25}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\dfrac{25}{16}$**

**Detailed Solution:**

Given integral is $I = \displaystyle\int \dfrac{dx}{x^{7/2}(x^4 + 1)^{3/8}}$

Factoring out $x^4$ from the term $(x^4 + 1)^{3/8}$, we get:

$I = \displaystyle\int \dfrac{dx}{x^{7/2} \cdot (x^4)^{3/8} \left(1 + \dfrac{1}{x^4}\right)^{3/8}}$

$I = \displaystyle\int \dfrac{dx}{x^{7/2} \cdot x^{3/2} (1 + x^{-4})^{3/8}}$

$I = \displaystyle\int \dfrac{dx}{x^5 (1 + x^{-4})^{3/8}}$

Let $1 + x^{-4} = t$

Differentiating both sides, we get:

$-4x^{-5} dx = dt \Rightarrow \dfrac{dx}{x^5} = -\dfrac{dt}{4}$

Substituting this into the integral:

$I = -\dfrac{1}{4} \displaystyle\int t^{-3/8} dt$

$I = -\dfrac{1}{4} \left( \dfrac{t^{5/8}}{5/8} \right) + c$

$I = -\dfrac{2}{5} t^{5/8} + c$

Substituting back $t = 1 + x^{-4} = \dfrac{x^4 + 1}{x^4}$:

$I = -\dfrac{2}{5} \left( \dfrac{x^4 + 1}{x^4} \right)^{5/8} + c$

Comparing this with the given expression $m\left(\dfrac{x^4 + 1}{x^4}\right)^n + c$, we get:

$m = -\dfrac{2}{5}$ and $n = \dfrac{5}{8}$

Therefore, the value of $\dfrac{n}{m}$ is:

$\dfrac{n}{m} = \dfrac{5/8}{-2/5} = \dfrac{5}{8} \times \left(-\dfrac{5}{2}\right) = -\dfrac{25}{16}$

Answer: $-\dfrac{25}{16}$

</details>

---

### Q41. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int e^{x + \tan^{-1}x}\left(\dfrac{x^2 + 2}{\sec^2(\tan^{-1}x)}\right)dx = e^{f(x)} + c$, then $\ldots$

**Options:**

- **(A)** $f(x)$ is strictly decreasing on $R$.
- **(B)** $f(x)$ is strictly increasing on $R^+$ and strictly decreasing on $R^-$.
- **(C)** $f(x)$ is strictly increasing on $R$.
- **(D)** $f(x)$ is strictly decreasing on $R^+$ and strictly increasing on $R^-$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $f(x)$ is strictly increasing on $R$.**

**Detailed Solution:**

The given integral is $I = \int e^{x + \tan^{-1}x}\left(\dfrac{x^2 + 2}{\sec^2(\tan^{-1}x)}\right)dx$.

Using the identity $\sec^2\theta = 1 + \tan^2\theta$, we have $\sec^2(\tan^{-1}x) = 1 + \tan^2(\tan^{-1}x) = 1 + x^2$.

Substituting this into the integral gives:

$I = \int e^{x + \tan^{-1}x}\left(\dfrac{x^2 + 2}{1 + x^2}\right)dx$

$I = \int e^{x + \tan^{-1}x}\left(\dfrac{x^2 + 1 + 1}{1 + x^2}\right)dx$

$I = \int e^{x + \tan^{-1}x}\left(1 + \dfrac{1}{1 + x^2}\right)dx$

Let $t = x + \tan^{-1}x$. Differentiating with respect to $x$, we get:

$dt = \left(1 + \dfrac{1}{1 + x^2}\right)dx$

The integral becomes:

$I = \int e^t dt = e^t + c$

Substituting back $t = x + \tan^{-1}x$, we get:

$I = e^{x + \tan^{-1}x} + c$

Comparing this with the given expression $e^{f(x)} + c$, we find:

$f(x) = x + \tan^{-1}x$

To determine the monotonicity of $f(x)$, we find its derivative:

$f'(x) = 1 + \dfrac{1}{1 + x^2}$

Since $x^2 \ge 0$ for all real $x$, $1 + x^2 \ge 1$, which implies $\dfrac{1}{1 + x^2} > 0$.

Thus, $f'(x) > 1 > 0$ for all $x \in R$.

Therefore, $f(x)$ is strictly increasing on $R$.

Answer: $f(x)$ is strictly increasing on $R$.

</details>

---

### Q42. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x) = x$, $f_1(x) = f(\log x)$, $f_2(x) = f_1(\log x)$, $f_3(x) = f_2(\log x)$, $\ldots$ and so on. Then $\int \dfrac{1}{f(x)\,f_1(x)\,f_2(x)\,\ldots f_{2026}(x)}\,dx = \ldots$

**Options:**

- **(A)** $f_{2025}(x) + c$
- **(B)** $2025 f_{2025}(x) + c$
- **(C)** $f_{2027}(x) + c$
- **(D)** $2027 f_{2027}(x) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $f_{2027}(x) + c$**

**Detailed Solution:**

Given $f(x) = x$

$f_1(x) = f(\log x) = \log x$

$f_2(x) = f_1(\log x) = \log(\log x)$

In general, $f_n(x) = \log(f_{n-1}(x))$.

Differentiating $f_n(x)$ with respect to $x$ using the chain rule:

$f_1'(x) = \dfrac{1}{x} = \dfrac{1}{f(x)}$

$f_2'(x) = \dfrac{d}{dx}(\log(f_1(x))) = \dfrac{1}{f_1(x)} f_1'(x) = \dfrac{1}{f_1(x) f(x)}$

$f_3'(x) = \dfrac{d}{dx}(\log(f_2(x))) = \dfrac{1}{f_2(x)} f_2'(x) = \dfrac{1}{f_2(x) f_1(x) f(x)}$

By induction, $f_n'(x) = \dfrac{1}{f_{n-1}(x) f_{n-2}(x) \ldots f_1(x) f(x)}$.

For $n = 2027$, we have:

$f_{2027}'(x) = \dfrac{1}{f_{2026}(x) f_{2025}(x) \ldots f_1(x) f(x)}$

The given integral is:

$I = \int \dfrac{1}{f(x) f_1(x) f_2(x) \ldots f_{2026}(x)} \, dx$

$I = \int f_{2027}'(x) \, dx$

$I = f_{2027}(x) + c$

Answer: $f_{2027}(x) + c$

</details>

---

### Q43. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\int\dfrac{n\sqrt{\text{cosec}^2 x^n - 1}}{x^{(1-n)}}\,dx$ is ...

**Options:**

- **(A)** $\log(\sin x) + c$
- **(B)** $\log(\sin x^n) + c$
- **(C)** $\log(\cot x^n) + c$
- **(D)** $\log(\cos x^n) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log(\sin x^n) + c$**

**Detailed Solution:**

Let the given integral be $I = \int \dfrac{n\sqrt{\text{cosec}^2 x^n - 1}}{x^{(1-n)}} \,dx$

Using the trigonometric identity $\text{cosec}^2 \theta - 1 = \cot^2 \theta$, the integral simplifies to:

$I = \int \dfrac{n \cot x^n}{x^{1-n}} \,dx$

$I = \int n x^{n-1} \cot x^n \,dx$

Let $x^n = t$, which gives $n x^{n-1} \,dx = dt$.

Substituting these into the integral, we get:

$I = \int \cot t \,dt$

$I = \log(\sin t) + c$

Substituting $t = x^n$ back into the expression:

$I = \log(\sin x^n) + c$

Answer: $\log(\sin x^n) + c$

</details>

---

### Q44. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int\dfrac{(x+1)\,dx}{x(1+xe^x)} = \ldots\ldots$

**Options:**

- **(A)** $\log\left|\dfrac{xe^x}{1+xe^x}\right| + c$
- **(B)** $\log\left|\dfrac{1+xe^x}{xe^x}\right| + c$
- **(C)** $\log\left|\dfrac{(x+1)e^x}{xe^x}\right| + c$
- **(D)** $\log\left|\dfrac{(x+1)e^x}{1+xe^x}\right| + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\log\left|\dfrac{xe^x}{1+xe^x}\right| + c$**

**Detailed Solution:**

Let $I = \int\dfrac{x+1}{x(1+xe^x)} dx$

Multiplying the numerator and the denominator by $e^x$:

$I = \int\dfrac{(x+1)e^x}{xe^x(1+xe^x)} dx$

Let $xe^x = t$

Differentiating both sides with respect to $x$:

$(1 \cdot e^x + x \cdot e^x) dx = dt$

$(x+1)e^x dx = dt$

Substituting these into the integral:

$I = \int\dfrac{dt}{t(1+t)}$

Using partial fractions:

$I = \int\left(\dfrac{1}{t} - \dfrac{1}{1+t}\right) dt$

$I = \log|t| - \log|1+t| + c$

$I = \log\left|\dfrac{t}{1+t}\right| + c$

Substituting $t = xe^x$ back into the expression:

$I = \log\left|\dfrac{xe^x}{1+xe^x}\right| + c$

Answer: $\log\left|\dfrac{xe^x}{1+xe^x}\right| + c$

</details>

---

### Q45. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\int\dfrac{\sin x}{\sin 4x}\, dx = \alpha\log\left|\dfrac{1 + \sin x}{1 - \sin x}\right| + \beta\log\left|\dfrac{1 + \sqrt{2}\sin x}{1 - \sqrt{2}\sin x}\right| + c$, then the value of $32(\alpha + \beta^2) =$

**Options:**

- **(A)** $5$
- **(B)** $-1$
- **(C)** $9$
- **(D)** $-3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-3$**

**Detailed Solution:**

Given integral is $I = \int \dfrac{\sin x}{\sin 4x} dx$

$I = \int \dfrac{\sin x}{2 \sin 2x \cos 2x} dx = \int \dfrac{\sin x}{4 \sin x \cos x \cos 2x} dx$

$I = \int \dfrac{1}{4 \cos x \cos 2x} dx$

Multiplying the numerator and denominator by $\cos x$:

$I = \int \dfrac{\cos x}{4 \cos^2 x \cos 2x} dx = \int \dfrac{\cos x}{4 (1 - \sin^2 x) (1 - 2\sin^2 x)} dx$

Substituting $\sin x = t \Rightarrow \cos x dx = dt$:

$I = \dfrac{1}{4} \int \dfrac{1}{(1 - t^2)(1 - 2t^2)} dt$

Using partial fractions:

$\dfrac{1}{(1 - t^2)(1 - 2t^2)} = \dfrac{2}{1 - 2t^2} - \dfrac{1}{1 - t^2}$

$I = \dfrac{1}{4} \int \left( \dfrac{2}{1 - 2t^2} - \dfrac{1}{1 - t^2} \right) dt$

$I = \dfrac{1}{2} \int \dfrac{1}{1 - (\sqrt{2}t)^2} dt - \dfrac{1}{4} \int \dfrac{1}{1 - t^2} dt$

Using the standard integral $\int \dfrac{1}{a^2 - x^2} dx = \dfrac{1}{2a} \log \left| \dfrac{a + x}{a - x} \right|$:

$I = \dfrac{1}{2} \left( \dfrac{1}{2\sqrt{2}} \log \left| \dfrac{1 + \sqrt{2}t}{1 - \sqrt{2}t} \right| \right) - \dfrac{1}{4} \left( \dfrac{1}{2} \log \left| \dfrac{1 + t}{1 - t} \right| \right) + c$

$I = \dfrac{1}{4\sqrt{2}} \log \left| \dfrac{1 + \sqrt{2}\sin x}{1 - \sqrt{2}\sin x} \right| - \dfrac{1}{8} \log \left| \dfrac{1 + \sin x}{1 - \sin x} \right| + c$

Comparing with the given expression:

$\alpha = -\dfrac{1}{8}$ and $\beta = \dfrac{1}{4\sqrt{2}}$

Calculating the required value:

$32(\alpha + \beta^2) = 32 \left( -\dfrac{1}{8} + \left( \dfrac{1}{4\sqrt{2}} \right)^2 \right)$

$32(\alpha + \beta^2) = 32 \left( -\dfrac{1}{8} + \dfrac{1}{32} \right) = 32 \left( \dfrac{-4 + 1}{32} \right) = -3$

Answer: $-3$

</details>

---

### Q46. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int f(x)\, dx = g(x)$ then $\int x^3 f(x^2)\, dx$ is equal to

**Options:**

- **(A)** $\dfrac{1}{2}\left[x^2 g(x^2) - \int g(x^2)\, d(x^2)\right]$
- **(B)** $\dfrac{1}{2}\left[x^2[f(x)]^2 - \int [g(x)]^2\, dx\right]$
- **(C)** $\dfrac{1}{2}\left[x^2 g(x) - \int g(x)\, d(x)\right]$
- **(D)** $\dfrac{1}{2}\left[x^2 g(x^2) + \int g(x^2)\, d(x^2)\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{2}\left[x^2 g(x^2) - \int g(x^2)\, d(x^2)\right]$**

**Detailed Solution:**

Let $I = \int x^3 f(x^2)\, dx$.

Substitute $x^2 = t$, which gives $2x\, dx = dt$ or $x\, dx = \dfrac{1}{2} dt$.

$I = \int x^2 f(x^2) x\, dx = \dfrac{1}{2} \int t f(t)\, dt$

Using integration by parts, taking $t$ as the first function and $f(t)$ as the second function:

$I = \dfrac{1}{2} \left[ t \int f(t)\, dt - \int \left( \dfrac{d}{dt}(t) \int f(t)\, dt \right) dt \right]$

Since $\int f(x)\, dx = g(x)$, we have $\int f(t)\, dt = g(t)$.

$I = \dfrac{1}{2} \left[ t g(t) - \int g(t)\, dt \right]$

Substituting back $t = x^2$ and $dt = d(x^2)$:

$I = \dfrac{1}{2} \left[ x^2 g(x^2) - \int g(x^2)\, d(x^2) \right]$

</details>

---

### Q47. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \dfrac{\sin^{-1}x}{\sqrt{1 - x^2}}$ and $g(x) = e^{\sin^{-1}x}$, then the value of $\int f(x)g(x)\, dx = \ldots$

**Options:**

- **(A)** $e^{\sin^{-1}x}(\sin^{-1}x - 1) + c$
- **(B)** $e^{\sin^{-1}x}(1 - \sin^{-1}x) + c$
- **(C)** $e^{\sin^{-1}x}(\sin^{-1}x + 1) + c$
- **(D)** $e^{\sin^{-1}x}(-\sin^{-1}x - 1) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $e^{\sin^{-1}x}(\sin^{-1}x - 1) + c$**

**Detailed Solution:**

Let $I = \int f(x)g(x) \, dx = \int \dfrac{\sin^{-1}x}{\sqrt{1 - x^2}} e^{\sin^{-1}x} \, dx$

Substitute $t = \sin^{-1}x$, which gives $dt = \dfrac{1}{\sqrt{1 - x^2}} \, dx$

The integral becomes:

$I = \int t e^t \, dt$

Using integration by parts, we get:

$I = t e^t - \int e^t \, dt$

$I = t e^t - e^t + c$

$I = e^t(t - 1) + c$

Substituting $t = \sin^{-1}x$ back into the expression:

$I = e^{\sin^{-1}x}(\sin^{-1}x - 1) + c$

Answer: $e^{\sin^{-1}x}(\sin^{-1}x - 1) + c$

</details>

---

### Q48. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int \dfrac{\sin^3 x}{(\cos^4 x + 3\cos^2 x + 1)\tan^{-1}(\sec x + \cos x)}\,dx$ is

**Options:**

- **(A)** $\log\left(\tan^{-1}(\sec x + \cos x)\right) + c$
- **(B)** $2\log\left(\tan^{-1}(\sec x + \cos x)\right) + c$
- **(C)** $\dfrac{\left(\tan^{-1}(\sec x + \cos x)\right)^2}{2} + c$
- **(D)** $\tan^{-1}(\sec x + \cos x) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\log\left(\tan^{-1}(\sec x + \cos x)\right) + c$**

**Detailed Solution:**

Let $t = \sec x + \cos x$.

Differentiating with respect to $x$, we get:

$dt = (\sec x \tan x - \sin x) dx$

$dt = \sin x \left(\dfrac{1}{\cos^2 x} - 1\right) dx = \dfrac{\sin^3 x}{\cos^2 x} dx$

The polynomial in the denominator can be rewritten as:

$\cos^4 x + 3\cos^2 x + 1 = \cos^2 x (\cos^2 x + 3 + \sec^2 x)$

$\Rightarrow \cos^4 x + 3\cos^2 x + 1 = \cos^2 x ((\cos x + \sec x)^2 + 1) = \cos^2 x (t^2 + 1)$

Substituting these into the given integral, we get:

$I = \int \dfrac{\sin^3 x}{\cos^2 x (t^2 + 1) \tan^{-1} t} dx$

$I = \int \dfrac{dt}{(t^2 + 1) \tan^{-1} t}$

Now, let $u = \tan^{-1} t$. Differentiating with respect to $t$, we get:

$du = \dfrac{dt}{t^2 + 1}$

The integral simplifies to:

$I = \int \dfrac{du}{u} = \log(u) + c$

Substituting back $u = \tan^{-1} t$ and $t = \sec x + \cos x$, we obtain:

$I = \log(\tan^{-1}(\sec x + \cos x)) + c$

Answer: $\log\left(\tan^{-1}(\sec x + \cos x)\right) + c$

</details>

---

### Q49. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int 2x^{\frac{1}{3}} \sin \sqrt[3]{x^2}\,dx$ is

**Options:**

- **(A)** $\left(x^{\frac{2}{3}}\cos x^{\frac{2}{3}} + \sin x^{\frac{2}{3}}\right) + c$
- **(B)** $3\left[x^{\frac{2}{3}}\cos x^{\frac{2}{3}} - \sin x^{\frac{2}{3}}\right] + c$
- **(C)** $3\left[-x^{\frac{2}{3}}\cos x^{\frac{2}{3}} - \sin x^{\frac{2}{3}}\right] + c$
- **(D)** $3\left[-x^{\frac{2}{3}}\cos x^{\frac{2}{3}} + \sin x^{\frac{2}{3}}\right] + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3\left[-x^{\frac{2}{3}}\cos x^{\frac{2}{3}} + \sin x^{\frac{2}{3}}\right] + c$**

**Detailed Solution:**

Let $x^{\dfrac{2}{3}} = t$.

Differentiating with respect to $x$, we get $\dfrac{2}{3}x^{-\dfrac{1}{3}}dx = dt \Rightarrow dx = \dfrac{3}{2}x^{\dfrac{1}{3}}dt$.

Substituting this in the integral:

$I = \int 2x^{\dfrac{1}{3}} \sin t \left(\dfrac{3}{2}x^{\dfrac{1}{3}}dt\right)$

$I = \int 3x^{\dfrac{2}{3}} \sin t \, dt$

Since $x^{\dfrac{2}{3}} = t$, we have:

$I = 3 \int t \sin t \, dt$

Using integration by parts:

$I = 3 \left[ t(-\cos t) - \int (-\cos t) \, dt \right]$

$I = 3 \left[ -t \cos t + \sin t \right] + c$

Substituting $t = x^{\dfrac{2}{3}}$ back:

$I = 3 \left[ -x^{\dfrac{2}{3}} \cos x^{\dfrac{2}{3}} + \sin x^{\dfrac{2}{3}} \right] + c$

Answer: $3\left[-x^{\frac{2}{3}}\cos x^{\frac{2}{3}} + \sin x^{\frac{2}{3}}\right] + c$

</details>

---

### Q50. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f'(x) = \dfrac{(\sqrt{x}+1)e^{\sqrt{x}}}{\sqrt{x}}$ and $f(0) = e$ then $f(1) = \ldots\ldots\ldots\ldots$

**Options:**

- **(A)** $e$
- **(B)** $2e$
- **(C)** $3e$
- **(D)** $4e$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3e$**

**Detailed Solution:**

$f(x) = \int \dfrac{(\sqrt{x}+1)e^{\sqrt{x}}}{\sqrt{x}} dx$

Let $\sqrt{x} = t \Rightarrow \dfrac{1}{2\sqrt{x}} dx = dt \Rightarrow \dfrac{dx}{\sqrt{x}} = 2 dt$

$f(x) = \int (t+1)e^t (2 dt) = 2 \int (t+1)e^t dt$

$f(x) = 2 t e^t + C$

Substituting $t = \sqrt{x}$:

$f(x) = 2 \sqrt{x} e^{\sqrt{x}} + C$

Given $f(0) = e$:

$2(0)e^0 + C = e \Rightarrow C = e$

Thus, $f(x) = 2 \sqrt{x} e^{\sqrt{x}} + e$

For $x = 1$:

$f(1) = 2(1)e^1 + e = 3e$

Answer: $3e$

</details>

---

### Q51. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int\dfrac{x^4 + 1}{x^6 + 1}dx = $

**Options:**

- **(A)** $\tan^{-1}x - \dfrac{1}{3}\tan^{-1}(x^3) + c$
- **(B)** $\tan^{-1}x + \dfrac{1}{3}\tan^{-1}(x^3) + c$
- **(C)** $\tan^{-1}x - \tan^{-1}(x^3) + c$
- **(D)** $\tan^{-1}x + \tan^{-1}(x^3) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\tan^{-1}x + \dfrac{1}{3}\tan^{-1}(x^3) + c$**

**Detailed Solution:**

The given integral is $I = \int \dfrac{x^4 + 1}{x^6 + 1} dx$

The denominator can be factored as $x^6 + 1 = (x^2)^3 + 1 = (x^2 + 1)(x^4 - x^2 + 1)$

Rewriting the numerator as $x^4 + 1 = (x^4 - x^2 + 1) + x^2$

$I = \int \dfrac{(x^4 - x^2 + 1) + x^2}{(x^2 + 1)(x^4 - x^2 + 1)} dx$

Separating the terms:

$I = \int \dfrac{x^4 - x^2 + 1}{(x^2 + 1)(x^4 - x^2 + 1)} dx + \int \dfrac{x^2}{x^6 + 1} dx$

$I = \int \dfrac{1}{x^2 + 1} dx + \dfrac{1}{3} \int \dfrac{3x^2}{(x^3)^2 + 1} dx$

Substituting $t = x^3 \Rightarrow dt = 3x^2 dx$ in the second integral:

$I = \tan^{-1}x + \dfrac{1}{3} \int \dfrac{1}{t^2 + 1} dt$

$I = \tan^{-1}x + \dfrac{1}{3} \tan^{-1}(t) + c$

$I = \tan^{-1}x + \dfrac{1}{3} \tan^{-1}(x^3) + c$

Answer: $\tan^{-1}x + \dfrac{1}{3}\tan^{-1}(x^3) + c$

</details>

---

### Q52. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $a > 0, b > 0$ and $\int\dfrac{1}{ax^2 + b}dx = \dfrac{1}{\sqrt{6}}\tan^{-1}\left(\dfrac{\sqrt{2}x}{\sqrt{3}}\right) + c$, then $\int\dfrac{1}{bx^2 + a}dx = \ldots$

**Options:**

- **(A)** $-\dfrac{1}{\sqrt{6}}\tan^{-1}\left(\dfrac{\sqrt{2}x}{\sqrt{3}}\right) + c$
- **(B)** $\dfrac{1}{\sqrt{6}}\tan^{-1}\left(\dfrac{\sqrt{3}x}{\sqrt{2}}\right) + c$
- **(C)** $-\sqrt{6}\,\tan^{-1}\left(\dfrac{\sqrt{2}x}{\sqrt{3}}\right) + c$
- **(D)** $\sqrt{6}\,\tan^{-1}\left(\dfrac{\sqrt{3}x}{\sqrt{2}}\right) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{\sqrt{6}}\tan^{-1}\left(\dfrac{\sqrt{3}x}{\sqrt{2}}\right) + c$**

**Detailed Solution:**

We know that $\int\dfrac{1}{ax^2 + b}dx = \dfrac{1}{\sqrt{ab}}\tan^{-1}\left(\sqrt{\dfrac{a}{b}}x\right) + c$

Comparing this with the given expression $\dfrac{1}{\sqrt{6}}\tan^{-1}\left(\dfrac{\sqrt{2}x}{\sqrt{3}}\right) + c$, we get:

$\dfrac{1}{\sqrt{ab}} = \dfrac{1}{\sqrt{6}} \Rightarrow ab = 6$

$\sqrt{\dfrac{a}{b}} = \dfrac{\sqrt{2}}{\sqrt{3}} \Rightarrow \dfrac{a}{b} = \dfrac{2}{3}$

Multiplying the two equations, we get $a^2 = 4 \Rightarrow a = 2$ (since $a > 0$).

Substituting $a = 2$ in $ab = 6$, we get $b = 3$.

Now, we need to evaluate $\int\dfrac{1}{bx^2 + a}dx$:

$\int\dfrac{1}{3x^2 + 2}dx = \dfrac{1}{\sqrt{3 \times 2}}\tan^{-1}\left(\sqrt{\dfrac{3}{2}}x\right) + c$

$= \dfrac{1}{\sqrt{6}}\tan^{-1}\left(\dfrac{\sqrt{3}x}{\sqrt{2}}\right) + c$

Answer: $\dfrac{1}{\sqrt{6}}\tan^{-1}\left(\dfrac{\sqrt{3}x}{\sqrt{2}}\right) + c$

</details>

---

### Q53. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\displaystyle\int \dfrac{(x + 1)(x + \log x)^2}{x}\,dx =$

**Options:**

- **(A)** $\left(\dfrac{x + \log x}{x}\right)^2 + c$, where c is the constant of integration
- **(B)** $\dfrac{(x + \log x)^2}{x} + c$, where c is the constant of integration
- **(C)** $\dfrac{(x + \log x)^3}{3} + c$, where c is the constant of integration
- **(D)** $\dfrac{(x + \log x)^3}{3x} + c$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{(x + \log x)^3}{3} + c$, where c is the constant of integration**

**Detailed Solution:**

Let $I = \displaystyle\int \dfrac{(x + 1)(x + \log x)^2}{x} \, dx$

$I = \displaystyle\int \left( 1 + \dfrac{1}{x} \right) (x + \log x)^2 \, dx$

Substituting $x + \log x = t$

Differentiating with respect to $x$,

$\left( 1 + \dfrac{1}{x} \right) dx = dt$

Substituting $t$ and $dt$ into the integral,

$I = \displaystyle\int t^2 \, dt$

$I = \dfrac{t^3}{3} + c$

Substituting back $t = x + \log x$,

$I = \dfrac{(x + \log x)^3}{3} + c$

Answer: $\dfrac{(x + \log x)^3}{3} + c$, where c is the constant of integration

</details>

---

### Q54. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\displaystyle\int \cot^4 x\,dx$ is equal to

**Options:**

- **(A)** $\dfrac{\cot^3 x}{3} - \cot x + x + c$
- **(B)** $\dfrac{\cot^3 x}{3} + \cot x + x + c$
- **(C)** $-\dfrac{\cot^3 x}{3} + \cot x + x + c$
- **(D)** $\dfrac{\cot^3 x}{3} - 2\cot x + x + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\dfrac{\cot^3 x}{3} + \cot x + x + c$**

**Detailed Solution:**

$I = \int \cot^4 x \, dx$

$I = \int \cot^2 x (\csc^2 x - 1) \, dx$

$I = \int \cot^2 x \csc^2 x \, dx - \int \cot^2 x \, dx$

$I = \int \cot^2 x \csc^2 x \, dx - \int (\csc^2 x - 1) \, dx$

Substituting $\cot x = t \Rightarrow -\csc^2 x \, dx = dt$ in the first integral:

$I = -\int t^2 \, dt - (-\cot x - x) + c$

$I = -\dfrac{t^3}{3} + \cot x + x + c$

$I = -\dfrac{\cot^3 x}{3} + \cot x + x + c$

Answer: $-\dfrac{\cot^3 x}{3} + \cot x + x + c$

</details>

---

### Q55. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\displaystyle\int \dfrac{\cos^3 x}{\sin^2 x + \sin x}\,dx =$

**Options:**

- **(A)** $\log(\cos x) + \cos x + c$, where c is the constant of integration
- **(B)** $\log(\sin x) - \sin x + c$, where c is the constant of integration
- **(C)** $\log(\sin x) + \sin x + c$, where c is the constant of integration
- **(D)** $\log(\cos x) - \cos x + c$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log(\sin x) - \sin x + c$, where c is the constant of integration**

**Detailed Solution:**

Let $I = \displaystyle\int \dfrac{\cos^3 x}{\sin^2 x + \sin x} \,dx$

We can write $\cos^3 x = \cos^2 x \cos x = (1 - \sin^2 x) \cos x$

$I = \displaystyle\int \dfrac{1 - \sin^2 x}{\sin^2 x + \sin x} \cos x \,dx$

Let $\sin x = t$, then $\cos x \,dx = dt$

Substituting these into the integral, we get:

$I = \displaystyle\int \dfrac{1 - t^2}{t^2 + t} \,dt$

$I = \displaystyle\int \dfrac{(1 - t)(1 + t)}{t(t + 1)} \,dt$

$I = \displaystyle\int \dfrac{1 - t}{t} \,dt$

$I = \displaystyle\int \left(\dfrac{1}{t} - 1\right) \,dt$

$I = \log(t) - t + c$

Substituting back $t = \sin x$, we get:

$I = \log(\sin x) - \sin x + c$

Answer: $\log(\sin x) - \sin x + c$, where c is the constant of integration

</details>

---

### Q56. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \text{cosec}^{-1}\left(\sqrt{\dfrac{a+x}{x}}\right)\, \text{d}x =$

**Options:**

- **(A)** $a\theta\tan^2\theta - a\tan\theta - a\theta + c$  $\left(\text{where } \theta = \tan^{-1}\left(\sqrt{\dfrac{x}{a}}\right)\right)$ and c is the constant of integration
- **(B)** $a\theta\tan^2\theta - a\tan\theta + a\theta + c$  $\left(\text{where } \theta = \tan^{-1}\left(\sqrt{\dfrac{x}{a}}\right)\right)$ and c is the constant of integration
- **(C)** $a\theta\tan^2\theta + a\tan\theta - a\theta + c$  $\left(\text{where } \theta = \tan^{-1}\left(\sqrt{\dfrac{x}{a}}\right)\right)$ and c is the constant of integration
- **(D)** $a\theta\tan^2\theta + a\tan\theta + a\theta + c$  $\left(\text{where } \theta = \tan^{-1}\left(\sqrt{\dfrac{x}{a}}\right)\right)$ and c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $a\theta\tan^2\theta - a\tan\theta + a\theta + c$  $\left(\text{where } \theta = \tan^{-1}\left(\sqrt{\dfrac{x}{a}}\right)\right)$ and c is the constant of integration**

**Detailed Solution:**

Let $I = \int \text{cosec}^{-1}\left(\sqrt{\dfrac{a+x}{x}}\right)\, \text{d}x$.

Substitute $x = a\tan^2\theta$, which gives $\theta = \tan^{-1}\left(\sqrt{\dfrac{x}{a}}\right)$.

Differentiating both sides, we get $\text{d}x = 2a\tan\theta\sec^2\theta\, \text{d}\theta$.

The term inside the inverse trigonometric function simplifies as:

$\sqrt{\dfrac{a+x}{x}} = \sqrt{\dfrac{a+a\tan^2\theta}{a\tan^2\theta}} = \sqrt{\dfrac{1+\tan^2\theta}{\tan^2\theta}} = \sqrt{\dfrac{\sec^2\theta}{\tan^2\theta}} = \text{cosec}\theta$

Therefore, the integrand becomes $\text{cosec}^{-1}(\text{cosec}\theta) = \theta$.

The integral transforms to:

$I = \int \theta (2a\tan\theta\sec^2\theta)\, \text{d}\theta$

Applying integration by parts, taking $\theta$ as the first function and $2a\tan\theta\sec^2\theta$ as the second function:

$I = \theta \int 2a\tan\theta\sec^2\theta\, \text{d}\theta - \int \left( \dfrac{\text{d}}{\text{d}\theta}(\theta) \int 2a\tan\theta\sec^2\theta\, \text{d}\theta \right) \text{d}\theta$

Since $\int 2a\tan\theta\sec^2\theta\, \text{d}\theta = a\tan^2\theta$, we get:

$I = \theta(a\tan^2\theta) - \int 1 \cdot (a\tan^2\theta)\, \text{d}\theta$

$I = a\theta\tan^2\theta - a\int (\sec^2\theta - 1)\, \text{d}\theta$

$I = a\theta\tan^2\theta - a(\tan\theta - \theta) + c$

$I = a\theta\tan^2\theta - a\tan\theta + a\theta + c$

Answer: $a\theta\tan^2\theta - a\tan\theta + a\theta + c$  $\left(\text{where } \theta = \tan^{-1}\left(\sqrt{\dfrac{x}{a}}\right)\right)$ and c is the constant of integration

</details>

---

### Q57. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \dfrac{1}{\cos^3 x \sqrt{\sin 2x}}\, dx = p(\tan^2 x + q)\sqrt{\tan x} + c$, then the values of $p$ and $q$ respectively are

**Options:**

- **(A)** $p = \dfrac{\sqrt{2}}{5}, q = \dfrac{1}{5}$
- **(B)** $p = \dfrac{\sqrt{2}}{3}, q = 3$
- **(C)** $p = \dfrac{\sqrt{2}}{5}, q = 5$
- **(D)** $p = \dfrac{2}{\sqrt{5}}, q = \sqrt{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $p = \dfrac{\sqrt{2}}{5}, q = 5$**

**Detailed Solution:**

Let $I = \int \dfrac{1}{\cos^3 x \sqrt{\sin 2x}} dx$

Using $\sin 2x = 2 \sin x \cos x$, we get:

$I = \int \dfrac{1}{\cos^3 x \sqrt{2 \sin x \cos x}} dx$

$I = \dfrac{1}{\sqrt{2}} \int \dfrac{1}{\cos^{7/2} x \sin^{1/2} x} dx$

Dividing the numerator and the denominator by $\cos^4 x$, we get:

$I = \dfrac{1}{\sqrt{2}} \int \dfrac{\sec^4 x}{\tan^{1/2} x} dx$

Let $\tan x = t \Rightarrow \sec^2 x dx = dt$

$I = \dfrac{1}{\sqrt{2}} \int \dfrac{1 + t^2}{\sqrt{t}} dt$

$I = \dfrac{1}{\sqrt{2}} \int (t^{-1/2} + t^{3/2}) dt$

$I = \dfrac{1}{\sqrt{2}} \left( \dfrac{t^{1/2}}{1/2} + \dfrac{t^{5/2}}{5/2} \right) + c$

$I = \dfrac{1}{\sqrt{2}} \left( 2\sqrt{t} + \dfrac{2}{5}t^{5/2} \right) + c$

$I = \sqrt{2} \sqrt{t} \left( 1 + \dfrac{1}{5}t^2 \right) + c$

$I = \dfrac{\sqrt{2}}{5} (t^2 + 5) \sqrt{t} + c$

Substituting $t = \tan x$:

$I = \dfrac{\sqrt{2}}{5} (\tan^2 x + 5) \sqrt{\tan x} + c$

Comparing this with $p(\tan^2 x + q)\sqrt{\tan x} + c$, we get:

$p = \dfrac{\sqrt{2}}{5}$ and $q = 5$

Answer: $p = \dfrac{\sqrt{2}}{5}, q = 5$

</details>

---

### Q58. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \sqrt{2}\sqrt{1+\sin x}\, dx = -4\cos(ax+b) + c$, then the value of $a, b$ respectively are...

**Options:**

- **(A)** $\dfrac{1}{2}, \dfrac{\pi}{2}$
- **(B)** $\dfrac{1}{2}, \dfrac{\pi}{4}$
- **(C)** $\dfrac{x}{2}, \dfrac{\pi}{4}$
- **(D)** $1, \dfrac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{2}, \dfrac{\pi}{4}$**

**Detailed Solution:**

The given integral is $\int \sqrt{2}\sqrt{1+\sin x} \, dx$.

Using the trigonometric identity $1 + \sin x = \left(\sin\dfrac{x}{2} + \cos\dfrac{x}{2}\right)^2$, the integral becomes:

$\int \sqrt{2} \left(\sin\dfrac{x}{2} + \cos\dfrac{x}{2}\right) \, dx$

Integrating the terms, we get:

$\sqrt{2} \left(-2\cos\dfrac{x}{2} + 2\sin\dfrac{x}{2}\right) + c$

$-2\sqrt{2} \left(\cos\dfrac{x}{2} - \sin\dfrac{x}{2}\right) + c$

Multiplying and dividing the expression inside the parenthesis by $\sqrt{2}$:

$-2\sqrt{2} \times \sqrt{2} \left(\dfrac{1}{\sqrt{2}}\cos\dfrac{x}{2} - \dfrac{1}{\sqrt{2}}\sin\dfrac{x}{2}\right) + c$

$-4 \left(\cos\dfrac{x}{2}\cos\dfrac{\pi}{4} - \sin\dfrac{x}{2}\sin\dfrac{\pi}{4}\right) + c$

Using the formula $\cos(A+B) = \cos A \cos B - \sin A \sin B$:

$-4\cos\left(\dfrac{x}{2} + \dfrac{\pi}{4}\right) + c$

Comparing this with the given expression $-4\cos(ax+b) + c$, we obtain:

$a = \dfrac{1}{2}, b = \dfrac{\pi}{4}$

Answer: $\dfrac{1}{2}, \dfrac{\pi}{4}$

</details>

---

### Q59. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{\sqrt{x-2}}{x}dx = $

**Options:**

- **(A)** $2\sqrt{x-2} - 2\sqrt{2}\tan^{-1}\left(\dfrac{\sqrt{x-2}}{\sqrt{2}}\right) + c$
- **(B)** $2\sqrt{x-2} + 2\sqrt{2}\tan^{-1}\left(\dfrac{\sqrt{x-2}}{\sqrt{2}}\right) + c$
- **(C)** $2\sqrt{x-2} - 2\sqrt{2}\tan^{-1}\left(\dfrac{\sqrt{x-2}}{2}\right) + c$
- **(D)** $2\sqrt{x-2} + 2\sqrt{2}\tan^{-1}\left(\dfrac{\sqrt{x-2}}{2}\right) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2\sqrt{x-2} - 2\sqrt{2}\tan^{-1}\left(\dfrac{\sqrt{x-2}}{\sqrt{2}}\right) + c$**

**Detailed Solution:**

Let $x - 2 = t^2$, which gives $dx = 2t dt$ and $x = t^2 + 2$.

Substituting these into the integral:

$I = \int \dfrac{t}{t^2 + 2} (2t dt) = 2 \int \dfrac{t^2}{t^2 + 2} dt$

$I = 2 \int \dfrac{t^2 + 2 - 2}{t^2 + 2} dt = 2 \int \left( 1 - \dfrac{2}{t^2 + 2} \right) dt$

$I = 2 \left( t - \dfrac{2}{\sqrt{2}} \tan^{-1} \left( \dfrac{t}{\sqrt{2}} \right) \right) + c$

$I = 2t - 2\sqrt{2} \tan^{-1} \left( \dfrac{t}{\sqrt{2}} \right) + c$

Substituting back $t = \sqrt{x-2}$:

$I = 2\sqrt{x-2} - 2\sqrt{2} \tan^{-1} \left( \dfrac{\sqrt{x-2}}{\sqrt{2}} \right) + c$

Answer: $2\sqrt{x-2} - 2\sqrt{2}\tan^{-1}\left(\dfrac{\sqrt{x-2}}{\sqrt{2}}\right) + c$

</details>

---

### Q60. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{(x+1)}{x(1+xe^x)^2}dx =$

**Options:**

- **(A)** $-\log\left(\dfrac{xe^x}{1+xe^x}\right) + \dfrac{1}{(1+xe^x)} + c$
- **(B)** $\log\left(\dfrac{xe^x}{1+xe^x}\right) + \dfrac{1}{(1+xe^x)} + c$
- **(C)** $\log\left(\dfrac{1+xe^x}{xe^x}\right) + (1+xe^x) + c$
- **(D)** $-\log\left(\dfrac{xe^x}{1+xe^x}\right) - \dfrac{1}{(1+xe^x)} + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log\left(\dfrac{xe^x}{1+xe^x}\right) + \dfrac{1}{(1+xe^x)} + c$**

**Detailed Solution:**

Let $I = \int \dfrac{x+1}{x(1+xe^x)^2} dx$

Multiplying the numerator and the denominator by $e^x$, we get:

$I = \int \dfrac{(x+1)e^x}{xe^x(1+xe^x)^2} dx$

Let $xe^x = t$. Differentiating both sides with respect to $x$, we get:

$(1 \cdot e^x + x \cdot e^x) dx = dt \Rightarrow (x+1)e^x dx = dt$

Substituting these into the integral:

$I = \int \dfrac{dt}{t(1+t)^2}$

Using partial fractions:

$\dfrac{1}{t(1+t)^2} = \dfrac{1+t-t}{t(1+t)^2} = \dfrac{1}{t(1+t)} - \dfrac{1}{(1+t)^2}$

$\dfrac{1}{t(1+t)^2} = \dfrac{1+t-t}{t(1+t)} - \dfrac{1}{(1+t)^2} = \dfrac{1}{t} - \dfrac{1}{1+t} - \dfrac{1}{(1+t)^2}$

Integrating with respect to $t$:

$I = \int \left( \dfrac{1}{t} - \dfrac{1}{1+t} - \dfrac{1}{(1+t)^2} \right) dt$

$I = \log|t| - \log|1+t| + \dfrac{1}{1+t} + c$

$I = \log\left|\dfrac{t}{1+t}\right| + \dfrac{1}{1+t} + c$

Substituting back $t = xe^x$:

$I = \log\left(\dfrac{xe^x}{1+xe^x}\right) + \dfrac{1}{1+xe^x} + c$

Answer: $\log\left(\dfrac{xe^x}{1+xe^x}\right) + \dfrac{1}{(1+xe^x)} + c$

</details>

---

### Q61. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \dfrac{x+1}{x^2+1}dx = \tan^{-1}x + g(x) + c$, where $c$ is constant of integration, then the function $g(x)$ is monotonically increasing in the interval

**Options:**

- **(A)** $R^+$
- **(B)** $R^-$
- **(C)** $R$
- **(D)** $R - \{0\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $R^+$**

**Detailed Solution:**

$\int \dfrac{x+1}{x^2+1}dx = \int \dfrac{x}{x^2+1}dx + \int \dfrac{1}{x^2+1}dx$

$= \dfrac{1}{2}\ln(x^2+1) + \tan^{-1}x + c$

Comparing with the given equation, we get:

$g(x) = \dfrac{1}{2}\ln(x^2+1)$

For $g(x)$ to be monotonically increasing, $g'(x) \ge 0$.

$g'(x) = \dfrac{x}{x^2+1} \ge 0$

Since $x^2+1 > 0$ for all $x \in R$, we must have $x \ge 0$.

Thus, $g(x)$ is monotonically increasing in $R^+$.

Answer: $R^+$

</details>

---

### Q62. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \sqrt{1+\sin x}\,dx$ is equal to

**Options:**

- **(A)** $2\sqrt{2}\sin\left(\dfrac{x}{2} - \dfrac{\pi}{4}\right) + c$
- **(B)** $2\sqrt{2}\sin\left(\dfrac{x}{2} + \dfrac{\pi}{4}\right) + c$
- **(C)** $\sqrt{2}\sin\left(\dfrac{x}{2} - \dfrac{\pi}{4}\right) + c$
- **(D)** $\sqrt{2}\sin\left(\dfrac{x}{2} + \dfrac{\pi}{4}\right) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2\sqrt{2}\sin\left(\dfrac{x}{2} - \dfrac{\pi}{4}\right) + c$**

**Detailed Solution:**

$I = \int \sqrt{1+\sin x}\,dx$

Using the trigonometric identities $\sin^2\left(\dfrac{x}{2}\right) + \cos^2\left(\dfrac{x}{2}\right) = 1$ and $\sin x = 2\sin\left(\dfrac{x}{2}\right)\cos\left(\dfrac{x}{2}\right)$, we get:

$1 + \sin x = \sin^2\left(\dfrac{x}{2}\right) + \cos^2\left(\dfrac{x}{2}\right) + 2\sin\left(\dfrac{x}{2}\right)\cos\left(\dfrac{x}{2}\right) = \left(\sin\left(\dfrac{x}{2}\right) + \cos\left(\dfrac{x}{2}\right)\right)^2$

Substituting this into the integral:

$I = \int \left(\sin\left(\dfrac{x}{2}\right) + \cos\left(\dfrac{x}{2}\right)\right)\,dx$

Integrating term by term:

$I = -2\cos\left(\dfrac{x}{2}\right) + 2\sin\left(\dfrac{x}{2}\right) + c$

$I = 2\left(\sin\left(\dfrac{x}{2}\right) - \cos\left(\dfrac{x}{2}\right)\right) + c$

Multiplying and dividing by $\sqrt{2}$:

$I = 2\sqrt{2}\left(\sin\left(\dfrac{x}{2}\right)\dfrac{1}{\sqrt{2}} - \cos\left(\dfrac{x}{2}\right)\dfrac{1}{\sqrt{2}}\right) + c$

$I = 2\sqrt{2}\left(\sin\left(\dfrac{x}{2}\right)\cos\left(\dfrac{\pi}{4}\right) - \cos\left(\dfrac{x}{2}\right)\sin\left(\dfrac{\pi}{4}\right)\right) + c$

Using the identity $\sin(A - B) = \sin A \cos B - \cos A \sin B$:

$I = 2\sqrt{2}\sin\left(\dfrac{x}{2} - \dfrac{\pi}{4}\right) + c$

Answer: $2\sqrt{2}\sin\left(\dfrac{x}{2} - \dfrac{\pi}{4}\right) + c$

</details>

---

### Q63. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\displaystyle\int \dfrac{30x^{14} + 15^x \log 225}{x^{15} + 15^x} \, dx =$

**Options:**

- **(A)** $x^{15} + 15x^{14} + 30x^{13} + c$, where c is the constant of integration
- **(B)** $\dfrac{\log(x^{15} + 15^x)}{2} + c$, where c is the constant of integration
- **(C)** $\log(x^{15} + 15^x)^2 + c$, where c is the constant of integration
- **(D)** $\log(x^{15} + 15^x) + c$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log(x^{15} + 15^x)^2 + c$, where c is the constant of integration**

**Detailed Solution:**

Let $I = \displaystyle\int \dfrac{30x^{14} + 15^x \log 225}{x^{15} + 15^x} \, dx$

Let $x^{15} + 15^x = t$

Differentiating both sides with respect to $x$, we get

$(15x^{14} + 15^x \log 15) \, dx = dt$

Multiplying by $2$, we get

$(30x^{14} + 2 \cdot 15^x \log 15) \, dx = 2 \, dt$

Since $2 \log 15 = \log(15^2) = \log 225$, this becomes

$(30x^{14} + 15^x \log 225) \, dx = 2 \, dt$

Substituting this into the integral, we obtain

$I = \displaystyle\int \dfrac{2}{t} \, dt$

$I = 2 \log t + c$

$I = \log(t^2) + c$

$I = \log(x^{15} + 15^x)^2 + c$

Answer: $\log(x^{15} + 15^x)^2 + c$, where c is the constant of integration

</details>

---

### Q64. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\displaystyle\int \dfrac{\sin 2x}{\sin^4 x + \cos^4 x} \, dx = f(x) + c$ where c is constant of integration, then the value of $\tan(f(x))$ is

**Options:**

- **(A)** $\tan x$
- **(B)** $\tan^2 x$
- **(C)** $\tan^4 x$
- **(D)** $\cot^4 x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\tan^2 x$**

**Detailed Solution:**

The given integral is $\displaystyle\int \dfrac{\sin 2x}{\sin^4 x + \cos^4 x} \, dx$.

Dividing the numerator and the denominator by $\cos^4 x$, we get

$\displaystyle\int \dfrac{\dfrac{2\sin x \cos x}{\cos^4 x}}{\dfrac{\sin^4 x + \cos^4 x}{\cos^4 x}} \, dx$

$= \displaystyle\int \dfrac{2\tan x \sec^2 x}{\tan^4 x + 1} \, dx$

Substituting $\tan^2 x = t$, we get $2\tan x \sec^2 x \, dx = dt$.

The integral becomes

$\displaystyle\int \dfrac{dt}{t^2 + 1} = \tan^{-1}(t) + c$

Substituting back $t = \tan^2 x$, we get

$f(x) + c = \tan^{-1}(\tan^2 x) + c$

Comparing both sides, $f(x) = \tan^{-1}(\tan^2 x)$.

Therefore, $\tan(f(x)) = \tan(\tan^{-1}(\tan^2 x)) = \tan^2 x$.

Answer: $\tan^2 x$

</details>

---

### Q65. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \dfrac{\sin x}{\sin 4x} dx = $

**Options:**

- **(A)** $\dfrac{1}{4\sqrt{2}}\log\left|\dfrac{1 + \sqrt{2}\sin x}{1 - \sqrt{2}\sin x}\right| + \dfrac{1}{4}\log|\sec x + \tan x| + c$
- **(B)** $\dfrac{1}{4\sqrt{2}}\log\left|\dfrac{1 + \sqrt{2}\sin x}{1 - \sqrt{2}\sin x}\right| - \dfrac{1}{4}\log|\sec x + \tan x| + c$
- **(C)** $\dfrac{1}{4\sqrt{2}}\log\left|\dfrac{1 - \sqrt{2}\sin x}{1 + \sqrt{2}\sin x}\right| + \dfrac{1}{4}\log|\sec x + \tan x| + c$
- **(D)** $\dfrac{1}{4\sqrt{2}}\log\left|\dfrac{1 - \sqrt{2}\sin x}{1 + \sqrt{2}\sin x}\right| - \dfrac{1}{4}\log|\sec x + \tan x| + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{4\sqrt{2}}\log\left|\dfrac{1 + \sqrt{2}\sin x}{1 - \sqrt{2}\sin x}\right| - \dfrac{1}{4}\log|\sec x + \tan x| + c$**

**Detailed Solution:**

Let $I = \int \dfrac{\sin x}{\sin 4x} dx$

Using the identity $\sin 4x = 2\sin 2x \cos 2x = 4\sin x \cos x \cos 2x$, we get:

$I = \int \dfrac{\sin x}{4\sin x \cos x \cos 2x} dx = \int \dfrac{1}{4\cos x \cos 2x} dx$

Multiplying the numerator and the denominator by $\cos x$:

$I = \int \dfrac{\cos x}{4\cos^2 x \cos 2x} dx = \int \dfrac{\cos x}{4(1 - \sin^2 x)(1 - 2\sin^2 x)} dx$

Substitute $\sin x = t \Rightarrow \cos x dx = dt$:

$I = \int \dfrac{1}{4(1 - t^2)(1 - 2t^2)} dt$

Using partial fractions:

$\dfrac{1}{(1 - t^2)(1 - 2t^2)} = \dfrac{2}{1 - 2t^2} - \dfrac{1}{1 - t^2}$

$I = \dfrac{1}{4} \int \left( \dfrac{2}{1 - 2t^2} - \dfrac{1}{1 - t^2} \right) dt$

$I = \dfrac{1}{2} \int \dfrac{1}{1 - (\sqrt{2}t)^2} dt - \dfrac{1}{4} \int \dfrac{1}{1 - t^2} dt$

Using the standard integral $\int \dfrac{1}{a^2 - x^2} dx = \dfrac{1}{2a} \log \left| \dfrac{a + x}{a - x} \right| + c$:

$I = \dfrac{1}{2} \left( \dfrac{1}{2\sqrt{2}} \log \left| \dfrac{1 + \sqrt{2}t}{1 - \sqrt{2}t} \right| \right) - \dfrac{1}{4} \left( \dfrac{1}{2} \log \left| \dfrac{1 + t}{1 - t} \right| \right) + c$

$I = \dfrac{1}{4\sqrt{2}} \log \left| \dfrac{1 + \sqrt{2}\sin x}{1 - \sqrt{2}\sin x} \right| - \dfrac{1}{8} \log \left| \dfrac{1 + \sin x}{1 - \sin x} \right| + c$

Since $\dfrac{1 + \sin x}{1 - \sin x} = \dfrac{(1 + \sin x)^2}{1 - \sin^2 x} = \dfrac{(1 + \sin x)^2}{\cos^2 x} = (\sec x + \tan x)^2$:

$\dfrac{1}{8} \log \left| \dfrac{1 + \sin x}{1 - \sin x} \right| = \dfrac{1}{8} \log (\sec x + \tan x)^2 = \dfrac{1}{4} \log |\sec x + \tan x|$

Therefore,

$I = \dfrac{1}{4\sqrt{2}} \log \left| \dfrac{1 + \sqrt{2}\sin x}{1 - \sqrt{2}\sin x} \right| - \dfrac{1}{4} \log |\sec x + \tan x| + c$

Answer: $\dfrac{1}{4\sqrt{2}}\log\left|\dfrac{1 + \sqrt{2}\sin x}{1 - \sqrt{2}\sin x}\right| - \dfrac{1}{4}\log|\sec x + \tan x| + c$

</details>

---

### Q66. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \sqrt{4^x(4^x + 4)}\, dx = \cdots$

**Options:**

- **(A)** $\dfrac{1}{\log 2}\left[\dfrac{2^x}{2}\sqrt{4^x + 4} + 2\log|2^x + \sqrt{4^x + 4}|\right] + c$
- **(B)** $\dfrac{2^x}{2}\sqrt{4^x + 4} + 2\log|2^x + \sqrt{4^x + 4}| + c$
- **(C)** $\dfrac{1}{\log 2}\left[\dfrac{2^x}{2}\sqrt{4^x + 4} + \log|2^x + \sqrt{4^x + 4}|\right] + c$
- **(D)** $\left[\dfrac{2^x}{\log 4}\sqrt{4^x + 4} + \log|2^x + \sqrt{4^x + 4}|\right] + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{\log 2}\left[\dfrac{2^x}{2}\sqrt{4^x + 4} + 2\log|2^x + \sqrt{4^x + 4}|\right] + c$**

**Detailed Solution:**

$I = \int \sqrt{4^x(4^x + 4)}\, dx$

$I = \int 2^x \sqrt{(2^x)^2 + 4}\, dx$

Let $2^x = t$, then $2^x \log 2 \, dx = dt \Rightarrow 2^x \, dx = \dfrac{dt}{\log 2}$

$I = \dfrac{1}{\log 2} \int \sqrt{t^2 + 2^2} \, dt$

Using the standard integral $\int \sqrt{x^2 + a^2} \, dx = \dfrac{x}{2} \sqrt{x^2 + a^2} + \dfrac{a^2}{2} \log |x + \sqrt{x^2 + a^2}| + c$:

$I = \dfrac{1}{\log 2} \left[ \dfrac{t}{2} \sqrt{t^2 + 4} + \dfrac{4}{2} \log |t + \sqrt{t^2 + 4}| \right] + c$

Substituting $t = 2^x$:

$I = \dfrac{1}{\log 2} \left[ \dfrac{2^x}{2} \sqrt{4^x + 4} + 2 \log |2^x + \sqrt{4^x + 4}| \right] + c$

Answer: $\dfrac{1}{\log 2}\left[\dfrac{2^x}{2}\sqrt{4^x + 4} + 2\log|2^x + \sqrt{4^x + 4}|\right] + c$

</details>

---

### Q67. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\int \dfrac{1}{x^2 - 5x + 8} dx$ is equal to...

**Options:**

- **(A)** $\dfrac{2}{\sqrt{7}}\tan^{-1}\left(\dfrac{2x+5}{\sqrt{7}}\right) + c$
- **(B)** $-\dfrac{2}{\sqrt{7}}\tan^{-1}\left(\dfrac{2x-5}{\sqrt{7}}\right) + c$
- **(C)** $\dfrac{2}{\sqrt{7}}\tan^{-1}\left(\dfrac{2x-5}{\sqrt{7}}\right) + c$
- **(D)** $-\dfrac{2}{\sqrt{7}}\tan^{-1}\left(\dfrac{2x+5}{\sqrt{7}}\right) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{2}{\sqrt{7}}\tan^{-1}\left(\dfrac{2x-5}{\sqrt{7}}\right) + c$**

**Detailed Solution:**

Let $I = \int \dfrac{1}{x^2 - 5x + 8} dx$

Completing the square in the denominator:

$x^2 - 5x + 8 = x^2 - 5x + \dfrac{25}{4} - \dfrac{25}{4} + 8 = \left(x - \dfrac{5}{2}\right)^2 + \dfrac{7}{4}$

Substituting this into the integral:

$I = \int \dfrac{1}{\left(x - \dfrac{5}{2}\right)^2 + \left(\dfrac{\sqrt{7}}{2}\right)^2} dx$

Using the standard formula $\int \dfrac{1}{X^2 + a^2} dX = \dfrac{1}{a}\tan^{-1}\left(\dfrac{X}{a}\right) + c$:

$I = \dfrac{1}{\dfrac{\sqrt{7}}{2}}\tan^{-1}\left(\dfrac{x - \dfrac{5}{2}}{\dfrac{\sqrt{7}}{2}}\right) + c$

$I = \dfrac{2}{\sqrt{7}}\tan^{-1}\left(\dfrac{2x - 5}{\sqrt{7}}\right) + c$

Answer: $\dfrac{2}{\sqrt{7}}\tan^{-1}\left(\dfrac{2x-5}{\sqrt{7}}\right) + c$

</details>

---

### Q68. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \dfrac{dx}{\sqrt{2ax - x^2}} = f(g(x)) + c$, where $c$ is constant of integration, then $f(x), g(x)$ are respectively equal to

**Options:**

- **(A)** $\sin^{-1} x, \dfrac{x - a}{a}$
- **(B)** $\sin^{-1} x, \dfrac{x + a}{a}$
- **(C)** $\tan^{-1} x, \dfrac{x - a}{a}$
- **(D)** $\tan^{-1} x, \dfrac{x + a}{a}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sin^{-1} x, \dfrac{x - a}{a}$**

**Detailed Solution:**

The given integral is $I = \int \dfrac{dx}{\sqrt{2ax - x^2}}$

Completing the square for the expression inside the square root:

$2ax - x^2 = a^2 - (x^2 - 2ax + a^2) = a^2 - (x - a)^2$

Substituting this back into the integral:

$I = \int \dfrac{dx}{\sqrt{a^2 - (x - a)^2}}$

Using the standard integration formula $\int \dfrac{dt}{\sqrt{a^2 - t^2}} = \sin^{-1}\left(\dfrac{t}{a}\right) + c$, we get:

$I = \sin^{-1}\left(\dfrac{x - a}{a}\right) + c$

Comparing this with $f(g(x)) + c$, we have:

$f(x) = \sin^{-1} x$

$g(x) = \dfrac{x - a}{a}$

Answer: $\sin^{-1} x, \dfrac{x - a}{a}$

</details>

---

### Q69. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int \dfrac{x}{x + 2} dx$ is equal to

**Options:**

- **(A)** $x + 2\log(x + 2) + c$
- **(B)** $x + \log(x + 2) + c$
- **(C)** $x - \log(x + 2) + c$
- **(D)** $x - 2\log(x + 2) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x - 2\log(x + 2) + c$**

**Detailed Solution:**

Let $I = \int \dfrac{x}{x + 2} dx$

Adding and subtracting $2$ in the numerator, we get:

$I = \int \dfrac{x + 2 - 2}{x + 2} dx$

$I = \int \left(1 - \dfrac{2}{x + 2}\right) dx$

Integrating with respect to $x$:

$I = x - 2\log(x + 2) + c$

Answer: $x - 2\log(x + 2) + c$

</details>

---

### Q70. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\sin 7 x}{\cos 9 x \cos 2 x} \mathrm{~d} x$ is equal to

**Options:**

- **(A)** $\log \sec (9 x)-\log \sec (2 x)+c$, where $c$ is the constant of integration
- **(B)** $\log \sec (9 x)+\log \sec (2 x)+c, \quad$ where $c$ is the constant of integration
- **(C)** $\frac{1}{9} \log \sec (9 x)-\frac{1}{2} \log \sec (2 x)+c$, where $c$ is the constant of integration
- **(D)** $\frac{1}{9} \log \sec (9 x)+\frac{1}{2} \log \sec (2 x)+c$, where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{9} \log \sec (9 x)-\frac{1}{2} \log \sec (2 x)+c$, where $c$ is the constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{\sin 7x}{\cos 9x \cos 2x} \mathrm{~d} x$

The numerator can be written as $\sin 7x = \sin(9x - 2x)$.

Using the formula $\sin(A - B) = \sin A \cos B - \cos A \sin B$, we get:

$\sin(9x - 2x) = \sin 9x \cos 2x - \cos 9x \sin 2x$

Substituting this into the integral:

$I = \int \dfrac{\sin 9x \cos 2x - \cos 9x \sin 2x}{\cos 9x \cos 2x} \mathrm{~d} x$

Separating the terms in the numerator:

$I = \int \left( \dfrac{\sin 9x \cos 2x}{\cos 9x \cos 2x} - \dfrac{\cos 9x \sin 2x}{\cos 9x \cos 2x} \right) \mathrm{~d} x$

$I = \int (\tan 9x - \tan 2x) \mathrm{~d} x$

Using the standard integral $\int \tan(ax) \mathrm{~d} x = \dfrac{1}{a} \log \sec(ax) + c$, we get:

$I = \dfrac{1}{9} \log \sec(9x) - \dfrac{1}{2} \log \sec(2x) + c$

Answer: $\frac{1}{9} \log \sec (9 x)-\frac{1}{2} \log \sec (2 x)+c$, where $c$ is the constant of integration

</details>

---

### Q71. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\mathrm{d} x}{\cos x(1+\cos x)}=$

**Options:**

- **(A)** $\log (\sec x+\tan x)+2 \tan \left(\frac{x}{2}\right)+c$, where $c$ is the constant of integration
- **(B)** $\log (\sec x+\tan x)-2 \tan \left(\frac{x}{2}\right)+c$, where $c$ is the constant of integration
- **(C)** $\log (\sec x+\tan x)+\tan \left(\frac{x}{2}\right)+c, \quad$ where $c$ is the constant of integration
- **(D)** $\log (\sec x+\tan x)-\tan \left(\frac{x}{2}\right)+c, \quad$ where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log (\sec x+\tan x)-\tan \left(\frac{x}{2}\right)+c, \quad$ where $c$ is the constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{1}{\cos x(1+\cos x)} \mathrm{d} x$

We can rewrite the numerator as $1 = (1+\cos x) - \cos x$.

$I = \int \dfrac{1+\cos x - \cos x}{\cos x(1+\cos x)} \mathrm{d} x$

$I = \int \left( \dfrac{1}{\cos x} - \dfrac{1}{1+\cos x} \right) \mathrm{d} x$

$I = \int \sec x \mathrm{d} x - \int \dfrac{1}{2\cos^2\left(\dfrac{x}{2}\right)} \mathrm{d} x$

$I = \int \sec x \mathrm{d} x - \dfrac{1}{2} \int \sec^2\left(\dfrac{x}{2}\right) \mathrm{d} x$

Integrating both terms, we get:

$I = \log (\sec x + \tan x) - \dfrac{1}{2} \dfrac{\tan\left(\dfrac{x}{2}\right)}{\dfrac{1}{2}} + c$

$I = \log (\sec x + \tan x) - \tan\left(\dfrac{x}{2}\right) + c$

Answer: $\log (\sec x+\tan x)-\tan \left(\frac{x}{2}\right)+c, \quad$ where $c$ is the constant of integration

</details>

---

### Q72. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{e^x}{\sqrt{\mathrm{e}^{2 x}+4 \mathrm{e}^x+13}} d x=\log \left|e^{a x}+2+\sqrt{\mathrm{e}^{2 x}+4 \mathrm{e}^x+13}\right|+\mathrm{c}$, (where c is the constant of integration), then the value of $a$ is equal to

**Options:**

- **(A)** 1
- **(B)** 0
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

Let $I = \int \dfrac{e^x}{\sqrt{e^{2x} + 4e^x + 13}} dx$

Substitute $e^x = t$, which gives $e^x dx = dt$.

$I = \int \dfrac{dt}{\sqrt{t^2 + 4t + 13}}$

$I = \int \dfrac{dt}{\sqrt{(t + 2)^2 + 3^2}}$

Using the standard integral formula $\int \dfrac{dx}{\sqrt{x^2 + A^2}} = \log |x + \sqrt{x^2 + A^2}| + c$, we get:

$I = \log |t + 2 + \sqrt{(t + 2)^2 + 3^2}| + c$

$I = \log |t + 2 + \sqrt{t^2 + 4t + 13}| + c$

Substituting back $t = e^x$:

$I = \log |e^x + 2 + \sqrt{e^{2x} + 4e^x + 13}| + c$

Comparing this with the given expression $\log |e^{ax} + 2 + \sqrt{e^{2x} + 4e^x + 13}| + c$, we get:

$a = 1$

Answer: 1

</details>

---

### Q73. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{d x}{x^{\frac{1}{2}}+x^{\frac{1}{3}}}=\mathrm{A} x^{\frac{1}{2}}+\mathrm{B} x^{\frac{1}{3}}+\mathrm{C} x^{\frac{1}{6}}+\mathrm{D} \log \left(x^{\frac{1}{6}}+1\right)+\mathrm{k}$
(where k is the integration constant) then values of $A, B, C$ and $D$ are respectively,

**Options:**

- **(A)** $2,-3,6,-6$
- **(B)** $2,3,-6,6$
- **(C)** $2,-3,-6,6$
- **(D)** $-2,-3,6,6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2,-3,6,-6$**

**Detailed Solution:**

Let $x = t^6$, then $dx = 6t^5 dt$.

Substituting into the integral, we get:

$\int \dfrac{6t^5}{t^3 + t^2} dt = \int \dfrac{6t^3}{t + 1} dt$

Adding and subtracting $1$ in the numerator:

$= 6 \int \dfrac{t^3 + 1 - 1}{t + 1} dt$

$= 6 \int \left( \dfrac{(t + 1)(t^2 - t + 1)}{t + 1} - \dfrac{1}{t + 1} \right) dt$

$= 6 \int \left( t^2 - t + 1 - \dfrac{1}{t + 1} \right) dt$

Integrating with respect to $t$:

$= 6 \left( \dfrac{t^3}{3} - \dfrac{t^2}{2} + t - \log|t + 1| \right) + k$

$= 2t^3 - 3t^2 + 6t - 6\log|t + 1| + k$

Substituting back $t = x^{\dfrac{1}{6}}$:

$= 2x^{\dfrac{1}{2}} - 3x^{\dfrac{1}{3}} + 6x^{\dfrac{1}{6}} - 6\log(x^{\dfrac{1}{6}} + 1) + k$

Comparing this with the given expression $\mathrm{A} x^{\dfrac{1}{2}}+\mathrm{B} x^{\dfrac{1}{3}}+\mathrm{C} x^{\dfrac{1}{6}}+\mathrm{D} \log \left(x^{\dfrac{1}{6}}+1\right)+\mathrm{k}$, we get:

$A = 2$, $B = -3$, $C = 6$, $D = -6$.

Answer: $2,-3,6,-6$

</details>

---

### Q74. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\sqrt{\tan x}}{\sin x \cdot \cos x} \mathrm{~d} x=$

**Options:**

- **(A)** $2 \sqrt{\sec x}+c$, where $c$ is a constant of integration
- **(B)** $2 \sqrt{\tan x}+c$, where $c$ is a constant of integration
- **(C)** $\frac{2}{\sqrt{\tan x}}+c$, where $c$ is a constant of integration
- **(D)** $\frac{2}{\sqrt{\sec x}}+c$, where $c$ is a constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \sqrt{\tan x}+c$, where $c$ is a constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{\sqrt{\tan x}}{\sin x \cdot \cos x} \mathrm{d} x$

Dividing the numerator and the denominator by $\cos^2 x$, we get

$I = \int \dfrac{\sqrt{\tan x} \cdot \sec^2 x}{\tan x} \mathrm{d} x$

$I = \int \dfrac{\sec^2 x}{\sqrt{\tan x}} \mathrm{d} x$

Let $\tan x = t$

Differentiating with respect to $x$, we get $\sec^2 x \mathrm{d} x = \mathrm{d} t$

Substituting these values in the integral, we get

$I = \int \dfrac{1}{\sqrt{t}} \mathrm{d} t$

$I = 2\sqrt{t} + c$

$I = 2\sqrt{\tan x} + c$

Answer: $2 \sqrt{\tan x}+c$, where $c$ is a constant of integration

</details>

---

### Q75. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{x^4 \cos \left(\tan ^{-1} x^5\right)}{1+x^{10}} \mathrm{~d} x$ equals

**Options:**

- **(A)** $\frac{\sin \left(\tan ^{-1} x^5\right)}{5}+c \quad, \quad$ where $c$ is the constant of integration
- **(B)** $x^4 \sin \left(\tan ^{-1} x^5\right)+\mathrm{c}, \quad$ where c is the constant of integration
- **(C)** $\frac{\sin \left(\tan ^{-1} x^5\right)}{4}+c \quad, \quad$ where $c$ is the constant of integration
- **(D)** $\cos \left(\tan ^{-1} x^5\right)+\mathrm{c}, \quad$ where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\sin \left(\tan ^{-1} x^5\right)}{5}+c \quad, \quad$ where $c$ is the constant of integration**

**Detailed Solution:**

Let $t = \tan^{-1}(x^5)$

Differentiating with respect to $x$, we get

$\dfrac{dt}{dx} = \dfrac{1}{1+(x^5)^2} \cdot \dfrac{d}{dx}(x^5)$

$\dfrac{dt}{dx} = \dfrac{5x^4}{1+x^{10}}$

$\dfrac{dt}{5} = \dfrac{x^4}{1+x^{10}} dx$

Substituting this in the given integral, we get

$\int \cos(t) \dfrac{dt}{5} = \dfrac{1}{5} \sin(t) + c$

Substituting $t = \tan^{-1}(x^5)$, we get

$\dfrac{\sin(\tan^{-1}(x^5))}{5} + c$

Answer: $\frac{\sin \left(\tan ^{-1} x^5\right)}{5}+c \quad, \quad$ where $c$ is the constant of integration

</details>

---

### Q76. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\mathrm{d} x}{x\left(x^3+1\right)}=$

**Options:**

- **(A)** $\log \left(\frac{x^3}{x^3+1}\right)+c \quad$, where $c$ is the constant of integration
- **(B)** $\frac{1}{3} \log \left(\sqrt[3]{x^3+1}\right)+c$, where $c$ is the constant of integration
- **(C)** $\log \left(\sqrt[3]{\frac{x^3}{x^3+1}}\right)+c, \quad$ where $c$ is the constant of integration
- **(D)** $\frac{1}{3} \log \left(\frac{x^3+1}{x^3}\right)+\mathrm{c} \quad, \quad$ where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log \left(\sqrt[3]{\frac{x^3}{x^3+1}}\right)+c, \quad$ where $c$ is the constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{1}{x(x^3+1)} \mathrm{d}x$

Multiplying the numerator and the denominator by $x^2$, we get:

$I = \int \dfrac{x^2}{x^3(x^3+1)} \mathrm{d}x$

Substitute $x^3 = t$, which gives $3x^2 \mathrm{d}x = \mathrm{d}t \Rightarrow x^2 \mathrm{d}x = \dfrac{\mathrm{d}t}{3}$.

$I = \dfrac{1}{3} \int \dfrac{1}{t(t+1)} \mathrm{d}t$

Using partial fractions:

$I = \dfrac{1}{3} \int \left( \dfrac{1}{t} - \dfrac{1}{t+1} \right) \mathrm{d}t$

$I = \dfrac{1}{3} \left( \log t - \log(t+1) \right) + c$

$I = \dfrac{1}{3} \log \left( \dfrac{t}{t+1} \right) + c$

Substituting back $t = x^3$:

$I = \dfrac{1}{3} \log \left( \dfrac{x^3}{x^3+1} \right) + c$

$I = \log \left( \dfrac{x^3}{x^3+1} \right)^{\dfrac{1}{3}} + c$

$I = \log \left( \sqrt[3]{\dfrac{x^3}{x^3+1}} \right) + c$

Answer: $\log \left(\sqrt[3]{\frac{x^3}{x^3+1}}\right)+c, \quad$ where $c$ is the constant of integration

</details>

---

### Q77. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\mathrm{d} x}{(x+a)^{\frac{9}{7}}(x-b)^{5 / 7}}=$

**Options:**

- **(A)** $\frac{7}{a+\mathrm{b}}\left(\frac{x-\mathrm{b}}{x+a}\right)^{\frac{9}{7}}+\mathrm{c}, \quad$ where c is the constant of integration.
- **(B)** $\frac{7}{a+\mathrm{b}}\left(\frac{x-\mathrm{b}}{x+a}\right)^{\frac{5}{7}}+\mathrm{c}, \quad$ where c is the constant of integration.
- **(C)** $\frac{7}{2(a+b)}\left(\frac{x-b}{x+a}\right)^{\frac{2}{7}}+c, \quad$ where c is the constant of integration.
- **(D)** $\frac{7}{a+\mathrm{b}}\left(\frac{x-\mathrm{b}}{x+a}\right)^{\frac{1}{7}}+\mathrm{c}, \quad$ where c is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{7}{2(a+b)}\left(\frac{x-b}{x+a}\right)^{\frac{2}{7}}+c, \quad$ where c is the constant of integration.**

**Detailed Solution:**

Let $I = \int \dfrac{\mathrm{d} x}{(x+a)^{\dfrac{9}{7}}(x-b)^{\dfrac{5}{7}}}$

Multiplying and dividing the denominator by $(x+a)^{\dfrac{5}{7}}$, we get:

$I = \int \dfrac{\mathrm{d} x}{(x+a)^{\dfrac{14}{7}} \left(\dfrac{x-b}{x+a}\right)^{\dfrac{5}{7}}}$

$I = \int \dfrac{\mathrm{d} x}{(x+a)^2 \left(\dfrac{x-b}{x+a}\right)^{\dfrac{5}{7}}}$

Let $t = \dfrac{x-b}{x+a}$

Differentiating with respect to $x$:

$\dfrac{\mathrm{d} t}{\mathrm{d} x} = \dfrac{(x+a)(1) - (x-b)(1)}{(x+a)^2} = \dfrac{a+b}{(x+a)^2}$

$\Rightarrow \dfrac{\mathrm{d} x}{(x+a)^2} = \dfrac{\mathrm{d} t}{a+b}$

Substituting this into the integral:

$I = \int \dfrac{1}{t^{\dfrac{5}{7}}} \dfrac{\mathrm{d} t}{a+b}$

$I = \dfrac{1}{a+b} \int t^{-\dfrac{5}{7}} \mathrm{d} t$

$I = \dfrac{1}{a+b} \left( \dfrac{t^{-\dfrac{5}{7} + 1}}{-\dfrac{5}{7} + 1} \right) + c$

$I = \dfrac{1}{a+b} \left( \dfrac{t^{\dfrac{2}{7}}}{\dfrac{2}{7}} \right) + c$

$I = \dfrac{7}{2(a+b)} \left(\dfrac{x-b}{x+a}\right)^{\dfrac{2}{7}} + c$

Answer: $\frac{7}{2(a+b)}\left(\frac{x-b}{x+a}\right)^{\frac{2}{7}}+c, \quad$ where c is the constant of integration.

</details>

---

### Q78. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\mathrm{d} x}{3 \cos 2 x+5}$ equals

**Options:**

- **(A)** $\frac{1}{2} \tan ^{-1}(\tan x)+c \quad, \quad$ where $c$ is the constant of integration.
- **(B)** $\frac{1}{2} \tan ^{-1}\left(\frac{\tan x}{2}\right)+c, \quad$ where $c$ is the constant of integration.
- **(C)** $\frac{1}{4} \tan ^{-1}\left(\frac{1}{2} \tan x\right)+c$, where $c$ is the constant of integration.
- **(D)** $\frac{1}{4} \tan ^{-1}(\tan x)+\mathrm{c}, \quad$ where c is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{4} \tan ^{-1}\left(\frac{1}{2} \tan x\right)+c$, where $c$ is the constant of integration.**

**Detailed Solution:**

Let $I = \int \dfrac{\mathrm{d} x}{3 \cos 2 x+5}$

Using the formula $\cos 2x = \dfrac{1 - \tan^2 x}{1 + \tan^2 x}$, we get:

$I = \int \dfrac{\mathrm{d} x}{3 \left( \dfrac{1 - \tan^2 x}{1 + \tan^2 x} \right) + 5}$

$I = \int \dfrac{(1 + \tan^2 x) \mathrm{d} x}{3(1 - \tan^2 x) + 5(1 + \tan^2 x)}$

$I = \int \dfrac{\sec^2 x \mathrm{d} x}{3 - 3\tan^2 x + 5 + 5\tan^2 x}$

$I = \int \dfrac{\sec^2 x \mathrm{d} x}{8 + 2\tan^2 x}$

Let $\tan x = t$, then $\sec^2 x \mathrm{d} x = \mathrm{d} t$

$I = \int \dfrac{\mathrm{d} t}{8 + 2t^2}$

$I = \dfrac{1}{2} \int \dfrac{\mathrm{d} t}{4 + t^2}$

$I = \dfrac{1}{2} \int \dfrac{\mathrm{d} t}{2^2 + t^2}$

Using the standard integral $\int \dfrac{\mathrm{d} x}{a^2 + x^2} = \dfrac{1}{a} \tan^{-1} \left( \dfrac{x}{a} \right) + c$, we get:

$I = \dfrac{1}{2} \left( \dfrac{1}{2} \tan^{-1} \left( \dfrac{t}{2} \right) \right) + c$

$I = \dfrac{1}{4} \tan^{-1} \left( \dfrac{1}{2} \tan x \right) + c$

Answer: $\frac{1}{4} \tan ^{-1}\left(\frac{1}{2} \tan x\right)+c$, where $c$ is the constant of integration.

</details>

---

### Q79. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{1}{e^x+1} \mathrm{~d} x=$

**Options:**

- **(A)** $x+\log \left(e^x+1\right)+c$, where $c$ is the constant of integration.
- **(B)** $x-\log \left(e^x+1\right)+c$, where $c$ is the constant of integration.
- **(C)** $\log \left(\mathrm{e}^x-1\right)+x+\mathrm{c}$, where c is the constant of integration.
- **(D)** $\log \left(\mathrm{e}^x-1\right)-x+\mathrm{c}$, where c is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x-\log \left(e^x+1\right)+c$, where $c$ is the constant of integration.**

**Detailed Solution:**

$\int \dfrac{1}{e^x+1} dx$

Adding and subtracting $e^x$ in the numerator:

$= \int \dfrac{e^x + 1 - e^x}{e^x+1} dx$

$= \int \left(1 - \dfrac{e^x}{e^x+1}\right) dx$

$= \int 1 dx - \int \dfrac{e^x}{e^x+1} dx$

For the second integral, substituting $e^x + 1 = t \Rightarrow e^x dx = dt$

$= x - \int \dfrac{1}{t} dt$

$= x - \log|t| + c$

$= x - \log(e^x+1) + c$

Answer: $x-\log \left(e^x+1\right)+c$, where $c$ is the constant of integration.

</details>

---

### Q80. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \sqrt{x^2+3 x} \mathrm{~d} x=$

**Options:**

- **(A)** $\sqrt{x^2+3 x}+\log \sqrt{x^2+3 x}+c$
where $c$ is the constant of integration.
- **(B)** $\frac{2 x+3}{4} \sqrt{x^2+3 x}-\frac{9}{8} \log \left(x+\frac{3}{2}+\sqrt{x^2+3 x}\right)+c$
where $c$ is the constant of integration.
- **(C)** $x \sqrt{x^2+3 x}+\log \left(x+\sqrt{x^2+3 x}\right)+c$
where $c$ is the constant of integration.
- **(D)** $x+3 \sqrt{x^2+3 x}+\frac{3}{2} \log \left(x+\sqrt{x^2+3 x}\right)+\mathrm{c}$
where $c$ is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2 x+3}{4} \sqrt{x^2+3 x}-\frac{9}{8} \log \left(x+\frac{3}{2}+\sqrt{x^2+3 x}\right)+c$
where $c$ is the constant of integration.**

**Detailed Solution:**

Let $I = \int \sqrt{x^2+3 x} \mathrm{~d} x$

Completing the square for the term inside the square root:

$I = \int \sqrt{x^2+3 x+\dfrac{9}{4}-\dfrac{9}{4}} \mathrm{~d} x$

$I = \int \sqrt{\left(x+\dfrac{3}{2}\right)^2-\left(\dfrac{3}{2}\right)^2} \mathrm{~d} x$

Using the standard integral formula $\int \sqrt{X^2-a^2} \mathrm{~d} X = \dfrac{X}{2} \sqrt{X^2-a^2}-\dfrac{a^2}{2} \log \left(X+\sqrt{X^2-a^2}\right)+c$

Substitute $X = x+\dfrac{3}{2}$ and $a = \dfrac{3}{2}$:

$I = \dfrac{x+\dfrac{3}{2}}{2} \sqrt{\left(x+\dfrac{3}{2}\right)^2-\left(\dfrac{3}{2}\right)^2}-\dfrac{\left(\dfrac{3}{2}\right)^2}{2} \log \left(x+\dfrac{3}{2}+\sqrt{\left(x+\dfrac{3}{2}\right)^2-\left(\dfrac{3}{2}\right)^2}\right)+c$

$I = \dfrac{2 x+3}{4} \sqrt{x^2+3 x}-\dfrac{9}{8} \log \left(x+\dfrac{3}{2}+\sqrt{x^2+3 x}\right)+c$

Answer: $\frac{2 x+3}{4} \sqrt{x^2+3 x}-\frac{9}{8} \log \left(x+\frac{3}{2}+\sqrt{x^2+3 x}\right)+c$
where $c$ is the constant of integration.

</details>

---

### Q81. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{x}{1+x^4} \mathrm{~d} x=$

**Options:**

- **(A)** $\frac{1}{2} \tan ^{-1} x^2+c$, where $c$ is the constant of integration
- **(B)** $2 \tan ^{-1} x+c$, where $c$ is the constant of integration
- **(C)** $\frac{1}{2} \tan ^{-1} x+c, \quad$ where $c$ is the constant of integration
- **(D)** $\tan ^{-1} x^2+c, \quad$ where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2} \tan ^{-1} x^2+c$, where $c$ is the constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{x}{1+x^4} dx$

Substitute $x^2 = t$

Differentiating both sides, we get $2x dx = dt \Rightarrow x dx = \dfrac{dt}{2}$

$I = \dfrac{1}{2} \int \dfrac{dt}{1+t^2}$

$I = \dfrac{1}{2} \tan^{-1} t + c$

Substituting $t = x^2$, we get:

$I = \dfrac{1}{2} \tan^{-1} x^2 + c$

Answer: $\frac{1}{2} \tan ^{-1} x^2+c$, where $c$ is the constant of integration

</details>

---

### Q82. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{(5 \sin \theta-2) \cos \theta}{\left(5-\cos ^2 \theta-4 \sin \theta\right)} d \theta=$

**Options:**

- **(A)** $\log (5 \sin \theta-2)+c$, where $c$ is the constant of integration
- **(B)** $5 \log (\sin \theta-2)-\frac{8}{(\sin \theta-2)}+c$, where $c$ is the constant of integration
- **(C)** $\log (5 \sin \theta-2)+\frac{8}{(\sin \theta-2)}+c, \quad$ where $c$ is the constant of integration
- **(D)** $\log (5 \sin \theta-2)+\frac{1}{(\sin \theta-2)}+c, \quad$ where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $5 \log (\sin \theta-2)-\frac{8}{(\sin \theta-2)}+c$, where $c$ is the constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{(5 \sin \theta - 2) \cos \theta}{5 - \cos^2 \theta - 4 \sin \theta} d\theta$

Substitute $\sin \theta = t$, which gives $\cos \theta d\theta = dt$.

The denominator can be rewritten as:
$5 - (1 - \sin^2 \theta) - 4 \sin \theta = \sin^2 \theta - 4 \sin \theta + 4 = (\sin \theta - 2)^2$

In terms of $t$, the denominator is $(t - 2)^2$.

The integral becomes:
$I = \int \dfrac{5t - 2}{(t - 2)^2} dt$

Expressing the numerator in terms of $(t - 2)$:
$5t - 2 = 5(t - 2) + 10 - 2 = 5(t - 2) + 8$

Substituting this back into the integral:
$I = \int \dfrac{5(t - 2) + 8}{(t - 2)^2} dt$

$I = \int \left( \dfrac{5}{t - 2} + \dfrac{8}{(t - 2)^2} \right) dt$

Integrating with respect to $t$:
$I = 5 \log (t - 2) - \dfrac{8}{t - 2} + c$

Substituting $t = \sin \theta$ back into the equation:
$I = 5 \log (\sin \theta - 2) - \dfrac{8}{\sin \theta - 2} + c$

Answer: $5 \log (\sin \theta-2)-\frac{8}{(\sin \theta-2)}+c$, where $c$ is the constant of integration

</details>

---

### Q83. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int\left(\frac{x-3}{x^2+9}\right)^2 \mathrm{~d} x=$

**Options:**

- **(A)** $\frac{1}{3} \tan ^{-1}\left(\frac{x}{3}\right)-\frac{3}{x^2+9}+c$, where $c$ is the constant of integration.
- **(B)** $\frac{1}{3} \tan ^{-1}\left(\frac{x}{3}\right)-\frac{1}{x^2+9}+c$, where $c$ is the constant of integration.
- **(C)** $\frac{1}{3} \tan ^{-1}\left(\frac{x}{3}\right)+\frac{3}{x^2+9}+c$, where $c$ is the constant of integration.
- **(D)** $\frac{1}{3} \tan ^{-1}\left(\frac{x}{3}\right)-\frac{1}{x^2+9}+c$, where $c$ is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{3} \tan ^{-1}\left(\frac{x}{3}\right)+\frac{3}{x^2+9}+c$, where $c$ is the constant of integration.**

**Detailed Solution:**

Let $I = \int\left(\dfrac{x-3}{x^2+9}\right)^2 \mathrm{d} x$

Expanding the numerator, we get:

$I = \int \dfrac{x^2 - 6x + 9}{(x^2+9)^2} \mathrm{d} x$

Grouping terms in the numerator to match the denominator:

$I = \int \dfrac{(x^2+9) - 6x}{(x^2+9)^2} \mathrm{d} x$

Separating the integral into two parts:

$I = \int \dfrac{x^2+9}{(x^2+9)^2} \mathrm{d} x - \int \dfrac{6x}{(x^2+9)^2} \mathrm{d} x$

$I = \int \dfrac{1}{x^2+9} \mathrm{d} x - 3 \int \dfrac{2x}{(x^2+9)^2} \mathrm{d} x$

For the first integral, using the standard formula $\int \dfrac{1}{x^2+a^2} \mathrm{d} x = \dfrac{1}{a} \tan^{-1}\left(\dfrac{x}{a}\right)$:

$\int \dfrac{1}{x^2+3^2} \mathrm{d} x = \dfrac{1}{3} \tan^{-1}\left(\dfrac{x}{3}\right)$

For the second integral, substituting $t = x^2+9 \Rightarrow \mathrm{d}t = 2x \mathrm{d}x$:

$\int \dfrac{2x}{(x^2+9)^2} \mathrm{d} x = \int \dfrac{1}{t^2} \mathrm{d} t = -\dfrac{1}{t} = -\dfrac{1}{x^2+9}$

Substituting these back into the expression for $I$:

$I = \dfrac{1}{3} \tan^{-1}\left(\dfrac{x}{3}\right) - 3 \left( -\dfrac{1}{x^2+9} \right) + c$

$I = \dfrac{1}{3} \tan^{-1}\left(\dfrac{x}{3}\right) + \dfrac{3}{x^2+9} + c$

Answer: $\frac{1}{3} \tan ^{-1}\left(\frac{x}{3}\right)+\frac{3}{x^2+9}+c$, where $c$ is the constant of integration.

</details>

---

### Q84. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\mathrm{d} x}{\mathrm{e}^x-1}=$

**Options:**

- **(A)** $\log \left(e^x-1\right)+x+c, \quad$ where $c$ is the constant of integration.
- **(B)** $\log \left(e^x-1\right)-x+c, \quad$ where $c$ is the constant of integration.
- **(C)** $x-\log \left(\mathrm{e}^{\mathrm{x}}-1\right)+\mathrm{c}, \quad$ where c is the constant of integration.
- **(D)** $\log \left(e^x-1\right)-x e^x+c$, where $c$ is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log \left(e^x-1\right)-x+c, \quad$ where $c$ is the constant of integration.**

**Detailed Solution:**

Let $I = \int \dfrac{1}{e^x - 1} dx$

Substitute $e^x = t \Rightarrow e^x dx = dt \Rightarrow dx = \dfrac{dt}{t}$

$I = \int \dfrac{1}{t(t - 1)} dt$

Using partial fractions:

$I = \int \left( \dfrac{1}{t - 1} - \dfrac{1}{t} \right) dt$

$I = \log(t - 1) - \log(t) + c$

Substituting $t = e^x$:

$I = \log(e^x - 1) - \log(e^x) + c$

$I = \log(e^x - 1) - x + c$

Answer: $\log \left(e^x-1\right)-x+c, \quad$ where $c$ is the constant of integration.

</details>

---

### Q85. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\mathrm{d} x}{\sqrt{x}+x}=$

**Options:**

- **(A)** $\log \sqrt{x}+c, \quad$ where $c$ is the constant of integration.
- **(B)** $\log (\sqrt{x}+x)+c, \quad$ where $c$ is the constant of integration.
- **(C)** $\log (1+\sqrt{x})+c, \quad$ where $c$ is the constant of integration.
- **(D)** $2 \log (1+\sqrt{x})+c, \quad$ where $c$ is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 \log (1+\sqrt{x})+c, \quad$ where $c$ is the constant of integration.**

**Detailed Solution:**

Let $I = \int \dfrac{\mathrm{d} x}{\sqrt{x}+x}$

$I = \int \dfrac{\mathrm{d} x}{\sqrt{x}(1+\sqrt{x})}$

Let $1+\sqrt{x} = t$

Differentiating both sides with respect to $x$, we get $\dfrac{1}{2\sqrt{x}} \mathrm{d} x = \mathrm{d} t$

$\dfrac{\mathrm{d} x}{\sqrt{x}} = 2 \mathrm{d} t$

Substituting these values in the integral, we get:

$I = \int \dfrac{2 \mathrm{d} t}{t}$

$I = 2 \log |t| + c$

Substituting $t = 1+\sqrt{x}$, we get:

$I = 2 \log (1+\sqrt{x}) + c$

Answer: $2 \log (1+\sqrt{x})+c, \quad$ where $c$ is the constant of integration.

</details>

---

### Q86. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \sec ^{\frac{2}{3}} x \cdot \operatorname{cosec}^{\frac{4}{3}} x \mathrm{~d} x=$

**Options:**

- **(A)** $3 \tan ^{\frac{-1}{3}} x+c$, where $c$ is the constant of integration
- **(B)** $-3 \tan ^{\frac{-1}{3}} x+c$, where $c$ is the constant of integration
- **(C)** $-3 \cot ^{\frac{-1}{3}} x+c$, where $c$ is the constant of integration
- **(D)** $-\frac{3}{4} \tan ^{\frac{-4}{3}} x+c$, where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-3 \tan ^{\frac{-1}{3}} x+c$, where $c$ is the constant of integration**

**Detailed Solution:**

$I = \int \sec^{\dfrac{2}{3}} x \cdot \operatorname{cosec}^{\dfrac{4}{3}} x \, \mathrm{d} x$

$I = \int \dfrac{1}{\cos^{\dfrac{2}{3}} x \sin^{\dfrac{4}{3}} x} \, \mathrm{d} x$

Dividing the numerator and the denominator by $\cos^2 x$:

$I = \int \dfrac{\sec^2 x}{\dfrac{\cos^{\dfrac{2}{3}} x \sin^{\dfrac{4}{3}} x}{\cos^2 x}} \, \mathrm{d} x$

$I = \int \dfrac{\sec^2 x}{\tan^{\dfrac{4}{3}} x} \, \mathrm{d} x$

Substituting $\tan x = t$, we get $\sec^2 x \, \mathrm{d} x = \mathrm{d} t$:

$I = \int t^{-\dfrac{4}{3}} \, \mathrm{d} t$

$I = \dfrac{t^{-\dfrac{1}{3}}}{-\dfrac{1}{3}} + c$

$I = -3 \tan^{-\dfrac{1}{3}} x + c$

Answer: $-3 \tan ^{\frac{-1}{3}} x+c$, where $c$ is the constant of integration

</details>

---

### Q87. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{x^3}{x^4+5 x^2+4} \mathrm{~d} x=$

**Options:**

- **(A)** $\frac{1}{3} \log \left(\frac{\left(x^2+4\right)^2}{\sqrt{x^2+1}}\right)+c$, where $c$ is the constant of integration
- **(B)** $\log \left(\frac{\left(x^2+4\right)^2}{\sqrt{x^2+1}}\right)+c, \quad$ where $c$ is the constant of integration
- **(C)** 3log $\left(\frac{\left(x^2+4\right)^2}{\sqrt{x^2+1}}\right)+c, \quad$ where $c$ is the constant of integration
- **(D)** $\frac{2}{3} \log \left(\frac{\left(x^2+4\right)^2}{\sqrt{x^2+1}}\right)+c$, where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{3} \log \left(\frac{\left(x^2+4\right)^2}{\sqrt{x^2+1}}\right)+c$, where $c$ is the constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{x^3}{x^4+5x^2+4} \, dx$

Substitute $x^2 = t$, which gives $2x \, dx = dt \Rightarrow x \, dx = \dfrac{dt}{2}$.

The integral becomes:

$I = \dfrac{1}{2} \int \dfrac{t}{t^2+5t+4} \, dt$

Factorizing the denominator, we get $t^2+5t+4 = (t+1)(t+4)$.

Using partial fractions:

$\dfrac{t}{(t+1)(t+4)} = \dfrac{A}{t+1} + \dfrac{B}{t+4}$

$t = A(t+4) + B(t+1)$

Putting $t = -1$, we get $-1 = 3A \Rightarrow A = -\dfrac{1}{3}$.

Putting $t = -4$, we get $-4 = -3B \Rightarrow B = \dfrac{4}{3}$.

Substituting these values back into the integral:

$I = \dfrac{1}{2} \int \left( \dfrac{-1/3}{t+1} + \dfrac{4/3}{t+4} \right) \, dt$

$I = \dfrac{1}{2} \left( -\dfrac{1}{3} \log|t+1| + \dfrac{4}{3} \log|t+4| \right) + c$

$I = -\dfrac{1}{6} \log|t+1| + \dfrac{2}{3} \log|t+4| + c$

Substituting $t = x^2$ back:

$I = -\dfrac{1}{6} \log(x^2+1) + \dfrac{2}{3} \log(x^2+4) + c$

Taking $\dfrac{1}{3}$ common:

$I = \dfrac{1}{3} \left( 2 \log(x^2+4) - \dfrac{1}{2} \log(x^2+1) \right) + c$

Using the properties of logarithms, $a \log b = \log(b^a)$ and $\log a - \log b = \log\left(\dfrac{a}{b}\right)$:

$I = \dfrac{1}{3} \left( \log\left((x^2+4)^2\right) - \log\left(\sqrt{x^2+1}\right) \right) + c$

$I = \dfrac{1}{3} \log \left( \dfrac{(x^2+4)^2}{\sqrt{x^2+1}} \right) + c$

Answer: $\frac{1}{3} \log \left(\frac{\left(x^2+4\right)^2}{\sqrt{x^2+1}}\right)+c$, where $c$ is the constant of integration

</details>

---

### Q88. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\sin 2 x \cos 2 x}{\sqrt{4-\cos ^4 2 x}} \mathrm{~d} x=$

**Options:**

- **(A)** $\frac{1}{4} \sin ^{-1}\left(\frac{\cos ^2 2 x}{2}\right)+c \quad$, where $c$ is the constant of integration.
- **(B)** $\frac{-1}{4} \sin ^{-1}\left(\frac{\cos ^2 2 x}{2}\right)+c$, where $c$ is the constant of integration.
- **(C)** $\frac{1}{2} \sin ^{-1}\left(\frac{\cos ^2 2 x}{2}\right)+c \quad$, where $c$ is the constant of integration.
- **(D)** $\frac{-1}{2} \sin ^{-1}\left(\frac{\cos ^2 2 x}{2}\right)+c \quad$, where $c$ is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-1}{4} \sin ^{-1}\left(\frac{\cos ^2 2 x}{2}\right)+c$, where $c$ is the constant of integration.**

**Detailed Solution:**

Let $I = \int \dfrac{\sin 2x \cos 2x}{\sqrt{4 - \cos^4 2x}} \, dx$

Put $\cos^2 2x = t$

Differentiating with respect to $x$, we get:

$2 \cos 2x (-\sin 2x) \times 2 \, dx = dt$

$-4 \sin 2x \cos 2x \, dx = dt$

$\sin 2x \cos 2x \, dx = -\dfrac{1}{4} dt$

Substituting this into the integral, we get:

$I = \int \dfrac{-\dfrac{1}{4} dt}{\sqrt{4 - t^2}}$

$I = -\dfrac{1}{4} \int \dfrac{1}{\sqrt{2^2 - t^2}} \, dt$

Using the standard integral formula $\int \dfrac{1}{\sqrt{a^2 - x^2}} \, dx = \sin^{-1}\left(\dfrac{x}{a}\right) + c$, we get:

$I = -\dfrac{1}{4} \sin^{-1}\left(\dfrac{t}{2}\right) + c$

Substituting back $t = \cos^2 2x$, we obtain:

$I = -\dfrac{1}{4} \sin^{-1}\left(\dfrac{\cos^2 2x}{2}\right) + c$

Answer: $\frac{-1}{4} \sin ^{-1}\left(\frac{\cos ^2 2 x}{2}\right)+c$, where $c$ is the constant of integration.

</details>

---

### Q89. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{x^3}{(x+1)^2} \mathrm{~d} x=$

**Options:**

- **(A)** $\frac{x^2}{2}-2 x+3 \log (x+1)+\frac{1}{x+1}+c$,
where $c$ is the constant of integration
- **(B)** $\frac{x^2}{2}+2 x-3 \log (x+1)+\frac{1}{x+1}+c$
where c is the constant of integration
- **(C)** $\frac{x^2}{2}-2 x+3 \log (x+1)-\frac{1}{x+1}+\mathrm{c}$,
where $c$ is the constant of integration
- **(D)** $\frac{x^2}{2}-2 x-3 \log (x+1)-\frac{1}{x+1}+\mathrm{c}$,
where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{x^2}{2}-2 x+3 \log (x+1)+\frac{1}{x+1}+c$,
where $c$ is the constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{x^3}{(x+1)^2} \mathrm{d} x$.

Substitute $x + 1 = t$, which gives $x = t - 1$ and $\mathrm{d}x = \mathrm{d}t$.

The integral becomes:

$I = \int \dfrac{(t-1)^3}{t^2} \mathrm{d}t$

Expanding the numerator using $(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$:

$I = \int \dfrac{t^3 - 3t^2 + 3t - 1}{t^2} \mathrm{d}t$

Separating the terms:

$I = \int \left( t - 3 + \dfrac{3}{t} - \dfrac{1}{t^2} \right) \mathrm{d}t$

Integrating term by term:

$I = \dfrac{t^2}{2} - 3t + 3 \log(t) + \dfrac{1}{t} + C_1$

Substituting back $t = x + 1$:

$I = \dfrac{(x+1)^2}{2} - 3(x+1) + 3 \log(x+1) + \dfrac{1}{x+1} + C_1$

Expanding the terms:

$I = \dfrac{x^2 + 2x + 1}{2} - 3x - 3 + 3 \log(x+1) + \dfrac{1}{x+1} + C_1$

$I = \dfrac{x^2}{2} + x + \dfrac{1}{2} - 3x - 3 + 3 \log(x+1) + \dfrac{1}{x+1} + C_1$

$I = \dfrac{x^2}{2} - 2x + 3 \log(x+1) + \dfrac{1}{x+1} + \left(C_1 - \dfrac{5}{2}\right)$

Let $c = C_1 - \dfrac{5}{2}$ be the new constant of integration:

$I = \dfrac{x^2}{2} - 2x + 3 \log(x+1) + \dfrac{1}{x+1} + c$

Answer: $\frac{x^2}{2}-2 x+3 \log (x+1)+\frac{1}{x+1}+c$,
where $c$ is the constant of integration

</details>

---

### Q90. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \cos \left(\frac{x}{16}\right) \cdot \cos \left(\frac{x}{8}\right) \cdot \cos \left(\frac{x}{4}\right) \cdot \sin \left(\frac{x}{16}\right) \mathrm{dx}=$

**Options:**

- **(A)** $\frac{\cos 16 x}{256}+c \quad$, where $c$ is the constant of integration
- **(B)** $\frac{-\cos 16 x}{256}+c$, where $c$ is the constant of integration
- **(C)** $\frac{\sin 16 x}{256}+c, \quad$ where $c$ is the constant of integration
- **(D)** $\frac{-\cos \left(\frac{x}{2}\right)}{4}+c$, where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{-\cos \left(\frac{x}{2}\right)}{4}+c$, where $c$ is the constant of integration**

**Detailed Solution:**

Let $I = \int \sin \left(\dfrac{x}{16}\right) \cos \left(\dfrac{x}{16}\right) \cos \left(\dfrac{x}{8}\right) \cos \left(\dfrac{x}{4}\right) \mathrm{dx}$

Multiplying and dividing by $2$:

$I = \dfrac{1}{2} \int 2 \sin \left(\dfrac{x}{16}\right) \cos \left(\dfrac{x}{16}\right) \cos \left(\dfrac{x}{8}\right) \cos \left(\dfrac{x}{4}\right) \mathrm{dx}$

Using $\sin(2\theta) = 2 \sin\theta \cos\theta$:

$I = \dfrac{1}{2} \int \sin \left(\dfrac{x}{8}\right) \cos \left(\dfrac{x}{8}\right) \cos \left(\dfrac{x}{4}\right) \mathrm{dx}$

Multiplying and dividing by $2$ again:

$I = \dfrac{1}{4} \int 2 \sin \left(\dfrac{x}{8}\right) \cos \left(\dfrac{x}{8}\right) \cos \left(\dfrac{x}{4}\right) \mathrm{dx}$

$I = \dfrac{1}{4} \int \sin \left(\dfrac{x}{4}\right) \cos \left(\dfrac{x}{4}\right) \mathrm{dx}$

Multiplying and dividing by $2$ once more:

$I = \dfrac{1}{8} \int 2 \sin \left(\dfrac{x}{4}\right) \cos \left(\dfrac{x}{4}\right) \mathrm{dx}$

$I = \dfrac{1}{8} \int \sin \left(\dfrac{x}{2}\right) \mathrm{dx}$

Integrating with respect to $x$:

$I = \dfrac{1}{8} \left( \dfrac{-\cos \left(\dfrac{x}{2}\right)}{\dfrac{1}{2}} \right) + c$

$I = \dfrac{-\cos \left(\dfrac{x}{2}\right)}{4} + c$

Answer: $\frac{-\cos \left(\frac{x}{2}\right)}{4}+c$, where $c$ is the constant of integration

</details>

---

### Q91. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\sin x}{\sqrt{5 \sin ^2 x+6 \cos ^2 x}} \mathrm{~d} x=$

**Options:**

- **(A)** $\log \left(\cos x+\sqrt{\cos ^2 x+5}\right)+c \quad, \quad$ where $c$ is the constant of integration
- **(B)** $\log \left(\sin x+\sqrt{6 \cos ^2 x+5}\right)+c, \quad$ where $c$ is the constant of integration
- **(C)** $-\log \left(\cos x+\sqrt{\cos ^2 x+6}\right)+c, \quad$ where $c$ is the constant of integration
- **(D)** $-\log \left(\cos x+\sqrt{\cos ^2 x+5}\right)+c$, where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\log \left(\cos x+\sqrt{\cos ^2 x+5}\right)+c$, where $c$ is the constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{\sin x}{\sqrt{5 \sin^2 x + 6 \cos^2 x}} \, dx$

Using the identity $\sin^2 x = 1 - \cos^2 x$, the expression inside the square root becomes:

$5(1 - \cos^2 x) + 6 \cos^2 x = 5 - 5 \cos^2 x + 6 \cos^2 x = \cos^2 x + 5$

Substituting this into the integral gives:

$I = \int \dfrac{\sin x}{\sqrt{\cos^2 x + 5}} \, dx$

Substituting $\cos x = t$, we get $-\sin x \, dx = dt$, which implies $\sin x \, dx = -dt$.

The integral becomes:

$I = \int \dfrac{-dt}{\sqrt{t^2 + 5}} = -\int \dfrac{dt}{\sqrt{t^2 + (\sqrt{5})^2}}$

Using the standard formula $\int \dfrac{dx}{\sqrt{x^2 + a^2}} = \log(x + \sqrt{x^2 + a^2}) + c$:

$I = -\log(t + \sqrt{t^2 + 5}) + c$

Substituting $t = \cos x$ back into the expression yields:

$I = -\log(\cos x + \sqrt{\cos^2 x + 5}) + c$

Answer: $-\log \left(\cos x+\sqrt{\cos ^2 x+5}\right)+c$, where $c$ is the constant of integration

</details>

---

### Q92. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \sqrt{x^2-6 x-16} \mathrm{~d} x$ equals.

**Options:**

- **(A)** $\left(\frac{x-3}{2}\right) \sqrt{x^2-6 x-16}+\frac{5}{2} \log \left(x-3+\sqrt{x^2-6 x-16}\right)+\mathrm{c}$ where $c$ is the constant of integration
- **(B)** $\left(\frac{x-3}{2}\right) \sqrt{x^2-6 x-16}-\frac{25}{2} \log \left(x-3+\sqrt{x^2-6 x-16}\right)+c$ where $c$ is the constant of integration
- **(C)** $\left(\frac{x-3}{2}\right) \sqrt{x^2-6 x-16}+\frac{25}{2} \log \left(x-3+\sqrt{x^2-6 x-16}\right)+\mathrm{c}$ where $c$ is the constant of integration
- **(D)** $\left(\frac{x-3}{2}\right) \sqrt{x^2-6 x-16}-\frac{5}{2} \log \left(x-3+\sqrt{x^2-6 x-16}\right)+c$, where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\frac{x-3}{2}\right) \sqrt{x^2-6 x-16}-\frac{25}{2} \log \left(x-3+\sqrt{x^2-6 x-16}\right)+c$ where $c$ is the constant of integration**

**Detailed Solution:**

Let $I = \int \sqrt{x^2 - 6x - 16} \, dx$.

Completing the square for the quadratic expression:

$x^2 - 6x - 16 = x^2 - 6x + 9 - 25 = (x - 3)^2 - 5^2$

Substituting this into the integral:

$I = \int \sqrt{(x - 3)^2 - 5^2} \, dx$

Using the standard integration formula:

$\int \sqrt{X^2 - a^2} \, dX = \dfrac{X}{2} \sqrt{X^2 - a^2} - \dfrac{a^2}{2} \log \left( X + \sqrt{X^2 - a^2} \right) + c$

Here, $X = x - 3$ and $a = 5$.

$I = \dfrac{x - 3}{2} \sqrt{(x - 3)^2 - 5^2} - \dfrac{25}{2} \log \left( (x - 3) + \sqrt{(x - 3)^2 - 5^2} \right) + c$

$I = \left(\dfrac{x - 3}{2}\right) \sqrt{x^2 - 6x - 16} - \dfrac{25}{2} \log \left( x - 3 + \sqrt{x^2 - 6x - 16} \right) + c$

Answer: $\left(\frac{x-3}{2}\right) \sqrt{x^2-6 x-16}-\frac{25}{2} \log \left(x-3+\sqrt{x^2-6 x-16}\right)+c$ where $c$ is the constant of integration

</details>

---

### Q93. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{\mathrm{d} x}{x\left(x^2+1\right)}=$

**Options:**

- **(A)** $\log (x)-\frac{1}{2} \log \left(x^2+1\right)+c$, where $c$ is the constant of integration.
- **(B)** $\frac{1}{2} \log (x)-\log \left(x^2+1\right)+c$, where $c$ is the constant of integration.
- **(C)** $\log (x)+\frac{1}{2} \log \left(x^2+1\right)+c$, where $c$ is the constant of integration.
- **(D)** $-\log (x)-\frac{1}{2} \log \left(x^2+1\right)+c$, where $c$ is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\log (x)-\frac{1}{2} \log \left(x^2+1\right)+c$, where $c$ is the constant of integration.**

**Detailed Solution:**

Let $I = \int \dfrac{\mathrm{d} x}{x(x^2+1)}$

Adding and subtracting $x^2$ in the numerator, we get:

$I = \int \dfrac{x^2+1-x^2}{x(x^2+1)} \mathrm{d} x$

Separating the terms:

$I = \int \left( \dfrac{x^2+1}{x(x^2+1)} - \dfrac{x^2}{x(x^2+1)} \right) \mathrm{d} x$

$I = \int \left( \dfrac{1}{x} - \dfrac{x}{x^2+1} \right) \mathrm{d} x$

$I = \int \dfrac{1}{x} \mathrm{d} x - \dfrac{1}{2} \int \dfrac{2x}{x^2+1} \mathrm{d} x$

Using the standard integral $\int \dfrac{f'(x)}{f(x)} \mathrm{d} x = \log(f(x)) + c$, we get:

$I = \log(x) - \dfrac{1}{2} \log(x^2+1) + c$

Answer: $\log (x)-\frac{1}{2} \log \left(x^2+1\right)+c$, where $c$ is the constant of integration.

</details>

---

### Q94. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^3 \frac{\mathrm{~d} x}{(x+2) \sqrt{x+1}}=$

**Options:**

- **(A)** $\tan ^{-1}\left(\frac{1}{3}\right)$
- **(B)** $2 \tan ^{-1}\left(\frac{1}{3}\right)$
- **(C)** $3 \tan ^{-1}\left(\frac{1}{3}\right)$
- **(D)** $4 \tan ^{-1}\left(\frac{1}{3}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \tan ^{-1}\left(\frac{1}{3}\right)$**

**Detailed Solution:**

Let $t = \sqrt{x+1} \Rightarrow x = t^2 - 1 \Rightarrow \mathrm{d}x = 2t \, \mathrm{d}t$

When $x = 0$, $t = 1$

When $x = 3$, $t = 2$

The integral becomes:

$I = \int_1^2 \dfrac{2t \, \mathrm{d}t}{(t^2 - 1 + 2)t}$

$I = 2 \int_1^2 \dfrac{\mathrm{d}t}{t^2 + 1}$

$I = 2 [\tan^{-1}(t)]_1^2$

$I = 2 (\tan^{-1}(2) - \tan^{-1}(1))$

Using the formula $\tan^{-1}(x) - \tan^{-1}(y) = \tan^{-1}\left(\dfrac{x-y}{1+xy}\right)$:

$I = 2 \tan^{-1}\left(\dfrac{2-1}{1+(2)(1)}\right)$

$I = 2 \tan^{-1}\left(\dfrac{1}{3}\right)$

Answer: $2 \tan ^{-1}\left(\frac{1}{3}\right)$

</details>

---

### Q95. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{e^{\tan ^{-1} 2 x}}{1+4 x^2}=$

**Options:**

- **(A)** $4 \mathrm{e}^{\tan ^{-1} 2 x}+\mathrm{c}, \quad$ where c is the constant of integration
- **(B)** $e^{\tan ^{-1} 2 x}+c, \quad$ where $c$ is the constant of integration
- **(C)** $\frac{e^{\tan ^{-1} 2 x}}{2}+c, \quad$ where $c$ is the constant of integration
- **(D)** $2 \mathrm{e}^{\tan ^{-1} 2 x}+\mathrm{c}, \quad$ where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{e^{\tan ^{-1} 2 x}}{2}+c, \quad$ where $c$ is the constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{e^{\tan^{-1} 2x}}{1+4x^2} dx$

Substitute $t = \tan^{-1} 2x$

Differentiating with respect to $x$, we get $dt = \dfrac{1}{1+(2x)^2} \times 2 dx = \dfrac{2}{1+4x^2} dx$

$\dfrac{dx}{1+4x^2} = \dfrac{dt}{2}$

Substituting in the integral, we get $I = \int e^t \dfrac{dt}{2}$

$I = \dfrac{1}{2} \int e^t dt = \dfrac{1}{2} e^t + c$

Substituting back $t = \tan^{-1} 2x$, we get $I = \dfrac{e^{\tan^{-1} 2x}}{2} + c$

Answer: $\frac{e^{\tan ^{-1} 2 x}}{2}+c, \quad$ where $c$ is the constant of integration

</details>

---

### Q96. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\mathrm{d} x}{2+\cos x} \mathrm{~d} x=$

**Options:**

- **(A)** $2 \tan ^{-1}\left(\frac{1}{\sqrt{3}} \tan \frac{x}{2}\right)+c$, where $c$ is the constant of integration
- **(B)** $\frac{2}{\sqrt{3}} \tan ^{-1}\left(\frac{1}{\sqrt{3}} \tan \frac{x}{2}\right)+c$, where $c$ is the constant of integration
- **(C)** $\frac{1}{\sqrt{3}} \tan ^{-1}\left(\frac{1}{\sqrt{3}} \tan \frac{x}{2}\right)+c$, where $c$ is the constant of integration
- **(D)** $\sqrt{3} \tan ^{-1}\left(\frac{1}{\sqrt{3}} \tan \frac{x}{2}\right)+c$, where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{\sqrt{3}} \tan ^{-1}\left(\frac{1}{\sqrt{3}} \tan \frac{x}{2}\right)+c$, where $c$ is the constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{\mathrm{d} x}{2+\cos x}$

Substitute $t = \tan \dfrac{x}{2}$, which gives $\mathrm{d} x = \dfrac{2 \mathrm{d} t}{1+t^2}$ and $\cos x = \dfrac{1-t^2}{1+t^2}$

$I = \int \dfrac{\dfrac{2 \mathrm{d} t}{1+t^2}}{2 + \dfrac{1-t^2}{1+t^2}}$

$I = \int \dfrac{2 \mathrm{d} t}{2(1+t^2) + 1 - t^2}$

$I = \int \dfrac{2 \mathrm{d} t}{t^2 + 3}$

$I = 2 \int \dfrac{\mathrm{d} t}{t^2 + (\sqrt{3})^2}$

Using the standard formula $\int \dfrac{\mathrm{d} t}{t^2 + a^2} = \dfrac{1}{a} \tan^{-1} \left( \dfrac{t}{a} \right) + c$

$I = \dfrac{2}{\sqrt{3}} \tan^{-1} \left( \dfrac{t}{\sqrt{3}} \right) + c$

$I = \dfrac{2}{\sqrt{3}} \tan^{-1} \left( \dfrac{1}{\sqrt{3}} \tan \dfrac{x}{2} \right) + c$

Answer: $\frac{2}{\sqrt{3}} \tan ^{-1}\left(\frac{1}{\sqrt{3}} \tan \frac{x}{2}\right)+c$, where $c$ is the constant of integration

</details>

---

### Q97. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \sin ^5 x \mathrm{~d} x=$

**Options:**

- **(A)** $\cos x+\frac{2}{3} \cos ^3 x-\frac{\cos ^5 x}{5}+c \quad$, where $c$ is the constant of integration
- **(B)** $\cos x+\frac{2}{3} \cos ^3 x+\frac{\cos ^5 x}{5}+c \quad, \quad$ where $c$ is the constant of integration
- **(C)** $-\left(\cos x-\frac{2}{3} \cos ^3 x+\frac{\cos ^5 x}{5}+c\right)$, where $c$ is the constant of integration
- **(D)** $\cos x-\frac{2}{3} \cos ^3 x+\frac{\cos ^5 x}{5}+c, \quad$ where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\left(\cos x-\frac{2}{3} \cos ^3 x+\frac{\cos ^5 x}{5}+c\right)$, where $c$ is the constant of integration**

**Detailed Solution:**

$I = \int \sin^5 x \, dx$

$I = \int (\sin^2 x)^2 \sin x \, dx$

$I = \int (1 - \cos^2 x)^2 \sin x \, dx$

Substituting $\cos x = t$, we get $-\sin x \, dx = dt \Rightarrow \sin x \, dx = -dt$

$I = -\int (1 - t^2)^2 \, dt$

$I = -\int (1 - 2t^2 + t^4) \, dt$

$I = -\left(t - \dfrac{2}{3}t^3 + \dfrac{t^5}{5}\right) + C$

$I = -\left(\cos x - \dfrac{2}{3}\cos^3 x + \dfrac{\cos^5 x}{5}\right) + C$

Since $C$ is an arbitrary constant of integration, we can write $C = -c$, which gives:

$I = -\left(\cos x - \dfrac{2}{3}\cos^3 x + \dfrac{\cos^5 x}{5} + c\right)$

Answer: $-\left(\cos x-\frac{2}{3} \cos ^3 x+\frac{\cos ^5 x}{5}+c\right)$, where $c$ is the constant of integration

</details>

---

### Q98. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\sin 2 x}{(a+b \cos x)^2} d x=$

**Options:**

- **(A)** $\frac{2}{a^2}\left[\log (a+\mathrm{b} \cos x)-\frac{a}{a+\mathrm{b} \cos x}\right]+\mathrm{c},$ 
where $c$ is the constant of integration.
- **(B)** $\frac{-1}{a^2}\left[\log (a+\mathrm{b} \cos x)+\frac{a}{a+\mathrm{b} \cos x}\right]+\mathrm{c},$
where c is the constant of integration.
- **(C)** $\frac{-2}{\mathrm{~b}^2}\left[\log (a+\mathrm{b} \cos x)+\frac{a}{a+\mathrm{b} \cos x}\right]+\mathrm{c}$
where $c$ is the constant of integration.
- **(D)** $\frac{-2}{\mathrm{~b}^2}\left[\log (a+\mathrm{b} \cos x)-\frac{a}{a+\mathrm{b} \cos x}\right]+\mathrm{c}$
where $c$ is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{-2}{\mathrm{~b}^2}\left[\log (a+\mathrm{b} \cos x)+\frac{a}{a+\mathrm{b} \cos x}\right]+\mathrm{c}$
where $c$ is the constant of integration.**

**Detailed Solution:**

Let $I = \int \dfrac{\sin 2x}{(a+b\cos x)^2} dx$

Using the identity $\sin 2x = 2\sin x \cos x$, we get:

$I = \int \dfrac{2\sin x \cos x}{(a+b\cos x)^2} dx$

Substitute $a+b\cos x = t$

Differentiating with respect to $x$, we get:

$-b\sin x dx = dt \Rightarrow \sin x dx = -\dfrac{dt}{b}$

Also, $\cos x = \dfrac{t-a}{b}$

Substituting these into the integral:

$I = \int \dfrac{2\left(\dfrac{t-a}{b}\right)}{t^2} \left(-\dfrac{dt}{b}\right)$

$I = \dfrac{-2}{b^2} \int \dfrac{t-a}{t^2} dt$

$I = \dfrac{-2}{b^2} \int \left(\dfrac{1}{t} - \dfrac{a}{t^2}\right) dt$

Integrating with respect to $t$:

$I = \dfrac{-2}{b^2} \left[ \log t - a\left(-\dfrac{1}{t}\right) \right] + c$

$I = \dfrac{-2}{b^2} \left[ \log t + \dfrac{a}{t} \right] + c$

Substituting back $t = a+b\cos x$:

$I = \dfrac{-2}{b^2} \left[ \log(a+b\cos x) + \dfrac{a}{a+b\cos x} \right] + c$

Answer: $\frac{-2}{\mathrm{~b}^2}\left[\log (a+\mathrm{b} \cos x)+\frac{a}{a+\mathrm{b} \cos x}\right]+\mathrm{c}$
where $c$ is the constant of integration.

</details>

---

### Q99. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\mathrm{d} x}{2 \mathrm{e}^{2 x}+3 \mathrm{e}^x+1}=$

**Options:**

- **(A)** $x+\log \left(\mathrm{e}^x+1\right)-2 \log \left(2 \mathrm{e}^x+1\right)+\mathrm{c},$
where $c$ is the constant of integration
- **(B)** $x-\log \left(\mathrm{e}^x+1\right)+4 \log \left(\mathrm{e}^x+1\right)+\mathrm{c}$
where $c$ is the constant of integration
- **(C)** $x+\log \left(\mathrm{e}^x+1\right)-4 \log \left(2 \mathrm{e}^x+1\right)+\mathrm{c},$
where $c$ is the constant of integration
- **(D)** $x-\log \left(\mathrm{e}^x+1\right)+2 \log \left(2 \mathrm{e}^x+1\right)+\mathrm{c},$
where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x+\log \left(\mathrm{e}^x+1\right)-2 \log \left(2 \mathrm{e}^x+1\right)+\mathrm{c},$
where $c$ is the constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{\mathrm{d} x}{2 \mathrm{e}^{2 x}+3 \mathrm{e}^x+1}$

Substitute $\mathrm{e}^x = t \Rightarrow \mathrm{e}^x \mathrm{d} x = \mathrm{d} t \Rightarrow \mathrm{d} x = \dfrac{\mathrm{d} t}{t}$

$I = \int \dfrac{\mathrm{d} t}{t(2t^2+3t+1)}$

Factorizing the quadratic expression in the denominator:

$I = \int \dfrac{\mathrm{d} t}{t(2t+1)(t+1)}$

Using partial fractions:

$\dfrac{1}{t(2t+1)(t+1)} = \dfrac{A}{t} + \dfrac{B}{2t+1} + \dfrac{C}{t+1}$

$1 = A(2t+1)(t+1) + Bt(t+1) + Ct(2t+1)$

Putting $t = 0 \Rightarrow A(1)(1) = 1 \Rightarrow A = 1$

Putting $t = -1 \Rightarrow C(-1)(-1) = 1 \Rightarrow C = 1$

Putting $t = -\dfrac{1}{2} \Rightarrow B\left(-\dfrac{1}{2}\right)\left(\dfrac{1}{2}\right) = 1 \Rightarrow B = -4$

Substituting the values of $A$, $B$, and $C$ back into the integral:

$I = \int \left( \dfrac{1}{t} - \dfrac{4}{2t+1} + \dfrac{1}{t+1} \right) \mathrm{d} t$

$I = \log|t| - \dfrac{4}{2}\log|2t+1| + \log|t+1| + \mathrm{c}$

$I = \log|t| - 2\log|2t+1| + \log|t+1| + \mathrm{c}$

Substitute $t = \mathrm{e}^x$:

$I = \log(\mathrm{e}^x) - 2\log(2\mathrm{e}^x+1) + \log(\mathrm{e}^x+1) + \mathrm{c}$

$I = x + \log(\mathrm{e}^x+1) - 2\log(2\mathrm{e}^x+1) + \mathrm{c}$

Answer: $x+\log \left(\mathrm{e}^x+1\right)-2 \log \left(2 \mathrm{e}^x+1\right)+\mathrm{c},$
where $c$ is the constant of integration

</details>

---

### Q100. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{\mathrm{e}^{\tan ^{-1} x}}{1+x^2}\left[\left(\sec ^{-1} \sqrt{1+x^2}\right)^2+\cos ^{-1}\left(\frac{1-x^2}{1+x^2}\right)\right] \mathrm{d} x$, where $x\gt0$ is

**Options:**

- **(A)** $\left(\tan ^{-1} x\right) \mathrm{e}^{\tan ^{-1} x}+\mathrm{c}$, where c is a constant of integration.
- **(B)** $\left(\tan ^{-1} x\right)^2 \mathrm{e}^{\tan ^{-1} x}+\mathrm{c}$, where c is a constant of integration.
- **(C)** $2\left(\tan ^{-1} x\right) \mathrm{e}^{\tan ^{-1} x}+\mathrm{c}$, where c is a constant of integration.
- **(D)** $2\left(\tan ^{-1} x\right)^2 \mathrm{e}^{\tan ^{-1} x}+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\tan ^{-1} x\right)^2 \mathrm{e}^{\tan ^{-1} x}+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $t = \tan^{-1} x$. Then $\mathrm{d}t = \dfrac{1}{1+x^2} \mathrm{d}x$.

Since $x > 0$, we have $t \in \left(0, \dfrac{\pi}{2}\right)$.

Evaluating the terms inside the bracket:

$\sec^{-1} \sqrt{1+x^2} = \sec^{-1} \sqrt{1+\tan^2 t} = \sec^{-1}(\sec t) = t$

$\cos^{-1}\left(\dfrac{1-x^2}{1+x^2}\right) = \cos^{-1}\left(\dfrac{1-\tan^2 t}{1+\tan^2 t}\right) = \cos^{-1}(\cos 2t) = 2t$

Substituting these into the given integral, we get:

$\int \mathrm{e}^t (t^2 + 2t) \mathrm{d}t$

Using the standard integral formula $\int \mathrm{e}^t [f(t) + f'(t)] \mathrm{d}t = \mathrm{e}^t f(t) + \mathrm{c}$, where $f(t) = t^2$ and $f'(t) = 2t$:

$\int \mathrm{e}^t (t^2 + 2t) \mathrm{d}t = t^2 \mathrm{e}^t + \mathrm{c}$

Substituting back $t = \tan^{-1} x$, we obtain:

$\left(\tan^{-1} x\right)^2 \mathrm{e}^{\tan^{-1} x} + \mathrm{c}$

Answer: $\left(\tan ^{-1} x\right)^2 \mathrm{e}^{\tan ^{-1} x}+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q101. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{x^2-4}{x^4+9 x^2+16} \cdot \mathrm{~d} x=\tan ^{-1}(\mathrm{f}(x))+\mathrm{c}($ where c is a constant of integration), then value of $f(2)$ is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

Let $I = \int \dfrac{x^2-4}{x^4+9 x^2+16} \mathrm{~d} x$

Dividing the numerator and the denominator by $x^2$, we get:

$I = \int \dfrac{1 - \dfrac{4}{x^2}}{x^2 + 9 + \dfrac{16}{x^2}} \mathrm{~d} x$

Let $x + \dfrac{4}{x} = t$. Differentiating with respect to $x$, we get:

$\left(1 - \dfrac{4}{x^2}\right) \mathrm{d}x = \mathrm{d}t$

Squaring $x + \dfrac{4}{x} = t$, we get:

$x^2 + \dfrac{16}{x^2} + 8 = t^2 \Rightarrow x^2 + \dfrac{16}{x^2} = t^2 - 8$

Substituting these into the integral:

$I = \int \dfrac{\mathrm{d}t}{(t^2 - 8) + 9}$

$I = \int \dfrac{\mathrm{d}t}{t^2 + 1}$

$I = \tan^{-1}(t) + c$

Substituting back $t = x + \dfrac{4}{x}$:

$I = \tan^{-1}\left(x + \dfrac{4}{x}\right) + c$

Comparing this with the given expression $\tan^{-1}(\mathrm{f}(x)) + \mathrm{c}$, we get:

$\mathrm{f}(x) = x + \dfrac{4}{x}$

Therefore, the value of $\mathrm{f}(2)$ is:

$\mathrm{f}(2) = 2 + \dfrac{4}{2} = 2 + 2 = 4$

Answer: 4

</details>

---

### Q102. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of the integral $\int_0^{\frac{\pi}{2}} \frac{\sqrt{\cot x}}{\sqrt{\cot x}+\sqrt{\tan x}} \mathrm{~d} x$ is

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{2}$
- **(C)** $\frac{\pi}{8}$
- **(D)** $2 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{4}$**

**Detailed Solution:**

Let $I = \int_0^{\dfrac{\pi}{2}} \dfrac{\sqrt{\cot x}}{\sqrt{\cot x}+\sqrt{\tan x}} \mathrm{~d} x$

Using the property $\int_0^a f(x) \mathrm{~d} x = \int_0^a f(a-x) \mathrm{~d} x$, we get:

$I = \int_0^{\dfrac{\pi}{2}} \dfrac{\sqrt{\cot(\dfrac{\pi}{2}-x)}}{\sqrt{\cot(\dfrac{\pi}{2}-x)}+\sqrt{\tan(\dfrac{\pi}{2}-x)}} \mathrm{~d} x$

$I = \int_0^{\dfrac{\pi}{2}} \dfrac{\sqrt{\tan x}}{\sqrt{\tan x}+\sqrt{\cot x}} \mathrm{~d} x$

Adding the two equations for $I$, we obtain:

$2I = \int_0^{\dfrac{\pi}{2}} \dfrac{\sqrt{\cot x} + \sqrt{\tan x}}{\sqrt{\cot x}+\sqrt{\tan x}} \mathrm{~d} x$

$2I = \int_0^{\dfrac{\pi}{2}} 1 \mathrm{~d} x$

$2I = [x]_0^{\dfrac{\pi}{2}} = \dfrac{\pi}{2}$

$I = \dfrac{\pi}{4}$

Answer: $\frac{\pi}{4}$

</details>

---

### Q103. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int\left(1+x-\frac{1}{x}\right) \mathrm{e}^{x+\frac{1}{x}} \mathrm{~d} x$ is equal to

**Options:**

- **(A)** $(x-1) \mathrm{e}^{x+\frac{1}{x}}+\mathrm{c}$, where c is a constant of integration.
- **(B)** $x \mathrm{e}^{x+\frac{1}{x}}+\mathrm{c}$, where c is a constant of integration.
- **(C)** $(x+1) \mathrm{e}^{x+\frac{1}{x}}+\mathrm{c}$, where c is a constant of integration.
- **(D)** $-x \mathrm{e}^{x+\frac{1}{x}}+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x \mathrm{e}^{x+\frac{1}{x}}+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $I = \int\left(1+x-\dfrac{1}{x}\right) \mathrm{e}^{x+\dfrac{1}{x}} \mathrm{~d} x$

We can split the integral into two parts:

$I = \int \mathrm{e}^{x+\dfrac{1}{x}} \mathrm{~d} x + \int \left(x-\dfrac{1}{x}\right) \mathrm{e}^{x+\dfrac{1}{x}} \mathrm{~d} x$

$I = \int \mathrm{e}^{x+\dfrac{1}{x}} \mathrm{~d} x + \int x\left(1-\dfrac{1}{x^2}\right) \mathrm{e}^{x+\dfrac{1}{x}} \mathrm{~d} x$

Applying integration by parts on the second integral, taking $x$ as the first function and $\left(1-\dfrac{1}{x^2}\right) \mathrm{e}^{x+\dfrac{1}{x}}$ as the second function:

$\int x\left(1-\dfrac{1}{x^2}\right) \mathrm{e}^{x+\dfrac{1}{x}} \mathrm{~d} x = x \int \left(1-\dfrac{1}{x^2}\right) \mathrm{e}^{x+\dfrac{1}{x}} \mathrm{~d} x - \int \left( \dfrac{\mathrm{d}}{\mathrm{d}x}(x) \int \left(1-\dfrac{1}{x^2}\right) \mathrm{e}^{x+\dfrac{1}{x}} \mathrm{~d} x \right) \mathrm{d} x$

To evaluate $\int \left(1-\dfrac{1}{x^2}\right) \mathrm{e}^{x+\dfrac{1}{x}} \mathrm{~d} x$, put $x+\dfrac{1}{x} = t \Rightarrow \left(1-\dfrac{1}{x^2}\right) \mathrm{d} x = \mathrm{d} t$.

$\int \mathrm{e}^t \mathrm{~d} t = \mathrm{e}^t = \mathrm{e}^{x+\dfrac{1}{x}}$

Substituting this back into the integration by parts formula:

$\int x\left(1-\dfrac{1}{x^2}\right) \mathrm{e}^{x+\dfrac{1}{x}} \mathrm{~d} x = x \mathrm{e}^{x+\dfrac{1}{x}} - \int 1 \cdot \mathrm{e}^{x+\dfrac{1}{x}} \mathrm{~d} x$

Now, substituting this result into the original expression for $I$:

$I = \int \mathrm{e}^{x+\dfrac{1}{x}} \mathrm{~d} x + x \mathrm{e}^{x+\dfrac{1}{x}} - \int \mathrm{e}^{x+\dfrac{1}{x}} \mathrm{~d} x + \mathrm{c}$

$I = x \mathrm{e}^{x+\dfrac{1}{x}} + \mathrm{c}$

Answer: $x \mathrm{e}^{x+\frac{1}{x}}+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q104. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{\mathrm{d} x}{1+3 \sin ^2 x}=\frac{1}{2} \tan ^{-1}(\mathrm{f}(x))+\mathrm{c}$, where c is -a constant of integration, then $\mathrm{f}(x)$ is equal to

**Options:**

- **(A)** $2 \tan x$
- **(B)** $2 \sin x$
- **(C)** $\tan x$
- **(D)** $\sin x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \tan x$**

**Detailed Solution:**

Let $I = \int \dfrac{dx}{1+3\sin^2 x}$

Dividing the numerator and the denominator by $\cos^2 x$:

$I = \int \dfrac{\sec^2 x}{\sec^2 x + 3\tan^2 x} dx$

Using the identity $\sec^2 x = 1 + \tan^2 x$:

$I = \int \dfrac{\sec^2 x}{1 + 4\tan^2 x} dx$

Let $2\tan x = t$, then $2\sec^2 x dx = dt$, which gives $\sec^2 x dx = \dfrac{dt}{2}$.

$I = \int \dfrac{1}{1 + t^2} \dfrac{dt}{2}$

$I = \dfrac{1}{2} \tan^{-1}(t) + c$

Substituting $t = 2\tan x$:

$I = \dfrac{1}{2} \tan^{-1}(2\tan x) + c$

Comparing with the given expression $\dfrac{1}{2} \tan^{-1}(\mathrm{f}(x)) + c$, we get:

$\mathrm{f}(x) = 2\tan x$

Answer: $2 \tan x$

</details>

---

### Q105. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{2 x+5}{\sqrt{7-6 x-x^2}} \mathrm{~d} x=\mathrm{A} \sqrt{7-6 x-x^2}+\mathrm{B} \sin ^{-1}\left(\frac{x+3}{4}\right)+\mathrm{c}$ (where c c is a constant of integration) then the value of $A+B$ is

**Options:**

- **(A)** -3
- **(B)** 1
- **(C)** -1
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -3**

**Detailed Solution:**

Let $I = \int \dfrac{2x+5}{\sqrt{7-6x-x^2}} dx$.

We express the numerator as $2x+5 = \lambda \dfrac{d}{dx}(7-6x-x^2) + \mu$.

$2x+5 = \lambda(-6-2x) + \mu$

Comparing coefficients, $-2\lambda = 2 \Rightarrow \lambda = -1$ and $-6\lambda + \mu = 5 \Rightarrow \mu = -1$.

$I = \int \dfrac{-(-6-2x) - 1}{\sqrt{7-6x-x^2}} dx$

$I = -\int \dfrac{-6-2x}{\sqrt{7-6x-x^2}} dx - \int \dfrac{1}{\sqrt{7-6x-x^2}} dx$

For the first integral, let $7-6x-x^2 = t \Rightarrow (-6-2x)dx = dt$.

$-\int t^{-1/2} dt = -2\sqrt{t} = -2\sqrt{7-6x-x^2}$.

For the second integral, complete the square:

$7-6x-x^2 = 16 - (x^2+6x+9) = 4^2 - (x+3)^2$.

$-\int \dfrac{1}{\sqrt{4^2 - (x+3)^2}} dx = -\sin^{-1}\left(\dfrac{x+3}{4}\right)$.

Combining both parts, we get:

$I = -2\sqrt{7-6x-x^2} - \sin^{-1}\left(\dfrac{x+3}{4}\right) + c$

Comparing with the given expression $A\sqrt{7-6x-x^2} + B\sin^{-1}\left(\dfrac{x+3}{4}\right) + c$, we have:

$A = -2$ and $B = -1$.

Therefore, $A+B = -2 - 1 = -3$.

Answer: -3

</details>

---

### Q106. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \cos (\log x) d x=$

**Options:**

- **(A)** $\frac{x}{2}(\sin (\log x)-\cos (\log x))+\mathrm{c}$,
(where c is a constant of integration)
- **(B)** $\quad x(\cos (\log x)-\sin (\log x))+\mathrm{c}$,
(where c is a constant of integration)
- **(C)** $\frac{x}{2}(\cos (\log x)+\sin (\log x))+\mathrm{c}$,
(where c is a constant of integration)
- **(D)** $\quad x(\cos (\log x)+\sin (\log x))+\mathrm{c}$,
(where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{x}{2}(\cos (\log x)+\sin (\log x))+\mathrm{c}$,
(where c is a constant of integration)**

**Detailed Solution:**

Let $I = \int \cos(\log x) dx$

Substitute $\log x = t \Rightarrow x = e^t \Rightarrow dx = e^t dt$

$I = \int e^t \cos t dt$

Using the standard integral $\int e^{at} \cos(bt) dt = \dfrac{e^{at}}{a^2+b^2}(a \cos(bt) + b \sin(bt)) + c$

Here $a = 1$ and $b = 1$

$I = \dfrac{e^t}{1^2+1^2}(\cos t + \sin t) + c$

$I = \dfrac{e^t}{2}(\cos t + \sin t) + c$

Substituting back $t = \log x$ and $e^t = x$

$I = \dfrac{x}{2}(\cos(\log x) + \sin(\log x)) + c$

Answer: $\frac{x}{2}(\cos (\log x)+\sin (\log x))+\mathrm{c}$,
(where c is a constant of integration)

</details>

---

### Q107. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{x+1}{x\left(1+x \mathrm{e}^x\right)^2} \mathrm{~d} x=$

**Options:**

- **(A)** $\log \left|\frac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right|+\frac{x}{1+x \mathrm{e}^x}+\mathrm{c},$ (where c is a constant of integration)
- **(B)** $\log \left|\frac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right|+\frac{\mathrm{e}^x}{1+x \mathrm{e}^x}+\mathrm{c}$ (where c is a constant of integration)
- **(C)** $\log \left|\frac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right|+\frac{1}{1+x \mathrm{e}^x}+\mathrm{c},$ (where c is a constant of integration)
- **(D)** $\log \left|\frac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right|-\frac{1}{1+x \mathrm{e}^x}+\mathrm{c},$ (where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log \left|\frac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right|+\frac{1}{1+x \mathrm{e}^x}+\mathrm{c},$ (where c is a constant of integration)**

**Detailed Solution:**

Let $I = \int \dfrac{x+1}{x(1+x \mathrm{e}^x)^2} \mathrm{d} x$

Multiplying the numerator and the denominator by $\mathrm{e}^x$, we get:

$I = \int \dfrac{(x+1)\mathrm{e}^x}{x \mathrm{e}^x (1+x \mathrm{e}^x)^2} \mathrm{d} x$

Let $x \mathrm{e}^x = t$. Differentiating both sides with respect to $x$:

$(x \mathrm{e}^x + \mathrm{e}^x) \mathrm{d} x = \mathrm{d} t$

$\mathrm{e}^x(x+1) \mathrm{d} x = \mathrm{d} t$

Substituting this into the integral, we get:

$I = \int \dfrac{1}{t(1+t)^2} \mathrm{d} t$

Using partial fractions, we can write:

$\dfrac{1}{t(1+t)^2} = \dfrac{1}{t} - \dfrac{1}{1+t} - \dfrac{1}{(1+t)^2}$

Integrating with respect to $t$:

$I = \int \left( \dfrac{1}{t} - \dfrac{1}{1+t} - \dfrac{1}{(1+t)^2} \right) \mathrm{d} t$

$I = \log|t| - \log|1+t| - \left(-\dfrac{1}{1+t}\right) + \mathrm{c}$

$I = \log \left| \dfrac{t}{1+t} \right| + \dfrac{1}{1+t} + \mathrm{c}$

Substituting back $t = x \mathrm{e}^x$:

$I = \log \left| \dfrac{x \mathrm{e}^x}{1+x \mathrm{e}^x} \right| + \dfrac{1}{1+x \mathrm{e}^x} + \mathrm{c}$

Answer: $\log \left|\frac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right|+\frac{1}{1+x \mathrm{e}^x}+\mathrm{c},$ (where c is a constant of integration)

</details>

---

### Q108. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $x \in[-1,1]$, then the value of $\int \mathrm{e}^{\sin ^{-1} x}\left(\frac{x+\sqrt{1-x^2}}{\sqrt{1-x^2}}\right) \mathrm{d} x$ is

**Options:**

- **(A)** $\mathrm{e}^{\sin ^{-1} x}+\mathrm{c}$, where c is constant of integration.
- **(B)** $\mathrm{e}^{\sin ^{-1} x} \cdot \sin x+\mathrm{c}$, where c is constant of integration.
- **(C)** $\mathrm{e}^{\sin ^{-1} x} \cdot \cos x+\mathrm{c}$, where c is constant of integration.
- **(D)** $\mathrm{e}^{\sin ^{-1} x} \cdot x+\mathrm{c}$, where c is constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{e}^{\sin ^{-1} x} \cdot x+\mathrm{c}$, where c is constant of integration.**

**Detailed Solution:**

Let $\sin^{-1} x = t$. Then $x = \sin t$ and $\dfrac{1}{\sqrt{1-x^2}} \mathrm{d}x = \mathrm{d}t$.

Also, $\sqrt{1-x^2} = \cos t$.

Substituting these into the given integral, we get:

$I = \int \mathrm{e}^t (\sin t + \cos t) \mathrm{d}t$

Using the standard integral formula $\int \mathrm{e}^t (f(t) + f'(t)) \mathrm{d}t = \mathrm{e}^t f(t) + c$, where $f(t) = \sin t$ and $f'(t) = \cos t$, we have:

$I = \mathrm{e}^t \sin t + c$

Substituting back $t = \sin^{-1} x$ and $\sin t = x$, we get:

$I = \mathrm{e}^{\sin^{-1} x} \cdot x + c$

Answer: $\mathrm{e}^{\sin ^{-1} x} \cdot x+\mathrm{c}$, where c is constant of integration.

</details>

---

### Q109. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \frac{\cos ^3 x}{\sin ^2 x+\sin x} \mathrm{~d} x$ is

**Options:**

- **(A)** $\quad \log (\sin x)-\sin x+\mathrm{c}$, where c is a constant of integration.
- **(B)** $\log (\sin x)-\cos x+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\log (\sin x)+\sin x+\mathrm{c}$, where c is a constant of integration.
- **(D)** $\log (\cos x)-\cos x+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\quad \log (\sin x)-\sin x+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $I = \int \dfrac{\cos^3 x}{\sin^2 x + \sin x} dx$

$I = \int \dfrac{\cos^2 x \cos x}{\sin x (\sin x + 1)} dx$

$I = \int \dfrac{(1 - \sin^2 x) \cos x}{\sin x (\sin x + 1)} dx$

$I = \int \dfrac{(1 - \sin x)(1 + \sin x) \cos x}{\sin x (\sin x + 1)} dx$

$I = \int \dfrac{(1 - \sin x) \cos x}{\sin x} dx$

$I = \int \left( \dfrac{\cos x}{\sin x} - \cos x \right) dx$

$I = \int (\cot x - \cos x) dx$

$I = \log (\sin x) - \sin x + c$

Answer: $\quad \log (\sin x)-\sin x+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q110. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If
$\int(7 x-2) \sqrt{3 x+2} \mathrm{~d} x=\mathrm{A}(3 x+2)^{\frac{5}{2}}+\mathrm{B}(3 x+2)^{\frac{3}{2}}+\mathrm{c}$
(where c is a constant of integration), then the values of $A$ and $B$ are respectively

**Options:**

- **(A)** $\frac{14}{45}, \frac{40}{27}$
- **(B)** $\frac{14}{15}, \frac{-40}{9}$
- **(C)** $\frac{14}{15}, \frac{40}{9}$
- **(D)** $\frac{14}{45}, \frac{-40}{27}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{14}{45}, \frac{-40}{27}$**

**Detailed Solution:**

Let $3x + 2 = t$.

Differentiating both sides, we get $3 \, dx = dt \Rightarrow dx = \dfrac{dt}{3}$.

Also, $x = \dfrac{t - 2}{3}$.

Substituting $x$ in the term $(7x - 2)$:

$7x - 2 = 7\left(\dfrac{t - 2}{3}\right) - 2 = \dfrac{7t - 14 - 6}{3} = \dfrac{7t - 20}{3}$

Now, substituting these into the integral:

$\int (7x - 2) \sqrt{3x + 2} \, dx = \int \left(\dfrac{7t - 20}{3}\right) \sqrt{t} \, \dfrac{dt}{3}$

$= \dfrac{1}{9} \int (7t - 20) t^{\dfrac{1}{2}} \, dt$

$= \dfrac{1}{9} \int \left(7t^{\dfrac{3}{2}} - 20t^{\dfrac{1}{2}}\right) \, dt$

Integrating term by term:

$= \dfrac{1}{9} \left[ 7 \left(\dfrac{t^{\dfrac{5}{2}}}{\dfrac{5}{2}}\right) - 20 \left(\dfrac{t^{\dfrac{3}{2}}}{\dfrac{3}{2}}\right) \right] + c$

$= \dfrac{1}{9} \left[ \dfrac{14}{5} t^{\dfrac{5}{2}} - \dfrac{40}{3} t^{\dfrac{3}{2}} \right] + c$

$= \dfrac{14}{45} t^{\dfrac{5}{2}} - \dfrac{40}{27} t^{\dfrac{3}{2}} + c$

Substituting back $t = 3x + 2$:

$= \dfrac{14}{45} (3x + 2)^{\dfrac{5}{2}} - \dfrac{40}{27} (3x + 2)^{\dfrac{3}{2}} + c$

Comparing this with the given expression $A(3x + 2)^{\dfrac{5}{2}} + B(3x + 2)^{\dfrac{3}{2}} + c$, we get:

$A = \dfrac{14}{45}$ and $B = \dfrac{-40}{27}$

Answer: $\frac{14}{45}, \frac{-40}{27}$

</details>

---

### Q111. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \sin ^{-1}\left(\dfrac{2 x}{1+x^2}\right) \mathrm{d} x=$

**Options:**

- **(A)** $2 x \tan ^{-1} x-\log \left(1+x^2\right)+\mathrm{c}$, where c is a constant of integration.
- **(B)** $2\left(x \tan ^{-1} x-\log \left(1+x^2\right)\right)+\mathrm{c}$, where c is a constant of integration.
- **(C)** $x \tan ^{-1} x+\log \left(1+x^2\right)+\mathrm{c}$, where c is a constant of integration.
- **(D)** $2\left(x \tan ^{-1} x+\log \left(1+x^2\right)\right)+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 x \tan ^{-1} x-\log \left(1+x^2\right)+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $I = \int \sin^{-1}\left(\dfrac{2x}{1+x^2}\right) \mathrm{d}x$

Substituting $x = \tan \theta$, we get $\mathrm{d}x = \sec^2 \theta \mathrm{d}\theta$.

$\sin^{-1}\left(\dfrac{2\tan\theta}{1+\tan^2\theta}\right) = \sin^{-1}(\sin 2\theta) = 2\theta = 2\tan^{-1}x$

Therefore, the integral becomes:

$I = \int 2\tan^{-1}x \mathrm{d}x$

Using integration by parts, taking $1$ as the second function:

$I = 2 \left[ \tan^{-1}x \int 1 \mathrm{d}x - \int \left( \dfrac{\mathrm{d}}{\mathrm{d}x}(\tan^{-1}x) \int 1 \mathrm{d}x \right) \mathrm{d}x \right]$

$I = 2 \left[ x \tan^{-1}x - \int \dfrac{x}{1+x^2} \mathrm{d}x \right]$

Multiplying and dividing the integral by $2$:

$I = 2 x \tan^{-1}x - \int \dfrac{2x}{1+x^2} \mathrm{d}x$

$I = 2 x \tan^{-1}x - \log(1+x^2) + \mathrm{c}$

Answer: $2 x \tan ^{-1} x-\log \left(1+x^2\right)+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q112. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \dfrac{\mathrm{d} x}{x^2\left(x^4+1\right)^{\dfrac{3}{4}}}$ is

**Options:**

- **(A)** $\left(\dfrac{-x^4+1}{x^4}\right)^{\dfrac{1}{4}}+\mathrm{c}$, where c is constant of integration.
- **(B)** $\left(x^4+1\right)^{\dfrac{1}{4}}+\mathrm{c}$, where c is constant of integration.
- **(C)** $-\left(x^4+1\right)^{\dfrac{1}{4}}+\mathrm{c}$, where c is constant of integration.
- **(D)** $-\left(\dfrac{x^4+1}{x^4}\right)^{\dfrac{1}{4}}+\mathrm{c}$, where c is constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\left(\dfrac{x^4+1}{x^4}\right)^{\dfrac{1}{4}}+\mathrm{c}$, where c is constant of integration.**

**Detailed Solution:**

Let $I = \int \dfrac{\mathrm{d} x}{x^2\left(x^4+1\right)^{\dfrac{3}{4}}}$

Taking $x^4$ common from the bracket in the denominator:

$I = \int \dfrac{\mathrm{d} x}{x^2 \left(x^4\left(1+\dfrac{1}{x^4}\right)\right)^{\dfrac{3}{4}}}$

$I = \int \dfrac{\mathrm{d} x}{x^2 \cdot x^3 \left(1+\dfrac{1}{x^4}\right)^{\dfrac{3}{4}}}$

$I = \int \dfrac{\mathrm{d} x}{x^5 \left(1+\dfrac{1}{x^4}\right)^{\dfrac{3}{4}}}$

Let $1+\dfrac{1}{x^4} = t$

Differentiating both sides with respect to $x$:

$-\dfrac{4}{x^5} \mathrm{d} x = \mathrm{d} t \Rightarrow \dfrac{\mathrm{d} x}{x^5} = -\dfrac{\mathrm{d} t}{4}$

Substituting this into the integral:

$I = \int \dfrac{1}{t^{\dfrac{3}{4}}} \left(-\dfrac{\mathrm{d} t}{4}\right)$

$I = -\dfrac{1}{4} \int t^{-\dfrac{3}{4}} \mathrm{d} t$

$I = -\dfrac{1}{4} \left(\dfrac{t^{\dfrac{1}{4}}}{\dfrac{1}{4}}\right) + \mathrm{c}$

$I = -t^{\dfrac{1}{4}} + \mathrm{c}$

Substituting back $t = 1+\dfrac{1}{x^4} = \dfrac{x^4+1}{x^4}$:

$I = -\left(\dfrac{x^4+1}{x^4}\right)^{\dfrac{1}{4}} + \mathrm{c}$

Answer: $-\left(\dfrac{x^4+1}{x^4}\right)^{\dfrac{1}{4}}+\mathrm{c}$, where c is constant of integration.

</details>

---

### Q113. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{\mathrm{d} x}{\sqrt{\mathrm{e}^x-1}}=2 \tan ^{-1}(\mathrm{f}(x))+\mathrm{c}$ where $x\gt0$ and c is a constant of integration, then $\mathrm{f}(x)$ is

**Options:**

- **(A)** $\mathrm{e}^x-1$
- **(B)** $\sqrt{\mathrm{e}^x-1}$
- **(C)** $\mathrm{e}^x+1$
- **(D)** $\sqrt{\mathrm{e}^x+1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{\mathrm{e}^x-1}$**

**Detailed Solution:**

Let $e^x - 1 = t^2$

Differentiating both sides, we get $e^x dx = 2t dt$

$\Rightarrow dx = \dfrac{2t dt}{e^x} = \dfrac{2t dt}{t^2 + 1}$

Substituting in the given integral:

$\int \dfrac{dx}{\sqrt{e^x - 1}} = \int \dfrac{1}{t} \left( \dfrac{2t dt}{t^2 + 1} \right)$

$= \int \dfrac{2 dt}{t^2 + 1}$

$= 2 \tan^{-1}(t) + c$

Substituting back $t = \sqrt{e^x - 1}$:

$= 2 \tan^{-1}(\sqrt{e^x - 1}) + c$

Comparing with $2 \tan^{-1}(f(x)) + c$, we get:

$f(x) = \sqrt{e^x - 1}$

Answer: $\sqrt{\mathrm{e}^x-1}$

</details>

---

### Q114. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int \dfrac{\sqrt{x}}{x+1} \mathrm{~d} x=$

**Options:**

- **(A)** $\left(2 \sqrt{x}-\tan ^{-1} \sqrt{x}\right)+\mathrm{c}$, where c is a constant of integration.
- **(B)** $2\left(\sqrt{x}-\tan ^{-1} \sqrt{x}\right)+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\left(2 \sqrt{x}+\tan ^{-1} \sqrt{x}\right)+\mathrm{c}$, where c is a constant of integration.
- **(D)** $2\left(\sqrt{x}+\tan ^{-1} \sqrt{x}\right)+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2\left(\sqrt{x}-\tan ^{-1} \sqrt{x}\right)+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $x = t^2$, which gives $\mathrm{d}x = 2t \mathrm{~d}t$.

Substituting these into the integral:

$\int \dfrac{\sqrt{x}}{x+1} \mathrm{~d}x = \int \dfrac{t}{t^2+1} (2t) \mathrm{~d}t$

$= 2 \int \dfrac{t^2}{t^2+1} \mathrm{~d}t$

$= 2 \int \dfrac{t^2+1-1}{t^2+1} \mathrm{~d}t$

$= 2 \int \left(1 - \dfrac{1}{t^2+1}\right) \mathrm{~d}t$

$= 2 \left(t - \tan^{-1} t\right) + \mathrm{c}$

Substituting $t = \sqrt{x}$:

$= 2 \left(\sqrt{x} - \tan^{-1} \sqrt{x}\right) + \mathrm{c}$

Answer: $2\left(\sqrt{x}-\tan ^{-1} \sqrt{x}\right)+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q115. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\int(2 x+4) \sqrt{x-1} \mathrm{~d} x=\mathrm{a}(x-1)^{\dfrac{5}{2}}+\mathrm{b}(x-1)^{\dfrac{3}{2}}+\mathrm{c}$, (where c is a constant of integration), then the value of $a+b$ is

**Options:**

- **(A)** $\dfrac{46}{5}$
- **(B)** $\dfrac{16}{15}$
- **(C)** $\dfrac{24}{5}$
- **(D)** $\dfrac{13}{15}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{24}{5}$**

**Detailed Solution:**

Let $x - 1 = t \Rightarrow dx = dt$.

Substituting this into the integral, we get:

$\int (2(t+1)+4) \sqrt{t} \, dt$

$= \int (2t+6) t^{\dfrac{1}{2}} \, dt$

$= \int \left(2t^{\dfrac{3}{2}} + 6t^{\dfrac{1}{2}}\right) \, dt$

$= 2 \left(\dfrac{t^{\dfrac{5}{2}}}{\dfrac{5}{2}}\right) + 6 \left(\dfrac{t^{\dfrac{3}{2}}}{\dfrac{3}{2}}\right) + c$

$= \dfrac{4}{5} t^{\dfrac{5}{2}} + 4 t^{\dfrac{3}{2}} + c$

Substituting back $t = x-1$:

$= \dfrac{4}{5} (x-1)^{\dfrac{5}{2}} + 4 (x-1)^{\dfrac{3}{2}} + c$

Comparing this with the given expression $\mathrm{a}(x-1)^{\dfrac{5}{2}}+\mathrm{b}(x-1)^{\dfrac{3}{2}}+\mathrm{c}$, we get:

$\mathrm{a} = \dfrac{4}{5}$ and $\mathrm{b} = 4$

Therefore, $\mathrm{a}+\mathrm{b} = \dfrac{4}{5} + 4 = \dfrac{24}{5}$

Answer: $\dfrac{24}{5}$

</details>

---

### Q116. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If, $\int \dfrac{d \theta}{\cos ^2 \theta(\tan 2 \theta+\sec 2 \theta)}=\lambda \tan \theta+2 \log _{\mathrm{e}}|\mathrm{f}(\theta)|+\mathrm{c}$ (where c is a constant of integration), then the ordered pair $(\lambda,|f(\theta)|)$ is equal to

**Options:**

- **(A)** $(1,|1+\tan \theta \mid)$
- **(B)** $(1,|1-\tan \theta|)$
- **(C)** $\quad(-1,|1+\tan \theta|)$
- **(D)** $\quad(-1,|1-\tan \theta|)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\quad(-1,|1+\tan \theta|)$**

**Detailed Solution:**

Let the given integral be $I = \int \dfrac{d \theta}{\cos ^2 \theta(\tan 2 \theta+\sec 2 \theta)}$.

We can rewrite the integral as:

$I = \int \dfrac{\sec^2 \theta}{\tan 2 \theta+\sec 2 \theta} d \theta$

Simplifying the denominator:

$\tan 2 \theta+\sec 2 \theta = \dfrac{\sin 2 \theta+1}{\cos 2 \theta} = \dfrac{(\cos \theta+\sin \theta)^2}{\cos^2 \theta-\sin^2 \theta} = \dfrac{\cos \theta+\sin \theta}{\cos \theta-\sin \theta} = \dfrac{1+\tan \theta}{1-\tan \theta}$

Substituting this back into the integral, we get:

$I = \int \dfrac{1-\tan \theta}{1+\tan \theta} \sec^2 \theta d \theta$

Let $\tan \theta = t$, then $\sec^2 \theta d \theta = dt$.

$I = \int \dfrac{1-t}{1+t} dt$

$I = \int \left(\dfrac{2}{1+t}-1\right) dt$

$I = 2 \log_e |1+t| - t + c$

Substituting $t = \tan \theta$ back into the expression:

$I = -\tan \theta + 2 \log_e |1+\tan \theta| + c$

Comparing this with the given expression $\lambda \tan \theta+2 \log_e|f(\theta)|+c$, we get:

$\lambda = -1$

$|f(\theta)| = |1+\tan \theta|$

Therefore, the ordered pair $(\lambda, |f(\theta)|)$ is $(-1, |1+\tan \theta|)$.

Answer: $\quad(-1,|1+\tan \theta|)$

</details>

---

### Q117. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \dfrac{\cos x-\sin x}{\sqrt{8-\sin 2 x}} \mathrm{~d} x=\operatorname{asin}^{-1}\left(\dfrac{\sin x+\cos x}{b}\right)+c$
Where c is a constant of integration, then the ordered pair $(\mathrm{a}, \mathrm{b})$ is equal to

**Options:**

- **(A)** $(1,3)$
- **(B)** $(3,1)$
- **(C)** $(-1,3)$
- **(D)** $(-3,1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(1,3)$**

**Detailed Solution:**

Let $t = \sin x + \cos x$.

Differentiating with respect to $x$, we get $dt = (\cos x - \sin x) dx$.

Squaring both sides of $t = \sin x + \cos x$, we get $t^2 = \sin^2 x + \cos^2 x + 2 \sin x \cos x = 1 + \sin 2x$.

This gives $\sin 2x = t^2 - 1$.

Substituting these into the given integral, we get:

$\int \dfrac{\cos x - \sin x}{\sqrt{8 - \sin 2x}} dx = \int \dfrac{dt}{\sqrt{8 - (t^2 - 1)}}$

$= \int \dfrac{dt}{\sqrt{9 - t^2}}$

$= \sin^{-1}\left(\dfrac{t}{3}\right) + c$

Substituting back $t = \sin x + \cos x$, we get:

$= \sin^{-1}\left(\dfrac{\sin x + \cos x}{3}\right) + c$

Comparing this with $a \sin^{-1}\left(\dfrac{\sin x + \cos x}{b}\right) + c$, we get $a = 1$ and $b = 3$.

Therefore, the ordered pair $(a, b)$ is $(1, 3)$.

Answer: $(1,3)$

</details>

---

### Q118. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \dfrac{\mathrm{d} x}{(x+1)^{3 / 4}(x-2)^{5 / 4}}$ is equal to

**Options:**

- **(A)** $4\left(\dfrac{x+1}{x-2}\right)^{1 / 4}+\mathrm{c}$, where c is a constant of integration.
- **(B)** $\quad 4\left(\dfrac{x-2}{x-1}\right)^{1 / 4}+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\dfrac{-4}{3}\left(\dfrac{x-2}{x+1}\right)^{1 / 4}+\mathrm{c}$, where c is a constant of integration.
- **(D)** $\dfrac{-4}{3}\left(\dfrac{x+1}{x-2}\right)^{1 / 4}+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{-4}{3}\left(\dfrac{x+1}{x-2}\right)^{1 / 4}+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $I = \int \dfrac{\mathrm{d} x}{(x+1)^{3 / 4}(x-2)^{5 / 4}}$

Dividing and multiplying the denominator by $(x-2)^{3/4}$, we get:

$I = \int \dfrac{\mathrm{d} x}{\left(\dfrac{x+1}{x-2}\right)^{3 / 4} (x-2)^2}$

Let $\dfrac{x+1}{x-2} = t$

Differentiating both sides with respect to $x$, we get:

$\dfrac{(x-2)(1) - (x+1)(1)}{(x-2)^2} \mathrm{d} x = \mathrm{d} t$

$\dfrac{-3}{(x-2)^2} \mathrm{d} x = \mathrm{d} t$

$\dfrac{\mathrm{d} x}{(x-2)^2} = -\dfrac{1}{3} \mathrm{d} t$

Substituting this into the integral, we get:

$I = \int \dfrac{1}{t^{3/4}} \left(-\dfrac{1}{3}\right) \mathrm{d} t$

$I = -\dfrac{1}{3} \int t^{-3/4} \mathrm{d} t$

$I = -\dfrac{1}{3} \left( \dfrac{t^{1/4}}{1/4} \right) + \mathrm{c}$

$I = -\dfrac{4}{3} t^{1/4} + \mathrm{c}$

$I = -\dfrac{4}{3} \left( \dfrac{x+1}{x-2} \right)^{1/4} + \mathrm{c}$

Answer: $\dfrac{-4}{3}\left(\dfrac{x+1}{x-2}\right)^{1 / 4}+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q119. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \sqrt{\mathrm{e}^x-1} \mathrm{~d} x=$

**Options:**

- **(A)** $\sqrt{\mathrm{e}^x-1}+\tan ^{-1} \sqrt{\mathrm{e}^x-1}+\mathrm{c}$, (where c is constant of integration)
- **(B)** $2 \sqrt{\mathrm{e}^x-1}+\tan ^{-1} \sqrt{\mathrm{e}^x-1}+\mathrm{c}$, (where c is constant of integration)
- **(C)** $2 \sqrt{\mathrm{e}^x-1}-2 \tan ^{-1} \sqrt{\mathrm{e}^x-1}+\mathrm{c}$, (where c is constant of integration)
- **(D)** $2 \sqrt{\mathrm{e}^x-1}-\tan ^{-1} \sqrt{\mathrm{e}^x-1}+\mathrm{c}$, (where c is constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 \sqrt{\mathrm{e}^x-1}-2 \tan ^{-1} \sqrt{\mathrm{e}^x-1}+\mathrm{c}$, (where c is constant of integration)**

**Detailed Solution:**

Let $\mathrm{e}^x - 1 = t^2$.

Differentiating both sides, we get $\mathrm{e}^x \mathrm{d}x = 2t \mathrm{d}t$.

$\mathrm{d}x = \dfrac{2t}{\mathrm{e}^x} \mathrm{d}t = \dfrac{2t}{t^2 + 1} \mathrm{d}t$

Substituting this into the integral, we get:

$I = \int t \cdot \dfrac{2t}{t^2 + 1} \mathrm{d}t = 2 \int \dfrac{t^2}{t^2 + 1} \mathrm{d}t$

$I = 2 \int \dfrac{t^2 + 1 - 1}{t^2 + 1} \mathrm{d}t = 2 \int \left( 1 - \dfrac{1}{t^2 + 1} \right) \mathrm{d}t$

$I = 2 \left( t - \tan^{-1} t \right) + \mathrm{c}$

$I = 2t - 2\tan^{-1} t + \mathrm{c}$

Substituting back $t = \sqrt{\mathrm{e}^x - 1}$, we get:

$I = 2\sqrt{\mathrm{e}^x - 1} - 2\tan^{-1} \sqrt{\mathrm{e}^x - 1} + \mathrm{c}$

Answer: $2 \sqrt{\mathrm{e}^x-1}-2 \tan ^{-1} \sqrt{\mathrm{e}^x-1}+\mathrm{c}$, (where c is constant of integration)

</details>

---

### Q120. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \dfrac{x+1}{x\left(1+x e^x\right)^2} \mathrm{~d} x$ is equal to

**Options:**

- **(A)** $\log \left(\dfrac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right)+\dfrac{x}{1+x \mathrm{e}^x}+\mathrm{c}$, where c is a constant of integration
- **(B)** $\log \left(\dfrac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right)+\dfrac{\mathrm{e}^x}{1+x \mathrm{e}^x}+\mathrm{c}$, where c is a constant of integration
- **(C)** $\log \left(\dfrac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right)+\dfrac{1}{1+x \mathrm{e}^x}+\mathrm{c}$, where c is a constant of integration
- **(D)** $\log \left(\dfrac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right)-\dfrac{x}{1+x \mathrm{e}^x}+\mathrm{c}$, where c is a constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log \left(\dfrac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right)+\dfrac{1}{1+x \mathrm{e}^x}+\mathrm{c}$, where c is a constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{x+1}{x\left(1+x e^x\right)^2} \mathrm{d} x$

Multiplying the numerator and the denominator by $e^x$, we get:

$I = \int \dfrac{(x+1)e^x}{x e^x \left(1+x e^x\right)^2} \mathrm{d} x$

Let $x e^x = t$. Differentiating both sides with respect to $x$:

$(x e^x + e^x) \mathrm{d} x = \mathrm{d} t$

$e^x(x+1) \mathrm{d} x = \mathrm{d} t$

Substituting this into the integral:

$I = \int \dfrac{1}{t(1+t)^2} \mathrm{d} t$

Using partial fractions, we can write:

$\dfrac{1}{t(1+t)^2} = \dfrac{1+t-t}{t(1+t)^2} = \dfrac{1}{t(1+t)} - \dfrac{1}{(1+t)^2}$

$\dfrac{1}{t(1+t)^2} = \dfrac{1+t-t}{t(1+t)} - \dfrac{1}{(1+t)^2} = \dfrac{1}{t} - \dfrac{1}{1+t} - \dfrac{1}{(1+t)^2}$

Now, integrating with respect to $t$:

$I = \int \left( \dfrac{1}{t} - \dfrac{1}{1+t} - \dfrac{1}{(1+t)^2} \right) \mathrm{d} t$

$I = \log t - \log(1+t) + \dfrac{1}{1+t} + \mathrm{c}$

$I = \log \left(\dfrac{t}{1+t}\right) + \dfrac{1}{1+t} + \mathrm{c}$

Substituting back $t = x e^x$:

$I = \log \left(\dfrac{x e^x}{1+x e^x}\right) + \dfrac{1}{1+x e^x} + \mathrm{c}$

Answer: $\log \left(\dfrac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right)+\dfrac{1}{1+x \mathrm{e}^x}+\mathrm{c}$, where c is a constant of integration

</details>

---

### Q121. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \dfrac{\mathrm{d} x}{\sqrt[3]{\sin ^{11} x \cos x}}=-\left(\dfrac{3}{8} \mathrm{f}(x)+\dfrac{3}{2} \mathrm{~g}(x)\right)+\mathrm{c}$ then

**Options:**

- **(A)** $\mathrm{f}(x)=\tan ^{\dfrac{-8}{3}} x, \mathrm{~g}(x)=\tan ^{\dfrac{-2}{3}} x$, (where c is a constant of integration)
- **(B)** $\mathrm{f}(x)=\tan ^{\dfrac{8}{3}} x, \mathrm{~g}(x)=\tan ^{-\dfrac{2}{3}} x$, (where c is a constant of integration)
- **(C)** $\mathrm{f}(x)=\tan ^{\dfrac{-8}{3}} x, \mathrm{~g}(x)=\tan ^{\dfrac{2}{3}} x$, (where c is a constant of integration)
- **(D)** $\mathrm{f}(x)=\tan ^{\dfrac{8}{3}} x, \mathrm{~g}(x)=\tan ^{\dfrac{2}{3}} x$, (where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{f}(x)=\tan ^{\dfrac{-8}{3}} x, \mathrm{~g}(x)=\tan ^{\dfrac{-2}{3}} x$, (where c is a constant of integration)**

**Detailed Solution:**

Let $I = \int \dfrac{\mathrm{d} x}{\sqrt[3]{\sin ^{11} x \cos x}} = \int \sin^{\dfrac{-11}{3}} x \cos^{\dfrac{-1}{3}} x \, \mathrm{d} x$

The sum of the exponents of $\sin x$ and $\cos x$ is $\dfrac{-11}{3} - \dfrac{1}{3} = -4$, which is an even negative integer. Dividing the numerator and denominator by $\cos^4 x$, we get:

$I = \int \dfrac{\sec^4 x}{\tan^{\dfrac{11}{3}} x} \, \mathrm{d} x$

Let $\tan x = t$, then $\sec^2 x \, \mathrm{d} x = \mathrm{d} t$.

$I = \int \dfrac{1 + t^2}{t^{\dfrac{11}{3}}} \, \mathrm{d} t$

$I = \int \left(t^{\dfrac{-11}{3}} + t^{\dfrac{-5}{3}}\right) \, \mathrm{d} t$

$I = \dfrac{t^{\dfrac{-8}{3}}}{\dfrac{-8}{3}} + \dfrac{t^{\dfrac{-2}{3}}}{\dfrac{-2}{3}} + \mathrm{c}$

$I = -\dfrac{3}{8} t^{\dfrac{-8}{3}} - \dfrac{3}{2} t^{\dfrac{-2}{3}} + \mathrm{c}$

Substituting $t = \tan x$:

$I = -\left(\dfrac{3}{8} \tan^{\dfrac{-8}{3}} x + \dfrac{3}{2} \tan^{\dfrac{-2}{3}} x\right) + \mathrm{c}$

Comparing this with the given expression $-\left(\dfrac{3}{8} \mathrm{f}(x)+\dfrac{3}{2} \mathrm{~g}(x)\right)+\mathrm{c}$, we get:

$\mathrm{f}(x) = \tan^{\dfrac{-8}{3}} x$ and $\mathrm{g}(x) = \tan^{\dfrac{-2}{3}} x$

Answer: $\mathrm{f}(x)=\tan ^{\dfrac{-8}{3}} x, \mathrm{~g}(x)=\tan ^{\dfrac{-2}{3}} x$, (where c is a constant of integration)

</details>

---

### Q122. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\int \mathrm{f}(x) \mathrm{d} x=\psi(x)$, then $\int x^5 \mathrm{f}\left(x^3\right) \mathrm{d} x$ is equal to

**Options:**

- **(A)** $\dfrac{1}{3} x^3 \psi\left(x^3\right)-3 \int x^3 \psi\left(x^3\right) \mathrm{d} x+\mathrm{c}$, (where c is a constant of integration)
- **(B)** $\dfrac{1}{3}\left(x^3 \psi\left(x^3\right)-\int x^3 \psi\left(x^3\right) \mathrm{d} x\right)+\mathrm{c}$, (where c is a constant of integration)
- **(C)** $\dfrac{1}{3} x^3 \psi\left(x^3\right)-\int x^2 \psi\left(x^3\right) \mathrm{d} x+\mathrm{c}$, (where c is a constant of integration)
- **(D)** $\dfrac{1}{3}\left(x^3 \psi\left(x^3\right)-\int x^2 \psi\left(x^3\right) \mathrm{d} x\right)+\mathrm{c}$, (where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{3} x^3 \psi\left(x^3\right)-\int x^2 \psi\left(x^3\right) \mathrm{d} x+\mathrm{c}$, (where c is a constant of integration)**

**Detailed Solution:**

Let $I = \int x^5 \mathrm{f}\left(x^3\right) \mathrm{d} x = \int x^3 \mathrm{f}\left(x^3\right) x^2 \mathrm{d} x$

Substitute $x^3 = t \Rightarrow 3x^2 \mathrm{d} x = \mathrm{d} t \Rightarrow x^2 \mathrm{d} x = \dfrac{1}{3} \mathrm{d} t$

$I = \dfrac{1}{3} \int t \mathrm{f}(t) \mathrm{d} t$

Using integration by parts, taking $t$ as the first function and $\mathrm{f}(t)$ as the second function:

$I = \dfrac{1}{3} \left( t \int \mathrm{f}(t) \mathrm{d} t - \int \left( \dfrac{\mathrm{d}}{\mathrm{d} t}(t) \int \mathrm{f}(t) \mathrm{d} t \right) \mathrm{d} t \right)$

Given $\int \mathrm{f}(x) \mathrm{d} x = \psi(x)$, we have $\int \mathrm{f}(t) \mathrm{d} t = \psi(t)$.

$I = \dfrac{1}{3} \left( t \psi(t) - \int \psi(t) \mathrm{d} t \right) + \mathrm{c}$

Substituting back $t = x^3$ and $\mathrm{d} t = 3x^2 \mathrm{d} x$:

$I = \dfrac{1}{3} \left( x^3 \psi\left(x^3\right) - \int \psi\left(x^3\right) 3x^2 \mathrm{d} x \right) + \mathrm{c}$

$I = \dfrac{1}{3} x^3 \psi\left(x^3\right) - \int x^2 \psi\left(x^3\right) \mathrm{d} x + \mathrm{c}$

Answer: $\dfrac{1}{3} x^3 \psi\left(x^3\right)-\int x^2 \psi\left(x^3\right) \mathrm{d} x+\mathrm{c}$, (where c is a constant of integration)

</details>

---

### Q123. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int \dfrac{\mathrm{d} x}{x^2\left(x^4+1\right)^{\dfrac{3}{4}}}$ is

**Options:**

- **(A)** $\left(x^4+1\right)^{\dfrac{1}{4}}+\mathrm{c}$, where c is a constant of integration.
- **(B)** $\dfrac{\left(x^4+1\right)^{\dfrac{1}{4}}}{x}+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\dfrac{-\left(x^4+1\right)^{\dfrac{1}{4}}}{x}+\mathrm{c}$, where c is a constant of integration.
- **(D)** $-\left(x^4+1\right)^{\dfrac{1}{4}}+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{-\left(x^4+1\right)^{\dfrac{1}{4}}}{x}+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $I = \int \dfrac{\mathrm{d} x}{x^2\left(x^4+1\right)^{\dfrac{3}{4}}}$

Factoring out $x^4$ from the term $\left(x^4+1\right)^{\dfrac{3}{4}}$, we get:

$\left(x^4+1\right)^{\dfrac{3}{4}} = \left(x^4\left(1+\dfrac{1}{x^4}\right)\right)^{\dfrac{3}{4}} = x^3\left(1+\dfrac{1}{x^4}\right)^{\dfrac{3}{4}}$

Substituting this back into the integral:

$I = \int \dfrac{\mathrm{d} x}{x^2 \cdot x^3 \left(1+\dfrac{1}{x^4}\right)^{\dfrac{3}{4}}} = \int \dfrac{\mathrm{d} x}{x^5 \left(1+\dfrac{1}{x^4}\right)^{\dfrac{3}{4}}}$

Let $1 + \dfrac{1}{x^4} = t$

Differentiating both sides with respect to $x$:

$-\dfrac{4}{x^5} \mathrm{d} x = \mathrm{d} t \Rightarrow \dfrac{\mathrm{d} x}{x^5} = -\dfrac{1}{4} \mathrm{d} t$

Substituting this into the integral:

$I = \int \dfrac{-\dfrac{1}{4} \mathrm{d} t}{t^{\dfrac{3}{4}}} = -\dfrac{1}{4} \int t^{-\dfrac{3}{4}} \mathrm{d} t$

Integrating with respect to $t$:

$I = -\dfrac{1}{4} \dfrac{t^{\dfrac{1}{4}}}{\dfrac{1}{4}} + \mathrm{c} = -t^{\dfrac{1}{4}} + \mathrm{c}$

Substituting $t = 1 + \dfrac{1}{x^4}$ back into the expression:

$I = -\left(1 + \dfrac{1}{x^4}\right)^{\dfrac{1}{4}} + \mathrm{c} = -\left(\dfrac{x^4+1}{x^4}\right)^{\dfrac{1}{4}} + \mathrm{c} = \dfrac{-\left(x^4+1\right)^{\dfrac{1}{4}}}{x} + \mathrm{c}$

Answer: $\dfrac{-\left(x^4+1\right)^{\dfrac{1}{4}}}{x}+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q124. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The integral $\int \sec ^{\dfrac{2}{3}} x \cdot \operatorname{cosec}^{\dfrac{4}{3}} x \mathrm{~d} x$ is equal to

**Options:**

- **(A)** $3(\tan x)^{-\dfrac{1}{3}}+\mathrm{c}$, (where c is the constant of integration)
- **(B)** $-\dfrac{3}{4}(\tan x)^{\dfrac{4}{3}}+\mathrm{c},($ where c is the constant of integration)
- **(C)** $\quad-3(\cot x)^{-\dfrac{1}{3}}+\mathrm{c}$, (where c is the constant of integration)
- **(D)** $\quad-3(\tan x)^{-\dfrac{1}{3}}+\mathrm{c},($ where c is the constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\quad-3(\tan x)^{-\dfrac{1}{3}}+\mathrm{c},($ where c is the constant of integration)**

**Detailed Solution:**

Let $I = \int \sec^{\dfrac{2}{3}} x \cdot \operatorname{cosec}^{\dfrac{4}{3}} x \, \mathrm{d} x$

$I = \int \dfrac{1}{\cos^{\dfrac{2}{3}} x \sin^{\dfrac{4}{3}} x} \, \mathrm{d} x$

Dividing the numerator and the denominator by $\cos^2 x$:

$I = \int \dfrac{\sec^2 x}{\dfrac{\cos^{\dfrac{2}{3}} x \sin^{\dfrac{4}{3}} x}{\cos^2 x}} \, \mathrm{d} x$

$I = \int \dfrac{\sec^2 x}{\tan^{\dfrac{4}{3}} x} \, \mathrm{d} x$

Let $\tan x = t$, then $\sec^2 x \, \mathrm{d} x = \mathrm{d} t$

$I = \int t^{-\dfrac{4}{3}} \, \mathrm{d} t$

$I = \dfrac{t^{-\dfrac{1}{3}}}{-\dfrac{1}{3}} + \mathrm{c}$

$I = -3(\tan x)^{-\dfrac{1}{3}} + \mathrm{c}$

Answer: $\quad-3(\tan x)^{-\dfrac{1}{3}}+\mathrm{c},($ where c is the constant of integration)

</details>

---

### Q125. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\mathrm{I}=\int \dfrac{x^2}{(\mathrm{a}+\mathrm{b} x)^2} \mathrm{~d} x$ is

**Options:**

- **(A)** $\dfrac{1}{b^3}\left[a+b x+2 a \log |a+b x|-\dfrac{a^2}{a+b x}\right]+c$,
(where c is the constant of integration)
- **(B)** $\dfrac{1}{b^3}\left[a+b x-2 a \log |a+b x|+\dfrac{a^2}{a+b x}\right]+c$,
(where c is the constant of integration)
- **(C)** $\dfrac{1}{b^3}\left[a+b x-2 a \log |a+b x|-\dfrac{a^2}{a+b x}\right]+c$, (where c is the constant of integration)
- **(D)** $\dfrac{1}{b^3}\left[a+b x+2 a \log |a+b x|+\dfrac{a^2}{a+b x}\right]+c$,
(where c is the constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{b^3}\left[a+b x-2 a \log |a+b x|-\dfrac{a^2}{a+b x}\right]+c$, (where c is the constant of integration)**

**Detailed Solution:**

Let $a+bx = t$. Then $x = \dfrac{t-a}{b}$ and $dx = \dfrac{1}{b} dt$.

Substituting these into the integral:

$I = \int \dfrac{\left(\dfrac{t-a}{b}\right)^2}{t^2} \dfrac{1}{b} dt$

$I = \dfrac{1}{b^3} \int \dfrac{(t-a)^2}{t^2} dt$

$I = \dfrac{1}{b^3} \int \dfrac{t^2 - 2at + a^2}{t^2} dt$

$I = \dfrac{1}{b^3} \int \left( 1 - \dfrac{2a}{t} + \dfrac{a^2}{t^2} \right) dt$

$I = \dfrac{1}{b^3} \left[ t - 2a \log|t| - \dfrac{a^2}{t} \right] + c$

Substituting $t = a+bx$ back into the expression:

$I = \dfrac{1}{b^3} \left[ a+bx - 2a \log|a+bx| - \dfrac{a^2}{a+bx} \right] + c$

Answer: $\dfrac{1}{b^3}\left[a+b x-2 a \log |a+b x|-\dfrac{a^2}{a+b x}\right]+c$, (where c is the constant of integration)

</details>

---

### Q126. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\int \sin \sqrt{x} d x$ is equal to

**Options:**

- **(A)** $\sin \sqrt{x}-2 \sqrt{x} \cos \sqrt{x}+c$, where $c$ is a constant of integration.
- **(B)** $2 \cos \sqrt{x}-2 \sqrt{x} \sin \sqrt{x}+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\cos \sqrt{x}-2 \sqrt{x} \sin \sqrt{x}+\mathrm{c}$, where c is a constant of integration.
- **(D)** $2 \sin \sqrt{x}-2 \sqrt{x} \cos \sqrt{x}+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 \sin \sqrt{x}-2 \sqrt{x} \cos \sqrt{x}+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $I = \int \sin \sqrt{x} d x$

Substitute $\sqrt{x} = t \Rightarrow x = t^2 \Rightarrow d x = 2t d t$

$I = \int (\sin t) 2t d t = 2 \int t \sin t d t$

Using integration by parts, taking $t$ as the first function and $\sin t$ as the second function:

$I = 2 \left[ t \int \sin t d t - \int \left( \dfrac{d}{d t}(t) \int \sin t d t \right) d t \right]$

$I = 2 \left[ t(-\cos t) - \int 1 \cdot (-\cos t) d t \right]$

$I = 2 \left[ -t \cos t + \int \cos t d t \right]$

$I = 2 \left[ -t \cos t + \sin t \right] + c$

$I = 2 \sin t - 2t \cos t + c$

Substituting $t = \sqrt{x}$:

$I = 2 \sin \sqrt{x} - 2 \sqrt{x} \cos \sqrt{x} + c$

Answer: $2 \sin \sqrt{x}-2 \sqrt{x} \cos \sqrt{x}+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q127. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{\operatorname{cosec} x d x}{\cos ^2\left(1+\log \tan \dfrac{x}{2}\right)}=$

**Options:**

- **(A)** $\tan \left(1+\log \tan \dfrac{x}{2}\right)+\mathrm{c}$, where c is a constant of integration.
- **(B)** $\dfrac{1}{2} \tan \left(1+\log \tan \dfrac{x}{2}\right)+\mathrm{c}$, where c is a constant of integration.
- **(C)** $2 \tan \left(1+\log \tan \dfrac{x}{2}\right)+\mathrm{c}$, where c is a constant of integration.
- **(D)** $\dfrac{1}{4} \tan \left(1+\log \tan \dfrac{x}{2}\right)+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\tan \left(1+\log \tan \dfrac{x}{2}\right)+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $t = 1 + \log \tan \dfrac{x}{2}$

Differentiating with respect to $x$:

$dt = \dfrac{1}{\tan \dfrac{x}{2}} \cdot \sec^2 \dfrac{x}{2} \cdot \dfrac{1}{2} dx$

$dt = \dfrac{\cos \dfrac{x}{2}}{\sin \dfrac{x}{2}} \cdot \dfrac{1}{\cos^2 \dfrac{x}{2}} \cdot \dfrac{1}{2} dx$

$dt = \dfrac{1}{2 \sin \dfrac{x}{2} \cos \dfrac{x}{2}} dx$

$dt = \dfrac{1}{\sin x} dx = \operatorname{cosec} x dx$

Substituting this into the given integral:

$\int \dfrac{\operatorname{cosec} x dx}{\cos^2\left(1+\log \tan \dfrac{x}{2}\right)} = \int \dfrac{dt}{\cos^2 t}$

$= \int \sec^2 t dt$

$= \tan t + c$

Substituting back the value of $t$:

$= \tan \left(1 + \log \tan \dfrac{x}{2}\right) + c$

Answer: $\tan \left(1+\log \tan \dfrac{x}{2}\right)+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q128. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\int(2 x+4) \sqrt{x-1} \mathrm{~d} x=\mathrm{a}(x-1)^{5 / 2}+\mathrm{b}(x-1)^{3 / 2}+\mathrm{c}$ where c is a constant of integration, then the value of $(2 a+b)$ is

**Options:**

- **(A)** $\dfrac{20}{5}$
- **(B)** $\dfrac{28}{5}$
- **(C)** $\dfrac{48}{5}$
- **(D)** $\dfrac{16}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{28}{5}$**

**Detailed Solution:**

Let $x - 1 = t \Rightarrow dx = dt$

The given integral becomes:

$I = \int (2(t+1)+4) \sqrt{t} dt$

$I = \int (2t+6) t^{1/2} dt$

$I = \int (2t^{3/2} + 6t^{1/2}) dt$

$I = 2 \left(\dfrac{t^{5/2}}{5/2}\right) + 6 \left(\dfrac{t^{3/2}}{3/2}\right) + c$

$I = \dfrac{4}{5}t^{5/2} + 4t^{3/2} + c$

Substituting back $t = x-1$:

$I = \dfrac{4}{5}(x-1)^{5/2} + 4(x-1)^{3/2} + c$

Comparing with the given expression $a(x-1)^{5/2} + b(x-1)^{3/2} + c$, we get:

$a = \dfrac{4}{5}$ and $b = 4$

Therefore, the value of $2a + b$ is:

$2a + b = 2\left(\dfrac{4}{5}\right) + 4 = \dfrac{8}{5} + \dfrac{20}{5} = \dfrac{28}{5}$

Answer: $\dfrac{28}{5}$

</details>

---

### Q129. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \dfrac{\mathrm{d} x}{\cos ^3 x \sqrt{2 \sin 2 x}}=(\tan x)^{\mathrm{A}}+\mathrm{C}(\tan x)^{\mathrm{B}}+\mathrm{K}$, where K is a constant of integration, then the value of $5(\mathrm{~A}+\mathrm{B}+\mathrm{C})$ is equal to
[Note: The question has been modified to get the correct answer.]

**Options:**

- **(A)** 25
- **(B)** 14
- **(C)** 16
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 16**

**Detailed Solution:**

Let $I = \int \dfrac{\mathrm{d} x}{\cos^3 x \sqrt{2 \sin 2 x}}$

Using $\sin 2x = 2 \sin x \cos x$:

$I = \int \dfrac{\mathrm{d} x}{\cos^3 x \sqrt{4 \sin x \cos x}} = \int \dfrac{\mathrm{d} x}{2 \cos^3 x \sqrt{\sin x \cos x}}$

Dividing the numerator and the denominator by $\cos^4 x$:

$I = \int \dfrac{\sec^4 x}{2 \sqrt{\tan x}} \mathrm{d} x$

Substituting $\tan x = t \Rightarrow \sec^2 x \mathrm{d} x = \mathrm{d} t$:

$I = \int \dfrac{1 + t^2}{2 \sqrt{t}} \mathrm{d} t$

$I = \dfrac{1}{2} \int \left( t^{-1/2} + t^{3/2} \right) \mathrm{d} t$

$I = \dfrac{1}{2} \left( \dfrac{t^{1/2}}{1/2} + \dfrac{t^{5/2}}{5/2} \right) + K$

$I = t^{1/2} + \dfrac{1}{5} t^{5/2} + K$

Substituting $t = \tan x$:

$I = (\tan x)^{1/2} + \dfrac{1}{5} (\tan x)^{5/2} + K$

Comparing with $(\tan x)^A + C(\tan x)^B + K$:

$A = \dfrac{1}{2}$, $B = \dfrac{5}{2}$, $C = \dfrac{1}{5}$

$5(A + B + C) = 5 \left( \dfrac{1}{2} + \dfrac{5}{2} + \dfrac{1}{5} \right) = 5 \left( 3 + \dfrac{1}{5} \right) = 16$

Answer: 16

</details>

---

### Q130. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \dfrac{\log \sqrt{x}}{3 x} \mathrm{~d} x$ is equal to

**Options:**

- **(A)** $\dfrac{1}{3}(\log \sqrt{x})+\mathrm{c}$, (where c is a constant of integration)
- **(B)** $\dfrac{2}{3}(\log \sqrt{x})^2+\mathrm{c}$, (where c is a constant of integration)
- **(C)** $\dfrac{2}{3}(\log x)^2+\mathrm{c}$, (where c is a constant of integration)
- **(D)** $\dfrac{1}{12}(\log x)^2+\mathrm{c},($ where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{12}(\log x)^2+\mathrm{c},($ where c is a constant of integration)**

**Detailed Solution:**

Let $I = \int \dfrac{\log \sqrt{x}}{3 x} \mathrm{~d} x$

Using the property of logarithms, $\log \sqrt{x} = \dfrac{1}{2} \log x$.

Substituting this into the integral:

$I = \int \dfrac{\dfrac{1}{2} \log x}{3 x} \mathrm{~d} x = \dfrac{1}{6} \int \dfrac{\log x}{x} \mathrm{~d} x$

Let $\log x = t$, which gives $\dfrac{1}{x} \mathrm{~d} x = \mathrm{d} t$.

The integral becomes:

$I = \dfrac{1}{6} \int t \mathrm{~d} t$

$I = \dfrac{1}{6} \left( \dfrac{t^2}{2} \right) + \mathrm{c}$

$I = \dfrac{1}{12} t^2 + \mathrm{c}$

Substituting back $t = \log x$:

$I = \dfrac{1}{12} (\log x)^2 + \mathrm{c}$

Answer: $\dfrac{1}{12}(\log x)^2+\mathrm{c},($ where c is a constant of integration)

</details>

---

### Q131. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\mathrm{I}=\int \dfrac{\mathrm{d} x}{x^2\left(x^4+1\right)^{\dfrac{3}{4}}}$ is

**Options:**

- **(A)** $-\left(x^4+1\right)^{\dfrac{1}{4}}+\mathrm{c}$, (where c is a constant of integration)
- **(B)** $\left(x^4+1\right)^{\dfrac{1}{4}}+\mathrm{c}$, (where c is a constant of integration)
- **(C)** $\left(1+\dfrac{1}{x^4}\right)^{\dfrac{1}{4}}+\mathrm{c}$, (where c is a constant of integration)
- **(D)** $-\left(1+\dfrac{1}{x^4}\right)^{\dfrac{1}{4}}+\mathrm{c}$, (where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\left(1+\dfrac{1}{x^4}\right)^{\dfrac{1}{4}}+\mathrm{c}$, (where c is a constant of integration)**

**Detailed Solution:**

Given integral is $I = \int \dfrac{\mathrm{d} x}{x^2\left(x^4+1\right)^{\dfrac{3}{4}}}$

Taking $x^4$ common from the bracket in the denominator:

$I = \int \dfrac{\mathrm{d} x}{x^2 \cdot \left(x^4\right)^{\dfrac{3}{4}} \left(1+\dfrac{1}{x^4}\right)^{\dfrac{3}{4}}}$

$I = \int \dfrac{\mathrm{d} x}{x^5 \left(1+\dfrac{1}{x^4}\right)^{\dfrac{3}{4}}}$

$I = \int \dfrac{x^{-5} \mathrm{d} x}{\left(1+x^{-4}\right)^{\dfrac{3}{4}}}$

Let $1+x^{-4} = t$

Differentiating both sides with respect to $x$:

$-4x^{-5} \mathrm{d} x = \mathrm{d} t \Rightarrow x^{-5} \mathrm{d} x = -\dfrac{\mathrm{d} t}{4}$

Substituting this in the integral:

$I = \int \dfrac{-\dfrac{\mathrm{d} t}{4}}{t^{\dfrac{3}{4}}} = -\dfrac{1}{4} \int t^{-\dfrac{3}{4}} \mathrm{d} t$

$I = -\dfrac{1}{4} \left( \dfrac{t^{\dfrac{1}{4}}}{\dfrac{1}{4}} \right) + \mathrm{c}$

$I = -t^{\dfrac{1}{4}} + \mathrm{c}$

Substituting the value of $t$ back:

$I = -\left(1+\dfrac{1}{x^4}\right)^{\dfrac{1}{4}} + \mathrm{c}$

Answer: $-\left(1+\dfrac{1}{x^4}\right)^{\dfrac{1}{4}}+\mathrm{c}$, (where c is a constant of integration)

</details>

---

### Q132. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\int \dfrac{x+1}{\sqrt{2 x-1}} \mathrm{~d} x=\mathrm{f}(x) \sqrt{2 x-1}+\mathrm{c}$, (where c is a constant of integration), then $\mathrm{f}(x)$ is equal to

**Options:**

- **(A)** $\dfrac{1}{3}(x+1)$
- **(B)** $\dfrac{1}{3}(x+4)$
- **(C)** $\dfrac{2}{3}(x+2)$
- **(D)** $\dfrac{2}{3}(x-4)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{3}(x+4)$**

**Detailed Solution:**

Let $2x - 1 = t^2$. Differentiating both sides, we get $2 \mathrm{d}x = 2t \mathrm{d}t \Rightarrow \mathrm{d}x = t \mathrm{d}t$.

Also, $x = \dfrac{t^2 + 1}{2}$.

Substituting these into the integral:

$\int \dfrac{x+1}{\sqrt{2 x-1}} \mathrm{d} x = \int \dfrac{\dfrac{t^2 + 1}{2} + 1}{t} t \mathrm{d}t$

$= \int \left( \dfrac{t^2 + 3}{2} \right) \mathrm{d}t$

$= \dfrac{1}{2} \left( \dfrac{t^3}{3} + 3t \right) + \mathrm{c}$

$= \dfrac{t}{6} (t^2 + 9) + \mathrm{c}$

Substituting back $t = \sqrt{2x - 1}$ and $t^2 = 2x - 1$:

$= \dfrac{\sqrt{2x - 1}}{6} (2x - 1 + 9) + \mathrm{c}$

$= \dfrac{\sqrt{2x - 1}}{6} (2x + 8) + \mathrm{c}$

$= \dfrac{1}{3}(x + 4) \sqrt{2x - 1} + \mathrm{c}$

Comparing this with $\mathrm{f}(x) \sqrt{2 x-1}+\mathrm{c}$, we get:

$\mathrm{f}(x) = \dfrac{1}{3}(x + 4)$

Answer: $\dfrac{1}{3}(x+4)$

</details>

---

### Q133. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\quad \int 3^{3^x} \cdot 3^x d x=$

**Options:**

- **(A)** $\dfrac{3^x}{(\log 3)^2}+\mathrm{c}$, where c is a constant of integration.
- **(B)** $\dfrac{3^{3^x}}{\log 3}+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\dfrac{3^{3^x}}{(\log 3)^2}+\mathrm{c}$, where c is a constant of integration.
- **(D)** $\dfrac{3^x}{\log 3}+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{3^{3^x}}{(\log 3)^2}+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $I = \int 3^{3^x} \cdot 3^x dx$

Substitute $3^x = t$

Differentiating both sides with respect to $x$, we get:

$3^x \log 3 dx = dt$

$\Rightarrow 3^x dx = \dfrac{dt}{\log 3}$

Substituting this into the integral:

$I = \int 3^t \dfrac{dt}{\log 3}$

$I = \dfrac{1}{\log 3} \int 3^t dt$

$I = \dfrac{1}{\log 3} \left( \dfrac{3^t}{\log 3} \right) + c$

$I = \dfrac{3^t}{(\log 3)^2} + c$

Substituting back $t = 3^x$:

$I = \dfrac{3^{3^x}}{(\log 3)^2} + c$

Answer: $\dfrac{3^{3^x}}{(\log 3)^2}+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q134. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{I}=\int \frac{\mathrm{d} x}{\sin (x-\mathrm{a}) \sin (x-\mathrm{b})}$, then $\mathrm{I}$ is given by

**Options:**

- **(A)** $\frac{1}{\sin (\mathrm{b}-\mathrm{a})} \log |\sin (x-\mathrm{a}) \sin (x-\mathrm{b})|+\mathrm{c}$
where $\mathrm{c}$ is a constant of integration.
- **(B)** $\log \left|\frac{\sin (x-a)}{\sin (x-b)}\right|+c$, where $\mathrm{c}$ is a cónstant of integration.
- **(C)** $\frac{1}{\sin (\mathrm{b}-\mathrm{a})} \log \left|\frac{\sin (x-\mathrm{a})}{\sin (x-\mathrm{b})}\right|+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $\frac{1}{\sin (\mathrm{b}-\mathrm{a})} \log \left|\frac{\sin (x-\mathrm{b})}{\sin (x-\mathrm{a})}\right|+\mathrm{c}$, where $\mathrm{c}$ is $\mathrm{a}$ constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{\sin (\mathrm{b}-\mathrm{a})} \log \left|\frac{\sin (x-\mathrm{b})}{\sin (x-\mathrm{a})}\right|+\mathrm{c}$, where $\mathrm{c}$ is $\mathrm{a}$ constant of integration.**

**Detailed Solution:**

$\begin{aligned} & \mathrm{I}=\int \frac{\mathrm{d} x}{\sin (x-\mathrm{a}) \sin (x-\mathrm{b})} \\ & =\frac{1}{\sin (\mathrm{b}-\mathrm{a})} \int \frac{\sin \{(x-\mathrm{a})-(x-\mathrm{b})\}}{\sin (x-\mathrm{a}) \sin (x-\mathrm{b})} \mathrm{d} x \\ & =\frac{1}{\sin (\mathrm{b}-\mathrm{a})} \int \frac{1}{\sin (x-\mathrm{a}) \sin (x-\mathrm{b})}[\sin (x-\mathrm{a}) \cos (x-\mathrm{b}) \\ & =\frac{1}{\sin (\mathrm{b}-\mathrm{a})} \int[\cot (x-\mathrm{b})-\cot (x-\mathrm{a})] \mathrm{d} x \\ & =\frac{1}{\sin (\mathrm{b}-\mathrm{a})}[\log |\sin (x-\mathrm{b})|-\log |\sin (x-\mathrm{a})|]+\mathrm{c} \\ & =\frac{1}{\sin (\mathrm{b}-\mathrm{a})} \log \left|\frac{\sin (x-\mathrm{b})}{\sin (x-\mathrm{a}) \mid}\right|+\mathrm{c}\end{aligned}$

</details>

---

### Q135. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$$
\int \frac{\sin x+\sin ^3 x}{\cos 2 x} \mathrm{~d} x=\mathrm{A} \cos x+\mathrm{B} \log \mathrm{f}(x)+\mathrm{c}
$$
(where $\mathrm{c}$ is a constant of integration). Then values of A, B and $\mathrm{f}(x)$ are

**Options:**

- **(A)** $\mathrm{A}=\frac{1}{2}, \mathrm{~B}=\frac{-3}{4 \sqrt{2}}, \mathrm{f}(x)=\frac{\sqrt{2} \cos x-1}{\sqrt{2} \cos x+1}$
- **(B)** $A=-\frac{1}{2}, B=\frac{-3}{4 \sqrt{2}}, f(x)=\frac{\sqrt{2} \cos x+1}{\sqrt{2} \cos x-1}$
- **(C)** $\mathrm{A}=\frac{1}{2}, \mathrm{~B}=\frac{-3}{4 \sqrt{2}}, \mathrm{f}(x)=\frac{\sqrt{2} \cos x+1}{\sqrt{2} \cos x-1}$
- **(D)** $\mathrm{A}=\frac{3}{2}, \mathrm{~B}=\frac{1}{2}, \mathrm{f}(x)=\frac{\sqrt{2} \cos x-1}{\sqrt{2} \cos x+1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{A}=\frac{1}{2}, \mathrm{~B}=\frac{-3}{4 \sqrt{2}}, \mathrm{f}(x)=\frac{\sqrt{2} \cos x-1}{\sqrt{2} \cos x+1}$**

**Detailed Solution:**

$$
\text { Let } \begin{aligned}
\mathrm{I} & =\int \frac{\sin x+\sin ^3 x}{\cos 2 x} \mathrm{~d} x \\
& =\int \frac{\sin x\left(1+\sin ^2 x\right)}{\cos 2 x} \mathrm{~d} x \\
& =\int \frac{\sin x\left(1+1-\cos ^2 x\right)}{2 \cos ^2 x-1} \mathrm{~d} x \\
& =\int \frac{\sin x\left(2-\cos ^2 x\right)}{2 \cos ^2 x-1} \mathrm{~d} x
\end{aligned}
$$

Put $\cos x=\mathrm{t} \Rightarrow \sin x \mathrm{~d} x=-\mathrm{dt}$
$$
\therefore \quad \mathrm{I}=-\int \frac{2-\mathrm{t}^2}{2 \mathrm{t}^2-1} \mathrm{dt}
$$
$\begin{aligned} & =\int \frac{t^2-2}{2 t^2-1} d t \\ & =\frac{1}{2} \int \frac{2 t^2-4}{2 t^2-1} d t \\ & =\frac{1}{2} \int\left(1-\frac{3}{2 t^2-1}\right) d t \\ & =\frac{1}{2} \int d t-\frac{3}{2} \int \frac{d t}{(\sqrt{2} t)^2-1^2} \\ & =\frac{1}{2} t-\frac{3}{2} \cdot \frac{1}{\sqrt{2}} \cdot \frac{1}{2} \log \left|\frac{\sqrt{2} t-1}{\sqrt{2} t+1}\right|+c \\ & =\frac{1}{2} \cos x-\frac{3}{4 \sqrt{2}} \log \left|\frac{\sqrt{2} \cos x-1}{\sqrt{2} \cos x+1}\right|+\mathrm{c} \\ A \quad A & =\frac{1}{2}, \mathrm{~B}=\frac{-3}{4 \sqrt{2}}, \mathrm{f}(x)=\frac{\sqrt{2} \cos x-1}{\sqrt{2} \cos x+1}\end{aligned}$

</details>

---

### Q136. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{\sin 2 x\left(1-\frac{3}{2} \cos x\right)}{\mathrm{e}^{\sin ^2 x+\cos ^3 x}} \mathrm{~d} x=$

**Options:**

- **(A)** $\mathrm{e}^{\sin ^2 x+\cos ^3 x}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $-\mathrm{e}^{-\left(\sin ^2 x+\cos ^3 x\right)}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\mathrm{e}^{-\left(\sin ^2 x+\cos ^3 x\right)^2}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $\mathrm{e}^{\sin ^2 x+\cos x}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\mathrm{e}^{-\left(\sin ^2 x+\cos ^3 x\right)}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

$\begin{aligned} & \text { Put } \sin ^2 x+\cos ^3 x=\mathrm{t} \\ & \Rightarrow\left(2 \sin x \cos x-3 \cos ^2 x \sin x\right) \mathrm{d} x=\mathrm{dt} \\ & \Rightarrow\left(\sin 2 x-\frac{3}{2} \sin 2 x \cos x\right) \mathrm{d} x=\mathrm{dt} \\ & \Rightarrow \sin 2 x\left(1-\frac{3}{2} \cos x\right) \mathrm{d} x=\mathrm{dt} \\ \therefore \quad & \int \frac{\sin 2 x\left(1-\frac{3}{2} \cos x\right)}{\mathrm{d}} \mathrm{d} x \\ & =\int \frac{1}{\mathrm{e}^{\mathrm{t}}} \mathrm{dt}^2 x+\cos ^3 x \\ & =\int \mathrm{e}^{-\mathrm{t}} \mathrm{dt} \\ & =-\mathrm{e}^{-\mathrm{t}}+\mathrm{c} \\ & =-\mathrm{e}^{-\left(\sin ^2 x+\cos ^3 x\right)}+\mathrm{c}\end{aligned}$

</details>

---

### Q137. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{\log \left(\mathrm{t}+\sqrt{1+\mathrm{t}^2}\right)}{\sqrt{1+\mathrm{t}^2}} \mathrm{dt}=\frac{1}{2}[\mathrm{~g}(\mathrm{t})]^2+\mathrm{c}$, (where $\mathrm{c}$ is a constant of integration) then $g(2)$ is

**Options:**

- **(A)** $\frac{1}{\sqrt{5}} \log (2+\sqrt{5})$
- **(B)** $\frac{1}{2} \log (2+\sqrt{5})$
- **(C)** $2 \log (2+\sqrt{5})$
- **(D)** $\log (2+\sqrt{5})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log (2+\sqrt{5})$**

**Detailed Solution:**

Put $\log \left(\mathrm{t}+\sqrt{1+\mathrm{t}^2}\right)=y$
$\begin{aligned} & \Rightarrow\left[\frac{1}{\mathrm{t}+\sqrt{1+\mathrm{t}^2}}\left(1+\frac{\mathrm{t}}{\sqrt{1+\mathrm{t}^2}}\right)\right] \mathrm{dt}=\mathrm{d} y \\ & \Rightarrow \frac{1}{\sqrt{1+\mathrm{t}^2}} \mathrm{dt}=\mathrm{d} y\end{aligned}$
$\begin{aligned} \therefore \quad \int \frac{\log \left(\mathrm{t}+\sqrt{1+\mathrm{t}^2}\right)}{\sqrt{1+\mathrm{t}^2}} \mathrm{dt} & =\int y \mathrm{~d} y \\ & =\frac{y^2}{2}+\mathrm{c} \\ & =\frac{\left[\log \left(\mathrm{t}+\sqrt{1+\mathrm{t}^2}\right)\right]^2}{2}+\mathrm{c}\end{aligned}$
$\begin{aligned} \therefore \quad & g(t)=\log \left(t+\sqrt{1+t^2}\right) \\ \Rightarrow & g(2)=\log \left(2+\sqrt{1+2^2}\right)=\log (2+\sqrt{5})\end{aligned}$

</details>

---

### Q138. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{I}=\int \frac{\mathrm{e}^x}{\mathrm{e}^{4 x}+\mathrm{e}^{2 x}+1} \mathrm{~d} x$ and $\mathrm{J}=\int \frac{\mathrm{e}^{-x}}{\mathrm{e}^{-4 x}+\mathrm{e}^{-2 x}+1} \mathrm{~d} x$ then for any arbitrary constant c, the value of $\mathrm{J}-\mathrm{I}$ equals

**Options:**

- **(A)** $\frac{1}{2} \log \left|\left(\frac{\mathrm{e}^{4 x}-\mathrm{e}^{2 x}+1}{\mathrm{e}^{4 x}+\mathrm{e}^{2 x}+1}\right)\right| c$
- **(B)** $\frac{1}{2} \log \left|\left(\frac{\mathrm{e}^{2 x}+\mathrm{e}^x+1}{\mathrm{e}^{2 x}-\mathrm{e}^x+1}\right)\right|+\mathrm{c}$
- **(C)** $\frac{1}{2} \log \left|\left(\frac{\mathrm{e}^{2 x}-\mathrm{e}^x+1}{\mathrm{e}^{2 x}+\mathrm{e}^x+1}\right)\right|+\mathrm{c}$
- **(D)** $\quad \frac{1}{2} \log \left|\left(\frac{\mathrm{e}^{4 x}+\mathrm{e}^{2 x}+1}{\mathrm{e}^{4 x}-\mathrm{e}^{2 x}+1}\right)\right|+\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2} \log \left|\left(\frac{\mathrm{e}^{2 x}-\mathrm{e}^x+1}{\mathrm{e}^{2 x}+\mathrm{e}^x+1}\right)\right|+\mathrm{c}$**

**Detailed Solution:**

$\begin{aligned} \mathrm{J}-\mathrm{I} & =\int\left(\frac{\mathrm{e}^{-x}}{\mathrm{e}^{-4 x}+\mathrm{e}^{-2 x}+1}-\frac{\mathrm{e}^x}{\mathrm{e}^{4 x}+\mathrm{e}^{2 x}+1}\right) \mathrm{d} x \\ & =\int\left(\frac{\mathrm{e}^{3 x}}{\mathrm{e}^{4 x}+\mathrm{e}^{2 x}+1}-\frac{\mathrm{e}^x}{\mathrm{e}^{4 x}+\mathrm{e}^{2 x}+1}\right) \mathrm{d} x \\ & =\int \frac{\left(\mathrm{e}^{2 x}-1\right) \mathrm{e}^x}{\mathrm{e}^{4 x}+\mathrm{e}^{2 x}+1} \mathrm{~d} x\end{aligned}$
Put $\mathrm{e}^x=\mathrm{t} \Rightarrow \mathrm{e}^x \mathrm{~d} x=\mathrm{dt}$
$\therefore \quad \mathrm{J}-\mathrm{I}=\int \frac{\mathrm{t}^2-1}{\mathrm{t}^4+\mathrm{t}^2+1} \mathrm{dt}=\int \frac{1-\frac{1}{\mathrm{t}^2}}{\left(\mathrm{t}+\frac{1}{\mathrm{t}}\right)^2-1} \mathrm{dt}$
Put $\mathrm{t}+\frac{1}{\mathrm{t}}=y$
$\Rightarrow\left(1-\frac{1}{\mathrm{t}^2}\right) \mathrm{dt}=\mathrm{d} y$
$\therefore \quad \mathrm{J}-\mathrm{I}=\int \frac{\mathrm{d} y}{y^2-1^2}=\frac{1}{2} \log \left|\frac{y-1}{y+1}\right|+\mathrm{c}$
$\begin{aligned} & =\frac{1}{2} \log \left|\frac{\mathrm{t}+\frac{1}{\mathrm{t}}-1}{\mathrm{t}+\frac{1}{\mathrm{t}}+1}\right|+\mathrm{c} \\ & =\frac{1}{2} \log \left|\frac{\mathrm{t}^2-\mathrm{t}+1}{\mathrm{t}^2+\mathrm{t}+1}\right|+\mathrm{c} \\ & =\frac{1}{2} \log \left|\frac{\mathrm{e}^{2 x}-\mathrm{e}^x+1}{\mathrm{e}^{2 x}+\mathrm{e}^x+1}\right|+\mathrm{c}\end{aligned}$

</details>

---

### Q139. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{2+\cos \frac{x}{2}}{x+\sin \frac{x}{2}} \mathrm{~d} x=$

**Options:**

- **(A)** $2 \log \left(x+\sin \frac{x}{2}\right)+\mathrm{c}$, where c is a constant of integration.
- **(B)** $\frac{1}{2} \log \left(x+\sin \frac{x}{2}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $4 \log \left(x+\sin \frac{x}{2}\right)+c$, where c is a constant of integration.
- **(D)** $\log \left(x+\sin \frac{x}{2}\right)+c$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \log \left(x+\sin \frac{x}{2}\right)+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

$\begin{aligned} & \text { Put } x+\sin \frac{x}{2}=\mathrm{t} \\ & \Rightarrow\left[1+\left(\cos \frac{x}{2}\right) \frac{1}{2}\right] \mathrm{d} x=\mathrm{dt} \\ & \Rightarrow\left(2+\cos \frac{x}{2}\right) \mathrm{d} x=2 \mathrm{dt}\end{aligned}$
$\therefore \quad \int \frac{2+\cos \frac{x}{2}}{x+\sin \frac{x}{2}} \mathrm{~d} x=2 \int \frac{\mathrm{dt}}{\mathrm{t}}$
$\begin{aligned} & =2 \log |t|+c \\ & =2 \log \left|x+\sin \frac{x}{2}\right|+c\end{aligned}$

</details>

---

### Q140. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{f}(x)=\int \frac{x^2 \mathrm{~d} x}{\left(1+x^2\right)\left(1+\sqrt{1+x^2}\right)}$ and $\mathrm{f}(0)=0$, then $f(1)$ is

**Options:**

- **(A)** $\log (1+\sqrt{2})$
- **(B)** $\log (1+\sqrt{2})-\frac{\pi}{4}$
- **(C)** $\log (1+\sqrt{2})+\frac{\pi}{4}$
- **(D)** $\log (1-\sqrt{2})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log (1+\sqrt{2})-\frac{\pi}{4}$**

**Detailed Solution:**

$\begin{aligned} \text { Put } & x=\tan \theta \Rightarrow \mathrm{d} x=\sec ^2 \theta \mathrm{d} \theta \\ \therefore \quad \mathrm{f}(x) & =\int \frac{\tan ^2 \theta \sec ^2 \theta \mathrm{d} \theta}{\sec ^2 \theta(1+\sec \theta)} \\ & =\int \frac{\tan ^2 \theta \mathrm{d} \theta}{1+\sec \theta} \\ & =\int \frac{\sin ^2 \theta \mathrm{d} \theta}{\cos \theta(1+\cos \theta)} \\ & =\int \frac{1-\cos ^2 \theta \mathrm{d} \theta}{\cos \theta(1+\cos \theta)} \\ & =\int \frac{(1-\cos \theta) \mathrm{d} \theta}{\cos \theta} \\ & =\int \sec \theta \mathrm{d} \theta-\int \mathrm{d} \theta \\ & =\log |\sec \theta+\tan \theta|-\theta+\mathrm{c} \\ \mathrm{f}(x) & =\log \left|x+\sqrt{1+x^2}\right|-\tan ^{-1} x+\mathrm{c} \\ \therefore \quad \mathrm{f}(0) & =\log |0+\sqrt{1+0}|-\tan ^{-1}(0)+\mathrm{c} \\ \Rightarrow 0 & =\log 1-0+\mathrm{c} \Rightarrow \mathrm{c}=0 \\ \therefore \quad \mathrm{f}(x) & =\log \left|x+\sqrt{1+x^2}\right|-\tan ^{-1} x \\ \therefore \quad \mathrm{f}(1) & =\log \left|1+\sqrt{1+1^2}\right|-\tan ^{-1}(1) \\ \therefore \quad & \log (1+\sqrt{2})-\frac{\pi}{4}\end{aligned}$

</details>

---

### Q141. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int x^5 \mathrm{e}^{-4 x^3} \mathrm{~d} x=\frac{1}{48} \mathrm{e}^{-4 x^3} \mathrm{f}(x)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration, then $\mathrm{f}(x)$ is given by

**Options:**

- **(A)** $4 x^3+1$
- **(B)** $-4 x^3-1$
- **(C)** $-2 x^3-1$
- **(D)** $-2 x^3+1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-4 x^3-1$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \mathrm{I}=\int x^5 \mathrm{e}^{-4 x^3} \mathrm{~d} x \\ & \begin{aligned} \text { Put } x^3=\mathrm{t} \Rightarrow 3 x^2 \mathrm{~d} x & =\mathrm{dt} \\ \therefore \quad \mathrm{I}=\frac{1}{3} \int \mathrm{te}^{-4 \mathrm{t}} \mathrm{dt} & =\frac{1}{3}\left(\mathrm{t} \cdot \frac{\mathrm{e}^{-4 \mathrm{t}}}{-4}-\int 1 \cdot \frac{\mathrm{e}^{-4 \mathrm{t}}}{-4} \mathrm{dt}\right) \\ & =\frac{1}{3}\left(\frac{-\mathrm{te}^{-4 \mathrm{t}}}{4}+\frac{1}{4} \cdot \frac{\mathrm{e}^{-4 \mathrm{t}}}{-4}\right)+\mathrm{c} \\ & =\frac{1}{48} \mathrm{e}^{-4 \mathrm{t}}(-4 \mathrm{t}-1)+\mathrm{c} \\ & =\frac{1}{48} \mathrm{e}^{-4 x^3}\left(-4 x^3-1\right)+\mathrm{c}\end{aligned}\end{aligned}$
$\therefore \quad \mathrm{f}(x)=-4 x^3-1$

</details>

---

### Q142. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$$
\int \frac{\log \left(x^2+\mathrm{a}^2\right)}{x^2} \mathrm{~d} x=
$$

**Options:**

- **(A)** $\frac{-\log \left(x^2+\mathrm{a}^2\right)}{x}+\frac{1}{\mathrm{a}} \tan ^{-1} \frac{x}{\mathrm{a}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\frac{-\log \left(x^2+\mathrm{a}^2\right)}{x}+\frac{2}{\mathrm{a}} \tan ^{-1} \frac{x}{\mathrm{a}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\frac{\log \left(x^2+\mathrm{a}^2\right)}{x^2}-\frac{1}{\mathrm{a}} \tan ^{-1} \frac{x}{\mathrm{a}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $\frac{\log \left(x^2+\mathrm{a}^2\right)}{x^2}-\frac{2}{\mathrm{a}} \tan ^{-1} \frac{x}{\mathrm{a}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-\log \left(x^2+\mathrm{a}^2\right)}{x}+\frac{2}{\mathrm{a}} \tan ^{-1} \frac{x}{\mathrm{a}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

Let $\begin{aligned} \mathrm{I} & =\int \frac{\log \left(x^2+\mathrm{a}^2\right)}{x^2} \mathrm{~d} x \\ & =\int \log \left(x^2+\mathrm{a}^2\right) \cdot x^{-2} \mathrm{~d} x \\ & =\log \left(x^2+\mathrm{a}^2\right) \int x^{-2} \mathrm{~d} x \\ & \quad-\int\left\{\frac{\mathrm{d}}{\mathrm{d} x}\left[\log \left(x^2+\mathrm{a}^2\right)\right] \int x^{-2} \mathrm{~d} x\right\} \mathrm{d} x \\ & =\log \left(x^2+\mathrm{a}^2\right) \cdot\left(-\frac{1}{x}\right)-\int \frac{2 x}{x^2+\mathrm{a}^2} \cdot\left(-\frac{1}{x}\right) \mathrm{d} x \\ & =-\frac{\log \left(x^2+\mathrm{a}^2\right)}{x}+2 \int \frac{1}{x^2+\mathrm{a}^2} \mathrm{~d} x \\ & =-\frac{\log \left(x^2+\mathrm{a}^2\right)}{x}+\frac{2}{\mathrm{a}} \tan ^{-1}\left(\frac{x}{\mathrm{a}}\right)+\mathrm{c}\end{aligned}$

</details>

---

### Q143. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int\left(\frac{\tan \left(\frac{1}{x}\right)}{x}\right)^2 \mathrm{~d} x=$

**Options:**

- **(A)** $x-\tan x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration
- **(B)** $\frac{1}{x}-\tan \left(\frac{1}{x}\right)+c$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\frac{1}{x}+\tan \left(\frac{1}{x}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $x+\tan x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{x}-\tan \left(\frac{1}{x}\right)+c$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

Let $\mathrm{I}=\int\left(\frac{\tan \left(\frac{1}{x}\right)}{x}\right)^2 \mathrm{~d} x$
Let $\frac{1}{x}=\mathrm{t} \Rightarrow \frac{1}{x^2} \mathrm{~d} x=-\mathrm{dt}$
$$
\begin{aligned}
\therefore \quad \mathrm{I} & =-\int \tan ^2 \mathrm{t} d \mathrm{t} \\
& =\int\left(1-\sec ^2 \mathrm{t}\right) \mathrm{dt} \\
& =\mathrm{t}-\tan \mathrm{t}+\mathrm{c} \\
& =\frac{1}{x}-\tan \left(\frac{1}{x}\right)+\mathrm{c}
\end{aligned}
$$

</details>

---

### Q144. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{1}{\cos ^3 x \sqrt{\sin 2 x}} \mathrm{~d} x=$

**Options:**

- **(A)** $\sqrt{2}\left(\sqrt{\tan x}+\frac{1}{5}(\tan x)^{\frac{5}{2}}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\left(\sqrt{\tan x}+\frac{2}{5}(\tan x)^{\frac{5}{2}}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\frac{1}{\sqrt{2}}\left(\sqrt{\tan x}+\frac{2}{5}(\tan x)^{\frac{5}{2}}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $2\left(\sqrt{\tan x}+\frac{1}{5}(\tan x)^{\frac{5}{2}}\right)+c$, where $c$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{2}\left(\sqrt{\tan x}+\frac{1}{5}(\tan x)^{\frac{5}{2}}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

$$
\text { Let } \begin{aligned}
\mathrm{I} & =\int \frac{1}{\cos ^3 x \sqrt{\sin 2 x}} \mathrm{~d} x \\
& =\frac{1}{\sqrt{2}} \int \frac{\sec ^3 x}{\sqrt{\sin x \cos x}} \mathrm{~d} \\
& =\frac{1}{\sqrt{2}} \int \frac{\sec ^4 x}{\sqrt{\tan x}} \mathrm{~d} x
\end{aligned}
$$

Let $\tan x=\mathrm{t} \Rightarrow \sec ^2 x=\mathrm{dt}$
$$
\begin{aligned}
\therefore \quad I & =\frac{1}{\sqrt{2}} \int \frac{1+t^2}{\sqrt{t}} d t \\
& =\frac{1}{\sqrt{2}} \int t^{-\frac{1}{2}} d t+\frac{1}{\sqrt{2}} \int t^{\frac{3}{2}} d t \\
& =\frac{1}{\sqrt{2}}\left(\frac{t^{\frac{1}{2}}}{\frac{1}{2}}\right)+\frac{1}{\sqrt{2}}\left(\frac{t^{\frac{5}{2}}}{\frac{5}{2}}\right)+\mathrm{c} \\
& =\sqrt{2}\left(\sqrt{\tan x}+\frac{1}{5}(\tan x)^{\frac{5}{2}}\right)+\mathrm{c}
\end{aligned}
$$

</details>

---

### Q145. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The integral $\int \frac{\sin ^2 x \cos ^2 x}{\left(\sin ^5 x+\cos ^3 x \sin ^2 x+\sin ^3 x \cos ^2 x+\cos ^5 x\right)^2} \mathrm{~d} x$ is equal to

**Options:**

- **(A)** $\frac{1}{3\left(1+\tan ^3 x\right)}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\frac{-1}{3\left(1+\tan ^3 x\right)}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\frac{1}{1+\cot ^3 x}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $\frac{-1}{1+\cos ^3 x}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-1}{3\left(1+\tan ^3 x\right)}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

Let
$$
\begin{aligned}
\mathrm{I} & =\int \frac{\sin ^2 x \cos ^2 x}{\left(\sin ^5 x+\cos ^3 x \sin ^2 x+\sin ^3 x \cos ^2 x+\cos ^5 x\right)^2} \mathrm{~d} x \\
& =\int \frac{\sin ^2 x \cos ^2 x}{\left(\sin ^5 x+\sin ^3 x \cos ^2 x+\cos ^5 x \sin ^2 x+\cos ^5 x\right)^2} \mathrm{~d} x \\
& =\int \frac{\sin ^2 x \cos ^2 x}{\left[\sin ^3 x\left(\sin ^2 x+\cos ^2 x\right)+\cos ^3 x\left(\sin ^2 x+\cos ^2 x\right)\right]^2} \mathrm{~d} x \\
& =\int \frac{\sin ^2 x \cos ^2 x}{\left(\sin ^3 x+\cos ^3 x\right)^2} \mathrm{~d} x \\
& =\int \frac{\sec ^2 x \tan ^2 x}{\left(1+\tan ^3 x\right)^2} \mathrm{~d} x
\end{aligned}
$$
[Dividing numerator and denominator by $\cos ^6 x$ ]
Let $1+\tan ^3 x=t$
Differentiating w.r.t. $x$, we get
$$
\begin{aligned}
& 3 \tan ^2 x \sec ^2 x \mathrm{~d} x=\mathrm{dt} \\
& \tan ^2 x \sec ^2 x \mathrm{~d} x=\frac{1}{3} \mathrm{dt}
\end{aligned}
$$
$$
\therefore \quad \tan ^2 x \sec ^2 x \mathrm{~d} x=\frac{1}{3} \mathrm{dt}
$$
$$
\begin{aligned}
\therefore \quad \mathrm{I} & =\frac{1}{3} \int \frac{1}{\mathrm{t}^2} \mathrm{dt} \\
& =\frac{-1}{3 \mathrm{t}}+\mathrm{c} \\
& =\frac{-1}{3\left(1+\tan ^3 x\right)}+\mathrm{c}
\end{aligned}
$$

</details>

---

### Q146. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$$
\int \frac{\operatorname{cosec} x \mathrm{~d} x}{\cos ^2\left(1+\log \tan \frac{x}{2}\right)}=
$$

**Options:**

- **(A)** $\tan \left(1+\log \left(\tan \frac{x}{2}\right)\right)+\mathrm{c}$, where $\mathrm{c}$ is constant of integration
- **(B)** $\tan (1+\log (\tan x))+\mathrm{c}$, where $\mathrm{c}$ is constant of integration
- **(C)** $\tan \left(\log \left(\tan \frac{x}{2}\right)\right)+\mathrm{c}$, where c is constant of integration.
- **(D)** $\tan \left(\tan \frac{x}{2}\right)+c$, where c is constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\tan \left(1+\log \left(\tan \frac{x}{2}\right)\right)+\mathrm{c}$, where $\mathrm{c}$ is constant of integration**

**Detailed Solution:**

Let $\mathrm{I}=\int \frac{\operatorname{cosec} x \mathrm{~d} x}{\cos ^2\left(1+\log \tan \frac{x}{2}\right)} \mathrm{d} x$
Let $1+\log \left(\tan \frac{x}{2}\right)=\mathrm{t}$
Differentiating both sides w.r.t. t, we get
$$
\begin{aligned}
& \frac{1}{\tan \frac{x}{2}} \sec ^2 \frac{x}{2} \times \frac{1}{2} \mathrm{~d} x=\mathrm{dt} \\
& \therefore \quad \frac{1}{2 \sin \frac{x}{2} \cos \frac{x}{2}} \mathrm{~d} x=\mathrm{dt} \\
& \therefore \quad \operatorname{cosec} x \mathrm{~d} x=\mathrm{dt} \\
& \therefore \quad \mathrm{I}=\int \frac{1}{\cos ^2 \mathrm{t}} \mathrm{dt}=\int \sec ^2 \mathrm{t} d \mathrm{t} \\
& =\tan (\mathrm{t})+\mathrm{c} \\
& =\tan \left(1+\log \left(\tan \frac{x}{2}\right)\right)+c \\
&
\end{aligned}
$$

</details>

---

### Q147. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int(1-\cos x) \cdot \operatorname{cosec}^2 x \mathrm{~d} x$ is

**Options:**

- **(A)** $\frac{1}{2} \tan \frac{x}{2}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\tan \frac{x}{2}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $2 \cot \frac{x}{2}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $\cot \frac{x}{2}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\tan \frac{x}{2}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

Let $\mathrm{I}=\int(1-\cos x) \cdot \operatorname{cosec}^2 \mathrm{~d} x$
$=\int \frac{2 \sin ^2 \frac{x}{2}}{[\sin x]^2} \mathrm{~d} x \quad \ldots\left[\because 1-\cos \theta=2 \sin ^2 \frac{\theta}{2}\right]$
$\begin{aligned} &=\int \frac{2 \sin ^2 \frac{x}{2}}{\left[2 \sin \frac{x}{2} \cos \frac{x}{2}\right]^2} \mathrm{~d} x \\ & \ldots\left[\because \sin \theta=2 \sin \frac{\theta}{2} \cos \frac{\theta}{2}\right]\end{aligned}$
$\begin{aligned}
& =\frac{1}{2} \int \sec ^2 \frac{x}{2} \mathrm{~d} x \\
& =\tan \frac{x}{2}+\mathrm{c}
\end{aligned}$

</details>

---

### Q148. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \frac{\cos 8 x+1}{\cot 2 x-\tan 2 x} \mathrm{~d} x=\mathrm{A} \cos 8 x+\mathrm{c}$, where $\mathrm{c}$ is an arbitrary constant, then the value of $\mathrm{A}$ is

**Options:**

- **(A)** $\frac{1}{16}$
- **(B)** $\frac{1}{8}$
- **(C)** $\frac{-1}{8}$
- **(D)** $\frac{-1}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{-1}{16}$**

**Detailed Solution:**

$\begin{aligned} I & =\int \frac{\cos 8 x+1}{\cot 2 x-\tan 2 x} d x \\ & =\int \frac{2 \cos ^2\left(\frac{8 x}{2}\right)}{\frac{\cos 2 x}{\sin 2 x}-\frac{\sin 2 x}{\cos 2 x}} d x\end{aligned}$
$\ldots\left[\because 1+\cos \theta=2 \cos ^2 \frac{\theta}{2}\right]$
$\begin{aligned}
& =\int \frac{2 \cos ^2(4 x) \times \sin 2 x \times \cos 2 x}{\cos ^2 2 x-\sin ^2 2 x} \mathrm{~d} x \\
& =\int \frac{\cos ^2(4 x) \sin (4 x)}{\cos (4 x)} \mathrm{d} x \\
& \quad \cdots\left[\begin{array}{r}
\because \sin 2 \theta=2 \sin \theta \cos \theta \text { and } \\
\cos 2 \theta=\cos ^2 \theta-\sin ^2 \theta
\end{array}\right]
\end{aligned}$
$\begin{aligned}
& =\frac{1}{2} \int 2 \sin (4 x) \cos (4 x) \mathrm{d} x \\
& =\frac{1}{2} \int \sin 8 x \mathrm{~d} x \\
& =\frac{-\cos 8 x}{2 \times 8}+c \\
& =\frac{-\cos 8 x}{16}+c
\end{aligned}$
Comparing with ' $\mathrm{A} \cos 8 x+\mathrm{c}$ ', we get $\mathrm{A}=\frac{-1}{16}$

</details>

---

### Q149. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int x \sqrt{\frac{2 \sin \left(x^2+1\right)-\sin 2\left(x^2+1\right)}{2 \sin \left(x^2+1\right)+\sin 2\left(x^2+1\right)}} \mathrm{d} x=$

**Options:**

- **(A)** $\log \left(\sec \left(\frac{x^2+1}{2}\right)\right)+\mathrm{c}$, where $\mathrm{c}$ is $\mathrm{a}$ constant of integration.
- **(B)** $\log \left(\frac{x^2+1}{2}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\log \left(\sin \left(\frac{x^2+1}{2}\right)\right)+\mathrm{c}$, where $\mathrm{c}$ is $\mathrm{a}$ constant of integration.
- **(D)** $2 \log \left(x^2+1\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\log \left(\sec \left(\frac{x^2+1}{2}\right)\right)+\mathrm{c}$, where $\mathrm{c}$ is $\mathrm{a}$ constant of integration.**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \mathrm{I}=\int x \sqrt{\frac{2 \sin \left(x^2+1\right)-\sin 2\left(x^2+1\right)}{2 \sin \left(x^2+1\right)+\sin 2\left(x^2+1\right)}} \mathrm{d} x \\ & =\int x \sqrt{\frac{2 \sin \left(x^2+1\right)-2 \sin \left(x^2+1\right) \cos \left(x^2+1\right)}{2 \sin x\left(x^2+1\right)+2 \sin \left(x^2+1\right) \cos \left(x^2+1\right)}} \mathrm{d} x \\ & =\int x \sqrt{\frac{1-\cos \left(x^2+1\right)}{1+\cos \left(x^2+1\right)}} d x \\ & =\int x \sqrt{\frac{2 \sin ^2\left(\frac{x^2+1}{2}\right)}{2 \cos ^2\left(\frac{x^2+1}{2}\right)}} d x \\ & =\int x \tan \left(\frac{x^2+1}{2}\right) \mathrm{d} x \\ & \text { Let }\left(\frac{x^2+1}{2}\right)=\mathrm{t} \Rightarrow x \mathrm{~d} x=\mathrm{dt} \\ & \therefore \quad \mathrm{I}=\int \tan \mathrm{t} d \mathrm{t} \\ & =\log (\sec \mathrm{t})+\mathrm{c} \\ & =\log \left(\sec \left(\frac{x^2+1}{2}\right)\right)+\mathrm{c} \\ & \end{aligned}$

</details>

---

### Q150. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{\log (\cot x)}{\sin 2 x} \mathrm{~d} x=$

**Options:**

- **(A)** $-\log (\cot x)^2+c$, where $c$ is constant of integration.
- **(B)** $2(\log (\cot x))^2+c$, where $\mathrm{c}$ is constant of integration.
- **(C)** $\frac{-1}{4}(\log (\sin x))^2+c$, where $\mathrm{c}$ is constant of integration.
- **(D)** $\frac{-1}{4}(\log (\cot x))^2+c$, where $c$ is constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{-1}{4}(\log (\cot x))^2+c$, where $c$ is constant of integration.**

**Detailed Solution:**

Let $\mathrm{I}=\int \frac{\log (\cot x)}{\sin 2 x} \mathrm{~d} x$
Put $\log (\cot x)=\mathrm{t}$
$$
\begin{aligned}
& \Rightarrow\left[\frac{1}{\cot x} \cdot\left(-\operatorname{cosec}^2 x\right)\right] \mathrm{d} x=\mathrm{dt} \\
& \Rightarrow\left[\frac{-\sin x}{\sin ^2 x \cdot \cos x}\right] \mathrm{d} x=\mathrm{dt} \\
& \Rightarrow \frac{\mathrm{d} x}{\sin 2 x}=\frac{-\mathrm{dt}}{2} \\
\therefore \quad \mathrm{I} & =\int \mathrm{t} \cdot\left(-\frac{\mathrm{dt}}{2}\right) \\
& =\frac{-1}{4} \mathrm{t}^2+\mathrm{c} \\
& =\frac{-1}{4}[\log (\cot x)]^2+\mathrm{c}
\end{aligned}
$$

</details>

---

### Q151. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{\mathrm{d} x}{x \sqrt{1-x^3}}=\mathrm{k} \log \left(\frac{\sqrt{1-x^3}-1}{\sqrt{1-x^3}+1}\right)+\mathrm{c},($ where $\mathrm{c}$ is a constant of integration), then value of $\mathrm{k}$ is

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $-\frac{2}{3}$
- **(C)** $\frac{1}{3}$
- **(D)** $-\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{3}$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \mathrm{I}=\int \frac{\mathrm{d} x}{x \sqrt{1-x^3}} \\ & =\int \frac{x^2 \mathrm{~d} x}{x^3 \sqrt{1-x^3}} \mathrm{~d} x \\ & \text { Put } 1-x^3=\mathrm{t}^2 \\ & \Rightarrow-3 x^2 \mathrm{~d} x=2 \mathrm{tdt} \\ & \Rightarrow x^2 \mathrm{~d} x=\frac{-2 \mathrm{tdt}}{3} \\ & \end{aligned}$
$\begin{aligned} \therefore \quad \mathrm{I} & =\int \frac{-\left(\frac{2 \mathrm{tdt}}{3}\right)}{\left(1-\mathrm{t}^2\right) \mathrm{t}} \\ & =-\frac{2}{3} \int \frac{1}{1-\mathrm{t}^2} \mathrm{dt} \\ & =\frac{2}{3} \int \frac{1}{\mathrm{t}^2-1} \mathrm{dt} \\ & =\frac{2}{3} \times \frac{1}{2} \cdot \log \left|\frac{\mathrm{t}-1}{\mathrm{t}+1}\right|+\mathrm{c} \\ & =\frac{1}{3} \log \left|\frac{\sqrt{1-x^3}-1}{\sqrt{1-x^3}+1}\right|+\mathrm{c} \\ \therefore \quad \mathrm{k} & =\frac{1}{3}\end{aligned}$

</details>

---

### Q152. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{\mathrm{e}^x(1+x)}{\cos ^2\left(\mathrm{e}^x \cdot x\right)} \mathrm{d} x=$

**Options:**

- **(A)** $-\cot \left(e^x\right)+c$, where $c$ is a constant of integration.
- **(B)** $\tan \left(x \cdot \mathrm{e}^x\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\tan \left(\mathrm{e}^x\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $-\cot \left(x \cdot \mathrm{e}^x\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\tan \left(x \cdot \mathrm{e}^x\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

Let $\mathrm{I}=\int \frac{\mathrm{e}^x(1+x)}{\cos ^2\left(\mathrm{e}^x \cdot x\right)} \mathrm{d} x$
Put $\mathrm{e}^x \cdot x=\mathrm{t} \Rightarrow \mathrm{e}^x(x+1) \mathrm{d} x=\mathrm{dt}$
$$
\begin{aligned}
\mathrm{I} & =\int \frac{\mathrm{dt}}{\cos ^2 \mathrm{t}} \\
& =\int \sec ^2 \mathrm{t} d \\
& =\tan \mathrm{t}+\mathrm{c} \\
\therefore \quad \mathrm{I} & =\tan \left(x \cdot \mathrm{e}^x\right)+\mathrm{c}
\end{aligned}
$$

</details>

---

### Q153. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{f}(x)=\int \frac{\sqrt{x}}{(1+x)^2} \mathrm{~d} x, x \geq 0$, then $\mathrm{f}(3)-\mathrm{f}(1)$ is equal to

**Options:**

- **(A)** $-\frac{\pi}{6}+\frac{1}{2}+\frac{\sqrt{3}}{4}$
- **(B)** $-\frac{\pi}{12}+\frac{1}{2}+\frac{\sqrt{3}}{4}$
- **(C)** $\frac{\pi}{6}+\frac{1}{2}-\frac{\sqrt{3}}{4}$
- **(D)** $\frac{\pi}{6}+\frac{1}{2}-\frac{\sqrt{3}}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{6}+\frac{1}{2}-\frac{\sqrt{3}}{4}$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{f}(x)=\int \frac{\sqrt{x}}{(1+x)^2} \mathrm{~d} x, x \geq 0 \\
& \mathrm{f}(3)-\mathrm{f}(1)=\int_1^3 \frac{\sqrt{x}}{(1+x)^2} \mathrm{~d} x=\mathrm{I}(\text { say })
\end{aligned}
$$

Put $\sqrt{x}=\tan \theta \Rightarrow \mathrm{d} x=2 \tan \theta \sec ^2 \theta \mathrm{d} \theta$
When $x=1, \theta=\frac{\pi}{4}$ and when $x=3, \theta=\frac{\pi}{3}$
$$
\begin{aligned}
\therefore \quad I & =\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \frac{2 \tan ^2 \theta \sec ^2 \theta}{\left(1+\tan ^2 \theta\right)^2} d \theta \\
& =\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \frac{2 \tan ^2 \theta}{1+\tan ^2 \theta} d \theta \\
& =\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \frac{2 \sin ^2 \theta+\cos ^2 \theta}{} d \theta \\
& =\int_{\frac{\pi}{4}}^{\frac{\pi}{3}}(1-\cos 2 \theta) \mathrm{d} \theta \\
& =\left[\theta-\frac{\sin 2 \theta}{2}\right]_{\frac{\pi}{4}}^{\frac{\pi}{3}} \\
& =\left(\frac{\pi}{3}-\frac{\pi}{4}\right)-\frac{1}{2}\left(\frac{\sqrt{3}}{2}-1\right) \\
& =\frac{\pi}{12}-\frac{\sqrt{3}}{4}+\frac{1}{2}
\end{aligned}
$$

</details>

---

### Q154. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int \frac{\left(x^2-1\right) \mathrm{d} x}{x^3 \sqrt{2 x^4-2 x^2+1}}$ is

**Options:**

- **(A)** $2 \sqrt{2-\frac{2}{x^2}+\frac{1}{x^4}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $2 \sqrt{2+\frac{2}{x^2}+\frac{1}{x^4}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\frac{1}{2} \sqrt{2-\frac{2}{x^2}+\frac{1}{x^4}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $2 \sqrt{2-\frac{2}{x^2}-\frac{1}{x^4}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2} \sqrt{2-\frac{2}{x^2}+\frac{1}{x^4}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \mathrm{I}=\int \frac{\left(x^2-1\right) \mathrm{d} x}{x^3 \sqrt{2 x^4-2 x^2+1}} \\ & =\int \frac{\left(x^2-1\right) \mathrm{d} x}{x^3 \cdot x^2 \sqrt{\left(2-\frac{2}{x^2}+\frac{1}{x^4}\right)}} \\ & =\int \frac{\left(\frac{x^2-1}{x^5}\right) \mathrm{d} x}{\sqrt{2-\frac{2}{x^2}+\frac{1}{x^4}}} \\ & \text { Put } 2-\frac{2}{x^2}+\frac{1}{x^4}=\mathrm{t} \\ & \Rightarrow\left(\frac{4}{x^3}-\frac{4}{x^5}\right) \mathrm{d} x=\mathrm{dt} \\ & \Rightarrow \frac{x^2-1}{x^5} \mathrm{~d} x=\frac{\mathrm{dt}}{4} \\ & \therefore \quad I=\int \frac{\frac{d t}{4}}{\sqrt{t}} \\ & =\frac{1}{4} \int \mathrm{t}^{\frac{-1}{2}} \mathrm{dt} \\ & =\frac{1}{4} \cdot \frac{\mathrm{t}^{\frac{1}{2}}}{\frac{1}{2}}+\mathrm{c} \\ & \therefore \quad \mathrm{I}=\frac{1}{2} \sqrt{2-\frac{2}{x^2}+\frac{1}{x^4}}+\mathrm{c} \\ & \end{aligned}$

</details>

---

### Q155. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{5 \tan x}{\tan x-2} \mathrm{~d} x=x+\mathrm{a} \log |\sin x-2 \cos x|+\mathrm{c}$
(where $\mathrm{c}$ is a constant of integration), then the value of $a$ is

**Options:**

- **(A)** $1$
- **(B)** $\frac{1}{2}$
- **(C)** $2$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2$**

**Detailed Solution:**

$\text { Let } \begin{aligned}
\mathrm{I} & =\int \frac{5 \tan x}{\tan x-2} \mathrm{~d} x \\
& =\int \frac{5 \sin x}{\sin x-2 \cos x} \mathrm{~d} x
\end{aligned}$
Let $5 \sin x=\mathrm{A}(\sin x-2 \cos x)$
$+\mathrm{B} \cdot \frac{\mathrm{d}}{\mathrm{d} x}(\sin x-2 \cos x)$
$\begin{aligned}
& \therefore \quad 5 \sin x=\mathrm{A}(\sin x-2 \cos x)+\mathrm{B}(\cos x+2 \sin x) \\
& \therefore \quad \mathrm{A}+2 \mathrm{~B}=5 \text { and }-2 \mathrm{~A}+\mathrm{B}=0
\end{aligned}$
Solving these equations, we get
$\begin{aligned}
\mathrm{A} & =1, \mathrm{~B}=2 \\
\therefore \quad \mathrm{I} & =\int 1 \mathrm{~d} x+2 \int \frac{\cos x+2 \sin x}{\sin x-2 \cos x} \mathrm{~d} x \\
& =x+2 \log |\sin x-2 \cos x|+\mathrm{c}
\end{aligned}$
But $\int \frac{5 \tan x}{\tan x-2} \mathrm{~d} x=x+\operatorname{alog}|\sin x-2 \cos x|+\mathrm{c}$
Comparing, we get $\mathrm{a}=2$

</details>

---

### Q156. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \frac{\mathrm{d} x}{x^2\left(x^4+1\right)^{\frac{3}{4}}}$ is

**Options:**

- **(A)** $\left(\frac{x^4+1}{x^4}\right)^{\frac{1}{4}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\left(x^4+1\right)^{\frac{1}{4}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $-\left(x^4+1\right)^{\frac{1}{4}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $-\left(\frac{x^4+1}{x^4}\right)^{\frac{1}{4}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\left(\frac{x^4+1}{x^4}\right)^{\frac{1}{4}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

Let $\mathrm{I}=\int \frac{1}{x^2\left(x^4+1\right)^{\frac{3}{4}}} \mathrm{~d} x=\int \frac{\mathrm{d} x}{x^5\left(1+\frac{1}{x^4}\right)^{\frac{3}{4}}}$
Put $1+\frac{1}{x^4}=\mathrm{t} \Rightarrow \frac{-4}{x^5} \mathrm{~d} x=\mathrm{dt}$
$\begin{aligned}
\therefore \quad I & =-\frac{1}{4} \int \frac{d t}{t^{\frac{3}{4}}} \\
& =-\frac{1}{4} \times 4 t^{\frac{1}{4}}+c=-t^{\frac{1}{4}}+c \\
& =-\left(1+\frac{1}{x^4}\right)^{\frac{1}{4}}+c=-\left(\frac{x^4+1}{x^4}\right)^{\frac{1}{4}}+c
\end{aligned}$

</details>

---

### Q157. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{I}=\int \frac{\mathrm{d} x}{x^2\left(x^4+1\right)^{\frac{3}{4}}}$, then I is

**Options:**

- **(A)** $\left(\frac{x^4+1}{x}\right)^{\frac{1}{4}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\frac{\left(x^4-1\right)^{\frac{1}{4}}}{x}+c$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $-\frac{\left(x^4+1\right)^{\frac{1}{4}}}{x}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $-\left(\frac{x^4+1}{x}\right)^{\frac{1}{4}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\frac{\left(x^4+1\right)^{\frac{1}{4}}}{x}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

Let $\mathrm{I}=\int \frac{1}{x^2\left(x^4+1\right)^{\frac{3}{4}}} \mathrm{~d} x=\int \frac{\mathrm{d} x}{x^5\left(1+\frac{1}{x^4}\right)^{\frac{3}{4}}}$
Put $1+\frac{1}{x^4}=\mathrm{t} \Rightarrow \frac{-4}{x^5} \mathrm{dx}=\mathrm{dt}$
$\begin{aligned}
\therefore \quad I & =-\frac{1}{4} \int \frac{\mathrm{dt}}{\mathrm{t}^{\frac{3}{4}}}=-\frac{1}{4} \times 4 \mathrm{t}^{\frac{1}{4}}+\mathrm{c}=-\mathrm{t}^{\frac{1}{4}}+\mathrm{c} \\
& =-\left(1+\frac{1}{x^4}\right)^{\frac{1}{4}}+\mathrm{c} \\
& =\frac{-\left(x^4+1\right)^{\frac{1}{4}}}{x}+\mathrm{c}
\end{aligned}$

</details>

---

### Q158. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{d x}{\sin x+\cos x}=$

**Options:**

- **(A)** $\sqrt{2} \log \tan \left(x+\frac{\pi}{4}\right)+c$, where c is a constant of integration.
- **(B)** $\frac{1}{\sqrt{2}} \log \tan \left(\frac{x}{2}+\frac{\pi}{8}\right)+c$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\frac{1}{\sqrt{2}} \log \left(\frac{\tan \frac{x}{2}-\sqrt{2}+1}{\tan \frac{x}{2}+\sqrt{2}+1}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $-\frac{1}{\sqrt{2}} \log \left(\frac{\tan \frac{x}{2}-(\sqrt{2}+1)}{\tan \frac{x}{2}+\sqrt{2}-1}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\frac{1}{\sqrt{2}} \log \left(\frac{\tan \frac{x}{2}-(\sqrt{2}+1)}{\tan \frac{x}{2}+\sqrt{2}-1}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \mathrm{I}=\int \frac{\mathrm{d} x}{\sin x+\cos x} \\ & \text { Put } \tan \frac{x}{2}=\mathrm{t} \\ & \Rightarrow x=2 \tan ^{-1} \mathrm{t} \\ & \Rightarrow \mathrm{d} x=\frac{2}{1+\mathrm{t}^2} \mathrm{dt} \\ & \text { and } \cos x=\frac{1-t^2}{1+t^2}, \sin x=\frac{2 t}{1+t^2} \\ & \therefore \quad I=\int \frac{\frac{2}{1+t^2}}{\frac{2 t}{1+t^2}+\frac{1-t^2}{1+t^2}} d t \\ & =\int \frac{2}{2 \mathrm{t}+1-\mathrm{t}^2} d \mathrm{t} \\ & =-2 \int \frac{1}{\mathrm{t}^2-2 \mathrm{t}-1} d \mathrm{t} \\ & =-2 \int \frac{1}{t^2-2 t+1-1-1} \\ & =-2 \int \frac{1}{(t-1)^2-(\sqrt{2})^2} \\ & \end{aligned}$
$\begin{aligned} & =-2 \times \frac{1}{2 \sqrt{2}} \log \left|\frac{\mathrm{t}-1-\sqrt{2}}{\mathrm{t}-1+\sqrt{2}}\right|+\mathrm{c} \\ & =\frac{-1}{\sqrt{2}} \log \left|\frac{\tan \frac{x}{2}-1-\sqrt{2}}{\tan \frac{x}{2}-1+\sqrt{2}}\right|+\mathrm{c} \\ & =\frac{-1}{\sqrt{2}} \log \left|\frac{\tan \frac{x}{2}-(\sqrt{2}+1)}{\tan \frac{x}{2}+\sqrt{2}-1}\right|+\mathrm{c}\end{aligned}$

</details>

---

### Q159. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha \in\left(0, \frac{\pi}{2}\right)$ be fixed. If the integral $\int \frac{\tan x+\tan \alpha}{\tan x-\tan \alpha} d x=A(x) \cos 2 \alpha+B(x) \sin 2 \alpha+c$, (where $\mathrm{c}$ is a constant of integration), then functions $\mathrm{A}(x)$ and $\mathrm{B}(x)$ are respectively

**Options:**

- **(A)** $x+\alpha$ and $\log |\sin (x+\alpha)|$.
- **(B)** $x-\alpha$ and $\log |\sin (x-\alpha)|$.
- **(C)** $x-\alpha$ and $\log |\cos (x-\alpha)|$.
- **(D)** $x+\alpha$ and $\log |\sin (x-\alpha)|$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x-\alpha$ and $\log |\sin (x-\alpha)|$.**

**Detailed Solution:**

$\text { Let } \begin{aligned}
\mathrm{I} & =\int \frac{\tan x+\tan \alpha}{\tan x-\tan \alpha} \mathrm{d} x \\
& =\int \frac{\frac{\sin x}{\cos x}+\frac{\sin \alpha}{\cos \alpha}}{\frac{\sin x}{\cos x}-\frac{\sin \alpha}{\cos \alpha}} \mathrm{d} x \\
& =\int \frac{\sin x \cos \alpha+\sin \alpha \cos x}{\sin x \cos \alpha-\sin \alpha \cos x} \mathrm{~d} x \\
& =\int \frac{\sin (x+\alpha)}{\sin (x-\alpha)} \mathrm{d} x
\end{aligned}$
Let $x-\alpha=\mathrm{t}$
$\begin{aligned}
\therefore \quad \mathrm{I} & =\frac{\sin (\mathrm{t}+2 \alpha)}{\sin \mathrm{t}} \\
& =\int \frac{\sin (\mathrm{t}) \cos 2 \alpha+\cos (\mathrm{t}) \sin 2 \alpha}{\sin (\mathrm{t})} \mathrm{d} x \\
& =\cos 2 \alpha \int 1 \mathrm{dt}+\sin 2 \alpha \int \cot (\mathrm{t}) \mathrm{dt} \\
& =\cos 2 \alpha \cdot \mathrm{t}+\sin 2 \alpha \cdot \log |\sin (\mathrm{t})|+\mathrm{c} \\
\therefore \quad \mathrm{I} & =(x-\alpha) \cos 2 \alpha+\log |\sin (x-\alpha)| \sin 2 \alpha+\mathrm{c} \\
& \mathrm{But} \int \frac{\tan x+\tan \alpha}{\tan x-\tan \alpha} \mathrm{d} x=\mathrm{A}(x) \cos 2 \alpha+\mathrm{B}(x) \sin 2 \alpha+\mathrm{c} ... [Given] \\
& \Rightarrow \mathrm{A}(x)=x-\alpha, \mathrm{B}(x)=\log |\sin (x-\alpha)|+\mathrm{c}
\end{aligned}$

</details>

---

### Q160. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int(\sqrt{\tan x}+\sqrt{\cot x}) d x=$

**Options:**

- **(A)** $\sqrt{2} \sin ^{-1}(\sin x-\cos x)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\frac{1}{\sqrt{2}} \sin ^{-1}(\sin x-\cos x)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\sin ^{-1}(\sin x-\cos x)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $2 \sin ^{-1}(\sin x-\cos x)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{2} \sin ^{-1}(\sin x-\cos x)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \mathrm{I}=\int(\sqrt{\tan x}+\sqrt{\cot x}) \mathrm{d} x \\ & =\int\left(\sqrt{\frac{\sin x}{\cos x}}+\sqrt{\frac{\cos x}{\sin x}}\right) d x \\ & \mathrm{I}=\int \frac{\sin x+\cos x}{\sqrt{\sin x \cos x}} \mathrm{~d} x \\ & \text { Let } \sin x-\cos x=\mathrm{t} \\ & \therefore \quad(\sin x+\cos x) \mathrm{d} x=\mathrm{dt} \\ & \text { Consider, } \sin x-\cos x=\mathrm{t} \\ & \text { Squaring on both sides, we get } \\ & 1-2 \sin t \cdot \cos t=t^2 \\ & 1-t^2=2 \sin t \cdot \cos t \\ & \therefore \quad \sin t \cdot \cos t=\frac{1-t^2}{2} \\ & \therefore \quad \mathrm{I}=\int \frac{\mathrm{dt}}{\frac{\sqrt{1-\mathrm{t}^2}}{\sqrt{2}}} \\ & \therefore \quad \mathrm{I}=\sqrt{2} \int \frac{1}{\sqrt{1-\mathrm{t}^2}} \mathrm{dt} \\ & \therefore \quad \mathrm{I}=\sqrt{2} \sin ^{-1}(\mathrm{t})+\mathrm{c} \\ & \therefore \quad \mathrm{I}=\sqrt{2} \sin ^{-1}(\sin x-\cos x)+\mathrm{c} \\ & \end{aligned}$

</details>

---

### Q161. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{\sin x}{3+4 \cos ^2 x} \mathrm{~d} x=\mathrm{A} \tan ^{-1}(\mathrm{~B} \cos x)+\mathrm{C}$, (where $\mathrm{c}$ is a constant of integration), then the value of $\mathrm{A}+\mathrm{B}$ is

**Options:**

- **(A)** $\frac{5}{2 \sqrt{3}}$
- **(B)** $\frac{-1}{2 \sqrt{3}}$
- **(C)** $\frac{-2}{\sqrt{3}}$
- **(D)** $\frac{\sqrt{3}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\sqrt{3}}{2}$**

**Detailed Solution:**

Let $\mathrm{I}=\int \frac{\sin x}{3+4 \cos ^2 x} \mathrm{~d} x$
Put $\cos x=\mathrm{t}$
$-\sin x \mathrm{~d} x=\mathrm{dt}$
$\therefore \quad \sin x \mathrm{~d} x=-\mathrm{dt}$
$\begin{aligned}
\therefore \quad \mathrm{I} & =\int \frac{-\mathrm{dt}}{3+4 \mathrm{t}^2} \\
& =-1 \int \frac{1}{4 \mathrm{t}^2+3}
\end{aligned}$
$=-1 \int \frac{1}{(2 t)^2+(\sqrt{3})^2}$
$=-1 \times \frac{1}{2 \times \sqrt{3}} \tan ^{-1}\left(\frac{2 \mathrm{t}}{\sqrt{3}}\right)+\mathrm{c}$
$\mathrm{I}=\frac{-1}{2 \sqrt{3}} \tan ^{-1}\left(\frac{2 \cos x}{\sqrt{3}}\right)+\mathrm{c}$
But $\int \frac{\sin x}{3+4 \cos ^2 x} \mathrm{~d} x=\mathrm{A} \tan ^{-1}(\mathrm{~B} \cos x)+\mathrm{c}$
Comparing above equations, we get
$\begin{aligned}
\mathrm{A} & =\frac{-1}{2 \sqrt{3}}, \mathrm{~B}=\frac{2}{\sqrt{3}} \\
\therefore \quad \mathrm{A} & +\mathrm{B}=\frac{-1}{2 \sqrt{3}}+\frac{2}{\sqrt{3}}=\frac{3}{2 \sqrt{3}}=\frac{\sqrt{3}}{2}
\end{aligned}$

</details>

---

### Q162. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{1}{\sin (x-a) \sin x} \mathrm{~d} x=$

**Options:**

- **(A)** $\sin \mathrm{a}(\log (\sin (x-\mathrm{a}) \cdot \operatorname{cosec} x))+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\operatorname{cosec} \mathrm{a}(\log (\sin (x-\mathrm{a}) \cdot \operatorname{cosec} x))+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $-\sin \mathrm{a}(\log (\sin (x-\mathrm{a}) \cdot \sin x))+\mathrm{c}$, where $\mathrm{c}$ is a const1
- **(D)** $-\operatorname{cosec} \mathrm{a}(\log (\sin (x-\mathrm{a}) \cdot \sin x))+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\operatorname{cosec} \mathrm{a}(\log (\sin (x-\mathrm{a}) \cdot \operatorname{cosec} x))+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

Let $\mathrm{I}=\int \frac{1}{\sin (x-\mathrm{a}) \sin x} \mathrm{~d} x$
Put $x-\mathrm{a}=\mathrm{t} \rightarrow x=\mathrm{a}+\mathrm{t}$ $\mathrm{d} x=\mathrm{dt}$
$\begin{aligned} \therefore \quad I & =\int \frac{1}{\sin t \cdot \sin (a+t)} d t \\ & =\frac{1}{\sin a} \int \frac{\sin a}{\sin t \cdot \sin (a+t)} d t \\ & =\frac{1}{\sin a} \int \frac{\sin ((a+t)-t)}{\sin (a+t) \cdot \sin t} d t \\ & =\frac{1}{\sin a}\left[\int \frac{\sin (a+t) \cos t}{\sin (a+t) \sin t} d t-\int \frac{\sin t \cos (a+t)}{\sin (a+t) \sin t} d t\right] \\ & =\frac{1}{\sin a}\left[\int \cot t d t-\int \cot (a+t) d t\right] \\ & =\operatorname{cosec} a[\log |\sin t|-\log |\sin (a+t)|]+c \\ & =\operatorname{cosec} a\left[\log \left|\frac{\sin t}{\sin (a+t)}\right|\right]+c \\ & =\operatorname{cosec} a[\log (\sin (x-a) \cdot \operatorname{cosec} x)]+c\end{aligned}$

</details>

---

### Q163. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If
$\mathrm{I}=\int \frac{\sin x+\sin ^3 x}{\cos 2 x} \mathrm{~d} x=\mathrm{P} \cos x+\mathrm{Q} \log \left|\frac{\sqrt{2} \cos x-1}{\sqrt{2} \cos x+1}\right|+\mathrm{c},$
(where $\mathrm{c}$ is a constant of integration), then the values of $\mathrm{P}$ and $\mathrm{Q}$ are respectively

**Options:**

- **(A)** $\frac{1}{2}, \frac{3}{4 \sqrt{2}}$
- **(B)** $\frac{1}{2}, \frac{-3}{4 \sqrt{2}}$
- **(C)** $\frac{1}{2}, \frac{3}{2 \sqrt{2}}$
- **(D)** $\frac{1}{2}, \frac{3}{2 \sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2}, \frac{-3}{4 \sqrt{2}}$**

**Detailed Solution:**

$\begin{aligned} I & =\int \frac{\sin x+\sin ^3 x}{\cos 2 x} d x \\ & =\int \frac{\sin x\left(1+\sin ^2 x\right)}{2 \cos ^2 x-1} d x \\ & =\int \frac{\sin x\left(2-\cos ^2 x\right)}{2 \cos ^2 x-1} d x\end{aligned}$
$\begin{aligned} & \text { Put } \cos x=\mathrm{t} \\ & -\sin x \mathrm{~d} x=\mathrm{dt} \\ & \mathrm{I}=\int \frac{\mathrm{t}^2-2}{2 \mathrm{t}^2-1} \mathrm{dt} \\ & =\frac{1}{2} \int \frac{2 \mathrm{t}^2-4}{2 \mathrm{t}^2-1} \mathrm{dt} \\ & =\frac{1}{2}\left[\int \frac{2 \mathrm{t}^2-1}{2 \mathrm{t}^2-1} \mathrm{dt}-\int \frac{3}{2 \mathrm{t}^2-1} \mathrm{dt}\right] \\ & I=\frac{1}{2} t-\frac{1}{2} \times \frac{3}{2 \sqrt{2}} \log \left|\frac{\sqrt{2} t-1}{\sqrt{2} t+1}\right|+c \\ & =\frac{1}{2} \cos x-\frac{3}{4 \sqrt{2}} \log \left|\frac{\sqrt{2} \cos x-1}{\sqrt{2} \cos x+1}\right|+\mathrm{c} \\ & \therefore \quad \mathrm{P}=\frac{1}{2} \text { and } \mathrm{Q}=\frac{-3}{4 \sqrt{2}} \\ & \end{aligned}$

</details>

---

### Q164. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{\mathrm{e}^{\tan ^{-1} x}}{1+x^2}\left[\left(\sec ^{-1} \sqrt{1+x^2}\right)^2+\cos ^{-1}\left(\frac{1-x^2}{1+x^2}\right)\right] \mathrm{d} x, x>0=$

**Options:**

- **(A)** $\left(\tan ^{-1} x\right)^2 \mathrm{e}^{\tan ^{-1} x}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\left(\tan ^{-1} x\right) \mathrm{e}^{\tan ^{-1} x}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\left(\tan ^{-1} x\right) \mathrm{e}^{2 \tan ^{-1} x}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $\left(\tan ^{-1} x\right)^2 \mathrm{e}^{2 \tan ^{-1} x}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(\tan ^{-1} x\right)^2 \mathrm{e}^{\tan ^{-1} x}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

$\begin{aligned} & \int \frac{\mathrm{e}^{\tan ^{-1} x}}{1+x^2}\left[\left(\sec ^{-1} \sqrt{1+x^2}\right)^2+\cos ^{-1}\left(\frac{1-x^2}{1+x^2}\right)\right] \mathrm{d} x, \\ & \text { Put } x=\tan \mathrm{t} \\ \therefore \quad & \mathrm{d} x=\sec ^2 \mathrm{t} d \mathrm{t}\end{aligned}$
$\begin{aligned} \therefore \quad \mathrm{I} & =\int \frac{\mathrm{e}^{\tan ^{-1}(\tan \mathrm{t})}}{1+\tan ^2 \mathrm{t}}\left[\left(\sec ^{-1} \sqrt{1+\tan ^2} \mathrm{t}\right)^2+\cos ^{-1}\left(\frac{1-\tan ^2 \mathrm{t}}{1+\tan ^2 \mathrm{t}}\right)\right] \\ & =\int \frac{\mathrm{e}^{\mathrm{t}}}{\sec ^2 \mathrm{t}}\left[\left(\sec ^2 \mathrm{t}(\sec \mathrm{t})\right)^2+\cos ^{-1}(\cos 2 \mathrm{t})\right] \sec ^2 \mathrm{t} d \mathrm{t} \\ & =\int \mathrm{e}^{\mathrm{t}}\left[\mathrm{t}^2+2 \mathrm{t}\right] \mathrm{dt} \\ & =\mathrm{e}^{\mathrm{t}} \cdot \mathrm{t}^2+\mathrm{c} \quad \ldots\left[\int \mathrm{e}^x \mathrm{f}(x) \cdot \mathrm{f}^{\prime}(x)=\mathrm{e}^x \mathrm{f}(x)+\mathrm{c}\right] \\ & =\mathrm{t}^2 \cdot \mathrm{e}^{\mathrm{t}}+\mathrm{c} \quad \\ & =\left(\tan ^{-1} \cdot x\right)^2 \mathrm{e}^{\tan \mathrm{tan}^{-1} x}+\mathrm{c} .\end{aligned}$

</details>

---

### Q165. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{x+1}{x\left(1+x \mathrm{e}^x\right)^2} d x=$

**Options:**

- **(A)** $\log \left|\frac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right|+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\log \left|\frac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right|-\frac{1}{1+x \mathrm{e}^x}+\mathrm{c}$, where $\mathrm{c}$ is $\mathrm{a}$ constant of integration.
- **(C)** $\log \left|1+x \mathrm{e}^x\right|+\frac{1}{1+x \mathrm{e}^x}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $\log \left|\frac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right|+\frac{1}{1+x \mathrm{e}^x}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log \left|\frac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right|+\frac{1}{1+x \mathrm{e}^x}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \mathrm{I}=\int \frac{x+1}{x\left(1+x \mathrm{e}^x\right)^2} \mathrm{~d} x=\int \frac{\mathrm{e}^x(x+1)}{\mathrm{e}^x \cdot x\left(1+x \mathrm{e}^x\right)^2} \mathrm{~d} x \\ & \text { Let } x \cdot \mathrm{e}^x=\mathrm{t} \\ & \Rightarrow(x+1) \mathrm{e}^x \mathrm{~d} x=\mathrm{dt} \\ & \therefore \quad \mathrm{I}=\int \frac{\mathrm{dt}}{\mathrm{t}(1+\mathrm{t})^2} \\ & =\int \frac{1+\mathrm{t}-\mathrm{t}}{\mathrm{t}(1+\mathrm{t})^2} \mathrm{dt} \\ & =\int \frac{1 d t}{t(1+t)}-\int \frac{1}{(1+t)^2} d t \\ & =\int \frac{1+t-t}{t(1+t)}-\int \frac{1}{(1+t)^2} d t \\ & =\int \frac{1}{t} d t-\int \frac{1}{(t+1)} d t-\int \frac{1}{(1+t)^2} d t \\ & =\log \mathrm{t}-\int \frac{\mathrm{dt}}{(\mathrm{t}+1)}-\int \frac{1}{(1+\mathrm{t})^2} \mathrm{dt}+\mathrm{c} \\ & \text { Let } y=1+\mathrm{t} \\ & \Rightarrow \mathrm{d} y=\mathrm{dt} \\ & \therefore \quad \mathrm{I}=\log \mathrm{t}-\int \frac{1}{y} \mathrm{~d} y-\int \frac{1}{y^2} \mathrm{~d} y+\mathrm{c} \\ & =\log \mathrm{t}-\log y+\frac{1}{y}+\mathrm{c} \\ & =\log \mathrm{t}-\log (1+\mathrm{t})+\frac{1}{(1+\mathrm{t})}+\mathrm{c} \\ & =\log x \mathrm{e}^x-\log \left(1+x \mathrm{e}^x\right)+\frac{1}{\left(1+x \mathrm{e}^x\right)}+\mathrm{c} \\ & \therefore \quad \mathrm{I}=\log \left|\frac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right|+\frac{1}{1+x \mathrm{e}^x}+\mathrm{c} \\ & \end{aligned}$

</details>

---

### Q166. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{e^{\frac{x}{2}}}{\sqrt{e^{-x}-e^x}} \mathrm{~d} x=\sin ^{-1}(f(x))+C, \quad$ (where $\quad C \quad$ is constant of integration.) then $f(2)$ has the value

**Options:**

- **(A)** $e$
- **(B)** $e^2$
- **(C)** $e^{\frac{1}{2}}$
- **(D)** $e^{\frac{3}{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $e^2$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{e^{x / 2}}{\sqrt{e^{-x}-e^x}} \mathrm{~d} x=\int \frac{e^x \mathrm{~d} x}{\sqrt{1-\left(e^x\right)^2}}\left[\text { Multiplying } N^r \text { and } D^r \text { by } e^{\frac{x}{2}} \text { ] }\right. \\ & =\int \frac{\mathrm{d} t}{\sqrt{1-t^2}}=\sin ^{-1} t+C=\sin ^{-1}\left(e^x\right)+C\left[\text { let } e^x=t\right] \\ & \Rightarrow f(x)=e^x \\ & \Rightarrow f(2)=e^2\end{aligned}$

</details>

---

### Q167. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\log \left(x+\sqrt{1+x^2}\right)}{\sqrt{1+x^2}} \mathrm{~d} x=\frac{1}{2}(g(x))^2+C$, (where $C$ is constant of integration.) Then $g(x)=$

**Options:**

- **(A)** $\log \left(x+\sqrt{1+x^2}\right)$
- **(B)** $\log \left(x+\sqrt{1+2 x^2}\right)$
- **(C)** $\log \left(x-\sqrt{1+x^2}\right)$
- **(D)** $\log \left(\sqrt{1+x^2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\log \left(x+\sqrt{1+x^2}\right)$**

**Detailed Solution:**

$\int \frac{\log \left(x+\sqrt{1+x^2}\right)}{\sqrt{1+x^2}} \mathrm{~d} x=\int t \mathrm{~d} t=\frac{t^2}{2}+C$
[where $t=\log \left(x+\sqrt{1+x^2}\right)$ ]
$\begin{aligned}
& =\frac{\left\{\log \left(x+\sqrt{1+x^2}\right)\right\}^2}{2}+C \\
& \Rightarrow g(x)=\log \left(x+\sqrt{1+x^2}\right)^2
\end{aligned}$

</details>

---

### Q168. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{x+1}{\sqrt{2 x-1}} \mathrm{~d} x=f(x) \sqrt{2 x-1}+C$, where $C$ is an arbitrary constant, then $f(x)$ is equal to

**Options:**

- **(A)** $\frac{2}{3}(x+2)$
- **(B)** $\frac{2}{3}(x-4)$
- **(C)** $\frac{1}{3}(x+4)$
- **(D)** $\frac{1}{3}(x+1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{3}(x+4)$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{x+1}{\sqrt{2 x-1}} \mathrm{~d} x=\int \frac{\frac{t+1}{2}+1}{\sqrt{t}} \mathrm{~d} t[\text { Let } 2 x-1=t] \\ & =\int \frac{t+3}{4+\sqrt{t}} \mathrm{~d} t=\frac{1}{4} \int \sqrt{t} \mathrm{~d} t+\frac{3}{4} \int \frac{\mathrm{d} t}{\sqrt{t}} \\ & =\frac{1}{4} \times \frac{2}{3} t^{3 / 2}+\frac{3}{4} \times 2 t^{1 / 2}+C=\frac{1}{6} \sqrt{t}\{t+9\}+C \\ & =\frac{1}{6} \sqrt{2 x-1}\{2 x-1+9\}+C \\ & =\frac{1}{3}(x+4) \sqrt{2 x-1}+C \\ & \Rightarrow f(x)=\frac{1}{3}(x+4)\end{aligned}$

</details>

---

### Q169. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{1}{3-2 \cos 2 x} \mathrm{~d} x=$ (where $C$ is constant of integration.)

**Options:**

- **(A)** $\frac{2}{5} \tan ^{-1}(5 \tan x)+C$
- **(B)** $\frac{1}{\sqrt{5}} \tan ^{-1}(\sqrt{5} \tan x)+C$
- **(C)** $\frac{2}{\sqrt{5}} \tan ^{-1}(\sqrt{5} \tan x)+C$
- **(D)** $\frac{1}{5} \tan ^{-1}(5 \tan x)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{\sqrt{5}} \tan ^{-1}(\sqrt{5} \tan x)+C$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{\mathrm{d} x}{3-2 \cos 2 x}=\int \frac{\mathrm{d} x}{3-2 \times \frac{1-\tan ^2 x}{1+\tan ^2 x}}=\int \frac{\sec ^2 x \mathrm{~d} x}{5 \tan ^2 x+1} \\ & =\int \frac{\mathrm{d} t}{5 t^2+1}[\text { let } \tan x=t] \\ & =\int \frac{\mathrm{d} t}{(\sqrt{5} t)^2+1^2}=\frac{1}{\sqrt{5}} \tan ^{-1}\left(\frac{\sqrt{5} t}{1}\right)+C \\ & =\frac{1}{\sqrt{5}} \tan ^{-1}(\sqrt{5} \tan x)+C\end{aligned}$

</details>

---

### Q170. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\int \frac{2 x^{12}+5 x^9}{\left(x^5+x^3+1\right)^3} \mathrm{~d} x$ is equal to (where $C$ is arbitrary constant.)

**Options:**

- **(A)** $\frac{x^5}{2\left(x^5+x^3+1\right)^2}+C$
- **(B)** $\frac{x^{10}}{2\left(x^5+x^3+1\right)^2}+C$
- **(C)** $\frac{-x^5}{\left(x^5+x^3+1\right)^2}+C$
- **(D)** $\frac{-x^{10}}{2\left(x^5+x^3+1\right)^2}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{x^{10}}{2\left(x^5+x^3+1\right)^2}+C$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{2 x^{12}+5 x^9}{\left(x^5+x^3+1\right)^3} \mathrm{~d} x=\int \frac{2 x^{12}+5 x^9}{x^{15}\left(1+\frac{1}{x^2}+\frac{1}{x^5}\right)^3} \mathrm{~d} x \\ & =\int \frac{\frac{2}{x^3}+\frac{5}{x^6}}{\left(1+\frac{1}{x^2}+\frac{1}{x^5}\right)^3} \mathrm{~d} x \\ & =\int \frac{-\mathrm{d} t}{t^3}=\frac{1}{2 t^2}+C\left[\operatorname{let} 1+\frac{1}{x^2}+\frac{1}{x^5}=t\right] \\ & =\frac{1}{2\left(1+\frac{1}{x^2}+\frac{1}{x^5}\right)^2}+C \\ & =\frac{x^{10}}{2\left(x^5+x^3+1\right)^2}+C\end{aligned}$

</details>

---

### Q171. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \cos \sqrt{x} \mathrm{~d} x=$
(where $C$ is a constant of integration.)

**Options:**

- **(A)** $2[\sqrt{x} \sin \sqrt{x}+\cos \sqrt{x}]+C$
- **(B)** $[\sqrt{x} \sin \sqrt{x}-\cos \sqrt{x}]+C$
- **(C)** $2[\sqrt{x} \sin \sqrt{x}-\cos \sqrt{x}]+C$
- **(D)** $[\sqrt{x} \sin \sqrt{x}+\cos \sqrt{x}]+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2[\sqrt{x} \sin \sqrt{x}+\cos \sqrt{x}]+C$**

**Detailed Solution:**

$\int \cos \sqrt{x} d x$ let $\sqrt{x}=t$ i.e. $\mathrm{d} x=2 t \mathrm{~d} t$
$=2 \int t \cos t \mathrm{~d} t=2\left[t \sin t-\int \sin t \mathrm{~d} t\right]$ [integrating by parts]
$=2[t \cdot \sin t+\cos t]+C=2[\sqrt{x} \sin \sqrt{x}+\cos \sqrt{x}]+C$

</details>

---

### Q172. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The integral $\int \frac{\sin ^2 x \cos ^2 x}{\left(\sin ^5 x+\cos ^3 x \sin ^2 x+\sin ^3 x \cos ^2 x+\cos ^5 x\right)^2} d x$ is equal to (Where $C$ is a constant of integration).

**Options:**

- **(A)** $\frac{1}{1+\cot ^3 x}+C$
- **(B)** $\frac{-1}{1+\cot ^3 x}+C$
- **(C)** $\frac{1}{3\left(1+\tan ^3 x\right)}+C$
- **(D)** $\frac{-1}{3\left(1+\tan ^3 x\right)}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{-1}{3\left(1+\tan ^3 x\right)}+C$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{\sin ^2 x \cos ^2 x}{\left(\sin ^5 x+\cos ^3 x \sin ^2 x+\sin ^3 x \cos ^2 x+\cos ^5 x\right)^2} d x \\ & =\int \frac{\tan ^2 x \cdot \sec ^6 x d x}{\left(\tan ^5 x+\tan ^2 x+\tan ^3 x+1\right)^2} \text { [dividing } N^r \text { and } D^r \text { by } \cos ^{10} x \text { ] } \\ & =\int \frac{\tan ^2 x \cdot\left(\tan ^2 x+1\right)^2 \sec ^2 x d x}{\left(\tan ^2 x+1\right)^2\left(\tan ^3 x+1\right)^2} \\ & =\int \frac{\tan ^2 x \cdot \sec ^2 x d x}{\left(\tan ^3 x+1\right)^2}\end{aligned}$
$\begin{aligned} & =\frac{1}{3} \int \frac{\mathrm{d} t}{t^2} \\ & \left\{\text { Let } \tan ^3 x+1=t \text { i.e., } 3 \tan ^2 x \cdot \sec ^2 x \mathrm{~d} x=\mathrm{d} t\right\} \\ & =-\frac{1}{3 t}+c \\ & =\frac{-1}{3\left(\tan ^3 x+1\right)}+c\end{aligned}$

</details>

---

### Q173. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$$
\int \frac{4 x^2 \cot ^{-1}\left(x^3\right)}{1+x^6} \mathrm{~d} x=
$$
(where $C$ is a constant of integration.)

**Options:**

- **(A)** $\frac{-2}{3}\left(\cot ^{-1} X^3\right)+C$
- **(B)** $\frac{-2}{3}\left(\cot ^{-1} X^3\right)^2+C$
- **(C)** $\frac{2}{3}\left(\cot ^{-1} x^3\right)+C$
- **(D)** $\frac{2}{3}\left(\cot ^{-1} x^3\right)^2+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-2}{3}\left(\cot ^{-1} X^3\right)^2+C$**

**Detailed Solution:**

$\int \frac{4 x^2 \cot ^{-1}\left(x^3\right)}{1+x^6} \mathrm{~d} x$ let $\cot ^{-1}\left(x^3\right)=t$
then $\frac{-3 x^2}{1+x^6} d x=d t$
$\begin{aligned} & =-\frac{4}{3} \int t \mathrm{~d} t \\ & =-\frac{4}{3} \times \frac{t^2}{2}+c=-\frac{2}{3}\left(\cot ^{-1} X^3\right)^2+c\end{aligned}$

</details>

---

### Q174. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \frac{2 x^3-1}{x^4+x} \mathrm{~d} x$ is equal to (where $C$ is a constant of integration.)

**Options:**

- **(A)** $\frac{1}{2} \log \frac{\left(x^3+1\right)^2}{x^3}+C$
- **(B)** $\log \frac{\left(x^3+1\right)}{x}+C$
- **(C)** $\log \left(\frac{x^3+1}{x^2}\right)+C$
- **(D)** $\frac{1}{2} \log \frac{\left(x^3+1\right)}{x^2}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log \frac{\left(x^3+1\right)}{x}+C$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{2 x^3-1}{x^4+x} \mathrm{~d} x=\int \frac{2 x^3-1}{x\left(x^3+1\right)} \mathrm{d} x=\int\left(\frac{3 x^2}{x^3+1}-\frac{1}{x}\right) \mathrm{d} x \\ & =\log \left(x^3+1\right)-\log x+c \\ & =\log \left(\frac{x^3+1}{x}\right)+c\end{aligned}$

</details>

---

### Q175. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The integral $\int \frac{\sin ^2 x \cos ^2 x d x}{\left(\sin ^5 x+\cos ^3 x \sin ^2 x+\sin ^3 x \cos ^2 x+\cos ^5 x\right)^2}$ is equal to (where $C$ is a constant of integration).

**Options:**

- **(A)** $\frac{1}{3\left(1+\tan ^3 x\right)}+C$
- **(B)** $\frac{-1}{3\left(1+\tan ^3 x\right)}+C$
- **(C)** $\frac{-1}{1+\cot ^3 x}+C$
- **(D)** $\frac{1}{1+\cot ^3 x}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-1}{3\left(1+\tan ^3 x\right)}+C$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{\sin ^2 x \cdot \cos ^2 x \mathrm{~d} x}{\left(\sin ^5 x+\cos ^3 x \sin ^2 x+\sin ^3 x \cos ^2 x+\cos ^5 x\right)^2} \\ & \int \frac{\tan ^2 x \cdot \sec ^6 x \mathrm{~d} x}{\left(\tan ^5 x+\tan ^2 x+\tan ^3 x+1\right)^2} \quad \text { [dividing } N^r \text { and } D^r \text { by } \cos ^{10} x \text { ] } \\ & \int \frac{\tan ^2 x\left(\tan ^2 x+1\right)^2 \sec ^2 x \mathrm{~d} x}{\left(\tan ^2 x+1\right)^2\left(\tan ^3 x+1\right)^2} \\ & \int \frac{\tan ^2 x \sec ^2 x \mathrm{~d} x}{\left(\tan ^3 x+1\right)^2} \\ & =\frac{-1}{3\left(\tan ^3 x+1\right)}+c\left[\text { Let } \tan ^3 x+1=t\right]\end{aligned}$

</details>

---

### Q176. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{\sqrt{1-x^2}}{x^4} \mathrm{~d} x=A(x)\left(\sqrt{1-x^2}\right)^m+C$ for a suitable chosen integer $m$ and a function $A(x)$, where $C$ is a constant of integration, then $(A(x))^m$ equals

**Options:**

- **(A)** $-\frac{1}{27 x^9}$
- **(B)** $\frac{1}{9 x^4}$
- **(C)** $\frac{1}{27 x^6}$
- **(D)** $-\frac{1}{3 x^3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\frac{1}{27 x^9}$**

**Detailed Solution:**

$\int \frac{\sqrt{1-x^2}}{x^4} \mathrm{~d} x=A(x)\left(\sqrt{1-x^2}\right)^m+C$
Let $x=\cos \theta d x=-\sin \theta d \theta$
$\begin{aligned}
& \Rightarrow \int \frac{\sqrt{1-\cos ^2 \theta}}{\cos ^4 \theta} \cdot(-\sin \theta \mathrm{d} \theta)=-\int \sec ^4 \theta \cdot \sin ^2 \theta \mathrm{d} \theta \\
& =-\int \tan ^2 \theta \cdot \sec ^2 \theta \mathrm{d} \theta \\
& =-\frac{\tan ^3 \theta}{3}+C \\
& =-\frac{1}{3}\left(\frac{\sqrt{1-\cos ^2 \theta}}{\cos \theta}\right)^3+C \\
& =-\frac{1}{3}\left(\frac{\sqrt{1-x^2}}{x}\right)^3+C \\
& =\frac{-1}{3 x^3} \cdot\left(\sqrt{1-x^2}\right)^3+C \\
& \Rightarrow A(x)=-\frac{1}{3 x^3} \text { and } m=3
\end{aligned}$
$\Rightarrow\{A(x)\}^m=\left(\frac{-1}{3 x^3}\right)^3=\frac{-1}{27 x^9}$

</details>

---

### Q177. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\mathrm{d} x}{2+\cos x}=$ (Where $C$ is a constant of integration.)

**Options:**

- **(A)** $\frac{2}{\sqrt{3}} \tan ^{-1}\left(\frac{\tan \left(\frac{x}{2}\right)}{2 \sqrt{3}}\right)+C$
- **(B)** $\frac{1}{2 \sqrt{3}} \tan ^{-1}\left(\frac{\tan \left(\frac{x}{2}\right)}{2 \sqrt{3}}\right)+C$
- **(C)** $\frac{1}{\sqrt{3}} \tan ^{-1}\left(\frac{\tan \left(\frac{x}{2}\right)}{\sqrt{3}}\right)+C$
- **(D)** $\frac{2}{\sqrt{3}} \tan ^{-1}\left(\frac{\tan \left(\frac{x}{2}\right)}{\sqrt{3}}\right)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2}{\sqrt{3}} \tan ^{-1}\left(\frac{\tan \left(\frac{x}{2}\right)}{\sqrt{3}}\right)+C$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{\mathrm{d} x}{2+\cos x}=\int \frac{\mathrm{d} x}{2+\frac{1-\tan ^2 \frac{x}{2}}{1+\tan ^2 \frac{x}{2}}}=\int \frac{\sec ^2 \frac{x}{2} \mathrm{~d} x}{3+\tan ^2 \frac{x}{2}} \\ & =2 \int \frac{\frac{1}{2} \sec ^2 \frac{x}{2} \mathrm{~d} x}{(\sqrt{3})^2+\left(\tan \frac{x}{2}\right)^2}=\frac{2}{\sqrt{3}} \cdot \tan ^{-1}\left(\frac{\tan \frac{x}{2}}{\sqrt{3}}\right)\end{aligned}$

</details>

---

### Q178. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{x}{\sqrt{1-2 x^4}} \mathrm{~d} x=$ (Where $C$ is a constant of integration)

**Options:**

- **(A)** $\frac{1}{2 \sqrt{2}} \sin ^{-1}\left(\sqrt{2} x^2\right)+C$
- **(B)** $\frac{1}{2 \sqrt{2}} \sin ^{-1}\left(2 \sqrt{2} x^2\right)+C$
- **(C)** $\frac{1}{2} \sin ^{-1}(2 x)+C$
- **(D)** $\frac{1}{\sqrt{2}} \sin ^{-1}(\sqrt{2} x)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2 \sqrt{2}} \sin ^{-1}\left(\sqrt{2} x^2\right)+C$**

**Detailed Solution:**

$\int \frac{x}{\sqrt{1-2 x^4}} \mathrm{~d} x=\frac{1}{2 \sqrt{2}} \int \frac{2 \sqrt{2} x \mathrm{~d} x}{\sqrt{1-\left(\sqrt{2} x^2\right)^2}}=\frac{1}{2 \sqrt{2}} \sin ^{-1}\left(\sqrt{2} x^2\right)$

</details>

---

### Q179. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\sin 4 x}{\sin x} \mathrm{~d} x=$ (where $C$ is a constant of integration.)

**Options:**

- **(A)** $\frac{\sin 3 x}{3}+4 \sin x+C$
- **(B)** $\frac{1}{3} \sin 3 x-\frac{2}{3} \sin x+C$
- **(C)** $\frac{2 \sin 3 x}{3}+2 \sin x+C$
- **(D)** $\frac{2}{3} \sin 3 x-2 \sin x+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2 \sin 3 x}{3}+2 \sin x+C$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{\sin 4 x}{\sin x} \mathrm{~d} x=\int \frac{4 \sin x \cdot \cos x \cdot \cos 2 x}{\sin x} \mathrm{~d} x=2 \int 2 \cos x \cdot \cos 2 x d x \\ & =2 \int\{\cos 3 x+\cos x\} \mathrm{d} x \\ & =2\left\{\frac{\sin 3 x}{3}+\sin x\right\}+c \\ & =\frac{2}{3} \sin 3 x+2 \sin x+c\end{aligned}$

</details>

---

### Q180. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^{\frac{\pi}{2}} \frac{d x}{5+4 \cos x}=$

**Options:**

- **(A)** $\frac{1}{3} \tan ^{-1}\left(\frac{1}{3}\right)$
- **(B)** $2 \tan ^{-1}\left(\frac{1}{3}\right)$
- **(C)** $\frac{2}{3} \tan ^{-1}\left(\frac{1}{3}\right)$
- **(D)** $\tan ^{-1}\left(\frac{1}{3}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{3} \tan ^{-1}\left(\frac{1}{3}\right)$**

**Detailed Solution:**

$\begin{aligned} & \int_0^{\frac{\pi}{2}} \frac{d x}{5+4 \cos x}=\int_0^{\frac{\pi}{2}} \frac{d x}{5+4 \cdot \frac{1-\tan ^2 \frac{x}{2}}{1+\tan ^2 \frac{x}{2}}}=\int_0^{\frac{\pi}{2}} \frac{\sec ^2 \frac{x}{2} d x}{9+\tan ^2 \frac{x}{2}}=2 \int_0^{\frac{\pi}{2}} \frac{\frac{1}{2} \sec ^2 \frac{x}{2}}{3^2+\tan ^2 \frac{x}{2}} \\ & x=2 \int_0^1 \frac{d t}{3^2+t^2} \frac{1}{3}=2 \times\left[\tan ^{-1} \frac{t}{3}\right]_0^1=2 \\ & =\frac{2}{3}\left\{\tan ^{-1} \frac{1}{3}-\tan ^{-1} 0\right\}=\frac{2}{3} \tan ^{-1} \frac{1}{3}\end{aligned}$

</details>

---

### Q181. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\sin ^8 x-\cos ^8 x}{1-2 \sin ^2 x \cos ^2 x}$ (where $\mathrm{C}$ is constant of integration.)

**Options:**

- **(A)** $-2 \sin (2 x)+C$
- **(B)** $\frac{1}{2} \cos (2 x)+C$
- **(C)** $2 \cos (2 x)+C$
- **(D)** $-\frac{1}{2} \sin (2 x)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\frac{1}{2} \sin (2 x)+C$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{\sin ^8 x-\cos ^8 x}{1-2 \sin ^2 x \cos ^2 x} d x \\ & =\int \frac{\left(\sin ^2 x+\cos ^2 x\right)\left(\sin ^2 x-\cos ^2 x\right)\left(1-2 \sin ^2 x \cdot \cos ^2 x\right)}{1-2 \sin ^2 x \cdot \cos ^2 x} d x \\ & =\int\left(\sin ^2 x-\cos ^2 x\right) d x \\ & =\int-\cos 2 x d x=-\frac{1}{2} \sin 2 x+c\end{aligned}$

</details>

---

### Q182. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int(3-x) \sqrt{4-x} d x=$ (Where $C$ is a constant of integration.)

**Options:**

- **(A)** $\frac{2}{3}(4-x)^{3 / 2}+\frac{2}{5}(4-x)^{5 / 2}+C$
- **(B)** $-\frac{2}{5}(4-x)^{5 / 2}+\frac{2}{3}(4-x)^{3 / 2}+C$
- **(C)** $\frac{2}{3}(4-x)^{3 / 2}-\frac{2}{5}(4-x)^{5 / 2}+C$
- **(D)** $\frac{2}{5}(4-x)^{5 / 2}-\frac{2}{5}(4-x)^{3 / 2}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{3}(4-x)^{3 / 2}-\frac{2}{5}(4-x)^{5 / 2}+C$**

**Detailed Solution:**

$\begin{aligned} & \int(3-x) \sqrt{4-x} d x \\ & =\int\{(4-x)-1\} \sqrt{4-x} d x=\int\left\{(4-x)^{\frac{3}{2}}-(4-x)^{\frac{1}{2}}\right\} d x \\ & =\frac{2}{5}(4-x)^{5 / 2}+\frac{2}{3}(4-x)^{3 / 2}+C \\ & =\frac{2}{3}(4-x)^{3 / 2}-\frac{2}{5}(4-x)^{5 / 2}+C\end{aligned}$

</details>

---

### Q183. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{e^x}{\left(2+e^x\right)\left(e^x+1\right)} d x=$
(where $C$ is $a$ constant of integration.)

**Options:**

- **(A)** $\frac{e^x+1}{e^x+2}+C$
- **(B)** $\log \left(\frac{e^x+2}{e^x+1}\right)+C$
- **(C)** $\log \left(\frac{e^x+1}{e^x+2}\right)+C$
- **(D)** $\log \left(\frac{e^x}{e^x+2}\right)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log \left(\frac{e^x+1}{e^x+2}\right)+C$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{e^x}{\left(2+e^x\right)\left(e^x+1\right)} d x \\ & =\int \frac{d t}{(t+2)(t+1)}=\int\left(\frac{-1}{t+2}+\frac{1}{t+1}\right) d t \\ & =-\log |t+2|+\log |t+1|+c \\ & =\log \left|\frac{t+1}{t+2}\right|+c \\ & =\log \left|\frac{e^x+1}{e^x+2}\right|+c\end{aligned}$

</details>

---

### Q184. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{5\left(x^6+1\right)}{x^2+1} \mathrm{~d} x=$ (Where $C$ is a constant of integration.)

**Options:**

- **(A)** $5\left(x^7+1\right)+\log \left(x^2+1\right)+C$
- **(B)** $x^5-\frac{5 x^3}{3}+5 x+C$
- **(C)** $\frac{5 x^7}{7}+5 x+5 \tan ^{-1} x+C$
- **(D)** $5 \tan ^{-1} x+\log \left(x^2+1\right)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^5-\frac{5 x^3}{3}+5 x+C$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{5\left(x^6+1\right)}{x^2+1} \mathrm{~d} x=\int \frac{5\left(x^2+1\right)\left(x^4-x^2+1\right)}{x^2+1} \mathrm{~d} x \\ & =5 \int\left(x^4-x^2+1\right) \mathrm{d} x \\ & =5\left\{\frac{x^5}{5}-\frac{x^3}{3}+x\right\}+C \\ & =x^5-\frac{5}{3} x^3+5 x+C\end{aligned}$

</details>

---

### Q185. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int_2^3 \frac{\log x}{x} d x=$

**Options:**

- **(A)** $\frac{1}{2} \log 6 \log 3$
- **(B)** $\log 6 \log \frac{3}{2}$
- **(C)** $\frac{1}{2} \log 6 \log \frac{3}{2}$
- **(D)** $2 \log 6 \log \frac{3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2} \log 6 \log \frac{3}{2}$**

**Detailed Solution:**

$\begin{aligned} & \int_2^3 \frac{\log x}{x} d x=\left[\frac{(\log x)^2}{2}\right]_2^3 \\ & =\frac{1}{2}\left\{(\log 3)^2-(\log 2)^2\right\} \\ & =\frac{1}{2}\{\log 3+\log 2\}\{\log 3-\log 2\} \\ & =\frac{1}{2} \log 6 \cdot \log \frac{3}{2}\end{aligned}$

</details>

---

### Q186. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{2 e^x+3 e^{-x}}{3 e^x+4 e^{-x}} d x=A x+B \log \left(3 e^{2 x}+4\right)+C$, then values of $A$ and $B$ are respectively (where $C$ is a constant of integration.)

**Options:**

- **(A)** $\frac{3}{4}, \frac{-1}{24}$
- **(B)** $\frac{3}{4}, \frac{1}{24}$
- **(C)** $\frac{4}{3},-24$
- **(D)** $\frac{1}{4}, \frac{1}{24}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3}{4}, \frac{-1}{24}$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{2 e^x+3 e^{-x}}{3 e^x+4 e^{-x}} d x=\int \frac{2 e^{2 x}+3}{3 e^{2 x}+4} d x \\ & \int \frac{\frac{3}{4}\left(3 e^{2 x}+4\right)-\frac{1}{24}\left(6 e^{2 x}\right)}{3 e^{2 x}+4} d x \\ & =\frac{3}{4} x-\frac{1}{24} \log \left(3 e^{2 x}+4\right)+c \\ & \Rightarrow A=\frac{3}{4} \text { and } B=\frac{-1}{24}\end{aligned}$

</details>

---

### Q187. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\int e^{x^2} \cdot x^3 d x=e^{x^2} f(x)+C$
(where $C$ is a constant of integration)
and $f(1)=0$, then value of $f(2)$ will be

**Options:**

- **(A)** $\frac{3}{2}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{-3}{2}$
- **(D)** $\frac{-1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3}{2}$**

**Detailed Solution:**

$\int e^{x^2 x^3}=\frac{1}{2} \int x^2 e^{x^2} 2 x d x=\frac{1}{2} \int t e^t d t \quad\left[\operatorname{let} x^2=t\right]$
Integrating by parts
$\begin{aligned} & =\frac{1}{2}\left[t \cdot e^t-e^t\right]+C \\ & =\frac{1}{2}\left[x^2 e^{x^2}-e^{x^2}\right]+C=e^{x^2} \cdot \frac{1}{2}\left(x^2-1\right)+C \\ & \Rightarrow f(x)=\frac{1}{2}\left(x^2-1\right) \Rightarrow f(2)=\frac{3}{2}\end{aligned}$

</details>

---

### Q188. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=\sqrt{\tan x}$ and $g(x)=\sin x \cdot \cos x$, then $\int \frac{f(x)}{g(x)} d x$ is equal to (where $C$ is a constant of integration)

**Options:**

- **(A)** $\sqrt{\tan x}+C$
- **(B)** $\frac{1}{2} \sqrt{\tan x}+C$
- **(C)** $\frac{3}{2} \sqrt{\tan x}+C$
- **(D)** $2 \sqrt{\tan x}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 \sqrt{\tan x}+C$**

**Detailed Solution:**

$f(x)=\sqrt{\tan x}, g(x)=\sin x \cdot \cos x$
Now,
$\begin{aligned} & \int \frac{f(x)}{g(x)} d x=\int \frac{\sqrt{\tan x}}{\sin x \cdot \cos x} d x=\int \frac{\sqrt{\tan x \cdot \sec ^2 x}}{\tan x} d x=\int \frac{\sec ^2 x}{\sqrt{\tan x}} d x \\ & =2 \sqrt{\tan x}+C\end{aligned}$

</details>

---

### Q189. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{1}{\cos x \sqrt{\cos 2 x}} d x=$
(where C is a constant of integration.)

**Options:**

- **(A)** $\sin ^{-1}(\tan x)+C$
- **(B)** $\log \left(\tan x+\sqrt{\tan ^2 x+1}\right)+C$
- **(C)** $\tan ^{-1} x+C$
- **(D)** $\log \left(\tan x+\sqrt{\tan ^2 x-1}\right)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sin ^{-1}(\tan x)+C$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{d x}{\cos x \sqrt{\cos 2 x}}=\int \frac{d x}{\cos x \sqrt{\frac{1-\tan ^2 x}{1+\tan ^2 x}}} \\ & \int \frac{d x}{\cos x \frac{\sqrt{1-\tan ^2 x}}{\sec x}}=\int \frac{\sec ^2 d x}{\sqrt{1-\tan ^2 x}} \\ & \int \frac{d t}{\sqrt{1-t^2}}=\sin ^{-1}(t)+C=\sin ^{-1}(\tan x)+C\end{aligned}$
[let $\tan \mathrm{x}=\mathrm{t}$ ]

</details>

---

### Q190. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The integral $\int \frac{3 x^{13}+2 x^{11}}{\left(2 x^4+3 x^2+1\right)^4} d x$ is equal to (where $C$ is a constant of integration.)

**Options:**

- **(A)** $\frac{x^{12}}{\left(2 x^4+3 x^2+1\right)^3}+C$
- **(B)** $\frac{x^4}{\left(2 x^4+3 x^2+1\right)^3}+C$
- **(C)** $\frac{x^4}{6\left(2 x^4+3 x^2+1\right)^3}+C$
- **(D)** $\frac{x^{12}}{6\left(2 x^4+3 x^2+1\right)^3}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{x^{12}}{6\left(2 x^4+3 x^2+1\right)^3}+C$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{3 x^{13}+2 x^{11}}{\left(2 x^4+3 x^2+1\right)^4} d x=\int \frac{3 x^{13}+2 x^{11}}{x^{16}\left(2+\frac{3}{x^2}+\frac{1}{x^4}\right)^4} d x \\ & =-\frac{1}{2} \int \frac{-6 x^{-3}-4 x^{-5}}{\left(2+\frac{3}{x^2}+\frac{1}{x^4}\right)^4} d x=\frac{-1}{2} \times \frac{-1}{3}\left(2+\frac{3}{x^2}+\frac{1}{x^4}\right)^{-3}+C \\ & =\frac{1}{6}\left(\frac{2 x^4+3 x^2+1}{x^4}\right)^{-3}+C=\frac{x^{12}}{6\left(2 x^4+3 x^2+1\right)^3}+C\end{aligned}$

</details>

---

### Q191. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\int \frac{5 x^8+7 x^6}{\left(x^2+1+2 x^7\right)^2} d x, x \geq 0$ and $f(0)=0$, then value of $f(1)$ is

**Options:**

- **(A)** $-\frac{1}{2}$
- **(B)** $\frac{1}{4}$
- **(C)** $-\frac{1}{4}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{4}$**

**Detailed Solution:**

$\begin{aligned} & f(x)=\int \frac{5 x^8+7 x^6}{\left(x^2+1+2 x^7\right)^2} d x \\ & =\int \frac{5 x^8+7 x^6}{x^{14}\left(\frac{1}{x^5}+\frac{1}{x^7}+2\right)^2} d x \\ & =\int \frac{5 x^{-6}+7 x^{-8}}{\left(\frac{1}{x^5}+\frac{1}{x^7}+2\right)^2} d x \\ & =-\int \frac{d t}{t^2}\left[\text { where } t=\frac{1}{x^5}+\frac{1}{x^7}+2\right] \\ & =\frac{1}{t}+C\end{aligned}$
$\begin{aligned} & =\frac{1}{\left(\frac{1}{x^5}+\frac{1}{x^7}+2\right)}+C \\ & \Rightarrow f(x)=\frac{x^7}{x^2+1+2 x^7}+C \\ & \because f(0)=0 \Rightarrow c=0 \text { i.e. } f(x)=\frac{x^7}{x^2+1+2 x^7} \\ & \Rightarrow f(1)=\frac{1}{4}\end{aligned}$

</details>

---

### Q192. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \sqrt{\frac{1+x}{1-x}} d x=$
(where $C$ is a constant of integration.)

**Options:**

- **(A)** $\sin ^{-1} x-\sqrt{1-x^2}+C$
- **(B)** $\sqrt{1-x^2}-\sqrt{x}+C$
- **(C)** $-\sqrt{1-x^2}+\sqrt{1+x}+C$
- **(D)** $\sin ^{-1} x+\sqrt{1-x^2}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sin ^{-1} x-\sqrt{1-x^2}+C$**

**Detailed Solution:**

$\begin{aligned} & \int \sqrt{\frac{1+x}{1-x}} \mathrm{~d} x=\int \sqrt{\frac{(1+x)^2}{1-x^2}} \mathrm{~d} x=\int\left\{\frac{1}{\sqrt{1-x^2}}+\frac{x}{\sqrt{1-x^2}}\right\} \mathrm{d} x \\ & =\sin ^{-1} x-\frac{1}{2} \times 2 \sqrt{1-x^2} \\ & =\sin ^{-1} x-\sqrt{1-x^2}+C\end{aligned}$

</details>

---

### Q193. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{f}(\mathrm{x})=\int \frac{\mathrm{x}^2+\sin ^2 \mathrm{x}}{1+\mathrm{x}^2}, \sec ^2 \mathrm{x} d \mathrm{x}$ and $\mathrm{f}(0)=0$, then $\mathrm{f}(1)=$

**Options:**

- **(A)** $\frac{\pi}{4}-1$
- **(B)** $\tan 1+\frac{\pi}{4}$
- **(C)** $1-\frac{\pi}{4}$
- **(D)** $\tan 1-\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\tan 1-\frac{\pi}{4}$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{f}(\mathrm{x})=\int \frac{\mathrm{x}^2+\sin ^2 \mathrm{x}}{1+\mathrm{x}^2} \cdot \sec ^2 \mathrm{x} d \mathrm{x} \\ & =\int \frac{1+\mathrm{x}^2+\sin ^2 \mathrm{x}-1}{1+\mathrm{x}^2} \cdot \sec ^2 \mathrm{x} d \mathrm{x} \\ & =\int\left(1-\frac{\cos ^2 \mathrm{x}}{1+\mathrm{x}^2}\right) \sec ^2 \mathrm{x} d \mathrm{x} \\ & =\int \sec ^2 \mathrm{x} d \mathrm{x}-\int \frac{\mathrm{dx}}{1+\mathrm{x}^2} \\ & =\mathrm{f}(\mathrm{x})=\tan \mathrm{x}-\tan ^{-1} \mathrm{x}+\mathrm{C} \\ & \because \mathrm{f}(0)=0 \Rightarrow \mathrm{c}=0\end{aligned}$
So, $\mathrm{f}(\mathrm{x})=\tan \mathrm{x}-\tan ^{-1} \mathrm{X}$
$\Rightarrow \mathrm{f}(1)=\tan 1-\tan ^{-1}(1)=\tan (1)-\frac{\pi}{4}$

</details>

---

### Q194. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{x^{2 x}}{(1+2 x)} d x=$
(where C is a constant of integration.)

**Options:**

- **(A)** $\frac{e^{2 x}}{1+2 x}+C$
- **(B)** $\frac{e^{2 x}}{4(1+2 x)}+C$
- **(C)** $\frac{4 e^{2 x}}{1+2 x}+C$
- **(D)** $\frac{e^{2 x}}{2(1+2 x)}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{e^{2 x}}{4(1+2 x)}+C$**

**Detailed Solution:**

$\int \frac{x \cdot e^{2 x}}{(1+2 x)^2} d x$
Let $2 \mathrm{x}=\mathrm{t} \Rightarrow 2 \mathrm{dx}=\mathrm{dt}$
$\begin{aligned} & =\frac{1}{4} \int \frac{2 \mathrm{x} \cdot \mathrm{e}^{2 \mathrm{x}}}{(1+2 \mathrm{x})^2} \cdot 2 \mathrm{dx} \\ & =\frac{1}{4} \int \frac{\mathrm{te} \mathrm{dt}}{(1+\mathrm{t})^2} \\ & =\frac{1}{4} \int \mathrm{e}^{\mathrm{t}}\left\{\frac{1}{1+\mathrm{t}}-\frac{1}{(1+\mathrm{t})^2}\right\} \mathrm{dt} \\ & =\frac{1}{4} \mathrm{e}^{\mathrm{t}} \cdot \frac{1}{1+\mathrm{t}}+\mathrm{C}\left[\because \int \mathrm{e}^{\mathrm{x}}\left\{\mathrm{f}(\mathrm{x})+\mathrm{f}^{\prime}(\mathrm{x})\right\} \mathrm{dx}=\mathrm{e}^{\mathrm{xf}}(\mathrm{x})+\mathrm{C}\right]\end{aligned}$

</details>

---

### Q195. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{x+1}{x\left(1+x \mathrm{e}^x\right)^2} \mathrm{~d} x=$
(where $C$ is a constant of integration.)

**Options:**

- **(A)** $\log \left(1+x \mathrm{e}^x\right)+\frac{1}{1+x \mathrm{e}^x}+C$
- **(B)** $\log \left(\frac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right)+\frac{1}{1+x \mathrm{e}^x}+C$
- **(C)** $\log \left(\frac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right)+C$
- **(D)** $\log \left(\frac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right)-\frac{1}{1+x \mathrm{e}^x}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log \left(\frac{x \mathrm{e}^x}{1+x \mathrm{e}^x}\right)+\frac{1}{1+x \mathrm{e}^x}+C$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{(x+1) \mathrm{d} x}{x\left(1+x \mathrm{e}^x\right)^2}=\int \frac{\mathrm{e}^x(x+1) \mathrm{d} x}{x \cdot \mathrm{e}^x\left(1+x \mathrm{e}^x\right)^2} \\ & =\int \frac{\mathrm{d} t}{t(1+t)^2} \quad[\operatorname{let} x \cdot \mathrm{e}=t \Rightarrow \mathrm{e}(x+1) \mathrm{d} x=\mathrm{d} t] \\ & =\int\left\{\frac{1}{t}-\frac{1}{1+t}-\frac{1}{(1+t)^2}\right\} \mathrm{d} t \\ & =\log |t|-\log |1+t|+\frac{1}{1+t}+C \\ & =\log \left(\frac{t}{1+t}\right)+\frac{1}{1+t}+C \\ & =\log \left(\frac{x \cdot \mathrm{e}^x}{1+x \cdot \mathrm{e}^x}\right)+\frac{1}{1+x \cdot \mathrm{e}^x}+C\end{aligned}$

</details>

---

### Q196. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \frac{d \theta}{\cos ^2 \theta(\tan 2 \theta+\sec 2 \theta)}=\lambda \tan \theta+2 \log |f(\theta)|+c$
where $\mathrm{C}$ is a constant of integration, then the ordered pair $(\lambda, f(\theta))$ is equal to

**Options:**

- **(A)** $(1,1-\tan \theta)$
- **(B)** $(1,1+\tan \theta)$
- **(C)** $(-1,1-\tan \theta)$
- **(D)** $(-1,1+\tan \theta)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(-1,1+\tan \theta)$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{d \theta}{\cos ^2 \theta(\tan 2 \theta+\sec 2 \theta)}=\int \frac{\sec ^2 \theta d \theta}{\frac{\sin 2 \theta+1}{\cos 2 \theta}} \\ & =\int \frac{\left(\cos ^2 \theta-\sin ^2 \theta\right) \sec ^2 \theta d \theta}{2 \sin \theta \cdot \cos \theta+\sin ^2 \theta+\cos ^2 \theta} \\ & =\int \frac{(\cos \theta+\sin \theta)(\cos \theta-\sin \theta) \sec ^2 \theta d \theta}{(\cos \theta+\sin \theta)^2} \\ & =\int \frac{\cos \theta-\sin \theta}{\cos \theta+\sin \theta} \sec ^2 \theta d \theta\end{aligned}$
$\begin{aligned} & =\int \frac{1-\tan \theta}{1+\tan \theta} \sec ^2 \theta d \theta \quad \quad \text { [dividing } \mathrm{N}^{\mathrm{r}}=\text { and } \Delta^{\mathrm{r}} \text { by } \cos \theta \text { ] } \\ & =\int \frac{1-t}{1+t} d t \quad \quad \text { [let } \tan \theta=t \text { ] } \\ & =\int\left(-1+\frac{2}{1+t}\right) d t \\ & =-t+2 \log |1+t|+C \\ & =-\tan \theta+2 \log |1+\tan \theta|+C \\ & \text { Comparing we get } \lambda=-1 \text { and } f(\theta)=1+\tan \theta\end{aligned}$

</details>

---

### Q197. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int \sqrt{\frac{1-\sqrt{x}}{1+\sqrt{x}}} d x=$
(where $\mathrm{C}$ is a constant of integration)

**Options:**

- **(A)** $-2 \sqrt{1-x}-\cos ^{-1} \sqrt{x}+\sqrt{x(1-x)}$
- **(B)** $-2 \sqrt{1-x}+\cos ^{-1} \sqrt{x}+\sqrt{x(1-x)}$
- **(C)** $2 \sqrt{1-x}+\cos ^{-1} \sqrt{x}+\sqrt{x(1-x)}$
- **(D)** $-2 \sqrt{1-x}+\cos ^{-1} \sqrt{x}-\sqrt{x(1-x)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-2 \sqrt{1-x}+\cos ^{-1} \sqrt{x}+\sqrt{x(1-x)}$**

**Detailed Solution:**

$\begin{aligned} & \int \sqrt{\frac{1-\sqrt{x}}{1+\sqrt{x}}} d x=\int \sqrt{\frac{(1-\sqrt{x})^2}{1-x}} d x \\ & \int \frac{1-\sqrt{x}}{\sqrt{1-x}} d x=\int \frac{d x}{\sqrt{1-x}}-\int \frac{\sqrt{x}}{\sqrt{1-x}} d x \\ & -2 \sqrt{1-x}-\int \frac{\sqrt{\cos ^2 \theta}}{\sqrt{1-\cos ^2 \theta}}(-2 \cos \theta \cdot \sin \theta d \theta)\left[\operatorname{let} x=\cos ^2 \theta\right] \\ & =-2 \sqrt{1-x}+\int 2 \cos ^2 \theta d \theta \\ & \end{aligned}$
$\begin{aligned} & =-2 \sqrt{1-x}+\int(1+\cos 2 \theta) d \theta \\ & =-2 \sqrt{1-x}+\theta+\frac{\sin 2 \theta}{2}+C \\ & =-2 \sqrt{1-x}+\theta+\sin \theta \cdot \cos \theta+C \\ & =-2 \sqrt{1-x}+\cos ^{-1} \sqrt{x}+\sqrt{1-x} \cdot \sqrt{x}+C \\ & =-2 \sqrt{1-x}+\cos ^{-1} \sqrt{x}+\sqrt{x(1-x)}+C\end{aligned}$

</details>

---

### Q198. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{d x}{e^x+e^{-x}+2}=$

**Options:**

- **(A)** $\frac{1}{\mathrm{e}^{2 \mathrm{x}}+1}+\mathrm{c}$
- **(B)** $\frac{-1}{\mathrm{e}^{\mathrm{x}}+1}+\mathrm{c}$
- **(C)** $\frac{1}{\mathrm{e}^{\mathrm{x}}}+\mathrm{c}$
- **(D)** $\frac{-1}{\mathrm{e}^{\mathrm{x}}}+\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-1}{\mathrm{e}^{\mathrm{x}}+1}+\mathrm{c}$**

**Detailed Solution:**

Let
$\begin{aligned}
I & =\int \frac{d x}{e^x+e^{-x}+2} \\
& =\int \frac{d x}{e^x+\frac{1}{e^x}+2}=\int \frac{e^x d x}{e^{2 x}+2 e^x+1}=\int \frac{e^x}{\left(e^x+1\right)^2} d x
\end{aligned}$
Put $\mathrm{e}^{\mathrm{x}}+1=\mathrm{t} \Rightarrow \mathrm{e}^{\mathrm{x}} \mathrm{dx}=\mathrm{dt}$
$I=\int \frac{d t}{t^2}=\int t^2 d t=\frac{t^{-1}}{-1}+c=\frac{-1}{t}+c=\frac{-1}{e^x+1}+c$

</details>

---

### Q199. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \cos ^3 x e^{\log (\sin x)^2} d x=$

**Options:**

- **(A)** $\frac{\sin ^3 x}{3}-\sin ^5 x+c$
- **(B)** $\frac{\sin ^3 x}{3}-\frac{\sin ^5 x}{5}+c$
- **(C)** $\frac{\sin ^3 x}{3}+\frac{\sin ^5 x}{5}+c$
- **(D)** $\sin ^3 x+\sin ^5 x+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\sin ^3 x}{3}-\frac{\sin ^5 x}{5}+c$**

**Detailed Solution:**

$\begin{aligned}
& \text { Let } I=\int \cos ^3 x e^{\log (\sin x)^2} d x \\
& =\int \cos ^3 x(\sin x)^2 d x=\int \cos ^2 x(\sin x)^2 \cos x d x \\
& =\int \cos ^3 x(\sin x)^2 d x=\int \cos ^2 x(\sin x)^2 \cos x d x
\end{aligned}$
Put $\sin x=t \Rightarrow \cos x d x=d t$
$\therefore \mathrm{I}=\int\left(\mathrm{t}^2-\mathrm{t}^4\right) \mathrm{dt}=\frac{\mathrm{t}^3}{3}-\frac{\mathrm{t}^5}{5}+\mathrm{c}=\frac{\sin ^3 \mathrm{x}}{3}-\frac{\sin ^5 \mathrm{x}}{5}+\mathrm{c}$

</details>

---

### Q200. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{d x}{\cos x \sqrt{\cos 2 x}}=$

**Options:**

- **(A)** $\sin ^{-1}(\tan x)+c$
- **(B)** $\frac{1}{2} \log \left|\tan \left(\frac{\pi}{4}+\mathrm{x}\right)\right|+\mathrm{c}$
- **(C)** $2 \log \left|\frac{1+\tan x}{1-\tan x}\right|+c$
- **(D)** $\frac{1}{2} \log \left|\frac{1-\tan x}{1+\tan x}\right|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sin ^{-1}(\tan x)+c$**

**Detailed Solution:**

$$
\begin{aligned}
& \text { Let } I=\int \frac{d x}{\cos x \sqrt{\cos 2 x}} \\
& =\int \frac{d x}{\cos x \cdot \cos x \sqrt{\frac{\cos ^2 x-\sin ^2 x}{\cos ^2 x}}}=\int \frac{d x}{\cos ^2 x \sqrt{1-\tan ^2 x}} \\
& I=\int \frac{\sec ^2 x}{\sqrt{1-\tan ^2 x}} d x
\end{aligned}
$$
Put $\tan x=t \Rightarrow \sec ^2 d x=d t$
$$
\therefore \mathrm{I}=\int \frac{\mathrm{dt}}{\sqrt{1-\mathrm{t}^2}}=\sin ^{-1}(\mathrm{t})+\mathrm{c}=\sin ^{-1}(\tan \mathrm{x})+\mathrm{c}
$$

</details>

---

### Q201. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \frac{\sqrt{x}}{x(x+1)} d x=k \tan ^{-1} m+c$, (where $c$ is constant of integration), then

**Options:**

- **(A)** $\mathrm{k}=1, \mathrm{~m}=\sqrt{\mathrm{x}}$
- **(B)** $\mathrm{k}=2, \mathrm{~m}=\sqrt{\mathrm{x}}$
- **(C)** $\mathrm{k}=1, \mathrm{~m}=\mathrm{x}$
- **(D)** $\mathrm{k}=2, \mathrm{~m}=\mathrm{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{k}=2, \mathrm{~m}=\sqrt{\mathrm{x}}$**

**Detailed Solution:**

$$
I=\int \frac{\sqrt{x}}{x(x+1)} d x
$$
Put $x \tan ^2 \theta \Rightarrow d x=2 \tan \theta \sec ^2 \theta d \theta$
$$
\begin{aligned}
& \therefore I=\int \frac{\tan \theta\left(2 \tan \theta \sec ^2 \theta\right)}{\tan ^2 \theta(1+\tan \theta)} d \theta \\
& =2 \int \frac{\sec ^2 \theta}{\sec ^2 \theta} d \theta=2 \int d \theta=2 \theta \\
& =2 \tan ^{-1} \sqrt{x}+c
\end{aligned}
$$
Comparing with given data, $\mathrm{k}=2, \mathrm{~m}=\sqrt{\mathrm{x}}$

</details>

---

### Q202. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int_0^{\pi / 2} \frac{\cos x}{3 \cos x+\sin x} d x=$

**Options:**

- **(A)** $\frac{3 \pi}{20}-\frac{\log 3}{100}$
- **(B)** $\frac{3 \pi}{10}-\frac{\log 3}{10}$
- **(C)** $\frac{3 \pi}{20}+\frac{\log 3}{10}$
- **(D)** $\frac{3 \pi}{20}-\frac{\log 3}{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{3 \pi}{20}-\frac{\log 3}{10}$**

**Detailed Solution:**

Let $I=\int_0^{\pi / 2} \frac{\cos x}{3 \cos x+\sin x} d x$
Put $\cos x=A(3 \cos x+\sin x)+B \frac{d}{d x}(3 \cos x+\sin x)$
$$
=\mathrm{A}(3 \cos \mathrm{x}+\sin \mathrm{x})+\mathrm{B}(-3 \sin \mathrm{x}+\cos \mathrm{x})
$$
Thus $3 \mathrm{~A}+\mathrm{B}=1$ and $\mathrm{A}-3 \mathrm{~B}=0$
Solving, we get $\mathrm{B}=\frac{1}{10}, \mathrm{~A}=\frac{3}{10}$
$$
\begin{aligned}
& =\frac{3}{10} \int_0^{\frac{\pi}{2}} d x+\frac{1}{10} \int_0^{\frac{\pi}{2}} \frac{d}{\frac{d x}{d x}(3 \cos x+\sin x)} d x \\
& =\frac{3}{10}[x]_0^{\frac{\pi}{2}}+\frac{1}{10}[\log |3 \cos x+\sin x|]_0^{\frac{\pi}{2}} \\
& =\frac{3}{10}\left(\frac{\pi}{2}\right)+\frac{1}{10}[\log |1|-\log |3|] \\
& =\frac{3 \pi}{20}-\frac{1}{10} \log 3 \\
&
\end{aligned}
$$

</details>

---

### Q203. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{10^{\frac{x}{2}}}{10^{-x}-10^x} d x=$

**Options:**

- **(A)** $2 \sqrt{10^{-x}-10^x+c}$
- **(B)** $\frac{1}{\log 10} \sin ^{-1}\left(10^x\right)+c$
- **(C)** $2 \sqrt{10^{-x}+10^x+c}$
- **(D)** $\frac{1}{\log 10} \cos ^{-1}\left(10^x\right)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{\log 10} \sin ^{-1}\left(10^x\right)+c$**

**Detailed Solution:**

Let $I=\int \frac{10^{\frac{x}{2}}}{10^{-x}-10^x} d x$
$$
\begin{aligned}
& =\int \frac{10^{\frac{x}{2}}}{\sqrt{\frac{1}{10^x}-10^x}} d x=\int \frac{10^{\frac{x}{2}}}{\sqrt{\frac{1-\left(10^x\right)^2}{10^x}}} d x \\
& =\int \frac{10^{\frac{x}{2}} \cdot 10^{\frac{x}{2}}}{\sqrt{1-\left(10^x\right)^2}} d x=\int \frac{10^x}{\sqrt{1-\left(10^x\right)^2}} d x
\end{aligned}
$$
Put $10^{\mathrm{x}}=\mathrm{t} \Rightarrow 10^{\mathrm{x}}(\log 10) \mathrm{dx}=\mathrm{dt}$
$$
\therefore \mathrm{I}=\frac{1}{\log 10} \int \frac{\mathrm{dt}}{\sqrt{1-\mathrm{t}^2}}=\frac{1}{\log 10} \sin ^{-1}(\mathrm{t})+\mathrm{c}=\frac{1}{\log 10} \sin ^{-1}\left(10^{\mathrm{x}}\right)+\mathrm{c}
$$

</details>

---

### Q204. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \mathrm{e}^{\left(\mathrm{e}^{\mathrm{x}}+\mathrm{x}\right)} \mathrm{dx}=$

**Options:**

- **(A)** $\mathrm{e}^{\mathrm{x}}+\mathrm{x}+\mathrm{c}$
- **(B)** $\mathrm{e}^{\left(\mathrm{e}^{\mathrm{x}}\right)} \cdot \mathrm{x}+\mathrm{cd}$
- **(C)** $\mathrm{e}^{\left(\mathrm{e}^{\mathrm{x}}\right)}+\mathrm{c}$
- **(D)** $\mathrm{e}^{\left(\mathrm{e}^{\mathrm{x}}\right)}\left(\mathrm{e}^{\mathrm{x}}-1\right)+\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{e}^{\left(\mathrm{e}^{\mathrm{x}}\right)}+\mathrm{c}$**

**Detailed Solution:**

$$
I=\int e^{e^x+x} d x=\int e^{e^x} \cdot e^x d x
$$
Put $\mathrm{e}^{\mathrm{x}}=\mathrm{t} \Rightarrow \mathrm{e}^{\mathrm{x}} \mathrm{dx}=\mathrm{dt}$
$$
\therefore \mathrm{I}=\int \mathrm{e}^{\mathrm{t}} \mathrm{dt}=\mathrm{e}^{\mathrm{t}}+\mathrm{c}=\mathrm{e}^{\mathrm{e}^{\mathrm{x}}}+\mathrm{c}
$$

</details>

---

### Q205. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int \cos ^3 x \cdot e^{\log (\sin x)} d x=$

**Options:**

- **(A)** $\frac{-e^{\sin x}}{4}+c$
- **(B)** $\frac{-\cos ^4 x}{4}+c$
- **(C)** $\frac{-\sin ^4 x}{4}+c$
- **(D)** $\frac{-e^{\sin x}}{4}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-\cos ^4 x}{4}+c$**

**Detailed Solution:**

Let
$$
\begin{aligned}
I & =\int \cos ^3 x \cdot e^{\log (\sin x)} d x \\
& =\int \cos ^3 x \cdot \sin x d x
\end{aligned}
$$
Put $\cos \mathrm{x}=\mathrm{t}$
$$
\therefore I=\int-t^3 d t=\frac{-t^4}{4}+t=\frac{-\cos ^4 x}{4}+c
$$

</details>

---

### Q206. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \frac{(\cos x-\sin x)}{8-\sin 2 x} d x=\frac{1}{p} \log \left[\frac{3+\sin x+\cos x}{3-\sin x-\cos x}\right]+c$, then $\mathrm{p}=($ Where $\mathrm{c}$ is a constant of integration)

**Options:**

- **(A)** 12
- **(B)** $\frac{1}{6}$
- **(C)** 6
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 6**

**Detailed Solution:**

$$
\begin{aligned}
& \text { Let } I=\int \frac{\cos x-\sin x}{8-\sin 2 x} d x \\
& =\int \frac{\cos x-\sin x}{9-1-\sin 2 x} d x=\int \frac{\cos x-\sin x}{9-(1+\sin 2 x)} d x \\
& =\int \frac{\cos x-\sin x}{(3)^2-(\sin x+\cos x)^2} d x
\end{aligned}
$$
Put $\sin x+\cos x=t \Rightarrow(\cos x-\sin x) d x=d t$
$$
\begin{aligned}
& \therefore I=\int \frac{d t}{(3)^2-(t)^2} d x=\frac{1}{3(2)} \log \left|\frac{3+t}{3-t}\right|+c \\
& =\frac{1}{6} \log \left|\frac{3+\sin x+\cos x}{3-\sin x-\cos x}\right|+c \Rightarrow p=6
\end{aligned}
$$

</details>

---

### Q207. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \frac{\operatorname{cosec} x \cdot \cot x}{1+\operatorname{cosec}^2 x} d x=$

**Options:**

- **(A)** $\frac{\pi}{4}-\tan ^{-1} 2$
- **(B)** $\tan ^{-1} 1$
- **(C)** $\tan ^{-1} 2$
- **(D)** $\tan ^{-1}\left(\frac{1}{3}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\tan ^{-1}\left(\frac{1}{3}\right)$**

**Detailed Solution:**

Let $I=\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \frac{\operatorname{cosec} x \cdot \cot x}{1+\operatorname{cosec}^2 x} d x$
Put $\operatorname{cosec} x=t \Rightarrow \operatorname{cosec} x \cot x=-d t$. When $x=\frac{\pi}{6}, t=2$ and when $x=\frac{\pi}{2}, t=1$
$$
\begin{aligned}
& \mathrm{I}=\int_2^1(-1) \frac{\mathrm{dt}}{1+\mathrm{t}^2} \\
& =\int_1^2 \frac{\mathrm{dt}}{1+\mathrm{t}^2}=\left[\tan ^{-1} \mathrm{t}_1^2=\tan ^{-1}(2)-\tan ^{-1}(1)=\tan ^{-1}\left[\frac{2-1}{1+(2)(1)}\right]=\tan ^{-1}\left(\frac{1}{3}\right)\right.
\end{aligned}
$$

</details>

---

### Q208. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\tan ^4 \sqrt{x} \cdot \sec ^2 \sqrt{x}}{\sqrt{x}} d x=$

**Options:**

- **(A)** $\frac{-5}{2}[\tan \sqrt{x}]^5+c$
- **(B)** $[\tan \sqrt{\mathrm{x}}]^5+\mathrm{c}$
- **(C)** $\frac{2}{5}[\tan \sqrt{x}]^5+c$
- **(D)** $\frac{5}{2}[\tan \sqrt{x}]^5+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{5}[\tan \sqrt{x}]^5+c$**

**Detailed Solution:**

$$
\begin{aligned}
& \text { Let } I=\int \frac{\tan ^4 \sqrt{x} \cdot \sec ^2 \sqrt{x}}{\sqrt{x}} d x \\
& \text { Put } \sqrt{x}=t \Rightarrow \frac{1}{2 \sqrt{x}} d x=d t \\
& \therefore I=2 \int \tan ^4 \operatorname{tsec}^2 t d t
\end{aligned}
$$
Put $\tan \mathrm{t}=\mathrm{u} \quad \Rightarrow \sec ^2 \mathrm{tdt}=\mathrm{du}$
$$
\begin{aligned}
& \therefore \mathrm{I}=2 \int \mathrm{u}^4 \mathrm{du} \\
& =\frac{2 \mathrm{u}^5}{5}=\frac{2(\tan \mathrm{t})^5}{5}=\frac{2}{5} \tan ^5 \sqrt{\mathrm{x}}+\mathrm{c}
\end{aligned}
$$

</details>

---

### Q209. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int \sin ^{-1}\left(\frac{2 x}{1+x^2}\right) d x=($ where $|x| < 1)$

**Options:**

- **(A)** $2 \tan ^{-1} x-\log \left|1+x^2\right|+c$
- **(B)** $x \tan ^{-1} x+\log \left|1+x^2\right|+c$
- **(C)** $\tan ^{-1} x+\log \left|1+x^2\right|+c$
- **(D)** $2 x \tan ^{-1} x-\log \left|1+x^2\right|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 x \tan ^{-1} x-\log \left|1+x^2\right|+c$**

**Detailed Solution:**

Let $I=\int \sin ^{-1}\left(\frac{2 x}{1+x^2}\right) d x$
When $x=\tan \theta, \sin ^{-1}\left(\frac{2 x}{1+x^2}\right)=\sin ^{-1}(\sin 2 \theta)=2 \theta$ and
$$
\begin{aligned}
& \mathrm{dx}=\sec ^2 \theta \mathrm{d} \theta \\
& \therefore \mathrm{I}=\int 2 \theta \sec ^2 \theta \mathrm{d} \theta \\
& =2 \int \theta \sec ^2 \theta d \theta=2\left[[\theta \tan \theta]-\int \tan \theta d \theta\right] \\
& =2[\theta \operatorname{tran} \theta+\log |\cos \theta|]+\mathrm{c} \\
& =2\left(\tan ^{-1} \mathrm{x}\right)(\mathrm{x})+2 \log \left|\sqrt{\frac{1}{1+\tan ^2 \theta}}\right|+\mathrm{c} \\
& =2 x \tan ^{-1} x+2 \log \left|\sqrt{\frac{1}{1+x^2}}\right|+c \\
& =2 x \tan ^{-1} x+2 \log \left|1+x^2\right|^{-\frac{1}{2}}+c=2 x \tan ^{-1} x-\log \left|1+x^2\right|+c \\
&
\end{aligned}
$$

</details>

---

### Q210. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{\sec ^8 x}{\operatorname{cosec} x} d x=$

**Options:**

- **(A)** $\frac{\sec ^8 x}{8}+c$
- **(B)** $\frac{\sec ^6 x}{6}+c$
- **(C)** $\frac{\sec ^7 x}{7}+c$
- **(D)** $\frac{\sec ^9 x}{9}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\sec ^7 x}{7}+c$**

**Detailed Solution:**

$$
\begin{aligned}
& \text { Let } I=\int \frac{\sec ^8 x}{\operatorname{cosec} x} d x \\
& =\int\left(\frac{\sin x}{\cos x}\right)\left(\sec ^6 x\right)(\sec x) d x \\
& =\int\left(\sec ^6 x\right)(\sec x)(\tan x) d x
\end{aligned}
$$
Put $\sec \mathrm{x}=\mathrm{t} \Rightarrow \sec \mathrm{x} \tan \mathrm{x} d \mathrm{x}=\mathrm{dt}$
$$
\therefore \mathrm{I}=\int \mathrm{t}^6 \mathrm{dt}=\frac{\mathrm{t}^7}{7}+\mathrm{c}=\frac{\sec ^7 \mathrm{x}}{7}+\mathrm{c}
$$

</details>

---

### Q211. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{1}{x^{\frac{1}{2}}+x^{\frac{1}{3}}} d x=$

**Options:**

- **(A)** $\sqrt{x}-\sqrt[3]{x}+\sqrt[6]{x}-\log |\sqrt[6]{x}+1|+c$
- **(B)** $2 \sqrt{x}-3 \sqrt[3]{x}+6 \sqrt[6]{x}-6 \log |\sqrt[6]{x}+1|+c$
- **(C)** $2 \sqrt{x}+3 \sqrt[3]{x}+6 \sqrt[6]{x}+6 \log |\sqrt[6]{x}+1|+c$
- **(D)** $\sqrt{x}+\sqrt[3]{x}+\sqrt[6]{x}+\log |\sqrt[6]{x}+1|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \sqrt{x}-3 \sqrt[3]{x}+6 \sqrt[6]{x}-6 \log |\sqrt[6]{x}+1|+c$**

**Detailed Solution:**

Let $I=\int \frac{d x}{x^{\frac{1}{2}}+x^{\frac{1}{3}}}$
Put $x^{\frac{1}{6}}=t \Rightarrow x=t^6 \Rightarrow d x=6 t^5$ dt. Also $x^{\frac{1}{2}}=t^3$ and $x^{\frac{1}{3}}=t^2$
$$
\begin{aligned}
& I=6 \int \frac{t^5 d t}{t^2(1+t)} \\
& =6 \int \frac{t^3}{(1+t)} d t=6 \int \frac{\left(t^3+1\right)-1}{(1+t)}=6 \int \frac{(t+1)\left(t^2-t+1\right)}{(1+t)} d t-6 \int \frac{d t}{1+t} \\
& =6 \int\left(t^2-t+1\right) d t-6 \log |1+t|+c=\frac{6 t^3}{3}-\frac{6 t^2}{2}+6 t-6[\log |1+t|]+c \\
& =2 \sqrt{x}-3 \sqrt[3]{x}+6 \sqrt[6]{x}-6 \log |1+\sqrt[6]{x}|+c
\end{aligned}
$$

</details>

---

### Q212. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int[\sin |\log x|+\cos |\log x|] d x=$

**Options:**

- **(A)** $\sin |\log x|+c$
- **(B)** $\cos |\log x|+c$
- **(C)** $x \cos |\log x|+c$
- **(D)** $x \sin |\log x|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x \sin |\log x|+c$**

**Detailed Solution:**

Let $\mathrm{I}=\int[\sin |\log \mathrm{x}|+\cos |\log \mathrm{x}|] \mathrm{dx}$
Put $\log \mathrm{x}=\mathrm{t} \Rightarrow \frac{1}{\mathrm{x}} \mathrm{dx}=\mathrm{dt} \Rightarrow \mathrm{dx}=\mathrm{e}^{\mathrm{t}} \mathrm{dt}$
$$
\begin{aligned}
& \therefore \mathrm{I}=\int(\sin +\cos t) \mathrm{e}^{\mathrm{t}} d t \\
& =\int \mathrm{e}^{\mathrm{t}}(\sin \mathrm{t}+\cos t) d t=\mathrm{e}^{\mathrm{t}} \sin \mathrm{t}+\mathrm{c}=\mathrm{x} \sin |\log \mathrm{x}|+\mathrm{c}
\end{aligned}
$$

</details>

---

### Q213. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\mathrm{x}^3}{\sqrt{1+\mathrm{x}^2}} \mathrm{dx}=\mathrm{a}\left(1+\mathrm{x}^2\right)^{\frac{3}{2}}+\mathrm{b} \sqrt{1+\mathrm{x}^2}+\mathrm{c}$, (where $\mathrm{c}$ is constant of integration) then find the value of $a+b$

**Options:**

- **(A)** $\frac{-2}{3}$
- **(B)** $\frac{-1}{3}$
- **(C)** $\frac{1}{3}$
- **(D)** $\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{-2}{3}$**

**Detailed Solution:**

Let $I=\int \frac{x^3}{\sqrt{1+x^2}} d x=\int \frac{x^2 x}{\sqrt{1+x^2}} d x$
Put $\sqrt{1+\mathrm{x}^2}=\mathrm{t} \Rightarrow 1+\mathrm{x}^2=\mathrm{t}^2 \quad \Rightarrow 2 \mathrm{xdx}=2 \mathrm{t} d \mathrm{t}$
$$
\therefore \mathrm{I}=\int \frac{\left(\mathrm{t}^2-1\right) \mathrm{t} \mathrm{dt}}{\mathrm{t}}=\int\left(\mathrm{t}^2-1\right) \mathrm{dt}=\frac{\mathrm{t}^3}{3}-\mathrm{t}+\mathrm{c}=\frac{\left(1+\mathrm{x}^2\right)^{\frac{3}{2}}}{3}-\sqrt{1-\mathrm{x}^2}+\mathrm{c}
$$
Comparing with given data, $\mathrm{a}=\frac{1}{3}, \mathrm{~b}=-1 \Rightarrow \mathrm{a}+\mathrm{b}=\frac{-2}{3}$

</details>

---

### Q214. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$$
\int e^{\tan x}\left(\sec ^2 x+\sec ^3 x \sin x\right) d x=
$$

**Options:**

- **(A)** $\tan x \cdot e^{\tan x}+c$
- **(B)** $(1+\tan x) e^{\tan }+c$
- **(C)** $\sec x \cdot e^{\tan x}+c$
- **(D)** $\mathrm{e}^{\tan x+\tan x}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\tan x \cdot e^{\tan x}+c$**

**Detailed Solution:**

Let
$$
I=\int e^{\tan x}\left(\sec ^2 x+\sec ^3 x \sin x\right) d x=\int e^{\tan x}\left(\sec ^2 x\right)+(1+\tan x) d x
$$
Put $\tan \mathrm{x}=\mathrm{t} \Rightarrow \sec ^2 \mathrm{xdx}=\mathrm{dt}$
$$
\therefore I=\int \mathrm{e}^{\mathrm{t}}(1+\mathrm{t}) \mathrm{dt}=\mathrm{e}^{\mathrm{t}}(\mathrm{t})+\mathrm{c}=\mathrm{e}^{\tan \mathrm{x}}(\tan \mathrm{x})+\mathrm{c}
$$

</details>

---

### Q215. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{x+\sin x}{1+\cos x} d x=$

**Options:**

- **(A)** $x \tan \left(\frac{x}{2}\right)+c$
- **(B)** $\log (x+\sin x)+c$
- **(C)** $\cot \left(\frac{x}{2}\right)+c$
- **(D)** $\log (1+\cos x)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x \tan \left(\frac{x}{2}\right)+c$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } I=\int \frac{x+\sin x}{1+\cos x} d x=\int \frac{x+\sin x}{2 \cos ^2 \frac{x}{2}} \\ & =\int \frac{x}{2 \cos ^2 \frac{x}{2}} d x+\int \frac{2 \sin \frac{x}{2} \cos \frac{x}{2}}{\cos ^2 \frac{x}{2}} d x=\frac{1}{2} \int x \sec ^2 \frac{x}{2} d x+\int \tan \frac{x}{2} d x \\ & =\frac{1}{2}\left[x \tan \frac{x}{2}(2)-\int 2 \tan \frac{x}{2} d x\right]-2 \log \left|\cos \frac{x}{2}\right|+c \\ & =x \tan \frac{x}{2}+2 \log \left|\cos \frac{x}{2}\right|-2 \log \left|\cos \frac{x}{2}\right|+c=\tan \frac{x}{2}+c\end{aligned}$

</details>

---

### Q216. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{1+\mathrm{x}^2}{1+\mathrm{x}^4} \mathrm{dx}=\frac{1}{\sqrt{2}} \tan ^{-1}\left[\frac{\mathrm{f}(\mathrm{x})}{\sqrt{2}}\right]+\mathrm{c}$, then $\mathrm{f}(\mathrm{x})=$

**Options:**

- **(A)** $x+\frac{1}{x^2}$
- **(B)** $x-\frac{1}{x^2}$
- **(C)** $x+\frac{2}{x}$
- **(D)** $x-\frac{2}{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x-\frac{2}{x}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/e_t5nNjfC7j73q421N6ozWxOhWvDpU1xD0oL0R7QC4o.original.fullsize.png">
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/QH1D92lNVJzo-XKo9FoHyiax8NKQws6svPCiQ6mfu24.original.fullsize.png">

</details>

---

### Q217. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\sin x \cdot \cos x}{\sin ^{4} x+\cos ^{4} x} d x=$

**Options:**

- **(A)** $\tan ^{-1}\left(\sin ^{2} x\right)+c$
- **(B)** $2 \tan ^{-1}\left(\tan ^{2} x\right)+c$
- **(C)** $\frac{1}{2} \tan ^{-1}\left(\tan ^{2} x\right)+c$
- **(D)** $\tan ^{-1}\left(\cos ^{2} x\right)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2} \tan ^{-1}\left(\tan ^{2} x\right)+c$**

**Detailed Solution:**

Let $I=\int \frac{\sin x \cdot \cos x}{\sin ^{4} x+\cos ^{4} x} d x$
Dividing numerator and denominator by $\cos ^{4} x$, we get
$$
I=\int \frac{\tan x \sec ^{2} x}{\tan ^{4} x+1} d x
$$
Put $\tan ^{2} x=t \Rightarrow 2 \tan x \sec ^{2} x d x=d t$
$$
I=\frac{1}{2} \int \frac{d t}{1+t^{2}}=\frac{1}{2} \tan ^{-1} t=\frac{1}{2} \tan ^{-1}\left(\tan ^{2} x\right)+c
$$

</details>

---

### Q218. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{\left(\sin ^{-1} x\right)^{\frac{3}{2}}}{\sqrt{1-x^{2}}} d x=$

**Options:**

- **(A)** $\frac{2}{5}\left(\sin ^{-1} x\right)^{\frac{5}{2}}+c$
- **(B)** $\frac{2}{5}\left(\cos ^{-1} x\right)^{\frac{5}{2}}+c$
- **(C)** $\frac{5}{2}\left(\cos ^{-1} x\right)^{\frac{5}{2}}+c$
- **(D)** $\frac{5}{2}\left(\sin ^{-1} x\right)^{\frac{5}{2}}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2}{5}\left(\sin ^{-1} x\right)^{\frac{5}{2}}+c$**

**Detailed Solution:**

Let $I=\int \frac{\left(\sin ^{-1} x\right)^{\frac{3}{2}}}{\sqrt{1-x^{2}}} d x$
Put $\sin ^{-1} x=t \Rightarrow \frac{1}{\sqrt{1-x^{2}}} d x=d t$
$\begin{aligned} \therefore I &=\int t^{\frac{3}{2}} d t \\ &=\frac{t^{\frac{5}{2}}}{\left(\frac{5}{2}\right)}=\frac{2}{5} t^{\frac{5}{2}}+c=\frac{2}{5}\left(\sin ^{-1} x\right)^{\frac{5}{2}}+c \end{aligned}$

</details>

---

### Q219. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{d x}{1+\sqrt{x}}=$

**Options:**

- **(A)** $2 \sqrt{x}-2 \log |1+\sqrt{x}|+c$
- **(B)** $\sqrt{x}+\log |1+\sqrt{x}|+c$
- **(C)** $2 \sqrt{x}+\log |1+\sqrt{x}|+c$
- **(D)** $\sqrt{x}-\log |1+\sqrt{x}|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \sqrt{x}-2 \log |1+\sqrt{x}|+c$**

**Detailed Solution:**

(C)
Let $\quad \mathrm{I}=\int \frac{\mathrm{dx}}{1+\sqrt{\mathrm{x}}}$
Put $\quad \sqrt{\mathrm{x}}=\mathrm{t} \Rightarrow \frac{1}{2 \sqrt{\mathrm{x}}} \mathrm{dx}=\mathrm{dt} \Rightarrow \mathrm{dx}=2 \mathrm{t} \mathrm{dt}$
$\therefore \mathrm{I}=\int \frac{2 \mathrm{t}}{1+\mathrm{t}} \mathrm{dt}$
$\quad=2 \int \frac{(\mathrm{t}+1)-1}{1+\mathrm{t}} \mathrm{dt}=2 \int \mathrm{dt}-2 \int \frac{\mathrm{dt}}{1+\mathrm{t}}$
$\quad=2 \mathrm{t}-2 \log |1+\mathrm{t}|=2 \sqrt{\mathrm{x}}-2 \log |1+\sqrt{\mathrm{x}}|+\mathrm{c}$

</details>

---

### Q220. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{1+2 e^{-x}}{1-2 e^{-x}} d x=$

**Options:**

- **(A)** $x-\log \left(1-2 e^{-x}\right)+\mathrm{c}$
- **(B)** $\log \left(1-2 e^{-x}\right)+\mathrm{c}$
- **(C)** $x+\log \left(1-2 e^{-x}\right)+\mathrm{c}$
- **(D)** $x+2\log \left(1-2 e^{-x}\right)+\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x+2\log \left(1-2 e^{-x}\right)+\mathrm{c}$**

**Detailed Solution:**

(B)
Let $\begin{aligned} 1 &=\int \frac{1-2 e^{-x}}{1-2 e^{-1}} \\=& \int \frac{1-2 e^{-x}+4 e^{-x}}{1-2 e^{-1}} d x=\int \frac{1-2 e^{-x}}{1-2 e^{-1}} d x+4 \int \frac{e^{-x}}{1-2 e^{-x}} d x \\=& \int d x+\frac{4}{2} \int \frac{2 e^{-x}}{1-2 e^{-x}} d x=x-2 \cdot \log 1-2 e^{-1}-c \end{aligned}$

</details>

---

### Q221. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

f $\int \sqrt{x-\frac{1}{x}}\left(\frac{x^{2}+1}{x^{2}}\right) d x=\frac{2}{3}\left(x-\frac{1}{x}\right)^{k}+c \quad$, then value of k is

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{3}{2}$
- **(C)** $\frac{5}{2}$
- **(D)** $\frac{2}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3}{2}$**

**Detailed Solution:**

(C)
$\begin{array}{l}
\text { Let } \mathrm{I}=\int \sqrt{\mathrm{x}-\frac{1}{\mathrm{x}}}\left(\frac{\mathrm{x}^{2}+1}{\mathrm{x}^{2}}\right) \mathrm{d} \mathrm{x}=\frac{2}{3}\left(\mathrm{x}-\frac{1}{\mathrm{x}}\right)^{\mathrm{k}}+\mathrm{c} \\
\text { Put } \sqrt{\mathrm{x}-\frac{1}{\mathrm{x}}}=\mathrm{t} \Rightarrow \frac{1}{2 \sqrt{\mathrm{x}-\frac{1}{\mathrm{x}}}}\left(1+\frac{1}{\mathrm{x}^{2}}\right) \mathrm{dx}=\mathrm{dt} \\
\therefore\left(\frac{\mathrm{x}^{2}+1}{\mathrm{x}^{2}}\right) \mathrm{d} \mathrm{x}=2 \mathrm{t} \mathrm{dt} \\
\therefore \mathrm{I}=\int \mathrm{t}(2 \mathrm{t}) \mathrm{dt}=2 \int \mathrm{t}^{2} \mathrm{dt}=\frac{2 \mathrm{t}^{3}}{3}=\frac{2}{3}\left[\sqrt{\mathrm{x}-\frac{1}{\mathrm{x}}}\right]^{3} \\
=\frac{2}{3}\left[\left(\mathrm{x}-\frac{1}{\mathrm{x}}\right)^{\frac{1}{2}}\right]^{3}=\frac{2}{3}\left[\mathrm{x}-\frac{1}{\mathrm{x}}\right]^{\frac{3}{2}} \Rightarrow \mathrm{k}=\frac{3}{2}
\end{array}$

</details>

---

### Q222. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int 7^{7^{7^{x}}} 7^{7^{x}} 7^{x} \mathrm{~d} x=$

**Options:**

- **(A)** $7^{7^{7^{x}}}(\log 7)^{3}+C$
- **(B)** $\frac{7^{7^{x}}}{(\log 7)^{2}}+C$
- **(C)** $\frac{7^{7^{x}}}{(\log 7)}+C$
- **(D)** $\frac{7^{7^{7} x}}{(\log 7)^{3}}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{7^{7^{7} x}}{(\log 7)^{3}}+C$**

**Detailed Solution:**

Let I $=\int 7^{7^{7^{x}}} 7^{7^{x}} 7^{x} \mathrm{dx}$
Let $y=7^{7^{7^{x}}}$
$\log y=7^{7^{x}}(\log 7)$
Differentiating w.r.t. x, we get
$$
\frac{1}{y} \frac{d y}{d x}=(\log 7) \frac{d}{d x}\left(7^{7^{x}}\right)
$$
Let $z=7^{7^{x}} \Rightarrow \log z=7^{x} \log 7$
Differentiating w.r.t. $\mathrm{x}$, we get
$$
\begin{aligned}
& \frac{1}{z} \frac{d z}{d x}=7^{x}(\log 7)^{2} \\
\therefore \quad & \frac{d}{d x}\left(7^{7^{x}}\right)=7^{7^{x}} 7^{x}(\log 7)^{2} \Rightarrow \frac{d y}{d x}=7^{7^{7}} 7^{7^{x}} 7^{x}(\log 7)^{3} \\
\therefore \quad I=& \int \frac{d}{d x}\left(7^{7^{7^{x}}}\right) \times \frac{1}{(\log 7)^{3}} d x=\frac{7^{7^{x}}}{(\log 7)^{3}}+C
\end{aligned}
$$

</details>

---

### Q223. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{\cos \sqrt{x}}{\sqrt{x}} d x=$

**Options:**

- **(A)** $\frac{1}{2} \cos \sqrt{x}+\mathrm{c}$
- **(B)** $2 \sin \sqrt{x}+\mathrm{c}$
- **(C)** $\frac{1}{2} \sin \sqrt{x}+\mathrm{c}$
- **(D)** $2 \cos \sqrt{x}+\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \sin \sqrt{x}+\mathrm{c}$**

**Detailed Solution:**

$\begin{aligned} \text { Let } I &=\int \frac{\cos \sqrt{x}}{\sqrt{x}} d x \\ \text { Put } \sqrt{x} &=t \Rightarrow \frac{1}{2 \sqrt{x}} d x=d t \\ \therefore I &=\int \cos t(2) d t \\ &=2 \int \cos t d t=2 \sin t+c=2 \sin \sqrt{x}+c \end{aligned}$

</details>

---

### Q224. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int x^{x}(1+\log x) d x=k x^{x}+c$, then $k=$

**Options:**

- **(A)** $\log _{e} e$
- **(B)** $\log _{e}\left(\frac{1}{e^{2}}\right)$
- **(C)** $\log _{e}\left(e^{2}\right)$
- **(D)** $\log _{e}\left(\frac{1}{e}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\log _{e} e$**

**Detailed Solution:**

Let $I=\int x^{x}(1+\log x) d x$
Put $x^{x}=t \Rightarrow e^{x \log x}=t \Rightarrow e^{x \log x}(1+\log x) d x=d t$ $\therefore x^{x}(1+\log x) d x=d t$
Thus, $I=\int d t=t+c$
$$
I=x^{x}+c
$$
Comparing with given data, we write $k=1=\log _{e} e$

</details>

---

### Q225. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{d x}{\sqrt{(x-1)(x-2)}}=$

**Options:**

- **(A)** $\log \left|\left(x-\frac{3}{2}\right)-\sqrt{x^{2}-3 x+2}\right|+c$
- **(B)** $\log \left|\left(x-\frac{3}{2}\right)+\sqrt{x^{2}-3 x+2}\right|+c$
- **(C)** $\log \left|(x-1)+\sqrt{x^{2}-3 x+2}\right|+c$
- **(D)** $\log \left|\left(x+\frac{3}{2}\right)+\sqrt{x^{2}-3 x+2}\right|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log \left|\left(x-\frac{3}{2}\right)+\sqrt{x^{2}-3 x+2}\right|+c$**

**Detailed Solution:**

$\begin{aligned} I &=\int \frac{\mathrm{dx}}{\sqrt{(\mathrm{x}-1)(\mathrm{x}-2)}}=\int \frac{\mathrm{dx}}{\sqrt{\mathrm{x}^{2}-3 \mathrm{x}+2}} \\ &=\int \frac{\mathrm{dx}}{\sqrt{\left(\mathrm{x}^{2}-3 \mathrm{x}+\frac{9}{4}\right)-\frac{1}{4}}}=\int \frac{\mathrm{dx}}{\sqrt{\left(\mathrm{x}-\frac{3}{2}\right)^{2}-\left(\frac{1}{2}\right)^{2}}} \\ &=\log \left(x-\frac{3}{2}\right)+\sqrt{\mathrm{x}^{2}-3 \mathrm{x}+2} \mid+\mathrm{c} \end{aligned}$

</details>

---

### Q226. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int\left[\frac{(1+\log x)}{\cos ^{2}(x \log x)}\right] d x=$

**Options:**

- **(A)** $\sin (x \log x)+c$
- **(B)** $\sin ^{2}(x \log x)+c$
- **(C)** $\log (x \log x)+c$
- **(D)** $\tan (x \log x)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\tan (x \log x)+c$**

**Detailed Solution:**

$I=\int \frac{(1+\log x)}{\cos ^{2}(x \log x)} d x$
Put $x \log x=t \Rightarrow\left[x \cdot \frac{1}{x}+\log x(1)\right] d x=d t \Rightarrow(1-\log x) d x=d t$
$1=\int \frac{1}{\cos ^{2} t} d t=\int \sec ^{2} t d t=\tan t+c$
$=\tan (x \log x)-c$

</details>

---

### Q227. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{\sec x}{\sqrt{\log (\sec x+\tan x)}} d x=$

**Options:**

- **(A)** $\sqrt{\log (\sec x+\tan x)}+c$
- **(B)** $\sqrt{\sec x+\tan x)}+c$
- **(C)** $2 \sqrt{\sec x+\tan x}+c$
- **(D)** $2 \sqrt{\log (\sec x+\tan x)}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 \sqrt{\log (\sec x+\tan x)}+c$**

**Detailed Solution:**

Let $I=\int \frac{\sec x}{\sqrt{\log (\sec x+\tan x)}} d x$
Put $\log (\sec x+\tan x)=t \Rightarrow \frac{1}{\sec x+\tan x}\left(\sec x \tan x+\sec ^{2} x\right) d x=d t$
$\begin{aligned} & \frac{\sec x(\sec x+\tan x)}{\sec x+\tan x} \mathrm{dx}=\mathrm{dt} \Rightarrow \sec x \mathrm{dx}=\mathrm{dt} \\ \therefore \quad \mathrm{I} &=\int \frac{\mathrm{dt}}{\sqrt{\mathrm{t}}}=\int \mathrm{t}^{-\frac{1}{2}} \mathrm{dt}=\frac{\mathrm{t}^{\frac{1}{2}}}{\left(\frac{1}{2}\right)}+\mathrm{c} \\ &=2 \sqrt{\mathrm{t}}+\mathrm{c}=2 \sqrt{\log (\sec x+\tan x)}+\mathrm{c} \end{aligned}$

</details>

---

### Q228. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{5^{x}}{\sqrt{5(-2 x)-5^{(2 x)}}} d x=$

**Options:**

- **(A)** $\sin ^{-1}\left(5^{2 x}\right)+c$
- **(B)** $\frac{\sin ^{-1}\left(5^{2 x}\right)}{\log 25}+c$
- **(C)** $\tan ^{-1}\left(5^{x}\right)+c$
- **(D)** $\tan ^{-1}\left(5^{2 x}\right) \cdot \log 25+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\sin ^{-1}\left(5^{2 x}\right)}{\log 25}+c$**

**Detailed Solution:**

Let
$\begin{aligned} I &=\int \frac{5^{x}}{\sqrt{\left(5^{2 x}\right)^{-1}-5^{2 x}}} d x \\ &=\int \frac{5^{x}}{\sqrt{\left(\frac{1}{5^{2 x}}\right)-5^{2 x}}} d x=\int \frac{5^{x} \cdot 5^{x}}{\sqrt{1-\left(5^{2 x}\right)}} d x \end{aligned}$
Put $5^{2 \mathrm{x}}=\mathrm{t} \Rightarrow(2 \log 5) 5^{2 \mathrm{x}} \mathrm{dx}=\mathrm{dt} \Rightarrow 5^{\mathrm{x}} \cdot 5^{\mathrm{x}} \mathrm{dx}=\frac{\mathrm{dt}}{\log 25}$
$\begin{aligned} \therefore \mathrm{I} &=\int \frac{1}{\sqrt{1-\mathrm{t}^{2}}} \times \frac{\mathrm{dt}}{(\log 25)}=\frac{1}{\log 25} \int \frac{\mathrm{dt}}{\sqrt{1-\mathrm{t}^{2}}} \mathrm{dt} \\ &=\frac{1}{\log 25} \sin ^{-1} \mathrm{t}+\mathrm{c}=\frac{1}{\log 25} \sin ^{-1}\left(5^{2 \mathrm{x}}\right)+\mathrm{c} \end{aligned}$

</details>

---

### Q229. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{d x}{(x+2) \sqrt{x+1}}=$

**Options:**

- **(A)** $\tan ^{-1}(\sqrt{x+1})+c$
- **(B)** $2 \tan ^{-1}(\sqrt{x+1})+c$
- **(C)** $2 \tan ^{-1}(\sqrt{x+2})+c$
- **(D)** $\tan ^{-1}(\sqrt{x+2})+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \tan ^{-1}(\sqrt{x+1})+c$**

**Detailed Solution:**

Let $I=\int \frac{d x}{(x+2) \sqrt{x+1}}$
Put $\sqrt{x+1}=t \Rightarrow(x+1)=t^{2}$ and $d x=2 t d t$
$\therefore I=\int \frac{2 t d t}{\left(t^{2}+1\right) t}$
$\quad=2 \int \frac{d t}{t^{2}+1}=2 \tan ^{-1} t+c=2 \tan ^{-1}(\sqrt{x+1})+c$

</details>

---

### Q230. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{d x}{\cos x \sqrt{\cos 2 x}}=$

**Options:**

- **(A)** $\frac{1}{2} \log \left|\tan \left(\frac{\pi}{4}+x\right)\right|+c$
- **(B)** $\frac{1}{2} \log \left|\frac{1-\tan x}{1+\tan x}\right|+c$
- **(C)** $2 \log \left|\frac{1+\tan x}{1-\tan x}\right|+c$
- **(D)** $\sin ^{-1}(\tan x)+\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sin ^{-1}(\tan x)+\mathrm{c}$**

**Detailed Solution:**

Let 
$\begin{aligned} I &=\int \frac{d x}{\cos x \sqrt{\cos 2 x}} \\ &=\int \frac{d x}{\cos x \cdot \cos x \sqrt{\frac{\cos ^{2} x-\sin ^{2} x}{\cos ^{2} x}}}=\int \frac{d x}{\cos ^{2} x \sqrt{1-\tan ^{2} x}} \\ I &=\int \frac{\sec ^{2} x}{\sqrt{1-\tan ^{2} x}} d x \end{aligned}$
Put $\tan x=t \quad \Rightarrow \sec ^{2} d x=d t$
$\therefore I=\int \frac{d t}{\sqrt{1-t^{2}}}=\sin ^{-1}(t)+c=\sin ^{-1}(\tan x)+c$

</details>

---

### Q231. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int e^{\cos ^{-1} x}\left[\frac{x-\sqrt{1-x^{2}}}{\sqrt{1-x^{2}}}\right] d x=$

**Options:**

- **(A)** $-e^{\sin ^{-1} x}+c$
- **(B)** $-x e^{\cos ^{-1} x}+c$
- **(C)** $-x e^{\sin ^{-1} x}+c$
- **(D)** $-e^{\cos ^{-1} x}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-x e^{\cos ^{-1} x}+c$**

**Detailed Solution:**

Put $\cos ^{-1} x=t \Rightarrow \frac{-1}{\sqrt{1-x^{2}}} d x=d t \Rightarrow \frac{1}{\sqrt{1-x^{2}}} d x=-d t$ and $x=\cos t$
$\begin{aligned} I &=-\int e^{t}[\cos t-\sin t] d t=-e^{t} \cos t+c \\ &=-e^{\cos ^{-1} x} \cos \left(\cos ^{-1} x\right)+c=-x e^{\cos ^{-1} x}+c \end{aligned}$

</details>

---

### Q232. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo></mrow></mrow></math> ________

**Options:**

- **(A)** <math><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><mi>x</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mn>2</mn><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(C)** <math><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(D)** <math><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>+</mo><mi>c</mi></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mn>2</mn><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>+</mo><mi>c</mi></mrow></mrow></math>**

**Detailed Solution:**

Let <math><mi>I</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math> put <math><mo> </mo><mi>x</mi><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>θ</mi></math>  
<math><mi>I</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi><mi>d</mi><mi>θ</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>θ</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>∫</mo><mn>2</mn><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi><mi>d</mi><mi>θ</mi></math>  
<math><mi>I</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>∫</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>θ</mi></mrow></mfenced><mi>d</mi><mi>θ</mi></math>  
<math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfrac><mrow><mn>2</mn><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></mrow></mfrac></mrow></mfenced></math>  
<math><mi>I</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfrac><mrow><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mi>c</mi></math>

</details>

---

### Q233. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mi>x</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mrow></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo></math> ________

**Options:**

- **(A)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mi>x</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mi>x</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(B)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(C)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mi>x</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(D)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>**

**Detailed Solution:**

Let,  <math><mi>I</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo> </mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac></math>  
<math><mo>=</mo><mo>∫</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>+</mo><mi>x</mi><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>x</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math>  
<math><mo>=</mo><mo>∫</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math>  
<math><mo> </mo><mo> </mo><mi mathvariant="normal">l</mi><mi>n</mi><mi>x</mi><mo>-</mo><mi>l</mi><mi>n</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mi>c</mi></math>  
<math><mo> </mo><mo>=</mo><mi>l</mi><mi>n</mi><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>-</mo><mi>c</mi></math>

</details>

---

### Q234. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<math><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo></math> ________

**Options:**

- **(A)** <math><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>-</mo><mi>a</mi><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>a</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(B)** <math><mi>x</mi><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>a</mi></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mi>a</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(C)** <math><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>+</mo><mi>a</mi><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mi>a</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(D)** <math><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>-</mo><mi>a</mi><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>a</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>**

**Detailed Solution:**

Let <math><mi>I</mi><mo>=</mo><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi></math> put <math><mi>x</mi><mo>=</mo><mi>a</mi><mrow><mrow><mi mathvariant="normal">secθ</mi></mrow><mo>⁡</mo><mrow></mrow></mrow></math>  
<math><mi>d</mi><mi>x</mi><mi></mi><mo>=</mo><mi></mi><mi>a</mi><mrow><mrow><mi mathvariant="normal">secθ</mi></mrow><mo>⁡</mo><mrow></mrow></mrow><mi></mi><mrow><mrow><mi mathvariant="normal">tanθ</mi></mrow><mo>⁡</mo><mrow></mrow></mrow></math>  
<math><mi>a</mi><mrow><mo stretchy="false">∫</mo><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><msup><mrow><mi mathvariant="normal">c</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>θ</mi><mo>=</mo><mi>a</mi><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mo>-</mo><mi>θ</mi></mrow></mfenced></mrow></mrow><mo>+</mo><mi>c</mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mo>&#8658;</mo><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>-</mo><mi>a</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><msup><mrow><mi mathvariant="normal">c</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mi>x</mi></mrow><mrow><mi>a</mi></mrow></mfrac><mo>+</mo><mi>c</mi></math>

</details>

---

### Q235. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<math><mo>∫</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo></math>

**Options:**

- **(A)** <math><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></math>
- **(B)** <math><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>+</mo><mi>c</mi></math>
- **(C)** <math><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>c</mi></math>
- **(D)** <math><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

Let l = <math><mo>∫</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math>  
<math><mo>=</mo><mo>∫</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mn>1</mn></mrow></mfrac></math>  
Put <math><mi>x</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>=</mo><mi>t</mi></math>  
<math><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math>  
<math><mo>∴</mo><mi>l</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced><mo>+</mo><mi>c</mi></math>  
<math><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></math>

</details>

---

### Q236. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math><mo>∫</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mo>⁡</mo><mo>(</mo><mi>x</mi><mo>-</mo><mi>α</mi><mo>).</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mo>⁡</mo><mo>(</mo><mi>x</mi><mo>+</mo><mi>α</mi><mo>)</mo><mo>.</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>p</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mo>|</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mn>2</mn><mi>x</mi><mo>|</mo><mo>+</mo><mi>q</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mo>|</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mo>⁡</mo><mo>(</mo><mi>x</mi><mo>+</mo><mi>α</mi><mo>)</mo><mo>+</mo><mi>r</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mo>|</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mo>⁡</mo><mo>(</mo><mi>x</mi><mo>-</mo><mi>α</mi><mo>)</mo><mo>|</mo><mo>+</mo><mi>c</mi></math> then <math><mi>p</mi><mo>+</mo><mi>q</mi><mo>+</mo><mi>r</mi></math> = ……

**Options:**

- **(A)** <math><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

We have, 
<math><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mrow><mo stretchy="false">∫</mo><mrow><mrow><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mi mathvariant="normal">a</mi><mo>)</mo><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>α</mi></mrow></mfenced></mrow></mrow><mo>.</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>x</mi><mi></mi><mi>d</mi><mi>x</mi></mrow></mrow></math>  
<math><mo>=</mo><mi>p</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mfenced close="|" open="|" separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mi>q</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfenced></mrow></mrow></mrow></mfenced><mo>+</mo><mi>r</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>a</mi></mrow></mfenced></mrow></mrow></mrow></mfenced><mo>+</mo><mi>C</mi></math>  
<math><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>x</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>α</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>α</mi></mrow></mfenced></mrow></mfenced></mrow></mrow></math>  
<math><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mo>⁡</mo><mo>(</mo><mi>x</mi><mo>-</mo><mi>α</mi><mo>)</mo><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mo>⁡</mo><mo>(</mo><mi>x</mi><mo>+</mo><mi>α</mi><mo>)</mo><mo>]</mo></math>  
<math><mn>1</mn><mo>-</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>α</mi></mrow></mfenced></mrow></mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>α</mi></mrow></mfenced></mrow></mrow></math>  
<math><mo>&#8658;</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>x</mi><mo>-</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>x</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>α</mi></mrow></mfenced><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>α</mi></mrow></mfenced></mrow></mrow></math>  
<math><mo>=</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>α</mi></mrow></mfenced></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>α</mi></mrow></mfenced></mrow></mrow></math>  
<math><mo>&#8658;</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>α</mi></mrow></mfenced></mrow></mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>α</mi></mrow></mfenced></mrow></mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>x</mi></math>  
<math><mo>&#8658;</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>x</mi><mo>-</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>α</mi></mrow></mfenced></mrow></mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>α</mi></mrow></mfenced></mrow></mrow></math>  
<math><mo>∴</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mrow><mo stretchy="false">∫</mo><mrow><mrow><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mi mathvariant="normal">a</mi><mo>)</mo><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>α</mi></mrow></mfenced></mrow></mrow><mo>.</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>x</mi><mi></mi><mi>d</mi><mi>x</mi></mrow></mrow></math>  
<math><mfrac><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mrow></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mo>⁡</mo><mo>|</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mo>⁡</mo><mo>(</mo><mi>x</mi><mo>-</mo><mi>α</mi><mo>)</mo><mo>|</mo><mo>-</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mo>⁡</mo><mo>|</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mo>⁡</mo><mo>(</mo><mi>x</mi><mo>+</mo><mi>α</mi><mo>)</mo><mo>+</mo><mi>C</mi></math>  
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mrow><mo>+</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>α</mi></mrow></mfenced></mrow></mrow></mrow></mfenced></mrow></mrow></math> + <math><mi></mi><mo>+</mo><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mo>⁡</mo><mo>|</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mo>⁡</mo><mo>(</mo><mi>x</mi><mo>-</mo><mi>α</mi><mo>)</mo><mo>+</mo><mi>C</mi></math>  
<math><mo>∴</mo><mi>p</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi>g</mi><mo>-</mo><mn>1</mn></math> and <math><mi>r</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>  
<math><mo>∴</mo><mi>p</mi><mo>+</mo><mi>q</mi><mo>+</mo><mi>r</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mn>2</mn><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

</details>

---

### Q237. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<math><mo>∫</mo><mfrac><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mrow><mn>8</mn><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>p</mi></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>3</mn><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow><mrow><mn>3</mn><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><mi>c</mi></math> , then p =……

**Options:**

- **(A)** 6
- **(B)** 1
- **(C)** 3
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 6**

**Detailed Solution:**

<math><mo>∫</mo><mfrac><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mrow><mn>8</mn><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>p</mi></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>3</mn><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow><mrow><mn>3</mn><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><mi>C</mi></math>  
Now, <math><mo>=</mo><mo>∫</mo><mfrac><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mrow><mn>9</mn><mo>-</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math>  
<math><mo>=</mo><mo>∫</mo><mfrac><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mrow><mn>9</mn><mo>-</mo><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi><mo>+</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math>  
<math><mo>=</mo><mo>∫</mo><mfrac><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math>  
Put <math><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>=</mo><mi>t</mi></math>  
<math><mfenced separators="|"><mrow><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math>  
<math><mo>=</mo><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mn>3</mn><mo>+</mo><mi>t</mi></mrow><mrow><mn>3</mn><mo>-</mo><mi>t</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><mi>C</mi></math>  
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mn>3</mn><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow><mrow><mn>3</mn><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><mi>C</mi></math>  
<math><mo>∴</mo><mi>p</mi><mo>=</mo><mn>6</mn></math>

</details>

---

### Q238. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<math><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>=</mo></math>

**Options:**

- **(A)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfenced></mrow></mrow><mo>+</mo><mi>c</mi></math>
- **(B)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><mi>c</mi></math>
- **(C)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow><mrow><mn>2</mn><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><mi>c</mi></math>
- **(D)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

Let <math><mi>l</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></mfenced></mrow></mfrac></math>
<math><mo>=</mo><mo>∫</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi></mrow><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math>
Put <math><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>=</mo><mi>t</mi></math>
<math><mo>⇒</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></math>
<math><mi mathvariant="normal">H</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi></math> , <math><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>A</mi></mrow><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>B</mi></mrow><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfrac></math>
<math><mo>⇒</mo><mn>1</mn><mo>=</mo><mi>A</mi><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>B</mi><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>
Put <math><mi>t</mi><mo>=</mo><mo>-</mo><mn>2</mn></math>
<math><mo>∴</mo><mn>1</mn><mo>=</mo><mi>B</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>⇒</mo><mi>B</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>
<math><mo>∴</mo><mi mathvariant="normal">P</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">t</mi><mi></mi><mi>t</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>⇒</mo><mi>t</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>
<math><mo>∴</mo><mn>1</mn><mo>=</mo><mi>A</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>⇒</mo><mi>A</mi><mo>=</mo><mn>1</mn></math>
<math><mi mathvariant="normal">N</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">w</mi></math> , <math><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mo>∫</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><mo>-</mo><mo>∫</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mi>d</mi><mi>t</mi></math>
<math><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mrow><mo>+</mo><mi>C</mi></math>
<math><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><mi>C</mi></math>
<math><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><mi>C</mi></math>

</details>

---

### Q239. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math><mo>∫</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">t</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>A</mi><mi>x</mi><mo>+</mo><mi>B</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mfenced close="|" open="|" separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mi>c</mi></math> then <math><mi>A</mi><mo>+</mo><mi>B</mi><mo>=</mo></math> …

**Options:**

- **(A)** 1
- **(B)** – 1
- **(C)** 0
- **(D)** – 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

Let <math><mi>l</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">t</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math>  
<math><mo>=</mo><mo>∫</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></mfrac></mrow></mfrac><mi>d</mi><mi>x</mi></math>  
<math><mo>=</mo><mo>∫</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math>  
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>∫</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math>  
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>∫</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math>  
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>∫</mo><mfrac><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math>  
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>[</mo><mo>∫</mo><mi>d</mi><mi>x</mi><mo>+</mo><mo>∫</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math>  
Let <math><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>=</mo><mi>t</mi></math>  
<math><mo>&#8658;</mo><mfenced separators="|"><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math>  
<math><mo>∴</mo><mi>l</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mo>∫</mo><mi>d</mi><mi>x</mi><mo>+</mo><mo>∫</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>t</mi></mrow></mfrac><mi>d</mi><mi>t</mi></mrow></mfenced></math>  
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>t</mi></mrow></mfenced></mrow></mrow></mrow></mfenced><mo>+</mo><mi>C</mi></math>  
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfenced></mrow></mrow></mrow></mfenced><mo>+</mo><mi>C</mi></math>  
<math><mo>=</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfenced></mrow></mrow><mo>+</mo><mi>C</mi></math>  
Here, <math><mi>A</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi>B</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>  
<math><mo>∴</mo><mi mathvariant="normal"></mi><mi>A</mi><mo>+</mo><mi>B</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mn>1</mn></math>

</details>

---

### Q240. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math><msup><mrow><mo>∫</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi><mo>.</mo><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>e</mi><mi>x</mi></mrow></mfenced></mrow></mrow></mrow></mfenced></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mo>…</mo></math>

**Options:**

- **(A)** <math><mfrac><mrow><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>c</mi></math>
- **(B)** <math><mi>x</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mi>c</mi></math>
- **(C)** <math><mi>x</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mi>c</mi></math>
- **(D)** <math><mfrac><mrow><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

Let <math><mi>l</mi><mo>=</mo><mo>∫</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mo>×</mo><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>e</mi><mi>x</mi></mrow></mfenced></mrow></mrow></mrow></mfenced></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><mi>d</mi><mi>x</mi></math>  
<math><mo>=</mo><mo>∫</mo><mfrac><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>e</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math>  
<math><mo>=</mo><mo>∫</mo><mfrac><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>e</mi><mo>+</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math>  
<math><mo>=</mo><mo>∫</mo><mfrac><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math>  
<math><mi mathvariant="normal">P</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal"></mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup></math>  
<math><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup><mi>d</mi><mi>t</mi></math>  
<math><mo>=</mo><mo>∫</mo><mfrac><mrow><mi>t</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup><mi>d</mi><mi>t</mi></math>  
<math><mo>=</mo><mo>∫</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi></math>  
<math><mo>=</mo><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup></mrow><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfrac><mo>+</mo><mi>C</mi></math>  
<math><mo>=</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mi>C</mi></math>

</details>

---

### Q241. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `1`

<math><mrow><mo stretchy="false">∫</mo><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>2</mn><mo>+</mo><mrow><mrow><mi mathvariant="italic">sin</mi></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mrow><mrow><mi mathvariant="italic">cos</mi></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mi> </mi><mi>d</mi><mi>x</mi><mo>=</mo></mrow></mrow></math>

**Options:**

- **(A)** <math><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mi>C</mi></mrow></mrow></math>
- **(B)** <math><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mi>C</mi></mrow></mrow></math>
- **(C)** <math><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mi>C</mi></mrow></mrow></math>
- **(D)** <math><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mi>C</mi></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mi>C</mi></mrow></mrow></math>**

**Detailed Solution:**

<math> <mrow> <mi>I</mi><mo>=</mo><mstyle displaystyle="true"> <mrow><mo>∫</mo> <mrow> <msup> <mi>e</mi> <mi>x</mi> </msup> <mrow><mo>(</mo> <mrow> <mfrac> <mrow> <mn>2</mn><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow> <mrow> <mn>2</mn><msup> <mrow> <mi>cos</mi></mrow> <mn>2</mn> </msup> <mi>x</mi></mrow> </mfrac> </mrow> <mo>)</mo></mrow><mi>d</mi><mi>x</mi></mrow> </mrow> </mstyle></mrow> </math>
<math> <mrow> <mi>I</mi><mo>=</mo><mstyle displaystyle="true"> <mrow><mo>∫</mo> <mrow> <msup> <mi>e</mi> <mi>x</mi> </msup> <mrow><mo>(</mo> <mrow> <mi>tan</mi><mi>x</mi><mo>+</mo><msup> <mrow> <mi>sec</mi></mrow> <mn>2</mn> </msup> <mi>x</mi></mrow> <mo>)</mo></mrow><mi>d</mi><mi>x</mi></mrow> </mrow> </mstyle></mrow> </math>
<math> <mrow> <mi>I</mi><mo>=</mo><msup> <mi>e</mi> <mi>x</mi> </msup> <mi>tan</mi><mi>x</mi><mo>+</mo><mi>C</mi></mrow> </math>
<math> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <mo>∵</mo> <mo>∫</mo> <msup> <mtext>e</mtext> <mtext>x</mtext> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mtext>f</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mtext>x</mtext> </mrow> </mfenced> <mo>+</mo> <msup> <mtext>f</mtext> <mo>′</mo> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mtext>x</mtext> </mrow> </mfenced> </mrow> </mfenced> <mtext>dx</mtext> <mo>=</mo> <msup> <mtext>e</mtext> <mtext>x</mtext> </msup> <mo>·</mo> <mtext>f</mtext> <mo>+</mo> <mtext>C</mtext> </mrow> </mfenced> </mrow> </math>

</details>

---

### Q242. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `1`

If <math><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msqrt><mn>16</mn><mo>-</mo><mn>9</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac><mo>=</mo><mi>A</mi><mrow><mrow><msup><mrow><mi mathvariant="italic">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>B</mi><mi>x</mi></mrow></mfenced></mrow></mrow><mo>+</mo><mi>C</mi></math> then <math><mi>A</mi><mo>+</mo><mi>B</mi><mo>=</mo></math>

**Options:**

- **(A)** <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>19</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math> <mrow> <mi>I</mi><mo>=</mo><mstyle displaystyle="true"> <mrow><mo>∫</mo> <mrow> <mfrac> <mrow> <mi>d</mi><mi>x</mi></mrow> <mrow> <msqrt> <mrow> <msup> <mn>4</mn> <mn>2</mn> </msup> <mo>−</mo><msup> <mrow> <mrow><mo>(</mo> <mrow> <mn>3</mn><mi>x</mi></mrow> <mo>)</mo></mrow></mrow> <mn>2</mn> </msup> </mrow> </msqrt> </mrow> </mfrac> </mrow> </mrow> </mstyle></mrow> </math>
<math> <mrow> <mi>I</mi><mo>=</mo><mfrac> <mn>1</mn> <mn>3</mn> </mfrac> <msup> <mrow> <mi>sin</mi></mrow> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> <mrow><mo>(</mo> <mrow> <mfrac> <mrow> <mn>3</mn><mi>x</mi></mrow> <mn>4</mn> </mfrac> </mrow> <mo>)</mo></mrow><mo>+</mo><mi>C</mi></mrow> </math>
<math> <mrow> <mi>A</mi><mo>+</mo><mi>B</mi><mo>=</mo><mfrac> <mn>1</mn> <mn>3</mn> </mfrac> <mo>+</mo><mfrac> <mn>3</mn> <mn>4</mn> </mfrac> <mo>=</mo><mfrac> <mrow> <mn>4</mn><mo>+</mo><mn>9</mn></mrow> <mrow> <mn>12</mn></mrow> </mfrac> <mo>=</mo><mfrac> <mrow> <mn>13</mn></mrow> <mrow> <mn>12</mn></mrow> </mfrac> </mrow> </math>

</details>

---

### Q243. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

<math><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>8</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mrow><mrow><mi mathvariant="normal">cosec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo></mrow></mrow></math>

**Options:**

- **(A)** <math><mfrac><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>8</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mn>8</mn></mrow></mfrac><mo>+</mo><mi>c</mi></math>
- **(B)** <math><mi> </mi><mfrac><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>7</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mn>7</mn></mrow></mfrac><mo>+</mo><mi>c</mi></math>
- **(C)** <math><mfrac><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>6</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mn>6</mn></mrow></mfrac><mo>+</mo><mi>c</mi></math>
- **(D)** <math><mfrac><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>9</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mn>9</mn></mrow></mfrac><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi> </mi><mfrac><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>7</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mn>7</mn></mrow></mfrac><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

<math>  <mrow>   <mi>I</mi><mo>=</mo><mstyle displaystyle='true'>    <mrow><mo>&#x222B;</mo>     <mrow>      <mfrac>       <mrow>        <msup>         <mrow>          <mi>sec</mi></mrow>         <mn>8</mn>        </msup>        <mi>x</mi></mrow>       <mrow>        <mtext>cosec</mtext><mtext>&#x2009;</mtext><mi>x</mi></mrow>      </mfrac>      </mrow>    </mrow>       </mstyle><mi>d</mi><mi>x</mi></mrow></math> 
Let <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>=</mo><mi>t</mi></mrow></mrow></math>
<math><mo>-</mo><mi> </mi><mi>s</mi><mi>i</mi><mi>n</mi><mi>x</mi><mi> </mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math>
<math><mi>I</mi><mo>=</mo><mi> </mi><mrow><mo stretchy="false">∫</mo><mrow><mo>-</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><msup><mrow><mi>t</mi></mrow><mrow><mn>8</mn></mrow></msup></mrow></mfrac></mrow></mrow></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>7</mn></mrow></mfrac><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>t</mi></mrow><mrow><mn>7</mn></mrow></msup></mrow></mfrac><mo>+</mo><mi>c</mi></math>
<math><mo>=</mo><mfrac><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>7</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mn>7</mn></mrow></mfrac><mo>+</mo><mi>c</mi></math>

</details>

---

### Q244. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `2`

If <math><mrow><mo stretchy="false">∫</mo><mrow><msqrt><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfrac></msqrt></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mi>A</mi><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>35</mn></msqrt><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi><mo>-</mo><mn>6</mn><mo>+</mo><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>35</mn></msqrt></mrow></mfenced><mo>+</mo><mi>C</mi></mrow></mrow></math> then <math><mi>A</mi><mo>=</mo><mi> </mi></math>

**Options:**

- **(A)** <math><mo>-</mo><mn>1</mn></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>1</mn></math>**

**Detailed Solution:**

<math><mrow><mo stretchy="false">∫</mo><mrow><msqrt><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfrac><mi> </mi></msqrt></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mi> </mi><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mi> </mi><mo>-</mo><mi> </mi><mn>12</mn><mi>x</mi><mi> </mi><mo>+</mo><mi> </mi><mn>35</mn></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mn>2</mn><mi>x</mi><mi> </mi><mo>-</mo><mi> </mi><mn>10</mn></mrow><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mi> </mi><mo>-</mo><mi> </mi><mn>12</mn><mi>x</mi><mi> </mi><mo>+</mo><mi> </mi><mn>35</mn></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></mrow></mrow></mrow></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>12</mn><mo>+</mo><mn>2</mn></mrow><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>35</mn></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></mrow></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>12</mn></mrow><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>35</mn></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi><mo>+</mo></mrow></mrow><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>36</mn><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac></mrow></mrow></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mn>2</mn><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>35</mn></msqrt><mo>+</mo><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msqrt><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>6</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac><mo>+</mo><msub><mrow><mi>c</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mrow></math>
<math><mo>=</mo><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>35</mn><mo>+</mo></msqrt><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi><mo>-</mo><mn>6</mn><mo>+</mo><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>35</mn></msqrt></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>
<math>   <mo>&#x21D2;</mo>  </math><math><mi>A</mi><mo>=</mo><mn>1</mn></math>

</details>

---

### Q245. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `2`

If <math><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>9</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>A</mi><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mi>B</mi><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>+</mo></mrow></mrow></mrow></mrow></mrow></mrow><mi>C</mi></math> then <math><mi>A</mi><mo>-</mo><mi>B</mi><mo>=</mo></math>

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>30</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>30</mn></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>**

**Detailed Solution:**

Since <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>A</mi><mi>B</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>B</mi><mo>-</mo><mi>A</mi></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>A</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>B</mi></mrow></mfrac></mrow></mfenced></math>
<math>   <mo>&#x21D2;</mo>  </math><math><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>9</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo></mrow></mrow><mi> </mi><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>9</mn></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mrow></mrow></mrow></mrow></mfenced><mo>+</mo><mi>C</mi></math>
<math>   <mo>&#x21D2;</mo>  </math><math><mi>A</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi>B</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math>
<math>  <mrow>   <mo>&#x21D2;</mo><mi>A</mi><mo>&#x2212;</mo><mi>B</mi><mo>=</mo><mfrac>    <mn>1</mn>    <mrow>     <mn>10</mn></mrow>   </mfrac>   <mo>+</mo><mfrac>    <mn>1</mn>    <mrow>     <mn>15</mn></mrow>   </mfrac>   <mo>=</mo><mfrac>    <mn>5</mn>    <mrow>     <mn>30</mn></mrow>   </mfrac>   <mo>=</mo><mfrac>    <mn>1</mn>    <mn>6</mn>   </mfrac>   </mrow></math>

</details>

---

### Q246. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `2`

If <math><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>9</mn><mo>-</mo><mn>16</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mi>α</mi><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mo>(</mo><mi>β</mi><mi>x</mi><mo>)</mo></mrow></mrow><mo>+</mo><mi>c</mi><mo>,</mo></math> then <math><mi>α</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>β</mi></mrow></mfrac><mo>=</mo></math>

**Options:**

- **(A)** <math > <mn>1</mn></math>
- **(B)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>19</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math > <mn>1</mn></math>**

**Detailed Solution:**

<math><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>9</mn><mo>-</mo><mn>16</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mi>α</mi><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mo>(</mo><mi>β</mi><mi>x</mi><mo>)</mo></mrow></mrow><mo>+</mo><mi>c</mi></math>
<math><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><msup><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mo>(</mo><mn>4</mn><msup><mrow><mi>x</mi><mo>)</mo></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mrow><mrow><msup><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><mi>c</mi></math>
<math><mi>α</mi><mi> </mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi>β</mi><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math><mi>α</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>β</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><mn>1</mn></math>

</details>

---

### Q247. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

If <math><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mo>[</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mrow><mo>]</mo></mrow></mrow><mo>+</mo><mi>c</mi><mo>,</mo></math> then <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo></math>

**Options:**

- **(A)** <math><mrow><mrow><mi>cot</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>
- **(B)** <math> <mrow> <mi>tan</mi><mi>x</mi> </mrow> </math>
- **(C)** <math><mrow><mrow><mi>sec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>
- **(D)** <math><mrow><mrow><mi>cosec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mrow><mrow><mi>cot</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>**

**Detailed Solution:**

Given <math><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mo>[</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mrow><mo>]</mo></mrow></mrow><mo>+</mo><mi>C</mi></math>
By using anti differentiation method, we will get
<math><mfrac><mrow><mi>d</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></mrow></mfenced></math>
<math><mo>=</mo><mi> </mi><mfrac><mrow><mn>1</mn></mrow><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow></mrow></mfrac><mo>⋅</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfrac><mo>⋅</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></math>
<math><mo>=</mo><mi> </mi><mfrac><mrow><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow></mrow></mfrac></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></math>

</details>

---

### Q248. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `2`

<math><mrow><mo stretchy="false">∫</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mfrac><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn></mrow></mfenced><mi> </mi><msup><mrow><mi>a</mi></mrow><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></msup></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo></mrow></mrow></math> ________

**Options:**

- **(A)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>a</mi></mrow></mrow><mo>&sdot;</mo><mi> </mi><msup><mrow><mi>a</mi></mrow><mrow><mi>x</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></msup><mo>+</mo><mi>c</mi></math>
- **(B)** <math><mfrac><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>a</mi></mrow></mrow></mrow></mfrac><mo>+</mo><mi>c</mi></math>
- **(C)** <math><mfrac><mrow><msup><mrow><mi>a</mi></mrow><mrow><mi>x</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></msup></mrow><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>a</mi></mrow></mrow></mrow></mfrac><mo>+</mo><mi>c</mi></math>
- **(D)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>a</mi></mrow></mrow><mo>&sdot;</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfenced><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><msup><mrow><mi>a</mi></mrow><mrow><mi>x</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></msup></mrow><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>a</mi></mrow></mrow></mrow></mfrac><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

<math> <mrow> <mi>I</mi><mo>=</mo><mstyle displaystyle="true"> <mrow><mo>∫</mo> <mrow> <mfrac> <mrow> <mrow><mo>(</mo> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>2</mn></mrow> <mo>)</mo></mrow><msup> <mi>a</mi> <mrow> <mrow><mo>(</mo> <mrow> <mi>x</mi><mo>+</mo><msup> <mrow> <mi>tan</mi></mrow> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> <mi>x</mi></mrow> <mo>)</mo></mrow></mrow> </msup> </mrow> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>1</mn></mrow> </mfrac> <mi>d</mi><mi>x</mi><mo>=</mo></mrow> </mrow> </mstyle><mstyle displaystyle="true"> <mrow><mo>∫</mo> <mrow> <mrow><mo>(</mo> <mrow> <mn>1</mn><mo>+</mo><mfrac> <mn>1</mn> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>1</mn></mrow> </mfrac> </mrow> <mo>)</mo></mrow><msup> <mi>e</mi> <mrow> <mrow><mo>(</mo> <mrow> <mi>x</mi><mo>+</mo><msup> <mrow> <mi>tan</mi></mrow> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> <mi>x</mi></mrow> <mo>)</mo></mrow><mo>⋅</mo><mtext> </mtext><mi>l</mi><mn>n</mn><mi>a</mi></mrow> </msup> </mrow> </mrow> </mstyle><mi>d</mi><mi>x</mi></mrow> </math>
Let <math> <mrow> <mrow><mo>(</mo> <mrow> <mi>x</mi><mo>+</mo><msup> <mrow> <mi>tan</mi></mrow> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> <mi>x</mi></mrow> <mo>)</mo></mrow><mi>l</mi><mn>n</mn><mi>a</mi><mtext> </mtext><mo>=</mo><mi>t</mi></mrow> </math>
<math> <mrow> <mo>⇒</mo><mrow><mo>(</mo> <mrow> <mn>1</mn><mo>+</mo><mfrac> <mn>1</mn> <mrow> <mn>1</mn><mo>+</mo><msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> <mo>)</mo></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mfrac> <mrow> <mi>d</mi><mi>t</mi></mrow> <mrow> <mi>l</mi><mn>n</mn><mtext> </mtext><mi>a</mi></mrow> </mfrac> </mrow> </math>
<math> <mrow> <mo>⇒</mo><mi>I</mi><mo>=</mo><mstyle displaystyle="true"> <mrow><mo>∫</mo> <mrow> <mfrac> <mrow> <msup> <mi>e</mi> <mi>t</mi> </msup> <mi>l</mi><mi>t</mi></mrow> <mrow> <mi>l</mi><mn>n</mn><mi>a</mi></mrow> </mfrac> </mrow> </mrow> </mstyle><mo>=</mo><mfrac> <mrow> <msup> <mi>e</mi> <mi>t</mi> </msup> </mrow> <mrow> <mi>l</mi><mn>n</mn> <mi>a</mi></mrow> </mfrac> <mo>+</mo><mi>C</mi></mrow> </math>
<math> <mrow> <mo>=</mo><mfrac> <mrow> <msup> <mi>a</mi> <mrow> <mi>x</mi><mo>+</mo><msup> <mrow> <mi>tan</mi></mrow> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> <mi>x</mi></mrow> </msup> </mrow> <mrow> <mi>l</mi><mn>n</mn><mtext> </mtext><mi>a</mi></mrow> </mfrac> <mo>+</mo><mi>C</mi></mrow> </math>

</details>

---

### Q249. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `2`

<math><mrow><mo stretchy="false">∫</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>-</mo><mn>25</mn></mrow><mrow><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>-</mo><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mi>A</mi><mi>x</mi><mo>+</mo><mi>B</mi><mrow><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi></mrow></mrow></mrow><mo>|</mo><mrow><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></mrow></mrow><mo>-</mo><mrow><mrow><mn>5</mn></mrow><mo>|</mo><mrow><mo>+</mo><mi>c</mi></mrow></mrow></math> then

**Options:**

- **(A)** <math><mi>A</mi><mo>=</mo><mn>5</mn><mo>,</mo><mi> </mi><mi>B</mi><mo>=</mo><mn>3</mn></math>
- **(B)** <math><mi>A</mi><mo>=</mo><mn>5</mn><mo>,</mo><mi> </mi><mi>B</mi><mo>=</mo><mo>-</mo><mn>3</mn></math>
- **(C)** <math><mi>A</mi><mo>=</mo><mo>-</mo><mn>5</mn><mo>,</mo><mi> </mi><mi>B</mi><mo>=</mo><mn>3</mn></math>
- **(D)** <math><mi>A</mi><mo>=</mo><mo>-</mo><mn>5</mn><mo>,</mo><mi> </mi><mi>B</mi><mo>=</mo><mo>-</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi>A</mi><mo>=</mo><mn>5</mn><mo>,</mo><mi> </mi><mi>B</mi><mo>=</mo><mo>-</mo><mn>3</mn></math>**

**Detailed Solution:**

Let  <math><mi>I</mi><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>-</mo><mn>25</mn></mrow><mrow><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>-</mo><mn>5</mn></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math> 
 <math><mo>⇒</mo><mi> </mi><mi>I</mi><mo>=</mo><mrow><mo stretchy="false">∫</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>10</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>-</mo><mn>25</mn><mo>-</mo><mn>6</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></mrow><mrow><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>-</mo><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mi>d</mi><mi>x</mi></math> 
 <math><mo>⇒</mo><mi> </mi><mi>I</mi><mo>=</mo><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mn>5</mn><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>-</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mn>6</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></mrow><mrow><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>-</mo><mn>5</mn></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></mrow></math> 
 <math><mo>⇒</mo><mi> </mi><mi>I</mi><mo>=</mo><mrow><mo stretchy="false">∫</mo><mrow><mfenced separators="|"><mrow><mn>5</mn><mo>-</mo><mfrac><mrow><mn>6</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></mrow><mrow><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>-</mo><mn>5</mn></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></math> 
 <math><mo>⇒</mo><mi> </mi><mi>I</mi><mo>=</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>3</mn><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mi>C</mi></mrow></mrow></math> 
 <math><mo>∴</mo><mi> </mi><mi> </mi><mi>A</mi><mo>=</mo><mn>5</mn><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><mi>B</mi><mo>=</mo><mo>-</mo><mn>3</mn></math>

</details>

---

### Q250. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

<math><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>8</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo></mrow></mrow></math>

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(B)** <math><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(D)** <math><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>**

**Detailed Solution:**

Let <math><mi>I</mi><mo>=</mo><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msqrt><mn>8</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></mrow></mrow></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi>I</mi><mo>=</mo><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msqrt><mn>9</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac></mrow></mrow></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi>I</mi><mo>=</mo><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mrow></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi>I</mi><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>

</details>

---

### Q251. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \frac{\left(x^{2}+1\right)}{x^{4}+x^{2}+1} d x$ is

**Options:**

- **(A)** $\frac{1}{\sqrt{3}} \tan ^{-1}\left\{\frac{x-1 / x}{\sqrt{3}}\right\}+C$
- **(B)** $\frac{1}{2 \sqrt{3}} \log \left\{\frac{(x-1 / x)-\sqrt{3}}{(x-1 / x)+\sqrt{3}}\right\}+C$
- **(C)** $\tan ^{-1}\left(\frac{x+1 / x}{\sqrt{3}}\right)+C$
- **(D)** $\tan ^{-1}\left(\frac{x-1 / x}{\sqrt{3}}\right)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{\sqrt{3}} \tan ^{-1}\left\{\frac{x-1 / x}{\sqrt{3}}\right\}+C$**

**Detailed Solution:**

Let $I=\int \frac{x^{2}+1}{x^{4}+x^{2}+1} d x$
$\begin{aligned}=& \int \frac{\left(1+\frac{1}{x^{2}}\right)}{x^{2}+1+\frac{1}{x^{2}}} d x \\=& \int \frac{\left(1+\frac{1}{x^{2}}\right)}{\left(x-\frac{1}{x}\right)^{2}+(\sqrt{3})^{2}} d x \\=& \int \frac{d t}{(\sqrt{3})^{2}+t^{2}} \\ \quad\left[\text { let } t=x-\frac{1}{x} \Rightarrow d t=\left(1+\frac{1}{x^{2}}\right) d x\right] \\=& \frac{1}{\sqrt{3}} \tan ^{-1}\left(\frac{t}{\sqrt{3}}\right)+C \\=& \frac{1}{\sqrt{3}} \tan ^{-1}\left\{\frac{1}{\sqrt{3}}\left(x-\frac{1}{x}\right)\right\}+C \end{aligned}$

</details>

---

### Q252. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \sqrt{1+\sec x} d x$ is

**Options:**

- **(A)** $\sin ^{-1}(\sqrt{2} \sin x)+C$
- **(B)** $2 \sin ^{-1}(\sqrt{2} \sin x / 2)+C$
- **(C)** $2 \sin ^{-1}(\sqrt{2} \sin x)+C$
- **(D)** $2 \sin ^{-1}(\sqrt{2} x / 2)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \sin ^{-1}(\sqrt{2} \sin x / 2)+C$**

**Detailed Solution:**

Let $I=\int \sqrt{1+\sec x} d x$
$=\int \frac{\sqrt{1+\cos x}}{\sqrt{\cos x}} d x$
$=\int \frac{\sqrt{2} \cdot \cos \frac{x}{2}}{\sqrt{1-2 \sin ^{2} \frac{x}{2}}} d x$
(let $\left.t=\sqrt{2} \sin \frac{x}{2} \Rightarrow d t=\frac{\sqrt{2}}{2} \cdot \cos \frac{x}{2} \cdot d x\right)$
$=\int \frac{2 d t}{\sqrt{1-t^{2}}}$
$=2 \sin ^{-1}(t)+C$
$=2 \sin ^{-1}\left(\sqrt{2} \cdot \sin \frac{x}{2}\right)+C$

</details>

---

### Q253. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int \frac{\sin 2 x}{\sin ^{4} x+\cos ^{4} x} d x$ is

**Options:**

- **(A)** $\tan ^{-1}\left(\cot ^{2} x\right)+C$
- **(B)** $-\tan ^{-1}(\cos 2 x)+C$
- **(C)** $\tan ^{-1}(\sin 2 x)+C$
- **(D)** $\tan ^{-1}\left(\tan ^{2} x\right)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\tan ^{-1}(\cos 2 x)+C$**

**Detailed Solution:**

Let $I=\int \frac{\sin 2 x}{\sin ^{4} x+\cos ^{4} x} d x$
$I=\int \frac{\sin 2 x}{\left(\sin ^{2} x+\cos ^{2} x\right)^{2}-2 \sin ^{2} x \cdot \cos ^{2} x} d x$
$I=\int \frac{\sin 2 x}{1-\frac{1}{2}(\sin 2 x)^{2}} d x$
$\begin{aligned}=2 & \int \frac{\sin 2 x}{1+\left(1-\sin ^{2} 2 x\right)} d x \\ & \quad \text { (let } t=\cos 2 x \Rightarrow d t=-2 \sin 2 x d x \\=& \int \frac{-d t}{1+t^{2}} \\=&-\tan ^{-1} t+C \\=&-\tan ^{-1}(\cos 2 x)+C \end{aligned}$

</details>

---

### Q254. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int \frac{1}{3 \sin x-\cos x+3} d x$ is

**Options:**

- **(A)** $\log \left(\frac{\tan \frac{x}{2}+1}{2 \tan \frac{x}{2}+1}\right)+C$
- **(B)** $\frac{1}{2} \log \left(\frac{2 \tan \frac{x}{2}+1}{\tan \frac{x}{2}+1}\right)+C$
- **(C)** $\log \left(\frac{2 \tan \frac{x}{2}+1}{\tan \frac{x}{2}+1}\right)+C$
- **(D)** $2 \log \left(\frac{2 \tan \frac{x}{2}+1}{\tan \frac{x}{2}+1}\right)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log \left(\frac{2 \tan \frac{x}{2}+1}{\tan \frac{x}{2}+1}\right)+C$**

**Detailed Solution:**

Let $I=\int \frac{d x}{3 \sin x-\cos x+3}$
$\left\{\begin{array}{l}\because \quad \sin x=\frac{2 \tan \frac{x}{2}}{1+\tan ^{2} \frac{x}{2}} \\ \text { and } \cos x=\frac{1-\tan ^{2} \frac{x}{2}}{1+\tan ^{2} \frac{x}{2}}\end{array}\right\}$
$I=\int \frac{d x}{3\left\{\frac{2 \tan \frac{x}{2}}{1+\tan ^{2} \frac{x}{2}}\right\}-\left\{\frac{1-\tan ^{2} \frac{x}{2}}{1+\tan ^{2} \frac{x}{2}}\right\}+3}$
$=\int \frac{\left(1+\tan ^{2} \frac{x}{2}\right) d x}{6 \tan \frac{x}{2}-1+\tan ^{2} \frac{x}{2}+3+3 \tan ^{2} \frac{x}{2}}$
$=\int \frac{\sec ^{2} \frac{x}{2}}{4 \tan ^{2} \frac{x}{2}+6 \tan \frac{x}{2}+2} d x$
$\left(\right.$ let $\left.t=\tan \frac{x}{2}, d t=\frac{1}{2} \sec ^{2} \frac{x}{2} d x\right)$
$=\int \frac{d t}{2 t^{2}+3 t+1}$
$=\int \frac{d t}{(t+1)(2 t+1)}$
$=\int\left\{\frac{-1}{(t+1)}+\frac{2}{(2 t+1)}\right\} d t$ (by partial
fraction) $=-\log (t+1)+\frac{2}{2} \log (2 t+1)+C$
$=\log \frac{(2 t+1)}{(t+1)}+C$
$=\log \left(\frac{2 \tan \frac{x}{2}+1}{\tan \frac{x}{2}+1}\right)+C$

</details>

---

### Q255. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \frac{d x}{x\left(x^{n}+1\right)}$ is

**Options:**

- **(A)** $\frac{1}{n} \log \left(\frac{x^{n}}{x^{n}+1}\right)+C$
- **(B)** $\log \left(\frac{x^{n}+1}{x^{n}}\right)+C$
- **(C)** $\frac{1}{n} \log \left(\frac{x^{n}+1}{x^{n}}\right)+C$
- **(D)** $\log \left(\frac{x^{n}}{x^{n}+1}\right)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{n} \log \left(\frac{x^{n}}{x^{n}+1}\right)+C$**

**Detailed Solution:**

Let $\begin{aligned} I=\int \frac{d x}{x\left(x^{n}+1\right)} \\ \left.\quad \text { (let } t=x^{n}+1, d t=n x^{n-1} d x\right) \\=& \int \frac{d t}{r x^{n} \cdot t} \quad\left(\frac{d t}{n x^{n}}=\frac{d x}{x}\right) \\=& \frac{1}{n} \int \frac{d t}{t(t-1)} \\=& \frac{1}{n} \int\left\{\frac{1}{t-1}-\frac{1}{t}\right\} d t \\=& \frac{1}{n}\{\log (t-1)-\log t\}+C \\=& \frac{1}{n} \log \frac{t-1}{t}+C \\=& \frac{1}{n} \log \frac{x^{n}}{x^{n}+1}+C \end{aligned}$

</details>

---

### Q256. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `3`

$\int(\sqrt{\tan x}+\sqrt{\cot } x) d x$

**Options:**

- **(A)** $\sqrt{2} \tan ^{-1}\left(\frac{\tan x}{\sqrt{2 \tan x}}\right)+C$
- **(B)** $\sqrt{2} \tan ^{-1}\left(\frac{\tan x-1}{\sqrt{2 \tan x}}\right)+C$
- **(C)** $\frac{\tan x}{\sqrt{2}} \cdot \tan ^{-1}\left(\frac{\cot x+1}{\sqrt{2 \tan x}}\right)+C$
- **(D)** $\frac{\tan x}{\sqrt{2}} \cdot \tan ^{-1}\left(\frac{\cot x+1}{\sqrt{2 \tan x}}\right)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{2} \tan ^{-1}\left(\frac{\tan x-1}{\sqrt{2 \tan x}}\right)+C$**

**Detailed Solution:**

Let $I=\int \frac{(\sin x+\cos x)}{\sqrt{\sin x \cdot \cos x}} d x$
$=\int \frac{\sqrt{2}(\sin x+\cos x)}{\sqrt{2 \sin x \cdot \cos x}} d x$
$=\sqrt{2} \int \frac{\sin x+\cos x}{\sqrt{\sin 2 x}} d x$
Put $\quad \sin x-\cos x=t$
Also, $\quad \sin 2 x=\left(1-t^{2}\right)$
$\therefore \quad I=\sqrt{2} \int \frac{d t}{\sqrt{1-t^{2}}}$
$\quad=\sqrt{2} \sin ^{-1} t+C$
$\quad=\sqrt{2} \sin ^{-1}(\sin x-\cos x)+C$
$\quad=\sqrt{2} \tan ^{-1}\left(\frac{\tan x-1}{\sqrt{2 \tan x}}\right)+C$

</details>

---

### Q257. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `2`

$\int e^{\tan x}\left(\sec ^{2} x+\sec ^{3} x \sin x\right) d x$ is equal to

**Options:**

- **(A)** $\sec x e^{\tan x}+c$
- **(B)** $\tan x e^{\tan x}+c$
- **(C)** $e^{\tan x}+\tan x+c$
- **(D)** $(1+\tan x) e^{\tan x}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\tan x e^{\tan x}+c$**

**Detailed Solution:**

Let $I=\int e^{\tan x}\left(\sec ^{2} x+\sec ^{3} x \sin x\right) d x$
$=\int e^{\tan x}(1+\tan x) \sec ^{2} x d x$
Put $\tan x=t$
$\Rightarrow \sec ^{2} x d x=d t$
$I=\int e^{t}(1+t) d t$
$=e^{t}+\int t e^{t} d t$
$=e^{t}+t e^{t}-e^{t}+c$
$=t e^{t}+c$
$=\tan x e^{\tan x}+c$

</details>

---

### Q258. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int x \sin x \sec ^{3} x d x$ is

**Options:**

- **(A)** $\frac{1}{2}\left[\sec ^{2} x-\tan x\right]+c$
- **(B)** $\frac{1}{2}\left[x \sec ^{2} x-\tan x\right]+c$
- **(C)** $\frac{1}{2}\left[x \sec ^{2} x+\tan x\right]+c$
- **(D)** $\frac{1}{2}\left[\sec ^{2} x+\tan x\right]+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2}\left[x \sec ^{2} x-\tan x\right]+c$**

**Detailed Solution:**

$$
\begin{aligned}
\int x \sin x \sec ^{3} x d x &=\int x \sin x \frac{1}{\cos ^{3} x} d x \\
&=\int x \tan x \cdot \sec ^{2} x d x \\
\text { Put } \tan x=t & \Rightarrow \sec ^{2} x d x=d t \\
\text { and } \quad x &=\tan ^{-1} t
\end{aligned}
$$
Then, it reduces to
$$
\begin{array}{l}
\int \tan ^{-1} t \cdot t d t=\frac{t^{2}}{2} \tan ^{-1} t-\int \frac{t^{2}}{2\left(1+t^{2}\right)} d t \\
=\frac{x \tan ^{2} x}{2}-\frac{1}{2} t+\frac{1}{2} \tan ^{-1} t+c \\
=\frac{x\left(\sec ^{2} x-1\right)}{2}-\frac{1}{2} \tan x+\frac{1}{2} x+c \\
=\frac{1}{2}\left[x \sec ^{2} x-\tan x\right]+c
\end{array}
$$

</details>

---

### Q259. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{x^{e-1}+e^{x-1}}{x^{e}+e^{x}} d x$ is equal to

**Options:**

- **(A)** $\log \left(x^{e}+e^{x}\right)+c$
- **(B)** $e \log \left(x^{e}+e^{x}\right)+c$
- **(C)** $\frac{1}{e} \log \left(x^{e}+e^{x}\right)+c$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{e} \log \left(x^{e}+e^{x}\right)+c$**

**Detailed Solution:**

Put 
$\begin{aligned} x^{e}+e^{x}=t \\ \Rightarrow e\left(x^{e-1}+e^{x-1}\right) d x &=d t \\ \therefore \int \frac{x^{e-1}+e^{x-1}}{x^{e}+e^{x}} d x &=\frac{1}{e} \int \frac{d t}{t} \\ &=\frac{1}{e} \log t+c \\ &=\frac{1}{e} \log \left(x^{e}+e^{x}\right)+c \end{aligned}$

</details>

---

### Q260. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

$\int \cos ^{3} x \cdot e^{\log (\sin x)} d x$ is equal to

**Options:**

- **(A)** $-\frac{\sin ^{4} x}{4}+c$
- **(B)** $-\frac{\cos ^{4} x}{4}+c$
- **(C)** $\frac{e^{\sin x}}{4}+c$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{\cos ^{4} x}{4}+c$**

**Detailed Solution:**

Let $I=\int \cos ^{3} x e^{\log \sin x} d x=\int \cos ^{3} x \sin x d x$
Put $x=t \quad \Rightarrow-\sin x d x=d t$
$$
I=-\int t^{3} d t=-\frac{t^{4}}{4}+c=-\frac{\cos ^{4} x}{4}+c
$$

</details>

---

