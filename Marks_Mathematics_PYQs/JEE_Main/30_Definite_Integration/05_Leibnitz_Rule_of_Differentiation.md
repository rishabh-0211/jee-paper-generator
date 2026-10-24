# JEE Main Mathematics - Definite Integration

## Topic 5: Leibnitz Rule of Differentiation

**Total Questions:** 46

---

### Q1. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be such that $f(xy) = f(x)f(y)$, for all $x, y \in \mathbb{R}$ and $f(0) \neq 0$. Let $g: [1, \infty) \rightarrow \mathbb{R}$ be a differentiable function such that
$x^2 g(x) = \int\limits_1^x (t^2 f(t) - tg(t))\,dt$.
Then $g(2)$ is equal to :

**Options:**

- **(A)** $\dfrac{13}{8}$
- **(B)** $\dfrac{11}{16}$
- **(C)** $\dfrac{15}{32}$
- **(D)** $\dfrac{17}{64}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{15}{32}$**

**Detailed Solution:**

Given $f(xy) = f(x)f(y)$ for all $x, y \in \mathbb{R}$ and $f(0) \neq 0$.

Substituting $y = 0$, we get $f(0) = f(x)f(0)$.

Since $f(0) \neq 0$, dividing by $f(0)$ gives $f(x) = 1$ for all $x \in \mathbb{R}$.

The given integral equation is:

$x^2 g(x) = \int\limits_1^x (t^2 f(t) - tg(t))\,dt$

Substituting $f(t) = 1$:

$x^2 g(x) = \int\limits_1^x (t^2 - tg(t))\,dt$

Differentiating both sides with respect to $x$ using Leibniz's rule:

$2x g(x) + x^2 g'(x) = x^2 - xg(x)$

$x^2 g'(x) + 3xg(x) = x^2$

Dividing by $x$ (since $x \ge 1$):

$x g'(x) + 3g(x) = x$

$g'(x) + \dfrac{3}{x}g(x) = 1$

This is a linear differential equation. The integrating factor is:

$\text{IF} = e^{\int \dfrac{3}{x}\,dx} = e^{3\ln x} = x^3$

Multiplying the differential equation by $x^3$:

$x^3 g'(x) + 3x^2 g(x) = x^3$

$\dfrac{d}{dx}(x^3 g(x)) = x^3$

Integrating both sides with respect to $x$:

$x^3 g(x) = \dfrac{x^4}{4} + C$

From the integral equation, substituting $x = 1$ gives $1^2 g(1) = \int\limits_1^1 (t^2 - tg(t))\,dt = 0$, so $g(1) = 0$.

Substituting $x = 1$ and $g(1) = 0$ into the integrated equation:

$1^3(0) = \dfrac{1^4}{4} + C \Rightarrow C = -\dfrac{1}{4}$

Thus, the function $g(x)$ is given by:

$x^3 g(x) = \dfrac{x^4 - 1}{4}$

$g(x) = \dfrac{x^4 - 1}{4x^3}$

Substituting $x = 2$:

$g(2) = \dfrac{2^4 - 1}{4(2^3)} = \dfrac{16 - 1}{32} = \dfrac{15}{32}$

Answer: $\dfrac{15}{32}$

</details>

---

### Q2. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f: [1, \infty) \rightarrow \mathbf{R}$ be a differentiable function defined as $f(x) = \int_1^x f(t)\,dt + (1-x)(\log_e x - 1) + e$. Then the value of $f(f(1))$ is :

**Options:**

- **(A)** $(1 + e^e)$
- **(B)** $(1 + e)$
- **(C)** $(1 + e + e^e)$
- **(D)** $1 + 2e$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(1 + e^e)$**

**Detailed Solution:**

Given $f(x) = \int_1^x f(t)\,dt + (1-x)(\log_e x - 1) + e$

Substituting $x = 1$ in the given equation:

$f(1) = \int_1^1 f(t)\,dt + (1-1)(\log_e 1 - 1) + e$

$f(1) = 0 + 0 + e = e$

Differentiating the given equation with respect to $x$ using the Leibniz rule:

$f'(x) = f(x) + \dfrac{d}{dx}[(1-x)(\log_e x - 1)]$

$f'(x) = f(x) + (-1)(\log_e x - 1) + (1-x)\left(\dfrac{1}{x}\right)$

$f'(x) = f(x) - \log_e x + 1 + \dfrac{1}{x} - 1$

$f'(x) - f(x) = \dfrac{1}{x} - \log_e x$

This is a linear differential equation of the form $\dfrac{dy}{dx} + Py = Q$, where $P = -1$ and $Q = \dfrac{1}{x} - \log_e x$.

Integrating Factor (IF) $= e^{\int -1 \,dx} = e^{-x}$

Multiplying the differential equation by the IF:

$e^{-x} f'(x) - e^{-x} f(x) = e^{-x} \left(\dfrac{1}{x} - \log_e x\right)$

$\dfrac{d}{dx}[e^{-x} f(x)] = e^{-x} \dfrac{1}{x} - e^{-x} \log_e x$

Notice that $\dfrac{d}{dx}[e^{-x} \log_e x] = -e^{-x} \log_e x + e^{-x} \dfrac{1}{x}$.

Thus, $\dfrac{d}{dx}[e^{-x} f(x)] = \dfrac{d}{dx}[e^{-x} \log_e x]$

Integrating both sides with respect to $x$:

$e^{-x} f(x) = e^{-x} \log_e x + C$

$f(x) = \log_e x + C e^x$

Using the initial condition $f(1) = e$:

$e = \log_e 1 + C e^1$

$e = 0 + C e \Rightarrow C = 1$

Therefore, the function is $f(x) = \log_e x + e^x$.

We need to find $f(f(1))$:

Since $f(1) = e$, we evaluate $f(e)$:

$f(e) = \log_e e + e^e = 1 + e^e$

Answer: $(1 + e^e)$

</details>

---

### Q3. JEE Main 2026 (04 April Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $f$ be a twice differentiable function such that $f(x)=\int_{0}^{x}\tan(t-x)dt-\int_{0}^{x}f(t)\tan t\,dt$, $x \in \left(-\dfrac{\pi}{2},\dfrac{\pi}{2}\right)$. Then $f''\left(\dfrac{\pi}{6}\right)+12f'\left(-\dfrac{\pi}{6}\right)+f\left(\dfrac{\pi}{6}\right)$ is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

Given the function:

$f(x) = \int_{0}^{x} \tan(t-x) dt - \int_{0}^{x} f(t) \tan t \, dt$

First, we simplify the first integral. Let $u = x - t$, then $du = -dt$. When $t = 0$, $u = x$; when $t = x$, $u = 0$.

$\int_{0}^{x} \tan(t-x) dt = \int_{x}^{0} \tan(-u) (-du) = \int_{x}^{0} \tan u \, du = -\int_{0}^{x} \tan u \, du = -[\ln(\sec u)]_{0}^{x} = -\ln(\sec x) = \ln(\cos x)$

So, the equation becomes:

$f(x) = \ln(\cos x) - \int_{0}^{x} f(t) \tan t \, dt$

Differentiating both sides with respect to $x$ using the Leibniz rule:

$f'(x) = \dfrac{-\sin x}{\cos x} - f(x) \tan x$

$f'(x) + f(x) \tan x = -\tan x$

This is a linear first-order differential equation. The integrating factor (IF) is:

$\text{IF} = e^{\int \tan x \, dx} = e^{\ln(\sec x)} = \sec x$

Multiplying the differential equation by $\sec x$:

$f'(x) \sec x + f(x) \sec x \tan x = -\sec x \tan x$

$\dfrac{d}{dx} (f(x) \sec x) = -\sec x \tan x$

Integrating both sides with respect to $x$:

$f(x) \sec x = -\sec x + C$

To find $C$, we use the initial condition. From $f(x) = \ln(\cos x) - \int_{0}^{x} f(t) \tan t \, dt$, substituting $x = 0$ gives $f(0) = \ln(1) - 0 = 0$.

$0 \cdot \sec 0 = -\sec 0 + C \Rightarrow 0 = -1 + C \Rightarrow C = 1$

Thus, $f(x) \sec x = 1 - \sec x$

$f(x) = \cos x - 1$

Now, we find the required derivatives:

$f'(x) = -\sin x$

$f''(x) = -\cos x$

Evaluating these at the given points:

$f\left(\dfrac{\pi}{6}\right) = \cos\left(\dfrac{\pi}{6}\right) - 1 = \dfrac{\sqrt{3}}{2} - 1$

$f'\left(-\dfrac{\pi}{6}\right) = -\sin\left(-\dfrac{\pi}{6}\right) = \sin\left(\dfrac{\pi}{6}\right) = \dfrac{1}{2}$

$f''\left(\dfrac{\pi}{6}\right) = -\cos\left(\dfrac{\pi}{6}\right) = -\dfrac{\sqrt{3}}{2}$

Finally, substituting these values into the required expression:

$f''\left(\dfrac{\pi}{6}\right) + 12f'\left(-\dfrac{\pi}{6}\right) + f\left(\dfrac{\pi}{6}\right) = -\dfrac{\sqrt{3}}{2} + 12\left(\dfrac{1}{2}\right) + \left(\dfrac{\sqrt{3}}{2} - 1\right)$

$= -\dfrac{\sqrt{3}}{2} + 6 + \dfrac{\sqrt{3}}{2} - 1 = 5$

Answer: $5$

</details>

---

### Q4. JEE Main 2026 (24 January Shift 2)

*Type:* `numerical` | *Level:* `3`

If $f(x)$ satisfies the relation $f(x)=e^{x}+\int_{0}^{1}\left(y+x e^{x}\right) f(y) d y$, then $e+f(0)$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

$f(x) = e^x + \displaystyle\int_0^1 (y + xe^x)f(y)\, dy$

Splitting the integral:
$f(x) = e^x + \displaystyle\int_0^1 yf(y)\, dy + xe^x \int_0^1 f(y)\, dy$

Let $A = \displaystyle\int_0^1 yf(y)\, dy$ and $B = \displaystyle\int_0^1 f(y)\, dy$

$\Rightarrow f(x) = (1 + Bx)e^x + A$

At $x = 0$: $f(0) = 1 + A$

Now compute $B$ using the expression for $f(y)$:
$B = \displaystyle\int_0^1 \left[(1 + By)e^y + A\right] dy$
$B = \displaystyle\int_0^1 e^y\, dy + B\int_0^1 ye^y\, dy + \int_0^1 A\, dy$

Evaluating each integral:
$\displaystyle\int_0^1 e^y\, dy = e - 1$
$\displaystyle\int_0^1 ye^y\, dy = [ye^y]_0^1 - \int_0^1 e^y\, dy = e - (e - 1) = 1$
$\displaystyle\int_0^1 A\, dy = A$

$\Rightarrow B = (e - 1) + B(1) + A$
$\Rightarrow 0 = e - 1 + A$
$\Rightarrow A = 1 - e$

$f(0) = 1 + A = 1 + (1 - e) = 2 - e$

$e + f(0) = e + (2 - e) = 2$

Answer: $2$

</details>

---

### Q5. JEE Main 2026 (24 January Shift 1)

*Type:* `numerical` | *Level:* `3`

Let a differentiable function $f$ satisfy the equation $\int_{0}^{36} f\left(\frac{t x}{36}\right) d t=4 \alpha f(x)$. If $y=f(x)$ is a standard parabola passing through the points $(2,1)$ and $(-4, \beta)$, then $\beta^{\alpha}$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **64**

**Detailed Solution:**

From $\int_0^{36} f\left(\frac{tx}{36}\right) dt = 4\alpha f(x)$, substitute $u = \frac{tx}{36}$ to get $\frac{36}{x} \int_0^x f(u) du = 4\alpha f(x)$.
Differentiating: $f(x) = \frac{\alpha}{9}[f(x) + xf'(x)]$, which simplifies to $(9-\alpha)f(x) = \alpha x f'(x)$.
This gives $\frac{f'(x)}{f(x)} = \frac{9-\alpha}{\alpha x}$, integrating to $f(x) = Kx^{\frac{9-\alpha}{\alpha}}$.
For f to be a standard parabola: $\frac{9-\alpha}{\alpha} = 2 \Rightarrow \alpha = 3$.
Thus $f(x) = Kx^2$. Using point $(2,1)$: $K = \frac{1}{4}$, so $f(x) = \frac{x^2}{4}$.
At $(-4, \beta)$: $\beta = \frac{16}{4} = 4$.
Therefore $\beta^\alpha = 4^3 = 64$

</details>

---

### Q6. JEE Main 2026 (23 January Shift 2)

*Type:* `numerical` | *Level:* `3`

The number of elements in the 
 set $\mathrm{S}=\left\{x: x \in[0,100]\right.$ and $\left.\int_{0}^{x} t^{2} \sin (x-t) \mathrm{d} t=x^{2}\right\}$ is $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

Using $u = x - t$: $\int_0^x t^2 \sin(x-t)\,dt = \int_0^x (x-u)^2 \sin u\,du$.
Expanding and integrating term by term:
$= x^2(1-\cos x) - 2x(-x\cos x + \sin x) + (-x^2\cos x + 2x\sin x + 2\cos x - 2)$
$= x^2 + 2\cos x - 2$.
Setting equal to $x^2$: $2\cos x - 2 = 0 \Rightarrow \cos x = 1 \Rightarrow x = 2n\pi$.
In $[0, 100]$: $2n\pi \le 100 \Rightarrow n \le \frac{50}{\pi} \approx 15.9$.
So $n = 0, 1, 2, \ldots, 15$, giving $16$ elements.

</details>

---

### Q7. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $f(x)=\int_0^t t\left(t^2-9 t+20\right) d t, 1 \leq x \leq 5$. If the range of $f$ is $[\alpha, \beta]$, then $4(\alpha+\beta)$ equals :

**Options:**

- **(A)** 253
- **(B)** 154
- **(C)** 125
- **(D)** 157

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 157**

**Detailed Solution:**

$f^{\prime}(x)=x\left(x^2-9 x+20\right), x \in(1,5)$
$=(x-4) x(x-5)$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/01raq0kRkylldagtWMIWmN9zaggG3i7-371jlf30A_Y.original.fullsize.png">

$\begin{aligned} & \Rightarrow f^{\prime}(x)>0 \forall x \in(1,4) \\ & \Rightarrow f^{\prime}(x) < 0 \forall x \in(4,5) \\ & \Rightarrow f(x) \text { increasing in }(1,4) \\ & \quad f(x) \text { decreasing in }(4,5) \\ & \Rightarrow \text { critical points to check: }\end{aligned}$
$\begin{aligned} & x=1,4,5 \\ & f(x)=\int_0^x\left(t^3-9 t^2+20 t\right) d t \\ & =\frac{t^4}{4}-3 t^3+\left.10 t^2\right|_0 ^x=\frac{x^4}{4}-3 x^3+10 x^2 \\ & f(1)=\frac{1}{4}-3+10=\frac{29}{4} \\ & f(4)=4^3-3.4^3+10.4^2=-2.4^3+10.4^2=32 \\ & f(5)=\frac{5^4}{4}-3.5^3+10.25=\frac{5^4}{4}-125=\frac{125}{4}\end{aligned}$
$\begin{aligned} & \text { Range } \Rightarrow\left[\frac{29}{4}, 32\right] \Rightarrow 4(\alpha+\beta)=128+29 \\ & =157\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let \(f:(0, \infty) \rightarrow \mathbf{R}\) be a twice differentiable function. If for some \(\mathrm{a} \neq 0, \int_0^1 f(\lambda x) \mathrm{d} \lambda=\mathrm{a} f(x), f(1)=1\) and \(f(16)=\frac{1}{8}\), then \(16-f^{\prime}\left(\frac{1}{16}\right)\) is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **112**

**Detailed Solution:**

Given, $\int_0^1 f(\lambda x) d \lambda=a f(x)$
Let $\lambda x=u$
$d \lambda=\frac{1}{x} d u$
$\therefore$ From (1) $\frac{1}{x} \int_0^x f(u) d u=a f(x)$
$\Rightarrow \int_0^x f(u) d u=\operatorname{axf}(x)$
Differentiate both sides
$\begin{aligned}
& f(x)=a\left(x f^{\prime}(x)+f(x)\right) \\
& \Rightarrow \quad f(x)=a x f^{\prime}(x)+a f(x) \\
& \Rightarrow \quad(1-a) f(x)=a x f^{\prime}(x) \\
& \Rightarrow \quad \frac{f^{\prime}(x)}{f(x)}=\frac{(1-a)}{a} \cdot \frac{1}{x}
\end{aligned}$
Integrate both side w.r.t. ( $x$ )
$\begin{aligned}
& \Rightarrow \quad \int \frac{f^{\prime}(x)}{f(x)} d x=\frac{(1-a)}{a} \int \frac{1}{x} d x \\
& \Rightarrow \ln f(x)=\left(\frac{1-a}{a}\right) \ln x+c
\end{aligned}$
Now at $x=1 f(1)=1$
$\Rightarrow c=0$
Also given $f(16)=\frac{1}{8}$
$\begin{aligned}
& \therefore \quad \frac{1}{8}=(16)^{\frac{1-a}{a}} \\
& \Rightarrow \quad 2^{-3}=2^{\frac{4-4 a}{a}} \\
& \Rightarrow \quad-3=\frac{4-4 a}{a} \\
& \Rightarrow-3 a=4-4 a \\
& \Rightarrow a=4 \\
& \therefore \quad f(x)=x^{-3 / 4} \\
& f(x)=\frac{-3}{4} x^{-\frac{7}{4}}
\end{aligned}$
$\begin{aligned} & \text { Put } x=\frac{1}{16} \\ & f^{\prime}\left(\frac{1}{16}\right)=\frac{-3}{4}\left(\frac{1}{16}\right)^{-7 / 4}=\frac{-3}{4} \cdot 2^{-4 x\left(\frac{-7}{4}\right)}=-96 \\ & \therefore \quad 16-f^{\prime}\left(\frac{1}{16}\right) \Rightarrow 16-(-96)=112\end{aligned}$

</details>

---

### Q9. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f$ be a real valued continuous function defined on the positive real axis such that $g(x)=\int_0^x \mathrm{t} f(\mathrm{t}) \mathrm{dt}$. If $\mathrm{g}\left(x^3\right)=x^6+x^7$, then value of $\sum_{r=1}^{15} f\left(\mathrm{r}^3\right)$ is :

**Options:**

- **(A)** $270$
- **(B)** $340$
- **(C)** $320$
- **(D)** $310$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $310$**

**Detailed Solution:**

$g(x)=x^2+x^{7 / 3}$
$\begin{aligned} & g^{\prime}(x)=2 x+\frac{7}{3} x^{4 / 3} \\ & f(x)=\frac{g^{\prime}(x)}{x} \\ & f(x)=2+\frac{7}{3} x^{1 / 3} \\ & f\left(r^3\right)=2+\frac{7}{3} r \\ & \sum_{r=1}^{15}\left(2+\frac{7}{3} r\right)=2(15)+\frac{7}{3}\left(\frac{15(16)}{2}\right)\end{aligned}$
$=310$

</details>

---

### Q10. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let for some function $\mathrm{y}=f(x), \int_0^x t f(t) d t=x^2 f(x), x\gt0$ and $f(2)=3$. Then $f(6)$ is equal to

**Options:**

- **(A)** 1
- **(B)** 3
- **(C)** 6
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

$\begin{aligned} & \int_0^x t f(t) d t=x^2 f(x) \\ & \Rightarrow \quad x f(x)=2 x f(x)+x^2 f^{\prime}(x) \\ & \Rightarrow x^2 \cdot f^{\prime}(x)=-x f(x) \\ & \Rightarrow \quad \frac{f^{\prime}(x)}{f(x)}=-\frac{1}{x} \\ & \\ & \quad \int \frac{f^{\prime}(x)}{f(x) d x}=-\int \frac{1}{x} d x \\ & \Rightarrow \quad \ln f(x)=-\ln x+C \\ & \\ & \quad f(2)=3 \Rightarrow \ln 3=-\ln 2+C \\ & \quad C=\ln 6 \\ & \Rightarrow \quad f(x)=\frac{6}{x} \Rightarrow f(6)=1\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $f(x)=\int_0^{x^2} \frac{\mathrm{t}^2-8 \mathrm{t}+15}{\mathrm{e}^{\mathrm{t}}} \mathrm{dt}, x \in \mathbf{R}$. Then the numbers of local maximum and local minimum points of $f$, respectively, are :

**Options:**

- **(A)** 2 and 3
- **(B)** 2 and 2
- **(C)** 3 and 2
- **(D)** 1 and 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2 and 3**

**Detailed Solution:**

$\begin{aligned}
& f(x)=\int_0^{x^2} \frac{t^2-8 t+15}{e^t} d t, x \in R \\
& f^{\prime}(x)=\frac{x^4-8 x^2+15}{e^{x^2}}(2 x)=0 \\
& \Rightarrow \quad \frac{2 \times\left(x^2-5\right)\left(x^2-3\right)}{e^{x^2}}=0 \\
& \Rightarrow x(x+\sqrt{5})(x-\sqrt{5})(x+\sqrt{3})(x-\sqrt{3})=0
\end{aligned}$
By using wavy curve method
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/_r1Y1-55B6kBNWX7xC6js9Ku_ZaysaTZ0BbartEfY5I.original.fullsize.png">

Number of local maximum $=2$
Number of local minimum $=3$

</details>

---

### Q12. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\int_0^x \sqrt{1-\left(y^{\prime}(t)\right)^2} d t=\int_0^x y(t) d t, 0 \leq x \leq 3, y \geq 0, y(0)=0$. Then at $x=2, y^{\prime \prime}+y+1$ is equal to

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** $\sqrt{2}$
- **(D)** $1 / 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

$\begin{aligned} & \sqrt{1-\left(y^{\prime}(x)\right)^2}=y(x) \\ & 1-\left(\frac{d y}{d x}\right)^2=y^2 \\ & \left(\frac{d y}{d x}\right)^2=1-y^2\end{aligned}$
$\begin{aligned} & \frac{d y}{\sqrt{1-y^2}}=d x \text { OR } \frac{d y}{\sqrt{1-y^2}}=-d x \\ & \Rightarrow \sin ^{-1} y=x+c, \sin ^{-1} y=-x+c \\ & x=0, y=0 \Rightarrow c=0 \\ & \sin ^{-1} y=x, \text { as } y \geq 0 \\ & \sin x=y \\ & \Rightarrow \frac{d y}{d x}=\cos x \\ & \frac{d^2 y}{d x^2}=-\sin x \\ & \Rightarrow-\sin x+\sin x+1=1\end{aligned}$

</details>

---

### Q13. JEE Main 2024 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mi>∞</mi></mrow></mfenced><mo>→</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munderover><mo>∫</mo><mn>0</mn><mi>x</mi></munderover><mi>t</mi><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mo>=</mo><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>x</mi><mn>5</mn></msup><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>∑</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>12</mn></munderover><mi>f</mi><mfenced><msup><mi>r</mi><mn>2</mn></msup></mfenced></math> is equal to:

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **219**

**Detailed Solution:**

<p>Given: </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munderover><mo>∫</mo><mn>0</mn><mi>x</mi></munderover><mi>t</mi><mo>⋅</mo><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math></p><p>Now, applying Newton Leibnitz Theorem we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>F</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>⋅</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p> And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mo>=</mo><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>x</mi><mn>5</mn></msup></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>F</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><msup><mi>t</mi><mfrac><mn>5</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>F</mi><mo>'</mo></msup><mfenced><mi>t</mi></mfenced><mo>=</mo><mn>2</mn><mi>t</mi><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><msup><mi>t</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><msup><mi>F</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>⋅</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>t</mi><mo>⋅</mo><mi>f</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mn>2</mn><mi>t</mi><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><msup><mi>t</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mn>2</mn><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><msup><mi>t</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>12</mn></munderover><mi>f</mi><mfenced><msup><mi>r</mi><mn>2</mn></msup></mfenced><mo>=</mo><munderover><mo>∑</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>12</mn></munderover><mn>2</mn><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>12</mn></munderover><mi>f</mi><mfenced><msup><mi>r</mi><mn>2</mn></msup></mfenced><mo>=</mo><mn>24</mn><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mfrac><mrow><mn>12</mn><mfenced><mn>13</mn></mfenced></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>12</mn></munderover><mi>f</mi><mfenced><msup><mi>r</mi><mn>2</mn></msup></mfenced><mo>=</mo><mn>219</mn></math></p>

</details>

---

### Q14. JEE Main 2024 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced><mrow><mo>−</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>∞</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>S</mi><mo>→</mo><mi mathvariant="normal">ℝ</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munderover><mo>∫</mo><mrow><mo>−</mo><mn>1</mn></mrow><mi>x</mi></munderover><msup><mfenced><mrow><msup><mi>e</mi><mi>t</mi></msup><mo>−</mo><mn>1</mn></mrow></mfenced><mn>11</mn></msup><msup><mfenced><mrow><mn>2</mn><mi>t</mi><mo>−</mo><mn>1</mn></mrow></mfenced><mn>5</mn></msup><msup><mfenced><mrow><mi>t</mi><mo>−</mo><mn>2</mn></mrow></mfenced><mn>7</mn></msup><msup><mfenced><mrow><mi>t</mi><mo>−</mo><mn>3</mn></mrow></mfenced><mn>12</mn></msup><msup><mfenced><mrow><mn>2</mn><mi>t</mi><mo>−</mo><mn>10</mn></mrow></mfenced><mn>61</mn></msup><mi>d</mi><mi>t</mi></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo></math> Sum of square of the values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> attains local maxima on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>. and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo></math>Sum of the values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> attains local minima on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>. Then, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>q</mi></math> is ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **27**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munderover><mo>∫</mo><mrow><mo>−</mo><mn>1</mn></mrow><mi>x</mi></munderover><msup><mfenced><mrow><msup><mi>e</mi><mi>t</mi></msup><mo>−</mo><mn>1</mn></mrow></mfenced><mn>11</mn></msup><msup><mfenced><mrow><mn>2</mn><mi>t</mi><mo>−</mo><mn>1</mn></mrow></mfenced><mn>5</mn></msup><msup><mfenced><mrow><mi>t</mi><mo>−</mo><mn>2</mn></mrow></mfenced><mn>7</mn></msup><msup><mfenced><mrow><mi>t</mi><mo>−</mo><mn>3</mn></mrow></mfenced><mn>12</mn></msup><msup><mfenced><mrow><mn>2</mn><mi>t</mi><mo>−</mo><mn>10</mn></mrow></mfenced><mn>61</mn></msup><mi>d</mi><mi>t</mi></math></p><p>Now, differentiating the above integral using Newton Leibnitz's theorem, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>−</mo><mn>1</mn></mrow></mfenced><mn>11</mn></msup><msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfenced><mn>5</mn></msup><msup><mfenced><mrow><mi>x</mi><mo>−</mo><mn>2</mn></mrow></mfenced><mn>7</mn></msup><msup><mfenced><mrow><mi>x</mi><mo>−</mo><mn>3</mn></mrow></mfenced><mn>12</mn></msup><msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>−</mo><mn>10</mn></mrow></mfenced><mn>61</mn></msup></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/36428b14-0613-4c1d-b43b-4ba6bbc98c3e.png" style="width: 415px; height: 109px;"/></p><p>Now, from the above diagram using first derivative test we get,</p><p>Local minima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo> </mo><mi>x</mi><mo>=</mo><mn>5</mn></math> </p><p>Local maxima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>0</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>4</mn><mo>,</mo><mo> </mo><mi>q</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>5</mn><mo>=</mo><mfrac><mn>11</mn><mn>2</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>q</mi><mo>=</mo><mn>16</mn><mo>+</mo><mn>11</mn><mo>=</mo><mn>27</mn></math></p>

</details>

---

### Q15. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let f be a continuous function satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup></msubsup><mfenced><mrow><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>+</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced><mi>dx</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msup><mi mathvariant="normal">t</mi><mn>3</mn></msup><mo>,</mo><mo>&#8704;</mo><mi mathvariant="normal">t</mi><mo>&#62;</mo><mn>0</mn></math> . Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mn>4</mn></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mn>16</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi mathvariant="normal">&#960;</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>3</mn></msup><mn>16</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#960;</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>3</mn></msup><mn>16</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mn>16</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#960;</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>3</mn></msup><mn>16</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup></msubsup><mfenced><mrow><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>+</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced><mi>dx</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msup><mi mathvariant="normal">t</mi><mn>3</mn></msup><mo>,</mo><mo>&#8704;</mo><mi mathvariant="normal">t</mi><mo>&#62;</mo><mn>0</mn></math></p><p>According to Newton Leibnitz theorem we have<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mo>d</mo><mrow><mo>d</mo><mi mathvariant="normal">x</mi></mrow></mfrac><mfenced><mrow><msubsup><mo>&#8747;</mo><mrow><mi mathvariant="normal">u</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></mrow><mrow><mi mathvariant="normal">v</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></mrow></msubsup><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">t</mi></mfenced><mo>d</mo><mi mathvariant="normal">t</mi></mrow></mfenced><mo>=</mo><mi mathvariant="normal">f</mi><mfenced><mrow><mi mathvariant="normal">v</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></mrow></mfenced><mo>&#215;</mo><mi mathvariant="normal">v</mi><mo>'</mo><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>-</mo><mi mathvariant="normal">f</mi><mfenced><mrow><mi mathvariant="normal">u</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></mrow></mfenced><mo>&#215;</mo><mi mathvariant="normal">u</mi><mo>'</mo><mfenced><mi mathvariant="normal">x</mi></mfenced></math></p><p>Apply Newtons Leibnitz theorem in the given equation.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi mathvariant="normal">f</mi><mfenced><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup></mfenced><mo>+</mo><msup><mi mathvariant="normal">t</mi><mn>4</mn></msup></mrow></mfenced><mn>2</mn><mi mathvariant="normal">t</mi><mo>-</mo><mn>0</mn><mo>=</mo><mn>4</mn><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">f</mi><mfenced><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup></mfenced><mo>+</mo><msup><mi mathvariant="normal">t</mi><mn>4</mn></msup><mo>=</mo><mn>2</mn><mi mathvariant="normal">t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">f</mi><mfenced><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mfenced><mo>=</mo><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>4</mn></msup><mo>+</mo><mn>2</mn><mi mathvariant="normal">x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>=</mo><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msqrt><mi mathvariant="normal">x</mi></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">f</mi><mfenced><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mn>4</mn></mfrac></mfenced><mo>=</mo><mo>-</mo><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>4</mn></msup><msup><mn>4</mn><mn>2</mn></msup></mfrac><mo>+</mo><mn>2</mn><mo>&#215;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><msup><mi mathvariant="normal">&#960;</mi><mn>4</mn></msup></mrow><mn>16</mn></mfrac><mo>+</mo><mi mathvariant="normal">&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi mathvariant="normal">&#960;</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>3</mn></msup><mn>16</mn></mfrac></mrow></mfenced></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q16. JEE Main 2023 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><msqrt><mi>x</mi></msqrt></mfrac><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mi>x</mi></msubsup><mfenced><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>t</mi><mo>-</mo><mn>3</mn><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mfenced><mi>d</mi><mi>t</mi><mo>,</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mrow><mn>6</mn><mo>+</mo><msqrt><mi>&#960;</mi></msqrt></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mrow><mn>6</mn><mo>+</mo><msqrt><mi>&#960;</mi></msqrt></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><msqrt><mi>&#960;</mi></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mrow><mn>6</mn><mo>-</mo><msqrt><mi>&#960;</mi></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mrow><mn>6</mn><mo>+</mo><msqrt><mi>&#960;</mi></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><msqrt><mi>x</mi></msqrt></mfrac><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow><mi>x</mi></msubsup><mfenced><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>t</mi><mo>-</mo><mn>3</mn><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p>Differentiate both sides w.r.t. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfrac><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow><mi>x</mi></msubsup><mfenced><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>t</mi><mo>-</mo><mn>3</mn><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mfenced><mi>d</mi><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><msqrt><mi>x</mi></msqrt></mfrac><mfenced><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>x</mi><mo>-</mo><mn>3</mn><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mo>(</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>)</mo><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><msup><mfenced><mstyle displaystyle="true"><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mstyle></mfenced><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfrac><mo>&#215;</mo><mn>0</mn><mo>+</mo><msqrt><mfrac><mn>4</mn><mi mathvariant="normal">&#960;</mi></mfrac></msqrt><mfenced><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>&#215;</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>-</mo><mn>3</mn><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mo>(</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>)</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></msqrt><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mo>(</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>)</mo><mo>+</mo><mn>3</mn><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mo>(</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>)</mo><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mfenced><mrow><mn>3</mn><mo>+</mo><msqrt><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msqrt></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>8</mn><mrow><mn>6</mn><mo>+</mo><msqrt><mi>&#960;</mi></msqrt></mrow></mfrac></math></p>

</details>

---

### Q17. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let a differentiable function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> satisfy <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><msubsup><mo>&#8747;</mo><mn>3</mn><mi>x</mi></msubsup><mfrac><mrow><mi>f</mi><mfenced><mi>t</mi></mfenced></mrow><mi>t</mi></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>,</mo><mi>x</mi><mo>&#8805;</mo><mn>3</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>f</mi><mfenced><mn>8</mn></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><msubsup><mo>&#8747;</mo><mn>3</mn><mi>x</mi></msubsup><mfrac><mrow><mi>f</mi><mfenced><mi>t</mi></mfenced></mrow><mi>t</mi></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mi>x</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mi>y</mi></mstyle><mstyle displaystyle="true"><mi>x</mi></mstyle></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mstyle></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>ln</mi><mfenced close="|" open="|"><mi>x</mi></mfenced></mrow></msup><mo>=</mo><mi>x</mi></math></p><p>Hence, solution is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mi>x</mi><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>1</mn></mrow><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfenced><mrow><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>-</mo><mfrac><mn>1</mn><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>-</mo><mn>2</mn><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>-</mo><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><mi>C</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>2</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>-</mo><mn>2</mn><mo>+</mo><mi>C</mi><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mfrac><mn>16</mn><mn>3</mn></mfrac></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>-</mo><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><mfrac><mn>16</mn><mn>3</mn></mfrac></math></p><p>So, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>8</mn></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>f</mi><mfenced><mn>8</mn></mfenced><mo>=</mo><mfrac><mn>27</mn><mn>3</mn></mfrac><mo>-</mo><mn>3</mn><mo>+</mo><mfrac><mn>16</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>8</mn></mfenced><mo>=</mo><mfrac><mn>34</mn><mrow><mn>3</mn><mo>&#215;</mo><mn>8</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>12</mn><mi>f</mi><mfenced><mn>8</mn></mfenced><mo>=</mo><mn>17</mn></math></p>

</details>

---

### Q18. JEE Main 2023 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mn>48</mn><msup><mi>x</mi><mn>4</mn></msup></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfrac><msup><mi>t</mi><mn>3</mn></msup><mrow><msup><mi>t</mi><mn>6</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>t</mi></math>  is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="}" open="{"><mfrac><mrow><mn>48</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfenced><mstyle displaystyle="true"><mfrac><msup><mi>t</mi><mn>3</mn></msup><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>6</mn></msup></mrow></mfrac></mstyle></mfenced><mi>d</mi><mi>t</mi></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac></mfenced><mo>&#8594;</mo><mfrac><mn>0</mn><mn>0</mn></mfrac></math></p><p>Applying L&#39;hospital rule, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="}" open="{"><mfrac><mfenced><mstyle displaystyle="true"><mfrac><mrow><mn>48</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></mrow></mfrac></mstyle></mfenced><mrow><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mn>12</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><mn>12</mn></math></p>

</details>

---

### Q19. JEE Main 2023 (24 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> be a differentiable function defined on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><msqrt><mn>1</mn><mo>-</mo><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>f</mi><mfenced><mi>t</mi></mfenced></mrow></mfenced></mrow></mfenced><mn>2</mn></msup></msqrt><mi>d</mi><mi>t</mi><mo>=</mo><mi>e</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="}" open="{"><mrow><mn>6</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>f</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mfenced></mrow></mfenced></mrow></mfenced><mn>2</mn></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **27**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><msqrt><mn>1</mn><mo>-</mo><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>f</mi><mfenced><mi>t</mi></mfenced></mrow></mfenced></mrow></mfenced><mn>2</mn></msup></msqrt><mi>d</mi><mi>t</mi><mo>=</mo><mi>e</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>e</mi></math>.</p><p>Differentiating <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> w.r.t. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><msqrt><mn>1</mn><mo>-</mo><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><mn>0</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><msqrt><mn>1</mn><mo>-</mo><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>y</mi></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>y</mi><msqrt><mn>1</mn><mo>-</mo><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>y</mi></mrow></mfenced><mn>2</mn></msup></msqrt></mrow></mfrac><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>y</mi></mrow></mfenced></mrow><msqrt><mn>1</mn><mo>-</mo><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>y</mi></mrow></mfenced><mn>2</mn></msup></msqrt></mfrac><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>y</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>e</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>0</mn><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>y</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>x</mi><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mi>e</mi></msub><mi>y</mi><mo>=</mo><mi>sin</mi><mfenced><mrow><mo>-</mo><mi>x</mi><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mi>e</mi></msub><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>sin</mi><mfenced><mrow><mo>-</mo><mi>x</mi><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mi>e</mi></msub><mi>f</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mi>sin</mi><mfenced><mrow><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mi>sin</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><msub><mi>log</mi><mi>e</mi></msub><mi>f</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced open="{" close="}"><mrow><mn>6</mn><msub><mi>log</mi><mi>e</mi></msub><mi>f</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mfenced></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>27</mn></math></p>

</details>

---

### Q20. JEE Main 2022 (28 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The minimum value of the twice differentiable function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mi>t</mi></mrow></msup><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>2</mn><msqrt><mi>e</mi></msqrt></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><msqrt><mi>e</mi></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mi>e</mi></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><msqrt><mi>e</mi></msqrt></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>2</mn><msqrt><mi>e</mi></msqrt></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mi>t</mi></mrow></msup><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>Differentiate on both side w.r.t <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mfenced><mrow><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mn>2</mn></mfenced><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now finding critical point we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Now differentiating equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> to check maxima and minima we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mn>2</mn></mfenced><mo>+</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mo>&#62;</mo><mn>0</mn></math>, so it will give point of  minima,</p><p>Now minimum value will be given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><msqrt><mi>e</mi></msqrt></mfrac></math></p></blockquote>

</details>

---

### Q21. JEE Main 2022 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> be a twice differentiable function on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfenced><mrow><mi>x</mi><mo>-</mo><mi>t</mi></mrow></mfenced><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><mfrac><mn>2</mn><mi>a</mi></mfrac><mi>x</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>5</mn></msup><msup><mi>a</mi><mn>2</mn></msup></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfenced><mrow><mi>x</mi><mo>-</mo><mi>t</mi></mrow></mfenced><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mi>a</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> both side we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mi>ii</mi></mfenced></math></p><p>On differentiating equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> w.r.t. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> we get:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>+</mo><mi>x</mi><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>x</mi><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mi>cos</mi><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mfrac><mn>2</mn><mi>a</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mi>cos</mi><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mfrac><mn>2</mn><mi>a</mi></mfrac></math></p><p>Replace <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> we get:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mo>=</mo><mfrac><mn>2</mn><mi>a</mi></mfrac><mo>&#160;&#160;</mo><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> in<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>5</mn></msup><mo>&#183;</mo><msup><mi>a</mi><mn>2</mn></msup></math></p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>5</mn></msup><mo>&#183;</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>=</mo><msup><mn>2</mn><mn>3</mn></msup><mo>=</mo><mn>8</mn></math></p></blockquote>

</details>

---

### Q22. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> be a differentiable function in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mi>cos</mi><mi>x</mi></mrow><mn>1</mn></msubsup><msup><mi>t</mi><mn>2</mn></msup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>-</mo><mn>9</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>+</mo><mfrac><mn>9</mn><msqrt><mn>2</mn></msqrt></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>-</mo><mfrac><mn>9</mn><msqrt><mn>2</mn></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>-</mo><mfrac><mn>9</mn><msqrt><mn>2</mn></msqrt></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mi>cos</mi><mi>x</mi></mrow><mn>1</mn></msubsup><msup><mi>t</mi><mn>2</mn></msup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></math></p><p>On differentiating, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mi>sin</mi><mi>x</mi><mo>&#183;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>3</mn><mi>tan</mi><mi>x</mi><mo>-</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></math></p><p>Again differentiating, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>sin</mi><mi>x</mi><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>3</mn><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>tan</mi><mi>x</mi></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sec</mi><mi>x</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>x</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mfrac><msqrt><mn>2</mn></msqrt><msqrt><mn>3</mn></msqrt></mfrac></math></p><p>Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><msqrt><mn>2</mn></msqrt><msqrt><mn>3</mn></msqrt></mfrac><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>=</mo><mn>3</mn><mo>&#215;</mo><mn>3</mn><mo>-</mo><mn>2</mn><mo>&#215;</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>=</mo><mn>6</mn><mo>-</mo><mfrac><mn>9</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p>

</details>

---

### Q23. JEE Main 2021 (01 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>&#8594;</mo><mi mathvariant="normal">R</mi></math> be a continuous function. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></munder><mfrac><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><msubsup><mo>&#8747;</mo><mn>2</mn><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow></msubsup><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mi mathvariant="normal">d</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>16</mn></mfrac></mrow></mfrac></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mo>(</mo><msqrt><mn>2</mn></msqrt><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mo>&#160;</mo><mi>lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mstyle displaystyle="true"><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mstyle><msubsup><mo>&#8747;</mo><mn>2</mn><mrow><mi>s</mi><mi>e</mi><msup><mi>c</mi><mn>2</mn></msup><mi>x</mi></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mstyle displaystyle="true"><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mn>16</mn></mfrac></mstyle></mrow></mfrac></math></p><p>Using L-Hospital&#39;s rule, we get</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mi>f</mi><mfenced><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>&#183;</mo><mn>2</mn><mo>&#183;</mo><mi>sec</mi><mi>x</mi><mo>&#183;</mo><mi>sec</mi><mi>x</mi><mo>&#183;</mo><mi>tan</mi><mi>x</mi><mo>-</mo><mn>0</mn></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#183;</mo><mn>2</mn><mo>(</mo><msqrt><mn>2</mn></msqrt><msup><mo>)</mo><mn>2</mn></msup><mo>&#183;</mo><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#183;</mo><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo></mrow><mrow><mn>2</mn><mo>&#183;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>f</mi><mfenced><mn>2</mn></mfenced></math></p>

</details>

---

### Q24. JEE Main 2021 (31 Aug Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>&#981;</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msubsup><mo>&#8747;</mo><mn>5</mn><mi>x</mi></msubsup><mfenced><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>&#981;</mi><mo>'</mo></msup><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mfenced><mi>d</mi><mi>t</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mo>-</mo><mn>2</mn><mo>,</mo></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>4</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>(</mo><mn>2</mn><mo>)</mo></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>Given that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>&#981;</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msubsup><mo>&#8747;</mo><mn>5</mn><mi>x</mi></msubsup><mfenced><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#62;</mo><mo>-</mo><mn>2</mn></math></p><p>Differentiating on both the sides and using Newton Leibnitz rule </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mn>1</mn><mi>&#981;</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mrow><mi>U</mi><mi>V</mi></mrow></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>U</mi><mfrac><mrow><mi>d</mi><mi>V</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi>V</mi><mfrac><mrow><mi>d</mi><mi>U</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>&#160;</mo><mo>;</mo><mo>&#160;</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><msubsup><mo>&#8747;</mo><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></msubsup><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mi>h</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>-</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mi>h</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mi>&#981;</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></math></p><p>It is a linear differential equation in the form of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mi>y</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>Q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfenced><mfrac><mn>1</mn><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#981;</mi><mfenced><mi>x</mi></mfenced><mo>&#183;</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#981;</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#183;</mo><mo>(</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>c</mi></math></p><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#981;</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mrow><mn>8</mn><mo>+</mo><mn>8</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q25. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> be a non-negative function in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>]</mo></math> and twice differentiable in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msqrt><mn>1</mn><mo>-</mo><msup><mfenced><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mfenced><mn>2</mn></msup></msqrt><mo>&#160;</mo><mi>dt</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>f</mi><mo>(</mo><mi mathvariant="normal">t</mi><mo>)</mo><mi>dt</mi><mo>,</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>f</mi><mo>(</mo><mi mathvariant="normal">t</mi><mo>)</mo><mi>dt</mi><mo>:</mo></math>

**Options:**

- **(A)** does not exist
- **(B)** equals <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** equals <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** equals <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) equals <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p> Newton - Leibnitz rule </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mrow><msubsup><mo>&#8747;</mo><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></msubsup><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>g</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mi>h</mi><mfenced><mrow><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mfenced><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mi>h</mi><mfenced><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mfenced></math></p><p>Given that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msqrt><mn>1</mn><mo>-</mo><msup><mfenced><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mfenced><mn>2</mn></msup></msqrt><mi>d</mi><mi>t</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>f</mi><mo>(</mo><mi>t</mi><mo>)</mo><mi>d</mi><mi>t</mi></math></p><p>Differentiate <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi><mo>.</mo><mi>r</mi><mo>.</mo><mi>t</mi><mo>.</mo><mo>&#160;</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>-</mo><msup><mfenced><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#160;</mo></math></p><p>Squaring on both sides
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><msup><mfenced><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mo>(</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><msup><mo>)</mo><mn>2</mn></msup><mo>&#160;&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>-</mo><mo>(</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><msup><mo>)</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>y</mi><mo>&#160;</mo><mo>&#8658;</mo><mi>f</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#160;&#160;</mo><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>&#177;</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><msqrt><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt></mfrac><mo>=</mo><mo>&#177;</mo><mi>d</mi><mi>x</mi></math></p><p>By using Variable Separable form</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>=</mo><mo>&#177;</mo><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mi>c</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>=</mo><mi>x</mi><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>sin</mi><mi>x</mi></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>sin</mi><mi>t</mi><mi>d</mi><mi>t</mi></math></p><p>It is in the form of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>0</mn><mn>0</mn></mfrac></math> so apply L hospital&#39;s rule</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mstyle displaystyle="true"><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mstyle><mfenced close="]" open="["><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>sin</mi><mi>t</mi><mi>d</mi><mi>t</mi></mrow></mfenced></mrow><mstyle displaystyle="true"><mfrac><mrow><mo>d</mo><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced></mrow><mrow><mo>d</mo><mi>x</mi></mrow></mfrac></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q26. JEE Main 2021 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>:</mo><mfenced close="]" open="["><mrow><mn>3</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be a twice differentiable function on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><msubsup><mo>&#8747;</mo><mn>3</mn><mi>x</mi></msubsup><mfenced><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>t</mi><mo>+</mo><mn>4</mn><msup><mi>F</mi><mo>&#39;</mo></msup><mfenced><mi>t</mi></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>F</mi><mo>&#39;</mo></msup><mfenced><mn>4</mn></mfenced><mo>=</mo><mfrac><mrow><mi>&#945;</mi><msup><mi>e</mi><mi>&#946;</mi></msup><mo>-</mo><mn>224</mn></mrow><msup><mfenced><mrow><msup><mi>e</mi><mi>&#946;</mi></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<p>Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><msubsup><mo>&#8747;</mo><mn>3</mn><mi>x</mi></msubsup><mfenced><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>t</mi><mo>+</mo><mn>4</mn><msup><mi>F</mi><mo>&#39;</mo></msup><mfenced><mi>t</mi></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi><mo>.</mo></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><msubsup><mo>&#8747;</mo><mn>3</mn><mn>3</mn></msubsup><mfenced><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>t</mi><mo>+</mo><mn>4</mn><msup><mi>F</mi><mo>'</mo></msup><mfenced><mi>t</mi></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi><mo>.</mo></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>F</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p>Again, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mi>F</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>3</mn><mi>x</mi></msubsup><mfenced><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>t</mi><mo>+</mo><mn>4</mn><msup><mrow><mo>&#160;</mo><mi>F</mi></mrow><mo>&#39;</mo></msup><mfenced><mi>t</mi></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p>Differentiate both sides</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mi>x</mi></msup><mi>F</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup><msup><mi>F</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><msup><mrow><mo>&#160;</mo><mi>F</mi></mrow><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math> (Newton Leibnitz Theorem for Definite Integral)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup><mi>y</mi><mo>=</mo><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced></math> (Use <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>F</mi><mfenced><mi>x</mi></mfenced></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>4</mn></mrow></mfenced></mfrac><mi>y</mi><mo>=</mo><mfrac><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>4</mn></mrow></mfenced></mfrac></math></p><p>Here, integrating factor is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><msup><mi>e</mi><mi>x</mi></msup><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>4</mn></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>ln</mi><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>4</mn></mrow></mfenced></mrow></msup><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>4</mn></math></p><p>So, the solution is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#183;</mo><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mo>-</mo><mn>36</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>36</mn></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>4</mn></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>F</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>36</mn></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></mrow><msup><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p>Now put value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn></math> we will get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>F</mi><mo>&#39;</mo></msup><mfenced><mn>4</mn></mfenced><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>3</mn><msup><mfenced><mn>4</mn></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced><mn>4</mn></mfenced></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mn>4</mn></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><msup><mfenced><mn>4</mn></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced><mn>4</mn></mfenced><mn>2</mn></msup><mo>-</mo><mn>36</mn></mrow></mfenced><msup><mi>e</mi><mn>4</mn></msup></mrow><msup><mfenced><mrow><msup><mi>e</mi><mn>4</mn></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mn>12</mn><msup><mi>e</mi><mn>4</mn></msup><mo>-</mo><mn>224</mn></mrow><msup><mfenced><mrow><msup><mi>e</mi><mn>4</mn></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>12</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>4</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>16</mn></math></p>

</details>

---

### Q27. JEE Main 2021 (17 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>sin</mi><mi>x</mi><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>:</mo><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> is a differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><msup><mi>F</mi><mo>'</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></math> lies in the interval

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mfrac><mn>327</mn><mn>360</mn></mfrac><mo>,</mo><mfrac><mn>329</mn><mn>360</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mfrac><mn>330</mn><mn>360</mn></mfrac><mo>,</mo><mfrac><mn>331</mn><mn>360</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mfrac><mn>331</mn><mn>360</mn></mfrac><mo>,</mo><mfrac><mn>334</mn><mn>360</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mfrac><mn>335</mn><mn>360</mn></mfrac><mo>,</mo><mfrac><mn>336</mn><mn>360</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mfrac><mn>330</mn><mn>360</mn></mfrac><mo>,</mo><mfrac><mn>331</mn><mn>360</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>sin</mi><mi>x</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math></p><p>Using Newton Leibnitz rule i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><msubsup><mo>&#8747;</mo><mrow><mi>u</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>v</mi><mfenced><mi>x</mi></mfenced></mrow></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mi>f</mi><mfenced><mrow><mi>v</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><msup><mi>v</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mrow><mi>u</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><msup><mi>u</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>F</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><msup><mi>F</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mfenced><msup><mi mathvariant="normal">e</mi><mi>x</mi></msup><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mo>(</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>)</mo><mo>&#183;</mo><msup><mi mathvariant="normal">e</mi><mi>x</mi></msup><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#183;</mo><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>sin</mi><mi>x</mi><mo>&#183;</mo><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mrow><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn><mo>(</mo><mn>1</mn><mo>-</mo><mi>cos</mi><mn>1</mn><mo>)</mo></math></p><p>Using the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>4</mn></msup><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>6</mn></msup><mrow><mn>6</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn><mfenced close="}" open="{"><mrow><mn>1</mn><mo>-</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>6</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>2</mn><mrow><mn>6</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mfrac><mn>2</mn><mrow><mn>9</mn><mo>!</mo></mrow></mfrac><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>&#60;</mo><mi>I</mi><mo>&#60;</mo><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>2</mn><mrow><mn>6</mn><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>11</mn><mn>12</mn></mfrac><mo>&#60;</mo><mi>I</mi><mo>&#60;</mo><mfrac><mn>331</mn><mn>360</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mn>11</mn><mn>12</mn></mfrac><mo>,</mo><mfrac><mn>331</mn><mn>360</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mn>330</mn><mn>360</mn></mfrac><mo>,</mo><mfrac><mn>331</mn><mn>360</mn></mfrac></mrow></mfenced><mo>.</mo></math></p>

</details>

---

### Q28. JEE Main 2021 (16 Mar Shift 1)

*Type:* `numerical` | *Level:* `2`

If the normal to the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfenced><mrow><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>15</mn><mi>t</mi><mo>+</mo><mn>10</mn></mrow></mfenced><mi>d</mi><mi>t</mi></math> at a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math> is parallel to the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mo>-</mo><mn>5</mn><mo>,</mo><mi>a</mi><mo>&#62;</mo><mn>1</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mo>+</mo><mn>6</mn><mi>b</mi></mrow></mfenced></math> is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **406**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfenced><mrow><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>15</mn><mi>t</mi><mo>+</mo><mn>10</mn></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced close="]" open=""><mrow><msup><mi>y</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced><mrow><mi>x</mi><mo>=</mo><mi>a</mi></mrow></msub><mo>=</mo><msub><mfenced close="]" open="["><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>15</mn><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfenced><mi>a</mi></msub><mo>=</mo><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>15</mn><mi>a</mi><mo>+</mo><mn>10</mn></math></p><p>Slope of normal <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>15</mn><mi>a</mi><mo>+</mo><mn>10</mn><mo>=</mo><mn>3</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>7</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>  (rejected)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mi>y</mi><mfenced><mn>7</mn></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>7</mn></msubsup><mfenced><mrow><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>15</mn><mi>t</mi><mo>+</mo><mn>10</mn></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced open="[" close="]"><mrow><mfrac><mrow><mn>2</mn><msup><mi>t</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mn>15</mn><msup><mi>t</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mn>10</mn><mi>t</mi></mrow></mfenced><mn>0</mn><mn>7</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi>b</mi><mo>=</mo><mn>4</mn><mo>&#215;</mo><msup><mn>7</mn><mn>3</mn></msup><mo>-</mo><mn>45</mn><mo>&#215;</mo><mn>49</mn><mo>+</mo><mn>60</mn><mo>&#215;</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>a</mi><mo>+</mo><mn>6</mn><mi>b</mi></mrow></mfenced><mo>=</mo><mn>406</mn></math></p>

</details>

---

### Q29. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>e</mi><mi mathvariant="normal">t</mi></msup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></math> be a differentiable function for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> equals :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><msup><mi>e</mi><mi>x</mi></msup></msup><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>e</mi><msup><mi>e</mi><mi>x</mi></msup></msup><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>e</mi><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced></msup><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>e</mi><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced></msup><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>e</mi><mi>t</mi></msup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup><mo>&#8658;</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math></p><p>Differentiating with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup></math></p><p>Integrate both the sides we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfrac><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><menclose notation="right"><mi>ln</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced></menclose><mn>0</mn><mi>x</mi></msubsup><msubsup><menclose notation="right"><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup></menclose><mn>0</mn><mi>x</mi></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>ln</mi><mfenced><mrow><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></math>   {as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math>}</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>e</mi><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced></msup><mo>-</mo><mn>1</mn></math></p>

</details>

---

### Q30. JEE Main 2021 (24 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><msup><mi>x</mi><mn>2</mn></msup></msubsup><mfenced><mrow><mi>sin</mi><msqrt><mi>t</mi></msqrt></mrow></mfenced><mi>d</mi><mi>t</mi></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>15</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><msup><mi>x</mi><mn>2</mn></msup></msubsup><mi>sin</mi><msqrt><mi>t</mi></msqrt><mi>d</mi><mi>t</mi></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mn>2</mn><mi>x</mi></mrow><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mi>x</mi></mfrac></mfenced><mo>&#215;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q31. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>1</mn></mrow></munder><mfenced><mfrac><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></msubsup><mi>t</mi><mi>cos</mi><msup><mi>t</mi><mn>2</mn></msup><mo>d</mo><mi>t</mi></mrow><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>sin</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow></mfrac></mfenced></math>

**Options:**

- **(A)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>.
- **(B)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>.
- **(C)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>.
- **(D)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>.**

**Detailed Solution:**

<p>Applying L&#39;Hospital&#39;s Rule, for numerator we have to apply Newton Leibnitz integral rule</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>1</mn></mrow></munder><mfenced><mfrac><mrow><mn>2</mn><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>&#215;</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mi>cos</mi><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>4</mn></msup><mo>-</mo><mn>0</mn></mrow><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>cos</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>sin</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow></mfrac></mfenced><mo>&#160;</mo><mo>&#160;</mo><mfenced><mfrac><mn>0</mn><mn>0</mn></mfrac></mfenced></math></p><p>Divide <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>1</mn></mrow></munder><mfrac><mrow><mn>2</mn><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mi>cos</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>4</mn></msup></mrow><mrow><mi>cos</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mi>sin</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow></mfrac></mstyle></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>0</mn><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q32. JEE Main 2020 (08 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>t</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mn>10</mn><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></mrow><mi>x</mi></mfrac></math>, is equal to

**Options:**

- **(A)** <math><mn>0</mn></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>10</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>10</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>0</mn></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>t</mi><mi>sin</mi><mfenced separators="|"><mrow><mn>10</mn><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></mrow><mi>x</mi></mfrac></math></p><p>The given limiting form is the indeterminate form <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>0</mn><mn>0</mn></mfrac></math>.</p><p>Thus, using Newton-Leibnitz Rule (differentiation under integral sign) and L&#39; Hospital Rule, we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mstyle displaystyle="true"><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mstyle><mfenced open="{" close="}"><mrow><msubsup><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>t</mi><mi>sin</mi><mfenced separators="|"><mrow><mn>10</mn><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></mrow></mfenced></mrow><mrow><mstyle displaystyle="true"><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mstyle><mfenced><mi>x</mi></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>x</mi><mi>sin</mi><mfenced separators="|"><mrow><mn>10</mn><mi>x</mi></mrow></mfenced></mrow><mn>1</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn></math>.</p>

</details>

---

### Q33. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a continuous and differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>2</mn></mfenced><mo>=</mo><mn>6</mn></math> and <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>48</mn></mrow></mfrac></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>6</mn><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow></msubsup><mn>4</mn><msup><mi>t</mi><mn>3</mn></msup><mi>d</mi><mi>t</mi><mo>=</mo><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>,</mo></math> then <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>2</mn></mrow></munder><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math><mn>24</mn></math>
- **(B)** <math><mn>18</mn></math>
- **(C)** <math><mn>12</mn></math>
- **(D)** <math><mn>36</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>18</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>2</mn></mrow></munder><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>2</mn></mrow></munder><mfrac><mrow><munderover><mo stretchy="true">&#8747;</mo><mn>6</mn><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></munderover><mn>4</mn><msup><mi>t</mi><mn>3</mn></msup><mi>d</mi><mi>t</mi></mrow><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mfrac><mn>0</mn><mn>0</mn></mfrac><mo>&#160;</mo><mi>form</mi></mrow></mfenced></math>.</p><p>By using L&#39;Hospital rule
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>2</mn></mrow></munder><mfrac><mrow><mn>4</mn><mo>.</mo><msup><mi>f</mi><mn>3</mn></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#8901;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced></mrow><mn>1</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><msup><mi>f</mi><mn>3</mn></msup><mfenced separators="|"><mn>2</mn></mfenced><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mn>2</mn></mfenced><mo>=</mo><mn>4</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>48</mn></mfrac><mo>=</mo><mn>18</mn></math>.</p>

</details>

---

### Q34. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> is a differentiable function and <math><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>=</mo><mn>6</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>2</mn></mrow></munder><msubsup><mo>&#8747;</mo><mn>6</mn><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></msubsup><mfrac><mrow><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi></mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mfrac></math> is:

**Options:**

- **(A)** <math><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mn>2</mn></mfenced></math>
- **(C)** <math><mn>24</mn><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></math>
- **(D)** <math><mn>12</mn><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>12</mn><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>The given limit can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>2</mn></mrow></munder><mfrac><mrow><msubsup><mo>&#8747;</mo><mn>6</mn><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></msubsup><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi></mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mfrac><mi>&#160;</mi><mi>&#160;</mi></math></p><p>Applying L&#39; Hospital&rsquo;s rule i.e. if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mfrac><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>h</mi><mfenced><mi>x</mi></mfenced></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#8594;</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>&#8594;</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mfrac><mrow><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></mrow><mrow><msup><mi>h</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>2</mn></mrow></munder><mfrac><mrow><mstyle displaystyle="true"><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mstyle><msubsup><mo>&#8747;</mo><mn>6</mn><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></msubsup><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi></mrow><mn>1</mn></mfrac></math></p><p>Now, applying Newton&#39;s Leibnitz rule i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>g</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>g</mi><mfenced><mi>b</mi></mfenced><mo>&#183;</mo><msup><mi>b</mi><mo>'</mo></msup><mo>-</mo><mi>g</mi><mfenced><mi>a</mi></mfenced><mo>&#183;</mo><msup><mi>a</mi><mo>'</mo></msup><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>l</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>2</mn></mrow></munder><mfenced><mrow><mn>2</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#183;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>l</mi><mo>=</mo><mn>2</mn><mi>f</mi><mfenced separators="|"><mn>2</mn></mfenced><mo>&#8901;</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mn>2</mn></mfenced></math></p><p>Put the given value, to get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>l</mi><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mn>2</mn></mfenced><mo>=</mo><mn>12</mn><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mn>2</mn></mfenced><mo>.</mo></math></p>

</details>

---

### Q35. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mn>0</mn><mi>x</mi></munderover><mi>f</mi><mfenced separators="|"><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><munderover><mo>&#8747;</mo><mi>x</mi><mn>1</mn></munderover><msup><mi>t</mi><mn>2</mn></msup><mi>f</mi><mfenced separators="|"><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>18</mn><mn>25</mn></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>24</mn></mrow><mrow><mn>25</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>6</mn></mrow><mrow><mn>25</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>24</mn></mrow><mrow><mn>25</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Differentiating both the sides w.r.t. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mi>f</mi><mfenced><mi>x</mi></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>&#215;</mo><mn>2</mn><mo>-</mo><mn>2</mn><mi>x</mi><mo>&#215;</mo><mn>2</mn><mi>x</mi></mrow><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>24</mn><mn>25</mn></mfrac></math></p>

</details>

---

### Q36. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>.</mo></math> If <math><mi>I</mi></math> is minimum then the ordered pair <math><mo>(</mo><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>b</mi><mo>)</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mo>,</mo><mi> </mi><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mo>-</mo><mi> </mi><msqrt><mn>2</mn></msqrt><mo>,</mo><mn>0</mn></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mi> </mi><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfenced separators="|"><mrow><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mi> </mi><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></math></p><p>To draw it&#39;s graph, finding the points where it intersects the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>&#177;</mo><msqrt><mn>2</mn></msqrt></math>.</p><p>The graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is,

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/zltbojddelryoliskhcfndndprjmfajhxealpruizlgcwrjies.png" />

From the figure, we get minimum area when <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><msqrt><mn>2</mn></msqrt></math>.</p><p>Hence, the ordered pair can be written as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mi>&#160;</mi><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>.</mo></math></p>

</details>

---

### Q37. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>t</mi><mfenced separators="|"><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'''</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>-</mo><msup><mi>f</mi><mo>''</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mn>2</mn><mi>x</mi><mi>sin</mi><mi>x</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'''</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>''</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>-</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>cos</mi><mi>x</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'''</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>''</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>sin</mi><mi>x</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'''</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mn>2</mn><mi>x</mi><mi>sin</mi><mi>x</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'''</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mn>2</mn><mi>x</mi><mi>sin</mi><mi>x</mi></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>t</mi><mfenced separators="|"><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>sin</mi><mi>x</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>t</mi><mi>d</mi><mi>t</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>t</mi><mi>sin</mi><mi>t</mi><mi>d</mi><mi>t</mi></math></p><p>On differentiating, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced separators="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>t</mi><mi>d</mi><mi>t</mi><mo>-</mo><mi>x</mi><mi>sin</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>cos</mi><mi>x</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>t</mi><mi>d</mi><mi>t</mi></math></p><p>Differentiating the above equation again, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>''</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced separators="|"><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mi>x</mi><mo>-</mo><mfenced separators="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>t</mi><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'''</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mfenced separators="|"><mrow><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mfenced separators="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mi>x</mi><mo>-</mo><mfenced separators="|"><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>t</mi><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'''</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mn>2</mn><mi>x</mi><mi>sin</mi><mi>x</mi></math>.</p>

</details>

---

### Q38. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

For <math><mi>x</mi><mo>∈</mo><mi>R</mi><mo>,</mo><mo> </mo><mi>x</mi><mo>≠</mo><mn>0</mn><mo>,</mo></math> if <math><mi>y</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is a differentiable function such that <math><mi>x</mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>y</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced></mrow></mrow><mi>d</mi><mi>t</mi><mo>=</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi> </mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>t</mi><mi>y</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced></mrow></mrow><mi>d</mi><mi>t</mi><mo>,</mo></math> then <math><mi>y</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> equals (where <math><mi>C</mi></math> is a constant)

**Options:**

- **(A)** <math><mi>C</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mi>&#160;</mi><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup></math>
- **(B)** <math><mfrac><mrow><mi>C</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mi>&#160;</mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup></math>
- **(C)** <math><mfrac><mrow><mi>C</mi></mrow><mrow><mi>x</mi></mrow></mfrac><mi> </mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup></math>
- **(D)** <math><mfrac><mrow><mi>C</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mi> </mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mi>C</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mi> </mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup></math>**

**Detailed Solution:**

<math><mi>x</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>y</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></mrow></mrow><mo>=</mo><mi>x</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>t</mi><mi>y</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced></mrow></mrow><mi>d</mi><mi>t</mi><mo>+</mo><mi>&#160;</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>t</mi><mi>y</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced></mrow></mrow><mi>d</mi><mi>t</mi></math>

Differentiate w.r.t. <math><mi>x</mi></math>

<math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>y</mi><mo>(</mo><mi>t</mi><mo>)</mo><mi>d</mi><mi>t</mi><mo>+</mo><mi>x</mi><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mrow><mo>=</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>t</mi><mi>y</mi><mo>(</mo><mi>t</mi><mo>)</mo><mi>d</mi><mi>t</mi><mo>+</mo><mi>x</mi><mo>[</mo><mi>x</mi><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>]</mo><mo>+</mo><mi>x</mi><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mrow></math>

<math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>y</mi><mo>(</mo><mi>t</mi><mo>)</mo><mi>d</mi><mi>t</mi></mrow></mrow><mo>=</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>t</mi><mi>y</mi><mo>(</mo><mi>t</mi><mo>)</mo><mi>d</mi><mi>t</mi><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo><mi>&#160;</mi></mrow></mrow></math>

Differentiate again w.r.t. <math><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>x</mi><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mn>2</mn><mi>x</mi><mi>&#160;</mi><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>y</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mi>&#160;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mi>y</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>y</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>y</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced></mrow><mrow><mi>y</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>x</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></math>

<math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>x</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

Integrating on both sides

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mi>y</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>-</mo><mn>3</mn><mi>ln</mi><mi>x</mi><mo>+</mo><mi>C</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mo>(</mo><mi>y</mi><msup><mi>x</mi><mn>3</mn></msup><mo>)</mo><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mi>C</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><msup><mi>x</mi><mn>3</mn></msup><mo>=</mo><mi>&#160;</mi><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mi>C</mi></mrow></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mi>C</mi></mrow></msup><msup><mi>x</mi><mn>3</mn></msup></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mi>C</mi><msup><mi>x</mi><mn>3</mn></msup></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup></math>

</details>

---

### Q39. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `3`

If $\frac{d}{d x} G(x)=\frac{e^{\tan x}}{x}, x \in(0, \pi / 2)$, then $\int_{1 / 4}^{1 / 2} \frac{2}{x} \cdot e^{\tan \left(\pi x^2\right)} d x$ is equal to

**Options:**

- **(A)** $G(\pi / 4)-G(\pi / 16)$
- **(B)** $2[G(\pi / 4)-G(\pi / 16)]$
- **(C)** $\pi[G(1 / 2)-G(1 / 4)]$
- **(D)** $G(1 / \sqrt{2})-G(1 / 2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $G(\pi / 4)-G(\pi / 16)$**

**Detailed Solution:**

Let $\frac{d}{d x} G(x)=\frac{e^{\tan x}}{x}, x \in\left(0, \frac{\pi}{2}\right)$
Now,
$$
\begin{aligned}
I & =\int_{1 / 4}^{1 / 2} \frac{2}{x} e^{\tan \pi x^2} \cdot d x \\
& =\int_{1 / 4}^{1 / 2} \frac{2 \pi x}{\pi x^2} e^{\tan \pi x^2} \cdot d x
\end{aligned}
$$
Let $\pi x^2=t \Rightarrow 2 \pi x d x=d t$
When $x=\frac{1}{2}, t=\frac{\pi}{4}$ and $x=\frac{1}{4}, t=\frac{\pi}{16}$
$$
\begin{aligned}
\therefore I & =\int_{\pi / 16}^{\pi / 4} \frac{e^{\tan t}}{t} d t=g(t) \mid \begin{array}{l}
\frac{\pi}{4} \\
\frac{\pi}{16}
\end{array} \\
& =G\left(\frac{\pi}{4}\right)-G\left(\frac{\pi}{16}\right)
\end{aligned}
$$

</details>

---

### Q40. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `1`

If $\int_e^x t f(t) d t=\sin x-x \cos x-\frac{x^2}{2}$, for all $x \in R-\{0\}$, then the value of $f\left(\frac{\pi}{6}\right)$ is

**Options:**

- **(A)** 1/2
- **(B)** 1
- **(C)** 0
- **(D)** $-1 / 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-1 / 2$**

**Detailed Solution:**

Let $\int_e^x t f(t) d t=\sin x-x \cos x-\frac{x^2}{2}$
By using Leibnitz rule, we get
$$
\begin{aligned}
& \frac{d}{d x}\left[\int_e^x t f(t) d t\right]=\frac{d}{d x}\left[\sin x-x \cos x-\frac{x^2}{2}\right] \\
& \Rightarrow x f(x)-e f(e) \cdot 0=x \sin x-x
\end{aligned}
$$
Now, put $x=\frac{\pi}{6}$, we get
$$
\begin{aligned}
& \frac{\pi}{6} \cdot f\left(\frac{\pi}{6}\right)=\frac{\pi}{6} \cdot \sin \frac{\pi}{6}-\frac{\pi}{6} \\
& \Rightarrow f\left(\frac{\pi}{6}\right)=\sin \frac{\pi}{6}-1=\frac{1}{2}-1=-\frac{1}{2}
\end{aligned}
$$

</details>

---

### Q41. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `3`

If $g(x)=\int_0^x \cos 4 t ~d t$, then $g(x+\pi)$ equals

**Options:**

- **(A)** $\frac{g(x)}{g(\pi)}$
- **(B)** $g(x)+g(\pi)$
- **(C)** $g(x)-g(\pi)$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $g(x)+g(\pi)$**

**Detailed Solution:**

$g(x)=\int_0^x \cos 4 t ~d t$
$\Rightarrow g^{\prime}(x)=\cos 4 x \quad \Rightarrow g(x)=\frac{\sin 4 x}{4}+k \quad \Rightarrow g(x)=\frac{\sin 4 x}{4}[\because g(0)=0]$
$g(x+\pi)=g(x)+g(\pi)=g(x)-g(\pi)(\because g(\pi)=0)$

</details>

---

### Q42. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `3`

For $x \in\left(0, \frac{5 \pi}{2}\right)$, define $f(x)=\int_0^x \sqrt{t} \sin t d t$. Then $f$ has

**Options:**

- **(A)** local minimum at $\pi$ and $2 \pi$
- **(B)** local minimum at $\pi$ and local maximum at $2 \pi$
- **(C)** local maximum at $\pi$ and local minimum at $2 \pi$
- **(D)** local maximum at $\pi$ and $2 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) local maximum at $\pi$ and local minimum at $2 \pi$**

**Detailed Solution:**

$f^{\prime}(x)=\sqrt{x} \sin x$
Given $x \in\left(0, \frac{5 \pi}{2}\right)$
$f^{\prime}(x)$ changes sign from +ve to -ve at $\pi$
$f^{\prime}(x)$ changes sign from -ve to +ve at $2 \pi$
$f$ has local max at $\pi$, local min at $2 \pi$

</details>

---

### Q43. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

Let $f: R \rightarrow R$ be a differentiable function having $f(2)=6, f^{\prime}(2)=\left(\frac{1}{48}\right)$. Then $\lim _{x \rightarrow 2} \int_6^{f(x)} \frac{4 t^3}{x-2} d t$ equals

**Options:**

- **(A)** 24
- **(B)** 36
- **(C)** 12
- **(D)** 18

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 18**

**Detailed Solution:**

$$
\lim _{x \rightarrow 2} \int_0^{f(x)} \frac{4 t^3}{x-2} d t
$$
Applying $L$ Hospital rule
$$
\begin{aligned}
& \lim _{x \rightarrow 2}\left[4 f(x)^2 f^{\prime}(x)\right]=4 f(2)^3 f^{\prime}(2) \\
& =4 \times 6^3 \times \frac{1}{48}=18 .
\end{aligned}
$$

</details>

---

### Q44. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

The value of $\lim _{x \rightarrow 0} \frac{\int_0^{x^2} \sec ^2 t d t}{x \sin x}$ is

**Options:**

- **(A)** 0
- **(B)** 3
- **(C)** 2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

$\operatorname{Lim}_{x \rightarrow 0} \frac{\frac{d}{d x} \int_0^{x^2} \sec ^2 t d t}{\frac{d}{d x}(x \sin x)}=\operatorname{Lim}_{x \rightarrow 0} \frac{\sec ^2 x^2 \cdot 2 x}{\sin x+x \cos x}$
(by L'Hospital rule)
$\operatorname{Lim}_{x \rightarrow 0} \frac{2 \sec ^2 x^2}{\left(\frac{\sin x}{x}+\cos x\right)}=\frac{2 \times 1}{1+1}=1$

</details>

---

### Q45. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(\mathrm{y})=\mathrm{e}^{\mathrm{y}}, \mathrm{g}(\mathrm{y})=\mathrm{y} ; \mathrm{y}>0$ and $F(t)=\int_0^{\mathrm{t}} \mathrm{f}(\mathrm{t}-\mathrm{y}) \mathrm{g}(\mathrm{y})$, then

**Options:**

- **(A)** $\mathrm{F}(\mathrm{t})=\mathrm{te}^{-t}$
- **(B)** $\mathrm{F}(\mathrm{t})=1-\mathrm{te}^{-t}(1+\mathrm{t})$
- **(C)** $\mathrm{F}(\mathrm{t})=\mathrm{e}^{\mathrm{t}}-(1+\mathrm{t})$
- **(D)** $\mathrm{F}(\mathrm{t})=\mathrm{te}^{\mathrm{t}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{F}(\mathrm{t})=\mathrm{e}^{\mathrm{t}}-(1+\mathrm{t})$**

**Detailed Solution:**

$F(t)=\int_0^t f(t-y) g(y) d y$
$=\int_0^t e^{t-y} y d y=e^t \int_0^t e^{-y} y d y$
$=e^t\left[-y e^{-y}-e^{-y}\right]_0^t=-e^t\left[y e^{-y}+e^{-y}\right]_0^t$
$=-e^t\left[t e^{-t}+e^{-t}-0-1\right]=e^t\left[\frac{t+1-e^t}{e^t}\right]=e^t-(1+t)$

</details>

---

### Q46. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `3`

$I_n=\int_0^{\pi / 4} \tan ^n x d x$ then $\operatorname{Lim}_{n \rightarrow \infty} n\left[I_n+I_{n-2}\right]$ equals

**Options:**

- **(A)** 1/2
- **(B)** 1
- **(C)** $\infty$
- **(D)** zero

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

$\int_0^{\pi / 4} \tan ^n x\left(1+\tan ^2 x\right) d x=\int_0^{\pi / 4} \tan ^n x \sec ^2 x d x=\int_0^1 t^n d t$ where $t=\tan x$
$I_n+I_{n+2}=\frac{1}{n+1} ; \Rightarrow \operatorname{Lim}_{x \rightarrow \infty} n\left[l_n+I_{n+2}\right]=\operatorname{Lim}_{x \rightarrow \infty} n \cdot \frac{1}{n+1}=\frac{n}{n+1}=\frac{n}{n\left(1+\frac{1}{n}\right)}=1$

</details>

---

