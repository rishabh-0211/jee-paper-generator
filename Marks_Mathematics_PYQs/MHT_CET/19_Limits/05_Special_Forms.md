# MHT CET Mathematics - Limits

## Topic 5: Special Forms

**Total Questions:** 9

---

### Q1. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\lim_{x \to 0}\left(\dfrac{f(x)}{x^2}\right)$ exists finitely and $\lim_{x \to 0}\left(1 + x + \dfrac{f(x)}{x}\right)^{1/x} = e^3$, then $\int f(x) \cdot \log x\,dx$ is equal to:

**Options:**

- **(A)** $\dfrac{2}{9}x^3(3\log x - 1) + c$
- **(B)** $\dfrac{1}{9}x^3(3\log x - 1) + c$
- **(C)** $\dfrac{2}{9}x^3(3\log x + 1) + c$
- **(D)** $\dfrac{2}{9}x^3(3\log x - 1/3) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{2}{9}x^3(3\log x - 1) + c$**

**Detailed Solution:**

Given that $\lim_{x \to 0}\left(\dfrac{f(x)}{x^2}\right)$ exists finitely, let $\lim_{x \to 0}\dfrac{f(x)}{x^2} = L$.

Then $\lim_{x \to 0}\dfrac{f(x)}{x} = \lim_{x \to 0}\left(x \cdot \dfrac{f(x)}{x^2}\right) = 0 \cdot L = 0$.

The given limit is of the form $1^{\infty}$:

$\lim_{x \to 0}\left(1 + x + \dfrac{f(x)}{x}\right)^{1/x} = e^{\lim_{x \to 0} \dfrac{1}{x} \left(1 + x + \dfrac{f(x)}{x} - 1\right)}$

$= e^{\lim_{x \to 0} \left(1 + \dfrac{f(x)}{x^2}\right)} = e^{1 + L}$

We are given that this limit is equal to $e^3$.

$e^{1 + L} = e^3 \Rightarrow 1 + L = 3 \Rightarrow L = 2$

Thus, $\lim_{x \to 0}\dfrac{f(x)}{x^2} = 2$. For the integral to match the given options, we take $f(x) = 2x^2$.

Now, we evaluate the integral $\int f(x) \log x \,dx = \int 2x^2 \log x \,dx$.

Using integration by parts, taking $\log x$ as the first function and $2x^2$ as the second function:

$\int 2x^2 \log x \,dx = \log x \int 2x^2 \,dx - \int \left( \dfrac{d}{dx}(\log x) \int 2x^2 \,dx \right) dx$

$= \log x \left(\dfrac{2x^3}{3}\right) - \int \dfrac{1}{x} \left(\dfrac{2x^3}{3}\right) dx$

$= \dfrac{2}{3}x^3 \log x - \int \dfrac{2}{3}x^2 \,dx$

$= \dfrac{2}{3}x^3 \log x - \dfrac{2}{9}x^3 + c$

$= \dfrac{2}{9}x^3(3\log x - 1) + c$

Answer: $\dfrac{2}{9}x^3(3\log x - 1) + c$

</details>

---

### Q2. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{A}=\lim _{\mathrm{x} \rightarrow 0^{+}}\left(1+\tan ^2 \sqrt{x}\right)^{\frac{1}{2 x}}$, then $\log _{\mathrm{e}} \mathrm{A}=$

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2}$**

**Detailed Solution:**

Given $\mathrm{A} = \lim_{\mathrm{x} \rightarrow 0^{+}} \left(1+\tan^2 \sqrt{x}\right)^{\dfrac{1}{2x}}$

As $x \rightarrow 0^{+}$, the limit is of the form $1^{\infty}$.

Using the standard result $\lim_{x \rightarrow a} (1+f(x))^{g(x)} = e^{\lim_{x \rightarrow a} f(x)g(x)}$ for $1^{\infty}$ forms:

$\mathrm{A} = e^{\lim_{x \rightarrow 0^{+}} \left(\tan^2 \sqrt{x}\right) \left(\dfrac{1}{2x}\right)}$

$\mathrm{A} = e^{\dfrac{1}{2} \lim_{x \rightarrow 0^{+}} \left(\dfrac{\tan \sqrt{x}}{\sqrt{x}}\right)^2}$

Since $\lim_{\theta \rightarrow 0} \dfrac{\tan \theta}{\theta} = 1$, we get:

$\mathrm{A} = e^{\dfrac{1}{2} (1)^2} = e^{\dfrac{1}{2}}$

Taking the natural logarithm on both sides:

$\log_{\mathrm{e}} \mathrm{A} = \log_{\mathrm{e}} \left(e^{\dfrac{1}{2}}\right) = \dfrac{1}{2}$

Answer: $\frac{1}{2}$

</details>

---

### Q3. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow 1}\left(\log _3 3 x\right)^{\log _x 8}=\ldots$

**Options:**

- **(A)** $e^{\log _3 8}$
- **(B)** $\log _8 3$
- **(C)** $e^{\log _8 3}$
- **(D)** $\log _3 8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $e^{\log _3 8}$**

**Detailed Solution:**

Let $L = \lim_{x \rightarrow 1} (\log_3 3x)^{\log_x 8}$

Using the properties of logarithms, we can write $\log_3 3x = \log_3 3 + \log_3 x = 1 + \log_3 x$.

Also, using the change of base formula, $\log_x 8 = \dfrac{\log_3 8}{\log_3 x}$.

Substituting these into the limit, we get:

$L = \lim_{x \rightarrow 1} (1 + \log_3 x)^{\dfrac{\log_3 8}{\log_3 x}}$

Let $t = \log_3 x$. As $x \rightarrow 1$, $t \rightarrow 0$. The limit becomes:

$L = \lim_{t \rightarrow 0} (1 + t)^{\dfrac{\log_3 8}{t}}$

$L = \lim_{t \rightarrow 0} \left[ (1 + t)^{\dfrac{1}{t}} \right]^{\log_3 8}$

Using the standard limit $\lim_{t \rightarrow 0} (1 + t)^{\dfrac{1}{t}} = e$, we obtain:

$L = e^{\log_3 8}$

Answer: $e^{\log _3 8}$

</details>

---

### Q4. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow \infty}\left(\frac{x+8}{x+1}\right)^{x+5}=\ldots$

**Options:**

- **(A)** $e^4$
- **(B)** $\mathrm{e}^5$
- **(C)** $\mathrm{e}^{11}$
- **(D)** $\mathrm{e}^7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{e}^7$**

**Detailed Solution:**

Let $L = \lim_{x \rightarrow \infty} \left(\dfrac{x+8}{x+1}\right)^{x+5}$

Rewriting the expression inside the limit:

$L = \lim_{x \rightarrow \infty} \left(1 + \dfrac{7}{x+1}\right)^{x+5}$

This is of the form $1^\infty$. Using the standard result $\lim_{x \rightarrow \infty} (1 + f(x))^{g(x)} = e^{\lim_{x \rightarrow \infty} f(x)g(x)}$ where $f(x) \rightarrow 0$ and $g(x) \rightarrow \infty$, we get:

$L = e^{\lim_{x \rightarrow \infty} \left(\dfrac{7}{x+1}\right)(x+5)}$

$L = e^{\lim_{x \rightarrow \infty} \dfrac{7(x+5)}{x+1}}$

Dividing the numerator and the denominator by $x$:

$L = e^{\lim_{x \rightarrow \infty} \dfrac{7(1+5/x)}{1+1/x}}$

As $x \rightarrow \infty$, $\dfrac{1}{x} \rightarrow 0$.

$L = e^{\dfrac{7(1+0)}{1+0}} = e^7$

Answer: $\mathrm{e}^7$

</details>

---

### Q5. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(x)=\left(\dfrac{1+\tan x}{1+\sin x}\right)^{\operatorname{cosec} x}$ is continuous at $x=0$, then $f(0)$ is equal to

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** e
- **(D)** $\dfrac{1}{\mathrm{e}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

Since $f(x)$ is continuous at $x=0$, $f(0) = \lim_{x \to 0} f(x)$.

$f(0) = \lim_{x \to 0} \left(\dfrac{1+\tan x}{1+\sin x}\right)^{\operatorname{cosec} x}$

This limit is of the form $1^{\infty}$. Using the standard result $\lim_{x \to a} u(x)^{v(x)} = e^{\lim_{x \to a} v(x)(u(x)-1)}$:

$f(0) = e^{\lim_{x \to 0} \operatorname{cosec} x \left(\dfrac{1+\tan x}{1+\sin x} - 1\right)}$

$f(0) = e^{\lim_{x \to 0} \dfrac{1}{\sin x} \left(\dfrac{\tan x - \sin x}{1+\sin x}\right)}$

$f(0) = e^{\lim_{x \to 0} \dfrac{1}{\sin x} \dfrac{\sin x (1 - \cos x)}{\cos x (1+\sin x)}}$

$f(0) = e^{\lim_{x \to 0} \dfrac{1 - \cos x}{\cos x (1+\sin x)}}$

Substituting $x = 0$:

$f(0) = e^{\dfrac{1 - 1}{1(1+0)}} = e^0 = 1$

Answer: 1

</details>

---

### Q6. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 2}\left(\frac{5 x-8}{8-3 x}\right)^{\frac{3}{2 x-4}}=$

**Options:**

- **(A)** $e^{5 / 2}$
- **(B)** $\mathrm{e}^{3 / 2}$
- **(C)** $\mathrm{e}^2$
- **(D)** $\mathrm{e}^6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{e}^6$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 2}\left(\frac{5 x-8}{8-3 x}\right) \frac{3}{2 x-4}=e^{\lim _{x \rightarrow 2}\left(\frac{5 x-8}{8-3 x}-1\right) \times \frac{3}{2 x-4}} \\ & =e^{\lim _{x \rightarrow 2} \frac{8(x-2) \times 3}{(8-3 x) 2(x-2)}}=e^6 \\ & \end{aligned}$

</details>

---

### Q7. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow 0}\left(\frac{1+\tan x}{1+\sin x}\right)^{\operatorname{cosec} x}=$

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** e
- **(D)** $\frac{1}{\mathrm{e}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 0}\left(\frac{1+\tan x}{1+\sin x}\right)^{\operatorname{cosec} x}=e^{\lim _{x \rightarrow 0}\left(\frac{1+\tan x}{1+\sin x}-1\right) \operatorname{cosec} x} \\ & =e^{\lim _{x \rightarrow 0}\left\{\frac{\tan x-\sin x}{1+\sin x} \cdot \frac{1}{\sin x}\right\}} \\ & \left.=e^{\lim _{x \rightarrow 0}\left\{\frac{\frac{1}{\cos x}-1}{1+\sin x}\right.}\right\} \\ & =\mathrm{e}^0=1 \\ & \end{aligned}$

</details>

---

### Q8. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

If $a, b, c$ and $d$ are positive, then
is equal

**Options:**

- **(A)** $e^{d / b}$
- **(B)** $e^{c / a}$
- **(C)** $e^{(c+d) /(a+b)}$
- **(D)** $\underline{e}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $e^{d / b}$**

**Detailed Solution:**

$L=\lim _{x \rightarrow \infty}\left(1+\frac{1}{a+b x}\right)^{c+d x} \quad\left[\right.$ form $\left.(1)^{\infty}\right]$
$$
\begin{aligned}
&=e^{\lim _{x \rightarrow \infty} \frac{c+d x}{a+b x}}=e^{\lim _{x \rightarrow \infty} \frac{c / x+d}{a / x+b}} \\
=& e^{\frac{0+d}{0+b}}=e^{d / b}
\end{aligned}
$$

</details>

---

### Q9. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

The value of $\lim _{x \rightarrow \infty}\left(\frac{x^{2}-2 x+1}{x^{2}-4 x+2}\right)^{x}$ is

**Options:**

- **(A)** $e^{2}$
- **(B)** $e^{-2}$
- **(C)** $e^{6}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $e^{2}$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow \infty}\left(\frac{x^{2}-2 x+1}{x^{2}-4 x+2}\right)^{x} \\ &=\lim _{x \rightarrow \infty}\left(1+\frac{2 x-1}{x^{2}-4 x+2}\right)^{x} \\ &=e^{\lim _{x \rightarrow-\infty}\left(\frac{x(2 x-1)}{x^{2}-4 x+2}\right)}=e^{2} \end{aligned}$

</details>

---

