# MHT CET Mathematics - Definite Integration

## Topic 3: Properties of Definite Integration

**Total Questions:** 146

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\displaystyle\int_{\alpha}^{2026-\alpha} \dfrac{(2026-x)^2}{x^2 + (2026-x)^2}\,dx = 100$, then $\alpha = $

**Options:**

- **(A)** $913$
- **(B)** $1013$
- **(C)** $1113$
- **(D)** $1213$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $913$**

**Detailed Solution:**

Let $I = \int_{\alpha}^{2026-\alpha} \dfrac{(2026-x)^2}{x^2 + (2026-x)^2}\,dx$

Using the definite integral property $\int_{a}^{b} f(x)\,dx = \int_{a}^{b} f(a+b-x)\,dx$, where $a+b = \alpha + 2026 - \alpha = 2026$, we replace $x$ with $2026-x$:

$I = \int_{\alpha}^{2026-\alpha} \dfrac{x^2}{(2026-x)^2 + x^2}\,dx$

Adding the two expressions for $I$, we get:

$2I = \int_{\alpha}^{2026-\alpha} \dfrac{(2026-x)^2 + x^2}{x^2 + (2026-x)^2}\,dx$

$2I = \int_{\alpha}^{2026-\alpha} 1 \,dx$

$2I = [x]_{\alpha}^{2026-\alpha} = (2026-\alpha) - \alpha = 2026 - 2\alpha$

$I = 1013 - \alpha$

Given that $I = 100$, we have:

$1013 - \alpha = 100$

$\alpha = 913$

Answer: $913$

</details>

---

### Q2. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\displaystyle\int_0^2 |4x - 5|\,dx =$

**Options:**

- **(A)** $\dfrac{17}{4}$
- **(B)** $\dfrac{-17}{4}$
- **(C)** $\dfrac{4}{17}$
- **(D)** $\dfrac{-4}{17}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{17}{4}$**

**Detailed Solution:**

The critical point of $|4x - 5|$ is $x = \dfrac{5}{4}$.

Splitting the integral at $x = \dfrac{5}{4}$:

$\displaystyle\int_0^2 |4x - 5|\,dx = \displaystyle\int_0^{5/4} (5 - 4x)\,dx + \displaystyle\int_{5/4}^2 (4x - 5)\,dx$

Evaluating the first integral:

$\displaystyle\int_0^{5/4} (5 - 4x)\,dx = \left[ 5x - 2x^2 \right]_0^{5/4} = 5\left(\dfrac{5}{4}\right) - 2\left(\dfrac{25}{16}\right) = \dfrac{25}{4} - \dfrac{25}{8} = \dfrac{25}{8}$

Evaluating the second integral:

$\displaystyle\int_{5/4}^2 (4x - 5)\,dx = \left[ 2x^2 - 5x \right]_{5/4}^2 = (8 - 10) - \left(\dfrac{25}{8} - \dfrac{25}{4}\right) = -2 + \dfrac{25}{8} = \dfrac{9}{8}$

Adding both parts:

$\dfrac{25}{8} + \dfrac{9}{8} = \dfrac{34}{8} = \dfrac{17}{4}$

Answer: $\dfrac{17}{4}$

</details>

---

### Q3. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int_0^\pi \log(\sin x)\,dx = k$, then the value of $\int_0^{\frac{\pi}{4}} \log(1 + \tan x)\,dx$ in terms of $k$ is...

**Options:**

- **(A)** $\dfrac{k}{8}$
- **(B)** $-\dfrac{k}{2}$
- **(C)** $-\dfrac{k}{8}$
- **(D)** $\dfrac{k}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\dfrac{k}{8}$**

**Detailed Solution:**

Given $k = \int_0^\pi \log(\sin x)\,dx$

Using the property $\int_0^{2a} f(x)\,dx = 2\int_0^a f(x)\,dx$ if $f(2a-x) = f(x)$, we have:

$k = 2\int_0^{\dfrac{\pi}{2}} \log(\sin x)\,dx$

We know that standard integral $\int_0^{\dfrac{\pi}{2}} \log(\sin x)\,dx = -\dfrac{\pi}{2} \log 2$

$k = 2 \left(-\dfrac{\pi}{2} \log 2\right) = -\pi \log 2$

Now, let $I = \int_0^{\dfrac{\pi}{4}} \log(1 + \tan x)\,dx$

Using the property $\int_0^a f(x)\,dx = \int_0^a f(a-x)\,dx$, we get:

$I = \int_0^{\dfrac{\pi}{4}} \log\left(1 + \tan\left(\dfrac{\pi}{4} - x\right)\right)\,dx$

$I = \int_0^{\dfrac{\pi}{4}} \log\left(1 + \dfrac{1 - \tan x}{1 + \tan x}\right)\,dx$

$I = \int_0^{\dfrac{\pi}{4}} \log\left(\dfrac{2}{1 + \tan x}\right)\,dx$

$I = \int_0^{\dfrac{\pi}{4}} (\log 2 - \log(1 + \tan x))\,dx$

$I = \log 2 \int_0^{\dfrac{\pi}{4}} dx - \int_0^{\dfrac{\pi}{4}} \log(1 + \tan x)\,dx$

$I = \dfrac{\pi}{4} \log 2 - I$

$2I = \dfrac{\pi}{4} \log 2 \Rightarrow I = \dfrac{\pi}{8} \log 2$

Since $k = -\pi \log 2$, we have $\pi \log 2 = -k$

Substituting this in $I$, we get:

$I = \dfrac{-k}{8} = -\dfrac{k}{8}$

Answer: $-\dfrac{k}{8}$

</details>

---

### Q4. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^{\frac{\pi}{2}} (1 + \sin x)^3\,dx = $

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $\dfrac{\pi}{2} - \dfrac{2}{3}$
- **(D)** $\dfrac{5\pi}{4} + \dfrac{11}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{5\pi}{4} + \dfrac{11}{3}$**

**Detailed Solution:**

Expanding the integrand using $(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$:

$\int_0^{\dfrac{\pi}{2}} (1 + \sin x)^3\,dx = \int_0^{\dfrac{\pi}{2}} (1 + 3\sin x + 3\sin^2 x + \sin^3 x)\,dx$

Using standard definite integrals:

$\int_0^{\dfrac{\pi}{2}} 1\,dx = \dfrac{\pi}{2}$

$\int_0^{\dfrac{\pi}{2}} \sin x\,dx = 1$

$\int_0^{\dfrac{\pi}{2}} \sin^2 x\,dx = \dfrac{\pi}{4}$

$\int_0^{\dfrac{\pi}{2}} \sin^3 x\,dx = \dfrac{2}{3}$

Substituting these values into the expanded integral:

$I = \dfrac{\pi}{2} + 3(1) + 3\left(\dfrac{\pi}{4}\right) + \dfrac{2}{3}$

$I = \left(\dfrac{\pi}{2} + \dfrac{3\pi}{4}\right) + \left(3 + \dfrac{2}{3}\right)$

$I = \dfrac{5\pi}{4} + \dfrac{11}{3}$

Answer: $\dfrac{5\pi}{4} + \dfrac{11}{3}$

</details>

---

### Q5. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $f(x)$ be odd and continuous on $[-a, a]$. Then the value of $\int_{-a}^{a} x f(x^2) dx$ is:

**Options:**

- **(A)** $0$
- **(B)** $f(a)$
- **(C)** $2f(a)$
- **(D)** $2a$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0$**

**Detailed Solution:**

Let $I = \int_{-a}^{a} x f(x^2) dx$

Let the integrand be $g(x) = x f(x^2)$

Replacing $x$ with $-x$, we get:

$g(-x) = (-x) f((-x)^2) = -x f(x^2) = -g(x)$

Since $g(-x) = -g(x)$, the function $g(x)$ is an odd function.

Using the property of definite integrals, $\int_{-a}^{a} g(x) dx = 0$ for any odd function $g(x)$.

Therefore, $\int_{-a}^{a} x f(x^2) dx = 0$

Answer: $0$

</details>

---

### Q6. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_0^{\pi/2} \dfrac{\cos 3x + 1}{2\cos x - 1} dx$ is

**Options:**

- **(A)** $2$
- **(B)** $1$
- **(C)** $\dfrac{1}{2}$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1$**

**Detailed Solution:**

Using the multiple angle identity $\cos 3x = 4\cos^3 x - 3\cos x$, the numerator becomes:

$\cos 3x + 1 = 4\cos^3 x - 3\cos x + 1$

Factoring the polynomial in terms of $\cos x$:

$4\cos^3 x - 3\cos x + 1 = (\cos x + 1)(4\cos^2 x - 4\cos x + 1) = (\cos x + 1)(2\cos x - 1)^2$

Substituting this back into the integral:

$I = \int_0^{\pi/2} \dfrac{(\cos x + 1)(2\cos x - 1)^2}{2\cos x - 1} dx$

Canceling the common factor $(2\cos x - 1)$:

$I = \int_0^{\pi/2} (\cos x + 1)(2\cos x - 1) dx$

Expanding the integrand:

$(\cos x + 1)(2\cos x - 1) = 2\cos^2 x + \cos x - 1$

Using the double angle identity $2\cos^2 x - 1 = \cos 2x$, we get:

$I = \int_0^{\pi/2} (\cos 2x + \cos x) dx$

Integrating with respect to $x$:

$I = \left[ \dfrac{\sin 2x}{2} + \sin x \right]_0^{\pi/2}$

Evaluating the limits:

$I = \left( \dfrac{\sin \pi}{2} + \sin \dfrac{\pi}{2} \right) - \left( \dfrac{\sin 0}{2} + \sin 0 \right)$

$I = (0 + 1) - (0 + 0) = 1$

Answer: $1$

</details>

---

### Q7. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\displaystyle\int_{\pi/5}^{3\pi/10} \dfrac{1}{1 + \sqrt{\tan x}}\,dx = \cdots$

**Options:**

- **(A)** $\dfrac{\pi}{10}$
- **(B)** $\dfrac{\pi}{15}$
- **(C)** $\dfrac{\pi}{20}$
- **(D)** $\dfrac{\pi}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{\pi}{20}$**

**Detailed Solution:**

Let $I = \displaystyle\int_{\pi/5}^{3\pi/10} \dfrac{1}{1 + \sqrt{\tan x}}\,dx$

Using the property $\displaystyle\int_{a}^{b} f(x)\,dx = \displaystyle\int_{a}^{b} f(a+b-x)\,dx$, we substitute $x$ with $\dfrac{\pi}{5} + \dfrac{3\pi}{10} - x = \dfrac{\pi}{2} - x$.

$I = \displaystyle\int_{\pi/5}^{3\pi/10} \dfrac{1}{1 + \sqrt{\tan(\pi/2 - x)}}\,dx$

$I = \displaystyle\int_{\pi/5}^{3\pi/10} \dfrac{1}{1 + \sqrt{\cot x}}\,dx$

$I = \displaystyle\int_{\pi/5}^{3\pi/10} \dfrac{\sqrt{\tan x}}{\sqrt{\tan x} + 1}\,dx$

Adding the two equations for $I$:

$2I = \displaystyle\int_{\pi/5}^{3\pi/10} \left( \dfrac{1}{1 + \sqrt{\tan x}} + \dfrac{\sqrt{\tan x}}{1 + \sqrt{\tan x}} \right)\,dx$

$2I = \displaystyle\int_{\pi/5}^{3\pi/10} 1 \,dx$

$2I = [x]_{\pi/5}^{3\pi/10} = \dfrac{3\pi}{10} - \dfrac{\pi}{5} = \dfrac{\pi}{10}$

$I = \dfrac{\pi}{20}$

Answer: $\dfrac{\pi}{20}$

</details>

---

### Q8. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int_{1/2}^{2} \dfrac{1}{x}\,\text{sin}^{101}\left(x - \dfrac{1}{x}\right) dx$ is equal to:

**Options:**

- **(A)** $\dfrac{1}{4}$
- **(B)** $1$
- **(C)** $0$
- **(D)** $\dfrac{101}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0$**

**Detailed Solution:**

Let $I = \int_{1/2}^{2} \dfrac{1}{x} \sin^{101} \left(x - \dfrac{1}{x}\right) dx$

Substitute $x = \dfrac{1}{t}$, which gives $dx = -\dfrac{1}{t^2} dt$.

The limits change from $x = \dfrac{1}{2}$ to $t = 2$, and $x = 2$ to $t = \dfrac{1}{2}$.

$I = \int_{2}^{1/2} t \sin^{101} \left(\dfrac{1}{t} - t\right) \left(-\dfrac{1}{t^2}\right) dt$

$I = \int_{2}^{1/2} -\dfrac{1}{t} \sin^{101} \left(\dfrac{1}{t} - t\right) dt$

Reversing the limits changes the sign of the integral:

$I = \int_{1/2}^{2} \dfrac{1}{t} \sin^{101} \left(\dfrac{1}{t} - t\right) dt$

Using the property of odd functions, $\sin(-\theta) = -\sin\theta$, we get $\sin^{101} \left(\dfrac{1}{t} - t\right) = -\sin^{101} \left(t - \dfrac{1}{t}\right)$.

$I = -\int_{1/2}^{2} \dfrac{1}{t} \sin^{101} \left(t - \dfrac{1}{t}\right) dt$

Replacing the dummy variable $t$ with $x$:

$I = -\int_{1/2}^{2} \dfrac{1}{x} \sin^{101} \left(x - \dfrac{1}{x}\right) dx$

$I = -I$

$2I = 0$

$I = 0$

</details>

---

### Q9. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\int_{-1}^{4} f(x)dx = 9$ and $\int_{2}^{4}(7 - f(x))dx = 10$, then $\int_{2}^{-1} f(x)dx = $

**Options:**

- **(A)** $13$
- **(B)** $19$
- **(C)** $-19$
- **(D)** $-5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-5$**

**Detailed Solution:**

Given $\int_{-1}^{4} f(x)dx = 9$ and $\int_{2}^{4}(7 - f(x))dx = 10$

Expanding the second integral:

$\int_{2}^{4} 7 dx - \int_{2}^{4} f(x)dx = 10$

$7(4 - 2) - \int_{2}^{4} f(x)dx = 10$

$14 - \int_{2}^{4} f(x)dx = 10$

$\int_{2}^{4} f(x)dx = 4$

Using the property of definite integrals:

$\int_{-1}^{4} f(x)dx = \int_{-1}^{2} f(x)dx + \int_{2}^{4} f(x)dx$

$9 = \int_{-1}^{2} f(x)dx + 4$

$\int_{-1}^{2} f(x)dx = 5$

$\int_{2}^{-1} f(x)dx = -\int_{-1}^{2} f(x)dx = -5$

Answer: $-5$

</details>

---

### Q10. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{\pi/6}^{\pi/3} \sin 2x \log(\tan x)\ dx = \ldots$

**Options:**

- **(A)** $0$
- **(B)** $\dfrac{\sqrt{3}}{2} - 1$
- **(C)** $\dfrac{\sqrt{3}}{2} + \dfrac{1}{2}$
- **(D)** $\left(\dfrac{\sqrt{3} - 1}{2}\right) - \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0$**

**Detailed Solution:**

Let $I = \int_{\pi/6}^{\pi/3} \sin 2x \log(\tan x)\ dx$

Using the definite integral property $\int_{a}^{b} f(x)\ dx = \int_{a}^{b} f(a+b-x)\ dx$, we substitute $x$ with $\dfrac{\pi}{6} + \dfrac{\pi}{3} - x = \dfrac{\pi}{2} - x$.

$I = \int_{\pi/6}^{\pi/3} \sin\left(2\left(\dfrac{\pi}{2} - x\right)\right) \log\left(\tan\left(\dfrac{\pi}{2} - x\right)\right)\ dx$

$I = \int_{\pi/6}^{\pi/3} \sin(\pi - 2x) \log(\cot x)\ dx$

$I = \int_{\pi/6}^{\pi/3} \sin 2x \log\left(\dfrac{1}{\tan x}\right)\ dx$

$I = -\int_{\pi/6}^{\pi/3} \sin 2x \log(\tan x)\ dx$

$I = -I$

$2I = 0$

$I = 0$

Answer: $0$

</details>

---

### Q11. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\displaystyle\int_0^1 \dfrac{\sin^{-1}\sqrt{x(2-x)}}{\cos^{-1} x + \sin^{-1}\sqrt{x(2-x)}}\, dx = \ldots$

**Options:**

- **(A)** $1$
- **(B)** $\dfrac{1}{2}$
- **(C)** $\dfrac{2}{3}$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{2}$**

**Detailed Solution:**

Let $I = \displaystyle\int_0^1 \dfrac{\sin^{-1}\sqrt{x(2-x)}}{\cos^{-1} x + \sin^{-1}\sqrt{x(2-x)}}\, dx$

Consider the term $\sin^{-1}\sqrt{x(2-x)}$.

Let $1-x = \cos\theta$. Since $x \in [0, 1]$, $1-x \in [0, 1]$, which implies $\theta \in \left[0, \dfrac{\pi}{2}\right]$.

We have $x(2-x) = 1 - (1-x)^2 = 1 - \cos^2\theta = \sin^2\theta$.

Since $\theta \in \left[0, \dfrac{\pi}{2}\right]$, $\sqrt{x(2-x)} = \sin\theta$.

Therefore, $\sin^{-1}\sqrt{x(2-x)} = \sin^{-1}(\sin\theta) = \theta = \cos^{-1}(1-x)$.

Substitute this back into the integral:

$I = \displaystyle\int_0^1 \dfrac{\cos^{-1}(1-x)}{\cos^{-1} x + \cos^{-1}(1-x)}\, dx$

Using the property of definite integrals $\displaystyle\int_0^a f(x)\, dx = \int_0^a f(a-x)\, dx$, we replace $x$ with $1-x$:

$I = \displaystyle\int_0^1 \dfrac{\cos^{-1} x}{\cos^{-1}(1-x) + \cos^{-1} x}\, dx$

Adding the two equations for $I$:

$2I = \displaystyle\int_0^1 \dfrac{\cos^{-1}(1-x) + \cos^{-1} x}{\cos^{-1} x + \cos^{-1}(1-x)}\, dx$

$2I = \displaystyle\int_0^1 1\, dx = 1$

$I = \dfrac{1}{2}$

Answer: $\dfrac{1}{2}$

</details>

---

### Q12. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\displaystyle\int_0^{\pi/4} \log(1 + \tan x)\, dx = \ldots$

**Options:**

- **(A)** $\dfrac{\pi}{4}\log(2)$
- **(B)** $\dfrac{\pi}{2}\log(2)$
- **(C)** $\dfrac{\pi}{8}\log(2)$
- **(D)** $\log(2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{\pi}{8}\log(2)$**

**Detailed Solution:**

Let $I = \int_0^{\pi/4} \log(1 + \tan x) \, dx$

Using the property $\int_0^a f(x) \, dx = \int_0^a f(a-x) \, dx$, we get:

$I = \int_0^{\pi/4} \log\left(1 + \tan\left(\dfrac{\pi}{4} - x\right)\right) \, dx$

Using the formula $\tan(A - B) = \dfrac{\tan A - \tan B}{1 + \tan A \tan B}$:

$I = \int_0^{\pi/4} \log\left(1 + \dfrac{1 - \tan x}{1 + \tan x}\right) \, dx$

$I = \int_0^{\pi/4} \log\left(\dfrac{1 + \tan x + 1 - \tan x}{1 + \tan x}\right) \, dx$

$I = \int_0^{\pi/4} \log\left(\dfrac{2}{1 + \tan x}\right) \, dx$

$I = \int_0^{\pi/4} (\log 2 - \log(1 + \tan x)) \, dx$

$I = \int_0^{\pi/4} \log 2 \, dx - \int_0^{\pi/4} \log(1 + \tan x) \, dx$

$I = \dfrac{\pi}{4} \log 2 - I$

$2I = \dfrac{\pi}{4} \log 2$

$I = \dfrac{\pi}{8} \log 2$

Answer: $\dfrac{\pi}{8}\log(2)$

</details>

---

### Q13. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of the integral $\displaystyle\int_0^{\pi/4} \dfrac{\cos x}{\sqrt{1 - \sin^2 x}}\, dx$ is

**Options:**

- **(A)** $\dfrac{\pi}{4}$
- **(B)** $\dfrac{\pi}{6}$
- **(C)** $\dfrac{\pi}{2}$
- **(D)** $\dfrac{\pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\pi}{4}$**

**Detailed Solution:**

Let $I = \displaystyle\int_0^{\pi/4} \dfrac{\cos x}{\sqrt{1 - \sin^2 x}}\, dx$

Using the trigonometric identity $1 - \sin^2 x = \cos^2 x$, we get:

$I = \displaystyle\int_0^{\pi/4} \dfrac{\cos x}{\sqrt{\cos^2 x}}\, dx$

Since $x \in \left[0, \dfrac{\pi}{4}\right]$, $\cos x > 0$, which implies $\sqrt{\cos^2 x} = \cos x$.

$I = \displaystyle\int_0^{\pi/4} \dfrac{\cos x}{\cos x}\, dx$

$I = \displaystyle\int_0^{\pi/4} 1 \, dx$

$I = [x]_0^{\pi/4} = \dfrac{\pi}{4}$

Answer: $\dfrac{\pi}{4}$

</details>

---

### Q14. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $a > 4$ and $\displaystyle\int_{-2}^{1} \dfrac{1}{x^2 + 4x + a}\,dx = \dfrac{1}{3}\tan^{-1}(1)$, then the value of $a$ is

**Options:**

- **(A)** $a = 9$
- **(B)** $a = 3$
- **(C)** $a = 13$
- **(D)** $a = 12$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $a = 13$**

**Detailed Solution:**

The given integral can be written as:

$\displaystyle\int_{-2}^{1} \dfrac{1}{(x+2)^2 + a - 4}\,dx = \dfrac{1}{3}\tan^{-1}(1)$

Since $a > 4$, let $a - 4 = k^2$ where $k > 0$. The integral becomes:

$\displaystyle\int_{-2}^{1} \dfrac{1}{(x+2)^2 + k^2}\,dx = \left[ \dfrac{1}{k}\tan^{-1}\left(\dfrac{x+2}{k}\right) \right]_{-2}^{1}$

$= \dfrac{1}{k}\tan^{-1}\left(\dfrac{3}{k}\right) - \dfrac{1}{k}\tan^{-1}(0) = \dfrac{1}{k}\tan^{-1}\left(\dfrac{3}{k}\right)$

Equating this to the given value:

$\dfrac{1}{k}\tan^{-1}\left(\dfrac{3}{k}\right) = \dfrac{1}{3}\tan^{-1}(1)$

By comparing both sides, we get $k = 3$.

Substituting $k = 3$ into $a - 4 = k^2$:

$a - 4 = 3^2$

$a = 9 + 4 = 13$

Answer: $a = 13$

</details>

---

### Q15. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int_0^1 \tan^{-1}\left[\dfrac{1}{1-x+x^2}\right] dx = 2k$, then the value of $k$ is:

**Options:**

- **(A)** $2\int_0^1 \tan^{-1} x \, dx$
- **(B)** $\int_0^1 \cot^{-1} x \, dx$
- **(C)** $0$
- **(D)** $\int_0^1 \tan^{-1} x \, dx$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\int_0^1 \tan^{-1} x \, dx$**

**Detailed Solution:**

Let $I = \int_0^1 \tan^{-1}\left[\dfrac{1}{1-x+x^2}\right] dx$

We can rewrite the argument of the inverse tangent function as:

$I = \int_0^1 \tan^{-1}\left[\dfrac{x - (x-1)}{1 + x(x-1)}\right] dx$

Using the formula $\tan^{-1}\left(\dfrac{A-B}{1+AB}\right) = \tan^{-1} A - \tan^{-1} B$, we get:

$I = \int_0^1 \left( \tan^{-1} x - \tan^{-1}(x-1) \right) dx$

$I = \int_0^1 \tan^{-1} x \, dx - \int_0^1 \tan^{-1}(x-1) \, dx$

Applying the definite integral property $\int_0^a f(x) dx = \int_0^a f(a-x) dx$ to the second integral:

$\int_0^1 \tan^{-1}(x-1) \, dx = \int_0^1 \tan^{-1}((1-x)-1) \, dx = \int_0^1 \tan^{-1}(-x) \, dx$

Since $\tan^{-1}(-x) = -\tan^{-1} x$, we have:

$\int_0^1 \tan^{-1}(x-1) \, dx = -\int_0^1 \tan^{-1} x \, dx$

Substituting this back into the expression for $I$:

$I = \int_0^1 \tan^{-1} x \, dx - \left( -\int_0^1 \tan^{-1} x \, dx \right)$

$I = 2\int_0^1 \tan^{-1} x \, dx$

We are given that $I = 2k$. Therefore:

$2k = 2\int_0^1 \tan^{-1} x \, dx$

$k = \int_0^1 \tan^{-1} x \, dx$

Answer: $\int_0^1 \tan^{-1} x \, dx$

</details>

---

### Q16. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int_0^\infty \dfrac{1}{(x^2 + 1)(x^2 + 16)} dx = \dfrac{\pi}{k^2 - 9}$, then $k = \ldots$

**Options:**

- **(A)** $\pm 2$
- **(B)** $\pm 5$
- **(C)** $\pm 4$
- **(D)** $\pm 7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\pm 7$**

**Detailed Solution:**

Let $I = \int_0^\infty \dfrac{1}{(x^2 + 1)(x^2 + 16)} dx$

Using partial fractions, we can write the integrand as:

$\dfrac{1}{(x^2 + 1)(x^2 + 16)} = \dfrac{1}{15} \left( \dfrac{1}{x^2 + 1} - \dfrac{1}{x^2 + 16} \right)$

Substituting this back into the integral:

$I = \dfrac{1}{15} \left( \int_0^\infty \dfrac{1}{x^2 + 1} dx - \int_0^\infty \dfrac{1}{x^2 + 16} dx \right)$

$I = \dfrac{1}{15} \left[ \tan^{-1} x - \dfrac{1}{4} \tan^{-1} \left( \dfrac{x}{4} \right) \right]_0^\infty$

Evaluating the limits:

$I = \dfrac{1}{15} \left( \dfrac{\pi}{2} - \dfrac{1}{4} \times \dfrac{\pi}{2} \right)$

$I = \dfrac{1}{15} \left( \dfrac{3\pi}{8} \right) = \dfrac{\pi}{40}$

We are given that $I = \dfrac{\pi}{k^2 - 9}$. Equating the two expressions:

$\dfrac{\pi}{40} = \dfrac{\pi}{k^2 - 9}$

$k^2 - 9 = 40$

$k^2 = 49$

$k = \pm 7$

Answer: $\pm 7$

</details>

---

### Q17. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int_{-1}^{4} f(x)dx = 4$ and $\int_{2}^{4}(5 - f(x))dx = 7$ then $\int_{2}^{-1} f(x) dx = $

**Options:**

- **(A)** $0$
- **(B)** $-5$
- **(C)** $-1$
- **(D)** $-4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-1$**

**Detailed Solution:**

Given $\int_{2}^{4}(5 - f(x))dx = 7$

$\int_{2}^{4} 5 dx - \int_{2}^{4} f(x) dx = 7$

$5(4 - 2) - \int_{2}^{4} f(x) dx = 7$

$10 - \int_{2}^{4} f(x) dx = 7$

$\int_{2}^{4} f(x) dx = 3$

Using the property of definite integrals, $\int_{-1}^{4} f(x) dx = \int_{-1}^{2} f(x) dx + \int_{2}^{4} f(x) dx$

$4 = \int_{-1}^{2} f(x) dx + 3$

$\int_{-1}^{2} f(x) dx = 1$

Therefore, $\int_{2}^{-1} f(x) dx = -\int_{-1}^{2} f(x) dx = -1$

Answer: $-1$

</details>

---

### Q18. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $I_n = \int_n^{n+1} x [x] dx$, where $[x]$ denotes greatest integer function and $n \in N$. If $I_n = 18$, then the value of $n$ is...

**Options:**

- **(A)** $3$
- **(B)** $4$
- **(C)** $5$
- **(D)** $6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4$**

**Detailed Solution:**

Given $I_n = \int_n^{n+1} x [x] dx$

For $x \in [n, n+1)$, the greatest integer function $[x] = n$.

$I_n = \int_n^{n+1} n x dx$

$I_n = n \left[ \dfrac{x^2}{2} \right]_n^{n+1}$

$I_n = \dfrac{n}{2} \left( (n+1)^2 - n^2 \right)$

$I_n = \dfrac{n(2n+1)}{2}$

Given $I_n = 18$, we have:

$\dfrac{n(2n+1)}{2} = 18$

$2n^2 + n - 36 = 0$

$(n - 4)(2n + 9) = 0$

Since $n \in N$, $n = 4$.

Answer: $4$

</details>

---

### Q19. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The values of $a$ for which $\int_0^a (3x^2 + 4x - 5) dx < a^3 - 2$ are...

**Options:**

- **(A)** $\dfrac{1}{2} < a < 2$
- **(B)** $\dfrac{1}{2} \leq a \leq 2$
- **(C)** $a \leq \dfrac{1}{2}$
- **(D)** $a \geq 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{2} < a < 2$**

**Detailed Solution:**

Evaluating the integral on the left side:

$\int_0^a (3x^2 + 4x - 5) dx = \left[ x^3 + 2x^2 - 5x \right]_0^a = a^3 + 2a^2 - 5a$

Substituting this into the given inequality:

$a^3 + 2a^2 - 5a < a^3 - 2$

$2a^2 - 5a + 2 < 0$

Factorizing the quadratic expression:

$2a^2 - 4a - a + 2 < 0$

$2a(a - 2) - 1(a - 2) < 0$

$(2a - 1)(a - 2) < 0$

The roots are $a = \dfrac{1}{2}$ and $a = 2$. The solution to the inequality is:

$\dfrac{1}{2} < a < 2$

Answer: $\dfrac{1}{2} < a < 2$

</details>

---

### Q20. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int_{10}^{20} \dfrac{1}{(x - 3)(x - 2)} dx$ is...

**Options:**

- **(A)** $\log\left(\dfrac{34}{21}\right)$
- **(B)** $\log\left(\dfrac{17}{7}\right)$
- **(C)** $\log\left(\dfrac{17}{18}\right)$
- **(D)** $\log\left(\dfrac{68}{63}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log\left(\dfrac{68}{63}\right)$**

**Detailed Solution:**

Using partial fractions, the integrand can be written as:

$\dfrac{1}{(x - 3)(x - 2)} = \dfrac{1}{x - 3} - \dfrac{1}{x - 2}$

Integrating with respect to $x$:

$\int_{10}^{20} \left( \dfrac{1}{x - 3} - \dfrac{1}{x - 2} \right) dx = \left[ \log|x - 3| - \log|x - 2| \right]_{10}^{20}$

$= \left[ \log\left(\dfrac{x - 3}{x - 2}\right) \right]_{10}^{20}$

Substituting the upper and lower limits:

$= \log\left(\dfrac{17}{18}\right) - \log\left(\dfrac{7}{8}\right)$

$= \log\left(\dfrac{17}{18} \times \dfrac{8}{7}\right)$

$= \log\left(\dfrac{17 \times 4}{9 \times 7}\right)$

$= \log\left(\dfrac{68}{63}\right)$

Answer: $\log\left(\dfrac{68}{63}\right)$

</details>

---

### Q21. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int_{-1}^{1} \dfrac{1}{(1 + e^x)(1 + x^2)} dx$ is....

**Options:**

- **(A)** $\dfrac{\pi}{4}$
- **(B)** $\dfrac{\pi}{2}$
- **(C)** $\pi$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\pi}{4}$**

**Detailed Solution:**

Let $I = \int_{-1}^{1} \dfrac{1}{(1 + e^x)(1 + x^2)} dx$

Using the property $\int_{a}^{b} f(x) dx = \int_{a}^{b} f(a+b-x) dx$, we replace $x$ with $-x$:

$I = \int_{-1}^{1} \dfrac{1}{(1 + e^{-x})(1 + (-x)^2)} dx$

$I = \int_{-1}^{1} \dfrac{e^x}{(e^x + 1)(1 + x^2)} dx$

Adding the two equations for $I$:

$2I = \int_{-1}^{1} \left( \dfrac{1}{(1 + e^x)(1 + x^2)} + \dfrac{e^x}{(1 + e^x)(1 + x^2)} \right) dx$

$2I = \int_{-1}^{1} \dfrac{1 + e^x}{(1 + e^x)(1 + x^2)} dx$

$2I = \int_{-1}^{1} \dfrac{1}{1 + x^2} dx$

$2I = [\tan^{-1} x]_{-1}^{1}$

$2I = \tan^{-1}(1) - \tan^{-1}(-1)$

$2I = \dfrac{\pi}{4} - \left(-\dfrac{\pi}{4}\right) = \dfrac{\pi}{2}$

$I = \dfrac{\pi}{4}$

Answer: $\dfrac{\pi}{4}$

</details>

---

### Q22. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \begin{cases} \dfrac{[x] \cdot |x|}{x}, & x \neq 0 \\ 0, & x = 0 \end{cases}$, where $[x]$ and $|x|$ denote the greatest integer function and the modulus function respectively, then $\int_{-2}^{1} f(x) \, dx = ...$

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $3$
- **(D)** $7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3$**

**Detailed Solution:**

The given function is $f(x) = \dfrac{[x] \cdot |x|}{x}$ for $x \neq 0$.

For $x < 0$, $\dfrac{|x|}{x} = -1$, so $f(x) = -[x]$.

For $x > 0$, $\dfrac{|x|}{x} = 1$, so $f(x) = [x]$.

The integral can be split into intervals:

$\int_{-2}^{1} f(x) \, dx = \int_{-2}^{-1} f(x) \, dx + \int_{-1}^{0} f(x) \, dx + \int_{0}^{1} f(x) \, dx$

In $(-2, -1)$, $[x] = -2$ and $x < 0$, so $f(x) = -(-2) = 2$.

In $(-1, 0)$, $[x] = -1$ and $x < 0$, so $f(x) = -(-1) = 1$.

In $(0, 1)$, $[x] = 0$ and $x > 0$, so $f(x) = 0$.

Substituting these values into the integral:

$\int_{-2}^{1} f(x) \, dx = \int_{-2}^{-1} 2 \, dx + \int_{-1}^{0} 1 \, dx + \int_{0}^{1} 0 \, dx$

$\int_{-2}^{1} f(x) \, dx = 2(-1 - (-2)) + 1(0 - (-1)) + 0$

$\int_{-2}^{1} f(x) \, dx = 2(1) + 1(1) = 3$

Answer: $3$

</details>

---

### Q23. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int\limits_{1/e}^{e}\dfrac{|\log x|}{x^2}dx$ is

**Options:**

- **(A)** $\dfrac{e^2 - 1}{2e}$
- **(B)** $\dfrac{2}{e}$
- **(C)** $2 - \dfrac{2}{e}$
- **(D)** $1 - \dfrac{1}{e}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 - \dfrac{2}{e}$**

**Detailed Solution:**

Let $I = \int\limits_{1/e}^{e}\dfrac{|\log x|}{x^2}dx$

Substitute $x = e^t \Rightarrow dx = e^t dt$

When $x = 1/e$, $t = -1$ and when $x = e$, $t = 1$

$I = \int\limits_{-1}^{1} \dfrac{|t|}{e^{2t}} e^t dt = \int\limits_{-1}^{1} |t| e^{-t} dt$

Splitting the integral at $t = 0$:

$I = \int\limits_{-1}^{0} -t e^{-t} dt + \int\limits_{0}^{1} t e^{-t} dt$

Using integration by parts:

$\int -t e^{-t} dt = t e^{-t} + e^{-t}$

$\int t e^{-t} dt = -t e^{-t} - e^{-t}$

Evaluating the definite integrals:

$I = \left[ t e^{-t} + e^{-t} \right]_{-1}^{0} + \left[ -t e^{-t} - e^{-t} \right]_{0}^{1}$

$I = \left( (0 + e^0) - (-e^1 + e^1) \right) + \left( (-e^{-1} - e^{-1}) - (0 - e^0) \right)$

$I = (1 - 0) + \left( -\dfrac{2}{e} - (-1) \right)$

$I = 1 + 1 - \dfrac{2}{e} = 2 - \dfrac{2}{e}$

Answer: $2 - \dfrac{2}{e}$

</details>

---

### Q24. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\int\limits_{-\pi/2}^{\pi/2}(\sin^2 x + \sin^3 x)dx = k$, then the value of $k$

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $\pi$
- **(D)** $\dfrac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{\pi}{2}$**

**Detailed Solution:**

Let $I = \int_{-\pi/2}^{\pi/2} (\sin^2 x + \sin^3 x) dx$

$I = \int_{-\pi/2}^{\pi/2} \sin^2 x dx + \int_{-\pi/2}^{\pi/2} \sin^3 x dx$

Since $\sin^3 x$ is an odd function, $\int_{-\pi/2}^{\pi/2} \sin^3 x dx = 0$

Since $\sin^2 x$ is an even function, $\int_{-\pi/2}^{\pi/2} \sin^2 x dx = 2 \int_{0}^{\pi/2} \sin^2 x dx$

$I = 2 \int_{0}^{\pi/2} \sin^2 x dx = 2 \left( \dfrac{\pi}{4} \right) = \dfrac{\pi}{2}$

Therefore, $k = \dfrac{\pi}{2}$

Answer: $\dfrac{\pi}{2}$

</details>

---

### Q25. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $[x]$ denotes the greatest integer less than or equal to $x$, then the value of the integral $\int_0^2 x^2[x]\, dx$ is equal to

**Options:**

- **(A)** $\dfrac{8}{3}$
- **(B)** $\dfrac{3}{8}$
- **(C)** $\dfrac{7}{3}$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{7}{3}$**

**Detailed Solution:**

The given integral is $I = \int_0^2 x^2[x]\, dx$.

Using the property of the greatest integer function, we split the integral at integer points within the limits of integration:

$I = \int_0^1 x^2[x]\, dx + \int_1^2 x^2[x]\, dx$

For $x \in [0, 1)$, $[x] = 0$.

For $x \in [1, 2)$, $[x] = 1$.

Substituting these values into the integrals:

$I = \int_0^1 x^2(0)\, dx + \int_1^2 x^2(1)\, dx$

$I = 0 + \left[ \dfrac{x^3}{3} \right]_1^2$

$I = \dfrac{2^3}{3} - \dfrac{1^3}{3}$

$I = \dfrac{8}{3} - \dfrac{1}{3} = \dfrac{7}{3}$

Answer: $\dfrac{7}{3}$

</details>

---

### Q26. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\int_0^1 \dfrac{dx}{\sqrt{x + 1} - \sqrt{x}} = \sqrt{2}k$, then the value of $k$ is...

**Options:**

- **(A)** $\dfrac{4}{\sqrt{3}}$
- **(B)** $\dfrac{4}{3}$
- **(C)** $\dfrac{2}{\sqrt{3}}$
- **(D)** $\dfrac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{4}{3}$**

**Detailed Solution:**

Rationalizing the denominator of the integrand:

$\int_0^1 \dfrac{dx}{\sqrt{x + 1} - \sqrt{x}} = \int_0^1 \dfrac{\sqrt{x + 1} + \sqrt{x}}{(\sqrt{x + 1})^2 - (\sqrt{x})^2} dx$

$= \int_0^1 (\sqrt{x + 1} + \sqrt{x}) dx$

Integrating with respect to $x$:

$= \left[ \dfrac{2}{3}(x + 1)^{3/2} + \dfrac{2}{3}x^{3/2} \right]_0^1$

Applying the limits:

$= \left( \dfrac{2}{3}(2)^{3/2} + \dfrac{2}{3}(1)^{3/2} \right) - \left( \dfrac{2}{3}(1)^{3/2} + 0 \right)$

$= \dfrac{4\sqrt{2}}{3} + \dfrac{2}{3} - \dfrac{2}{3}$

$= \dfrac{4\sqrt{2}}{3}$

Equating to the given value $\sqrt{2}k$:

$\sqrt{2}k = \dfrac{4\sqrt{2}}{3}$

$k = \dfrac{4}{3}$

Answer: $\dfrac{4}{3}$

</details>

---

### Q27. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = |5x - 3|$ is defined on interval $[0, 1]$, then the value of $\int_0^1 f(x)\,dx$ is...

**Options:**

- **(A)** $\dfrac{13}{10}$
- **(B)** $\dfrac{9}{10}$
- **(C)** $\dfrac{3}{10}$
- **(D)** $\dfrac{17}{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{13}{10}$**

**Detailed Solution:**

Let $I = \int_0^1 |5x - 3| \, dx$

The expression $5x - 3$ changes sign at $x = \dfrac{3}{5}$. Splitting the integral at this point:

$I = \int_0^{3/5} (3 - 5x) \, dx + \int_{3/5}^1 (5x - 3) \, dx$

$I = \left[ 3x - \dfrac{5x^2}{2} \right]_0^{3/5} + \left[ \dfrac{5x^2}{2} - 3x \right]_{3/5}^1$

$I = \left( 3\left(\dfrac{3}{5}\right) - \dfrac{5}{2}\left(\dfrac{9}{25}\right) \right) + \left( \left(\dfrac{5}{2} - 3\right) - \left(\dfrac{5}{2}\left(\dfrac{9}{25}\right) - 3\left(\dfrac{3}{5}\right)\right) \right)$

$I = \left( \dfrac{9}{5} - \dfrac{9}{10} \right) + \left( -\dfrac{1}{2} - \left(\dfrac{9}{10} - \dfrac{9}{5}\right) \right)$

$I = \dfrac{9}{10} + \left( -\dfrac{1}{2} + \dfrac{9}{10} \right)$

$I = \dfrac{9}{10} + \dfrac{4}{10} = \dfrac{13}{10}$

Answer: $\dfrac{13}{10}$

</details>

---

### Q28. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $[x]$ is the greatest integer function not greater than $x$, then the value of $\displaystyle\int_0^2 x[x^2]\,dx$ is...

**Options:**

- **(A)** $\dfrac{3}{2}$
- **(B)** $\dfrac{5}{2}$
- **(C)** $3$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3$**

**Detailed Solution:**

Let $I = \displaystyle\int_0^2 x[x^2]\,dx$

Substitute $x^2 = t \Rightarrow 2x\,dx = dt \Rightarrow x\,dx = \dfrac{dt}{2}$

When $x = 0$, $t = 0$ and when $x = 2$, $t = 4$

$I = \dfrac{1}{2} \displaystyle\int_0^4 [t]\,dt$

$I = \dfrac{1}{2} \left( \displaystyle\int_0^1 0\,dt + \displaystyle\int_1^2 1\,dt + \displaystyle\int_2^3 2\,dt + \displaystyle\int_3^4 3\,dt \right)$

$I = \dfrac{1}{2} (0 + 1(2-1) + 2(3-2) + 3(4-3))$

$I = \dfrac{1}{2} (1 + 2 + 3) = \dfrac{6}{2} = 3$

Answer: $3$

</details>

---

### Q29. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\displaystyle\int_2^4 (\{x\} + [x])\,dx =$...(where $\{x\}$ and $[x]$ are the fractional part function and the greatest integer function, respectively)

**Options:**

- **(A)** $2$
- **(B)** $4$
- **(C)** $6$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $6$**

**Detailed Solution:**

By the definition of the fractional part and greatest integer functions, $x = [x] + \{x\}$.

Substituting this into the integral:

$\displaystyle\int_2^4 (\{x\} + [x])\,dx = \displaystyle\int_2^4 x\,dx$

Evaluating the definite integral:

$\displaystyle\int_2^4 x\,dx = \left[ \dfrac{x^2}{2} \right]_2^4$

$= \dfrac{16}{2} - \dfrac{4}{2}$

$= 8 - 2 = 6$

Answer: $6$

</details>

---

### Q30. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int_0^2 x(2 - x)^b\,dx = \dfrac{32}{7}$, where $b \in N$ then $b = $

**Options:**

- **(A)** $5$
- **(B)** $6$
- **(C)** $7$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $6$**

**Detailed Solution:**

Let $I = \int_0^2 x(2 - x)^b \, dx$.

Using the property $\int_0^a f(x) \, dx = \int_0^a f(a - x) \, dx$, we get:

$I = \int_0^2 (2 - x)(2 - (2 - x))^b \, dx$

$I = \int_0^2 (2 - x)x^b \, dx$

$I = \int_0^2 (2x^b - x^{b+1}) \, dx$

Integrating the terms, we get:

$I = \left[ \dfrac{2x^{b+1}}{b+1} - \dfrac{x^{b+2}}{b+2} \right]_0^2$

$I = \dfrac{2 \cdot 2^{b+1}}{b+1} - \dfrac{2^{b+2}}{b+2}$

$I = 2^{b+2} \left( \dfrac{1}{b+1} - \dfrac{1}{b+2} \right)$

$I = \dfrac{2^{b+2}}{(b+1)(b+2)}$

It is given that $I = \dfrac{32}{7}$.

$\dfrac{2^{b+2}}{(b+1)(b+2)} = \dfrac{32}{7}$

Substituting $b = 6$ from the options:

$\dfrac{2^{6+2}}{(6+1)(6+2)} = \dfrac{2^8}{7 \times 8} = \dfrac{256}{56} = \dfrac{32}{7}$

This satisfies the given equation. Therefore, $b = 6$.

Answer: $6$

</details>

---

### Q31. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^2 |4x - 5|\,dx = \ldots$

**Options:**

- **(A)** $\dfrac{17}{4}$
- **(B)** $\dfrac{18}{3}$
- **(C)** $\dfrac{1}{25}$
- **(D)** $\dfrac{13}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{17}{4}$**

**Detailed Solution:**

The expression inside the absolute value is zero when $4x - 5 = 0 \Rightarrow x = \dfrac{5}{4}$.

The interval of integration is from $0$ to $2$, so we split the integral at $x = \dfrac{5}{4}$.

$\int_{0}^{2} |4x - 5| dx = \int_{0}^{\dfrac{5}{4}} -(4x - 5) dx + \int_{\dfrac{5}{4}}^{2} (4x - 5) dx$

$= \int_{0}^{\dfrac{5}{4}} (5 - 4x) dx + \int_{\dfrac{5}{4}}^{2} (4x - 5) dx$

Evaluating the first integral:

$\int_{0}^{\dfrac{5}{4}} (5 - 4x) dx = \left[ 5x - 2x^2 \right]_{0}^{\dfrac{5}{4}}$

$= 5\left(\dfrac{5}{4}\right) - 2\left(\dfrac{5}{4}\right)^2$

$= \dfrac{25}{4} - 2\left(\dfrac{25}{16}\right) = \dfrac{25}{4} - \dfrac{25}{8} = \dfrac{50}{8} - \dfrac{25}{8} = \dfrac{25}{8}$

Evaluating the second integral:

$\int_{\dfrac{5}{4}}^{2} (4x - 5) dx = \left[ 2x^2 - 5x \right]_{\dfrac{5}{4}}^{2}$

$= \left( 2(2)^2 - 5(2) \right) - \left( 2\left(\dfrac{5}{4}\right)^2 - 5\left(\dfrac{5}{4}\right) \right)$

$= (8 - 10) - \left( 2\left(\dfrac{25}{16}\right) - \dfrac{25}{4} \right)$

$= -2 - \left( \dfrac{25}{8} - \dfrac{25}{4} \right) = -2 - \left( \dfrac{25 - 50}{8} \right)$

$= -2 - \left( -\dfrac{25}{8} \right) = -2 + \dfrac{25}{8} = \dfrac{-16 + 25}{8} = \dfrac{9}{8}$

Adding the two parts together:

$\int_{0}^{2} |4x - 5| dx = \dfrac{25}{8} + \dfrac{9}{8} = \dfrac{34}{8} = \dfrac{17}{4}$

</details>

---

### Q32. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $[\cdot]$ denotes the greatest integer function, then $\int_0^{\pi/3}[\tan x]\,dx = $

**Options:**

- **(A)** $\dfrac{\pi}{12}$
- **(B)** $\dfrac{\pi}{6}$
- **(C)** $\dfrac{\pi}{4}$
- **(D)** $\dfrac{\pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\pi}{12}$**

**Detailed Solution:**

The given integral is $I = \int_0^{\pi/3} [\tan x] \, dx$.

In the interval $[0, \pi/3]$, the function $\tan x$ is strictly increasing.

For $0 \le x < \pi/4$, $0 \le \tan x < 1 \Rightarrow [\tan x] = 0$.

For $\pi/4 \le x \le \pi/3$, $1 \le \tan x \le \sqrt{3} < 2 \Rightarrow [\tan x] = 1$.

Splitting the integral at $x = \pi/4$, we get:

$I = \int_0^{\pi/4} 0 \, dx + \int_{\pi/4}^{\pi/3} 1 \, dx$

$I = 0 + [x]_{\pi/4}^{\pi/3}$

$I = \dfrac{\pi}{3} - \dfrac{\pi}{4} = \dfrac{\pi}{12}$.

Answer: $\dfrac{\pi}{12}$

</details>

---

### Q33. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int_a^b(x^2 - x)\, dx = 18, \int_a^b x^3\, dx = 0$, then $a + b$ is equal to

**Options:**

- **(A)** $3$
- **(B)** $6$
- **(C)** $0$
- **(D)** $9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0$**

**Detailed Solution:**

Given $\int_a^b x^3 \, dx = 0$

$\Rightarrow \left[ \dfrac{x^4}{4} \right]_a^b = 0$

$\Rightarrow \dfrac{b^4 - a^4}{4} = 0$

$\Rightarrow b^4 = a^4$

$\Rightarrow b = a$ or $b = -a$

If $b = a$, then $\int_a^b (x^2 - x) \, dx = 0$, which contradicts the given condition $\int_a^b (x^2 - x) \, dx = 18$.

Therefore, $b = -a$.

This directly gives $a + b = 0$.

To find the exact values, substituting $b = -a$ into the first integral:

$\int_a^{-a} (x^2 - x) \, dx = 18$

$\Rightarrow -\int_{-a}^a (x^2 - x) \, dx = 18$

Using properties of definite integrals for even and odd functions:

$- \left( 2 \int_0^a x^2 \, dx - 0 \right) = 18$

$\Rightarrow -2 \left[ \dfrac{x^3}{3} \right]_0^a = 18$

$\Rightarrow -\dfrac{2a^3}{3} = 18$

$\Rightarrow a^3 = -27 \Rightarrow a = -3$

Since $b = -a$, we get $b = 3$.

Hence, $a + b = -3 + 3 = 0$.

Answer: $0$

</details>

---

### Q34. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_0^\pi \dfrac{1}{1 + 2^{\cos x}}\,dx$ is _____

**Options:**

- **(A)** $\dfrac{\pi}{2}$
- **(B)** $\pi$
- **(C)** $2\pi$
- **(D)** $\dfrac{3\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\pi}{2}$**

**Detailed Solution:**

Let $I = \int_0^\pi \dfrac{1}{1 + 2^{\cos x}} \, dx$

Using the property $\int_0^a f(x) \, dx = \int_0^a f(a-x) \, dx$, we get:

$I = \int_0^\pi \dfrac{1}{1 + 2^{\cos(\pi - x)}} \, dx$

$I = \int_0^\pi \dfrac{1}{1 + 2^{-\cos x}} \, dx$

$I = \int_0^\pi \dfrac{2^{\cos x}}{2^{\cos x} + 1} \, dx$

Adding the two equations for $I$:

$2I = \int_0^\pi \left( \dfrac{1}{1 + 2^{\cos x}} + \dfrac{2^{\cos x}}{1 + 2^{\cos x}} \right) \, dx$

$2I = \int_0^\pi 1 \, dx$

$2I = \pi$

$I = \dfrac{\pi}{2}$

Answer: $\dfrac{\pi}{2}$

</details>

---

### Q35. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_{-\pi}^{\pi}\dfrac{2x(1 + \sin x)}{1 + \cos^2 x}dx$ is...

**Options:**

- **(A)** $-\sqrt{2}\pi^2$
- **(B)** $\pi^2$
- **(C)** $\dfrac{\pi^2}{\sqrt{2}}$
- **(D)** $-\dfrac{\pi^2}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\pi^2$**

**Detailed Solution:**

Let $I = \int_{-\pi}^{\pi}\dfrac{2x(1 + \sin x)}{1 + \cos^2 x}dx$

Splitting the integral, we get:

$I = \int_{-\pi}^{\pi}\dfrac{2x}{1 + \cos^2 x}dx + \int_{-\pi}^{\pi}\dfrac{2x \sin x}{1 + \cos^2 x}dx$

The first integral is zero because the integrand $f(x) = \dfrac{2x}{1 + \cos^2 x}$ is an odd function.

The second integral has an even integrand, so:

$I = 2 \int_{0}^{\pi}\dfrac{2x \sin x}{1 + \cos^2 x}dx = 4 \int_{0}^{\pi}\dfrac{x \sin x}{1 + \cos^2 x}dx$

Using the property $\int_{0}^{a}f(x)dx = \int_{0}^{a}f(a-x)dx$, we get:

$I = 4 \int_{0}^{\pi}\dfrac{(\pi - x) \sin(\pi - x)}{1 + \cos^2(\pi - x)}dx = 4 \int_{0}^{\pi}\dfrac{(\pi - x) \sin x}{1 + \cos^2 x}dx$

Adding the two expressions for $I$:

$2I = 4 \int_{0}^{\pi}\dfrac{\pi \sin x}{1 + \cos^2 x}dx$

$I = 2\pi \int_{0}^{\pi}\dfrac{\sin x}{1 + \cos^2 x}dx$

Substituting $\cos x = t$, we get $-\sin x dx = dt$. The limits change from $1$ to $-1$:

$I = 2\pi \int_{1}^{-1}\dfrac{-dt}{1 + t^2} = 2\pi \int_{-1}^{1}\dfrac{dt}{1 + t^2}$

$I = 2\pi [\tan^{-1} t]_{-1}^{1} = 2\pi \left(\dfrac{\pi}{4} - \left(-\dfrac{\pi}{4}\right)\right)$

$I = 2\pi \left(\dfrac{\pi}{2}\right) = \pi^2$

Answer: $\pi^2$

</details>

---

### Q36. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\displaystyle\int_{\pi/6}^{\pi/3} \dfrac{\sin x - \cos x}{1 + \sin x\cos x}\,dx =$

**Options:**

- **(A)** $0$
- **(B)** $\dfrac{\pi}{12}$
- **(C)** $\dfrac{\pi}{24}$
- **(D)** $\dfrac{\pi^2}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0$**

**Detailed Solution:**

Let $I = \int_{\pi/6}^{\pi/3} \dfrac{\sin x - \cos x}{1 + \sin x\cos x}\,dx$

Using the definite integral property $\int_{a}^{b} f(x)\,dx = \int_{a}^{b} f(a+b-x)\,dx$, we substitute $x$ with $\dfrac{\pi}{6} + \dfrac{\pi}{3} - x = \dfrac{\pi}{2} - x$.

$I = \int_{\pi/6}^{\pi/3} \dfrac{\sin(\dfrac{\pi}{2} - x) - \cos(\dfrac{\pi}{2} - x)}{1 + \sin(\dfrac{\pi}{2} - x)\cos(\dfrac{\pi}{2} - x)}\,dx$

$I = \int_{\pi/6}^{\pi/3} \dfrac{\cos x - \sin x}{1 + \cos x\sin x}\,dx$

$I = -\int_{\pi/6}^{\pi/3} \dfrac{\sin x - \cos x}{1 + \sin x\cos x}\,dx$

$I = -I$

$2I = 0$

$I = 0$

Answer: $0$

</details>

---

### Q37. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int\limits_{0}^{\pi} |\sin 2x|\, \text{d}x =$

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $2$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2$**

**Detailed Solution:**

Let $I = \int_{0}^{\pi} |\sin 2x| \, dx$

Using the property $\int_{0}^{2a} f(x) \, dx = 2 \int_{0}^{a} f(x) \, dx$ if $f(2a - x) = f(x)$, we check $f(\pi - x) = |\sin(2\pi - 2x)| = |-\sin 2x| = |\sin 2x| = f(x)$.

Therefore, $I = 2 \int_{0}^{\pi/2} |\sin 2x| \, dx$

In the interval $[0, \pi/2]$, $2x \in [0, \pi]$, which means $\sin 2x \ge 0$.

$I = 2 \int_{0}^{\pi/2} \sin 2x \, dx$

$I = 2 \left[ -\dfrac{\cos 2x}{2} \right]_{0}^{\pi/2}$

$I = -(\cos \pi - \cos 0)$

$I = -(-1 - 1) = 2$

Answer: $2$

</details>

---

### Q38. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)$ is an even function, then $\int\limits_{-2}^{2} (|x| + f(x)\sin x)\, \text{d}x$ is

**Options:**

- **(A)** $2$
- **(B)** $4$
- **(C)** $6$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4$**

**Detailed Solution:**

Let $I = \int_{-2}^{2} (|x| + f(x)\sin x)\, dx$

$I = \int_{-2}^{2} |x|\, dx + \int_{-2}^{2} f(x)\sin x\, dx$

Since $f(x)$ is an even function, $f(-x) = f(x)$.

Let $g(x) = f(x)\sin x$. Then $g(-x) = f(-x)\sin(-x) = -f(x)\sin x = -g(x)$.

Thus, $g(x)$ is an odd function, which gives $\int_{-2}^{2} f(x)\sin x\, dx = 0$.

The function $|x|$ is an even function, so $\int_{-2}^{2} |x|\, dx = 2\int_{0}^{2} x\, dx$.

$I = 2 \left[ \dfrac{x^2}{2} \right]_{0}^{2} + 0$

$I = 4$

Answer: $4$

</details>

---

### Q39. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int_{-\pi/2}^{\pi/2}\left(\dfrac{x^2 \cos x}{1+e^x}\right)dx$ is equal to $\left(\dfrac{\pi^2}{A}\right) - B$. Then $\left(\dfrac{A}{B}\right) = $

**Options:**

- **(A)** $-2$
- **(B)** $2$
- **(C)** $6$
- **(D)** $-6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$**

**Detailed Solution:**

Let $I = \int_{-\pi/2}^{\pi/2} \left(\dfrac{x^2 \cos x}{1+e^x}\right) dx$

Using the property $\int_{-a}^{a} f(x) dx = \int_{0}^{a} (f(x) + f(-x)) dx$, we get:

$I = \int_{0}^{\pi/2} \left( \dfrac{x^2 \cos x}{1+e^x} + \dfrac{(-x)^2 \cos(-x)}{1+e^{-x}} \right) dx$

$I = \int_{0}^{\pi/2} x^2 \cos x \left( \dfrac{1}{1+e^x} + \dfrac{e^x}{e^x+1} \right) dx$

$I = \int_{0}^{\pi/2} x^2 \cos x dx$

Applying integration by parts:

$I = [x^2 \sin x]_{0}^{\pi/2} - \int_{0}^{\pi/2} 2x \sin x dx$

$I = \dfrac{\pi^2}{4} - \left( [-2x \cos x]_{0}^{\pi/2} - \int_{0}^{\pi/2} (-2 \cos x) dx \right)$

$I = \dfrac{\pi^2}{4} - \left( 0 + [2 \sin x]_{0}^{\pi/2} \right)$

$I = \dfrac{\pi^2}{4} - 2$

Comparing this with $\dfrac{\pi^2}{A} - B$, we get $A = 4$ and $B = 2$.

Therefore, $\dfrac{A}{B} = \dfrac{4}{2} = 2$.

Answer: $2$

</details>

---

### Q40. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int_0^a (x^2 - 4x + 1)dx = 6$, then the real value of $a$ is

**Options:**

- **(A)** $4$
- **(B)** $6$
- **(C)** $3$
- **(D)** $-3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $6$**

**Detailed Solution:**

Evaluating the given definite integral:

$\int_0^a (x^2 - 4x + 1)dx = \left[ \dfrac{x^3}{3} - 2x^2 + x \right]_0^a$

Substituting the limits, we get:

$\dfrac{a^3}{3} - 2a^2 + a = 6$

Multiplying by $3$ on both sides:

$a^3 - 6a^2 + 3a - 18 = 0$

Factorizing the polynomial:

$a^2(a - 6) + 3(a - 6) = 0$

$(a^2 + 3)(a - 6) = 0$

Since $a$ is a real number, $a^2 + 3 \neq 0$.

Therefore, $a - 6 = 0 \Rightarrow a = 6$.

Answer: $6$

</details>

---

### Q41. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int_{\pi/6}^{\pi/3} \dfrac{1}{1+\sin x + \cos x}dx = \log 2$, then the value of $\int_{\pi/6}^{\pi/3} \dfrac{\cos x}{1+\sin x + \cos x}dx = $ ............

**Options:**

- **(A)** $\dfrac{\pi}{12} - \dfrac{1}{2}\log 2$
- **(B)** $\dfrac{\pi}{12} - \dfrac{1}{3}\log 2$
- **(C)** $\dfrac{\pi}{6} - \dfrac{1}{2}\log 2$
- **(D)** $\dfrac{\pi}{12} - \dfrac{1}{4}\log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\pi}{12} - \dfrac{1}{2}\log 2$**

**Detailed Solution:**

Let $I = \int_{\pi/6}^{\pi/3} \dfrac{\cos x}{1+\sin x + \cos x}dx$

Using the definite integral property $\int_{a}^{b} f(x)dx = \int_{a}^{b} f(a+b-x)dx$, we substitute $x$ with $\dfrac{\pi}{6} + \dfrac{\pi}{3} - x = \dfrac{\pi}{2} - x$:

$I = \int_{\pi/6}^{\pi/3} \dfrac{\cos(\pi/2 - x)}{1+\sin(\pi/2 - x) + \cos(\pi/2 - x)}dx$

$I = \int_{\pi/6}^{\pi/3} \dfrac{\sin x}{1+\cos x + \sin x}dx$

Adding the two expressions for $I$:

$2I = \int_{\pi/6}^{\pi/3} \dfrac{\sin x + \cos x}{1+\sin x + \cos x}dx$

$2I = \int_{\pi/6}^{\pi/3} \dfrac{1+\sin x + \cos x - 1}{1+\sin x + \cos x}dx$

$2I = \int_{\pi/6}^{\pi/3} \left(1 - \dfrac{1}{1+\sin x + \cos x}\right)dx$

$2I = \int_{\pi/6}^{\pi/3} 1 dx - \int_{\pi/6}^{\pi/3} \dfrac{1}{1+\sin x + \cos x}dx$

Given that $\int_{\pi/6}^{\pi/3} \dfrac{1}{1+\sin x + \cos x}dx = \log 2$, we substitute this value:

$2I = [x]_{\pi/6}^{\pi/3} - \log 2$

$2I = \left(\dfrac{\pi}{3} - \dfrac{\pi}{6}\right) - \log 2$

$2I = \dfrac{\pi}{6} - \log 2$

$I = \dfrac{\pi}{12} - \dfrac{1}{2}\log 2$

Answer: $\dfrac{\pi}{12} - \dfrac{1}{2}\log 2$

</details>

---

### Q42. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\displaystyle\int_0^a \dfrac{dx}{1 + 4x^2} = \dfrac{\pi}{8}$, then $a =$

**Options:**

- **(A)** $\dfrac{1}{3}$
- **(B)** $\dfrac{1}{2}$
- **(C)** $\dfrac{1}{4}$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{2}$**

**Detailed Solution:**

Given $\displaystyle\int_0^a \dfrac{dx}{1 + 4x^2} = \dfrac{\pi}{8}$

Let $2x = t \Rightarrow 2dx = dt$

When $x = 0$, $t = 0$ and when $x = a$, $t = 2a$

The integral becomes $\dfrac{1}{2} \displaystyle\int_0^{2a} \dfrac{dt}{1 + t^2} = \dfrac{\pi}{8}$

$\dfrac{1}{2} [\tan^{-1} t]_0^{2a} = \dfrac{\pi}{8}$

$\dfrac{1}{2} \tan^{-1}(2a) = \dfrac{\pi}{8}$

$\tan^{-1}(2a) = \dfrac{\pi}{4}$

$2a = \tan\left(\dfrac{\pi}{4}\right) = 1$

$a = \dfrac{1}{2}$

Answer: $\dfrac{1}{2}$

</details>

---

### Q43. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\displaystyle\int_{-\sqrt{3}}^{\sqrt{3}} \dfrac{(2x^9 + 3x^8 - 5x^7 + 9x^6 + 4x^3 - x + 3)}{x^2 + 3} \, dx$ is

**Options:**

- **(A)** $\dfrac{162}{7} + \sqrt{3} \dfrac{\pi}{4}$
- **(B)** $\dfrac{162\sqrt{3}}{7} + \sqrt{3} \dfrac{\pi}{2}$
- **(C)** $\dfrac{162\sqrt{3}}{7} + \dfrac{\pi}{2}$
- **(D)** $\dfrac{162\sqrt{3}}{7} - \dfrac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{162\sqrt{3}}{7} + \sqrt{3} \dfrac{\pi}{2}$**

**Detailed Solution:**

Let the given integral be $I$. We can split the integrand into odd and even functions:

$I = \displaystyle\int_{-\sqrt{3}}^{\sqrt{3}} \dfrac{2x^9 - 5x^7 + 4x^3 - x}{x^2 + 3} \, dx + \displaystyle\int_{-\sqrt{3}}^{\sqrt{3}} \dfrac{3x^8 + 9x^6 + 3}{x^2 + 3} \, dx$

The first integral is $0$ because the integrand is an odd function and the limits are symmetric about the origin.

For the second integral, simplifying the integrand gives:

$I = \displaystyle\int_{-\sqrt{3}}^{\sqrt{3}} \dfrac{3x^6(x^2 + 3) + 3}{x^2 + 3} \, dx = \displaystyle\int_{-\sqrt{3}}^{\sqrt{3}} \left( 3x^6 + \dfrac{3}{x^2 + 3} \right) \, dx$

Since the integrand is an even function, we can write:

$I = 2 \displaystyle\int_{0}^{\sqrt{3}} \left( 3x^6 + \dfrac{3}{x^2 + 3} \right) \, dx$

Integrating with respect to $x$:

$I = 2 \left[ \dfrac{3x^7}{7} + \dfrac{3}{\sqrt{3}} \tan^{-1}\left(\dfrac{x}{\sqrt{3}}\right) \right]_0^{\sqrt{3}}$

Substituting the limits:

$I = 2 \left( \dfrac{3(\sqrt{3})^7}{7} + \sqrt{3} \tan^{-1}(1) - 0 \right)$

Using $(\sqrt{3})^7 = 27\sqrt{3}$ and $\tan^{-1}(1) = \dfrac{\pi}{4}$:

$I = 2 \left( \dfrac{3 \times 27\sqrt{3}}{7} + \sqrt{3} \dfrac{\pi}{4} \right)$

$I = \dfrac{162\sqrt{3}}{7} + \sqrt{3} \dfrac{\pi}{2}$

Answer: $\dfrac{162\sqrt{3}}{7} + \sqrt{3} \dfrac{\pi}{2}$

</details>

---

### Q44. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $[\cdot]$ denotes the greatest integer function, then $\int_1^4 x[x] dx$ is equal to

**Options:**

- **(A)** $34$
- **(B)** $-17$
- **(C)** $-34$
- **(D)** $17$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $17$**

**Detailed Solution:**

The given integral can be split at integer values since $[x]$ changes its value at integers.

$I = \int_1^4 x[x] dx$

$I = \int_1^2 x[x] dx + \int_2^3 x[x] dx + \int_3^4 x[x] dx$

Substituting the values of $[x]$ in the respective intervals:

$I = \int_1^2 x(1) dx + \int_2^3 x(2) dx + \int_3^4 x(3) dx$

$I = \left[ \dfrac{x^2}{2} \right]_1^2 + \left[ x^2 \right]_2^3 + \left[ \dfrac{3x^2}{2} \right]_3^4$

$I = \left( \dfrac{4}{2} - \dfrac{1}{2} \right) + (9 - 4) + \left( \dfrac{48}{2} - \dfrac{27}{2} \right)$

$I = \dfrac{3}{2} + 5 + \dfrac{21}{2}$

$I = \dfrac{24}{2} + 5$

$I = 12 + 5 = 17$

Answer: $17$

</details>

---

### Q45. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\int_1^a (2x + 1) dx = 5$, then the sum of the values of $a$ is..

**Options:**

- **(A)** $1$
- **(B)** $-1$
- **(C)** $7$
- **(D)** $-7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-1$**

**Detailed Solution:**

Evaluating the definite integral:

$\int_1^a (2x + 1) dx = [x^2 + x]_1^a$

Substituting the limits:

$(a^2 + a) - (1^2 + 1) = 5$

$a^2 + a - 2 = 5$

$a^2 + a - 7 = 0$

This is a quadratic equation in $a$. The sum of the roots of the equation is $-\dfrac{1}{1} = -1$.

Answer: $-1$

</details>

---

### Q46. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_0^\pi\left|\sin ^3 x\right| \mathrm{d} x$ is

**Options:**

- **(A)** 0
- **(B)** $\frac{3}{8}$
- **(C)** $\frac{4}{3}$
- **(D)** $\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{4}{3}$**

**Detailed Solution:**

In the interval $[0, \pi]$, $\sin x \ge 0$, so $\left|\sin^3 x\right| = \sin^3 x$.

The integral becomes:

$I = \int_0^\pi \sin^3 x \mathrm{d} x$

Using the identity $\sin 3x = 3\sin x - 4\sin^3 x$, we get $\sin^3 x = \dfrac{3\sin x - \sin 3x}{4}$.

Substituting this into the integral:

$I = \int_0^\pi \dfrac{3\sin x - \sin 3x}{4} \mathrm{d} x$

$I = \dfrac{1}{4} \left[ -3\cos x + \dfrac{\cos 3x}{3} \right]_0^\pi$

$I = \dfrac{1}{4} \left[ \left( -3\cos \pi + \dfrac{\cos 3\pi}{3} \right) - \left( -3\cos 0 + \dfrac{\cos 0}{3} \right) \right]$

$I = \dfrac{1}{4} \left[ \left( -3(-1) + \dfrac{-1}{3} \right) - \left( -3(1) + \dfrac{1}{3} \right) \right]$

$I = \dfrac{1}{4} \left[ \left( 3 - \dfrac{1}{3} \right) - \left( -3 + \dfrac{1}{3} \right) \right]$

$I = \dfrac{1}{4} \left[ \dfrac{8}{3} - \left( -\dfrac{8}{3} \right) \right]$

$I = \dfrac{1}{4} \left[ \dfrac{16}{3} \right] = \dfrac{4}{3}$

Answer: $\frac{4}{3}$

</details>

---

### Q47. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(5-x)=\mathrm{f}(x)$ and $\int_2^3 \mathrm{f}(x) \mathrm{d} x=2$ then $\int_2^3 x \mathrm{f}(x) \mathrm{d} x=$

**Options:**

- **(A)** 5
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 5**

**Detailed Solution:**

Let $I = \int_2^3 x \mathrm{f}(x) \mathrm{d} x$

Using the property $\int_a^b \mathrm{g}(x) \mathrm{d} x = \int_a^b \mathrm{g}(a+b-x) \mathrm{d} x$, we get:

$I = \int_2^3 (2+3-x) \mathrm{f}(2+3-x) \mathrm{d} x$

$I = \int_2^3 (5-x) \mathrm{f}(5-x) \mathrm{d} x$

Since $\mathrm{f}(5-x) = \mathrm{f}(x)$, this becomes:

$I = \int_2^3 (5-x) \mathrm{f}(x) \mathrm{d} x$

$I = 5 \int_2^3 \mathrm{f}(x) \mathrm{d} x - \int_2^3 x \mathrm{f}(x) \mathrm{d} x$

$I = 5 \int_2^3 \mathrm{f}(x) \mathrm{d} x - I$

$2I = 5 \int_2^3 \mathrm{f}(x) \mathrm{d} x$

Substituting $\int_2^3 \mathrm{f}(x) \mathrm{d} x = 2$:

$2I = 5 \times 2$

$2I = 10$

$I = 5$

Answer: 5

</details>

---

### Q48. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^{\frac{\pi}{2}} \frac{300 \sin x+100 \cos x}{\sin x+\cos x} \mathrm{~d} x=\ldots$

**Options:**

- **(A)** $100 \pi$
- **(B)** $300 \pi$
- **(C)** $200 \pi$
- **(D)** $150 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $100 \pi$**

**Detailed Solution:**

Let $I = \int_0^{\dfrac{\pi}{2}} \dfrac{300 \sin x + 100 \cos x}{\sin x + \cos x} \mathrm{d} x$

Using the property $\int_0^a f(x) \mathrm{d} x = \int_0^a f(a-x) \mathrm{d} x$, we get:

$I = \int_0^{\dfrac{\pi}{2}} \dfrac{300 \sin\left(\dfrac{\pi}{2}-x\right) + 100 \cos\left(\dfrac{\pi}{2}-x\right)}{\sin\left(\dfrac{\pi}{2}-x\right) + \cos\left(\dfrac{\pi}{2}-x\right)} \mathrm{d} x$

$I = \int_0^{\dfrac{\pi}{2}} \dfrac{300 \cos x + 100 \sin x}{\cos x + \sin x} \mathrm{d} x$

Adding the two equations for $I$:

$2I = \int_0^{\dfrac{\pi}{2}} \dfrac{300 \sin x + 100 \cos x + 300 \cos x + 100 \sin x}{\sin x + \cos x} \mathrm{d} x$

$2I = \int_0^{\dfrac{\pi}{2}} \dfrac{400(\sin x + \cos x)}{\sin x + \cos x} \mathrm{d} x$

$2I = \int_0^{\dfrac{\pi}{2}} 400 \mathrm{d} x$

$2I = 400 [x]_0^{\dfrac{\pi}{2}} = 400 \left(\dfrac{\pi}{2}\right) = 200 \pi$

$I = 100 \pi$

Answer: $100 \pi$

</details>

---

### Q49. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^1 x\left|x-\frac{1}{2}\right| \mathrm{d} x=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{1}{12}$
- **(C)** $\frac{1}{8}$
- **(D)** $\frac{1}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{8}$**

**Detailed Solution:**

Let $I = \int_0^1 x\left|x-\dfrac{1}{2}\right| \mathrm{d} x$

Substitute $t = x - \dfrac{1}{2}$, so $\mathrm{d}x = \mathrm{d}t$. The limits change from $x=0 \Rightarrow t=-\dfrac{1}{2}$ and $x=1 \Rightarrow t=\dfrac{1}{2}$.

$I = \int_{-1/2}^{1/2} \left(t + \dfrac{1}{2}\right) |t| \mathrm{d} t$

$I = \int_{-1/2}^{1/2} t |t| \mathrm{d} t + \dfrac{1}{2} \int_{-1/2}^{1/2} |t| \mathrm{d} t$

The function $f(t) = t|t|$ is an odd function, so its integral over a symmetric interval $[-a, a]$ is $0$.

The function $g(t) = |t|$ is an even function, so its integral over $[-a, a]$ is $2 \int_0^a |t| \mathrm{d} t$.

$I = 0 + \dfrac{1}{2} \times 2 \int_0^{1/2} t \mathrm{d} t$

$I = \int_0^{1/2} t \mathrm{d} t = \left[ \dfrac{t^2}{2} \right]_0^{1/2}$

$I = \dfrac{1}{2} \left( \dfrac{1}{4} - 0 \right) = \dfrac{1}{8}$

Answer: $\frac{1}{8}$

</details>

---

### Q50. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{\frac{1}{2}}^2 \frac{1}{x} \sin^{101}\left(x-\frac{1}{x}\right) \mathrm{d} x=$

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{101}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Let $I = \int_{\dfrac{1}{2}}^2 \dfrac{1}{x} \sin^{101}\left(x-\dfrac{1}{x}\right) dx$

Substitute $x = \dfrac{1}{t}$, which gives $dx = -\dfrac{1}{t^2} dt$.

The limits of integration change from $\dfrac{1}{2} \rightarrow 2$ to $2 \rightarrow \dfrac{1}{2}$.

$I = \int_2^{\dfrac{1}{2}} t \sin^{101}\left(\dfrac{1}{t}-t\right) \left(-\dfrac{1}{t^2}\right) dt$

$I = \int_{\dfrac{1}{2}}^2 \dfrac{1}{t} \sin^{101}\left(-\left(t-\dfrac{1}{t}\right)\right) dt$

Since $\sin(-\theta) = -\sin\theta$ and $101$ is an odd integer, $\sin^{101}(-\theta) = -\sin^{101}\theta$.

$I = -\int_{\dfrac{1}{2}}^2 \dfrac{1}{t} \sin^{101}\left(t-\dfrac{1}{t}\right) dt$

Replacing the dummy variable $t$ with $x$, we get:

$I = -\int_{\dfrac{1}{2}}^2 \dfrac{1}{x} \sin^{101}\left(x-\dfrac{1}{x}\right) dx$

$I = -I$

$2I = 0$

$I = 0$

Answer: 0

</details>

---

### Q51. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{\frac{-\pi}{4}}^{\frac{\pi}{4}} \sec ^{4} x \mathrm{~d} x=$

**Options:**

- **(A)** $-\frac{8}{3}$
- **(B)** $\frac{8}{3}$
- **(C)** $\frac{2}{3}$
- **(D)** $-\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{8}{3}$**

**Detailed Solution:**

Let $I = \int_{-\pi/4}^{\pi/4} \sec^4 x \, dx$

Since $f(x) = \sec^4 x$ is an even function, $I = 2 \int_{0}^{\pi/4} \sec^4 x \, dx$

$I = 2 \int_{0}^{\pi/4} (1 + \tan^2 x) \sec^2 x \, dx$

Let $\tan x = t$, then $\sec^2 x \, dx = dt$

When $x = 0$, $t = 0$ and when $x = \pi/4$, $t = 1$

$I = 2 \int_{0}^{1} (1 + t^2) \, dt$

$I = 2 \left[ t + \dfrac{t^3}{3} \right]_{0}^{1}$

$I = 2 \left( 1 + \dfrac{1}{3} \right) = 2 \left( \dfrac{4}{3} \right) = \dfrac{8}{3}$

Answer: $\frac{8}{3}$

</details>

---

### Q52. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{\log \frac{1}{2}}^{\log 2} \sin \left(\frac{e^x-1}{e^x+1}\right) d x=$

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** $\cos \frac{1}{2}$
- **(D)** $2 \log \frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Let $I = \int_{\log \dfrac{1}{2}}^{\log 2} \sin \left(\dfrac{e^x-1}{e^x+1}\right) d x$

The lower limit is $\log \dfrac{1}{2} = -\log 2$.

The integral is of the form $\int_{-a}^{a} f(x) d x$, where $a = \log 2$ and $f(x) = \sin \left(\dfrac{e^x-1}{e^x+1}\right)$.

Checking if the function is even or odd:

$f(-x) = \sin \left(\dfrac{e^{-x}-1}{e^{-x}+1}\right)$

$f(-x) = \sin \left(\dfrac{\dfrac{1}{e^x}-1}{\dfrac{1}{e^x}+1}\right)$

$f(-x) = \sin \left(\dfrac{1-e^x}{1+e^x}\right)$

$f(-x) = \sin \left(-\dfrac{e^x-1}{e^x+1}\right)$

$f(-x) = -\sin \left(\dfrac{e^x-1}{e^x+1}\right) = -f(x)$

Since $f(-x) = -f(x)$, $f(x)$ is an odd function.

Using the property of definite integrals, $\int_{-a}^{a} f(x) d x = 0$ if $f(x)$ is an odd function.

Therefore, $I = 0$.

Answer: 0

</details>

---

### Q53. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_1^3 \frac{\log x^2}{\log \left(16 x^2-8 x^3+x^4\right)} \mathrm{d} x=\ldots$

**Options:**

- **(A)** 1
- **(B)** 3
- **(C)** $\log 2$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

Let $I = \int_1^3 \dfrac{\log x^2}{\log \left(16 x^2-8 x^3+x^4\right)} \mathrm{d} x$

Simplifying the expression in the denominator:

$16 x^2 - 8 x^3 + x^4 = x^2(16 - 8x + x^2) = x^2(4-x)^2 = (x(4-x))^2$

Substituting this back into the integral:

$I = \int_1^3 \dfrac{\log x^2}{\log (x(4-x))^2} \mathrm{d} x$

$I = \int_1^3 \dfrac{2\log x}{2\log (x(4-x))} \mathrm{d} x$

$I = \int_1^3 \dfrac{\log x}{\log x + \log (4-x)} \mathrm{d} x$

Using the definite integral property $\int_a^b f(x) \mathrm{d} x = \int_a^b f(a+b-x) \mathrm{d} x$, we replace $x$ with $1+3-x = 4-x$:

$I = \int_1^3 \dfrac{\log (4-x)}{\log (4-x) + \log (4-(4-x))} \mathrm{d} x$

$I = \int_1^3 \dfrac{\log (4-x)}{\log (4-x) + \log x} \mathrm{d} x$

Adding the two equations for $I$:

$2I = \int_1^3 \dfrac{\log x + \log (4-x)}{\log x + \log (4-x)} \mathrm{d} x$

$2I = \int_1^3 1 \mathrm{d} x$

$2I = [x]_1^3 = 3 - 1 = 2$

$I = 1$

Answer: 1

</details>

---

### Q54. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^1 \log \left(\frac{1}{x}-1\right) \mathrm{d} x=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** 1
- **(C)** 2
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

Let $I = \int_0^1 \log \left(\dfrac{1}{x}-1\right) \mathrm{d} x$

$I = \int_0^1 \log \left(\dfrac{1-x}{x}\right) \mathrm{d} x$

Using the property $\int_0^a f(x) \mathrm{d} x = \int_0^a f(a-x) \mathrm{d} x$, we substitute $x$ with $1-x$:

$I = \int_0^1 \log \left(\dfrac{1-(1-x)}{1-x}\right) \mathrm{d} x$

$I = \int_0^1 \log \left(\dfrac{x}{1-x}\right) \mathrm{d} x$

Adding the two equations for $I$, we get:

$2I = \int_0^1 \left[ \log \left(\dfrac{1-x}{x}\right) + \log \left(\dfrac{x}{1-x}\right) \right] \mathrm{d} x$

Using the property $\log A + \log B = \log(AB)$:

$2I = \int_0^1 \log \left(\dfrac{1-x}{x} \times \dfrac{x}{1-x}\right) \mathrm{d} x$

$2I = \int_0^1 \log(1) \mathrm{d} x$

Since $\log(1) = 0$:

$2I = 0 \Rightarrow I = 0$

Answer: 0

</details>

---

### Q55. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{\frac{-\pi}{2}}^{\frac{\pi}{2}}\left(x^2+\log \left(\frac{\pi-x}{\pi+x}\right) \cdot \cos x\right) \mathrm{d} x=$

**Options:**

- **(A)** $0$
- **(B)** $\frac{\pi^3}{48}$
- **(C)** $\frac{\pi^3}{12}$
- **(D)** $\frac{\pi^3}{24}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi^3}{12}$**

**Detailed Solution:**

Let $I = \int_{-\dfrac{\pi}{2}}^{\dfrac{\pi}{2}} \left(x^2 + \log \left(\dfrac{\pi-x}{\pi+x}\right) \cos x\right) dx$

$I = \int_{-\dfrac{\pi}{2}}^{\dfrac{\pi}{2}} x^2 dx + \int_{-\dfrac{\pi}{2}}^{\dfrac{\pi}{2}} \log \left(\dfrac{\pi-x}{\pi+x}\right) \cos x dx$

Let $f(x) = \log \left(\dfrac{\pi-x}{\pi+x}\right) \cos x$

$f(-x) = \log \left(\dfrac{\pi+x}{\pi-x}\right) \cos(-x) = -\log \left(\dfrac{\pi-x}{\pi+x}\right) \cos x = -f(x)$

Since $f(x)$ is an odd function, $\int_{-\dfrac{\pi}{2}}^{\dfrac{\pi}{2}} \log \left(\dfrac{\pi-x}{\pi+x}\right) \cos x dx = 0$

Since $x^2$ is an even function:

$I = 2 \int_{0}^{\dfrac{\pi}{2}} x^2 dx + 0$

$I = 2 \left[ \dfrac{x^3}{3} \right]_{0}^{\dfrac{\pi}{2}}$

$I = 2 \left( \dfrac{\pi^3}{24} \right) = \dfrac{\pi^3}{12}$

Answer: $\frac{\pi^3}{12}$

</details>

---

### Q56. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_3^5 \frac{\sqrt{x} d x}{\sqrt{8-x}+\sqrt{x}}=$

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

Let $I = \int_3^5 \dfrac{\sqrt{x}}{\sqrt{8-x}+\sqrt{x}} dx$

Using the property $\int_a^b f(x) dx = \int_a^b f(a+b-x) dx$, we substitute $x$ with $3+5-x = 8-x$:

$I = \int_3^5 \dfrac{\sqrt{8-x}}{\sqrt{8-(8-x)}+\sqrt{8-x}} dx$

$I = \int_3^5 \dfrac{\sqrt{8-x}}{\sqrt{x}+\sqrt{8-x}} dx$

Adding the two equations for $I$:

$2I = \int_3^5 \dfrac{\sqrt{x} + \sqrt{8-x}}{\sqrt{8-x}+\sqrt{x}} dx$

$2I = \int_3^5 1 dx$

$2I = [x]_3^5$

$2I = 5 - 3 = 2$

$I = 1$

Answer: 1

</details>

---

### Q57. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_0^1 \tan ^{-1}\left(1-x+x^2\right) \mathrm{d} x$ is

**Options:**

- **(A)** $\frac{\pi}{2}-\log 2$
- **(B)** $\frac{\pi}{2}+\log 2$
- **(C)** $\log 2$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log 2$**

**Detailed Solution:**

Let $I = \int_0^1 \tan^{-1}(1 - x + x^2) \, dx$.

Using the identity $\tan^{-1}(y) + \cot^{-1}(y) = \dfrac{\pi}{2}$, we can write:

$\tan^{-1}(1 - x + x^2) = \dfrac{\pi}{2} - \cot^{-1}(1 - x + x^2) = \dfrac{\pi}{2} - \tan^{-1}\left(\dfrac{1}{1 - x + x^2}\right)$

We can rewrite the argument of the second term as:

$\dfrac{1}{1 - x + x^2} = \dfrac{x - (x - 1)}{1 + x(x - 1)}$

Using the formula $\tan^{-1}\left(\dfrac{A - B}{1 + AB}\right) = \tan^{-1}(A) - \tan^{-1}(B)$, we get:

$\tan^{-1}\left(\dfrac{x - (x - 1)}{1 + x(x - 1)}\right) = \tan^{-1}(x) - \tan^{-1}(x - 1)$

Substitute this back into the integral:

$I = \int_0^1 \left[ \dfrac{\pi}{2} - \tan^{-1}(x) + \tan^{-1}(x - 1) \right] dx$

$I = \int_0^1 \dfrac{\pi}{2} \, dx - \int_0^1 \tan^{-1}(x) \, dx + \int_0^1 \tan^{-1}(x - 1) \, dx$

For the third integral, using the property $\int_0^a f(x) \, dx = \int_0^a f(a - x) \, dx$:

$\int_0^1 \tan^{-1}(x - 1) \, dx = \int_0^1 \tan^{-1}((1 - x) - 1) \, dx = \int_0^1 \tan^{-1}(-x) \, dx = -\int_0^1 \tan^{-1}(x) \, dx$

Thus, the integral simplifies to:

$I = \dfrac{\pi}{2} - 2 \int_0^1 \tan^{-1}(x) \, dx$

Now, evaluate $\int_0^1 \tan^{-1}(x) \, dx$ using integration by parts:

$\int_0^1 \tan^{-1}(x) \cdot 1 \, dx = \left[ x \tan^{-1}(x) \right]_0^1 - \int_0^1 \dfrac{x}{1 + x^2} \, dx$

$= \left( 1 \cdot \dfrac{\pi}{4} - 0 \right) - \dfrac{1}{2} \left[ \log(1 + x^2) \right]_0^1$

$= \dfrac{\pi}{4} - \dfrac{1}{2} \log 2$

Substituting this value back into $I$:

$I = \dfrac{\pi}{2} - 2 \left( \dfrac{\pi}{4} - \dfrac{1}{2} \log 2 \right)$

$I = \dfrac{\pi}{2} - \dfrac{\pi}{2} + \log 2 = \log 2$

Answer: $\log 2$

</details>

---

### Q58. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^{\frac{\pi}{4}}(\sqrt{\tan x}+\sqrt{\cot x}) \mathrm{d} x=$

**Options:**

- **(A)** $\sqrt{2} \pi$
- **(B)** $\frac{\pi}{2}$
- **(C)** $2 \pi$
- **(D)** $\frac{\pi}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{\sqrt{2}}$**

**Detailed Solution:**

Let $I = \int_0^{\dfrac{\pi}{4}} (\sqrt{\tan x} + \sqrt{\cot x}) \mathrm{d}x$

$I = \int_0^{\dfrac{\pi}{4}} \left( \dfrac{\sqrt{\sin x}}{\sqrt{\cos x}} + \dfrac{\sqrt{\cos x}}{\sqrt{\sin x}} \right) \mathrm{d}x$

$I = \int_0^{\dfrac{\pi}{4}} \dfrac{\sin x + \cos x}{\sqrt{\sin x \cos x}} \mathrm{d}x$

Multiplying and dividing by $\sqrt{2}$:

$I = \sqrt{2} \int_0^{\dfrac{\pi}{4}} \dfrac{\sin x + \cos x}{\sqrt{2 \sin x \cos x}} \mathrm{d}x$

$I = \sqrt{2} \int_0^{\dfrac{\pi}{4}} \dfrac{\sin x + \cos x}{\sqrt{1 - (1 - 2 \sin x \cos x)}} \mathrm{d}x$

$I = \sqrt{2} \int_0^{\dfrac{\pi}{4}} \dfrac{\sin x + \cos x}{\sqrt{1 - (\sin x - \cos x)^2}} \mathrm{d}x$

Let $\sin x - \cos x = t$

Differentiating with respect to $x$, we get $(\cos x + \sin x) \mathrm{d}x = \mathrm{d}t$

When $x = 0$, $t = \sin 0 - \cos 0 = -1$

When $x = \dfrac{\pi}{4}$, $t = \sin \dfrac{\pi}{4} - \cos \dfrac{\pi}{4} = 0$

Substituting these values into the integral:

$I = \sqrt{2} \int_{-1}^{0} \dfrac{1}{\sqrt{1 - t^2}} \mathrm{d}t$

$I = \sqrt{2} [ \sin^{-1} t ]_{-1}^{0}$

$I = \sqrt{2} (\sin^{-1} 0 - \sin^{-1} (-1))$

$I = \sqrt{2} \left( 0 - \left( -\dfrac{\pi}{2} \right) \right)$

$I = \sqrt{2} \times \dfrac{\pi}{2} = \dfrac{\pi}{\sqrt{2}}$

Answer: $\frac{\pi}{\sqrt{2}}$

</details>

---

### Q59. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^2 \frac{3 x+1}{x^2+4} d x=$

**Options:**

- **(A)** $\log (2 \sqrt{2})+\frac{\pi}{4}$
- **(B)** $\log (2 \sqrt{2})+\frac{\pi}{6}$
- **(C)** $\log (2 \sqrt{2})+\frac{\pi}{8}$
- **(D)** $\log (2 \sqrt{2})+\frac{\pi}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log (2 \sqrt{2})+\frac{\pi}{8}$**

**Detailed Solution:**

Let $I = \int_0^2 \dfrac{3x+1}{x^2+4} dx$

Splitting the integral into two parts:

$I = \int_0^2 \dfrac{3x}{x^2+4} dx + \int_0^2 \dfrac{1}{x^2+4} dx$

$I = \dfrac{3}{2} \int_0^2 \dfrac{2x}{x^2+4} dx + \int_0^2 \dfrac{1}{x^2+2^2} dx$

Using the standard integrals $\int \dfrac{f'(x)}{f(x)} dx = \log|f(x)|$ and $\int \dfrac{1}{x^2+a^2} dx = \dfrac{1}{a} \tan^{-1}\left(\dfrac{x}{a}\right)$:

$I = \dfrac{3}{2} \left[ \log(x^2+4) \right]_0^2 + \dfrac{1}{2} \left[ \tan^{-1}\left(\dfrac{x}{2}\right) \right]_0^2$

$I = \dfrac{3}{2} (\log 8 - \log 4) + \dfrac{1}{2} (\tan^{-1} 1 - \tan^{-1} 0)$

$I = \dfrac{3}{2} \log\left(\dfrac{8}{4}\right) + \dfrac{1}{2} \left(\dfrac{\pi}{4} - 0\right)$

$I = \dfrac{3}{2} \log 2 + \dfrac{\pi}{8}$

$I = \log(2^{3/2}) + \dfrac{\pi}{8}$

$I = \log(2\sqrt{2}) + \dfrac{\pi}{8}$

Answer: $\log (2 \sqrt{2})+\frac{\pi}{8}$

</details>

---

### Q60. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{\frac{\pi}{3}}^{\frac{2 \pi}{3}} \frac{x}{1+\sin x} \mathrm{~d} x=$

**Options:**

- **(A)** $\pi(\sqrt{3}-2)$
- **(B)** $\pi(2-\sqrt{3})$
- **(C)** $\pi(\sqrt{3}+2)$
- **(D)** $\frac{\pi}{2}(2-\sqrt{3})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\pi(2-\sqrt{3})$**

**Detailed Solution:**

Let $I = \int_{\dfrac{\pi}{3}}^{\dfrac{2 \pi}{3}} \dfrac{x}{1+\sin x} \mathrm{~d} x$

Using the property $\int_{a}^{b} f(x) \mathrm{~d} x = \int_{a}^{b} f(a+b-x) \mathrm{~d} x$, we substitute $x$ with $\dfrac{\pi}{3} + \dfrac{2\pi}{3} - x = \pi - x$:

$I = \int_{\dfrac{\pi}{3}}^{\dfrac{2 \pi}{3}} \dfrac{\pi - x}{1+\sin(\pi - x)} \mathrm{~d} x = \int_{\dfrac{\pi}{3}}^{\dfrac{2 \pi}{3}} \dfrac{\pi - x}{1+\sin x} \mathrm{~d} x$

Adding the two equations for $I$:

$2I = \int_{\dfrac{\pi}{3}}^{\dfrac{2 \pi}{3}} \dfrac{\pi}{1+\sin x} \mathrm{~d} x$

$I = \dfrac{\pi}{2} \int_{\dfrac{\pi}{3}}^{\dfrac{2 \pi}{3}} \dfrac{1}{1+\sin x} \mathrm{~d} x$

Multiplying the numerator and denominator by $1-\sin x$:

$I = \dfrac{\pi}{2} \int_{\dfrac{\pi}{3}}^{\dfrac{2 \pi}{3}} \dfrac{1-\sin x}{1-\sin^2 x} \mathrm{~d} x$

$I = \dfrac{\pi}{2} \int_{\dfrac{\pi}{3}}^{\dfrac{2 \pi}{3}} \dfrac{1-\sin x}{\cos^2 x} \mathrm{~d} x$

$I = \dfrac{\pi}{2} \int_{\dfrac{\pi}{3}}^{\dfrac{2 \pi}{3}} (\sec^2 x - \sec x \tan x) \mathrm{~d} x$

$I = \dfrac{\pi}{2} [\tan x - \sec x]_{\dfrac{\pi}{3}}^{\dfrac{2 \pi}{3}}$

Substituting the limits:

$I = \dfrac{\pi}{2} \left[ \left( \tan\left(\dfrac{2\pi}{3}\right) - \sec\left(\dfrac{2\pi}{3}\right) \right) - \left( \tan\left(\dfrac{\pi}{3}\right) - \sec\left(\dfrac{\pi}{3}\right) \right) \right]$

$I = \dfrac{\pi}{2} \left[ (-\sqrt{3} - (-2)) - (\sqrt{3} - 2) \right]$

$I = \dfrac{\pi}{2} [ 2 - \sqrt{3} - \sqrt{3} + 2 ]$

$I = \dfrac{\pi}{2} [ 4 - 2\sqrt{3} ]$

$I = \pi(2 - \sqrt{3})$

Answer: $\pi(2-\sqrt{3})$

</details>

---

### Q61. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^{\frac{\pi}{4}} \frac{\cos ^2 x \sin ^2 x}{\left(\cos ^3 x+\sin ^3 x\right)^2} \mathrm{~d} x=$

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{-1}{3}$
- **(C)** $\frac{1}{6}$
- **(D)** $\frac{-1}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{6}$**

**Detailed Solution:**

Let $I = \int_0^{\dfrac{\pi}{4}} \dfrac{\cos^2 x \sin^2 x}{(\cos^3 x + \sin^3 x)^2} dx$

Dividing the numerator and the denominator by $\cos^6 x$, we get:

$I = \int_0^{\dfrac{\pi}{4}} \dfrac{\dfrac{\cos^2 x \sin^2 x}{\cos^6 x}}{\dfrac{(\cos^3 x + \sin^3 x)^2}{\cos^6 x}} dx$

$I = \int_0^{\dfrac{\pi}{4}} \dfrac{\tan^2 x \sec^2 x}{(1 + \tan^3 x)^2} dx$

Substitute $t = 1 + \tan^3 x$

Differentiating with respect to $x$, we get:

$dt = 3 \tan^2 x \sec^2 x dx$

$\Rightarrow \tan^2 x \sec^2 x dx = \dfrac{dt}{3}$

Changing the limits of integration:
When $x = 0$, $t = 1 + \tan^3(0) = 1$
When $x = \dfrac{\pi}{4}$, $t = 1 + \tan^3\left(\dfrac{\pi}{4}\right) = 1 + 1 = 2$

Substituting these into the integral:

$I = \int_1^2 \dfrac{1}{t^2} \dfrac{dt}{3}$

$I = \dfrac{1}{3} \int_1^2 t^{-2} dt$

$I = \dfrac{1}{3} \left[ -\dfrac{1}{t} \right]_1^2$

$I = \dfrac{1}{3} \left( -\dfrac{1}{2} - \left(-\dfrac{1}{1}\right) \right)$

$I = \dfrac{1}{3} \left( 1 - \dfrac{1}{2} \right)$

$I = \dfrac{1}{3} \times \dfrac{1}{2} = \dfrac{1}{6}$

Answer: $\frac{1}{6}$

</details>

---

### Q62. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{-1}^3\left(\tan ^{-1}\left(\frac{x}{x^2+1}\right)+\tan ^{-1}\left(\frac{x^2+1}{x}\right)\right) \mathrm{d} x=$

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{2 \pi}{3}$
- **(C)** $2 \pi$
- **(D)** $\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\pi$**

**Detailed Solution:**

Let $I = \int_{-1}^3 \left( \tan^{-1}\left(\dfrac{x}{x^2+1}\right) + \tan^{-1}\left(\dfrac{x^2+1}{x}\right) \right) \mathrm{d} x$

We know the standard property of inverse trigonometric functions:
$\tan^{-1}(y) + \tan^{-1}\left(\dfrac{1}{y}\right) = \dfrac{\pi}{2}$ for $y > 0$
$\tan^{-1}(y) + \tan^{-1}\left(\dfrac{1}{y}\right) = -\dfrac{\pi}{2}$ for $y < 0$

Here, $y = \dfrac{x}{x^2+1}$. Since $x^2+1 > 0$ for all real $x$, the sign of $y$ depends entirely on the sign of $x$.

For $x > 0$, $y > 0 \Rightarrow \tan^{-1}\left(\dfrac{x}{x^2+1}\right) + \tan^{-1}\left(\dfrac{x^2+1}{x}\right) = \dfrac{\pi}{2}$

For $x < 0$, $y < 0 \Rightarrow \tan^{-1}\left(\dfrac{x}{x^2+1}\right) + \tan^{-1}\left(\dfrac{x^2+1}{x}\right) = -\dfrac{\pi}{2}$

Splitting the integral at $x = 0$, we get:
$I = \int_{-1}^0 \left(-\dfrac{\pi}{2}\right) \mathrm{d} x + \int_0^3 \left(\dfrac{\pi}{2}\right) \mathrm{d} x$

$I = -\dfrac{\pi}{2} [x]_{-1}^0 + \dfrac{\pi}{2} [x]_0^3$

$I = -\dfrac{\pi}{2} (0 - (-1)) + \dfrac{\pi}{2} (3 - 0)$

$I = -\dfrac{\pi}{2}(1) + \dfrac{\pi}{2}(3)$

$I = -\dfrac{\pi}{2} + \dfrac{3\pi}{2} = \pi$

Answer: $\pi$

</details>

---

### Q63. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_0^2\left[x^2\right] \mathrm{d} x$ is (where $[x]$ denotes the greatest integer function not greater than $x$ )

**Options:**

- **(A)** $5-\sqrt{2}-\sqrt{3}$
- **(B)** $5+\sqrt{2}-\sqrt{3}$
- **(C)** $5+\sqrt{2}+\sqrt{3}$
- **(D)** $5-\sqrt{2}+\sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $5-\sqrt{2}-\sqrt{3}$**

**Detailed Solution:**

Let $I = \int_0^2 [x^2] \, dx$

The interval $[0, 2]$ is divided into sub-intervals where $[x^2]$ takes constant integer values. The points of discontinuity are where $x^2$ is an integer, which are $x = 1, \sqrt{2}, \sqrt{3}$.

$I = \int_0^1 [x^2] \, dx + \int_1^{\sqrt{2}} [x^2] \, dx + \int_{\sqrt{2}}^{\sqrt{3}} [x^2] \, dx + \int_{\sqrt{3}}^2 [x^2] \, dx$

In $(0, 1)$, $0 \leq x^2 < 1 \Rightarrow [x^2] = 0$

In $(1, \sqrt{2})$, $1 \leq x^2 < 2 \Rightarrow [x^2] = 1$

In $(\sqrt{2}, \sqrt{3})$, $2 \leq x^2 < 3 \Rightarrow [x^2] = 2$

In $(\sqrt{3}, 2)$, $3 \leq x^2 < 4 \Rightarrow [x^2] = 3$

Substituting these values into the integral:

$I = \int_0^1 0 \, dx + \int_1^{\sqrt{2}} 1 \, dx + \int_{\sqrt{2}}^{\sqrt{3}} 2 \, dx + \int_{\sqrt{3}}^2 3 \, dx$

$I = 0 + [x]_1^{\sqrt{2}} + 2[x]_{\sqrt{2}}^{\sqrt{3}} + 3[x]_{\sqrt{3}}^2$

$I = (\sqrt{2} - 1) + 2(\sqrt{3} - \sqrt{2}) + 3(2 - \sqrt{3})$

$I = \sqrt{2} - 1 + 2\sqrt{3} - 2\sqrt{2} + 6 - 3\sqrt{3}$

$I = 5 - \sqrt{2} - \sqrt{3}$

Answer: $5-\sqrt{2}-\sqrt{3}$

</details>

---

### Q64. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_2^4 \frac{\log x^2}{\log x^2+\log \left(36-12 x+x^2\right)} \mathrm{d} x$ is equal to

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $4$
- **(D)** $6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

Let $I = \int_2^4 \dfrac{\log x^2}{\log x^2+\log \left(36-12 x+x^2\right)} \mathrm{d} x$

Since $36-12x+x^2 = (6-x)^2$, we can write:

$I = \int_2^4 \dfrac{\log x^2}{\log x^2+\log (6-x)^2} \mathrm{d} x$

Using the definite integral property $\int_a^b f(x) \mathrm{d} x = \int_a^b f(a+b-x) \mathrm{d} x$, we substitute $x$ with $2+4-x = 6-x$:

$I = \int_2^4 \dfrac{\log (6-x)^2}{\log (6-x)^2+\log (6-(6-x))^2} \mathrm{d} x$

$I = \int_2^4 \dfrac{\log (6-x)^2}{\log (6-x)^2+\log x^2} \mathrm{d} x$

Adding the two equations for $I$:

$2I = \int_2^4 \dfrac{\log x^2 + \log (6-x)^2}{\log x^2 + \log (6-x)^2} \mathrm{d} x$

$2I = \int_2^4 1 \mathrm{d} x$

$2I = [x]_2^4 = 4 - 2 = 2$

$I = 1$

Answer: $1$

</details>

---

### Q65. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_0^{\frac{\pi}{2}} \frac{\mathrm{~d} x}{1+(\cot x)^{101}}=$

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{8}$
- **(D)** $\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{4}$**

**Detailed Solution:**

Let $I = \int_0^{\dfrac{\pi}{2}} \dfrac{1}{1+(\cot x)^{101}} \mathrm{d} x$

Using the property $\int_0^a f(x) \mathrm{d} x = \int_0^a f(a-x) \mathrm{d} x$, we get:

$I = \int_0^{\dfrac{\pi}{2}} \dfrac{1}{1+\cot^{101} (\dfrac{\pi}{2}-x)} \mathrm{d} x$

$I = \int_0^{\dfrac{\pi}{2}} \dfrac{1}{1+\tan^{101} x} \mathrm{d} x$

$I = \int_0^{\dfrac{\pi}{2}} \dfrac{1}{1+\dfrac{1}{\cot^{101} x}} \mathrm{d} x$

$I = \int_0^{\dfrac{\pi}{2}} \dfrac{\cot^{101} x}{\cot^{101} x + 1} \mathrm{d} x$

Adding the two equations for $I$:

$2I = \int_0^{\dfrac{\pi}{2}} \left( \dfrac{1}{1+\cot^{101} x} + \dfrac{\cot^{101} x}{1+\cot^{101} x} \right) \mathrm{d} x$

$2I = \int_0^{\dfrac{\pi}{2}} 1 \mathrm{d} x$

$2I = [x]_0^{\dfrac{\pi}{2}} = \dfrac{\pi}{2}$

$I = \dfrac{\pi}{4}$

Answer: $\frac{\pi}{4}$

</details>

---

### Q66. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\int_{-1}^1\left(\sqrt{1+x+x^2}-\sqrt{1-x+x^2}\right) \mathrm{d} x$ is

**Options:**

- **(A)** $-1$
- **(B)** $0$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0$**

**Detailed Solution:**

Let $I = \int_{-1}^1 \left(\sqrt{1+x+x^2} - \sqrt{1-x+x^2}\right) \mathrm{d} x$

Let $f(x) = \sqrt{1+x+x^2} - \sqrt{1-x+x^2}$

$f(-x) = \sqrt{1+(-x)+(-x)^2} - \sqrt{1-(-x)+(-x)^2}$

$f(-x) = \sqrt{1-x+x^2} - \sqrt{1+x+x^2}$

$f(-x) = - \left(\sqrt{1+x+x^2} - \sqrt{1-x+x^2}\right)$

$f(-x) = -f(x)$

Since $f(x)$ is an odd function, $\int_{-a}^a f(x) \mathrm{d} x = 0$.

Therefore, $I = 0$.

Answer: $0$

</details>

---

### Q67. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{-2}^2\left|x^2-x-2\right| \mathrm{dx}=$

**Options:**

- **(A)** $\frac{17}{3}$
- **(B)** $\frac{19}{3}$
- **(C)** $19$
- **(D)** $17$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{19}{3}$**

**Detailed Solution:**

Let $I = \int_{-2}^2\left|x^2-x-2\right| \mathrm{dx}$

First, find the roots of the quadratic expression:
$x^2 - x - 2 = (x - 2)(x + 1)$

The roots are $x = -1$ and $x = 2$.
For $x \in [-2, -1]$, $x^2 - x - 2 \ge 0$.
For $x \in [-1, 2]$, $x^2 - x - 2 \le 0$.

Splitting the integral at $x = -1$, we get:
$I = \int_{-2}^{-1} (x^2 - x - 2) \mathrm{dx} - \int_{-1}^2 (x^2 - x - 2) \mathrm{dx}$

Integrating the terms:
$I = \left[ \dfrac{x^3}{3} - \dfrac{x^2}{2} - 2x \right]_{-2}^{-1} - \left[ \dfrac{x^3}{3} - \dfrac{x^2}{2} - 2x \right]_{-1}^2$

Substituting the limits for the first integral:
$\left( -\dfrac{1}{3} - \dfrac{1}{2} + 2 \right) - \left( -\dfrac{8}{3} - \dfrac{4}{2} + 4 \right) = \dfrac{7}{6} - \left( -\dfrac{2}{3} \right) = \dfrac{7}{6} + \dfrac{4}{6} = \dfrac{11}{6}$

Substituting the limits for the second integral:
$\left( \dfrac{8}{3} - \dfrac{4}{2} - 4 \right) - \left( -\dfrac{1}{3} - \dfrac{1}{2} + 2 \right) = -\dfrac{10}{3} - \dfrac{7}{6} = -\dfrac{20}{6} - \dfrac{7}{6} = -\dfrac{27}{6}$

Now, combining both parts:
$I = \dfrac{11}{6} - \left( -\dfrac{27}{6} \right) = \dfrac{11}{6} + \dfrac{27}{6} = \dfrac{38}{6} = \dfrac{19}{3}$

Answer: $\frac{19}{3}$

</details>

---

### Q68. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\int_{-3}^3 \sin ^7 x \cos ^{16} x \mathrm{~d} x$ is

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $0$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0$**

**Detailed Solution:**

Let $I = \int_{-3}^3 \sin^7 x \cos^{16} x \, \mathrm{d}x$

Let $f(x) = \sin^7 x \cos^{16} x$

Evaluating $f(-x)$:

$f(-x) = \sin^7(-x) \cos^{16}(-x)$

Since $\sin(-x) = -\sin x$ and $\cos(-x) = \cos x$, we get:

$f(-x) = (-\sin x)^7 (\cos x)^{16} = -\sin^7 x \cos^{16} x = -f(x)$

Since $f(-x) = -f(x)$, $f(x)$ is an odd function.

Using the property of definite integrals, $\int_{-a}^a f(x) \, \mathrm{d}x = 0$ if $f(x)$ is an odd function.

Therefore, $I = 0$.

Answer: $0$

</details>

---

### Q69. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_1^4 \log [x] \mathrm{d} x$ where $[x]$ is the greatest integer function less than or equal to $x$ is equal to

**Options:**

- **(A)** $\log 5$
- **(B)** $\log 6$
- **(C)** $\log 2$
- **(D)** $\log 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log 6$**

**Detailed Solution:**

The given integral is $I = \int_1^4 \log [x] \mathrm{d} x$.

We split the integral at integer values of $x$ because the greatest integer function $[x]$ changes its value at integers.

$I = \int_1^2 \log [x] \mathrm{d} x + \int_2^3 \log [x] \mathrm{d} x + \int_3^4 \log [x] \mathrm{d} x$

For $x \in [1, 2)$, $[x] = 1 \Rightarrow \log [x] = \log 1 = 0$

For $x \in [2, 3)$, $[x] = 2 \Rightarrow \log [x] = \log 2$

For $x \in [3, 4)$, $[x] = 3 \Rightarrow \log [x] = \log 3$

Substituting these values into the integrals:

$I = \int_1^2 0 \mathrm{d} x + \int_2^3 \log 2 \mathrm{d} x + \int_3^4 \log 3 \mathrm{d} x$

$I = 0 + \log 2 [x]_2^3 + \log 3 [x]_3^4$

$I = \log 2 (3 - 2) + \log 3 (4 - 3)$

$I = \log 2 + \log 3$

Using the property of logarithms $\log a + \log b = \log(ab)$:

$I = \log(2 \times 3) = \log 6$

Answer: $\log 6$

</details>

---

### Q70. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $[x]$ denotes the greatest integer function, then $\int_0^5 x^2[x] \mathrm{d} x=$

**Options:**

- **(A)** $\frac{244}{3}$
- **(B)** $\frac{316}{3}$
- **(C)** $\frac{200}{3}$
- **(D)** $\frac{400}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{400}{3}$**

**Detailed Solution:**

The given integral can be split into intervals of length $1$ because the greatest integer function $[x]$ is constant on each such interval.

$\int_0^5 x^2[x] \mathrm{d} x = \int_0^1 x^2(0) \mathrm{d} x + \int_1^2 x^2(1) \mathrm{d} x + \int_2^3 x^2(2) \mathrm{d} x + \int_3^4 x^2(3) \mathrm{d} x + \int_4^5 x^2(4) \mathrm{d} x$

Evaluating each integral separately:

$\int_0^5 x^2[x] \mathrm{d} x = 0 + \left[ \dfrac{x^3}{3} \right]_1^2 + 2\left[ \dfrac{x^3}{3} \right]_2^3 + 3\left[ \dfrac{x^3}{3} \right]_3^4 + 4\left[ \dfrac{x^3}{3} \right]_4^5$

Substituting the limits:

$\int_0^5 x^2[x] \mathrm{d} x = 0 + \dfrac{8 - 1}{3} + 2\left( \dfrac{27 - 8}{3} \right) + 3\left( \dfrac{64 - 27}{3} \right) + 4\left( \dfrac{125 - 64}{3} \right)$

$\int_0^5 x^2[x] \mathrm{d} x = \dfrac{7}{3} + 2\left( \dfrac{19}{3} \right) + 3\left( \dfrac{37}{3} \right) + 4\left( \dfrac{61}{3} \right)$

$\int_0^5 x^2[x] \mathrm{d} x = \dfrac{7}{3} + \dfrac{38}{3} + \dfrac{111}{3} + \dfrac{244}{3}$

$\int_0^5 x^2[x] \mathrm{d} x = \dfrac{7 + 38 + 111 + 244}{3} = \dfrac{400}{3}$

Answer: $\frac{400}{3}$

</details>

---

### Q71. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $I=\int_0^{\frac{\pi}{4}} \log (1+\tan x) d x$, then value of $I$ is

**Options:**

- **(A)** $\frac{\pi}{16} \log 2$
- **(B)** $\frac{\pi}{2} \log 2$
- **(C)** $\frac{\pi}{8} \log 2$
- **(D)** $\frac{\pi}{4} \log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{8} \log 2$**

**Detailed Solution:**

$I = \int_0^{\dfrac{\pi}{4}} \log (1+\tan x) d x$

Using the property $\int_0^a f(x) d x = \int_0^a f(a-x) d x$,

$I = \int_0^{\dfrac{\pi}{4}} \log \left(1+\tan \left(\dfrac{\pi}{4}-x\right)\right) d x$

$I = \int_0^{\dfrac{\pi}{4}} \log \left(1+\dfrac{1-\tan x}{1+\tan x}\right) d x$

$I = \int_0^{\dfrac{\pi}{4}} \log \left(\dfrac{1+\tan x+1-\tan x}{1+\tan x}\right) d x$

$I = \int_0^{\dfrac{\pi}{4}} \log \left(\dfrac{2}{1+\tan x}\right) d x$

$I = \int_0^{\dfrac{\pi}{4}} (\log 2 - \log (1+\tan x)) d x$

$I = \int_0^{\dfrac{\pi}{4}} \log 2 \, d x - \int_0^{\dfrac{\pi}{4}} \log (1+\tan x) d x$

$I = \log 2 [x]_0^{\dfrac{\pi}{4}} - I$

$2I = \dfrac{\pi}{4} \log 2$

$I = \dfrac{\pi}{8} \log 2$

Answer: $\frac{\pi}{8} \log 2$

</details>

---

### Q72. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0.2}^{3.5}[x] \mathrm{d} x=$
(where $[x]=$ greatest integer not greater than $x$ )

**Options:**

- **(A)** 4
- **(B)** 4.2
- **(C)** 4.5
- **(D)** 4.4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4.5**

**Detailed Solution:**

$\int_{0.2}^{3.5}[x] \mathrm{d} x = \int_{0.2}^{1}[x] \mathrm{d} x + \int_{1}^{2}[x] \mathrm{d} x + \int_{2}^{3}[x] \mathrm{d} x + \int_{3}^{3.5}[x] \mathrm{d} x$

$= \int_{0.2}^{1} 0 \mathrm{d} x + \int_{1}^{2} 1 \mathrm{d} x + \int_{2}^{3} 2 \mathrm{d} x + \int_{3}^{3.5} 3 \mathrm{d} x$

$= 0 + [x]_{1}^{2} + [2x]_{2}^{3} + [3x]_{3}^{3.5}$

$= 0 + (2 - 1) + (6 - 4) + (10.5 - 9)$

$= 1 + 2 + 1.5 = 4.5$

Answer: 4.5

</details>

---

### Q73. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int_{\frac{-\pi}{4}}^{\frac{\pi}{4}}(\cos x)^{-4} \mathrm{~d} x$ has the value

**Options:**

- **(A)** $\dfrac{-3}{2}$
- **(B)** $\dfrac{3}{2}$
- **(C)** $\dfrac{8}{3}$
- **(D)** $\dfrac{-8}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{8}{3}$**

**Detailed Solution:**

Let $I = \int_{-\dfrac{\pi}{4}}^{\dfrac{\pi}{4}} (\cos x)^{-4} dx$

$I = \int_{-\dfrac{\pi}{4}}^{\dfrac{\pi}{4}} \sec^4 x dx$

$I = \int_{-\dfrac{\pi}{4}}^{\dfrac{\pi}{4}} (1 + \tan^2 x) \sec^2 x dx$

Let $\tan x = t$, then $\sec^2 x dx = dt$

When $x = -\dfrac{\pi}{4}$, $t = -1$ and when $x = \dfrac{\pi}{4}$, $t = 1$

$I = \int_{-1}^{1} (1 + t^2) dt$

$I = \left[ t + \dfrac{t^3}{3} \right]_{-1}^{1}$

$I = \left( 1 + \dfrac{1}{3} \right) - \left( -1 - \dfrac{1}{3} \right)$

$I = \dfrac{4}{3} - \left( -\dfrac{4}{3} \right) = \dfrac{8}{3}$

Answer: $\dfrac{8}{3}$

</details>

---

### Q74. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^{\dfrac{\pi}{4}} \log \left(\dfrac{\sin x+\cos x}{\cos x}\right) d x=$

**Options:**

- **(A)** $\dfrac{\pi}{2} \log 2$
- **(B)** $\dfrac{\pi}{4} \log 2$
- **(C)** $\dfrac{\pi}{6} \log 2$
- **(D)** $\dfrac{\pi}{8} \log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{\pi}{8} \log 2$**

**Detailed Solution:**

Let $I = \int_0^{\dfrac{\pi}{4}} \log \left(\dfrac{\sin x+\cos x}{\cos x}\right) d x$

$I = \int_0^{\dfrac{\pi}{4}} \log (1 + \tan x) d x$

Using the property $\int_0^a f(x) d x = \int_0^a f(a-x) d x$:

$I = \int_0^{\dfrac{\pi}{4}} \log \left(1 + \tan \left(\dfrac{\pi}{4} - x\right)\right) d x$

$I = \int_0^{\dfrac{\pi}{4}} \log \left(1 + \dfrac{1 - \tan x}{1 + \tan x}\right) d x$

$I = \int_0^{\dfrac{\pi}{4}} \log \left(\dfrac{2}{1 + \tan x}\right) d x$

$I = \int_0^{\dfrac{\pi}{4}} (\log 2 - \log (1 + \tan x)) d x$

$I = \int_0^{\dfrac{\pi}{4}} \log 2 d x - \int_0^{\dfrac{\pi}{4}} \log (1 + \tan x) d x$

$I = \dfrac{\pi}{4} \log 2 - I$

$2I = \dfrac{\pi}{4} \log 2$

$I = \dfrac{\pi}{8} \log 2$

Answer: $\dfrac{\pi}{8} \log 2$

</details>

---

### Q75. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^{\dfrac{\pi}{2}}|\sin x-\cos x| d x$ has the value

**Options:**

- **(A)** $2 \sqrt{2}+1$
- **(B)** $2(\sqrt{2}+1)$
- **(C)** $2(\sqrt{2}-1)$
- **(D)** $2 \sqrt{2}-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2(\sqrt{2}-1)$**

**Detailed Solution:**

Let $I = \int_0^{\dfrac{\pi}{2}} |\sin x - \cos x| dx$

Since $\cos x \ge \sin x$ for $x \in [0, \dfrac{\pi}{4}]$ and $\sin x \ge \cos x$ for $x \in [\dfrac{\pi}{4}, \dfrac{\pi}{2}]$, we split the integral at $x = \dfrac{\pi}{4}$:

$I = \int_0^{\dfrac{\pi}{4}} (\cos x - \sin x) dx + \int_{\dfrac{\pi}{4}}^{\dfrac{\pi}{2}} (\sin x - \cos x) dx$

Evaluating the first integral:

$\int_0^{\dfrac{\pi}{4}} (\cos x - \sin x) dx = [\sin x + \cos x]_0^{\dfrac{\pi}{4}} = (\dfrac{1}{\sqrt{2}} + \dfrac{1}{\sqrt{2}}) - (0 + 1) = \sqrt{2} - 1$

Evaluating the second integral:

$\int_{\dfrac{\pi}{4}}^{\dfrac{\pi}{2}} (\sin x - \cos x) dx = [-\cos x - \sin x]_{\dfrac{\pi}{4}}^{\dfrac{\pi}{2}} = (0 - 1) - (-\dfrac{1}{\sqrt{2}} - \dfrac{1}{\sqrt{2}}) = \sqrt{2} - 1$

Adding both parts:

$I = (\sqrt{2} - 1) + (\sqrt{2} - 1) = 2(\sqrt{2} - 1)$

Answer: $2(\sqrt{2}-1)$

</details>

---

### Q76. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of $I=I=\int_{-\dfrac{\pi}{2}}^{\dfrac{\pi}{2}} \dfrac{x^2 \cos x}{1+e^{-x}} \mathrm{~d} x$ is equal to

**Options:**

- **(A)** $\dfrac{\pi^2}{4}-2$
- **(B)** $\dfrac{\pi^2}{4}+2$
- **(C)** $\pi^2-\mathrm{e}^{\dfrac{\pi}{2}}$
- **(D)** $\pi^2+\mathrm{e}^{\dfrac{\pi}{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\pi^2}{4}-2$**

**Detailed Solution:**

Let $I = \int_{-\dfrac{\pi}{2}}^{\dfrac{\pi}{2}} \dfrac{x^2 \cos x}{1+e^{-x}} \mathrm{d} x$

Using the property $\int_{-a}^{a} f(x) \mathrm{d} x = \int_{0}^{a} (f(x) + f(-x)) \mathrm{d} x$, we get:

$I = \int_{0}^{\dfrac{\pi}{2}} \left( \dfrac{x^2 \cos x}{1+e^{-x}} + \dfrac{(-x)^2 \cos(-x)}{1+e^{x}} \right) \mathrm{d} x$

$I = \int_{0}^{\dfrac{\pi}{2}} x^2 \cos x \left( \dfrac{e^x}{e^x+1} + \dfrac{1}{e^x+1} \right) \mathrm{d} x$

$I = \int_{0}^{\dfrac{\pi}{2}} x^2 \cos x \mathrm{d} x$

Applying integration by parts:

$I = \left[ x^2 \sin x \right]_{0}^{\dfrac{\pi}{2}} - \int_{0}^{\dfrac{\pi}{2}} 2x \sin x \mathrm{d} x$

$I = \dfrac{\pi^2}{4} - \left( \left[ -2x \cos x \right]_{0}^{\dfrac{\pi}{2}} + \int_{0}^{\dfrac{\pi}{2}} 2 \cos x \mathrm{d} x \right)$

$I = \dfrac{\pi^2}{4} - \left( 0 + \left[ 2 \sin x \right]_{0}^{\dfrac{\pi}{2}} \right)$

$I = \dfrac{\pi^2}{4} - 2$

Answer: $\dfrac{\pi^2}{4}-2$

</details>

---

### Q77. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The integral $\int_{\dfrac{-1}{2}}^{\dfrac{1}{2}}\left([x]+\log _c\left(\dfrac{1+x}{1-x}\right)\right) \mathrm{d} x$, where $[x]$ represent greatest integer function, equals

**Options:**

- **(A)** $-\dfrac{1}{2}$
- **(B)** $\log _e\left(\dfrac{1}{2}\right)$
- **(C)** $\dfrac{1}{2}$
- **(D)** $2 \log _{\mathrm{e}}\left(\dfrac{1}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\dfrac{1}{2}$**

**Detailed Solution:**

Let the given integral be $I = \int_{\dfrac{-1}{2}}^{\dfrac{1}{2}} [x] \mathrm{d} x + \int_{\dfrac{-1}{2}}^{\dfrac{1}{2}} \log_e\left(\dfrac{1+x}{1-x}\right) \mathrm{d} x$

Let $f(x) = \log_e\left(\dfrac{1+x}{1-x}\right)$

$f(-x) = \log_e\left(\dfrac{1-x}{1+x}\right) = -\log_e\left(\dfrac{1+x}{1-x}\right) = -f(x)$

Since $f(x)$ is an odd function, $\int_{\dfrac{-1}{2}}^{\dfrac{1}{2}} \log_e\left(\dfrac{1+x}{1-x}\right) \mathrm{d} x = 0$

For the first integral, splitting the limits at $x = 0$:

$\int_{\dfrac{-1}{2}}^{\dfrac{1}{2}} [x] \mathrm{d} x = \int_{\dfrac{-1}{2}}^{0} [x] \mathrm{d} x + \int_{0}^{\dfrac{1}{2}} [x] \mathrm{d} x$

In the interval $\left[\dfrac{-1}{2}, 0\right)$, $[x] = -1$

In the interval $\left[0, \dfrac{1}{2}\right)$, $[x] = 0$

$\int_{\dfrac{-1}{2}}^{\dfrac{1}{2}} [x] \mathrm{d} x = \int_{\dfrac{-1}{2}}^{0} (-1) \mathrm{d} x + \int_{0}^{\dfrac{1}{2}} 0 \mathrm{d} x$

$= -1 \left(0 - \left(\dfrac{-1}{2}\right)\right) + 0 = -\dfrac{1}{2}$

Therefore, $I = -\dfrac{1}{2} + 0 = -\dfrac{1}{2}$

Answer: $-\dfrac{1}{2}$

</details>

---

### Q78. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\mathrm{I}=\int_{\sqrt{\log _e 2}}^{\sqrt{\log _e 3}} \dfrac{x \sin x^2}{\sin x^2+\sin \left(\log _e 6-x^2\right)} \mathrm{d} x$ is

**Options:**

- **(A)** $\dfrac{1}{4} \log _e \dfrac{3}{2}$
- **(B)** $\dfrac{1}{2} \log _e \dfrac{3}{2}$
- **(C)** $\quad \log _{\mathrm{e}} \dfrac{3}{2}$
- **(D)** $\dfrac{1}{6} \log _e \dfrac{3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{4} \log _e \dfrac{3}{2}$**

**Detailed Solution:**

Let $I = \int_{\sqrt{\log_e 2}}^{\sqrt{\log_e 3}} \dfrac{x \sin x^2}{\sin x^2 + \sin(\log_e 6 - x^2)} dx$

Substitute $x^2 = t \Rightarrow 2x dx = dt \Rightarrow x dx = \dfrac{1}{2} dt$

When $x = \sqrt{\log_e 2}$, $t = \log_e 2$

When $x = \sqrt{\log_e 3}$, $t = \log_e 3$

$I = \dfrac{1}{2} \int_{\log_e 2}^{\log_e 3} \dfrac{\sin t}{\sin t + \sin(\log_e 6 - t)} dt \dots (1)$

Using the property $\int_a^b f(t) dt = \int_a^b f(a+b-t) dt$, where $a+b = \log_e 2 + \log_e 3 = \log_e 6$

$I = \dfrac{1}{2} \int_{\log_e 2}^{\log_e 3} \dfrac{\sin(\log_e 6 - t)}{\sin(\log_e 6 - t) + \sin t} dt \dots (2)$

Adding (1) and (2):

$2I = \dfrac{1}{2} \int_{\log_e 2}^{\log_e 3} \dfrac{\sin t + \sin(\log_e 6 - t)}{\sin t + \sin(\log_e 6 - t)} dt$

$2I = \dfrac{1}{2} \int_{\log_e 2}^{\log_e 3} 1 dt$

$2I = \dfrac{1}{2} [t]_{\log_e 2}^{\log_e 3}$

$2I = \dfrac{1}{2} (\log_e 3 - \log_e 2)$

$2I = \dfrac{1}{2} \log_e \dfrac{3}{2}$

$I = \dfrac{1}{4} \log_e \dfrac{3}{2}$

Answer: $\dfrac{1}{4} \log _e \dfrac{3}{2}$

</details>

---

### Q79. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f$ and $g$ be continuous functions on $[0, \mathrm{a}]$ such that $\mathrm{f}(x)=\mathrm{f}(\mathrm{a}-x)$ and $g(x)+g(a-x)=4$, then $\int_0^a f(x) g(x) d x$ is equal to

**Options:**

- **(A)** $\quad 4 \int_0^a \mathrm{f}(x) \mathrm{d} x$
- **(B)** $\int_0^a \mathrm{f}(x) \mathrm{d} x$
- **(C)** $2 \int_0^{\mathrm{a}} \mathrm{f}(x) \mathrm{d} x$
- **(D)** $\quad-3 \int_0^a \mathrm{f}(x) \mathrm{d} x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 \int_0^{\mathrm{a}} \mathrm{f}(x) \mathrm{d} x$**

**Detailed Solution:**

Let $I = \int_0^a f(x) g(x) dx$

Using the property of definite integrals $\int_0^a h(x) dx = \int_0^a h(a-x) dx$, we get:

$I = \int_0^a f(a-x) g(a-x) dx$

Given $f(x) = f(a-x)$, the integral becomes:

$I = \int_0^a f(x) g(a-x) dx$

Adding the two equations for $I$ yields:

$2I = \int_0^a f(x) g(x) dx + \int_0^a f(x) g(a-x) dx$

$2I = \int_0^a f(x) [g(x) + g(a-x)] dx$

Substituting the given relation $g(x) + g(a-x) = 4$:

$2I = \int_0^a f(x) (4) dx$

$2I = 4 \int_0^a f(x) dx$

$I = 2 \int_0^a f(x) dx$

Answer: $2 \int_0^{\mathrm{a}} \mathrm{f}(x) \mathrm{d} x$

</details>

---

### Q80. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $I_n=\int_0^{\frac{\pi}{4}} \tan ^n \theta d \theta$, then $I_{12}+I_{10}=$

**Options:**

- **(A)** $\frac {1}{8}$
- **(B)** $\frac {1}{12}$
- **(C)** $\frac {1}{11}$
- **(D)** $\frac {1}{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac {1}{11}$**

**Detailed Solution:**

$\begin{aligned} & \int_0^{\frac{\pi}{4}}\left(\tan ^{\mathrm{n}} x+\tan ^{\mathrm{n}-2} x\right) \mathrm{d} x=\frac{1}{\mathrm{n}-1} \\ & \therefore \quad \mathrm{I}_{12}+\mathrm{I}_{10}=\int_0^{\frac{\pi}{4}}\left(\tan ^{12} \theta+\tan ^{10} \theta\right) \mathrm{d} \theta \\ &=\frac{1}{12-1} \\ &=\frac{1}{11}\end{aligned}$

</details>

---

### Q81. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\left\{\begin{array}{ll}\mathrm{e}^{\cos x} \sin x & , \text { for }|x| \leq 2 \\ 2, & \text { otherwise }\end{array}\right.$, then $\int_{-2}^3 \mathrm{f}(x) \mathrm{d} x$ is equal to

**Options:**

- **(A)** 0
- **(B)** 2
- **(C)** 1
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2**

**Detailed Solution:**

$$
\begin{aligned}
\int_{-2}^3 \mathrm{f}(x) \mathrm{d} x & =\int_{-2}^2 \mathrm{f}(x) \mathrm{d} x+\int_2^3 \mathrm{f}(x) \mathrm{d} x \\
& =\int_{-2}^2 \mathrm{e}^{\cos x} \sin x \mathrm{~d} x+\int_2^3 2 \mathrm{~d} x
\end{aligned}
$$
Since $\mathrm{e}^{\cos x} \sin x$ is an odd function.
$$
\therefore \quad \int_{-2}^3 \mathrm{f}(x) \mathrm{d} x=0+2(3-2)=2
$$

</details>

---

### Q82. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_0^\pi\left|\sin x-\frac{2 x}{\pi}\right| \mathrm{d} x$ is

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{2}$
- **(C)** $\pi$
- **(D)** $2\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{2}$**

**Detailed Solution:**

$\begin{aligned} & \int_0^\pi\left|\sin x-\frac{2 x}{\pi}\right| \mathrm{d} x \\ & =\int_0^{\frac{\pi}{2}}\left(\sin x-\frac{2 x}{\pi}\right) \mathrm{d} x+\int_{\frac{\pi}{2}}^\pi\left(\frac{2 x}{\pi}-\sin x\right) \mathrm{d} x \\ & =[-\cos x]_0^{\frac{\pi}{2}}-\left[\frac{x^2}{\pi}\right]_0^{\frac{\pi}{2}}+\left[\frac{x^2}{\pi}\right]_{\frac{\pi}{2}}^\pi+[\cos x]_{\frac{\pi}{2}}^\pi \\ & =(0+1)-\left(\frac{\pi}{4}-0\right)+\left(\pi-\frac{\pi}{4}\right)+(-1-0) \\ & =\frac{\pi}{2}\end{aligned}$

</details>

---

### Q83. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$$
\int_0^4|2 x-5| \mathrm{d} x=
$$

**Options:**

- **(A)** $\frac{13}{2}$
- **(B)** $\frac{15}{2}$
- **(C)** $\frac{17}{4}$
- **(D)** $\frac{17}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{17}{2}$**

**Detailed Solution:**

$\begin{aligned} \int_0^4|2 x-5| \mathrm{d} x & =\int_0^{\frac{5}{2}}(5-2 x) \mathrm{d} x+\int_{\frac{5}{2}}^4(2 x-5) \mathrm{d} x \\ & =\left[5 x-x^2\right]_0^{\frac{5}{2}}+\left[x^2-5 x\right]_{\frac{5}{2}}^4 \\ & =\frac{25}{4}+\frac{9}{4} \\ & =\frac{34}{4} \\ & =\frac{17}{2}\end{aligned}$

</details>

---

### Q84. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{-1}^3\left(\cot ^{-1}\left(\frac{x}{x^2+1}\right)+\cot ^{-1}\left(\frac{x^2+1}{x}\right)\right) \mathrm{d} x=$

**Options:**

- **(A)** $\left(\frac{\pi}{4}\right)$
- **(B)** $\pi$
- **(C)** $\left(\frac{\pi}{2}\right)$
- **(D)** $(2 \pi)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(2 \pi)$**

**Detailed Solution:**

$\begin{array}{rlr}\text { Let } \mathrm{I} & =\int_{-1}^3\left(\cot ^{-1}\left(\frac{x}{x^2+1}\right)+\cot ^{-1}\left(\frac{x^2+1}{x}\right)\right) \mathrm{d} x \\ & =\int_{-1}^3\left(\tan ^{-1}\left(\frac{x^2+1}{x}\right)+\cot ^{-1}\left(\frac{x^2+1}{x}\right)\right) \mathrm{d} x \\ & =\int_{-1}^3 \frac{\pi}{2} \mathrm{~d} x \quad \ldots\left[\because \cot ^{-1}(x)=\tan ^{-1}\left(\frac{1}{x}\right)\right] \\ & =\frac{\pi}{2}[x]_{-1}^3 & \\ & =\frac{\pi}{2}(4) & \end{array}$
OBJECT END]

</details>

---

### Q85. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int_0^\pi \frac{\mathrm{d} x}{4+3 \cos x}=$

**Options:**

- **(A)** $\frac{2 \pi}{7}$
- **(B)** $\frac{\pi}{\sqrt{7}}$
- **(C)** $\frac{\pi}{2 \sqrt{7}}$
- **(D)** $\frac{\pi}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{\sqrt{7}}$**

**Detailed Solution:**

Let $\mathrm{I}=\int_0^\pi \frac{\mathrm{dx}}{4+3 \cos x}$
Put $\tan \frac{x}{2}=\mathrm{t}$
$\therefore \quad \mathrm{d} x=\frac{2 \mathrm{dt}}{1+\mathrm{t}^2}$ and $\cos x=\frac{1-\mathrm{t}^2}{1+\mathrm{t}^2}$
$\begin{aligned} \therefore \quad \mathrm{I}=\int_0^\pi \frac{\mathrm{d} x}{4+3 \cos x} & =\int_0^{\infty} \frac{2 \mathrm{dt}}{7+\mathrm{t}^2} \\ & =\left[\frac{2}{\sqrt{7}} \tan ^{-1}\left(\frac{\mathrm{t}}{\sqrt{7}}\right)\right]_0^{\infty} \\ & =\frac{2}{\sqrt{7}}\left[\tan ^{-1} \infty-0\right] \\ & =\frac{2}{\sqrt{7}} \cdot \frac{\pi}{2}=\frac{\pi}{\sqrt{7}}\end{aligned}$

</details>

---

### Q86. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f: R \rightarrow R$ and $g: R \rightarrow R$ be continuous functions. Then the value of the integral
$\int_{\frac{-\pi}{2}}^{\frac{\pi}{2}}[\mathrm{f}(x)+\mathrm{f}(-x)][\mathrm{g}(x)-\mathrm{g}(-x)] \mathrm{d} x$ is

**Options:**

- **(A)** $\pi$
- **(B)** $1$
- **(C)** $-1$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0$**

**Detailed Solution:**

Let $\mathrm{h}(x)=[\mathrm{f}(x)+\mathrm{f}(-x)][\mathrm{g}(x)-\mathrm{g}(-x)]$
$\begin{aligned}
\therefore \quad \mathrm{h}(-x) & =[\mathrm{f}(-x)+\mathrm{f}(x)][\mathrm{g}(-x)-\mathrm{g}(x)] \\
& =-[\mathrm{f}(x)+\mathrm{f}(-x)][\mathrm{g}(x)-\mathrm{g}(-x)] \\
& =-\mathrm{h}(x)
\end{aligned}$
$\therefore \quad \mathrm{h}(x)$ is an odd function.
$\therefore \quad \int_{\frac{-\pi}{2}}^{\frac{\pi}{2}} \mathrm{~h}(x)=0$

</details>

---

### Q87. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{-\frac{\pi}{4}}^{\frac{\pi}{4}} \frac{e^x(x \sin x)}{e^{2 x}-1} d x=$

**Options:**

- **(A)** 0
- **(B)** $\frac{\pi}{3}$
- **(C)** $\frac{\pi}{2}$
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

$\int_{\frac{-\pi}{4}}^{\frac{\pi}{4}} \frac{e^x \cdot x \cdot \sin x}{e^{2 x}-1} \mathrm{~d} x=0\left[\begin{array}{c}a \\ \because \int_{-a}^a f(x) \mathrm{d} x=0 \\ \text { if } f(x) \text { is an odd function }\end{array}\right]$

</details>

---

### Q88. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\frac{\pi}{2}$
The value of $\int_0 \frac{\mathrm{d} x}{1+\tan ^3 x}$

**Options:**

- **(A)** 0
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{2}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{4}$**

**Detailed Solution:**

$\begin{aligned} & \int_0^{\frac{\pi}{2}} \frac{\mathrm{d} x}{1+\tan ^3 x}=\int_0^{\frac{\pi}{2}} \frac{\cos ^3 x}{\cos ^3 x+\sin ^3 x} \mathrm{~d} x=\frac{\frac{\pi}{2}-0}{2}=\frac{\pi}{4} \\ & {\left[\because \int_a^b \frac{f(x) \mathrm{d} x}{f(x)+f(a+b-x)}=\frac{b-a}{2}\right]}\end{aligned}$

</details>

---

### Q89. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_0^2|2 x| \mathrm{d}=$ (where [.] denotes the greatest integer function.)

**Options:**

- **(A)** 4
- **(B)** 3
- **(C)** 2
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3**

**Detailed Solution:**

$\begin{aligned} & \int_0^2[2 x] \mathrm{d} x=\int_0^{1 / 2} 0 \mathrm{~d} x+\int_{\frac{1}{2}}^1 1 \cdot \mathrm{d} x+\int_1^{3 / 2} 2 \mathrm{~d} x+\int_{\frac{3}{2}}^2 3 \mathrm{~d} x \\ & =0+\left(1-\frac{1}{2}\right)+2\left(\frac{3}{2}-1\right)+3\left(2-\frac{3}{2}\right) \\ & =0+\frac{1}{2}+2 \times \frac{1}{2}+3 \times \frac{1}{2}=3\end{aligned}$

</details>

---

### Q90. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{-1 / 2}^{1 / 2} \log \left(\frac{1+x}{1-x}\right) \mathrm{d} x=$

**Options:**

- **(A)** $0$
- **(B)** $\frac{1}{2}$
- **(C)** $-1$
- **(D)** $-\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0$**

**Detailed Solution:**

$\int_{\frac{-1}{2}}^{1 / 2} \log \left(\frac{1+x}{1-x}\right) \mathrm{d} x=0\left[\because \int_{-a}^a f(x) \mathrm{d} x=0\right.$ if $f(x)$ is odd $]$

</details>

---

### Q91. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_{-\pi}^\pi \frac{\cos ^2 x}{1+\alpha^x} \mathrm{~d} x, \alpha>0$ is

**Options:**

- **(A)** $2 \pi$
- **(B)** $\pi$
- **(C)** $\alpha \pi$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{2}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/q28uo6mmC3WxsAegoIuRuzZYSEUqwBwVVGU5JMkhCeA.original.fullsize.png">
from (i)+(ii)
$\begin{aligned} & 2 I=\int_{-\pi}^\pi \frac{\left(1+\alpha^x\right) \cos ^2 x}{\left(1+\alpha^x\right)} \mathrm{d} x=\int_{-\pi}^\pi \cos ^2 x \mathrm{~d} x \\ & \Rightarrow 2 I=2 \int_0^\pi \cos ^2 x \mathrm{~d} x \quad\left[\because \cos ^2(\pi-x)=\cos ^2 x\right] \\ & \Rightarrow I=\int_0^\pi \frac{1+\cos 2 x}{2} \mathrm{~d} x\left[\frac{x}{2}+\frac{\sin 2 x}{4}\right]_0^\pi=\frac{\pi}{2}\end{aligned}$

</details>

---

### Q92. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int_0^1 \frac{1}{\sqrt{3+2 x-x^2}} d x=$

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{\pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{6}$**

**Detailed Solution:**

$\begin{aligned} & \int_0^1 \frac{1}{\sqrt{3+2 x-x^2}} \mathrm{~d} x=\int_0^1 \frac{\mathrm{d} x}{\sqrt{(2)^2-(x-1)^2}}=\left[\sin ^{-1}\left(\frac{x-1}{2}\right)\right]_0^1 \\ & =\sin ^{-1}(0)-\sin ^{-1}\left(\frac{-1}{2}\right)=0-\left(-\frac{\pi}{6}\right)=\frac{\pi}{6}\end{aligned}$

</details>

---

### Q93. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{-1}^1 \log \left(\frac{2-x}{2+x}\right) d x=$

**Options:**

- **(A)** 1
- **(B)** -1
- **(C)** 0
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

$\begin{aligned} & \int_{-1}^1 \log \left(\frac{2-x}{2+x}\right) \mathrm{d} x=0 \\ & \because \log \left(\frac{2-x}{2+x}\right) \text { is an odd function. }\end{aligned}$

</details>

---

### Q94. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{\frac{-\pi}{2}}^{\frac{\pi}{2}} f(x) d x=$
Where $f(x)=\sin |x|+\cos |x|, x \in\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$.

**Options:**

- **(A)** 0
- **(B)** 8
- **(C)** 4
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

$\begin{aligned} & \int_{\frac{-\pi}{2}}^{\frac{\pi}{2}} f(x) d x=\int_{\frac{-\pi}{2}}^{\frac{\pi}{2}}(\sin |x|+\cos |x|) d x \\ & \quad=2 \int_0^{\frac{\pi}{2}}(\sin |x|+\cos |x|) d x \quad[\because \text { even function }] \\ & \quad \frac{\pi}{2} \\ & =2 \int_0(\sin x+\cos x) d x \quad[\because x>0] \\ & =2[-\cos x+\sin x]_0^{\frac{\pi}{2}}=4\end{aligned}$

</details>

---

### Q95. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int_0^1 \sqrt{\frac{1-x}{1+x}} d x$ is

**Options:**

- **(A)** $\left(\frac{\pi}{2}\right)-1$
- **(B)** $-1$
- **(C)** $\left(\frac{\pi}{2}\right)+1$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(\frac{\pi}{2}\right)-1$**

**Detailed Solution:**

$\begin{aligned} & \int_0^1 \sqrt{\frac{1-x}{1+x}} d x=\int_0^1 \frac{1-x}{\sqrt{1-x^2}} d x=\int_0^1 \frac{d x}{\sqrt{1-x^2}}+\int_0^1 \frac{-2 x}{2 \sqrt{1-x^2}} d x \\ & =\left[\sin ^{-1} x\right]_0^1+\left[\sqrt{1-x^2}\right]_0^1 \\ & =\left\{\sin ^{-1}(1)-\sin ^{-1}(0)\right\}+\left\{\sqrt{1-1^2}-\sqrt{1-0^2}\right\} \\ & =\frac{\pi}{2}-0+0-1 \\ & =\frac{\pi}{2}-1\end{aligned}$

</details>

---

### Q96. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\int_0^{\mathrm{k}} \frac{d x}{2+8 x^2}=\frac{\pi}{16}$, then value of $\mathrm{k}$ is

**Options:**

- **(A)** $4$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{1}{4}$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2}$**

**Detailed Solution:**

$\begin{aligned} & \int_0^k \frac{d x}{2+8 x^2}=\frac{\pi}{16} \Rightarrow \frac{1}{2} \int_0^k \frac{d x}{1+(2 x)^2}=\frac{\pi}{16} \\ & \Rightarrow \frac{1}{2}\left[\frac{\tan ^{-1}(2 x)}{2}\right]_0^k=\frac{\pi}{16} \\ & \Rightarrow \tan ^{-1}(2 k)=\frac{\pi}{16} \\ & \Rightarrow 2 k=1 \\ & \Rightarrow k=\frac{1}{2}\end{aligned}$

</details>

---

### Q97. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{\log \frac{1}{2}}^{\log 2} \sin \left(\frac{\mathrm{e}^{\mathrm{x}}-1}{\mathrm{e}^{\mathrm{x}}+1}\right) \mathrm{dx}=$

**Options:**

- **(A)** $2 \log 2$
- **(B)** $-2 \log 2$
- **(C)** $\frac{1}{2}$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

$\begin{aligned} & \int_{\log \frac{1}{2}}^{\log 2} \sin \left(\frac{\mathrm{e}^{\mathrm{x}}-1}{\mathrm{e}^{\mathrm{x}}+1}\right) \mathrm{dx}=\int_{-\log 2}^{\log 2} \sin \left(\frac{\mathrm{e}^{\mathrm{x}}-1}{\mathrm{e}^{\mathrm{x}}+1}\right) \mathrm{dx}=0 \\ & {\left[\because \sin \left(\frac{\mathrm{e}^{\mathrm{x}}-1}{\mathrm{e}^{\mathrm{x}}+1}\right) \text { is an odd function }\right]}\end{aligned}$

</details>

---

### Q98. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\frac{\pi}{2}$
If $\int_0 \frac{\cot x}{\cot x+\operatorname{cosec} x} d x=m(\pi+n)$, then (m.n) equals

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $-1$
- **(C)** $-\frac{1}{2}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-1$**

**Detailed Solution:**

$\begin{aligned} & \int_0^{\frac{\pi}{2}} \frac{\cot x}{\cot x+\operatorname{cosec} x} d x=\int_0^{\frac{\pi}{2}} \frac{\cos x}{\cos x+1} d x \\ & =\int_0^{\frac{\pi}{2}} \frac{2 \cos ^2 \frac{x}{2}-1}{2 \cos ^2 \frac{x}{2}} d x=\int_0^{\frac{\pi}{2}}\left(1-\frac{1}{2} \sec ^2 \frac{x}{2}\right) d x \\ & =\left[x-\tan \frac{x}{2}\right]_0^{\pi / 2}=\frac{\pi}{2}-1=\frac{1}{2}(\pi+(-2)) \\ & \Rightarrow m=\frac{1}{2} \text { and } n=-2 \\ & \Rightarrow \mathrm{m} \times \mathrm{n}=\frac{1}{2} \times(-2)=-1\end{aligned}$

</details>

---

### Q99. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^1 x(1-x)^n d x=$

**Options:**

- **(A)** $\frac{n+3}{(n+1)(n+2)}$
- **(B)** $\frac{1}{(n+1)(n+2)}$
- **(C)** $\frac{2 n+3}{(n+1)(n+2)}$
- **(D)** $\frac{4}{(n+1)(n+2)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{(n+1)(n+2)}$**

**Detailed Solution:**

$\begin{aligned} & \int_0^1 x(1-x)^n d x=\int_0^1(1-x)^n d x\left[\because \int_0^a f(x) d x=\int_0^a f(a-x) d x\right] \\ & =\int_0^1\left(x^n-x^{n+1}\right) d x=\left[\frac{x^{n+1}}{n+1}-\frac{x^{n+2}}{n+2}\right]_0^1 \\ & =\frac{1}{n+1}-\frac{1}{n+2}=\frac{1}{(n+1)(n+2)}\end{aligned}$

</details>

---

### Q100. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\int_a^b x^3 d x=0$ and if $\int_a^b x^2 d x=\frac{2}{3}$, then $a$ and $b$ are respectively

**Options:**

- **(A)** $1,-1$
- **(B)** $-1,-1$
- **(C)** 1,1
- **(D)** -1,1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -1,1**

**Detailed Solution:**

$\begin{aligned} & \int_a^b x^3 d x=0 \text { and } \int_a^b x^2 d x=\frac{2}{3} \\ & \Rightarrow\left[\frac{x^4}{4}\right]_a^b=0 \text { and }\left[\frac{x^3}{3}\right]_a^b=\frac{2}{3} \\ & \Rightarrow \frac{b^4}{4}-\frac{a^4}{4}=0 \text { and } \frac{b^3}{3}-\frac{a^3}{3}=\frac{2}{3} \\ & \Rightarrow a^4=b^4 \text { and } b^3-a^3=2\end{aligned}$
which is satisfied by $\mathrm{a}=-1$ and $\mathrm{b}=1$

</details>

---

### Q101. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $f:[-1,2] \rightarrow[0, \infty)$ be a continuous function such that $f(x)=f(1-x), \forall x \in[-1,2]$. If $R_1=\int_{-1}^2 x f(x) d x$ and $R_2$ is the area of the region bounded by $y=f(x), x=-1, x=2$ and the X-asis. Then

**Options:**

- **(A)** $2 R_1=R_2$
- **(B)** $R_1=3 R_2$
- **(C)** $R_1=2 R_2$
- **(D)** $3 R_1=R_2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 R_1=R_2$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/1o3xycK4b7RE24CnCsO2Y_NVl4kzgjG_MN-E4IftvvM.original.fullsize.png">
$\left[\right.$ as $\int_a^b f(x) d x=\int_a^b f(a+b-x)$ also $\left.f(1-x)=f(x)\right]$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Z-C9xlAMsxFwijufXFhGFeFDlhyNWKIIsaSv0Araau4.original.fullsize.png">
from (iii) and (iv) $2 R_1=R_2$

</details>

---

### Q102. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^\pi x \sin x \cos ^4 x d x=$

**Options:**

- **(A)** $\frac{\pi}{10}$
- **(B)** $\frac{2 \pi}{5}$
- **(C)** $\frac{\pi}{5}$
- **(D)** $\frac{\pi}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{5}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/NxPSCOFgWD6bEriAekOt1egnxRbu5YkAMX2Z1iBqdB8.original.fullsize.png">

$=\int_0^\pi(\pi-x) \sin (\pi-x)[\cos (\pi-x)]^4 d x$<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/rmvqpmPw2lx3Txd1TT79y6LQnzMogbEuzifcu6aPHaE.original.fullsize.png">

Eq. (1) $+(2)$ gives,
$2 I=\int_0^\pi \pi \sin x \cos ^4 x d x$
Eq. (1) $+(2)$ gives,
$2 I=\int_0^\pi \pi \sin x \cos ^4 x d x$
Put $\cos x=t \Rightarrow-\sin x d x=$
When $\mathrm{x}=0, \mathrm{t}=$ and when $\mathrm{x}=\pi, \mathrm{t}=-1$
$2 \mathrm{I}=\pi \int_1^{-1}(\mathrm{t})^4(-\mathrm{dt})$
... ( $\mathrm{t}^4$ is an even function)
$\therefore \quad 2 I=\frac{2 \pi}{5}\left[\mathrm{t}^5\right]_0^1 \Rightarrow \mathrm{I}=\frac{\pi}{5}$

</details>

---

### Q103. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^1|5 x-3| d x=$

**Options:**

- **(A)** $\frac{13}{10}$
- **(B)** 1
- **(C)** $\frac{3}{10}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{13}{10}$**

**Detailed Solution:**

Let $\mathrm{I}=\int_0^1|5 \mathrm{x}-3| \mathrm{dx}$
$$
\begin{aligned}
& 5 x-3=0 \Rightarrow x=\frac{3}{5} \\
& \therefore \quad I=\int_0^{\frac{3}{5}}-(5 x-3) d x+\int_{\frac{3}{5}}^1(5 x-3) d x \\
& =\frac{-5}{2}\left[x^2\right]_0^{\frac{3}{5}}+3[x]_0^{\frac{3}{5}}+\frac{5}{2}\left[x^2\right]_{\frac{3}{5}}^1-3[x]_{\frac{3}{5}}^1 \\
& =\left(\frac{-5}{2}\right)\left(\frac{9}{25}\right)+3\left(\frac{3}{5}\right)+\frac{5}{2}\left(1-\frac{9}{25}\right)-3\left(1-\frac{3}{5}\right) \\
& =\frac{-45}{50}+\frac{9}{5}+\left(\frac{5}{2}\right)\left(\frac{16}{25}\right)-3\left(\frac{2}{5}\right)=\frac{-45}{50}+\frac{3}{5}+\frac{8}{5} \\
& =\frac{-45+110}{50}=\frac{65}{50}=\frac{13}{10}
\end{aligned}
$$

</details>

---

### Q104. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int_0^{\pi / 2} \log \left(\frac{4+3 \sin x}{4+3 \cos x}\right) d x=$

**Options:**

- **(A)** 0
- **(B)** $4 \log 3$
- **(C)** $\frac{1}{2}$
- **(D)** $2 \log 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/PqcqT5n6V_IPbNTi7vPoxsE5PjCSyZOITMObacGbQkU.original.fullsize.png">

Eq. (1) $+(2)$ gives,
$$
2 I=\log \left[\frac{4+3 \sin x}{4+3 \cos x} \times \frac{4+3 \cos x}{4+3 \sin x}\right] d x=\int_0^{\frac{\pi}{2}}(\log 1) d x=0
$$

</details>

---

### Q105. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^4 x[x] d x=($ where $[x]$ denotes greatest integer function not greater than $\mathrm{x}$ )

**Options:**

- **(A)** 17
- **(B)** 24
- **(C)** $\frac{21}{2}$
- **(D)** $\frac{33}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 17**

**Detailed Solution:**

Let $I=\int_0^4 x[x] d x$
$$
\begin{aligned}
& \therefore I=\int_0^1(0) d x+\int_1^2 x d x+\int_2^3 2 x d x+\int_3^4 3 x d x \\
& =\left[\frac{x^2}{2}\right]_1^2+\left[\frac{2 x^2}{2}\right]_2^3+\left[\frac{3 x^2}{2}\right]_3^4 \\
& =\frac{1}{2}(4-1)+(9-4)+\left(\frac{3}{2}\right)(16-9)=\frac{3}{2}+5+\frac{21}{2}=17
\end{aligned}
$$

</details>

---

### Q106. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^2|2 x-3| d x=$

**Options:**

- **(A)** $\frac{3}{10}$
- **(B)** $\frac{5}{2}$
- **(C)** $\frac{10}{3}$
- **(D)** $\frac{2}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{5}{2}$**

**Detailed Solution:**

Let
When $x=\frac{3}{2}, 2 x-3=0$
$$
\begin{aligned}
& \therefore \mathrm{I}=\int_0^{3 / 2}(3-2 \mathrm{x}) \mathrm{dx}+\int_{\frac{3}{2}}^2(2 \mathrm{x}-3) \mathrm{dx}=[3 \mathrm{x}]_0^{3 / 2}-\frac{2}{2}\left[\mathrm{x}^2\right]_{3 / 2}^2-[3 \mathrm{x}]_{3 / 2}^2 \\
& =\left(\frac{9}{2}\right)-\left(\frac{9}{4}\right)+\left(4-\frac{9}{4}\right)-3\left(2-\frac{3}{2}\right)=\frac{5}{2}
\end{aligned}
$$

</details>

---

### Q107. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{-\pi}^\pi \frac{x \sin x}{1+\cos ^2 x} d x=$

**Options:**

- **(A)** $\frac{\pi^2}{2}$
- **(B)** $\pi^2$
- **(C)** $\frac{\pi^2}{4}$
- **(D)** $3 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi^2}{2}$**

**Detailed Solution:**

Let $f(x)=\frac{x \sin x}{1+\cos ^2 x}$
$f(-x)=\frac{(-x) \sin (-x)}{1+\cos ^2 x}=\frac{x \sin x}{1+\cos ^2 x}$
$\therefore \mathrm{f}(\mathrm{x})=\mathrm{f}(-\mathrm{x}) \Rightarrow \mathrm{f}(\mathrm{x})$ is an even function
Let $I=\int_{-\pi}^\pi \frac{x \sin x}{1+\cos ^2 x} d x$
$\therefore \mathrm{I}=2 \int_0^\pi \frac{\mathrm{x} \sin \mathrm{x}}{1+\cos ^2 \mathrm{x}} \mathrm{dx}$
$=2 \int_0^\pi \frac{(\pi-x) \sin (\pi-x)}{1+[\cos (\pi-x)]^2} d x=2 \int_0^\pi \frac{(\pi-x) \sin x}{1+\cos ^2 x} d x$
Eq. (1) $+(2)$ gives,
$$
2 I=2 \pi \int_0^\pi \frac{\sin x}{1+\cos ^2 \mathrm{x}}
$$
Put $\cos x=t \Rightarrow \sin x d x=-d t$. Also when $x=0, t=1$ and when
$$
\begin{aligned}
& \mathrm{x}=\pi, \mathrm{t}=-1 \\
& \therefore 2 \mathrm{I}=2 \pi \int_1^{-1} \frac{-\mathrm{dt}}{1+\mathrm{t}^2} \\
& =2 \pi \int_{-1}^1 \frac{\mathrm{dt}}{1+\mathrm{t}^2}=4 \pi \int_0^1 \frac{\mathrm{dt}}{1+\mathrm{t}^2}=4 \pi\left[\tan ^{-1}\right]_0^2=4 \pi\left(\frac{\pi}{4}\right)=\pi^2 \\
& \therefore \mathrm{I}=\frac{\pi^2}{2}
\end{aligned}
$$

</details>

---

### Q108. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int_0^1 \tan ^{-1}\left(\frac{2 x-1}{1+x-x^2}\right) d x$ is

**Options:**

- **(A)** 2
- **(B)** -1
- **(C)** 1
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

$\begin{aligned} & \text { Let } I=\int_0^1 \tan ^{-1}\left(\frac{2 x-1}{1+x-x^2}\right) d x \\ & =\int_0^1 \tan ^{-1}\left[\frac{x+(x-1)}{1+x(1-x)}\right] d x=\int_0^1 \tan ^{-1}\left[\frac{x+(x-1)}{1-(x-1)(x)}\right] d x \\ & =\int_0^1\left[\tan ^{-1} x+\tan ^{-1}(x-1) d x=\int_0^1 \tan ^{-1} x d x+\int_0^1 \tan ^{-1}(x-1) d x\right. \\ & \left.=\left[\left[x \tan ^{-1} x\right]_0^1-\frac{1}{2} \int_0^1 \frac{2 x}{1+x^2} d x\right]+\left[x \tan ^{-1}(x-1)\right]_0^1-\frac{1}{2} \int_0^1 \frac{2 x-2+2}{1+(x-1)^2} d x\right] \\ & =\left(\frac{\pi}{4}\right)-\frac{1}{2}\left[\log \left|1+x^2\right|\right]_0^1+0-\frac{1}{2} \int_0^1 \frac{2 x-2}{1+(x-1)^2} d x-\int_0^1 \frac{d x}{1+(x-1)^2} \\ & =\left(\frac{\pi}{4}\right)-\frac{1}{2} \log 2-\frac{1}{2}\left[\log \left|1+(x-1)^2\right|\right]_0^1-\left[\tan ^{-1}(x-1)\right]_0^1 \\ & =\frac{\pi}{4}-\frac{1}{2} \log 2-\frac{1}{2}(0-\log 2)-\left[0-\tan ^{-1}(-1)\right] \\ & =\frac{\pi}{4}-\frac{1}{2} \log 2+\frac{1}{2} \log 2-\frac{\pi}{4}=0\end{aligned}$

</details>

---

### Q109. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{\frac{-\pi}{2}}^{\frac{\pi}{2}} \frac{\cos x}{1+e^x} d x=$

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** -1
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/2dXOSTHlxEygs-dxxZdz9OeiMOzWCPTNEqhwZtHly1M.original.fullsize.png">

</details>

---

### Q110. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_5^{10} \frac{d x}{(x-1)(x-2)}=$

**Options:**

- **(A)** $\log \left|\frac{27}{32}\right|$
- **(B)** $\log \left|\frac{3}{4}\right|$
- **(C)** $\log \left|\frac{8}{9}\right|$
- **(D)** $\log \left|\frac{32}{27}\right|$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log \left|\frac{32}{27}\right|$**

**Detailed Solution:**

$\begin{aligned} & I=\int_5^{10} \frac{d x}{(x-1)(x-2)} \\ & =\int_5^{10}\left[\frac{1}{x-1}-\frac{1}{x-2}\right](-1) d x=-\int_5^{10}\left[\frac{1}{x-1}-\frac{1}{x-2}\right] d x \\ & =-[\log |x-1|]_5^{10}+[\log |x-2|]_5^{10}=-[\log |9|-\log |4|]+[\log |8|-\log |3|] \\ & =\left[\log \left|\frac{8}{3}\right|\right]-\left[\log \left|\frac{9}{4}\right|\right]=\log \left|\frac{8}{3} \times \frac{9}{4}\right|=\log \left|\frac{32}{27}\right|\end{aligned}$

</details>

---

### Q111. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(\mathrm{x})=|\mathrm{x}-1|+|\mathrm{x}-2|+|\mathrm{x}-3|, \forall \mathrm{x} \in[1,4]$, then $\int_1^4 \mathrm{f}(\mathrm{x}) \mathrm{dx}=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** 7
- **(C)** $\frac{9}{2}$
- **(D)** $\frac{19}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{19}{2}$**

**Detailed Solution:**

$$
\begin{aligned}
& \int_1^4 f(x) d x=\int_1^4[|x-1|+|x-2|+|x-3| d x \\
& =\int_1^2(x-1)+(2-x)+(3-x) d x+\int_2^3[(x-1)+(x-2)+(3-x)] d x \\
& +\int_3^4[(x-1)+(x-2)+(x-3)] d x \\
& =\int_1^2(4-x) d x+\int_2^3 x d x+\int_3^4(3 x-6) d x
\end{aligned}
$$


$$
\begin{aligned}
& =\left[4 x-\frac{x^2}{2}\right]_1^2+\left[\frac{x^2}{2}\right]_2^3+\left[\frac{3 x^2}{2}-6 x\right]_3^4 \\
& =\left[(8-2)-\left(4-\frac{1}{2}\right)\right]+\left[\left(\frac{9}{2}-2\right)\right]+\left[(24-24)-\left(\frac{27}{2}-18\right)\right] \\
& =\left(2+\frac{1}{2}\right)+\left(\frac{5}{2}\right)+\left(\frac{9}{2}\right)=\frac{19}{2}
\end{aligned}
$$

</details>

---

### Q112. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int_0^{\pi / 4} \log (1+\tan x) d x=$

**Options:**

- **(A)** $\frac{\pi}{16} \log 2$
- **(B)** $\frac{\pi}{4} \log 2$
- **(C)** $\frac{\pi}{8} \log 2$
- **(D)** $\pi \log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{8} \log 2$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } I=\int_0^{\pi / 4} \log (1+\tan x) d x \\ & =\int_0^{\pi / 4} \log \left[1+\tan \left(\frac{\pi}{4}-x\right)\right] d x \\ & =\int_0^{\pi / 4} \log \left[1+\left(\frac{1-\tan x}{1+\tan x}\right)\right] d x=\int_0^{\pi / 4} \log \left(\frac{2}{1+\tan x}\right) d x \\ & =\int_0^{\pi / 4}(\log 2) d x-\int_0^{\pi / 4} \log (1+\tan x) d x=\int_0^{\pi / 4}(\log 2) d x-I \\ & \therefore 2 I=(\log 2)[x]_0^{\pi / 4}=(\log 2)\left(\frac{\pi}{4}\right) \Rightarrow I=\left(\frac{\pi}{8}\right) \log 2\end{aligned}$

</details>

---

### Q113. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{-8}^{8} \frac{x^{5}+x^{3}}{4-x^{2}} d x=$

**Options:**

- **(A)** 16
- **(B)** 0
- **(C)** 8
- **(D)** $-8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0**

**Detailed Solution:**

Let $\quad I=\int_{-8}^{8} \frac{x^{5}+x^{3}}{4-x^{2}} d x$
Let $f(x)=\frac{x^{5}+x^{3}}{4-x^{2}} \Rightarrow f(-x)=\frac{-\left(x^{5}+x^{3}\right)}{4-x^{2}}$
$\therefore \quad \mathrm{f}(-\mathrm{x})=-\mathrm{f}(\mathrm{x}) \Rightarrow \mathrm{I}=0$

</details>

---

### Q114. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0}^{\pi} \frac{e^{\cos x}}{\left(e^{\cos x}+e^{-\cos x)}\right.} d x=$

**Options:**

- **(A)** $\frac{-\pi}{2}$
- **(B)** $-\pi$
- **(C)** $\pi$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{2}$**

**Detailed Solution:**

$$
\text { Let } \begin{aligned}
I &=\int_{0}^{\pi} \frac{e^{\cos x}}{e^{\cos x}+e^{-\cos x} d x}...(1) \\
&=\int_{0}^{\pi} \frac{e^{\cos (\pi-x)}}{e^{\cos (\pi-x)}+e^{-\cos (\pi-x)}} d x \\
&=\int_{0}^{\pi} \frac{e^{-\cos x}}{e^{-\cos x}+e^{\cos x} d x}...(2)
\end{aligned}
$$
Adding equation (1) \& (2), we get
$$
2 I=\int_{0}^{\pi} 1 d x=[x]_{0}^{\pi} \Rightarrow I=\frac{\pi}{2}
$$

</details>

---

### Q115. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int_{0}^{1} \tan ^{-1}\left(\frac{2 x-1}{1+x-x^{2}}\right) d x=$

**Options:**

- **(A)** 1
- **(B)** 4
- **(C)** 2
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

(A)
$\int_{0}^{1} \tan ^{-1}\left(\frac{2 x-1}{1+x-x^{2}}\right) d x$
$=\int_{0}^{1} \tan ^{-1}\left[\frac{x-(1-x)}{1+x(1-x)}\right] d x=\int_{0}^{1}\left[\tan ^{-1} x-\tan ^{-1}(1-x)\right] d x$...(1)
$=\int_{0}^{1}\left[\tan ^{-1}(1-x)-\tan ^{-1}(1-(1-x))\right] d x=\int_{0}^{1}\left[\tan ^{-1}(1-x)-\tan ^{-1}(x)\right] d x$...(2)
Adding (1) \& (2), we get
$2 I=0 \Rightarrow I=0$

</details>

---

### Q116. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0}^{\frac{\pi}{2}} \frac{\sqrt[7]{\sin x}}{\sqrt[7]{\sin x}+\sqrt[7]{\cos x}} d x=$

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{\pi}{3}$
- **(C)** $\frac{\pi}{4}$
- **(D)** $\frac{\pi}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{4}$**

**Detailed Solution:**

(D)
$I=\int_{0}^{\frac{\pi}{2}} \frac{\sqrt[7]{\sin x}}{\sqrt[7]{\sin x}+\sqrt[7]{\cos x}}$...(1)
$=\int_{0}^{\frac{\pi}{2}} \frac{\sqrt{\sin \left(\frac{\pi}{2}-x\right)}}{\sqrt{\sin \left(\frac{\pi}{2}-x\right)+\sqrt{\cos \left(\frac{\pi-x}{2}\right)}} \mathrm{dx}}$
$I=\int_{0}^{r / 2} \frac{\sqrt[7]{\cos x}}{\sqrt[7]{\cos x}+\sqrt[7]{\sin x}} d x$...(2)
Equation $(1)-(2)$ gives
$\begin{aligned}
2 I &=\int_{0}^{\frac{\pi}{2}} 1 d x=[x]_{0}^{\frac{\pi}{2}}=\frac{\pi}{2} \\
\therefore I &=\frac{\pi}{4}
\end{aligned}$

</details>

---

### Q117. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{-5}^{5} \log \left(\frac{7-x}{7+x}\right) d x=$

**Options:**

- **(A)** 5
- **(B)** 0
- **(C)** -5
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0**

**Detailed Solution:**

(B)
Let $1=\int_{-4}^{5} \log \frac{7-x}{7+x}$
Let $\quad f(x)=\log \frac{7-x}{7+x}$
$f(-x)=\log \left[\frac{7-(-x)}{7+(-x)}\right]=\log \left(\frac{7+x}{7-x}\right)=-\log \left(\frac{7-x}{7+x}\right)=-f(x)$
$\therefore f(x)$ is an odd function $\Rightarrow I=0$

</details>

---

### Q118. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{\frac{\pi}{5}}^{\frac{3 \pi}{10}}\left[\frac{\tan x}{\tan x+\cot x}\right] d x=$

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{3 \pi}{10}$
- **(C)** $\frac{\pi}{5}$
- **(D)** $\frac{\pi}{20}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{20}$**

**Detailed Solution:**

(C)
$\begin{array}{l}
\int_{\frac{\pi}{5}}^{\frac{3 \pi}{10}}\left[\frac{\tan x}{\tan x+\cot x}\right] d x...(1)
\\
=\int_{\frac{\pi}{5}}^{\frac{3 \pi}{10}}\left[\frac{\tan \left(\frac{3 \pi}{10}+\frac{\pi}{5}-x\right)+\cot \left(\frac{3 \pi}{10}+\frac{\pi}{5}-x\right)}{\tan \left(\frac{3 \pi}{10}+\frac{\pi}{5}-x\right)}\right] d x=\int_{\frac{\pi}{5}}^{10} \frac{3 \pi}{\tan \left(\frac{\pi}{2}-x\right)+\cot \left(\frac{\pi}{2}-x\right)} \tan \left(\frac{\pi}{2}-x\right) \\
=\int_{\frac{\pi}{5}}^{\frac{3 \pi}{10}} \frac{\tan x+\cot x} d x...(2)
\end{array}$
Equation (1) + (2) gives
$\begin{aligned} 2 I &=\int_{\frac{\pi}{5}}^{\frac{3 \pi}{10}} d x=[x]_{\frac{\pi}{5}}^{\frac{3 \pi}{10}}=\left(\frac{3 \pi}{10}-\frac{\pi}{5}\right)=\frac{\pi}{10} \\ \therefore I &=\frac{\pi}{20} \end{aligned}$

</details>

---

### Q119. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{-4}^{4} \log \left(\frac{8-x}{8+x}\right) d x=$

**Options:**

- **(A)** $-4$
- **(B)** 8
- **(C)** 4
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

$\begin{aligned} \text { Let } f(x) &=\log (8-x)-\log (8+x) \\ f(-x) &=\log (8+x)-\log (8-x) \\ &=-[\log (8-x)-\log (8+x)] \\ \text { Thus } f(-x) &=-f(x) \Rightarrow I=0 \end{aligned}$

</details>

---

### Q120. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{0}^{1} \frac{x^{2}}{1+x^{2}} d x=$

**Options:**

- **(A)** $1+\frac{\pi}{4}$
- **(B)** $1-\frac{\pi}{4}$
- **(C)** $1-\frac{\pi}{2}$
- **(D)** $1+\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1-\frac{\pi}{4}$**

**Detailed Solution:**

Let $\begin{aligned} I &=\int_{0}^{1} \frac{x^{2}}{1+x^{2}} d x=\int_{0}^{1} \frac{\left(1+x^{2}\right)-1}{1+x^{2}} d x=\int_{0}^{1}\left(\frac{1+x^{2}}{1+x^{2}}-\frac{1}{1+x^{2}}\right) d x=\int_{0}^{1}\left(1-\frac{1}{1+x^{2}}\right) d x \\ &=\left[x-\tan ^{-1} x\right]_{0}^{1}=1-\frac{\pi}{4} \end{aligned}$

</details>

---

### Q121. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0}^{\frac{\pi}{2}}\left(e^{\sin x}-e^{\cos x}\right) d x=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $0$
- **(C)** $1$
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0$**

**Detailed Solution:**

$$
\text { Let } \begin{aligned}
I &=\int_{0}^{\frac{\pi}{2}}\left(e^{\sin x}-e^{\cos x}\right) d x ....(1)\\
&=\int_{0}^{\pi / 2} e^{\sin \left(\frac{\pi}{2}-x\right)}-e^{\cos \left(\frac{\pi}{2}-x\right)} \mathrm{dx} \\
&=\int_{0}^{\pi / 2} e^{\cos x}-e^{\sin x} d x....(2)
\end{aligned}
$$
Adding equation (1) \& (2) we get
$$
\begin{array}{l}
2 I=\int_{0}^{\pi / 2}\left(e^{\sin x}-e^{\cos x}-e^{\cos x}-e^{\sin x}\right) d x \\
2 I=0 \Rightarrow I=0
\end{array}
$$

</details>

---

### Q122. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$$
\int_{-1}^{1}\left[\sqrt{1+x+x^{2}}-\sqrt{1-x+x^{2}}\right] d x=
$$

**Options:**

- **(A)** 2
- **(B)** 5
- **(C)** 1
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

Given I $=\int_{-1}^{1}\left(\sqrt{1+x+x^{2}}-\sqrt{1-x+x^{2}}\right) d x$
Let $f(x)=\sqrt{1+x+x^{2}}-\sqrt{1-x+x^{2}}$
$\therefore f(-x)=\sqrt{1-x+x^{2}}-\sqrt{1+x+x^{2}}=-\left(\sqrt{1+x+x^{2}}-\sqrt{1-x-x^{2}}\right)=-f(x)$
$\therefore I=0$

</details>

---

### Q123. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$$\int_{0}^{\pi} \frac{x \cos x \cdot \sin x}{\cos ^{3} x+\cos x} d x=$$

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi^{2}}{4}$
- **(C)** $\frac{\pi}{8}$
- **(D)** $\frac{\pi^{2}}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{8}$**

**Detailed Solution:**

Let I $=\int_{0}^{\pi} \frac{x \cos x \sin x}{\cos ^{3} x+\cos x} d x$
$\quad=\int_{0}^{\pi} \frac{x \sin x}{\cos ^{2} x+1} d x$
$\quad=\int_{0}^{\pi} \frac{(\pi-x) \sin x}{\cos ^{2} x+1} d x=\int_{0}^{\pi} \frac{\pi \sin x}{\cos ^{2} x+1} d x-\int_{0}^{\pi} \frac{x \sin x}{\cos ^{2} x+1} d x$
$\quad=\int_{0}^{\pi} \frac{\pi \sin x}{\cos ^{2} x+1} d x-I$
$2 I=\int_{0}^{\pi} \frac{\pi \sin x}{\cos ^{2} x+1} d x$
Put $\cos x=t=\sin d x=-d t$
When $x=0, t=1$ and when $x=\pi, t=-1$
$2 I=-\int_{1}^{-1} \frac{\pi d t}{1+t^{2}}=\pi \int_{-1}^{1} \frac{d t}{1+t^{2}}=2 \pi \int_{0}^{1} \frac{d t}{1+t^{2}}$
$2 I=2 \pi\left[\tan ^{-1} t\right]_{0}^{1}=2 \pi\left(\frac{\pi}{4}\right)=\left(\frac{\pi^{2}}{2}\right)$
$\therefore \frac{\pi^{2}}{4}$

</details>

---

### Q124. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{-\pi}^{\pi} \frac{2 x}{1+\cos ^{2} x} d x=$

**Options:**

- **(A)** $\pi$
- **(B)** $0$
- **(C)** $1$
- **(D)** $-\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0$**

**Detailed Solution:**

Let $f(x)=\frac{2 x}{1+\cos ^{2} x} \Rightarrow f(-x)=\frac{-2 x}{1+\cos ^{2} x}$
Thus $\mathrm{f}(-\mathrm{x})=-\mathrm{f}(\mathrm{x}) \Rightarrow \mathrm{I}=0$

</details>

---

### Q125. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{0}^{\frac{\pi}{2}} \frac{\sqrt[3]{\sec x}}{\sqrt[3]{\sec x}+\sqrt[3]{\operatorname{cosec} x}} d x=$

**Options:**

- **(A)** 0
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{2}$
- **(D)** $\frac{-\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{4}$**

**Detailed Solution:**

Let
$\begin{aligned} I &=\int_{0}^{\frac{\pi}{2}} \frac{\sqrt[3]{\sec x}}{\sqrt[3]{\sec x}+\sqrt[3]{\operatorname{cosec} x}} \mathrm{dx} ...(1) \\ &=\int_{0}^{\frac{\pi}{2}} \frac{\sqrt[3]{\sec \left(\frac{\pi}{2}-x\right)} \sqrt{\sec \left(\frac{\pi}{2}-x\right)+\sqrt[3]{\operatorname{cosec}\left(\frac{\pi}{2}-x\right)}}}{\sqrt[3]{\frac{\pi}{2}}} d x \\ \therefore \text { I }=& \int_{0}^{\frac{\pi}{2}} \frac{\sqrt[3]{\sec x}+\sqrt[3]{\operatorname{cosec} x}} d x ...(2) \end{aligned}$
Adding equation (1) \& (2), we get
$2 I=\int_{0}^{\frac{\pi}{2}} 1 d x=[x]_{0}^{\frac{\pi}{2}} \Rightarrow 2 I=\frac{\pi}{2}-0 \Rightarrow I=\frac{\pi}{4}$

</details>

---

### Q126. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0}^{\frac{\pi}{2}} \frac{1-\cot x}{\operatorname{cosec} x+\cos x} d x=$

**Options:**

- **(A)** 0
- **(B)** $\frac{\pi}{2}$
- **(C)** 1
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

$\text { Let } \begin{aligned}
I &=\int_{0}^{\frac{\pi}{2}} \frac{1-\cot x}{\operatorname{cosec} x+\cos x} d x \\
I &=\int_{0}^{\frac{\pi}{2}} \frac{1-\frac{\cos x}{\sin x}}{\frac{1}{\sin x}+\cos x} d x=\int_{0}^{\frac{\pi}{2}} \frac{\sin x-\cos x}{1+\sin x \cos x} d x ...(1)\\
I &=\int_{0}^{\frac{\pi}{2}} \frac{\sin \left(\frac{\pi}{2}-x\right)-\cos \left(\frac{\pi}{2}-x\right)}{1+\sin \left(\frac{\pi}{x}-x\right) \cos \left(\frac{\pi}{2}-x\right)} d x \\
I &=\int_{0}^{\frac{\pi}{2}} \frac{\cos x-\sin x}{1+\cos x \sin x} d x ...(2)
\end{aligned}$
Adding equations (1) \& (2), we get
$\begin{array}{l}
2 I=\int_{0}^{\frac{\pi}{2}} \frac{\sin x-\cos x+\cos x-\sin x}{1+\sin x \cos x} d x \\
2 I=0 \Rightarrow I=0
\end{array}$

</details>

---

### Q127. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int_{0}^{1} \tan ^{-1}\left[\frac{2 x-1}{1+x-x^{2}}\right] d x=$

**Options:**

- **(A)** 0
- **(B)** $\frac{\pi}{6}$
- **(C)** 1
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Let 
$\begin{aligned} I &=\int_{0}^{1} \tan ^{-1}\left[\frac{2 x-1}{1+x-x^{2}}\right] d x \\ &=\int_{0}^{1} \tan ^{-1}\left[\frac{2 x-1}{1+x(1-x)}\right] d x=\int_{0}^{1} \tan ^{-1}\left[\frac{x-(1-x)}{1+x(1-x)}\right] d x \\ &=\int_{0}^{1}\left[\tan ^{-1} x-\tan ^{-1}(1-x)\right] d x ...(1) \\ &=\int_{0}^{1}\left\{\tan ^{-1}(1-x)-\tan ^{-1}[1-(1-x)]\right\} d x \\ &=\int_{0}^{1}\left[\tan ^{-1}(1-x)-\tan ^{-1} x\right] d x ...(2) \\ \text { Equation }(1)+(2) \operatorname{gives} \\ 2 I=0 \Rightarrow I=0 \end{aligned}$

</details>

---

### Q128. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0}^{\frac{\pi}{2}} \frac{\sin ^{\frac{2}{3}} x}{\sin ^{\frac{2}{3}} x+\cos ^{\frac{2}{3}} x} d x=$

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{8}$
- **(C)** $\frac{\pi}{2}$
- **(D)** $\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{4}$**

**Detailed Solution:**

$\begin{aligned} I &=\int_{0}^{\frac{\pi}{2}} \frac{\sin ^{\frac{2}{3}} x}{\sin ^{\frac{2}{3}} x+\cos ^{\frac{2}{3}} x} d x ...(1)\\ &=\int_{0}^{\frac{\pi}{2}} \frac{\sin ^{\frac{2}{3}}\left(\frac{\pi}{2}-x\right)}{\sin ^{\frac{2}{3}}\left(\frac{\pi}{2}-x\right)+\cos ^{\frac{2}{3}}\left(\frac{\pi}{2}-x\right)} d x \\ \therefore I &=\int_{0}^{2} \frac{\cos ^{\frac{2}{3}} x}{\sin ^{\frac{2}{3}} x+\cos ^{\frac{2}{3}} x} d x ...(2) \end{aligned}$
Adding equation (1) \& (2) we get
$\begin{aligned}
2 I &=\int_{0}^{2} 1 d x \Rightarrow 2 I=[x]_{0}^{\frac{\pi}{2}} \\
I &=\frac{1}{2}\left(\frac{\pi}{2}-0\right)=\frac{\pi}{4}
\end{aligned}$

</details>

---

### Q129. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$$
\int_{-a}^{a} x^{2}\left(\frac{e^{x^{3}}-e^{-x^{3}}}{e^{x^{3}}+e^{-x^{3}}}\right) d x=
$$

**Options:**

- **(A)** $a^{2}$
- **(B)** 0
- **(C)** $a$
- **(D)** $2 \int_{0}^{a} x^{2}\left(\frac{e^{x^{3}}-e^{-x^{3}}}{e^{x^{3}}+e^{-x^{3}}}\right) d x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0**

**Detailed Solution:**

Let
$\begin{aligned}
f(x) &=x^{2}\left[\frac{e^{x^{3}}-e^{-x^{3}}}{e^{x^{3}}+e^{-x^{3}}}\right]=x^{2}\left[\frac{e^{x^{3}}-\frac{1}{e^{x^{3}}}}{e^{x^{3}}+\frac{1}{e^{x^{3}}}}\right]=x^{2}\left[\frac{\left(e^{x^{3}}\right)^{2}-1}{\left(e^{x^{3}}\right)^{2}+1}\right] \\
f(-x) &=(-x)^{2}\left[\frac{e^{-x^{3}}-e^{x^{3}}}{e^{-x^{3}}+e^{x^{3}}}\right]
\end{aligned}$
$=x^{2}\left[\frac{\frac{1}{e^{x^{3}}}-e^{x^{3}}}{\frac{1}{e^{x^{3}}}+e^{x^{3}}}\right]=x^{2}\left[\frac{1-\left(e^{x^{3}}\right)^{2}}{1+\left(e^{x^{3}}\right)^{2}}\right]=-x^{2}\left[\frac{\left(e^{x^{3}}\right)^{2}-1}{1+\left(e^{x^{3}}\right) 2}\right]=-f(x)$
Thus $f(-x)=-f(x) \Rightarrow$ Given function is an odd function.
$\therefore \quad I=0$

</details>

---

### Q130. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{\frac{-\pi}{2}}^{\frac{\pi}{2}} \sin ^{2} x d x=$

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{3}$
- **(C)** $\frac{\pi}{2}$
- **(D)** $\frac{3 \pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{2}$**

**Detailed Solution:**

Let $f(x)=\sin ^{2} x$
$\therefore \mathrm{f}(-\mathrm{x})=[\sin (-\mathrm{x})]^{2}=\sin ^{2} \mathrm{x}$
Thus $\sin ^{2} x$ is an even function.
$\therefore \int_{\frac{-\pi}{2}}^{\frac{\pi}{2}} \sin ^{2} x d x=2 \int_{0}^{\frac{\pi}{2}} \sin ^{2} x d x$
$=2 \int_{0}^{\frac{\pi}{2}} \frac{1}{2}(1-\cos 2 x) d x=\left[x-\frac{\sin 2 x}{2}\right]_{0}^{\frac{\pi}{2}}$
$=\left(\frac{\pi}{2}-0\right)-\left(\frac{\sin \pi}{2}-\frac{\sin 0}{2}\right)=\frac{\pi}{2}$

</details>

---

### Q131. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{0}^{a}(a-x)^{\frac{3}{2}} \cdot x^{2} d x=$

**Options:**

- **(A)** $\frac{-16 a^{\frac{9}{2}}}{315}$
- **(B)** $\frac{16 a^{\frac{9}{2}}}{315}$
- **(C)** $\frac{16 a^{\frac{7}{2}}}{315}$
- **(D)** $\frac{-16 a^{\frac{7}{2}}}{315}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{16 a^{\frac{9}{2}}}{315}$**

**Detailed Solution:**

Let 
$\begin{aligned} I &=\int_{0}^{a}(a-x)^{\frac{3}{2}} x^{2} d x \\ &=\int_{0}^{a}[a-(a-x)]^{\frac{3}{2}}(a-x)^{2} d x \\ &=\int_{0}^{a} x^{\frac{3}{2}}\left(a^{2}-2 a x+x^{2}\right) d x=\int_{0}^{a}\left(a^{2} x^{\frac{3}{2}}-2 a x^{\frac{5}{2}}+x^{\frac{7}{2}}\right)_{d x} \\ &=a^{2}\left[\frac{x^{\frac{5}{2}}}{\frac{5}{2}}\right]_{0}^{a}-2 a\left[\frac{x^{\frac{7}{2}}}{\frac{7}{2}}\right]_{0}^{a}+\left[\frac{x^{\frac{9}{2}}}{\frac{9}{2}}\right]_{0}^{a} \\ &=\frac{2 a^{2}}{5}\left[a^{\frac{5}{2}}-0\right]-2 a \times \frac{2}{7}\left[a^{\frac{7}{2}}-0\right]+\frac{2}{9}\left[a^{\frac{9}{2}}-0\right]=\frac{2}{5} a^{\frac{9}{2}}-\frac{4}{7} a^{\frac{9}{2}}+\frac{2}{9} a^{\frac{9}{2}} \\ &=a^{\frac{9}{2}}\left[\frac{2}{5}-\frac{4}{7}+\frac{2}{9}\right]=\frac{16}{315} a^{\frac{9}{2}} \end{aligned}$

</details>

---

### Q132. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{-5}^{5}\left[\frac{e^{x}+e^{-x}}{e^{x}-e^{-x}}\right] d x=$

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** $3 e^{5}$
- **(D)** $2 e^{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

$\begin{aligned}
\text { Let } f(x)=& \frac{e^{x}+e^{-x}}{e^{x}-e^{-x}} \\
=& \frac{e^{x}+\frac{1}{e^{x}}}{e^{x}-\frac{1}{e^{x}}}=\frac{e^{2 x}+1}{e^{2 x}-1} \text { and } f(-x)=\frac{e^{-x}+e^{x}}{e^{-x}-e^{x}}=\frac{\frac{1}{e^{x}}+e^{x}}{\frac{1}{e^{x}}-e^{x}}=\frac{1+e^{2 x}}{1-e^{2 x}} \\
\therefore f(x)=-f(x)
\end{aligned}$
Thus $f(x)$ is an odd function.
$\therefore \int_{-5}^{5} \frac{e^{x}+e^{-x}}{e^{x}-e^{-x}} d x=0$

</details>

---

### Q133. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the body cools from $135^{\circ} \mathrm{C}$ to $80^{\circ} \mathrm{C}$ at room temperature of $25^{\circ} \mathrm{C}$ in 60 minutes,
then the temperature of body after 2 hours is

**Options:**

- **(A)** $(52.5)^{\circ} \mathrm{C}$
- **(B)** $(10.5)^{\circ} \mathrm{C}$
- **(C)** $(52.75)^{\circ} \mathrm{C}$
- **(D)** $(10.75)^{\circ} \mathrm{C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(52.5)^{\circ} \mathrm{C}$**

**Detailed Solution:**

Let $\theta^{\circ} \mathrm{C}$ be the temperature of the body at time $\mathrm{t}$ min. Room temp is given $25^{\circ} \mathrm{C}$ Then by Newton's law of cooling, we write
$\begin{aligned}
& \frac{\mathrm{d} \theta}{\mathrm{dt}} \propto(\theta-25) \Rightarrow \frac{\mathrm{d} \theta}{\mathrm{dt}}=-\mathrm{k}(\theta-25) \\
\therefore & \int \frac{\mathrm{d} \theta}{\theta-25}=\int-\mathrm{kdt} \\
& \log (\theta-25)=-\mathrm{kt}+\mathrm{c} ...(1) \\
\text { Initially when } \mathrm{t}=0, \theta=135 \\
\therefore & \log (135-25)=0+\mathrm{c} \Rightarrow \mathrm{c}=\log 110 \\
& \log (\theta-25)=-\mathrm{kt}+\log 110 \\
\therefore & \log \left(\frac{\theta-25}{110}\right)=-\mathrm{kt} ...(2)
\end{aligned}$
Now when $t=60, \theta=80$
$\begin{array}{l}
\text { w when } t=60, \theta=80 \\
\log \left(\frac{55}{110}\right)=-60 k \Rightarrow k=-\frac{1}{60} \log \left(\frac{1}{2}\right)
\end{array}$
From (2) $\log \left(\frac{\theta-25}{110}\right)=\frac{t}{60} \log \left(\frac{1}{2}\right)$
At $t=120$, we get $$ \log \left(\frac{\theta-25}{110}\right)=2 \log \frac{1}{2} \Rightarrow \log \left(\frac{\theta-25}{110}\right)=\log \left(\frac{1}{4}\right) $$ $\therefore \frac{\theta-25}{110}=\frac{1}{4} \Rightarrow 4 \theta-100=110 \Rightarrow 4 \theta=210 \Rightarrow \theta=52.5^{\circ} \mathrm{C}$

</details>

---

### Q134. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math><mrow><munderover><mo stretchy="false">∫</mo><mrow><mo>-</mo><mn>3</mn></mrow><mrow><mn>3</mn></mrow></munderover><mrow><mfenced separators="|"><mrow><mi>a</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup><mo>+</mo><mi>b</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mi>c</mi><mi>x</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>,</mo></mrow></mrow></math> where <math><mi>a</mi><mo>,</mo><mi></mi><mi>b</mi><mo>,</mo><mi></mi><mi>c</mi><mo>,</mo><mi></mi><mi>k</mi></math> are constants, depends only on ________

**Options:**

- **(A)** <math><mi>a</mi><mo>,</mo><mi></mi><mi>b</mi></math> and <math><mi>c</mi></math>
- **(B)** <math><mi>k</mi></math>
- **(C)** <math><mi>a</mi></math> and <math><mi>b</mi></math>
- **(D)** <math><mi>a</mi></math> and <math><mi>k</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi>k</mi></math>**

**Detailed Solution:**

Let <math><mi>I</mi><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mo>-</mo><mn>3</mn></mrow><mrow><mn>3</mn></mrow></msubsup><mrow><mfenced separators="|"><mrow><mi>a</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup><mo>+</mo><mi>b</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mi>c</mi><mi>x</mi><mo>+</mo><mi>k</mi></mrow></mfenced></mrow></mrow><mi>d</mi><mi>x</mi></math>  
Where, <math><mi>a</mi><mo>,</mo><mi></mi><mi>b</mi><mo>,</mo><mi></mi><mi>c</mi></math> and <math><mi>k</mi></math> are constants. 
<math><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mo>-</mo><mn>3</mn></mrow><mrow><mn>3</mn></mrow></msubsup><mrow><mfenced separators="|"><mrow><mi>a</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup><mo>+</mo><mi>b</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mi>c</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mo>-</mo><mn>3</mn></mrow><mrow><mn>3</mn></mrow></msubsup><mrow><mi>k</mi><mi>d</mi><mi>x</mi></mrow></mrow></mrow></mrow></math>  
( <math><mo>∵</mo></math> <math><mi>a</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup><mo>+</mo><mi>b</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mi>c</mi><mi>x</mi></math> is an odd function) 
<math><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>0</mn><mo>+</mo><mn>2</mn><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>3</mn></mrow></msubsup><mrow><mi>k</mi><mi>d</mi><mi>x</mi></mrow></mrow></math>

</details>

---

### Q135. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mrow><munderover><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mi>a</mi></mrow></munderover><mrow><msqrt><mfrac><mrow><mi>a</mi><mo>-</mo><mi>x</mi></mrow><mrow><mi>x</mi></mrow></mfrac></msqrt><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>K</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow></math> , then K = ….

**Options:**

- **(A)** <math><mfrac><mrow><mi>π</mi><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>5</mn><mi>π</mi><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>3</mn><mi>π</mi><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mi>π</mi><mi>a</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi>π</mi><mi>a</mi></math>**

**Detailed Solution:**

We have, <math><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mi>a</mi></mrow></msubsup><mrow><msqrt><mfrac><mrow><mi>a</mi><mo>-</mo><mi>x</mi></mrow><mrow><mi>x</mi></mrow></mfrac></msqrt><mi>d</mi><mi>x</mi></mrow></mrow><mo>=</mo><mfrac><mrow><mi>k</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>  
Let <math><mi>l</mi><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mi>a</mi></mrow></msubsup><mrow><msqrt><mfrac><mrow><mi>a</mi><mo>-</mo><mi>x</mi></mrow><mrow><mi>x</mi></mrow></mfrac></msqrt><mi>d</mi><mi>x</mi></mrow></mrow></math>  
Put <math><mi>x</mi><mo>=</mo><mi>a</mi><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></math>  
<math><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mi>a</mi><mfenced separators="|"><mrow><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mrow></mfenced><mi>d</mi><mi>θ</mi></math>  
When, <math><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>θ</mi><mo>=</mo><mn>0</mn><mi></mi><mi>a</mi><mi>n</mi><mi>d</mi><mi></mi><mi>x</mi><mo>=</mo><mi>a</mi><mo>,</mo><mi>θ</mi><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>  
<math><mo>∴</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mi>π</mi><mo>/</mo><mn>2</mn></mrow></munderover><mrow><msqrt><mfrac><mrow><mi>a</mi><mo>-</mo><mi>a</mi><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></mrow><mrow><mi>a</mi><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></mrow></mfrac></msqrt><mfenced separators="|"><mrow><mn>2</mn><mi>a</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mrow></mfenced><mi>d</mi><mi>θ</mi></mrow></mrow><mo>=</mo><mn>2</mn><mi>a</mi><mi></mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mrow><mrow><mi>π</mi></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></munderover><mrow><mo>(</mo><mi>c</mi><mi>o</mi><mi>t</mi><mi>θ</mi><mo>)</mo><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mrow></mfenced><mi>d</mi><mi>θ</mi></mrow></mrow></math>  
<math><mo>=</mo><mn>2</mn><mi>a</mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mrow><mrow><mi>π</mi></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></munderover><mrow><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi><mi>d</mi><mi>θ</mi><mi></mi></mrow></mrow><mo>=</mo><mn>2</mn><mi>a</mi><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mrow><mrow><mi>π</mi></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msubsup><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>θ</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mi>d</mi><mi>θ</mi></mrow></mrow></math>  
<math><mo>=</mo><mi>a</mi><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mrow><mrow><mi>π</mi></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msubsup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>θ</mi></mrow></mfenced></mrow></mrow><mi>d</mi><mi>θ</mi></math>  
<math><mo>=</mo><mi>a</mi><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>θ</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mrow><mrow><mi>π</mi></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msubsup><mo>=</mo><mi>a</mi><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>π</mi><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>  
<math><mo>∴</mo><mi>k</mi><mo>=</mo><mi>π</mi><mi>a</mi></math>

</details>

---

### Q136. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<math><mrow><munderover><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mi>x</mi><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>5</mn></mrow></msup></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mo>…</mo><mo>…</mo><mo>.</mo></math>

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>42</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>13</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>42</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>42</mn></mrow></mfrac></math>**

**Detailed Solution:**

Let = <math><mi>l</mi><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup><mrow><mi>x</mi><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>5</mn></mrow></msup><mi>d</mi><mi>x</mi></mrow></mrow></math>  
Put <math><mn>1</mn><mo>-</mo><mi>x</mi><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>-</mo><mi>t</mi></math>  
<math><mo>&#8658;</mo><mo>-</mo><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math>  
<math><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mo>-</mo><mi>d</mi><mi>t</mi></math> 
When <math><mi>x</mi><mo>=</mo><msup><mrow><mn>0</mn></mrow><mrow><mi>'</mi></mrow></msup><mo>,</mo></math> then <math><mi>t</mi><mo>=</mo><mn>1</mn></math> and 
When <math><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>t</mi><mi>h</mi><mi>e</mi><mi>n</mi><mi></mi><mi>t</mi><mo>=</mo><mn>0</mn></math>  
<math><mo>∴</mo><mi>l</mi><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>1</mn></mrow><mrow><mn>0</mn></mrow></msubsup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced></mrow><mrow><mn>5</mn></mrow></msup><mfenced separators="|"><mrow><mo>-</mo><mi>d</mi><mi>t</mi></mrow></mfenced><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>t</mi></mrow><mrow><mn>5</mn></mrow></msup><mo>-</mo><msup><mrow><mi>t</mi></mrow><mrow><mn>6</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>t</mi></mrow></mrow></mrow></mrow></math>  
<math><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>t</mi></mrow><mrow><mn>6</mn></mrow></msup></mrow><mrow><mn>6</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi>t</mi></mrow><mrow><mn>7</mn></mrow></msup></mrow><mrow><mn>7</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>7</mn></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></mrow><mrow><mn>7</mn></mrow></msup></math>  
<math><mo>=</mo><mfrac><mrow><mn>7</mn><mo>-</mo><mn>6</mn></mrow><mrow><mn>42</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>42</mn></mrow></mfrac></math>

</details>

---

### Q137. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<math><mrow><munderover><mo stretchy="true">∫</mo><mrow><mi>a</mi></mrow><mrow><mi>b</mi></mrow></munderover><mrow><mfrac><mrow><msqrt><mi>x</mi></msqrt></mrow><mrow><msqrt><mi>x</mi></msqrt><mo>+</mo><msqrt><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=.........</mo></mrow></mrow></math>

**Options:**

- **(A)** <math><mi>a</mi><mo>+</mo><mi>b</mi></math>
- **(B)** <math><mfrac><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mi>a</mi><mo>-</mo><mi>b</mi></math>
- **(D)** <math><mfrac><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

Let <math><mi>l</mi><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mi>a</mi></mrow><mrow><mi>b</mi></mrow></msubsup><mrow><mfrac><mrow><msqrt><mi>x</mi></msqrt></mrow><mrow><mi>a</mi><msqrt><mi>x</mi></msqrt><mo>+</mo><msqrt><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></msqrt></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi></math> ….(i) 
<math><mi>l</mi><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mi>a</mi></mrow><mrow><mi>b</mi></mrow></msubsup><mrow><mfrac><mrow><msqrt><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></msqrt></mrow><mrow><msqrt><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></msqrt><mo>+</mo><msqrt><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced></msqrt></mrow></mfrac></mrow></mrow></math>  
<math><mi>l</mi><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mi>a</mi></mrow><mrow><mi>b</mi></mrow></msubsup><mrow><mfrac><mrow><msqrt><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></msqrt></mrow><mrow><msqrt><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></msqrt><mo>+</mo><msqrt><mi>x</mi></msqrt></mrow></mfrac></mrow></mrow></math> ….(ii) 
On adding Eqs. (i) and (ii), we get 
<math><mn>2</mn><mi>l</mi><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mi>a</mi></mrow><mrow><mi>b</mi></mrow></msubsup><mrow><mfrac><mrow><msqrt><mi>x</mi></msqrt><mo>+</mo><msqrt><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></msqrt></mrow><mrow><msqrt><mi>x</mi></msqrt><mo>+</mo><msqrt><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></msqrt></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi></math>  
<math><mo>&#8658;</mo><mn>2</mn><mi>l</mi><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mi>a</mi></mrow><mrow><mi>b</mi></mrow></msubsup><mrow><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mrow><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mi>a</mi></mrow><mrow><mi>b</mi></mrow></msubsup><mo>=</mo><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mrow></math>  
<math><mo>&#8658;</mo><mi>l</mi><mo>=</mo><mfrac><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>

</details>

---

### Q138. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `1`

If <math><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mi>k</mi></mrow></munderover><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>2</mn><mo>+</mo><mn>18</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>24</mn></mrow></mfrac></mrow></mrow></math> , then the value of <math><mi>k</mi></math> is

**Options:**

- **(A)** <math><mn>3</mn></math>
- **(B)** <math><mn>4</mn></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math> <mrow> <mfrac> <mn>1</mn> <mn>2</mn> </mfrac> <mstyle displaystyle="true"> <mrow><munderover> <mo>∫</mo> <mn>0</mn> <mi>k</mi> </munderover> <mrow> <mfrac> <mrow> <mi>d</mi><mi>x</mi></mrow> <mrow> <mn>1</mn><mo>+</mo><mn>9</mn><msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </mrow> </mstyle><mo>=</mo><mfrac> <mi>π</mi> <mrow> <mn>24</mn></mrow> </mfrac> </mrow> </math>
<math> <mo>&rArr;</mo><mrow> <mstyle displaystyle="true"> <mrow><munderover> <mo>∫</mo> <mn>0</mn> <mi>k</mi> </munderover> <mrow> <mfrac> <mrow> <mi>d</mi><mi>x</mi></mrow> <mrow> <mn>1</mn><mo>+</mo><msup> <mrow> <mrow><mo>(</mo> <mrow> <mn>3</mn><mi>x</mi></mrow> <mo>)</mo></mrow></mrow> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </mrow> </mstyle><mo>=</mo><mfrac> <mi>π</mi> <mrow> <mn>12</mn></mrow> </mfrac> </mrow> </math>
<math> <mo>&rArr;</mo><mrow> <msubsup> <mrow> <mrow><mo>(</mo> <mrow> <mfrac> <mn>1</mn> <mn>3</mn> </mfrac> <msup> <mrow> <mi>tan</mi></mrow> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> <mrow><mo>(</mo> <mrow> <mn>3</mn><mi>x</mi></mrow> <mo>)</mo></mrow></mrow> <mo>)</mo></mrow></mrow> <mn>0</mn> <mi>k</mi> </msubsup> <mo>=</mo><mfrac> <mi>π</mi> <mrow> <mn>12</mn></mrow> </mfrac> </mrow> </math>
<math> <mo>&rArr;</mo><mrow> <msup> <mrow> <mi>tan</mi></mrow> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> <mn>3</mn><mi>k</mi><mo>=</mo><mfrac> <mi>π</mi> <mn>4</mn> </mfrac> </mrow> </math>
<math> <mo>&rArr;</mo><mrow> <mn>3</mn><mi>k</mi><mo>=</mo><mn>1</mn></mrow> </math>
<math> <mo>&rArr;</mo><mrow> <mi>k</mi><mo>=</mo><mfrac> <mn>1</mn> <mn>3</mn> </mfrac> </mrow> </math>

</details>

---

### Q139. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

<math><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>3</mn></mrow></munderover><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mo>_</mo><mo>_</mo><mo>_</mo><mo>_</mo><mo>_</mo><mo>_</mo><mo>,</mo></mrow></mrow></math> where <math><mo>[</mo><mi>x</mi><mo>]</mo></math> is greatest integer function

**Options:**

- **(A)** <math > <mn>3</mn></math>
- **(B)** <math > <mn>0</mn></math>
- **(C)** <math > <mn>2</mn></math>
- **(D)** <math > <mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math > <mn>3</mn></math>**

**Detailed Solution:**

<math><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>3</mn></mrow></munderover><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced><mi> </mi><mi>d</mi><mi>x</mi><mo>=</mo></mrow></mrow><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mn>0</mn><mi> </mi><mi>d</mi><mi>x</mi><mo>+</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></munderover><mrow><mn>1</mn><mi> </mi><mi>d</mi><mi>x</mi></mrow></mrow></mrow></mrow><mo>+</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></munderover><mrow><mn>2</mn><mi> </mi><mi>d</mi><mi>x</mi></mrow></mrow></math>
<math><mo>=</mo><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><mn>2</mn><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></msubsup></math>
<math><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><mn>2</mn></mrow></mfenced></math>
<math><mo>=</mo><mn>1</mn><mo>+</mo><mn>2</mn></math>
<math><mo>=</mo><mn>3</mn></math>

</details>

---

### Q140. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int_{0}^{\pi} \log (1+\cos x) d x$ is

**Options:**

- **(A)** $-\frac{\pi}{2} \log 2$
- **(B)** $\pi \log \frac{1}{2}$
- **(C)** $\pi \log 2$
- **(D)** $\frac{\pi}{2} \log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\pi \log \frac{1}{2}$**

**Detailed Solution:**

Let $\begin{aligned} I &=\int_{0}^{\pi} \log (1+\cos x) d x...(i) \\ I &=\int_{0}^{\pi} \log \{1+\cos (\pi-x)\} d x \\ &=\int_{0}^{\pi} \log (1-\cos x) d x...(ii) \end{aligned}$
On adding Eqs. (i) and (ii), we get $\begin{aligned} 2 I &=\int_{0}^{\pi}\{\log (1+\cos x)+\log (1-\cos x)\} d x \\ I &=\frac{1}{2} \int_{0}^{\pi} \log \left(1-\cos ^{2} x\right) d x \\ &=\frac{1}{2} \int_{0}^{\pi} \log \sin ^{2} x d x \\ &=\int_{0}^{\pi} \log \sin x d x \\ &=2 \int_{0}^{\pi / 2} \log \sin x d x \end{aligned}$
$\begin{aligned}\left\{\because \int_{0}^{2 a} f(x) d x=2 \int_{0}^{a} f(x) d x,\right.\\ &\text { if } f(2 a-x)=f(x)\} \\=2\left\{-\frac{\pi}{2} \log 2\right\} \\\left(\because \int_{0}^{\pi / 2} \log \sin x d x=-\frac{\pi}{2} \log 2\right) \\=\pi \log \frac{1}{2} \end{aligned}$

</details>

---

### Q141. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0}^{\pi / 2} \frac{d x}{1+\tan x}$ is equal to

**Options:**

- **(A)** $\pi$
- **(B)** $\pi / 2$
- **(C)** $\pi / 3$
- **(D)** $\pi / 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\pi / 4$**

**Detailed Solution:**

Given, $I=\int_{0}^{\pi / 2} \frac{d x}{1+\tan x}$
$$
\begin{array}{rlr}
I & =\int_{0}^{\pi / 2} \frac{\cos x}{\sin x+\cos x} d x & \ldots \\
I & =\int_{0}^{\pi / 2} \frac{\cos (\pi / 2-x)}{\sin (\pi / 2-x)+\cos (\pi / 2-x)} d x \\
& =\int_{0}^{\pi / 2} \frac{\sin x}{\cos x+\sin x} d x & \ldots
\end{array}
$$
On adding Eqs. (i) and (ii), we get
$$
\begin{aligned}
2 I &=\int_{0}^{\pi / 2}\left(\frac{\sin x+\cos x}{\sin x+\cos x}\right) d x \\
&=\int_{0}^{\pi / 2} d x=\pi / 2 \\
\Rightarrow \quad I &=\pi / 4
\end{aligned}
$$

</details>

---

### Q142. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

$\int_{-\pi / 2}^{-\pi / 2} \frac{\cos x}{1+e^{x}} d x$ is equal to

**Options:**

- **(A)** 1
- **(B)** 0
- **(C)** $-1$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

$I=\int_{-\pi / 2}^{\pi / 2} \frac{\cos x}{1+e^{x}} d x$
$$
\begin{aligned}
I &=\int_{-\pi / 2}^{\pi / 2} \frac{\cos (\pi / 2-\pi / 2-x)}{1+e^{(\pi / 2-\pi / 2-x)}} d x \\
&=\int_{-\pi / 2}^{\pi / 2} \frac{\cos (-x)}{1+e^{-x}} d x \\
I &=\int_{-\pi / 2}^{\pi / 2} \frac{\cos x}{1+e^{-x}} d x \\
&=\int_{-\pi / 2}^{\pi / 2} \frac{e^{x} \cos x}{1+e^{x}} d x
\end{aligned}
$$
On adding Eqs. (i) and (ii), we get
$$
\begin{aligned}
2 I &=\int_{-\pi / 2}^{\pi / 2} \frac{\left(1+e^{x}\right) \cos x}{\left(1+e^{x}\right)} d x \\
&=\int_{-\pi / 2}^{\pi / 2} \cos x d x \\
&=2 \int_{0}^{\pi / 2} \cos x d x
\end{aligned}
$$
[Since, $\cos x$ is an even function.]
$$
\therefore \quad 2 I=2[\sin x]_{0}^{\pi / 2}=2(1-0)=2
$$
$$
\Rightarrow \quad I=1
$$

</details>

---

### Q143. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

The value of $\int_{4}^{7} \frac{(11-x)^{2}}{x^{2}+(11-x)^{2}} d x$ is

**Options:**

- **(A)** 1
- **(B)** $1 / 2$
- **(C)** $3 / 2$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3 / 2$**

**Detailed Solution:**

Let
$$
\begin{aligned}
I &=\int_{4}^{7} \frac{(11-x)^{2}}{x^{2}+(11-x)^{2}} d x \\
&=\int_{4}^{7} \frac{x^{2}}{(11-x)^{2}+x^{2}} d x
\end{aligned}
$$
On adding Eqs. (i) and (ii), we get
$$
2 I=\int_{4}^{7} 1 d x=[x]_{4}^{7}=3
$$
$$
\Rightarrow \quad I=\frac{3}{2}
$$

</details>

---

### Q144. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int_{0}^{\pi / 2} \log (\operatorname{cosec} x) d x$ is

**Options:**

- **(A)** $\frac{\pi}{2} \log 2$
- **(B)** $\pi \log 2$
- **(C)** $-\frac{\pi}{2} \log 2$
- **(D)** $2 \pi \log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{2} \log 2$**

**Detailed Solution:**

Let $\quad I=\int_{0}^{\pi / 2} \log (\operatorname{cosec} x) d x$
$=\int_{0}^{\pi / 2} \log \left(\frac{1}{\sin x}\right) d x$
$=-\int_{0}^{\pi / 2} \log \sin x d x$
$=\frac{\pi}{2} \log 2$
$\left[\because \int_{0}^{\pi / 2} \log \sin x d x=-\frac{\pi}{2} \log 2\right]$

</details>

---

### Q145. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0}^{\pi / 2} \frac{\sin x-\cos x}{1-\sin x \cdot \cos x} d x$ is equal to

**Options:**

- **(A)** 0
- **(B)** $\frac{\pi}{2}$
- **(C)** $\frac{\pi}{4}$
- **(D)** $\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Let $I=\int_{0}^{\pi / 2} \frac{\sin x-\cos x}{1-\sin x \cos x} d x$
On putting $x=\left(\frac{\pi}{2}-x\right)$ in Eq. (i), we get
$$
\begin{aligned}
I &=\int_{0}^{\pi / 2} \frac{\sin \left(\frac{\pi}{2}-x\right)-\cos \left(\frac{\pi}{2}-x\right)}{1-\sin \left(\frac{\pi}{2}-x\right) \cos \left(\frac{\pi}{2}-x\right)} d x \\
&=\int_{0}^{\pi / 2} \frac{\cos x-\sin x}{1-\sin x \cos x} d x \\
&=-\int_{0}^{\pi / 2}\left(\frac{\sin x-\cos x}{1-\sin x \cos x}\right) d x
\end{aligned}
$$
On adding Eqs. (i) and (ii), we get
$$
2 I=\int_{0}^{\pi / 2} 0 d x=0
$$
$\Rightarrow \quad I=0$

</details>

---

### Q146. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_{0}^{\pi} x \sin ^{3} x d x$ is

**Options:**

- **(A)** $\frac{4 \pi}{3}$
- **(B)** $\frac{2 \pi}{3}$
- **(C)** 0
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2 \pi}{3}$**

**Detailed Solution:**

Let $I=\int_{0}^{\pi} x \sin ^{3} x d x$ ...(i)
Also, $I=\int_{0}^{\pi}(\pi-x) \sin ^{3} x d x$ ...(ii)
On adding Eqs. (i) and (ii), we get
$$
\begin{aligned}
2 I &=\pi \int_{0}^{\pi} \sin ^{3} x d x \\
&=\frac{\pi}{4} \int_{0}^{\pi}(3 \sin x-\sin 3 x) d x \\
&=\frac{\pi}{4}\left[-3 \cos x+\frac{\cos 3 x}{3}\right]_{0}^{\pi} \\
&=\frac{\pi}{4}\left[3-\frac{1}{3}+3-\frac{1}{3}\right]=\frac{4 \pi}{3} \\
\text { Hence, } I &=\frac{2 \pi}{3}
\end{aligned}
$$

</details>

---

