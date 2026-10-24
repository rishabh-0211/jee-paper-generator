# MHT CET Mathematics - Differentiation

## Topic 4: Logarithmic differentiation

**Total Questions:** 49

---

### Q1. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = x^{x^{x^{\cdot^{\cdot^{\cdot^{\infty}}}}}}$, then $\dfrac{dy}{dx}$ is:

**Options:**

- **(A)** $yx^{y-1}$
- **(B)** $\dfrac{y^2}{x(1 - y\log x)}$
- **(C)** $\dfrac{y}{x(1 + y\log x)}$
- **(D)** $yx^{y+1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{y^2}{x(1 - y\log x)}$**

**Detailed Solution:**

Given $y = x^{x^{x^{\cdot^{\cdot^{\cdot^{\infty}}}}}}$

This can be written as $y = x^y$

Taking logarithm on both sides:

$\log y = y \log x$

Differentiating both sides with respect to $x$:

$\dfrac{1}{y} \dfrac{dy}{dx} = \dfrac{dy}{dx} \log x + y \cdot \dfrac{1}{x}$

$\dfrac{dy}{dx} \left( \dfrac{1}{y} - \log x \right) = \dfrac{y}{x}$

$\dfrac{dy}{dx} \left( \dfrac{1 - y \log x}{y} \right) = \dfrac{y}{x}$

$\dfrac{dy}{dx} = \dfrac{y^2}{x(1 - y \log x)}$

Answer: $\dfrac{y^2}{x(1 - y\log x)}$

</details>

---

### Q2. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = (\log x)^{\log x}$ and $\dfrac{dy}{dx} = \dfrac{y}{x} \times f(x)$ then $f(x) = \ldots$

**Options:**

- **(A)** $(\log x)^x$
- **(B)** $\log(\log x)$
- **(C)** $x^{\log x}$
- **(D)** $\log(\log x^e)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log(\log x^e)$**

**Detailed Solution:**

Given $y = (\log x)^{\log x}$

Taking logarithm on both sides:

$\log y = \log x \cdot \log(\log x)$

Differentiating both sides with respect to $x$ using the product rule:

$\dfrac{1}{y} \dfrac{dy}{dx} = \dfrac{d}{dx}(\log x) \cdot \log(\log x) + \log x \cdot \dfrac{d}{dx}(\log(\log x))$

$\dfrac{1}{y} \dfrac{dy}{dx} = \dfrac{1}{x} \cdot \log(\log x) + \log x \cdot \left(\dfrac{1}{\log x} \cdot \dfrac{1}{x}\right)$

$\dfrac{1}{y} \dfrac{dy}{dx} = \dfrac{\log(\log x)}{x} + \dfrac{1}{x}$

$\dfrac{dy}{dx} = \dfrac{y}{x} [1 + \log(\log x)]$

Since $1 = \log e$, we can rewrite the expression inside the bracket as:

$1 + \log(\log x) = \log e + \log(\log x) = \log(e \log x) = \log(\log x^e)$

Thus, $\dfrac{dy}{dx} = \dfrac{y}{x} \log(\log x^e)$

Comparing this with $\dfrac{dy}{dx} = \dfrac{y}{x} \times f(x)$, we get:

$f(x) = \log(\log x^e)$

Answer: $\log(\log x^e)$

</details>

---

### Q3. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x^y y^x = 1$, then $\dfrac{dy}{dx}$ is equal to

**Options:**

- **(A)** $\dfrac{y^2(1 + \log y)}{x^2(1 - \log x)}$
- **(B)** $\dfrac{y^2(1 + \log x)}{x^2(1 - \log y)}$
- **(C)** $\dfrac{-y^2(1 - \log x)}{x^2(1 - \log y)}$
- **(D)** $\dfrac{-x^2(1 - \log x)}{y^2(1 - \log y)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{-y^2(1 - \log x)}{x^2(1 - \log y)}$**

**Detailed Solution:**

Given $x^y y^x = 1$

Taking logarithm on both sides, we get:

$y \log x + x \log y = 0$

Differentiating both sides with respect to $x$:

$\dfrac{dy}{dx} \log x + y \left( \dfrac{1}{x} \right) + 1 \cdot \log y + x \left( \dfrac{1}{y} \dfrac{dy}{dx} \right) = 0$

$\dfrac{dy}{dx} \left( \log x + \dfrac{x}{y} \right) = - \left( \dfrac{y}{x} + \log y \right)$

$\dfrac{dy}{dx} \left( \dfrac{y \log x + x}{y} \right) = - \left( \dfrac{y + x \log y}{x} \right)$

$\dfrac{dy}{dx} = - \dfrac{y}{x} \left( \dfrac{y + x \log y}{x + y \log x} \right)$

From the equation $y \log x + x \log y = 0$, we can write $x \log y = -y \log x$ and $y \log x = -x \log y$.

Substituting these into the numerator and denominator respectively:

$\dfrac{dy}{dx} = - \dfrac{y}{x} \left( \dfrac{y - y \log x}{x - x \log y} \right)$

$\dfrac{dy}{dx} = - \dfrac{y}{x} \left( \dfrac{y(1 - \log x)}{x(1 - \log y)} \right)$

$\dfrac{dy}{dx} = \dfrac{-y^2(1 - \log x)}{x^2(1 - \log y)}$

Answer: $\dfrac{-y^2(1 - \log x)}{x^2(1 - \log y)}$

</details>

---

### Q4. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = x^{\sqrt{x}}$, then $\dfrac{dy}{dx} =$

**Options:**

- **(A)** $\dfrac{y}{2\sqrt{x}}(2 + \log x)$
- **(B)** $\dfrac{y}{\sqrt{x}}(2 + \log x)$
- **(C)** $\dfrac{y}{2\sqrt{x}}(2 - \log x)$
- **(D)** $\dfrac{y}{\sqrt{x}}(2 - \log x)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{y}{2\sqrt{x}}(2 + \log x)$**

**Detailed Solution:**

Given $y = x^{\sqrt{x}}$

Taking logarithm on both sides:

$\log y = \sqrt{x} \log x$

Differentiating both sides with respect to $x$ using the product rule:

$\dfrac{1}{y} \dfrac{dy}{dx} = \sqrt{x} \cdot \dfrac{d}{dx}(\log x) + \log x \cdot \dfrac{d}{dx}(\sqrt{x})$

$\dfrac{1}{y} \dfrac{dy}{dx} = \sqrt{x} \cdot \dfrac{1}{x} + \log x \cdot \dfrac{1}{2\sqrt{x}}$

$\dfrac{1}{y} \dfrac{dy}{dx} = \dfrac{1}{\sqrt{x}} + \dfrac{\log x}{2\sqrt{x}}$

$\dfrac{1}{y} \dfrac{dy}{dx} = \dfrac{2 + \log x}{2\sqrt{x}}$

$\dfrac{dy}{dx} = \dfrac{y}{2\sqrt{x}}(2 + \log x)$

Answer: $\dfrac{y}{2\sqrt{x}}(2 + \log x)$

</details>

---

### Q5. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y = 2^x + (\sin x)^x$, then $\dfrac{dy}{dx} = $

**Options:**

- **(A)** $2^x \log 2 + (\sin x)^x [x \cot x + \log(\sin x)]$
- **(B)** $2^x \log 2 + (\sin x)^x [x \cot x - \log(\sin x)]$
- **(C)** $2^x \log 2 + (\sin x)^x [-x \cot x - \log(\sin x)]$
- **(D)** $2^x \log 2 + (\sin x)^x [-x \cot x + \log(\sin x)]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2^x \log 2 + (\sin x)^x [x \cot x + \log(\sin x)]$**

**Detailed Solution:**

Given $y = 2^x + (\sin x)^x$

Let $y = u + v$, where $u = 2^x$ and $v = (\sin x)^x$

Differentiating $u$ with respect to $x$:

$\dfrac{du}{dx} = 2^x \log 2$

For $v = (\sin x)^x$, taking logarithm on both sides:

$\log v = x \log(\sin x)$

Differentiating with respect to $x$:

$\dfrac{1}{v} \dfrac{dv}{dx} = 1 \cdot \log(\sin x) + x \cdot \dfrac{1}{\sin x} \cdot \cos x$

$\dfrac{1}{v} \dfrac{dv}{dx} = \log(\sin x) + x \cot x$

$\dfrac{dv}{dx} = v [x \cot x + \log(\sin x)]$

$\dfrac{dv}{dx} = (\sin x)^x [x \cot x + \log(\sin x)]$

Therefore, $\dfrac{dy}{dx} = \dfrac{du}{dx} + \dfrac{dv}{dx}$

$\dfrac{dy}{dx} = 2^x \log 2 + (\sin x)^x [x \cot x + \log(\sin x)]$

Answer: $2^x \log 2 + (\sin x)^x [x \cot x + \log(\sin x)]$

</details>

---

### Q6. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x^y \cdot y^x = 1$ then the value of $\dfrac{dy}{dx}$ is

**Options:**

- **(A)** $-\dfrac{(y + x\log y)}{(x + y\log x)} \cdot \dfrac{y}{x}$
- **(B)** $\dfrac{(y + x\log y)}{(x + y\log x)} \cdot \dfrac{y}{x}$
- **(C)** $-\dfrac{(x + y\log y)}{(y + x\log x)} \cdot \dfrac{y}{x}$
- **(D)** $\dfrac{y}{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\dfrac{(y + x\log y)}{(x + y\log x)} \cdot \dfrac{y}{x}$**

**Detailed Solution:**

Given $x^y \cdot y^x = 1$

Taking logarithm on both sides:

$\log(x^y \cdot y^x) = \log(1)$

$y \log x + x \log y = 0$

Differentiating both sides with respect to $x$:

$\dfrac{dy}{dx} \log x + y \cdot \dfrac{1}{x} + 1 \cdot \log y + x \cdot \dfrac{1}{y} \dfrac{dy}{dx} = 0$

$\dfrac{dy}{dx} \left( \log x + \dfrac{x}{y} \right) + \left( \dfrac{y}{x} + \log y \right) = 0$

$\dfrac{dy}{dx} \left( \dfrac{y \log x + x}{y} \right) = - \left( \dfrac{y + x \log y}{x} \right)$

$\dfrac{dy}{dx} = - \dfrac{(y + x \log y)}{(x + y \log x)} \cdot \dfrac{y}{x}$

Answer: $-\dfrac{(y + x\log y)}{(x + y\log x)} \cdot \dfrac{y}{x}$

</details>

---

### Q7. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x = \sqrt{2^{\tan^{-1} t}}$ and $y = \sqrt[3]{2^{\cot^{-1} t}}$, then $\dfrac{dy}{dx} = $ ...

**Options:**

- **(A)** $\dfrac{2x^2}{3y^3}$
- **(B)** $\dfrac{-2x}{3y}$
- **(C)** $\dfrac{-2y}{3x}$
- **(D)** $\dfrac{2y}{3x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{-2y}{3x}$**

**Detailed Solution:**

Given $x = \sqrt{2^{\tan^{-1} t}}$ and $y = \sqrt[3]{2^{\cot^{-1} t}}$.

Squaring the first equation and cubing the second, we get:

$x^2 = 2^{\tan^{-1} t}$

$y^3 = 2^{\cot^{-1} t}$

Multiplying both equations:

$x^2 y^3 = 2^{\tan^{-1} t} \cdot 2^{\cot^{-1} t}$

$x^2 y^3 = 2^{\tan^{-1} t + \cot^{-1} t}$

Since $\tan^{-1} t + \cot^{-1} t = \dfrac{\pi}{2}$, we have:

$x^2 y^3 = 2^{\pi/2}$

Differentiating both sides with respect to $x$:

$2x y^3 + x^2 \left(3y^2 \dfrac{dy}{dx}\right) = 0$

$3x^2 y^2 \dfrac{dy}{dx} = -2x y^3$

$\dfrac{dy}{dx} = \dfrac{-2x y^3}{3x^2 y^2}$

$\dfrac{dy}{dx} = \dfrac{-2y}{3x}$

Answer: $\dfrac{-2y}{3x}$

</details>

---

### Q8. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = (x^2 + 1)^{\sin x}$ for $x > 0$ such that $\dfrac{dy}{dx} = y\left[\dfrac{2x \sin x}{g(x)} + \cos x \cdot \log[g(x)]\right]$, then the function $\dfrac{1}{g(x)}$ is...

**Options:**

- **(A)** increasing
- **(B)** strictly increasing.
- **(C)** decreasing
- **(D)** strictly decreasing

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) strictly decreasing**

**Detailed Solution:**

Given $y = (x^2 + 1)^{\sin x}$

Taking natural logarithm on both sides:

$\log y = \sin x \cdot \log(x^2 + 1)$

Differentiating with respect to $x$:

$\dfrac{1}{y} \dfrac{dy}{dx} = \cos x \cdot \log(x^2 + 1) + \sin x \cdot \dfrac{2x}{x^2 + 1}$

$\dfrac{dy}{dx} = y \left[ \dfrac{2x \sin x}{x^2 + 1} + \cos x \cdot \log(x^2 + 1) \right]$

Comparing with the given expression, we get $g(x) = x^2 + 1$.

Let $h(x) = \dfrac{1}{g(x)} = \dfrac{1}{x^2 + 1}$.

Differentiating $h(x)$ with respect to $x$:

$h'(x) = \dfrac{-2x}{(x^2 + 1)^2}$

For $x > 0$, $h'(x) < 0$.

Thus, the function $\dfrac{1}{g(x)}$ is strictly decreasing for $x > 0$.

</details>

---

### Q9. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = [(x+1)(2x+1)(3x+1)\ldots\ldots(nx+1)]^4$, where $n \in N$ and $\dfrac{dy}{dx}$ at $x = 0$ is $2k$, then the value of $k$ is

**Options:**

- **(A)** $\dfrac{n(n+1)}{2}$
- **(B)** $n(n+1)$
- **(C)** $2n(n+1)$
- **(D)** $4n(n+1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $n(n+1)$**

**Detailed Solution:**

Given $y = [(x+1)(2x+1)(3x+1)\ldots(nx+1)]^4$

Taking natural logarithm on both sides:

$\ln y = 4 [\ln(x+1) + \ln(2x+1) + \ln(3x+1) + \ldots + \ln(nx+1)]$

Differentiating with respect to $x$:

$\dfrac{1}{y} \dfrac{dy}{dx} = 4 \left[ \dfrac{1}{x+1} + \dfrac{2}{2x+1} + \dfrac{3}{3x+1} + \ldots + \dfrac{n}{nx+1} \right]$

At $x = 0$, $y = [(0+1)(0+1)(0+1)\ldots(0+1)]^4 = 1$

Substituting $x = 0$ and $y = 1$ in the derivative expression:

$\dfrac{1}{1} \left( \dfrac{dy}{dx} \right)_{x=0} = 4 [1 + 2 + 3 + \ldots + n]$

$\left( \dfrac{dy}{dx} \right)_{x=0} = 4 \left[ \dfrac{n(n+1)}{2} \right] = 2n(n+1)$

Given that $\left( \dfrac{dy}{dx} \right)_{x=0} = 2k$

$2k = 2n(n+1)$

$k = n(n+1)$

Answer: $n(n+1)$

</details>

---

### Q10. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Derivative of $x^{\left(x^x\right)}$ is

**Options:**

- **(A)** $x^{\left(x^x\right)}\left(x^x+1+\log x\right)$
- **(B)** $x^{\left(x^x\right)}\left(x^x+\log x\right)$
- **(C)** $x^{\left(x^x\right)}\left(x^x+x^{x-1} \log x(1+\log x)\right)$
- **(D)** $x^{\left(x^x\right)}\left(x^{x-1}+x^x \log x(1+\log x)\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x^{\left(x^x\right)}\left(x^{x-1}+x^x \log x(1+\log x)\right)$**

**Detailed Solution:**

Let $y = x^{\left(x^x\right)}$

Taking logarithm on both sides:

$\log y = x^x \log x$

Differentiating with respect to $x$ using the product rule:

$\dfrac{1}{y} \dfrac{dy}{dx} = \dfrac{d}{dx}(x^x) \cdot \log x + x^x \cdot \dfrac{d}{dx}(\log x)$

We know that $\dfrac{d}{dx}(x^x) = x^x(1 + \log x)$

$\dfrac{1}{y} \dfrac{dy}{dx} = x^x(1 + \log x) \log x + x^x \cdot \dfrac{1}{x}$

$\dfrac{1}{y} \dfrac{dy}{dx} = x^x \log x(1 + \log x) + x^{x-1}$

$\dfrac{dy}{dx} = y \left(x^{x-1} + x^x \log x(1 + \log x)\right)$

$\dfrac{dy}{dx} = x^{\left(x^x\right)} \left(x^{x-1} + x^x \log x(1 + \log x)\right)$

Answer: $x^{\left(x^x\right)}\left(x^{x-1}+x^x \log x(1+\log x)\right)$

</details>

---

### Q11. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(\theta)=\cos \theta_1 \cdot \cos \theta_2 \cdot \cos \theta_3 \cdots \cdots \cdots \cdot \cos \theta_n$ (where $\frac{d\theta_i}{d\theta}=1$), then $\tan \theta_1+\tan \theta_2+\tan \theta_3+\cdots \cdots \cdots+\tan \theta_{\mathrm{n}}=$

**Options:**

- **(A)** $\frac{-\mathrm{f}^{\prime}(\theta)}{\mathrm{f}(\theta)}$
- **(B)** $\frac{f^{\prime}(\theta)}{f(\theta)}$
- **(C)** $\frac{-\mathrm{f}^{\prime \prime}(\theta)}{\mathrm{f}^{\prime}(\theta)}$
- **(D)** $\frac{\mathrm{f}^{\prime \prime}(\theta)}{\mathrm{f}^{\prime}(\theta)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{-\mathrm{f}^{\prime}(\theta)}{\mathrm{f}(\theta)}$**

**Detailed Solution:**

$f(\theta) = \cos \theta_1 \cdot \cos \theta_2 \cdot \cos \theta_3 \cdots \cos \theta_n$

Taking natural logarithm on both sides:

$\ln f(\theta) = \ln(\cos \theta_1) + \ln(\cos \theta_2) + \dots + \ln(\cos \theta_n)$

Differentiating with respect to $\theta$:

$\dfrac{1}{f(\theta)} f'(\theta) = \dfrac{1}{\cos \theta_1}(-\sin \theta_1)\dfrac{d\theta_1}{d\theta} + \dfrac{1}{\cos \theta_2}(-\sin \theta_2)\dfrac{d\theta_2}{d\theta} + \dots + \dfrac{1}{\cos \theta_n}(-\sin \theta_n)\dfrac{d\theta_n}{d\theta}$

Given $\dfrac{d\theta_i}{d\theta} = 1$ for all $i=1, 2, \dots, n$:

$\dfrac{f'(\theta)}{f(\theta)} = -\tan \theta_1 - \tan \theta_2 - \dots - \tan \theta_n$

$\tan \theta_1 + \tan \theta_2 + \dots + \tan \theta_n = \dfrac{-f'(\theta)}{f(\theta)}$

Answer: $\frac{-\mathrm{f}^{\prime}(\theta)}{\mathrm{f}(\theta)}$

</details>

---

### Q12. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{y}=x^x+x^{\frac{1}{x}}$, then $\frac{\mathrm{dy}}{\mathrm{d} x}$ is equal to

**Options:**

- **(A)** $x^x(1+\log x)+x^{\frac{1}{x}} \frac{1}{x^2}(1-\log x)$
- **(B)** $\left(x^x+x^{\frac{1}{x}}\right)\left[1+\log x+\frac{1}{x^2}(1-\log x)\right]$
- **(C)** $\left(x^x+x^{\frac{1}{x}}\right)\left[(1+\log x)-\frac{1}{x^2}(1-\log x)\right]$
- **(D)** $x^x(1+\log x)-x^{\frac{1}{x}} \frac{1}{x^2}(1-\log x)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x^x(1+\log x)+x^{\frac{1}{x}} \frac{1}{x^2}(1-\log x)$**

**Detailed Solution:**

Let $y = u + v$ where $u = x^x$ and $v = x^{\dfrac{1}{x}}$.

Taking logarithm of $u = x^x$, we get $\log u = x \log x$.

Differentiating with respect to $x$, we get $\dfrac{1}{u} \dfrac{du}{dx} = x \cdot \dfrac{1}{x} + \log x \cdot 1 = 1 + \log x$.

$\dfrac{du}{dx} = x^x(1 + \log x)$.

Taking logarithm of $v = x^{\dfrac{1}{x}}$, we get $\log v = \dfrac{1}{x} \log x$.

Differentiating with respect to $x$, we get $\dfrac{1}{v} \dfrac{dv}{dx} = \dfrac{x \cdot \dfrac{1}{x} - \log x \cdot 1}{x^2} = \dfrac{1 - \log x}{x^2}$.

$\dfrac{dv}{dx} = x^{\dfrac{1}{x}} \dfrac{1}{x^2} (1 - \log x)$.

Therefore, $\dfrac{dy}{dx} = \dfrac{du}{dx} + \dfrac{dv}{dx} = x^x(1 + \log x) + x^{\dfrac{1}{x}} \dfrac{1}{x^2} (1 - \log x)$.

Answer: $x^x(1+\log x)+x^{\frac{1}{x}} \frac{1}{x^2}(1-\log x)$

</details>

---

### Q13. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If
$y=[(x+1)(2 x+1)(3 x+1) \ldots \ldots \ldots(\mathrm{n} x+1)]^2,$
then $\frac{\mathrm{d} y}{\mathrm{~d} x}$ at $x=0$ is

**Options:**

- **(A)** $2 \mathrm{n}(\mathrm{n}+1)$
- **(B)** $\mathrm{n}(\mathrm{n}+1)$
- **(C)** $\frac{\mathrm{n}(\mathrm{n}+1)}{2}$
- **(D)** $\left(\frac{\mathrm{n}(\mathrm{n}+1)}{2}\right)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{n}(\mathrm{n}+1)$**

**Detailed Solution:**

Given $y = [(x+1)(2x+1)(3x+1) \dots (nx+1)]^2$

Let $f(x) = (x+1)(2x+1)(3x+1) \dots (nx+1)$

Then $y = [f(x)]^2$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = 2f(x)f'(x)$

At $x=0$, $f(0) = (0+1)(0+1) \dots (0+1) = 1$

Taking logarithm of $f(x)$ on both sides:

$\ln f(x) = \ln(x+1) + \ln(2x+1) + \dots + \ln(nx+1)$

Differentiating with respect to $x$:

$\dfrac{1}{f(x)}f'(x) = \dfrac{1}{x+1} + \dfrac{2}{2x+1} + \dots + \dfrac{n}{nx+1}$

Substituting $x=0$:

$\dfrac{1}{f(0)}f'(0) = 1 + 2 + \dots + n$

Since $f(0) = 1$, we get:

$f'(0) = \dfrac{n(n+1)}{2}$

Therefore, $\left(\dfrac{dy}{dx}\right)_{x=0} = 2f(0)f'(0) = 2(1)\left(\dfrac{n(n+1)}{2}\right) = n(n+1)$

Answer: $\mathrm{n}(\mathrm{n}+1)$

</details>

---

### Q14. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y=(\sin x)^{\tan x}$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}$ is equal to

**Options:**

- **(A)** $(\sin x)^{\tan x}\left(1+\sec ^2 x \log (\sin x)\right)$
- **(B)** $\tan x(\sin x)^{\tan x-1} \cos x$
- **(C)** $(\sin x)^{\tan x} \sec ^2 x \log \sin x$
- **(D)** $\tan x(\sin x)^{\tan x-1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(\sin x)^{\tan x}\left(1+\sec ^2 x \log (\sin x)\right)$**

**Detailed Solution:**

Given $y = (\sin x)^{\tan x}$

Taking logarithm on both sides:

$\log y = \tan x \log (\sin x)$

Differentiating both sides with respect to $x$ using the product rule:

$\dfrac{1}{y} \dfrac{\mathrm{d} y}{\mathrm{d} x} = \dfrac{\mathrm{d}}{\mathrm{d} x}(\tan x) \cdot \log (\sin x) + \tan x \cdot \dfrac{\mathrm{d}}{\mathrm{d} x}(\log (\sin x))$

$\dfrac{1}{y} \dfrac{\mathrm{d} y}{\mathrm{d} x} = \sec^2 x \log (\sin x) + \tan x \left( \dfrac{1}{\sin x} \cdot \cos x \right)$

$\dfrac{1}{y} \dfrac{\mathrm{d} y}{\mathrm{d} x} = \sec^2 x \log (\sin x) + \left( \dfrac{\sin x}{\cos x} \right) \left( \dfrac{\cos x}{\sin x} \right)$

$\dfrac{1}{y} \dfrac{\mathrm{d} y}{\mathrm{d} x} = \sec^2 x \log (\sin x) + 1$

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = y \left( 1 + \sec^2 x \log (\sin x) \right)$

Substituting $y = (\sin x)^{\tan x}$:

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = (\sin x)^{\tan x} \left( 1 + \sec^2 x \log (\sin x) \right)$

Answer: $(\sin x)^{\tan x}\left(1+\sec ^2 x \log (\sin x)\right)$

</details>

---

### Q15. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(x)=\log _{x^2}(\log x)$, then at $x=\mathrm{e}, \mathrm{f}^{\prime}(x)$ has the value

**Options:**

- **(A)** $\frac{1}{\mathrm{e}^2}$
- **(B)** $\frac{1}{\mathrm{e}}$
- **(C)** $\mathrm{e}^{2 \cdot}$
- **(D)** $\frac{1}{2 \mathrm{e}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{2 \mathrm{e}}$**

**Detailed Solution:**

Given $f(x) = \log_{x^2}(\log x)$

Using the change of base formula and assuming the natural logarithm (base $e$) as standard in calculus, we can write:

$f(x) = \dfrac{\log_e(\log_e x)}{\log_e(x^2)} = \dfrac{\log_e(\log_e x)}{2 \log_e x}$

Differentiating with respect to $x$ using the quotient rule:

$f'(x) = \dfrac{1}{2} \left[ \dfrac{\log_e x \cdot \dfrac{d}{dx}(\log_e(\log_e x)) - \log_e(\log_e x) \cdot \dfrac{d}{dx}(\log_e x)}{(\log_e x)^2} \right]$

$f'(x) = \dfrac{1}{2} \left[ \dfrac{\log_e x \cdot \left(\dfrac{1}{\log_e x} \cdot \dfrac{1}{x}\right) - \log_e(\log_e x) \cdot \dfrac{1}{x}}{(\log_e x)^2} \right]$

$f'(x) = \dfrac{1}{2x} \left[ \dfrac{1 - \log_e(\log_e x)}{(\log_e x)^2} \right]$

Substitute $x = e$:

$f'(e) = \dfrac{1}{2e} \left[ \dfrac{1 - \log_e(\log_e e)}{(\log_e e)^2} \right]$

Since $\log_e e = 1$ and $\log_e 1 = 0$:

$f'(e) = \dfrac{1}{2e} \left[ \dfrac{1 - 0}{1^2} \right] = \dfrac{1}{2e}$

Answer: $\frac{1}{2 \mathrm{e}}$

</details>

---

### Q16. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=(1+x)\left(1+x^2\right)\left(1+x^4\right)\left(1+x^8\right)$, then $f^{\prime}(1)=$

**Options:**

- **(A)** 60
- **(B)** 80
- **(C)** 240
- **(D)** 120

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 120**

**Detailed Solution:**

Given $f(x) = (1+x)(1+x^2)(1+x^4)(1+x^8)$

Taking logarithm on both sides:

$\ln f(x) = \ln(1+x) + \ln(1+x^2) + \ln(1+x^4) + \ln(1+x^8)$

Differentiating with respect to $x$:

$\dfrac{f'(x)}{f(x)} = \dfrac{1}{1+x} + \dfrac{2x}{1+x^2} + \dfrac{4x^3}{1+x^4} + \dfrac{8x^7}{1+x^8}$

Substituting $x = 1$:

$f(1) = (1+1)(1+1)(1+1)(1+1) = 16$

$\dfrac{f'(1)}{16} = \dfrac{1}{2} + \dfrac{2}{2} + \dfrac{4}{2} + \dfrac{8}{2}$

$\dfrac{f'(1)}{16} = \dfrac{15}{2}$

$f'(1) = 16 \times \dfrac{15}{2} = 120$

Answer: 120

</details>

---

### Q17. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y$ is a function of $x$ and $\log (x+y)=2 x y$, then the value of $y^{\prime}(0)$ is

**Options:**

- **(A)** 1
- **(B)** -1
- **(C)** 2
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

Given equation is $\log(x+y) = 2xy$.

Substituting $x=0$ in the given equation:

$\log(0+y) = 2(0)y$

$\log y = 0 \Rightarrow y = 1$

Differentiating the given equation with respect to $x$:

$\dfrac{1}{x+y} \left(1 + y^{\prime}\right) = 2y + 2x y^{\prime}$

Substituting $x=0$ and $y=1$ in the above equation:

$\dfrac{1}{0+1} (1 + y^{\prime}(0)) = 2(1) + 2(0)y^{\prime}(0)$

$1 + y^{\prime}(0) = 2$

$y^{\prime}(0) = 1$

Answer: 1

</details>

---

### Q18. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y$ is a function of $x$ and $\log (x+y)=2 x y$, then the value of $y^{\prime}(0)$ is

**Options:**

- **(A)** 1
- **(B)** -1
- **(C)** 2
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

Given equation is $\log(x+y) = 2xy$.

Substituting $x = 0$ in the given equation:

$\log(0+y) = 2(0)y$

$\log(y) = 0 \Rightarrow y = 1$

Differentiating the given equation with respect to $x$:

$\dfrac{1}{x+y} \left(1 + y'\right) = 2y + 2xy'$

Substituting $x = 0$ and $y = 1$:

$\dfrac{1}{0+1} (1 + y'(0)) = 2(1) + 2(0)y'(0)$

$1 + y'(0) = 2$

$y'(0) = 1$

Answer: 1

</details>

---

### Q19. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\log (x+y)=\sin (x+y)$, then $\dfrac{\mathrm{d} y}{\mathrm{~d} x}$ is

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** 0
- **(D)** -1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -1**

**Detailed Solution:**

Given $\log(x+y) = \sin(x+y)$

Differentiating both sides with respect to $x$:

$\dfrac{1}{x+y} \left(1 + \dfrac{\mathrm{d}y}{\mathrm{d}x}\right) = \cos(x+y) \left(1 + \dfrac{\mathrm{d}y}{\mathrm{d}x}\right)$

$\left( \dfrac{1}{x+y} - \cos(x+y) \right) \left(1 + \dfrac{\mathrm{d}y}{\mathrm{d}x}\right) = 0$

Since $\dfrac{1}{x+y} - \cos(x+y) \neq 0$ for the constant value of $x+y$ satisfying the given equation, we get:

$1 + \dfrac{\mathrm{d}y}{\mathrm{d}x} = 0$

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = -1$

Answer: -1

</details>

---

### Q20. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\left((x+1)(4 x+1)(9 x+1) \ldots\left(\mathrm{n}^2 x+1\right)\right)^2$, then $\dfrac{\mathrm{dy}}{\mathrm{d} x}$ at $x=0$ is

**Options:**

- **(A)** $\dfrac{\mathrm{n}(\mathrm{n}+1)(2 \mathrm{n}+1)}{4}$
- **(B)** $\dfrac{\mathrm{n}(\mathrm{n}+1)(2 \mathrm{n}+1)}{6}$
- **(C)** $\dfrac{\mathrm{n}(\mathrm{n}+1)(2 \mathrm{n}+1)}{2}$
- **(D)** $\dfrac{\mathrm{n}(\mathrm{n}+1)(2 \mathrm{n}+1)}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{\mathrm{n}(\mathrm{n}+1)(2 \mathrm{n}+1)}{3}$**

**Detailed Solution:**

Given $y = \left( (x+1)(4x+1)(9x+1) \ldots (n^2 x+1) \right)^2$

Taking the natural logarithm on both sides:

$\ln y = 2 \left( \ln(x+1) + \ln(4x+1) + \ln(9x+1) + \ldots + \ln(n^2 x+1) \right)$

Differentiating with respect to $x$:

$\dfrac{1}{y} \dfrac{dy}{dx} = 2 \left( \dfrac{1}{x+1} + \dfrac{4}{4x+1} + \dfrac{9}{9x+1} + \ldots + \dfrac{n^2}{n^2 x+1} \right)$

At $x=0$, the value of $y$ is:

$y = \left( (0+1)(0+1)(0+1) \ldots (0+1) \right)^2 = 1$

Substituting $x=0$ and $y=1$ into the derivative equation:

$\dfrac{1}{1} \left. \dfrac{dy}{dx} \right|_{x=0} = 2 \left( 1 + 4 + 9 + \ldots + n^2 \right)$

$\left. \dfrac{dy}{dx} \right|_{x=0} = 2 \sum_{k=1}^{n} k^2$

Using the formula for the sum of squares of the first $n$ natural numbers:

$\left. \dfrac{dy}{dx} \right|_{x=0} = 2 \left( \dfrac{n(n+1)(2n+1)}{6} \right)$

$\left. \dfrac{dy}{dx} \right|_{x=0} = \dfrac{n(n+1)(2n+1)}{3}$

Answer: $\dfrac{\mathrm{n}(\mathrm{n}+1)(2 \mathrm{n}+1)}{3}$

</details>

---

### Q21. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y=a \log{|x|}+b x^2+x$ has its extreme value at $x=-1$ and $x=2$, then the value of $\mathrm{a}+\mathrm{b}$ is

**Options:**

- **(A)** $\dfrac{3}{2}$
- **(B)** $\dfrac{1}{2}$
- **(C)** $\dfrac{5}{2}$
- **(D)** $\dfrac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{3}{2}$**

**Detailed Solution:**

Given $y = a \log|x| + b x^2 + x$

Differentiating with respect to $x$, we get

$\dfrac{dy}{dx} = \dfrac{a}{x} + 2bx + 1$

Since $y$ has extreme values at $x = -1$ and $x = 2$, $\dfrac{dy}{dx} = 0$ at these points.

At $x = -1$:

$\dfrac{a}{-1} + 2b(-1) + 1 = 0 \Rightarrow a + 2b = 1$

At $x = 2$:

$\dfrac{a}{2} + 2b(2) + 1 = 0 \Rightarrow a + 8b = -2$

Solving the two equations by subtracting the first from the second:

$6b = -3 \Rightarrow b = -\dfrac{1}{2}$

Substituting $b$ in the first equation:

$a + 2\left(-\dfrac{1}{2}\right) = 1 \Rightarrow a - 1 = 1 \Rightarrow a = 2$

Therefore, $a + b = 2 - \dfrac{1}{2} = \dfrac{3}{2}$

Answer: $\dfrac{3}{2}$

</details>

---

### Q22. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\log \left[\mathrm{e}^{5 x}\left(\dfrac{3 x-4}{x+5}\right)^{\dfrac{4}{3}}\right]$, then $\dfrac{\mathrm{d} y}{\mathrm{~d} x}$ is equal to

**Options:**

- **(A)** $5+\dfrac{4}{3 x-4}-\dfrac{4}{3(x+5)}$
- **(B)** $5+\dfrac{4}{3(3 x-4)}-\dfrac{4}{3(x+5)}$
- **(C)** $5 x+\dfrac{4}{3 x-4}-\dfrac{4}{3(x+5)}$
- **(D)** $5+\dfrac{12}{3 x-4}-\dfrac{4}{(x+5)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $5+\dfrac{4}{3 x-4}-\dfrac{4}{3(x+5)}$**

**Detailed Solution:**

Given $y = \log \left[ \mathrm{e}^{5 x} \left( \dfrac{3 x - 4}{x + 5} \right)^{\dfrac{4}{3}} \right]$

Using the properties of logarithms, $\log(ab) = \log a + \log b$ and $\log(a^b) = b \log a$:

$y = \log(\mathrm{e}^{5x}) + \log \left( \dfrac{3 x - 4}{x + 5} \right)^{\dfrac{4}{3}}$

$y = 5x \log \mathrm{e} + \dfrac{4}{3} [ \log(3x - 4) - \log(x + 5) ]$

Since $\log \mathrm{e} = 1$:

$y = 5x + \dfrac{4}{3} \log(3x - 4) - \dfrac{4}{3} \log(x + 5)$

Differentiating with respect to $x$:

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = \dfrac{\mathrm{d}}{\mathrm{d} x}(5x) + \dfrac{4}{3} \dfrac{\mathrm{d}}{\mathrm{d} x} \log(3x - 4) - \dfrac{4}{3} \dfrac{\mathrm{d}}{\mathrm{d} x} \log(x + 5)$

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = 5 + \dfrac{4}{3} \left( \dfrac{3}{3x - 4} \right) - \dfrac{4}{3} \left( \dfrac{1}{x + 5} \right)$

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = 5 + \dfrac{4}{3x - 4} - \dfrac{4}{3(x + 5)}$

Answer: $5+\dfrac{4}{3 x-4}-\dfrac{4}{3(x+5)}$

</details>

---

### Q23. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(x)=\log _{x^2}\left(\log _{\mathrm{e}} x\right)$, then $\mathrm{f}^{\prime}(x)$ at $x=\mathrm{e}$ is

**Options:**

- **(A)** 1
- **(B)** $\dfrac{1}{\mathrm{e}}$
- **(C)** $\dfrac{1}{2 \mathrm{e}}$
- **(D)** $\dfrac{1}{4 \mathrm{e}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{2 \mathrm{e}}$**

**Detailed Solution:**

Given $f(x) = \log_{x^2}(\log_e x)$

Using the change of base formula, we can write:

$f(x) = \dfrac{\ln(\ln x)}{\ln(x^2)} = \dfrac{\ln(\ln x)}{2 \ln x}$

Differentiating with respect to $x$ using the quotient rule:

$f^{\prime}(x) = \dfrac{1}{2} \left[ \dfrac{\dfrac{d}{dx}(\ln(\ln x)) \cdot \ln x - \ln(\ln x) \cdot \dfrac{d}{dx}(\ln x)}{(\ln x)^2} \right]$

$f^{\prime}(x) = \dfrac{1}{2} \left[ \dfrac{\left(\dfrac{1}{\ln x} \cdot \dfrac{1}{x}\right) \cdot \ln x - \ln(\ln x) \cdot \dfrac{1}{x}}{(\ln x)^2} \right]$

$f^{\prime}(x) = \dfrac{1}{2} \left[ \dfrac{\dfrac{1}{x} - \dfrac{\ln(\ln x)}{x}}{(\ln x)^2} \right] = \dfrac{1 - \ln(\ln x)}{2x(\ln x)^2}$

Substituting $x = e$:

$f^{\prime}(e) = \dfrac{1 - \ln(\ln e)}{2e(\ln e)^2}$

Since $\ln e = 1$ and $\ln(1) = 0$:

$f^{\prime}(e) = \dfrac{1 - 0}{2e(1)^2} = \dfrac{1}{2e}$

Answer: $\dfrac{1}{2 \mathrm{e}}$

</details>

---

### Q24. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(x)=3^x ; \mathrm{g}(x)=4^x$, then $\frac{\mathrm{f}^{\prime}(0)-\mathrm{g}^{\prime}(0)}{1+\mathrm{f}^{\prime}(0) \mathrm{g}^{\prime}(0)}$ is

**Options:**

- **(A)** $\frac{\log \left(\frac{3}{4}\right)}{1+(\log 3)(\log 4)}$
- **(B)** $\frac{\log \left(\frac{3}{4}\right)}{1+\log 12}$
- **(C)** $\frac{\log 12}{1+\log 12}$
- **(D)** $\frac{\log \left(\frac{3}{4}\right)}{1-\log 12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\log \left(\frac{3}{4}\right)}{1+(\log 3)(\log 4)}$**

**Detailed Solution:**

$\begin{aligned} \mathrm{f}^{\prime}(x)=3^x \log 3 & \Rightarrow \mathrm{f}^{\prime}(0)=\log 3 \\ \mathrm{~g}^{\prime}(x)=4^x \log 4 & \Rightarrow \mathrm{g}^{\prime}(0)=\log 4 \\ \therefore \quad \frac{\mathrm{f}^{\prime}(0)-\mathrm{g}^{\prime}(0)}{1+\mathrm{f}^{\prime}(0) \mathrm{g}^{\prime}(0)} & =\frac{\log 3-\log 4}{1+(\log 3)(\log 4)} \\ & =\frac{\log \left(\frac{3}{4}\right)}{1+(\log 3)(\log 4)}\end{aligned}$

</details>

---

### Q25. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y$ is a function of $x$ and $\log (x+y)=2 x y$, then the value of $y^{\prime}(0)$ is

**Options:**

- **(A)** 1
- **(B)** -1
- **(C)** 2
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

$\log (x+y)=2 x y$
Differentiating w.r.t. $x$, we get
$\begin{aligned}
& \frac{1}{x+y}\left(1+\frac{\mathrm{d} y}{\mathrm{~d} x}\right)=2 x \frac{\mathrm{d} y}{\mathrm{~d} x}+2 y \\
& \frac{1}{x+y}+\frac{1}{(x+y)} \frac{\mathrm{d} y}{\mathrm{~d} x}=2 x \frac{\mathrm{d} y}{\mathrm{~d} x}+2 y \\
& \left(\frac{1}{x+y}-2 x\right) \frac{\mathrm{d} y}{\mathrm{~d} x}=2 y-\frac{1}{x+y} \\
& \frac{\mathrm{d} y}{\mathrm{~d} x}\left(\frac{1}{x+y}-2 x\right)=2 y-\frac{1}{x+y} \\
& \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{\left(2 y-\frac{1}{x+y}\right)}{\left(\frac{1}{x+y}-2 x\right)} \\
& \text { For } x=0, \log (y)=0 \\
& \Rightarrow y=1 \\
& \left.\frac{\mathrm{d} y}{\mathrm{~d} x}\right|_{(0,1)}=\frac{\left(2-\frac{1}{0+1}\right)}{\left(\frac{1}{0+1}-0\right)}=1
\end{aligned}$

</details>

---

### Q26. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For $x>1$, if $(2 x)^{2 y}=4 e^{2 x-2 y}$, then $\left(1+\log _e 2 x\right)^2 \frac{\mathrm{d} y}{\mathrm{~d} x}$ is equal to

**Options:**

- **(A)** $x \log _{\mathrm{e}} 2 x$
- **(B)** $\log _e 2 x$
- **(C)** $\frac{x \log _{\mathrm{e}} 2 x+\log _{\mathrm{e}} 2}{x}$
- **(D)** $\frac{x \log _{\mathrm{e}} 2 x-\log _{\mathrm{e}} 2}{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{x \log _{\mathrm{e}} 2 x-\log _{\mathrm{e}} 2}{x}$**

**Detailed Solution:**

$(2 x)^{2 y}=4 \cdot e^{2 x-2 y}$
$\Rightarrow 2 y \log 2 x=\log 4+2 x-2 y$
$\Rightarrow y=\frac{x+\log 2}{1+\log 2 x}$
$\begin{aligned} & \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{(1+\log 2 x)-(x+\log 2) \cdot \frac{1}{2 x} \cdot 2}{(1+\log 2 x)^2} \\ & \Rightarrow(1+\log 2 x)^2 \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{x \log 2 x-\log 2}{x}\end{aligned}$

</details>

---

### Q27. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=b \cdot e^{a x}+a \cdot e^{b x}$, then $f^{\prime \prime}(0)=$

**Options:**

- **(A)** $(a+b)$
- **(B)** $a b(a+b)^2$
- **(C)** $2 a b(a+b)$
- **(D)** $a b(a+b)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $a b(a+b)$**

**Detailed Solution:**

$\begin{aligned} & f(x)=b \cdot e^{a x}+a \cdot e^{b x} \\ & \Rightarrow f^{\prime}(x)=b a e^{a x}+a b e^{b x} \\ & \Rightarrow f^{\prime \prime}(x)=b a^2 e^{a x}+a b^2 e^{b x} \\ & \Rightarrow f^{\prime \prime}(0)=b a^2+a b^2=a b(a+b)\end{aligned}$

</details>

---

### Q28. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\frac{\mathrm{d}}{\mathrm{d} x}\left(\log \sqrt{\frac{1+\sin x}{1-\sin x}}\right)=$

**Options:**

- **(A)** $\cos ^2 x$
- **(B)** $\sec ^2 x$
- **(C)** $\cos x$
- **(D)** $\sec x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sec x$**

**Detailed Solution:**

$\begin{aligned} & \frac{d\left\{\log \sqrt{\frac{1+\sin x}{1-\sin x}}\right\}}{\mathrm{d} x}=\frac{\mathrm{d}\left\{\frac{1}{2} \log \left(\frac{1+\sin x}{1-\sin x}\right)\right\}}{\mathrm{d} x} \\ & =\frac{1}{2} \times \frac{1}{\frac{1+\sin x}{1-\sin x}} \times \frac{(1-\sin x)(0+\cos x)-(1+\sin x)(0-\cos x)}{(1-\sin x)^2} \\ & =\frac{1}{2} \times \frac{2 \cos x}{(1+\sin x)(1-\sin x)} \\ & =\frac{\cos x}{1-\sin ^2 x}=\frac{\cos x}{\cos ^2 x}=\sec x\end{aligned}$

</details>

---

### Q29. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\log \sqrt{\frac{1+\sin x}{1-\sin x}}$, then $\frac{d y}{d x}$ at $x=\frac{\pi}{3}$ is

**Options:**

- **(A)** $2$
- **(B)** $\frac{1}{4}$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{-1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2$**

**Detailed Solution:**

$\begin{aligned} & y=\log \sqrt{\frac{1+\sin x}{1-\sin x}}=\frac{1}{2}\{\log (1+\sin x)-\log (1-\sin x)\} \\ & \left\{\frac{1}{1+\sin x} \cdot \cos x-\frac{1}{1-\sin x} \cdot(-\cos x)\right\} \\ & \Rightarrow \frac{d y}{d x}_{\text {at } x=\frac{\pi}{3}}=\frac{1}{2}\left\{\frac{1}{1+\sin \frac{\pi}{3}} \cos \frac{\pi}{3}-\frac{1}{1-\sin \frac{\pi}{3}} \cdot\left(-\cos \frac{\pi}{3}\right)\right\} \\ & =\frac{1}{2} \frac{1}{2}\left\{\frac{1}{1+\frac{\sqrt{3}}{2}} \cdot \frac{1}{2}+\frac{1}{1-\frac{\sqrt{3}}{2}} \cdot \frac{1}{2}\right\} \\ & =\frac{1}{2}\left\{\frac{1}{2+\sqrt{3}}+\frac{1}{2-\sqrt{3}}\right\} \\ & =\frac{1}{2} \times \frac{4}{4-3}=2 \\ & \end{aligned}$

</details>

---

### Q30. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y=3 \cos (\log x)+4 \sin (\log x)$, then $x^2 y_2+x y_1=$

**Options:**

- **(A)** xy
- **(B)** $-x y$
- **(C)** $-y$
- **(D)** y

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-y$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{y}=3 \cos (\log \mathrm{x})+4 \sin (\log \mathrm{x}) \\ & \Rightarrow \mathrm{y}_1=-3 \sin (\log \mathrm{x}) \cdot \frac{1}{\mathrm{x}}+4 \cos (\log \mathrm{x}) \cdot \frac{1}{\mathrm{x}} \\ & \Rightarrow \mathrm{xy}_1=-3 \sin (\log \mathrm{x})+4 \cos (\log \mathrm{x}) \\ & \Rightarrow 1 \cdot \mathrm{y}_1+\mathrm{x} \cdot \mathrm{y}_2=-3 \cos (\log \mathrm{x}) \cdot \frac{1}{\mathrm{x}}-4 \sin (\log \mathrm{x}) \cdot \frac{1}{\mathrm{x}} \\ & \Rightarrow \mathrm{xy}_1+\mathrm{x}^2 \mathrm{y}_2=-3 \cos (\log \mathrm{x})-4 \sin (\log \mathrm{x})=-\mathrm{y}\end{aligned}$

</details>

---

### Q31. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

For $x>1$, if $(2 x)^{2 y}=4 e^{2 x-2 y}$, then $(1+\log 2 x)^2 \frac{d y}{d x}$ is equal to

**Options:**

- **(A)** $\frac{\log 2 x+\log 2}{x}$
- **(B)** $\frac{x \log 2 x-\log 2}{x}$
- **(C)** $\frac{x \log 2 x+\log 2}{x}$
- **(D)** $\frac{\log 2 x-\log 2}{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{x \log 2 x-\log 2}{x}$**

**Detailed Solution:**

$\begin{aligned} & (2 x)^{2 y}=4 e^{2 x-2 y} \Rightarrow 2 y \log (2 x)=\log 4+2 x-2 y \\ & \Rightarrow 2 y \log (2 x)=2 \log 2+2 x-2 y\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/iPiak6D7ZfFFfvDilprh06IJ-yTJx_tqDLJBXvJR0nM.original.fullsize.png">
Different w.r.t $x$
$\begin{aligned} & \frac{d y}{d x} \cdot \log (2 x)+y \cdot \frac{1}{2 x} \cdot 2=0+1-\frac{d y}{d x} \\ & \Rightarrow \frac{d y}{d x}(1+\log 2 x)=1-\frac{y}{x}=1-\frac{x+\log 2}{x(1+\log 2 x)} \\ & {\left[\because \text { from }(1) y=\frac{x+\log 2}{(1+\log 2 x)}\right]} \\ & \Rightarrow \frac{d y}{d x}(1+\log 2 x)^2=\frac{x(1+\log 2 x)-x-\log 2}{x} \\ & \Rightarrow(1+\log 2 x)^2=\frac{d y}{d x}=\frac{x \log 2 x-\log 2}{x}\end{aligned}$

</details>

---

### Q32. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x=e^{\left(\frac{x}{y}\right)}$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{x-y}{x \log y}$
- **(B)** $\frac{x-y}{y \log x}$
- **(C)** $\frac{x-y}{x \log x}$
- **(D)** $\frac{x+y}{x \log x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{x-y}{x \log x}$**

**Detailed Solution:**

$x=e^{\left(\frac{x}{y}\right)} \Rightarrow \log _e x=\frac{x}{y} \Rightarrow y \log _e x=x$
Differentiating both sides w.r.t $x$ we get $\frac{d y}{d x} \cdot \log _e x+y \cdot \frac{1}{x}=1$
$\Rightarrow \frac{d y}{d x} \cdot x \log _e x+y=x$
$\Rightarrow \frac{d y}{d x}=\frac{x-y}{x \log _e x}$
Change the option (C) as $\frac{x-y}{x \log x}$

</details>

---

### Q33. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\left(x^x\right) x$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $x^{x^2}(1+\log x)$
- **(B)** $x \cdot x^{x^2}(1+\log x)$
- **(C)** $x^{x^2}(1+2 \log x)$
- **(D)** $x \cdot x^{x^2}(2 \log x+1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x \cdot x^{x^2}(2 \log x+1)$**

**Detailed Solution:**

$y=\left(x^x\right) x \Rightarrow \log y=x \log x^x=x^2 \log x$
Differentiating both sides w.r.t. $\mathrm{x}$
$\begin{aligned} & \frac{1}{y} \cdot \frac{d y}{d x}=x^2 \times \frac{1}{x}+2 x \times \log x \\ & \Rightarrow \frac{d y}{d x}=y(x+2 x \log x) \\ & \Rightarrow \frac{d y}{d x}=\left(x^x\right)^x \cdot x(1+2 \log x) \\ & \Rightarrow \frac{d y}{d x}=x^{x^2} \cdot x(1+2 \log x)\end{aligned}$

</details>

---

### Q34. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x^y \cdot y^x=16$, then $\frac{d y}{d x}$ at $(2,2)$ is

**Options:**

- **(A)** -1
- **(B)** 0
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -1**

**Detailed Solution:**

$x^y \cdot y^x=16$
Taking $\log$ on both sides, $\therefore \mathrm{y} \log \mathrm{x}+\mathrm{x} \log \mathrm{y}=\log 16$
Differentiating w.r.t. $x, \therefore \frac{y}{x}+(\log x) \frac{d y}{d x}+\left(\frac{x}{y}\right) \frac{d y}{d x}+\log y=0$
$$
\begin{aligned}
& \therefore\left[\log x+\frac{x}{y}\right] \frac{d y}{d x}=-\left[\frac{y}{x}+\log y\right] \\
& \therefore \frac{d y}{d x}=\frac{-\left[\frac{y}{x}+\log y\right]}{\left[\log x+\frac{x}{y}\right]} \Rightarrow\left(\frac{d y}{d x}\right)_{(2,2)}=-\left[\frac{(1+\log 2)}{\log 2+1}\right]=-1
\end{aligned}
$$

</details>

---

### Q35. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y=2^{a x}$ and $\left(\frac{d y}{d x}\right)_{x=1}=\log 256$, then $a=$

**Options:**

- **(A)** 4
- **(B)** 2
- **(C)** 8
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2**

**Detailed Solution:**

$y=2^{2 x} \Rightarrow \frac{d y}{d x}=2^{2 x}(\log 2)(a)$
$\therefore\left(\frac{d y}{d x}\right)_{x=1}=\left(2^{a}\right)(a)(\log 2)$
As per condition given
$\left(2^{a}\right)(a)(\log 2)=\log 256=\log (2)^{8}=8 \log 2$
$\therefore\left(2^{a}\right)(a)=8 \Rightarrow a=2$

</details>

---

### Q36. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=x^{x e^{x}}, \frac{d y}{d x}=y \cdot g(x)$, then $g(x)=$

**Options:**

- **(A)** $\left[e^{x}+e^{x}(x+1) \log x\right]$
- **(B)** $\left[e^{x}-e^{x} \cdot x \cdot(1+\log x)\right]$
- **(C)** $\left[e^{x}+e^{x} \cdot x \cdot(1+\log x)\right]$
- **(D)** $\left[e^{x}(x+1) \log x\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[e^{x}+e^{x}(x+1) \log x\right]$**

**Detailed Solution:**

We have $y=x^{x e^{x}}$
$\therefore \log y=x e^{x} \log x$
$\therefore \frac{1}{y} \frac{d y}{d x}=e^{x} \log x+\frac{x e^{x}}{x}+x e^{x} \log x$
$=e^{x} \log x+e^{x}+x e^{x} \log x$
$\therefore \frac{d y}{d x}=y\left[e^{x}+e^{x} \log x(1+x)\right]$

</details>

---

### Q37. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x=e^{(y+e)^{(y+e)}(y+\ldots \ldots \infty)}$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{1-x}{x}$
- **(B)** $\frac{1+x}{x}$
- **(C)** $\frac{1}{x}$
- **(D)** $\frac{x}{1+x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1-x}{x}$**

**Detailed Solution:**

Here $x=e^{y+x}$
Differentiating w.r.t. $\mathrm{x}$
$$
\begin{array}{l}
1=e^{y+x}\left(\frac{d y}{d x}+1\right) \Rightarrow 1=e^{y+x} \frac{d y}{d x}+e^{y+x} \\
\therefore 1=x \cdot \frac{d y}{d x}+x \\
\frac{d y}{d x}=\frac{1-x}{x}
\end{array}
$$

</details>

---

### Q38. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\left(\frac{x^{2}}{x+1}\right)^{x}$ and $\frac{d y}{d x}=y\left[g(x)+\log \left(\frac{x^{2}}{x+1}\right)\right]$, then $g(x)=$

**Options:**

- **(A)** $\frac{x+2}{x+1}$
- **(B)** $x \log \left(\frac{x^{2}}{x+1}\right)$
- **(C)** $\frac{x^{2}}{x+1}$
- **(D)** $\frac{x-1}{x+2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{x+2}{x+1}$**

**Detailed Solution:**

No solution

</details>

---

### Q39. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\log _{10}\left(\frac{x^{3}-y^{3}}{x^{3}+y^{3}}\right)=2$ then $\frac{d x}{d y}=$

**Options:**

- **(A)** $\left(-\frac{99}{101}\right) \frac{x^{2}}{y^{2}}$
- **(B)** $\left(-\frac{101}{99}\right) \frac{x^{2}}{y^{2}}$
- **(C)** $\left(-\frac{101}{99}\right) \frac{y^{2}}{x^{2}}$
- **(D)** $\left(-\frac{99}{101}\right) \frac{y^{2}}{x^{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(-\frac{101}{99}\right) \frac{y^{2}}{x^{2}}$**

**Detailed Solution:**

$\begin{array}{l}
\text { Given } \log _{10}\left(\frac{x^{3}-y^{3}}{x^{3}+y^{3}}\right)=2 \Rightarrow \frac{x^{3}-y^{3}}{x^{3}+y^{3}}=10^{2} \quad \ldots\left[\because \log _{a} m=x \Rightarrow a^{x}=m\right] \\
\therefore x^{3}-y^{3}=100\left(x^{3}+y^{3}\right)
\end{array}$
Differentiating w.r.t. $x$,
$\begin{array}{l}
\quad 3 x^{2}-3 y^{2} \frac{d y}{d x}=100\left(3 x^{2}+3 y^{2} \frac{d y}{d x}\right)\end{array}$
$\therefore x^{2}-100 x^{2}=y^{2}(1+100) \frac{d y}{d x}$ ...[Dividing both sides by 3 ]
$\quad-99 x^{2}=101 y^{2} \frac{d y}{d x} \Rightarrow \frac{d x}{d y}=\left(-\frac{101}{99}\right) \frac{y^{2}}{x^{2}}$

</details>

---

### Q40. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Derivative of <math><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></msub></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow></math> with respect to <math><mi>x</mi></math> is ________

**Options:**

- **(A)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mi>x</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></mrow></mfrac></math>**

**Detailed Solution:**

Let <math><mi>y</mi><mo>=</mo><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></msub><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow></mfenced></math>  
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow></mfenced></math>  
then  <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfrac><mrow><mn>1</mn></mrow><mrow><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub></mrow></mfrac><mfrac><mrow><mi>d</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mo> </mo><mi>x</mi><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mrow><mi mathvariant="normal">g</mi></mrow><mrow><msup><mrow><mi>b</mi></mrow><mrow><mi>α</mi></mrow></msup></mrow></msub><mi></mi><mi>a</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>α</mi></mrow></mfrac><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mrow><mi mathvariant="normal">g</mi></mrow><mrow><mi>b</mi></mrow></msub><mi>a</mi></mrow></mfenced></math>  
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfrac><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></mrow></mfrac><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></math>  
Note: Here, <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>=</mo><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi mathvariant="normal">e</mi></mrow></msub></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>

</details>

---

### Q41. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If then <math><mi>y</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt></mrow><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt><mo>-</mo><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow></math> then <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo></math> ….

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

We have, <math><mi>y</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt></mrow><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn><mo>-</mo><mi>x</mi></msqrt></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
<math><mo>⇒</mo><mi>y</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
<math><mo>⇒</mo><mi>y</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>25</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
<math><mo>⇒</mo><mi>y</mi><mo>=</mo><mn>2</mn><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt></mrow></mfenced></mrow></mrow><mo>-</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mn>25</mn></math>
On differentiating both sides w.r.t.x, we get
<math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt></mrow></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt></mrow></mfrac><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mfenced></math>
<math><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt><mo>+</mo><mi>x</mi></mrow><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt></mrow></mfrac></mrow></mfenced></math>
<math><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></msqrt></mrow></mfrac></math>

</details>

---

### Q42. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `1`

If <math><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mn>10</mn></mrow></msub></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>2</mn> </mrow></mrow></math>, then <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo></math>

**Options:**

- **(A)** <math><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac></math>
- **(B)** <math><mo>-</mo><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></math>**

**Detailed Solution:**

Given, <math><msub><mi>log</mi><mn>10</mn></msub><mo>⁡</mo><mfenced separators="|"><mfrac><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>y</mi><mn>3</mn></msup></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>y</mi><mn>3</mn></msup></mrow></mfrac></mfenced><mo>=</mo><mn>2</mn></math>
<math><mo>⇒</mo><mfenced separators="|"><mfrac><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>y</mi><mn>3</mn></msup></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>y</mi><mn>3</mn></msup></mrow></mfrac></mfenced><mo>=</mo><msup><mfenced><mn>10</mn></mfenced><mn>2</mn></msup><mo>=</mo><mn>100</mn></math>
Applying componendo and dividendo, we get, 
<math><mfrac><msup><mi>x</mi><mn>3</mn></msup><msup><mi>y</mi><mn>3</mn></msup></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>101</mn><mn>99</mn></mfrac><mo>⇒</mo><mfrac><mi>x</mi><mi>y</mi></mfrac><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mfrac><mn>101</mn><mn>99</mn></mfrac></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></math>......(i)
Hence, <math><mi>y</mi><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mfrac><mn>99</mn><mn>101</mn></mfrac></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mi>x</mi></math>
Differentiating, we get,
<math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mfrac><mn>99</mn><mn>101</mn></mfrac></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>=</mo><mfrac><mi>y</mi><mi>x</mi></mfrac></math> (from (i))

</details>

---

### Q43. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

If <math><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mn>10</mn></mrow></msub></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>2</mn></mrow></mrow><mo>,</mo></math> then <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo></math> _______

**Options:**

- **(A)** <math><mo>-</mo><mfrac><mrow><mn>99</mn><mi>x</mi></mrow><mrow><mn>101</mn><mi>y</mi></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>99</mn><mi>x</mi></mrow><mrow><mn>101</mn><mi>y</mi></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>99</mn><mi>y</mi></mrow><mrow><mn>101</mn><mi>x</mi></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>99</mn><mi>y</mi></mrow><mrow><mn>101</mn><mi>x</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mo>-</mo><mfrac><mrow><mn>99</mn><mi>x</mi></mrow><mrow><mn>101</mn><mi>y</mi></mrow></mfrac></math>**

**Detailed Solution:**

Given,  <math><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mn>10</mn></mrow></msub></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>2</mn></mrow></mrow></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>100</mn></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>100</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>100</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>0</mn></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mfrac><mrow><mo>-</mo><mn>99</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>101</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>0</mn></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mn>99</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>101</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math> 
 <math><mo>⇒</mo><mi> </mi><mfenced separators="|"><mrow><mn>2</mn><mo>×</mo><mn>99</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mo>×</mo><mn>101</mn></mrow></mfenced><mi> </mi><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><mn>99</mn><mi>x</mi></mrow><mrow><mn>101</mn><mi>y</mi></mrow></mfrac></math>

</details>

---

### Q44. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $(\log x)^{x}$ with respect to $\log x$ is

**Options:**

- **(A)** $(\log x)^{x}\left[\frac{1}{\log x}+\log (\log x)\right]$
- **(B)** $(\log x)^{x}\left[\log x+\frac{1}{\log (\log x)}\right]$
- **(C)** $x(\log x)^{x}\left[\frac{1}{\log x}+\log (\log x)\right]$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x(\log x)^{x}\left[\frac{1}{\log x}+\log (\log x)\right]$**

**Detailed Solution:**

Let $\quad u=(\log x)^{x}$
$\begin{array}{ll}\Rightarrow & \log u=x \log (\log x) \\ \therefore & \frac{1}{u} \frac{d u}{d x}=x \frac{1}{\log x} \cdot \frac{1}{x}+\log (\log x) \\ \Rightarrow & \quad \frac{d u}{d x}=(\log x)^{x}\left[\frac{1}{\log x}+\log (\log x)\right]\end{array}$
and $\quad v=\log x$
$\therefore \quad \frac{d v}{d x}=\frac{1}{x}$
Now, $\frac{d u}{d v}=(\log x)^{x}\left[\frac{1}{\log x} \times \log (\log x)\right] \times x$
$=x(\log x)^{x}\left[\frac{1}{\log x}+\log (\log x)\right]$

</details>

---

### Q45. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

Find the derivative of $e^{x}+e^{y}=e^{x+y}$

**Options:**

- **(A)** $-e^{x-y}$
- **(B)** $e^{x-y}$
- **(C)** $-e^{y-x}$
- **(D)** $e^{y-x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-e^{y-x}$**

**Detailed Solution:**

$e^{x}+e^{y}=e^{x+y}=e^{x} e^{y}$
$\Rightarrow \quad e^{-y}+e^{-x}=1$
On differentiating, we get $-e^{-y} \frac{d y}{d x}+e^{-x}(-1)=0$
$\Rightarrow \quad \frac{d y}{d x}=\frac{e^{-x}}{-e^{-y}}$
$\Rightarrow \quad \frac{d y}{d x}=-e^{y-x}$

</details>

---

### Q46. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

If $y=x^{n} \log x+x(\log x)^{n}$, then $\frac{d y}{d x}$ is equal to

**Options:**

- **(A)** $x^{n-1}(1+n \log x)+(\log x)^{n-1}[n+\log x]$
- **(B)** $x^{n-2}(1+n \log x)+(\log x)^{n-1}[n+\log x]$
- **(C)** $x^{n-1}(1+n \log x)+(\log x)^{n-1}[n-\log x]$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x^{n-1}(1+n \log x)+(\log x)^{n-1}[n+\log x]$**

**Detailed Solution:**

Given, $y=x^{n} \log x+x(\log x)^{n}$
$$
\begin{array}{c}
\frac{d y}{d x}=n x^{n-1} \log x+x^{n} \cdot \frac{1}{x}+x n(\log x)^{n-1}\left(\frac{1}{x}\right) \\
+1 \cdot(\log x)^{n} \\
=x^{n-1}(1+n \log x)+(\log x)^{n-1}[n+\log x]
\end{array}
$$

</details>

---

### Q47. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

If $y=\log _{10} x+\log _{x} 10+\log _{x} x+\log _{10} 10$,
then $\frac{d y}{d x}$ is equal to

**Options:**

- **(A)** $\frac{1}{x \log _{e} 10}-\frac{\log _{e} 10}{x\left(\log _{e} x\right)^{2}}$
- **(B)** $\frac{1}{x \log _{e} 10}-\frac{1}{x \log _{10} e}$
- **(C)** $\frac{1}{x \log _{e} 10}+\frac{\log _{e} 10}{x\left(\log _{e} x\right)^{2}}$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{x \log _{e} 10}-\frac{\log _{e} 10}{x\left(\log _{e} x\right)^{2}}$**

**Detailed Solution:**

Given,
$$
y=\log _{10} x+\log _{x} 10+\log _{x} x+\log _{10} 10
$$
$\Rightarrow \quad y=\log _{10} e \cdot \log _{e} x+\frac{\log _{e} 10}{\log _{e} x}+1+1$
On differentiating w.r.t. $x$, we get
$\begin{aligned} \frac{d y}{d x} &=\frac{1}{x} \log _{10} e-\frac{\log _{e} 10}{x\left(\log _{e} x\right)^{2}} \\ &=\frac{1}{x \log _{e} 10}-\frac{\log _{e} 10}{x\left(\log _{e} x\right)^{2}} \end{aligned}$

</details>

---

### Q48. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

If $y=\log _{\cos x} \sin x$, then $\frac{d y}{d x}$ is equal to

**Options:**

- **(A)** $\frac{(\cot x \log \cos x+\tan x \log \sin x)}{(\log \cos x)^{2}}$
- **(B)** $\frac{(\tan x \log \cos x+\cot x \log \sin x)}{(\log \cos x)^{2}}$
- **(C)** $\frac{(\cot x \log \cos x+\tan x \log \sin x)}{(\log \sin x)^{2}}$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{(\cot x \log \cos x+\tan x \log \sin x)}{(\log \cos x)^{2}}$**

**Detailed Solution:**

Given, $y=\log _{\cos x} \sin x=\frac{\log \sin x}{\log \cos x}$
On differentiating w.r.t. $x$, we get
$$
\frac{d y}{d x}=\frac{\cot x \cdot \log \cos x+\tan x \cdot \log \sin x}{(\log \cos x)^{2}}
$$

</details>

---

### Q49. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

The derivative of $\log |x|$ is

**Options:**

- **(A)** $\frac{1}{x}, x>0$
- **(B)** $\frac{1}{|x|}, x \neq 0$
- **(C)** $\frac{1}{x}, x \neq 0$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{x}, x \neq 0$**

**Detailed Solution:**

We have, $y=\log |x|=\left\{\begin{array}{ll}\log x & , x>0 \\ \log (-x), & x < 0\end{array}\right.$
$$
\begin{array}{l}
\therefore \quad \frac{d y}{d x}=\left\{\begin{array}{ll}
\frac{1}{x}, & x>0 \\
\frac{1}{-x}(-1)=\frac{1}{x}, & x < 0
\end{array}\right. \\
\Rightarrow \quad \frac{d y}{d x}=\frac{1}{x}, x \neq 0
\end{array}
$$

</details>

---

