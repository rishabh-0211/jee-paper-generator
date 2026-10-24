# JEE Main Mathematics - Definite Integration

## Topic 2: Definite Integration by Substitution

**Total Questions:** 42

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `numerical` | *Level:* `2`

If $\displaystyle\int_{\pi/6}^{\pi/4}\left(\cot\left(x-\dfrac{\pi}{3}\right)\cot\left(x+\dfrac{\pi}{3}\right)+1\right)dx = \alpha\log_e(\sqrt{3}-1)$, then $9\alpha^2$ is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

Given integral is $I = \displaystyle\int_{\pi/6}^{\pi/4}\left(\cot\left(x-\dfrac{\pi}{3}\right)\cot\left(x+\dfrac{\pi}{3}\right)+1\right)dx$

Using the identity $\cot A \cot B + 1 = \dfrac{\cos(A-B)}{\sin A \sin B}$, the integrand simplifies to:

$f(x) = \dfrac{\cos\left(\left(x-\dfrac{\pi}{3}\right) - \left(x+\dfrac{\pi}{3}\right)\right)}{\sin\left(x-\dfrac{\pi}{3}\right)\sin\left(x+\dfrac{\pi}{3}\right)}$

$f(x) = \dfrac{\cos\left(-\dfrac{2\pi}{3}\right)}{\sin^2 x - \sin^2\left(\dfrac{\pi}{3}\right)}$

$f(x) = \dfrac{-1/2}{\sin^2 x - 3/4} = \dfrac{2}{3 - 4\sin^2 x}$

Dividing the numerator and the denominator by $\cos^2 x$:

$f(x) = \dfrac{2\sec^2 x}{3\sec^2 x - 4\tan^2 x} = \dfrac{2\sec^2 x}{3(1+\tan^2 x) - 4\tan^2 x} = \dfrac{2\sec^2 x}{3 - \tan^2 x}$

The integral becomes:

$I = \displaystyle\int_{\pi/6}^{\pi/4} \dfrac{2\sec^2 x}{3 - \tan^2 x} dx$

Substituting $\tan x = t \Rightarrow \sec^2 x dx = dt$.

When $x = \dfrac{\pi}{6}$, $t = \dfrac{1}{\sqrt{3}}$. When $x = \dfrac{\pi}{4}$, $t = 1$.

$I = \displaystyle\int_{1/\sqrt{3}}^{1} \dfrac{2}{3 - t^2} dt$

Using the standard integral $\displaystyle\int \dfrac{1}{a^2 - x^2} dx = \dfrac{1}{2a}\ln\left|\dfrac{a+x}{a-x}\right|$:

$I = 2 \left[ \dfrac{1}{2\sqrt{3}} \ln\left|\dfrac{\sqrt{3}+t}{\sqrt{3}-t}\right| \right]_{1/\sqrt{3}}^{1}$

$I = \dfrac{1}{\sqrt{3}} \left( \ln\left(\dfrac{\sqrt{3}+1}{\sqrt{3}-1}\right) - \ln\left(\dfrac{\sqrt{3}+\dfrac{1}{\sqrt{3}}}{\sqrt{3}-\dfrac{1}{\sqrt{3}}}\right) \right)$

$I = \dfrac{1}{\sqrt{3}} \left( \ln\left(\dfrac{\sqrt{3}+1}{\sqrt{3}-1}\right) - \ln\left(\dfrac{3+1}{3-1}\right) \right)$

$I = \dfrac{1}{\sqrt{3}} \left( \ln\left(\dfrac{\sqrt{3}+1}{\sqrt{3}-1}\right) - \ln 2 \right) = \dfrac{1}{\sqrt{3}} \ln\left(\dfrac{\sqrt{3}+1}{2(\sqrt{3}-1)}\right)$

Rationalizing the term inside the logarithm by multiplying the numerator and the denominator by $(\sqrt{3}-1)$:

$\dfrac{\sqrt{3}+1}{2(\sqrt{3}-1)} = \dfrac{(\sqrt{3}+1)(\sqrt{3}-1)}{2(\sqrt{3}-1)^2} = \dfrac{3-1}{2(\sqrt{3}-1)^2} = \dfrac{1}{(\sqrt{3}-1)^2} = (\sqrt{3}-1)^{-2}$

Thus,

$I = \dfrac{1}{\sqrt{3}} \ln\left((\sqrt{3}-1)^{-2}\right) = -\dfrac{2}{\sqrt{3}} \ln(\sqrt{3}-1)$

Comparing this with $I = \alpha\log_e(\sqrt{3}-1)$, we get:

$\alpha = -\dfrac{2}{\sqrt{3}}$

Therefore, $9\alpha^2 = 9 \left(-\dfrac{2}{\sqrt{3}}\right)^2 = 9 \times \dfrac{4}{3} = 12$.

Answer: $12$

</details>

---

### Q2. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of the integral $\displaystyle\int_{0}^{2} \dfrac{\sqrt{x(x^2+x+1)}}{(\sqrt{x+1})(\sqrt{x^4+x^2+1})} \, dx$ is equal to:

**Options:**

- **(A)** $\dfrac{1}{3}\log_e(3-2\sqrt{2})$
- **(B)** $\dfrac{2}{3}\log_e(4+\sqrt{2})$
- **(C)** $\dfrac{2}{3}\log_e(3+2\sqrt{2})$
- **(D)** $\dfrac{1}{3}\log_e(1+6\sqrt{2})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{2}{3}\log_e(3+2\sqrt{2})$**

**Detailed Solution:**

Let $I = \displaystyle\int_{0}^{2} \dfrac{\sqrt{x(x^2 + x + 1)}}{\sqrt{x + 1}\,\sqrt{x^4 + x^2 + 1}}\, dx$.

Using the identity $x^4 + x^2 + 1 = (x^2 + x + 1)(x^2 - x + 1)$:
$I = \displaystyle\int_{0}^{2} \dfrac{\sqrt{x}\,\sqrt{x^2 + x + 1}}{\sqrt{x + 1}\,\sqrt{(x^2 + x + 1)(x^2 - x + 1)}}\, dx$

Cancelling $\sqrt{x^2 + x + 1}$:
$I = \displaystyle\int_{0}^{2} \dfrac{\sqrt{x}}{\sqrt{(x + 1)(x^2 - x + 1)}}\, dx$

Using $(x + 1)(x^2 - x + 1) = x^3 + 1$:
$I = \displaystyle\int_{0}^{2} \dfrac{\sqrt{x}}{\sqrt{x^3 + 1}}\, dx$

Substitution:
Let $t = x^{3/2}$, so $dt = \dfrac{3}{2}x^{1/2}\, dx \Rightarrow \sqrt{x}\, dx = \dfrac{2}{3}\, dt$.

Also, $t^2 = x^3$, so $x^3 + 1 = t^2 + 1$.

Changing limits:
$x = 0 \Rightarrow t = 0$
$x = 2 \Rightarrow t = 2^{3/2} = 2\sqrt{2}$

Therefore:
$I = \dfrac{2}{3}\displaystyle\int_{0}^{2\sqrt{2}} \dfrac{dt}{\sqrt{t^2 + 1}}$

Using $\displaystyle\int \dfrac{dt}{\sqrt{t^2 + a^2}} = \log_e\left|t + \sqrt{t^2 + a^2}\right| + C$:
$I = \dfrac{2}{3}\left[\log_e\left(t + \sqrt{t^2 + 1}\right)\right]_{0}^{2\sqrt{2}}$

$I = \dfrac{2}{3}\left[\log_e\left(2\sqrt{2} + \sqrt{8 + 1}\right) - \log_e(1)\right]$

$I = \dfrac{2}{3}\log_e\left(2\sqrt{2} + 3\right)$

$I = \dfrac{2}{3}\log_e\left(3 + 2\sqrt{2}\right)$

Hence, the correct option is $(3)\ \dfrac{2}{3}\log_e\left(3 + 2\sqrt{2}\right)$.

</details>

---

### Q3. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $(2^{1-a} + 2^{1+a})$, $f(a)$, $(3^a + 3^{-a})$ be in A.P. and $\alpha$ be the minimum value of $f(a)$. Then the value of the integral $\int_{\log_e(\alpha-1)}^{\log_e(\alpha)} \dfrac{dx}{(e^{2x} - e^{-2x})}$ is :

**Options:**

- **(A)** $\dfrac{1}{2} \log_e\left(\dfrac{4}{3}\right)$
- **(B)** $\dfrac{1}{4} \log_e\left(\dfrac{4}{3}\right)$
- **(C)** $\dfrac{1}{2} \log_e\left(\dfrac{8}{5}\right)$
- **(D)** $\dfrac{1}{4} \log_e\left(\dfrac{8}{5}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{4} \log_e\left(\dfrac{4}{3}\right)$**

**Detailed Solution:**

Since $(2^{1-a} + 2^{1+a})$, $f(a)$, and $(3^a + 3^{-a})$ are in A.P., we have:

$2f(a) = 2^{1-a} + 2^{1+a} + 3^a + 3^{-a}$

$f(a) = (2^{-a} + 2^a) + \dfrac{1}{2}(3^a + 3^{-a})$

Using the AM-GM inequality, $x + \dfrac{1}{x} \ge 2$ for $x > 0$.

$2^a + 2^{-a} \ge 2$ and $3^a + 3^{-a} \ge 2$.

The minimum value of $f(a)$ occurs when $a = 0$.

$\alpha = f(0) = (2^0 + 2^0) + \dfrac{1}{2}(3^0 + 3^0) = 2 + 1 = 3$.

Now, we evaluate the integral:

$I = \int_{\log_e 2}^{\log_e 3} \dfrac{dx}{e^{2x} - e^{-2x}} = \int_{\log_e 2}^{\log_e 3} \dfrac{e^{2x}}{e^{4x} - 1} dx$

Let $e^{2x} = t \Rightarrow 2e^{2x} dx = dt$.

When $x = \log_e 2$, $t = e^{2\log_e 2} = 4$.

When $x = \log_e 3$, $t = e^{2\log_e 3} = 9$.

$I = \dfrac{1}{2} \int_{4}^{9} \dfrac{dt}{t^2 - 1}$

$I = \dfrac{1}{2} \left[ \dfrac{1}{2} \log_e \left| \dfrac{t-1}{t+1} \right| \right]_{4}^{9}$

$I = \dfrac{1}{4} \left( \log_e \dfrac{8}{10} - \log_e \dfrac{3}{5} \right)$

$I = \dfrac{1}{4} \left( \log_e \dfrac{4}{5} - \log_e \dfrac{3}{5} \right) = \dfrac{1}{4} \log_e \left( \dfrac{4/5}{3/5} \right) = \dfrac{1}{4} \log_e \left( \dfrac{4}{3} \right)$

Answer: $\dfrac{1}{4} \log_e\left(\dfrac{4}{3}\right)$

</details>

---

### Q4. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\displaystyle\int_{\pi/6}^{\pi/3} \left(\dfrac{4 - \csc^2 x}{\cos^4 x}\right) dx$ is:

**Options:**

- **(A)** $\dfrac{11}{\sqrt{3}}$
- **(B)** $\dfrac{16}{\sqrt{3}}$
- **(C)** $\dfrac{32}{3\sqrt{3}}$
- **(D)** $\dfrac{64}{3\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{32}{3\sqrt{3}}$**

**Detailed Solution:**

The given integral is $I = \displaystyle\int_{\pi/6}^{\pi/3} \left(\dfrac{4 - \csc^2 x}{\cos^4 x}\right) dx$.

We can rewrite the integrand in terms of $\tan x$ and $\sec x$. Using the identity $\csc^2 x = 1 + \cot^2 x = 1 + \dfrac{1}{\tan^2 x}$, we get:

$I = \displaystyle\int_{\pi/6}^{\pi/3} \left(4 - 1 - \dfrac{1}{\tan^2 x}\right) \sec^4 x \, dx$

$I = \displaystyle\int_{\pi/6}^{\pi/3} \left(3 - \dfrac{1}{\tan^2 x}\right) (1 + \tan^2 x) \sec^2 x \, dx$

Substitute $t = \tan x$, which gives $dt = \sec^2 x \, dx$.

The limits of integration change as follows:
When $x = \dfrac{\pi}{6}$, $t = \dfrac{1}{\sqrt{3}}$.
When $x = \dfrac{\pi}{3}$, $t = \sqrt{3}$.

The integral becomes:

$I = \displaystyle\int_{1/\sqrt{3}}^{\sqrt{3}} \left(3 - \dfrac{1}{t^2}\right) (1 + t^2) dt$

Expanding the integrand, we get:

$I = \displaystyle\int_{1/\sqrt{3}}^{\sqrt{3}} \left(3 + 3t^2 - \dfrac{1}{t^2} - 1\right) dt$

$I = \displaystyle\int_{1/\sqrt{3}}^{\sqrt{3}} \left(3t^2 + 2 - t^{-2}\right) dt$

Integrating with respect to $t$:

$I = \left[ t^3 + 2t + \dfrac{1}{t} \right]_{1/\sqrt{3}}^{\sqrt{3}}$

Substitute the upper limit $t = \sqrt{3}$:

$\left( \sqrt{3} \right)^3 + 2\sqrt{3} + \dfrac{1}{\sqrt{3}} = 3\sqrt{3} + 2\sqrt{3} + \dfrac{\sqrt{3}}{3} = \dfrac{16\sqrt{3}}{3} = \dfrac{48}{3\sqrt{3}}$

Substitute the lower limit $t = \dfrac{1}{\sqrt{3}}$:

$\left( \dfrac{1}{\sqrt{3}} \right)^3 + 2\left( \dfrac{1}{\sqrt{3}} \right) + \sqrt{3} = \dfrac{1}{3\sqrt{3}} + \dfrac{2}{\sqrt{3}} + \sqrt{3} = \dfrac{1 + 6 + 9}{3\sqrt{3}} = \dfrac{16}{3\sqrt{3}}$

Subtracting the lower limit value from the upper limit value:

$I = \dfrac{48}{3\sqrt{3}} - \dfrac{16}{3\sqrt{3}} = \dfrac{32}{3\sqrt{3}}$

Answer: $\dfrac{32}{3\sqrt{3}}$

</details>

---

### Q5. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\displaystyle\int_0^\infty \dfrac{\log_e(x)}{x^2 + 4}\,dx$ is:

**Options:**

- **(A)** $\dfrac{\pi\log_e(2)}{2}$
- **(B)** $\dfrac{\pi\log_e(2)}{4}$
- **(C)** $1 + \pi\log_e(2)$
- **(D)** $2 + \pi\log_e(2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\pi\log_e(2)}{4}$**

**Detailed Solution:**

Let $I = \displaystyle\int_0^\infty \dfrac{\log_e(x)}{x^2 + 4}\,dx$

Substitute $x = 2 \tan \theta$, which gives $dx = 2 \sec^2 \theta \,d\theta$.

The limits of integration change from $x = 0 \to \theta = 0$ to $x \to \infty \to \theta = \dfrac{\pi}{2}$.

$I = \displaystyle\int_0^{\pi/2} \dfrac{\log_e(2 \tan \theta)}{4 \tan^2 \theta + 4} (2 \sec^2 \theta) \,d\theta$

$I = \displaystyle\int_0^{\pi/2} \dfrac{\log_e(2 \tan \theta)}{4 \sec^2 \theta} (2 \sec^2 \theta) \,d\theta$

$I = \dfrac{1}{2} \displaystyle\int_0^{\pi/2} \log_e(2 \tan \theta) \,d\theta$

$I = \dfrac{1}{2} \displaystyle\int_0^{\pi/2} (\log_e 2 + \log_e(\tan \theta)) \,d\theta$

$I = \dfrac{1}{2} \log_e 2 \displaystyle\int_0^{\pi/2} 1 \,d\theta + \dfrac{1}{2} \displaystyle\int_0^{\pi/2} \log_e(\tan \theta) \,d\theta$

Let $I_1 = \displaystyle\int_0^{\pi/2} \log_e(\tan \theta) \,d\theta$

Using the property $\displaystyle\int_0^a f(x)\,dx = \displaystyle\int_0^a f(a-x)\,dx$, we get:

$I_1 = \displaystyle\int_0^{\pi/2} \log_e\left(\tan\left(\dfrac{\pi}{2} - \theta\right)\right) \,d\theta = \displaystyle\int_0^{\pi/2} \log_e(\cot \theta) \,d\theta$

$I_1 = \displaystyle\int_0^{\pi/2} \log_e\left(\dfrac{1}{\tan \theta}\right) \,d\theta = -\displaystyle\int_0^{\pi/2} \log_e(\tan \theta) \,d\theta = -I_1$

$2I_1 = 0 \Rightarrow I_1 = 0$

Substituting $I_1 = 0$ back into the equation for $I$:

$I = \dfrac{1}{2} \log_e 2 \left[\theta\right]_0^{\pi/2} + 0$

$I = \dfrac{1}{2} \log_e 2 \left(\dfrac{\pi}{2}\right) = \dfrac{\pi \log_e 2}{4}$

Answer: $\dfrac{\pi\log_e(2)}{4}$

</details>

---

### Q6. JEE Main 2026 (21 January Shift 2)

*Type:* `numerical` | *Level:* `3`

If $\int_{0}^{1} 4 \cot ^{-1}\left(1-2 x+4 x^{2}\right) \mathrm{d} x=\mathrm{atan}^{-1}(2)-\mathrm{blog}_{\mathrm{e}}(5)$, where $\mathrm{a}, \mathrm{b} \in \mathbf{N}$, then $(2 \mathrm{a}+\mathrm{b})$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

Let $I=\int_0^1 \cot ^{-1}\left(1-2 x+4 x^2\right) d x$
$I=\int_0^1\left(\cot ^{-1}(2 x-1)-\cot ^{-1}(2 x)\right) d x$

Applying king
$I=\int_0^1\left(-\cot ^{-1}(2 x-1)+\cot ^{-1}(2 x-2)\right) d x$

From (1) and (2)

$2 I=\int_0^1\left(\cot ^{-1}(2 x-2)-\cot ^{-1}(2 x)\right) d x$
$=\int_0^1 \cot ^{-1}(2 x-2) d x-\int_0^1 \cot ^{-1}(2 x) d x$

Applying King

$=\int_0^1 \cot ^{-1}(-2 x) d x-\int_0^1 \cot ^{-1}(2 x) d x$
$=\int_0^1\left(\pi-\cot ^{-1}(2 x)\right) d x-\int_0^1 \cot ^{-1}(2 x) d x$
$=\int_0^1\left(\pi-2 \cot ^{-1}(2 x)\right) d x$
$=\pi-2 \int_0^1\left(\cot ^{-1} 2 x\right) \cdot 1 d x$

By parts
$=\pi-2\left[\left(x \cot ^{-1} 2 x\right)_0^1+\int_0^1 \frac{2 x}{1+4 x^2} d x\right]$

Let $1+4 \mathrm{x}^2=\mathrm{t}$
$8 \mathrm{xdx}=\mathrm{dt}$
$=\pi-2\left[\cot ^{-1} 2+\frac{1}{4} \int_1^5 \frac{\mathrm{dt}}{\mathrm{t}}\right]$
$=\pi-2 \cot ^{-1} 2-\frac{1}{2} \ell \mathrm{n} 5$
$2 \mathrm{I}=2 \tan ^{-1} 2-\frac{1}{2} \ell \mathrm{n} 5$
$\Rightarrow 4 \mathrm{I}=4 \tan ^{-1} 2-\ell \mathrm{n} 5$
$\therefore 2 \mathrm{a}+\mathrm{b}=8+1=9$

</details>

---

### Q7. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The integral \(80 \int_0^{\frac{\pi}{4}}\left(\frac{\sin \theta+\cos \theta}{9+16 \sin 2 \theta}\right) d \theta\) is equal to :

**Options:**

- **(A)** \(3 \log _e 4\)
- **(B)** \(4 \log _{\mathrm{e}} 3\)
- **(C)** \(6 \log _e 4\)
- **(D)** \(2 \log _e 3\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) \(4 \log _{\mathrm{e}} 3\)**

**Detailed Solution:**

$\begin{aligned} & I=\int_0^{\frac{\pi}{4}}\left(\frac{\sin \theta+\cos \theta}{9-16 \sin 2 \theta}\right) d \theta \\ & \text { Take } \sin \theta-\cos \theta=t \\ & (\cos \theta+\sin \theta) d \theta=d t \\ & (\sin \theta-\cos \theta)^2=t^2 \\ & \Rightarrow \sin 2 \theta=1-t^2 \\ & \theta=0 \rightarrow t=-1 \\ & \quad \theta=\frac{\pi}{4} \rightarrow t=0 \\ & I=\int_{-1}^0 \frac{d t}{9+16\left(1-t^2\right)} \\ & =\frac{1}{16} \int_{-1}^0 \frac{d t}{25} \frac{16}{16}-t^2 \\ & =\frac{1}{4}\left[\frac{1}{10} \log _{\left\lvert\, \frac{5+4 t}{}\right.}^{5-4 t}\right]_{-1}^0 \\ & =\frac{1}{40}\left[0+\log _e 9\right] \\ & I=\frac{\log _e 9}{40} \\ & 80 I=2 \log _e 9 \\ & 80 I=4 \log _e 3\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let for $f(x)=7 \tan ^8 x+7 \tan ^6 x-3 \tan ^4 x-3 \tan ^2 x, \quad \mathrm{I}_1=\int_0^{\pi / 4} f(x) \mathrm{d} x$ and $\mathrm{I}_2=\int_0^{\pi / 4} x f(x) \mathrm{d} x$. Then $7 \mathrm{I}_1+12 \mathrm{I}_2$ is equal to :

**Options:**

- **(A)** $2$
- **(B)** $1$
- **(C)** $2 \pi$
- **(D)** $\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1$**

**Detailed Solution:**

$\begin{aligned} f(x) & =7 \tan ^8 x+7 \tan ^6 x-3 \tan ^4 x-3 \tan ^2 x \\ & =7 \tan ^6 x\left(1+\tan ^2 x\right)-3 \tan ^2 x\left(1+\tan ^2 x\right) \\ & =\left(7 \tan ^6 x-3 \tan ^2 x\right)\left(1+\tan ^2 x\right) \\ & =\left(7 \tan ^6 x-3 \tan ^2 x\right) \sec ^2 x \\ l_1= & \int_0^{\frac{\pi}{4}} f(x) d x=\int_0^{\frac{\pi}{4}}\left(7 \tan ^6 x-3 \tan ^2 x\right) \sec ^2 x d x \\ & =\left.\left(\frac{7 \tan ^7 x}{7}-\frac{3 \tan ^3 x}{3}\right)\right|_0 ^{\frac{\pi}{4}}=1-1=0\end{aligned}$
$\begin{aligned}
I_2= & \int_0^{\frac{\pi}{4}} x f(x) d x=\int_0^{\frac{\pi}{4}} x\left(7 \tan ^6 x-3 \tan ^2 x\right) \sec ^2 x d x \\
& =\left.x\left(\tan ^7 x-\tan ^3 x\right)\right|_0 ^{\frac{\pi}{4}}-\int_0^{\frac{\pi}{4}} 1 \cdot\left(\tan ^7 x-\tan ^3 x\right) d x \\
& =0-\int_0^{\frac{\pi}{4}} \tan ^3 x\left(\tan ^2 x-1\right)\left(\tan ^2 x+1\right) d x \\
& =\int_0^{\frac{\pi}{4}}\left(\tan ^3 x-\tan ^5 x\right) \sec ^2 x d x=\frac{\tan ^4 x}{4}-\left.\frac{\tan ^6 x}{6}\right|_0 ^{\frac{\pi}{4}} \\
& =\frac{1}{12}
\end{aligned}$

Hence $7 I_1+12 I_2=1$

</details>

---

### Q9. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\int_\alpha^{\log _e 4} \frac{\mathrm{d} x}{\sqrt{\mathrm{e}^x-1}}=\frac{\pi}{6}$. Then $\mathrm{e}^\alpha$ and $\mathrm{e}^{-\alpha}$ are the roots of the equation :

**Options:**

- **(A)** $x^2+2 x-8=0$
- **(B)** $x^2-2 x-8=0$
- **(C)** $2 x^2-5 x+2=0$
- **(D)** $2 x^2-5 x-2=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 x^2-5 x+2=0$**

**Detailed Solution:**

$\begin{aligned} & \int_\alpha^{\log 4} \frac{\mathrm{dx}}{\sqrt{\mathrm{e}^{\mathrm{x}}-1}}=\frac{\pi}{6} \\ & \text { Let } \mathrm{e}^{\mathrm{x}}-1=\mathrm{t}^2 \\ & \mathrm{e}^{\mathrm{x}} \mathrm{dx}=2 \mathrm{t} \mathrm{dt} \\ & =\int \frac{2 \mathrm{dt}}{\mathrm{t}^2+1} \\ & =2 \tan ^{-1} \mathrm{t} \\ & =\left.2 \tan ^{-1}\left(\sqrt{\mathrm{e}^{\mathrm{x}}-1}\right)\right|_\alpha ^{\log _{\mathrm{e}}^4} \\ & =2\left[\tan ^{-1} \sqrt{3}-\tan ^{-1} \sqrt{\mathrm{e}^\alpha-1}\right]=\frac{\pi}{6} \\ & =\frac{\pi}{3}-\tan ^{-1} \sqrt{\mathrm{e}^\alpha-1}=\frac{\pi}{12} \\ & \Rightarrow \tan ^{-1} \sqrt{\mathrm{e}^\alpha-1}=\frac{\pi}{4} \\ & \mathrm{e}^\alpha=2 \quad \mathrm{e}^{-\alpha}=\frac{1}{2} \\ & \mathrm{x}^2-\left(2+\frac{1}{2}\right) \mathrm{x}+1=0 \\ & 2 \mathrm{x}^2-5 \mathrm{x}+2=0\end{aligned}$

</details>

---

### Q10. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int_0^{\pi / 4} \frac{\cos ^2 x \sin ^2 x}{\left(\cos ^3 x+\sin ^3 x\right)^2} d x$ is equal to

**Options:**

- **(A)** $1 / 6$
- **(B)** $1 / 3$
- **(C)** $1 / 12$
- **(D)** $1 / 9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1 / 6$**

**Detailed Solution:**

Divide $\mathrm{Nr} \& \mathrm{Dr}$ by $\cos \mathrm{x}$
$\int_0^{\pi / 4} \frac{\tan ^2 x \sec ^2 x d x}{\left(1+\tan ^3 x\right)^2} d x$
Let $1+\tan ^3 \mathrm{x}=\mathrm{t}$
$\begin{aligned}
& \tan ^2 x \sec ^2 x d x=\frac{d t}{3} \\
& \frac{1}{3} \int_1^2 \frac{\mathrm{dt}}{\mathrm{t}^2}=\frac{1}{6}
\end{aligned}$

</details>

---

### Q11. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mfenced><mrow><mo>-</mo><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></mrow></mfenced></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>∫</mo><mfrac><mrow><mo>cosec</mo><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mo>cosec</mo><mi>x</mi><mi>sec</mi><mi>x</mi><mo>+</mo><mi>tan</mi><mi>x</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><msup><mfenced><mfrac><mi>π</mi><mn>2</mn></mfrac></mfenced><mo>-</mo></msup></mrow></munder><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>π</mi><mn>4</mn></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>∫</mo><mfrac><mrow><mi>cosec</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mi>cosec</mi><mi>x</mi><mi>sec</mi><mi>x</mi><mo>+</mo><mi>tan</mi><mi>x</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>∫</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac></mstyle><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mrow><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac></mstyle><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>∫</mo><mfrac><mstyle displaystyle="true"><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow></mfrac></mstyle></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>∫</mo><mfrac><mstyle displaystyle="true"><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mi>cos</mi><mi>x</mi></mstyle><mstyle displaystyle="true"><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mstyle></mfrac><mi>d</mi><mi>x</mi></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>∫</mo><mfrac><mstyle displaystyle="true"><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mstyle><mstyle displaystyle="true"><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>4</mn></msup></mstyle></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>∫</mo><mfrac><mstyle displaystyle="true"><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></mstyle><mstyle displaystyle="true"><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></mstyle></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>∫</mo><mfrac><mstyle displaystyle="true"><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></mstyle><mstyle displaystyle="true"><msup><mfenced><mrow><mi>t</mi><mo>-</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn></mstyle></mfrac><mi>d</mi><mi>t</mi></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>-</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>=</mo><mi>u</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>∫</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><msup><mi>u</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mstyle></mfrac><mi>d</mi><mi>u</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>u</mi><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>t</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>t</mi></mfrac></mstyle></mrow><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac></mstyle></mrow><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mstyle displaystyle="true"><mi>cosec</mi><mi>x</mi></mstyle></mrow><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mo>+</mo><mi>C</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><msup><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><msup><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><msup><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>-</mo></msup></mrow></munder><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mstyle displaystyle="true"><mi>cosec</mi><mi>x</mi></mstyle></mrow><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mo>+</mo><mi>C</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>0</mn></mfenced><mo>+</mo><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mstyle displaystyle="true"><mi>cosec</mi><mi>x</mi></mstyle></mrow><msqrt><mn>2</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mfenced><mfrac><mi>π</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>sin</mi><mfrac><mi>π</mi><mn>4</mn></mfrac><mo>-</mo><mstyle displaystyle="true"><mi>cosec</mi><mfrac><mi>π</mi><mn>4</mn></mfrac></mstyle></mrow><msqrt><mn>2</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mfenced><mfrac><mi>π</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow><msqrt><mn>2</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mfenced><mfrac><mi>π</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac><msqrt><mn>2</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mfenced><mfrac><mi>π</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced></math></p>

</details>

---

### Q12. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&lt;</mo><mi mathvariant="normal">a</mi><mo>&lt;</mo><mn>1</mn></math>, the value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mn>0</mn><mi>π</mi></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>a</mi><mi>cos</mi><mi>x</mi><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>π</mi><mn>2</mn></msup><mrow><mi>π</mi><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>π</mi><mn>2</mn></msup><mrow><mi>π</mi><mo>-</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mrow><mn>1</mn><mo>-</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mrow><mn>1</mn><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mrow><mn>1</mn><mo>-</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">π</mi></msubsup><mfrac><mi>dx</mi><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>acosx</mi><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">π</mi></msubsup><mfrac><mi>dx</mi><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>acos</mi><mfenced><mrow><mi mathvariant="normal">π</mi><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">π</mi></msubsup><mfrac><mi>dx</mi><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>acosx</mi><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">π</mi></msubsup><mfrac><mi>dx</mi><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>acosx</mi><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac><mo> </mo><mo>+</mo><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">π</mi></msubsup><mfrac><mi>dx</mi><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>acosx</mi><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">π</mi></msubsup><mfenced><mrow><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>acosx</mi><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac><mo> </mo><mo>+</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>acosx</mi><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">π</mi></msubsup><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>acosx</mi><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><mi>acosx</mi><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mrow><mn>2</mn><mi>acosx</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></mfenced><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">π</mi></msubsup><mfenced><mfrac><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mrow><mn>2</mn><mi>acosx</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></mfenced><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi mathvariant="normal">I</mi><mo>=</mo><mn>2</mn><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><msup><mi>cos</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow></mfrac><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced><mo>·</mo><msup><mi>sec</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>·</mo><msup><mi>sec</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi><mo>-</mo><mn>4</mn><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced><mo>·</mo><msup><mi>sec</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><msup><mi>tan</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi><mo>-</mo><mn>4</mn><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced><mo>·</mo><msup><mi>sec</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi mathvariant="normal">a</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><msup><mi>tan</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow></mfrac><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>2</mn><mo>·</mo><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced><mo>·</mo><msup><mi>sec</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>·</mo><msup><mi>tan</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mfrac><mrow><mn>2</mn><mo>·</mo><msup><mi>sec</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac><mo>·</mo><mi>dx</mi></mrow><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi><mo>+</mo><msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tanx</mi><mo>=</mo><mi mathvariant="normal">t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>xdx</mi><mo>=</mo><mi>dt</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac><msubsup><mo>∫</mo><mn>0</mn><mo>∞</mo></msubsup><mfrac><mi>dt</mi><mrow><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac><mo>×</mo><mfrac><mn>1</mn><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac></mfenced></mfrac><msubsup><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi mathvariant="normal">t</mi><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac></mfenced></mfrac></mrow></mfenced><mn>0</mn><mo>∞</mo></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mo>∞</mo></mfenced><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>0</mn></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfenced></mfrac><mfenced close="]" open="["><mrow><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac><mo>-</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mi mathvariant="normal">π</mi><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup></mrow></mfrac></math></p>

</details>

---

### Q13. JEE Main 2023 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `3`

If
<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><msup><mi>x</mi><mn>21</mn></msup><mo>+</mo><msup><mi>x</mi><mn>14</mn></msup><mo>+</mo><msup><mi>x</mi><mn>7</mn></msup></mrow></mfenced><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>14</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>7</mn></msup><mo>+</mo><mn>6</mn></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>7</mn></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mi>l</mi></mfrac><msup><mfenced><mn>11</mn></mfenced><mrow><mi>m</mi><mo>/</mo><mi>n</mi></mrow></msup></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>,</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi><mo>,</mo><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> are co-prime then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>+</mo><mi>m</mi><mo>+</mo><mi>n</mi></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **63**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><msup><mi>x</mi><mn>20</mn></msup><mo>+</mo><msup><mi>x</mi><mn>13</mn></msup><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></mrow></mfenced><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>21</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>14</mn></msup><mo>+</mo><mn>6</mn><msup><mi>x</mi><mn>7</mn></msup></mrow></mfenced><mfrac><mn>1</mn><mn>7</mn></mfrac></msup><mi>d</mi><mi>x</mi></math></p><p>Put</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>21</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>14</mn></msup><mo>+</mo><mn>6</mn><msup><mi>x</mi><mn>7</mn></msup><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>42</mn><mfenced><mrow><msup><mi>x</mi><mn>20</mn></msup><mo>+</mo><msup><mi>x</mi><mn>13</mn></msup><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>42</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>11</mn></msubsup><msup><mi>t</mi><mfrac><mn>1</mn><mn>7</mn></mfrac></msup><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>42</mn></mfrac><msubsup><mfenced close="]" open="["><mfrac><mrow><mn>7</mn><msup><mi>t</mi><mfrac><mn>8</mn><mn>7</mn></mfrac></msup></mrow><mn>8</mn></mfrac></mfenced><mn>0</mn><mn>11</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>48</mn></mfrac><msup><mfenced><mn>11</mn></mfenced><mfrac><mn>8</mn><mn>7</mn></mfrac></msup></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>48</mn><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>=</mo><mn>8</mn><mo>,</mo><mi>n</mi><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>l</mi><mo>+</mo><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>63</mn></math></p>

</details>

---

### Q14. JEE Main 2023 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#62;</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#945;</mi></msubsup><mfrac><mi>x</mi><mrow><msqrt><mi>x</mi><mo>+</mo><mi>&#945;</mi></msqrt><mo>-</mo><msqrt><mi>x</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>16</mn><mo>+</mo><mn>20</mn><msqrt><mn>2</mn></msqrt></mrow><mn>15</mn></mfrac></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#945;</mi></msubsup><mfrac><mi>x</mi><mrow><msqrt><mi>x</mi><mo>+</mo><mi>&#945;</mi></msqrt><mo>-</mo><msqrt><mi>x</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>16</mn><mo>+</mo><mn>20</mn><msqrt><mn>2</mn></msqrt></mrow><mn>15</mn></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>Rationalise the denominator in L.H.S we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#945;</mi></msubsup><mfrac><mrow><mi>x</mi><mo>(</mo><msqrt><mi>&#945;</mi><mo>+</mo><mi>x</mi></msqrt><mo>+</mo><msqrt><mi>x</mi></msqrt><mo>)</mo></mrow><mi>&#945;</mi></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac><mfenced close="]" open="["><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#945;</mi></msubsup><mi>x</mi><msqrt><mi>&#945;</mi><mo>+</mo><mi>x</mi></msqrt><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#945;</mi></msubsup><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>x</mi><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>tdt</mi></math></p><p>Limit when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8594;</mo><mi>t</mi><mo>=</mo><msqrt><mi>&#945;</mi></msqrt><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mi>&#945;</mi><mo>&#8594;</mo><mi>t</mi><mo>=</mo><msqrt><mn>2</mn><mi>&#945;</mi></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>&#945;</mi></mfrac><msubsup><mo>&#8747;</mo><msqrt><mi>&#945;</mi></msqrt><msqrt><mn>2</mn><mi>&#945;</mi></msqrt></msubsup><mfenced><mrow><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mn>2</mn><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup><mi>dt</mi><mo>+</mo><mfrac><mrow><mn>2</mn><msup><mi>&#945;</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac><msubsup><mfenced close="]" open="["><mrow><mfrac><mrow><mn>2</mn><msup><mi>t</mi><mn>5</mn></msup></mrow><mn>5</mn></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><mi>&#945;</mi><msup><mi>t</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac></mrow></mfenced><msqrt><mi>&#945;</mi></msqrt><msqrt><mn>2</mn><mi>&#945;</mi></msqrt></msubsup><mo>+</mo><mfrac><mrow><mn>2</mn><msup><mi>&#945;</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><mi>&#945;</mi><msqrt><mn>2</mn><mi>&#945;</mi></msqrt><mo>+</mo><mn>10</mn><mi>&#945;</mi><msqrt><mi>&#945;</mi></msqrt></mrow><mn>15</mn></mfrac></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#945;</mi></msubsup><mfrac><mi>x</mi><mrow><msqrt><mi>x</mi><mo>+</mo><mi>&#945;</mi></msqrt><mo>-</mo><msqrt><mi>x</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>16</mn><mo>+</mo><mn>20</mn><msqrt><mn>2</mn></msqrt></mrow><mn>15</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>4</mn><mi>&#945;</mi><msqrt><mn>2</mn><mi>&#945;</mi></msqrt><mo>+</mo><mn>10</mn><mi>&#945;</mi><msqrt><mi>&#945;</mi></msqrt></mrow><mn>15</mn></mfrac><mo>=</mo><mfrac><mrow><mn>16</mn><mo>+</mo><mn>20</mn><msqrt><mn>2</mn></msqrt></mrow><mn>15</mn></mfrac></math></p><p>On comparing both sides we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q15. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mfenced><mrow><mn>2</mn><mo>+</mo><mn>3</mn><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mi>sin</mi><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>2</mn></mfrac><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>+</mo><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><mn>3</mn></mfrac><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><mn>3</mn></mfrac><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><mn>3</mn></mfrac><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>2</mn><mo>+</mo><mn>3</mn><mi>sin</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Now rearranging the above integral we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mn>2</mn><mrow><mi>sin</mi><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mn>3</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mn>3</mn><mfenced><mrow><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><munder><munder><mrow><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>d</mo><mi>x</mi></mrow><mo>&#9183;</mo></munder><msub><mi>I</mi><mn>1</mn></msub></munder><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><munder><munder><mrow><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><msup><mi>sec</mi><mn>2</mn></msup><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mo>d</mo><mi>x</mi></mrow><mo>&#9183;</mo></munder><msub><mi>I</mi><mn>2</mn></msub></munder></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><munder><munder><mrow><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></mrow><mo>&#9183;</mo></munder><msub><mi>I</mi><mn>1</mn></msub></munder><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>2</mn><munder><munder><msubsup><mfenced open="[" close="]"><mrow><mi>tan</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mo>&#9183;</mo></munder><msub><mi>I</mi><mn>2</mn></msub></munder></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><munder><munder><mrow><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></mrow><mo>&#9183;</mo></munder><msub><mi>I</mi><mn>1</mn></msub></munder><mo>+</mo><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mrow></mfenced></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mn>1</mn><mrow><mi>sin</mi><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mn>1</mn><mrow><mfenced><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi>tan</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow></mfrac></mstyle></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow></mfrac></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mfenced><mfrac><mstyle displaystyle="true"><mi>x</mi></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mfenced></mrow></mfenced><msup><mi>sec</mi><mn>2</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow><mstyle displaystyle="true"><mi>tan</mi><mfenced><mfrac><mstyle displaystyle="true"><mi>x</mi></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mfenced></mstyle></mfrac><mi>d</mi><mi>x</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><mi>v</mi><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>sec</mi><mn>2</mn></msup><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>v</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mn>1</mn></msubsup><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>v</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>v</mi></mrow><mi>v</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mfenced open="[" close="]"><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mi>v</mi></mfenced><mo>+</mo><mfrac><msup><mi>v</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>1</mn></mfenced><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>10</mn><mn>3</mn></mfrac><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><msqrt><mn>3</mn></msqrt></math></p>

</details>

---

### Q16. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></math>   is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></math>**

**Detailed Solution:**

<p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>2</mn></msubsup><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mi>x</mi></mfrac><mo>d</mo><mi>x</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac><mi>d</mi><mi>t</mi></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>-</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>t</mi></mfrac></mstyle></mfenced></mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>t</mi></mfrac></mstyle></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac><mo>d</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mi>t</mi></mfrac></mfenced><mo>&#215;</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>d</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>2</mn></msubsup><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi><mo>&#215;</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>2</mn></msubsup><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>&#215;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>d</mo><mi>x</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>2</mn></msubsup><mfrac><mn>1</mn><mi>x</mi></mfrac><mfenced><mrow><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>2</mn></msubsup><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>&#215;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><msubsup><mfenced close="]" open="["><mrow><mi>ln</mi><mi>x</mi></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math></p>

</details>

---

### Q17. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>6</mn></mfrac><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>12</mn></mfrac><mo>+</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>12</mn></mfrac><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>6</mn></mfrac><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>6</mn></mfrac><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mn>4</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>16</mn><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>16</mn><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><msup><mi>x</mi><mn>4</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>-</mo><mn>4</mn><msubsup><mo>&#8747;</mo><mn>3</mn><mfrac><mn>3</mn><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><msup><mfenced><mfrac><mn>2</mn><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mn>2</mn></msup><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mn>4</mn><msubsup><mo>&#8747;</mo><mn>3</mn><mfrac><mn>3</mn><mn>2</mn></mfrac></msubsup><msup><mfenced><mfrac><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mi>t</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>4</mn><mn>4</mn></mfrac><msubsup><mo>&#8747;</mo><mn>3</mn><mfrac><mn>3</mn><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mi>t</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>dt</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mn>1</mn><msubsup><mfenced close="]" open="["><mrow><mi mathvariant="normal">t</mi><mo>-</mo><mn>2</mn><mi>ln</mi><mfenced close="|" open="|"><mi>t</mi></mfenced><mo>-</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></mrow></mfenced><mn>3</mn><mfrac><mn>2</mn><mn>2</mn></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mn>1</mn><mfenced close="]" open="["><mrow><mfenced><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mi>ln</mi><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn><mi>ln</mi><mn>3</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mn>1</mn><mfenced close="]" open="["><mrow><mn>2</mn><mi>ln</mi><mn>2</mn><mo>-</mo><mfrac><mn>11</mn><mn>6</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>11</mn><mn>6</mn></mfrac><mo>-</mo><mi>ln</mi><mn>4</mn></math></p>

</details>

---

### Q18. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>&#945;</mi></msubsup><mfrac><mrow><msub><mi>log</mi><mn>10</mn></msub><mi>t</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfrac><mi>d</mi><mi>t</mi><mo>,</mo><mi>&#945;</mi><mo>&#62;</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mi>e</mi><mn>3</mn></msup></mfenced><mo>+</mo><mi>f</mi><mfenced><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>10</mn></mfenced></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mrow><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>10</mn></mfenced></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mrow><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>10</mn></mfenced></mrow></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>&#945;</mi></msubsup><mfrac><mrow><msub><mi>log</mi><mn>10</mn></msub><mi>t</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mi>e</mi><mn>3</mn></msup></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><msup><mi>e</mi><mn>3</mn></msup></msubsup><mfrac><mrow><mi>ln</mi><mi>t</mi></mrow><mrow><mi>ln</mi><mn>10</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced></mrow></mfrac><mi>dt</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Again <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>&#945;</mi></msubsup><mfrac><mrow><mi>ln</mi><mi>t</mi></mrow><mrow><mfenced><mrow><mi>ln</mi><mn>10</mn></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mi>t</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mfrac><mn>1</mn><mi>a</mi></mfrac></msubsup><mfrac><mrow><mo>-</mo><mi>ln</mi><mi>n</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mi>ln</mi><mn>10</mn></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced></mrow></mfrac><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mi>l</mi><mi mathvariant="normal">n</mi><mn>10</mn></mrow></mfrac><msubsup><mo>&#8747;</mo><mn>1</mn><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></msubsup><mfrac><mrow><mi>l</mi><mi>n</mi><mi>x</mi></mrow><mrow><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mi>l</mi><mi>n</mi><mn>10</mn></mrow></mfrac><msubsup><mo>&#8747;</mo><mn>1</mn><msup><mi>e</mi><mn>3</mn></msup></msubsup><mfrac><mrow><mi>l</mi><mi>n</mi><mi>t</mi></mrow><mrow><mi>t</mi><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now adding equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mi>e</mi><mn>3</mn></msup></mfenced><mo>+</mo><mi>f</mi><mfenced><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mfrac><mn>1</mn><mrow><mi>ln</mi><mi>n</mi><mn>10</mn></mrow></mfrac></mfenced><msubsup><mo>&#8747;</mo><mn>1</mn><msup><mi mathvariant="normal">c</mi><mn>3</mn></msup></msubsup><mfrac><mrow><mi>l</mi><mi>n</mi><mi>t</mi></mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced></mfrac><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><msup><mi>e</mi><mn>3</mn></msup></mfenced><mo>+</mo><mi>f</mi><mfenced><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></mfenced><mo>=</mo><mfenced><mfrac><mn>1</mn><mrow><mi>ln</mi><mn>10</mn></mrow></mfrac></mfenced><msubsup><mo>&#8747;</mo><mn>1</mn><mn>3</mn></msubsup><mfrac><mrow><mi>ln</mi><mi>t</mi></mrow><mi>t</mi></mfrac><mi>d</mi><mi>t</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mi>t</mi><mo>=</mo><mi>r</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mi>t</mi></mfrac><mo>=</mo><mi>d</mi><mi>r</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mi>e</mi><mn>3</mn></msup></mfenced><mo>+</mo><mi>f</mi><mfenced><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mi>ln</mi><mn>10</mn></mrow></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mi>r</mi><mi>d</mi><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><msup><mi>e</mi><mn>3</mn></msup></mfenced><mo>+</mo><mi>f</mi><mfenced><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></mfenced><msubsup><menclose notation="right"><mo>=</mo><mfenced><mrow><mfrac><mn>1</mn><mi>ln</mi></mfrac><mn>10</mn></mrow></mfenced><mfenced><mfrac><msup><mi>r</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced></menclose><mn>0</mn><mn>3</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><msup><mi>e</mi><mn>3</mn></msup></mfenced><mo>+</mo><mi>f</mi><mfenced><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></mfenced><mo>=</mo><mfenced><mfrac><mn>1</mn><mrow><mi>log</mi><mn>10</mn></mrow></mfrac></mfenced><mfenced><mfrac><mn>9</mn><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><msup><mi>e</mi><mn>3</mn></msup></mfenced><mo>+</mo><mi>f</mi><mfenced><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></mfenced><mo>=</mo><mfrac><mn>9</mn><mrow><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mn>10</mn></mrow></mfrac></math></p></blockquote>

</details>

---

### Q19. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mn>1</mn><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>2</mn></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>2</mn></mfenced><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>2</mn></mfenced><mo>-</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>2</mn></mfenced><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mstyle displaystyle="true"><mfenced><mfrac><mrow><mn>2</mn><mi>tan</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow></mfrac></mfenced></mstyle><mo>+</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>&#183;</mo><mi>d</mi><mi>x</mi></mrow><mrow><mn>2</mn><msup><mi>tan</mi><mn>2</mn></msup><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mn>4</mn><mi>tan</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mn>4</mn></mrow></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>=</mo><mi>t</mi><mo>&#160;</mo><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mtext>sec</mtext><mn>2</mn></msup><mfrac><mi>x</mi><mn>2</mn></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math>, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msubsup><menclose notation="right"><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></menclose><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mo>-</mo><mstyle displaystyle="false"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle></math></p></blockquote>

</details>

---

### Q20. JEE Main 2022 (28 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mn>60</mn><mfrac><mrow><mi>sin</mi><mfenced><mrow><mn>6</mn><mi>x</mi></mrow></mfenced></mrow><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **104**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mn>60</mn><mfrac><mrow><mi>sin</mi><mn>6</mn><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mn>60</mn><mfrac><mrow><mn>2</mn><mi>sin</mi><mn>3</mn><mi>x</mi><mi>cos</mi><mn>3</mn><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>60</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>2</mn><mfenced><mrow><mn>3</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mn>4</mn><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>4</mn><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mo>-</mo><mn>3</mn><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>120</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>120</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math> and limit changes to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#160;</mo><mtext>to&#160;</mtext><mn>1</mn></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>120</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>4</mn><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mn>4</mn><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>120</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mn>3</mn><mo>-</mo><mn>16</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><msup><mi>t</mi><mn>4</mn></msup><mo>&#160;</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>120</mn><msubsup><mfenced close="]" open="["><mrow><mn>3</mn><mi>t</mi><mo>-</mo><mfrac><mrow><mn>16</mn><msup><mi>t</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>16</mn><msup><mi>t</mi><mn>5</mn></msup></mrow><mn>5</mn></mfrac></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>120</mn><mfenced close="]" open="["><mrow><mn>3</mn><mo>-</mo><mfrac><mn>16</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>16</mn><mn>5</mn></mfrac></mrow></mfenced><mo>=</mo><mn>120</mn><mo>&#215;</mo><mfrac><mrow><mn>45</mn><mo>-</mo><mn>80</mn><mo>+</mo><mn>48</mn></mrow><mn>15</mn></mfrac><mo>=</mo><mn>8</mn><mo>&#215;</mo><mn>13</mn><mo>=</mo><mn>104</mn></math></p></blockquote>

</details>

---

### Q21. JEE Main 2022 (28 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><msqrt><mn>3</mn></msqrt></msubsup><mfrac><mrow><mn>15</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msqrt><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>3</mn></msup></msqrt></msqrt></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>&#946;</mi><msqrt><mn>3</mn></msqrt></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math> are integers, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><msqrt><mn>3</mn></msqrt></msubsup><mfrac><mrow><mn>15</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msqrt><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>3</mn></msup></msqrt></msqrt></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>&#946;</mi><msqrt><mn>3</mn></msqrt></math>, </p><p>Taking L.H.S we get <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><msqrt><mn>3</mn></msqrt></msubsup><mfrac><mrow><mn>15</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msqrt><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>3</mn></msup></msqrt></msqrt></mfrac><mi>d</mi><mi>x</mi></math></p><p>Now put <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>d</mi><mi>t</mi><mo>=</mo><mi>t</mi><mi>d</mi><mi mathvariant="normal">t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfrac><mrow><mn>15</mn><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mi>t</mi><mi>d</mi><mi>t</mi></mrow><msqrt><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><msup><mi>t</mi><mn>3</mn></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>15</mn><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfrac><mrow><mi>t</mi><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>t</mi><msqrt><mn>1</mn><mo>+</mo><mi>t</mi></msqrt></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p>Now put <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>t</mi><mo>=</mo><msup><mi>u</mi><mn>2</mn></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mi>t</mi><mo>=</mo><mn>2</mn><mi>u</mi><mi>d</mi><mi>u</mi></math></p><p>So, the integral will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><msubsup><mo>&#8747;</mo><msqrt><mn>2</mn></msqrt><msqrt><mn>3</mn></msqrt></msubsup><mfrac><mrow><msup><mfenced><mrow><msup><mi>u</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mi>u</mi></mfrac><mo>&#215;</mo><mn>2</mn><mi>u</mi><mi>d</mi><mi>u</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>30</mn><msubsup><mo>&#8747;</mo><msqrt><mn>2</mn></msqrt><msqrt><mn>3</mn></msqrt></msubsup><mfenced><mrow><msup><mi>u</mi><mn>4</mn></msup><mo>-</mo><mn>2</mn><msup><mi>u</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>u</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>30</mn><msubsup><mfenced><mrow><mfrac><msup><mi>u</mi><mn>5</mn></msup><mn>5</mn></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><msup><mi>u</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac></mrow></mfenced><msqrt><mn>2</mn></msqrt><msqrt><mn>3</mn></msqrt></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>30</mn><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>5</mn></mfrac><mfenced><mrow><msup><msqrt><mn>3</mn></msqrt><mn>5</mn></msup><mo>-</mo><msup><msqrt><mn>2</mn></msqrt><mn>5</mn></msup></mrow></mfenced><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mfenced><mrow><msup><msqrt><mn>3</mn></msqrt><mn>3</mn></msup><mo>-</mo><msup><msqrt><mn>2</mn></msqrt><mn>3</mn></msup></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>30</mn><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>5</mn></mfrac><mfenced><mrow><mn>9</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mfenced><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>30</mn><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>&#215;</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><mfrac><mn>8</mn><mn>15</mn></mfrac><msqrt><mn>2</mn></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>6</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>16</mn><msqrt><mn>2</mn></msqrt></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><msqrt><mn>4</mn></msqrt></msubsup><mfrac><mrow><mn>15</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msqrt><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>3</mn></msup></msqrt></msqrt></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>&#946;</mi><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>6</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>16</mn><msqrt><mn>2</mn></msqrt><mo>=</mo><mi>&#945;</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>&#946;</mi><msqrt><mn>3</mn></msqrt></math></p><p>Now on comparing we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>16</mn><mo>,</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>10</mn></math></p></blockquote>

</details>

---

### Q22. JEE Main 2022 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> be a differentiable function satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><msqrt><mn>3</mn></msqrt></msubsup><mi>f</mi><mfenced><mfrac><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mi>x</mi></mrow><mn>3</mn></mfrac></mfenced><mi>d</mi><mi>&#955;</mi><mo>,</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mn>6</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><msqrt><mn>3</mn></msqrt></msubsup><mi>f</mi><mfenced><mfrac><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mi>x</mi></mrow><mn>3</mn></mfrac></mfenced><mi>d</mi><mi>&#955;</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mi>x</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mi>&#955;</mi><mi>x</mi></mrow><mn>3</mn></mfrac><mo>&#160;</mo><mi>d</mi><mi>&#955;</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mi>&#955;</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#183;</mo><mfrac><mrow><mn>1</mn><msqrt><mi>x</mi></msqrt></mrow><mrow><mi mathvariant="normal">x</mi><mo>&#183;</mo><msqrt><mn>3</mn></msqrt><msqrt><mi>t</mi></msqrt></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mi>&#955;</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>&#183;</mo><mfrac><mn>1</mn><msqrt><mi>x</mi></msqrt></mfrac><mo>&#183;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msqrt><mi>t</mi></msqrt></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mi>x</mi></msqrt></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfrac><mrow><mi>f</mi><mfenced><mi>t</mi></mfenced></mrow><msqrt><mi>t</mi></msqrt></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>x</mi></msqrt><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfrac><mrow><mi>f</mi><mfenced><mi>t</mi></mfenced></mrow><msqrt><mi>t</mi></msqrt></mfrac><mi>d</mi><mi>t</mi></math></p><p>Now differentiating both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mi>x</mi></msqrt><mo>&#183;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mn>2</mn><msqrt><mi>x</mi></msqrt></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><msqrt><mi>x</mi></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mi>x</mi></msqrt><mo>&#183;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mn>2</mn><msqrt><mi>x</mi></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mi>y</mi></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></math></p><p>Now integrating both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mi>y</mi></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mi>x</mi><mo>+</mo><mi>ln</mi><mi>c</mi></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>0</mn><mo>+</mo><mi>ln</mi><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msqrt><mn>3</mn><mi>x</mi></msqrt></math></p><p>Now given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mn>6</mn></mrow></mfenced></math>,</p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><mn>6</mn><mo>&#8658;</mo><mn>36</mn><mo>=</mo><mn>3</mn><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>12</mn></math></p></blockquote>

</details>

---

### Q23. JEE Main 2022 (26 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>24</mn><mi>&#960;</mi></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><msqrt><mn>2</mn></msqrt></msubsup><mfrac><mrow><mfenced><mrow><mn>2</mn><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced><mi>dx</mi></mrow><mrow><mfenced><mrow><mn>2</mn><mo>+</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced><msqrt><mn>4</mn><mo>+</mo><msup><mi mathvariant="normal">x</mi><mn>4</mn></msup></msqrt></mrow></mfrac></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>24</mn><mi>&#960;</mi></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><msqrt><mn>2</mn></msqrt></msubsup><mfrac><mrow><mn>2</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mfenced><mrow><mn>2</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><msqrt><mn>4</mn><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></msqrt></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>24</mn><mi>&#960;</mi></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><msqrt><mn>2</mn></msqrt></msubsup><mfrac><mrow><mn>2</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><msqrt><mfenced><mrow><mfrac><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>24</mn><mi>&#960;</mi></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><msqrt><mn>2</mn></msqrt></msubsup><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mstyle><mo>-</mo><mn>1</mn></mrow><mrow><mfenced><mrow><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><msqrt><msup><mfenced><mrow><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>+</mo><mi>x</mi><mo>=</mo><mi>t</mi><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mo>-</mo><mfrac><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>24</mn><mi>&#960;</mi></mfrac><msubsup><mo>&#8747;</mo><mo>&#8734;</mo><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></msubsup><mfrac><mstyle displaystyle="true"><mi>d</mi><mi>t</mi></mstyle><mrow><mi>t</mi><msqrt><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></msqrt></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>12</mn><mi>&#960;</mi></mfrac><msubsup><mo>&#8747;</mo><mo>&#8734;</mo><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></msubsup><mfrac><mstyle displaystyle="true"><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi></mstyle><mrow><msup><mi>t</mi><mn>2</mn></msup><msqrt><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></msqrt></mrow></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>=</mo><msup><mi>z</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi><mo>=</mo><mn>2</mn><mi>z</mi><mi>d</mi><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>12</mn><mi>&#960;</mi></mfrac><msubsup><mo>&#8747;</mo><mo>&#8734;</mo><mn>2</mn></msubsup><mfrac><mstyle displaystyle="true"><mn>2</mn><mi>z</mi><mi>d</mi><mi>z</mi></mstyle><mrow><mi>z</mi><mfenced><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>24</mn><mi>&#960;</mi></mfrac><msubsup><mo>&#8747;</mo><mo>&#8734;</mo><mn>2</mn></msubsup><mfrac><mstyle displaystyle="true"><mi>d</mi><mi>z</mi></mstyle><mfenced><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>24</mn><mi>&#960;</mi></mfrac><msubsup><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>z</mi><mn>2</mn></mfrac></mrow></mfenced><mo>&#8734;</mo><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>24</mn><mi mathvariant="normal">&#960;</mi></mfrac><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>8</mn></mfrac><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q24. JEE Main 2022 (25 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mi>n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>n</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>,</mo><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>3</mn></msub><mo>-</mo><msub><mi>b</mi><mn>2</mn></msub><mo>,</mo><msub><mi>b</mi><mn>4</mn></msub><mo>-</mo><msub><mi>b</mi><mn>3</mn></msub><mo>,</mo><msub><mi>b</mi><mn>5</mn></msub><mo>-</mo><msub><mi>b</mi><mn>4</mn></msub></math> are in an A.P. with common difference<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msub><mi>b</mi><mn>3</mn></msub><mo>-</mo><msub><mi>b</mi><mn>2</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>b</mi><mn>4</mn></msub><mo>-</mo><msub><mi>b</mi><mn>3</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>b</mi><mn>5</mn></msub><mo>-</mo><msub><mi>b</mi><mn>4</mn></msub></mrow></mfrac></math> are in an A.P. with common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>3</mn></msub><mo>-</mo><msub><mi>b</mi><mn>2</mn></msub><mo>,</mo><msub><mi>b</mi><mn>4</mn></msub><mo>-</mo><msub><mi>b</mi><mn>3</mn></msub><mo>,</mo><msub><mi>b</mi><mn>5</mn></msub><mo>-</mo><msub><mi>b</mi><mn>4</mn></msub></math> are in a G.P.
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msub><mi>b</mi><mn>3</mn></msub><mo>-</mo><msub><mi>b</mi><mn>2</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>b</mi><mn>4</mn></msub><mo>-</mo><msub><mi>b</mi><mn>3</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>b</mi><mn>5</mn></msub><mo>-</mo><msub><mi>b</mi><mn>4</mn></msub></mrow></mfrac></math> are in an A.P. with common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msub><mi>b</mi><mn>3</mn></msub><mo>-</mo><msub><mi>b</mi><mn>2</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>b</mi><mn>4</mn></msub><mo>-</mo><msub><mi>b</mi><mn>3</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>b</mi><mn>5</mn></msub><mo>-</mo><msub><mi>b</mi><mn>4</mn></msub></mrow></mfrac></math> are in an A.P. with common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mi>n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mn>2</mn><mi>n</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mrow><mi mathvariant="normal">n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><msub><mi>b</mi><mi mathvariant="normal">n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>x</mi><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>n</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfrac><mrow><mo>-</mo><mi>sin</mi><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>x</mi><mi>sin</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced><mfrac><mrow><mi>cos</mi><mo>(</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mi>x</mi></mrow><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>So,<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msub><mi>b</mi><mn>3</mn></msub><mo>-</mo><msub><mi>b</mi><mn>2</mn></msub></mrow></mfrac><mo>=</mo><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msub><mi>b</mi><mn>4</mn></msub><mo>-</mo><msub><mi>b</mi><mn>3</mn></msub></mrow></mfrac><mo>=</mo><mo>-</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msub><mi>b</mi><mn>5</mn></msub><mo>-</mo><msub><mi>b</mi><mn>4</mn></msub></mrow></mfrac><mo>=</mo><mo>-</mo><mn>9</mn></math></p><p>So,<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msub><mi>b</mi><mn>3</mn></msub><mo>-</mo><msub><mi>b</mi><mn>2</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>b</mi><mn>4</mn></msub><mo>-</mo><msub><mi>b</mi><mn>3</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>b</mi><mn>5</mn></msub><mo>-</mo><msub><mi>b</mi><mn>4</mn></msub></mrow></mfrac></math> are in A.P. with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>.</mo><mi>d</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p>

</details>

---

### Q25. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><msqrt><mi>x</mi></msqrt><mi>d</mi><mi>x</mi></mrow><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo><mo>(</mo><mn>1</mn><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo><mo>(</mo><mn>3</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow></mfrac></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>&#8722;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>&#8722;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>6</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>&#8722;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>6</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>&#8722;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>x</mi></msqrt><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><msqrt><mi>x</mi></msqrt><mi>d</mi><mi>x</mi></mrow><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo><mo>(</mo><mn>1</mn><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo><mo>(</mo><mn>3</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mo>&#8202;</mo><mfrac><mrow><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup><mi>d</mi><mi>t</mi></mrow><mrow><mfenced separators="|"><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mo>&#8202;</mo><mfrac><mrow><mfenced separators="|"><mrow><mfenced separators="|"><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#8722;</mo><mfenced separators="|"><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi></mrow><mrow><mfenced separators="|"><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mo>&#8202;</mo><mfenced separators="|"><mrow><mfrac><mn>1</mn><mrow><mfenced separators="|"><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>&#8722;</mo><mfrac><mn>1</mn><mrow><mfenced separators="|"><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mo>&#8202;</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mn>2</mn><mfenced separators="|"><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>&#8722;</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mfrac><mrow><mn>3</mn><mi>d</mi><mi>t</mi></mrow><mfenced separators="|"><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>&#8722;</mo><mfrac><mn>3</mn><mn>8</mn></mfrac><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mfenced separators="|"><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>tan</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mi>t</mi><mo>&#8722;</mo><mfrac><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>8</mn><mo>&#215;</mo><mn>3</mn></mrow></mfrac><msup><mi>tan</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><msqrt><mn>3</mn></msqrt><mi>t</mi><mo>&#8722;</mo><mfrac><mn>3</mn><mrow><mn>8</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><msup><mi>tan</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfrac><mi>t</mi><msqrt><mn>3</mn></msqrt></mfrac></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mo>&#8722;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>8</mn></mfrac><mo>&#215;</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>&#8722;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>8</mn></mfrac><mo>&#215;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mo>&#8722;</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi>&#960;</mi></mrow><mn>16</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>&#8722;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></math></p>

</details>

---

### Q26. JEE Main 2021 (26 Feb Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>x</mi><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>d</mi><mi>x</mi></math>, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>,</mo><mi>n</mi><mo>&#10878;</mo><mn>1</mn></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><msup><mi>x</mi><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><msub><mi>I</mi><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></msub><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>&#8712;</mo><mi>R</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> equals ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>x</mi><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><msub><mi>I</mi><mrow><mi>n</mi><mo>,</mo><mi>m</mi></mrow></msub></math></p><p>Now Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><msup><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>y</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></msub><mo>=</mo><mo>-</mo><msubsup><mo>&#8747;</mo><mo>&#8734;</mo><mn>0</mn></msubsup><mfrac><mn>1</mn><msup><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup></mfrac><mfrac><msup><mi>y</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><msup><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mfrac><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><msup><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mo>&#8734;</mo></msubsup><mfrac><msup><mi>y</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></msup></mfrac><mi>d</mi><mi>y</mi></math></p><p>similarly <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mo>&#8734;</mo></msubsup><mfrac><msup><mi>y</mi><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></msup></mfrac><mi>d</mi><mi>y</mi></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>I</mi><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mo>&#8734;</mo></msubsup><mfrac><mrow><msup><mi>y</mi><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><msup><mi>y</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></msup></mfrac><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mo>&#8734;</mo></msubsup><mfrac><mrow><msup><mi>y</mi><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><msup><mi>y</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></msup></mfrac><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><msup><mi>y</mi><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><msup><mi>y</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></msup></mfrac><mi>d</mi><mi>y</mi><mo>+</mo><munder><munder><mrow><msubsup><mo>&#8747;</mo><mn>1</mn><mo>&#8734;</mo></msubsup><mfrac><mrow><msup><mi>y</mi><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><msup><mi>y</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></msup></mfrac><mi>d</mi><mi>y</mi></mrow><mo>&#9183;</mo></munder><mrow><mi>substitute</mi><mo>&#160;</mo><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></mrow></munder></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msub><mi>I</mi><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><msup><mi>y</mi><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><msup><mi>y</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></msup></mfrac><mi>d</mi><mi>y</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>0</mn></msubsup><mfrac><mrow><msup><mi>t</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><msup><mi>t</mi><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow><msup><mi>t</mi><mrow><mi>m</mi><mo>+</mo><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup></mfrac><mfrac><msup><mi>t</mi><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></msup></mfrac><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mi>t</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>I</mi><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></msub><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><msup><mi>y</mi><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><msup><mi>y</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></msup></mfrac><mi>d</mi><mi>y</mi><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q27. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>t</mi></mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced></mfrac><mi>d</mi><mi>t</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>e</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>e</mi></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>t</mi></mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mrow><mn>1</mn><mo>/</mo><mi>x</mi></mrow></msubsup><mfrac><mrow><mi>&#8467;</mi><mi>n</mi><mi>t</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfrac><mi>d</mi><mi>t</mi></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mi>y</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><mfrac><mrow><mi>&#8467;</mi><mi>n</mi><mfenced><mrow><mn>1</mn><mo>/</mo><mi>y</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mfenced><mrow><mn>1</mn><mo>/</mo><mi>y</mi></mrow></mfenced></mrow></mfrac><mo>.</mo><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msup><mi>y</mi><mn>2</mn></msup></mfrac></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><mfrac><mrow><mi>&#8467;</mi><mi>n</mi><mi>y</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfrac><mo>.</mo><mfrac><mi>y</mi><msup><mi>y</mi><mn>2</mn></msup></mfrac><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><mfrac><mrow><mi>&#8467;</mi><mi>n</mi><mi>y</mi></mrow><mrow><mi>y</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>y</mi></math></p><p>hence </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced><mi>&#8467;</mi><mi>n</mi><mi>t</mi></mrow><mrow><mi>t</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><mfrac><mrow><mi>&#8467;</mi><mi>n</mi><mi>t</mi></mrow><mi>t</mi></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>ln</mi><mn>2</mn></msup><mfenced><mi>x</mi></mfenced></math></p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>e</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>e</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p>

</details>

---

### Q28. JEE Main 2020 (06 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><msup><mi mathvariant="normal">e</mi><mi mathvariant="normal">x</mi></msup><mo>.</mo><mo>&#160;</mo><msup><mi mathvariant="normal">x</mi><mi>x</mi></msup><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>+</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mo>&#160;</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mo>&#160;</mo><mi>dx</mi></math> equals :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">e</mi><mfenced><mrow><mn>4</mn><mi mathvariant="normal">e</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">e</mi><mfenced><mrow><mn>4</mn><mi mathvariant="normal">e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">e</mi><mfenced><mrow><mn>2</mn><mi mathvariant="normal">e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">e</mi><mfenced><mrow><mn>4</mn><mi mathvariant="normal">e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><msup><mfenced><mi>ex</mi></mfenced><mi mathvariant="normal">x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="script">l</mi><mi>ny</mi><mo>=</mo><mi>x</mi><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mi mathvariant="script">l</mi><mi>nx</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi mathvariant="normal">y</mi></mfrac><mfrac><mi>dy</mi><mi>dx</mi></mfrac><mo>=</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mi mathvariant="script">l</mi><mi>nx</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>dy</mi><mo>=</mo><msup><mfenced><mi>ex</mi></mfenced><mi mathvariant="normal">x</mi></msup><mfenced><mrow><mn>2</mn><mo>+</mo><mi mathvariant="script">l</mi><mi>nx</mi></mrow></mfenced><mo>&#160;</mo><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mn>1</mn><mn>2</mn></munderover><msup><mi mathvariant="normal">e</mi><mi mathvariant="normal">x</mi></msup><mo>.</mo><msup><mi mathvariant="normal">x</mi><mi mathvariant="normal">x</mi></msup><mfenced><mrow><mn>2</mn><mo>+</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mi mathvariant="normal">x</mi></mrow></mfenced><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced><mi mathvariant="normal">y</mi></mfenced><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced><msup><mfenced><mi>ex</mi></mfenced><mi mathvariant="normal">x</mi></msup></mfenced><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup><mo>&#8722;</mo><mi mathvariant="normal">e</mi></math></p>

</details>

---

### Q29. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></msubsup><msup><mi>tan</mi><mn>3</mn></msup><mi>x</mi><mo>&#183;</mo><msup><mi>sin</mi><mn>2</mn></msup><mn>3</mn><mi>x</mi><mfenced><mrow><mn>2</mn><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>&#183;</mo><msup><mi>sin</mi><mn>2</mn></msup><mn>3</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>tan</mi><mi>x</mi><mo>&#183;</mo><mi>sin</mi><mn>6</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>18</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>18</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>18</mn></mfrac></math>**

**Detailed Solution:**

<p>Rearranging, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>6</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>3</mn></mrow></msubsup><mfenced><mrow><mfrac><mrow><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mrow><msup><mi>tan</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>&#183;</mo><msup><mi>sin</mi><mn>4</mn></msup><mn>3</mn><mi>x</mi><mo>+</mo><msup><mi>tan</mi><mn>4</mn></msup><mi>x</mi><mo>&#183;</mo><mfrac><mrow><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mn>3</mn><mi>x</mi></mrow></mfenced></mrow><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>6</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>3</mn></mrow></msubsup><mfenced><mrow><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mrow><msup><mi>tan</mi><mn>4</mn></msup><mi>x</mi><mo>&#183;</mo><msup><mi>sin</mi><mn>4</mn></msup><mn>3</mn><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mfenced open="[" close="]"><mrow><msup><mi>tan</mi><mn>4</mn></msup><mi>x</mi><mo>&#183;</mo><msup><mi>sin</mi><mn>4</mn></msup><mn>3</mn><mi>x</mi></mrow></mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>/</mo><mn>6</mn></mrow><mrow><mi mathvariant="normal">&#960;</mi><mo>/</mo><mn>3</mn></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>4</mn></msup><mo>&#215;</mo><mn>0</mn><mo>-</mo><msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mn>4</mn></msup><mo>&#215;</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>18</mn></mfrac></math></p>

</details>

---

### Q30. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></msup></mfrac><mi>d</mi><mi>x</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>k</mi><mn>6</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mi mathvariant="normal">&#960;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mi mathvariant="normal">&#960;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mi mathvariant="normal">&#960;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mi mathvariant="normal">&#960;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mi mathvariant="normal">&#960;</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>k</mi><mn>6</mn></mfrac><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfrac><msup><mi>x</mi><mn>2</mn></msup><mstyle displaystyle="true"><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mstyle></mfrac><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>sin</mi><mi>&#952;</mi><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mi>cos</mi><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>k</mi><mn>6</mn></mfrac><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></msubsup><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mo>&#160;</mo><mi>&#952;</mi></mrow><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mo>&#160;</mo><mi>&#952;</mi></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></msup></mfrac><mi>cos</mi><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi><mo>&#8658;</mo><mfrac><mi>k</mi><mn>6</mn></mfrac><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></msubsup><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mo>&#160;</mo><mi>&#952;</mi></mrow><mfenced><mrow><msup><mi>cos</mi><mn>3</mn></msup><mo>&#160;</mo><mi>&#952;</mi></mrow></mfenced></mfrac><mi>cos</mi><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>k</mi><mn>6</mn></mfrac><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></msubsup><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></msubsup><mfenced><mrow><mi>s</mi><mi>e</mi><msup><mi>c</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>&#952;</mi><mo>&#8658;</mo><mfrac><mi>k</mi><mn>6</mn></mfrac><mo>=</mo><msubsup><mfenced><mrow><mi>tan</mi><mi>&#952;</mi><mo>-</mo><mi>&#952;</mi></mrow></mfenced><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></msubsup><mo>=</mo><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mi>&#960;</mi></math></p>

</details>

---

### Q31. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math><msub><mrow><mi>&#952;</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi>&#952;</mi></mrow><mrow><mn>2</mn></mrow></msub></math> be respectively the smallest and the largest values of <math><mi>&#952;</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi></mrow></mfenced><mo>-</mo><mfenced open="{" close="}" separators="|"><mi>&#960;</mi></mfenced></math> which satisfy the equation, <math><mn>2</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">cot</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi><mo>-</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></mrow></mfrac><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></mrow></mrow></math> , then <math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><msub><mrow><mi>&#952;</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>&#952;</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></munderover><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mn>3</mn><mi>&#952;</mi></mrow></mrow></mrow></mrow><mi>d</mi><mi>&#952;</mi></math> is equal to:

**Options:**

- **(A)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mn>2</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">cot</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow><mo>-</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></mrow></mfrac><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
<math><mfrac><mrow><mn>2</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></mrow><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></mrow></mfrac><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi mathvariant="normal">&#952;</mi><mo>-</mo><mn>5</mn><mi>sin</mi><mo>&#8289;</mo><mi mathvariant="normal">&#952;</mi><mo>+</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mi mathvariant="normal">&#952;</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>sin</mi><mo>&#8289;</mo><mi mathvariant="normal">&#952;</mi><mo>&#8800;</mo><mn>0</mn></math>
<math><mn>2</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow><mo>-</mo><mn>5</mn><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>
<math><mfenced separators="|"><mrow><mn>2</mn><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi><mo>-</mo><mn>1</mn></mrow></mrow></mrow></mfenced><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi><mo>-</mo><mn>2</mn></mrow></mrow></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi></mrow></mfenced><mo>-</mo><mfenced open="{" close="}" separators="|"><mi>&#960;</mi></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><munderover><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>6</mn></mrow><mrow><mn>5</mn><mi mathvariant="normal">&#960;</mi><mo>/</mo><mn>6</mn></mrow></munderover><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mn>3</mn><mi mathvariant="normal">&#952;</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">&#952;</mi><mo>=</mo><munderover><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>6</mn></mrow><mrow><mn>5</mn><mi mathvariant="normal">&#960;</mi><mo>/</mo><mn>6</mn></mrow></munderover><mfrac><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mo>&#8289;</mo><mn>6</mn><mi mathvariant="normal">&#952;</mi></mrow><mn>2</mn></mfrac><mi mathvariant="normal">d</mi><mi mathvariant="normal">&#952;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mfenced close="]" open="[" separators="|"><mrow><mi>&#952;</mi><mo>+</mo><mfrac><mrow><mi>sin</mi><mo>&#8289;</mo><mn>6</mn><mi mathvariant="normal">&#952;</mi></mrow><mn>6</mn></mfrac></mrow></mfenced><mrow><mi>x</mi><mo>/</mo><mn>6</mn></mrow><mrow><mn>5</mn><mi mathvariant="normal">&#960;</mi><mo>/</mo><mn>6</mn></mrow></msubsup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mfenced separators="|"><mrow><mn>0</mn><mo>-</mo><mn>0</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>.</mo><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>

</details>

---

### Q32. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math><mi>f</mi><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>,</mo><mi></mi></math> for all <math><mi>x</mi><mo>,</mo><mi></mi></math> where <math><mi>a</mi></math> and <math><mi>b</mi></math> are fixed positive real numbers, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfrac><munderover><mo stretchy="true">&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>x</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">&#8747;</mo><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></munderover><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">&#8747;</mo><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></munderover><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">&#8747;</mo><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow></munderover><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">&#8747;</mo><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow></munderover><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">&#8747;</mo><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></munderover><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced></mfrac><munderover><mo stretchy="true">&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>x</mi><mfenced open="[" close="]" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math>
<math><mi>x</mi><mo>&#8594;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced></mfrac><munderover><mo stretchy="true">&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mfenced open="[" close="]" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced></mfrac><munderover><mo stretchy="true">&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>a</mi><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mfenced open="[" close="]" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo></math> Keeping <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mi>x</mi><mo>+</mo><mn>1</mn></math> in given relation
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mn>1</mn></mfenced><mo>+</mo><mfenced separators="|"><mn>2</mn></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><munderover><mo stretchy="true">&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mfenced open="[" close="]" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mo>d</mo><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><munderover><mo stretchy="true">&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><munderover><mo stretchy="true">&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><munderover><mo stretchy="true">&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>I</mi><mo>=</mo><mn>2</mn><munderover><mo stretchy="true">&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo stretchy="true">&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math>
Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>t</mi><mo>+</mo><mn>1</mn><mo>&#8658;</mo><mi>I</mi><mo>=</mo><munderover><mo stretchy="true">&#8747;</mo><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></munderover><mi>f</mi><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><munderover><mo stretchy="true">&#8747;</mo><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></munderover><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math>

</details>

---

### Q33. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></msubsup><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow><mfrac><mn>2</mn><mn>3</mn></mfrac></msup><mi>x</mi><mo>&#183;</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><msup><mi mathvariant="normal">c</mi><mfrac><mn>4</mn><mn>3</mn></mfrac></msup><mi>x</mi><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mfrac><mn>7</mn><mn>6</mn></mfrac></msup><mo>-</mo><msup><mn>3</mn><mfrac><mn>5</mn><mn>6</mn></mfrac></msup></math>
- **(B)** <math><msup><mrow><mn>3</mn></mrow><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>-</mo><msup><mrow><mn>3</mn></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></math>
- **(C)** <math><msup><mrow><mn>3</mn></mrow><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mi mathvariant="normal"> </mi></mrow></msup><mo>-</mo><msup><mrow><mn>3</mn></mrow><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></math>
- **(D)** <math><msup><mrow><mn>3</mn></mrow><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>-</mo><msup><mrow><mn>3</mn></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mfrac><mn>7</mn><mn>6</mn></mfrac></msup><mo>-</mo><msup><mn>3</mn><mfrac><mn>5</mn><mn>6</mn></mfrac></msup></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></msubsup><msup><mi>sec</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup><mi>x</mi><mo>&#183;</mo><msup><mi>cosec</mi><mfrac><mn>4</mn><mn>3</mn></mfrac></msup><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></msubsup><mfenced><mfrac><mn>1</mn><mrow><msup><mi>cos</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup><mi>x</mi><mo>&#183;</mo><msup><mi>sin</mi><mfrac><mn>4</mn><mn>3</mn></mfrac></msup><mi>x</mi></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></msubsup><mfenced><mfrac><mrow><msup><mi>cos</mi><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>3</mn></mfrac></mstyle></msup><mi>x</mi></mrow><mrow><msup><mi>cos</mi><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>3</mn></mfrac></mstyle></mrow></msup><mi>x</mi><mo>&#183;</mo><msup><mi>sin</mi><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>3</mn></mfrac></mstyle></msup><mi>x</mi></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></msubsup><mpadded lspace="-3px"><mfenced><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><msup><mi>tan</mi><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>3</mn></mfrac></mstyle></msup><mi>x</mi></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></mpadded></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>x</mi><mo>=</mo><mi>t</mi><mo>,</mo><msup><mi>&#160;sec</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math> and at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>t</mi><mo>=</mo><mi>tan</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math> and at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>t</mi><mo>=</mo><mi>tan</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><msqrt><mn>3</mn></msqrt></msubsup><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mi>t</mi><mfrac><mn>4</mn><mn>3</mn></mfrac></msup></mfrac></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>x</mi><mi>n</mi></msup><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><msup><mi>x</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mfenced open="[" close="]" separators="|"><mfrac><msup><mi>t</mi><mrow><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>+</mo><mn>1</mn></mrow></msup><mrow><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><msqrt><mn>3</mn></msqrt></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mfenced open="[" close="]" separators="|"><mrow><mo>-</mo><mn>3</mn><msup><mi>t</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></msup></mrow></mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><msqrt><mn>3</mn></msqrt></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mn>3</mn><mfenced open="{" close="}"><mrow><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></msup><mo>-</mo><msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mn>3</mn><mfenced open="{" close="}"><mrow><msup><mfenced><msup><mn>3</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></msup><mo>-</mo><msup><mfenced><mfrac><mn>1</mn><msup><mn>3</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></mfrac></mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>3</mn><mfenced separators="|"><mrow><mfrac><mn>1</mn><msup><mn>3</mn><mfrac><mn>1</mn><mn>6</mn></mfrac></msup></mfrac><mo>-</mo><msup><mn>3</mn><mfrac><mn>1</mn><mn>6</mn></mfrac></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><msup><mn>3</mn><mfrac><mn>1</mn><mn>6</mn></mfrac></msup></mfrac><mo>+</mo><mn>3</mn><mo>&#215;</mo><msup><mn>3</mn><mfrac><mn>1</mn><mn>6</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow><mo>=</mo><mn>3</mn></mrow><mfrac><mn>7</mn><mn>6</mn></mfrac></msup><mo>-</mo><msup><mn>3</mn><mfrac><mn>5</mn><mn>6</mn></mfrac></msup><mo>.</mo></math></p>

</details>

---

### Q34. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">&#8747;</mo><mn>1</mn><mi>e</mi></munderover><mfenced close="}" open="{" separators="|"><mrow><msup><mfenced separators="|"><mfrac><mi>x</mi><mi>e</mi></mfrac></mfenced><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mfenced separators="|"><mfrac><mi>e</mi><mi>x</mi></mfrac></mfenced><mi>x</mi></msup></mrow></mfenced><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mi mathvariant="normal">g</mi><mi>e</mi></msub><mtext>&#8201;</mtext><mi>x</mi><mtext>&#8201;&#8201;</mtext><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mi>e</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mi>e</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mi>e</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let <math><msub><mrow><mi>I</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mrow><msubsup><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></msubsup><mrow><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mi>e</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn><mi>x</mi></mrow></msup><mrow><mrow><msub><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi>e</mi></mrow></msub><mtext>&#8201;</mtext><mi>x</mi></mrow><mrow><mi>&#160;</mi></mrow></msub></mrow><mo>&#8289;</mo><mrow><mi>d</mi><mi>x</mi></mrow></mrow></mrow></mrow></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mfrac><mi>x</mi><mi>e</mi></mfrac></mfenced><mi>x</mi></msup><mo>=</mo><mi>t</mi></math></p><p>Taking natural logarithm on both sides, we get</p><p><math> <mi>x</mi><mtext>&#8201;</mtext><mtext>ln</mtext><mfrac> <mi>x</mi> <mi>e</mi> </mfrac> <mo>=</mo><mtext>ln&#160;</mtext><mi>t</mi> </math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfenced><mrow><mtext>ln&#8201;</mtext><mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mtext>ln</mtext><mtext>&#8201;</mtext><mi>t</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><table border="1" cellpadding="1" cellspacing="1" style="width: 250px;">	<tbody>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mfenced><mrow><mi>ln</mi><mn>1</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>ln</mi><mi>t</mi><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mi>e</mi></mfrac></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mfenced><mrow><mi>ln</mi><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>ln</mi><mi>t</mi><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>1</mn></math></td>		</tr>	</tbody></table><p>Differentiating equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> on both the sides, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>ln</mtext><mtext>&#8201;</mtext><mi>x</mi><mo>&#8722;</mo><mn>1</mn><mo>+</mo><mi>x</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#8658;ln</mtext><mtext>&#8201;</mtext><mi>x</mi><mtext>&#8201;</mtext><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mi>e</mi></mfrac><mn>1</mn></msubsup><msup><mi>t</mi><mn>2</mn></msup><mfrac><mn>1</mn><mi>t</mi></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><msubsup><mfenced><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mfrac><mn>1</mn><mi>e</mi></mfrac><mn>1</mn></msubsup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>e</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>e</mi></msubsup><msup><mfenced separators="|"><mfrac><mi>e</mi><mi>x</mi></mfrac></mfenced><mi>x</mi></msup><msub><mi>log</mi><mi>e</mi></msub><mtext>&#8201;</mtext><mi>x</mi><mo>&#8289;</mo><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mfrac><mi>e</mi><mi>x</mi></mfrac></mfenced><mi>x</mi></msup><mo>=</mo><mi>t</mi></math></p><p>Taking natural logarithm on both sides, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>ln</mi><mfenced><mfrac><mi>e</mi><mi>x</mi></mfrac></mfenced><mo>=</mo><mi>ln</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>ln</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mi>ln</mi><mi>t</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><table border="1" cellpadding="1" cellspacing="1" style="width: 250px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>ln</mi><mn>1</mn></mrow></mfenced><mo>=</mo><mi>ln</mi><mi>t</mi><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mi>e</mi></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>ln</mi><mi>e</mi></mrow></mfenced><mo>=</mo><mi>ln</mi><mi>t</mi><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>1</mn></math></td>		</tr>	</tbody></table><p>Differentiating equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math> both sides, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mrow><mi>x</mi><mfenced><mrow><mn>0</mn><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>ln</mi><mi>x</mi></mrow></mfenced><mo>.</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mi>t</mi></mfrac></math> (using product rule of differentiation)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mi>t</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mi>e</mi><mn>1</mn></msubsup><mi>t</mi><mo>.</mo><mfrac><mrow><mo>-</mo><mi>d</mi><mi>t</mi></mrow><mi>t</mi></mfrac><mo>=</mo><msubsup><mfenced><mrow><mo>-</mo><mi>t</mi></mrow></mfenced><mi>e</mi><mn>1</mn></msubsup><mo>=</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mo>-</mo><mi>e</mi></mrow></mfenced><mo>=</mo><mi>e</mi><mo>-</mo><mn>1</mn></math></p><p>Hence, required integral is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>-</mo><msub><mi>I</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>e</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mi>e</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>.</p>

</details>

---

### Q35. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The integral $\int_{\pi / 6}^{\pi / 4} \frac{\mathrm{d} x}{\sin 2 x\left(\tan ^{5} x+\cot ^{5} x\right)}$ equals:

**Options:**

- **(A)** $\frac{1}{20} \tan ^{-1}\left(\frac{1}{9 \sqrt{3}}\right)$
- **(B)** $\frac{1}{10}\left(\frac{\pi}{4}-\tan ^{-1}\left(\frac{1}{9 \sqrt{3}}\right)\right)$
- **(C)** $\frac{\pi}{40}$
- **(D)** $\frac{1}{5}\left(\frac{\pi}{4}-\tan ^{-1}\left(\frac{1}{3 \sqrt{3}}\right)\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{10}\left(\frac{\pi}{4}-\tan ^{-1}\left(\frac{1}{9 \sqrt{3}}\right)\right)$**

**Detailed Solution:**

$\mathrm{I}=\int_{\frac{\pi}{6}}^{\frac{\pi}{4}} \frac{d x}{\sin 2 x\left(\tan ^{5} x+\cot ^{5} x\right)}$

$\begin{array}{l}

=\int_{\frac{\pi}{6}}^{\frac{\pi}{4}} \frac{\tan ^{5} x \cdot \sec ^{2} x}{2 \frac{\sin x}{\cos x}\left(\left(\tan ^{5} x\right)^{2}+1\right)} \\

=\frac{1}{2} \int_{\frac{\pi}{6}}^{\frac{\pi}{4} \tan ^{4} x \cdot \sec ^{2} x}{\left(\tan ^{5} x\right)^{2}+1} d x

\end{array}$

Let $\tan ^{4} x=t$

$5 \tan ^{4} x \cdot \sec ^{2} x d x=d t$

When $x \rightarrow \frac{\pi}{4}$ then $t \rightarrow 1$

and $x \rightarrow \frac{\pi}{6}$ then $t \rightarrow\left(\frac{1}{\sqrt{3}}\right)^{5}$

$\begin{aligned}

\therefore \quad & \mathrm{I}=\frac{1}{10} \int_{\left(\frac{1}{\sqrt{3}}\right)^{5}}^{1} \frac{d t}{t^{2}+1} \\

&=\frac{1}{10}\left(\frac{\pi}{4}-\tan ^{-1}\left(\frac{1}{9 \sqrt{3}}\right)\right)

\end{aligned}$

</details>

---

### Q36. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mrow><mrow><mi>&#960;</mi></mrow><mo>/</mo><mrow><mn>3</mn></mrow></mrow></mrow></munderover><mrow><mfrac><mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></mrow><mrow><msqrt><mn>2</mn><mi>k</mi><mtext>&#8201;</mtext><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt></mrow></mfrac></mrow></mrow><mi>d</mi><mi>&#952;</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>,</mo><mi>&#160;</mi><mo>(</mo><mi>k</mi><mo>&#62;</mo><mn>0</mn><mo>)</mo></math> , then the value of <math><mi>k</mi></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mn>1</mn></math>
- **(C)** <math><mn>2</mn></math>
- **(D)** <math><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>2</mn></math>**

**Detailed Solution:**

<math><mrow><msubsup><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mrow><mrow><mi>π</mi></mrow><mo>/</mo><mrow><mn>3</mn></mrow></mrow></mrow></msubsup><mrow><mfrac><mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><msqrt><mn>2</mn><mi>k</mi><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></mrow></math>  

 <math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn><mi>k</mi></msqrt></mrow></mfrac><mi> </mi><mrow><msubsup><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mrow><mrow><mi>π</mi></mrow><mo>/</mo><mrow><mn>3</mn></mrow></mrow></mrow></msubsup><mrow><mfrac><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><msqrt><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></mrow></math>  

Put  <math><mi>t</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math> 

 <math><mi>d</mi><mi>t</mi><mo>=</mo><mi> </mi><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mi> </mi><mi>d</mi><mi>x</mi><mo>,</mo></mrow></mrow></math>  also  <math><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>t</mi><mo>=</mo><mn>1</mn><mo>;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mi> </mi><mi>t</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> 

 <math><mo>∴</mo><mi> </mi><mi> </mi><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn><mi>k</mi></msqrt></mrow></mfrac><mi> </mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>1</mn></mrow><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></munderover><mrow><mfrac><mrow><mo>-</mo><mi>d</mi><mi>t</mi></mrow><mrow><msqrt><mi>t</mi></msqrt></mrow></mfrac></mrow></mrow></math>  

 <math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn><mi>k</mi></msqrt></mrow></mfrac><msub><mrow><mrow><munderover><mo stretchy="false">∫</mo><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow><mrow><mn>1</mn></mrow></munderover><mrow><msup><mrow><mi>t</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi> </mi></mrow></msup><mi>d</mi><mi>t</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn><mi>k</mi></msqrt></mrow></mfrac><mo>×</mo><mn>2</mn><mi> </mi><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mi>t</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></mrow></mfenced></mrow><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow><mrow><mn>1</mn></mrow></msubsup></mrow></mrow></mrow><mrow><mi> </mi></mrow></msub></math>  

 <math><mo>=</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt></mrow><mrow><msqrt><mi>k</mi></msqrt><mi> </mi></mrow></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mi>k</mi></msqrt></mrow></mfrac></math>  

Given  <math><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mi>k</mi></msqrt></mrow></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math> 

 <math><mo>∴</mo><mi>k</mi><mo>=</mo><mn>2</mn></math>

</details>

---

### Q37. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `3`

If $I_1=\int_0^1 e^{-x} \cos ^2 x d x ; I_2=\int_0^1 e^{-x^2} \cos ^2 x d x$ and $I_3=\int_0^1 e^{-x^3} d x$; then

**Options:**

- **(A)** $I_2>I_3>I_1$
- **(B)** $I_3>I_1>I_2$
- **(C)** $I_2>I_1>I_3$
- **(D)** $I_3>I_2>I_1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $I_3>I_2>I_1$**

**Detailed Solution:**

Given:
$$
\begin{aligned}
&I_1=\int_0^1 e^{-x} \cos ^2 x d x \\
&I_2=\int_0^1 e^{-x^2} \cos ^2 x d x \text { and } \\
&I_3=\int_0^1 e^{-x^3} d x \\
&\text { For } x \in(0,1) \\
&\Rightarrow x>x^2 \text { or }-x < -x^2 \\
&\text { and } x^2>x^3 \text { or }-x^2 < -x^3 \\
&\therefore e^{-x^2} < e^{-x^3} \text { and } e^{-x} < e^{-x^2} \\
&\Rightarrow e^{-x} < e^{-x^2} < e^{-x^3} \\
&\Rightarrow e^{-x^3}>e^{-x^2}>e^{-x} \\
&\Rightarrow I_3>I_2>I_1
\end{aligned}
$$

</details>

---

### Q38. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `1`

The value of integral $\int_{\frac{\pi}{4}}^{\frac{3 \pi}{4}} \frac{x}{1+\sin x} d x$ is

**Options:**

- **(A)** $\frac{\pi}{2}(\sqrt{2}+1)$
- **(B)** $\pi(\sqrt{2}-1)$
- **(C)** $2 \pi(\sqrt{2}-1)$
- **(D)** $\pi \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{2}(\sqrt{2}+1)$**

**Detailed Solution:**

Let $I=\int_{\frac{\pi}{4}}^{\frac{3 \pi}{4}} \frac{x}{1+\sin x} d x$ also let $K=\frac{x}{1+\sin x}$
Multiplying numerator and denominator by $(1-\sin x)$, we get;
$$
\begin{aligned}
K &=\frac{x(1-\sin x)}{1-(\sin x)^2}=\frac{x(1-\sin x)}{(\cos x)^2} \\
&=x(1-\sin x) \sec ^2 x \\
&=x \sec ^2 x-x \sin x \sec ^2 x=x \sec ^2 x-x \tan \\
x & \sec x
\end{aligned}
$$
Now, $I=\int_{\frac{\pi}{4}}^{\frac{3 \pi}{4}} x \sec ^2 x d x-\int_{\frac{\pi}{4}}^{\frac{3 \pi}{4}} x \sec x \tan x d x$
$$
=\left[x \tan x-\int \frac{d x}{d x} \tan x d x\right]_{\frac{\pi}{4}}^{\frac{3 \pi}{4}}-\left[x \sec x-\int \frac{d x}{d x} \sec x d x\right]_{\frac{\pi}{4}}^{\frac{3 \pi}{4}}
$$

$$
\begin{aligned}
&=[x \tan x-\ln |\sec x|]_{\frac{\pi}{4}}^{\frac{3 \pi}{4}} \\
&-[x \sec x-\ln |\sec x+\tan x|]_{\frac{\pi}{4}}^{\frac{3 \pi}{4}}+c \\
&\Rightarrow I=\left\{\left[\frac{3 \pi}{4} \tan \frac{3 \pi}{4}-\ln \left|\frac{3 \pi}{4}\right|\right.\right. \\
&\left.-\left[\frac{3 \pi}{4} \sec \frac{3 \pi}{4}-\ln \left|\sec \frac{3 \pi}{4}+\tan \frac{3 \pi}{4}\right|\right]\right\} \\
&-\left\{\left[\frac{\pi}{4} \tan \frac{\pi}{4}-\ln \left|\frac{\pi}{4}\right|\right.\right. \\
&\left.-\left[\frac{\pi}{4} \sec \frac{\pi}{4}-\ln \left|\sec \frac{\pi}{4}+\tan \frac{\pi}{4}\right|\right]\right\} \\
&=\frac{\pi}{2}(\sqrt{2}+1)
\end{aligned}
$$

</details>

---

### Q39. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If for $\mathrm{n} \geq 1, \mathrm{P}_{\mathrm{n}}=\int_1^{\mathrm{e}}\left(\log \mathrm{x}^{\mathrm{n}}\right) \mathrm{dx}$, then $\mathrm{P}_{10}-90 \mathrm{P}_8$ is equal to:

**Options:**

- **(A)** $-9$
- **(B)** $10 \mathrm{e}$
- **(C)** $-9 \mathrm{e}$
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-9 \mathrm{e}$**

**Detailed Solution:**

$\mathrm{P}_{\mathrm{n}}=\int_1^e(\log x)^n d x$ put $\log x=t$ then $x=e^t$ and $d x=e^t d t$
Also, when $x=1$, then $t=\log 1=0$ and when $x=e$, then $t=\log _e e=1$
$$
\begin{gathered}
\therefore \mathrm{P}_{\mathrm{n}}=\int_0^1 t^n \cdot e^t d t \\
\therefore \mathrm{P}_{10}=\int_0^1 t^{10} e^t d t \text { and } \mathrm{P}_8=\int_0^1 t^8 e^t d t \\
\text { Now, } \mathrm{P}_{10}-90 \mathrm{P}_8=\int_0^1 t^{10} e^t d t-90 \int_0^1 t^8 e^t d t \\
\mathrm{P}_{10}-90 \mathrm{P}_8 \\
\mathrm{P}_{10}-90 \mathrm{P}_8 \\
=\left[t^{10} e^t\right]_0^1-10 \int_0^1 t^9 e^t d t-90 \int_0^1 t^8 e^t d t \\
\mathrm{P}_{10}-90 \mathrm{P}_8= \\
e-10\left[t^9 \int_0^1 e^t d t-\int_0^1 \frac{d}{d t}\left(t^9\right) \int e^t d t\right]-90 \int_0^1 t^8 e^t d t
\end{gathered}
$$

$$
\begin{gathered}
\mathrm{P}_{10}-90 \mathrm{P}_8=e-10\left[e-9 \int_0^1 t^8 e^t d t\right]-90 \int_0^1 t^8 e^t d t \\
\mathrm{P}_{10}-90 \mathrm{P}_8=e-10 e+90 \int t^8 e^t d t-90 \int_0^1 t^8 e^t d t \\
\therefore P_{10}-90 P_8=-9 e
\end{gathered}
$$

</details>

---

### Q40. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

For $0 \leq x \leq \frac{\pi}{2}$, the value of
$$
\int_0^{\sin ^2 x} \sin ^{-1}(\sqrt{t}) d t+\int_0^{\cos ^2 x} \cos ^{-1}(\sqrt{t}) d t \text { equals : }
$$

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** 0
- **(C)** 1
- **(D)** $-\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{4}$**

**Detailed Solution:**

Consider
$$
\int_0^{\sin ^2 x} \sin ^{-1}(\sqrt{t}) d t+\int_0^{\cos ^2 x} \cos ^{-1}(\sqrt{t}) d t
$$
Let $\mathrm{I}=f(x)$ after integrating and putting the limits.
$$
\begin{aligned}
&f^{\prime}(x)=\sin ^{-1} \sqrt{\sin ^2 x}(2 \sin x \cos x)-0 \\
&\quad+\cos ^{-1} \sqrt{\cos ^2 x}(-2 \cos x \sin x)-0 \\
&\therefore f^{\prime}(x)=0 \Rightarrow f(x)=\mathrm{C} \quad \text { (constant) }
\end{aligned}
$$
Now, we find $f(x)$ at $x=\frac{\pi}{4}$
$$
\begin{aligned}
\therefore \mathrm{I} &=\int_0^{1 / 2} \sin ^{-1} \sqrt{t} d t+\int_0^{1 / 2} \cos ^{-1} \sqrt{t} d t \\
&=\int_0^{1 / 2}\left(\sin ^{-1} \sqrt{t}+\cos ^{-1} \sqrt{t}\right) d t \\
&=\int_0^{1 / 2} \frac{\pi}{2} d t=\frac{\pi}{4}=\mathrm{C} \\
\therefore \quad f(x)=\frac{\pi}{4} \\
\therefore \text { Required integration }=\frac{\pi}{4}
\end{aligned}
$$

</details>

---

### Q41. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `3`

If $f(x)=\frac{e^x}{1+e^x}, l_1=\int_{f(-a)}^{f(a)} x g\{x(1-x)\} d x$ and $I_2=\int_{f(-a)}^{f(a)} g\{x(1-x)\} d x$ then the value of $\frac{l_2}{l_1}$ is

**Options:**

- **(A)** 2
- **(B)** $-3$
- **(C)** $-1$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

$f(-a)+f(a)=1$
$I_1=\int_{f(-a)}^{f(a)} x g\{x(1-x)\} d x=\int_{f(-a)}^{f(a)}(1-x) g\{x(1-x)\} d x \quad\left(\because \int_a^b f(x) d x=\int_a^b f(a+b-x) d x\right)$
$2 I_1=\int_{f(-a)}^{f(a)} g\{x(1-x)\} d x=I_2 \Rightarrow I_2 / I_1=2$.

</details>

---

### Q42. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

If $\int_0^\pi x f(\sin x) d x=A \int_0^{\pi / 2} f(\sin x) d x$, then $A$ is

**Options:**

- **(A)** 0
- **(B)** $\pi$
- **(C)** $\frac{\pi}{4}$
- **(D)** $2 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\pi$**

**Detailed Solution:**

Let $I=\int_0^\pi x f(\sin x) d x=\int_0^\pi(\pi-x) f(\sin x) d x=\pi \int_0^\pi f(\sin x) d x-I \quad(\sin c e f(2 a-x)=f(x))$
$\Rightarrow I=\pi \int_0^{\pi / 2} f(\sin x) d x \Rightarrow A=\pi$

</details>

---

