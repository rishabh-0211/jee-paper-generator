# MHT CET Mathematics - Indefinite Integration

## Topic 1: Fundamental of Indefinite Integration

**Total Questions:** 36

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\int \dfrac{1}{f(x)}\,dx = \log|f(x)|^2 + c$, then $f(x) = \ldots$

**Options:**

- **(A)** $x + c$
- **(B)** $\dfrac{x}{2} + c$
- **(C)** $\dfrac{x^2}{2} + c$
- **(D)** $x^2 + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{x}{2} + c$**

**Detailed Solution:**

Given $\int \dfrac{1}{f(x)}\,dx = \log|f(x)|^2 + c$

$\int \dfrac{1}{f(x)}\,dx = 2\log|f(x)| + c$

Differentiating both sides with respect to $x$:

$\dfrac{1}{f(x)} = 2 \cdot \dfrac{1}{f(x)} \cdot f'(x)$

$1 = 2f'(x)$

$f'(x) = \dfrac{1}{2}$

Integrating with respect to $x$:

$f(x) = \dfrac{x}{2} + k$

From the given options, $f(x) = \dfrac{x}{2} + c$.

Answer: $\dfrac{x}{2} + c$

</details>

---

### Q2. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f'(x) = k(\cos x - \sin x)$, $f'(0) = 5$, $f\left(\dfrac{\pi}{2}\right) = 19$, Then $f(x) = $

**Options:**

- **(A)** $14(\cos x - \sin x) + 5$
- **(B)** $14(\cos x + \sin x) + 5$
- **(C)** $5(\cos x - \sin x) + 14$
- **(D)** $5(\cos x + \sin x) + 14$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5(\cos x + \sin x) + 14$**

**Detailed Solution:**

Given $f'(x) = k(\cos x - \sin x)$

Substituting $x = 0$, we get $f'(0) = k(\cos 0 - \sin 0) = k$

Since $f'(0) = 5$, we have $k = 5$

Thus, $f'(x) = 5(\cos x - \sin x)$

Integrating with respect to $x$, we get

$f(x) = \int 5(\cos x - \sin x) dx = 5(\sin x + \cos x) + C$

Substituting $x = \dfrac{\pi}{2}$, we get

$f\left(\dfrac{\pi}{2}\right) = 5\left(\sin \dfrac{\pi}{2} + \cos \dfrac{\pi}{2}\right) + C = 5(1 + 0) + C = 5 + C$

Since $f\left(\dfrac{\pi}{2}\right) = 19$, we have $5 + C = 19 \Rightarrow C = 14$

Therefore, $f(x) = 5(\cos x + \sin x) + 14$

Answer: $5(\cos x + \sin x) + 14$

</details>

---

### Q3. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \sin 4x \cos 3x\, dx$ is

**Options:**

- **(A)** $-\dfrac{1}{14}\cos 7x - \dfrac{1}{2}\cos x + c$
- **(B)** $-\dfrac{1}{14}\cos 7x + \dfrac{1}{2}\cos x + c$
- **(C)** $\dfrac{1}{14}\cos 7x - \dfrac{1}{2}\cos x + c$
- **(D)** $\dfrac{1}{14}\cos 7x + \dfrac{1}{2}\cos x + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\dfrac{1}{14}\cos 7x - \dfrac{1}{2}\cos x + c$**

**Detailed Solution:**

Let $I = \int \sin 4x \cos 3x \, dx$

Multiplying and dividing by $2$, we get:

$I = \dfrac{1}{2} \int 2 \sin 4x \cos 3x \, dx$

Using the trigonometric identity $2 \sin A \cos B = \sin(A+B) + \sin(A-B)$ with $A = 4x$ and $B = 3x$:

$I = \dfrac{1}{2} \int (\sin 7x + \sin x) \, dx$

Integrating with respect to $x$:

$I = \dfrac{1}{2} \left( -\dfrac{\cos 7x}{7} - \cos x \right) + c$

$I = -\dfrac{1}{14} \cos 7x - \dfrac{1}{2} \cos x + c$

Answer: $-\dfrac{1}{14}\cos 7x - \dfrac{1}{2}\cos x + c$

</details>

---

### Q4. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $u$ and $v$ are functions of $x$, then $\int \dfrac{1}{v^3}\left(uv\dfrac{du}{dx} - u^2\dfrac{dv}{dx}\right)dx = $

**Options:**

- **(A)** $\log uv + c$
- **(B)** $\log\dfrac{u}{v} + c$
- **(C)** $\dfrac{v^2}{2u^2} + c$
- **(D)** $\dfrac{u^2}{2v^2} + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{u^2}{2v^2} + c$**

**Detailed Solution:**

The given integral is $I = \int \dfrac{1}{v^3}\left(uv\dfrac{du}{dx} - u^2\dfrac{dv}{dx}\right)dx$

Rearranging the terms in the integrand, we get:

$I = \int \dfrac{u}{v}\left(\dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}\right)dx$

We know that by the quotient rule of differentiation, $\dfrac{d}{dx}\left(\dfrac{u}{v}\right) = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$

Substituting this into the integral:

$I = \int \dfrac{u}{v} \dfrac{d}{dx}\left(\dfrac{u}{v}\right) dx$

Let $\dfrac{u}{v} = t$, then $\dfrac{d}{dx}\left(\dfrac{u}{v}\right) dx = dt$

$I = \int t dt$

$I = \dfrac{t^2}{2} + c$

Substituting back $t = \dfrac{u}{v}$:

$I = \dfrac{u^2}{2v^2} + c$

Answer: $\dfrac{u^2}{2v^2} + c$

</details>

---

### Q5. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \dfrac{\sin^6 x + \cos^6 x}{\sin^2 x \cdot \cos^2 x}\, \text{d}x$ is

**Options:**

- **(A)** $\cot x + \cot^2 x + c$, where c is the constant of integration
- **(B)** $\tan x - \cot x - 3x + c$, where c is the constant of integration
- **(C)** $2\sin^5 x + 2\cos^5 x + c$, where c is the constant of integration
- **(D)** $\sin^3 x + 2\cos^3 x + c$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\tan x - \cot x - 3x + c$, where c is the constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{\sin^6 x + \cos^6 x}{\sin^2 x \cos^2 x} \, dx$

Using the algebraic identity $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$, we can simplify the numerator:

$\sin^6 x + \cos^6 x = (\sin^2 x + \cos^2 x)(\sin^4 x - \sin^2 x \cos^2 x + \cos^4 x)$

Since $\sin^2 x + \cos^2 x = 1$, this becomes:

$\sin^4 x - \sin^2 x \cos^2 x + \cos^4 x = (\sin^2 x + \cos^2 x)^2 - 3\sin^2 x \cos^2 x = 1 - 3\sin^2 x \cos^2 x$

Substituting this back into the integral:

$I = \int \dfrac{1 - 3\sin^2 x \cos^2 x}{\sin^2 x \cos^2 x} \, dx$

$I = \int \left( \dfrac{1}{\sin^2 x \cos^2 x} - 3 \right) \, dx$

Using the identity $1 = \sin^2 x + \cos^2 x$ in the numerator of the first term:

$I = \int \left( \dfrac{\sin^2 x + \cos^2 x}{\sin^2 x \cos^2 x} - 3 \right) \, dx$

$I = \int (\sec^2 x + \csc^2 x - 3) \, dx$

Integrating term by term, we get:

$I = \tan x - \cot x - 3x + c$

Answer: $\tan x - \cot x - 3x + c$, where c is the constant of integration

</details>

---

### Q6. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)$ and $g(x)$ are integrable functions then $\left[\int f(x)dx\right]\left[\int g(x)dx\right] = $

**Options:**

- **(A)** $\int \left[f(x)g'(x) + f'(x)g(x)\right]dx$
- **(B)** $\int \left[f(x)g'(x) - f'(x)g(x)\right]dx$
- **(C)** $\int \left[f(x)\int g(x)dx + g(x)\int f(x)dx\right]dx$
- **(D)** $\int \left[f(x)\int g(x)dx - g(x)\int f(x)dx\right]dx$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\int \left[f(x)\int g(x)dx + g(x)\int f(x)dx\right]dx$**

**Detailed Solution:**

Let $u = \int f(x)dx$ and $v = \int g(x)dx$.

Differentiating with respect to $x$, we get $\dfrac{du}{dx} = f(x)$ and $\dfrac{dv}{dx} = g(x)$.

Using the product rule of differentiation, $\dfrac{d}{dx}(uv) = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$.

Substituting the expressions for $u$, $v$, $\dfrac{du}{dx}$, and $\dfrac{dv}{dx}$, we get $\dfrac{d}{dx}\left[\left(\int f(x)dx\right)\left(\int g(x)dx\right)\right] = \left(\int f(x)dx\right)g(x) + \left(\int g(x)dx\right)f(x)$.

Integrating both sides with respect to $x$, we obtain $\left[\int f(x)dx\right]\left[\int g(x)dx\right] = \int \left[f(x)\int g(x)dx + g(x)\int f(x)dx\right]dx$.

Answer: $\int \left[f(x)\int g(x)dx + g(x)\int f(x)dx\right]dx$

</details>

---

### Q7. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{A}=\left[\begin{array}{lll}\mathrm{a} & 0 & 0 \\ 0 & \mathrm{~b} & 0 \\ 0 & 0 & \mathrm{c}\end{array}\right]$ where $\mathrm{a}=7^{\mathrm{x}}, \mathrm{b}=7^{7^x}, \mathrm{c}=7^{7^{7^x}}$ then $\int|A| \mathrm{d} x$, (Where $|A|$ is the determinant of the matrix $A$ ) is equal to

**Options:**

- **(A)** $\frac{7^{7^x}}{(\log 7)^3}+k, \quad$ where $k$ is constant of integration
- **(B)** $\frac{7^{7^{7^x}}}{\log 7}+\mathrm{k}, \quad$ where k is constant of integration
- **(C)** $\frac{7^{7^{7^x}}}{(\log 7)^3}+\mathrm{k} \quad, \quad$ where k is constant of integration
- **(D)** $7^{7^{7^x}}(\log 7)^3+\mathrm{k}, \quad$ where k is constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{7^{7^{7^x}}}{(\log 7)^3}+\mathrm{k} \quad, \quad$ where k is constant of integration**

**Detailed Solution:**

The determinant of the diagonal matrix $A$ is given by the product of its diagonal elements.

$|A| = a \cdot b \cdot c = 7^x \cdot 7^{7^x} \cdot 7^{7^{7^x}}$

We need to evaluate the integral:

$I = \int |A| dx = \int 7^x \cdot 7^{7^x} \cdot 7^{7^{7^x}} dx$

Let $t = 7^{7^{7^x}}$. Differentiating both sides with respect to $x$ using the chain rule:

$\dfrac{dt}{dx} = 7^{7^{7^x}} \cdot \log 7 \cdot \dfrac{d}{dx}(7^{7^x})$

$\dfrac{dt}{dx} = 7^{7^{7^x}} \cdot \log 7 \cdot 7^{7^x} \cdot \log 7 \cdot \dfrac{d}{dx}(7^x)$

$\dfrac{dt}{dx} = 7^{7^{7^x}} \cdot \log 7 \cdot 7^{7^x} \cdot \log 7 \cdot 7^x \cdot \log 7$

$dt = 7^{7^{7^x}} \cdot 7^{7^x} \cdot 7^x \cdot (\log 7)^3 dx$

$\Rightarrow 7^x \cdot 7^{7^x} \cdot 7^{7^{7^x}} dx = \dfrac{dt}{(\log 7)^3}$

Substituting this into the integral:

$I = \int \dfrac{dt}{(\log 7)^3} = \dfrac{t}{(\log 7)^3} + k$

Substituting back $t = 7^{7^{7^x}}$:

$I = \dfrac{7^{7^{7^x}}}{(\log 7)^3} + k$

Answer: $\frac{7^{7^{7^x}}}{(\log 7)^3}+\mathrm{k} \quad, \quad$ where k is constant of integration

</details>

---

### Q8. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{\mathrm{d} x}{\sin ^2 x \cos ^2 x}=$

**Options:**

- **(A)** $\tan x+\cot x+\mathrm{c}$, where c is the constant of integration.
- **(B)** $\tan x-\cot x+\mathrm{c}$, where c is the constant of integration.
- **(C)** $\tan x \cot x+\mathrm{c}, \quad$ where c is the constant of integration.
- **(D)** $\tan x-\cot 2 x+c$, where $c$ is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\tan x-\cot x+\mathrm{c}$, where c is the constant of integration.**

**Detailed Solution:**

Let $I = \int \dfrac{1}{\sin^2 x \cos^2 x} \mathrm{d} x$

Using the trigonometric identity $\sin^2 x + \cos^2 x = 1$, we can write:

$I = \int \dfrac{\sin^2 x + \cos^2 x}{\sin^2 x \cos^2 x} \mathrm{d} x$

Separating the terms in the numerator, we get:

$I = \int \left( \dfrac{\sin^2 x}{\sin^2 x \cos^2 x} + \dfrac{\cos^2 x}{\sin^2 x \cos^2 x} \right) \mathrm{d} x$

$I = \int \left( \dfrac{1}{\cos^2 x} + \dfrac{1}{\sin^2 x} \right) \mathrm{d} x$

$I = \int (\sec^2 x + \csc^2 x) \mathrm{d} x$

Integrating each term with respect to $x$:

$I = \tan x - \cot x + \mathrm{c}$

Answer: $\tan x-\cot x+\mathrm{c}$, where c is the constant of integration.

</details>

---

### Q9. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\cos 2 x-\cos 2 \alpha}{\cos x-\cos \alpha} \mathrm{d} x=$

**Options:**

- **(A)** $2 \cos x+2 x \cos \alpha+c \quad$, where $c$ is the constant of integration.
- **(B)** $2 \cos x-2 x \cos \alpha+c \quad$, where $c$ is the constant of integration.
- **(C)** $2 \sin x+2 x \cos \alpha+c, \quad$ where $c$ is the constant of integration.
- **(D)** $2 \sin x+2 x \sin \alpha+c \quad$, where $c$ is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 \sin x+2 x \cos \alpha+c, \quad$ where $c$ is the constant of integration.**

**Detailed Solution:**

Let $I = \int \dfrac{\cos 2x - \cos 2\alpha}{\cos x - \cos \alpha} dx$

Using the trigonometric identity $\cos 2\theta = 2\cos^2 \theta - 1$, we can write:

$\cos 2x = 2\cos^2 x - 1$

$\cos 2\alpha = 2\cos^2 \alpha - 1$

Substituting these into the integral, we get:

$I = \int \dfrac{(2\cos^2 x - 1) - (2\cos^2 \alpha - 1)}{\cos x - \cos \alpha} dx$

$I = \int \dfrac{2(\cos^2 x - \cos^2 \alpha)}{\cos x - \cos \alpha} dx$

Using the identity $a^2 - b^2 = (a - b)(a + b)$, the numerator can be factored as:

$I = \int \dfrac{2(\cos x - \cos \alpha)(\cos x + \cos \alpha)}{\cos x - \cos \alpha} dx$

Canceling the common term $(\cos x - \cos \alpha)$ from the numerator and the denominator:

$I = \int 2(\cos x + \cos \alpha) dx$

Integrating with respect to $x$ (keeping in mind that $\cos \alpha$ is a constant):

$I = 2 \int \cos x dx + 2 \cos \alpha \int 1 dx$

$I = 2\sin x + 2x\cos \alpha + c$

Answer: $2 \sin x+2 x \cos \alpha+c, \quad$ where $c$ is the constant of integration.

</details>

---

### Q10. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{x+\sin x}{1+\cos x} \mathrm{~d} x=$

**Options:**

- **(A)** $x \cos x+c$, where $c$ is the constant integration
- **(B)** $x \tan x+c$, where $c$ is the constant integration
- **(C)** $x \tan \frac{x}{2}+c$, where $c$ is the constant integration
- **(D)** $x \sec ^2 \frac{x}{2}+c$, where $c$ is the constant integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x \tan \frac{x}{2}+c$, where $c$ is the constant integration**

**Detailed Solution:**

$I = \int \dfrac{x+\sin x}{1+\cos x} dx$

Using the half-angle formulas $1 + \cos x = 2\cos^2 \dfrac{x}{2}$ and $\sin x = 2\sin \dfrac{x}{2} \cos \dfrac{x}{2}$:

$I = \int \dfrac{x + 2\sin \dfrac{x}{2} \cos \dfrac{x}{2}}{2\cos^2 \dfrac{x}{2}} dx$

$I = \int \left( \dfrac{x}{2} \sec^2 \dfrac{x}{2} + \tan \dfrac{x}{2} \right) dx$

Applying integration by parts on the first term:

$\int \dfrac{x}{2} \sec^2 \dfrac{x}{2} dx = x \tan \dfrac{x}{2} - \int \tan \dfrac{x}{2} dx$

Substituting this back into the integral:

$I = x \tan \dfrac{x}{2} - \int \tan \dfrac{x}{2} dx + \int \tan \dfrac{x}{2} dx$

$I = x \tan \dfrac{x}{2} + c$

Answer: $x \tan \frac{x}{2}+c$, where $c$ is the constant integration

</details>

---

### Q11. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\mathrm{e}^{2030 \log x}-\mathrm{e}^{2029 \log x}}{\mathrm{e}^{2028 \log x}-\mathrm{e}^{2027 \log x}} \mathrm{~d} x=\ldots$.

**Options:**

- **(A)** $\frac{x^2}{2}+c$, where $c$ is the constant of integration
- **(B)** $x+c$, where $c$ is the constant of integration
- **(C)** $\frac{x^3}{3}+c$, where $c$ is the constant of integration
- **(D)** $\frac{x}{3}+c, \quad$ where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{x^3}{3}+c$, where $c$ is the constant of integration**

**Detailed Solution:**

Using the property of logarithms $a \log x = \log x^a$ and $e^{\log f(x)} = f(x)$, we can simplify the terms in the integrand.

$e^{2030 \log x} = e^{\log x^{2030}} = x^{2030}$

$e^{2029 \log x} = e^{\log x^{2029}} = x^{2029}$

$e^{2028 \log x} = e^{\log x^{2028}} = x^{2028}$

$e^{2027 \log x} = e^{\log x^{2027}} = x^{2027}$

Substituting these into the integral, we get:

$I = \int \dfrac{x^{2030} - x^{2029}}{x^{2028} - x^{2027}} dx$

Factoring out the common terms in the numerator and the denominator:

$I = \int \dfrac{x^{2029}(x - 1)}{x^{2027}(x - 1)} dx$

Cancelling the common factor $(x - 1)$:

$I = \int \dfrac{x^{2029}}{x^{2027}} dx$

$I = \int x^2 dx$

Integrating with respect to $x$:

$I = \dfrac{x^3}{3} + c$

Answer: $\frac{x^3}{3}+c$, where $c$ is the constant of integration

</details>

---

### Q12. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{x^3-7 x+6}{x^2+3 x} \mathrm{~d} x=$

**Options:**

- **(A)** $\frac{x^2}{2}+3 x-\log |x|+\mathrm{c}$, where c is a constant of integration.
- **(B)** $\frac{x^2}{2}+3 x+2 \log |x|+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\frac{x^2}{2}-3 x+2 \log |x|+\mathrm{c}$, where c is a constant of integration.
- **(D)** $\frac{x^2}{2}-3 x-\log |x|+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{x^2}{2}-3 x+2 \log |x|+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $I = \int \dfrac{x^3 - 7x + 6}{x^2 + 3x} \mathrm{~d} x$

Factorizing the numerator:

$x^3 - 7x + 6 = x^3 - x - 6x + 6$

$= x(x^2 - 1) - 6(x - 1)$

$= x(x - 1)(x + 1) - 6(x - 1)$

$= (x - 1)(x^2 + x - 6)$

$= (x - 1)(x + 3)(x - 2)$

Factorizing the denominator:

$x^2 + 3x = x(x + 3)$

Substituting these into the integral:

$I = \int \dfrac{(x - 1)(x + 3)(x - 2)}{x(x + 3)} \mathrm{~d} x$

$I = \int \dfrac{(x - 1)(x - 2)}{x} \mathrm{~d} x$

$I = \int \dfrac{x^2 - 3x + 2}{x} \mathrm{~d} x$

$I = \int \left( x - 3 + \dfrac{2}{x} \right) \mathrm{~d} x$

Integrating with respect to $x$:

$I = \dfrac{x^2}{2} - 3x + 2 \log |x| + \mathrm{c}$

Answer: $\frac{x^2}{2}-3 x+2 \log |x|+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q13. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\dfrac{\mathrm{d}}{\mathrm{d} x} \mathrm{f}(x)=4 x^3-\dfrac{3}{x^4}$ such that $\mathrm{f}(2)=0$, then $\mathrm{f}(x)$ is equal to

**Options:**

- **(A)** $x^4+\dfrac{1}{x^3}+\dfrac{129}{8}$
- **(B)** $x^4+\dfrac{1}{x^3}-\dfrac{129}{8}$
- **(C)** $x^3+\dfrac{1}{x^4}+\dfrac{129}{8}$
- **(D)** $x^3+\dfrac{1}{x^4}-\dfrac{129}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^4+\dfrac{1}{x^3}-\dfrac{129}{8}$**

**Detailed Solution:**

Given $\dfrac{\mathrm{d}}{\mathrm{d} x} \mathrm{f}(x) = 4 x^3 - \dfrac{3}{x^4}$

Integrating both sides with respect to $x$:

$\mathrm{f}(x) = \int \left( 4 x^3 - \dfrac{3}{x^4} \right) \mathrm{d} x$

$\mathrm{f}(x) = x^4 + \dfrac{1}{x^3} + C$

Given $\mathrm{f}(2) = 0$, substituting $x = 2$:

$\mathrm{f}(2) = 2^4 + \dfrac{1}{2^3} + C = 0$

$16 + \dfrac{1}{8} + C = 0$

$\dfrac{129}{8} + C = 0 \Rightarrow C = -\dfrac{129}{8}$

Therefore, $\mathrm{f}(x) = x^4 + \dfrac{1}{x^3} - \dfrac{129}{8}$

Answer: $x^4+\dfrac{1}{x^3}-\dfrac{129}{8}$

</details>

---

### Q14. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{x^4+x^2+1}{x^2-x+1} \mathrm{~d} x$ is equal to

**Options:**

- **(A)** $\dfrac{x^3}{3}-\dfrac{x^2}{2}+x+\mathrm{c}$, (where c is a constant of integration)
- **(B)** $\dfrac{x^3}{3}+\dfrac{x^2}{2}+x+\mathrm{c}$, (where c is a constant of integration)
- **(C)** $\dfrac{x^3}{3}-\dfrac{x^2}{2}-x+\mathrm{c}$, (where c is a constant of integration)
- **(D)** $\dfrac{x^3}{3}+\dfrac{x^2}{2}-x+\mathrm{c}$, ( where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{x^3}{3}+\dfrac{x^2}{2}+x+\mathrm{c}$, (where c is a constant of integration)**

**Detailed Solution:**

The given integral is $I = \int \dfrac{x^4+x^2+1}{x^2-x+1} \mathrm{~d} x$

Factorizing the numerator:

$x^4+x^2+1 = (x^2+1)^2 - x^2$

$= (x^2-x+1)(x^2+x+1)$

Substituting this into the integral:

$I = \int \dfrac{(x^2-x+1)(x^2+x+1)}{x^2-x+1} \mathrm{~d} x$

$I = \int (x^2+x+1) \mathrm{~d} x$

Integrating with respect to $x$:

$I = \dfrac{x^3}{3} + \dfrac{x^2}{2} + x + \mathrm{c}$

Answer: $\dfrac{x^3}{3}+\dfrac{x^2}{2}+x+\mathrm{c}$, (where c is a constant of integration)

</details>

---

### Q15. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{\left(x^2+1\right)}{(x+1)^2} d x=$

**Options:**

- **(A)** $\quad x-2 \log |(x+1)|-\dfrac{1}{x+1}+c$, where c is a constant of integration.
- **(B)** $\quad x-2 \log |(x+1)|-\dfrac{2}{x+1}+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\quad x-\log |(x+1)|-\dfrac{2}{x+1}+c$, where c is a constant of integration.
- **(D)** $\quad x-\log |(x+1)|-\dfrac{x}{x+1}+c$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\quad x-2 \log |(x+1)|-\dfrac{2}{x+1}+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $I = \int \dfrac{x^2+1}{(x+1)^2} dx$

Substitute $x+1 = t$, which gives $dx = dt$ and $x = t-1$.

$I = \int \dfrac{(t-1)^2+1}{t^2} dt$

$I = \int \dfrac{t^2-2t+2}{t^2} dt$

$I = \int \left(1 - \dfrac{2}{t} + \dfrac{2}{t^2}\right) dt$

$I = t - 2\log|t| - \dfrac{2}{t} + C$

Substituting $t = x+1$:

$I = (x+1) - 2\log|x+1| - \dfrac{2}{x+1} + C$

$I = x - 2\log|x+1| - \dfrac{2}{x+1} + c$

where $c = C+1$ is the constant of integration.

Answer: $\quad x-2 \log |(x+1)|-\dfrac{2}{x+1}+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q16. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \tan ^{-1}\sqrt{\left(\dfrac{1-\sin x}{1 + \sin x}\right)} d x=$

**Options:**

- **(A)** $\dfrac{\pi}{4} x-x+c$, where $c$ is a constant of integration.
- **(B)** $\dfrac{\pi}{4}-\dfrac{x}{2}+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\dfrac{\pi}{4} x-\dfrac{x^2}{4}+\mathrm{c}$, where c is a constant of integration.
- **(D)** $\dfrac{\pi}{4} x+\dfrac{x^2}{4}+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{\pi}{4} x-\dfrac{x^2}{4}+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $I = \int \tan^{-1} \sqrt{\dfrac{1-\sin x}{1+\sin x}} dx$

Using the trigonometric identities $1 - \sin x = \left(\cos\dfrac{x}{2} - \sin\dfrac{x}{2}\right)^2$ and $1 + \sin x = \left(\cos\dfrac{x}{2} + \sin\dfrac{x}{2}\right)^2$:

$\sqrt{\dfrac{1-\sin x}{1+\sin x}} = \sqrt{\dfrac{\left(\cos\dfrac{x}{2} - \sin\dfrac{x}{2}\right)^2}{\left(\cos\dfrac{x}{2} + \sin\dfrac{x}{2}\right)^2}} = \dfrac{\cos\dfrac{x}{2} - \sin\dfrac{x}{2}}{\cos\dfrac{x}{2} + \sin\dfrac{x}{2}}$

Dividing the numerator and the denominator by $\cos\dfrac{x}{2}$:

$\dfrac{1 - \tan\dfrac{x}{2}}{1 + \tan\dfrac{x}{2}} = \tan\left(\dfrac{\pi}{4} - \dfrac{x}{2}\right)$

Substituting this back into the integral:

$I = \int \tan^{-1} \left( \tan\left(\dfrac{\pi}{4} - \dfrac{x}{2}\right) \right) dx$

$I = \int \left( \dfrac{\pi}{4} - \dfrac{x}{2} \right) dx$

$I = \dfrac{\pi}{4} x - \dfrac{x^2}{4} + c$

Answer: $\dfrac{\pi}{4} x-\dfrac{x^2}{4}+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q17. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\int\left(\dfrac{4 \mathrm{e}^x-25}{2 \mathrm{e}^x-5}\right) \mathrm{d} x=\mathrm{A} x+\operatorname{Blog}\left(2 \mathrm{e}^x-5\right)+\mathrm{c} \quad$ (where c is a constant of integration) then

**Options:**

- **(A)** $\mathrm{A}=5, \mathrm{~B}=3$
- **(B)** $\mathrm{A}=5, \mathrm{~B}=-3$
- **(C)** $\mathrm{A}=-5, \mathrm{~B}=3$
- **(D)** $\mathrm{A}=-5, \mathrm{~B}=-3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{A}=5, \mathrm{~B}=-3$**

**Detailed Solution:**

Let the numerator be expressed as $A(\text{denominator}) + B(\text{derivative of denominator})$.

$4\mathrm{e}^x - 25 = A(2\mathrm{e}^x - 5) + B\left(\dfrac{\mathrm{d}}{\mathrm{d}x}(2\mathrm{e}^x - 5)\right)$

$4\mathrm{e}^x - 25 = A(2\mathrm{e}^x - 5) + B(2\mathrm{e}^x)$

Comparing the constant terms on both sides:

$-25 = -5A \Rightarrow A = 5$

Comparing the coefficients of $\mathrm{e}^x$ on both sides:

$4 = 2A + 2B$

Substituting $A = 5$:

$4 = 2(5) + 2B \Rightarrow 2B = -6 \Rightarrow B = -3$

Now, rewrite the integral using these values:

$\int \dfrac{5(2\mathrm{e}^x - 5) - 3(2\mathrm{e}^x)}{2\mathrm{e}^x - 5} \mathrm{d}x$

$= \int \left( 5 - \dfrac{3(2\mathrm{e}^x)}{2\mathrm{e}^x - 5} \right) \mathrm{d}x$

$= 5x - 3 \log(2\mathrm{e}^x - 5) + \mathrm{c}$

Comparing this with the given expression $\mathrm{A}x + \mathrm{B}\log(2\mathrm{e}^x - 5) + \mathrm{c}$, we get:

$\mathrm{A} = 5, \mathrm{B} = -3$

Answer: $\mathrm{A}=5, \mathrm{~B}=-3$

</details>

---

### Q18. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\int \mathrm{e}^x\left(\dfrac{1-\sin x}{1-\cos x}\right) \mathrm{dx}$ is equal to

**Options:**

- **(A)** $-\mathrm{e}^x \cot \dfrac{x}{2}+\mathrm{c}$, (where c is a constant of integration)
- **(B)** $\mathrm{e}^x \cot \dfrac{x}{2}+\mathrm{c}$, (where c is a constant of integration)
- **(C)** $\mathrm{e}^x \operatorname{cosec} \dfrac{x}{2}+\mathrm{c}$, ( where c is a constant of integration)
- **(D)** $-\mathrm{e}^x \operatorname{cosec} \dfrac{x}{2}+\mathrm{c}$, (where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\mathrm{e}^x \cot \dfrac{x}{2}+\mathrm{c}$, (where c is a constant of integration)**

**Detailed Solution:**

Let $I = \int \mathrm{e}^x\left(\dfrac{1-\sin x}{1-\cos x}\right) \mathrm{dx}$

Using the trigonometric identities $1 - \cos x = 2 \sin^2 \dfrac{x}{2}$ and $\sin x = 2 \sin \dfrac{x}{2} \cos \dfrac{x}{2}$:

$I = \int \mathrm{e}^x \left( \dfrac{1 - 2 \sin \dfrac{x}{2} \cos \dfrac{x}{2}}{2 \sin^2 \dfrac{x}{2}} \right) \mathrm{dx}$

$I = \int \mathrm{e}^x \left( \dfrac{1}{2} \operatorname{cosec}^2 \dfrac{x}{2} - \cot \dfrac{x}{2} \right) \mathrm{dx}$

$I = \int \mathrm{e}^x \left( -\cot \dfrac{x}{2} + \dfrac{1}{2} \operatorname{cosec}^2 \dfrac{x}{2} \right) \mathrm{dx}$

Let $f(x) = -\cot \dfrac{x}{2}$, then $f'(x) = \dfrac{1}{2} \operatorname{cosec}^2 \dfrac{x}{2}$.

Using the standard integral $\int \mathrm{e}^x (f(x) + f'(x)) \mathrm{dx} = \mathrm{e}^x f(x) + \mathrm{c}$:

$I = -\mathrm{e}^x \cot \dfrac{x}{2} + \mathrm{c}$

Answer: $-\mathrm{e}^x \cot \dfrac{x}{2}+\mathrm{c}$, (where c is a constant of integration)

</details>

---

### Q19. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{(\log x-1)^2}{\left[1+(\log x)^2\right]^2} d x=$ (where $C$ is constant of integration.)

**Options:**

- **(A)** $\frac{\log x}{(1+\log x)^2}+C$
- **(B)** $\frac{e^{\log x}}{1+\log x}+C$
- **(C)** $\frac{x}{1+(\log x)^2}+C$
- **(D)** $\frac{\log x}{1+(\log x)^2}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{x}{1+(\log x)^2}+C$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{(\log x-1)^2}{\left\{1+(\log x)^2\right\}^2} \mathrm{~d} x=\int \frac{(\log x)^2+1-2 \log x}{\left\{1+(\log x)^2\right\}^2} \mathrm{~d} x \\ & =\int\left\{\frac{1}{1+(\log x)^2}-\frac{2 \log x}{\left\{1+(\log x)^2\right\}^2}\right\} \mathrm{d} x \\ & \int\left\{x\left\{\frac{-2 \log x}{x \cdot\left(1+(\log x)^2\right)^2}\right\}+\frac{1}{1+(\log x)^2}\right\} \mathrm{d} x \\ & =\frac{x}{1+(\log x)^2}+C\end{aligned}$

</details>

---

### Q20. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int(x-a)\left(x^{n-1}+x^{n-2} a+\ldots . .+a^{n-1}\right) d x=$ (where $C$ is a constant of integration)

**Options:**

- **(A)** $\frac{x^{n+1}}{n+1}-a^n x+C$
- **(B)** $x^n-a^n+C$
- **(C)** $\frac{x^{n+1}}{n+1}-a^n+C$
- **(D)** $n a^{n-1}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{x^{n+1}}{n+1}-a^n x+C$**

**Detailed Solution:**

$\begin{aligned} & \int(x-a)\left(x^{n-1}+x^{n-2} \cdot a+\ldots \ldots+a^{n-1}\right) d x \\ & =\int\left(x^n-a^n\right) d x \\ & =\frac{x^{n+1}}{n+1}-a^n x+c\end{aligned}$

</details>

---

### Q21. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\sin \frac{5 x}{2}}{\sin \frac{x}{2}} d x=$
(where $C$ is a constant of integration.)

**Options:**

- **(A)** $x+\sin x+2 \sin 2 x+C$
- **(B)** $x+2 \sin x+2 \sin 2 x+C$
- **(C)** $x+2 \sin x+\sin 2 x+C$
- **(D)** $x+\sin x+\sin 2 x+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x+2 \sin x+\sin 2 x+C$**

**Detailed Solution:**

$\begin{aligned} & \int \frac{\sin \frac{5 x}{2}}{\sin \frac{x}{2}} d x=\int \frac{\sin \left(\frac{x}{2}+2 x\right)}{\sin \frac{x}{2}} d x \\ & =\int \frac{\sin \frac{x}{2} \cos 2 x+\cos \frac{x}{2} \sin 2 x}{\sin \frac{x}{2}} d x \\ & \int\left(\cos 2 x+\cos \frac{x}{2} \cdot 4 \cos \frac{x}{2} \cdot \cos x\right) d x \\ & =\int(\cos 2 x+2(1+\cos x) \cos x) d x \\ & =\int\left(\cos 2 x+2 \cos x+2 \cos ^2 x\right) d x \\ & =\int(\cos 2 x+2 \cos x+1+\cos 2 x) d x\end{aligned}$
$\begin{aligned} & =\int(1+2 \cos x+2 \cos x) d x \\ & =x+2 \sin x+\sin 2 x+C\end{aligned}$

</details>

---

### Q22. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{\sin x}{\sin (x-\alpha)} d x=A x+B \log \sin (x-\alpha)+c$, then the value of $\mathrm{A}$ and $\mathrm{B}$ are respectively (where $\mathrm{c}$ is a constant of integration)

**Options:**

- **(A)** $\cos \alpha, \sin \alpha$
- **(B)** $\sin \alpha, \cos \alpha$
- **(C)** $-\cos \alpha, \sin \alpha$
- **(D)** $-\sin \alpha, \cos \alpha$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\cos \alpha, \sin \alpha$**

**Detailed Solution:**

$$
\begin{aligned}
& \text { Let } I=\int \frac{\sin x}{\sin (x-\alpha)} d x \\
& =\int \frac{\sin [(x-\alpha)+\alpha]}{\sin (x-\alpha)} d x=\int \frac{\sin (x-\alpha) \cos \alpha+\cos (x-\alpha) \sin \alpha}{\sin (x-\alpha)} \\
& =\cos \alpha \int d x+\sin \alpha \int \frac{\cos (x-\alpha)}{\sin (x-\alpha)} d x=(\cos \alpha)(x)+(\sin \alpha) \\
& \log |\sin (x-\alpha)|+c
\end{aligned}
$$
Comparing with given data, we get $\mathrm{A}=\cos \alpha$ and $\mathrm{B}=\sin \alpha$

</details>

---

### Q23. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{1}{\cos x+\sqrt{3} \sin x} d x=$

**Options:**

- **(A)** $2 \log \left[\tan \left(\frac{\mathrm{x}}{2}+\frac{\pi}{12}\right)\right]+\mathrm{c}$
- **(B)** $\frac{1}{2} \log \left[\tan \left(\frac{x}{2}-\frac{\pi}{12}\right)\right]+c$
- **(C)** $\frac{1}{2} \log \left[\tan \left(\frac{\mathrm{x}}{2}+\frac{\pi}{12}\right)\right]+\mathrm{c}$
- **(D)** $2 \log \left[\tan \left(\frac{x}{2}-\frac{\pi}{12}\right)\right]+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2} \log \left[\tan \left(\frac{\mathrm{x}}{2}+\frac{\pi}{12}\right)\right]+\mathrm{c}$**

**Detailed Solution:**

Dividing numerator and denominator by 2 , we get
$$
=\frac{1}{2} \int \frac{\mathrm{dx}}{\left(\frac{1}{2} \cos \mathrm{x}+\frac{\sqrt{3}}{2} \sin \mathrm{x}\right)}=\frac{1}{2} \int \frac{\mathrm{dx}}{\sin \left(\mathrm{x}+\frac{\pi}{6}\right)}=\frac{1}{2} \log \left|\tan \left(\frac{\mathrm{x}}{2}+\frac{\pi}{12}\right)\right|+\mathrm{C}
$$

</details>

---

### Q24. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int e^x\left(\frac{x-1}{x^2}\right) d x=$

**Options:**

- **(A)** $\frac{-e^x}{x^2}+c$
- **(B)** $\frac{-e^x}{x}+c$
- **(C)** $\frac{e^x}{x^2}+c$
- **(D)** $\frac{e^x}{x}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{e^x}{x}+c$**

**Detailed Solution:**

Let $I=\int e^x\left(\frac{x-1}{x^2}\right) d x=\int e^x\left(\frac{1}{x}-\frac{1}{x^2}\right) d x=e^x\left(\frac{1}{x}\right)+c$

</details>

---

### Q25. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$$
\int[1+2 \tan x(\tan x+\sec x)]^{\frac{1}{2}} d x=
$$

**Options:**

- **(A)** $\log [\sec x(\sec x-\tan \mathrm{x})]+\mathrm{c}$
- **(B)** $\log [\operatorname{cosec} x(\sec x+\tan x)]+c$
- **(C)** $\log [\sec x(\sec x+\tan x)]+c$
- **(D)** $\log [\sec \mathrm{x}+\tan \mathrm{x}]+\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log [\sec x(\sec x+\tan x)]+c$**

**Detailed Solution:**

Let $\left.I=\int[1+2 \tan x(\tan x+\sec x)]^{1 / 2} d x=\int 1+2 \tan ^2 x+2 \tan x \sec x\right)^{1 / 2} d x$
$$
\int\left[\left(1+\tan ^2 x\right)+\tan ^2 x+2 \sec x \tan x\right]^{1 / 2} d x=\int\left(\sec ^2 x+\tan ^2 x+2 \sec x \tan x\right)^{1 / 2} d x
$$

$$
\begin{aligned}
& =\int\left[(\sec x+\tan x)^2\right]^{1 / 2} d x=\int(\sec x+\tan x) d x=\int \sec x d x+\int \tan x d x \\
& =\log |\sec x+\tan x|-\log |\cos x|+c \quad=\log \frac{|\sec x+\tan x|}{|\cos x|}+c \\
& =\log [\sec x(\sec x+\tan x)]+c
\end{aligned}
$$

</details>

---

### Q26. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{d x}{x^{2}+4 x+13}=$

**Options:**

- **(A)** $\frac{1}{3} \tan ^{-1}\left(\frac{x+2}{3}\right)+c$
- **(B)** $\frac{1}{6} \log \left(\frac{x-1}{x+5}\right)+c$
- **(C)** $\frac{1}{6} \tan ^{-1}\left(\frac{x+2}{3}\right)+c$
- **(D)** $3 \tan ^{-1}\left(\frac{x+2}{3}\right)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{3} \tan ^{-1}\left(\frac{x+2}{3}\right)+c$**

**Detailed Solution:**

(D)
$\int \frac{1}{x^{2}+4 x+13} d x$
$=\int \frac{1}{x^{2}+4 x+4+9} d x=\int \frac{1}{(x+2)^{2}+3^{2}} d x=\frac{1}{3} \tan ^{-1}\left(\frac{x-2}{3}\right)-c$

</details>

---

### Q27. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f^{\prime}(x)=k(\cos x-\sin x), f^{\prime}(0)=3, f\left(\frac{\pi}{2}\right)=15$, then $f(x)=$

**Options:**

- **(A)** $3(\sin x+\cos x)+12$
- **(B)** $3(\sin x+\cos x)-12$
- **(C)** $-3(\sin x+\cos x)-12$
- **(D)** $12(\sin x+\cos x)+3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3(\sin x+\cos x)+12$**

**Detailed Solution:**

$f^{\prime}(x)=k(\cos x-\sin x)$ 
$f^{\prime}(0)=3 \quad f(\pi / 2)=15$ 
$k=3$ then $f(x)=8$
Integrate $f^{\prime}(x)$
$f(x)=k \sin x+k \cos x+c$
$f(x)=3 \sin x+3 \cos x+c$
$f(\pi / 2)=15$
$c+3=15$
$c=12$
$f(x)=3 \sin x+3 \cos x+12$

</details>

---

### Q28. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{d x}{\cos 2 x-\cos ^{2} x}=$

**Options:**

- **(A)** $-\cot x+c$
- **(B)** $\tan x+c$
- **(C)** $-\tan x+c$
- **(D)** $\cot x+\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\cot x+\mathrm{c}$**

**Detailed Solution:**

(B)
$\begin{aligned} \int \frac{d x}{\cos 2 x-\cos ^{2} x} &=\int \frac{1}{2 \cos ^{2} x-1-\cos ^{2} x} d x=\int \frac{1}{\cos ^{2} x-1} d x \\ &=\int \frac{-1}{1-\cos ^{2} x} d x=-\int \frac{d x}{\sin ^{2} x}=\int-\cos e c^{2} x d x=\cot x+c \end{aligned}$

</details>

---

### Q29. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{4 e^{x}+6 e^{-x}}{9 e^{x}-4 e^{-x}} d x=A x+B \log \left|9 e^{2 x}-4\right|+c$, then
(Where $c$ is constant of integration)

**Options:**

- **(A)** $A=\frac{3}{2}, B=\frac{35}{36}$
- **(B)** $A=\frac{1}{2}, B=\frac{35}{36}$
- **(C)** $A=\frac{-3}{2}, B=\frac{35}{36}$
- **(D)** $A=\frac{-3}{2}, B=\frac{36}{35}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $A=\frac{-3}{2}, B=\frac{35}{36}$**

**Detailed Solution:**

$I=\int \frac{4 e^{2 x}+6}{9 e^{2 x}-4} d x$
$4 e^{2 x}+6=A\left(18 e^{2 x}\right)+B\left(9 e^{2 x}-4\right)...(1)$
$4 e^{2 x}+6=(18 A+9 B) e^{2 x}-4 B$
$\therefore-4 \mathrm{~B}=6 \Rightarrow \mathrm{B}=\frac{-3}{2}$ and $18 \mathrm{~A}+9 \mathrm{~B}=4$
$\therefore \quad 18 \mathrm{~A}-\frac{9 \times 3}{2}=4 \Rightarrow 18 \mathrm{~A}=\frac{35}{2} \Rightarrow \mathrm{A}=\frac{35}{36}$
$\therefore 4 e^{2 x}+6=\frac{35}{36}\left(18 e^{2 x}\right)-\frac{3}{2}\left(9 e^{2 x}-4\right)$
$I=\int\left[\frac{\frac{35}{36}\left(18 e^{2 x}\right)}{9 e^{2 x}-4}-\frac{\frac{3}{2}\left(9 e^{x}-4\right)}{9 e^{x}-4}\right] d x$
$I=\frac{35}{36} \log \left|9 e^{2 x}-4\right|-\frac{3}{2} x+c=A x+B \log \left|9 e^{2 x}-4\right|+c$
$\Rightarrow \mathrm{A}=-\frac{3}{2}$ and $\mathrm{B}=\frac{35}{36}$

</details>

---

### Q30. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{d x}{\cos 2 x+\sin ^{2} x}=$

**Options:**

- **(A)** $\sin x+c$
- **(B)** $\tan x+c$
- **(C)** $\sec ^{2} x+c$
- **(D)** $\cos x+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\tan x+c$**

**Detailed Solution:**

$\begin{aligned} I &=\int \frac{d x}{1-2 \sin ^{2} x+\sin ^{2} x} \\ &=\int \frac{d x}{1-\sin ^{2} x}=\int \frac{d x}{\cos ^{2} x}=\int \sec ^{2} x d x=\tan x+c \end{aligned}$

</details>

---

### Q31. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f^{\prime}(x)=k(\cos x+\sin x)$ and $f(0)=9, f\left(\frac{\pi}{2}\right)=15$, then $f(x)=$

**Options:**

- **(A)** $3(\sin x-\cos x)+12$
- **(B)** $3(\sin x-\cos x)-12$
- **(C)** $3(\sin x+\cos x)+12$
- **(D)** $3(\cos x+\sin x)-12$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3(\sin x-\cos x)+12$**

**Detailed Solution:**

$f^{\prime}(x)=k(\cos x+\sin x)$
On integrating both sides, we get
$f(x)=k(\sin x-\cos x)+C$
$f(0)=k(0-1)+C$
$f(0)=-k+C \Rightarrow-k+C=9$ ...(1)
Also $f\left(\frac{\pi}{2}\right)=k\left(\sin \frac{\pi}{2}-\cos \frac{\pi}{2}\right)+C$
$15=k+C$ ...(2)
Adding (1) $\&(2)$ we get
$2 C=24 \Rightarrow C=12 \Rightarrow k=3$
$\therefore f(x)=3(\sin x-\cos x)+12$

</details>

---

### Q32. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$$
\int \frac{d x}{\sqrt{5+4 x-x^{2}}}=
$$

**Options:**

- **(A)** $\sin ^{-1}\left(\frac{x-2}{3}\right)+c$
- **(B)** $\log \left|(x-2)+\sqrt{5+4 x-x^{2}}\right|+c$
- **(C)** $\log \left|(x+2)+\sqrt{5+4 x-x^{2}}\right|+c$
- **(D)** $\sin ^{-1}\left(\frac{x+2}{3}\right)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sin ^{-1}\left(\frac{x-2}{3}\right)+c$**

**Detailed Solution:**

$I=\int \frac{d x}{\sqrt{9+\left(-4+4 x-x^{2}\right)}}=\int \frac{d x}{\sqrt{(3)^{2}-(x-2)^{2}}}=\sin ^{-1}\left(\frac{x-2}{3}\right)+c$

</details>

---

### Q33. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If r is the radius of spherical balloon at time t and the surface area of balloon changes at a constant rate K, then ….

**Options:**

- **(A)** <math><mn>4</mn><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mi>K</mi><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mi>c</mi></math>
- **(B)** <math><mn>8</mn><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>K</mi><mi>t</mi><mo>+</mo><mi>c</mi></math>
- **(C)** <math><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mi>K</mi><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mi>c</mi></math>
- **(D)** <math><mn>4</mn><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>K</mi><mi>t</mi><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>4</mn><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>K</mi><mi>t</mi><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

According to question,
<math><mfrac><mrow><mi>d</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mfenced separators="|"><mrow><mn>4</mn><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>=</mo><mi>K</mi></math> ( <math><mo>∵</mo><mi></mi></math> surface area of spherical ballon with radius r is <math><mn>4</mn><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></math> )
<math><mo>⇒</mo><mn>4</mn><mi>π</mi><mfenced separators="|"><mrow><mn>2</mn><mi>r</mi></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>r</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mi>K</mi><mo>⇒</mo><mn>8</mn><mi>π</mi><mi>r</mi><mtext> </mtext><mi>d</mi><mi>r</mi><mo>=</mo><mi>K</mi><mi>d</mi><mi>t</mi></math>
On Integrating both sides, we get
<math><mn>8</mn><mi>π</mi><mo>∫</mo><mi>r</mi><mtext> </mtext><mi>d</mi><mi>r</mi><mo>=</mo><mi>K</mi><mo>∫</mo><mi>d</mi><mi>t</mi></math>
<math><mo>⇒</mo><mn>8</mn><mi>π</mi><mfrac><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mi>K</mi><mi>t</mi><mo>+</mo><mi>C</mi></math>
<math><mo>⇒</mo><mn>4</mn><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>K</mi><mi>t</mi><mo>+</mo><mi>C</mi></math>

</details>

---

### Q34. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `2`

<math><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>.</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></mrow><mo>=</mo></math>

**Options:**

- **(A)** sec  <math><mi>x</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(B)** sec  <math><mi>x</mi><mo>.</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(C)** sec  <math><mi>x</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>-</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(D)** sec <math><mi>x</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cosec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>-</mo><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) sec <math><mi>x</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cosec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>-</mo><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mrow></math>**

**Detailed Solution:**

<math> <mrow> <mi>I</mi><mo>=</mo><mstyle displaystyle="true"> <mrow><mo>∫</mo> <mrow> <mfrac> <mn>1</mn> <mrow> <mi>sin</mi><mi>x</mi><mo>⋅</mo><msup> <mrow> <mi>cos</mi></mrow> <mn>2</mn> </msup> <mi>x</mi></mrow> </mfrac> </mrow> </mrow> </mstyle></mrow> </math>
<math> <mrow> <mi>I</mi><mo>=</mo><mstyle displaystyle="true"> <mrow><mo>∫</mo> <mrow> <mfrac> <mrow> <msup> <mrow> <mi>sin</mi></mrow> <mn>2</mn> </msup> <mi>x</mi><mo>+</mo><msup> <mrow> <mi>cos</mi></mrow> <mn>2</mn> </msup> <mi>x</mi></mrow> <mrow> <mi>sin</mi><mi>x</mi><mo>⋅</mo><msup> <mrow> <mi>cos</mi></mrow> <mn>2</mn> </msup> <mi>x</mi></mrow> </mfrac> <mi>d</mi><mi>x</mi></mrow> </mrow> </mstyle></mrow> </math>
<math> <mrow> <mi>I</mi><mo>=</mo><mstyle displaystyle="true"> <mrow><mo>∫</mo> <mrow> <mfrac> <mrow> <msup> <mrow> <mi>sin</mi></mrow> <mn>2</mn> </msup> <mi>x</mi></mrow> <mrow> <mi>sin</mi><mi>x</mi><mo>⋅</mo><msup> <mrow> <mi>cos</mi></mrow> <mn>2</mn> </msup> <mi>x</mi></mrow> </mfrac> <mi>d</mi><mi>x</mi><mo>+</mo><mstyle displaystyle="true"> <mrow><mo>∫</mo> <mrow> <mfrac> <mrow> <msup> <mrow> <mi>cos</mi></mrow> <mn>2</mn> </msup> <mi>x</mi><mtext> </mtext><mi>d</mi><mi>x</mi></mrow> <mrow> <mi>sin</mi><mi>x</mi><mtext> </mtext><msup> <mrow> <mi>cos</mi></mrow> <mn>2</mn> </msup> <mi>x</mi></mrow> </mfrac> </mrow> </mrow> </mstyle></mrow> </mrow> </mstyle></mrow> </math>
<math> <mrow> <mi>I</mi><mo>=</mo><mstyle displaystyle="true"> <mrow><mo>∫</mo> <mrow> <mi>sec</mi><mtext> </mtext><mi>x</mi><mtext> </mtext><mi>tan</mi><mtext> </mtext><mi>x</mi><mtext> </mtext><mi>d</mi><mi>x</mi><mo>+</mo><mstyle displaystyle="true"> <mrow><mo>∫</mo> <mrow> <mtext>cosec</mtext><mtext> </mtext><mi>x</mi><mtext> </mtext><mi>d</mi><mi>x</mi></mrow> </mrow> </mstyle></mrow> </mrow> </mstyle></mrow> </math>
<math> <mrow> <mi>I</mi><mo>=</mo><mi>sec</mi><mi>x</mi><mo>+</mo><mi>ln</mi><mrow><mo>|</mo> <mrow> <mtext>cosec</mtext><mtext> </mtext><mi>x</mi><mo>−</mo><mi>cot</mi><mi>x</mi></mrow> <mo>|</mo></mrow><mo>+</mo><mi>c</mi></mrow> </math>

</details>

---

### Q35. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{1}{16 x^{2}+9} d x$ is equal to

**Options:**

- **(A)** $\frac{1}{3} \tan ^{-1}\left(\frac{4 x}{3}\right)+c$
- **(B)** $\frac{1}{4} \tan ^{-1}\left(\frac{4 x}{3}\right)+c$
- **(C)** $\frac{1}{12} \tan ^{-1}\left(\frac{4 x}{3}\right)+c$
- **(D)** $\frac{1}{12} \tan ^{-1}\left(\frac{3 x}{4}\right)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{12} \tan ^{-1}\left(\frac{4 x}{3}\right)+c$**

**Detailed Solution:**

$\begin{aligned} \int \frac{1}{16 x^{2}+9} d x &=\frac{1}{16} \int \frac{1}{x^{2}+\left(\frac{3}{4}\right)^{2}} d x \\ &=\frac{1}{16} \times \frac{4}{3} \tan ^{-1}\left(\frac{x}{3 / 4}\right)+c \\ &=\frac{1}{12} \tan ^{-1}\left(\frac{4 x}{3}\right)+c \end{aligned}$

</details>

---

### Q36. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=x, g(x)=\sin x$, then $\int f(g(x)) d x$ is equal to

**Options:**

- **(A)** $\sin x+c$
- **(B)** $-\cos x+c$
- **(C)** $\frac{x^{2}}{2}+c$
- **(D)** $x \sin x+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\cos x+c$**

**Detailed Solution:**

$\begin{aligned} \int f(g(x)) d x &=\int f(\sin x) d x \\ &=\int \sin x d x \\ &=-\cos x+c \end{aligned}$

</details>

---

