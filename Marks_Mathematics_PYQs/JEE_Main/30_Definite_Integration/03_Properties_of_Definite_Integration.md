# JEE Main Mathematics - Definite Integration

## Topic 3: Properties of Definite Integration

**Total Questions:** 143

---

### Q1. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int\limits_{-1}^{1} \left(\dfrac{x^3 + |x| + 1}{x^2 + 2|x| + 1}\right) dx$ is equal to :

**Options:**

- **(A)** $3\log_e 2$
- **(B)** $2\log_e 2$
- **(C)** $5\log_e 3$
- **(D)** $3\log_e 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2\log_e 2$**

**Detailed Solution:**

Let $I = \int_{-1}^{1} \left(\dfrac{x^3 + |x| + 1}{x^2 + 2|x| + 1}\right) dx$

We can split the integral into two parts:

$I = \int_{-1}^{1} \dfrac{x^3}{x^2 + 2|x| + 1} dx + \int_{-1}^{1} \dfrac{|x| + 1}{x^2 + 2|x| + 1} dx$

The first integrand $f(x) = \dfrac{x^3}{x^2 + 2|x| + 1}$ is an odd function since $f(-x) = -f(x)$. Therefore, its integral over the symmetric interval $[-1, 1]$ is zero.

The second integrand $g(x) = \dfrac{|x| + 1}{x^2 + 2|x| + 1}$ is an even function since $g(-x) = g(x)$. Therefore, its integral over $[-1, 1]$ is twice the integral over $[0, 1]$.

$I = 0 + 2 \int_{0}^{1} \dfrac{x + 1}{x^2 + 2x + 1} dx$

$I = 2 \int_{0}^{1} \dfrac{x + 1}{(x + 1)^2} dx$

$I = 2 \int_{0}^{1} \dfrac{1}{x + 1} dx$

$I = 2 [\log_e(x + 1)]_{0}^{1}$

$I = 2(\log_e 2 - \log_e 1) = 2\log_e 2$

Answer: $2\log_e 2$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A = \begin{bmatrix} 1 & 3 & -1 \\ 2 & 1 & \alpha \\ 0 & 1 & -1 \end{bmatrix}$ be a singular matrix. Let $f(x) = \int\limits_0^x (t^2 + 2t + 3)\,dt$, $x \in [1, \alpha]$. If $M$ and $m$ are respectively the maximum and the minimum values of $f$ in $[1, \alpha]$, then $3(M - m)$ is equal to :

**Options:**

- **(A)** $64$
- **(B)** $68$
- **(C)** $72$
- **(D)** $76$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $68$**

**Detailed Solution:**

Since $A$ is a singular matrix, $|A| = 0$.

$|A| = 1(-1 - \alpha) - 3(-2 - 0) - 1(2 - 0) = 0$

$-1 - \alpha + 6 - 2 = 0 \Rightarrow \alpha = 3$

The function is $f(x) = \int\limits_0^x (t^2 + 2t + 3)\,dt = \dfrac{x^3}{3} + x^2 + 3x$

Differentiating with respect to $x$, we get $f'(x) = x^2 + 2x + 3 = (x+1)^2 + 2 > 0$ for all $x$.

Thus, $f(x)$ is a strictly increasing function on the interval $[1, 3]$.

The maximum value $M$ occurs at $x = 3$:

$M = f(3) = \dfrac{3^3}{3} + 3^2 + 3(3) = 9 + 9 + 9 = 27$

The minimum value $m$ occurs at $x = 1$:

$m = f(1) = \dfrac{1^3}{3} + 1^2 + 3(1) = \dfrac{13}{3}$

We need to find $3(M - m)$:

$3(M - m) = 3\left(27 - \dfrac{13}{3}\right) = 81 - 13 = 68$

Answer: $68$

</details>

---

### Q3. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int_{-\pi/4}^{\pi/4}\left(\dfrac{32\cos^4 x}{1 + e^{\sin x}}\right)dx$ is:

**Options:**

- **(A)** $4\pi + 2$
- **(B)** $3\pi + 8$
- **(C)** $3\pi + 4$
- **(D)** $4\pi + 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3\pi + 8$**

**Detailed Solution:**

Let $I = \int_{-\pi/4}^{\pi/4} \dfrac{32\cos^4 x}{1 + e^{\sin x}} dx$

Using the definite integral property $\int_{-a}^{a} f(x) dx = \int_{0}^{a} (f(x) + f(-x)) dx$, we get:

$I = \int_{0}^{\pi/4} \left( \dfrac{32\cos^4 x}{1 + e^{\sin x}} + \dfrac{32\cos^4(-x)}{1 + e^{\sin(-x)}} \right) dx$

$I = \int_{0}^{\pi/4} \left( \dfrac{32\cos^4 x}{1 + e^{\sin x}} + \dfrac{32\cos^4 x}{1 + e^{-\sin x}} \right) dx$

$I = \int_{0}^{\pi/4} \left( \dfrac{32\cos^4 x}{1 + e^{\sin x}} + \dfrac{32\cos^4 x \cdot e^{\sin x}}{e^{\sin x} + 1} \right) dx$

$I = \int_{0}^{\pi/4} 32\cos^4 x \left( \dfrac{1 + e^{\sin x}}{1 + e^{\sin x}} \right) dx$

$I = \int_{0}^{\pi/4} 32\cos^4 x dx$

Using the trigonometric identity $\cos^2 x = \dfrac{1 + \cos 2x}{2}$, we can write:

$\cos^4 x = \left( \dfrac{1 + \cos 2x}{2} \right)^2 = \dfrac{1}{4} (1 + 2\cos 2x + \cos^2 2x)$

$\cos^4 x = \dfrac{1}{4} \left( 1 + 2\cos 2x + \dfrac{1 + \cos 4x}{2} \right) = \dfrac{3}{8} + \dfrac{1}{2}\cos 2x + \dfrac{1}{8}\cos 4x$

Substituting this back into the integral:

$I = 32 \int_{0}^{\pi/4} \left( \dfrac{3}{8} + \dfrac{1}{2}\cos 2x + \dfrac{1}{8}\cos 4x \right) dx$

$I = \int_{0}^{\pi/4} (12 + 16\cos 2x + 4\cos 4x) dx$

Integrating term by term:

$I = \left[ 12x + 8\sin 2x + \sin 4x \right]_{0}^{\pi/4}$

$I = \left( 12\left(\dfrac{\pi}{4}\right) + 8\sin\left(\dfrac{\pi}{2}\right) + \sin(\pi) \right) - (0 + 0 + 0)$

$I = 3\pi + 8(1) + 0 = 3\pi + 8$

Answer: $3\pi + 8$

</details>

---

### Q4. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\displaystyle\int_{-2}^{2} (|\sin x| + [x \sin x])\,dx = 2(3 - \cos 2) + \beta$, where $[\cdot]$ is the greatest integer function. Then $\beta \sin\left(\dfrac{\beta}{2}\right)$ equals:

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $4$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$**

**Detailed Solution:**

Let $I = \displaystyle\int_{-2}^{2} \left(|\sin x| + [x \sin x]\right) dx = I_1 + I_2$, where
$I_1 = \displaystyle\int_{-2}^{2} |\sin x|\, dx$ and $I_2 = \displaystyle\int_{-2}^{2} [x \sin x]\, dx$.

Evaluating $I_1$:
Since $|\sin x|$ is even, $I_1 = 2\displaystyle\int_{0}^{2} |\sin x|\, dx$.
For $x \in [0, 2]$, $2 < \pi$, so $\sin x \geq 0$ and $|\sin x| = \sin x$.
$I_1 = 2\displaystyle\int_{0}^{2} \sin x\, dx = 2\left[-\cos x\right]_0^2 = 2(1 - \cos 2) = 2 - 2\cos 2$

Evaluating $I_2$:
Let $g(x) = x\sin x$. Then $g(-x) = (-x)\sin(-x) = x\sin x = g(x)$, so $g(x)$ is even, and hence $[x\sin x]$ is also even.
$I_2 = 2\displaystyle\int_{0}^{2} [x\sin x]\, dx$

Behaviour of $y = x\sin x$ on $[0, 2]$:
At $x = 0$, $y = 0$. At $x = 2$, $y = 2\sin 2 \approx 1.818$.
$y' = \sin x + x\cos x > 0$ on $[0, 2]$, so $y$ is strictly increasing on this interval.

Therefore, $x\sin x$ takes each value in $[0, 1.818]$ exactly once, and crosses $1$ at some unique $\alpha \in (0, 2)$ with $\alpha\sin\alpha = 1$.

For $x \in [0, \alpha)$: $0 \leq x\sin x < 1 \Rightarrow [x\sin x] = 0$
For $x \in [\alpha, 2]$: $1 \leq x\sin x < 2 \Rightarrow [x\sin x] = 1$

$I_2 = 2\left(\displaystyle\int_{0}^{\alpha} 0\, dx + \displaystyle\int_{\alpha}^{2} 1\, dx\right) = 2(2 - \alpha) = 4 - 2\alpha$

Combining:
$I = I_1 + I_2 = (2 - 2\cos 2) + (4 - 2\alpha) = 6 - 2\cos 2 - 2\alpha$

Given $I = 2(3 - \cos 2) + \beta = 6 - 2\cos 2 + \beta$, so:
$6 - 2\cos 2 - 2\alpha = 6 - 2\cos 2 + \beta \Rightarrow \beta = -2\alpha$

Now:
$\beta \sin\left(\dfrac{\beta}{2}\right) = -2\alpha \sin\left(\dfrac{-2\alpha}{2}\right) = -2\alpha \sin(-\alpha) = 2\alpha\sin\alpha$

Since $\alpha\sin\alpha = 1$:
$\beta \sin\left(\dfrac{\beta}{2}\right) = 2 \cdot 1 = 2$

Hence, the correct option is $(2)\ 2$.

</details>

---

### Q5. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $[\cdot]$ denote the greatest integer function. Then the value of $\displaystyle\int_0^3 \left(\dfrac{e^x + e^{-x}}{[x]!}\right) dx$ is :

**Options:**

- **(A)** $e^2 + e^3 - \dfrac{1}{e^2} - \dfrac{1}{e^3}$
- **(B)** $\dfrac{1}{2}\left(e^2 + e^3 - \dfrac{1}{e^2} - \dfrac{1}{e^3}\right)$
- **(C)** $e^2 + e^3 - \dfrac{1}{2e^2} - \dfrac{1}{2e^3}$
- **(D)** $\dfrac{1}{2}(e^2 + e^3) - \dfrac{1}{e^2} - \dfrac{1}{e^3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{2}\left(e^2 + e^3 - \dfrac{1}{e^2} - \dfrac{1}{e^3}\right)$**

**Detailed Solution:**

The given integral can be split at integer values of $x$ because of the greatest integer function $[x]$.

$\displaystyle I = \int_0^3 \left(\dfrac{e^x + e^{-x}}{[x]!}\right) dx$

$\displaystyle I = \int_0^1 \dfrac{e^x + e^{-x}}{0!} dx + \int_1^2 \dfrac{e^x + e^{-x}}{1!} dx + \int_2^3 \dfrac{e^x + e^{-x}}{2!} dx$

Since $0! = 1$, $1! = 1$, and $2! = 2$, we get:

$\displaystyle I = \int_0^2 (e^x + e^{-x}) dx + \dfrac{1}{2} \int_2^3 (e^x + e^{-x}) dx$

Integrating the terms:

$\displaystyle I = \left[ e^x - e^{-x} \right]_0^2 + \dfrac{1}{2} \left[ e^x - e^{-x} \right]_2^3$

$\displaystyle I = (e^2 - e^{-2} - (1 - 1)) + \dfrac{1}{2} (e^3 - e^{-3} - (e^2 - e^{-2}))$

$\displaystyle I = e^2 - e^{-2} + \dfrac{1}{2} e^3 - \dfrac{1}{2} e^{-3} - \dfrac{1}{2} e^2 + \dfrac{1}{2} e^{-2}$

$\displaystyle I = \dfrac{1}{2} e^2 + \dfrac{1}{2} e^3 - \dfrac{1}{2} e^{-2} - \dfrac{1}{2} e^{-3}$

$\displaystyle I = \dfrac{1}{2} \left( e^2 + e^3 - \dfrac{1}{e^2} - \dfrac{1}{e^3} \right)$

Answer: $\dfrac{1}{2}\left(e^2 + e^3 - \dfrac{1}{e^2} - \dfrac{1}{e^3}\right)$

</details>

---

### Q6. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $[\cdot]$ denote the greatest integer function. Then $\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\left(\frac{12(3+[x])}{3+[\sin x]+[\cos x]}\right) \mathrm{d} x$ is equal to :

**Options:**

- **(A)** $13 \pi+1$
- **(B)** $12 \pi+5$
- **(C)** $11 \pi+2$
- **(D)** $15 \pi+4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $11 \pi+2$**

**Detailed Solution:**

$I = \int_{-\pi/2}^{\pi/2} \dfrac{12(3 + [x]) \, dx}{3 + [\sin x] + [\cos x]}$
$I = \int_{-\pi/2}^{-1} \dfrac{12(1) \, dx}{2} + \int_{-1}^{0} \dfrac{12(2) \, dx}{2} + \int_{0}^{1} \dfrac{12(3) \, dx}{3} + \int_{1}^{\pi/2} \dfrac{12(4) \, dx}{3}$
$I = 6\left(\dfrac{\pi}{2} - 1\right) + 12(0 + 1) + 12(1 - 0) + 16\left(\dfrac{\pi}{2} - 1\right)$
$I = 3\pi - 6 + 12 + 12 + 8\pi - 16$
$I = 11\pi + 2$

</details>

---

### Q7. JEE Main 2026 (28 January Shift 1)

*Type:* `numerical` | *Level:* `3`

The value of $\sum_{r=1}^{20}\left(\left|\sqrt{\pi\left(\int_{0}^{r} x|\sin \pi x| d x\right)}\right|\right)$ is $\_\_\_\_$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **210**

**Detailed Solution:**

Let $I_r = \int_{0}^{r} x|\sin \pi x| \, dx$ .....(1)
Apply King Property
$= \int_{0}^{r} (r - x)|\sin \pi x| \, dx$ .....(2)
By (1) + (2)
$2I_r = \int_{0}^{r} r|\sin \pi x| \, dx \Rightarrow I_r = \dfrac{r}{2} \int_{0}^{r} |\sin \pi x| \, dx$
$I_1 = \dfrac{1}{2} \int_{0}^{1} |\sin \pi x| \, dx = \dfrac{1}{2\pi} \int_{0}^{\pi} |\sin t| \, dt = \dfrac{1}{2\pi}(2)$
$I_2 = \dfrac{2}{2} \int_{0}^{2} |\sin \pi x| \, dx = \dfrac{2}{2\pi} \int_{0}^{2\pi} |\sin t| \, dt = \dfrac{2}{2\pi}(4)$
$S = \sqrt{\pi \cdot \dfrac{1}{2\pi} \cdot 2} + \sqrt{\pi \cdot \dfrac{2}{2\pi} \cdot 4} + \sqrt{\pi \cdot \dfrac{3}{2\pi} \cdot 6} + \ldots + \sqrt{\pi \cdot \dfrac{20}{2\pi}(2 \cdot 20)}$
$= 1 + 2 + 3 + \ldots + 20$
$= \dfrac{20 \times 21}{2} = 210$

</details>

---

### Q8. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f$ be a polynomial function such that $f\left(x^{2}+1\right)=x^{4}+5 x^{2}+2$, for all $x \in \mathbb{R}$. Then $\int_{0}^{3} f(x) d x$ is equal to

**Options:**

- **(A)** $\frac{5}{3}$
- **(B)** $\frac{41}{3}$
- **(C)** $\frac{27}{2}$
- **(D)** $\frac{33}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{33}{2}$**

**Detailed Solution:**

Let $u = x^2 + 1$, then $x^2 = u - 1$.
Substituting into the given condition:
$f(u) = (u-1)^2 + 5(u-1) + 2 =$ 
 $u^2 - 2u + 1 + 5u - 5 + 2$ 
 $= u^2 + 3u - 2$.
Therefore, $f(x) = x^2 + 3x - 2$.
Calculating the integral: $\int_0^3 f(x)dx = \int_0^3 (x^2 + 3x - 2)dx$ 
 $= \left[\frac{x^3}{3} + \frac{3x^2}{2} - 2x\right]_0^3 = 9 + \frac{27}{2} - 6 = \frac{33}{2}$.

</details>

---

### Q9. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int_{\frac{\pi}{24}}^{\frac{5 \pi}{24}} \frac{\mathrm{~d} x}{1+\sqrt[3]{\tan 2 x}}$ is :

**Options:**

- **(A)** $\frac{\pi}{3}$
- **(B)** $\frac{\pi}{12}$
- **(C)** $\frac{\pi}{18}$
- **(D)** $\frac{\pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{12}$**

**Detailed Solution:**

Let $I = \int_{\pi/24}^{5\pi/24} \frac{dx}{1+\sqrt[3]{\tan 2x}}$.
Apply King's rule ($x \to \pi/4 - x$):
$I = \int_{\pi/24}^{5\pi/24} \frac{dx}{1+\sqrt[3]{\cot 2x}} = \int_{\pi/24}^{5\pi/24} \frac{\sqrt[3]{\tan 2x}}{1+\sqrt[3]{\tan 2x}}dx$.
Adding: $2I = \int_{\pi/24}^{5\pi/24} dx = \frac{5\pi}{24} - \frac{\pi}{24} = \frac{\pi}{6}$.
$I = \frac{\pi}{12}$.

</details>

---

### Q10. JEE Main 2026 (22 January Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $[\cdot]$ be the greatest integer function. If $\alpha=\int_{0}^{64}\left(x^{1 / 3}-\left[x^{1 / 3}\right]\right) \mathrm{d} x$, then $\frac{1}{\pi} \int_{0}^{\alpha \pi}\left(\frac{\sin ^{2} \theta}{\sin ^{6} \theta+\cos ^{6} \theta}\right) \mathrm{d} \theta$ is equal to $\_\_\_\_$ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **36**

**Detailed Solution:**

$\because \int_{0}^{64} x^{\frac{1}{3}} \, dx = \dfrac{3}{4} \left[ x^{\frac{4}{3}} \right]_{0}^{64} = 192$ &
$\int_{0}^{64} [x^{1/3}] \, dx = \int_{0}^{1} [x^{1/3}] \, dx + \int_{1}^{8} [x^{1/3}] \, dx + \int_{8}^{27} [x^{1/3}] \, dx + \int_{27}^{64} [x^{1/3}] \, dx = 156$
So $\alpha = 192 - 156 = 36$
Now $E = \dfrac{1}{\pi} \int_{0}^{36\pi} \dfrac{\sin^2\theta}{\sin^6\theta + \cos^6\theta} \, d\theta$
$= \dfrac{36}{\pi} \int_{0}^{\pi} \dfrac{\sin^2\theta}{\sin^6\theta + \cos^6\theta} \, d\theta$
$\Rightarrow E = \dfrac{36 \cdot 2}{\pi} \int_{0}^{\pi/2} \dfrac{\sin^2\theta}{\sin^6\theta + \cos^6\theta} \, d\theta$
Let $J = \int_{0}^{\pi/2} \dfrac{\sin^2\theta}{\sin^6\theta + \cos^6\theta} \, d\theta$ ....(1)
Applying King
$J = \int_{0}^{\pi/2} \dfrac{\cos^2\theta}{\sin^6\theta + \cos^6\theta} \, d\theta$ .....(2)
Now $2J = \int_{0}^{\pi/2} \dfrac{1}{\sin^6\theta + \cos^6\theta} \, d\theta$ (add (1) & (2))
$= \int_{0}^{\pi/2} \dfrac{\sec^6\theta}{\tan^6\theta + 1} \, d\theta$
$= \int_{0}^{\infty} \dfrac{(1 + \lambda^2)}{\lambda^4 - \lambda^2 + 1} \, d\lambda$
$= \int_{0}^{\infty} \dfrac{1 + \dfrac{1}{\lambda^2}}{\lambda^2 - 1 + \dfrac{1}{\lambda^2}} \, d\lambda$
$= \pi$
$\Rightarrow J = \dfrac{\pi}{2}$
$\Rightarrow E = \dfrac{36 \cdot 2}{\pi} \times J = 36$

</details>

---

### Q11. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=[x]^{2}-[x+3]-3, x \in \mathbf{R}$, where [] is the greatest integer funtion. Then

**Options:**

- **(A)** $\int_{0}^{2} f(x) \mathrm{d} x=-6$
- **(B)** $f(x)<0$ only for $x \in[-1,3)$
- **(C)** $f(x)>0$ only for $x \in[4, \infty)$
- **(D)** $f(x)=0$ for finitely many values of $x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $f(x)<0$ only for $x \in[-1,3)$**

**Detailed Solution:**

For $x \in [n, n+1)$ where $n$ is an integer, $[x] = n$ and $[x+3] = n+3$.
Thus $f(x) = n^2 - (n+3) - 3 = n^2 - n - 6 = (n-3)(n+2)$.
For $f(x) < 0$, we need $(n-3)(n+2) < 0$, which gives $-2 < n < 3$, i.e., $n \in \{-1, 0, 1, 2\}$.
This corresponds to $x \in [-1, 3)$.
We can verify:
For $n = -1$: $f = 1 - 2 - 3 = -4 < 0$
For $n = 0,1$: $f = -6 < 0$
For $n = 2$: $f = 4 - 5 - 3 = -4 < 0$
For $n = 3$: $f = 9 - 6 - 3 = 0$
For $n \geq 4$, $(n-3)(n+2) > 0$.
Therefore $f(x) < 0$ only for $x \in [-1, 3)$.

</details>

---

### Q12. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\left(\frac{1}{[x]+4}\right) d x$, where $[\cdot]$ denotes the greatest integer function, is

**Options:**

- **(A)** $\frac{1}{60}(21 \pi-1)$
- **(B)** $\frac{7}{60}(\pi-3)$
- **(C)** $\frac{7}{60}(3 \pi-1)$
- **(D)** $\frac{1}{60}(\pi-7)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{7}{60}(3 \pi-1)$**

**Detailed Solution:**

$I = \int_{-\pi/2}^{\pi/2} \dfrac{1}{[x] + 4} \, dx$
$I = \int_{-\pi/2}^{-1} \dfrac{dx}{2} + \int_{-1}^{0} \dfrac{dx}{3} + \int_{0}^{1} \dfrac{dx}{4} + \int_{1}^{\pi/2} \dfrac{dx}{5}$
$= \dfrac{1}{2}\left(-1 + \dfrac{\pi}{2}\right) + \dfrac{1}{3}(1) + \dfrac{1}{4}(1) + \dfrac{1}{5}\left(\dfrac{\pi}{2} - 1\right)$
$= \dfrac{7\pi}{20} - \dfrac{7}{60} = \dfrac{7}{60}(3\pi - 1)$

</details>

---

### Q13. JEE Main 2026 (21 January Shift 1)

*Type:* `numerical` | *Level:* `3`

$6 \int_{0}^{\pi}|(\sin 3 x+\sin 2 x+\sin x)| d x$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **17**

**Detailed Solution:**

Using $\sin 3x + \sin x = 2\sin 2x \cos x$:
$\sin 3x + \sin 2x + \sin x = \sin 2x(2\cos x + 1) = 2\sin x \cos x(2\cos x + 1)$
Zeros in $[0, \pi]$: $x = 0, \pi/2, 2\pi/3, \pi$
Expression is positive on $(0, \pi/2)$, negative on $(\pi/2, 2\pi/3)$, positive on $(2\pi/3, \pi)$
Let $F(x) = -\frac{\cos 3x}{3} - \frac{\cos 2x}{2} - \cos x$
$F(0) = -\frac{11}{6}$, $F(\pi/2) = \frac{1}{2}$, $F(2\pi/3) = \frac{5}{12}$, $F(\pi) = \frac{5}{6}$
$\int_0^{\pi/2} = \frac{7}{3}$, $\left|\int_{\pi/2}^{2\pi/3}\right| = \frac{1}{12}$, $\int_{2\pi/3}^{\pi} = \frac{5}{12}$
Total $= \frac{7}{3} + \frac{1}{12} + \frac{5}{12} = \frac{17}{6}$
$6 \times \frac{17}{6} = 17$

</details>

---

### Q14. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_{-\pi / 6}^{\pi / 6}\left(\frac{\pi+4 x^{11}}{1-\sin (|x|+\pi / 6)}\right) d x$ is equal to:

**Options:**

- **(A)** $8 \pi$
- **(B)** $6 \pi$
- **(C)** $2 \pi$
- **(D)** $4 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4 \pi$**

**Detailed Solution:**

Split: $\int_{-\pi/6}^{\pi/6} \frac{\pi}{1 - \sin(|x| + \pi/6)} dx + \int_{-\pi/6}^{\pi/6} \frac{4x^{11}}{1 - \sin(|x| + \pi/6)} dx$.
Second integral = 0 (odd function over symmetric interval).
First integral: $2\pi \int_{0}^{\pi/6} \frac{1}{1 - \sin(x + \pi/6)} dx$.
Let $u = x + \pi/6$: $= 2\pi \int_{\pi/6}^{\pi/3} \frac{1}{1 - \sin u} du$.
$\frac{1}{1-\sin u} = \sec^2 u + \sec u \tan u$.
$= 2\pi [\tan u + \sec u]_{\pi/6}^{\pi/3} = 2\pi[(\sqrt{3}+2) - \sqrt{3}] = 4\pi$.

</details>

---

### Q15. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The integral $\int_{-1}^{\frac{3}{2}}\left(\left|\pi^2 x \sin (\pi x)\right|\right) d x$ is equal to:

**Options:**

- **(A)** $3+2 \pi$
- **(B)** $4+\pi$
- **(C)** $1+3 \pi$
- **(D)** $2+3 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1+3 \pi$**

**Detailed Solution:**

Let, $\mathrm{I}=\pi^2 \int_{-1}^{3 / 2}|\mathrm{x} \sin \pi \mathrm{x}| \mathrm{dx}$
$\begin{aligned}
& =\pi^2\left\{\int_{-1}^1 \mathrm{x} \sin \pi \mathrm{xdx}-\int_1^{3 / 2} \mathrm{x} \sin \pi \mathrm{xdx}\right\} \\
& =\pi^2\left\{2 \int_0^1 \mathrm{x} \sin \pi \mathrm{xdx}-\int_{-1}^{3 / 2} \mathrm{x} \sin \pi \mathrm{xdx}\right\}
\end{aligned}$
Consider
$\begin{aligned}
& \int \mathrm{x} \sin \pi \mathrm{xdx} \\
& -\mathrm{x} \cdot \frac{1}{\pi} \cos \pi \mathrm{x}+\int 1 \cdot \frac{1}{\pi} \cos \pi \mathrm{xdx} \\
& =-\frac{\mathrm{x}}{\pi} \cos \pi \mathrm{x}+\frac{\sin \pi \mathrm{x}}{\pi^2}
\end{aligned}$
$\begin{aligned} \mathrm{I} & =\pi^2\left\{2\left(-\frac{\mathrm{x}}{\pi} \cos \pi \mathrm{x}+\frac{\sin \pi \mathrm{x}}{\pi^2}\right)_0^1-\left(-\frac{\mathrm{x}}{\pi} \cos \pi \mathrm{x}+\frac{\sin \pi \mathrm{x}}{\pi^2}\right)_1^{3 / 2}\right\} \\ & =\pi^2\left\{\frac{2}{\pi}-\left(-\frac{1}{\pi^2}-\frac{1}{\pi}\right)\right\} \\ & =\pi^2\left\{\frac{3}{\pi}+\frac{1}{\pi^2}\right\} \\ & =3 \pi+1\end{aligned}$

</details>

---

### Q16. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)$ be a positive function and $I_1=\int_{-\frac{1}{2}}^1 2 x f(2 x(1-2 x)) d x$ and $I_2=\int_{-1}^2 f(x(1-x)) d x$. Then the value of $\frac{I_2}{I_1}$ is equal to ________

**Options:**

- **(A)** 9
- **(B)** 6
- **(C)** 12
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

$\begin{aligned} & \mathrm{I}_1=\int_{-\frac{1}{2}}^1 2 \mathrm{xf}(2 \mathrm{x}(1-2 \mathrm{x})) \mathrm{dx} \\ & \Rightarrow 2 \mathrm{x}=\mathrm{t} \Rightarrow 2 \mathrm{dx}=\mathrm{dt} \quad \Rightarrow \mathrm{I}_1=\frac{1}{2} \int_{-1}^2 \mathrm{tf}(\mathrm{t}(1-\mathrm{t})) \mathrm{dt} \\ & \Rightarrow 2 \mathrm{I}_1=\int_{-1}^2(1-\mathrm{t}) \mathrm{f}(1-\mathrm{t})(1-(1-\mathrm{t})) \mathrm{dt} \\ & \Rightarrow 2 \mathrm{I}_1=\int_{-1}^2 \mathrm{f}\left(\mathrm{t}(1-\mathrm{t}) \mathrm{dt}-\int_{-1}^2 \mathrm{tf}(\mathrm{t}(1-\mathrm{t}) \mathrm{dt}\right. \\ & \Rightarrow 2 \mathrm{I}_1=\mathrm{I}_2-2 \mathrm{I}_1 \\ & \Rightarrow 4 \mathrm{I}_1=\mathrm{I}_2 \\ & \Rightarrow \frac{\mathrm{I}_2}{\mathrm{I}_1}=4\end{aligned}$

</details>

---

### Q17. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The integral $\int_0^\pi \frac{(x+3) \sin x}{1+3 \cos ^2 x} d x$ is equal to :

**Options:**

- **(A)** $\frac{\pi}{\sqrt{3}}(\pi+1)$
- **(B)** $\frac{\pi}{\sqrt{3}}(\pi+2)$
- **(C)** $\frac{\pi}{3 \sqrt{3}}(\pi+6)$
- **(D)** $\frac{\pi}{2 \sqrt{3}}(\pi+4)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{3 \sqrt{3}}(\pi+6)$**

**Detailed Solution:**

$\begin{aligned} & I=\int_0^\pi \frac{(x+3) \sin x}{1+3 \cos ^2 x} d x \\ & I=\int_0^\pi \frac{(\pi-x+3) \sin x}{\left(1+3 \cos ^2 x\right)} d x \\ & 2 I=\int_0^\pi \frac{(\pi+6) \sin x \cdot d x}{\left(1+3 \cos ^2 x\right)}=2 \int_0^{\pi / 2} \frac{(\pi+6) \sin x}{\left(1+3 \cos ^2 x\right)} \\ & I=\int_0^{\pi / 2} \frac{(\pi+6) \sin x \cdot d x}{\left(1+3 \cos ^2 x\right)}=\frac{\pi}{3 \sqrt{3}}(\pi+6) \\ & \sqrt{3} \cos x=t \\ & \sqrt{3} \sin x=d t\end{aligned}$

</details>

---

### Q18. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_{-1}^1 \frac{(1+\sqrt{|x|-x}) e^x+(\sqrt{|x|-x}) e^{-x}}{e^x+e^{-x}} d x$ is equal to

**Options:**

- **(A)** $3-\frac{2 \sqrt{2}}{3}$
- **(B)** $2+\frac{2 \sqrt{2}}{3}$
- **(C)** $1-\frac{2 \sqrt{2}}{3}$
- **(D)** $1+\frac{2 \sqrt{2}}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1+\frac{2 \sqrt{2}}{3}$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{I}=\int_{-1}^1 \frac{(1+\sqrt{|-\mathrm{x}|-(-\mathrm{x})}) \mathrm{e}^{-\mathrm{x}}+(\sqrt{|-\mathrm{x}|-(-\mathrm{x})}) \mathrm{e}^{-(-\mathrm{x})}}{\mathrm{e}^{-\mathrm{x}}+\mathrm{e}^{-(-\mathrm{x})}} \mathrm{dx} \\ & \Rightarrow \mathrm{I}=\int_{-1}^1 \frac{(1+\sqrt{|\mathrm{x}|+\mathrm{x}}) \mathrm{e}^{-\mathrm{x}}+(\sqrt{|\mathrm{x}|+\mathrm{x}}) \mathrm{e}^{\mathrm{x}}}{\mathrm{e}^{\mathrm{x}}+\mathrm{e}^{\mathrm{x}}} \mathrm{dx} \\ & \Rightarrow 2 \mathrm{I}=\int_{-1}^1 \frac{(1+\sqrt{|\mathrm{x}|+\mathrm{x}}+\sqrt{|\mathrm{x}|-\mathrm{x}})\left(\mathrm{e}^{\mathrm{x}}+\mathrm{e}^{-\mathrm{x}}\right)}{\left(\mathrm{e}^{\mathrm{x}}+\mathrm{e}^{-\mathrm{x}}\right)} \mathrm{dx} \\ & \Rightarrow 2 \mathrm{I}=\int_{-1}^1(1+\sqrt{|\mathrm{x}|+\mathrm{x}}+\sqrt{|\mathrm{x}|-\mathrm{x}}) \mathrm{dx} \\ & \Rightarrow 2 \mathrm{I}=2 \int_0^1(1+\sqrt{|\mathrm{x}|+\mathrm{x}}+\sqrt{|\mathrm{x}|-\mathrm{x}}) \mathrm{dx} \\ & \Rightarrow 2 \mathrm{I}=2 \int_0^1(1+\sqrt{2 \mathrm{x}}+\sqrt{0}) \mathrm{dx} \\ & \Rightarrow \mathrm{I}=\int_0^1(1+\sqrt{2 \mathrm{x}}) \mathrm{dx}=\left[\mathrm{x}+\frac{2 \sqrt{2}}{3} \mathrm{x}^{3 / 2}\right]_0^1 \\ & \Rightarrow \mathrm{I}=\frac{2 \sqrt{2}}{3}+1\end{aligned}$

</details>

---

### Q19. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The integral $\int_0^\pi \frac{8 x d x}{4 \cos ^2 x+\sin ^2 x}$ is equal to

**Options:**

- **(A)** $2 \pi^2$
- **(B)** $4 \pi^2$
- **(C)** $\pi^2$
- **(D)** $\frac{3 \pi^2}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \pi^2$**

**Detailed Solution:**

$\begin{aligned}
& I=\int_0^\pi \frac{8 x d x}{4 \cos ^2 x+\sin ^2 x} \\
& I=\int_0^\pi \frac{8(\pi-x) d x}{4 \cos ^2 x+\sin ^2 x}
\end{aligned}$
$2 \mathrm{I}=8 \pi \int_0^\pi \frac{d x}{4 \cos ^2 x+\sin ^2 x}$
$2 \mathrm{I}=8 \pi \times 2 \int_0^{\pi / 2} \frac{\sec ^2 x}{4+\tan ^2 \mathrm{x}} \mathrm{dx}$
$\begin{aligned}
& \mathrm{I}=8 \pi \int_0^{\infty} \frac{\mathrm{dt}}{4+\mathrm{t}^2}=8 \pi \times \frac{1}{2}\left(\tan ^{-1} \frac{\mathrm{t}}{2}\right]_0^{\infty} \\
& =4 \pi \times \frac{\pi}{2}=2 \pi^2
\end{aligned}$
option (1)

</details>

---

### Q20. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let the domain of the function
$f(\mathrm{x})=\log _2 \log _4 \log _6\left(3+4 x-x^2\right)$ be $(\mathrm{a}, \mathrm{~b})$. If $\int_0^{\mathrm{b}-\mathrm{a}}\left[\mathrm{x}^2\right] \mathrm{dx}=\mathrm{p}-\sqrt{\mathrm{q}}-\sqrt{\mathrm{r}}, \mathrm{p}, \mathrm{q},$ $\mathrm{r} \in \mathbb{N}, \operatorname{gcd}(\mathrm{p}, \mathrm{q}, \mathrm{r})=1,$
where [$\cdot]$ is the greatest integer function, then $\mathrm{p}+\mathrm{q}+\mathrm{r}$ is equal to

**Options:**

- **(A)** $10$
- **(B)** $8$
- **(C)** $11$
- **(D)** $9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $10$**

**Detailed Solution:**

$\begin{aligned} & \log _4 \log _6\left(3+4 x-x^2\right) \gt 0 \\ & \log _6\left(3+4 x-x^2\right) \gt 1\end{aligned}$
$\begin{aligned} & 3+4 x-x^2 \gt 6 \\ & x^2-4 x+3 \lt 0 \\ & (x-1)(x-3) \lt 0 \\ & x \in(1,3) \\ & \text { so } a=1 \& b=3 \\ & \Rightarrow \int_0^2\left[x^2\right] d x=? \\ & I=\int_0^1\left[x^2\right] d x+\int_1^{\sqrt{2}}\left[x^2\right] d x+\int_{\sqrt{2}}^{\sqrt{3}}\left[x^2\right] d x+\int_{\sqrt{3}}^{\sqrt{4}}\left[x^2\right] d x \\ & =0+|x|_1^{\sqrt{2}}+2|x|_{\sqrt{2}}^{\sqrt{3}}+3|x|_{\sqrt{3}}^{\sqrt{4}}\end{aligned}$
$\begin{aligned} & =(\sqrt{2}-1)+2(\sqrt{3}-\sqrt{2})+3(2-\sqrt{3}) \\ & =5-\sqrt{2}-\sqrt{3} \Rightarrow \mathrm{p}+\mathrm{q}+\mathrm{r}=10\end{aligned}$

</details>

---

### Q21. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$4 \int_0^1\left(\frac{1}{\sqrt{3+x^2}+\sqrt{1+x^2}}\right) d x-3 \log _e(\sqrt{3})$ is equal to :

**Options:**

- **(A)** $2+\sqrt{2}+\log _e(1+\sqrt{2})$
- **(B)** $2-\sqrt{2}-\log _e(1+\sqrt{2})$
- **(C)** $2+\sqrt{2}-\log _e(1+\sqrt{2})$
- **(D)** $2-\sqrt{2}+\log _e(1+\sqrt{2})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2-\sqrt{2}-\log _e(1+\sqrt{2})$**

**Detailed Solution:**

$\begin{aligned} & 4 \int_0^1 \frac{1}{\sqrt{3+\mathrm{x}^2}+\sqrt{1+\mathrm{x}^2}} \mathrm{dx}-3 \ln \sqrt{3} \\ & =4 \int_0^1 \frac{\sqrt{3+\mathrm{x}^2}-\sqrt{1+\mathrm{x}^2}}{\left(3+\mathrm{x}^2\right)-\left(1-\mathrm{x}^2\right)} \mathrm{dx}-\frac{3}{2} \ln 3 \\ & = \\ & 2\left[\left\{\frac{\mathrm{x}}{2} \sqrt{3+\mathrm{x}^2}+\frac{3}{2} \ln \left(\mathrm{x}+\sqrt{3+\mathrm{x}^2}\right)\right\}_0^1\right. \\ & \left.\quad-\left\{\frac{\mathrm{x}}{2} \sqrt{1+\mathrm{x}^2}+\frac{1}{2} \ln \left(\mathrm{x}+\sqrt{1+\mathrm{x}^2}\right)\right\}_0^1\right]-\frac{3}{2} \ln 3\end{aligned}$
$\begin{aligned}= & 2\left[\left\{\frac{1}{2} \sqrt{4}+\frac{3}{2} \ln (1+\sqrt{4})\right\}-\left\{0+\frac{3}{2} \ln \sqrt{3}\right\}\right. \\ & \left.-\left\{\frac{1}{2} \sqrt{2}+\frac{1}{2} \ln (1+\sqrt{2})\right\}+\left\{0+\frac{1}{2}(0)\right\}\right]-\frac{3}{2} \ln 3\end{aligned}$
$\begin{aligned} & =2\left[1+\frac{3}{2} \ln 3-\frac{3}{4} \ln 3-\frac{1}{\sqrt{2}}-\frac{1}{2} \ln (1+\sqrt{2})\right]-\frac{3}{2} \ln 3 \\ & =2+3 \ln 3-\frac{3}{2} \ln 3-\sqrt{2}-\ln (1+\sqrt{2})-\frac{3}{2} \ln 3 \\ & =2-\sqrt{2}-\ln (1+\sqrt{2})\end{aligned}$

</details>

---

### Q22. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $(a, b)$ be the point of intersection of the curve $x^2=2 y$ and the straight line $y-2 x-6=0$ in the second quadrant. Then the integral $I=\int_a^b \frac{9 x^2}{1+5^x} d x$ is equal to :

**Options:**

- **(A)** $24$
- **(B)** $27$
- **(C)** $18$
- **(D)** $21$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $24$**

**Detailed Solution:**

$\begin{aligned} & x^2=2 y \& y=2 x+6 \\ & x^2=4 x+12\end{aligned}$
$\left.x^2-4 x-12=0 \Rightarrow \begin{gathered}x=6 \\ y=18\end{gathered} \right\rvert\, \begin{gathered}\text { if } x=-2 \\ y=2\end{gathered}$
$\therefore(6,18) \&(-2,2)$
Here $(6,18)$ Rejected because $(a, b)$ lies in $2^{\text {nd }}$ quadrant
$\begin{aligned} & \therefore \mathrm{a}=-2 \& \mathrm{~b}=2 \\ & \therefore \mathrm{I}=\int_{-2}^2 \frac{9 \mathrm{x}^2}{1+5^{\mathrm{x}}} \mathrm{dx}=\int_{-2}^2 \frac{9 \cdot 5^{\mathrm{x}} \cdot \mathrm{x}^2}{1+5^{\mathrm{x}}} \mathrm{dx} \\ & \therefore 2 \mathrm{I}=\int_{-2}^2 9 \mathrm{x}^2 \mathrm{dx}=18 \int_0^2 \mathrm{x}^2 \mathrm{dx}=18\left(\frac{\mathrm{x}^3}{3}\right)_0^2 \\ & 2 \mathrm{I}=48 \\ & \therefore \mathrm{I}=24\end{aligned}$

</details>

---

### Q23. JEE Main 2025 (2 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let [.] denote the greatest integer function. If $\int_0^{e^3}\left[\frac{1}{\mathrm{e}^{\mathrm{x}-1}}\right] \mathrm{dx}=\alpha-\log _{\mathrm{e}} 2$, then $\alpha^3$ is equal to _______ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

$f(x)=\frac{1}{e^{x-1}}=e^{1-x}$
\begin{array}{c|c}\mathrm{f}(\mathrm{x})=2 & \mathrm{f}(\mathrm{x})=1 \\\frac{1}{\mathrm{e}^{\mathrm{x}-1}}=2 & \mathrm{x}=1 \\\mathrm{x}=1-\ln 2 &\end{array}
$f(0)=e^1=2.71$
$f\left(e^3\right)=e^{1-e^3} \in(0,1)$
$\mathrm{I}=\int_0^{1-\ell \mathrm{n} 2} 2 \mathrm{dx}+\int_{1-\ell \mathrm{n} 2}^1 1 \mathrm{dx}+\int_1^{\mathrm{e}^3} 0 \mathrm{dx}$
$=2(1-\ell \operatorname{n} 2-0)+1(1-1+\ln 2)+0$
$\alpha-\ln 2=2-\ln 2$
$\alpha=2$
$\alpha^3=8$

</details>

---

### Q24. JEE Main 2025 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

If $24 \int_0^{\frac{\pi}{4}}\left(\sin \left|4 x-\frac{\pi}{12}\right|+[2 \sin x]\right) \mathrm{d} x=2 \pi+\alpha$, where $[\cdot]$ denotes the greatest integer function, then $\alpha$ is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

Let $I=24 \int_0^{\frac{\pi}{2}}\left(\sin \left|4 x-\frac{\pi}{2}\right|+[2 \sin x]\right) d x$   ...(i)
Now $\left|4 x-\frac{\pi}{12}\right|= \begin{cases}-4 x+\frac{\pi}{12} & ; x < \frac{\pi}{48} \\ 4 x-\frac{\pi}{12} & ; \quad x \geq \frac{\pi}{48}\end{cases}$
$\therefore$ from $(\mathrm{i})$
$\begin{aligned} & I=24 \int_0^{\frac{\pi}{48}}-\sin \left(4 x-\frac{\pi}{12}\right) d x+\int_{\frac{\pi}{48}}^{\frac{\pi}{4}} \sin \left(4 x-\frac{\pi}{12}\right) \\ & +\int_0^{\frac{\pi}{6}}[2 \sin x] d x+\int_{\frac{\pi}{6}}^{\frac{\pi}{4}}[2 \sin x] d x \\ & I=24\left[\frac{\left(1-\cos \frac{\pi}{12}\right)}{4}-\frac{\left(-\cos \frac{\pi}{12}-1\right)}{4}\right)+\frac{\pi}{4}-\frac{\pi}{6} \\ & I=24\left(\frac{1}{2}\right)+\frac{\pi}{4}-\frac{\pi}{6} \\ & I=2 \pi+12=2 \pi+\alpha \text { (from above) } \\ & \therefore \quad \alpha=12\end{aligned}$

</details>

---

### Q25. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \frac{96 x^2 \cos ^2 x}{\left(1+e^x\right)} \mathrm{d} x=\pi\left(\alpha \pi^2+\beta\right), \alpha, \beta \in \mathbb{Z}$, then $(\alpha+\beta)^2$ equals

**Options:**

- **(A)** 64
- **(B)** 196
- **(C)** 144
- **(D)** 100

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 100**

**Detailed Solution:**

$\begin{aligned} & I=\int_0^{\frac{\pi}{2}} \frac{96 x^2 \cos ^2 x}{1+e^x} d x \\ & 2 I=2 \int_0^{\frac{\pi}{2}} 96 x^2 \cos ^2 x d x \\ & I=96 \int_0^{\frac{\pi}{2}} x^2 \cos ^2 x d x \\ & =48 \int_0^{\frac{\pi}{2}} x^2(1+\cos 2 x) d x \\ & =2 \pi^2+48(0-0)-48 \int_0^{\frac{\pi}{2}} x \sin 2 x d x \\ & =2 \pi^2-12 \pi+[0-0]=\pi\left(2 \pi^2-12\right) \\ & =\pi\left(\alpha \pi^2+\beta\right) \\ & \Rightarrow(\alpha+\beta)^2=100\end{aligned}$

</details>

---

### Q26. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{I}=\int_0^{\frac{\pi}{2}} \frac{\sin ^{\frac{3}{2}} x}{\sin ^{\frac{3}{2}} x+\cos ^{\frac{3}{2}} x} \mathrm{~d} x$, then $\int_0^{21} \frac{x \sin x \cos x}{\sin ^4 x+\cos ^4 x} \mathrm{~d} x$ equals :

**Options:**

- **(A)** $\frac{\pi^2}{12}$
- **(B)** $\frac{\pi^2}{4}$
- **(C)** $\frac{\pi^2}{16}$
- **(D)** $\frac{\pi^2}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi^2}{16}$**

**Detailed Solution:**

$\begin{aligned}
& I=\int_0^{\frac{\pi}{2}} \frac{(\sin x)^{\frac{3}{2}} d x}{(\sin x)^{\frac{3}{2}} x+(\cos x)^{\frac{3}{2}}}=\int_0^{\frac{\pi}{2}} \frac{\sin ^{\frac{3}{2}}\left(\frac{\pi}{2}-x\right) d x}{\sin ^{\frac{3}{2}}\left(\frac{\pi}{2}-x\right)+\cos ^{\frac{3}{2}}\left(\frac{\pi}{2}-x\right)} \\
& \Rightarrow \text { Adding } 2 l=\int_0^{\frac{\pi}{2}} \frac{(\sin x)^{\frac{3}{2}}+(\cos x)^{\frac{3}{2}}}{(\sin x)^{\frac{3}{2}}+(\cos x)^{\frac{3}{2}}} d x=\frac{\pi}{2} \\
& I_0=\int_0^{\frac{\pi}{2}} \frac{x \sin x \cos x}{\sin ^4 x+\cos ^4 x} d x=\int_0^{\frac{\pi}{2}} \frac{\left(\frac{\pi}{2}-x\right) \sin x \cos x}{(\sin x)^4+(\cos x)^4} d x
\end{aligned}$
Adding, $2 I_0=\int_0^{\frac{\pi}{2}} \frac{\frac{\pi}{2}(\sin x) \cos x}{\left(\sin ^4 x+\cos ^4 x\right)} d x$
$\Rightarrow I_0=\frac{\pi}{4} \int_0^{\frac{\pi}{2}} \frac{\tan x\left(\sec ^2 x\right) d x}{1+\tan ^4 x}$
put $\tan ^2 x=t \Rightarrow 2 \tan x \sec ^2 x d x=d t$
$\begin{aligned}
& \Rightarrow I_0=\frac{\pi}{4} \int_0^{\infty} \frac{\frac{d t}{2}}{\left(1+t^2\right)}=\left.\frac{\pi}{8}\left(\tan ^{-1} t\right)\right|_0 ^{\infty}=\frac{\pi}{8}\left(\frac{\pi}{2}-0\right) \\
& \Rightarrow I_0=\frac{\pi^2}{16}
\end{aligned}$

</details>

---

### Q27. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of
$\int_{e^2}^{e^4} \frac{1}{x}\left(\frac{e^{\left(\left(\log _e x\right)^2+1\right)^{-1}}}{e^{\left(\left(\log _e x\right)^2+1\right)^{-1}}+e^{\left(\left(6-\log _e x\right)^2+1\right)^{-1}}}\right) d x$ is

**Options:**

- **(A)** $2$
- **(B)** $\log _e 2$
- **(C)** $1$
- **(D)** $e^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

$\begin{aligned}
& \text {Put } \ln x=t \Rightarrow \frac{1}{x} d x=d t \quad \begin{array}{|c|c|}
\hline x & t \\
\hline e^2 & 2 \\
\hline e^4 & 4 \\
\hline \end{array} \\
& I=\int_2^4 \frac{e^{\left(\mathrm{t}^2+1\right)^{-1}}}{e^{\left(\mathrm{t}^2+1\right)^{-1}}+e^{\left((6-t)^2+1\right)^{-1}}} d t \quad \ldots \text { (i) } \\
& I=\int_2^4 \frac{e^{\left((6-t)^2+1\right)^{-1}}}{e^{\left((6-t)^2+1\right)^{-1}}+e^{\left(t^2+1\right)^{-1}} d t} \ldots \text { (ii) } \\
& \left\{\text { Using } \int_a^0 f(x) d x=\int_a^0 f(a+b-x) d x\right\}
\end{aligned}$
Adding (i) and (ii) gives
$2 l=\int d t \Rightarrow l=1$

</details>

---

### Q28. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int_{-1}^2 \log _e\left(x+\sqrt{x^2+1}\right) d x$ is

**Options:**

- **(A)** $\sqrt{5}-\sqrt{2}+\log _e\left(\frac{7+4 \sqrt{5}}{1+\sqrt{2}}\right)$
- **(B)** $\sqrt{5}-\sqrt{2}+\log _e\left(\frac{9+4 \sqrt{5}}{1+\sqrt{2}}\right)$
- **(C)** $\sqrt{2}-\sqrt{5}+\log _e\left(\frac{7+4 \sqrt{5}}{1+\sqrt{2}}\right)$
- **(D)** $\sqrt{2}-\sqrt{5}+\log _e\left(\frac{9+4 \sqrt{5}}{1+\sqrt{2}}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{2}-\sqrt{5}+\log _e\left(\frac{9+4 \sqrt{5}}{1+\sqrt{2}}\right)$**

**Detailed Solution:**

$\begin{aligned} & I=\int_{-1}^2 \log _e\left(x+\sqrt{x^2+1}\right) d x \\ & =x \log _e\left(x+\sqrt{x^2+1}\right)-\int_{-1}^2\left(\frac{1+\frac{x}{\sqrt{x^2+1}}}{x+\sqrt{x^2+1}}\right) d x \\ & =x \log _e\left(x+\sqrt{x^2+1}\right)-\int_{-1}^2 \frac{x}{\sqrt{x^2+1}} d x\end{aligned}$
$\begin{aligned} & =x \log _e\left(x+\sqrt{x^2+1}\right)-\left.\sqrt{x^2+1}\right|_{-1} ^2 \\ & =\left(2 \log _e(2+\sqrt{5})-\sqrt{5}\right) \\ & -\left(-\log _e(-1+\sqrt{2})-\sqrt{2}\right) \\ & =\log _e(2+\sqrt{5})^2-\sqrt{5}+\log _e(\sqrt{2}-1)+\sqrt{2} \\ & =\log _e(2+\sqrt{5})^2-\sqrt{5}+\log _e(\sqrt{2}-1)+\sqrt{2}\end{aligned}$
$\begin{aligned} & =\sqrt{2}-\sqrt{5}+\log _e\left(\frac{(2+\sqrt{5})^2}{\sqrt{2+1}}\right) \\ & =\sqrt{2}-\sqrt{5}+\log _e\left(\frac{9+4 \sqrt{5}}{\sqrt{2+1}}\right)\end{aligned}$

</details>

---

### Q29. JEE Main 2024 (05 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

If $f(t)=\int_0^\pi \frac{2 x \mathrm{~d} x}{1-\cos ^2 \mathrm{t} \sin ^2 x}, 0 < \mathrm{t} < \pi$, then the value of $\int_0^{\frac{\pi}{2}} \frac{\pi^2 \mathrm{dt}}{f(\mathrm{t})}$ equals_________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

$f(t)=\int_0^\pi \frac{2 x}{1-\cos ^2 t \sin ^2 x} d x$ .....(1)
$=2 \int_0^\pi \frac{(\pi-x) d x}{1-\cos ^2 \sin ^2 x}$ .....(2)
$\begin{aligned}
& 2 f(t)=2 \int_0^\pi \frac{\pi}{1-\cos ^2 \sin ^2 x} d x \\
& f(t)=\int_0^\pi \frac{\pi}{1-\cos ^2 t \sin ^2 x} d x
\end{aligned}$
divide \& by $\cos ^2 \mathrm{x}$
$\begin{aligned}
& f(t)=\pi \int_0^\pi \frac{\sec ^2 x d x}{\sec ^2 x-\cos ^2 t^2 x} \\
& f(t)=2 \pi \int_0^{\pi / 2} \frac{\sec ^2 x d x}{\sec ^2 x-\cos ^2 t^2 \tan ^2 x} \\
& \tan x=z \\
& \sec ^2 x d x=d z \\
& f(t)=2 \pi \int_0^{\infty} \frac{d z}{1+\sin ^2 t \cdot z^2} \\
& =\frac{\pi^2}{\sin t}
\end{aligned}$
Then $\int_0^{\pi / 2} \frac{\pi^2}{f(t)} d t$
$\begin{aligned}
& =\int_0^{\pi / 2} \sin t d t \\
& =1
\end{aligned}$

</details>

---

### Q30. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The integral $\int_0^{\pi / 4} \frac{136 \sin x}{3 \sin x+5 \cos x} d x$ is equal to :

**Options:**

- **(A)** $3 \pi-50 \log _e 2+20 \log _e 5$
- **(B)** $3 \pi-25 \log _e 2+10 \log _e 5$
- **(C)** $3 \pi-10 \log _e(2 \sqrt{2})+10 \log _e 5$
- **(D)** $3 \pi-30 \log _e 2+20 \log _e 5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3 \pi-50 \log _e 2+20 \log _e 5$**

**Detailed Solution:**

$\begin{aligned} & I=\int_0^{\pi / 4} \frac{136 \sin x}{3 \sin x+5 \cos x} d x \\ & 136 \sin x=A(3 \sin x+5 \cos x)+B(3 \cos x-5 \sin x) \\ & 136=3 A-5 B...(i) \\ & 0=5 A+3 B...(ii)\end{aligned}$
$\begin{aligned} & 3 \mathrm{~B}=-5 \mathrm{~A} \Rightarrow \mathrm{B}=-\frac{5}{3} \mathrm{~A} \\ & 136=3 \mathrm{~A}-5\left(-\frac{5}{3} \mathrm{~A}\right) \\ & 136=3 \mathrm{~A}+\frac{25}{3} \mathrm{~A} \\ & 136=\frac{34 \mathrm{~A}}{3} \\ & \Rightarrow \mathrm{A}=\frac{136 \times 3}{34}=12 \\ & \mathrm{~B}=\frac{-5}{3}(12)=-20\end{aligned}$
$\begin{aligned} & I=\int_0^{\pi / 4} \frac{A(3 \sin x+5 \cos x)}{3 \sin x+5 \cos x}+\int_0^{\pi / 4} \frac{B(3 \cos x-5 \sin x)}{3 \sin x+5 \cos x} \\ & =A(x)_0^{\pi / 4}+B[\ln (3 \sin x+5 \cos x)]_0^{\pi / 4} \\ & =12\left(\frac{\pi}{4}\right)-20 \ln \left(\frac{3}{\sqrt{2}}+\frac{5}{\sqrt{2}}\right)-\ln (0+5) \\ & =3 \pi-20 \ln 4 \sqrt{2}+20 \ln 5 \\ & =3 \pi-20 \times \frac{5}{2} \ln 2+20 \ln 5 \\ & =3 \pi-50 \ln 2+20 \ln 5\end{aligned}$

</details>

---

### Q31. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_{-\pi}^\pi \frac{2 y(1+\sin y)}{1+\cos ^2 y} d y$ is :

**Options:**

- **(A)** $2 \pi^2$
- **(B)** $\frac{\pi^2}{2}$
- **(C)** $\frac{\pi}{2}$
- **(D)** $\pi^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\pi^2$**

**Detailed Solution:**

$\int_{-\pi}^\pi \frac{2 y(1+\sin y)}{1+\cos ^2 y} d y$
\(=\underset{\text{(Odd)}}{\int_{-\pi}^\pi \frac{2 y}{1+\cos ^2 y} d y}+\underset{\text{(Even)}}{\int_{-\pi}^\pi \frac{2 y \sin y}{1+\cos ^2 y} d y}\)
$=0+2.2 \int_0^\pi y\left(\frac{\sin y}{1+\cos ^2 y}\right) d y$
$\begin{aligned} & I=4 \int_0^\pi \frac{y \sin y}{1+\cos ^2 y} d y \\ & I=4 \int_0^\pi \frac{(\pi-y) \sin y}{1+\cos ^2 y} d y \\ & 2 I=4 \int_0^\pi \frac{\pi \sin y}{1+\cos ^2 y} d y \\ & I=2 \pi \int_0^\pi \frac{\sin y}{1+\cos ^2 y} d y \\ & =2 \pi\left(-\tan ^{-1}(\cos y)\right)_0^\pi \\ & =-2 \pi\left[\left(-\frac{\pi}{4}\right)-\left(\frac{\pi}{4}\right)\right] \\ & =-2 \pi\left[-\frac{2 \pi}{4}\right]=\pi^2\end{aligned}$

</details>

---

### Q32. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the value of the integral $\int_{-1}^1 \frac{\cos \alpha x}{1+3^x} d x$ is $\frac{2}{\pi}$. Then, a value of $\alpha$ is

**Options:**

- **(A)** $\frac{\pi}{3}$
- **(B)** $\frac{\pi}{6}$
- **(C)** $\frac{\pi}{4}$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{2}$**

**Detailed Solution:**

Let $I=\int_{-1}^{+1} \frac{\cos \alpha x}{1+3^x} d x$ ...(I)
$I=\int_{-1}^{+1} \frac{\cos \alpha x}{1+3^{-x}} d x$
$\left(u \operatorname{sing} \int_a^b f(x) d x=\int_a^b f(a+b-x) d x\right)$ ...(II)
Add (1) and (II)
$\begin{aligned}
& 2 I=\int_{-1}^{+1} \cos (\alpha x) d x=2 \int_0^1 \cos (\alpha x) d x \\
& I=\frac{\sin \alpha}{\alpha}=\frac{2}{\pi}(\text { given }) \\
& \therefore \alpha=\frac{\pi}{2}
\end{aligned}$

</details>

---

### Q33. JEE Main 2024 (04 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

If $\int_0^{\frac{\pi}{4}} \frac{\sin ^2 x}{1+\sin x \cos x} \mathrm{~d} x=\frac{1}{\mathrm{a}} \log _{\mathrm{e}}\left(\frac{\mathrm{a}}{3}\right)+\frac{\pi}{\mathrm{b} \sqrt{3}}$, where $\mathrm{a}, \mathrm{b} \in \mathbf{N}$, then $\mathrm{a}+\mathrm{b}$ is equal to_________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

$\begin{aligned}
& \int_0^{\frac{\pi}{2}} \frac{\sin ^2 x}{1+\frac{1}{2} \sin 2 x} d x=\int_0^{\frac{\pi}{4}} \frac{1-\cos 2 x}{2+\sin 2 x} d x \\
& \int \frac{1}{2+\sin 2 x}-\int \frac{\cos 2 x}{2+\sin 2 x}
\end{aligned}$
$\left(\mathrm{I}_1\right) \quad-\quad\left(\mathrm{I}_2\right)$
$\begin{aligned}
& \left(\mathrm{I}_1\right)=\int \frac{\mathrm{dx}}{2+\frac{2 \tan \mathrm{x}}{1+\tan ^2 x}} \\
& \int_0^{\frac{\pi}{4}} \frac{\sec ^2 \mathrm{xdx}}{2 \tan ^2 \mathrm{x}+2 \tan x+2}
\end{aligned}$
$\begin{aligned}
& \tan x=t \\
& \frac{1}{2} \int_0^1 \frac{\mathrm{dt}}{\left(\mathrm{t}+\frac{1}{2}\right)^2+\frac{3}{4}}=\frac{\pi}{6 \sqrt{3}} \\
& \mathrm{I}_2=\int_0^{\pi / 4} \frac{\cos 2 \mathrm{x}}{2+\sin 2 \mathrm{x}} \mathrm{dx}=\frac{1}{2}\left(\ln \frac{3}{2}\right) \\
& \mathrm{I}_1-\mathrm{I}_2=\frac{1}{\sqrt{3}} \frac{\pi}{6}+\frac{1}{2} \ln \frac{2}{3} \\
& \Rightarrow \mathrm{a}=2, \mathrm{~b}=6
\end{aligned}$
Ans. 8

</details>

---

### Q34. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>3</mn></mfrac></munderover><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>a</mi><mi>π</mi><mo>+</mo><mi>b</mi><msqrt><mn>3</mn></msqrt></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> are rational numbers, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>a</mi><mo>+</mo><mn>8</mn><mi>b</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Let,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>3</mn></mfrac></msubsup><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>3</mn></mfrac></msubsup><msup><mfenced><mrow><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>3</mn></mfrac></msubsup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>3</mn></mfrac></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>3</mn></mfrac></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mo>d</mo><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>3</mn></mfrac></msubsup><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>3</mn></mfrac></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mo>d</mo><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>3</mn></mfrac></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mn>4</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><mi>x</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mrow><mi>sin</mi><mn>4</mn><mi>x</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></mrow></mfenced><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>3</mn></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><mfrac><mi mathvariant="normal">π</mi><mn>3</mn></mfrac><mo>+</mo><mi>sin</mi><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mfenced><mrow><mfrac><mi mathvariant="normal">π</mi><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mi>sin</mi><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfenced><mrow><mfrac><mi mathvariant="normal">π</mi><mn>12</mn></mfrac><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>8</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mi mathvariant="normal">π</mi><mn>24</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>64</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mi mathvariant="normal">π</mi><mn>8</mn></mfrac><mo>+</mo><mfrac><mrow><mn>7</mn><msqrt><mn>3</mn></msqrt></mrow><mn>64</mn></mfrac></math></p><p>So, on comparing with given value we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>,</mo><mo> </mo><mi>b</mi><mo>=</mo><mfrac><mn>7</mn><mn>64</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>9</mn><mi>a</mi><mo>+</mo><mn>8</mn><mi>b</mi><mo>=</mo><mfrac><mn>9</mn><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>7</mn><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>9</mn><mi>a</mi><mo>+</mo><mn>8</mn><mi>b</mi><mo>=</mo><mfrac><mn>16</mn><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>9</mn><mi>a</mi><mo>+</mo><mn>8</mn><mi>b</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q35. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>−</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mi>d</mi><mi>x</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>∫</mo><mn>0</mn><mn>1</mn></munderover><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>−</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mi>d</mi><mi>x</mi></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>∫</mo><mn>0</mn><mrow><mn>2</mn><mi>a</mi></mrow></munderover><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math> when<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>2</mn><mi>a</mi><mo>−</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mo>−</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p>Now, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><munderover><mo>∫</mo><mn>0</mn><mn>1</mn></munderover><msup><mfenced><mrow><mn>2</mn><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mo>−</mo><mn>3</mn><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>−</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><munderover><mo>∫</mo><mn>0</mn><mn>1</mn></munderover><msup><mfenced><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>−</mo><mn>3</mn><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>−</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><munderover><mo>∫</mo><mn>0</mn><mn>1</mn></munderover><msup><mfenced><mrow><mn>2</mn><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>−</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><munderover><mo>∫</mo><mn>0</mn><mn>1</mn></munderover><msup><mfenced><mrow><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>-</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mrow><mn>1</mn><mo>−</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mo>−</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mo> </mo><mi>I</mi><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q36. JEE Main 2024 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mrow><mo>−</mo><mi>π</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi>π</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mi>α</mi><mi>π</mi><mo>+</mo><mi>β</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>,</mo><mo> </mo><mi>β</mi></math> are integers, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup></math> equals __________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>∫</mo><mrow><mo>−</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></mrow><mfrac><mi>π</mi><mn>2</mn></mfrac></munderover><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt><mi>cos</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Applying <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><msubsup><mo>∫</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>d</mo><mi>x</mi></math> rule we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><munderover><mo>∫</mo><mrow><mo>−</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></mrow><mfrac><mi>π</mi><mn>2</mn></mfrac></munderover><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt><mi>cos</mi><mi>x</mi><mfenced><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup></mfenced></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>I</mi><mo>=</mo><munderover><mo>∫</mo><mrow><mo>−</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></mrow><mfrac><mi>π</mi><mn>2</mn></mfrac></munderover><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><munderover><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></munderover><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Putting, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><munderover><mo>∫</mo><mn>0</mn><mn>1</mn></munderover><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>4</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><munderover><mo>∫</mo><mn>0</mn><mn>1</mn></munderover><mfenced><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></mrow><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></mrow></mfrac><mo>−</mo><mfrac><mrow><mn>1</mn><mo>−</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></mrow><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><munderover><mo>∫</mo><mn>0</mn><mn>1</mn></munderover><mfenced><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></mrow><mrow><msup><mfenced><mrow><mi>t</mi><mo>−</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfrac><mo>−</mo><mfrac><mfenced><mrow><mn>1</mn><mo>−</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mrow><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>−</mo><mn>2</mn></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>−</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>=</mo><mi>z</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>=</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mfenced close="]" open="["><mrow><munderover><mo>∫</mo><mrow><mo>−</mo><mi>∞</mi></mrow><mn>0</mn></munderover><mfrac><mrow><mi>d</mi><mi>z</mi></mrow><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfrac><mo>-</mo><munderover><mo>∫</mo><mi>∞</mi><mn>2</mn></munderover><mfrac><mrow><mi>d</mi><mi>k</mi></mrow><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><msubsup><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfrac><mi>z</mi><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mrow><mo>−</mo><mi>∞</mi></mrow><mn>0</mn></msubsup><mo>−</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mi>ln</mi><mfenced><mfrac><mrow><mi>k</mi><mo>−</mo><msqrt><mn>2</mn></msqrt></mrow><mrow><mi>k</mi><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></mrow></mfenced><mi>∞</mi><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mfenced close="]" open="["><mrow><mfrac><mi>π</mi><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>−</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mfenced close="]" open="["><mrow><mi>ln</mi><mfrac><mrow><mn>2</mn><mo>−</mo><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>2</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mn>2</mn><mi>π</mi><mo>+</mo><mn>2</mn><mi>log</mi><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math></p><p>Comparing this value with <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>α</mi><mi>π</mi><mo>+</mo><mi>β</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q37. JEE Main 2024 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>4</mn></mfrac></munderover><mfrac><mrow><mi>x</mi><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mfrac></math> equals:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>2</mn></msqrt><msup><mi>π</mi><mn>2</mn></msup></mrow><mn>8</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>2</mn></msqrt><msup><mi>π</mi><mn>2</mn></msup></mrow><mn>16</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>2</mn></msqrt><msup><mi>π</mi><mn>2</mn></msup></mrow><mn>32</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>2</mn></msqrt><msup><mi>π</mi><mn>2</mn></msup></mrow><mn>64</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>2</mn></msqrt><msup><mi>π</mi><mn>2</mn></msup></mrow><mn>32</mn></mfrac></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mrow><mi>I</mi><mo>=</mo><mo>∫</mo></mrow><mn>0</mn><mfrac><mi>π</mi><mn>4</mn></mfrac></munderover><mfrac><mrow><mi>x</mi><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mfrac></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>=</mo><mi>t</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><munderover><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></munderover><mfrac><mrow><mi>t</mi><mi>d</mi><mi>t</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>t</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>t</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><munderover><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></munderover><mfrac><mrow><mfenced><mrow><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>−</mo><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mrow><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>−</mo><mi>t</mi></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mfenced><mrow><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>−</mo><mi>t</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><munderover><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></munderover><mfrac><mrow><mfrac><mi>π</mi><mn>2</mn></mfrac><mi>d</mi><mi>t</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>t</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>t</mi></mrow></mfrac><mo>−</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mi>π</mi><mn>8</mn></mfrac><munderover><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></munderover><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>t</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>t</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mi>π</mi><mn>8</mn></mfrac><munderover><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></munderover><mfrac><mrow><msup><mi>sec</mi><mn>4</mn></msup><mi>t</mi><mi>d</mi><mi>t</mi></mrow><mrow><msup><mi>tan</mi><mn>4</mn></msup><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>t</mi><mo>=</mo><mi>y</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sec</mi><mn>2</mn></msup><mi>t</mi><mi>d</mi><mi>t</mi><mo>=</mo><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mi>π</mi><mn>8</mn></mfrac><munderover><mo>∫</mo><mn>0</mn><mi>∞</mi></munderover><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>4</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mi>π</mi><mn>16</mn></mfrac><munderover><mo>∫</mo><mn>0</mn><mi>∞</mi></munderover><mfrac><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>y</mi><mn>2</mn></msup></mfrac></mrow><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>y</mi><mn>2</mn></msup></mfrac></mrow></mfrac><mi>d</mi><mi>y</mi></math></p><p>Putting, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>−</mo><mfrac><mn>1</mn><mi>y</mi></mfrac><mo>=</mo><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mi>π</mi><mn>16</mn></mfrac><munderover><mo>∫</mo><mrow><mo>−</mo><mi>∞</mi></mrow><mi>∞</mi></munderover><mfrac><mrow><mi>d</mi><mi>p</mi></mrow><mrow><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mi>π</mi><mrow><mn>16</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><msubsup><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>p</mi><msqrt><mn>2</mn></msqrt></mfrac></mfenced></mrow></mfenced><mrow><mo>−</mo><mi>∞</mi></mrow><mi>∞</mi></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><msup><mi>π</mi><mn>2</mn></msup><mrow><mn>16</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><msup><mi>π</mi><mn>2</mn></msup></mrow><mn>32</mn></mfrac></math></p>

</details>

---

### Q38. JEE Main 2024 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mfrac><mn>120</mn><msup><mi>π</mi><mn>3</mn></msup></mfrac><munderover><mo>∫</mo><mn>0</mn><mi>π</mi></munderover><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></mfenced></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **15**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">π</mi></msubsup><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mo>d</mo><mi>x</mi></math></p><p>Now using the property <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mn>0</mn><mrow><mn>2</mn><mi>a</mi></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>+</mo><msubsup><mo>∫</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced><mrow><mn>2</mn><mi>a</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>d</mo><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mfenced><mrow><mi mathvariant="normal">π</mi><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mfenced><mrow><mn>2</mn><mi>πx</mi><mo>-</mo><msup><mi mathvariant="normal">π</mi><mn>2</mn></msup></mrow></mfenced><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mn>2</mn><mi>π</mi><munder><munder><mrow><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>x</mi><mo>·</mo><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mo>d</mo><mi>x</mi></mrow><mo>⏟</mo></munder><msub><mi>I</mi><mn>1</mn></msub></munder><mo>-</mo><msup><mi mathvariant="normal">π</mi><mn>2</mn></msup><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mo>d</mo><mi>x</mi></math></p><p>Now, solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>x</mi><mo>·</mo><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mfenced><mrow><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>·</mo><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Adding both equations we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><mi mathvariant="normal">π</mi><mn>4</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Now, putting the value in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mn>2</mn><mi>π</mi><mo>·</mo><mfrac><mi mathvariant="normal">π</mi><mn>4</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>x</mi><mo>·</mo><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>-</mo><msup><mi mathvariant="normal">π</mi><mn>2</mn></msup><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><msup><mi mathvariant="normal">π</mi><mn>2</mn></msup><mn>2</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><msup><mi mathvariant="normal">π</mi><mn>2</mn></msup><mn>2</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><msup><mi mathvariant="normal">π</mi><mn>2</mn></msup><mn>2</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfrac><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><msup><mi mathvariant="normal">π</mi><mn>2</mn></msup><mn>2</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mstyle displaystyle="true"><mi>sin</mi><mn>2</mn><mi>x</mi></mstyle><mrow><mn>2</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfrac><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><msup><mi mathvariant="normal">π</mi><mn>2</mn></msup><mn>2</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mstyle displaystyle="true"><mi>sin</mi><mn>2</mn><mi>x</mi></mstyle><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfrac><mo>d</mo><mi>x</mi></math></p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>x</mi><mo>=</mo><mi>t</mi><mo>⇒</mo><mo>-</mo><mn>2</mn><mi>sin</mi><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><msup><mi mathvariant="normal">π</mi><mn>2</mn></msup><mn>2</mn></mfrac><msubsup><mo>∫</mo><mn>1</mn><mrow><mo>-</mo><mn>1</mn></mrow></msubsup><mfrac><mstyle displaystyle="true"><mo>-</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mn>2</mn></mfrac></mstyle><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mo>d</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><msup><mi mathvariant="normal">π</mi><mn>2</mn></msup><mn>4</mn></mfrac><msubsup><mo>∫</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>1</mn></msubsup><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mo>d</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><msup><mi mathvariant="normal">π</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>·</mo><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><msup><mi mathvariant="normal">π</mi><mn>3</mn></msup><mn>8</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>120</mn><msup><mi mathvariant="normal">π</mi><mn>3</mn></msup></mfrac><mfenced close="|" open="|"><mrow><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">π</mi></msubsup><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mo>d</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mn>120</mn><msup><mi mathvariant="normal">π</mi><mn>3</mn></msup></mfrac><mo>×</mo><mfrac><msup><mi mathvariant="normal">π</mi><mn>3</mn></msup><mn>8</mn></mfrac><mo>=</mo><mn>15</mn></math></p>

</details>

---

### Q39. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>,</mo><mi>g</mi><mo>:</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo> </mo><mi>∞</mi></mrow></mfenced><mo>→</mo><mi>R</mi></math> be two functions defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>∫</mo><mrow><mo>−</mo><mi>x</mi></mrow><mi>x</mi></msubsup><mfenced><mrow><mfenced close="|" open="|"><mi>t</mi></mfenced><mo>−</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>t</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><msup><mi>x</mi><mn>2</mn></msup></msubsup><msup><mi>t</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>t</mi></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mfenced><mrow><mi>f</mi><mfenced><mrow><msqrt><msub><mi>log</mi><mi>e</mi></msub><mn>9</mn></msqrt><mo>+</mo><mi>g</mi><mfenced close=""><msqrt><msub><mi>log</mi><mi>e</mi></msub><mn>9</mn></msqrt></mfenced></mrow></mfenced></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><msup><mi>x</mi><mn>2</mn></msup></msubsup><msup><mi>t</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><msup><mi>e</mi><mrow><mo>−</mo><mi>t</mi></mrow></msup><mi>d</mi><mi>t</mi></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><msup><mi>y</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>d</mi><mi>t</mi><mo>=</mo><mn>2</mn><mi>y</mi><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mi>x</mi></msubsup><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msubsup><mo>∫</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>t</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>t</mi></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msubsup><mo>∫</mo><mn>0</mn><mi>x</mi></msubsup><mfenced><mrow><mi>t</mi><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>t</mi></math>y</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msubsup><mo>∫</mo><mn>0</mn><mi>x</mi></msubsup><mi>t</mi><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>t</mi></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup><mo>=</mo><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi><mo>=</mo><mi>d</mi><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><msup><mi>x</mi><mn>2</mn></msup></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>p</mi></mrow></msup><mi>d</mi><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>9</mn><mi>f</mi><mfenced><msqrt><msub><mi>log</mi><mi>e</mi></msub><mn>9</mn></msqrt></mfenced><mo>+</mo><mi>g</mi><mfenced><msqrt><msub><mi>log</mi><mi>e</mi></msub><mn>9</mn></msqrt></mfenced><mo>=</mo><mn>9</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>log</mi><mn>9</mn></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>9</mn><mi>f</mi><mfenced><msqrt><msub><mi>log</mi><mi>e</mi></msub><mn>9</mn></msqrt></mfenced><mo>+</mo><mi>g</mi><mfenced><msqrt><msub><mi>log</mi><mi>e</mi></msub><mn>9</mn></msqrt></mfenced><mo>=</mo><mn>9</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>9</mn><mi>f</mi><mfenced><msqrt><msub><mi>log</mi><mi>e</mi></msub><mn>9</mn></msqrt></mfenced><mo>+</mo><mi>g</mi><mfenced><msqrt><msub><mi>log</mi><mi>e</mi></msub><mn>9</mn></msqrt></mfenced><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q40. JEE Main 2024 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>ℝ</mi><mo>→</mo><mi>ℝ</mi></math> be a function defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mn>4</mn><mi>x</mi></msup><mrow><msup><mn>4</mn><mi>x</mi></msup><mo>+</mo><mn>2</mn></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><munderover><mo>∫</mo><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced></mrow><mrow><mi>f</mi><mfenced><mrow><mn>1</mn><mo>−</mo><mi>a</mi></mrow></mfenced></mrow></munderover><mi>x</mi><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mrow><mi>x</mi><mfenced><mrow><mn>1</mn><mo>−</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>=</mo><munderover><mo>∫</mo><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced></mrow><mrow><mi>f</mi><mfenced><mrow><mn>1</mn><mo>−</mo><mi>a</mi></mrow></mfenced></mrow></munderover><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mrow><mi>x</mi><mfenced><mrow><mn>1</mn><mo>−</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>;</mo><mo> </mo><mi>a</mi><mo>≠</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mi>M</mi><mo>=</mo><mi>β</mi><mi>N</mi><mo>,</mo><mi>α</mi><mo>,</mo><mo> </mo><mi>β</mi><mo>∈</mo><mi>ℕ</mi></math>, then the least value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup></math> is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mn>4</mn><mi>x</mi></msup><mrow><msup><mn>4</mn><mi>x</mi></msup><mo>+</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><msup><mn>4</mn><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></msup><mrow><msup><mn>4</mn><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mn>4</mn><mrow><mn>4</mn><mo>+</mo><mn>2</mn><mo>·</mo><msup><mn>4</mn><mi>x</mi></msup></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mrow><mn>2</mn><mo>+</mo><msup><mn>4</mn><mi>x</mi></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mn>1</mn><mo>−</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p>Now, solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><munderover><mo>∫</mo><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced></mrow><mrow><mi>f</mi><mfenced><mrow><mn>1</mn><mo>−</mo><mi>a</mi></mrow></mfenced></mrow></munderover><mi>x</mi><mo>·</mo><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mrow><mi>x</mi><mfenced><mrow><mn>1</mn><mo>−</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Now, using the formula <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><msubsup><mo>∫</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>d</mo><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>M</mi><mo>=</mo><munderover><mo>∫</mo><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced></mrow><mrow><mi>f</mi><mfenced><mrow><mn>1</mn><mo>−</mo><mi>a</mi></mrow></mfenced></mrow></munderover><mfenced><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mo>-</mo><mi>x</mi></mrow></mfenced><mo>·</mo><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mo>-</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>−</mo><mfenced><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>M</mi><mo>=</mo><munderover><mo>∫</mo><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced></mrow><mrow><mi>f</mi><mfenced><mrow><mn>1</mn><mo>−</mo><mi>a</mi></mrow></mfenced></mrow></munderover><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>·</mo><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>M</mi><mo>=</mo><munderover><mo>∫</mo><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced></mrow><mrow><mi>f</mi><mfenced><mrow><mn>1</mn><mo>−</mo><mi>a</mi></mrow></mfenced></mrow></munderover><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>-</mo><munderover><mo>∫</mo><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced></mrow><mrow><mi>f</mi><mfenced><mrow><mn>1</mn><mo>−</mo><mi>a</mi></mrow></mfenced></mrow></munderover><mi>x</mi><mo>·</mo><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>M</mi><mo>=</mo><mi>N</mi><mo>−</mo><mi>M</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>M</mi><mo>=</mo><mi>N</mi></math></p><p>So, on comparing we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup><mo>=</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q41. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>→</mo><mi>R</mi></math> be defined <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mi>b</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>c</mi><mi>x</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfenced><mo>=</mo><mn>21</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mn>0</mn><mrow><mi>log</mi><mn>4</mn></mrow></msubsup><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>c</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>39</mn><mn>2</mn></mfrac></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>|</mo></math> equals:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<blockquote><p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mi>b</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>c</mi><mi>x</mi><mo>,</mo><mo> </mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo> </mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mrow><mi>log</mi><mn>2</mn></mrow></mfenced><mo>=</mo><mn>21</mn><mo>,</mo><mo> </mo><msubsup><mo>∫</mo><mn>0</mn><mrow><mi>log</mi><mn>4</mn></mrow></msubsup><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>c</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mn>39</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>a</mi><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mi>b</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mrow><mi>log</mi><mn>2</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mi>a</mi><mfenced><mn>4</mn></mfenced><mo>+</mo><mi>b</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>c</mi><mo>=</mo><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>8</mn><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>21</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mn>0</mn><mrow><mi>log</mi><mn>4</mn></mrow></msubsup><mfenced><mrow><mi>a</mi><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mi>b</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>c</mi><mi>x</mi><mo>-</mo><mi>c</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mn>39</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msubsup><mo>∫</mo><mn>0</mn><mrow><mi>log</mi><mn>4</mn></mrow></msubsup><mfenced><mrow><mi>a</mi><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mi>b</mi><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mo>=</mo><mfrac><mn>39</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><mrow><mi>a</mi><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mi>b</mi><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mn>0</mn><mrow><mi>log</mi><mn>4</mn></mrow></msubsup><mo>=</mo><mfrac><mn>39</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>a</mi><msup><mi>e</mi><mrow><mn>2</mn><mi>log</mi><mn>4</mn></mrow></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mi>b</mi><msup><mi>e</mi><mrow><mi>log</mi><mn>4</mn></mrow></msup><mo>-</mo><mfrac><mi>a</mi><mn>2</mn></mfrac><mo>-</mo><mi>b</mi><mo>=</mo><mfrac><mn>39</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mn>15</mn><mi>a</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mn>3</mn><mi>b</mi><mo>=</mo><mfrac><mn>39</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>15</mn><mi>a</mi><mo>+</mo><mn>6</mn><mi>b</mi><mo>=</mo><mn>39</mn></math></p><p>Using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>15</mn><mi>a</mi><mo>+</mo><mn>6</mn><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mo>=</mo><mn>39</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>15</mn><mi>a</mi><mo>-</mo><mn>6</mn><mo>-</mo><mn>6</mn><mi>a</mi><mo>=</mo><mn>39</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>9</mn><mi>a</mi><mo>=</mo><mn>45</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>-</mo><mn>5</mn><mo>=</mo><mo>-</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>c</mi><mo>=</mo><mn>21</mn><mo>-</mo><mn>8</mn><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>c</mi><mo>=</mo><mn>21</mn><mo>-</mo><mn>40</mn><mo>+</mo><mn>12</mn><mo>=</mo><mo>-</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>c</mi><mo>=</mo><mo>-</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mn>8</mn></math></p></blockquote>

</details>

---

### Q42. JEE Main 2024 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

The value <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msubsup><mo>∫</mo><mn>0</mn><mn>9</mn></msubsup><mfenced close="]" open="["><msqrt><mfrac><mrow><mn>10</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msqrt></mfenced><mi>dx</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>, is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **155**

**Detailed Solution:**

<p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mn>9</mn></msubsup><mfenced close="]" open="["><mrow><msqrt><mfrac><mrow><mn>10</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msqrt><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p>The square of integers are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mo> </mo><mn>1</mn><mo>,</mo><mo> </mo><mn>4</mn><mo>,</mo><mo> </mo><mn>9</mn><mo>,</mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>0</mn><mo>=</mo><mfrac><mrow><mn>10</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>1</mn><mo>=</mo><mfrac><mrow><mn>10</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>⇒</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>10</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mo>=</mo><mfrac><mrow><mn>10</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>⇒</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>10</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>9</mn><mo>=</mo><mfrac><mrow><mn>10</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>⇒</mo><mn>9</mn><mi>x</mi><mo>+</mo><mn>9</mn><mo>=</mo><mn>10</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>9</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced></math></p><p>Now, from the above equations using the law <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><msubsup><mo>∫</mo><mi>a</mi><mi>c</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>+</mo><msubsup><mo>∫</mo><mi>c</mi><mi>d</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>+</mo><msubsup><mo>∫</mo><mi>d</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mn>1</mn><mn>9</mn></mfrac></msubsup><mfenced><mn>0</mn></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>∫</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mfrac><mn>2</mn><mn>3</mn></mfrac></msubsup><mfenced><mn>1</mn></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>∫</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mn>9</mn></msubsup><mfenced><mn>2</mn></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo>+</mo><mn>2</mn><mfenced><mrow><mn>9</mn><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>155</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>9</mn><mi>I</mi><mo>=</mo><mn>155</mn></math></p>

</details>

---

### Q43. JEE Main 2024 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mfrac><mi>π</mi><mn>6</mn></mfrac><mfrac><mi>π</mi><mn>3</mn></mfrac></msubsup><msqrt><mn>1</mn><mo>-</mo><mi>sin</mi><mn>2</mn><mi>x</mi></msqrt><mi>d</mi><mi>x</mi><mo>=</mo><mi>α</mi><mo>+</mo><mi>β</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>γ</mi><msqrt><mn>3</mn></msqrt></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>,</mo><mi>β</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>γ</mi></math> are rational numbers, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>α</mi><mo>+</mo><mn>4</mn><mi>β</mi><mo>-</mo><mi>γ</mi></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mfrac><mi>π</mi><mn>6</mn></mfrac><mfrac><mi>π</mi><mn>3</mn></mfrac></msubsup><msqrt><mn>1</mn><mo>-</mo><mi>sin</mi><mn>2</mn><mi>x</mi></msqrt><mi>d</mi><mi>x</mi><mo>=</mo><mi>α</mi><mo>+</mo><mi>β</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>γ</mi><msqrt><mn>3</mn></msqrt></math></p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>∫</mo><mfrac><mi>π</mi><mn>6</mn></mfrac><mfrac><mi>π</mi><mn>3</mn></mfrac></msubsup><msqrt><mn>1</mn><mo>-</mo><mi>sin</mi><mn>2</mn><mi>x</mi></msqrt><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><msubsup><mo>∫</mo><mfrac><mi>π</mi><mn>6</mn></mfrac><mfrac><mi>π</mi><mn>3</mn></mfrac></msubsup><mo>|</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi><mo>|</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><msubsup><mo>∫</mo><mfrac><mi>π</mi><mn>6</mn></mfrac><mfrac><mi>π</mi><mn>4</mn></mfrac></msubsup><mo>(</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>∫</mo><mfrac><mi>π</mi><mn>4</mn></mfrac><mfrac><mi>π</mi><mn>3</mn></mfrac></msubsup><mo>(</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><msqrt><mn>3</mn></msqrt></math></p><p>Now, comparing with </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mi>α</mi><mo>+</mo><mi>β</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>γ</mi><msqrt><mn>3</mn></msqrt></math></p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi>β</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>γ</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>α</mi><mo>+</mo><mn>4</mn><mi>β</mi><mo>-</mo><mi>γ</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q44. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the value of the integral<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mrow><mo>-</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></mrow><mfrac><mi>π</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>π</mi><mi>x</mi></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mn>2023</mn></msup></msup></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mi>π</mi><mn>4</mn></mfrac><mfenced><mrow><mpadded lspace="+2px"><mi>π</mi></mpadded><mo>+</mo><mi>a</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mfrac><mrow><mo>-</mo><mi>π</mi></mrow><mn>2</mn></mfrac><mfrac><mi>π</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>π</mi><mi>x</mi></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><msup><mi>sin</mi><mn>2023</mn></msup><mi>x</mi></mrow></msup></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mi>π</mi><mn>4</mn></mfrac><mfenced><mrow><mi>π</mi><mo>+</mo><mi>α</mi></mrow></mfenced><mo>-</mo><mn>4</mn></math></p><p>Now let, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>∫</mo><mfrac><mrow><mo>-</mo><mi>π</mi></mrow><mn>2</mn></mfrac><mfrac><mi>π</mi><mn>2</mn></mfrac></msubsup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>π</mi><mi>x</mi></msup></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Now using the property <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><msubsup><mo>∫</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>d</mo><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>∫</mo><mfrac><mrow><mo>-</mo><mi>π</mi></mrow><mn>2</mn></mfrac><mfrac><mi>π</mi><mn>2</mn></mfrac></msubsup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>π</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Now adding above equations we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mi>cos</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mi>a</mi></mrow><mi>a</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><mn>2</mn><msubsup><mo>∫</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>,</mo><mo> </mo><mtext>if</mtext><mo> </mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo> </mo><mtext>is even</mtext></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></msubsup><mo>-</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></msubsup><mn>2</mn><mi>x</mi><mo>·</mo><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><msup><mi>π</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>-</mo><mfenced close="]" open="["><mrow><msubsup><mfenced close="]" open="["><mrow><mo>-</mo><mn>2</mn><mi>x</mi><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></msubsup><mo>+</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></msubsup><mn>2</mn><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><msup><mi>π</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>-</mo><mn>2</mn></math></p><p>Similarly solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>∫</mo><mfrac><mrow><mo>-</mo><mi>π</mi></mrow><mn>2</mn></mfrac><mfrac><mi>π</mi><mn>2</mn></mfrac></msubsup><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><msup><mi>sin</mi><mn>2023</mn></msup><mi>x</mi></mrow></msup></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>3</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mfenced close="]" open="["><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mn>3</mn><mi>π</mi></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><msup><mi>π</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>-</mo><mn>2</mn><mo>+</mo><mfrac><mrow><mn>3</mn><mi>π</mi></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>π</mi><mn>4</mn></mfrac><mfenced><mrow><mi>π</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mo>=</mo><mfrac><mi>π</mi><mn>4</mn></mfrac><mfenced><mrow><mi>π</mi><mo>+</mo><mi>α</mi></mrow></mfenced><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q45. JEE Main 2024 (27 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">x</mi></msubsup><mi mathvariant="normal">g</mi><mfenced><mi mathvariant="normal">t</mi></mfenced><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">t</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">t</mi></mrow></mfrac></mfenced><mi>dt</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi></math> is a continuous odd function. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mrow><mo>-</mo><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></mrow><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>+</mo><mfrac><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mi>cosx</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">e</mi><mi mathvariant="normal">x</mi></msup></mrow></mfrac></mrow></mfenced><mi>dx</mi><mo>=</mo><msup><mfenced><mfrac><mi mathvariant="normal">π</mi><mi mathvariant="normal">α</mi></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><mi mathvariant="normal">α</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">α</mi></math> is equal to _____.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">x</mi></msubsup><mi mathvariant="normal">g</mi><mfenced><mi mathvariant="normal">t</mi></mfenced><mi>log</mi><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">t</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">t</mi></mrow></mfrac></mfenced><mi>dt</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">f</mi><mfenced><mrow><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mrow><mo>-</mo><mi mathvariant="normal">x</mi></mrow></msubsup><mi mathvariant="normal">g</mi><mfenced><mi mathvariant="normal">t</mi></mfenced><mi>log</mi><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">t</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">t</mi></mrow></mfrac></mfenced><mi>dt</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">f</mi><mfenced><mrow><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">x</mi></msubsup><mi mathvariant="normal">g</mi><mfenced><mrow><mo>-</mo><mi mathvariant="normal">y</mi></mrow></mfenced><mi>log</mi><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">y</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">y</mi></mrow></mfrac></mfenced><mi>dy</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">x</mi></msubsup><mi mathvariant="normal">g</mi><mo>(</mo><mi mathvariant="normal">y</mi><mo>)</mo><mi>ln</mi><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">y</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">y</mi></mrow></mfrac></mfenced><mi>dy</mi></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi></math> is odd)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>(</mo><mo>-</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>=</mo><mo>-</mo><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>⇒</mo><mi mathvariant="normal">f</mi></math> is also odd.</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></mrow><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>+</mo><mfrac><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mi>cosx</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">e</mi><mi mathvariant="normal">x</mi></msup></mrow></mfrac></mrow></mfenced><mi>dx</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></mrow><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mi mathvariant="normal">f</mi><mo>(</mo><mo>-</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>+</mo><mfrac><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><msup><mi mathvariant="normal">e</mi><mi mathvariant="normal">x</mi></msup><mi>cosx</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">e</mi><mi mathvariant="normal">x</mi></msup></mrow></mfrac></mrow></mfenced><mi>dx</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></mrow><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mi>cosxdx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi mathvariant="normal">I</mi><mo>=</mo><mn>2</mn><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mi>cosxdx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mi>cosxdx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mi>sinx</mi></mrow></mfenced><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mo>-</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mn>2</mn><mi>xsinxdx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><msup><mi mathvariant="normal">π</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>-</mo><mn>2</mn><msubsup><mfenced><mrow><mo>-</mo><mi>xcosx</mi><mo>+</mo><mi>sinx</mi></mrow></mfenced><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><msup><mi mathvariant="normal">π</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>-</mo><mn>2</mn><mo>(</mo><mn>0</mn><mo>+</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><msup><mi mathvariant="normal">π</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><msup><mfenced><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mi mathvariant="normal">α</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q46. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mn>1</mn><mrow><msqrt><mn>3</mn><mo>+</mo><mi>x</mi></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi>x</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>b</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>c</mi><msqrt><mn>3</mn></msqrt></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></math> are rational numbers, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mo> </mo><mi>b</mi><mo>-</mo><mn>4</mn><mi>c</mi></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mn>1</mn><mrow><msqrt><mn>3</mn><mo>+</mo><mi>x</mi></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi>x</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><msqrt><mn>3</mn><mo>+</mo><mi>x</mi></msqrt><mo>-</mo><msqrt><mn>1</mn><mo>+</mo><mi>x</mi></msqrt></mrow><mrow><mo>(</mo><mn>3</mn><mo>+</mo><mi>x</mi><mo>)</mo><mo>-</mo><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msubsup><mo>∫</mo><mn>0</mn><mn>1</mn></msubsup><msqrt><mn>3</mn><mo>+</mo><mi>x</mi></msqrt><mi>d</mi><mi>x</mi><mo>-</mo><msubsup><mo>∫</mo><mn>0</mn><mn>1</mn></msubsup><mo>(</mo><msqrt><mn>1</mn><mo>+</mo><mi>x</mi></msqrt><mo>)</mo><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mfenced close="]" open="["><mrow><mfrac><mrow><mn>2</mn><mo>(</mo><mn>3</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mrow><mn>3</mn></mfrac></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="}" open="{"><mrow><mfenced close="]" open="["><mrow><mfrac><mrow><mn>2</mn><mo>(</mo><mn>3</mn><mo>+</mo><mn>1</mn><msup><mo>)</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><mo>(</mo><mn>1</mn><mo>+</mo><mn>1</mn><msup><mo>)</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced close="]" open="["><mrow><mfrac><mrow><mn>2</mn><mo>(</mo><mn>3</mn><msup><mo>)</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><mo>(</mo><mn>1</mn><msup><mo>)</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="}" open="{"><mrow><mfrac><mrow><mn>2</mn><mo>×</mo><mn>8</mn></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><mo>×</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="}" open="{"><mrow><mn>6</mn><mo>-</mo><mfrac><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mn>3</mn><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msqrt><mn>2</mn></msqrt><mo>=</mo><mi>a</mi><mo>+</mo><mi>b</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>c</mi><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo> </mo><mi>b</mi><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>,</mo><mi>c</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mo> </mo><mi>a</mi><mo>+</mo><mn>3</mn><mo> </mo><mi>b</mi><mo>-</mo><mn>4</mn><mo> </mo><mi>c</mi><mo>=</mo><mn>6</mn><mo>-</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q47. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>5</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mfenced><mrow><mn>2</mn><mo>-</mo><mn>4</mn><mi>x</mi></mrow></mfenced></msup></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow><mi>&#946;</mi></mfrac></mfenced><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>&#62;</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>4</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>4</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>21</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>5</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mfenced><mrow><mn>2</mn><mo>-</mo><mn>4</mn><mi>x</mi></mrow></mfenced></msup></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow><mi>&#946;</mi></mfrac></mfenced></math></p><p>Now let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mn>1</mn><mrow><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></mrow></msup></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mn>1</mn><mrow><mfenced><mrow><mfenced><mfrac><mn>11</mn><mn>4</mn></mfrac></mfenced><mo>-</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></mrow></msup></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p>So, integral becomes,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfrac><mn>1</mn><mrow><mfenced open=""><mrow><msup><mfenced><mfrac><msqrt><mn>11</mn></msqrt><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mi>t</mi></mrow></msup></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mn>0</mn></msubsup><mfrac><mn>1</mn><mrow><mfenced open=""><mrow><msup><mfenced><mfrac><msqrt><mn>11</mn></msqrt><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mi>t</mi></mrow></msup></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi><mo>+</mo><munder><munder><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfrac><mn>1</mn><mrow><mfenced open=""><mrow><msup><mfenced><mfrac><msqrt><mn>11</mn></msqrt><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mi>t</mi></mrow></msup></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi></mrow><mo>&#9183;</mo></munder><msub><mi>I</mi><mn>2</mn></msub></munder></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfrac><mn>1</mn><mrow><mfenced open=""><mrow><msup><mfenced><mfrac><msqrt><mn>11</mn></msqrt><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mi>t</mi></mrow></msup></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi></math>, </p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mo>-</mo><mi>z</mi></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>t</mi><mo>=</mo><mo>-</mo><mi>d</mi><mi>z</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>0</mn></msubsup><mfrac><mrow><mi>d</mi><mi>z</mi></mrow><mrow><mfenced open=""><mrow><msup><mfenced><mfrac><msqrt><mn>11</mn></msqrt><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>z</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mn>4</mn><mi>z</mi></mrow></msup></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mfenced open=""><mrow><msup><mfenced><mfrac><msqrt><mn>11</mn></msqrt><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mn>4</mn><mi>t</mi></mrow></msup></mrow></mfenced></mrow></mfrac></math></p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>&#160;</mo><mtext>in</mtext><mo>&#160;</mo><mi>I</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfrac><mn>1</mn><mrow><mfenced><mrow><msup><mfenced><mfrac><msqrt><mn>11</mn></msqrt><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mi>t</mi></mrow></msup></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><msup><mfenced><mfrac><msqrt><mn>11</mn></msqrt><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mn>4</mn><mi>t</mi></mrow></msup></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfrac><msup><mi>e</mi><mrow><mn>4</mn><mi>t</mi></mrow></msup><mrow><mfenced><mrow><msup><mfenced><mfrac><msqrt><mn>11</mn></msqrt><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mrow><mn>4</mn><mi>t</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><msup><mfenced><mfrac><msqrt><mn>11</mn></msqrt><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mn>4</mn><mi>t</mi></mrow></msup></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfrac><mn>1</mn><mrow><msup><mfenced><mfrac><msqrt><mn>11</mn></msqrt><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mfenced><mfrac><msqrt><mn>11</mn></msqrt><mn>2</mn></mfrac></mfenced></mrow></mfrac><msubsup><mfenced close="]" open="["><mrow><mi>ln</mi><mfenced close="|" open="|"><mfrac><mrow><mfrac><msqrt><mn>11</mn></msqrt><mn>2</mn></mfrac><mo>+</mo><mi>t</mi></mrow><mrow><mfrac><msqrt><mn>11</mn></msqrt><mn>2</mn></mfrac><mo>-</mo><mi>t</mi></mrow></mfrac></mfenced></mrow></mfenced><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>11</mn></msqrt></mrow></mfrac><mi>ln</mi><mfenced><mfrac><mrow><msqrt><mn>11</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><msqrt><mn>11</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>11</mn></msqrt></mrow></mfrac><mi>ln</mi><mfenced><mfrac><mrow><mo>(</mo><msqrt><mn>11</mn></msqrt><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>10</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>11</mn></msqrt></mfrac><mi>ln</mi><mfenced><mfrac><mrow><msqrt><mn>11</mn></msqrt><mo>+</mo><mn>1</mn></mrow><msqrt><mn>10</mn></msqrt></mfrac></mfenced></math></p><p>Now on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>&#945;</mi></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow><mi>&#946;</mi></mfrac></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><msqrt><mn>11</mn></msqrt><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><msqrt><mn>10</mn></msqrt><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>4</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>4</mn></msup><mo>=</mo><mn>21</mn></math></p></blockquote>

</details>

---

### Q48. JEE Main 2023 (12 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>0</mn><mo>.</mo><mn>15</mn></mrow><mrow><mn>0</mn><mo>.</mo><mn>15</mn></mrow></msubsup><mfenced close="|" open="|"><mrow><mn>100</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mi>k</mi><mn>3000</mn></mfrac><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to _____.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **575**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>0</mn><mo>.</mo><mn>15</mn></mrow><mrow><mn>0</mn><mo>.</mo><mn>15</mn></mrow></msubsup><mfenced close="|" open="|"><mrow><mn>100</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><mfrac><mi>k</mi><mn>3000</mn></mfrac></math></p><p>Now we know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>a</mi></mrow><mi>a</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>&#160;</mo><mtext>if</mtext><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mtext>is&#160;even</mtext></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>0</mn><mo>.</mo><mn>15</mn></mrow><mrow><mn>0</mn><mo>.</mo><mn>15</mn></mrow></msubsup><mfenced close="|" open="|"><mrow><mn>100</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>0</mn><mo>.</mo><mn>15</mn></mrow></msubsup><mfenced close="|" open="|"><mrow><mn>100</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>d</mo><mi>x</mi></math></p><p>Now solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>0</mn><mo>.</mo><mn>15</mn></mrow></msubsup><mfenced close="|" open="|"><mrow><mn>100</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><mn>2</mn><mfenced><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>0</mn><mo>.</mo><mn>1</mn></mrow></msubsup><mo>-</mo><mfenced><mrow><mn>100</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>d</mo><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mn>0</mn><mo>.</mo><mn>1</mn></mrow><mrow><mn>0</mn><mo>.</mo><mn>15</mn></mrow></msubsup><mn>100</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>d</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>0</mn><mo>.</mo><mn>15</mn></mrow></msubsup><mfenced close="|" open="|"><mrow><mn>100</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><mn>2</mn><mfenced><mrow><msubsup><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mn>100</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac></mrow></mfenced><mn>0</mn><mrow><mn>0</mn><mo>.</mo><mn>1</mn></mrow></msubsup><mo>+</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><mrow><mn>100</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mrow><mn>0</mn><mo>.</mo><mn>1</mn></mrow><mrow><mn>0</mn><mo>.</mo><mn>15</mn></mrow></msubsup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>0</mn><mo>.</mo><mn>15</mn></mrow></msubsup><mfenced close="|" open="|"><mrow><mn>100</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><mn>2</mn><mfenced><mrow><mfenced><mrow><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>30</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mrow><mn>100</mn><mo>&#215;</mo><msup><mn>15</mn><mn>3</mn></msup></mrow><mrow><mn>3</mn><mo>&#215;</mo><msup><mn>100</mn><mn>3</mn></msup></mrow></mfrac><mo>-</mo><mfrac><mn>15</mn><mn>100</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mn>1</mn><mn>30</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>0</mn><mo>.</mo><mn>15</mn></mrow></msubsup><mfenced close="|" open="|"><mrow><mn>100</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><mn>2</mn><mfenced><mrow><mfrac><mn>2</mn><mn>30</mn></mfrac><mo>+</mo><mfenced><mrow><mfrac><mn>225</mn><mn>2000</mn></mfrac><mo>-</mo><mfrac><mn>15</mn><mn>100</mn></mfrac></mrow></mfenced><mo>+</mo><mfrac><mn>2</mn><mn>30</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>0</mn><mo>.</mo><mn>15</mn></mrow></msubsup><mfenced close="|" open="|"><mrow><mn>100</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><mn>2</mn><mfenced><mrow><mfrac><mn>4</mn><mn>30</mn></mfrac><mo>+</mo><mfenced><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>80</mn></mfrac></mfenced></mrow></mfenced><mo>=</mo><mfenced><mrow><mfrac><mn>8</mn><mn>30</mn></mfrac><mo>-</mo><mfrac><mn>3</mn><mn>40</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>32</mn><mo>-</mo><mn>9</mn></mrow><mn>120</mn></mfrac><mo>=</mo><mfrac><mn>23</mn><mn>120</mn></mfrac><mo>=</mo><mfrac><mn>575</mn><mn>3000</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>0</mn><mo>.</mo><mn>15</mn></mrow></msubsup><mfenced close="|" open="|"><mrow><mn>100</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><mfrac><mn>575</mn><mn>3000</mn></mfrac></math></p><p>Now comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>0</mn><mo>.</mo><mn>15</mn></mrow><mrow><mn>0</mn><mo>.</mo><mn>15</mn></mrow></msubsup><mfenced close="|" open="|"><mrow><mn>100</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><mfrac><mi>k</mi><mn>3000</mn></mfrac></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>575</mn></math></p>

</details>

---

### Q49. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="normal">&#8477;</mi><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be a continuous function satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>sin</mi><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>+</mo><mi>&#945;</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></msubsup><mi>f</mi><mfenced><mrow><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>cos</mi><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced><mrow><mi>sin</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>sin</mi><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>+</mo><mi>&#945;</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></msubsup><mi>f</mi><mfenced><mrow><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>cos</mi><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced><mrow><mi>sin</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>.</mo><mi>sin</mi><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p>Now using property <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>c</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mi>c</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi></math> we get,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></msubsup><mi>f</mi><mfenced><mrow><mi>sin</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced><mrow><mi>sin</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>.</mo><mi>sin</mi><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p>Now using property <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>d</mo><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></msubsup><mi>f</mi><mfenced><mrow><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></msubsup><mi>f</mi><mfenced><mrow><mi>sin</mi><mo>&#160;</mo><mn>2</mn><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></msubsup><mi>f</mi><mfenced><mrow><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mi>cos</mi><mo>&#160;</mo><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></msubsup><mi>f</mi><mfenced><mrow><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mi>cos</mi><mo>&#160;</mo><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></msubsup><mi>f</mi><mfenced><mrow><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>&#160;</mo><mi>cos</mi><mo>&#160;</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>So, the putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced><mrow><mi>sin</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>sin</mi><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>+</mo><mi>&#945;</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></msubsup><mi>f</mi><mfenced><mrow><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>cos</mi><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><msqrt><mn>2</mn></msqrt></math></p>

</details>

---

### Q50. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><msup><mi>e</mi><mrow><mi>min</mi><mfenced close="}" open="{"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced></mrow></mfenced></mrow></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></mtd></mtr><mtr><mtd><msup><mi>e</mi><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>. Then the value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><mrow><mn>3</mn><mi>e</mi></mrow><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>e</mi><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>e</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>e</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><msup><mi>e</mi><mrow><mi>min</mi><mfenced open="{" close="}"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo><mi>x</mi><mo>-</mo><mfenced open="[" close="]"><mi>x</mi></mfenced></mrow></mfenced></mrow></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></mtd></mtr><mtr><mtd><msup><mi>e</mi><mfenced open="[" close="]"><mrow><mi>x</mi><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></mtd></mtr><mtr><mtd><mi>e</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>ln</mi><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>)</mo></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>]</mo></math>, so<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mi>ln</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close="}"><mi>x</mi></mfenced></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#60;</mo><mfenced open="{" close="}"><mi>x</mi></mfenced></math></p><p>Now solving the integral we get,<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>x</mi><mo>&#183;</mo><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>x</mi><mo>&#183;</mo><mi>e</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p>Now in first integral, let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>e</mi><mi>t</mi></msup><mo>&#160;</mo><mi>d</mi><mi>t</mi></mrow></mfenced><mo>+</mo><msubsup><mfenced close="]" open="["><mrow><mi>e</mi><mo>&#183;</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mfrac><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mfrac><mrow><mn>3</mn><mi>e</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>e</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q51. JEE Main 2023 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>t</mi><mo>]</mo></math> denote the greatest integer function. If
<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mo>.</mo><mn>4</mn></mrow></msubsup><mfenced open="[" close="]"><msup><mi>x</mi><mn>2</mn></msup></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>&#947;</mi><msqrt><mn>3</mn></msqrt><mo>+</mo><mi>&#948;</mi><msqrt><mn>5</mn></msqrt><mtext>, then&#160;</mtext><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>+</mo><mi>&#948;</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<blockquote><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mo>.</mo><mn>4</mn></mrow></msubsup><mfenced close="]" open="["><msup><mi>x</mi><mn>2</mn></msup></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>&#947;</mi><msqrt><mn>3</mn></msqrt><mo>+</mo><mi>&#948;</mi><msqrt><mn>5</mn></msqrt><mtext>, then&#160;</mtext><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>+</mo><mi>&#948;</mi></math></p><p>We know that for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></math>​, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math>​​​​​​<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mo>.</mo><mn>4</mn></mrow></msubsup><mfenced open="[" close="]"><msup><mi>x</mi><mn>2</mn></msup></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mn>0</mn><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><msqrt><mn>2</mn></msqrt></msubsup><mn>1</mn><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><msqrt><mn>2</mn></msqrt><msqrt><mn>3</mn></msqrt></msubsup><mn>2</mn><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><msqrt><mn>3</mn></msqrt><mn>2</mn></msubsup><mn>3</mn><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><msqrt><mn>5</mn></msqrt></msubsup><mn>4</mn><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><msqrt><mn>5</mn></msqrt><mrow><mn>2</mn><mo>.</mo><mn>4</mn></mrow></msubsup><mn>5</mn><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>+</mo><mo>(</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn><mo>)</mo><mo>+</mo><mn>2</mn><mo>(</mo><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>)</mo><mo>+</mo><mn>3</mn><mo>(</mo><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>)</mo><mo>+</mo><mn>4</mn><mo>(</mo><msqrt><mn>5</mn></msqrt><mo>-</mo><mn>2</mn><mo>)</mo><mo>+</mo><mn>5</mn><mfenced><mrow><mn>2</mn><mo>.</mo><mn>4</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>5</mn></msqrt></math></p><p>This is in the form of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>&#947;</mi><msqrt><mn>3</mn></msqrt><mo>+</mo><mi>&#948;</mi><msqrt><mn>5</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>9</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>&#948;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>+</mo><mi>&#948;</mi><mo>=</mo><mn>9</mn><mo>-</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>6</mn></math></p><p>Hence this is the required answer.</p></blockquote>

</details>

---

### Q52. JEE Main 2023 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>t</mi><mo>]</mo></math> denote the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>t</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mi>&#960;</mi></mfrac><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></msubsup><mfenced><mrow><mn>8</mn><mfenced open="[" close="]"><mrow><mi>cosec</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mn>5</mn><mfenced open="[" close="]"><mrow><mi>cot</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

<blockquote><p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></msubsup><mfenced><mrow><mn>8</mn><mfenced close="]" open="["><mrow><mi>cosec</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mn>5</mn><mfenced close="]" open="["><mrow><mi>cot</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>8</mn><mo>&#160;</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></msubsup><mfenced close="]" open="["><mrow><mi>cosec</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>-</mo><mn>5</mn><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></msubsup><mfenced close="]" open="["><mrow><mi>cot</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>8</mn><msub><mi>I</mi><mn>1</mn></msub><mo>-</mo><mn>5</mn><msub><mi>I</mi><mn>2</mn></msub></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mn>8</mn><mo>&#160;</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></msubsup><mfenced close="]" open="["><mrow><mi>cosec</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></msubsup><mfenced close="]" open="["><mrow><mi>cot</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Now solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></msubsup><mfenced close="]" open="["><mrow><mi>cosec</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></msubsup><mn>1</mn><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math> </p><p>As when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>6</mn></mfrac></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>cosec</mi><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>cosec</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p>Now solving, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></msubsup><mfenced close="]" open="["><mrow><mi>cot</mi><mo>&#160;</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mn>1</mn><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mn>0</mn><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></msubsup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></msubsup><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math></p><p>Required value will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mi>&#960;</mi></mfrac><mi>I</mi><mo>=</mo><mfrac><mn>2</mn><mi>&#960;</mi></mfrac><mfenced close="]" open="["><mrow><mn>8</mn><mo>&#215;</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mn>5</mn><mo>&#215;</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mn>14</mn></math></p></blockquote>

</details>

---

### Q53. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> be a function satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi mathvariant="normal">&#960;</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>sin</mi><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></math>**

**Detailed Solution:**

<blockquote><p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi mathvariant="normal">&#960;</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now using the property <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi mathvariant="normal">&#960;</mi></msubsup><mi>f</mi><mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>sin</mi><mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi mathvariant="normal">&#960;</mi></msubsup><mi>f</mi><mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>sinx</mi><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi mathvariant="normal">&#960;</mi></msubsup><mfenced close="]" open="["><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>sinx</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><msubsup><mo>&#8747;</mo><mn>0</mn><mi mathvariant="normal">&#960;</mi></msubsup><mi>sinx</mi><mi>d</mi><mi>x</mi></math> {as given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></math>}</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><msubsup><mfenced close="]" open="["><mrow><mo>-</mo><mi>cosx</mi></mrow></mfenced><mn>0</mn><mi mathvariant="normal">&#960;</mi></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mn>2</mn><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q54. JEE Main 2023 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfrac><mrow><msup><mn>5</mn><mrow><mi>cos</mi><mi>x</mi></mrow></msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi><mi>cos</mi><mn>3</mn><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mn>5</mn><mrow><mi>cos</mi><mi>x</mi></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi><mi>&#960;</mi></mrow><mn>16</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **13**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfrac><mrow><msup><mn>5</mn><mrow><mi>cos</mi><mi>x</mi></mrow></msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi><mi>cos</mi><mn>3</mn><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><msup><mn>5</mn><mrow><mi>cos</mi><mi>x</mi></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now using the property <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>d</mo><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfrac><mrow><msup><mn>5</mn><mrow><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi><mi>cos</mi><mn>3</mn><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><msup><mn>5</mn><mrow><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now adding above equations we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi><mi>cos</mi><mn>3</mn><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Now using the property <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>a</mi></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mi>a</mi><mi>a</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>&#160;</mo><mfenced open="{" close="}"><mrow><mtext>when&#160;</mtext><mi>f</mi><mfenced><mi>x</mi></mfenced><mtext>&#160;is&#160;even</mtext></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi><mi>cos</mi><mn>3</mn><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi><mi>cos</mi><mn>3</mn><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi><mfenced><mrow><mo>-</mo><mi>sin</mi><mn>3</mn><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mi>sin</mi><mn>3</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p>Now adding equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>4</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>3</mn><mo>+</mo><mi>cos</mi><mn>4</mn><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mi>cos</mi><mn>3</mn><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mi>sin</mi><mn>3</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mn>3</mn><mo>+</mo><mi>cos</mi><mn>4</mn><mi>x</mi><mo>+</mo><mfenced><mfrac><mrow><mi>cos</mi><mn>3</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>cos</mi><mi>x</mi></mrow><mn>4</mn></mfrac></mfenced><mi>cos</mi><mn>3</mn><mi>x</mi><mo>-</mo><mi>sin</mi><mn>3</mn><mi>x</mi><mfenced><mfrac><mrow><mn>3</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mn>3</mn><mi>x</mi></mrow><mn>4</mn></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>3</mn><mo>+</mo><mi>cos</mi><mn>4</mn><mi mathvariant="normal">x</mi><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mi>cos</mi><mn>4</mn><mi mathvariant="normal">x</mi></mrow></mfenced><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mn>13</mn><mn>4</mn></mfrac><mo>&#215;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>7</mn><mn>4</mn></mfrac><msubsup><mfenced><mfrac><mrow><mi>sin</mi><mn>4</mn><mi mathvariant="normal">x</mi></mrow><mn>4</mn></mfrac></mfenced><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mrow><mn>13</mn><mi>&#960;</mi></mrow><mn>16</mn></mfrac></math>,</p><p>Now on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>k</mi><mi mathvariant="normal">&#960;</mi></mrow><mn>16</mn></mfrac></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>13</mn></math></p>

</details>

---

### Q55. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfrac><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow><mrow><mn>2</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>12</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>6</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>6</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfrac><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow><mrow><mn>2</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now replacing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>&#8594;</mo><mo>-</mo><mi mathvariant="normal">x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfrac><mrow><mo>-</mo><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow><mrow><mn>2</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now both the equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfrac><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mrow><mn>2</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#183;</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>2</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo>&#160;</mo><mi>cos</mi><mn>2</mn><mi>x</mi><mo>&#160;</mo><mtext>is&#160;even&#160;function</mtext></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#183;</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow></mfenced><mi>dx</mi></mrow><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#183;</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>dx</mi></mrow><mrow><mn>3</mn><msup><mi>tan</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>x</mi><mo>=</mo><mi>t</mi><mo>&#8658;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>6</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math></p>

</details>

---

### Q56. JEE Main 2023 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If [ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> denotes the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mn>1</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mi>e</mi></mfrac><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>+</mo><mfenced open="[" close="]"><msup><mi>x</mi><mn>3</mn></msup></mfenced></mrow></msup><mi>d</mi><mi>x</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>9</mn></msup><mo>-</mo><mi>e</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>8</mn></msup><mo>-</mo><mi>e</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>7</mn></msup><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>8</mn></msup><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>8</mn></msup><mo>-</mo><mi>e</mi></math>**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mfenced close="]" open="["><mi>x</mi></mfenced><mo>+</mo><mfenced close="]" open="["><msup><mi>x</mi><mn>3</mn></msup></mfenced></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mfenced close="]" open="["><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mfenced><mo>+</mo><mn>1</mn></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mi>e</mi><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mfenced close="]" open="["><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mfenced></msup><mi>d</mi><mi>x</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mi>e</mi><mn>3</mn></mfrac><msubsup><mo>&#8747;</mo><mn>1</mn><mn>8</mn></msubsup><msup><mi>e</mi><mfenced close="]" open="["><mi>t</mi></mfenced></msup><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mi>e</mi><mn>3</mn></mfrac><mfenced close="}" open="{"><mrow><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>e</mi><mi>d</mi><mi>t</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>3</mn></msubsup><msup><mi>e</mi><mn>2</mn></msup><mi>d</mi><mi>t</mi><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msubsup><mo>&#8747;</mo><mn>7</mn><mn>8</mn></msubsup><msup><mi>e</mi><mn>7</mn></msup><mi>d</mi><mi>t</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mi>e</mi><mn>3</mn></mfrac><mfenced><mrow><mi>e</mi><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>e</mi><mn>7</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><msup><mi>e</mi><mn>2</mn></msup><mn>3</mn></mfrac><mfrac><mfenced><mrow><msup><mi>e</mi><mn>7</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mo>(</mo><mi>e</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mo>(</mo><mi>e</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mi>e</mi></mfrac><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>+</mo><mfenced open="[" close="]"><msup><mi>x</mi><mn>3</mn></msup></mfenced></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>3</mn><mi>e</mi></mfrac><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mfrac><msup><mi>e</mi><mn>2</mn></msup><mn>3</mn></mfrac><mfrac><mfenced><mrow><msup><mi>e</mi><mn>7</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mo>(</mo><mi>e</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>3</mn><mo>(</mo><mi>e</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mi>e</mi></mfrac><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>+</mo><mfenced open="[" close="]"><msup><mi>x</mi><mn>3</mn></msup></mfenced></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><msup><mi>e</mi><mn>8</mn></msup><mo>-</mo><mi>e</mi></math></p>

</details>

---

### Q57. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let [x] denote the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi mathvariant="normal">x</mi></math>. Consider the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>=</mo><mi>max</mi><mfenced open="{" close="}"><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>,</mo><mn>1</mn><mo>+</mo><mo>[</mo><mi>x</mi><mo>]</mo></mrow></mfenced></math>. Then the value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>+</mo><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>8</mn><mo>+</mo><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>+</mo><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Plotting the diagram of the given function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>=</mo><mi>max</mi><mfenced close="}" open="{"><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>,</mo><mn>1</mn><mo>+</mo><mo>[</mo><mi>x</mi><mo>]</mo></mrow></mfenced></math> we get,</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dfb3f118-5f30-48af-896b-ba02644a18f6-9886942.png" style="width: 400px; height: 277px;" /></p><p>Now when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><msqrt><mn>2</mn></msqrt><mo>)</mo><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn></math></p><p>And when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><msqrt><mn>2</mn></msqrt><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p>So, from above diagram area can be calculated as,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mn>1</mn><mo>.</mo><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><msqrt><mn>2</mn></msqrt></msubsup><mn>2</mn><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><msqrt><mn>2</mn></msqrt><mn>2</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn><mo>+</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac></math></p>

</details>

---

### Q58. JEE Main 2023 (24 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>dx</mi></math> is ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **22**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mfenced open="|" close="|"><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>3</mn></msubsup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced open="[" close="]"><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mn>3</mn><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>-</mo><msubsup><mfenced open="[" close="]"><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mn>3</mn><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mfenced open="[" close="]"><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mn>3</mn><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>2</mn><mn>3</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mfenced close="]" open="["><mrow><mfenced><mrow><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>-</mo><mn>6</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mfenced><mrow><mn>9</mn><mo>-</mo><mfrac><mn>27</mn><mn>2</mn></mfrac><mo>+</mo><mn>6</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>-</mo><mn>6</mn><mo>+</mo><mn>4</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>-</mo><mn>3</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mn>16</mn><mn>3</mn></mfrac><mo>-</mo><mn>12</mn><mo>+</mo><mn>8</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>9</mn><mo>-</mo><mfrac><mn>27</mn><mn>2</mn></mfrac><mo>+</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>20</mn><mo>-</mo><mfrac><mn>109</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>11</mn><mn>6</mn></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>I</mi><mo>=</mo><mn>12</mn><mo>&#215;</mo><mfrac><mn>11</mn><mn>6</mn></mfrac><mo>=</mo><mn>22</mn></math></p>

</details>

---

### Q59. JEE Main 2023 (24 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mi>&#960;</mi></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><msup><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2023</mn></msup><mrow><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mn>2023</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2023</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>8</mn><mi>&#960;</mi></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><msup><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2023</mn></msup><mrow><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mn>2023</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2023</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mi>dx</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mo>(</mo><mi>a</mi><mo>-</mo><mi>x</mi><mo>)</mo><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>8</mn><mi>&#960;</mi></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mn>2023</mn></msup><mrow><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mn>2023</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2023</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mn>8</mn><mi>&#960;</mi></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mn>1</mn><mo>&#160;</mo><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mn>8</mn><mi mathvariant="normal">&#960;</mi></mfrac><msubsup><mfenced open="[" close="]"><mi>x</mi></mfenced><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q60. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> denotes the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi mathvariant="normal">t</mi></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced close="]" open="["><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mfenced close="|" open="|"><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>37</mn></msqrt><mo>+</mo><msqrt><mn>13</mn></msqrt><mo>-</mo><mn>4</mn></mrow><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>37</mn></msqrt><mo>-</mo><msqrt><mn>13</mn></msqrt><mo>-</mo><mn>4</mn></mrow><mn>6</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><msqrt><mn>37</mn></msqrt><mo>-</mo><msqrt><mn>13</mn></msqrt><mo>+</mo><mn>4</mn></mrow><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><msqrt><mn>37</mn></msqrt><mo>+</mo><msqrt><mn>13</mn></msqrt><mo>+</mo><mn>4</mn></mrow><mn>6</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>37</mn></msqrt><mo>+</mo><msqrt><mn>13</mn></msqrt><mo>-</mo><mn>4</mn></mrow><mn>6</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced close="]" open="["><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mfenced close="|" open="|"><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced close="]" open="["><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mfenced close="|" open="|"><mrow><mfenced><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mn>1</mn><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>2</mn><mn>3</mn></mfrac></msubsup><mfenced close="]" open="["><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfenced></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mn>1</mn></msubsup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>2</mn><mn>3</mn></mfrac></msubsup><mfenced open="[" close="]"><mrow><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>7</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mn>1</mn></msubsup><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>2</mn><mn>3</mn></mfrac></msubsup><mfenced open="[" close="]"><mrow><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>7</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>The graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>7</mn><mi>x</mi><mo>-</mo><mn>2</mn></math> and </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mn>1</mn></msubsup><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/63130d70-2975-43ab-8d93-a99f2940e5f9-image.png" style="width: 287px; height: 200px;" /></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#945;</mi></msubsup><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mi>&#945;</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msubsup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow><mi>&#946;</mi></msubsup><mn>0</mn><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mi>&#946;</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msubsup><mn>1</mn><mo>&#183;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>-</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4858d51a-cdcb-4527-8ed3-356bcc2913a3-image.png" style="width: 318px; height: 200px;" /></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#8712;</mo><mfenced><mrow><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mn>1</mn></msubsup><mfenced open="[" close="]"><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>1</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>)</mo></mrow></mfenced><mo>+</mo><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>-</mo><mfenced><mrow><mfrac><mrow><mn>7</mn><mo>-</mo><msqrt><mn>37</mn></msqrt></mrow><mn>6</mn></mfrac><mo>+</mo><mfrac><mrow><mn>7</mn><mo>-</mo><msqrt><mn>13</mn></msqrt></mrow><mn>6</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><msqrt><mn>37</mn></msqrt><mo>+</mo><msqrt><mn>13</mn></msqrt></mrow><mn>6</mn></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><msqrt><mn>37</mn></msqrt><mo>+</mo><msqrt><mn>13</mn></msqrt></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msqrt><mn>37</mn></msqrt><mo>+</mo><msqrt><mn>13</mn></msqrt><mo>-</mo><mn>4</mn></mrow><mn>6</mn></mfrac></math></p></blockquote>

</details>

---

### Q61. JEE Main 2022 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>min</mi><mfenced close="}" open="{"><mrow><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mn>10</mn></mrow></mfenced></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> denotes the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>t</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><msup><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mn>2</mn></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><mfenced open="|" close="|"><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math> is equal _______. to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **385**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>min</mi><mfenced close="}" open="{"><mrow><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mn>10</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mn>10</mn></math></p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#183;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mo>-</mo><mn>10</mn><mo>-</mo><mn>9</mn><mo>-</mo><mn>8</mn><mo>-</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mrow><mn>10</mn><mo>&#183;</mo><mn>11</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mo>-</mo><mn>55</mn></math></p><p>Finding<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><mfenced><mrow><mi>f</mi><msup><mfenced><mi>x</mi></mfenced><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msup><mn>10</mn><mn>2</mn></msup><mo>+</mo><msup><mn>9</mn><mn>2</mn></msup><mo>+</mo><msup><mn>8</mn><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>10</mn><mo>&#183;</mo><mn>11</mn><mo>&#183;</mo><mn>21</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mn>385</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><mfenced close="|" open="|"><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mn>10</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>8</mn><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>10</mn><mo>&#183;</mo><mn>11</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>55</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><msup><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mn>2</mn></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><mfenced close="|" open="|"><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>55</mn><mo>+</mo><mn>385</mn><mo>+</mo><mn>55</mn><mo>=</mo><mn>385</mn></math></p></blockquote>

</details>

---

### Q62. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced><mrow><mfenced open="|" close="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced open="[" close="]"><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> is the greatest integer function, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>12</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>31</mn><mn>12</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>12</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced><mrow><mfenced close="|" open="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced close="|" open="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced close="|" open="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>3</mn><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mn>2</mn></msubsup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced><mrow><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac></mrow></mfenced><mn>0</mn><mfrac><mn>3</mn><mn>2</mn></mfrac></msubsup><mo>+</mo><msubsup><mfenced><mrow><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mfrac><mn>27</mn><mn>8</mn></mfrac><mo>-</mo><mfrac><mn>9</mn><mn>4</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>-</mo><mn>6</mn><mo>-</mo><mfrac><mn>9</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>27</mn><mn>8</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>9</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>10</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>19</mn><mn>12</mn></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Assume <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mi>t</mi></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mfrac><mn>3</mn><mn>2</mn></mfrac></msubsup><mfenced close="]" open="["><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><mn>0</mn></msubsup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>t</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mn>0</mn><mo>&#183;</mo><mi>d</mi><mi>t</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mfrac><mn>3</mn><mn>2</mn></mfrac></msubsup><mn>1</mn><mo>&#183;</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced><mrow><mo>-</mo><mi>t</mi></mrow></mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><mn>0</mn></msubsup><mo>+</mo><msubsup><mfenced><mi>t</mi></mfenced><mn>1</mn><mfrac><mn>3</mn><mn>2</mn></mfrac></msubsup><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfenced><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced><mrow><mfenced close="|" open="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>19</mn><mn>12</mn></mfrac></math></p></blockquote>

</details>

---

### Q63. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>5</mn></msubsup><mi>cos</mi><mfenced><mrow><mi>&#960;</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> denotes greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>5</mn></msubsup><mi>cos</mi><mfenced><mrow><mfenced open="[" close="]"><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mi>&#960;</mi><mo>-</mo><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>&#160;</mo><mo>&#8756;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#8658;</mo><mfenced close="]" open="["><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>cos</mi><mfenced><mrow><mo>-</mo><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>4</mn></msubsup><mi>cos</mi><mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>4</mn><mn>5</mn></msubsup><mi>cos</mi><mfenced><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi><mo>-</mo><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mfenced open="[" close="]"><mfrac><mrow><mi>sin&#960;</mi><mi>x</mi></mrow><mi mathvariant="normal">&#960;</mi></mfrac></mfenced><mn>0</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mfenced open="[" close="]"><mrow><mo>-</mo><mfrac><mrow><mi>sin&#960;</mi><mi>x</mi></mrow><mi mathvariant="normal">&#960;</mi></mfrac></mrow></mfenced><mn>2</mn><mn>4</mn></msubsup><mo>+</mo><msubsup><mfenced open="[" close="]"><mfrac><mrow><mi>sin&#960;</mi><mi>x</mi></mrow><mi mathvariant="normal">&#960;</mi></mfrac></mfenced><mn>4</mn><mn>5</mn></msubsup><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q64. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>t</mi></mfenced></math> denote the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>. Then, the value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced open="[" close="]"><mrow><mo>-</mo><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>5</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>-</mo><mn>13</mn></mrow><mn>8</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>-</mo><mn>16</mn></mrow><mn>8</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>-</mo><mn>13</mn></mrow><mn>8</mn></mfrac></math>**

**Detailed Solution:**

<p>The graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>1</mn></math> will be as shown </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dff9c064-12b3-4314-a823-30975cd24459-image.png" style="width: 250px; height: 209px;" /></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced close="]" open="["><mrow><mo>-</mo><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msubsup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfenced><mn>0</mn></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfrac><mn>3</mn><mn>4</mn></mfrac></msubsup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mfrac><mrow><mn>3</mn><mo>+</mo><msqrt><mn>17</mn></msqrt></mrow><mn>8</mn></mfrac></msubsup><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mrow><mn>3</mn><mo>+</mo><msqrt><mn>17</mn></msqrt></mrow><mn>8</mn></mfrac><mn>1</mn></msubsup><mfenced><mrow><mo>-</mo><mn>3</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msubsup><mfenced close="]" open="["><mi>x</mi></mfenced><mn>0</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msubsup><mo>+</mo><mn>0</mn><mo>-</mo><msubsup><mfenced close="]" open="["><mi>x</mi></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac><mfrac><mn>3</mn><mn>4</mn></mfrac></msubsup><mo>+</mo><mo>-</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mi>x</mi></mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac><mfrac><mrow><mn>3</mn><mo>+</mo><msqrt><mn>17</mn></msqrt></mrow><mn>8</mn></mfrac></msubsup><mo>-</mo><mn>3</mn><msubsup><mfenced close="]" open="["><mi>x</mi></mfenced><mfrac><mrow><mn>3</mn><mo>+</mo><msqrt><mn>17</mn></msqrt></mrow><mn>8</mn></mfrac><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfenced><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mn>0</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mfrac><mrow><mn>3</mn><mo>+</mo><msqrt><mn>17</mn></msqrt></mrow><mn>8</mn></mfrac><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced><mo>-</mo><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>3</mn><mo>+</mo><msqrt><mn>17</mn></msqrt></mrow><mn>8</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mrow><mo>-</mo><mn>6</mn><mo>-</mo><mn>2</mn><msqrt><mn>17</mn></msqrt></mrow><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mn>3</mn><mo>+</mo><mfrac><mrow><mn>9</mn><mo>+</mo><mn>3</mn><msqrt><mn>17</mn></msqrt></mrow><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>-</mo><mn>13</mn></mrow><mn>8</mn></mfrac></math></p>

</details>

---

### Q65. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mn>1</mn><msup><mn>7</mn><mfenced close="]" open="["><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></msup></mfrac><mi>d</mi><mi>x</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mo>&#183;</mo></mfenced></math> denotes the greatest integer function, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mn>6</mn><mi>ln</mi><mfenced><mfrac><mn>6</mn><mn>7</mn></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>6</mn><mi>ln</mi><mfenced><mfrac><mn>6</mn><mn>7</mn></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mn>7</mn><mi>ln</mi><mfenced><mfrac><mn>6</mn><mn>7</mn></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>7</mn><mi>ln</mi><mfenced><mfrac><mn>6</mn><mn>7</mn></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>6</mn><mi>ln</mi><mfenced><mfrac><mn>6</mn><mn>7</mn></mfrac></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><msup><mn>7</mn><mfenced open="[" close="]"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></msup></mfrac><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mfrac><mn>1</mn><mn>7</mn></mfrac></mfenced><mfenced open="[" close="]"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></msup><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>7</mn></mfrac><mo>=</mo><mi>k</mi><mo>&#160;</mo><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>k</mi><mfenced open="[" close="]"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>k</mi><mfenced open="[" close="]"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>1</mn></msubsup><msup><mi>k</mi><mfenced open="[" close="]"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><msup><mi>k</mi><mfenced open="[" close="]"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfrac><mn>1</mn><mn>3</mn></mfrac></msubsup><msup><mi>k</mi><mfenced open="[" close="]"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></msup><mi>d</mi><mi>x</mi><mo>+</mo><mo>&#8943;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>I</mi><mo>=</mo><mi>k</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><msup><mi>k</mi><mn>3</mn></msup><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mo>+</mo><mo>&#8943;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfenced><mrow><mi>k</mi><mo>+</mo><mfrac><msup><mi>k</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>k</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mo>&#8943;</mo></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mi>k</mi></mfrac><mfenced><mrow><mfrac><msup><mi>k</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>k</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mo>&#8943;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>k</mi></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mi>k</mi></mfrac><mfenced open="[" close="]"><mrow><mo>-</mo><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>k</mi></mrow></mfenced><mo>-</mo><mi>k</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mi>ln</mi><mfrac><mn>6</mn><mn>7</mn></mfrac><mo>-</mo><mn>7</mn><mfenced open="[" close="]"><mrow><mo>-</mo><mi>ln</mi><mfrac><mn>6</mn><mn>7</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></mrow></mfenced><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mi>k</mi><mo>=</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>I</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>6</mn><mi>ln</mi><mfrac><mn>6</mn><mn>7</mn></mfrac></math></p>

</details>

---

### Q66. JEE Main 2022 (27 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mfrac><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mrow><mi>x</mi><mfenced open="|" close="|"><mi>x</mi></mfenced></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msup><mi>e</mi><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mrow><mi>x</mi><mfenced close="|" open="|"><mi>x</mi></mfenced></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced><mrow><mfrac><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mrow><mi>x</mi><mfenced close="|" open="|"><mi>x</mi></mfenced></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>+</mo><mfrac><mfenced close="|" open="|"><mrow><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi><mfenced close="|" open="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced><mrow><mfrac><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mrow><mi>x</mi><mfenced close="|" open="|"><mi>x</mi></mfenced></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>+</mo><mfrac><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi><mfenced close="|" open="|"><mi>x</mi></mfenced></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced><mrow><mfrac><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>x</mi></mrow><mfenced><mrow><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>+</mo><mfrac><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>x</mi></mrow><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced><mrow><mfrac><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mn>0</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q67. JEE Main 2022 (26 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>48</mn><msup><mi>&#960;</mi><mn>4</mn></msup></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>48</mn><msup><mi>&#960;</mi><mn>4</mn></msup></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi></math></p><p>We get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>48</mn><msup><mi>&#960;</mi><mn>4</mn></msup></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><msup><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>3</mn></msup></mrow></mfenced><mfrac><mrow><mi>sin</mi><mfenced><mrow><mn>0</mn><mo>+</mo><mi mathvariant="normal">&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mrow><mn>0</mn><mo>+</mo><mi mathvariant="normal">&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>48</mn><msup><mi>&#960;</mi><mn>4</mn></msup></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfenced><mrow><mfrac><mrow><mn>3</mn><msup><mi>&#960;</mi><mn>3</mn></msup></mrow><mn>2</mn></mfrac><mo>-</mo><mn>3</mn><msup><mi>&#960;</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>-</mo><msup><mi>&#960;</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><msup><mi>&#960;</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>3</mn><mi>&#960;</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math> ..............equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></p><p>Now adding equation (1) + equation (2)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mn>48</mn><msup><mi>&#960;</mi><mn>4</mn></msup></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfenced><mrow><mfrac><mrow><mn>3</mn><msup><mi>&#960;</mi><mn>3</mn></msup></mrow><mn>2</mn></mfrac><mo>-</mo><msup><mi>&#960;</mi><mn>3</mn></msup></mrow></mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mn>48</mn><msup><mi>&#960;</mi><mn>4</mn></msup></mfrac><mo>&#215;</mo><mfrac><msup><mi>&#960;</mi><mn>3</mn></msup><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mn>24</mn><mi>&#960;</mi></mfrac><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Let  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mo>-</mo><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math> </p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>24</mn><mi>&#960;</mi></mfrac><mo>&#215;</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>0</mn></msubsup><mfrac><mrow><mo>-</mo><mi>d</mi><mi>t</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>24</mn></mrow><mi>&#960;</mi></mfrac><msubsup><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mn>1</mn></msup><mi>t</mi></mrow></mfenced><mn>1</mn><mn>0</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>24</mn><mi>&#960;</mi></mfrac><mfenced close="]" open="["><mrow><mn>0</mn><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mn>6</mn></math></p><p> </p>

</details>

---

### Q68. JEE Main 2022 (26 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>max</mi><mfenced open="{" close="}"><mrow><mfenced open="|" close="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced open="|" close="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mfenced open="|" close="|"><mrow><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>6</mn></mrow><mn>0</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **21**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo></math> max <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ffbebd80-1b0e-4810-abd6-d070566ff789-image.png" style="width: 300px; height: 171px;" /></p><p> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>6</mn></mrow><mn>0</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>6</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msubsup><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>3</mn></mrow><mn>0</mn></msubsup><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>6</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msubsup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>3</mn></mrow><mn>0</mn></msubsup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>6</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msubsup><mo>+</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mn>5</mn><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>3</mn></mrow><mn>0</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfenced close="]" open="["><mrow><mfenced><mrow><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>-</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>18</mn><mo>-</mo><mn>6</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>-</mo><mfenced><mrow><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>-</mo><mn>15</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfenced close="&#8969;" open="["><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mn>12</mn></mrow></mfenced><mo>+</mo><mfrac><mn>21</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>21</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>21</mn><mn>2</mn></mfrac><mo>=</mo><mn>21</mn></math></p>

</details>

---

### Q69. JEE Main 2022 (25 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfrac><mrow><msup><mi mathvariant="normal">e</mi><mrow><mi>cos</mi><mi>x</mi></mrow></msup><mi>sin</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi mathvariant="normal">e</mi><mrow><mi>cos</mi><mi>x</mi></mrow></msup><mo>+</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></msup></mrow></mfenced></mrow></mfrac><mi mathvariant="normal">d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></munderover><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>&#8901;</mo><msup><mi>e</mi><mrow><mi>cos</mi><mi>x</mi></mrow></msup></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mrow><mi>cos</mi><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>&#8722;</mo><mi>cos</mi><mi>x</mi></mrow></msup></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Using property of integral <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mrow><mo>&#8747;</mo><mi>f</mi></mrow><mi>a</mi><mi>b</mi></munderover><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>&#8722;</mo><mi>x</mi></mrow></mfenced><mo>=</mo><munderover><mo>&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p>we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></munderover><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>&#8901;</mo><msup><mi>e</mi><mrow><mo>&#8722;</mo><mi>cos</mi><mi>x</mi></mrow></msup></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mrow><mo>&#8722;</mo><mi>cos</mi><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mi>cos</mi><mi>x</mi></mrow></msup></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Adding equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></munderover><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mfrac><mo>&#8901;</mo><mfrac><mfenced><mrow><msup><mi>e</mi><mrow><mi>cos</mi><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>&#8722;</mo><mi>cos</mi><mi>x</mi></mrow></msup></mrow></mfenced><mrow><msup><mi>e</mi><mrow><mi>cos</mi><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>&#8722;</mo><mi>cos</mi><mi>x</mi></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></munderover><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mn>2</mn><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mo>&#8722;</mo><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8722;</mo><munderover><mo>&#8747;</mo><mn>1</mn><mn>0</mn></munderover><mrow><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><msubsup><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><mi>t</mi></mrow></mfenced><mn>1</mn><mn>0</mn></msubsup></mrow><mo>=</mo><mo>&#8722;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>&#8722;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p>

</details>

---

### Q70. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of the integral<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mfenced><mrow><msup><mi>sin</mi><mn>6</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>6</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#960;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mfenced><mrow><msup><mo>sm</mo><mn>6</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>6</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Now we know <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mfenced><mrow><msup><mi>sin</mi><mn>6</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>6</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mfenced><mrow><msup><mi>sin</mi><mn>6</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>6</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mrow><mo>=</mo><mo>&#8747;</mo></mrow><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>&#8722;</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>&#8722;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfrac></math></p><p>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>4</mn><msup><mi>sec</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi></mrow><mrow><mn>4</mn><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mn>3</mn><msup><mi>tan</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfrac><mrow><mn>4</mn><msup><mi>sec</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow><mrow><mn>4</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mn>2</mn><mi>x</mi><mo>=</mo><mi>t</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>sec</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>4</mn><munderover><mo>&#8747;</mo><mn>0</mn><mo>&#8734;</mo></munderover><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>2</mn></mfrac><msubsup><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><mfrac><mi>t</mi><mn>2</mn></mfrac></mrow></mfenced><mn>0</mn><mo>&#8734;</mo></msubsup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mi>&#960;</mi></math></p>

</details>

---

### Q71. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> is the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>x</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#960;</mi><mn>2</mn></msup><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced><mrow><mi>sin</mi><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfenced open="[" close="]"><mi>x</mi></mfenced></mrow></mfenced><mrow><mo>[</mo><mi>x</mi><mo>]</mo></mrow></msup><mi mathvariant="normal">d</mi><mi>x</mi></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>1</mn><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>(</mo><mi>&#960;</mi><mo>-</mo><mn>1</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>(</mo><mi>&#960;</mi><mo>-</mo><mn>1</mn><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>1</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>(</mo><mi>&#960;</mi><mo>-</mo><mn>1</mn><mo>)</mo></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msup><mi>&#960;</mi><mn>2</mn></msup><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced></mrow></mfenced><mrow><mo>[</mo><mi>x</mi><mo>]</mo></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msup><mi>&#960;</mi><mn>2</mn></msup><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced></mrow></mfenced><mrow><mo>[</mo><mi>x</mi><mo>]</mo></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><msup><mi>&#960;</mi><mn>2</mn></msup><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced></mrow></mfenced><mrow><mo>[</mo><mi>x</mi><mo>]</mo></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msup><mi>&#960;</mi><mn>2</mn></msup><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><msup><mi>x</mi><mn>0</mn></msup><mi>d</mi><mi>x</mi><mo>+</mo><msup><mi>&#960;</mi><mn>2</mn></msup><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>1</mn></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msup><mi>&#960;</mi><mn>2</mn></msup><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msup><mi>&#960;</mi><mn>2</mn></msup><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msup><mi>&#960;</mi><mn>2</mn></msup><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msup><mi>&#960;</mi><mn>2</mn></msup><mfenced close="]" open="["><mrow><mi>x</mi><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mo>d</mo><mi>x</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced close="}" open="{"><mrow><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mi>x</mi><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced><mo>-</mo><msup><mi>&#960;</mi><mn>2</mn></msup><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msup><mi>&#960;</mi><mn>2</mn></msup><msubsup><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><mn>2</mn><mi>&#960;</mi></mfrac><mi>cos</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>+</mo><msup><mi>&#960;</mi><mn>2</mn></msup><msubsup><mrow><mfenced close="" open="["><mrow><mfenced><mi>x</mi></mfenced><mfrac><mn>2</mn><mi>&#960;</mi></mfrac></mrow></mfenced><menclose notation="right"><mfenced><mrow><mo>-</mo><mi>cos</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced></menclose></mrow><mn>1</mn><mn>2</mn></msubsup><mfenced close="]" open=""><mrow><mo>-</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfrac><mn>2</mn><mi>&#960;</mi></mfrac><mfenced><mrow><mo>-</mo><mi>cos</mi><mfrac><mrow><mi>&#960;</mi><mi mathvariant="normal">x</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mo>&#215;</mo><mfrac><mn>2</mn><mi mathvariant="normal">&#960;</mi></mfrac><msubsup><mfenced close="]" open="["><mrow><mi>cos</mi><mfenced><mfrac><mi>&#960;x</mi><mn>2</mn></mfrac></mfenced></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msup><mi>&#960;</mi><mn>2</mn></msup><msubsup><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><mn>2</mn><mi>&#960;</mi></mfrac><mi>cos</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>+</mo><msup><mi>&#960;</mi><mn>2</mn></msup><msubsup><mrow><mfenced close="" open="["><mrow><mfenced><mi>x</mi></mfenced><mfrac><mn>2</mn><mi>&#960;</mi></mfrac></mrow></mfenced><menclose notation="right"><mfenced><mrow><mo>-</mo><mi>cos</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced></menclose></mrow><mn>1</mn><mn>2</mn></msubsup><mfenced close="]" open=""><mrow><mo>+</mo><msup><mfenced><mfrac><mn>2</mn><mi mathvariant="normal">&#960;</mi></mfrac></mfenced><mn>2</mn></msup><msubsup><mfenced close="]" open="["><mrow><mi>sin</mi><mfenced><mfrac><mi>&#960;x</mi><mn>2</mn></mfrac></mfenced></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup></mrow></mfenced><mo>+</mo><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mo>&#215;</mo><mfrac><mn>2</mn><mi mathvariant="normal">&#960;</mi></mfrac><msubsup><mfenced close="]" open="["><mrow><mi>cos</mi><mfenced><mfrac><mi>&#960;x</mi><mn>2</mn></mfrac></mfenced></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>-</mo><msup><mi>&#960;</mi><mn>2</mn></msup><mfenced close="]" open="["><mrow><mfrac><mn>2</mn><mi>&#960;</mi></mfrac><mi>cos</mi><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>-</mo><mfrac><mn>2</mn><mi>&#960;</mi></mfrac><mi>cos</mi><mfenced><mn>0</mn></mfenced></mrow></mfenced><mo>+</mo><msup><mi>&#960;</mi><mn>2</mn></msup><mfenced close="]" open="["><mrow><mn>2</mn><mo>&#215;</mo><mfrac><mn>2</mn><mi>&#960;</mi></mfrac><mfenced><mrow><mo>-</mo><mi>cos</mi><mi>&#960;</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mo>&#215;</mo><mfrac><mn>2</mn><mi>&#960;</mi></mfrac><mo>&#215;</mo><menclose notation="right"><mfenced><mrow><mi>cos</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></menclose></mrow></mfenced><mfenced close="]" open=""><mrow><mo>+</mo><mn>4</mn><mfenced close="]" open="["><mrow><mi>sin</mi><mfenced><mi mathvariant="normal">&#960;</mi></mfenced><mo>-</mo><mi>sin</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></mrow></mfenced><mo>+</mo><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mo>&#215;</mo><mfrac><mn>2</mn><mi mathvariant="normal">&#960;</mi></mfrac><mfenced close="]" open="["><mrow><mi>cos</mi><mfenced><mi mathvariant="normal">&#960;</mi></mfenced><mo>-</mo><mi>cos</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>2</mn><mi>&#960;</mi><mo>+</mo><mn>4</mn><mi>&#960;</mi><mo>+</mo><mn>4</mn><mo>(</mo><mn>0</mn><mo>-</mo><mn>1</mn><mo>)</mo><mo>-</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>4</mn><mi>&#960;</mi><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>4</mn><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

### Q72. JEE Main 2021 (31 Aug Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>t</mi><mo>]</mo></math> denote the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi mathvariant="normal">t</mi><mo>.</mo></math> Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#183;</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><mn>1</mn></msubsup><mo>(</mo><mo>[</mo><mn>2</mn><mi>x</mi><mo>]</mo><mo>+</mo><mo>|</mo><mi>x</mi><mo>|</mo><mo>)</mo><mi mathvariant="normal">d</mi><mi>x</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><mn>1</mn></msubsup><mo>(</mo><mo>[</mo><mn>2</mn><mi>x</mi><mo>]</mo><mo>+</mo><mo>|</mo><mi>x</mi><mo>|</mo><mo>)</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>2</mn><mi>x</mi></mrow></mfenced></math> will be discontinuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;</mo><mo>;</mo><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mo>&#8712;</mo><mo>&#160;</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mo>&#8805;</mo><mo>&#160;</mo><mn>0</mn><mo>&#160;</mo><mo>;</mo><mo>&#160;</mo><mo>-</mo><mi>x</mi><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mo>&#60;</mo><mn>0</mn><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><mn>0</mn></msubsup><mo>(</mo><mo>-</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msubsup><mo>(</mo><mn>0</mn><mo>+</mo><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>1</mn></msubsup><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>x</mi><mi>n</mi></msup><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><msup><mi>x</mi><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced><mrow><mo>-</mo><mi>x</mi><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><mn>0</mn></msubsup><mo>+</mo><msubsup><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mn>0</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mn>0</mn><mo>)</mo><mo>-</mo><mfenced><mrow><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><mn>1</mn></msubsup><mo>(</mo><mo>[</mo><mn>2</mn><mi>x</mi><mo>]</mo><mo>+</mo><mo>|</mo><mi>x</mi><mo>|</mo><mo>)</mo><mi>d</mi><mi>x</mi><mo>=</mo><mn>5</mn></math>.</p>

</details>

---

### Q73. JEE Main 2021 (27 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>6</mn><mn>16</mn></msubsup><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><msub><mi>log</mi><mi>e</mi></msub><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>44</mn><mi>x</mi><mo>+</mo><mn>484</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>6</mn><mn>16</mn></msubsup><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><msup><mi>x</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>d</mi><mi>x</mi></mrow><mrow><msub><mi>log</mi><mi>e</mi></msub><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>44</mn><mi>x</mi><mo>+</mo><mn>484</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>6</mn><mn>16</mn></msubsup><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><msub><mi>log</mi><mi>e</mi></msub><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>22</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>We know</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>d</mo><mi>x</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>6</mn><mn>16</mn></msubsup><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><msup><mfenced><mrow><mn>22</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mrow><mrow><msub><mi>log</mi><mi>e</mi></msub><msup><mfenced><mrow><mn>22</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><msup><mfenced><mrow><mn>22</mn><mo>-</mo><mfenced><mrow><mn>22</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>6</mn><mn>16</mn></msubsup><mfrac><mrow><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><msup><mfenced><mrow><mn>22</mn><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mn>2</mn></msup></mrow><mrow><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>+</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><msup><mfenced><mrow><mn>22</mn><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mi>dx</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p>Add <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>6</mn><mn>16</mn></msubsup><mi>d</mi><mi>x</mi><mo>=</mo><mn>10</mn><mo>,</mo><mi>I</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q74. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If the value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>5</mn></msubsup><mfrac><mrow><mi>x</mi><mo>+</mo><mo>[</mo><mi>x</mi><mo>]</mo></mrow><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mo>[</mo><mi>x</mi><mo>]</mo></mrow></msup></mfrac><mi mathvariant="normal">d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mi>&#946;</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo><mo>&#160;</mo><mn>5</mn><mi>&#945;</mi><mo>+</mo><mn>6</mn><mi>&#946;</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>;</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><msup><mo>)</mo><mn>2</mn></msup></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>5</mn></msubsup><mfrac><mrow><mi>x</mi><mo>+</mo><mo>[</mo><mi>x</mi><mo>]</mo></mrow><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mo>[</mo><mi>x</mi><mo>]</mo></mrow></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>3</mn></msubsup><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></msup></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>3</mn><mn>4</mn></msubsup><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></msup></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>4</mn><mn>5</mn></msubsup><mfrac><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mi>p</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mi>q</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>=</mo><mi>r</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mi>w</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>p</mi><mo>+</mo><mn>2</mn></mrow><msup><mi>e</mi><mi>p</mi></msup></mfrac><mi>d</mi><mi>p</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>q</mi><mo>+</mo><mn>4</mn></mrow><msup><mi>e</mi><mi>q</mi></msup></mfrac><mi>d</mi><mi>q</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>r</mi><mo>+</mo><mn>6</mn></mrow><msup><mi>e</mi><mi>r</mi></msup></mfrac><mi>d</mi><mi>r</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>w</mi><mo>+</mo><mn>8</mn></mrow><msup><mi>e</mi><mi>w</mi></msup></mfrac><mi>d</mi><mi>w</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><msup><mi>e</mi><mi>x</mi></msup></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow><msup><mi>e</mi><mi>x</mi></msup></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>x</mi><mo>+</mo><mn>6</mn></mrow><msup><mi>e</mi><mi>x</mi></msup></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>x</mi><mo>+</mo><mn>8</mn></mrow><msup><mi>e</mi><mi>x</mi></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>20</mn></mrow><msup><mi>e</mi><mi>x</mi></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mn>5</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow><msup><mi>e</mi><mi>x</mi></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><msubsup><mfenced close="]" open="["><mrow><mfenced><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mfrac><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mrow><mo>-</mo><mn>1</mn></mrow></mfrac></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mfenced close="]" open="["><mrow><mo>-</mo><mn>5</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>4</mn><mo>+</mo><mfenced><mrow><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mfenced><mrow><mo>-</mo><mn>6</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>30</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>30</mn><mo>,</mo><mi>&#946;</mi><mo>=</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mn>25</mn></math></p>

</details>

---

### Q75. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>&#960;</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>&#960;</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#8230;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>&#960;</mi><mrow><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Add equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mi>&#960;</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mi>&#960;</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mfenced open="[" close="]"><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mi>&#960;</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mn>0</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mn>0</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mi>&#960;</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math></p>

</details>

---

### Q76. JEE Main 2021 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfenced><mrow><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><mo>-</mo><mfrac><mi>&#946;</mi><mi>e</mi></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msqrt><mi>t</mi></msqrt><msup><mi>e</mi><mi>t</mi></msup><mi>d</mi><mi>t</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>&#160;</mo><mfenced open="{" close="}"><mrow><mtext>applying</mtext><mo>&#160;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>a</mi><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mtext>when</mtext><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>a</mi><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mi>sin</mi><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mi>sin</mi><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi><mo>&#183;</mo><mi>cos</mi><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>sin</mi><mi>x</mi><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><munder><munder><mrow><mi>cos</mi><mi>x</mi></mrow><mo>&#9183;</mo></munder><mi>I</mi></munder><mo>&#183;</mo><munder><munder><mrow><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mfenced><mrow><mo>-</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow><mo>&#9183;</mo></munder><mi>II</mi></munder><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>sin</mi><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mfenced close="]" open="["><mrow><mi>cos</mi><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup></mrow></mfenced><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>sin</mi><mi>x</mi><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>sin</mi><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><mfrac><mrow><msup><mi>e</mi><mi>&#945;</mi></msup><mi>d</mi><mi>&#945;</mi></mrow><msqrt><mn>1</mn><mo>+</mo><mi>&#945;</mi></msqrt></mfrac><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mi>Put</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mi>&#945;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mrow><mn>2</mn><mi>e</mi></mrow></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><msup><mi>e</mi><mi>x</mi></msup><msqrt><mi>x</mi></msqrt></mfrac><mi>d</mi><mi>x</mi><mo>-</mo><mn>1</mn><mfenced><mrow><mi>Put</mi><mo>&#160;</mo><mn>1</mn><mo>+</mo><mi>&#945;</mi><mo>=</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mrow><mn>2</mn><mi>e</mi></mrow></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>e</mi><mi>x</mi></msup><mfrac><mn>1</mn><msqrt><mi>x</mi></msqrt></mfrac><mi>d</mi><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mn>3</mn><mrow><mn>2</mn><mi>e</mi></mrow></mfrac><mfenced><mrow><msubsup><mfenced><mrow><mn>2</mn><msqrt><mi>x</mi></msqrt><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mn>2</mn><msqrt><mi>x</mi></msqrt><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mrow><mn>2</mn><mi>e</mi></mrow></mfrac><mfenced><mrow><mfenced><mrow><mn>2</mn><mi>e</mi></mrow></mfenced><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mn>2</mn><msqrt><mi>x</mi></msqrt><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>-</mo><mfrac><mn>3</mn><mi>e</mi></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>e</mi><mi>x</mi></msup><msqrt><mi>x</mi></msqrt><mi>d</mi><mi>x</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>5</mn><mo>.</mo></math></p>

</details>

---

### Q77. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the definite integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mi>x</mi><mi>cos</mi><mi>x</mi></mrow></msup></mrow></mfenced><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><msqrt><mn>2</mn></msqrt></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mi>x</mi><mi>cos</mi><mi>x</mi></mrow></msup></mrow></mfenced><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi><mi>cos</mi><mi>x</mi></mrow></msup></mrow></mfenced><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Add <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><msup><mi>tan</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></mrow></mfenced><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><msup><mfenced><mrow><mi>tan</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mrow><mi>tan</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mrow><mi>tan</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></mrow></mfenced><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mo>&#8734;</mo></mrow><mn>0</mn></msubsup><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfrac><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi mathvariant="normal">t</mi><msqrt><mn>2</mn></msqrt></mfrac></mfenced></mrow></mfenced><mrow><mo>-</mo><mo>&#8734;</mo></mrow><mn>0</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>0</mn><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math></p>

</details>

---

### Q78. JEE Main 2021 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>1</mn></msubsup><mi>log</mi><mfenced><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfenced><mi>d</mi><mi>x</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>1</mn></msubsup><mi>log</mi><mfenced><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Consider <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>log</mi><mfenced><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfenced></math> </p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>log</mi><mfenced><mrow><mo>-</mo><mi>x</mi><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>log</mi><mfenced><mrow><mi>x</mi><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is an odd function.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>I</mi><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q79. JEE Main 2021 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the definite integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>24</mn></mrow><mrow><mn>5</mn><mi>&#960;</mi><mo>/</mo><mn>24</mn></mrow></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mroot><mrow><mi>tan</mi><mn>2</mn><mi>x</mi></mrow><mn>3</mn></mroot></mrow></mfrac></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>18</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>24</mn></mrow><mrow><mn>5</mn><mi>&#960;</mi><mo>/</mo><mn>24</mn></mrow></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mroot><mrow><mi>tan</mi><mn>2</mn><mi>x</mi></mrow><mn>3</mn></mroot></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>24</mn></mrow><mrow><mn>5</mn><mi>&#960;</mi><mo>/</mo><mn>24</mn></mrow></msubsup><mfrac><mrow><mo>(</mo><mi>cos</mi><mn>2</mn><mi>x</mi><msup><mo>)</mo><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mrow><mrow><mo>(</mo><mi>cos</mi><mn>2</mn><mi>x</mi><msup><mo>)</mo><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>+</mo><mo>(</mo><mi>sin</mi><mn>2</mn><mi>x</mi><msup><mo>)</mo><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>24</mn></mrow><mrow><mn>5</mn><mi>&#960;</mi><mo>/</mo><mn>24</mn></mrow></msubsup><mfrac><msup><mfenced><mrow><mi>cos</mi><mfenced close="}" open="{"><mrow><mn>2</mn><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mrow><msup><mfenced><mrow><mi>cos</mi><mfenced close="}" open="{"><mrow><mn>2</mn><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><msup><mfenced><mrow><mi>sin</mi><mfenced close="}" open="{"><mrow><mn>2</mn><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>24</mn></mrow><mrow><mn>5</mn><mi>&#960;</mi><mo>/</mo><mn>24</mn></mrow></msubsup><mfrac><mrow><mo>(</mo><mi>sin</mi><mn>2</mn><mi>x</mi><msup><mo>)</mo><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mrow><mrow><mo>(</mo><mi>sin</mi><mn>2</mn><mi>x</mi><msup><mo>)</mo><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>+</mo><mo>(</mo><mi>cos</mi><mn>2</mn><mi>x</mi><msup><mo>)</mo><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Adding the equation (i)+(ii), we get</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>24</mn></mrow><mrow><mn>5</mn><mi>&#960;</mi><mo>/</mo><mn>24</mn></mrow></msubsup><mi>d</mi><mi>x</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mi>x</mi></mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>24</mn></mfrac><mfrac><mrow><mn>5</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>24</mn></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mfenced close="]" open="["><mrow><mfrac><mrow><mn>5</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>24</mn></mfrac><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>24</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>24</mn></mfrac><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math></p>

</details>

---

### Q80. JEE Main 2021 (20 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mrow><mi>cos</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mi>t</mi><mo>+</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfenced><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>.</mo></math> Then which one of the following is correct?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>g</mi><mfenced><mn>0</mn></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mo>&#160;</mo><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>g</mi><mfenced><mn>0</mn></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>&#160;</mo><mi>g</mi><mfenced><mn>0</mn></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>g</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mo>&#160;</mo><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>g</mi><mfenced><mn>0</mn></mfenced></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfenced><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mfenced><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfenced></mrow><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>1</mn><mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>1</mn><mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><msup><mfenced><mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is an odd function.</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mrow><mi>cos</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mi>t</mi><mo>+</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mi>cos</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mi>t</mi><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mn>1</mn><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mi>&#960;</mi><mi>cos</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mi>t</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mi>&#960;</mi><mi>cos</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mi>t</mi><mo>+</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is an odd function.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><msqrt><mn>2</mn></msqrt></mfrac><mo>&#8658;</mo><msqrt><mn>2</mn></msqrt><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi mathvariant="normal">&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>&#960;</mi></math></p>

</details>

---

### Q81. JEE Main 2021 (20 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo mathvariant="italic">,</mo></math> then the value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced close="]" open="["><mrow><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>&#960;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi></math>
- **(C)** <span style="font-family:Times New Roman,Times,serif;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></span>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>&#960;</mi></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mfenced open="[" close="]"><mrow><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mfenced><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msubsup><mfenced><mfenced close="]" open="["><mrow><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><mfenced><mfenced close="]" open="["><mrow><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mfenced close="]" open="["><mrow><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mfenced close="]" open="["><mrow><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msubsup><mfenced><mfenced close="]" open="["><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><mfenced><mfenced close="]" open="["><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mfenced close="]" open="["><mrow><mn>0</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msubsup><mi>d</mi><mi>x</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><mi>d</mi><mi>x</mi><mo>-</mo><mn>1</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mn>0</mn><mo>&#183;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mn>1</mn><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mi>&#960;</mi></math></p>

</details>

---

### Q82. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> be a positive real number such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mn>10</mn><mi>e</mi><mo>-</mo><mn>9</mn></math> where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo></math> is the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>e</mi></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>e</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math>**

**Detailed Solution:**

Given:<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#62;</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8804;</mo><mi>a</mi><mo>&#60;</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>W</mi></math></p><p>Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfenced open="[" close="]"><mi>a</mi></mfenced><mo>+</mo><mfenced open="{" close="}"><mi>a</mi></mfenced></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>a</mi></mfenced><mo>=</mo><mi>n</mi></math>
Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mfenced open="[" close="]"><mi>x</mi></mfenced></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mn>10</mn><mi>e</mi><mo>-</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>n</mi></msubsup><msup><mi>e</mi><mfenced open="{" close="}"><mi>x</mi></mfenced></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mi>n</mi><mi>a</mi></msubsup><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mfenced open="[" close="]"><mi>x</mi></mfenced></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mn>10</mn><mi>e</mi><mo>-</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mi>n</mi><mi>a</mi></msubsup><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mi>n</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mn>10</mn><mi>e</mi><mo>-</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>e</mi><mrow><mi>a</mi><mo>-</mo><mi>n</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>10</mn><mi>e</mi><mo>-</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mi>e</mi><mo>-</mo><mi>n</mi><mo>+</mo><msup><mi>e</mi><mrow><mi>a</mi><mo>-</mo><mi>n</mi></mrow></msup><mo>-</mo><mn>1</mn><mo>=</mo><mn>10</mn><mi>e</mi><mo>-</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mi>e</mi><mo>-</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>+</mo><msup><mi>e</mi><mi>a</mi></msup><msup><mi>e</mi><mrow><mo>-</mo><mi>n</mi></mrow></msup><mo>=</mo><mn>10</mn><mi>e</mi><mo>-</mo><mn>9</mn></math></p><p>On comparing, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>10</mn></math></p><p>and,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>+</mo><msup><mi>e</mi><mi>a</mi></msup><msup><mi>e</mi><mrow><mo>-</mo><mi>n</mi></mrow></msup><mo>=</mo><mo>-</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>10</mn><mo>-</mo><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mi>a</mi><mo>-</mo><mn>10</mn></mrow></msup><mo>=</mo><mo>-</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mi>a</mi><mo>-</mo><mn>10</mn></mrow></msup><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mn>10</mn></mrow></mfenced><msub><mi>log</mi><mi>e</mi></msub><mfenced><mi>e</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfenced><mrow><mn>10</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfenced></math></p>

</details>

---

### Q83. JEE Main 2021 (18 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous function in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mn>3</mn><mo>]</mo></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#8804;</mo><mi>f</mi><mfenced><mi>t</mi></mfenced><mo>&#8804;</mo><mn>1</mn></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>]</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>f</mi><mfenced><mi>t</mi></mfenced><mo>&#8804;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#8712;</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>]</mo></math>.</p><p>The largest possible interval in which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mn>3</mn><mo>)</mo></math> lies is :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mn>2</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>]</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#8804;</mo><mi>f</mi><mfenced><mi>t</mi></mfenced><mo>&#8804;</mo><mn>1</mn><mo>&#8704;</mo><mi>t</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>f</mi><mfenced><mi>t</mi></mfenced><mo>&#8804;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8704;</mo><mi>t</mi><mo>&#8712;</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>]</mo></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>3</mn></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>d</mi><mi>t</mi><mo>&#8804;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>&#8804;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mn>1</mn><mo>.</mo><mi>d</mi><mi>t</mi><mo>&#160;&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>1</mn><mn>3</mn></msubsup><mn>0</mn><mi>d</mi><mi>t</mi><mo>&#8804;</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>3</mn></msubsup><mi>f</mi><mfenced><mn>1</mn></mfenced><mi>d</mi><mi>t</mi><mo>&#8804;</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>3</mn></msubsup><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>d</mi><mi>t</mi><mo>&#160;&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Adding, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mn>0</mn><mo>&#8804;</mo><mi>g</mi><mfenced><mn>3</mn></mfenced><mo>&#8804;</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#8804;</mo><mi>g</mi><mfenced><mn>3</mn></mfenced><mo>&#8804;</mo><mn>2</mn></math></p>

</details>

---

### Q84. JEE Main 2021 (18 Mar Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> be two functions satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mo>+</mo><mi>g</mi><mo>(</mo><mn>4</mn><mo>-</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mn>4</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>4</mn></mrow><mn>4</mn></msubsup><mi>f</mi><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mi>d</mi><mi>x</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **512**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>4</mn></mrow><mn>4</mn></msubsup><mi>f</mi><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>4</mn></msubsup><mi>f</mi><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mi>d</mi><mi>x</mi></math> {Even function}</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>4</mn></msubsup><mfenced><mrow><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mi>g</mi><mfenced><mrow><mn>4</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><mfrac><mrow><mn>4</mn><msup><mi>x</mi><mn>4</mn></msup></mrow><mn>4</mn></mfrac><msubsup><mo>|</mo><mn>0</mn><mn>4</mn></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>4</mn></msubsup><mi>g</mi><mfenced><mrow><mn>4</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>512</mn><mo>-</mo><mn>2</mn><msub><mi>I</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>4</mn></msubsup><mi>g</mi><mfenced><mrow><mn>4</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>g</mi><mfenced><mrow><mn>4</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>4</mn></msubsup><mi>g</mi><mfenced><mrow><mn>4</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>4</mn></msubsup><mi>g</mi><mfenced><mrow><mn>4</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>-</mo><mi>x</mi><mo>=</mo><mi>t</mi></math> then </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>0</mn></msubsup><mi>g</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>g</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>g</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>g</mi><mfenced><mrow><mn>4</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>g</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>512</mn></math></p>

</details>

---

### Q85. JEE Main 2021 (17 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><mfrac><mfenced open="[" close="]"><mrow><mi>sin</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi></mrow></mfenced><msup><mi mathvariant="normal">e</mi><mrow><mi>x</mi><mo>-</mo><mfenced open="[" close="]"><mi>x</mi></mfenced></mrow></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mi>&#946;</mi><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup><mo>+</mo><mi>&#947;</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi></math> are integers and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>x</mi></mfenced></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><mfrac><mfenced close="]" open="["><mrow><mi>sin</mi><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced></mrow></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><mfrac><mfenced close="]" open="["><mrow><mi>sin</mi><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mfenced close="}" open="{"><mi>x</mi></mfenced></msup></mfrac><mi>d</mi><mi>x</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>=</mo><mfenced close="}" open="{"><mi>x</mi></mfenced></math> is the fractional part function.</p><p>We know that the <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mi>x</mi></mfenced></math> is a periodic function with period <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and also that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi></math> is a periodic function with period <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow></mfrac><mo>=</mo><mn>1</mn><mo>.</mo></math></p><p>Thus, the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><mrow><mi>sin</mi><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mfenced close="}" open="{"><mi>x</mi></mfenced></msup></mfrac></math> is periodic with period <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is a periodic function with period <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>n</mi><mi>T</mi></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>n</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mi>T</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math></p><p>Therefore <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>10</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mfenced open="[" close="]"><mrow><mi>sin</mi><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mfenced open="{" close="}"><mi>x</mi></mfenced></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>10</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mfenced open="[" close="]"><mrow><mi>sin</mi><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p>Now, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn><mo>&#160;</mo><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>sin</mi><mn>2</mn><mi>&#960;x</mi><mo>&#8804;</mo><mn>1</mn><mo>,</mo></math> hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced></math> can take values <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>10</mn><mfenced><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msubsup><mfrac><mfenced open="[" close="]"><mrow><mi>sin</mi><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow><mn>1</mn></msubsup><mfrac><mfenced open="[" close="]"><mrow><mi>sin</mi><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></mfrac><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>10</mn><mfenced><mrow><mn>0</mn><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow><mn>1</mn></msubsup><mfrac><mrow><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo></mrow><msup><mi>e</mi><mi>x</mi></msup></mfrac><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mn>10</mn><msubsup><mo>&#8747;</mo><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow><mn>1</mn></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>10</mn><msubsup><mfenced open="[" close="]"><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>10</mn><mfenced><mrow><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mi>&#945;</mi><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mi>&#946;</mi><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup><mo>+</mo><mi>&#947;</mi><mo>,</mo></math> thus <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mo>=</mo><mn>0</mn><mo>.</mo></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>10</mn><mo>-</mo><mn>10</mn><mo>=</mo><mn>0</mn><mo>.</mo></math></p>

</details>

---

### Q86. JEE Main 2021 (17 Mar Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>&#183;</mo><mo>]</mo></math> represents the greatest integer function, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><msqrt><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msqrt></msubsup><mfenced close="]" open="["><mrow><mfenced close="]" open="["><msup><mi>x</mi><mn>2</mn></msup></mfenced><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced></math> is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><msqrt><mi>&#960;</mi><mo>/</mo><mn>2</mn></msqrt></msubsup><mfenced><mrow><mfenced close="]" open="["><msup><mi>x</mi><mn>2</mn></msup></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mn>0</mn><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><msqrt><mi>&#960;</mi><mo>/</mo><mn>2</mn></msqrt></msubsup><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><msqrt><mi>&#960;</mi><mo>/</mo><mn>2</mn></msqrt></msubsup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msqrt><mo>-</mo><mn>1</mn><mo>-</mo><msqrt><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msqrt><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi mathvariant="normal">I</mi></mfenced><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q87. JEE Main 2021 (17 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following statement is correct for the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>&#945;</mi><mo>)</mo></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mi>R</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></msubsup><mfrac><mrow><msup><mi>sin</mi><mi>&#945;</mi></msup><mi>x</mi></mrow><mrow><msup><mi>cos</mi><mi>&#945;</mi></msup><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mi>&#945;</mi></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi><mo>(</mo><mi>&#945;</mi><mo>)</mo></math> is a strictly increasing function
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi><mo>(</mo><mi>&#945;</mi><mo>)</mo></math> has an inflection point at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi><mo>(</mo><mi>&#945;</mi><mo>)</mo></math> is a strictly decreasing function
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>&#945;</mi><mo>)</mo></math> is an even function

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>&#945;</mi><mo>)</mo></math> is an even function**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></msubsup><mfrac><mrow><msup><mi>sin</mi><mi>&#945;</mi></msup><mi>x</mi></mrow><mfenced><mrow><msup><mi>sin</mi><mi>&#945;</mi></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mi>&#945;</mi></msup><mi>x</mi></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></msubsup><mfrac><mrow><msup><mi>cos</mi><mi>&#945;</mi></msup><mi>x</mi></mrow><mfenced><mrow><msup><mi>sin</mi><mi>&#945;</mi></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mi>&#945;</mi></msup><mi>x</mi></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>+</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>g</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math></p><p>Which is constant and an even function.</p>

</details>

---

### Q88. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Consider the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><mfrac><mrow><mfenced close="]" open="["><mi>x</mi></mfenced><msup><mi>e</mi><mfenced close="]" open="["><mi>x</mi></mfenced></msup></mrow><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup></mfrac><mi>d</mi><mi>x</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> is equal to :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mfenced><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mfenced><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><mfenced close="]" open="["><mi>x</mi></mfenced><mo>&#183;</mo><msup><mi>e</mi><mrow><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mn>0</mn><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mn>1</mn><mo>&#183;</mo><msup><mi>e</mi><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>3</mn></msubsup><mn>2</mn><mo>&#183;</mo><msup><mi>e</mi><mrow><mn>3</mn><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><msubsup><mo>&#8747;</mo><mn>9</mn><mn>10</mn></msubsup><mn>9</mn><mo>&#183;</mo><msup><mi>e</mi><mrow><mn>10</mn><mo>-</mo><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mn>9</mn></munderover><msubsup><mo>&#8747;</mo><mi>n</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msubsup><mi>n</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn><mo>-</mo><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mn>9</mn></munderover><mi>n</mi><msubsup><mfenced><msup><mi>e</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn><mo>-</mo><mi>x</mi></mrow></msup></mfenced><mi>n</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mn>9</mn></munderover><mi>n</mi><mo>&#183;</mo><mfenced><mrow><msup><mi>e</mi><mn>0</mn></msup><mo>-</mo><msup><mi>e</mi><mn>1</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mn>9</mn></munderover><mi>n</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#183;</mo><mfrac><mrow><mn>9</mn><mo>&#183;</mo><mn>10</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>45</mn><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

### Q89. JEE Main 2021 (26 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfenced open="|" close="|"><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math> is ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mn>2</mn><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>&#960;</mi></mrow></msubsup><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfenced open="|" close="|"><mrow><mi>sin</mi><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mi>sin</mi><mi>t</mi><mo>&#160;</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mo>-</mo><mi>cos</mi><mi>t</mi></mrow></mfenced><mn>0</mn><mi mathvariant="normal">&#960;</mi></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q90. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfrac><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mn>3</mn><mi>x</mi></msup></mrow></mfrac><mo>&#160;</mo><mi>d</mi><mi>x</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#960;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#960;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfrac><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mn>3</mn><mi>x</mi></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfrac><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mn>3</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfrac><mrow><msup><mn>3</mn><mi>x</mi></msup><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mn>3</mn><mi>x</mi></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mn>3</mn><mi>x</mi></msup></mrow></mfenced><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mn>3</mn><mi>x</mi></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mfenced close="]" open="["><mrow><mi>x</mi><mo>+</mo><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p>

</details>

---

### Q91. JEE Main 2021 (25 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mfenced open="|" close="|"><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **19**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mn>3</mn><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mfenced open="[" close="]"><mrow><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msubsup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></msubsup><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mfenced open="[" close="]"><mrow><msubsup><menclose notation="right"><mfenced><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced></menclose><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msubsup><mo>-</mo><msubsup><mfenced><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></msubsup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mfenced open="[" close="]"><mrow><mn>7</mn><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>19</mn></math></p>

</details>

---

### Q92. JEE Main 2021 (25 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>1</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mfenced close="]" open="["><msup><mi>x</mi><mn>3</mn></msup></mfenced></msup><mi>d</mi><mi>x</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> denotes the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>t</mi><mo>,</mo></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn><mi>e</mi></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>3</mn><mi>e</mi></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>3</mn><mi>e</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>3</mn><mi>e</mi></mrow></mfrac></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>1</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mfenced close="]" open="["><msup><mi>x</mi><mn>3</mn></msup></mfenced></msup><mi>d</mi><mi>x</mi></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mfenced close="]" open="["><msup><mi>x</mi><mn>3</mn></msup></mfenced></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mfenced close="]" open="["><msup><mi>x</mi><mn>3</mn></msup></mfenced></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mn>0</mn></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mi>e</mi></mfrac><mo>&#215;</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><msubsup><mfenced close="|" open="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable><mo>+</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mi>e</mi></mfrac><mo>&#215;</mo><mfenced><mrow><mn>0</mn><mo>-</mo><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac></mfenced></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mi>e</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>e</mi></mrow><mrow><mn>3</mn><mi>e</mi></mrow></mfrac></math></p>

</details>

---

### Q93. JEE Main 2021 (24 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of the integral, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>1</mn><mn>3</mn></msubsup><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>1</mn><mn>3</mn></msubsup><mfenced><mrow><mfenced close="]" open="["><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfenced><mo>-</mo><mn>3</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced open="[" close="]"><msup><mi>x</mi><mn>2</mn></msup></mfenced><mi>d</mi><mi>x</mi><mo>-</mo><mn>3</mn><msubsup><mo>&#8747;</mo><mn>1</mn><mn>3</mn></msubsup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mn>0</mn><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><msqrt><mn>2</mn></msqrt></msubsup><mn>1</mn><mo>&#183;</mo><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><msqrt><mn>2</mn></msqrt><msqrt><mn>3</mn></msqrt></msubsup><mn>2</mn><mo>&#183;</mo><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><msqrt><mn>3</mn></msqrt><mn>2</mn></msubsup><mn>3</mn><mo>&#183;</mo><mi>d</mi><mi>x</mi><mo>-</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mrow><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mo>-</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></math></p>

</details>

---

### Q94. JEE Main 2021 (24 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>a</mi></mrow><mi>a</mi></msubsup><mfenced><mrow><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>+</mo><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>22</mn><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>&#62;</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>x</mi></mfenced></math> denotes the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>x</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mrow><mo>-</mo><mi>a</mi></mrow></msubsup><mfenced><mrow><mi>x</mi><mo>+</mo><mfenced open="[" close="]"><mi>x</mi></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>a</mi></mrow><mn>0</mn></msubsup><mfenced><mrow><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mi>a</mi></msubsup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>22</mn></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><msubsup><mo>|</mo><mrow><mo>-</mo><mi>a</mi></mrow><mn>0</mn></msubsup><mo>+</mo><mn>2</mn><mi>x</mi><msubsup><mo>|</mo><mn>0</mn><mn>2</mn></msubsup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><msubsup><mo>|</mo><mn>0</mn><mi>a</mi></msubsup><mo>=</mo><mn>22</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>4</mn><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>a</mi><mo>=</mo><mn>22</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mn>18</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>(</mo><mi>a</mi><mo>&#8800;</mo><mo>-</mo><mn>3</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>3</mn><mrow><mo>-</mo><mn>3</mn></mrow></msubsup><mfenced><mrow><mi>x</mi><mo>+</mo><mfenced close="]" open="["><mi>x</mi></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>3</mn><mrow><mo>-</mo><mn>3</mn></mrow></msubsup><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>3</mn><mrow><mo>-</mo><mn>3</mn></mrow></msubsup><mfenced close="]" open="["><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn><mo>+</mo><mo>-</mo><mfenced><mrow><mo>-</mo><mn>3</mn><mo>-</mo><mn>2</mn><mo>-</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q95. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#960;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mi>sin</mi><mfenced><mrow><mstyle displaystyle="true"><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mstyle><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mi>sin</mi><mfenced><mstyle displaystyle="true"><mo>-</mo><mi>x</mi></mstyle></mfenced></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Using the property, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>c</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mn>1</mn><mi mathvariant="normal">d</mi><mi>x</mi><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi mathvariant="normal">d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mfenced open="[" close="]"><mi>x</mi></mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p>

</details>

---

### Q96. JEE Main 2020 (04 Sep Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mi>x</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>x</mi></mfenced></math> denote the fractional part of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>x</mi></math> respectively of a real number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. if <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>n</mi></msubsup><mfenced open="{" close="}"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>n</mi></msubsup><mfenced open="[" close="]"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mi>n</mi></mrow></mfenced><mo>,</mo><mo>(</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi><mo>,</mo><mi>n</mi><mo>&#62;</mo><mn>1</mn><mo>)</mo></math> are three consecutive terms of a G.P. then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to__

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **21**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>n</mi></msubsup><mfenced open="{" close="}"><mi>x</mi></mfenced><mi mathvariant="normal">d</mi><mi>x</mi><mo>=</mo><mi>n</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>n</mi><msubsup><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>=</mo><mfrac><mi>n</mi><mn>2</mn></mfrac></math>
and <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>n</mi></msubsup><mfenced close="]" open="["><mi>x</mi></mfenced><mi mathvariant="normal">d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>n</mi></msubsup><mfenced><mrow><mi>x</mi><mo>-</mo><mfenced close="}" open="{"><mi>x</mi></mfenced></mrow></mfenced><mi mathvariant="normal">d</mi><mi>x</mi><mo>=</mo><msubsup><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mn>0</mn><mi>n</mi></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>n</mi></msubsup><mfenced close="}" open="{"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><msup><mi>n</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><mi>n</mi><mn>2</mn></mfrac></math>
Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>n</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mi>n</mi></mrow><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mi>n</mi></mrow></mfenced></math> are in Geometric progression</p><p>So,<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mi>n</mi></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mi>n</mi><mn>2</mn></mfrac><mo>&#183;</mo><mn>10</mn><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mi>n</mi></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>=</mo><mn>5</mn><mo>.</mo><msup><mi>n</mi><mn>2</mn></msup><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>20</mn><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>21</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8757;</mo><mi>n</mi><mo>&#8800;</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

### Q97. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>&#160;</mo><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>2</mn><mo>&#8722;</mo><mi>x</mi><mo>;</mo><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;</mtext><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>&#8722;</mo><mn>2</mn><mo>;</mo><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>x</mi><mo>&#8805;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>2</mn><mo>&#8722;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>;</mo><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;</mtext><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8722;</mo><mn>2</mn><mo>;</mo><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>2</mn><mo>&#8722;</mo><mfenced><mrow><mn>2</mn><mo>&#8722;</mo><mi>x</mi></mrow></mfenced><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mn>2</mn><mo>&#8722;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn><mo>,</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mfenced><mrow><mn>2</mn><mo>&#8722;</mo><mi>x</mi></mrow></mfenced><mo>&#8722;</mo><mn>2</mn><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mn>2</mn><mo>&#8722;</mo><mi>x</mi><mo>&#8805;</mo><mn>2</mn><mo>,</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn><mo>&#8722;</mo><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>x</mi><mo>&#8722;</mo><mn>2</mn><mo>&#60;</mo><mn>2</mn><mo>,</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>x</mi><mo>&#8805;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mo>&#8722;</mo><mn>2</mn><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>x</mi><mo>&#8722;</mo><mn>2</mn><mo>&#8805;</mo><mn>2</mn><mo>,</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>x</mi><mo>&#8805;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>2</mn><mo>&#8722;</mo><mfenced><mrow><mn>2</mn><mo>&#8722;</mo><mi>x</mi></mrow></mfenced><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8201;&#8201;&#8201;0&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mfenced><mrow><mn>2</mn><mo>&#8722;</mo><mi>x</mi></mrow></mfenced><mo>&#8722;</mo><mn>2</mn><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8201;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn><mo>&#8722;</mo><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8201;&#8201;&#8201;2&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>4</mn></mtd></mtr><mtr><mtd><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mo>&#8722;</mo><mn>2</mn><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mn>0</mn><mn>3</mn></munderover><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#8722;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mn>2</mn></munderover><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><munderover><mo>&#8747;</mo><mn>2</mn><mn>3</mn></munderover><mfenced><mrow><mn>4</mn><mo>&#8722;</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>&#8722;</mo><munderover><mo>&#8747;</mo><mn>0</mn><mn>3</mn></munderover><mfenced close="|" open="|"><mrow><mi>x</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mn>0</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mfenced close="]" open="["><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn><mn>3</mn></msubsup><mo>-</mo><msubsup><mfenced close="]" open="["><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mn>0</mn><mn>2</mn></msubsup><mo>-</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>2</mn><mn>3</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn></math>.</p>

</details>

---

### Q98. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi></mrow><mi>&#960;</mi></msubsup><mfenced open="|" close="|"><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mfenced open="|" close="|"><mi mathvariant="normal">x</mi></mfenced></mrow></mfenced><mi mathvariant="normal">d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><msup><mi>&#960;</mi><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>&#960;</mi><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#960;</mi><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#960;</mi><mn>2</mn></msup></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi></mrow><mi>&#960;</mi></msubsup><mfenced open="|" close="|"><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mfenced open="|" close="|"><mi mathvariant="normal">x</mi></mfenced></mrow></mfenced><mi mathvariant="normal">d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mfenced open="|" close="|"><mi mathvariant="normal">x</mi></mfenced></mrow></mfenced></math></p><p>Replace <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>x</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mfenced open="|" close="|"><mrow><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced></mrow></mfenced><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mfenced open="|" close="|"><mi mathvariant="normal">x</mi></mfenced></mrow></mfenced></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is an even function.</p><p>Now by the property of definite integration for even function.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi></mrow><mi>&#960;</mi></msubsup><mfenced open="|" close="|"><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mfenced open="|" close="|"><mi mathvariant="normal">x</mi></mfenced></mrow></mfenced><mi mathvariant="normal">d</mi><mi>x</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfenced open="|" close="|"><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mfenced open="|" close="|"><mi mathvariant="normal">x</mi></mfenced></mrow></mfenced><mi mathvariant="normal">d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfenced open="|" close="|"><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mi mathvariant="normal">d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mi mathvariant="normal">d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mi mathvariant="normal">&#960;</mi><mo>-</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">&#960;</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><menclose notation="right"><mfenced><mrow><mi>&#960;x</mi><mo>-</mo><mfrac><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced></menclose><mn>0</mn><mi mathvariant="normal">&#960;</mi></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>-</mo><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mn>0</mn><mo>-</mo><mn>0</mn></mrow></mfenced><mo>=</mo><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></math></p>

</details>

---

### Q99. JEE Main 2020 (02 Sep Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>t</mi></mfenced></math> denote the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced open="|" close="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mfenced open="[" close="]"><mrow><mn>3</mn><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced close="|" open="|"><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mrow><mn>3</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced close="|" open="|"><mrow><mfenced close="}" open="{"><mrow><mn>3</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><mi>x</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mn>3</mn><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>x</mi><mi>d</mi><mi>x</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced open="{" close="}"><mrow><mn>3</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><msubsup><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mn>1</mn><mn>2</mn></msubsup><mo>-</mo><mn>3</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msubsup><mn>3</mn><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mfrac><mn>4</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mn>9</mn><msubsup><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mn>0</mn><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mfenced><mrow><mo>(</mo><mn>1</mn><mo>/</mo><mn>3</mn><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><msup><mn>0</mn><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q100. JEE Main 2020 (02 Sep Shift 1)

*Type:* `numerical` | *Level:* `3`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced open="|" close="|"><mrow><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1.5**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced open="|" close="|"><mrow><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced open="|" close="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>1</mn></msubsup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mo>+</mo><msubsup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>1</mn></msubsup><mo>+</mo><msubsup><mfenced><mi>x</mi></mfenced><mn>1</mn><mn>2</mn></msubsup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mfenced><mrow><mn>0</mn><mo>-</mo><mn>0</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mn>2</mn><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mn>1</mn><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>=</mo><mn>1</mn><mo>.</mo><mn>5</mn></math></p>

</details>

---

### Q101. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>&#960;</mi></mrow></msubsup><mfrac><mrow><mi>x</mi><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math> is equal to:

**Options:**

- **(A)** <math><mn>2</mn><mi>π</mi></math>
- **(B)** <math><mn>2</mn><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(C)** <math><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(D)** <math><mn>4</mn><mi>π</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>&#960;</mi></mrow></msubsup><mfrac><mrow><mi>x</mi><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Use the property <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>&#960;</mi></mrow></msubsup><mfrac><mrow><mfenced><mrow><mn>2</mn><mi>&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mfenced><mrow><mn>2</mn><mi>&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mfenced><mrow><mn>2</mn><mi>&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mn>8</mn></msup><mo>&#8289;</mo><mfenced><mrow><mn>2</mn><mi>&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>&#960;</mi></mrow></msubsup><mfrac><mrow><mfenced><mrow><mn>2</mn><mi>&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Adding equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>&#160;</mo></math>we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>&#960;</mi></mrow></msubsup><mfrac><mrow><mn>2</mn><mi>&#960;</mi><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Use the property <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>a</mi></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced><mrow><mn>2</mn><mi>a</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfrac><mrow><mi>&#960;</mi><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Use the property <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>a</mi></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced><mrow><mn>2</mn><mi>a</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>&#160;</mo></math>we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>4</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi mathvariant="normal">&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfrac><mrow><mi>&#960;</mi><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Use the property <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>4</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi mathvariant="normal">&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfrac><mrow><mi>&#960;</mi><msup><mi>cos</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mi>sin</mi><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></math></p><p>Adding the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced><mo>&#160;</mo></math>we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mn>4</mn><mi mathvariant="normal">&#960;</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi mathvariant="normal">&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mn>1</mn><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn><mi>&#960;</mi><msubsup><mfenced close="]" open="["><mi>x</mi></mfenced><mn>0</mn><mrow><mi mathvariant="normal">&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mo>=</mo><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></math></p>

</details>

---

### Q102. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math><mi>&#945;</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#945;</mi><munderover><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></munderover><msup><mi>e</mi><mrow><mo>-</mo><mi>&#945;</mi><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mn>5</mn></math> , is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced separators="|"><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced separators="|"><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#945;</mi><mfenced open="{" close="}" separators="|"><mrow><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><msup><mi>e</mi><mrow><mi>&#945;</mi><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>&#945;</mi><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>&#945;</mi><mfenced open="{" close="}" separators="|"><mrow><msubsup><mfenced separators="|"><mfrac><msup><mi>e</mi><mrow><mi>&#945;</mi><mi>x</mi></mrow></msup><mi>&#945;</mi></mfrac></mfenced><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><mo>+</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>&#945;</mi><mi>x</mi></mrow></msup><mrow><mo>-</mo><mi>&#945;</mi></mrow></mfrac><msubsup><mfenced open="" close="|" separators="|"><mi>&#8203;</mi></mfenced><mn>0</mn><mn>2</mn></msubsup></mrow></mfenced><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>&#945;</mi><mfenced open="{" close="}" separators="|"><mrow><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>&#945;</mi></mrow></msup></mrow><mi>&#945;</mi></mfrac></mfenced><mo>-</mo><mfenced separators="|"><mfrac><mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>&#945;</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow><mi>&#945;</mi></mfrac></mfenced></mrow></mfenced><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>&#945;</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>&#945;</mi></mrow></msup></mrow></mfenced><mo>=</mo><mn>5</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mi>&#945;</mi></mrow></msup><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>t</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mfenced separators="|"><mrow><mn>2</mn><mi>t</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>&#945;</mi></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mi>ln</mi><mn>2</mn></math></p>

</details>

---

### Q103. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>2</mn><mi>&#960;</mi></mrow></munderover><mrow><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>3</mn><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></math> , where <math><mo>[</mo><mi>t</mi><mo>]</mo></math> denotes the greatest integer function is

**Options:**

- **(A)** <math><mi>π</mi></math>
- **(B)** <math><mn>2</mn><mi>π</mi></math>
- **(C)** <math><mo>-</mo><mi>π</mi></math>
- **(D)** <math><mo>-</mo><mn>2</mn><mi>π</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mo>-</mo><mi>π</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>&#960;</mi></mrow></munderover><mfenced close="]" open="[" separators="|"><mrow><mi>sin</mi><mn>2</mn><mi>x</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>&#960;</mi></mrow></munderover><mfenced close="]" open="[" separators="|"><mrow><mi>sin</mi><mfenced><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mfenced><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math> </p><p>Applying <math><mfenced separators="|"><mrow><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi>a</mi></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi>a</mi></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mrow><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>&#960;</mi></mrow></munderover><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p><math><mn>2</mn><mi>I</mi><mo>=</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>2</mn><mi>&#960;</mi></mrow></munderover><mrow><mfenced separators="|"><mrow><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>3</mn><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mfenced><mo>+</mo><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>3</mn><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>&#960;</mi></mrow></munderover><mo>-</mo><mn>1</mn><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mi>&#160;</mi><mo>{</mo><mo>&#8757;</mo><mi>&#160;</mi><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mi>x</mi></mfenced><mo>+</mo><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mi>&#160;</mi><mo>:</mo><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">I</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn><mi>&#160;</mi><mo>:</mo><mi>x</mi><mo>&#8713;</mo><mi mathvariant="normal">I</mi></mtd></mtr></mtable><mi>&#160;</mi></mrow></mfenced><mspace linebreak="newline"></mspace></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mn>0</mn><mrow><mn>2</mn><mi>&#960;</mi></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>I</mi><mo>=</mo><mi>&#160;</mi><mo>-</mo><mi>&#960;</mi></math></p>

</details>

---

### Q104. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></munderover><mfrac><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mn>3</mn></msup><mi>x</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math> is:

**Options:**

- **(A)** <math><mfrac><mrow><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>π</mi><mo>-</mo><mn>2</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>π</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>π</mi><mo>-</mo><mn>2</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mi>π</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi><mi>&#160;</mi><mo>+</mo><mi>&#160;</mi><mi>cos</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Using property of definite integration <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mn>3</mn></msup><mfenced separators="|"><mrow><mstyle displaystyle="true"><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mstyle><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mi>sin</mi><mfenced separators="|"><mrow><mstyle displaystyle="true"><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mstyle><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mi>cos</mi><mfenced separators="|"><mrow><mstyle displaystyle="true"><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mstyle><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>&#160;</mi><mi>d</mi><mi>x</mi></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>cos</mi><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>cos</mi><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>sin</mi><mi>x</mi><mo>,</mo></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><msup><mi>cos</mi><mn>3</mn></msup><mfenced separators="|"><mstyle displaystyle="true"><mi>x</mi></mstyle></mfenced></mrow><mrow><mi>cos</mi><mfenced separators="|"><mstyle displaystyle="true"><mi>x</mi></mstyle></mfenced><mo>+</mo><mi>sin</mi><mfenced separators="|"><mstyle displaystyle="true"><mi>x</mi></mstyle></mfenced></mrow></mfrac><mi>&#160;</mi><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>On adding the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mn>3</mn></msup><mi>x</mi><mo>+</mo><mi>&#160;</mi><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mn>3</mn></msup><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mi>sin</mi><mo>&#160;</mo><mi>x</mi><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mi>sin</mi><mo>&#160;</mo><mi>x</mi><mi>cos</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi><mo>=</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mi>&#160;</mi><msubsup><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi><mo>+</mo><mfrac><mrow><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><mn>4</mn></mfrac></mrow></mfenced><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mi>cos</mi><mn>2</mn><mfenced><mstyle displaystyle="true"><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow><mn>4</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>0</mn><mo>+</mo><mfrac><mrow><mi>cos</mi><mn>2</mn><mfenced><mstyle displaystyle="true"><mn>0</mn></mstyle></mfenced></mrow><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced separators="|"><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q105. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi><mo>,</mo></mrow></mrow></math> where <math><mi>g</mi></math> is a non-zero even function. If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>,</mo></math> then <math><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>f</mi><mo>(</mo><mi>t</mi><mo>)</mo><mi>d</mi><mi>t</mi></mrow></mrow></math> equals

**Options:**

- **(A)** <math><mrow><munderover><mo stretchy="true">∫</mo><mrow><mn>5</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>5</mn></mrow></munderover><mrow><mi>g</mi><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mrow><mi>d</mi><mi>t</mi></math>
- **(B)** <math><mi mathvariant="normal"> </mi><mrow><munderover><mo stretchy="true">∫</mo><mrow><mi>x</mi><mo>+</mo><mn>5</mn></mrow><mrow><mn>5</mn></mrow></munderover><mrow><mi>g</mi><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mrow><mi>d</mi><mi>t</mi></math>
- **(C)** <math><mn>5</mn><mrow><munderover><mo stretchy="true">∫</mo><mrow><mi>x</mi><mo>+</mo><mn>5</mn></mrow><mrow><mn>5</mn></mrow></munderover><mrow><mi>g</mi><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mrow><mi>d</mi><mi>t</mi></math>
- **(D)** <math><mn>2</mn><mrow><munderover><mo stretchy="true">∫</mo><mrow><mn>5</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>5</mn></mrow></munderover><mrow><mi>g</mi><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mrow><mi>d</mi><mi>t</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi mathvariant="normal"> </mi><mrow><munderover><mo stretchy="true">∫</mo><mrow><mi>x</mi><mo>+</mo><mn>5</mn></mrow><mrow><mn>5</mn></mrow></munderover><mrow><mi>g</mi><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mrow><mi>d</mi><mi>t</mi></math>**

**Detailed Solution:**

<u>Given</u>: <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is an even function, then
<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>g</mi><mo>(</mo><mi>t</mi><mo>)</mo><mi>d</mi><mi>t</mi></mrow></mrow></math> will be an odd function,
<math><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>
Let <math><mi>I</mi><mo>=</mo><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></mrow></mrow></math> put <math><mi>t</mi><mo>=</mo><mi>z</mi><mo>+</mo><mn>5</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><munderover><mo stretchy="true">&#8747;</mo><mrow><mo>-</mo><mn>5</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></munderover><mi>f</mi><mfenced separators="|"><mrow><mi>z</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mi>d</mi><mi>z</mi></math>
<math><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mo>-</mo><mn>5</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></munderover><mrow><mi>g</mi><mo>(</mo><mi>z</mi><mo>)</mo><mi>d</mi><mi>z</mi></mrow></mrow></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mo>&#8757;</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><munderover><mo stretchy="true">&#8747;</mo><mrow><mo>-</mo><mn>5</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></munderover><mrow><msup><mi>f</mi><mi>&#39;</mi></msup><mo>(</mo><mi>z</mi><mo>)</mo><mi>d</mi><mi>z</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mo>(</mo><mo>&#8757;</mo><msup><mi>f</mi><mi>&#39;</mi></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>)</mo></mrow></math>
<math><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mi>f</mi><mo>(</mo><mi>z</mi><mo>)</mo><msubsup><mrow><mo>|</mo></mrow><mrow><mo>-</mo><mn>5</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></msubsup><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>5</mn><mo>)</mo><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>5</mn></mrow></mfenced></math>
<math><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mi>f</mi><mo>(</mo><mn>5</mn><mo>)</mo><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>5</mn><mo>+</mo><mi>x</mi></mrow></mfenced></math> ( <math><mi>f</mi></math> is an odd function and <math><mi>g</mi></math> is given as an even function)
<math><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>5</mn><mo>+</mo><mi>x</mi></mrow><mrow><mn>5</mn></mrow></munderover><mrow><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mo>(</mo><mi>t</mi><mo>)</mo><mi>d</mi><mi>t</mi><mo>=</mo></mrow></mrow><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>5</mn><mo>+</mo><mi>x</mi></mrow><mrow><mn>5</mn></mrow></munderover><mrow><mi>g</mi><mo>(</mo><mi>t</mi><mo>)</mo><mi>d</mi><mi>t</mi></mrow></mrow></math>

</details>

---

### Q106. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mo>-</mo><mi>x</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow><mrow><mn>2</mn><mo>+</mo><mi>x</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><mi>x</mi><mo>,</mo></math> then the value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><mi>e</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mo>-</mo><mi>x</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow><mrow><mn>2</mn><mo>+</mo><mi>x</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mi mathvariant="normal">g</mi><mi mathvariant="normal">e</mi></msub><mfenced separators="|"><mfrac><mrow><mn>2</mn><mo>-</mo><mi>x</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow><mrow><mn>2</mn><mo>+</mo><mi>x</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mo>&#8289;</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mi mathvariant="normal">g</mi><mi>e</mi></msub><mfenced separators="|"><mfrac><mrow><mn>2</mn><mo>-</mo><mo>(</mo><mo>-</mo><mi>x</mi><mo>)</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mo>&#8289;</mo><mo>(</mo><mo>-</mo><mi>x</mi><mo>)</mo></mrow><mrow><mn>2</mn><mo>+</mo><mo>(</mo><mo>-</mo><mi>x</mi><mo>)</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mo>&#8289;</mo><mo>(</mo><mo>-</mo><mi>x</mi><mo>)</mo></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced separators="|"><mfrac><mrow><mn>2</mn><mo>+</mo><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><mn>2</mn><mo>-</mo><mi>x</mi><mi>cos</mi><mi>x</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mo>-</mo><mi>log</mi><mfenced separators="|"><mfrac><mrow><mn>2</mn><mo>-</mo><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><mn>2</mn><mo>+</mo><mi>x</mi><mi>cos</mi><mi>x</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mo>&#8211;</mo><mi>g</mi><mo>(</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>)</mo></math></p><p>Hence, <math><mi>g</mi><mo>(</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>)</mo></math> is an odd function.</p><p>By using the property of definite integration, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>a</mi></mrow><mi>a</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left left" columnspacing="1.4ex 1.4ex"><mtr><mtd><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup></mtd><mtd><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mtd></mtr></mtable></mfenced></math>, we can write
<math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mrow><mi>g</mi><mo>(</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>)</mo><mi>d</mi><mi>x</mi><mo>=</mo></mrow><mn>0</mn><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><mn>1</mn></math></p>

</details>

---

### Q107. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>f</mi></math> and <math><mi>g</mi></math> be continuous functions on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>a</mi></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mi>x</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><mi>g</mi><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>4</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>g</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></mrow></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></mrow></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>g</mi><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math>    (Using properties of definite integration)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mfenced separators="|"><mrow><mn>4</mn><mo>-</mo><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>a</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>g</mi><mfenced><mrow><mi>a</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>4</mn><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>-</mo><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>4</mn><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>-</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mn>4</mn><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p>

</details>

---

### Q108. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int_{-2}^{2} \frac{\sin ^{2} x}{\left[\frac{x}{\pi}\right]+\frac{1}{2}} d x$

(where $[x]$ denotes the greatest integer less than or equal to x) is

**Options:**

- **(A)** 0
- **(B)** $\sin 4$
- **(C)** 4
- **(D)** $4-\sin 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Let $f(x)=\frac{\sin ^{2} x}{\left[\frac{x}{\pi}\right]+\frac{1}{2}}$.

$\begin{array}{l}

\text { So, } f(-x)=\frac{\sin ^{2}(-x)}{\left[\frac{-x}{\pi}\right]+\frac{1}{2}} \quad \because[-x]=-1-[x] \\

\Rightarrow f(-x)=\frac{\sin ^{2} x}{-1-\left[\frac{x}{\pi}\right]+\frac{1}{2}}=\frac{\sin ^{2} x}{-\frac{1}{2}-\left[\frac{x}{\pi}\right]}=-f(x)

\end{array}$

$\Rightarrow f(x)$ is odd function

Hence, $\int_{-2}^{2} f(x) d x=0$

</details>

---

### Q109. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of <math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mrow><mrow><mo>-</mo><mi>&#960;</mi></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow><mrow><mrow><mrow><mi>&#960;</mi></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></munderover><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced><mi>&#160;</mi><mo>+</mo><mi>&#160;</mi><mn>4</mn></mrow></mfrac></mrow></mrow><mo>,</mo></math> where <math><mfenced close="]" open="[" separators="|"><mrow><mi>t</mi></mrow></mfenced></math> denotes the greatest integer less than or equal to <math><mi>t</mi><mo>,</mo></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>20</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>4</mn><mi>π</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math>
- **(B)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>4</mn><mi>π</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>7</mn><mi>π</mi><mo>-</mo><mn>5</mn></mrow></mfenced></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>7</mn><mi>π</mi><mo>+</mo><mn>5</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>20</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>4</mn><mi>π</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>We have<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo stretchy="true">&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mo>[</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>]</mo><mo>+</mo><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo stretchy="true">&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mn>0</mn></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>3</mn></mrow></mfrac><mo>+</mo><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo stretchy="true">&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mn>1</mn></mfrac><mo>+</mo><msubsup><mo stretchy="true">&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mn>2</mn></mfrac><mo>+</mo><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mn>4</mn></mfrac><mo>+</mo><msubsup><mo stretchy="true">&#8747;</mo><mn>1</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mn>5</mn></mfrac></math>

<math><mo>=</mo><msubsup><mrow><mo>[</mo><mi>x</mi><mo>]</mo></mrow><mrow><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>0</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>1</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msubsup><mo>=</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mn>0</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>10</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

<math><mo>=</mo><mfrac><mrow><mo>-</mo><mn>20</mn><mo>+</mo><mn>10</mn><mi>&#960;</mi><mo>+</mo><mn>10</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>2</mn><mi>&#960;</mi><mo>-</mo><mn>4</mn></mrow><mrow><mn>20</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>12</mn><mi>&#960;</mi><mo>-</mo><mn>9</mn></mrow><mrow><mn>20</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>20</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>4</mn><mi>&#960;</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math></p>

</details>

---

### Q110. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><msup><mfenced open="|" close="|" separators="|"><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mi>d</mi><mi>x</mi></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mn>0</mn></math>
- **(C)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><msup><mfenced open="|" close="|"><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><msup><mi mathvariant="normal">s</mi><mn>3</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><msup><mi mathvariant="normal">n</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced open="[" close="]" separators="|"><mrow><munderover><mo stretchy="true">&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>-</mo><munderover><mo stretchy="true">&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><msup><mi mathvariant="normal">n</mi><mn>2</mn></msup><mi>x</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><msup><mi mathvariant="normal">n</mi><mn>3</mn></msup><mi>x</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced open="[" close="]" separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mn>0</mn><mo>+</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q111. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><msup><mi>sin</mi><mn>4</mn></msup><mo>&#8289;</mo><mi>x</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>ln</mi><mo>&#8289;</mo><mfenced separators="|"><mfrac><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mo>&#8289;</mo><mi>x</mi></mrow><mrow><mn>2</mn><mo>-</mo><mi>sin</mi><mo>&#8289;</mo><mi>x</mi></mrow></mfrac></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac><mi>&#960;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>16</mn></mrow></mfrac><mi>π</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac><mi>&#960;</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><msup><mi>sin</mi><mn>4</mn></msup><mo>&#8289;</mo><mi>x</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>ln</mi><mo>&#8289;</mo><mfenced separators="|"><mfrac><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mo>&#8289;</mo><mi>x</mi></mrow><mrow><mn>2</mn><mo>-</mo><mi>sin</mi><mo>&#8289;</mo><mi>x</mi></mrow></mfrac></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>2</mn><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></munderover><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced><mo>,</mo><mfenced><mrow><mo>&#8757;</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>&#160;</mo><mtext>is&#160;an&#160;even&#160;function</mtext></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><munderover><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced><mi>ln</mi><mo>&#8289;</mo><mfenced separators="|"><mfrac><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mn>2</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#8757;</mo><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced><mi>ln</mi><mo>&#8289;</mo><mfenced separators="|"><mfrac><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mn>2</mn><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfrac></mfenced><mo>&#160;</mo><mtext>is&#160;odd&#160;function</mtext></mrow></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></munderover><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mi>&#160;</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>m</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></munderover><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></munderover><msup><mi>cos</mi><mn>4</mn></msup><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p>Adding both, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>m</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></munderover><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></munderover><msup><mi>cos</mi><mn>4</mn></msup><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>m</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></munderover><mfenced close="}" open="{"><mrow><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>m</mi><mo>=</mo><msup><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mi>x</mi></mfenced><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>m</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>m</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></munderover><mfenced close="}" open="{"><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>4</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></munderover><mfenced close="}" open="{"><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mrow><mi>cos</mi><mn>4</mn><mi>x</mi></mrow><mn>4</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>m</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>4</mn></mfrac><mo>+</mo><mfrac><mrow><mi>sin</mi><mn>4</mn><mi>x</mi></mrow><mn>16</mn></mfrac></mrow></mfenced><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mo>=</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>16</mn></mfrac></math></p><p>Substituting in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>2</mn><mi>m</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac></math></p>

</details>

---

### Q112. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The values of <math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mi>x</mi></mrow></msup></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>8</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mn>4</mn><mi>π</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mi>&#160;</mi><munderover><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfrac><mi>&#160;</mi><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math>

As <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi></mrow><mo>=</mo><munderover><mo>&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mrow><mi>f</mi><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>&#8722;</mo><mi>x</mi><mo>)</mo></mrow><mi>d</mi><mi>x</mi></math>

<math><mi>I</mi><mo>=</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mrow></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mi>&#160;</mi><munderover><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><mfrac><mrow><msup><mn>2</mn><mi>x</mi></msup><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>ii</mi><mo>)</mo></math> 

By adding Equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>ii</mi><mo>)</mo></math>,

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mi>&#160;</mi><munderover><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><mfrac><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfenced><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mn>2</mn><mi>x</mi></msup></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mn>2</mn><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>x</mi><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>x</mi><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced></math></p><p>On adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced></math>, we get

<math><mn>2</mn><mi>I</mi><mo>=</mo><mi>&#160;</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mi>&#160;</mi><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><mn>1</mn><mi>&#160;</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mi>&#160;</mi><msubsup><mfenced open="[" close="]"><mi>x</mi></mfenced><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mn>0</mn></math>
<math><mi>I</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math></p>

</details>

---

### Q113. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mn>1</mn><mn>2</mn></munderover><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mfrac><mo>=</mo><mfrac><mi>k</mi><mrow><mi>k</mi><mo>+</mo><mn>5</mn></mrow></mfrac></math>, then <math><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<math> <mrow> <mstyle displaystyle="true"> <mrow><munderover> <mo>&#8747;</mo> <mn>1</mn> <mn>2</mn> </munderover> <mrow> <mfrac> <mrow> <mi>d</mi><mi>x</mi></mrow> <mrow> <msup> <mrow> <mrow><mo>(</mo> <mrow> <msup> <mrow> <mrow><mo>(</mo> <mrow> <mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow> <mo>)</mo></mrow></mrow> <mn>2</mn> </msup> <mo>+</mo><mn>3</mn></mrow> <mo>)</mo></mrow></mrow> <mrow> <mfrac> <mn>3</mn> <mn>2</mn> </mfrac> </mrow> </msup> </mrow> </mfrac> </mrow> </mrow> </mstyle></mrow> </math>

Substituting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><msqrt><mn>3</mn></msqrt><mi>tan</mi><mo>&#8289;</mo><mi>&#952;</mi><mo>&#8203;</mo></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><msqrt><mn>3</mn></msqrt><msup><mi>sec</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#183;</mo><mi>d</mi><mi>&#952;</mi><mo>&#8203;</mo></math>

Now <math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><msqrt><mn>3</mn></msqrt><mrow><mrow> <msup> <mrow> <mi>sec</mi> </mrow> <mn>2</mn> </msup> <mi>&#952;&#8203;</mi> </mrow><mo>&#8289;</mo><mrow><mi>d</mi><mi>&#952;&#8203;</mi></mrow></mrow></mrow><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mrow><mrow> <msup> <mrow> <mi>sec</mi> </mrow> <mn>3</mn> </msup> <mi>&#952;&#8203;</mi> </mrow></mrow></mrow></mfrac></mrow></mrow></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></munderover><mi>cos</mi><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi><mo>&#8203;</mo><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><msubsup><mfenced open="[" close="]"><mrow><mi>sin</mi><mo>&#8289;</mo><mi>&#952;</mi></mrow></mfenced><mn>0</mn><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></msubsup><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mi>k</mi><mrow><mi>k</mi><mo>+</mo><mn>5</mn></mrow></mfrac><mo>=</mo><mi>k</mi><mo>+</mo><mn>5</mn><mo>=</mo><mn>6</mn><mi>k</mi></math>

<math><mo>=</mo><mi>k</mi><mo>=</mo><mn>1</mn></math>.

</details>

---

### Q114. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mfrac><mrow><mn>8</mn><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><msup><mfenced separators="|"><mrow><mi>tan</mi><mi>x</mi><mo>+</mo><mi>cot</mi><mi>x</mi></mrow></mfenced><mn>3</mn></msup></mfrac><mi>d</mi><mi>x</mi></math> equals

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>13</mn><mn>256</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><mn>64</mn></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>32</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>15</mn></mrow><mrow><mn>128</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>15</mn></mrow><mrow><mn>128</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mfrac><mrow><mn>8</mn><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><msup><mfenced separators="|"><mrow><mi>tan</mi><mi>x</mi><mo>+</mo><mi>cot</mi><mi>x</mi></mrow></mfenced><mn>3</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><munderover><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mfrac><mrow><mn>8</mn><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><msup><mfenced separators="|"><mrow><mstyle displaystyle="true"><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mi>cos</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac></mstyle></mrow></mfenced><mn>3</mn></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mfrac><mrow><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><msup><mfenced separators="|"><mfrac><mn>1</mn><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfrac></mfenced><mn>3</mn></msup></mfrac><mo>=</mo><munderover><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mi>cos</mi><mn>2</mn><mi>x</mi><mo>&#183;</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>&#183;</mo><msup><mi>sin</mi><mn>2</mn></msup><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><munderover><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mi>sin</mi><mn>4</mn><mi>x</mi><mo>&#183;</mo><mrow><mo>(</mo><mn>1</mn><mo>&#8722;</mo><mi>cos</mi><mn>4</mn><mi>x</mi><mo>)</mo></mrow><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><munderover><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mi>sin</mi><mn>4</mn><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><munderover><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mi>sin</mi><mn>8</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8722;</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><msubsup><mfenced open="[" close="]"><mrow><mi>cos</mi><mn>4</mn><mi>x</mi></mrow></mfenced><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mo>+</mo><mfrac><mn>1</mn><mrow><mn>8</mn><mo>&#215;</mo><mn>8</mn></mrow></mfrac><msubsup><mfenced open="[" close="]"><mrow><mi>cos</mi><mn>8</mn><mi>x</mi></mrow></mfenced><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8722;</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mfenced open="[" close="]"><mrow><mo>&#8722;</mo><mn>1</mn><mo>&#8722;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>64</mn></mfrac><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>15</mn><mn>128</mn></mfrac></math>.</p>

</details>

---

### Q115. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></munderover><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math><mo>-</mo><mn>2</mn></math>
- **(B)** <math><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>2</mn></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></munderover><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></munderover><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></munderover><msup><mi>sec</mi><mn>2</mn></msup><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>&#160;</mo><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mfenced open="[" close="]" separators="|"><mrow><mi>tan</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></msubsup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mi>tan</mi><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac><mo>-</mo><mi>tan</mi><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn></math>.</p>

</details>

---

### Q116. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mn>4</mn><mn>10</mn></munderover><mfrac><mfenced open="[" close="]"><msup><mi>x</mi><mn>2</mn></msup></mfenced><mrow><mfenced open="[" close="]"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>28</mn><mi>x</mi><mo>+</mo><mn>196</mn></mrow></mfenced><mo>+</mo><mfenced open="[" close="]"><msup><mi>x</mi><mn>2</mn></msup></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mi>x</mi></mfenced></math> denotes the greatest integer less than or equal to <math><mi>x</mi></math>, is

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mn>6</mn></math>
- **(C)** <math><mn>7</mn></math>
- **(D)** <math><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>3</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mi>&#160;</mi><munderover><mo>&#8747;</mo><mn>4</mn><mn>10</mn></munderover><mfrac><mfenced open="[" close="]" separators="|"><msup><mi>x</mi><mn>2</mn></msup></mfenced><mrow><mfenced open="[" close="]" separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>28</mn><mi>x</mi><mo>+</mo><mn>196</mn></mrow></mfenced><mo>+</mo><mfenced open="[" close="]" separators="|"><msup><mi>x</mi><mn>2</mn></msup></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mi>&#160;</mi><munderover><mo>&#8747;</mo><mn>4</mn><mn>10</mn></munderover><mfrac><mfenced close="]" open="[" separators="|"><msup><mi>x</mi><mn>2</mn></msup></mfenced><mrow><mfenced close="]" open="[" separators="|"><msup><mfenced separators="|"><mrow><mn>14</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfenced><mo>+</mo><mfenced close="]" open="[" separators="|"><msup><mi>x</mi><mn>2</mn></msup></mfenced></mrow></mfrac><mi>&#160;</mi><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Use <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><munderover><mo>&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mi>&#160;</mi><munderover><mo>&#8747;</mo><mn>4</mn><mn>10</mn></munderover><mfrac><mfenced close="]" open="[" separators="|"><msup><mfenced separators="|"><mrow><mn>14</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfenced><mrow><mfenced close="]" open="[" separators="|"><msup><mi>x</mi><mn>2</mn></msup></mfenced><mo>+</mo><mfenced close="]" open="[" separators="|"><msup><mfenced separators="|"><mrow><mn>14</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfenced></mrow></mfrac><mi>&#160;</mi><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math> </p><p>By adding equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mi>ii</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mi>&#160;</mi><munderover><mo>&#8747;</mo><mn>4</mn><mn>10</mn></munderover><mfrac><mrow><mfenced close="]" open="[" separators="|"><msup><mfenced separators="|"><mrow><mn>14</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfenced><mo>+</mo><mfenced close="]" open="[" separators="|"><msup><mi>x</mi><mn>2</mn></msup></mfenced></mrow><mrow><mfenced close="]" open="[" separators="|"><msup><mi>x</mi><mn>2</mn></msup></mfenced><mo>+</mo><mfenced close="]" open="[" separators="|"><msup><mfenced separators="|"><mrow><mn>14</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfenced></mrow></mfrac><mi>&#160;</mi><mi>d</mi><mi>x</mi></math></p><p><math><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mi>&#160;</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>4</mn></mrow><mrow><mn>10</mn></mrow></munderover><mrow><mi>d</mi><mi>x</mi></mrow></mrow></math></p><p><math><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mn>6</mn><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q117. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mi>ln</mi><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>ln</mi><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mn>2</mn></math>**

**Detailed Solution:**

<p>From the given equation

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#160;</mi><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#160;</mi><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mi>&#160;</mi><mi>d</mi><mi>x</mi><mo>-</mo><mi>&#160;</mi><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math>
 <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mi>&#160;</mi><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mi>x</mi><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math>         
Let <math><msub><mrow><mi>I</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mi>&#160;</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi><mi>d</mi><mi>x</mi></mrow></mrow></mrow></mrow></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mi>x</mi></mrow></mfenced><mi>x</mi></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>-</mo><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>x</mi><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mi>&#160;</mi><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><mfrac><mi>x</mi><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>&#160;</mi><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>&#160;</mi><msubsup><mfenced open="[" close="]"><mrow><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math>

<math><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn></mrow></mrow></math>

By equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math>,

<math><mrow><msubsup><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></mrow></mrow><mo>=</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mfenced close="]" open="[" separators="|"><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mn>2</mn></mrow></mfenced><mo>=</mo><mi>ln</mi><mo>&#8289;</mo><mn>2</mn><mi>&#160;</mi></math></p>

</details>

---

### Q118. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

For <math><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><mfrac><mrow><mi>log</mi><mo>&#8289;</mo><mi>t</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfrac><mi>&#160;</mi><mi>d</mi><mi>t</mi><mo>.</mo><mi>&#160;</mi></math> Then <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi> </mi><msup><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(B)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mi> </mi><msup><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi> </mi><msup><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mfrac><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi></mrow></mrow></mrow><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfrac></mrow></mrow><mi>&#160;</mi><mi>d</mi><mi>t</mi></math> <math><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mfrac><mrow><mrow><mrow><mi mathvariant="italic">log</mi></mrow><mo>&#8289;</mo><mrow><mi>z</mi></mrow></mrow></mrow><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>z</mi><mo>)</mo></mrow></mfrac><mi>d</mi><mi>z</mi></mrow></mrow></math>
And <math><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi></mrow></mrow></mrow><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfrac><mi>&#160;</mi><mi>d</mi><mi>t</mi></mrow></mrow></math>
Put <math><mi>t</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>z</mi></mrow></mfrac></math>
<math><mi>d</mi><mi>t</mi><mo>=</mo><mi>&#160;</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>z</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mi>&#160;</mi><mi>d</mi><mi>z</mi></math>
<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mfrac><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>&#8289;</mo><mrow><mi>z</mi></mrow></mrow></mrow><mrow><msup><mrow><mi>z</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>&#160;</mi><mfrac><mrow><mn>1</mn></mrow><mrow><mi>z</mi></mrow></mfrac></mrow></mfenced></mrow></mfrac></mrow></mrow><mi>&#160;</mi><mo>&#8901;</mo><mi>d</mi><mi>z</mi></math>
<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mfrac><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>&#8289;</mo><mrow><mi>z</mi></mrow></mrow></mrow><mrow><mi>z</mi><mo>(</mo><mn>1</mn><mo>+</mo><mi>z</mi><mo>)</mo></mrow></mfrac><mi>&#160;</mi><mi>&#160;</mi><mi>d</mi><mi>z</mi></mrow></mrow></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><mi>&#160;</mi><munderover><mo>&#8747;</mo><mn>1</mn><mi>x</mi></munderover><mi>log</mi><mo>&#8289;</mo><mi>z</mi><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>z</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>z</mi><mo>(</mo><mn>1</mn><mo>+</mo><mi>z</mi><mo>)</mo></mrow></mfrac></mrow></mfenced><mi>&#160;</mi><mi>d</mi><mi>z</mi></math>
<math><mo>=</mo><mi>&#160;</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>z</mi></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>&#8289;</mo><mrow><mi>z</mi><mi>&#160;</mi><mi>d</mi><mi>z</mi></mrow></mrow></mrow></mrow></math>
Put <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>&#8289;</mo><mrow><mi>z</mi><mo>=</mo><mi>P</mi></mrow></mrow></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mi>z</mi></mfrac><mi>&#160;</mi><mi>d</mi><mi>z</mi><mo>=</mo><mi>d</mi><mi>P</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mn>1</mn><mi>x</mi></munderover><mi>P</mi><mo>&#8901;</mo><mi>d</mi><mi>P</mi><mo>=</mo><msubsup><mfenced separators="|"><mfrac><msup><mi>P</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mn>1</mn><mi>x</mi></msubsup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>&#160;</mi><msubsup><mfenced separators="|"><mrow><msup><mi>log</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>z</mi></mrow></mfenced><mn>1</mn><mi>x</mi></msubsup><mo>=</mo><mi>&#160;</mi><mfrac><msup><mfenced separators="|"><mrow><mi>log</mi><mo>&#8289;</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mn>2</mn></mfrac></math>

</details>

---

### Q119. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mn>2</mn><mn>4</mn></munderover><mfrac><mrow><mo>log</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mo>log</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>log</mo><msup><mfenced><mrow><mn>6</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">I</mo><mo>=</mo><munderover><mo>&#8747;</mo><mn>2</mn><mn>4</mn></munderover><mfrac><mrow><mo>log</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mo>log</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>log</mo><msup><mfenced><mrow><mn>6</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">I</mo><mo>=</mo><munderover><mo>&#8747;</mo><mn>2</mn><mn>4</mn></munderover><mfrac><mrow><mo>log</mo><msup><mfenced><mrow><mn>6</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mo>log</mo><msup><mfenced><mrow><mn>6</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>log</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><munderover><mo>&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><munderover><mo>&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo mathvariant="italic">I</mo><mo>=</mo><munderover><mo>&#8747;</mo><mn>2</mn><mn>4</mn></munderover><mfrac><mrow><mo>log</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>log</mo><msup><mfenced><mrow><mn>6</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mo>log</mo><msup><mfenced><mrow><mn>6</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>log</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>2</mn><mn>4</mn></munderover><mn>1</mn><mo mathvariant="italic">dx</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mfenced open="[" close="]"><mi>x</mi></mfenced><mn>2</mn><mn>4</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>I</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q120. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If [ ] denotes the greatest integer function, then the integral $\int_0^\pi[\cos x d x$ is equal to:

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** 0
- **(C)** $-1$
- **(D)** $-\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\frac{\pi}{2}$**

**Detailed Solution:**

Let $\mathrm{I}=\int_0^\pi[\cos x] d x$
$$
\mathrm{I}=\int_0^\pi[\cos (\pi-x)] d x=\int_0^\pi[-\cos x] d x
$$
On adding (1) and (2), we get
$$
\begin{aligned}
&2 \mathrm{I}=\int_0^\pi[\cos x] d x+\int_0^\pi[-\cos x] d x \\
&2 \mathrm{I}=\int_0^\pi[\cos x]+[-\cos x] d x \\
&2 \mathrm{I} \\
&=\int_0^\pi-1 d x \quad(\because[x]+[-x]=-1 \text { if } x \notin Z) \\
&2 \mathrm{I}=-\left.x\right|_0 ^\pi=-\pi \\
&\Rightarrow \mathrm{I}=\frac{-\pi}{2}
\end{aligned}
$$

</details>

---

### Q121. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></munderover><mfrac><mrow><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math> equals

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mi>ln</mi><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mrow><mn>1</mn><mn>6</mn></mrow></mfrac><mi>ln</mi><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mi>ln</mi><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mrow><mn>3</mn><mn>2</mn></mrow></mfrac><mi>ln</mi><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mrow><mn>1</mn><mn>6</mn></mrow></mfrac><mi>ln</mi><mn>2</mn></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></munderover><mfrac><mrow><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>=</mo><mi>tan</mi><mi>&#952;</mi><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>s</mi><mi>e</mi><msup><mi>c</mi><mn>2</mn></msup><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mfrac><mrow><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfenced></mrow><mrow><mi>s</mi><mi>e</mi><msup><mi>c</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac><mo>&#183;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><mi>s</mi><mi>e</mi><msup><mi>c</mi><mn>2</mn></msup><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8757;</mo><mo>&#160;</mo><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></math>
 <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mo>ln</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfenced><mi>d</mi><mi>&#952;</mi></math>
  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mo>ln</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mi>&#952;</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>&#952;</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8757;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mo>ln</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>&#952;</mi></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mo>ln</mo><mfenced><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfrac></mfenced><mi>d</mi><mi>&#952;</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mfenced><mrow><mi>ln</mi><mn>2</mn></mrow></mfenced><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mi>d</mi><mi>&#952;</mi><mo>-</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfenced><mi>d</mi><mi>&#952;</mi></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mfenced><mrow><mi>ln</mi><mn>2</mn></mrow></mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mn>2</mn><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>16</mn></mfrac><mfenced><mrow><mi>ln</mi><mn>2</mn></mrow></mfenced></math></p>

</details>

---

### Q122. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></munderover><msqrt><mn>1</mn><mo>+</mo><mn>4&#160;</mn><msup><mtext>sin</mtext><mn>2</mn></msup><mfrac><mo mathvariant="italic">x</mo><mn>2</mn></mfrac><mo>-</mo><mn>4&#160;</mn><mtext>sin</mtext><mfrac><mi>x</mi><mn>2</mn></mfrac></msqrt><mi>d</mi><mi>x</mi></math> equals

**Options:**

- **(A)** <math> <mrow> <mn>4</mn> <msqrt> <mn>3</mn> </msqrt> <mo>-</mo> <mn>4</mn> </mrow> </math>
- **(B)** <math> <mrow> <mn>4</mn> <msqrt> <mn>3</mn> </msqrt> <mo>-</mo> <mn>4</mn> <mo>-</mo> <mfrac> <mrow> <mi>&pi;</mi> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </math>
- **(C)** <math> <mrow> <mi>&pi;</mi> <mo>-</mo> <mn>4</mn> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>2</mn> <mi>&pi;</mi> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> <mo>-</mo> <mn>4</mn> <mo>-</mo> <mn>4</mn> <msqrt> <mn>3</mn> </msqrt> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math> <mrow> <mn>4</mn> <msqrt> <mn>3</mn> </msqrt> <mo>-</mo> <mn>4</mn> <mo>-</mo> <mfrac> <mrow> <mi>&pi;</mi> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></munderover><msqrt><mn>1</mn><mo>+</mo><mn>4&#160;</mn><msup><mtext>sin</mtext><mn>2</mn></msup><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>-</mo><mn>4&#160;</mn><mtext>sin</mtext><mfrac><mi>x</mi><mn>2</mn></mfrac></msqrt><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></munderover><msqrt><msup><mfenced><mrow><mn>2&#160;</mn><mtext>sin</mtext><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></msqrt><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></munderover><mfenced close="|" open="|"><mrow><mn>2&#160;</mn><mtext>sin</mtext><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><munderover><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></munderover><mfenced close="|" open="|"><mrow><mtext>sin</mtext><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2&#160;</mn><mfenced close="]" open="["><mrow><munderover><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>3</mn></mrow></munderover><mfenced close="|" open="|"><mrow><mtext>sin</mtext><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><munderover><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>3</mn></mrow><mi>&#960;</mi></munderover><mfenced close="|" open="|"><mrow><mtext>sin</mtext><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2&#160;</mn><mfenced close="]" open="["><mrow><munderover><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>3</mn></mrow></munderover><mo>-</mo><mfenced><mrow><mtext>sin</mtext><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><munderover><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>3</mn></mrow><mi>&#960;</mi></munderover><mfenced><mrow><mtext>sin</mtext><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2&#160;</mn><mfenced close="]" open="["><mrow><msubsup><mfenced close="]" open="["><mrow><mn>2</mn><mtext>cos</mtext><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>3</mn></mrow></msubsup><mo>+</mo><msubsup><mfenced close="]" open="["><mrow><mo>-</mo><mn>2</mn><mtext>cos</mtext><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mrow><mi>&#960;</mi><mo>/</mo><mn>3</mn></mrow><mi>&#960;</mi></msubsup></mrow></mfenced></math>

<math> <mrow> <mo>=</mo> <mn>2&#160;</mn> <mfenced close="]" open="[" separators=","> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <mn>2</mn> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <msqrt> <mn>3</mn> </msqrt> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </mfenced> <mo>+</mo> <mfrac> <mrow> <mi>&#960;</mi> </mrow> <mrow> <mn>6</mn> </mrow> </mfrac> <mo>-</mo> <mn>2</mn> </mrow> </mfenced> <mo>+</mo> <mfenced close="]" open="[" separators=","> <mrow> <mo>-</mo> <mfrac> <mrow> <mi>&#960;</mi> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>+</mo> <mn>2</mn> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <msqrt> <mn>3</mn> </msqrt> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </mfenced> <mo>+</mo> <mfrac> <mrow> <mi>&#960;</mi> </mrow> <mrow> <mn>6</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </mfenced> </mrow> </math>

<math> <mrow> <mo>=</mo> <mn>2&#160;</mn> <mfenced close="]" open="[" separators=","> <mrow> <msqrt> <mn>3</mn> </msqrt> <mo>+</mo> <mfrac> <mrow> <mi>&#960;</mi> </mrow> <mrow> <mn>6</mn> </mrow> </mfrac> <mo>-</mo> <mn>2</mn> <mo>-</mo> <mfrac> <mrow> <mi>&#960;</mi> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>+</mo> <msqrt> <mn>3</mn> </msqrt> <mo>+</mo> <mfrac> <mrow> <mi>&#960;</mi> </mrow> <mrow> <mn>6</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>

<math> <mrow> <mo>=</mo> <mn>2&#160;</mn> <mfenced close="]" open="[" separators=","> <mrow> <mn>2</mn> <msqrt> <mn>3</mn> </msqrt> <mo>-</mo> <mfrac> <mrow> <mi>&#960;</mi> </mrow> <mrow> <mn>6</mn> </mrow> </mfrac> <mo>-</mo> <mn>2</mn> </mrow> </mfenced> </mrow> </math>

<math> <mrow> <mo>=</mo> <mn>4</mn> <msqrt> <mn>3</mn> </msqrt> <mo>-</mo> <mfrac> <mrow> <mi>&#960;</mi> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> <mo>-</mo> <mn>4</mn> </mrow> </math>.

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6df23644-f09d-47cc-935c-1480dc68854d-image.png" style="width: 340px; height: 124px;" />

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d55dd24d-9dcc-4b8f-85d4-64854e3343fd-image.png" style="width: 340px; height: 127px;" /></p>

</details>

---

### Q123. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\int_{-\pi / 2}^{\pi / 2} \frac{\sin ^2 x}{1+2^x} d x$ is :

**Options:**

- **(A)** $\pi$
- **(B)** $\frac{\pi}{2}$
- **(C)** $4 \pi$
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{4}$**

**Detailed Solution:**

$\mathrm{I}=\int_{\pi / 2}^{\pi / 2} \frac{\sin ^2 x}{1+2^x} d x$
$$
\Rightarrow \mathrm{I}=\int_{-\pi / 2}^{\pi / 2} \frac{\sin ^2 x}{1+2^{-x}} d x \text {, by replacing } x \text { by }
$$

$$
\begin{aligned}
& \left(\frac{\pi}{2}-\frac{\pi}{2}-x\right) \\
\Rightarrow \quad \mathrm{I} & =\int_{-\pi / 2}^{\pi / 2} \frac{2^x \cdot \sin ^2 x}{1+2^x} d x
\end{aligned}
$$
Adding equations (i) and (ii), we get
$$
\begin{array}{rl}
2 & I=\int_{-\pi / 2}^{\pi / 2} \sin ^2 x d x=\frac{1}{2} \int_{-\pi / 2}^{\pi / 2}(1-\cos 2 x) d x \\
\Rightarrow \quad \mathrm{I} & =\frac{1}{4}\left[x+\frac{\sin 2 x}{2}\right]_{-\pi / 2}^{\pi / 2} \\
& =\frac{1}{4}\left[\left(\frac{\pi}{2}+\frac{\sin \pi}{2}\right)-\left(-\frac{\pi}{2}+\frac{\sin (-\pi)}{2}\right)\right] \\
\Rightarrow \quad \mathrm{I} & =\frac{1}{4}\left[\frac{\pi}{2}+\frac{\pi}{2}\right]=\frac{\pi}{4}
\end{array}
$$

</details>

---

### Q124. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `1`

<p><strong>Statement - I : </strong>The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>6</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>3</mn></mrow></munderover><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msqrt><mi>tan</mi><mo>&#160;</mo><mi>x</mi></msqrt></mrow></mfrac></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>.</mo></math></p><p><strong>Statement - II : </strong><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><munderover><mo>&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>.</mo></math></p>

**Options:**

- **(A)** Statement - <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> is true; Statement - <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> is false.
- **(B)** Statement - <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> is false; Statement - <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> is true.
- **(C)** Statement - <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> true; Statement - <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> is true; Statement - <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> is a correct explanation for Statement - <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math>.
- **(D)** Statement - <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> is true; Statement - <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> is true; Statement - <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> is not a correct explanation for Statement - <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement - <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> is false; Statement - <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> is true.**

**Detailed Solution:**

<p>Statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> is a standard property of definite integrals.</p><p>For statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> : <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>6</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>3</mn></mrow></munderover><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msqrt><mi>tan</mi><mo>&#160;</mo><mi>x</mi></msqrt></mrow></mfrac><mo>=</mo><munderover><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>6</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>3</mn></mrow></munderover><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msqrt><mi>cot</mi><mo>&#160;</mo><mi>x</mi></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>6</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>3</mn></mrow></munderover><mfrac><msqrt><mi>tan</mi><mo>&#160;</mo><mi>x</mi></msqrt><mrow><mn>1</mn><mo>+</mo><msqrt><mi>tan</mi><mo>&#160;</mo><mi>x</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><munderover><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>6</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>3</mn></mrow></munderover><mfrac><mrow><msqrt><mi>sin</mi></msqrt><mi>x</mi></mrow><mrow><msqrt><mi>cos</mi></msqrt><mi>x</mi><mo>+</mo><msqrt><mi>sin</mi><mi>x</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><munderover><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>6</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>3</mn></mrow></munderover><mfrac><mrow><msqrt><mi>cos</mi></msqrt><mi>x</mi></mrow><mrow><msqrt><mi>cos</mi></msqrt><mi>x</mi><mo>+</mo><msqrt><mi>sin</mi><mi>x</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>6</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>3</mn></mrow></munderover><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mrow><mn>1</mn><mn>2</mn></mrow></mfrac></math></p><p>Hence, statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> is false.</p>

</details>

---

### Q125. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `3`

If $[x]$ is the greatest integer $\leq x$, then the value of the integral $\int_{-0.9}^{0.9}\left(\left[x^2\right]+\log \left(\frac{2-x}{2+x}\right)\right) d x$ is

**Options:**

- **(A)** $0.486$
- **(B)** $0.243$
- **(C)** $1.8$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

$$
\text { } \begin{aligned}
& \int_{-0.9}^{0.9}\left\{\left[x^2\right]+\log \left(\frac{2-x}{2+x}\right)\right\} d x \\
= & \int_{-0.9}^{0.9}\left[x^2\right] d x+\int_{-0.9}^{0.9} \log \left(\frac{2-x}{2+x}\right) d x
\end{aligned}
$$

$$
\begin{aligned}
& =0+\int_{-0.9}^{0.9} \log \left(\frac{2-x}{2+x}\right) d x \\
& \text { Put } x=-x \Rightarrow f(x)=\log \frac{2-x}{2+x} \\
& \text { and } f(-x)=\log \frac{2+x}{2-x} \\
& =-\log \frac{(2-x)}{2+x}=-f(x)
\end{aligned}
$$
So, it is an odd function, hence Required integral $=0$.

</details>

---

### Q126. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `1`

The value of the integral $\int_0^{0.9}[x-2[x]] d x$, where [.] denotes the greatest integer function is

**Options:**

- **(A)** $0.9$
- **(B)** $1.8$
- **(C)** $-0.9$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

Since $\int_0^a[x]=0$ where $0 \leq a \leq 1$
$$
\therefore \int_0^{0.9}[x-2[x]] d x=0
$$

</details>

---

### Q127. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int_0^1 \frac{8 \log (1+x)}{1+x^2} d x$ is

**Options:**

- **(A)** $\frac{\pi}{8} \log 2$
- **(B)** $\frac{\pi}{2} \log 2$
- **(C)** $\log 2$
- **(D)** $\pi \log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\pi \log 2$**

**Detailed Solution:**

$\mathrm{I}=8 \int_0^1 \frac{\log (1+\mathrm{x})}{1+\mathrm{x}^2} \mathrm{dx}$
$=8 \int_0^{\frac{\pi}{4}} \frac{\log (1+\tan \theta)}{1+\tan ^2 \theta} \sec ^2 \theta d \theta(\operatorname{let} x=\tan \theta)$
$=8 \int_0^{\frac{\pi}{4}} \log \left(1+\tan \left(\frac{\pi}{4}-\theta\right)\right) d \theta=8 \int_0^{\frac{\pi}{4}} \log \left(1+\frac{1-\tan \theta}{1+\tan \theta}\right) d \theta=8 \int_0^{\frac{\pi}{4}} \log 2 d \theta-8 \int_0^{\frac{\pi}{4}} \log (1+\tan \theta) d \theta$
$=8 \log 2 \frac{\pi}{4}-I$
$2 \mathrm{I}=2 \pi \log 2$
$\mathrm{I}=\pi \log 2$

</details>

---

### Q128. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `3`

$\int_0^\pi[\cot x] d x,[\bullet]$ denotes the greatest integer function, is equal to

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** 1
- **(C)** $-1$
- **(D)** $-\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\frac{\pi}{2}$**

**Detailed Solution:**

$$
\begin{aligned}
& \text { Let } \mathrm{I}=\int_0^\pi[\cot x] d x \\
& =\int_0^\pi[\cot (\pi-x)] d x=\int_0^\pi[-\cot x] d x
\end{aligned}
$$
Adding (1) and (2)
$$
\begin{aligned}
& 2 I=\int_0^\pi[\cot x] d x+\int_0^\pi[-\cot x] d x==\int_0^\pi(-1) d x \quad[\because[x]+[-x]=-1 \text { if } x \notin Z \\
& =[-x]_0^\pi=-\pi \\
& \therefore I=-\frac{\pi}{2}
\end{aligned}
$$

</details>

---

### Q129. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `2`

The solution for $x$ of the equation 
$\int_{\sqrt{2}}^x \frac{d t}{t \sqrt{t^2-1}}=\frac{\pi}{2}$ is

**Options:**

- **(A)** $2$
- **(B)** $\pi$
- **(C)** $\frac{\sqrt{3}}{2}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) None of these**

**Detailed Solution:**

$\int_{\sqrt{2}}^x \frac{d t}{t \sqrt{t^2-1}}=\frac{\pi}{2}$
$\left[\sec ^{-1} t\right]_{\sqrt{2}}^x=\frac{\pi}{2}$
$\sec ^{-1} x-\frac{\pi}{4}=\frac{\pi}{2}$
$\sec ^{-1} x=\frac{3 \pi}{4}$
$x=-\sqrt{2}$.

</details>

---

### Q130. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `3`

Let $F(x)=f(x)+f\left(\frac{1}{x}\right)$, where $f(x)=\int_1^x \frac{\log t}{1+t} d t$. Then $F(e)$ equals

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $0$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

$f(x)=\int_1^x \frac{\log t}{1+t} d t$
$F(e)=f(e)+f\left(\frac{1}{e}\right)$
$F(e)=\int_1^e \frac{\log t}{1+t} d t+\int_1^{1 / e} \frac{\log t}{1+t} d t$
$=\int_1^e \frac{\log t}{1+t}+\int_1^e \frac{\log t}{t(1+t)} d t$
$=\int_1^e \frac{\log t}{t} d t=\frac{1}{2}$.

</details>

---

### Q131. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int_1^a[x] f^{\prime}(x) d x, a>1$, where $[x]$ denotes the greatest integer not exceeding $x$ is

**Options:**

- **(A)** $\operatorname{af}(a)-\{f(1)+f(2)+\ldots+f([a])\}$
- **(B)** $[a] f(a)-\{f(1)+f(2)+\ldots+f([a])\}$
- **(C)** $[a] f([a])-\{f(1)+f(2)+\ldots+f(a)\}$
- **(D)** $a f([a])-\{f(1)+f(2)+\ldots+f(a)\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $[a] f(a)-\{f(1)+f(2)+\ldots+f([a])\}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cQMUmJVcTP6NWGJ155iIIrrcxVn7sw4SZOJ4vAtECf4.original.fullsize.png">

</details>

---

### Q132. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `2`

$\int_{-3 \pi / 2}^{-\pi / 2}\left[(x+\pi)^3+\cos ^2(x+3 \pi)\right] d x$ is equal to

**Options:**

- **(A)** $\frac{\pi^4}{32}$
- **(B)** $\frac{\pi^4}{32}+\frac{\pi}{2}$
- **(C)** $\frac{\pi}{2}$
- **(D)** $\frac{\pi}{4}-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{2}$**

**Detailed Solution:**

$$
I=\int_{-3 \pi / 2}^{-\pi / 2}\left[(x+\pi)^3+\cos ^2(x+3 \pi)\right] d x
$$
Put $\mathrm{x}+\pi=\mathrm{t}$
$$
\begin{aligned}
& I=\int_{-\pi / 2}^{\pi / 2}\left[t^3+\cos ^2 t\right] d t=2 \int_0^{\pi / 2} \cos ^2 t d t \\
& =\int_0^{\pi / 2}(1+\cos 2 t) d t=\frac{\pi}{2}+0 .
\end{aligned}
$$

</details>

---

### Q133. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `3`

$\int_0^\pi x f(\sin x) d x$ is equal to

**Options:**

- **(A)** $\pi \int_0^\pi f(\cos x) d x$
- **(B)** $\pi \int_0^\pi f(\sin x) d x$
- **(C)** $\frac{\pi}{2} \int_0^{\pi / 2} f(\sin x) d x$
- **(D)** $\pi \int_0^{\pi / 2} f(\cos x) d x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\pi \int_0^{\pi / 2} f(\cos x) d x$**

**Detailed Solution:**

$I=\int_0^\pi x f(\sin x) d x=\int_0^\pi(\pi-x) f(\sin x) d x$
$=\pi \int_0^\pi f(\sin x) d x-1$
$2 I=\pi \int_0^\pi f(\sin x) d x$
$I=\frac{\pi}{2} \int_0^\pi f(\sin x) d x=\pi \int_0^{\pi / 2} f(\sin x) d x$
$=\pi \int_0^{\pi / 2} f(\cos x) d x$

</details>

---

### Q134. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

The value of the integral, $\int_3^6 \frac{\sqrt{x}}{\sqrt{9-x}+\sqrt{x}} d x$ is

**Options:**

- **(A)** 1/2
- **(B)** 3/2
- **(C)** 2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3/2**

**Detailed Solution:**

$I=\int_3^6 \frac{\sqrt{x}}{\sqrt{9-x}+\sqrt{x}} d x$
$I=\int_3^6 \frac{\sqrt{9-x}}{\sqrt{9-x}+\sqrt{x}} d x$
$2 I=\int_3^6 d x=3 \Rightarrow I=\frac{3}{2}$

</details>

---

### Q135. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_{-\pi}^\pi \frac{\cos ^2 x}{1+a^x} d x, a>0$, is

**Options:**

- **(A)** $a \pi$
- **(B)** $\frac{\pi}{2}$
- **(C)** $\frac{\pi}{a}$
- **(D)** $2 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{2}$**

**Detailed Solution:**

$$
\int_{-\pi}^\pi \frac{\cos ^2 x}{1+a^x} d x=\int_0^\pi \cos ^2 x d x=\frac{\pi}{2} .
$$

</details>

---

### Q136. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

The value of $I=\int_0^{\pi / 2} \frac{(\sin x+\cos x)^2}{\sqrt{1+\sin 2 x}} d x$ is

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

$\int_0^{\frac{\pi}{2}} \frac{(\sin x+\cos x)^2}{\sqrt{(\sin x+\cos x)^2}} d x=\int_0^{\frac{\pi}{2}}(\sin x+\cos x) d x=|-\cos x+\sin x|_0^{\frac{\pi}{2}}=2$

</details>

---

### Q137. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_{-2}^3\left|1-x^2\right| d x$ is

**Options:**

- **(A)** $\frac{28}{3}$
- **(B)** $\frac{14}{3}$
- **(C)** $\frac{7}{3}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{28}{3}$**

**Detailed Solution:**

$\int_{-2}^{-1}\left(x^2-1\right) d x+\int_{-1}^1\left(1-x^2\right) d x+\int_1^3\left(x^2-1\right) d x=\frac{x^3}{3}-\left.x\right|_{-2} ^{-1}+x-\left.\frac{x^3}{3}\right|_{-1} ^1+\frac{x^3}{3}-\left.x\right|_1 ^3=\frac{28}{3}$

</details>

---

### Q138. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $I=\int_0^1 x(1-x)^n d x$ is

**Options:**

- **(A)** $\frac{1}{n+1}+\frac{1}{n+2}$
- **(B)** $\frac{1}{n+1}$
- **(C)** $\frac{1}{n+2}$
- **(D)** $\frac{1}{n+1}-\frac{1}{n+2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{n+1}-\frac{1}{n+2}$**

**Detailed Solution:**

$I=\int_0^1 x(1-x)^n d x$
$-I=\int_0^1-x(1-x)^n d x=\int_0^1(1-x-1)(1-x)^n d x$
$=\int_0^1(1-x)^{n+1} d x-\int_0^1(1-x)^n d x$
$=\left[\frac{(1-x)^{n+2}}{-(n+2)}\right]_0^1-\left[\frac{(1-x)^{n+1}}{-(n+1)}\right]_0^1=\frac{1}{n+2}-\frac{1}{n+1}$
$I=\frac{1}{n+1}-\frac{1}{n+2}$

</details>

---

### Q139. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)$ be a function satisfying $f^{\prime}(x)=f(x)$ with $f(0)=1$ and $g(x)$ be a function that satisfies $f(x)+g(x)=x^2$. Then the value of the integral $\int_0^1 f(x) g(x) d x$, is

**Options:**

- **(A)** $\mathrm{e}+\frac{\mathrm{e}^2}{2}+\frac{5}{2}$
- **(B)** $\mathrm{e}-\frac{\mathrm{e}^2}{2}-\frac{5}{2}$
- **(C)** $\mathrm{e}+\frac{\mathrm{e}^2}{2}-\frac{3}{2}$
- **(D)** $\mathrm{e}-\frac{\mathrm{e}^2}{2}-\frac{3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{e}-\frac{\mathrm{e}^2}{2}-\frac{3}{2}$**

**Detailed Solution:**

Let $f(x)=e^x$
$\therefore \int_0^1 f(x) g(x) d x=\int_0^1 e^x\left(x^2-e^x\right) d x$
$=\int_0^1 x^2 e^x d x-\int_0^1 e^{2 x} d x$
$=\left[\mathrm{x}^2 \mathrm{e}^{\mathrm{x}}\right]_0^1-2\left[\mathrm{xe}^{\mathrm{x}}-\mathrm{e}^{\mathrm{x}}\right]_0^1-\frac{1}{2}\left[\mathrm{e}^{2 \mathrm{x}}\right]$
$=\mathrm{e}-\left[\frac{\mathrm{e}^2}{2}-\frac{1}{2}\right]-2[\mathrm{e}-\mathrm{e}+1]=\mathrm{e}-\frac{\mathrm{e}^2}{2}-\frac{3}{2}$

</details>

---

### Q140. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{f}(\mathrm{a}+\mathrm{b}-\mathrm{x})=\mathrm{f}(\mathrm{x})$ then $\int_a^b \mathrm{xf}(\mathrm{x}) \mathrm{dx}$ is equal to

**Options:**

- **(A)** $\frac{a+b}{2} \int_a^b f(a+b-x) d x$
- **(B)** $\frac{a+b}{2} \int_a^b f(b-x) d x$
- **(C)** $\frac{a+b}{2} \int_a^b f(x) d x$
- **(D)** $\frac{b-a}{2} \int_a^b f(x) d x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{a+b}{2} \int_a^b f(a+b-x) d x$**

**Detailed Solution:**

$I=\int_a^b x f(x) d x=\int_a^b(a+b-x) f(a+b-x) d x$
$=(a+b) \int_a^b f(a+b-x) d x-\int_a^b x f(a+b-x) d x$
$=(a+b) \int_a^b f(a+b-x) d x-\int_a^b x f(x) d x$
$2 I=(a+b) \int_a^b f(x) d x$
$I=\frac{(a+b)}{2} \int_a^b f(x) d x ; I=\frac{(a+b)}{2} \int_a^b f(a+b-x) d x$

</details>

---

### Q141. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

$\int_{-\pi}^\pi \frac{2 x(1+\sin x)}{1+\cos ^2 x} d x$ is

**Options:**

- **(A)** $\frac{\pi^2}{4}$
- **(B)** $\pi^2$
- **(C)** zero
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\pi^2$**

**Detailed Solution:**

$$
\begin{aligned}
& \int_{-\pi}^\pi \frac{2 x(1+\sin x)}{1+\cos ^2 x} d x=\int_{-\pi}^\pi \frac{2 x}{1+\cos ^2 x}+2 \int_{-\pi}^\pi \frac{x \sin x}{1+\cos ^2 x} \\
& =0+4 \int_0^\pi \frac{x \sin x d x}{1+\cos ^2 x} I=4 \int_0^\pi \frac{(\pi-x) \sin (\pi-x)}{1+\cos ^2(\pi-x)} \\
& I=4 \int_0^\pi \frac{(\pi-x) \sin x}{1+\cos ^2 x} \Rightarrow I=4 \pi \int_0^\pi \frac{\sin x}{1+\cos ^2 x}-4 \pi \int \frac{x \sin x}{1+\cos ^2 x} \Rightarrow 2 I=4 \pi \int_0^\pi \frac{\sin x}{1+\cos ^2 x} d x
\end{aligned}
$$
put $\cos x=t$ and solve it.

</details>

---

### Q142. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `3`

$\int_0^{\sqrt{2}}\left[x^2\right] d x$ is

**Options:**

- **(A)** $2-\sqrt{2}$
- **(B)** $2+\sqrt{2}$
- **(C)** $\sqrt{2}-1$
- **(D)** $\sqrt{2}-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{2}-1$**

**Detailed Solution:**

$\int_1^0\left[x^2\right] d x+\int_1^{\sqrt{2}}\left[x^2\right] d x=0+\int_1^{\sqrt{2}} d x=\sqrt{2}-1$

</details>

---

### Q143. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^{10 \pi}|\sin x| d x$ is

**Options:**

- **(A)** 20
- **(B)** 8
- **(C)** 10
- **(D)** 18

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 18**

**Detailed Solution:**

$\int_0^{10 \pi}|\sin x| d x=10\left[\int_0^{\pi / 2} \sin x d x+\int_{\pi / 2}^\pi \sin x d x\right]$
$=10 \times[\cos x]_0^{\pi / 2}+[\cos x]_{\pi / 2}^\pi ; \quad 10[1+1]=10 \times 2=20$

</details>

---

