# MHT CET Mathematics - Definite Integration

## Topic 1: Definite Integration by Parts

**Total Questions:** 13

---

### Q1. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $I = \int_1^3 e^x \dfrac{(x+2)^2}{(x+4)^2}\,dx$ is:

**Options:**

- **(A)** $e\left(\dfrac{3e^2}{7} + \dfrac{1}{5}\right)$
- **(B)** $e\left(\dfrac{3e^2}{7} - \dfrac{1}{5}\right)$
- **(C)** $e^2\left(\dfrac{3e}{7} - \dfrac{1}{5}\right)$
- **(D)** $e\left(\dfrac{3e^2}{7} - \dfrac{e}{5}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $e\left(\dfrac{3e^2}{7} - \dfrac{1}{5}\right)$**

**Detailed Solution:**

The given integral is $I = \int_1^3 e^x \dfrac{(x+2)^2}{(x+4)^2}\,dx$

We can rewrite the algebraic part of the integrand as:

$\dfrac{(x+2)^2}{(x+4)^2} = \dfrac{x^2 + 4x + 4}{(x+4)^2} = \dfrac{x(x+4) + 4}{(x+4)^2} = \dfrac{x}{x+4} + \dfrac{4}{(x+4)^2}$

Let $f(x) = \dfrac{x}{x+4}$

Differentiating $f(x)$ with respect to $x$, we get:

$f'(x) = \dfrac{1 \cdot (x+4) - x \cdot 1}{(x+4)^2} = \dfrac{4}{(x+4)^2}$

The integral is now of the standard form $\int e^x [f(x) + f'(x)]\,dx = e^x f(x) + C$

Applying this to our definite integral:

$I = \left[ e^x \dfrac{x}{x+4} \right]_1^3$

Substituting the upper and lower limits:

$I = e^3 \left(\dfrac{3}{3+4}\right) - e^1 \left(\dfrac{1}{1+4}\right)$

$I = \dfrac{3e^3}{7} - \dfrac{e}{5}$

$I = e\left(\dfrac{3e^2}{7} - \dfrac{1}{5}\right)$

Answer: $e\left(\dfrac{3e^2}{7} - \dfrac{1}{5}\right)$

</details>

---

### Q2. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $n$ is an odd natural number and $I_n=\displaystyle\int_0^1 e^x(x-1)^n\,dx$, then the value of $I_n+nI_{n-1}$ is equal to ...

**Options:**

- **(A)** $2$
- **(B)** $0$
- **(C)** $1$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

Given $I_n = \displaystyle\int_0^1 e^x(x-1)^n\,dx$

Using integration by parts, taking $(x-1)^n$ as the first function and $e^x$ as the second function:

$I_n = \left[ (x-1)^n e^x \right]_0^1 - \displaystyle\int_0^1 n(x-1)^{n-1} e^x \, dx$

$I_n = \left( 0 - (-1)^n e^0 \right) - n I_{n-1}$

$I_n = -(-1)^n - n I_{n-1}$

Since $n$ is given as an odd natural number, $(-1)^n = -1$.

$I_n = -(-1) - n I_{n-1}$

$I_n = 1 - n I_{n-1}$

$I_n + n I_{n-1} = 1$

Answer: $1$

</details>

---

### Q3. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $I_n = \int_1^e (\log_e x)^n\,dx$ where $n \in Z^+$ and $I_m + mI_{2026} = e$, then $m = $

**Options:**

- **(A)** $2024$
- **(B)** $2025$
- **(C)** $2026$
- **(D)** $2027$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2027$**

**Detailed Solution:**

$I_n = \int_1^e (\log_e x)^n \, dx$

Using integration by parts, taking $1$ as the second function:

$I_n = \left[ x (\log_e x)^n \right]_1^e - \int_1^e x \cdot n (\log_e x)^{n-1} \cdot \dfrac{1}{x} \, dx$

$I_n = e (1)^n - 0 - n \int_1^e (\log_e x)^{n-1} \, dx$

$I_n = e - n I_{n-1}$

$I_n + n I_{n-1} = e$

Given $I_m + m I_{2026} = e$

Comparing the two equations, we get $n = m$ and $n-1 = 2026$.

$m - 1 = 2026 \Rightarrow m = 2027$

</details>

---

### Q4. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of integral $\int_0^1\cot^{-1}(1 + x^2 - x)\,dx$ is...

**Options:**

- **(A)** $\dfrac{\pi}{2} - \log 2$
- **(B)** $\pi - \log 2$
- **(C)** $\dfrac{\pi}{4} - \log 2$
- **(D)** $2\pi - \log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\pi}{2} - \log 2$**

**Detailed Solution:**

$I = \int_0^1 \cot^{-1}(1 + x^2 - x) \, dx$

$I = \int_0^1 \tan^{-1}\left(\dfrac{1}{1 + x(x - 1)}\right) \, dx$

$I = \int_0^1 \tan^{-1}\left(\dfrac{x - (x - 1)}{1 + x(x - 1)}\right) \, dx$

$I = \int_0^1 (\tan^{-1}x - \tan^{-1}(x - 1)) \, dx$

Using the property $\int_0^a f(x) \, dx = \int_0^a f(a - x) \, dx$ on the second term:

$\int_0^1 \tan^{-1}(x - 1) \, dx = \int_0^1 \tan^{-1}(1 - x - 1) \, dx = \int_0^1 \tan^{-1}(-x) \, dx = -\int_0^1 \tan^{-1}x \, dx$

$I = \int_0^1 \tan^{-1}x \, dx - \left(-\int_0^1 \tan^{-1}x \, dx\right) = 2\int_0^1 \tan^{-1}x \, dx$

Using integration by parts:

$I = 2 \left[ x \tan^{-1}x \right]_0^1 - 2 \int_0^1 \dfrac{x}{1 + x^2} \, dx$

$I = 2 \left( 1 \cdot \dfrac{\pi}{4} - 0 \right) - \left[ \log(1 + x^2) \right]_0^1$

$I = \dfrac{\pi}{2} - \log 2$

Answer: $\dfrac{\pi}{2} - \log 2$

</details>

---

### Q5. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^1 \log (x+1) \mathrm{d} x=$

**Options:**

- **(A)** $\log 2-1$
- **(B)** $\log 2+1$
- **(C)** $2 \log 2+1$
- **(D)** $2 \log 2-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 \log 2-1$**

**Detailed Solution:**

Let $I = \int_0^1 \log(x+1) \mathrm{d} x$

Substitute $t = x+1 \Rightarrow \mathrm{d}t = \mathrm{d}x$

When $x=0$, $t=1$ and when $x=1$, $t=2$

$I = \int_1^2 \log t \, \mathrm{d}t$

Using integration by parts, $\int \log t \, \mathrm{d}t = t \log t - t$

$I = [t \log t - t]_1^2$

$I = (2 \log 2 - 2) - (1 \log 1 - 1)$

Since $\log 1 = 0$,

$I = 2 \log 2 - 2 - (0 - 1)$

$I = 2 \log 2 - 1$

Answer: $2 \log 2-1$

</details>

---

### Q6. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^{\frac{\pi}{6}}\left(2+3 x^2\right) \cos 3 x d x=$

**Options:**

- **(A)** $\frac{4}{9}+\frac{\pi^2}{36}$
- **(B)** $\frac{2}{9}+\frac{\pi^2}{36}$
- **(C)** $\frac{2}{9}-\frac{\pi^2}{36}$
- **(D)** $\frac{4}{9}-\frac{\pi^2}{36}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{4}{9}+\frac{\pi^2}{36}$**

**Detailed Solution:**

Let $I = \int_0^{\dfrac{\pi}{6}} (2+3x^2) \cos 3x \, dx$

Using integration by parts, $\int u \, dv = uv - \int v \, du$.

Let $u = 2+3x^2$ and $dv = \cos 3x \, dx$. Then $du = 6x \, dx$ and $v = \dfrac{\sin 3x}{3}$.

$I = \left[ (2+3x^2) \dfrac{\sin 3x}{3} \right]_0^{\dfrac{\pi}{6}} - \int_0^{\dfrac{\pi}{6}} 6x \left( \dfrac{\sin 3x}{3} \right) dx$

$I = \left[ \dfrac{1}{3} (2+3x^2) \sin 3x \right]_0^{\dfrac{\pi}{6}} - \int_0^{\dfrac{\pi}{6}} 2x \sin 3x \, dx$

Applying the limits to the first term:

$\left[ \dfrac{1}{3} \left( 2 + 3\left(\dfrac{\pi}{6}\right)^2 \right) \sin\left(3 \times \dfrac{\pi}{6}\right) \right] - \left[ \dfrac{1}{3} (2 + 0) \sin(0) \right]$

$= \dfrac{1}{3} \left( 2 + \dfrac{\pi^2}{12} \right) \sin\left(\dfrac{\pi}{2}\right) - 0$

$= \dfrac{2}{3} + \dfrac{\pi^2}{36}$

Now, evaluate the second integral using integration by parts again:

$\int_0^{\dfrac{\pi}{6}} 2x \sin 3x \, dx = \left[ 2x \left( -\dfrac{\cos 3x}{3} \right) \right]_0^{\dfrac{\pi}{6}} - \int_0^{\dfrac{\pi}{6}} 2 \left( -\dfrac{\cos 3x}{3} \right) dx$

$= \left[ -\dfrac{2x}{3} \cos 3x \right]_0^{\dfrac{\pi}{6}} + \dfrac{2}{3} \int_0^{\dfrac{\pi}{6}} \cos 3x \, dx$

Applying the limits:

$= \left( -\dfrac{\pi}{9} \cos\left(\dfrac{\pi}{2}\right) - 0 \right) + \dfrac{2}{3} \left[ \dfrac{\sin 3x}{3} \right]_0^{\dfrac{\pi}{6}}$

$= 0 + \dfrac{2}{9} \left( \sin\left(\dfrac{\pi}{2}\right) - \sin(0) \right)$

$= \dfrac{2}{9} (1 - 0) = \dfrac{2}{9}$

Substitute this back into $I$:

$I = \left( \dfrac{2}{3} + \dfrac{\pi^2}{36} \right) - \dfrac{2}{9}$

$I = \dfrac{6}{9} - \dfrac{2}{9} + \dfrac{\pi^2}{36} = \dfrac{4}{9} + \dfrac{\pi^2}{36}$

Answer: $\frac{4}{9}+\frac{\pi^2}{36}$

</details>

---

### Q7. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^1 \tan ^{-1} x d x=$

**Options:**

- **(A)** $\frac{\pi}{4}-\log 2$
- **(B)** $\frac{\pi}{4}-\log \sqrt{2}$
- **(C)** $\frac{\pi}{4}+\log 2$
- **(D)** $\frac{\pi}{4}+\log \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{4}-\log \sqrt{2}$**

**Detailed Solution:**

Let $I = \int_0^1 \tan^{-1} x \, dx$

Using integration by parts, taking $1$ as the second function:

$I = \left[x \tan^{-1} x\right]_0^1 - \int_0^1 x \cdot \dfrac{1}{1+x^2} \, dx$

$I = \left(1 \cdot \dfrac{\pi}{4} - 0\right) - \dfrac{1}{2} \int_0^1 \dfrac{2x}{1+x^2} \, dx$

$I = \dfrac{\pi}{4} - \dfrac{1}{2} \left[\log(1+x^2)\right]_0^1$

$I = \dfrac{\pi}{4} - \dfrac{1}{2} (\log 2 - \log 1)$

$I = \dfrac{\pi}{4} - \dfrac{1}{2} \log 2$

$I = \dfrac{\pi}{4} - \log \sqrt{2}$

Answer: $\frac{\pi}{4}-\log \sqrt{2}$

</details>

---

### Q8. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int_{\dfrac{-\pi}{2}}^{\dfrac{\pi}{2}}\left(x^2+\log \dfrac{\pi-x}{\pi+x}\right) \cos x d x$ is equal to

**Options:**

- **(A)** 0
- **(B)** $\dfrac{\pi^2}{2}-4$
- **(C)** $\dfrac{\pi^2}{2}$
- **(D)** $\dfrac{\pi^2}{2}+4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\pi^2}{2}-4$**

**Detailed Solution:**

Let the given integral be $I = \int_{-\pi/2}^{\pi/2} \left(x^2 + \log \dfrac{\pi-x}{\pi+x}\right) \cos x \, dx$.

We can split the integral into two parts:

$I = \int_{-\pi/2}^{\pi/2} x^2 \cos x \, dx + \int_{-\pi/2}^{\pi/2} \log \left(\dfrac{\pi-x}{\pi+x}\right) \cos x \, dx$

Let $f(x) = \log \left(\dfrac{\pi-x}{\pi+x}\right) \cos x$.

$f(-x) = \log \left(\dfrac{\pi+x}{\pi-x}\right) \cos(-x) = -\log \left(\dfrac{\pi-x}{\pi+x}\right) \cos x = -f(x)$

Since $f(x)$ is an odd function, $\int_{-\pi/2}^{\pi/2} f(x) \, dx = 0$.

Also, $x^2 \cos x$ is an even function, so:

$I = 2 \int_{0}^{\pi/2} x^2 \cos x \, dx$

Using integration by parts:

$I = 2 \left[ x^2 \sin x - \int 2x \sin x \, dx \right]_{0}^{\pi/2}$

$I = 2 \left[ x^2 \sin x - 2 \left( -x \cos x + \int \cos x \, dx \right) \right]_{0}^{\pi/2}$

$I = 2 \left[ x^2 \sin x + 2x \cos x - 2 \sin x \right]_{0}^{\pi/2}$

Evaluating the limits:

$I = 2 \left( \left( \dfrac{\pi^2}{4}(1) + 0 - 2(1) \right) - (0 + 0 - 0) \right)$

$I = 2 \left( \dfrac{\pi^2}{4} - 2 \right) = \dfrac{\pi^2}{2} - 4$

Answer: $\dfrac{\pi^2}{2}-4$

</details>

---

### Q9. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^1 \cos ^{-1} x d x=$

**Options:**

- **(A)** $-1$
- **(B)** $0$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

Let
$\begin{aligned}
\mathrm{I} & =\int_0^1\left(\cos ^{-1} x\right)(1) \mathrm{d} x \\
& =\left[\cos ^{-1} x \cdot x-\int\left(\frac{-1}{\sqrt{1-x^2}} \cdot x\right) \mathrm{d} x\right]_0^1 \\
& =\left[x \cdot \cos ^{-1} x+\int \frac{x}{\sqrt{1-x^2}} \mathrm{~d} x\right]_0^1 \\
& =\left[x \cos ^{-1} x-\sqrt{1-x^2}\right]_0^1 \\
& =\left[1 \cdot \cos ^{-1}(1)-\sqrt{1-(1)^2}\right]-\left[0 \cdot \cos ^{-1}(0)-\sqrt{1-0^2}\right] \\
& =0-(-1) \\
& =1
\end{aligned}$

</details>

---

### Q10. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\int \cos \left(\log _e(x)\right) \mathrm{d} x$ is equal to (where $C$ is a constant of integration.)

**Options:**

- **(A)** $x[\cos (\log x)-\sin (\log x)]+C$
- **(B)** $\frac{x}{2}[\sin (\log x)-\cos (\log x)]+C$
- **(C)** $\frac{x}{2}[\sin (\log x)+\cos (\log x)]+C$
- **(D)** $x[\cos (\log x)+\sin (\log x)]+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{x}{2}[\sin (\log x)+\cos (\log x)]+C$**

**Detailed Solution:**

$\begin{aligned} & \int \cos \left(\log _{\mathrm{e}} x\right) \mathrm{d} x \operatorname{let}_{\log _{\mathrm{e}} x=t} \\ & \Rightarrow \mathrm{d} x=e^t \\ & \Rightarrow I=\int \cos t \cdot e^t \mathrm{~d} t=\cos t \cdot e^t+\sin t \cdot e^t-I \quad[\text { Integrating by parts] } \\ & \Rightarrow 2 I=e^t(\cos t+\sin t) \\ & \Rightarrow I=\frac{x}{2}\left\{\cos \left(\log _{\mathrm{e}} x\right)+\sin \left(\log _{\mathrm{e}} x\right)\right\}\end{aligned}$

</details>

---

### Q11. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{0}^{\frac{\pi}{2}} \log \left[\sqrt{\frac{1-\cos 2 x}{1+\cos 2 x}}\right] d x=$

**Options:**

- **(A)** 1
- **(B)** $\frac{\pi}{4}$
- **(C)** 0
- **(D)** $\frac{\pi}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

(C)
$\int_{0}^{\frac{\pi}{2}} \log \sqrt{\frac{2 \sin ^{2} x}{2 \cos ^{2} x}} d x$
$=\int_{0}^{\pi / 2} \log \left(\frac{\sin x}{\cos x}\right) d x \Rightarrow \int_{0}^{\pi / 2} \log (\tan x) d x$...(1)
$=\int_{0}^{\pi / 2}\left[\tan \left(\frac{\pi}{2}-x\right)\right] d x=\int_{0}^{\pi / 2} \log \cot x d x$...(2)
Eq. (1) $+(2)$ gives
$\begin{aligned}
2 \mathrm{I} &=\int_{0}^{\pi / 2}[\log (\tan \mathrm{x})+\log (\cot \mathrm{x})] \mathrm{dx}=\int_{0}^{\pi / 2} \log [\tan \mathrm{x} \cot \mathrm{x}] \mathrm{d} \mathrm{x} \\
&=\int_{0}^{\pi / 2} \log 1 \mathrm{dx}=0 \Rightarrow \mathrm{I}=0
\end{aligned}$

</details>

---

### Q12. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `2`

<math><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></munderover><mrow><mi>x</mi><mo>.</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi mathvariant="normal"> </mi></mrow></mrow></mrow></mrow></math>

**Options:**

- **(A)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><msqrt><mn>2</mn></msqrt></mrow></mrow></math>
- **(B)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><msqrt><mn>2</mn></msqrt></mrow></mrow></math>
- **(C)** <math><mn>1</mn><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><msqrt><mn>2</mn></msqrt></mrow></mrow></math>
- **(D)** <math><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><msqrt><mn>2</mn></msqrt></mrow></mrow></math>**

**Detailed Solution:**

Integrating by parts
<math> <mrow> <mstyle displaystyle="true"> <mrow> <msubsup> <mo>∫</mo> <mn>0</mn> <mrow> <mfrac> <mi>π</mi> <mn>4</mn> </mfrac> </mrow> </msubsup> <mrow> <mi>x</mi><mtext> </mtext><msup> <mrow> <mi>sec</mi></mrow> <mn>2</mn> </msup> <mi>x</mi><mtext> </mtext><mi>d</mi><mi>x</mi></mrow> </mrow> </mstyle><mo>=</mo><msubsup> <mrow> <mrow><mo>(</mo> <mrow> <mi>x</mi><mstyle displaystyle="true"> <mrow><mo>∫</mo> <mrow> <msup> <mrow> <mi>sec</mi></mrow> <mn>2</mn> </msup> <mi>x</mi><mi>d</mi><mi>x</mi></mrow> </mrow> </mstyle></mrow> <mo>)</mo></mrow></mrow> <mn>0</mn> <mrow> <mfrac> <mi>π</mi> <mn>4</mn> </mfrac> </mrow> </msubsup> <mo>−</mo><mstyle displaystyle="true"> <mrow> <msubsup> <mo>∫</mo> <mn>0</mn> <mrow> <mfrac> <mi>π</mi> <mn>4</mn> </mfrac> </mrow> </msubsup> <mrow> <mrow><mo>(</mo> <mrow> <mfrac> <mi>d</mi> <mrow> <mi>d</mi><mi>x</mi></mrow> </mfrac> <mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>.</mo><mstyle displaystyle="true"> <mrow><mo>∫</mo> <mrow> <msup> <mrow> <mi>sec</mi></mrow> <mn>2</mn> </msup> <mi>x</mi></mrow> </mrow> </mstyle><mtext> </mtext><mi>d</mi><mi>x</mi></mrow> <mo>)</mo></mrow><mi>d</mi><mi>x</mi></mrow> </mrow> </mstyle></mrow> </math>
<math> <mrow> <mo>=</mo><msubsup> <mrow> <mrow><mo>(</mo> <mrow> <mi>x</mi><mi>tan</mi><mi>x</mi></mrow> <mo>)</mo></mrow></mrow> <mn>0</mn> <mrow> <mfrac> <mi>π</mi> <mn>4</mn> </mfrac> </mrow> </msubsup> <mo>−</mo><mstyle displaystyle="true"> <mrow> <msubsup> <mo>∫</mo> <mn>0</mn> <mrow> <mfrac> <mi>π</mi> <mn>4</mn> </mfrac> </mrow> </msubsup> <mrow> <mi>tan</mi><mi>x</mi><mtext> </mtext><mi>d</mi><mi>x</mi></mrow> </mrow> </mstyle></mrow> </math>
<math> <mrow> <mo>&rArr;</mo><mtext>I</mtext> <mo>=</mo> <msubsup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mi>x</mi> <mtext>tan</mtext> <mi>x</mi> <mo>-</mo> <mi>ℓ</mi> <mi>n</mi> <mtext>sec</mtext> <mi>x</mi> </mrow> </mfenced> </mrow> <mn>0</mn> <mfrac> <mrow> <mi>π</mi> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </msubsup> <mo>=</mo> <mfrac> <mrow> <mi>π</mi> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> </mrow> </mfenced> <mo>-</mo> <mi>ℓ</mi> <mi>n</mi> <msqrt> <mn>2</mn> </msqrt> </mrow> </math>
<math> <mrow> <mo>=</mo> <mfrac> <mrow> <mi>π</mi> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mo>-</mo> <mtext>log</mtext> <msqrt> <mn>2</mn> </msqrt> </mrow> </math>

</details>

---

### Q13. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int_{\pi / 4}^{\pi / 2} e^{x}(\log \sin x+\cot x) d x$ is

**Options:**

- **(A)** $e^{\pi / 4} \log 2$
- **(B)** $-e^{\pi / 4} \log 2$
- **(C)** $\frac{1}{2} e^{\pi / 4} \log 2$
- **(D)** $-\frac{1}{2} e^{\pi / 4} \log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2} e^{\pi / 4} \log 2$**

**Detailed Solution:**

Let 
$\begin{array}{rl}I=\int_{\pi / 4}^{\pi / 2} e^{x}(\log \sin x & +\cot x) d x \\ \Rightarrow I=\int_{\pi / 4}^{\pi / 2} e^{x} \log \sin x & d x \\ +\int_{\pi / 4}^{\pi / 2} e^{x} \cot x d x \\ =\int_{\pi / 4}^{\pi / 2} e^{x} \log \sin x d x+\left[e^{x} \log \sin x\right]_{\pi / 4}^{\pi / 2} \\ -\int_{\pi / 4}^{\pi / 2} e^{x} \log \sin x d x \\ = & e^{\pi / 2} \log \sin \frac{\pi}{2}-e^{\pi / 4} \log \sin \frac{\pi}{4} \\ = & -e^{\pi / 4} \log \left(\frac{1}{\sqrt{2}}\right) \\ = & \frac{1}{2} e^{\pi / 4} \log 2\end{array}$

</details>

---

