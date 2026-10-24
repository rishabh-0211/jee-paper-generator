# MHT CET Mathematics - Definite Integration

## Topic 2: Definite Integration by Substitution

**Total Questions:** 59

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_1^2 \dfrac{1}{x(1 + \log x)^2}\,dx$ is.......

**Options:**

- **(A)** $\dfrac{\log 2}{1 - \log 2}$
- **(B)** $\dfrac{\log 2}{1 + \log 2}$
- **(C)** $\dfrac{\log 2}{-1 + \log 2}$
- **(D)** $\dfrac{-\log 2}{1 + \log 2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\log 2}{1 + \log 2}$**

**Detailed Solution:**

Let $1 + \log x = t$

Differentiating both sides, we get $\dfrac{1}{x} dx = dt$

When $x = 1$, $t = 1 + \log 1 = 1$

When $x = 2$, $t = 1 + \log 2$

The integral becomes $\int_{1}^{1+\log 2} \dfrac{1}{t^2} dt$

$= \left[ -\dfrac{1}{t} \right]_{1}^{1+\log 2}$

$= -\dfrac{1}{1+\log 2} - (-1)$

$= 1 - \dfrac{1}{1+\log 2}$

$= \dfrac{1 + \log 2 - 1}{1 + \log 2}$

$= \dfrac{\log 2}{1 + \log 2}$

Answer: $\dfrac{\log 2}{1 + \log 2}$

</details>

---

### Q2. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int_{8}^{15} \dfrac{dx}{(x - 3)\sqrt{x + 1}}$ is....

**Options:**

- **(A)** $\dfrac{1}{2}\log\dfrac{5}{3}$
- **(B)** $\dfrac{1}{3}\log\dfrac{5}{3}$
- **(C)** $\dfrac{1}{2}\log\dfrac{3}{5}$
- **(D)** $\dfrac{1}{5}\log\dfrac{3}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{2}\log\dfrac{5}{3}$**

**Detailed Solution:**

Let $x + 1 = t^2$, which gives $dx = 2t dt$.

When $x = 8$, $t = 3$.

When $x = 15$, $t = 4$.

Substituting these into the integral, we get:

$I = \int_{3}^{4} \dfrac{2t dt}{(t^2 - 4)t}$

$I = 2 \int_{3}^{4} \dfrac{dt}{t^2 - 2^2}$

Using the standard formula $\int \dfrac{dx}{x^2 - a^2} = \dfrac{1}{2a} \log \left| \dfrac{x - a}{x + a} \right|$, we have:

$I = 2 \left[ \dfrac{1}{2(2)} \log \left| \dfrac{t - 2}{t + 2} \right| \right]_{3}^{4}$

$I = \dfrac{1}{2} \left[ \log \left| \dfrac{t - 2}{t + 2} \right| \right]_{3}^{4}$

$I = \dfrac{1}{2} \left( \log \dfrac{2}{6} - \log \dfrac{1}{5} \right)$

$I = \dfrac{1}{2} \left( \log \dfrac{1}{3} - \log \dfrac{1}{5} \right)$

$I = \dfrac{1}{2} \log \dfrac{5}{3}$

Answer: $\dfrac{1}{2}\log\dfrac{5}{3}$

</details>

---

### Q3. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\displaystyle\int_0^4\sqrt{\dfrac{4-x}{4+x}}\,dx=$

**Options:**

- **(A)** $2\pi-4$
- **(B)** $2\pi+4$
- **(C)** $2\pi-2$
- **(D)** $2\pi+2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2\pi-4$**

**Detailed Solution:**

Let $I = \displaystyle\int_0^4\sqrt{\dfrac{4-x}{4+x}}\,dx$

Substitute $x = 4\cos\theta$, which gives $dx = -4\sin\theta \, d\theta$.

When $x = 0$, $\theta = \dfrac{\pi}{2}$ and when $x = 4$, $\theta = 0$.

$I = \displaystyle\int_{\pi/2}^0 \sqrt{\dfrac{4-4\cos\theta}{4+4\cos\theta}} (-4\sin\theta) \, d\theta$

$I = \displaystyle\int_0^{\pi/2} \sqrt{\dfrac{1-\cos\theta}{1+\cos\theta}} (4\sin\theta) \, d\theta$

Using $1-\cos\theta = 2\sin^2\left(\dfrac{\theta}{2}\right)$ and $1+\cos\theta = 2\cos^2\left(\dfrac{\theta}{2}\right)$:

$I = \displaystyle\int_0^{\pi/2} \dfrac{\sin(\theta/2)}{\cos(\theta/2)} \left(8\sin\left(\dfrac{\theta}{2}\right)\cos\left(\dfrac{\theta}{2}\right)\right) \, d\theta$

$I = \displaystyle\int_0^{\pi/2} 8\sin^2\left(\dfrac{\theta}{2}\right) \, d\theta$

$I = \displaystyle\int_0^{\pi/2} 4(1-\cos\theta) \, d\theta$

$I = 4\left[\theta - \sin\theta\right]_0^{\pi/2}$

$I = 4\left(\dfrac{\pi}{2} - 1\right) = 2\pi - 4$

Answer: $2\pi-4$

</details>

---

### Q4. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of integral $\int_0^\infty \dfrac{1}{1 + e^x}\,dx$ is...

**Options:**

- **(A)** $\log 2$
- **(B)** $\log\left(\dfrac{2}{e}\right)$
- **(C)** $-\log e$
- **(D)** $\log\left(\dfrac{4}{e}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\log 2$**

**Detailed Solution:**

Let $I = \int_0^\infty \dfrac{1}{1 + e^x} dx$

Multiplying the numerator and the denominator by $e^{-x}$:

$I = \int_0^\infty \dfrac{e^{-x}}{e^{-x} + 1} dx$

Let $e^{-x} + 1 = t$

Differentiating both sides, $-e^{-x} dx = dt \Rightarrow e^{-x} dx = -dt$

Limits of integration:

When $x = 0$, $t = e^0 + 1 = 2$

When $x \to \infty$, $t = e^{-\infty} + 1 = 1$

Substituting these into the integral:

$I = \int_2^1 \dfrac{-dt}{t} = \int_1^2 \dfrac{dt}{t}$

$I = [\log t]_1^2 = \log 2 - \log 1 = \log 2$

Answer: $\log 2$

</details>

---

### Q5. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)$ is an antiderivative of $\dfrac{x + 1}{\sqrt{x - 1}}$ with respect to $x$, then value of $f(5) - f(2)$ is...

**Options:**

- **(A)** $4$
- **(B)** $\dfrac{14}{3}$
- **(C)** $7$
- **(D)** $\dfrac{26}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{26}{3}$**

**Detailed Solution:**

$f(x) = \int \dfrac{x + 1}{\sqrt{x - 1}} dx$

$f(x) = \int \dfrac{x - 1 + 2}{\sqrt{x - 1}} dx$

$f(x) = \int \left( \sqrt{x - 1} + \dfrac{2}{\sqrt{x - 1}} \right) dx$

$f(x) = \dfrac{2}{3}(x - 1)^{3/2} + 4(x - 1)^{1/2} + C$

$f(5) = \dfrac{2}{3}(4)^{3/2} + 4(4)^{1/2} + C = \dfrac{16}{3} + 8 + C = \dfrac{40}{3} + C$

$f(2) = \dfrac{2}{3}(1)^{3/2} + 4(1)^{1/2} + C = \dfrac{2}{3} + 4 + C = \dfrac{14}{3} + C$

$f(5) - f(2) = \dfrac{40}{3} - \dfrac{14}{3} = \dfrac{26}{3}$

Answer: $\dfrac{26}{3}$

</details>

---

### Q6. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the definite integral $\int_0^{\log_e 5}\dfrac{e^x\sqrt{e^x-1}}{e^x+3}\,dx$ is equal to...

**Options:**

- **(A)** $5 + \pi$
- **(B)** $5 - \pi$
- **(C)** $4 + \pi$
- **(D)** $4 - \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4 - \pi$**

**Detailed Solution:**

Let $e^x - 1 = t^2$, which gives $e^x dx = 2t dt$.

When $x = 0$, $t = 0$.

When $x = \log_e 5$, $t = 2$.

The integral becomes:

$I = \int_0^2 \dfrac{t}{t^2 + 1 + 3} (2t dt) = \int_0^2 \dfrac{2t^2}{t^2 + 4} dt$

$I = 2 \int_0^2 \dfrac{t^2 + 4 - 4}{t^2 + 4} dt$

$I = 2 \int_0^2 \left( 1 - \dfrac{4}{t^2 + 4} \right) dt$

$I = 2 \left[ t - 4 \times \dfrac{1}{2} \tan^{-1} \left( \dfrac{t}{2} \right) \right]_0^2$

$I = 2 \left[ 2 - 2 \tan^{-1}(1) \right]$

$I = 2 \left( 2 - 2 \times \dfrac{\pi}{4} \right)$

$I = 4 - \pi$

Answer: $4 - \pi$

</details>

---

### Q7. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of the definite integral $\int_0^{\pi}\dfrac{1}{5 + 4\cos x}\, dx$ is equal to ...

**Options:**

- **(A)** $\pi$
- **(B)** $\dfrac{\pi}{2}$
- **(C)** $\dfrac{\pi}{3}$
- **(D)** $\dfrac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{\pi}{3}$**

**Detailed Solution:**

Let $I = \int_0^{\pi}\dfrac{1}{5 + 4\cos x}\, dx$

Using the half-angle substitution $\cos x = \dfrac{1 - \tan^2(x/2)}{1 + \tan^2(x/2)}$ and $dx = \dfrac{2\, dt}{1 + t^2}$ where $t = \tan(x/2)$

The limits change from $x = 0 \rightarrow \pi$ to $t = 0 \rightarrow \infty$

$I = \int_0^{\infty} \dfrac{1}{5 + 4\left(\dfrac{1 - t^2}{1 + t^2}\right)} \dfrac{2\, dt}{1 + t^2}$

$I = \int_0^{\infty} \dfrac{2\, dt}{5(1 + t^2) + 4(1 - t^2)}$

$I = \int_0^{\infty} \dfrac{2\, dt}{9 + t^2}$

$I = 2 \left[ \dfrac{1}{3} \tan^{-1}\left(\dfrac{t}{3}\right) \right]_0^{\infty}$

$I = \dfrac{2}{3} \left( \dfrac{\pi}{2} - 0 \right) = \dfrac{\pi}{3}$

Answer: $\dfrac{\pi}{3}$

</details>

---

### Q8. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\displaystyle\int_0^{\log 5} \dfrac{e^x\sqrt{e^x - 1}}{e^x + 3}\,dx =$

**Options:**

- **(A)** $2 - \dfrac{\pi}{4}$
- **(B)** $4 - \dfrac{\pi}{4}$
- **(C)** $2 - \pi$
- **(D)** $4 - \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4 - \pi$**

**Detailed Solution:**

Let $e^x - 1 = t^2$. Differentiating both sides, we get $e^x dx = 2t dt$.

When $x = 0$, $t^2 = e^0 - 1 = 0 \Rightarrow t = 0$.

When $x = \log 5$, $t^2 = e^{\log 5} - 1 = 5 - 1 = 4 \Rightarrow t = 2$.

The denominator becomes $e^x + 3 = (t^2 + 1) + 3 = t^2 + 4$.

Substituting these into the integral, we get:

$\displaystyle\int_0^{\log 5} \dfrac{\sqrt{e^x - 1}}{e^x + 3} (e^x dx) = \int_0^2 \dfrac{t}{t^2 + 4} (2t dt)$

$= \displaystyle\int_0^2 \dfrac{2t^2}{t^2 + 4} dt$

$= 2 \displaystyle\int_0^2 \dfrac{t^2 + 4 - 4}{t^2 + 4} dt$

$= 2 \displaystyle\int_0^2 \left( 1 - \dfrac{4}{t^2 + 4} \right) dt$

$= 2 \left[ t - 4 \left( \dfrac{1}{2} \tan^{-1} \left( \dfrac{t}{2} \right) \right) \right]_0^2$

$= 2 \left[ t - 2 \tan^{-1} \left( \dfrac{t}{2} \right) \right]_0^2$

$= 2 \left[ \left( 2 - 2 \tan^{-1}(1) \right) - (0 - 0) \right]$

$= 2 \left( 2 - 2 \left( \dfrac{\pi}{4} \right) \right)$

$= 4 - \pi$

Answer: $4 - \pi$

</details>

---

### Q9. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^{\log 10}\left[\dfrac{e^x \sqrt{e^x - 1}}{e^x + 8}\right]dx = $

**Options:**

- **(A)** $\dfrac{3}{2}(4 + \pi)$
- **(B)** $\dfrac{3}{2}(4 - \pi)$
- **(C)** $\dfrac{3}{4}(4 - \pi)$
- **(D)** $\dfrac{3}{4}(4 + \pi)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{3}{2}(4 - \pi)$**

**Detailed Solution:**

Let $e^x - 1 = t^2$, then $e^x dx = 2t dt$.

When $x = 0$, $t = 0$.

When $x = \log 10$, $t = 3$.

Substituting these into the integral, we get:

$I = \int_0^3 \dfrac{t}{t^2 + 1 + 8} (2t dt)$

$I = 2 \int_0^3 \dfrac{t^2}{t^2 + 9} dt$

$I = 2 \int_0^3 \left( 1 - \dfrac{9}{t^2 + 9} \right) dt$

$I = 2 \left[ t - 3 \tan^{-1} \left( \dfrac{t}{3} \right) \right]_0^3$

$I = 2 \left[ 3 - 3 \tan^{-1}(1) \right]$

$I = 2 \left( 3 - \dfrac{3\pi}{4} \right)$

$I = \dfrac{3}{2}(4 - \pi)$

Answer: $\dfrac{3}{2}(4 - \pi)$

</details>

---

### Q10. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int_{2}^{e}\left[\dfrac{1}{\log x} - \dfrac{1}{(\log x)^2}\right] dx = a + \dfrac{b}{\log 2}$, then values of $a$ and $b$ are

**Options:**

- **(A)** $a = e, b = 2$
- **(B)** $a = -e, b = 2$
- **(C)** $a = e, b = -2$
- **(D)** $a = -e, b = -2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $a = e, b = -2$**

**Detailed Solution:**

Let $I = \int_{2}^{e}\left[\dfrac{1}{\log x} - \dfrac{1}{(\log x)^2}\right] dx$

Using integration by parts on the first term:

$\int \dfrac{1}{\log x} dx = \dfrac{x}{\log x} - \int x \left( -\dfrac{1}{(\log x)^2} \right) \dfrac{1}{x} dx = \dfrac{x}{\log x} + \int \dfrac{1}{(\log x)^2} dx$

Therefore, $\int \left[ \dfrac{1}{\log x} - \dfrac{1}{(\log x)^2} \right] dx = \dfrac{x}{\log x}$

Evaluating the definite integral from $2$ to $e$:

$I = \left[ \dfrac{x}{\log x} \right]_{2}^{e} = \dfrac{e}{\log e} - \dfrac{2}{\log 2} = e - \dfrac{2}{\log 2}$

Comparing this with $a + \dfrac{b}{\log 2}$, we get $a = e$ and $b = -2$.

Answer: $a = e, b = -2$

</details>

---

### Q11. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int_{0}^{k} \dfrac{1}{1 + 4^x} dx = \log_2\left(\dfrac{4}{3}\right)$, then $k = $ _____

**Options:**

- **(A)** $\dfrac{2}{\sqrt{3}}$
- **(B)** $\dfrac{3}{2}$
- **(C)** $\dfrac{\sqrt{3}}{2}$
- **(D)** $\dfrac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{3}{2}$**

**Detailed Solution:**

Let $I = \int_{0}^{k} \dfrac{1}{1 + 4^x} dx$

Substitute $4^x = t \Rightarrow x \ln 4 = \ln t \Rightarrow dx = \dfrac{dt}{t \ln 4}$

When $x = 0$, $t = 1$. When $x = k$, $t = 4^k$.

$I = \int_{1}^{4^k} \dfrac{1}{1 + t} \dfrac{dt}{t \ln 4} = \dfrac{1}{\ln 4} \int_{1}^{4^k} \left( \dfrac{1}{t} - \dfrac{1}{1 + t} \right) dt$

$I = \dfrac{1}{\ln 4} \left[ \ln t - \ln(1 + t) \right]_{1}^{4^k} = \dfrac{1}{\ln 4} \left[ \ln \left( \dfrac{t}{1 + t} \right) \right]_{1}^{4^k}$

$I = \dfrac{1}{2 \ln 2} \left( \ln \left( \dfrac{4^k}{1 + 4^k} \right) - \ln \left( \dfrac{1}{2} \right) \right) = \dfrac{1}{2 \ln 2} \ln \left( \dfrac{2 \cdot 4^k}{1 + 4^k} \right)$

Given $I = \log_2\left(\dfrac{4}{3}\right) = \dfrac{\ln(4/3)}{\ln 2}$

Equating the two expressions:

$\dfrac{1}{2 \ln 2} \ln \left( \dfrac{2 \cdot 4^k}{1 + 4^k} \right) = \dfrac{\ln(4/3)}{\ln 2}$

$\ln \left( \dfrac{2 \cdot 4^k}{1 + 4^k} \right) = 2 \ln \left( \dfrac{4}{3} \right) = \ln \left( \dfrac{16}{9} \right)$

$\dfrac{2 \cdot 4^k}{1 + 4^k} = \dfrac{16}{9}$

$18 \cdot 4^k = 16 + 16 \cdot 4^k$

$2 \cdot 4^k = 16 \Rightarrow 4^k = 8$

$2^{2k} = 2^3 \Rightarrow 2k = 3 \Rightarrow k = \dfrac{3}{2}$

Answer: $\dfrac{3}{2}$

</details>

---

### Q12. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^1 \frac{1}{2+\sqrt{x}} \mathrm{~d} x=$

**Options:**

- **(A)** $2 \log \left(\frac{2 e}{3}\right)$
- **(B)** $2 \log \left(\frac{4 e}{9}\right)$
- **(C)** $\log \left(\frac{2 \mathrm{e}}{3}\right)$
- **(D)** $\log \left(\frac{4 \mathrm{e}}{9}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \log \left(\frac{4 e}{9}\right)$**

**Detailed Solution:**

Let $I = \int_0^1 \dfrac{1}{2+\sqrt{x}} \, dx$

Substitute $x = t^2$, which gives $dx = 2t \, dt$.

When $x = 0$, $t = 0$ and when $x = 1$, $t = 1$.

$I = \int_0^1 \dfrac{2t}{2+t} \, dt$

$I = 2 \int_0^1 \dfrac{t+2-2}{t+2} \, dt$

$I = 2 \int_0^1 \left( 1 - \dfrac{2}{t+2} \right) \, dt$

Integrating with respect to $t$:

$I = 2 \left[ t - 2 \log|t+2| \right]_0^1$

Substituting the limits:

$I = 2 \left( (1 - 2 \log 3) - (0 - 2 \log 2) \right)$

$I = 2 \left( 1 + 2 \log 2 - 2 \log 3 \right)$

Using the properties $m \log n = \log(n^m)$ and $1 = \log e$:

$I = 2 \left( \log e + \log 4 - \log 9 \right)$

$I = 2 \log \left( \dfrac{4e}{9} \right)$

Answer: $2 \log \left(\frac{4 e}{9}\right)$

</details>

---

### Q13. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int_{\frac{1}{3}}^1\frac{\left(x-x^3\right)^{\frac{1}{3}}}{x^4} \mathrm{~d} x$ is

**Options:**

- **(A)** $6$
- **(B)** $0$
- **(C)** $2$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $6$**

**Detailed Solution:**

Let $I = \int_{\dfrac{1}{3}}^1 \dfrac{(x-x^3)^{\dfrac{1}{3}}}{x^4} dx$

Taking $x^3$ common from the term inside the cube root, we get:

$I = \int_{\dfrac{1}{3}}^1 \dfrac{x \left(\dfrac{1}{x^2}-1\right)^{\dfrac{1}{3}}}{x^4} dx$

$I = \int_{\dfrac{1}{3}}^1 \left(\dfrac{1}{x^2}-1\right)^{\dfrac{1}{3}} \dfrac{1}{x^3} dx$

Let $\dfrac{1}{x^2}-1 = t$

Differentiating both sides with respect to $x$:

$\dfrac{-2}{x^3} dx = dt \Rightarrow \dfrac{1}{x^3} dx = -\dfrac{1}{2} dt$

When $x = \dfrac{1}{3}$, $t = 9 - 1 = 8$

When $x = 1$, $t = 1 - 1 = 0$

Substituting these values into the integral:

$I = \int_8^0 t^{\dfrac{1}{3}} \left(-\dfrac{1}{2}\right) dt$

$I = \dfrac{1}{2} \int_0^8 t^{\dfrac{1}{3}} dt$

$I = \dfrac{1}{2} \left[ \dfrac{t^{\dfrac{4}{3}}}{\dfrac{4}{3}} \right]_0^8$

$I = \dfrac{3}{8} \left[ 8^{\dfrac{4}{3}} - 0 \right]$

$I = \dfrac{3}{8} \times 16 = 6$

Answer: $6$

</details>

---

### Q14. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_1^{\mathrm{e}} \frac{\mathrm{e}^x}{x}(1+x \log x) \mathrm{d} x=$

**Options:**

- **(A)** $e^e$
- **(B)** $\mathrm{e}^{\mathrm{e}}-\mathrm{e}$
- **(C)** $e^e+e$
- **(D)** e

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $e^e$**

**Detailed Solution:**

Let $I = \int_1^{e} \dfrac{e^x}{x}(1+x \log x) dx$

$I = \int_1^{e} e^x \left(\log x + \dfrac{1}{x}\right) dx$

Using the standard integral $\int e^x (f(x) + f'(x)) dx = e^x f(x) + C$

Here, $f(x) = \log x$ and $f'(x) = \dfrac{1}{x}$

$I = \left[ e^x \log x \right]_1^{e}$

$I = e^e \log e - e^1 \log 1$

Since $\log e = 1$ and $\log 1 = 0$

$I = e^e(1) - e(0) = e^e$

Answer: $e^e$

</details>

---

### Q15. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of integral $\int_{-2}^0\left(x^3+3 x^2+3 x+5+(x+1) \cos (x+1)\right) d x$ is equal to

**Options:**

- **(A)** 0
- **(B)** 6
- **(C)** 4
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 8**

**Detailed Solution:**

Let $I = \int_{-2}^0\left(x^3+3 x^2+3 x+5+(x+1) \cos (x+1)\right) d x$

We can rewrite the integrand by completing the cube:

$x^3+3 x^2+3 x+5 = (x^3+3 x^2+3 x+1) + 4 = (x+1)^3 + 4$

So the integral becomes:

$I = \int_{-2}^0 \left((x+1)^3 + 4 + (x+1) \cos (x+1)\right) d x$

Substitute $t = x+1$, which gives $dt = dx$.

When $x = -2$, $t = -1$.

When $x = 0$, $t = 1$.

The integral transforms to:

$I = \int_{-1}^1 \left(t^3 + 4 + t \cos t\right) dt$

We can split this into three separate integrals:

$I = \int_{-1}^1 t^3 dt + \int_{-1}^1 4 dt + \int_{-1}^1 t \cos t dt$

Since $f(t) = t^3$ and $g(t) = t \cos t$ are odd functions, their definite integrals over the symmetric interval $[-1, 1]$ are zero.

$I = 0 + \int_{-1}^1 4 dt + 0$

$I = [4t]_{-1}^1 = 4(1) - 4(-1) = 8$

Answer: 8

</details>

---

### Q16. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^a \dfrac{x-\mathrm{a}}{x+\mathrm{a}} \mathrm{d} x=$

**Options:**

- **(A)** $\mathrm{a}-2 \mathrm{a} \log 2$
- **(B)** $a-a \log 2$
- **(C)** $\mathrm{a}+2 \mathrm{a} \log 2$
- **(D)** $a+a \log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{a}-2 \mathrm{a} \log 2$**

**Detailed Solution:**

Let $I = \int_0^a \dfrac{x-a}{x+a} dx$

Adding and subtracting $a$ in the numerator:

$I = \int_0^a \dfrac{x+a-2a}{x+a} dx$

$I = \int_0^a \left( 1 - \dfrac{2a}{x+a} \right) dx$

Integrating with respect to $x$:

$I = \left[ x - 2a \log|x+a| \right]_0^a$

Substituting the upper and lower limits:

$I = (a - 2a \log(2a)) - (0 - 2a \log a)$

$I = a - 2a (\log(2a) - \log a)$

$I = a - 2a \log\left(\dfrac{2a}{a}\right)$

$I = a - 2a \log 2$

Answer: $\mathrm{a}-2 \mathrm{a} \log 2$

</details>

---

### Q17. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The integral $\int_{\dfrac{\pi}{6}}^{\dfrac{\pi}{4}} \dfrac{d x}{\sin 2 x\left(\tan ^5 x+\cot ^5 x\right)}$ is equal to

**Options:**

- **(A)** $\dfrac{1}{5}\left(\dfrac{\pi}{4}-\tan ^{-1}\left(\dfrac{1}{3 \sqrt{3}}\right)\right)$
- **(B)** $\dfrac{1}{10}\left(\dfrac{\pi}{4}-\tan ^{-1}\left(\dfrac{1}{9 \sqrt{3}}\right)\right)$
- **(C)** $\dfrac{1}{20} \tan ^{-1}\left(\dfrac{1}{9 \sqrt{3}}\right)$
- **(D)** $\dfrac{\pi}{40}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{10}\left(\dfrac{\pi}{4}-\tan ^{-1}\left(\dfrac{1}{9 \sqrt{3}}\right)\right)$**

**Detailed Solution:**

Let $I = \int_{\dfrac{\pi}{6}}^{\dfrac{\pi}{4}} \dfrac{d x}{\sin 2 x\left(\tan ^5 x+\cot ^5 x\right)}$

Using the identity $\sin 2x = \dfrac{2\tan x}{1+\tan^2 x}$, we can rewrite the integral in terms of $\tan x$.

Substitute $\tan x = t$, which gives $\sec^2 x \, dx = dt \Rightarrow dx = \dfrac{dt}{1+t^2}$.

The limits of integration change as follows:
When $x = \dfrac{\pi}{6}$, $t = \dfrac{1}{\sqrt{3}}$
When $x = \dfrac{\pi}{4}$, $t = 1$

Substituting these into the integral, we get:
$I = \int_{1/\sqrt{3}}^{1} \dfrac{1}{\left(\dfrac{2t}{1+t^2}\right) \left(t^5 + \dfrac{1}{t^5}\right)} \dfrac{dt}{1+t^2}$

$I = \int_{1/\sqrt{3}}^{1} \dfrac{1}{2t \left(\dfrac{t^{10} + 1}{t^5}\right)} dt$

$I = \int_{1/\sqrt{3}}^{1} \dfrac{t^4}{2(t^{10} + 1)} dt$

Now, substitute $t^5 = u$, which gives $5t^4 \, dt = du \Rightarrow t^4 \, dt = \dfrac{du}{5}$.

The limits for $u$ become:
When $t = \dfrac{1}{\sqrt{3}}$, $u = \left(\dfrac{1}{\sqrt{3}}\right)^5 = \dfrac{1}{9\sqrt{3}}$
When $t = 1$, $u = 1$

The integral transforms to:
$I = \int_{1/(9\sqrt{3})}^{1} \dfrac{1}{2(u^2 + 1)} \dfrac{du}{5}$

$I = \dfrac{1}{10} \int_{1/(9\sqrt{3})}^{1} \dfrac{du}{u^2 + 1}$

$I = \dfrac{1}{10} \left[ \tan^{-1} u \right]_{1/(9\sqrt{3})}^{1}$

$I = \dfrac{1}{10} \left( \tan^{-1}(1) - \tan^{-1}\left(\dfrac{1}{9\sqrt{3}}\right) \right)$

$I = \dfrac{1}{10} \left( \dfrac{\pi}{4} - \tan^{-1}\left(\dfrac{1}{9\sqrt{3}}\right) \right)$

Answer: $\dfrac{1}{10}\left(\dfrac{\pi}{4}-\tan ^{-1}\left(\dfrac{1}{9 \sqrt{3}}\right)\right)$

</details>

---

### Q18. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int_{\dfrac{\pi}{6}}^{\dfrac{\pi}{4}} \dfrac{1}{\sin 2 x\left(\tan ^5 x+\cot ^5 x\right)} \mathrm{dx}$ is

**Options:**

- **(A)** $\dfrac{1}{5}\left(\dfrac{\pi}{4}-\tan ^{-1}\left(\dfrac{1}{3 \sqrt{3}}\right)\right)$
- **(B)** $\dfrac{1}{2}\left(\dfrac{\pi}{4}-\tan ^{-1}\left(\dfrac{1}{9 \sqrt{3}}\right)\right)$
- **(C)** $\dfrac{1}{10}\left(\dfrac{\pi}{4}-\tan ^{-1}\left(\dfrac{1}{9 \sqrt{3}}\right)\right)$
- **(D)** $\dfrac{1}{10}\left(\dfrac{\pi}{4}-\tan ^{-1}\left(\dfrac{1}{3 \sqrt{3}}\right)\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{10}\left(\dfrac{\pi}{4}-\tan ^{-1}\left(\dfrac{1}{9 \sqrt{3}}\right)\right)$**

**Detailed Solution:**

Let $I = \int_{\dfrac{\pi}{6}}^{\dfrac{\pi}{4}} \dfrac{1}{\sin 2 x\left(\tan ^5 x+\cot ^5 x\right)} \mathrm{dx}$

Using $\sin 2x = \dfrac{2 \tan x}{1 + \tan^2 x}$ and $\sec^2 x = 1 + \tan^2 x$, we can rewrite the integral as:

$I = \int_{\dfrac{\pi}{6}}^{\dfrac{\pi}{4}} \dfrac{\sec^2 x}{2 \tan x \left(\tan^5 x + \dfrac{1}{\tan^5 x}\right)} \mathrm{dx}$

Let $\tan x = t \Rightarrow \sec^2 x \mathrm{dx} = \mathrm{dt}$

When $x = \dfrac{\pi}{6}$, $t = \dfrac{1}{\sqrt{3}}$

When $x = \dfrac{\pi}{4}$, $t = 1$

$I = \int_{\dfrac{1}{\sqrt{3}}}^{1} \dfrac{1}{2 t \left(t^5 + \dfrac{1}{t^5}\right)} \mathrm{dt} = \int_{\dfrac{1}{\sqrt{3}}}^{1} \dfrac{t^4}{2(t^{10} + 1)} \mathrm{dt}$

Let $t^5 = u \Rightarrow 5 t^4 \mathrm{dt} = \mathrm{du}$

When $t = \dfrac{1}{\sqrt{3}}$, $u = \dfrac{1}{9\sqrt{3}}$

When $t = 1$, $u = 1$

$I = \dfrac{1}{10} \int_{\dfrac{1}{9\sqrt{3}}}^{1} \dfrac{1}{u^2 + 1} \mathrm{du}$

$I = \dfrac{1}{10} \left[ \tan^{-1} u \right]_{\dfrac{1}{9\sqrt{3}}}^{1}$

$I = \dfrac{1}{10} \left( \dfrac{\pi}{4} - \tan^{-1}\left(\dfrac{1}{9 \sqrt{3}}\right) \right)$

Answer: $\dfrac{1}{10}\left(\dfrac{\pi}{4}-\tan ^{-1}\left(\dfrac{1}{9 \sqrt{3}}\right)\right)$

</details>

---

### Q19. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int_0^{\dfrac{\pi}{3}} \dfrac{\tan \theta}{\sqrt{2 \mathrm{ksec} \theta}} \mathrm{d} \theta=1-\dfrac{1}{\sqrt{2}},(k\gt0)$, then the value of $k$ is

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** $\dfrac{1}{2}$
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

Let $I = \int_0^{\dfrac{\pi}{3}} \dfrac{\tan \theta}{\sqrt{2 k \sec \theta}} \mathrm{d} \theta$

Expressing $\tan \theta$ and $\sec \theta$ in terms of sine and cosine:

$I = \dfrac{1}{\sqrt{2k}} \int_0^{\dfrac{\pi}{3}} \dfrac{\sin \theta}{\cos \theta \sqrt{\dfrac{1}{\cos \theta}}} \mathrm{d} \theta$

$I = \dfrac{1}{\sqrt{2k}} \int_0^{\dfrac{\pi}{3}} \sin \theta (\cos \theta)^{-\dfrac{1}{2}} \mathrm{d} \theta$

Let $\cos \theta = t$, then $-\sin \theta \mathrm{d} \theta = \mathrm{d} t$.

When $\theta = 0$, $t = 1$. When $\theta = \dfrac{\pi}{3}$, $t = \dfrac{1}{2}$.

$I = \dfrac{1}{\sqrt{2k}} \int_{\dfrac{1}{2}}^1 t^{-\dfrac{1}{2}} \mathrm{d} t$

$I = \dfrac{1}{\sqrt{2k}} \left[ 2\sqrt{t} \right]_{\dfrac{1}{2}}^1$

$I = \dfrac{2}{\sqrt{2k}} \left( 1 - \dfrac{1}{\sqrt{2}} \right) = \sqrt{\dfrac{2}{k}} \left( 1 - \dfrac{1}{\sqrt{2}} \right)$

Given that $I = 1 - \dfrac{1}{\sqrt{2}}$, we have:

$\sqrt{\dfrac{2}{k}} \left( 1 - \dfrac{1}{\sqrt{2}} \right) = 1 - \dfrac{1}{\sqrt{2}}$

$\sqrt{\dfrac{2}{k}} = 1 \Rightarrow \dfrac{2}{k} = 1 \Rightarrow k = 2$

Answer: 2

</details>

---

### Q20. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{\mathrm{d} x}{3-2 \cos 2 x}=\dfrac{\tan ^{-1}(\mathrm{f}(x))}{\sqrt{5}}+\mathrm{c}$, (where c is constant of integration), then $f(\pi / 4)$ has the value

**Options:**

- **(A)** $-\sqrt{5}$
- **(B)** $\sqrt{5}$
- **(C)** $\dfrac{2}{\sqrt{5}}$
- **(D)** $\dfrac{1}{\sqrt{5}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{5}$**

**Detailed Solution:**

Let $I = \int \dfrac{\mathrm{d} x}{3-2 \cos 2 x}$

Using the identity $\cos 2x = \dfrac{1 - \tan^2 x}{1 + \tan^2 x}$, we get:

$I = \int \dfrac{\mathrm{d} x}{3 - 2 \left( \dfrac{1 - \tan^2 x}{1 + \tan^2 x} \right)}$

$I = \int \dfrac{(1 + \tan^2 x) \mathrm{d} x}{3(1 + \tan^2 x) - 2(1 - \tan^2 x)}$

$I = \int \dfrac{\sec^2 x \mathrm{d} x}{1 + 5 \tan^2 x}$

Let $\tan x = t \Rightarrow \sec^2 x \mathrm{d} x = \mathrm{d} t$

$I = \int \dfrac{\mathrm{d} t}{1 + 5 t^2} = \dfrac{1}{5} \int \dfrac{\mathrm{d} t}{t^2 + \left(\dfrac{1}{\sqrt{5}}\right)^2}$

$I = \dfrac{1}{5} \times \sqrt{5} \tan^{-1} (\sqrt{5} t) + c$

$I = \dfrac{1}{\sqrt{5}} \tan^{-1} (\sqrt{5} \tan x) + c$

Comparing with the given expression $\dfrac{\tan^{-1}(f(x))}{\sqrt{5}} + c$, we have:

$f(x) = \sqrt{5} \tan x$

Substituting $x = \pi/4$:

$f(\pi/4) = \sqrt{5} \tan(\pi/4) = \sqrt{5}$

Answer: $\sqrt{5}$

</details>

---

### Q21. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The integral $\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \sec ^{\frac{2}{3}} x \operatorname{cosec}^{\frac{4}{3}} x d x$ is equal to

**Options:**

- **(A)** $3^{\frac{5}{6}}-3^{\frac{2}{3}}$
- **(B)** $3^{\frac{7}{6}}-3^{\frac{5}{6}}$
- **(C)** $3^{\frac{5}{3}}-3^{\frac{1}{3}}$
- **(D)** $3^{\frac{4}{3}}-3^{\frac{1}{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3^{\frac{7}{6}}-3^{\frac{5}{6}}$**

**Detailed Solution:**

Let $\mathrm{I}=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \sec ^{\frac{2}{3}} x \operatorname{cosec}^{\frac{4}{3}} x \mathrm{~d} x$
$=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{d x}{\cos ^{\frac{2}{3}} x \cdot \sin ^{\frac{4}{3}} x}$
$=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{d x}{\frac{\sin ^{\frac{4}{3}} x}{\cos ^{\frac{4}{3}} x} \cdot \cos ^2 x}$
$=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{\sec ^2 x}{\tan ^{\frac{4}{3}} x} \mathrm{~d} x$
$\begin{aligned} & \text { Put } \tan x=\mathrm{t} \\ & \Rightarrow \sec ^2 x \mathrm{~d} x=\mathrm{dt} \\ \therefore \quad \mathrm{I} & =\int_{\frac{1}{\sqrt{3}}} \mathrm{t}^{\frac{\sqrt{3}}{3}} \frac{\mathrm{dt}}{\mathrm{x}^{-1}} \\ & =\left[-3 \mathrm{t}^{-\frac{1}{3}}\right]_{\frac{1}{\sqrt{3}}}^{\sqrt{3}} \\ & =-3\left[(\sqrt{3})^{\frac{-1}{3}}-\left(\frac{1}{\sqrt{3}}\right)^{\frac{-1}{3}}\right] \\ & =-3\left(3^{-\frac{1}{6}}-3^{\frac{1}{6}}\right) \\ & =3^{\frac{7}{6}}-3^{\frac{5}{6}}\end{aligned}$

</details>

---

### Q22. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The integral $\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \sec ^{\frac{2}{3}} x \operatorname{cosec}^{\frac{4}{3}} x \mathrm{~d} x$ is equal to

**Options:**

- **(A)** $3^{\frac{5}{6}}-3^{\frac{2}{3}}$
- **(B)** $3^{\frac{7}{6}}-3^{\frac{5}{6}}$
- **(C)** $3^{\frac{5}{3}}-3^{\frac{1}{3}}$
- **(D)** $3^{\frac{4}{3}}-3^{\frac{1}{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3^{\frac{7}{6}}-3^{\frac{5}{6}}$**

**Detailed Solution:**

Let $\mathrm{I}=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \sec ^{\frac{2}{3}} x \operatorname{cosec}^{\frac{4}{3}} x \mathrm{~d} x=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{\mathrm{d} x}{\cos ^{\frac{2}{3}} x \cdot \sin ^{\frac{4}{3}} x}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/_OXoNLcu2iZ4djoGRtB72TzW_Dekq8-jEtJfpVY0QA4.original.fullsize.png">

$=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{\sec ^2 x}{\tan ^{\frac{4}{3}} x} \mathrm{~d} x$
Put $\tan x=\mathrm{t} \Rightarrow \sec ^2 x \mathrm{~d} x=\mathrm{dt}$
$\therefore \quad I=\int_{\frac{1}{\sqrt{3}}}^{t^{\frac{\sqrt{3}}{3}}} \frac{\mathrm{dt}}{\frac{4}{3}}=\left[-3 \mathrm{t}^{-\frac{1}{3}}\right]_{\frac{1}{\sqrt{3}}}^{\sqrt{3}}$
$=-3\left[(\sqrt{3})^{\frac{-1}{3}}-\left(\frac{1}{\sqrt{3}}\right)^{\frac{-1}{3}}\right]$
$=-3\left(3^{-\frac{1}{6}}-3^{\frac{1}{6}}\right)$
$=3^{\frac{7}{6}}-3^{\frac{5}{6}}$

</details>

---

### Q23. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^\pi \frac{x \tan x}{\sec x+\cos x} \mathrm{~d} x=$

**Options:**

- **(A)** $\frac{\pi}{8}$
- **(B)** $-\frac{\pi^2}{8}$
- **(C)** $\frac{\pi^2}{4}$
- **(D)** $-\frac{\pi^2}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi^2}{4}$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \mathrm{I}=\int_0^\pi \frac{x \tan x}{\sec x+\cos x} \mathrm{~d} x \quad \ldots \text { (i) } \\ & \therefore \quad \mathrm{I}=\int_0^\pi \frac{(\pi-x) \tan x}{\sec x+\cos x} \mathrm{~d} x \ldots \text { (ii) } \\ & \ldots\left[\because \int_0^{\mathrm{a}} \mathrm{f}(x) \mathrm{d} x=\int_0^{\mathrm{a}} \mathrm{f}(\mathrm{a}-x) \mathrm{d} x\right]\end{aligned}$
Adding (i) and (ii), we get
$\begin{aligned}
& 2 \mathrm{I}=\pi \int_0^\pi \frac{\tan x}{\sec x+\cos x} \mathrm{~d} x \\
& \Rightarrow \mathrm{I}=\frac{\pi}{2} \int_0^\pi \frac{\sin x}{1+\cos ^2 x} \mathrm{~d} x
\end{aligned}$
Put $\cos x=\mathrm{t} \Rightarrow \sin x \mathrm{~d} x=-\mathrm{dt}$
$\begin{aligned}
\therefore \quad \mathrm{I} & =-\frac{\pi}{2} \int_1^{-1} \frac{\mathrm{dt}}{1+\mathrm{t}^2} \\
& =-\frac{\pi}{2}\left[\tan ^{-1} \mathrm{t}\right]_1^{-1} \\
& =\left(-\frac{\pi}{2}\right)\left(-\frac{\pi}{2}\right)=\frac{\pi^2}{4}
\end{aligned}$

</details>

---

### Q24. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int_0^{\frac{1}{2}} \frac{x^2}{\left(1-x^2\right)^{\frac{3}{2}}} \mathrm{~d} x=\frac{\mathrm{k}}{6}$, then the value of $\mathrm{k}$ is

**Options:**

- **(A)** $2 \sqrt{3}-\pi$
- **(B)** $2 \sqrt{3}+\pi$
- **(C)** $3 \sqrt{2}+\pi$
- **(D)** $3 \sqrt{2}-\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \sqrt{3}-\pi$**

**Detailed Solution:**

Let $\mathrm{I}=\int_0^{\frac{1}{2}} \frac{x^2}{\left(1-x^2\right)^{\frac{3}{2}}} \mathrm{~d} x$ 
Put $x=\sin \theta$
$\begin{aligned} & \Rightarrow \mathrm{d} x=\cos \theta \mathrm{d} \theta \\ & \left(1-x^2\right)^{\frac{3}{2}}=\left(1-\sin ^2 \theta\right)^{\frac{3}{2}} \\ & =\left(\cos ^2 \theta\right)^{\frac{3}{2}} \\ & =\cos ^3 \theta \\ & \therefore \quad I=\int_0^{\frac{\pi}{6}} \frac{\sin ^2 \theta \cdot \cos \theta d \theta}{\cos ^3 \theta} \\ & =\int_0^{\frac{\pi}{6}} \tan ^2 \theta d \theta \\ & =\int_0^{\frac{\pi}{6}}\left(\sec ^2 \theta-1\right) d \theta \\ & =[\tan \theta]_0^{\frac{\pi}{6}}-[\theta]_0^{\frac{\pi}{6}} \\ & =\left(\tan \frac{\pi}{6}-\tan 0\right)-\left(\frac{\pi}{6}-0\right) \\ & =\frac{1}{\sqrt{3}}-\frac{\pi}{6} \\ & =\frac{\sqrt{3}}{3}-\frac{\pi}{6} \\ & =\frac{2 \sqrt{3}-\pi}{6} \\ & \text { But, } \int_0^{\frac{1}{2}} \frac{x^2}{\left(1-x^2\right)^{\frac{3}{2}}} \mathrm{~d} x=\frac{\mathrm{k}}{6} \quad \ldots \text { [Given] } \\ & \therefore \quad \mathrm{k}=2 \sqrt{3}-\pi \\ & \end{aligned}$

</details>

---

### Q25. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int_1^2 \frac{\mathrm{d} x}{\left(x^2-2 x+4\right)^{\frac{3}{2}}}=\frac{\mathrm{k}}{\mathrm{k}+5}$, then $\mathrm{k}$ has the value

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** -1
- **(D)** -2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

$\text { Let } \begin{aligned}
\mathrm{I} & =\int_1^2 \frac{\mathrm{d} x}{\left(x^2-2 x+4\right)^{\frac{3}{2}}} \\
& =\int_1^2 \frac{\mathrm{d} x}{\left[(x-1)^2+3\right]^{\frac{3}{2}}}
\end{aligned}$
Put $x-1=\sqrt{3} \tan \theta$
$\mathrm{d} x=\sqrt{3} \sec ^2 \theta \mathrm{d} \theta$
When $x=1, \theta=0$
When $x=2, \theta=\frac{\pi}{6}$
$\begin{aligned} & \therefore \quad I=\int_0^{\frac{\pi}{6}} \frac{\sqrt{3} \sec ^2 \theta}{\left[3 \tan ^2 \theta+3\right]^{\frac{3}{2}}} d \theta \\ & =\int_0^{\frac{\pi}{6}} \frac{\sqrt{3} \sec ^2 \theta}{\left[3\left(1+\tan ^2 \theta\right)\right]^{\frac{3}{2}}} \\ & =\int_0^{\frac{\pi}{6}} \frac{\sqrt{3} \sec ^2 \theta}{3 \cdot \sqrt{3}\left(\sec ^2 \theta\right)^{\frac{3}{2}}} \\ & =\int_0^{\frac{\pi}{6}} \frac{1}{3} \cdot \frac{\sec ^2 \theta}{\sec ^3 \theta} \\ & =\frac{1}{3} \int_{\infty}^{\frac{\pi}{6}} \cos \theta \\ & =\frac{1}{3}[\sin \theta]_0^{\frac{\pi}{6}} \\ & I=\frac{1}{3}\left[\sin \frac{\pi}{6}-\sin 0\right] \\ & I=\frac{1}{6} \\ & \therefore \quad \frac{k}{k+5}=\frac{1}{6} \\ & 6 k=k+5 \\ & \therefore \quad \mathrm{k}=1 \\ & \end{aligned}$

</details>

---

### Q26. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^{\pi / 2} \sin ^5\left(\frac{x}{2}\right) \cdot \sin x d x=$

**Options:**

- **(A)** $\frac{1}{7 \sqrt{2}}$
- **(B)** $\frac{1}{56 \sqrt{2}}$
- **(C)** $\frac{1}{14 \sqrt{2}}$
- **(D)** $\frac{1}{28 \sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{14 \sqrt{2}}$**

**Detailed Solution:**

$\begin{aligned} & \int_0^{\pi / 2} \sin ^5 \frac{x}{2} \sin x \mathrm{~d} x \\ & =\int_0^{\pi / 2} \sin ^5 \frac{x}{2} \cdot 2 \sin \frac{x}{2} \cdot \cos \frac{x}{2} \mathrm{~d} x \\ & =2 \int_0^{\pi / 2} \sin ^6 \frac{x}{2} \cdot \cos \frac{x}{2} \cdot \mathrm{d} x \\ & \quad \frac{1}{\sqrt{2}} \\ & =4 \int_0^6 t^6 \mathrm{~d} t=\frac{4}{7}\left[t^7\right]_0^{\frac{1}{\sqrt{2}}}\left[\text { let } \sin \frac{x}{2}=t\right]\end{aligned}$
$=\frac{4}{7} \cdot\left(\frac{1}{\sqrt{2}}\right)^7=\frac{1}{14 \sqrt{2}}$

</details>

---

### Q27. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{-3}^0 x \sqrt{x+4} d x=$

**Options:**

- **(A)** $\frac{-94}{15}$
- **(B)** $\frac{94}{15}$
- **(C)** $\frac{-34}{15}$
- **(D)** $\frac{64}{15}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{-94}{15}$**

**Detailed Solution:**

$\int_{-3}^0 x \sqrt{x+4} d x$
let $x+4=t$
$$
\begin{aligned}
& \Rightarrow x=t-4 \\
& \Rightarrow \mathrm{d} x=\mathrm{d} t
\end{aligned}
$$
when $x=-3, t=1$
when $x=0, t=4$
$\begin{aligned} & \int_1^4(t-4) \sqrt{t} \mathrm{~d} t=\int_1^4\left(t^{3 / 2}-4 t^{1 / 2}\right) \mathrm{d} t=\left[\frac{2}{5} t^{5 / 2}-\frac{8}{3} t^{3 / 2}\right]_1^4 \\ & =\frac{2}{5}(32-1)-\frac{8}{3}(8-1)=\frac{186-280}{15}=-\frac{94}{15}\end{aligned}$

</details>

---

### Q28. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int_0^{\pi / 4} \sqrt{1-\sin 2 x} d x=$

**Options:**

- **(A)** $\sqrt{2}+1$
- **(B)** $1+2 \sqrt{2}$
- **(C)** $\sqrt{2}-1$
- **(D)** $2 \sqrt{2}-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{2}-1$**

**Detailed Solution:**

$\begin{aligned} & \int_0^{\pi / 4} \sqrt{1-\sin 2 x} \mathrm{~d} x=\int_0^{\pi / 4} \sqrt{\cos ^2 x+\sin ^2 x-2 \sin x \cdot \cos x} \mathrm{~d} x \\ & =\int_0^{\pi / 4} \sqrt{(\cos x-\sin x)^2} \mathrm{~d} x=\int_0^{\pi / 4}|\cos x-\sin x| \mathrm{d} x \\ & =\int_0^{\pi / 4}(\cos x-\sin x) \mathrm{d} x=[\sin x+\cos x]_0^{\pi / 4} \\ & =\left(\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{2}}\right)-(0+1)=-1\end{aligned}$

</details>

---

### Q29. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_0^1|5 x-3| \mathrm{d} x=$

**Options:**

- **(A)** $\frac{23}{10}$
- **(B)** $\frac{13}{10}$
- **(C)** $\frac{31}{10}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{13}{10}$**

**Detailed Solution:**

$\begin{aligned} & \int_0^1|5 x-3| \mathrm{d} x=\int_0^{3 / 5}(3-5 x) \mathrm{d} x+\int_{3 / 5}^1(5 x-3) \mathrm{d} x \\ & =\left[3 x-\frac{5 x^2}{2}\right]_0^{3 / 5}+\left[\frac{5 x^2}{2}-3 x\right]_{3 / 5}^1 \\ & =\left(\frac{9}{5}-\frac{9}{10}\right)-0+\left(\frac{5}{2}-3\right)-\left(\frac{9}{10}-\frac{9}{5}\right) \\ & =\frac{13}{10}\end{aligned}$

</details>

---

### Q30. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^{\frac{\pi}{4}} \sec ^4 x d x=$

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{4}{3}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{4}{3}$**

**Detailed Solution:**

$\begin{aligned} & \int_0^{\frac{\pi}{4}} \sec ^4 x \mathrm{~d} x=\int_0^{\frac{\pi}{4}}\left(\tan ^2 x+1\right) \sec ^2 x \mathrm{~d} x \\ & =\left[\frac{\tan ^3 x}{3}+\tan x\right]_0^{\frac{\pi}{4}} \\ & =\frac{1}{3}+1 \\ & =\frac{4}{3}\end{aligned}$

</details>

---

### Q31. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^1 \sqrt{\frac{1-x}{1+x}} d x=$

**Options:**

- **(A)** $\frac{\pi}{4}+1$
- **(B)** $\frac{\pi}{2}+1$
- **(C)** $\frac{\pi}{4}-1$
- **(D)** $\frac{\pi}{2}-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{2}-1$**

**Detailed Solution:**

$\begin{aligned} & \int_0^1 \sqrt{\frac{1-x}{1+x}} d x=\int_0^1 \frac{1-x}{\sqrt{1-x^2}} d x=\int_0^1 \frac{1}{\sqrt{1-x^2}} d x+\frac{1}{2} \int_0^1 \frac{-2 x}{\sqrt{1-x^2}} d x \\ & =\left[\sin ^{-1} x\right]_0^1+\left[\sqrt{1-x^2}\right]_0^1 \\ & =\sin ^{-1}(1)-\sin ^{-1}(0)+\sqrt{1-1^2}-\sqrt{1-0^2} \\ & =\frac{\pi}{2}-0+0-1 \\ & =\frac{\pi}{2}-1\end{aligned}$

</details>

---

### Q32. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{\frac{\pi}{4}}^{\frac{3 \pi}{4}} \frac{d x}{1+\cos x}$ is equal to

**Options:**

- **(A)** $-2$
- **(B)** $-2-2 \sqrt{2}$
- **(C)** $2$
- **(D)** $-2 \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2$**

**Detailed Solution:**

$\begin{aligned} & \int_{\frac{\pi}{4}}^{\frac{3 \pi}{4}} \frac{d x}{1+\cos x}=\int_{\frac{\pi}{4}}^{\frac{3 \pi}{4}} \frac{1}{2} \sec ^2 \frac{x}{2} d x=\left[\tan \frac{x}{2}\right]_{\frac{\pi}{4}}^{\frac{3 \pi}{4}} \\ & =\left(\tan \frac{3 \pi}{8}-\tan \frac{\pi}{8}\right)=\left(\cot \frac{\pi}{8}-\tan \frac{\pi}{8}\right)=\frac{\cos ^2 \frac{\pi}{8}-\sin ^2 \frac{\pi}{8}}{\sin \frac{\pi}{8} \cdot \cos \frac{\pi}{8}} \\ & =\frac{2 \cos \frac{\pi}{4}}{\sin \frac{\pi}{4}}=2\end{aligned}$

</details>

---

### Q33. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int_0^{\frac{\pi}{2}} \frac{\sin x}{1+\cos ^2 x} d x$ has the value

**Options:**

- **(A)** $-\frac{\pi}{4}$
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{2}$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{4}$**

**Detailed Solution:**

$\begin{aligned} & \int_0^{\pi / 2} \frac{\sin x}{1+\cos ^2 \mathrm{x}} \mathrm{dx}=-\int_1^0 \frac{\mathrm{dt}}{1+\mathrm{t}^2}[\text { let } \cos \mathrm{x}=\mathrm{t}] \\ & =-\left[\tan ^{-1} \mathrm{t}\right]_1^0 \\ & =-\left(0-\frac{\pi}{4}\right) \\ & =\frac{\pi}{4}\end{aligned}$

</details>

---

### Q34. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^\pi \frac{1}{4+3 \cos x} d x=$

**Options:**

- **(A)** 1
- **(B)** $\frac{\pi}{\sqrt{7}}$
- **(C)** 0
- **(D)** $\frac{2}{\sqrt{7}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{\sqrt{7}}$**

**Detailed Solution:**

Let $\int_0^\pi \frac{1}{4+3 \cos x} d x$
Put $\frac{x}{2}=t \Rightarrow \cos x=\frac{1-t^2}{1+t^2}$ and $\sec ^2 \frac{x}{2}\left(\frac{1}{2}\right) d x=d t \Rightarrow d t=\frac{2}{1+t^2} d t$
When $\mathrm{x}=0, \mathrm{t}=0$ and when $\mathrm{x}=\pi, \mathrm{t}=\infty$
$$
\begin{aligned}
& \therefore \quad \mathrm{I}=\int_0^{\infty} \frac{1}{4+3\left(\frac{1-\mathrm{t}^2}{1+\mathrm{t}^2}\right)} \times \frac{2}{1+\mathrm{t}^2} \\
& =\int_0^{\infty} \frac{\left(1+\mathrm{t}^2\right)}{4\left(1+\mathrm{t}^2\right)+3\left(1-\mathrm{t}^2\right)} \times \frac{2}{1+\mathrm{t}^2} \mathrm{dt}=\int_0^{\infty} \frac{2}{7+\mathrm{t}^2} \mathrm{dt}=\frac{2}{7} \int_0^{\infty} \frac{\mathrm{dt}}{1+\left(\frac{1}{\sqrt{7}}\right)^2} \\
& =\frac{2}{7}\left[\tan ^{-1}\left(\frac{\mathrm{t}}{7}\right)\right]_0^{\infty} \frac{1}{\left(\frac{1}{\sqrt{7}}\right)}=\frac{2}{\sqrt{7}}\left[\tan ^{-1} \infty-\tan ^{-1} 0\right]=\frac{2}{\sqrt{7}} \times \frac{\pi}{2}=\frac{\pi}{\sqrt{7}}
\end{aligned}
$$

</details>

---

### Q35. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int_0^a \sqrt{\frac{a-x}{x}} d x=\frac{k}{2}$, then $k=$

**Options:**

- **(A)** $\pi \mathrm{a}$
- **(B)** $\frac{\pi \mathrm{a}}{2}$
- **(C)** $\frac{5 \pi \mathrm{a}}{2}$
- **(D)** $\frac{3 \pi \mathrm{a}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\pi \mathrm{a}$**

**Detailed Solution:**

We have $\int_0^3 \sqrt{\frac{a-x}{x}} d x=\frac{k}{2}$
Put $x=a \sin ^2 \theta \Rightarrow d x=a(2 \sin \theta) \cos \theta d \theta=2 a \sin \theta \cos \theta d \theta$
When $\mathrm{x}=0, \theta=0$ and when $\mathrm{x}=\mathrm{a}, \theta=\frac{\pi}{2}$
$$
\begin{aligned}
& \therefore \int_0^{\frac{\pi}{2}} \sqrt{\frac{\mathrm{a}-\mathrm{a} \sin ^2 \theta}{\mathrm{a} \sin ^2 \theta}}(2 \mathrm{a} \sin \theta \cos \theta) \mathrm{d} \theta=\frac{\mathrm{k}}{2} \\
& \int_0^{\frac{\pi}{2}} \sqrt{\frac{\cos ^2 \theta}{\sin ^2 \theta}} 2(\mathrm{a} \sin \theta \cos \theta) \mathrm{d} \theta=\frac{\mathrm{k}}{2} \Rightarrow \int_0^{\frac{\pi}{2}} \sqrt{\frac{\cos \theta}{\sin \theta}} 2(\mathrm{a} \sin \theta \cos \theta) \mathrm{d} \theta=\frac{\mathrm{k}}{2} \\
& \int_0^{\frac{\pi}{2}} 2 \mathrm{a} \cos \theta^2 \mathrm{~d} \theta=\frac{\mathrm{k}}{2} \Rightarrow 2 \mathrm{a} \int_0^{\frac{\pi}{2}} \frac{1+\cos 2 \theta}{2} \mathrm{~d} \theta=\frac{\mathrm{k}}{2} \\
& \int_0^{\frac{\pi}{2}} 2 \mathrm{a} \cos \theta^2 \mathrm{~d} \theta=\frac{\mathrm{k}}{2} \Rightarrow 2 \mathrm{a} \int_0^{\frac{\pi}{2}} \frac{1+\cos 2 \theta}{2} \mathrm{~d} \theta=\frac{\mathrm{k}}{2} \\
& \mathrm{a}\left[\left(\frac{\pi}{2}+0\right)-(0+0)\right]=\frac{\mathrm{k}}{2} \Rightarrow \mathrm{a} \frac{\pi}{2}=\frac{\mathrm{k}}{2} \Rightarrow \mathrm{k}=\pi \mathrm{a}
\end{aligned}
$$

</details>

---

### Q36. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A fair coin is tossed 4 times. If $X$ a random variable which indicates number of heads, then $\mathrm{P}[\mathrm{X} < 3]=$

**Options:**

- **(A)** $\frac{10}{16}$
- **(B)** $\frac{1}{16}$
- **(C)** $\frac{12}{16}$
- **(D)** $\frac{11}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{11}{16}$**

**Detailed Solution:**

A coin is tossed 4 times
$$
\therefore \mathrm{n}(\mathrm{S})=2^4=16
$$
Following possibilities exist.
(i) All Heads $\Rightarrow 1$ way
(ii) 3 Heads, 1 Tail $\Rightarrow \frac{4 !}{3 !}=4$ ways
(iii) 2 Heads, 2 Tails $\Rightarrow \frac{4 !}{2 ! 2 !}=6$ ways
(iv) 1 Head, 3 Tails $\Rightarrow \frac{4 !}{3 !}=4$ ways
(v) 0 head, 4 Tails $\Rightarrow 1$ way
$\therefore$ Required probability.
$$
\begin{aligned}
& =\mathrm{P}(\mathrm{x}=0,1,2)=\frac{1}{16}+\frac{4}{16}+\frac{6}{16} \\
& =\frac{11}{16}
\end{aligned}
$$

</details>

---

### Q37. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_2^{\mathrm{e}}\left[\frac{1}{\log x}-\frac{1}{(\log x)^2}\right] d x=a+\frac{b}{\log 2}$, then

**Options:**

- **(A)** $\mathrm{a}=-\mathrm{e}, \mathrm{b}=2$
- **(B)** $\mathrm{a}=\mathrm{e}, \mathrm{b}=-2$
- **(C)** $\mathrm{a}=\mathrm{e}, \mathrm{b}=2$
- **(D)** $\mathrm{a}=-\mathrm{e}, \mathrm{b}=2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{a}=\mathrm{e}, \mathrm{b}=-2$**

**Detailed Solution:**

$$
\mathrm{a}+\frac{\mathrm{b}}{\log 2}=\int_2^{\mathrm{e}}\left[\frac{1}{\log x}-\frac{1}{(\log x)^2}\right] \mathrm{dx}
$$
Put $\log \mathrm{x}=\mathrm{t} \Rightarrow \frac{1}{\mathrm{x}} \mathrm{dx}=\mathrm{dt} \Rightarrow \mathrm{dx}=\mathrm{e}^{\mathrm{t}} \mathrm{dt}$
When $\mathrm{x}=\mathrm{e}, \mathrm{t}=1$ and when $\mathrm{x}=2, \mathrm{t}=\log 2$
$$
\begin{aligned}
& \therefore a+\frac{b}{\log 2}=\int_{\log 2}^1\left(\frac{1}{t}-\frac{1}{t^2}\right) e^t \cdot d t=\left[e^t \cdot \frac{1}{t}\right]_{\log 2}^1=e-\frac{e^{\log 2}}{\log 2}=e-\frac{2}{\log 2} \\
& \therefore a=e, b=-2
\end{aligned}
$$

</details>

---

### Q38. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int_0^{\pi / 2} \frac{d x}{5+4 \sin x}=A \tan ^{-1} B$, then $A+B=$

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** 1
- **(C)** 2
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

Let $I=\int_0^{\pi / 2} \frac{d x}{5+4 \sin x}$
Put $\tan \frac{\mathrm{x}}{2}=\mathrm{t} \Rightarrow \sec ^2 \frac{\mathrm{x}}{2}\left(\frac{1}{2}\right) \mathrm{dx}=\mathrm{dt}$
$$
\therefore \mathrm{dx}=\frac{2 \mathrm{dt}}{1+\mathrm{t}^2} \text { and } \sin \mathrm{x}=\frac{2 \mathrm{t}}{1+\mathrm{t}^2}
$$
When $\mathrm{x}=0, \mathrm{t}=0$ and when $\mathrm{x}=\frac{\pi}{2}, \mathrm{t}=1$
$$
\begin{aligned}
& \therefore=\int_0^1 \frac{1}{5+4\left(\frac{2 \mathrm{t}}{1+\mathrm{t}^2}\right)} \times \frac{2 \mathrm{dt}}{1+\mathrm{t}^2}=2 \int_0^1 \frac{\mathrm{dt}}{5+5 \mathrm{t}^2+8 \mathrm{t}}=\frac{2}{5} \int_0^1 \frac{\mathrm{dt}}{\mathrm{t}^2+\frac{8}{5} \mathrm{t}+1} \\
& =\frac{2}{5} \int_0^1 \frac{\mathrm{dt}}{\mathrm{t}^2+\frac{8}{5} \mathrm{t}+\frac{16}{25}+\frac{9}{25}}=\frac{2}{5} \int_0^1 \frac{\mathrm{dt}}{\left(\mathrm{t}+\frac{4}{5}\right)^2+\left(\frac{3}{5}\right)^2}
\end{aligned}
$$
$$
\begin{aligned}
& \therefore I=\frac{2}{5} \times \frac{1}{\left(\frac{3}{5}\right)}\left[\tan ^{-1}\left[\frac{\mathrm{t}+\frac{4}{5}}{\left(\frac{3}{5}\right)}\right]\right]_0^1=\frac{2}{3}\left[\tan ^{-1}\left(\frac{5 \mathrm{t}+4}{3}\right)\right]_0^1 \\
& =\frac{2}{3}\left[\tan ^{-1} 3-\tan ^{-1} \frac{4}{3}\right]=\frac{2}{3} \tan ^{-1}\left[\frac{3-\left(\frac{4}{3}\right)}{1+3\left(\frac{4}{3}\right)}\right] \\
& =\frac{2}{3} \tan ^{-1}\left(\frac{5}{3} \times \frac{1}{5}\right)=\frac{2}{3} \tan ^{-1}\left(\frac{1}{3}\right)
\end{aligned}
$$
Comparing with given data, we get
$$
\mathrm{A}=\frac{2}{3}, \mathrm{~B}=\frac{1}{3} \Rightarrow \mathrm{A}+\mathrm{B}=1
$$

</details>

---

### Q39. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int_{o}^{a} \frac{d x}{1+4 x^{2}}=\frac{\pi}{8}$, then $a=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** 2
- **(C)** $\frac{1}{4}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

We have $\int_{0}^{a} \frac{d x}{1+4 x^{2}}=\frac{\pi}{8}$
$\therefore \frac{\pi}{8}=\frac{1}{4} \int_{0}^{a} \frac{d x^{2}+\left(\frac{1}{2}\right)^{2}}{2}=\frac{1}{4} \frac{1}{\left(\frac{1}{2}\right)}\left[\tan ^{-1} \frac{x}{\left(\frac{1}{2}\right)}\right]_{0}^{a}$
$\quad=\frac{1}{2}\left[\tan ^{-1} 2 a-\tan ^{-1} 0\right]$
$\therefore \frac{\pi}{8}=\frac{1}{2} \tan ^{-1} 2 a \Rightarrow \frac{\pi}{4}=\tan ^{-1} 2 a \Rightarrow 2 a=\tan \frac{\pi}{4}=1 \Rightarrow a=\frac{1}{2}$

</details>

---

### Q40. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{1}^{28} \frac{\mathrm{d} x}{x(1+\log x)^{2}}=$

**Options:**

- **(A)** $\cdot \log 2$
- **(B)** $1+\log 2$
- **(C)** $\frac{\log 2}{(1+\log 2)}$
- **(D)** $\frac{1}{(1+\log 2)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\log 2}{(1+\log 2)}$**

**Detailed Solution:**

$I=\int_{1}^{2} \frac{d x}{x(1+\log x)}$
Put $\quad 1+\log x=t \Rightarrow \frac{1}{x} d x=d t$
When $x=1, t=1$ and when $x=2, t=1+\log 2$
$\begin{aligned} I &=\int_{1}^{1+\log 2} \frac{d t}{t}=[\log t]_{1}^{1+\log 2}=\log (1+\log 2)-\log 1 \\ &=\log (1+\log 2) \end{aligned}$

</details>

---

### Q41. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0}^{1}\left(1-\frac{x}{1 !}+\frac{x^{2}}{2 !}-\frac{x^{3}}{3 !}+\cdots\right.$ upto $\left.\infty\right) e^{2 x} d x=$

**Options:**

- **(A)** $e^{2}$
- **(B)** $e-1$
- **(C)** $e+1$
- **(D)** $e$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $e-1$**

**Detailed Solution:**

(B)
$\int_{0}^{1}\left(1-\frac{x}{1 !}+\frac{x^{2}}{2 !}-\frac{x^{3}}{3 !}+\ldots \infty\right) e^{2 x} d x$
$=\int_{0}^{1} e^{-x} e^{2 x} d x=\int_{0}^{1} e^{x} d x$
$=\left[e^{x}\right]_{0}^{1}=e^{1}-e^{0}=e-1$

</details>

---

### Q42. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\int_{1}^{k}\left(3 x^{2}+2 x+1\right) d x=11$, then $\mathrm{k}=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $-2$
- **(C)** $-\frac{1}{2}$
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2**

**Detailed Solution:**

(C)
We have $\left[3\left(\frac{x^{3}}{3}\right)+2\left(\frac{x^{2}}{2}\right)+x\right]_{1}^{k}=11$
$\therefore\left[x^{3}+x^{2}+x\right]_{1}^{k}=11$
$\left(k^{3}+k^{2}+k\right)-(1+1+1)=11 \quad \Rightarrow k^{3}+k^{2}+k=14$
$\therefore \mathrm{k}\left(\mathrm{k}^{2}+\mathrm{k}+1\right)=2 \times 7 \Rightarrow \mathrm{k}=2$

</details>

---

### Q43. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0}^{1}\left(\frac{x^{2}-2}{x^{2}+1}\right) d x=$

**Options:**

- **(A)** $1+\frac{3 \pi}{4}$
- **(B)** $1-\frac{3 \pi}{4}$
- **(C)** $1-\frac{\pi}{4}$
- **(D)** $1+\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1-\frac{3 \pi}{4}$**

**Detailed Solution:**

(C)
$\begin{aligned} \int_{0}^{1} \frac{x^{2}+1-3}{x^{2}+1} d x &=\int_{0}^{1} \frac{x^{2}+1}{x^{2}+1}-\frac{3}{x^{2}+1} d x \\ &=\int_{0}^{1} 1-\frac{3}{x^{2}+1} d x=\left[x-3 \tan ^{-1} x\right]_{0}^{1} \\ &=\left(1-3 \tan ^{-1} 1\right)-\left(0-3 \tan ^{-1} 0\right)=1-3 \frac{\pi}{4} \end{aligned}$

</details>

---

### Q44. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0}^{a} \sqrt{\frac{x}{a-x}} d x=$

**Options:**

- **(A)** $\left(\frac{\pi}{4}\right) a$
- **(B)** $-\pi a$
- **(C)** $2 \pi a$
- **(D)** $\left(\frac{\pi}{2}\right) a$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(\frac{\pi}{2}\right) a$**

**Detailed Solution:**

(C)

</details>

---

### Q45. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{2}^{3} \frac{x}{x^{2}-1} d x=$

**Options:**

- **(A)** $\left(\frac{-1}{2}\right) \log \left(\frac{8}{3}\right)$
- **(B)** $\left(\frac{1}{2}\right) \log \left(\frac{8}{3}\right)$
- **(C)** $\left(\frac{-1}{3}\right) \log \left(\frac{8}{3}\right)$
- **(D)** $\left(\frac{1}{3}\right) \log \left(\frac{8}{3}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\frac{1}{2}\right) \log \left(\frac{8}{3}\right)$**

**Detailed Solution:**

$\int \frac{1}{x^{2}-1} d x$
$=\int_{2}^{1} \frac{(x-1)+1}{(x-1)(x+1)} d x-\int_{2}^{1} \frac{d x}{x+1}+\int_{2}^{1}\left(\frac{1}{x-1}-\frac{1}{x+1}\right) \frac{1}{2} d x$
$=|\log | x+1||_{2}^{1}+\frac{1}{2}\left[\left.\log \left|\frac{x-1}{x+1}\right|\right|_{2} ^{1}\right.$
$=(\log 4-\log 3)+\frac{1}{2}\left|\log \left(\frac{2}{4}\right)-\log \left(\frac{1}{3}\right)\right|$
$\left.=\log \left(\frac{4}{3}\right)+\frac{1}{2} \mid \frac{\log \left(\frac{1}{2}\right)}{1}\right)-\log \left(\frac{4}{3}\right)+\log \left|\frac{3}{2}\right|^{2}$
$=\log \left(\frac{4}{3} x \sqrt{\frac{3}{2}}\right)^{1}-\log \left(\frac{8}{3}\right)^{2} \mid-\frac{1}{2} \log \left(\frac{8}{3}\right)$
This problem con ulso be nolved an follows :
$\begin{array}{l}
\int_{0}^{1} \frac{x}{x^{2}-1} d x \\
-\int_{2}^{1} \frac{x}{(x-1)(x+1)} d x-\frac{1}{2} \int_{0}^{1}\left|\frac{1}{x-1}+\frac{1}{x+1}\right| d x
\end{array}$
$=\frac{1}{2}\left\{[\log (x-1)]_{2}^{3}+[\log (x+1)]_{2}^{3}\right\}$
$=\frac{1}{2}\left\{[\log [(x-1)(x+1)]]_{2}^{3}\right\}=\frac{1}{2}\left[\log \left(x^{2}-1\right)\right]_{2}^{3}$
$=\frac{1}{2}[\log (9-1)-\log (4-1)]=\frac{1}{2} \log \left(\frac{8}{3}\right)$

</details>

---

### Q46. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0}^{5} \frac{\mathrm{d} x}{x^{2}+2 x+10}$ =

**Options:**

- **(A)** $\frac{\pi}{6}$
- **(B)** $\frac{\pi}{12}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{12}$**

**Detailed Solution:**

$\begin{aligned} I &=\int_{0}^{5} \frac{d x}{x^{2}+2 x+10}=\int_{0}^{5} \frac{d x}{(x+1)^{2}+(3)^{2}} \\ &=\frac{1}{3}\left[\tan ^{-1} \frac{x+1}{3}\right]_{0}^{5}=\frac{1}{3}\left[\tan ^{-1} 2-\tan ^{-1} \frac{1}{3}\right] \\ &=\frac{1}{3}\left[\tan ^{-1}\left[\frac{2-\frac{1}{3}}{1+\frac{2}{3}}\right]\right]=\frac{1}{3} \tan ^{-1}(1) \\ &=\frac{1}{3} \times \frac{\pi}{4}=\frac{\pi}{12} \end{aligned}$

</details>

---

### Q47. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$$
\int_{0}^{\frac{\pi}{2}} \frac{d x}{1+\cos x}=
$$

**Options:**

- **(A)** -2
- **(B)** 2
- **(C)** 1
- **(D)** -1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

$\begin{aligned}{\text{Let}}1 &=\int_{0}^{\frac{\pi}{2}} \frac{\mathrm{dx}}{1+\cos \mathrm{x}}=\int_{0}^{\frac{\pi}{2}} \frac{\mathrm{dx}}{2 \cos ^{2} \frac{\mathrm{x}}{2}}=\frac{1}{2} \int_{0}^{\frac{\pi}{2}} \sec ^{2} \frac{\mathrm{x}}{2} \mathrm{dx} \\ &=\frac{1}{2}\left[\frac{\tan \frac{\mathrm{x}}{2}}{\left(\frac{1}{2}\right)}\right]_{0}^{\frac{\pi}{2}}=\tan \frac{\pi}{4}-\tan 0=1-0=1 \end{aligned}$

</details>

---

### Q48. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int_{0}^{1} \tan ^{-1}\left(\frac{2 x}{1-x^{2}}\right) d x=$

**Options:**

- **(A)** $\pi-\log 2$
- **(B)** $\frac{\pi}{2}-\log 2$
- **(C)** $\pi+\log 2$
- **(D)** $\frac{\pi}{2}+\log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{2}-\log 2$**

**Detailed Solution:**

Let $I=\int_{0}^{1} \tan ^{-1}\left(\frac{2 x}{1-x^{2}}\right) d x$
Put $x=\tan \theta \Rightarrow d x=\sec ^{2} \theta d \theta$
When $x=0, \theta=0$ and when $x=1, \theta=\frac{\pi}{4}$
$\therefore \mathrm{I}=\int_{0}^{\frac{\pi}{4}}\left[\tan ^{-1}\left(\frac{2 \tan \theta}{1-\tan ^{2} \theta}\right)\right]\left(1+\tan ^{2} \theta\right) \mathrm{d} \theta=\int_{0}^{\frac{\pi}{4}} \tan ^{-1}(\tan 2 \theta)\left(1+\tan ^{2} \theta\right) \mathrm{d} \theta$
$=\int_{0}^{\frac{\pi}{4}} 2 \theta \sec ^{2} \theta d \theta=2 \int_{0}^{\pi / 4} \theta \sec ^{2} \theta d \theta=2[\theta \tan \theta]_{0}^{\pi / 4}-2 \int_{0}^{\pi / 4} \tan \theta d \theta$
$=2\left[\frac{\pi}{4}\right]+2[\log |\cos \theta|]_{0}^{\pi / 4}=\frac{\pi}{2}+2\left[\log \left|\frac{1}{\sqrt{2}}\right|\right]$
$=\frac{\pi}{2}+2 \log (2)^{\frac{1}{2}}$
$=\frac{\pi}{2}-\log 2$

</details>

---

### Q49. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int_{0}^{\frac{\pi}{4}} \frac{\sin x+\cos x}{9+16 \sin 2 x} d x=k \log 3$, then $k=$

**Options:**

- **(A)** $\frac{1}{30}$
- **(B)** $\frac{1}{20}$
- **(C)** $\frac{1}{10}$
- **(D)** $\frac{1}{40}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{20}$**

**Detailed Solution:**

Let $I=\int_{0}^{\frac{\pi}{4}} \frac{\sin x+\cos x}{9+16 \sin 2 x} d x=K \log 3$
Put $\sin x-\cos x=t \Rightarrow(\cos x+\sin x) d x=d t$ ...(1)
Now squaring equation (1), we get
$\begin{aligned} \therefore I &=\int_{-1}^{0} \frac{d t}{9+16\left(1-t^{2}\right)} \\ &=\int_{-1}^{0} \frac{d t}{25-16 t^{2}}=\frac{1}{16} \int_{-1}^{0} \frac{d t}{\left(\frac{5}{4}\right)^{2}-t^{2}} \end{aligned}$
$\begin{array}{l}
=\frac{1}{16} \times \frac{1}{2\left(\frac{5}{4}\right)}\left[\log \mid \frac{\frac{5}{4}+t}{\frac{5}{4}-t}\right]_{-1}^{0}=\frac{1}{40}\left[\log \left(\frac{5+4 t}{5-4 t}\right)\right]_{-1}^{0}=\frac{1}{40}\left[\log (1)-\log \left(\frac{1}{9}\right)\right] \\
=\frac{1}{40}(\log 9)=\frac{1}{40} \log 3^{2}=\frac{2}{40} \log 3=\frac{1}{20} \log 3
\end{array}$
As per given data, $K=\frac{1}{20}$

</details>

---

### Q50. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{0}^{\frac{\pi}{2}} \frac{\sin x \cos x}{1+\sin ^{4} x} d x=$

**Options:**

- **(A)** $\frac{\pi}{6}$
- **(B)** $\frac{\pi}{8}$
- **(C)** $\frac{\pi}{2}$
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{8}$**

**Detailed Solution:**

$I=\int_{0}^{\frac{\pi}{2}} \frac{\sin x \cos x}{1+\sin ^{4} x} d x \quad=\frac{1}{2} \int_{0}^{\frac{\pi}{2}} \frac{2 \sin x \cos x}{1+\left(\sin ^{2} x\right)^{2}} d x$ 
Put $\sin ^{2} x=t \Rightarrow 2 \sin x \cos x d x=d t$
When $x=0, t=0$ and when $x=\frac{\pi}{2}, t=1$
$\therefore I=\frac{1}{2} \int_{0}^{1} \frac{\mathrm{dt}}{1+\mathrm{t}^{2}}=\frac{1}{2}\left[\tan ^{-1} \mathrm{t}\right]_{0}^{1}=\frac{1}{2}\left[\frac{\pi}{4}-0\right]=\frac{\pi}{8}$

</details>

---

### Q51. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>4</mn></mrow></munderover><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><msqrt><mi>x</mi></msqrt></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo></math> ________

**Options:**

- **(A)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
- **(B)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
- **(C)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
- **(D)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>**

**Detailed Solution:**

Let <math><mi>I</mi><mo>=</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>4</mn></mrow></munderover><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msqrt><mi>x</mi></msqrt></mrow></mfrac></mrow></mrow></math> put <math><mi>x</mi><mo>=</mo><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></math>  
<math><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi></math>  
Then, <math><mi>I</mi><mo>=</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>2</mn></mrow></munderover><mrow><mfrac><mrow><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfrac><mo>=</mo></mrow></mrow><mn>2</mn><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>2</mn></mrow></munderover><mrow><mfrac><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced><mo>-</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfrac><mi>d</mi><mi>t</mi></mrow></mrow></math>  
<math><mi>I</mi><mo>=</mo><mn>2</mn><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>2</mn></mrow></munderover><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi></mrow></mrow></math>  
<math><mi>I</mi><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mn>3</mn></mrow></mfenced><mo>=</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mfenced></math>

</details>

---

### Q52. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msubsup><mrow><msqrt><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></msqrt></mrow></mrow><mo>.</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>3</mn></mrow></msup><mi>θ</mi><mi>d</mi><mi>θ</mi><mo>=</mo></math> <em>…</em>

**Options:**

- **(A)** <math><mfrac><mrow><mo>-</mo><mn>20</mn></mrow><mrow><mn>21</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mo>-</mo><mn>8</mn></mrow><mrow><mn>21</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>20</mn></mrow><mrow><mn>21</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>21</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>21</mn></mrow></mfrac></math>**

**Detailed Solution:**

Let <math><mi>l</mi><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msubsup><mrow><msqrt><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></msqrt></mrow></mrow><mo>.</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>3</mn></mrow></msup><mi>θ</mi><mi>d</mi><mi>θ</mi></math>  
<math><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msubsup><mrow><msqrt><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></msqrt></mrow></mrow><mo>.</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></mrow></mfenced><mi>d</mi><mi>θ</mi></math>  
Put <math><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi><mo>=</mo><mi>t</mi></math>  
<math><mo>&#8658;</mo><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mi>d</mi><mi>θ</mi><mo>=</mo><mi>d</mi><mi>t</mi></math>  
<math><mo>&#8658;</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mi>d</mi><mi>θ</mi><mo>=</mo><mo>-</mo><mi>d</mi><mi>t</mi></math>  
If <math><mi>θ</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>t</mi><mo>=</mo><mn>1</mn><mtext> </mtext><mi>a</mi><mi>n</mi><mi>d</mi><mtext> </mtext><mi>θ</mi><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi>t</mi><mo>=</mo><mn>0</mn></math>  
<math><mo>∴</mo><mi>l</mi><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>1</mn></mrow><mrow><mn>0</mn></mrow></msubsup><mrow><msqrt><mi>t</mi></msqrt></mrow></mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mfenced separators="|"><mrow><mo>-</mo><mi>d</mi><mi>t</mi></mrow></mfenced></math>  
<math><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>t</mi></mrow><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msup><mo>-</mo><msup><mrow><mi>t</mi></mrow><mrow><mrow><mrow><mn>5</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msup></mrow></mfenced><mi>d</mi><mi>t</mi></mrow></mrow></math>  
<math><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>t</mi></mrow><mrow><mrow><mrow><mn>3</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msup></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi>t</mi></mrow><mrow><mrow><mrow><mn>7</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msup></mrow><mrow><mfrac><mrow><mn>7</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfrac></mrow></mfenced></math>  
<math><mo>=</mo><msubsup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><msup><mrow><mi>t</mi></mrow><mrow><mrow><mrow><mn>3</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msup><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>7</mn></mrow></mfrac><msup><mrow><mi>t</mi></mrow><mrow><mrow><mrow><mn>7</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msup></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup></math>  
<math><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>7</mn></mrow></mfrac></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mn>0</mn><mo>-</mo><mn>0</mn></mrow></mfenced></math>  
<math><mo>=</mo><mfrac><mrow><mn>14</mn><mo>-</mo><mn>6</mn></mrow><mrow><mn>21</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>21</mn></mrow></mfrac></math>

</details>

---

### Q53. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `2`

If <math><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn><mi> </mi></mrow></mfrac></mrow></munderover><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mi> </mi><mi>d</mi><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mrow><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>,</mo></math> then <math><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn><mi> </mi></mrow></mfrac></mrow></munderover><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mi> </mi><mi>d</mi><mi>x</mi><mo>=</mo></mrow></mrow></mrow></mrow></mrow></mrow></math>

**Options:**

- **(A)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
- **(B)** <math><mn>1</mn><mo>-</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
- **(C)** <math><mi> </mi><mn>1</mn><mo>+</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
- **(D)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow></math>**

**Detailed Solution:**

<math><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn><mi> </mi></mrow></mfrac></mrow></munderover><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mi> </mi><mi>d</mi><mi>x</mi><mo>=</mo></mrow></mrow></mrow></mrow></mrow></mrow><mi> </mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn><mi> </mi></mrow></mfrac></mrow></munderover><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></mfenced></mrow></mrow></mrow></mrow><mi>d</mi><mi>x</mi></math>
<math><mo>=</mo><mo>-</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn><mi> </mi></mrow></mfrac></mrow></munderover><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mo>(</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>)</mo><mi> </mi><mi>d</mi><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mrow></math>
<math> <mrow> <mo>=</mo><mo>-</mo><mfrac> <mi>π</mi> <mn>2</mn> </mfrac> <mi>log</mi><mrow><mo>(</mo> <mrow> <mfrac> <mn>1</mn> <mn>2</mn> </mfrac> </mrow> <mo>)</mo></mrow><mo>=</mo><mfrac> <mi>π</mi> <mn>2</mn> </mfrac> <mi>log</mi><mn>2</mn></mrow> </math>

</details>

---

### Q54. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `2`

<math><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mi>x</mi><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo></mrow></mrow></mrow></mrow></math>

**Options:**

- **(A)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mrow><munderover><mo stretchy="false">∫</mo><mrow><mtable><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>(</mo><mi mathvariant="normal">u</mi><mi mathvariant="normal">v</mi><mi> </mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">e</mi><mo>)</mo></mtd></mtr></mtable></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mi>x</mi><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo></mrow></mrow></mrow></mrow><mi> </mi><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mrow><mo stretchy="false">∫</mo><mrow><mi>x</mi></mrow></mrow><mi> </mi><mi>d</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup><mo>-</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>d</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi><mrow><mo stretchy="false">∫</mo><mrow><mi>x</mi><mi> </mi><mi>d</mi><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mfenced></mrow></mrow><mi> </mi><mi>d</mi><mi>x</mi></math>
<math><mo>=</mo><msubsup><mrow><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>⋅</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mi> </mi></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup><mo>-</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mrow><mo>⋅</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math>
<math><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>⋅</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mn>0</mn></mrow></mfenced><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi></math>
<math><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>8</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></math>
<math><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>8</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup><mi> </mi></math>
<math><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>8</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>0</mn></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mn>0</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>8</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>8</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

</details>

---

### Q55. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

<math><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mfenced separators="|"><mrow><mfrac><mrow><mroot><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow><mrow><mi>n</mi></mrow></mroot></mrow><mrow><mroot><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow><mrow><mi>n</mi></mrow></mroot><mo>+</mo><mroot><mrow><mrow><mrow><mi mathvariant="normal">cosec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow><mrow><mi>n</mi></mrow></mroot></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi> </mi></mrow></mrow></math>

**Options:**

- **(A)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mfenced separators="|"><mrow><mfrac><mrow><mroot><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow><mrow><mi>n</mi></mrow></mroot></mrow><mrow><mroot><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow><mrow><mi>n</mi></mrow></mroot><mo>+</mo><mroot><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi> </mi><mi>x</mi></mrow></mrow></mrow><mrow><mi>n</mi></mrow></mroot></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mi> </mi></mrow></mrow></math>             ..... (i)
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mi>I</mi><mo>=</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><mroot><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mrow></mrow><mrow><mi>n</mi></mrow></mroot></mrow><mrow><mroot><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mi> </mi><mroot><mrow><mrow><mrow><mi mathvariant="normal">cosce</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mrow></mrow><mrow><mi>n</mi></mrow></mroot></mrow></mrow></mrow><mrow><mi>n</mi></mrow></mroot></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></mrow></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mi>I</mi><mo>=</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><mroot><mrow><mrow><mrow><mi mathvariant="normal">cosce</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow><mrow><mi>n</mi></mrow></mroot></mrow><mrow><mroot><mrow><mrow><mrow><mi mathvariant="normal">cosce</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mi>n</mi></mrow></mroot><mi> </mi><mo>+</mo><mi> </mi><mroot><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow><mrow><mi>n</mi></mrow></mroot></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></mrow></math>             ..... (ii)
Adding equation (i) and (ii)
 <math><mn>2</mn><mi>I</mi><mo>=</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mi>d</mi><mi>x</mi><mi> </mi></mrow></mrow></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msubsup></math> 
 <math><mo>⇒</mo><mi> </mi><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>

</details>

---

### Q56. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

<math><mrow><munderover><mo stretchy="false">∫</mo><mrow><mo>-</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow><mrow><mn>2</mn><mo>+</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo></mrow></mrow><mi> </mi></mrow></mrow></math>

**Options:**

- **(A)** <math > <mn>1</mn></math>
- **(B)** <math > <mn>3</mn></math>
- **(C)** <math > <mn>2</mn></math>
- **(D)** <math> <mn>0</mn> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math> <mn>0</mn> </math>**

**Detailed Solution:**

Let <math><mi>I</mi><mo>=</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mo>-</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow><mrow><mn>2</mn><mo>+</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></mrow></mrow></math>
As given function <math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mi>log</mi><mrow><mo>(</mo> <mrow> <mfrac> <mrow> <mn>2</mn><mo>−</mo><mi>sin</mi><mi>x</mi></mrow> <mrow> <mn>2</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow> </mfrac> </mrow> <mo>)</mo></mrow></mrow> </math> is odd.
<math> <mrow> <mo>⇒</mo><mi>I</mi><mo>=</mo><mstyle displaystyle="true"> <mrow><mo>∫</mo> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></mrow> </mrow> </mstyle></mrow> </math>

</details>

---

### Q57. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_{0}^{1} x^{2}\left(1-x^{2}\right)^{3 / 2} d x$ is

**Options:**

- **(A)** $\frac{1}{32}$
- **(B)** $\frac{\pi}{8}$
- **(C)** $\frac{\pi}{16}$
- **(D)** $\frac{\pi}{32}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{32}$**

**Detailed Solution:**

Let $I=\int_{0}^{1} x^{2}\left(1-x^{2}\right)^{3 / 2} d x$
$\begin{aligned} &\text { (let } x=\sin \theta \Rightarrow d x=\cos \theta d \theta) \\ I=\int_{0}^{\pi / 2} \sin ^{2} \theta\left(\cos ^{2} \theta\right)^{3 / 2} \cdot \cos \theta d \theta \\=\int_{0}^{\pi / 2} \sin ^{2} \theta \cdot \cos ^{4} \theta d \theta \end{aligned}$
By Gamma function, $I=\frac{\sqrt{\frac{2+1}{2}} \mid \frac{4+1}{2}}{2 \mid \frac{2+4+2}{2}}=\frac{\sqrt{\frac{3}{2}} \sqrt{\frac{5}{2}}}{2 \Gamma 4}$
$=\frac{\frac{1}{2} \mid \frac{1}{2} \cdot \frac{3}{2} \cdot \frac{1}{2} \cdot \sqrt{\frac{1}{2}}}{2 \cdot 3 \cdot 2}$
$=\frac{3 \cdot \sqrt{\pi} \cdot \sqrt{\pi}}{2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 2}=\frac{\pi}{32}$

</details>

---

### Q58. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int_{3}^{4} \sqrt{(4-x)(x-3)} d x$ is

**Options:**

- **(A)** $\frac{\pi}{16}$
- **(B)** $\frac{\pi}{8}$
- **(C)** $\frac{\pi}{4}$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{8}$**

**Detailed Solution:**

Let $I=\int_{3}^{4} \sqrt{(4-x)(x-3)} d x$
$=\int_{3}^{4} \sqrt{-x^{2}+7 x-12} d x$
$=\int_{3}^{4} \sqrt{-\left(x^{2}-7 x+\frac{49}{4}-\frac{49}{4}\right)-12} d x$
$=\int_{3}^{4} \sqrt{-\left(x-\frac{7}{2}\right)^{2}+\frac{49}{4}-12} d x$
$=\int_{3}^{4} \sqrt{\frac{1}{4}-\left(x-\frac{7}{2}\right)^{2}} d x$
Let $t=x-\frac{7}{2} \Rightarrow d t=d x$
$\therefore$ Upper limit $=\frac{1}{2}$ and lower limit $=-\frac{1}{2}$
$$
\begin{array}{l}
=\int_{-1 / 2}^{1 / 2} \sqrt{\left(\frac{1}{2}\right)^{2}-t^{2}} d t \\
=2 \int_{0}^{1 / 2} \sqrt{\left(\frac{1}{2}\right)^{2}-t^{2}} d t \\
=2\left[\frac{t}{2} \sqrt{\frac{1}{4}-t^{2}}+\frac{1}{8} \sin ^{-1} 2 t\right]_{0}^{1 / 2} \\
=2\left[0+\frac{1}{8} \times \frac{\pi}{2}\right] \\
=\frac{\pi}{8}
\end{array}
$$

</details>

---

### Q59. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int_{0}^{\pi / 2} \frac{\cos 3 x+1}{2 \cos x-1} d x$ is

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** $\frac{1}{2}$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

Let $\begin{aligned} I=\int_{0}^{\pi / 2} \frac{\cos 3 x+1}{2 \cos x-1} d x \\ &=\int_{0}^{\pi / 2} \frac{\cos 3 x-\cos \frac{3 \pi}{3}}{2\left(\cos x-\cos \frac{\pi}{3}\right)} d x \\=\int_{0}^{\pi / 2} \frac{\left(4 \cos ^{3} x-3 \cos x\right)-\left(4 \cos ^{3} \frac{\pi}{3}-3 \cos \frac{\pi}{3}\right)}{2\left(\cos x-\cos \frac{\pi}{3}\right)} d x \\=& 2 \int_{0}^{\pi / 2}\left(\frac{\cos ^{3} x-\cos ^{3} \frac{\pi}{3}}{\cos x-\cos \frac{\pi}{3}}\right) d x \\=\frac{3}{2} \int_{0}^{\pi / 2}\left(\frac{\cos x-\cos \frac{\pi}{3}}{\cos x-\cos \frac{\pi}{3}}\right) d x \\=& \int_{0}^{\pi / 2}\left(1+\cos 2 x+\frac{1}{2}+\cos x\right) d x-\frac{3 \pi}{4} \\=& \frac{3 \pi}{4}+1-\frac{3 \pi}{4}=1 \end{aligned}$
$$

</details>

---

